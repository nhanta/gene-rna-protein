# Role C — Planner todos (Rosetta Cellular NCKH)

**Khóa sở hữu:** fusion MoA trên **compound** (CDRP-bio / LINCS); protocol đo lại **percent predictable** sau CP đã batch/sphering (A); khung **complementary** (Haghighi + Way compound).  
**Tham chiếu bus:** [`work/00-COORDINATION-MAP.md`](../00-COORDINATION-MAP.md) · [`OUTLINE.md`](../../OUTLINE.md) §0 · [`SPLIT_PLAN.md`](../../SPLIT_PLAN.md) Đồ án C · [`math/MATH_NOTES.md`](../../math/MATH_NOTES.md) §6–7 · [`data/DATA.md`](../../data/DATA.md)

---

## 1. Bài toán (complementary / fusion)

Hai readout Rosetta — **Cell Painting (morphology)** và **L1000 (landmark mRNA)** — mang thông tin **chung (shared)** và **bổ sung (complementary)** (Haghighi). Bài toán Role C:

1. **Ứng dụng compound:** ghép multimodal có cải thiện **MoA retrieval / classification** so với từng modality một không? (Haghighi Application 2, Fig. 4 — chỉ CDRP-bio & LINCS).
2. **Alignment sau batch:** sau khi A chỉnh batch/sphering trên CP, **percent predictable** cross-modal (metric của B) có tăng theo hướng Haghighi gợi ý (*batch effect corrections to improve alignment*) không?

**Không thuộc C:** MoA fusion trên **TA-ORF** (paper không có nhãn MoA Fig. 4); viết lại chứng minh TVN/SVD (A); triển khai Lasso/MLP đầy đủ (B).

---

## 2. Mục đích

| Mục tiêu | Đo lường thành công |
|----------|---------------------|
| Tái lập hướng **Fig. 4** trên subset compound Rosetta | Bảng Jaccard (unsupervised) + weighted F1/accuracy (supervised); so CP-only, GE-only, early/late fusion, RGCCA+early |
| Kiểm tra **A → B** trên cùng subset LUAD/LINCS (± CDRP-bio nếu B đã chạy) | Bảng percent predictable **trước/sau** profile CP version từ A |
| Luận văn C đủ **Phần 1–2–3** | Theo [`SPLIT_PLAN.md`](../../SPLIT_PLAN.md) D3 |
| Slides NCKH nhóm (T4) | 5–8 slide C: complementary + MoA + một bảng batch→alignment |

---

## 3. Ứng dụng MoA multimodal (Haghighi / Way)

- **Haghighi Fig. 4:** MoA unsupervised (Jaccard vs cluster ground truth) và supervised (logistic / MLP; early, late, RGCCA_EarlyFusion) trên **CDRP-bio** (n≈16 MoA class boxplot) và **LINCS** (n≈57).
- **Way 2022:** Khung **complementary** và **spherize DMSO** trên **compound** (1.327 compound A549) — dùng cho **slide/lý thuyết Phần 1**, **không** gán kết quả Way sang ORF/TA-ORF; **không** dùng Way làm claim MoA chính (Way không phải paper fusion CP×L1000 MoA).
- **Operational complementary (mở rộng nhẹ, không mediation):** phân tích residual không predict được = góc *complementary subspace* (Haghighi wording) — **không** đặt tên mediation nhân quả Gene→RNA→Morphology làm kết luận NCKH.

---

## 4. Phương pháp (mức paper + protocol nhóm)

| Phương pháp | Mô tả ngắn | Nguồn |
|-------------|------------|--------|
| Single modality | CP hoặc L1000 riêng | Haghighi Fig. 4 |
| **Early fusion** | Nối vector feature hai modality | Haghighi Fig. 4b |
| **Late fusion** | Trung bình xác suất lớp từ classifier từng modality | Haghighi Fig. 4b |
| **RGCCA** | Regularized GCCA → early fusion trong không gian tích hợp | Haghighi Fig. 4a–b; MATH_NOTES §6 |
| **Protocol alignment** | CP `version_A` (sphering/batch) → gọi **API metric B** (percent predictable, không re-implement Lasso/MLP) | Haghighi đoạn batch/alignment; MATH_NOTES §6 |

