# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `OnlyTwo`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-OnlyTwo-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Văn Hải Quân | 2A202603994 | Sản phẩm và kinh doanh | ✅ |
|   2 | Nguyễn Văn Lên | 2A202604007 | Kỹ sư cổng | |
|   3 | Nguyễn Lương Nguyên | 2A202604005 | Vận hành và pháp lý | |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenVanHaiQuan-2A202603994

### Phần việc phụ trách

Sản phẩm và kinh doanh, trưởng nhóm, chủ PRD v1.1 dùng chung. Câu 1.1, 1.5, 1.6, 2.3, 2.5, 2.9, 3.2, 3.4, quyết định v1/v2; Phiếu A (A1 câu 1.1, A3–A5), Phiếu B (B3, B6, B7.4, B8), Phiếu C (C1, C5 câu 3.2, C6, C12); `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`. Chi tiết: [`tasks/NguyenVanHaiQuan-2A202603994.md`](tasks/NguyenVanHaiQuan-2A202603994.md).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NguyenVanLen-2A202604007

### Phần việc phụ trách

Kỹ sư cổng, giữ máy chạy chính (eval, gate, checkpoint, grade, check_submission). Câu 1.3, 2.1, 2.2, 2.6–2.8, 3.1 (trace), 3.5 (code), 3.6; Phiếu A (A2 câu 1.3), Phiếu B (B0–B2, B7.1–B7.3), Phiếu C (C0, C2, C7, C8); `lab10/guards.py`, `lab10/monitors.py`. Chi tiết: [`tasks/NguyenVanLen-2A202604007.md`](tasks/NguyenVanLen-2A202604007.md).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NguyenLuongNguyen-2A202604005

### Phần việc phụ trách

Vận hành và pháp lý, gom bài nộp. Câu 1.2, 1.4, 2.4, 2.10, 3.1 (phần riêng theo thẻ), 3.3, 3.5 (`operations`, `legal`), 3.7; Phiếu A (A1 câu 1.2, A2 câu 1.4), Phiếu B (B4, B5, B7.5, B7.6), Phiếu C (C3, C4, C5 câu 3.3, C9–C11); `config/operating_gates.json` mục `operations`, `legal`; `submission/submission.json`. Chi tiết: [`tasks/NguyenLuongNguyen-2A202604005.md`](tasks/NguyenLuongNguyen-2A202604005.md).

### Đóng góp cụ thể

**Vòng 1**
- **Câu 1.2 (Phiếu A, A1):** mục tiêu nhìn từ chị Oanh (đối soát được 100% khoản hoàn và lỗi hãng, 0 hoàn oan, 0 lỗi ghi oan, không vượt ngân sách 2.000.000đ/ngày) và chị Hạnh (≤ 6 ca/giờ, không ca nào chờ quá 60 phút, có ghi chú để kiểm mẫu).
- **Câu 1.4 (Phiếu A, A2 cột phải):** telemetry production cho hành vi ghi lỗi hãng: số lỗi tự động/hãng trong 24 giờ và 7 ngày, tỉ lệ lỗi có `delay_cause ∉ fault_causes`; ngưỡng vàng/đỏ khớp `ops_limits` và `wrongful_carrier_faults_max = 0`. Sửa lại định nghĩa "khớp" sau khi đối chiếu nhãn T-006 (`FORCE_MAJEURE` vẫn ghi lỗi cho MKD).
- **Câu 2.4 (Phiếu B, B4):** HAZOP vòng 1 trên `file_carrier_fault`, 4 dòng kỹ thuật (ghi lỗi cho hãng của kiện đầu tiên thay vì kiện trễ nhất; nhánh `fail_open` ghi lỗi bất kể nguyên nhân; không đếm lỗi/hãng/ngày; chép `customer_note` và `recipient_contact` sang hãng) và 3 dòng ngoài kỹ thuật (người duyệt, ngân sách, dữ liệu gửi bên thứ ba).
- **Câu 2.4 (Phiếu B, B5):** checklist 9 nhóm việc lần 1, mỗi dòng một PIC có tên; cập nhật dòng 1 bằng lần chạy base.
- **Câu 2.10:** điền `config/operating_gates.json` mục `operations` (PIC `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực × 6 ca/giờ, chờ tối đa 60 phút, 7 điều kiện dừng, kênh cảnh báo, `decision_note = true`, kiểm mẫu 10%) và `legal` (chặn `recipient_contact`, `customer_note` gửi hãng; bắt buộc có nguyên nhân ghi nhận khi ghi lỗi hãng).
- **B7.5, B7.6:** runbook phần 1–3 khớp các con số trong config (dừng tối đa 15 phút, NV-TUNG bấm) và mục giờ cao điểm (ước tính tải từ `ops_facts` và lần chạy base).

**Vòng 2** (bổ sung sau khi có thẻ): C3, C4, C5 câu 3.3, câu 3.5 phần `operations`/`legal`, C9, C10, C11 (runbook 4–5), `submission/submission.json`.

### Bằng chứng

Các commit có tiền tố `[Nguyen]` (tác giả git hiển thị mã trưởng nhóm `2A202603994` theo README bước 2a; email `2A202604005@example.com`):

| Commit | Nội dung |
|---|---|
| `33f1e4e` | Phiếu A câu 1.2, 1.4 |
| `eef94d1` | Phiếu B mục B4 (HAZOP vòng 1), B5 (checklist lần 1); sửa câu 1.4 theo `fault_causes` |
| `5fb4a7e` | Câu 2.10: `config/operating_gates.json` mục `operations`, `legal` |
| `69cbf63` | Phiếu B mục B7.5 (runbook 1–3), B7.6 (giờ cao điểm) |
| `e8b4fd8` | Phiếu B mục B5 dòng 1: bằng chứng lần chạy base |

Lần chạy dùng làm bằng chứng: `R-base-before-20261119-155220-f6ac62` (B5 dòng 1, B7.6).

### Exit ticket

Một điều học được, một điều còn chưa chắc. *(viết cuối buổi)*
