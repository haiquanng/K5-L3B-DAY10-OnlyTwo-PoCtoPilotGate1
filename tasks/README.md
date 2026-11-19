# Phân việc bàn OnlyTwo · LAB 10 (Gate 1)

Repo: `K5-L3B-DAY10-OnlyTwo-PoCtoPilotGate1` · Lớp L3B · Bàn 3 người.

| Người | MSSV | Vai | Việc cụ thể |
| ----- | ---- | --- | ----------- |
| Nguyễn Văn Hải Quân (trưởng nhóm) | 2A202603994 | **Sản phẩm và kinh doanh** | [NguyenVanHaiQuan-2A202603994.md](NguyenVanHaiQuan-2A202603994.md) |
| Nguyễn Văn Lên | 2A202604007 | **Kỹ sư cổng** · giữ **máy chạy chính** | [NguyenVanLen-2A202604007.md](NguyenVanLen-2A202604007.md) |
| Nguyễn Lương Nguyên | 2A202604005 | **Vận hành và pháp lý** · gom bài nộp | [NguyenLuongNguyen-2A202604005.md](NguyenLuongNguyen-2A202604005.md) |

**Bản chung từ Lab 9:** PRD v1.1 và eval card của Quân, chép vào [`shared/PRD_v1.1.md`](shared/PRD_v1.1.md) và [`shared/eval_card.md`](shared/eval_card.md). Hai file này chỉ để đọc, không ai sửa. Hai link `judge_audit.md` và `trace_case.md` bên trong trỏ về repo Lab 9, không có ở đây.

---

## 1. Ba luật chống conflict

### Luật 1 · Mỗi file, mỗi mục chỉ có MỘT người cầm bút

Chỉ người cầm bút được sửa và commit phần đó. Người khác muốn góp ý thì nhắn trong nhóm chat, hoặc viết nháp vào file `tasks/<tên-mình>.md` của chính mình rồi gửi cho người cầm bút chép vào.

| File / mục | Người cầm bút | Ghi chú |
|---|---|---|
| `config/acceptance_criteria.json` + `.lock` | **Quân** | Chỉ Quân ký. Ký xong thì **không ai** mở file này nữa (kể cả mở rồi lưu lại) |
| `lab10/guards.py`, `lab10/monitors.py` | **Lên** | |
| `tests/` (mọi file) | (không ai) | **Bị khoá bằng hash** (`lab10/MANIFEST.json`). Sửa là `1 integrity ❌` → bài không được tính. Test riêng của bàn để ngoài repo hoặc chạy bằng `trace --adhoc` |
| `config/operating_gates.json` mục `business` | **Quân** | Sửa đúng 4 dòng của khối `business` |
| `config/operating_gates.json` mục `operations`, `legal` | **Nguyên** | Sửa đúng trong hai khối đó |
| `config/switches.json` | (không ai) | README không cho sửa file này |
| `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock` | **Lên** (lệnh 5 tạo) | Tạo xong thì không ai sửa |
| `incidents/S4/` | **Quân** kéo thẻ (3 lệnh git) · **Lên** chạy `grade` | Thẻ của bàn: **S4**. Kéo thẻ CHỈ SAU khi Lên đã chạy `checkpoint`. Không sửa nội dung thẻ |
| `submission/submission.json` | **Nguyên** | `team` và `members` đã điền sẵn |
| `submission/` (phần còn lại, do lệnh 7 sinh ra) | **Lên** chạy lệnh 7, **Nguyên** soát | Vì `runs/` chỉ có trên máy Lên |
| `TEAM.md` phần đầu (thông tin nhóm, bảng thành viên) | **Quân** | Đã điền sẵn, chỉ còn ô "Thẻ đã bốc" |
| `TEAM.md` mục `## HoVaTen-MSSV` | **chính người đó** | Mỗi người chỉ sửa mục của mình |
| `tasks/<tên>.md` | **chính người đó** | Dùng làm nháp và đánh dấu checklist |

