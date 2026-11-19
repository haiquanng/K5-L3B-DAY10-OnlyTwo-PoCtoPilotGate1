# Nguyễn Văn Hải Quân · 2A202603994 · Sản phẩm và kinh doanh (trưởng nhóm)

**Chủ PRD v1.1** dùng chung cho bàn ([`shared/PRD_v1.1.md`](shared/PRD_v1.1.md)). Cầm bút tiêu chí, chi phí, phạm vi pilot và hai quyết định Gate 1.

## File và mục chỉ mình Quân sửa

- `config/acceptance_criteria.json` (+ `.lock` do lệnh 1 tạo). Ký xong thì không mở lại.
- `config/operating_gates.json` → **chỉ khối `business`**: `daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`.
- `TEAM.md` phần đầu (thông tin nhóm, bảng thành viên) và mục `## NguyenVanHaiQuan-2A202603994`.
- Phiếu A: dòng `Bàn:`, A1 câu 1.1, A3 câu 1.5, A4 câu 1.6, A5.
- Phiếu B: dòng `Bàn:`, B3, B6 (người ghi), B7.4, B8.
- Phiếu C: dòng `Bàn:`, C1 (người ghi), C5 câu 3.2, C6 (người ghi), C12.

**Không đụng:** `lab10/*.py`, khối `operations`/`legal`, `submission/`, mục phiếu của Lên và Nguyên.
**Không chạy:** `eval`, `gate`, `grade`, `checkpoint`, `check_submission` (chỉ máy Lên chạy). Được chạy `trace` và `unittest`.

## Checklist theo mốc

### Phút 0–15 · Cài đặt
- [ ] Repo đã fork đúng tên `K5-L3B-DAY10-OnlyTwo-PoCtoPilotGate1`, Public. **Settings → Collaborators**: mời Lên và Nguyên (quyền Write).
- [ ] Điền danh tính Git theo README bước 2a.
- [ ] `python3 -m unittest discover -s tests` → `Ran 13 tests … OK`.
- [ ] Gửi link PRD v1.1 cho cả bàn đọc §2, §3, §6 (Nguyên cần cho câu 1.2).

### Phút 15–60 · Phiếu A (chưa chạy trợ lý)
- [ ] **Câu 1.1** (A1): một mục tiêu cấp hệ thống, khác "model trả lời đúng", dựa vào PRD §3.
- [ ] **Câu 1.5** (A3): cả bàn chọn một kết luận, Quân ghi một câu giải thích.
- [ ] **Câu 1.6** (A4): mỗi chỉ số bắt buộc thành câu "Nếu … thì chúng tôi sẽ …"; soát bốn câu hỏi; hai câu ranh giới đầu ra (một hành động bị cấm, một ngưỡng chuyển người duyệt).
- [ ] Điền `config/acceptance_criteria.json`: `team` = `K5-L3B-DAY10-OnlyTwo-PoCtoPilotGate1`, `signed_by`, 5 ngưỡng `required`, `nice_to_have.escalation_rate_max`, 3 ngưỡng `business_ops`, `stop_condition`, 4 dòng `decision_rule`. Không chép ngưỡng từ file `.example.json`.
- [ ] Phút ~45: hỏi Lên về `pass_rate_min`, `pass_k_min`; hỏi Nguyên về `pii_leaks_max`, `queue_stuck_max`, `escalation_rate_max`.

### Phút 60–65 · Ký (chỉ Quân)
- [ ] Báo nhóm: "Đang ký, không ai chạy `eval`."
- [ ] `python3 -m lab10.criteria sign` → thấy `ĐÃ KÝ.`
- [ ] Chạy đúng dòng git máy in ra (commit + push `acceptance_criteria.json` và `.lock`).
- [ ] Ghi A5 (giờ ký, mã commit). Báo nhóm: "Đã ký, Lên pull rồi chạy base."

### Phút 65–85 · Phiếu B khối 2A
- [ ] **Câu 2.3** (B3): bản đồ dữ liệu + một ví dụ drift trong 3 tháng (xem `data/world.json` → `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`). Nói rõ đầu vào đổi hay quan hệ vào–ra đổi, chỉ số nào phát hiện.
- [ ] **Câu 2.5** (B6): điều phối pre-mortem 8–10 phút, ghi bảng, đủ bốn lăng kính; khoanh 2–3 lý do thành cổng.

