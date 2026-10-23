# Kế hoạch lịch: 4 tháng NCKH + 1 tháng luận văn + 1 tháng thủ tục

**Ngày giao bài (mặc định):** **Chủ nhật 22/11/2026** (dự phòng **23/11/2026** nếu lùi một ngày).  
**Sản phẩm NCKH:** **bộ slides** (HTML → PDF), *chưa* bắt buộc nộp báo cáo/luận văn đầy đủ.  
**Trong 4 tháng NCKH:** mỗi người **viết dần** Phần 1–2–3 đồ án theo `SPLIT_PLAN.md`.  
**Sau NCKH:** 1 tháng hoàn thiện luận văn → 1 tháng thủ tục bảo vệ.

Mốc tính từ **22/11/2026**. Nếu giao ngày 23/11 thì dịch toàn bộ mốc **+1 ngày**.

---

## 0. Tổng quan lịch

| Giai đoạn | Khoảng thời gian | Deliverable chính |
|-----------|------------------|-------------------|
| **NCKH (4 tháng)** | 22/11/2026 → 22/03/2027 | Slides NCKH + code chạy được trên 3 nhánh + draft luận văn ≥70% |
| **Hoàn thiện ĐA (1 tháng)** | 22/03/2027 → 22/04/2027 | Luận văn 3 phần đủ trang; số liệu khóa; không còn TODO lớn |
| **Thủ tục BV (1 tháng)** | 22/04/2027 → 22/05/2027 | Hồ sơ, lịch hội đồng, chạy lại demo từ `main` sạch |

---

## 1. Phân vai cố định (không đổi giữa kỳ)

| Role | Git branch | Sở hữu khoa học | Paper chính |
|------|------------|-----------------|-------------|
| **A** | `branch_a` | Sphering/TVN + batch trên **Cell Painting** | Ando, Way (spherize), Arevalo, Moshkov |
| **B** | `branch_b` | Cross-modal **Lasso/MLP** CP↔L1000 | Haghighi Fig. 2–3, Subramanian, Rohban |
| **C** | `branch_c` | Fusion **MoA** (compound) + đo alignment sau batch A | Haghighi Fig. 4, Way complementary |
| Chung | `main` | Loader Rosetta, metric chung, slides NCKH, README | — |

Chi tiết mục lục trang từng đồ án: [`SPLIT_PLAN.md`](SPLIT_PLAN.md).  
Phạm vi đúng paper: [`OUTLINE.md`](OUTLINE.md) §0.

---

## 2. Lịch NCKH 4 tháng (theo tuần / mốc)

### Tháng 1 — Nền + data (22/11 → 22/12/2026)

| Tuần | Chung | A | B | C |
|------|-------|---|---|---|
| W1 (22–28/11) | Kickoff; đọc Haghighi+Way; clone repo; tạo 3 branch | Đọc Ando, Arevalo | Đọc Haghighi Methods + Subramanian | Đọc Haghighi Fig.4 |
| W2 | Tải Rosetta curated (AWS); `data/inventory.md` | Pipeline CP + control wells | Pipeline L1000 khớp ID | Spec MoA labels compound |
| W3 | Khóa schema `shared/` | Sphering v0 trên 1 plate/subset | Lasso v0 1 subset (ưu tiên LUAD) | Early-fusion stub |
| W4 | Sync 30′; checklist M1 | Viết draft ĐA Phần 1 (≥8 trang) | Draft Phần 1 (≥8 trang) | Draft Phần 1 (≥8 trang) |

**Cổng tháng 1:** data local mở được; 3 draft Phần 1; không còn “chưa clone”.

### Tháng 2 — Phương pháp + baseline (22/12/2026 → 22/01/2027)

| Tuần | Chung | A | B | C |
|------|-------|---|---|---|
| W5–6 | Freeze interface profile v0 | Sphering/TVN + ≥1 method so (Harmony/ComBat) | Lasso+MLP trên **LUAD + LINCS** | Fusion CP vs L1000 vs early fusion trên **1** compound set |
| W7 | Bảng số nội bộ chung | Metric Arevalo/Way-style | Percent predictable + shuffle null | Jaccard/F1 hướng Fig.4 |
| W8 | Sync; draft Phần 2 toán | Phần 2 viết công thức whitening/TVN | Phần 2 Lasso/MLP | Phần 2 fusion + protocol A→B |

