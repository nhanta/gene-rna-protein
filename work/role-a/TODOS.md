# Role A — Todos NCKH / Đồ án A (Cell Painting: sphering, TVN, batch)

**Khóa nội dung:** chỉ hình thái CP, nhiễu kỹ thuật batch/plate/well; **không** Lasso/MLP (B), **không** fusion MoA (C).  
**Template bắt buộc:** `work/00-COORDINATION-MAP.md` §3.

---

## PHẦN I — Phát biểu bài toán (batch/plate làm méo hình thái)

### A-P1-01 · Viết đoạn “bài toán Role A” cho slides NCKH + mục 1.3 đồ án
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phát biểu rõ vì sao profile Cell Painting bị méo bởi batch/plate/vị trí giếng trước khi so sánh perturbation hoặc giao profile cho B/C.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. 1A (ví dụ ảnh CP năm kênh); Fig. 1B (percent replicating — ngữ cảnh đo tin cậy sau xử lý); Fig. S5 (plate position, edge wells — xác nhận số hình khi mở PDF)
- **Data tải:** Rosetta CP curated — xem `data/DATA.md` §1.2 (`aws s3 sync --no-sign-request s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data ./raw/rosetta_curated`)
- **Toán / mô hình:** Không mô hình mới — mô tả bài toán: vector profile \(x \in \mathbb{R}^d\) (well-level aggregate) mang tín hiệu sinh học + nhiễu kỹ thuật; mục tiêu Role A là biến đổi \(x \mapsto x'\) giảm nhiễu batch mà vẫn giữ metric sinh học (Way spherize DMSO; Arevalo replicate retrieval).
- **Deliverable:** `work/role-a/draft/P1-01-bai-toan.md` (1–2 tr) + 1 slide “Câu hỏi A” trong `slides/` (khi nhóm ghép)
- **Phụ thuộc:** Chung: `data/inventory.md` có số plate/control
- **Không overlap với:** Role B (cross-modal), Role C (MoA fusion)

### A-P1-02 · Neo bài toán vào khung Rosetta (chỉ CP, không claim multimodal của A)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Giải thích CP trong Rosetta là readout hình thái tách đĩa với L1000; A chỉ xử lý nhánh CP.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** «Fig. trong paper Haghighi mô tả layout CP+L1000 — xác nhận khi mở PDF» (không dùng Fig. 2–4 làm kết quả của A)
- **Data tải:** Cùng Rosetta curated; liệt kê subset CP: `LUAD-BBBC041-Caicedo/`, `LINCS-Pilot1/`, `CDRP-...`, `TA-ORF-.../CellPainting/` (`data/DATA.md` §1.2)
- **Toán / mô hình:** Không — phạm vi: ma trận profile CP theo well/plate, cột metadata batch/plate/control.
- **Deliverable:** Bảng 1 cột trong `work/role-a/draft/P1-02-rosetta-cp-scope.md` (subset | số plate ước lượng | loại control)
- **Phụ thuộc:** A-P1-01
- **Không overlap với:** Role B (L1000, percent predictable), Role C (fusion)

### A-P1-03 · Phân biệt “nuisance variation” vs phenotypic signal (từ vựng luận văn)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Dùng cùng từ ngữ paper khi giải thích vì sao batch làm lệch MOA/replicate nếu không hiệu chỉnh.
- **Paper (PDF local):** `literature/papers/2017_Ando_TVN_Sphering.pdf` · DOI `10.1101/161422` · **Hình được phép chụp+cite:** Fig. 3A (batch effect trên trục PCA control); Fig. 2B (t-SNE — minh họa cụm, không claim số liệu Rosetta)
- **Data tải:** Không bắt buộc (lý thuyết); ví dụ số liệu sau từ Rosetta inventory
- **Toán / mô hình:** Ando: nuisance = batch, plate, well-position; TVN fit trên **negative controls** (MATH_NOTES §2, bước 1–3).
- **Deliverable:** Đoạn ½ tr trong `P1-01-bai-toan.md` + glossary 5 thuật ngữ (TVN, sphering, DMSO control, batch, replicate)
- **Phụ thuộc:** A-P1-01
- **Không overlap với:** Role C (complementary / shared subspace)

### A-P1-04 · Sơ đồ pipeline Role A (input → correction → metric → export cho B/C)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Khóa interface `shared/`: profile thô vs profile đã sphering/batch + metadata batch id.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 1 (evaluation pipeline — adapt cho Rosetta/JUMP subset)
- **Data tải:** `data/DATA.md` §1.3 (`data/processed/`)
- **Toán / mô hình:** Pipeline: fit trên negative control (Sphering/TVN) hoặc batch label (Harmony/ComBat) → áp toàn profile → đo replicate retrieval / percent replicating.
- **Deliverable:** `work/role-a/draft/P1-04-pipeline.mmd` hoặc slide 1 flowchart; spec cột parquet export (`branch_a/README` khi code sẵn)
- **Phụ thuộc:** Freeze schema tháng 1 (`PLAN_4MONTH.md` W4)
- **Không overlap với:** Role B pipeline Lasso/MLP

---

## PHẦN II — Mục đích (Role A)

### A-P2-01 · Mục tiêu NCKH (4 tháng) — câu hỏi có thể trả bằng bảng số
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Viết mục đích đo lường được: so ≥3 phương pháp batch trên CP Rosetta (+ tuỳ chọn JUMP) theo metric Way/Arevalo.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. 1B (percent replicating theo dose — minh họa metric, dataset Way compound không phải kết quả Rosetta)
- **Data tải:** Rosetta CP subsets (`data/DATA.md` §1.2); JUMP profiles — «URL/lệnh cụ thể khi chọn scenario Arevalo — ghi trong `data/inventory.md` khi khóa»
- **Toán / mô hình:** Mục tiêu tối ưu hoá: cao **percent replicating** (Way) và/hoặc **mAP** replicate retrieval (Arevalo), không tối ưu cross-modal \(R^2\) (B).
- **Deliverable:** `work/role-a/draft/P2-01-muc-tieu.md` + bullet trong slides NCKH chung
- **Phụ thuộc:** A-P1-04
- **Không overlap với:** Role B/C mục đích dự đoán chéo / MoA

### A-P2-02 · Mục tiêu Đồ án A (sau NCKH) — đủ Phần 1–3 SPLIT_PLAN
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Map mục đích dài hạn vào `SPLIT_PLAN.md` D1 (Phần 1–3 A): benchmark + thảo luận hạn chế control-only.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 2 hoặc Fig. 3 (quantitative scenario — cite làm mẫu bảng, không copy số Arevalo sang Rosetta)
- **Data tải:** Rosetta (bắt buộc); JUMP (tuỳ chọn mở rộng Arevalo-style)
- **Toán / mô hình:** Xem MATH_NOTES §1–3, §5.
- **Deliverable:** Checklist trang mục tiêu trong `work/role-a/draft/P2-02-do-an-muc-tieu.md` (neo SPLIT_PLAN D1)
- **Phụ thuộc:** A-P2-01
- **Không overlap với:** Role B/C tiêu đề đồ án §C SPLIT_PLAN

### A-P2-03 · Tiêu chí “thành công” và hạn chế (không phóng đại)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Liệt kê điều **không** claim (mediation, proteinomics, Way ORF); ghi hạn chế sphering cần control mỗi batch (Arevalo).
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** «Fig. discussion/limitation trong Arevalo — xác nhận khi mở PDF»
- **Data tải:** `OUTLINE.md` §0 (sự thật quan trọng) — không tải thêm
- **Toán / mô hình:** Sphering: mọi batch phải có negative control (Arevalo Results, Sphering28); Harmony/ComBat: cần batch labels (Arevalo §Selection).
- **Deliverable:** Mục “Hạn chế” trong `P2-01-muc-tieu.md`
- **Phụ thuộc:** A-P2-01
- **Không overlap với:** Role C simulation (mở rộng)

---

## PHẦN III — Ứng dụng thực tế (trong giới hạn paper)

### A-P3-01 · Ứng dụng: profile hình thái tin cậy hơn cho so sánh perturbation
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Mô tả ứng dụng đúng paper: sau batch correction, replicate/MOA retrieval ổn định hơn trên CP (Way compound; Arevalo JUMP).
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. 1D (compound signal một/both assay — chỉ dùng ý “đo được perturbation”, không gán ORF)
- **Data tải:** Rosetta CP compound subsets (LINCS, CDRP) + LUAD nếu có đủ replicate
- **Toán / mô hình:** Percent replicating: % replicate có median pairwise Spearman vượt null khớp dose, sample size, well position (Way Methods; Fig. S6).
- **Deliverable:** 1 tr `work/role-a/draft/P3-01-ung-dung.md` + 1 slide ứng dụng
- **Phụ thuộc:** A-P2-01
- **Không overlap với:** Role C MoA fusion supervised

### A-P3-02 · Ứng dụng nội bộ nhóm: export profile CP cho B/C (alignment sau batch)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Ghi rõ Haghighi **gợi ý** batch correction có thể cải thiện alignment — C đo lại trên output A, A không chạy Lasso.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** «Đoạn text gợi ý batch/alignment — trích trang, không bịa Fig. số»
- **Data tải:** `data/processed/cp_profiles_v0.parquet` (tên freeze theo `shared/`)
- **Toán / mô hình:** Không — protocol: cùng ID perturbation, khác transform CP (raw vs sphering vs Harmony…).
- **Deliverable:** `work/role-a/draft/P3-02-handoff-bc.md` (version profile, hash, cột metadata)
- **Phụ thuộc:** A-P1-04; PLAN_4MONTH T2 profile v0
- **Không overlap với:** Role C chạy fusion; Role B huấn luyện Lasso

### A-P3-03 · Ngữ cảnh Moshkov: sphering trong workflow CNN CP (không train CNN ở A)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Trích dẫn thực hành cộng đồng: sphering trên control trong pipeline profiling (bổ sung lý do làm A).
- **Paper (PDF local):** `literature/papers/2024_Moshkov_SVD_Sphering.pdf` · DOI `10.1038/s41467-024-45999-1` · **Hình được phép chụp+cite:** Fig. 1D (minh họa sphering batch-correction trên control — xác nhận nhãn panel khi mở PDF)
- **Data tải:** Không (cite-only); A dùng feature CP cổ điển/pycytominer như Rosetta
- **Toán / mô hình:** MATH_NOTES §1: \(z = \hat\Sigma^{-1/2}(x - \hat\mu_{\mathrm{ctrl}})\); fit \(\hat\Sigma\) trên control wells.
- **Deliverable:** Đoạn 2 đoạn trong `P3-01-ung-dung.md` (phân biệt: A không triển khai Cell Painting CNN)
- **Phụ thuộc:** A-P5-01
- **Không overlap với:** Role B representation learning

---

## PHẦN IV — Kiến thức nền Cell Painting + control wells (Bray)

### A-P4-01 · Assay Cell Painting: kênh, compartment, profile well-level
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Viết Phần 1 đồ án §1.2: năm kênh, ~1500 feature/cell, aggregate well (Arevalo dùng mean cell trong well).
- **Paper (PDF local):** `literature/papers/2016_Bray_CellPainting.pdf` · DOI `10.1038/nprot.2016.105` · **Hình được phép chụp+cite:** Fig. 1 (sáu stain, năm kênh); Fig. 2 (pipeline profile)
- **Data tải:** Rosetta CP parquet — đếm số cột feature thực tế (`data/inventory.md`)
- **Toán / mô hình:** Vector feature well: trung bình theo cell trong well (Arevalo Methods: population-averaged well-level profiles).
- **Deliverable:** `work/role-a/draft/P4-01-cell-painting-nen.md` (4–5 tr hướng SPLIT_PLAN 1.2)
- **Phụ thuộc:** Data inventory
- **Không overlap với:** Role B mô tả L1000 assay sâu

### A-P4-02 · Thiết kế plate: replicate, DMSO negative control, positive control
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Giải thích vì sao control wells là cơ sở sphering/TVN (Way: 24 DMSO + 24 proteasome inhibitor trên layout Way — dùng làm **ví dụ paper**, Rosetta layout đọc từ metadata).
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. S3A (plate layout — xác nhận khi mở PDF)
- **Paper (PDF local, bổ sung):** `literature/papers/2016_Bray_CellPainting.pdf` · DOI `10.1038/nprot.2016.105` · **Hình được phép chụp+cite:** «Mục Plate layout and selection of replicates and controls — Fig. trong protocol nếu có — xác nhận khi mở PDF»
- **Data tải:** Rosetta metadata cột well type / perturbation / plate
- **Toán / mô hình:** Tập control \( \mathcal{C} \): wells DMSO (negative); ước \(\hat\mu_{\mathrm{ctrl}}, \hat\Sigma\) trên \(x_i, i \in \mathcal{C}\) (MATH_NOTES §1).
- **Deliverable:** Bảng `control_well_counts_by_subset.csv` + đoạn Bray/Way trong `P4-01`
- **Phụ thuộc:** A-P4-01
- **Không overlap với:** Role B khớp ID perturbation GE

### A-P4-03 · Batch / plate / well-position effects trên CP
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 1.3 đồ án: edge wells, cùng vị trí well across replicate plates (Way).
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. S5 (plate position); Fig. S7 (ảnh hưởng spherize lên percent replicating)
- **Data tải:** Rosetta: plot correlation theo row/col well (kết quả tự chạy)
- **Toán / mô hình:** Null percent replicating điều chỉnh well position (Way Methods); spherize làm DMSO covariance → identity (Way main text + Methods ZCA-cor).
- **Deliverable:** 1 hình diagnostic Rosetta (tự chạy) + caption; 1 screenshot Fig. S5 Way (cite)
- **Phụ thuộc:** A-P4-02; code QC v0
- **Không overlap với:** Role C plate effects cho multimodal narrative chính

### A-P4-04 · PCA, cosine similarity, ý tưởng whitening (SGK + Ando)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 1.4 đồ án: nền đại số trước TVN/sphering.
- **Paper (PDF local):** `literature/papers/2017_Ando_TVN_Sphering.pdf` · DOI `10.1101/161422` · **Hình được phép chụp+cite:** Fig. 1C–D (TVN transform trên control → áp treatment)
- **Data tải:** Không
- **Toán / mô hình:** PCA trên embeddings/features control không giảm chiều (Ando TVN); normalize từng trục zero-mean unit variance trên control; correlation alignment batch (CORAL, Sun et al. 2016) — MATH_NOTES §2.
- **Deliverable:** `work/role-a/draft/P4-04-pca-whitening-nen.md`
- **Phụ thuộc:** A-P4-01
- **Không overlap với:** Role B CCA/ridge mở rộng

### A-P4-05 · Phạm vi data A: Rosetta CP subsets + tuỳ chọn JUMP (Arevalo)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 1.5: khóa subset tháng 1–2, ghi rõ JUMP là mở rộng benchmark batch không thay Rosetta làm neo chính NCKH.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 1 (scenarios nhiều lab/batch)
- **Data tải:** `data/DATA.md` §1–2; JUMP Hub / Cell Painting Gallery — link ghi trong `data/inventory.md` khi tải
- **Toán / mô hình:** Không
- **Deliverable:** `work/role-a/draft/P4-05-data-scope.md` + cập nhật `data/inventory.md` (A sở hữu số liệu CP)
- **Phụ thuộc:** Checklist tải DATA.md §4
- **Không overlap với:** Role B bốn subset Rosetta cho L1000 (cùng bảng inventory, cột khác)

---

## PHẦN V — Phương pháp (sphering, TVN, Harmony, ComBat, metrics)

### A-P5-01 · Sphering / whitening trên negative control (Way ZCA-cor)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Implement baseline spherize như Way Methods (DMSO → identity covariance).
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. S3B (processing pipeline — xác nhận khi mở PDF)
- **Data tải:** Rosetta CP + nhãn DMSO/control (`data/raw/rosetta_curated`)
- **Toán / mô hình:** Way: ZCA whitening trên ma trận correlation profile (ZCA-cor); tương đương whitening làm covariance DMSO → \(I\). MATH_NOTES §1: \(z = \hat\Sigma^{-1/2}(x - \hat\mu_{\mathrm{ctrl}})\).
- **Deliverable:** `branch_a/spherize.py` (hoặc module freeze) + unit test 1 plate; subsection 2.2 đồ án
- **Phụ thuộc:** A-P4-02; shared schema
- **Không overlap với:** Role B pretreatment L1000

### A-P5-02 · TVN — 3 bước Ando (PCA control → scale trục → CORAL batch)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Implement TVN song song sphering để so sánh (Ando đặt tên **TVN**, không gọi là “SVD sphering của Ando”).
- **Paper (PDF local):** `literature/papers/2017_Ando_TVN_Sphering.pdf` · DOI `10.1101/161422` · **Hình được phép chụp+cite:** Fig. 1 (overview A–D); Fig. 3B (ablation trục PCA)
- **Data tải:** Rosetta CP; batch id theo plate
- **Toán / mô hình:** (1) PCA trên control, không giảm chiều; (2) chuẩn hóa mỗi trục: zero-mean, unit variance trên control; (3) CORAL alignment covariance control từng batch với covariance control toàn cục — MATH_NOTES §2; áp cùng transform cho control + treatment (Ando TVN section).
- **Deliverable:** `branch_a/tvn.py` + bảng so sánh nhanh vs sphering trên 1 subset; subsection 2.3 đồ án
- **Phụ thuộc:** A-P5-01
- **Không overlap với:** Role C

### A-P5-03 · Arevalo “Sphering” trong benchmark (đối chiếu implementation)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Đảm bảo cách gọi và giả thiết khớp Arevalo (whitening matrix từ negative controls, mọi batch có control).
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 2 (Scenario 1 quantitative — Sphering vs others)
- **Data tải:** Rosetta hoặc JUMP subset có nhiều batch
- **Toán / mô hình:** Arevalo: Sphering28 — whitening từ negative controls, áp toàn dataset; cần control mỗi batch.
- **Deliverable:** Ghi chú `work/role-a/notes/sphering-arevalo-vs-way.md` + tham số chung hóa trong code
- **Phụ thuộc:** A-P5-01
- **Không overlap với:** Role B

### A-P5-04 · Harmony — mô tả mức cao + cite SI (không chứng minh dài)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Thêm Harmony vào bảng so sánh (Arevalo top performer một số scenario).
- **Paper (PDF local):** `literature/papers/2019_Korsunsky_Harmony.pdf` · DOI preprint `10.1101/461954` · journal `10.1038/s41592-019-0619-0` · **Hình được phép chụp+cite:** «Fig. workflow Harmony trong paper chính — xác nhận khi mở PDF»
- **Paper (PDF local, toán):** `literature/papers/2019_Korsunsky_Harmony_SI.pdf` · **Hình được phép chụp+cite:** «Equation / algorithm block trong SI — xác nhận khi mở PDF»
- **Data tải:** Rosetta CP + cột `batch_id` / `plate_id`
- **Toán / mô hình:** Arevalo tóm tắt: Harmony = EM lặp, tìm cụm đa batch rồi mixture correction trong cụm (MATH_NOTES §3). **Không** chỉ fit negative control — ghi giả thiết khác Sphering.
- **Deliverable:** Wrapper `branch_a/batch_harmony.py` + subsection 2.4 đồ án (mức high-level + pointer SI)
- **Phụ thuộc:** A-P5-01; batch labels QC
- **Không overlap với:** Role B Harmony trên embedding L1000 (nếu có)

### A-P5-05 · ComBat — mô tả mức cao (Arevalo + sva)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Baseline batch thứ ba trong bảng ≥3 phương pháp.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 4 hoặc Fig. 5 (scenario ít replicate — cite qualitative)
- **Paper (PDF local, bổ sung):** `literature/papers/2017_Johnson_ComBat.pdf` · **Hình được phép chụp+cite:** «Fig. vignette ComBat — xác nhận khi mở PDF»
- **Data tải:** Rosetta CP matrices + batch factor
- **Toán / mô hình:** Arevalo: ComBat27 — batch = nhiễu nhân + cộng trên signal, fit linear + empirical Bayes (MATH_NOTES §3).
- **Deliverable:** `branch_a/batch_combat.py` + ghi version R/Python sva
- **Phụ thuộc:** A-P5-04 (cùng interface)
- **Không overlap với:** Role C

### A-P5-06 · Tiền xử lý profile CP (pycytominer / khớp Haghighi prep mức A cần)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 2.1: normalize, feature selection trước batch correction (Arevalo preprocessing).
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Supplementary Fig. 1 (preprocessing — xác nhận số hình khi mở PDF)
- **Data tải:** Rosetta curated (đã preprocess gallery) — ghi bước bổ sung nếu có
- **Toán / mô hình:** Không thêm công thức ngoài paper; log/transform theo Arevalo Methods trích trong text.
- **Deliverable:** `branch_a/preprocess_cp.py` + doc pipeline order (preprocess → batch → metric)
- **Phụ thuộc:** shared loader
- **Không overlap với:** Role B L1000 pretreatment

### A-P5-07 · Metric: percent replicating (Way) trên CP Rosetta
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Implement metric reproducibility cho subset có replicate cùng compound+dose.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. S6 (giải thích metric); Fig. 1B (kết quả minh họa trên data Way)
- **Data tải:** Rosetta LINCS/CDRP/LUAD — lọc perturbation có ≥2 replicate
- **Toán / mô hình:** Median pairwise Spearman giữa replicate profiles; percent replicating = % treatment có correlation median > null matched (dose, n replicate, well position) — Way Methods “Calculating reproducibility metrics - percent replicating”.
- **Deliverable:** `shared/metrics/percent_replicating.py` (A chủ spec) + cột bảng kết quả
- **Phụ thuộc:** A-P5-06
- **Không overlap với:** Role B percent predictable / shuffle null

### A-P5-08 · Metric: mAP replicate retrieval (Arevalo) trên CP
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Metric thứ hai cho benchmark batch (cosine similarity, AP trung bình).
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 2 (mAP trong scenario 1 — cite paper gốc, số Rosetta tự chạy)
- **Data tải:** Rosetta/JUMP subset có compound id + replicate cross-batch nếu có
- **Toán / mô hình:** Similarity cosine; mỗi sample là query; positive = cùng compound; negative = cùng plate khác compound hoặc control cùng plate (mAP nonrep / mAP control); \( \mathrm{AP}_i = \sum_{k=1}^{(M-1)+N} (R_{k-1} - R_k) P_k \), \( R_k = \mathrm{TP}_k/(M-1) \), \( P_k = \mathrm{TP}_k/k \); \( \mathrm{mAP} = \frac{1}{M}\sum_{i=1}^M \mathrm{AP}_i \) (Arevalo Methods, trích `literature/text/2024_Arevalo_BatchCorrection.txt`).
- **Deliverable:** `shared/metrics/map_retrieval.py` + doc giải thích biến thể áp Rosetta
- **Phụ thuộc:** A-P5-06
- **Không overlap với:** Role C Jaccard MoA

### A-P5-09 · Giả thiết control-only & hạn chế (subsection 2.6 đồ án)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Viết thảo luận phương pháp: khi sphering/TVN giả định sai (thiếu control/batch).
- **Paper (PDF local):** `literature/papers/2017_Ando_TVN_Sphering.pdf` · DOI `10.1101/161422` · **Hình được phép chụp+cite:** Table 2 (DMSO mock-treatment bias — nuisance)
- **Data tải:** Rosetta ablation: bỏ 1 plate control → đo metric (tự chạy)
- **Toán / mô hình:** Fit transform chỉ trên \(\mathcal{C}\); không dùng label treatment khi fit sphering/TVN (Ando, Arevalo Sphering).
- **Deliverable:** `work/role-a/draft/P5-09-gia-thiet-han-che.md` + 1 hàng ablation bảng Phần 3
- **Phụ thuộc:** A-P5-01, A-P5-07
- **Không overlap với:** Role C simulation planted batch (mở rộng)

### A-P5-10 · Baseline “no correction” cho bảng so sánh
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Cột Baseline như Arevalo Fig. 2 để Δ metric có ý nghĩa.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 2 (Baseline vs corrected)
- **Data tải:** Cùng matrix preprocess A-P5-06
- **Toán / mô hình:** Identity transform \(x' = x\).
- **Deliverable:** Cột `baseline` trong `results/benchmark_cp.csv`
- **Phụ thuộc:** A-P5-07, A-P5-08
- **Không overlap với:** Role B shuffle null

---

## PHẦN VI — Thực nghiệm (Rosetta CP + tuỳ chọn JUMP; bảng kết quả)

### A-P6-01 · Inventory & QC: đếm plate, control, replicate theo subset
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 3.1 đồ án — thống kê dataset thực dùng.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** «Table/dataset overview Haghighi — xác nhận khi mở PDF» (số liệu báo cáo = inventory tự đếm)
- **Data tải:** `data/DATA.md` §1.2 sync curated
- **Toán / mô hình:** Không
- **Deliverable:** `data/inventory.md` (mục CP Role A) + `results/cp_subset_stats.tex`
- **Phụ thuộc:** DATA.md checklist §4
- **Không overlap với:** Role B inventory L1000 (cùng file, section riêng)

### A-P6-02 · Chạy benchmark subset 1 — LUAD-BBBC041 (CP)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Subset cross-modal mạnh (Haghighi) nhưng A chỉ báo metric CP batch/replicate.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 3 (scenario multi-lab — style bảng, không copy số)
- **Data tải:** `./raw/rosetta_curated/LUAD-BBBC041-Caicedo/.../CellPainting/`
- **Toán / mô hình:** Lưới: `{baseline, sphering, TVN, Harmony, ComBat}` × `{percent_replicating, mAP}` (subset metric nếu thiếu replicate).
- **Deliverable:** `results/luad_benchmark.csv` + figure bar chart (số tự chạy)
- **Phụ thuộc:** A-P5-01…P5-08
- **Không overlap với:** Role B Lasso LUAD

### A-P6-03 · Chạy benchmark subset 2 — LINCS-Pilot1 (CP, compound)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Compound layout gần use-case Way/Arevalo hơn TA-ORF.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. 1B (minh họa percent replicating theo dose — so sánh **định tính**, không dùng số Way)
- **Data tải:** `./raw/rosetta_curated/LINCS-Pilot1/.../CellPainting/`
- **Toán / mô hình:** Cùng lưới A-P6-02; stratify theo dose nếu metadata có.
- **Deliverable:** `results/lincs_cp_benchmark.csv`
- **Phụ thuộc:** A-P6-02 (cùng script)
- **Không overlap với:** Role C fusion LINCS MoA

### A-P6-04 · Chạy benchmark subset 3 — CDRP-bio / CDRPBIO (CP)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Compound thêm cho độ phủ plate/batch; C dùng cùng subset cho MoA nhưng bảng số khác.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 5 (scenario khác microscope — nếu Rosetta không có, cite làm mẫu thảo luận)
- **Data tải:** `./raw/rosetta_curated/CDRP-.../CellPainting/` (đúng tên thư mục sau inventory)
- **Toán / mô hình:** Giống A-P6-02
- **Deliverable:** `results/cdrp_cp_benchmark.csv`
- **Phụ thuộc:** A-P6-01
- **Không overlap với:** Role C MoA table

### A-P6-05 · TA-ORF CP — báo cáo trung thực (batch metric, không kỳ vọng cao cross-modal)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** ORF genetic: A vẫn đo batch correction trên hình thái; không claim Way complementary cho ORF.
- **Paper (PDF local):** `literature/papers/2017_Rohban_ORF_CellPainting.pdf` · DOI `10.7554/eLife.24060` · **Hình được phép chụp+cite:** «Fig. trong Rohban giới thiệu ORF screen — xác nhận khi mở PDF»
- **Data tải:** `./raw/rosetta_curated/TA-ORF-BBBC037-Rohban/CellPainting/`
- **Toán / mô hình:** Cùng metric A-P5-07/08
- **Deliverable:** `results/ta_orf_cp_benchmark.csv` + 1 đoạn “hạn chế ORF” (OUTLINE §0)
- **Phụ thuộc:** A-P6-02
- **Không overlap với:** Role B TA-ORF percent predictable

### A-P6-06 · (Tuỳ chọn) JUMP CP profiles — scenario Arevalo-style
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Mở rộng nếu Rosetta ít batch; ghi nhãn *mở rộng* trong luận văn.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 1, Fig. 2 (pipeline + scenario 1)
- **Data tải:** JUMP / Cell Painting Gallery — lệnh URL ghi `data/inventory.md` (`data/DATA.md` §2)
- **Toán / mô hình:** Replicate retrieval cross-batch như Arevalo Methods
- **Deliverable:** `results/jump_cp_benchmark.csv` (optional) hoặc ghi “skipped + lý do”
- **Phụ thuộc:** Bandwidth tháng 2–3; không block Rosetta
- **Không overlap với:** Role B benchmark JUMP thay Arevalo (B cấm trong SPLIT_PLAN)

### A-P6-07 · Bảng tổng hợp ≥3 phương pháp × metric (deliverable NCKH cốt lõi)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 3.2 đồ án + slide kết quả A.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 2 (format bảng/bar quantitative)
- **Data tải:** Gộp CSV A-P6-02…06
- **Toán / mô hình:** Không — aggregate mean/median mAP và percent replicating theo method
- **Deliverable:** `results/table_main_benchmark_cp.md` + `figures/main_benchmark.png`
- **Phụ thuộc:** A-P6-02, A-P6-03, A-P6-04 tối thiểu
- **Không overlap với:** Role B/C bảng chính

### A-P6-08 · Ablation: fit control trên một plate vs pooled; edge well filter
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 3.3 đồ án (SPLIT_PLAN 3.3).
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. S7 (edge filter / null / spherize ablation trên data Way)
- **Data tải:** Rosetta plate đã chọn case study
- **Toán / mô hình:** So sánh transform fit \(\hat\Sigma\) pooled controls vs per-plate; metric A-P5-07
- **Deliverable:** `results/ablation_control_fit.csv`
- **Phụ thuộc:** A-P5-09
- **Không overlap với:** Role C

### A-P6-09 · Case study: một plate / perturbation (UMAP hoặc correlation heatmap)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Phần 3.4 — qualitative giống Arevalo (UMAP chỉ qualitative).
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** «UMAP panels trong Fig. 3–5 — xác nhận panel khi mở PDF» + cite Arevalo cảnh báo UMAP distortion (Methods UMAP)
- **Data tải:** Subset 1 plate Rosetta
- **Toán / mô hình:** Không — before/after batch color by batch id
- **Deliverable:** `figures/case_plate_umap.pdf` (data tự chạy) + 1 screenshot Fig. Arevalo (cite)
- **Phụ thuộc:** A-P6-07
- **Không overlap với:** Role B Fig.2-style prediction

### A-P6-10 · Xuất profile v0/v1 cho Role C (batch corrected)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** PLAN_4MONTH: profile v0 cuối T2, cập nhật v1 cuối T3.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** Không bắt buộc hình — protocol nội bộ
- **Data tải:** Output pipeline A trên LUAD (+ subset thống nhất nhóm)
- **Toán / mô hình:** Áp transform đã fit (không refit khi export nếu đã khóa model)
- **Deliverable:** `data/processed/cp_profiles_spherized_v0.parquet`, `..._v1.parquet` + changelog
- **Phụ thuộc:** A-P6-07; sync thứ Năm 20:30 (`PLAN_4MONTH.md` §4)
- **Không overlap với:** Role C fusion code

### A-P6-11 · Thảo luận Phần 3.5 — đúng hạn chế paper (Ando/Way/Arevalo)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Viết kết luận thực nghiệm: method X tốt trên subset Y; không generalize JUMP→Rosetta nếu chưa chạy.
- **Paper (PDF local):** `literature/papers/2017_Ando_TVN_Sphering.pdf` · DOI `10.1101/161422` · **Hình được phép chụp+cite:** Fig. 4 (dose-response sau TVN — minh họa sensitivity, không claim ORF Rosetta)
- **Data tải:** Kết quả CSV nhóm A
- **Toán / mô hình:** Không
- **Deliverable:** `work/role-a/draft/P6-11-thao-luan.md` (~2–3 tr)
- **Phụ thuộc:** A-P6-07
- **Không overlap với:** Role C KL fusion

---

## PHẦN VII — Mapping NCKH todos → Đồ án A (Phần 1 / 2 / 3) + slides

### A-P7-01 · Map Phần 1 đồ án (15–20 tr) ← todos nền tảng
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Đảm bảo SPLIT_PLAN D1 mục 1.1–1.5 có nguồn draft tương ứng trước cuối T1.
- **Paper (PDF local):** `literature/papers/2016_Bray_CellPainting.pdf` · DOI `10.1038/nprot.2016.105` · **Hình được phép chụp+cite:** Fig. 1–2
- **Data tải:** —
- **Toán / mô hình:** —
- **Deliverable:** Bảng map `work/role-a/MAPPING-DO-AN-A.md` (cột: SPLIT mục | Todo ID | Deliverable | ~tr)
- **Phụ thuộc:** A-P1…P4 todos
- **Không overlap với:** SPLIT_PLAN D2/D3

### A-P7-02 · Map Phần 2 đồ án (20–30 tr) ← todos phương pháp
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Khóa công thức §2.2–2.6 trước cổng tháng 2 (PLAN_4MONTH W8).
- **Paper (PDF local):** `literature/papers/2017_Ando_TVN_Sphering.pdf` · DOI `10.1101/161422` · **Hình được phép chụp+cite:** Fig. 1
- **Data tải:** —
- **Toán / mô hình:** MATH_NOTES §1–3, §5
- **Deliverable:** Cập nhật `MAPPING-DO-AN-A.md` §Phần 2; link `branch_a/*`
- **Phụ thuộc:** A-P5 todos
- **Không overlap với:** Role B Phần 2 Lasso

### A-P7-03 · Map Phần 3 đồ án (~20 tr) ← todos thực nghiệm
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Mỗi mục 3.1–3.5 SPLIT_PLAN gắn CSV/figure cụ thể.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Fig. 2 + case UMAP Fig. 3–5 (cite)
- **Data tải:** `results/*`
- **Toán / mô hình:** —
- **Deliverable:** `MAPPING-DO-AN-A.md` §Phần 3 + checklist ≥2 bảng số riêng A (SPLIT_PLAN §E)
- **Phụ thuộc:** A-P6 todos
- **Không overlap với:** Role B/C Phần 3

### A-P7-04 · Slides NCKH — slot Role A (4 tháng)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** 4–6 slide: bài toán → PP (Fig. Ando 1, Way S6, Arevalo 1) → bảng Rosetta → handoff C.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI `10.1016/j.cels.2022.10.001` · **Hình được phép chụp+cite:** Fig. 1A, Fig. S6
- **Data tải:** Figure tự chạy + screenshot PDF đã tải (quy tắc COORDINATION-MAP §5)
- **Toán / mô hình:** 1 slide công thức: MATH_NOTES §1–2 (whitening + TVN 3 bước)
- **Deliverable:** `slides/nckh-briefing/role-a/` hoặc section trong deck chung (W13 PLAN_4MONTH)
- **Phụ thuộc:** A-P6-07, A-P7-01…03
- **Không overlap với:** Slide Lasso/Fig.4 Haghighi (B/C)

### A-P7-05 · Kết luận đồ án A (3–5 tr) — draft bullet từ kết quả bảng
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Sau NCKH tháng 5 hoàn thiện; T4 chỉ cần bullet.
- **Paper (PDF local):** `literature/papers/2024_Arevalo_BatchCorrection.pdf` · DOI `10.1038/s41467-024-50613-5` · **Hình được phép chụp+cite:** Không bắt buộc
- **Data tải:** `results/table_main_benchmark_cp.md`
- **Toán / mô hình:** Không
- **Deliverable:** `work/role-a/draft/KL-outline.md`
- **Phụ thuộc:** A-P6-11
- **Không overlap với:** KL B/C

---

## PHẦN VIII — Đồng thực hiện NCKH (≤3–5 tr/slide chung, không chiếm đề A)

### A-P8-01 · Đoạn Rosetta / CP+L1000 chung nhóm (cite đồng thực hiện)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** SPLIT_PLAN §B: phần giới thiệu chung, không copy bảng số B/C.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI `10.1038/s41592-022-01667-0` · **Hình được phép chụp+cite:** «Fig. tổng quan dataset — xác nhận khi mở PDF»
- **Data tải:** Portal https://broad.io/rosetta/
- **Toán / mô hình:** Không
- **Deliverable:** 2–3 tr shared draft hoặc pointer `OUTLINE.md` §1.1 (A không viết L1000 sâu)
- **Phụ thuộc:** Kickoff W1
- **Không overlap với:** Role B/C chi tiết assay

### A-P8-02 · Review claim — checklist chống bịa (Role A)
- [ ] Trạng thái: chưa làm
- **Mục đích bước:** Rehearsal W14: không nói “SVD sphering của Ando”; không gán số Way cho Rosetta; không Lasso.
- **Paper (PDF local):** `math/MATH_NOTES.md` · **Hình:** —
- **Data tải:** —
- **Toán / mô hình:** COORDINATION-MAP §5 + OUTLINE §0
- **Deliverable:** `work/role-a/CHECKLIST-CLAIMS.md` (tick trước nộp slides)
- **Phụ thuộc:** A-P7-04
- **Không overlap với:** Checklist B/C riêng

---

*Cập nhật file này: chỉ Role A; thay `- [ ]` → `- [x]` khi xong. Ghi Nhật ký tại `work/00-COORDINATION-MAP.md` §4.*
