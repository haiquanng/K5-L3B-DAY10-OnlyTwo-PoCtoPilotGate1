"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def fail_open_rate(trials):
    """Kỹ thuật (thẻ S4): tỉ lệ ticket mà trợ lý rơi vào nhánh fail_open vì LLM lỗi (429) ở bước kiểm chính sách.
    Không cần nhãn: đọc sự kiện llm_fallback trong trace. Ngày thường ~0; giờ nhà cung cấp LLM nghẽn thì vọt lên."""
    hit = sum(any(e.get("type") == "llm_fallback" and e.get("mode") == "fail_open" for e in t["events"]) for t in trials)
    return round(hit / max(1, len(trials)), 4)


def peak_hour_review_load(trials):
    """Vận hành (thẻ S4): số ca vào hàng chờ người duyệt trong 60 phút đông nhất của một ngày (lấy ngày/seed tệ nhất).
    So với sức duyệt: 1 người = 6 ca/giờ (ops_facts). Vượt sức duyệt là dấu hiệu sắp có ca bị ùn."""
    worst = 0
    days = {}
    for t in trials:
        if t.get("review_kind"):
            days.setdefault((t.get("seed"), t.get("day")), []).append(t.get("arrive_min") or 0)
    for mins in days.values():
        mins.sort()
        j = 0
        for i, m in enumerate(mins):
            while mins[j] < m - 59:
                j += 1
            worst = max(worst, i - j + 1)
    return worst


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "fail_open_rate": fail_open_rate,
    "peak_hour_review_load": peak_hour_review_load,
}
STARTER_MONITORS = ("escalation_rate",)
