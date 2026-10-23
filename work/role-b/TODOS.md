# Role B — Todos NCKH / Đồ án B

**Sở hữu:** dự đoán chéo CP ↔ L1000 (Lasso/MLP, percent predictable, shuffle null) trên Rosetta.  
**Khóa phối hợp:** [`work/00-COORDINATION-MAP.md`](../00-COORDINATION-MAP.md) · **Template todo:** §3.

---

## Cover (định hướng — không thay cho claim số liệu)

1. **Bài toán góc — dự đoán chéo / shared subspace:** Với mỗi perturbation khớp ID, hai assay (Cell Painting profile vs L1000 landmark) có thông tin **chung** đủ để dự đoán lẫn nhau không? Khung *shared vs complementary* theo Haghighi Application 1 (Fig. 2–3), **không** lấy deep-dive batch/sphering của Role A làm phương pháp chính, **không** làm fusion MoA (Role C).

2. **Mục đích — tái lập baseline Haghighi:** Baseline **Lasso** (tuyến tính + ℓ₁) và **MLP** (phi tuyến) cho hai chiều CP→GE và GE→CP; báo **percent predictable** và null **shuffle** như paper — mục tiêu NCKH là khớp **hướng** (LUAD/LINCS mạnh hơn TA-ORF/CDRP-bio), không bắt buộc trùng mọi chữ số ([`OUTLINE.md`](../../OUTLINE.md) §8).

3. **Ứng dụng (trong giới hạn paper):** Gợi ý **tiết kiệm đo** / suy diễn một modality từ modality kia **chỉ** trong phạm vi Rosetta và hạn chế timepoint, landmark ~978, nhiễu kỹ thuật — không claim proteomics, không claim map 1–1 gen–hình thái ([`OUTLINE.md`](../../OUTLINE.md) §0).

4. **Nền L1000 landmark (~978):** Assay đo mRNA bulk cho bộ landmark; ~82% phương sai transcriptome *ước lượng* (Haghighi; chi tiết assay: Subramanian). CDRP-bio dùng probe set khác (977, overlap ~785 với epsilon) — xử lý đúng Methods Haghighi.

