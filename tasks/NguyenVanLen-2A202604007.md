# Nguyễn Văn Lên · 2A202604007 · Kỹ sư cổng (giữ máy chạy chính)

Cầm bút lệnh, trace, cổng code và chỉ số theo dõi. **Máy của Lên là máy duy nhất chạy `eval`, `gate`, `checkpoint`, `grade`, `check_submission`**, vì `runs/` không lên git (xem [README.md](README.md) Luật 2).

## File và mục chỉ mình Lên sửa

- `lab10/guards.py` (hàm `pre_guard`, `write_gate`), `lab10/monitors.py` (hàm mới + dict `MONITORS`).
- File do lệnh tạo ra trên máy Lên: `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock` (lệnh 5), `incidents/Sx/` (nhận thẻ), `submission/` trừ `submission.json` (lệnh 7).
- `TEAM.md` mục `## NguyenVanLen-2A202604007`.
- Phiếu A: A2 **cột trái** câu 1.3.
- Phiếu B: B0, B1, B2, B7.1, B7.2, B7.3.
- Phiếu C: dòng `Thẻ đã bốc:`, C0, C2, C7 (người ghi cả bảng), C8.

**Không đụng:** `config/acceptance_criteria.json`, `config/operating_gates.json` (Quân và Nguyên sửa; Lên chỉ đọc), `config/switches.json`, bản chụp vòng 1 sau khi tạo, `submission/submission.json`.

## Checklist theo mốc

### Phút 0–15 · Cài đặt
- [ ] Nhận lời mời Collaborator, clone repo, danh tính Git theo README bước 2a.
- [ ] `python3 -m unittest discover -s tests` → `Ran 13 tests … OK`; `git remote -v` có `origin` trỏ về repo bàn.
- [ ] Đọc đầu `lab10/guards.py`, `lab10/helpers.py`, [guide Phụ lục C](../docs/guide.md#phu-luc-c).

### Phút 15–60 · Phiếu A (chưa chạy trợ lý)
- [ ] **Câu 1.3** (A2, cột trái): chọn MỘT bước của agent; Thước đo · Dữ liệu · Cách tính · Điểm mù. **Push trước phút ~28**, báo Nguyên điền cột phải.
- [ ] Phút ~45: gửi Quân ý kiến về `pass_rate_min`, `pass_k_min`.
- [ ] **Không chạy `eval`** cho tới khi Quân báo đã ký và đã `git pull`.

### Phút 65–85 · Đo base
- [ ] `git pull --rebase origin main` (lấy commit ký).
- [ ] **Câu 2.1**: `python3 -m lab10.eval --suite base --stage base --note "baseline"` rồi `python3 -m lab10.gate --run runs/<mã>/report.json`. Gửi mã lần chạy + output vào nhóm chat.
- [ ] B0 dòng 1, B1 (lý lẽ ủng hộ/phản đối cổng tự chặn, khuyến nghị).
- [ ] **Câu 2.2** (B2): `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`, điền bảng soát lỗi.
- [ ] Tham gia pre-mortem B6 (Quân ghi).

### Phút 85–105 · Cổng code
- [ ] **Câu 2.6** (B7.1): 2–3 cổng trong `guards.py`, mỗi cổng ứng với một lý do pre-mortem hoặc một dòng HAZOP. Không xử lý riêng theo mã ticket hay câu chữ.
- [ ] Sau khi Quân push `business` (~95) và Nguyên push `operations`/`legal` (~100): `git pull`, chạy `python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."` và `unittest`. Không có ca mới hỏng so với base. Ghi B0 dòng 2.
- [ ] **Câu 2.7** (B7.2): hai bước tránh rò rỉ dữ liệu.
- [ ] **Câu 2.8** (B7.3): một tính chất + 2 ticket hiểm (cùng Quân), chạy bằng `trace --adhoc`, dán kết quả. Giữ 2 ticket này cho demo.

### Phút 103–115 · Chốt vòng 1 (điểm khoá)
- [ ] Phút 103: xác nhận Quân và Nguyên đã push, `git pull`.
- [ ] `python3 -m lab10.checkpoint` → `ĐÃ CHỐT cổng vòng 1 (mốc prepared)`.
- [ ] `python3 -m lab10.eval --suite base --stage prepared` → `python3 -m lab10.gate --run runs/<mã>/report.json`. Gửi mã + output cho Quân (B8). Ghi B0 dòng 3.
- [ ] Commit bản chụp vòng 1 + `guards.py` + Phiếu B phần của mình, push (lệnh cuối Phiếu B mục B8).

### Phút 125–135 · Nhận thẻ (chỉ máy Lên)
- [ ] Lab Coach báo số thẻ. Chạy từng dòng (thay `Sx`):
  `git fetch https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_cards.git main` → `git checkout FETCH_HEAD -- incidents/Sx` → `git commit -m "Nhận thẻ Sx"` → `python3 -m lab10.grade --incident Sx` → `git push origin main`.
- [ ] Ghi `Thẻ đã bốc: Sx` ở đầu Phiếu C và C0. Báo nhóm số thẻ để Quân điền ô thẻ trong `TEAM.md`.

### Phút 135–185 · Phân tích và sửa
- [ ] **Câu 3.1** (C2): trace ≥ 2 ticket hỏng theo hai kiểu khác nhau (`python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11`); ≥ 2 lỗi nguồn khác nhau, ≥ 1 lỗi chìm. Gửi danh sách cho Quân (C6) và Nguyên (C4).
- [ ] **Câu 3.5** (code): sửa nhánh trong `write_gate`/`pre_guard` cho nguyên nhân kỹ thuật.
- [ ] **Câu 3.6** (C8): một hàm mới trên dict `MONITORS` (nhận `trials`, trả về một số), đăng ký `"tên_chỉ_số": tên_hàm`. `escalation_rate` không tính.
- [ ] Mỗi lần Quân/Nguyên push config: `git pull` rồi `eval --suite Sx --stage after --note "đổi MỘT thứ: ..."` và `eval --suite base --stage after --note "kiểm lại bộ nền"`.
- [ ] **C7**: ghi cả bảng sửa (hàng code của mình + hàng Quân, Nguyên gửi), mỗi biện pháp "giảm" hay "ngăn".
- [ ] Phút 180: `python3 -m lab10.grade --incident Sx` → `monitor ✅`, `regression ✅`. Gửi report cho cả bàn.

### Phút 195–200 · Gom bài (chỉ máy Lên)
- [ ] Sau khi Nguyên push `submission.json`: `git pull`, `python3 -m lab10.check_submission --collect`, sửa `[THIẾU]` (hoặc báo người cầm bút mục đó), chạy lại tới `ĐỦ THÀNH PHẦN`.
- [ ] `git add -u && git add submission templates TEAM.md && git commit -m "LAB 10: bài nộp" && git push origin main`.

### Demo và sau demo
- [ ] Chiếu ba cột `base · prepared · after`. Chạy ticket hiểm hoặc số đổi thử của bàn kia.
- [ ] **Trả mọi số về bản v2**, chạy lại lệnh 6 và lệnh 7, push.
- [ ] Viết mục `## NguyenVanLen-2A202604007` trong `TEAM.md`; nộp link repo trên LMS.
