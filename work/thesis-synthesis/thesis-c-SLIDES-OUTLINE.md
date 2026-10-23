# Outline slides Đồ án C — Fusion MoA & alignment sau batch (A→B)

**Map:** `SPLIT_PLAN.md` **D3**  
**Nguồn NCKH:** `work/role-c/TODOS.md`  
**Lưu ý:** HTML slides ĐA **chỉ viết sau khi user duyệt outline này.**

---

## Mở đầu (5 slide)

1. **Trang bìa — Đồ án C**  
   - Todos: C-P3-THESIS-01  
   - SPLIT_PLAN D3 tiêu đề §C

2. **Mục lục Phần 1–2–3 + KL**  
   - Todos: C §7 map table

3. **Hai câu hỏi C: MoA fusion & batch→alignment**  
   - Todos: C-P1-01, header §1  
   - Paper: Haghighi · Fig. 4 + text batch/alignment

4. **Shared vs complementary — góc fusion (không Lasso owner)**  
   - Todos: C-P1-01, C-P1-02  
   - Paper: Haghighi intro; Way compound  
   - Toán: MATH_NOTES §6

5. **Phạm vi cấm: TA-ORF MoA, TVN proof, mediation trụ**  
   - Todos: C-GUARD-01, C-GUARD-02  
   - OUTLINE §0 · MATH_NOTES §8

---

## PHẦN 1 · Cơ bản (1.1–1.5) — ~14 slide

### 1.1 Vì sao multimodal profiling (2 slide)

6. **Drug discovery & phenotypic screening — động cơ**  
   - Todos: C-P1-03  
   - Paper: Haghighi intro

7. **Rosetta — cặp CP + L1000 cùng perturbation layout**  
   - Todos: C-P1-03  
   - Paper: Haghighi · Fig overview (WARN trùng A/B — 1 slide)

### 1.2 Complementary subspace & fusion (3 slide)

8. **Thông tin chung vs bổ sung — wording Haghighi**  
   - Todos: C-P1-01  
   - Paper: Haghighi Application 2 intro

9. **Way 2022 complementary trên compound A549**  
   - Todos: C-P1-02  
   - Paper: `2022_Way_Complementary.pdf` · Fig complementary/spherize (xác nhận PDF)  
   - **Không** gán MoA Way; **không** ORF

10. **Operational complementary — residual không predict (*không mediation*)**  
    - Todos: header §3, C-GUARD-02  
    - MATH_NOTES §8

### 1.3 MoA từ profile (3 slide)

11. **Mechanism of Action — retrieval vs classification**  
    - Todos: C-P1-03  
    - Paper: Haghighi MoA section

12. **Fig. 4 setup — chỉ CDRP-bio & LINCS compound**  
    - Todos: C-P1-01, C-P2-MOA-01  
    - Paper: Haghighi · Fig. 4a–c

13. **Nhãn MoA imperfect — hạn chế sẽ trả lời §3.5**  
    - Todos: C-P3-MOA-02  
    - OUTLINE §0 item 5

### 1.4 Batch phá alignment multimodal (3 slide)

14. **Batch/plate trên CP và hệ quả so sánh đa modal**  
    - Todos: C-P1-04  
    - Paper: Haghighi batch quote; Way plate effects

15. **Gợi ý paper: batch correction có thể cải thiện alignment**  
    - Todos: C-P1-04, C-P2-ALIGN-03  
    - Paper: Haghighi discussion (text)

16. **Spherize DMSO — ngữ cảnh Way (Role A implement)**  
    - Todos: C-P1-02  
    - Toán: tham chiếu MATH_NOTES §1 — **C không code TVN**

### 1.5 Pipeline nhóm A / B / C (3 slide)

17. **Sơ đồ A: CP batch → export version**  
    - Todos: C-P1-04 · cross-ref A-P6-10

18. **Sơ đồ B: Lasso/MLP metric API**  
    - Todos: C-P2-ALIGN-01 · cross-ref B-601