5. **Methods — Lasso + MLP + metrics:** \(y \approx f(X_{\mathrm{CP}})\) (và chiều ngược); đánh giá \(R^2\) với nested k-fold CV; null shuffle từng output; percent predictable theo ngưỡng null 99th + margin 0.2 ([`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §4; Haghighi Online Methods).

6. **Thực nghiệm theo subset; deliverable:** LUAD, LINCS, CDRP-bio, TA-ORF — bảng percent predictable, phân bố score, overlap gene predictable (hướng Fig. 2–3). TA-ORF: báo trung thực ~**4,7% (Lasso) / 5,5% (MLP)** landmark predictable ([`OUTLINE.md`](../../OUTLINE.md) §0, trích **Fig. 2b** Haghighi); LUAD/LINCS/CDRP-bio: **đo theo protocol Haghighi** (Fig. 2b), không bịa % nếu chưa chạy hoặc chưa screenshot bảng paper.

7. **Map todos → Đồ án B:** Phần 1 (L1000, shared/complementary, subset) · Phần 2 (khớp ID, Lasso, MLP, metric) · Phần 3 (tái lập subset, TA-ORF vs LUAD/LINCS, gene/feature predictable, CP sau batch A nếu có) — [`SPLIT_PLAN.md`](../../SPLIT_PLAN.md) D2.

**Phụ thuộc Role A (chỉ cite, không sở hữu):** profile CP đã sphering/TVN/batch → todo B-4xx chạy lại cross-modal; mô tả batch: output A + [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §1–3.

**Way 2022:** chỉ khung *complementary* trên **compound** + spherize như ngữ cảnh — **không** gán kết quả Way sang ORF/TA-ORF.

---

## PHẦN 1 · Khởi động, đọc nguồn, claim khóa

### B-101 · Khóa phạm vi Role B trên COORDINATION-MAP
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Xác nhận không overlap A (TVN/sphering sâu), C (MoA fusion Fig. 4).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 1 (layout Rosetta, mức 1 slide chung nhóm)
- **Data tải:** (chưa) — tham chiếu [`data/DATA.md`](../../data/DATA.md) §1
- **Toán / mô hình:** — 
- **Deliverable:** `work/role-b/SCOPE.md` (1 trang) hoặc ghi chú đầu notebook B
- **Phụ thuộc:** —
- **Không overlap với:** Role A, C

### B-102 · Đọc Haghighi Application shared subspace + Methods regression
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Nắm baseline Lasso/MLP, hai chiều dự đoán, lý do TA-ORF yếu.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2 (a–c), Fig. 3 (a–c); Extended Data Fig. 2–3 (LUAD gene/ORA — slide Phần 3)
- **Data tải:** —
- **Toán / mô hình:** \(y \approx f(X_{\mathrm{CP}})\); \(y\): vector mRNA landmark \(g\) qua perturbations; \(X_{\mathrm{CP}}\): ma trận profile CP — xem [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §4
- **Deliverable:** `work/role-b/notes/haghighi_fig2-3_outline.md`
- **Phụ thuộc:** B-101
- **Không overlap với:** Role C (Fig. 4)

### B-103 · Đọc L1000 landmark (Subramanian) — slide Phần 1
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Viết §1.2 Đồ án B: landmark, CMap, không nhầm full transcriptome.
- **Paper (PDF local):** `literature/papers/2017_Subramanian_L1000_CMap.pdf` · DOI `10.1101/136168` → `10.1016/j.cell.2017.10.049` · **Hình được phép chụp+cite:** Fig. 1 hoặc schematic L1000 (chọn 1 hình có caption rõ trong PDF)
- **Data tải:** —
- **Toán / mô hình:** —
- **Deliverable:** draft `docs/thesis_b/01-2-l1000.md` (hoặc tương đương branch_b)
- **Phụ thuộc:** —
- **Không overlap với:** Role A

### B-104 · Ngữ cảnh TA-ORF (Rohban) — không nhầm với Way ORF
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Giải thích perturbation ORF overexpression + CP; kỳ vọng cross-modal thấp (Haghighi).
- **Paper (PDF local):** `literature/papers/2017_Rohban_ORF_CellPainting.pdf` · DOI `10.7554/eLife.24060` · **Hình được phép chụp+cite:** Fig. 1 hoặc workflow ORF+CP (1 hình)
- **Data tải:** subset `TA-ORF-BBBC037-Rohban/` — [`data/DATA.md`](../../data/DATA.md) §1.1
- **Toán / mô hình:** —
- **Deliverable:** 1 slide «TA-ORF là gì» + cite Rohban; **không** dùng số liệu Way cho ORF
- **Phụ thuộc:** B-102
- **Không overlap với:** Role C (MoA compound)

### B-105 · Khung complementary Way (compound only) — 1 đoạn cite
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Nối khái niệm complementary với hạn chế modality không predict hết (Haghighi), **không** claim ORF.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. 1a hoặc intro schematic (compound A549)
- **Data tải:** —
- **Toán / mô hình:** —
- **Deliverable:** đoạn ≤½ trang trong Phần 1.4 (shared vs complementary) với nhãn «Way = compound»
- **Phụ thuộc:** B-102
- **Không overlap với:** Role A (spherize deep-dive)

### B-106 · Clone repo baseline Haghighi + liệt kê script regression
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Điểm bám implementation (grid-search, CV) trước khi viết pipeline riêng.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** — (Methods text)
- **Data tải:** GitHub `https://github.com/carpenter-singh-lab/2022_Haghighi_NatureMethods` (BSD-3)
- **Toán / mô hình:** nested k-fold + shuffle null — Haghighi Online Methods
- **Deliverable:** `work/role-b/notes/github_entrypoints.md`
- **Phụ thuộc:** B-102
- **Không overlap với:** —

---

## PHẦN 2 · Data Rosetta — tải, inventory, subset

### B-201 · Tải curated Rosetta (AWS no-sign-request)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Có local CP+L1000 khớp gallery Haghighi.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:**
  ```bash
  aws s3 sync --no-sign-request \
    s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data \
    ./data/raw/rosetta_curated
  ```
  (hoặc `preprocessed_data` ~8.5 GB nếu curated thiếu cột — [`data/DATA.md`](../../data/DATA.md))
- **Toán / mô hình:** —
- **Deliverable:** thư mục `data/raw/rosetta_curated/` + log sync
- **Phụ thuộc:** AWS CLI v2
- **Không overlap với:** Role A (JUMP benchmark Arevalo làm trụ A)

### B-202 · Inventory bốn subset B (LUAD, LINCS, CDRP-bio, TA-ORF)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Đếm perturbation, replicate, control; ghi probe set L1000.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:** `LUAD-BBBC041-Caicedo/`, `LINCS-Pilot1/`, `CDRP-...` / `CDRPBIO-...`, `TA-ORF-BBBC037-Rohban/` — [`data/DATA.md`](../../data/DATA.md)
- **Toán / mô hình:** CDRP-bio n=977 landmark (delta prime); LUAD/LINCS/TA-ORF n=978 (epsilon); overlap 785 — Haghighi Methods
- **Deliverable:** `data/inventory.md` (cột B ký hiệu)
- **Phụ thuộc:** B-201
- **Không overlap với:** Role C (MoA label compound — C lead, B chỉ dùng union ID cho regression)

### B-203 · QC mở file CP + L1000 TA-ORF (pandas)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Cổng tháng 1 PLAN: file mở được, không missing toàn bộ.
- **Paper (PDF local):** `literature/papers/2017_Rohban_ORF_CellPainting.pdf` · DOI `10.7554/eLife.24060` · **Hình được phép chụp+cite:** —
- **Data tải:** `TA-ORF-BBBC037-Rohban/CellPainting/...`, `.../L1000/...`
- **Toán / mô hình:** —
- **Deliverable:** snippet QC trong `data/inventory.md`
- **Phụ thuộc:** B-201
- **Không overlap với:** —

### B-204 · Ưu tiên tải LUAD + LINCS trước CDRP-bio + TA-ORF
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Khớp ưu tiên 6 tháng / W5–6 PLAN ([`PLAN_4MONTH.md`](../../PLAN_4MONTH.md)).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2b (bảng percent predictable — screenshot làm mục tiêu đối chiếu)
- **Data tải:** LUAD, LINCS paths trong gallery (B-201)
- **Toán / mô hình:** —
- **Deliverable:** checklist ưu tiên trong `work/role-b/DATA_PRIORITY.md`
- **Phụ thuộc:** B-202
- **Không overlap với:** —

---

## PHẦN 3 · Khớp perturbation & tiền xử lý (Haghighi Methods)

### B-301 · Khớp treatment-level CP ↔ L1000 (union ID)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Một hàng = một perturbation (± dose) dùng chung hai modality.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:** curated parquet/csv từng subset (B-201)
- **Toán / mô hình:** ma trận \(X_{\mathrm{CP}} \in \mathbb{R}^{N \times p}\), \(Y_{\mathrm{GE}} \in \mathbb{R}^{N \times 978}\) (977 CDRP-bio)
- **Deliverable:** `data/processed/{subset}_aligned.parquet` + số dòng N
- **Phụ thuộc:** B-202, interface `shared/` (nhóm)
- **Không overlap với:** Role C (lọc MoA — C dùng subset con compound)

### B-302 · Áp «normalized variable-selected» CP profiles (Haghighi)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Dùng đúng số feature CP paper cho chiều CP→GE (không tự chế feature mới làm baseline).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:** CP đã preprocess gallery / repo Haghighi
- **Toán / mô hình:** variable selection: loại near-zero variance; không cặp feature Pearson \(r > 0.9\); số feature sau chọn: **CDRP-bio 601, LUAD 291, TA-ORF 63, LINCS 119** (Haghighi Methods — chiều CP→GE)
- **Deliverable:** bảng `work/role-b/tables/cp_feature_counts_by_subset.csv`
- **Phụ thuộc:** B-301
- **Không overlap với:** Role A (sphering **trước** variable selection — nếu A gửi profile mới, todo B-401)

### B-303 · Xử lý probe set CDRP-bio vs epsilon (785 overlap)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Regression CDRP-bio chỉ trên landmark có trong dataset; không bịa infer 20% absent trừ khi gắn nhãn *mở rộng*.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:** CDRP-bio L1000
- **Toán / mô hình:** n=977 genes CDRP; overlap 785 (80%) — Haghighi Methods
- **Deliverable:** `data/processed/cdrpbio_landmark_index.json`
- **Phụ thuộc:** B-301
- **Không overlap với:** —

### B-304 · Freeze schema export cho Role C (chỉ ID + path, không MoA)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** C cần compound union; B cung cấp khóa perturbation đã align.
- **Paper (PDF local):** — · DOI — · **Hình được phép chụp+cite:** —
- **Data tải:** LINCS, CDRP-bio aligned (B-301)
- **Toán / mô hình:** —
- **Deliverable:** `shared/perturbation_keys_{subset}.csv`
- **Phụ thuộc:** B-301
- **Không overlap với:** Role C (fusion, RGCCA)

---

## PHẦN 4 · Pipeline Lasso (baseline tuyến tính)

### B-401 · Module CP→GE: Lasso từng landmark
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Tái lập nhánh tuyến tính Fig. 2a.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a (boxplot score vs shuffle)
- **Data tải:** `*_aligned.parquet` (B-301)
- **Toán / mô hình:** với từng gen landmark \(g\): \(y_g \approx f_{\mathrm{Lasso}}(X_{\mathrm{CP}})\); Lasso: \(\min \ \|y - Xw\|_2^2 + \lambda\|w\|_1\); đánh giá \(R^2\), nested k-fold CV; grid-search trên train fold — Haghighi + [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §4
- **Deliverable:** `branch_b/src/cp_to_ge_lasso.py` + unit test 1 subset nhỏ
- **Phụ thuộc:** B-302
- **Không overlap với:** Role A

### B-402 · Module GE→CP: Lasso từng feature CP
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Chiều ngược Fig. 3a (Lasso nếu paper so sánh; ít nhất MLP bắt buộc — Lasso tùy repo Haghighi, ưu tiên parity Methods).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 3a
- **Data tải:** aligned matrices
- **Toán / mô hình:** \(x_f \approx f_{\mathrm{Lasso}}(Y_{\mathrm{GE}})\) cho feature CP \(f\); cùng protocol CV + shuffle
- **Deliverable:** `branch_b/src/ge_to_cp_lasso.py`
- **Phụ thuộc:** B-401
- **Không overlap với:** —

### B-403 · Shuffle null (Lasso) — từng output vector
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Negative control như caption Fig. 2a (shuffle outputs mỗi iteration).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a (green shuffle distribution)
- **Data tải:** —
- **Toán / mô hình:** shuffle vector \(y_g\) (hoặc \(x_f\)) across perturbations; lặp CV → phân bố null; score \(<0\) = không generalize — Haghighi caption Fig. 2a
- **Deliverable:** `branch_b/src/shuffle_null.py` + seed documented
- **Phụ thuộc:** B-401
- **Không overlap với:** —

---

## PHẦN 5 · Pipeline MLP (baseline phi tuyến)

### B-501 · Module CP→GE: MLP từng landmark
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Baseline chính paper (MLP > Lasso).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a–b
- **Data tải:** aligned (B-301)
- **Toán / mô hình:** \(y_g \approx f_{\mathrm{MLP}}(X_{\mathrm{CP}})\); MLP feedforward; cùng nested k-fold + grid-search — Haghighi Methods
- **Deliverable:** `branch_b/src/cp_to_ge_mlp.py`
- **Phụ thuộc:** B-401 (cùng splitter CV)
- **Không overlap với:** —

### B-502 · Module GE→CP: MLP từng feature (Fig. 3)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Tái lập phân bố score feature CP.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 3a (MLP + shuffle)
- **Data tải:** aligned; n features: TA-ORF 1569, CDRP-bio 1570, LINCS 1670, LUAD 1569 (caption Fig. 3a)
- **Toán / mô hình:** \(x_f \approx f_{\mathrm{MLP}}(Y_{\mathrm{GE}})\)
- **Deliverable:** `branch_b/src/ge_to_cp_mlp.py`
- **Phụ thuộc:** B-501
- **Không overlap với:** —

### B-503 · Shuffle null (MLP) — parity với Lasso
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Null distributions Fig. 2a / 3a màu shuffle.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 3a (green)
- **Data tải:** —
- **Toán / mô hình:** cùng B-403, áp cho MLP
- **Deliverable:** hội tụ trong `shuffle_null.py`
- **Phụ thuộc:** B-403, B-501
- **Không overlap với:** —

---

## PHẦN 6 · Metrics — percent predictable & bảng tổng

### B-601 · Implement percent predictable (ngưỡng null 99th + 0.2)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Metric chính Application 1 — không tự đặt ngưỡng khác khi nói «tái lập Haghighi».
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2b (bảng Percent Predictable)
- **Data tải:** score distributions từ B-401/B-501
- **Toán / mô hình:** % landmark có **median** score predictability > threshold; threshold = 99th percentile của null (medians of single-gene nulls) **+ 0.2** — Haghighi «Percent Predictable» Online Methods
- **Deliverable:** `branch_b/src/percent_predictable.py`
- **Phụ thuộc:** B-403, B-503
- **Không overlap với:** Role A (percent **replicating** trên CP)

### B-602 · Bảng percent predictable × subset × model (CP→GE)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Deliverable NCKH tháng 2 (W7 PLAN).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2b (đối chiếu hình paper + bảng nhóm tự chạy)
- **Data tải:** LUAD, LINCS, CDRP-bio, TA-ORF
- **Toán / mô hình:** Lasso & MLP; **TA-ORF mục tiêu paper:** ~4,7% / 5,5% (OUTLINE §0, Fig. 2b); **LUAD/LINCS/CDRP-bio:** báo số tự chạy + «đo theo protocol Haghighi», không hard-code % paper nếu chưa verify screenshot
- **Deliverable:** `work/role-b/tables/percent_predictable_cp2ge.csv` + figure boxplot
- **Phụ thuộc:** B-601, B-701–B-704
- **Không overlap với:** Role C

### B-603 · Overlap 59 gene predictable ≥3 dataset (hướng Fig. 2c)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Shared subspace ở mức gen — so sánh hướng paper (59 gen MLP).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2c
- **Data tải:** kết quả MLP CP→GE bốn subset
- **Toán / mô hình:** tập gen «predictable» theo B-601; intersection/upset
- **Deliverable:** `work/role-b/tables/gene_overlap_predictable.csv` + UpSet/Venn
- **Phụ thuộc:** B-602
- **Không overlap với:** —

### B-604 · Metric feature CP predictable (GE→CP, median > 0.6 cross-dataset)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Hướng Fig. 3b (category radial distribution, texture).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 3b
- **Data tải:** GE→CP MLP scores
- **Toán / mô hình:** nhóm feature theo category CP; % highly predictable khi median score across datasets > 0.6 — caption Fig. 3b
- **Deliverable:** `work/role-b/figures/fig3b_style_categories.png`
- **Phụ thuộc:** B-502, B-704
- **Không overlap với:** —

---

## PHẦN 7 · Thực nghiệm theo subset (CP→GE + GE→CP)

### B-701 · Chạy full pipeline **LUAD** (CP→GE + GE→CP)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Subset cross-modal mạnh nhất (Haghighi text); case study Phần 3.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a (LUAD panel), Extended Data Fig. 2–3
- **Data tải:** `LUAD-BBBC041-Caicedo/`
- **Toán / mô hình:** Lasso + MLP; 291 CP features (CP→GE); percent predictable đo protocol Haghighi
- **Deliverable:** `work/role-b/results/luad/` (scores, plots, CSV)
- **Phụ thuộc:** B-401–B-503, B-601
- **Không overlap với:** —

### B-702 · Chạy full pipeline **LINCS-Pilot1**
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Compound A549; so với LUAD (cùng cell line — thảo luận chất lượng kỹ thuật, không claim nhân quả).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a (LINCS panel)
- **Data tải:** `LINCS-Pilot1/`
- **Toán / mô hình:** 119 CP features (CP→GE); Lasso + MLP
- **Deliverable:** `work/role-b/results/lincs/`
- **Phụ thuộc:** B-701 (cùng config)
- **Không overlap với:** Role C (MoA trên LINCS — C sở hữu fusion)

### B-703 · Chạy full pipeline **CDRP-bio** (không full CDRP)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Subset bioactive; kỳ vọng yếu hơn LUAD/LINCS (Haghighi text).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a (CDRP-bio); Supplementary 1–2 nếu cần cite lọc replicate
- **Data tải:** CDRP-bio subset gallery
- **Toán / mô hình:** 601 CP features; n=977 landmarks; percent predictable đo protocol Haghighi
- **Deliverable:** `work/role-b/results/cdrpbio/`
- **Phụ thuộc:** B-303
- **Không overlap với:** Role C (MoA CDRP-bio Fig. 4)

### B-704 · Chạy full pipeline **TA-ORF** — báo cáo yếu trung thực
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Góc genetic ORF; đối chiếu số paper TA-ORF.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2b (dòng TAORF); `literature/papers/2017_Rohban_ORF_CellPainting.pdf` · DOI `10.7554/eLife.24060`
- **Data tải:** `TA-ORF-BBBC037-Rohban/`
- **Toán / mô hình:** 63 CP features; **percent predictable paper (CP→GE landmark):** ~**4,7% Lasso, ~5,5% MLP** ([`OUTLINE.md`](../../OUTLINE.md) §0, Fig. 2b) — nhóm tự chạy so sánh, không «nặn» ORF
- **Deliverable:** `work/role-b/results/ta_orf/` + slide «TA-ORF yếu là expected»
- **Phụ thuộc:** B-104
- **Không overlap với:** Way (ORF)

### B-705 · Bảng so sánh TA-ORF vs LUAD/LINCS (Phần 3.2 Đồ án)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Thảo luận chất lượng/alignment vs cell line — đúng đoạn discussion Haghighi (không mediation).
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a–b (side-by-side cite)
- **Data tải:** kết quả B-701–704
- **Toán / mô hình:** percent predictable + phân bố median \(R^2\)
- **Deliverable:** `work/role-b/tables/subset_comparison_summary.md`
- **Phụ thuộc:** B-602, B-704
- **Không overlap với:** —

### B-706 · (*Tuỳ chọn, không baseline paper*) Cross-dataset train LINCS→test LUAD
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Minh họa generalizability yếu + gợi ý batch (cite A/C), không làm trụ NCKH.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Extended Data Fig. 1 (cross-dataset prediction)
- **Data tải:** LUAD + LINCS aligned
- **Toán / mô hình:** train Lasso/MLP trên A, test trên B — Haghighi Extended Data
- **Deliverable:** 1 figure + đoạn «batch là việc A/C»
- **Phụ thuộc:** B-701, B-702
- **Không overlap với:** Role A (không implement sphering ở đây)

---

## PHẦN 8 · Phân tích gene / feature predictable (explorative)

### B-801 · Top predictable genes LUAD — gene groups (Extended Data)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Slide/case Phần 3.3; không over-claim lung cancer only.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Extended Data Fig. 2; Extended Data Table 2 (nếu cite bảng)
- **Data tải:** LUAD MLP scores
- **Toán / mô hình:** top 100 MLP predictable — Haghighi
- **Deliverable:** `work/role-b/tables/luad_top100_genes.csv`
- **Phụ thuộc:** B-701
- **Không overlap với:** —

### B-802 · ORA predictable genes LUAD (WebGestalt hướng paper)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Liên hệ GO với kênh CP (DNA, actin…) — cite Fig. Extended Data 3.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Extended Data Fig. 3
- **Data tải:** top predictable set B-801
- **Toán / mô hình:** ORA FDR<0.2 như caption — hoặc chạy lại và so **hướng** enriched terms
- **Deliverable:** figure ORA + caption cite Haghighi
- **Phụ thuộc:** B-801
- **Không overlap với:** —

### B-803 · Exploratory notebook «gene ↔ CP feature» (hướng repo Haghighi)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Demo link cục bộ; không bắt buộc tái lập đủ Fig. 3c.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 3c (example output — screenshot paper nếu chưa chạy được)
- **Data tải:** LUAD preferred
- **Toán / mô hình:** top connections gene–feature từ model weights / importance (ghi rõ heuristic)
- **Deliverable:** `notebooks/B_explore_cp_ge_link.ipynb`
- **Phụ thuộc:** B-701
- **Không overlap với:** —

### B-804 · (*Mở rộng nhẹ*) Ridge/CCA so với Lasso — ghi không phải baseline gốc
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 2.5 SPLIT_PLAN — biến thể tuyến tính.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:** 1 subset (LUAD)
- **Toán / mô hình:** Ridge; CCA *so sánh* — [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §4 footnote
- **Deliverable:** 1 bảng phụ `ridge_vs_lasso_luad.csv`
- **Phụ thuộc:** B-701
- **Không overlap với:** Role C (RGCCA fusion)

---

## PHẦN 9 · Phụ thuộc Role A — CP sau batch (không sở hữu sphering)

### B-901 · Nhận profile CP «post-A» + metadata phương pháp
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Input cho Phần 3.4 Đồ án B + protocol C đo alignment.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** — (cite câu «batch effect corrections to improve alignment» trong discussion — text, không Fig.)
- **Data tải:** `shared/cp_profiles_post_batch_{subset}.parquet` từ Role A
- **Toán / mô hình:** **Không** triển khai TVN/sphering — chỉ đọc [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §1–3 như dependency
- **Deliverable:** `work/role-b/notes/cp_post_a_provenance.md`
- **Phụ thuộc:** Role A deliverable sphering/TVN
- **Không overlap với:** Role A (sở hữu PP batch)

### B-902 · Chạy lại percent predictable CP→GE trên CP post-A (≥1 subset)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Trả lời câu hỏi nhóm «batch có cải thiện alignment?» — Role C có thể trích bảng.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** —
- **Data tải:** CP gốc vs CP post-A (B-901)
- **Toán / mô hình:** cùng B-601; so sánh Δ percent predictable
- **Deliverable:** `work/role-b/tables/batch_ablation_percent_predictable.csv`
- **Phụ thuộc:** B-901, B-601, B-701 hoặc B-702
- **Không overlap với:** Role C (fusion MoA)

---

## PHẦN 10 · Đồ án B — viết & slides (map SPLIT_PLAN D2)

### B-1001 · Draft Phần 1 Đồ án B (≥8 trang, cổng T1)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Mục 1.1–1.5 D2 SPLIT_PLAN.
- **Paper (PDF local):** Haghighi + Subramanian + Rohban (cite trong text) · DOI như trên · **Hình được phép chụp+cite:** Fig. 2b (TA-ORF weak), 1 hình L1000 Subramanian
- **Data tải:** —
- **Toán / mô hình:** shared vs complementary định nghĩa paper
- **Deliverable:** `branch_b/docs/part1_draft.pdf` (≥8 tr)
- **Phụ thuộc:** B-103, B-104, B-105
- **Không overlap với:** A Phần 1 batch

### B-1002 · Draft Phần 2 — Lasso, MLP, metric (≥12 tr, cổng T2)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Mục 2.1–2.6 D2; công thức đủ [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §4.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** — (tự vẽ pipeline từ Methods, không generate fake boxplot)
- **Data tải:** —
- **Toán / mô hình:** \(y \approx f(X_{\mathrm{CP}})\); nested CV; shuffle; percent predictable threshold
- **Deliverable:** `branch_b/docs/part2_draft.pdf`
- **Phụ thuộc:** B-401–B-601
- **Không overlap với:** A §2 TVN

### B-1003 · Draft Phần 3 — kết quả subset + TA-ORF (≥10 tr, cổng T3)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Mục 3.1–3.5 D2; hạn chế landmark & timepoint.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2a–c, Fig. 3a–b (screenshot + bảng nhóm)
- **Data tải:** results B-701–705
- **Toán / mô hình:** —
- **Deliverable:** `branch_b/docs/part3_draft.pdf`
- **Phụ thuộc:** B-602, B-705, B-902 (nếu có)
- **Không overlap với:** C Fig. 4

### B-1004 · Slides NCKH — nhánh B (5–8 slide)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Poster/slides chung T4 — bài toán → Lasso/MLP → bảng subset.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Fig. 2b + 1 panel Fig. 2a (cite); TA-ORF 4,7/5,5% chỉ khi cite Fig. 2b/OUTLINE
- **Data tải:** `work/role-b/tables/*.csv`
- **Toán / mô hình:** một slide \(y \approx f(X_{\mathrm{CP}})\)
- **Deliverable:** `slides/nckh-briefing/role_b_*.html` hoặc section trong deck chung
- **Phụ thuộc:** B-602, B-705
- **Không overlap với:** Role A/C slides chính

### B-1005 · QC claim trước bảo vệ (OUTLINE §0 + QC_REPORT)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Không nhầm protein/Way-ORF/MoA; số TA-ORF có nguồn.
- **Paper (PDF local):** [`OUTLINE.md`](../../OUTLINE.md) · [`slides/nckh-briefing/QC_REPORT.md`](../../slides/nckh-briefing/QC_REPORT.md) · **Hình được phép chụp+cite:** —
- **Data tải:** —
- **Toán / mô hình:** —
- **Deliverable:** checklist ticked trong `work/role-b/QC_CLAIMS.md`
- **Phụ thuộc:** B-1004
- **Không overlap với:** —

---

## PHẦN 11 · Map todo → Đồ án B Phần 1 / 2 / 3 (slides luận văn sau)

| Đồ án B (SPLIT_PLAN D2) | Todo ID chính |
|-------------------------|---------------|
| **Phần 1** 1.1–1.5 | B-103, B-104, B-105, B-102, B-1001 |
| **Phần 2** 2.1–2.6 | B-301–B-303, B-401–B-503, B-601, B-804, B-1002 |
| **Phần 3** 3.1–3.5 | B-701–B-706, B-801–B-803, B-901–B-902, B-1003 |
| **Kết luận B** | B-705, B-1005 |
| **Slides NCKH** | B-1004, B-602, figures B-604 |

---

## PHẦN 12 · Hình ảnh bắt buộc lưu `work/role-b/figures/paper_screenshots/`

- [ ] Fig. 2a Haghighi — boxplot Lasso/MLP + shuffle (CP→GE)
- [ ] Fig. 2b Haghighi — bảng Percent Predictable (mọi subset)
- [ ] Fig. 2c Haghighi — overlap gene predictable
- [ ] Fig. 3a Haghighi — MLP GE→CP + shuffle
- [ ] Fig. 3b Haghighi — category feature predictable
- [ ] Extended Data Fig. 2–3 (LUAD) — nếu dùng trong Phần 3
- [ ] Extended Data Fig. 1 — nếu làm B-706

*(Mỗi file: `YYYYMMDD_Haghighi_FigX_panelY.png` + sidecar `.caption.md` tác giả, DOI, số hình.)*

---

*Planner Role B · cập nhật lần đầu khi tạo file.*