---

## 5. Thực nghiệm MoA — **chỉ compound**

| Dataset Rosetta | MoA fusion (C) | Cross-modal re-run sau batch (C orchestrate, B metric) |
|-----------------|----------------|--------------------------------------------------------|
| **CDRP-bio** | ✓ (Fig. 4) | Tuỳ B (compound, alignment yếu hơn LUAD/LINCS — báo cáo trung thực) |
| **LINCS-Pilot1** | ✓ (Fig. 4) | ✓ ưu tiên (A549, khớp narrative Haghighi) |
| **LUAD** | ✗ (không Fig. 4 MoA) | ✓ ưu tiên cho bảng batch→predictable |
| **TA-ORF** | ✗ **cấm** MoA fusion (không nhãn MoA paper) | Chỉ nhận số từ B để **đối chiếu** độ khó cross-modal (~5% predictable) |

Lọc chất lượng replicate: bám mô tả Haghighi Methods (>90th percentile null) khi tái lập — nếu compute hạn chế, ghi rõ **subset rút gọn** trong caption bảng.

---

## 6. Simulation (*chỉ mở rộng luận văn — không NCKH claim chính*)

Planted batch + planted biology; đo recovery sau sphering/ComBat — xem MATH_NOTES §7. Gắn nhãn **mở rộng phương pháp luận**; không viết như Haghighi/Way đã làm.

---

## 7. Ánh xạ todos → Đồ án C (SPLIT_PLAN D3)

| Khối todos C | Phần 1 (15–20 tr) | Phần 2 (20–30 tr) | Phần 3 (~20 tr) |
|--------------|-------------------|-------------------|-----------------|
| C-P1-* | 1.1–1.5 | — | — |
| C-P2-MOA-* | — | 2.1–2.2 | 3.1, 3.4 |
| C-P2-ALIGN-* | 1.4–1.5 | 2.3–2.4 | 3.2 |
| C-P2-SIM-* (*tuỳ*) | — | 2.5 | 3.3 |
| C-NCKH-* | slide intro | slide methods | slide kết quả |
| C-GUARD-* | 2.6 | — | 3.5 |

---

# LARGE PART A — Nền tảng & Phần 1 đồ án

