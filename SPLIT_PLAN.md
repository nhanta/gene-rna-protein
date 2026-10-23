# Biên bản tách NCKH → ba đồ án tốt nghiệp

Cùng data Rosetta và khung **shared / complementary** (Haghighi 2022; Way 2022), nhưng **ba câu hỏi / ba bảng số**.  
Cấu trúc mỗi đồ án: **(1) Cơ bản 15–20 tr → (2) Phương pháp 20–30 tr → (3) Thực nghiệm ~20 tr → Kết luận 3–5 tr**.

**Lịch:** NCKH **4 tháng** từ **22/11/2026** (sản phẩm slides) → viết dần ĐA → **1 tháng** đủ trang → **1 tháng** thủ tục BV. Xem [`PLAN_4MONTH.md`](PLAN_4MONTH.md), [`GITHUB.md`](GITHUB.md).

**Tải dữ liệu (máy SV):** xem **§C2** — sync S3 công khai; không cần quyền server HUS. Chi tiết [`data/DATA.md`](data/DATA.md).

**Họp nhóm:** **20:30 tối thứ Năm** hàng tuần (sync blocker / interface `shared/` / số liệu).

**Bám paper:** xem bảng đối chiếu trong `OUTLINE.md` §0. Phần *mở rộng* phải ghi rõ trong luận văn.

**Thuật ngữ (tránh gọi tắt sai):**

- **L1000:** phép đo mức ~978 bản phiên mã mRNA của **gen landmark** (landmark genes trong paper = bộ gen L1000 đo trực tiếp; giữ thuật ngữ Anh, không dịch “điểm mốc”) — Subramanian; Haghighi gọi là gene expression / transcriptional state.
- **Cell Painting:** phép **nhuộm** huỳnh quang nhiều cấu trúc tế bào rồi **chụp ảnh** đa kênh (Bray 2016); phần mềm (CellProfiler) mới rút **đặc trưng hình thái** từ ảnh. Không đồng nghĩa “Cell Painting = hình thái”.

---

## A. Thông tin chung (điền khi ký)

| Mục | Nội dung |
|-----|----------|
| Tên dự án NCKH | Áp dụng học máy trong phân tích thông tin chung và thông tin bổ sung giữa hồ sơ kiểu hình tế bào và biểu hiện gen khi tế bào bị quá biểu hiện gen hoặc bị xử lý bằng hợp chất hóa học |
| Thời gian NCKH | từ __________ đến __________ |
| **Người A** (CP sphering/batch) | Họ tên: __________ MSSV: __________ |
| **Người B** (cross-modal Lasso/MLP) | Họ tên: __________ MSSV: __________ |
| **Người C** (fusion MoA + alignment sau batch) | Họ tên: __________ MSSV: __________ |
| GVHD | __________ |

---

## B. Quy tắc tránh trùng đề

1. **Được giống (~3–5 trang):** giới thiệu Rosetta, định nghĩa CP & L1000, sơ đồ NCKH — ghi đồng thực hiện.
2. **Không copy:** bảng số chính, chứng minh dài, case study sâu.
3. **Code:** `shared/`, `branch_a/`, `branch_b/`, `branch_c/`.
4. Không viết Cell Painting như “đo protein”; không gán Way (compound) thành kết quả ORF; không lấy mediation nhân quả làm trụ trừ mục *mở rộng* có giả định.

Câu trích dẫn mẫu:

> Khung dữ liệu và bài toán multimodal dựa trên Rosetta (Haghighi et al., 2022) và được triển khai trong đề tài NCKH *[tên]* (đồng thực hiện với *[hai bạn]*). Các kết quả Chương 2–3 là đóng góp riêng của luận văn này.

---

## C. Ba đề tài đăng ký TN

### Đồ án A

