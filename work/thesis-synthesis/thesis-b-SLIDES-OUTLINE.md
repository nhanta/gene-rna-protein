# Outline slides Đồ án B — Dự đoán chéo CP ↔ L1000 (Haghighi baseline)

**Map:** `SPLIT_PLAN.md` **D2**  
**Nguồn NCKH:** `work/role-b/TODOS.md`  
**Lưu ý:** HTML slides ĐA **chỉ viết sau khi user duyệt outline này.**

---

## Mở đầu (5 slide)

1. **Trang bìa — Đồ án B**  
   - Todos: B-1001  
   - SPLIT_PLAN D2 tiêu đề gợi ý §C

2. **Mục lục Phần 1–2–3 + Kết luận**  
   - Todos: B PHẦN 11 map table

3. **Câu hỏi: hai assay có dự đoán chéo được không?**  
   - Todos: B-102, B-101  
   - Paper: Haghighi · Fig. 2 concept  
   - Toán: \(y \approx f(X_{\mathrm{CP}})\) — MATH_NOTES §4

4. **Vị trí B trong NCKH (shared/complementary — Application 1)**  
   - Todos: B-101, B-105  
   - Paper: Haghighi · Fig. 1 (1 slide chung — WARN trùng A/C)  
   - Không TVN deep-dive; không Fig. 4 MoA

5. **Phạm vi claim — OUTLINE §0 (TA-ORF yếu, không protein, không Way-ORF)**  
   - Todos: B-1005, B-704  
   - OUTLINE §0 · Haghighi Fig. 2b

---

## PHẦN 1 · Cơ bản (1.1–1.5) — ~15 slide

### 1.1 Gen → mRNA (mức L1000) (2 slide)

6. **Central dogma — mức giải thích cho landmark mRNA**  
   - Todos: B-1001 (§1.1)  
   - Paper: Haghighi intro wording  
   - Không claim proteomics assay

7. **Perturbation → transcriptional state trong Rosetta**  
   - Todos: B-102  
   - Paper: Haghighi · Fig. 2 setup

### 1.2 L1000 landmark ~978 (4 slide)

8. **L1000 & Connectivity Map — ý tưởng landmark**  
   - Todos: B-103  
   - Paper: `2017_Subramanian_L1000_CMap.pdf` · Fig. 1 hoặc schematic

9. **~978 landmark vs full transcriptome — phương sai ước lượng**  
   - Todos: B-103, cover §4  
   - Paper: Haghighi Methods

10. **Probe set epsilon vs CDRP-bio delta (977, overlap 785)**  
    - Todos: B-303, B-202  
    - Paper: Haghighi Methods  
    - Data: `cdrpbio_landmark_index.json`

11. **Bulk mRNA well/treatment — khớp layout perturbation Haghighi**  
    - Todos: B-301  
    - Data: aligned parquet B-301

### 1.3 Cell Painting (mức multimodal) (2 slide)

12. **CP profile mức cần cho regression — không assay sâu A**  
    - Todos: B-302, cover §4  
    - Paper: Bray · Fig. 2 (1 hình); Haghighi variable selection counts

13. **Số feature CP sau selection theo subset (601/291/63/119)**  
    - Todos: B-302  
    - Paper: Haghighi Methods  
    - Deliverable: `cp_feature_counts_by_subset.csv`

### 1.4 Shared vs complementary (4 slide)

14. **Định nghĩa shared subspace — Haghighi Application 1**  
    - Todos: B-102, B-105  
    - Paper: Haghighi · Fig. 2a–c intro

15. **Complementary — modality không predict hết**  
    - Todos: B-105  
    - Paper: Way · Fig. 1a (**compound only**)

16. **Percent predictable vs percent replicating — phân vai A/B**  
    - Todos: B-601, cover  
    - Toán: MATH_NOTES §4 vs §5 (A metric CP)

17. **Không mediation Gene→RNA→Morphology**  
    - Todos: B-705 (discussion)  
    - OUTLINE §0 · Haghighi discussion