19. **Sơ đồ C: MoA fusion + orchestrate alignment**  
    - Todos: C-NCKH-02, C-P2-ALIGN-05  
    - Deliverable: `code/c/main.py`

---

## PHẦN 2 · Phương pháp (2.1–2.6) — ~18 slide

### 2.1 Unsupervised MoA / Jaccard (4 slide)

20. **Inventory compound + nhãn MoA CDRP-bio / LINCS**  
    - Todos: C-P2-MOA-01  
    - Data: `aws s3 sync` DATA.md · `work/role-c/data/moa_inventory.md`

21. **Clustering MoA — không gian CP, GE, tích hợp**  
    - Todos: C-P2-MOA-02  
    - Paper: Fig. 4a

22. **Jaccard index vs ground-truth MoA clusters**  
    - Todos: C-P2-MOA-02  
    - Toán: MATH_NOTES §6

23. **Figure style Fig. 4a — số liệu nhóm tự chạy**  
    - Todos: C-P2-MOA-02  
    - Data: `results/c/moa_unsupervised_jaccard.csv`, `fig4a_style.png`

### 2.2 Supervised fusion (5 slide)

24. **Baseline CP-only vs GE-only (logistic / MLP, k=5 CV)**  
    - Todos: C-P2-MOA-03  
    - Paper: Fig. 4b

25. **Early fusion — concat \([x_{\mathrm{CP}}; x_{\mathrm{GE}}]\)**  
    - Todos: C-P2-MOA-04  
    - Toán: MATH_NOTES §6

26. **Late fusion — mean probability**  
    - Todos: C-P2-MOA-04  
    - Paper: Fig. 4b

27. **RGCCA + RGCCA_EarlyFusion**  
    - Todos: C-P2-MOA-05  
    - Paper: Fig. 4a–b · cite RGCCA ref trong Haghighi

28. **Draft luận văn §2.1–2.2 — screenshot Fig. 4 có caption**  
    - Todos: C-P2-MOA-07  
    - Deliverable: `thesis/c/part2_2.1-2.2.docx`

### 2.3 Protocol A → B (4 slide)

29. **API metric B — input CP path, L1000, cp_version**  
    - Todos: C-P2-ALIGN-01  
    - Paper: Fig. 2b (cite metric only)  
    - Deliverable: `shared/b_metrics_api.md`  
    - Toán: MATH_NOTES §4 read-only

30. **Subsets protocol: LUAD, LINCS, ± CDRP-bio — không TA-ORF MoA**  
    - Todos: C-P2-ALIGN-02  
    - Data: `work/role-c/protocol/subsets.yaml`

31. **Baseline alignment — CP v0 (trước batch A)**  
    - Todos: C-P2-ALIGN-03  
    - Data: `results/c/alignment_before_batch.csv`

32. **Sau batch — CP version A (metadata method, fit-on-control)**  
    - Todos: C-P2-ALIGN-04  
    - Data: `data/processed/cp_vA/` · log `cp_version_log.md` (C-COORD-01)

### 2.4 Metric thống nhất (2 slide)

33. **Δ percent predictable — định nghĩa cột trước/sau**  
    - Todos: C-P2-ALIGN-05  
    - Toán: MATH_NOTES §6 protocol paragraph

34. **Bootstrap / CI (*nếu có*) — method ngắn**  
    - Todos: C-P2-ALIGN-05

### 2.5 Simulation (*mở rộng tuỳ chọn*) (2 slide)

35. **Thiết kế planted batch + biology — MATH_NOTES §7**  
    - Todos: C-P2-SIM-01  
    - Nhãn **mở rộng phương pháp luận**

36. **Recovery curves sphering/ComBat trên synthetic**  
    - Todos: C-P2-SIM-02  
    - Data: `results/c/sim_recovery.png`

### 2.6 Không mediation PP chính (1 slide)

37. **§2.6 — giới hạn nhân quả, timepoint, two-way**  
    - Todos: C-GUARD-02  
    - Paper: Haghighi discussion  
    - MATH_NOTES §8

---