| | |
|--|--|
| **Tên đề tài dự kiến** | Nghiên cứu phương pháp chuẩn hóa dữ liệu và hiệu chỉnh nhiễu kỹ thuật trên hồ sơ kiểu hình tế bào từ kính hiển vi huỳnh quang đa kênh |
| **Dữ liệu dùng** | Hồ sơ kiểu hình sau xử lý ảnh nhuộm (Cell Painting); đánh giá trên bộ Haghighi 2022 và/hoặc hồ sơ JUMP (Arevalo 2024) |
| **Phạm vi** | Chỉnh nhiễu đĩa/lô trên nhánh kiểu hình; không làm dự đoán biểu hiện gen; không phân loại cơ chế thuốc |
| **Paper chủ** | Ando 2017; Way 2022; Arevalo 2024; Moshkov 2024 |

### Đồ án B

| | |
|--|--|
| **Tên đề tài dự kiến** | Nghiên cứu học máy dự đoán mức biểu hiện gen từ hồ sơ kiểu hình tế bào |
| **Dữ liệu dùng** | Cặp hồ sơ cùng layout: kiểu hình (ảnh nhuộm) + mức mRNA (L1000); bốn tập con Haghighi 2022 (LUAD, LINCS, CDRP-bio, TA-ORF) |
| **Phạm vi** | Hồi quy Lasso/MLP, phần trăm gen dự đoán được; không làm benchmark chỉnh nhiễu đa lab; không fusion MoA |
| **Paper chủ** | Haghighi 2022 (Fig. 2–3); Rohban 2017 |

### Đồ án C

| | |
|--|--|
| **Tên đề tài dự kiến** | Nghiên cứu học máy kết hợp hồ sơ kiểu hình tế bào và biểu hiện gen để xác định cơ chế tác dụng của hợp chất hóa học |
| **Dữ liệu dùng** | Tập hợp chất có nhãn cơ chế (CDRP-bio, LINCS — Haghighi Fig. 4); không dùng tập ORF cho bài MoA của paper đó |
| **Phạm vi** | Ghép sớm/muộn/RGCCA; so sánh trước/sau khi dùng hồ sơ kiểu hình đã chỉnh nhiễu từ A; không viết lại TVN; không sở hữu Lasso |
| **Paper chủ** | Haghighi 2022 (Fig. 4); Way 2022 |
| **Mở rộng tùy chọn** | Simulation recovery — ghi rõ *mở rộng phương pháp luận* |

**Chống trùng khi bảo vệ:** ba bảng số chính khác nhau — A chỉnh nhiễu kiểu hình; B dự đoán biểu hiện gen từ kiểu hình; C ghép hai hồ sơ cho cơ chế thuốc. Khung dữ liệu chung ghi đồng thực hiện NCKH (§B).

---

## C2. Hướng dẫn tải dữ liệu cho từng sinh viên

**Nguyên tắc:** dữ liệu nằm trên **Cell Painting Gallery (AWS S3 công khai)**. Mỗi SV tải về **máy cá nhân / Colab / máy lab**; **không** cần tài khoản AWS và **không** cần quyền SSH server HUS của GV. Chi tiết đầy đủ: [`data/DATA.md`](data/DATA.md). Script mẫu: [`scripts/download_all.sh`](scripts/download_all.sh).

**Chuẩn bị (cả nhóm):**