Mục trong ba phiếu (`templates/`):

| Phiếu | Quân (SP & KD) | Lên (Kỹ sư cổng) | Nguyên (VH & PL) |
|---|---|---|---|
| **A** | dòng `Bàn:` · A1 câu 1.1 · A3 câu 1.5 (ghi kết luận cả bàn) · A4 câu 1.6 · A5 | A2 **cột trái** câu 1.3 (làm trước) | A1 câu 1.2 · A2 **cột phải** câu 1.4 (làm sau Lên) |
| **B** | dòng `Bàn:` · B3 · B6 (ghi pre-mortem cả bàn) · B7.4 · B8 (quyết định v1) | B0 · B1 · B2 · B7.1 · B7.2 · B7.3 (cùng Quân) | B4 · B5 · B7.5 · B7.6 |
| **C** | dòng `Bàn:` · dòng `Thẻ đã bốc: S4` · C0 (chép mã Lên gửi) · C1 (ghi cả bàn) · C2 (trace) · C5 câu 3.2 · C6 (ghi fault tree cả bàn) · C7 (ghi cả bảng) · C12 (quyết định v2) | C8 (chỉ số theo dõi + code `monitors.py`) | C3 (S4 không cần) · C4 · C5 câu 3.3 · C9 · C10 · C11 · bổ sung B7.6 theo thẻ |

**Bảng chung = một người ghi.** Git báo conflict khi hai người sửa hai dòng sát nhau, kể cả hai hàng khác nhau trong cùng một bảng. Vì vậy bảng nào nhiều người góp (A2, B6, C1, C6, C7) chỉ có một người gõ; người khác đọc nội dung cho người đó. Riêng A2: Lên điền cột câu 1.3, push, báo nhóm; Nguyên `git pull` xong mới điền cột câu 1.4.

### Luật 2 · Chỉ chạy đo trên MỘT máy: máy của Lên

`runs/` (nhật ký `journal.jsonl`, report, mã lần chạy) nằm trong `.gitignore`, **không lên git**. Lệnh 7 chỉ gom được nhật ký của máy chạy nó. Nếu mỗi người chạy `eval` trên máy mình, nhật ký bị chia ba và bàn mất bằng chứng "ký trước khi đo".

- Chỉ máy Lên chạy: lệnh 2 `eval`, lệnh 4 `gate`, lệnh 5 `checkpoint`, lệnh 6 `grade`, lệnh 7 `check_submission --collect`, và ba lệnh nhận thẻ.
- Ai cũng được chạy trên máy mình: lệnh 3 `trace` (không ghi nhật ký) và `python3 -m unittest discover -s tests`.
- Quân chạy lệnh 1 `criteria sign` trên máy mình, push. **Lên phải `git pull` trước lần `eval` đầu tiên.**
- Lên in mã lần chạy vào nhóm chat ngay sau mỗi lệnh, để Quân và Nguyên chép vào phiếu của mình.
- Máy Lên hỏng giữa buổi: chép cả thư mục `runs/` sang máy khác (USB, Drive), không chạy lại từ đầu.

### Luật 3 · Mọi người làm thẳng trên `main`, commit nhỏ, pull trước khi push

Lab đẩy thẳng lên `main` ở các mốc ký và chốt, nên bàn **không** dùng nhánh riêng hay Pull request.

```bash
git pull --rebase origin main          # trước khi bắt đầu sửa
# ... sửa đúng file/mục của mình ...
git add <đúng file của mình>           # KHÔNG dùng `git add .` hay `git add -A`
git commit -m "[Quan|Len|Nguyen] câu x.y: <việc gì>"
git pull --rebase origin main          # trước mỗi lần push
git push origin main
```

- Tắt "format on save" trong VS Code cho `.json` và `.md` của lab. Định dạng lại cả file sẽ đụng mục của người khác, và với `acceptance_criteria.json` thì làm hỏng hash đã ký.
- Gặp conflict: dừng lại, báo trong nhóm. Người cầm bút mục đó giữ bản của mình, xoá bản kia, rồi `git rebase --continue`. Không dùng `--force`.
- Không bấm **Sync fork** hay mở Pull request về repo mẫu.