## PHẦN 3 · Thực nghiệm (3.1–3.5) — ~15 slide

### 3.1 Fusion vs single-modality (6 slide)

38. **CDRP-bio — Jaccard unsupervised (CP vs GE vs RGCCA)**  
    - Todos: C-P2-MOA-02, C-P3-MOA-01  
    - Paper: Fig. 4a

39. **LINCS — unsupervised MoA (~57 class context)**  
    - Todos: C-P2-MOA-02  
    - Paper: Fig. 4a caption context

40. **Supervised weighted F1 / accuracy — single modality**  
    - Todos: C-P2-MOA-03  
    - Data: `moa_supervised_single_modality.csv`

41. **Early vs late fusion — bảng số**  
    - Todos: C-P2-MOA-04  
    - Data: `moa_supervised_fusion_early_late.csv`

42. **RGCCA results — so CP-only**  
    - Todos: C-P2-MOA-05  
    - Data: `moa_rgcca.csv`

43. **Master table modality × method × dataset (§3.1)**  
    - Todos: C-P3-MOA-01  
    - Data: `moa_master_table.csv` · `part3_3.1_tables.docx`

### 3.2 Batch → percent predictable (3 slide)

44. **Bảng trước/sau batch — LUAD ưu tiên**  
    - Todos: C-P2-ALIGN-05  
    - Data: merge alignment_before/after CSV

45. **LINCS — cùng protocol**  
    - Todos: C-P2-ALIGN-02, C-P2-ALIGN-05

46. **Slide NCKH batch→alignment (không copy bảng Fig. 2b thuần của B)**  
    - Todos: C-P2-ALIGN-05, C-NCKH-01  
    - Deliverable: `slides/nckh/c02_batch_alignment.pptx`

### 3.3 Simulation (*nếu có*) (1 slide)

47. **§3.3 recovery — chỉ mở rộng, không NCKH claim chính**  
    - Todos: C-P2-SIM-02  
    - Data: `part3_3.3_optional.docx`

### 3.4 Fusion không luôn thắng (2 slide)

48. **Class-wise F1 — Fig. 4c style**  
    - Todos: C-P2-MOA-06  
    - Paper: Fig. 4c  
    - Data: `moa_class_f1.png`

49. **Thảo luận — integrated vs modality mạnh hơn từng class**  
    - Todos: C-P2-MOA-06  
    - Deliverable: `part3_3.4_discussion.docx`

### 3.5 Hạn chế (2 slide)

50. **MoA labels imperfect; không suy ORF từ compound**  
    - Todos: C-P3-MOA-02  
    - OUTLINE §0

51. **TA-ORF — chỉ số cross-modal từ B (~5%), không MoA C**  
    - Todos: header §5, C-P3-MOA-02  
    - Cross-ref B-704

---

## KẾT LUẬN & NCKH — ~8 slide

52. **Tóm tắt MoA fusion — hướng Haghighi Fig. 4**  
    - Todos: C-P3-THESIS-01, C-P3-MOA-01

53. **Tóm tắt batch→alignment — câu trả lời protocol A→B**  
    - Todos: C-P2-ALIGN-05

54. **Đóng góp pipeline C & demo reproducible**  
    - Todos: C-NCKH-02  
    - Data: `code/c/README.md`

55. **Checklist guard C-GUARD-01 — tick trước T4**  
    - Todos: C-GUARD-01  
    - Deliverable: `checklist_guard.md`

56. **Hạn chế & không claim mediation / Lasso owner / TVN**  
    - Todos: C-GUARD-02, C-P3-MOA-02

57. **Slides NCKH block C (5–8 slide) — complementary + 2 bảng**  
    - Todos: C-NCKH-01  
    - Paper screenshots: Fig. 4, Fig. 2b (metric cite), Way 1 slide

58. **Cảm ơn & Q&A — nhật ký phối hợp cp_version**  
    - Todos: C-COORD-01  
    - COORDINATION-MAP §4

---

**Tổng ~58 tiêu đề slide** · SPLIT_PLAN D3 · HTML sau duyệt.