1. Cài [AWS CLI v2](https://aws.amazon.com/cli/).
2. Tạo thư mục làm việc repo, ví dụ `./data/raw/`.
3. Không commit file raw lên GitHub (`data/raw/` trong `.gitignore`).

**Kiểm tra sau khi tải:** mở được ít nhất một parquet bằng `pandas` / `polars`; ghi đường dẫn + kích thước vào `data/inventory.md` (máy mình).

### Chung — bắt buộc cả A, B, C (tháng 1)

Rosetta curated (~3–4 GB; đủ neo multimodal):

```bash
aws s3 sync --no-sign-request \
  s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data \
  ./data/raw/rosetta_curated
```

Sau sync phải có bốn tập con: `LUAD-BBBC041-Caicedo/`, `LINCS-Pilot1/`, `CDRP-BBBC047-Bray/`, `TA-ORF-BBBC037-Rohban/` (mỗi tập có `CellPainting/` + `L1000/`).

### Người A (sphering / batch trên CP)

| Ưu tiên | Nội dung | ~Size | Lệnh / nguồn |
|---------|----------|-------|----------------|
| Bắt buộc | Rosetta curated (trên) | ~3–4G | mục Chung |
| Khuyến nghị | JUMP CRISPR interpretable (chưa sphering) | ~1.1G | lệnh dưới |
| Khuyến nghị | JUMP ORF interpretable | ~1.7G | lệnh dưới |
| Tuỳ chọn | JUMP compound interpretable | ~12G | chỉ khi làm mở rộng Arevalo-style |
| Tuỳ chọn | Rosetta preprocessed | ~9G | `DATA.md` §1.2 |
| Tham chiếu | Code/số Arevalo 2024 | Zenodo | https://doi.org/10.5281/zenodo.11644046 · repo https://github.com/carpenter-singh-lab/2023_Arevalo_BatchCorrection |

```bash
mkdir -p ./data/raw/jump/crispr_interpretable ./data/raw/jump/orf_interpretable

aws s3 cp --no-sign-request \
  s3://cellpainting-gallery/cpg0016-jump-assembled/source_all/workspace/profiles_assembled/CRISPR/v1.0a/profiles_wellpos_cc_var_mad_outlier.parquet \
  ./data/raw/jump/crispr_interpretable/

aws s3 cp --no-sign-request \
  s3://cellpainting-gallery/cpg0016-jump-assembled/source_all/workspace/profiles_assembled/ORF/v1.0a/profiles_wellpos_cc_var_mad_outlier.parquet \
  ./data/raw/jump/orf_interpretable/
```

**Lưu ý A:** dùng bản `*_outlier.parquet` (**interpretable**, chưa `sphering_harmony`). Không tải ảnh thô JUMP/BBBC. Xuất CP đã chỉnh nhiễu vào `shared/` theo [`work/01-NCKH-SHARED-INTERFACE.md`](work/01-NCKH-SHARED-INTERFACE.md) để B/C dùng.

### Người B (Lasso / MLP cross-modal)

| Ưu tiên | Nội dung | Ghi chú |
|---------|----------|---------|
| Bắt buộc | Rosetta curated | Cả bốn subset; tập trung LUAD, LINCS, CDRP-bio, TA-ORF |
| Tuỳ chọn | Rosetta preprocessed | Nếu cần bảng CSV gốc Haghighi (`DATA.md` §1.2) |
| Nhận từ A | `shared/cp_profiles_post_batch_*` | Chỉ khi đo ảnh hưởng tiền xử lý batch (không tự benchmark JUMP) |

```bash
# Giống mục Chung — đủ để bắt đầu B
aws s3 sync --no-sign-request \
  s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data \
  ./data/raw/rosetta_curated
```

**Không bắt buộc** tải JUMP profiles (JUMP là phạm vi A / mở rộng Arevalo).

### Người C (fusion MoA)

| Ưu tiên | Nội dung | Ghi chú |
|---------|----------|---------|
| Bắt buộc | Rosetta curated | Ưu tiên `CDRP-BBBC047-Bray/` và `LINCS-Pilot1/` (compound + nhãn MoA; Haghighi Fig. 4) |
| Không dùng làm trụ MoA | `TA-ORF-BBBC037-Rohban/` | Đúng paper: không gán MoA ORF như compound |
| Nhận từ A | CP đã sphering/batch | So sánh trước/sau alignment |
| Nhận từ B (nếu có) | metric / protocol cross-modal thống nhất | Không viết lại Lasso làm trụ |

Cùng lệnh sync Rosetta curated như B. Chỉ cần đủ dung lượng cho curated (~3–4G) khi mới bắt đầu.

### Nếu không cài được AWS CLI

- Xin GV **bản đóng gói** `rosetta_curated` (Drive/USB) — đủ cho B và C khởi động.  
- Người A vẫn nên tự `aws s3 cp` JUMP interpretable khi có mạng ổn định (~3G cho CRISPR+ORF).  
- Không phụ thuộc SSH vào máy chủ nội bộ của GV.

### Checklist data trước họp nhóm tuần

- [ ] A/B/C: `./data/raw/rosetta_curated/` mở được bằng pandas  
- [ ] A: có ít nhất CRISPR hoặc ORF interpretable trong `./data/raw/jump/`  
- [ ] B: xác nhận đủ 4 subset curated  
- [ ] C: xác nhận CDRP + LINCS trong curated  
- [ ] Không ai commit raw lên Git  

---

## D. Mục lục gợi ý + ước trang

### D1. Đồ án A

**Phần 1 · Cơ bản (15–20)**

| Mục | Neo | ~Tr |
|-----|-----|-----|
| 1.1 Nhiễu loạn & high-content profiling | Bray; Arevalo intro | 2–3 |
| 1.2 Cell Painting: kênh, profile, control wells | Bray 2016 | 4–5 |
| 1.3 Batch / plate / well-position effects | Way; Ando; Arevalo | 3–4 |
| 1.4 PCA, khoảng cách cosine, ý tưởng whitening | SGK + Ando | 3–4 |
| 1.5 JUMP / Rosetta CP — phạm vi data A dùng | Arevalo / Haghighi | 2–3 |

**Phần 2 · Phương pháp (20–30)**

| Mục | Neo | ~Tr |
|-----|-----|-----|
| 2.1 Tiền xử lý profile CP | pycytominer / Haghighi prep | 3–4 |
| 2.2 Sphering / whitening trên control | Way Methods; Arevalo Sphering | 5–7 |
| 2.3 TVN (PCA + scale + CORAL) | Ando 2017 | 4–5 |
| 2.4 Harmony, ComBat, … so sánh | Arevalo | 4–5 |
| 2.5 Metric: percent replicating / mAP | Way; Arevalo | 3–4 |
| 2.6 Giả thiết control-only & hạn chế | Ando; Arevalo discussion | 2–3 |

**Phần 3 · Thực nghiệm (~20)**

| Mục | | ~Tr |
|-----|--|-----|
| 3.1 Dataset CP đã dùng + thống kê | | 2–3 |
| 3.2 Bảng ≥3 phương pháp × metric | | 5–6 |
| 3.3 Ablation control-fit / tham số | | 3–4 |
| 3.4 Case plate hoặc perturbation | | 4–5 |
| 3.5 Thảo luận đúng hạn chế paper | | 2–3 |

**Kết luận A:** 3–5 trang.

---

### D2. Đồ án B

**Phần 1 · Cơ bản (15–20)**

| Mục | Neo | ~Tr |
|-----|-----|-----|
| 1.1 Gen → mRNA (mức dùng cho L1000) | SGK + Haghighi wording | 2–3 |
| 1.2 L1000 landmark (~978) | Haghighi; Subramanian nếu đọc thêm | 4–5 |
| 1.3 Cell Painting profile (mức cần cho multimodal) | Bray; Haghighi | 2–3 |
| 1.4 Shared vs complementary — định nghĩa paper | Haghighi § shared/complementary | 4–5 |
| 1.5 Bốn/năm subset Rosetta; TA-ORF yếu đã biết | Haghighi Table percent predictable | 2–3 |

**Phần 2 · Phương pháp (20–30)**

| Mục | Neo | ~Tr |
|-----|-----|-----|
| 2.1 Khớp perturbation CP–L1000; pretreatment | Haghighi Methods / GitHub | 3–4 |
| 2.2 **Lasso** baseline | Haghighi | 4–5 |
| 2.3 **MLP** baseline | Haghighi | 4–5 |
| 2.4 Metric prediction score, percent predictable, shuffle null | Haghighi | 3–4 |
| 2.5 (So sánh thêm) ridge/CCA — ghi không phải baseline gốc | *mở rộng nhẹ* | 3–4 |
| 2.6 Hướng GE→CP và CP→GE | Haghighi Fig. 2–3 | 2–3 |

**Phần 3 · Thực nghiệm (~20)**

| Mục | | ~Tr |
|-----|--|-----|
| 3.1 Tái lập phân bố score theo dataset | Khớp hướng Haghighi | 5–6 |
| 3.2 So TA-ORF vs LUAD/LINCS (báo cáo trung thực) | | 3–4 |
| 3.3 Gene/feature predictable — explorative | | 4–5 |
| 3.4 Ảnh hưởng tiền xử lý (nếu nhận profile từ A) | | 3–4 |
| 3.5 Hạn chế landmark & timepoint khác nhau | Đúng Haghighi | 2–3 |

**Kết luận B:** 3–5 trang.

---

### D3. Đồ án C

**Phần 1 · Cơ bản (15–20)**

| Mục | Neo | ~Tr |
|-----|-----|-----|
| 1.1 Vì sao cần multimodal profiling | Haghighi intro; Way intro | 3–4 |
| 1.2 Complementary subspace & fusion (ý tưởng) | Haghighi | 4–5 |
| 1.3 MoA prediction từ profile — bài toán drug | Haghighi MoA section; Way MOA | 4–5 |
| 1.4 Batch có thể phá/hỏng so sánh multimodal | Haghighi gợi ý; Way plate effects | 3–4 |
| 1.5 Vai trò A/B trong pipeline nhóm | OUTLINE | 2–3 |

**Phần 2 · Phương pháp (20–30)**

| Mục | Neo | ~Tr |
|-----|-----|-----|
| 2.1 Unsupervised MoA retrieval / Jaccard | Haghighi Fig. 4a | 4–5 |
| 2.2 Supervised MoA: single modality, early/late fusion, RGCCA (mức tái lập) | Haghighi Fig. 4b | 5–7 |
| 2.3 Protocol: áp CP đã sphering/batch từ A → đo lại cross-modal B | Haghighi “batch…alignment” | 4–5 |
| 2.4 Metric thống nhất với B/A | | 2–3 |
| 2.5 (*Mở rộng*) Simulation planted batch/signal | Ghi mở rộng | 4–6 |
| 2.6 Không dùng mediation nhân quả làm PP chính | OUTLINE §0 | 1–2 |

**Phần 3 · Thực nghiệm (~20)**

| Mục | | ~Tr |
|-----|--|-----|
| 3.1 Fusion vs CP vs L1000 trên CDRP-bio và/hoặc LINCS | Hướng Haghighi Fig.4 | 6–7 |
| 3.2 Bảng “trước/sau batch” → đổi percent predictable | | 4–5 |
| 3.3 (*Nếu có*) Simulation recovery | Mở rộng | 3–4 |
| 3.4 Thảo luận: fusion không luôn thắng (Haghighi cũng báo) | | 2–3 |
| 3.5 Hạn chế: MoA labels imperfect; không suy ORF từ compound | | 2–3 |

**Kết luận C:** 3–5 trang.

---

## E. Checklist trước đăng ký TN

- [ ] Ba tiêu đề khác nhau đúng §C  
- [ ] Mỗi SV đã tải data đúng vai trò theo §C2 (Rosetta curated tối thiểu)  
- [ ] B tái lập **Lasso/MLP** (không chỉ ridge tự bịa baseline)  
- [ ] C fusion trên **compound** Rosetta (không bịa MoA ORF)  
- [ ] TA-ORF được mô tả đúng mức yếu theo Haghighi  
- [ ] Không có chương “proteinomics Cell Painting”  
- [ ] Mediation nhân quả không phải trụ (hoặc chỉ phụ lục mở rộng)  
- [ ] Mỗi người ≥2 bảng số không trùng  

---

## F. Ma trận sản phẩm

| Sản phẩm | NCKH | A | B | C |
|----------|------|---|---|---|
| Loader Rosetta | ✓ | dùng | dùng | dùng |
| Sphering/batch CP | ✓ | **chủ** | nhận profile | thử alignment |
| Lasso/MLP cross-modal | ✓ | — | **chủ** | đo lại sau batch |
| MoA fusion compound | ✓ | — | — | **chủ** |
| Simulation | tuỳ | — | — | mở rộng |
| Luận văn 3 phần | — | riêng | riêng | riêng |

---

## G. Chữ ký

| Vai trò | Ký tên | Ngày |
|---------|--------|------|
| Người A | | |
| Người B | | |
| Người C | | |
| GVHD (ba đề không trùng; đúng phạm vi paper) | | |