### 1.5 Bốn subset Rosetta + TA-ORF (3 slide)

18. **Bảng inventory B — LUAD, LINCS, CDRP-bio, TA-ORF**  
    - Todos: B-202, B-204  
    - Data: `data/inventory.md` cột B · `aws s3 sync` B-201

19. **TA-ORF — ORF overexpression + CP (Rohban)**  
    - Todos: B-104  
    - Paper: Rohban · Fig. 1/workflow

20. **Kỳ vọng TA-ORF yếu — ~4,7% / 5,5% (cite Fig. 2b)**  
    - Todos: B-704, B-602  
    - Paper: Haghighi · Fig. 2b · OUTLINE §0

---

## PHẦN 2 · Phương pháp (2.1–2.6) — ~17 slide

### 2.1 Khớp ID & pretreatment (3 slide)

21. **Union perturbation ID — ma trận \(X_{\mathrm{CP}}\), \(Y_{\mathrm{GE}}\)**  
    - Todos: B-301  
    - Toán: MATH_NOTES §4  
    - Data: `{subset}_aligned.parquet`

22. **Normalized variable-selected CP profiles (Haghighi)**  
    - Todos: B-302  
    - Paper: Haghighi Methods

23. **Export khóa perturbation cho Role C (không MoA)**  
    - Todos: B-304  
    - Deliverable: `shared/perturbation_keys_{subset}.csv`

### 2.2 Lasso baseline (3 slide)

24. **Lasso CP→GE — từng landmark \(g\)**  
    - Todos: B-401  
    - Paper: Haghighi · Fig. 2a  
    - Toán: \(\min \|y-Xw\|_2^2 + \lambda\|w\|_1\) — MATH_NOTES §4

25. **Lasso GE→CP — từng feature \(f\)**  
    - Todos: B-402  
    - Paper: Haghighi · Fig. 3a

26. **Nested k-fold CV + grid-search (parity repo Haghighi)**  
    - Todos: B-106, B-401  
    - Data: GitHub 2022_Haghighi_NatureMethods

### 2.3 MLP baseline (3 slide)

27. **MLP CP→GE — feedforward**  
    - Todos: B-501  
    - Paper: Haghighi · Fig. 2a–b

28. **MLP GE→CP — số feature theo subset (caption Fig. 3a)**  
    - Todos: B-502  
    - Paper: Haghighi · Fig. 3a

29. **MLP > Lasso — động cơ paper**  
    - Todos: B-501, cover §6

### 2.4 Metrics & null (4 slide)

30. **Shuffle null — shuffle output vector across perturbations**  
    - Todos: B-403, B-503  
    - Paper: Haghighi · Fig. 2a green distribution

31. **Prediction score \(R^2\) — nested CV**  
    - Todos: B-401  
    - Toán: MATH_NOTES §4

32. **Percent predictable — 99th null + margin 0.2**  
    - Todos: B-601  
    - Paper: Haghighi · Fig. 2b · Online Methods

33. **Pipeline tổng thể B (sơ đồ tự vẽ từ Methods)**  
    - Todos: B-1002  
    - **Không** fake boxplot

### 2.5 Ridge/CCA — mở rộng nhẹ (2 slide)

34. **Ridge so với Lasso — ghi «không baseline gốc»**  
    - Todos: B-804  
    - Toán: MATH_NOTES §4 footnote

35. **Kết quả phụ LUAD — bảng ridge_vs_lasso**  
    - Todos: B-804  
    - Data: `ridge_vs_lasso_luad.csv`

### 2.6 Hai chiều CP↔GE (2 slide)

36. **CP→GE: landmark predictable**  
    - Todos: B-602, B-1002  
    - Paper: Fig. 2

37. **GE→CP: feature predictable theo category**  
    - Todos: B-604, B-1002  
    - Paper: Fig. 3b

---

## PHẦN 3 · Thực nghiệm (3.1–3.5) — ~16 slide

