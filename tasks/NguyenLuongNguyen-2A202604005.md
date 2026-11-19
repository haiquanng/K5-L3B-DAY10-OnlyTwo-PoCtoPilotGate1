# Nguyễn Lương Nguyên · 2A202604005 · Vận hành và pháp lý (gom bài nộp)

Cầm bút người trực, trách nhiệm, dữ liệu cá nhân, HAZOP, checklist go-live, runbook và `submission.json`.

## File và mục chỉ mình Nguyên sửa

- `config/operating_gates.json` → **chỉ khối `operations` và `legal`**: `pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`, `decision_note`, `review_sampling_pct`; `pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`.
- `submission/submission.json` (`team`, `members` đã điền sẵn; còn `incident`, `decision_v1`, `decision_v2`, `three_lines`).
- `TEAM.md` mục `## NguyenLuongNguyen-2A202604005`.
- Phiếu A: A1 câu 1.2, A2 **cột phải** câu 1.4 (sau khi Lên push cột trái).
- Phiếu B: B4, B5, B7.5, B7.6.
- Phiếu C: C3, C4, C5 câu 3.3, C9, C10, C11.

**Không đụng:** `lab10/*.py`, khối `business`, `config/acceptance_criteria.json`, `config/switches.json`, phần `submission/` do lệnh 7 sinh ra.
**Không chạy:** `eval`, `gate`, `grade`, `checkpoint`, `check_submission` (chỉ máy Lên chạy). Được chạy `trace` và `unittest` để đọc ticket.

## Checklist theo mốc

### Phút 0–15 · Cài đặt
- [ ] Nhận lời mời Collaborator, clone repo, danh tính Git theo README bước 2a, `unittest` → `OK`.
- [ ] Đọc PRD v1.1 §2, §6 ([`shared/PRD_v1.1.md`](shared/PRD_v1.1.md)) và `data/world.json` → `staff`, `ops_limits`, `ops_facts`, `staff_behavior`.

### Phút 15–60 · Phiếu A
- [ ] **Câu 1.2** (A1): một mục tiêu nhìn từ chị Oanh (NV-OANH, kế toán đối soát) và một mục tiêu nhìn từ chị Hạnh (NV-HANH, trưởng ca CSKH).
- [ ] **Câu 1.4** (A2, cột phải): telemetry production, không có nhãn; thêm khung thời gian và ngưỡng báo động. Viết nháp trong file này trước; **chỉ dán vào phiếu sau khi Lên push cột trái (~28) và đã `git pull`**.
- [ ] Phút ~45: gửi Quân ý kiến về `pii_leaks_max`, `queue_stuck_max`, `escalation_rate_max`.

### Phút 65–85 · Phiếu B khối 2A
- [ ] **Câu 2.4** (B4): HAZOP vòng 1 trên một tool ghi, ≥ 3 dòng, cộng ≥ 2 dòng ngoài kỹ thuật (người duyệt, ngân sách, phạm vi pilot, dữ liệu gửi bên thứ ba).
- [ ] **Câu 2.4** (B5): checklist 9 nhóm việc lần 1: trạng thái, bằng chứng, **PIC có tên** cho từng dòng.
- [ ] Tham gia pre-mortem B6 (Quân ghi), lo lăng kính "con người và vận hành" và "pháp lý".

### Phút 85–105 · Cổng con người, vận hành, pháp lý
- [ ] **Câu 2.10**: điền khối `operations` và `legal` trong `config/operating_gates.json` (nghĩa từng khoá: [guide, Cổng trong config](../docs/guide.md#ban-do)). `pic` không được trống. **Push trước phút ~100**, báo Lên.
- [ ] **B7.5**: runbook phần 1–3 khớp đúng các con số trong config, có dòng thời hạn dừng (từ tín hiệu đỏ đến lúc dừng xong tối đa bao nhiêu phút, ai bấm).
- [ ] **B7.6**: Giờ cao điểm (ai trực, mấy người, ngưỡng gọi thêm người, ngưỡng thu hẹp hoặc tắt). Bắt buộc nếu bốc thẻ S4, nên có với thẻ khác.
- [ ] Phút 103: dừng sửa config, đã push hết.

### Phút 125–185 · Phiếu C
- [ ] `git pull` sau khi Lên push thẻ; đọc `incidents/Sx/card.md`.
- [ ] **C3** (câu 3.1): phần riêng theo đúng số thẻ đã bốc (bàn bốc S4 không cần điền C3).
- [ ] **C4**: HAZOP của thẻ ≥ 3 dòng, mục riêng, không ghi đè HAZOP vòng 1. Dùng danh sách ticket hỏng Lên gửi.
- [ ] **Câu 3.3** (C5): một giả định về môi trường mà thiết kế ngầm tin nhưng có thể sai.
- [ ] **Câu 3.5** (phần `operations`, `legal`): đổi người trực, kiểm mẫu, `decision_note`, cổng pháp lý nếu nguyên nhân là người hoặc quy trình. **Không xếp thật nhiều người trực** (report đo cả chi phí). Push, báo Lên chạy lại. Gửi Lên nội dung hàng của mình cho bảng C7.
- [ ] Phút 180: dừng sửa config.
- [ ] **C9**: fault tree sau khi sửa (cổng nằm ở nhánh nào, tầng nào, nhánh nào còn hở).
- [ ] **C10**: ≥ 1 dòng risk register.
- [ ] **C11**: cập nhật checklist (cột PIC), runbook phần 4–5 (có thể xong trong 185–200).

### Phút 185–200 · Gom bài
- [ ] Sau khi Quân push C12: điền `submission/submission.json` → `incident` (`Sx`), `decision_v1`, `decision_v2`, ba câu `three_lines` chép đúng từ C12. Push, báo Lên chạy lệnh 7.
- [ ] Soát output lệnh 7 cùng Lên; dòng `[THIẾU]` thuộc mục ai thì báo người đó sửa.

### Sau buổi
- [ ] Viết mục `## NguyenLuongNguyen-2A202604005` trong `TEAM.md`; nộp link repo trên LMS.

## Nháp (chỉ Nguyên sửa phần này)

<!-- Viết nháp câu 1.4 và các con số operations/legal ở đây trước khi chép sang phiếu và config. -->
