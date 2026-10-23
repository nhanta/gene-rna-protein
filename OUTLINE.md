# Dàn ý dự án: Cell Painting × L1000 dưới nhiễu loạn gen/hóa chất

**Tên NCKH:** *Áp dụng học máy trong phân tích thông tin chung và thông tin bổ sung giữa hồ sơ kiểu hình tế bào và biểu hiện gen khi tế bào bị quá biểu hiện gen hoặc bị xử lý bằng hợp chất hóa học*

**Thành viên:** **3 người** (A, B, C)  
**Giai đoạn 1 — NCKH:** **4 tháng** (giao bài **22/11/2026**, dự phòng 23/11) → sản phẩm **slides** (không bắt buộc nộp luận văn)  
**Song song:** viết dần đồ án theo [`SPLIT_PLAN.md`](SPLIT_PLAN.md)  
**Giai đoạn 2:** **1 tháng** hoàn thiện luận văn + **1 tháng** thủ tục bảo vệ  
**Lịch chi tiết:** [`PLAN_4MONTH.md`](PLAN_4MONTH.md) · Git: [`GITHUB.md`](GITHUB.md)  
**Tải data từng SV:** [`SPLIT_PLAN.md`](SPLIT_PLAN.md) **§C2** · nguồn đầy đủ [`data/DATA.md`](data/DATA.md) (S3 công khai; không cần SSH HUS)

**Nguyên tắc nội dung:** mọi bài toán lõi phải **bám paper đã đọc** (Haghighi 2022, Way 2022, Ando 2017, Arevalo 2024, Rohban 2017, Moshkov 2024). Phần mở rộng luận văn phải gắn nhãn rõ *mở rộng*, không viết như thể paper đã làm.

---

## 0. Đối chiếu paper (đọc trước khi làm)

| Paper | DOI / nguồn | Dự án lấy gì từ paper |
|-------|-------------|------------------------|
| **Haghighi et al. 2022** (Rosetta) | 10.1038/s41592-022-01667-0 | Dataset cặp CP+L1000; khung *shared vs complementary*; baseline **Lasso / MLP** dự đoán chéo; fusion MoA trên **bộ compound**; gợi ý batch correction để cải thiện alignment |
| **Way et al. 2022** | 10.1016/j.cels.2022.10.001 | Complementary trên **1.327 compound** (A549); metric percent replicating; **spherize** CP bằng DMSO (Ando); **không** phải ORF/CRISPR |
| **Ando et al. 2017** | 10.1101/161422 | **TVN**: PCA trên control → chuẩn hóa trục → correlation alignment (CORAL) |
| **Arevalo et al. 2024** | 10.1038/s41467-024-50613-5 | Benchmark batch trên **JUMP Cell Painting**; **Sphering** cần negative control; Harmony / Seurat RPCA trong top |
| **Rohban et al. 2017** | 10.7554/eLife.24060 | Nguồn sinh học **TA-ORF** (ORF overexpression + Cell Painting) |
| **Moshkov et al. 2024** | 10.1038/s41467-024-45999-1 | Sphering / SVD trên control trong thực hành Cell Painting CNN (ngữ cảnh phương pháp) |
| **Bray et al. 2016** | 10.1038/nprot.2016.105 | Định nghĩa phép đo Cell Painting |

### Sự thật quan trọng (tránh phóng đại)

1. **Rosetta không đo proteomics.** Hai readout là **morphology (Cell Painting)** và **mRNA (L1000)**. Nói “protein” chỉ là *ngữ cảnh sinh học tầng dưới RNA*, không phải phép đo protein trong data.  
2. **Way 2022 chỉ dùng compound**, không phải ORF/CRISPR. Dùng Way cho khung complementary + spherize, không gán kết luận Way sang ORF.  
3. **TA-ORF (genetic ORF) trong Haghighi có cross-modal yếu:** paper báo ~**4.7% (Lasso) / 5.5% (MLP)** landmark predictable — thấp hơn LUAD/LINCS. Phải báo cáo trung thực; ưu tiên tái lập trên **nhiều subset** (LUAD, LINCS, CDRP-bio, TA-ORF), không chỉ TA-ORF.  
4. **Haghighi không làm mediation nhân quả Gene→RNA→Morphology.** Paper nói quan hệ **phức tạp, hai chiều**, không kỳ vọng map 1–1; thời điểm đo hai phép đo khác nhau.  
5. **Fusion MoA trong Haghighi** chạy trên **CDRP-bio và LINCS (compound)**, không phải benchmark MoA trên TA-ORF.  
6. **CRISPR + CP + L1000 cặp sẵn** không phải trụ Rosetta. CPJUMP1 có CRISPR/ORF/compound nhưng là **hình thái** (không thay Rosetta cho bài multimodal). CRISPR chỉ dùng **đối chiếu hình thái** nếu nhóm còn bandwidth — gắn nhãn *mở rộng*.

