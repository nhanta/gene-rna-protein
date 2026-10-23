# Hàm lượng toán — bám tên gọi và baseline trong paper

Tham số ước từ **control wells** hoặc cross-validation. Không hard-code hằng số sinh học.

**Phân vai:** A = §1–3; B = §4–5; C = §6 (+ §7 mở rộng).

---

## 1. Sphering / whitening trên negative control (A; Way, Arevalo)

Way 2022: *spherize* CP bằng DMSO controls để covariance control → identity (trích Ando; Kessy et al.).  
Arevalo 2024: **Sphering** — fit trên negative controls, áp lên toàn bộ; cần control mỗi batch.

Dạng whitening / sphering (viết luận văn): \(\widehat{\mathrm{Cov}}_{\mathrm{ctrl}}\) là **ma trận hiệp phương sai** ước trên giếng đối chứng — **không** phải ký hiệu tổng \(\sum\).

\[
z = \widehat{\mathrm{Cov}}_{\mathrm{ctrl}}^{-1/2}\,(x - \hat\mu_{\mathrm{ctrl}})
\]

Mũ \(-\tfrac12\) = nghịch đảo căn bậc hai của ma trận (làm “tròn” đám mây đối chứng về phương sai đơn vị, tương quan gần 0). Có thể thực hiện qua SVD/PCA của ma trận control. Cộng đồng CP gọi *sphering*; Ando gọi quy trình đầy đủ hơn là *TVN* (PCA + scale + CORAL).

**Hình cite (đã trích PNG cho slides):** `slides/nckh-briefing/figures/arevalo_fig1.png` (Arevalo Fig.1), `ando_fig3.png` (Ando Fig.3), `way_fig1.png` (Way Fig.1).

---

## 2. TVN — Typical Variation Normalization (A; Ando 2017)

Ando (đúng thứ tự paper):

1. PCA trên embedding/feature của **negative controls** (không nhất thiết giảm chiều).  
2. Chuẩn hóa từng trục (zero-mean, unit variance trên control).  
3. **Correlation alignment** theo batch (CORAL / Sun et al. 2016): whiten theo covariance control từng batch, recolor theo covariance control toàn cục.

Áp cùng transform cho control và treatment.

---

## 3. Harmony / ComBat (A so sánh; Arevalo liệt kê)

- **ComBat:** mô hình vị trí–tỷ lệ + empirical Bayes (sva).  
- **Harmony:** soft clustering + sửa batch lặp (Korsunsky; Arevalo benchmark trên JUMP CP).

Khi bảo vệ: nêu giả thiết khác sphering (Harmony không chỉ fit negative control).

---

## 4. Cross-modal regression — baseline Haghighi (B)

Haghighi: với mỗi landmark gene (hoặc mỗi CP feature chiều ngược),

\[
y \approx f(X_{\mathrm{CP}})
\]

baseline **Lasso**:

\[
\hat\beta=\arg\min_{\beta}\,\|y-X\beta\|_{2}^{2}+\lambda\|\beta\|_{1}
\]

- **MLP** (phi tuyến) — multilayer perceptron như baseline paper  

**Hình cite:** `slides/nckh-briefing/figures/haghighi_fig2.png` (Fig.2), `haghighi_fig4.png` (Fig.4 MoA fusion).

Đánh giá: prediction score; **percent predictable**; null bằng **shuffle** output (Haghighi Fig. 2).

**Ridge / CCA:** chỉ *so sánh thêm* — không thay Lasso/MLP khi nhận “tái lập paper”.

---

## 5. Percent replicating / mAP (A, B theo assay)

- **Percent replicating** (Way): tỷ lệ perturbation có tương quan replicate vượt null đã khớp dose / well position.  
- **mAP / AP** (Arevalo, CPJUMP1-style): retrieval replicate hoặc cùng nhãn sinh học; null permutation.

Dùng đúng metric paper đang neo — không trộn tên.

---

## 6. Fusion multimodal cho MoA (C; Haghighi Fig. 4)

Trên **CDRP-bio / LINCS (compound)**:

- Single modality: CP hoặc L1000  
- **Early fusion:** nối feature  
- **Late fusion:** trung bình xác suất lớp  
- **RGCCA** (Haghighi dùng Regularized GCCA) rồi early fusion trong không gian đó  

Metric: Jaccard vs MoA clusters (unsupervised); weighted F1 / accuracy (supervised) — bám setup paper hoặc nêu rõ subset rút gọn.

**Protocol alignment (C + A + B):**  
CP đã qua sphering/batch (A) → chạy lại percent predictable (B). Đây là kiểm tra đúng hướng câu Haghighi gợi ý *batch effect corrections to improve alignment* — không phải kết quả sẵn có trong bảng paper.

---

## 7. Simulation recovery (C — *mở rộng luận văn*)

Không phải kết quả Rosetta/Way. Sinh

\[
X = \cdots + B\beta_x^\top + G\gamma_x^\top + E_x
\]

(và tương tự \(Y\)) với batch \(B\) và tín hiệu \(G\) biết trước; đo recovery sau sphering/ComBat.  
Chỉ dùng để giải thích phương pháp; không viết như thể Haghighi đã làm.

---

## 8. Những gì **không** đưa làm trụ toán NCKH

| Tránh như claim chính | Lý do |
|------------------------|--------|
| Mediation nhân quả Gene→RNA→Morphology | Haghighi强调 quan hệ phức tạp, hai chiều, khác timepoint — không phải path nhân quả đã chứng minh |
| “Cell Painting = đo protein” | Paper: morphological profiles |
| Baseline tự chế thay Lasso/MLP khi nói tái lập Haghighi | Phải nêu Lasso/MLP trước |

---

## 9. Checklist toán khi nộp

| Mục | A | B | C |
|-----|---|---|---|
| Sphering/TVN đúng nguồn tên | ✓ | đọc | dùng khi nối A |
| Harmony/ComBat có mô tả | so | tuỳ | tuỳ |
| Lasso + MLP + shuffle null | — | ✓ | đo lại sau batch |
| Fusion MoA / early–late / RGCCA mức paper | — | — | ✓ |
| Simulation | — | — | chỉ mở rộng |
| Không mediation làm KT chính | ✓ | ✓ | ✓ |
