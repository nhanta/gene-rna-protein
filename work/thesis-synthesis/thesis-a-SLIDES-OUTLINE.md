# Outline slides Đồ án A — Sphering/TVN & batch trên Cell Painting

**Map:** `SPLIT_PLAN.md` **D1** (Phần 1 · 2 · 3 + Kết luận)  
**Nguồn NCKH:** `work/role-a/TODOS.md`  
**Lưu ý:** File HTML slides (Bio-Infras UI) **chỉ viết sau khi user duyệt outline này.**

---

## Nhóm mở đầu & định vị (5 slide)

1. **Trang bìa — Đồ án A**  
   - Todos: A-P2-02  
   - Paper: — · Fig: — · Toán: — · Data: —

2. **Mục lục luận văn A (Phần 1–2–3 + KL)**  
   - Todos: A-P7-01, A-P7-02, A-P7-03  
   - SPLIT_PLAN D1 bảng mục

3. **Câu hỏi nghiên cứu Role A — nhiễu kỹ thuật làm méo hình thái**  
   - Todos: A-P1-01, A-P2-01  
   - Paper: `2022_Way_Complementary.pdf` · Fig. 1A  
   - Toán: mô tả \(x \mapsto x'\) (A-P1-01) · Data: Rosetta CP (`data/DATA.md` §1.2)

4. **Vị trí A trong NCKH Rosetta Cellular (A / B / C)**  
   - Todos: A-P8-01, A-P1-04  
   - Paper: `2022_Haghighi_Rosetta.pdf` · Fig: overview dataset (xác nhận khi mở PDF)  
   - Ghi **đồng thực hiện**; không slide Lasso/Fig.4

5. **Phạm vi & giới hạn claim (OUTLINE §0)**  
   - Todos: A-P2-03, A-P8-02  
   - Paper: `OUTLINE.md` §0 · Toán: COORDINATION-MAP §5

---

## PHẦN 1 · Cơ bản (SPLIT 1.1–1.5) — ~16 slide

### 1.1 Nhiễu loạn & high-content profiling (2 slide)

6. **Thí nghiệm perturbation + đo hình thái high-content**  
   - Todos: A-P1-01  
   - Paper: Way · Fig. 1A (5 kênh CP)  
   - Data: ví dụ well Rosetta (inventory sau A-P6-01)

7. **Vì sao profile well-level cần hiệu chỉnh trước so sánh sinh học**  
   - Todos: A-P1-03  
   - Paper: Ando · Fig. 3A (batch trên PCA control)

### 1.2 Cell Painting — kênh, profile, control (4 slide)

8. **Assay Cell Painting — sáu stain, năm kênh fluorescence**  
   - Todos: A-P4-01  
   - Paper: `2016_Bray_CellPainting.pdf` · Fig. 1

9. **Pipeline từ ảnh → feature → profile well**  
   - Todos: A-P4-01  
   - Paper: Bray · Fig. 2  
   - Toán: trung bình theo cell trong well (Arevalo Methods wording)

10. **Compartment & loại feature (~1500/cell)**  
    - Todos: A-P4-01  
    - Paper: Bray · Fig. 2 (panel workflow)  
    - Data: đếm cột thực tế `data/inventory.md`

11. **Rosetta — nhánh CP tách đĩa với L1000 (A chỉ xử lý CP)**  
    - Todos: A-P1-02, A-P8-01  
    - Paper: Haghighi · Fig layout CP+L1000 (không Fig. 2–4)  
    - Data: subset LUAD, LINCS, CDRP, TA-ORF paths DATA.md §1.2

### 1.3 Batch / plate / well-position (4 slide)

12. **Negative control DMSO & positive control — cơ sở ước lượng nhiễu**  
    - Todos: A-P4-02  
    - Paper: Way · Fig. S3A (layout ví dụ); Bray (protocol controls)

13. **Plate position & edge wells làm lệch profile**  
    - Todos: A-P4-03  
    - Paper: Way · Fig. S5  
    - Data: diagnostic Rosetta (tự chạy A-P4-03)

14. **Batch / plate effects — từ vựng «nuisance variation»**  
    - Todos: A-P1-03  
    - Paper: Ando · Fig. 3A  
    - Toán: fit trên negative controls — MATH_NOTES §2 bước 1

15. **Glossary 5 thuật ngữ (TVN, sphering, DMSO, batch, replicate)**  
    - Todos: A-P1-03  
    - Deliverable: P1-01-bai-toan.md

### 1.4 PCA, cosine, whitening (3 slide)

16. **PCA trên embeddings control — không giảm chiều (TVN bước 1)**  
    - Todos: A-P4-04  
    - Paper: Ando · Fig. 1C–D  
    - Toán: MATH_NOTES §2

17. **Cosine similarity & ý tưởng whitening / sphering**  
    - Todos: A-P4-04, A-P5-01  
    - Toán: MATH_NOTES §1 \(z = \hat\Sigma^{-1/2}(x - \hat\mu_{\mathrm{ctrl}})\)

18. **CORAL alignment batch (TVN bước 3) — pointer Ando**  
    - Todos: A-P5-02  
    - Paper: Ando · Fig. 1 overview  
    - Toán: MATH_NOTES §2

### 1.5 Phạm vi data A — Rosetta + tuỳ chọn JUMP (3 slide)

19. **Bảng subset CP Role A (plate, control, replicate)**  
    - Todos: A-P4-05, A-P6-01  
    - Paper: Haghighi · Table overview (cite; số = inventory)  
    - Data: `aws s3 sync` DATA.md §1.2

20. **LUAD / LINCS / CDRP / TA-ORF — vai trò từng subset trong benchmark A**  
    - Todos: A-P6-02…A-P6-05  
    - Paper: Arevalo · Fig. 1 scenarios (style)

21. **JUMP Cell Painting — mở rộng Arevalo-style (*tuỳ chọn*)**  
    - Todos: A-P6-06, A-P4-05  
    - Paper: `2024_Arevalo_BatchCorrection.pdf` · Fig. 1  
    - Data: JUMP Hub — `data/inventory.md` khi tải

---

## PHẦN 2 · Phương pháp (SPLIT 2.1–2.6) — ~18 slide

### 2.1 Tiền xử lý CP (2 slide)

22. **Thứ tự pipeline: preprocess → batch correction → metric**  
    - Todos: A-P5-06, A-P1-04  
    - Paper: Arevalo · Supp Fig. 1 (preprocessing)  
    - Data: `data/processed/` DATA.md §1.3

23. **Normalize / feature selection trước batch (Arevalo spirit)**  
    - Todos: A-P5-06  
    - Deliverable: `branch_a/preprocess_cp.py`

### 2.2 Sphering / whitening trên control (4 slide)

24. **Sphering Way (ZCA-cor) — DMSO covariance → identity**  
    - Todos: A-P5-01, A-P5-03  
    - Paper: Way · Fig. S3B; Arevalo · Fig. 2 (Sphering panel)  
    - Toán: MATH_NOTES §1

25. **Giả thiết: mọi batch cần negative control (Arevalo Sphering28)**  
    - Todos: A-P5-03, A-P5-09  
    - Paper: Arevalo · discussion/limitation

26. **So sánh cách gọi Way vs Arevalo vs Moshkov**  
    - Todos: A-P5-03, A-P3-03  
    - Paper: Moshkov · Fig. 1D (cite-only workflow CNN)  
    - Toán: MATH_NOTES §1 — **A không train CNN**

27. **Implementation & unit test 1 plate**  
    - Todos: A-P5-01  
    - Data: `./data/raw/rosetta_curated` + nhãn DMSO

### 2.3 TVN — Ando 2017 (3 slide)

28. **TVN ba bước — overview**  
    - Todos: A-P5-02  
    - Paper: Ando · Fig. 1 A–D  
    - Toán: MATH_NOTES §2 (PCA → scale trục → CORAL)

29. **Ablation trục PCA (Ando Fig. 3B)**  
    - Todos: A-P5-02  
    - Paper: Ando · Fig. 3B

30. **TVN vs sphering Way — cùng interface export**  
    - Todos: A-P5-02, A-P1-04  
    - Deliverable: `branch_a/tvn.py`

### 2.4 Harmony & ComBat — so sánh (4 slide)

31. **Harmony — EM cụm đa batch (mức cao)**  
    - Todos: A-P5-04  
    - Paper: Korsunsky 2019 + SI · Fig workflow / equation block  
    - Toán: MATH_NOTES §3

32. **ComBat — batch nhân + cộng + empirical Bayes**  
    - Todos: A-P5-05  
    - Paper: Arevalo · Fig. 4–5; Johnson ComBat vignette  
    - Toán: MATH_NOTES §3

33. **Giả thiết khác Sphering: cần batch labels, không chỉ control**  
    - Todos: A-P5-04, A-P5-05, A-P2-03  
    - Paper: Arevalo §Selection

34. **Bảng phương pháp so sánh ≥3 (+ baseline identity)**  
    - Todos: A-P5-10, A-P6-07  
    - Paper: Arevalo · Fig. 2 (Baseline vs corrected)

### 2.5 Metric sinh học (4 slide)

35. **Percent replicating — định nghĩa Way**  
    - Todos: A-P5-07  
    - Paper: Way · Fig. S6, Fig. 1B (minh họa metric)  
    - Toán: MATH_NOTES §5 (percent replicating)

36. **Null percent replicating — dose, n replicate, well position**  
    - Todos: A-P5-07, A-P4-03  
    - Paper: Way Methods

37. **mAP replicate retrieval — cosine, AP, mAP**  
    - Todos: A-P5-08  
    - Paper: Arevalo · Fig. 2  
    - Toán: MATH_NOTES §5 (mAP); công thức Arevalo Methods trong todo

38. **Pipeline đánh giá Arevalo-style adapt Rosetta**  
    - Todos: A-P1-04, A-P5-08  
    - Paper: Arevalo · Fig. 1 (evaluation pipeline)

### 2.6 Giả thiết control-only & hạn chế (1 slide)

39. **Hạn chế: thiếu control/batch; DMSO mock-treatment bias**  
    - Todos: A-P5-09, A-P2-03  
    - Paper: Ando · Table 2  
    - Toán: fit chỉ trên \(\mathcal{C}\)

---

## PHẦN 3 · Thực nghiệm (SPLIT 3.1–3.5) — ~14 slide

### 3.1 Dataset & QC (2 slide)

40. **Thống kê plate / control / replicate (inventory A)**  
    - Todos: A-P6-01, A-P4-02  
    - Paper: Haghighi · Table overview (cite)  
    - Data: `results/cp_subset_stats.tex`, inventory CP section

41. **QC well-position correlation Rosetta**  
    - Todos: A-P4-03  
    - Data: figure tự chạy + Way Fig. S5 screenshot

### 3.2 Bảng benchmark chính (5 slide)

42. **Benchmark LUAD-BBBC041 — methods × metrics**  
    - Todos: A-P6-02  
    - Paper: Arevalo · Fig. 3 (style)  
    - Data: `results/luad_benchmark.csv`

43. **Benchmark LINCS-Pilot1 (compound, dose)**  
    - Todos: A-P6-03  
    - Paper: Way · Fig. 1B (định tính)  
    - Data: `results/lincs_cp_benchmark.csv`

44. **Benchmark CDRP-bio CP**  
    - Todos: A-P6-04  
    - Data: `results/cdrp_cp_benchmark.csv`

45. **TA-ORF CP — metric batch, hạn chế ORF (OUTLINE §0)**  
    - Todos: A-P6-05  
    - Paper: Rohban ORF · Fig intro  
    - Data: `results/ta_orf_cp_benchmark.csv`

46. **Bảng tổng hợp ≥3 phương pháp × 2 metric (deliverable cốt lõi)**  
    - Todos: A-P6-07  
    - Paper: Arevalo · Fig. 2  
    - Data: `results/table_main_benchmark_cp.md`, `figures/main_benchmark.png`

### 3.3 Ablation (2 slide)

47. **Ablation fit control pooled vs per-plate**  
    - Todos: A-P6-08, A-P5-09  
    - Paper: Way · Fig. S7  
    - Data: `results/ablation_control_fit.csv`

48. **Ablation bỏ 1 plate control → metric**  
    - Todos: A-P5-09  
    - Data: tự chạy Rosetta

### 3.4 Case study qualitative (2 slide)

49. **UMAP before/after batch — một plate Rosetta**  
    - Todos: A-P6-09  
    - Paper: Arevalo · UMAP panels Fig. 3–5 (cite + cảnh báo distortion Methods)  
    - Data: `figures/case_plate_umap.pdf`

50. **Heatmap correlation replicate — case perturbation**  
    - Todos: A-P6-09  
    - Data: subset 1 plate

### 3.5 Thảo luận & handoff (3 slide)

51. **Thảo luận: method X tốt subset Y; không generalize chưa chạy**  
    - Todos: A-P6-11  
    - Paper: Ando · Fig. 4 (dose-response minh họa)

52. **JUMP mở rộng — kết quả hoặc «skipped + lý do»**  
    - Todos: A-P6-06  
    - Data: `results/jump_cp_benchmark.csv` (optional)

53. **Export profile v0/v1 cho Role B & C**  
    - Todos: A-P3-02, A-P6-10  
    - Paper: Haghighi · text batch/alignment (trích, không Fig.)  
    - Data: `data/processed/cp_profiles_spherized_v0.parquet`, changelog

---

## KẾT LUẬN — ~6 slide

54. **Tóm tắt câu trả lời — batch correction trên CP Rosetta**  
    - Todos: A-P7-05, A-P6-11  
    - Data: `results/table_main_benchmark_cp.md`

55. **Đóng góp phương pháp & thực nghiệm Đồ án A**  
    - Todos: A-P2-02, A-P7-03

56. **Hạn chế (control-only, subset, UMAP qualitative)**  
    - Todos: A-P2-03, A-P5-09

57. **Không claim: cross-modal, MoA, mediation, proteinomics**  
    - Todos: A-P8-02  
    - OUTLINE §0

58. **Hướng mở rộng (JUMP, thêm metric, tích hợp profile B/C)**  
    - Todos: A-P6-06, A-P3-02

59. **Cảm ơn & Q&A — slide phụ pipeline `.mmd`**  
    - Todos: A-P1-04, A-P7-04  
    - Deliverable: `P1-04-pipeline.mmd`

---

**Tổng ~59 tiêu đề slide** · Map đầy đủ SPLIT_PLAN D1 · HTML sau duyệt.