---

## 1. Bài toán — lời thường, đúng paper

### 1.1 Thí nghiệm đang nói tới

Tế bào nuôi cấy bị **nhiễu loạn** (thuốc hoặc **ORF overexpression** gen), rồi đo:

| Phép đo | Đo gì (theo paper) |
|-------|---------------------|
| **L1000** | ~978 mRNA landmark → **gene expression / transcriptional state** |
| **Cell Painting** | Ảnh 5 kênh → đặc trưng hình thái (shape, intensity, texture, …) → **morphological profile** |

Haghighi: cùng layout perturbation, **hai bộ đĩa song song** — một đo GE, một đo morphology (không phải cùng giếng đo cả hai cùng lúc).

### 1.2 Câu hỏi khoa học chung (đúng khung Haghighi + Way)

> Thông tin nào **chung (shared)** giữa Cell Painting và L1000, thông tin nào **bổ sung (complementary)**? Batch/sphering trên hình thái thay đổi các phép đo đó thế nào?

Ba người = ba mảnh của cùng khung paper, không phải ba câu chuyện khác.

### 1.3 Ba câu hỏi (mỗi người) — neo paper

| Người | Câu hỏi | Neo paper |
|-------|---------|-----------|
| **A** | Trên profile **Cell Painting**, sphering/TVN và các phương pháp batch (Harmony, ComBat, …) ảnh hưởng tín hiệu sinh học (replicate / retrieval) thế nào? | Way (spherize DMSO); Ando (TVN); Arevalo (benchmark JUMP); Moshkov (sphering thực hành) |
| **B** | Tái lập / mở rộng **dự đoán chéo** CP↔L1000 (baseline Lasso/MLP của Haghighi) trên các subset Rosetta; mô tả gene/feature predictable vs không | Haghighi Application “shared subspace” (Fig. 2–3); baseline Lasso/MLP |
| **C** | (1) **Fusion** CP+L1000 có cải thiện bài MoA trên CDRP-bio/LINCS như Haghighi không? (2) Batch/sphering của A có **cải thiện alignment** cross-modal (đúng hướng Haghighi gợi ý) không? | Haghighi complementary / MoA fusion (Fig. 4); câu “batch effect corrections to improve alignment” trong Haghighi |

**Simulation có đáp án** (người C): công cụ *đánh giá phương pháp* cho luận văn — **không** có trong Rosetta/Way như kết quả chính. Gắn nhãn *mở rộng phương pháp luận*.

---

## 2. Kiến trúc 3 nhánh

```text
     Perturbation (chemical và/hoặc ORF overexpression)
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
      Nhánh A         Nhánh B         Nhánh C
      CP profiles     L1000 +         Fusion MoA
      sphering/batch  cross-predict   + kiểm alignment
      (Arevalo/Ando)  (Haghighi       sau batch (A→B)
                       App. shared)
         │               │               │
         └───────────────┴───────┬───────┘
                                 ▼
                    Poster / báo cáo NCKH chung
```

| Thành phần | Chủ trì | Paper |
|------------|---------|-------|
| Loader Rosetta, QC | Cả nhóm | Haghighi + repo GitHub |
| Sphering / batch trên CP | **A** | Ando, Way, Arevalo, Moshkov |
| Cross-modal Lasso/MLP (± ridge so sánh) | **B** | Haghighi Fig. 2–3 |
| Fusion MoA + đo lại cross-modal sau batch | **C** | Haghighi Fig. 4 + đoạn batch/alignment |
| Simulation (tuỳ) | **C** | *Mở rộng* |

---

## 3. Chi tiết từng bài toán (phạm vi đúng paper)

### 3.1 Người A — Sphering / batch trên Cell Painting