### C-P1-01 · Đọc Haghighi Application 2 + Fig. 4 (MoA)
- [ ] Trạng thái
- **Mục đích bước:** Chốt setup unsupervised/supervised MoA, metric, và phạm vi **chỉ compound**.
- **Paper (PDF local):** `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI 10.1038/s41592-022-01667-0 · **Hình được phép chụp+cite:** Fig. 4a–c (MoA retrieval + classification + class F1)
- **Data tải:** không (đọc trước khi sync data)
- **Toán / mô hình:** Jaccard vs MoA clusters; weighted F1/accuracy; early / late / RGCCA — xem MATH_NOTES §6
- **Deliverable:** `work/role-c/notes/haghighi-fig4-summary.md` (bullet setup + hạn chế MoA labels)
- **Phụ thuộc:** không
- **Không overlap với:** Role B (Fig. 2–3 Lasso/MLP); Role A (TVN proof)

### C-P1-02 · Đọc Way complementary (compound only)
- [ ] Trạng thái
- **Mục đích bước:** Lấy định nghĩa complementary và spherize DMSO cho **Phần 1** — không mượn số MoA Way làm kết quả C.
- **Paper (PDF local):** `literature/papers/2022_Way_Complementary.pdf` · DOI 10.1016/j.cels.2022.10.001 · **Hình được phép chụp+cite:** Fig. chính complementary / spherize (ghi số hình sau khi mở PDF)
- **Data tải:** không
- **Toán / mô hình:** percent replicating; spherize trên control — tham chiếu Way Methods, không derive lại
- **Deliverable:** 1 slide outline `slides/nckh/c01_complementary_way_haghighi.pptx` (draft bullet)
- **Phụ thuộc:** C-P1-01
- **Không overlap với:** Role B (cross-predict chính); claim Way trên ORF

### C-P1-03 · Draft luận văn §1.1–1.3 (multimodal & MoA drug)
- [ ] Trạng thái
- **Mục đích bước:** Viết Phần 1 mục multimodal profiling và bài toán MoA từ profile.
- **Paper (PDF local):** Haghighi intro + MoA section; Way intro · **Hình:** Fig. 4 (cite) nếu minh họa bài toán
- **Data tải:** không
- **Toán / mô hình:** mô tả khái niệm MoA retrieval vs classification (không công thức mediation)
- **Deliverable:** `thesis/c/part1_1.1-1.3.docx` (~8–10 tr hướng SPLIT_PLAN D3)
- **Phụ thuộc:** C-P1-01, C-P1-02
- **Không overlap với:** Role A (batch benchmark JUMP); Role B (L1000 landmark chi tiết §1.2 B)

### C-P1-04 · Draft luận văn §1.4–1.5 (batch & pipeline A/B/C)
- [ ] Trạng thái
- **Mục đích bước:** Giải thích vì sao batch có thể phá alignment multimodal và vai trò nhánh A/B trong pipeline C.
- **Paper (PDF local):** Haghighi (đoạn batch/alignment); Way plate effects · **Hình:** không bắt buộc
- **Data tải:** không
- **Toán / mô hình:** protocol A→B ở mức lời (chi tiết ở C-P2-ALIGN-*)
- **Deliverable:** `thesis/c/part1_1.4-1.5.docx`
- **Phụ thuộc:** đọc `OUTLINE.md` §2–3; S-03 schema
- **Không overlap với:** Role A viết chi tiết TVN/Harmony; Role B viết Lasso/MLP

---

# LARGE PART B — Phương pháp MoA fusion (Phần 2.1–2.2)

### C-P2-MOA-01 · Inventory compound + nhãn MoA CDRP-bio / LINCS
- [ ] Trạng thái
- **Mục đích bước:** Xác nhận file curated, cột MoA, số class, intersection landmark CDRP vs epsilon probe set.
- **Paper (PDF local):** `2022_Haghighi_Rosetta.pdf` · Methods L1000 probe sets · **Hình:** không
- **Data tải:** `aws s3 sync --no-sign-request s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data ./data/raw/rosetta_curated` (xem `data/DATA.md` §1.2); thư mục `LINCS-Pilot1/`, `CDRP-.../CDRPBIO-...`
- **Toán / mô hình:** ghi n=785 overlap landmark khi gộp CDRP với dataset khác (Haghighi Methods)
- **Deliverable:** `work/role-c/data/moa_inventory.md` (số compound, dose, class MoA, filter replicate)
- **Phụ thuộc:** S-02
- **Không overlap với:** Role B inventory TA-ORF cross-modal

### C-P2-MOA-02 · Pipeline unsupervised MoA clustering + Jaccard
- [ ] Trạng thái
- **Mục đích bước:** Tái lập task Fig. 4a: cluster theo MoA trong không gian CP, GE, và tích hợp.
- **Paper (PDF local):** Haghighi · **Hình được phép chụp+cite:** Fig. 4a
- **Data tải:** curated Rosetta compound paths từ C-P2-MOA-01
- **Toán / mô hình:** Jaccard index per MoA class vs ground-truth clusters; RGCCA so với CP-only — MATH_NOTES §6
- **Deliverable:** `results/c/moa_unsupervised_jaccard.csv` + figure `results/c/fig4a_style.png` (số liệu nhóm tự chạy)
- **Phụ thuộc:** C-P2-MOA-01
- **Không overlap với:** Role A (clustering batch QC trên JUMP)

### C-P2-MOA-03 · Baseline supervised single-modality (CP vs GE)
- [ ] Trạng thái
- **Mục đích bước:** Logistic + MLP MoA trên CP-only và GE-only (k=5 CV) trước khi fusion.
- **Paper (PDF local):** Haghighi Fig. 4b · **Hình:** Fig. 4b (so sánh hướng)
- **Data tải:** cùng C-P2-MOA-01
- **Toán / mô hình:** weighted F1 / accuracy; filtered compound subset như paper hoặc ghi rõ rút gọn
- **Deliverable:** `results/c/moa_supervised_single_modality.csv`
- **Phụ thuộc:** C-P2-MOA-01
- **Không overlap với:** Role B (Lasso/MLP **cross-modal** landmark/feature — khác task MoA class)

### C-P2-MOA-04 · Early fusion + late fusion MoA
- [ ] Trạng thái
- **Mục đích bước:** Concat feature (early) và trung bình prob (late) như Haghighi Fig. 4b.
- **Paper (PDF local):** Haghighi Fig. 4b · **Hình:** Fig. 4b
- **Data tải:** curated compound
- **Toán / mô hình:** early = `[x_CP; x_GE]`; late = mean(p_CP, p_GE) — MATH_NOTES §6
- **Deliverable:** `results/c/moa_supervised_fusion_early_late.csv`
- **Phụ thuộc:** C-P2-MOA-03
- **Không overlap với:** Role B owns regression CP↔GE

### C-P2-MOA-05 · RGCCA + early fusion trong không gian RGCCA
- [ ] Trạng thái
- **Mục đích bước:** Tích hợp RGCCA (unsupervised + supervised RGCCA_EarlyFusion) — claim chính unsupervised: RGCCA vượt CP-only trên Jaccard nếu khớp hướng paper.
- **Paper (PDF local):** Haghighi Fig. 4a–b · cite RGCCA ref trong Haghighi · **Hình:** Fig. 4a–b
- **Data tải:** curated compound
- **Toán / mô hình:** Regularized GCCA (mức tái lập paper, không chứng minh lý thuyết GCCA dài)
- **Deliverable:** `code/c/moa_rgcca.py` (hoặc notebook) + `results/c/moa_rgcca.csv`
- **Phụ thuộc:** C-P2-MOA-02, C-P2-MOA-04
- **Không overlap với:** Role A SVD/TVN implementation

### C-P2-MOA-06 · MoA class-wise F1 (Fig. 4c style)
- [ ] Trạng thái
- **Mục đích bước:** Báo cáo fusion **không luôn thắng** từng class — đúng thảo luận Haghighi.
- **Paper (PDF local):** Haghighi Fig. 4c · **Hình:** Fig. 4c
- **Data tải:** kết quả C-P2-MOA-04/05
- **Toán / mô hình:** F1 theo MoA class; so integrated vs modality mạnh hơn
- **Deliverable:** heatmap/bar `results/c/moa_class_f1.png` + đoạn `thesis/c/part3_3.4_discussion.docx`
- **Phụ thuộc:** C-P2-MOA-04
- **Không overlap với:** không

### C-P2-MOA-07 · Draft luận văn §2.1–2.2 (MoA methods)
- [ ] Trạng thái
- **Mục đích bước:** Viết Phần 2 unsupervised + supervised fusion ở mức paper.
- **Paper (PDF local):** Haghighi Fig. 4 · **Hình:** screenshot Fig. 4 có caption cite
- **Data tải:** không
- **Toán / mô hình:** MATH_NOTES §6 (early, late, RGCCA)
- **Deliverable:** `thesis/c/part2_2.1-2.2.docx`
- **Phụ thuộc:** C-P2-MOA-02 … C-P2-MOA-05 (concept; có thể draft song song T2)
- **Không overlap với:** Role B §2.2–2.3 Lasso/MLP

---

# LARGE PART C — Protocol alignment A → B (Phần 2.3–2.4, 3.2)

### C-P2-ALIGN-01 · Thỏa thuận API metric với Role B
- [ ] Trạng thái
- **Mục đích bước:** Định nghĩa hàm/CLI **chỉ đọc** percent predictable & prediction score trên cặp profile CP+L1000 — C không sở hữu Lasso/MLP training code.
- **Paper (PDF local):** Haghighi Fig. 2b (metric percent predictable) · **Hình:** Fig. 2b (cite khi mô tả API)
- **Data tải:** không
- **Toán / mô hình:** percent predictable, shuffle null — MATH_NOTES §4 (đọc, không implement)
- **Deliverable:** `shared/b_metrics_api.md` (input: path CP, path L1000, `cp_version`, subset name; output: JSON/CSV metrics)
- **Phụ thuộc:** S-03; Role B cam kết endpoint (branch B)
- **Không overlap với:** Role B owns `code/b/lasso_mlp_*`

### C-P2-ALIGN-02 · Bảng subset cho protocol (LUAD, LINCS, ± CDRP-bio)
- [ ] Trạng thái
- **Mục đích bước:** Chốt subset và chiều CP→GE / GE→CP cần gọi API — **không** thêm TA-ORF vào claim MoA.
- **Paper (PDF local):** Haghighi Table/Fig. 2b percent predictable · **Hình:** Fig. 2b
- **Data tải:** curated LUAD, LINCS (và CDRP-bio nếu B sẵn sàng)
- **Toán / mô hình:** cùng định nghĩa predictable như B (ngưỡng score paper)
- **Deliverable:** `work/role-c/protocol/subsets.yaml`
- **Phụ thuộc:** C-P2-ALIGN-01
- **Không overlap với:** Role B chọn gene lists chi tiết Fig. 2d

### C-P2-ALIGN-03 · Baseline metrics trước batch (v0 CP)
- [ ] Trạng thái
- **Mục đích bước:** Gọi API B trên CP gốc (chưa A) làm cột “trước”.
- **Paper (PDF local):** Haghighi (gợi ý batch/alignment) · **Hình:** không
- **Data tải:** Rosetta curated; CP v0 từ loader chung
- **Toán / mô hình:** Δ percent predictable định nghĩa ở C-P2-ALIGN-05
- **Deliverable:** `results/c/alignment_before_batch.csv`
- **Phụ thuộc:** C-P2-ALIGN-01, C-P2-ALIGN-02; B baseline chạy xong (B todos)
- **Không overlap với:** Role B không fusion MoA

### C-P2-ALIGN-04 · Metrics sau CP version A (sphering/batch)
- [ ] Trạng thái
- **Mục đích bước:** Nhận `cp_profile_vA` từ A (metadata: method, fit-on-control); gọi lại API B.
- **Paper (PDF local):** Haghighi batch suggestion; Way spherize (ngữ cảnh) · **Hình:** không
- **Data tải:** `data/processed/cp_vA/` do A publish (path + changelog)
- **Toán / mô hình:** cùng model B, chỉ đổi input CP — MATH_NOTES §6 protocol
- **Deliverable:** `results/c/alignment_after_batch.csv`
- **Phụ thuộc:** Role A deliver profile vA ( cổng T3 ); C-P2-ALIGN-03
- **Không overlap với:** Role A owns sphering code

### C-P2-ALIGN-05 · Bảng tổng hợp trước/sau + slide NCKH
- [ ] Trạng thái
- **Mục đích bước:** Trả lời câu hỏi đồ án C: batch A có cải thiện alignment cross-modal không?
- **Paper (PDF local):** Haghighi (không bảng sẵn — claim **nhóm tự chạy**) · **Hình:** không generate số giả
- **Data tải:** merge C-P2-ALIGN-03/04
- **Toán / mô hình:** Δ predictable; CI/bootstrap nếu có — ghi method ngắn
- **Deliverable:** `results/c/table_batch_to_crossmodal.tex` + slide `slides/nckh/c02_batch_alignment.pptx`
- **Phụ thuộc:** C-P2-ALIGN-04
- **Không overlap với:** Role B bảng tái lập Fig. 2 thuần (không batch)

### C-P2-ALIGN-06 · Draft luận văn §2.3–2.4 + §3.2
- [ ] Trạng thái
- **Mục đích bước:** Mô tả protocol và metric thống nhất A/B/C.
- **Paper (PDF local):** Haghighi alignment quote · **Hình:** optional pipeline diagram (tự vẽ sơ đồ, không fake data)
- **Data tải:** không
- **Toán / mô hình:** MATH_NOTES §6 protocol paragraph
- **Deliverable:** `thesis/c/part2_2.3-2.4.docx`, `thesis/c/part3_3.2.docx`
- **Phụ thuộc:** C-P2-ALIGN-05
- **Không overlap với:** Role A §2.2–2.4 batch methods

---

# LARGE PART D — Phần 3 thực nghiệm MoA + kết luận

### C-P3-MOA-01 · Bảng tổng hợp fusion vs single-modality (CDRP-bio + LINCS)
- [ ] Trạng thái
- **Mục đích bước:** Một bảng luận văn §3.1 đủ modality × method × dataset.
- **Paper (PDF local):** Haghighi Fig. 4 · **Hình:** Fig. 4 (cite); figure nhóm tự chạy
- **Data tải:** aggregate C-P2-MOA-02…06
- **Toán / mô hình:** Jaccard + weighted F1/accuracy
- **Deliverable:** `thesis/c/part3_3.1_tables.docx` + `results/c/moa_master_table.csv`
- **Phụ thuộc:** C-P2-MOA-06
- **Không overlap với:** B master cross-modal table

### C-P3-MOA-02 · Thảo luận hạn chế §3.5 (labels, compound vs ORF)
- [ ] Trạng thái
- **Mục đích bước:** Ghi rõ MoA labels imperfect; không suy MoA ORF từ compound; TA-ORF chỉ cross-modal B.
- **Paper (PDF local):** Haghighi limitations; OUTLINE §0 · **Hình:** không
- **Data tải:** không
- **Toán / mô hình:** không mediation — MATH_NOTES §8
- **Deliverable:** `thesis/c/part3_3.5.docx`
- **Phụ thuộc:** C-P3-MOA-01
- **Không overlap với:** Role B TA-ORF experiment narrative

### C-P3-THESIS-01 · Kết luận C (3–5 tr)
- [ ] Trạng thái
- **Mục đích bước:** Tóm complementary/fusion + batch→alignment; nhắc không claim mediation.
- **Paper (PDF local):** Haghighi · **Hình:** không
- **Data tải:** không
- **Toán / mô hình:** không
- **Deliverable:** `thesis/c/conclusion.docx`
- **Phụ thuộc:** C-P3-MOA-01, C-P2-ALIGN-05
- **Không overlap với:** KL A/B

---

# LARGE PART E — Simulation (*mở rộng — tùy chọn sau M3*)

### C-P2-SIM-01 · Thiết kế planted batch + signal (MATH_NOTES §7)
- [ ] Trạng thái
- **Mục đích bước:** Mô phỏng đánh giá khi nào sphering giúp recovery — **không** slide NCKH chính.
- **Paper (PDF local):** không có trong Haghighi/Way kết quả · tham chiếu Ando/Arevalo chỉ để đặt tên sphering · **Hình:** không cite Rosetta Fig. là simulation
- **Data tải:** không (sinh synthetic)
- **Toán / mô hình:** MATH_NOTES §7 — \(X = \cdots + B\beta_x^\top + G\gamma_x^\top + E_x\)
- **Deliverable:** `code/c/sim_design.md`
- **Phụ thuộc:** không (song song muộn)
- **Không overlap với:** Role A benchmark thật trên JUMP

### C-P2-SIM-02 · Chạy recovery curves + §3.3 luận văn (*nếu có thời gian*)
- [ ] Trạng thái
- **Mục đích bước:** Figure recovery sau sphering/ComBat trên data giả — nhãn **mở rộng phương pháp luận**.
- **Paper (PDF local):** không · **Hình:** tự vẽ từ sim
- **Data tải:** synthetic
- **Toán / mô hình:** MATH_NOTES §7
- **Deliverable:** `results/c/sim_recovery.png`, `thesis/c/part3_3.3_optional.docx`
- **Phụ thuộc:** C-P2-SIM-01
- **Không overlap với:** NCKH claim chính

---

# LARGE PART F — Guardrails, NCKH slides, phối hợp

### C-GUARD-01 · Checklist không vi phạm khóa COORDINATION-MAP
- [ ] Trạng thái
- **Mục đích bước:** Rà soát: không MoA TA-ORF; không TVN proof; không Lasso/MLP owner; không mediation KT chính.
- **Paper (PDF local):** OUTLINE §0 · **Hình:** không
- **Data tải:** không
- **Toán / mô hình:** MATH_NOTES §8
- **Deliverable:** `work/role-c/checklist_guard.md` (signed off trước T4)
- **Phụ thuộc:** mọi C-P3-*, C-P2-*
- **Không overlap với:** không

### C-GUARD-02 · Draft §2.6 — không mediation làm PP chính
- [ ] Trạng thái
- **Mục đích bước:** 1–2 tr trong luận văn nêu rõ giới hạn nhân quả (Haghighi two-way, timepoint).
- **Paper (PDF local):** Haghighi discussion · **Hình:** không
- **Data tải:** không
- **Toán / mô hình:** không Baron–Kenny làm trụ
- **Deliverable:** `thesis/c/part2_2.6_no_mediation.docx`
- **Phụ thuộc:** C-P1-01
- **Không overlap với:** không

### C-NCKH-01 · Slides nhóm — block Role C (T4)
- [ ] Trạng thái
- **Mục đích bước:** 5–8 slide: complementary → MoA fusion một bảng → batch→predictable một bảng → limitations.
- **Paper (PDF local):** Haghighi Fig. 4 + Fig. 2b (cite); Way 1 slide complementary compound · **Hình:** screenshot PDF đã tải + kết quả nhóm
- **Data tải:** figures từ `results/c/`
- **Toán / mô hình:** tóm MATH_NOTES §6
- **Deliverable:** `slides/nckh/role_c_final.pptx`
- **Phụ thuộc:** C-P3-MOA-01, C-P2-ALIGN-05, C-GUARD-01
- **Không overlap với:** slide sphering (A), slide Lasso (B)

### C-NCKH-02 · Demo script `main` nhánh C (MoA + gọi API alignment)
- [ ] Trạng thái
- **Mục đích bước:** Entry point reproducible cho fusion MoA và orchestrate alignment (gọi B).
- **Paper (PDF local):** Haghighi repo tham khảo · https://github.com/carpenter-singh-lab/2022_Haghighi_NatureMethods · **Hình:** không
- **Data tải:** expects `data/raw/rosetta_curated`
- **Toán / mô hình:** wrap C-P2-MOA-05 + C-P2-ALIGN-04
- **Deliverable:** `code/c/main.py` + README ngắn `code/c/README.md`
- **Phụ thuộc:** C-P2-MOA-05, C-P2-ALIGN-01
- **Không overlap với:** `code/a/*`, `code/b/*` implementation core

### C-COORD-01 · Nhật ký tuần + version CP từ A
- [ ] Trạng thái
- **Mục đích bước:** Mỗi tuần ghi blocker vào COORDINATION-MAP §4; log `cp_version` khi A đổi profile.
- **Paper (PDF local):** không
- **Data tải:** không
- **Toán / mô hình:** không
- **Deliverable:** dòng Nhật ký + `work/role-c/cp_version_log.md`
- **Phụ thuộc:** S-04
- **Không overlap với:** không

---

## Lộ trình gợi ý (khớp PLAN_4MONTH)

| Tháng | Todos ưu tiên |
|-------|----------------|
| T1 | C-P1-*, C-P2-MOA-01, C-P2-ALIGN-01 |
| T2 | C-P2-MOA-02 … C-P2-MOA-07, C-P2-ALIGN-02/03 |
| T3 | C-P2-MOA-06, C-P2-ALIGN-04/05, C-P3-* |
| T4 | C-NCKH-*, C-GUARD-* |
| Sau M3 (tuỳ) | C-P2-SIM-* |

---

## Cổng hoàn thành Role C (NCKH)

- [ ] MoA fusion chạy trên **≥1** compound set (ưu tiên cả CDRP-bio và LINCS)
- [ ] Bảng batch→percent predictable (trước/sau) trên **≥1** subset LUAD/LINCS
- [ ] Slides C + demo `code/c/main.py`
- [ ] Checklist C-GUARD-01 pass
- [ ] Draft luận văn C ≥70% trước T4 (gộp part1/2/3 files)
