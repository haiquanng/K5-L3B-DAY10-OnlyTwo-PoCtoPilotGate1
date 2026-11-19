"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        ctx.log("no_effective_policy", as_of=ctx.as_of)
        return Verdict.escalate("không tìm thấy chính sách có hiệu lực; chuyển người duyệt")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()

    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    order = ctx.tools.lookup_order(action.get("order_id"))
    if policy is None or order is None:
        ctx.log("write_missing_source_data", tool=tool, order_id=action.get("order_id"))
        return Verdict.escalate("thiếu đơn hàng hoặc chính sách hiệu lực để xác minh lệnh ghi")

    if tool == "issue_refund":
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        expected = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if action.get("amount_vnd") != expected or action.get("payer", "LOGIX") != "LOGIX":
            ctx.log("refund_mismatch", order_id=order["order_id"], delay_days=delay,
                    expected_amount_vnd=expected, requested_amount_vnd=action.get("amount_vnd"),
                    payer=action.get("payer", "LOGIX"))
            return Verdict.escalate("số tiền hoặc bên trả không khớp tracking và chính sách; chuyển người duyệt")
        return Verdict.allow()

    parcel = next((p for p in order["parcels"] if p["parcel_id"] == action.get("parcel_id")), None)
    if parcel is None:
        ctx.log("fault_unknown_parcel", order_id=order["order_id"], parcel_id=action.get("parcel_id"))
        return Verdict.escalate("không xác minh được kiện hàng của lỗi hãng; chuyển người duyệt")

    delay = H.db_delay_days(parcel, ctx.as_of)
    # Vòng 2 (S4): tới bước này khoản hoàn ĐÃ được ghi đúng theo tracking. Nếu tracking cho thấy hãng không có lỗi
    # (vd. MERCHANT_HANDOVER, nhánh fail_open khi LLM lỗi) thì chỉ BỎ lệnh ghi lỗi hãng (deny), không chuyển cả ticket
    # sang người: chuyển người lúc này làm sổ cái (đã hoàn) và trạng thái (chờ duyệt) mâu thuẫn, và làm ngập hàng chờ.
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("fault_denied_not_carrier", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                tracking_delay_days=delay, tracking_cause=parcel.get("delay_cause"))
        return Verdict.deny("tracking không cho thấy lỗi thuộc hãng; không ghi lỗi hãng")
    if action.get("delay_days") != delay or action.get("carrier_id") != parcel.get("carrier_id"):
        ctx.log("fault_mismatch", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                tracking_delay_days=delay, requested_delay_days=action.get("delay_days"),
                tracking_cause=parcel.get("delay_cause"))
        return Verdict.escalate("lỗi hãng không khớp số ngày và nguyên nhân trong tracking; chuyển người duyệt")
    return Verdict.allow()