**Làm (có paper):**

- Spherize/whiten ước trên **negative control** (Way Methods; Arevalo mô tả Sphering; Ando TVN = PCA control + scale + CORAL).  
- So với Harmony, ComBat, … theo tinh thần Arevalo (metric sinh học vs batch).  
- Data: CP từ Rosetta; **mở rộng mạnh** nếu dùng JUMP profiles (Arevalo) — không cần ảnh thô TB.

**Không làm / không nhận là paper đã làm:**

- Mediation nhân quả.  
- Claim “SVD sphering” là thuật ngữ duy nhất của Ando — Ando gọi **TVN**; cộng đồng CP hay gọi **sphering/whitening**; Moshkov/Arevalo dùng sphering. Viết đúng nguồn từng tên.

### 3.2 Người B — Shared subspace: dự đoán chéo CP ↔ L1000

**Làm (có paper):**

- Tái lập baseline **Lasso** và **MLP** (Haghighi): dự đoán từng landmark từ CP; dự đoán feature CP từ L1000.  
- Báo **percent predictable** theo dataset; so LUAD / LINCS / CDRP-bio / **TA-ORF** (chấp nhận TA-ORF yếu nếu khớp paper).  
- Phân tích gene/feature predictable (Haghighi đã làm khung này).  
- *So sánh thêm* ridge/CCA chỉ như biến thể tuyến tính — ghi rõ không phải baseline gốc paper.

**Không làm:**

- Gán kết luận complementary của **Way (compound)** sang ORF mà không chạy lại trên data ORF/genetic.  
- Nói L1000 = toàn transcriptome (paper: landmark ~82% variance *ước lượng*, không phải đo hết gen).

### 3.3 Người C — Complementary: fusion + alignment sau batch

**Làm (có paper):**

1. **MoA fusion** trên CDRP-bio và/hoặc LINCS: CP alone, GE alone, early fusion, (tuỳ) RGCCA như Haghighi Fig. 4; metric Jaccard / classification như paper (hoặc subset trung thực nếu compute hạn chế).  
2. **Câu Haghighi gợi ý:** sau khi A áp batch/sphering lên CP, chạy lại cross-modal của B — alignment / percent predictable có tăng không?

**Mở rộng (ghi rõ trong luận văn):**

- Simulation planted batch + planted biology để giải thích *khi nào* sphering giúp/hại recovery (không có bảng này trong Rosetta).  
- Phân tích residual “không predict được” = operational hóa *complementary subspace* (đúng ý Haghighi), **không** đổi tên thành “mediation nhân quả” trừ khi viết riêng mục giả định và hạn chế.

**Đã loại khỏi đề C (vì không có trong paper lõi):** mediation Baron–Kenny kiểu Gene→RNA→Morphology như claim chính.

---

## 4. Đủ trang đồ án (3 phần)

Cấu trúc mục tiêu: Phần 1 **15–20** · Phần 2 **20–30** · Phần 3 **~20** · Kết luận **3–5**.  
Mục lục chi tiết: [`SPLIT_PLAN.md`](SPLIT_PLAN.md).

| Người | Phần 1 bám | Phần 2 bám | Phần 3 bám |
|-------|------------|------------|------------|
| A | Bray + batch + đại số PCA | TVN/sphering, Arevalo methods | Bảng benchmark CP |
| B | L1000 + central dogma mức dùng | Lasso/MLP (+ ridge so), metric Haghighi | Tái lập Fig.2-style trên Rosetta subsets |
| C | Shared vs complementary (Haghighi/Way) | Fusion + protocol đo alignment sau batch | Fig.4-style + bảng “batch→cross-modal” |

---

## 5. Dữ liệu công khai

| Dataset | Perturbation | Dùng cho |
|---------|--------------|----------|
| Rosetta **LUAD**, **LINCS**, **CDRP-bio** | Chủ yếu chemical / allele (LUAD) | B cross-modal; C fusion MoA (compound) |
| Rosetta **TA-ORF** | ORF overexpression (U2OS) | B + góc genetic; kỳ vọng cross-modal **thấp** (đúng paper) |
| JUMP CP profiles (Arevalo) | Chemical + genetic | A batch (*mở rộng* nếu cần) |
| CPJUMP1 profiles | Compound + ORF + CRISPR | Chỉ *mở rộng* hình thái — **không** có L1000 cặp như Rosetta |