### Phút 85–105 · Cổng kinh doanh
- [ ] **Câu 2.9** (B7.4): điền khối `business` trong `config/operating_gates.json`, mỗi số một câu lý do từ `ops_limits`, `ops_facts`. **Push trước phút ~95**, báo nhóm.
- [ ] **Câu 2.8** (B7.3): cùng Lên nghĩ 2 "ticket hiểm" cho behavioral test (Quân là "người không viết code" của câu này).
- [ ] Phút 103: dừng sửa config, đã push hết.

### Phút 105–115 · Quyết định v1
- [ ] Nhận mã lần chạy prepared + output lệnh 4 từ Lên.
- [ ] **B8 cột v1**: một quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule` tương ứng, kho/hãng có số xấu nhất, ngày quyết định lại. Cả bàn duyệt rồi commit, push.

### Phút 125–185 · Phiếu C
- [ ] **C1** (câu 3.0): cả bàn đọc report prepared; Quân ghi cổng vòng 1 đỡ được ô nào, dòng nào vượt trần, sự cố có trong pre-mortem không (đối chiếu B6).
- [ ] **Câu 3.2** (C5): một specification, kiểm được bằng code hoặc một con số trong report.
- [ ] **C6** (câu 3.4): ghi fault tree trước khi sửa; ít nhất hai nhánh ở hai tầng; mỗi lá có bằng chứng (`ticket@seed`, trường dữ liệu, dòng report).
- [ ] **Câu 3.5** (phần `business`): đổi `pilot_scope` / trần / ngân sách nếu nguyên nhân là tiền hoặc phạm vi. **Không thu hẹp về 0.** Push, báo Lên chạy lại. Gửi Lên nội dung hàng của mình cho bảng C7.
- [ ] Phút 180: dừng sửa config.

### Phút 185–200 · Quyết định v2
- [ ] **C12**: quyết định v2, đổi hay giữ so với v1 và vì con số nào, mã lần chạy ba mốc, **ba dòng bắt buộc** (giả định môi trường · giảm hay ngăn · cần đo lại gì trong pilot thật). Không chọn "Tiếp tục" nếu report còn vượt trần hoặc ngưỡng đã ký chưa đạt.
- [ ] Push C12, báo Nguyên chép vào `submission.json`.

### Sau buổi
- [ ] Viết mục `## NguyenVanHaiQuan-2A202603994` trong `TEAM.md` (phần việc, đóng góp, bằng chứng, exit ticket, AI đã dùng cho việc gì).
- [ ] Nộp link repo trên LMS.

## Nối PRD v1.1 sang Lab 10 (gợi ý, ngưỡng cuối cùng là của bàn)

| PRD v1.1 | Dùng cho |
|---|---|
| §3 metric an toàn (`approval_bypass`, `host_gate_violation`, `secret_leak` = 0, "không bù trừ") | Câu 1.1; `wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max` |
| §3 `pass_rate ≥ 0.85`, `pass_5 ≥ 0.80` (Lab 9) | Điểm xuất phát để cả bàn bàn `pass_rate_min`, `pass_k_min` cho bộ nền 22 ticket × 5 seed. Không nhất thiết giữ nguyên |
| §3 `cost_per_success` tăng ≤ 10% | `business_ops.cost_per_ticket_vnd_max` (so với `ops_facts.manual_cost_per_ticket_vnd` và `ops_limits.max_llm_cost_per_ticket_vnd`) |
| §2 phạm vi pilot (một đơn của chính khách; ngoài phạm vi luôn `escalated`) | `business.pilot_scope`; câu ranh giới đầu ra ở 1.6 |
| §5 cổng release (exit 1 thì không merge; không waiver cho metric an toàn) | `decision_rule` và `stop_condition` |
| §6 rủi ro mở (mock tất định, CI rộng, bug ≤ 1/3 seed) | Pre-mortem B6; dòng 3 của C12 (đo lại gì trong pilot thật) |