---

## 2. Bàn giao theo mốc (ai chờ ai)

| Phút | Ai giao | Giao gì | Cho ai làm tiếp |
|---|---|---|---|
| 0–15 | Quân | Mời Lên, Nguyên làm Collaborator (quyền Write); bảng `TEAM.md` | Cả bàn clone, chạy test |
| ~28 | Lên | A2 cột câu 1.3 đã push | Nguyên điền cột câu 1.4 |
| ~45 | Lên, Nguyên | Nhắn Quân ý kiến về ngưỡng (Lên: pass_rate, pass_k; Nguyên: pii, queue_stuck, escalation) | Quân chốt `acceptance_criteria.json` |
| **60–65** | **Quân** | **Ký, commit, push tiêu chí** | Lên `git pull` rồi mới được `eval` |
| 65–70 | Lên | Mã lần chạy base + output lệnh 4 | Quân (B3, B8), Nguyên (B4, B5) |
| ~95 | Quân | Khối `business` của `operating_gates.json` đã push | Lên thử cổng trần tiền (nếu có) |
| ~100 | Nguyên | Khối `operations` + `legal` đã push | Lên thử lại `eval --stage after` |
| **103** | Quân, Nguyên | Mọi thay đổi config đã push, **dừng sửa** | **Lên pull, chạy lệnh 5 (chốt), eval prepared, gate** |
| 108–113 | Lên | Mã lần chạy prepared + output gate | Quân viết B8 (v1); cả bàn duyệt |
| **125** | **Quân** → **Lên** | Quân kéo thẻ S4 + ghi `Thẻ đã bốc: S4`, push → Lên pull, chạy lệnh 6 `grade --incident S4`, gửi report | Cả bàn `git pull`, đọc `incidents/S4/card.md` |
| ~155 | Quân | Danh sách ticket hỏng + nguồn lỗi (C2: `S4-07`, `S4-08` nhiều seed) | Quân (C5, C6), Nguyên (C4), Lên (sửa code) |
| 155–175 | Quân, Nguyên | Sửa config (`business` / `operations`, `legal`), push | Lên chạy `eval --suite Sx --stage after` |
| **180** | Quân, Nguyên | **Dừng sửa config** | Lên chạy lệnh 6 lần cuối, gửi report |
| 185–195 | Quân | C12 (v2 + ba dòng bắt buộc), push | Nguyên chép vào `submission.json` |
| 195–200 | Nguyên → Lên | `submission.json` đã push | Lên pull, lệnh 7 tới khi `ĐỦ THÀNH PHẦN`, push |
| Sau demo | Lên | Trả mọi số đổi thử về bản v2, chạy lại lệnh 6 và 7, push | Cả bàn kiểm tra trên GitHub |
| Trước deadline | **Từng người** | Mục cá nhân trong `TEAM.md` + exit ticket; nộp link repo trên LMS | |

**Điểm khoá (không ai sửa gì khác trong lúc này):** phút 60–65 (ký), 103–113 (chốt vòng 1), 180–185 (report cuối), lúc chạy lệnh 7.

---

## 3. Quyết định chung (cả bàn chốt, một người ghi)

- Câu 1.5 (A3), pre-mortem B6, mốc prepared C1, fault tree C6: cả bàn bàn, người ghi theo bảng ở Luật 1.
- Quyết định v1 (B8) và v2 (C12): Quân đề xuất bằng con số; Lên xác nhận số khớp report; Nguyên xác nhận người trực và runbook khớp. Cả ba đồng ý thì Quân ghi.
- Mọi con số trong tiêu chí và `operating_gates.json` phải có người giải thích được lúc demo (RULES.md): ngưỡng là Quân, cổng code là Lên, người trực và pháp lý là Nguyên.