### 3.1 Phân bố score theo dataset (5 slide)

38. **Boxplot Lasso/MLP + shuffle — LUAD panel**  
    - Todos: B-701  
    - Paper: Haghighi · Fig. 2a LUAD · Ext Data 2–3

39. **LINCS-Pilot1 — full pipeline**  
    - Todos: B-702  
    - Paper: Fig. 2a LINCS panel  
    - Data: `work/role-b/results/lincs/`

40. **CDRP-bio — 601 features, n=977 landmarks**  
    - Todos: B-703  
    - Paper: Fig. 2a CDRP-bio

41. **TA-ORF — báo cáo yếu trung thực**  
    - Todos: B-704  
    - Paper: Fig. 2b dòng TAORF; Rohban

42. **Bảng Percent Predictable × subset × model (CP→GE)**  
    - Todos: B-602  
    - Paper: Fig. 2b đối chiếu + CSV nhóm  
    - Data: `percent_predictable_cp2ge.csv`

### 3.2 TA-ORF vs LUAD/LINCS (3 slide)

43. **So sánh side-by-side percent predictable**  
    - Todos: B-705  
    - Paper: Fig. 2a–b

44. **Thảo luận chất lượng kỹ thuật / cell line — không nhân quả**  
    - Todos: B-705, B-702

45. **Cross-dataset LINCS→LUAD (*tuỳ chọn B-706*)**  
    - Todos: B-706  
    - Paper: Ext Data Fig. 1  
    - Ghi «batch là việc A/C»

### 3.3 Gene / feature predictable (4 slide)

46. **Overlap 59 gene predictable ≥3 dataset (hướng Fig. 2c)**  
    - Todos: B-603  
    - Paper: Fig. 2c  
    - Data: `gene_overlap_predictable.csv`

47. **Top 100 predictable genes LUAD**  
    - Todos: B-801  
    - Paper: Ext Data Fig. 2

48. **ORA GO — Ext Data Fig. 3**  
    - Todos: B-802  
    - Paper: Ext Data Fig. 3

49. **Exploratory gene ↔ CP feature (notebook)**  
    - Todos: B-803  
    - Paper: Fig. 3c (screenshot nếu chưa chạy)

### 3.4 CP sau batch Role A (3 slide)

50. **Nhận profile post-A — provenance**  
    - Todos: B-901  
    - Paper: Haghighi text batch/alignment  
    - Data: `shared/cp_profiles_post_batch_{subset}.parquet`  
    - Toán: đọc MATH_NOTES §1–3 only

51. **Δ percent predictable — CP gốc vs post-A**  
    - Todos: B-902  
    - Data: `batch_ablation_percent_predictable.csv`

52. **Liên hệ C protocol alignment (B cung metric, C orchestrate)**  
    - Todos: B-902, C-P2-ALIGN-01 (cross-ref)

### 3.5 Hạn chế (1 slide)

53. **Landmark, timepoint khác nhau; không map 1–1 gen–hình**  
    - Todos: B-1003, B-1005  
    - Haghighi limitations

---

## KẾT LUẬN — ~6 slide

54. **Tóm tắt — subset nào predictable, TA-ORF expected weak**  
    - Todos: B-705, B-1003

55. **Đóng góp tái lập Lasso/MLP + phân tích gene/feature**  
    - Todos: B-1002, B-603

56. **Ảnh hưởng batch A — kết quả B-902**  
    - Todos: B-902

57. **Hạn chế & không claim MoA / sphering owner / JUMP benchmark**  
    - Todos: B-101, B-1005

58. **Screenshots bắt buộc PHẦN 12 checklist**  
    - Todos: B PHẦN 12 (Fig. 2a–c, 3a–b, Ext Data)

59. **Cảm ơn — slides NCKH nhánh B (B-1004)**  
    - Deliverable: `slides/nckh-briefing/role_b_*`

---

**Tổng ~59 tiêu đề slide** · SPLIT_PLAN D2 · HTML sau duyệt.