**Cổng tháng 2:** mỗi người ≥1 bảng số riêng; Phần 2 draft ≥12 trang (nhấn toán).

### Tháng 3 — Kết nối 3 nhánh + kết quả (22/01 → 22/02/2027)

| Tuần | Chung | A | B | C |
|------|-------|---|---|---|
| W9 | Profile “batch A” xuất cho B/C | Bảng ≥3 PP × metric | TA-ORF + CDRP báo cáo trung thực | Chạy lại cross-modal sau batch A |
| W10–11 | Hình poster/slide kết quả | Ablation control-fit | Gene/feature predictable | So fusion vs single |
| W12 | Sync; draft Phần 3 | Case study góc CP | Case góc L1000 | Bảng alignment trước/sau batch |

**Cổng tháng 3:** có hình “ba nhánh một câu chuyện”; draft Phần 3 ≥10 trang/người.

### Tháng 4 — Slides NCKH + khóa demo (22/02 → 22/03/2027)

| Tuần | Việc |
|------|------|
| W13 | Ghép slides NCKH (bài toán → PP → kết quả đã có → dự kiến); QC số liệu |
| W14 | Rehearsal 15–20′; sửa claim lệch paper |
| W15 | `main` xanh: README chạy được; 3 branch merge PR đã review |
| W16 (→22/03) | **Nộp / trình slides NCKH**; ký tiến độ `SPLIT_PLAN`; không yêu cầu luận văn đủ trang |

**Cổng NCKH:** slides PDF + demo `main` + draft ĐA ≥70% (ước lượng trang).

---

## 3. Hai tháng sau NCKH

### Tháng 5 — Hoàn thiện đồ án (22/03 → 22/04/2027)

- Đủ Phần 1 (15–20) · Phần 2 (20–30) · Phần 3 (~20) · Kết luận  
- Khóa số liệu (không đổi metric trừ lỗi)  
- Mỗi người chỉ sửa `branch_*` + chương mình; `shared/` chỉ bugfix  
- Checklist [`SPLIT_PLAN.md`](SPLIT_PLAN.md) §E

### Tháng 6 — Thủ tục bảo vệ (22/04 → 22/05/2027)

- Hồ sơ nhà trường / lịch hội đồng  
- Clone sạch `main` + checkout branch mình → chạy README ≤30′  
- Slide bảo vệ cá nhân (rút từ NCKH + ĐA)  
- Không thêm dataset mới

---

## 4. Nhịp phối hợp (bắt buộc)

| Nhịp | Tần suất | Mục đích |
|------|----------|----------|
| Sync ngắn | **Mỗi thứ Năm 20:30** | Blocker, interface `shared/`, số liệu C cần từ A/B |
| Freeze schema | Cuối tháng 1, 2 | Không đổi cột profile lung tung |
| Rehearsal NCKH | Tuần 14 | Một người trình, hai người bắt lỗi claim |
| Tag release | `nckh-2027-03` trên `main` ngày nộp slides |

**Phụ thuộc cứng:** C không chờ hết tháng 3 mới chạy simulation/alignment — dùng profile A **v0** từ cuối tháng 2; cập nhật lại một lần cuối tháng 3.

---

## 5. Viết dần đồ án trong 4 tháng NCKH

| Thời điểm | A/B/C nên có |
|-----------|----------------|
| Cuối T1 | Phần 1 ≥8 trang |
| Cuối T2 | Phần 2 ≥12 trang (toán) |
| Cuối T3 | Phần 3 ≥10 trang |
| Cuối T4 | Tổng draft ≥70% mục tiêu trang; hình/bảng gần final |
| Cuối T5 | Đủ trang theo SPLIT_PLAN |

---

## 6. Rủi ro lịch (4 tháng chặt hơn 6)

| Rủi ro | Giảm |
|--------|------|
| TA-ORF yếu làm mất thời gian | Ưu tiên LUAD/LINCS trước; TA-ORF chỉ đối chiếu |
| C chờ A | Profile v0 sớm (T2); alignment là phép đo lại, không làm lại hết B |
| Lan man paper mới | Cấm dataset mới sau T2 |
| Trùng đề khi BV | Khóa tiêu đề SPLIT_PLAN trước T5 |

Chi tiết Git: [`GITHUB.md`](GITHUB.md).  
Slides hướng dẫn giao bài: [`slides/nckh-briefing/index.html`](slides/nckh-briefing/index.html).