**Ai tải gì / lệnh cụ thể:** [`SPLIT_PLAN.md`](SPLIT_PLAN.md) **§C2** (A: Rosetta + JUMP interpretable; B/C: Rosetta curated; không phụ thuộc server HUS).  
**Catalog & lệnh đầy đủ:** [`data/DATA.md`](data/DATA.md).

---

## 6. Lộ trình (rút gọn — xem PLAN_4MONTH)

| Tháng lịch | Việc chính |
|------------|------------|
| **T1** (22/11→22/12/2026) | Đọc paper; tải Rosetta; pipeline; draft ĐA Phần 1 |
| **T2** (→22/01/2027) | Baseline A/B/C; draft Phần 2 (toán) |
| **T3** (→22/02/2027) | Nối batch→cross-modal; draft Phần 3 |
| **T4** (→22/03/2027) | **Slides NCKH** + demo `main`; draft ĐA ≥70% |
| **T5** (→22/04/2027) | Hoàn thiện luận văn đủ trang |
| **T6** (→22/05/2027) | Thủ tục bảo vệ; clone sạch chạy lại |

Chi tiết tuần và cổng: [`PLAN_4MONTH.md`](PLAN_4MONTH.md).

---

## 7. Toán (phân vai, đúng tên paper)

Chi tiết: [`math/MATH_NOTES.md`](math/MATH_NOTES.md).

| Chủ đề | Ai | Nguồn tên gọi |
|--------|-----|----------------|
| PCA whitening / sphering / TVN | A | Ando TVN; Way spherize; Arevalo Sphering |
| Harmony, ComBat, … | A so; B nếu đụng L1000 | Arevalo; sva |
| Lasso, MLP regression | B | Haghighi |
| Ridge / CCA | B/C *so sánh thêm* | Không thay baseline paper |
| Early fusion / RGCCA (mức dùng lại) | C | Haghighi Fig. 4 |
| mAP / percent replicating / percent predictable | A/B theo phép đo | Way; Haghighi; Arevalo |
| Simulation recovery | C *mở rộng* | Luận văn |

---

## 8. Tiêu chí thành công NCKH (không bịa số liệu)

1. Tái lập được **hướng** kết quả Haghighi: LUAD/LINCS cross-modal mạnh hơn TA-ORF/CDRP-bio (không cần trùng số tuyệt đối mọi chữ số).  
2. A có bảng sphering/batch với metric rõ (Arevalo-style hoặc Way percent replicating trên CP).  
3. C có ít nhất một kết quả fusion (compound) **hoặc** một bảng “sau batch → đổi cross-modal”.  
4. Mọi claim ORF/CRISPR/protein đều đúng phạm vi §0.  
5. `SPLIT_PLAN.md` đã điền 3 người.

---

## 9. Rủi ro

| Rủi ro | Xử lý đúng paper |
|--------|------------------|
| TA-ORF yếu | Đã được Haghighi báo — chọn thêm LUAD/LINCS; không “nặn” ORF thành success giả |
| Nhầm Way = genetic | Giữ Way ở compound + spherize |
| Muốn mediation nhân quả | Đưa xuống phụ lục *mở rộng* hoặc bỏ; không làm trụ NCKH |
| MoA trên ORF không có label như compound | Fusion MoA chỉ trên CDRP-bio/LINCS như Haghighi |

---

## 10. File trong folder

| Path | Vai trò |
|------|---------|
| `OUTLINE.md` | File này |
| `README.md` | Điểm vào |
| `PLAN_4MONTH.md` | Lịch 4+1+1, cổng tháng |
| `GITHUB.md` | Nhánh + clone trước BV |
| `NOTES_GAPS.md` | Mục dễ quên |
| `SPLIT_PLAN.md` | Tách 3 đồ án + mục lục trang + **§C2 tải data từng SV** |
| `slides/nckh-briefing/` | Slides giao bài (HTML→PDF) + `QC_REPORT.md` |
| `data/DATA.md` | Catalog / lệnh S3 đầy đủ |
| `scripts/download_all.sh` | Script mẫu sync (máy SV hoặc lab) |
| `math/MATH_NOTES.md` | Công thức |
| `literature/` | PDF/text paper |
