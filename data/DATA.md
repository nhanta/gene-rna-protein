# Dữ liệu công khai — vai trò + link tải

**Nguyên tắc:** NCKH lõi multimodal (L1000 **và** hồ sơ từ Cell Painting, cùng layout) chỉ có **Rosetta (`cpg0003-rosetta`)**.  
Các bộ khác dùng cho **chỉnh nhiễu / đối chiếu hình thái / mở rộng** — không thay Rosetta cho bài dự đoán chéo CP↔L1000.

Mục lục gallery: https://broadinstitute.github.io/cellpainting-gallery/complete_datasets.html  
Hướng dẫn tải S3: https://broadinstitute.github.io/cellpainting-gallery/download_instructions.html  
Duyệt bucket: https://cellpainting-gallery.s3.amazonaws.com/index.html  
Liệt kê: `aws s3 ls --no-sign-request s3://cellpainting-gallery/`

---

## 1. Neo multimodal (bắt buộc tháng 1) — Rosetta

| | |
|--|--|
| **ID gallery** | `cpg0003-rosetta` (~8,5 GB số; **không** kèm ảnh thô) |
| **Paper** | Haghighi et al., Nat Methods 2022 · DOI https://doi.org/10.1038/s41592-022-01667-0 |
| **Portal** | https://broad.io/rosetta/ |
| **Code** | https://github.com/carpenter-singh-lab/2022_Haghighi_NatureMethods |
| **Gallery entry** | https://broadinstitute.github.io/cellpainting-gallery/complete_datasets.html (dòng cpg0003-rosetta) |

### 1.1 Curated parquet (khuyến nghị)

```bash
aws s3 sync --no-sign-request \
  s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data \
  ./data/raw/rosetta_curated
```

### 1.2 Preprocessed đầy đủ hơn

```bash
aws s3 sync --no-sign-request \
  s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/preprocessed_data \
  ./data/raw/rosetta_preprocessed
```

### 1.3 Tập con trong curated (theo repo Haghighi)

```text
LUAD-BBBC041-Caicedo/     CellPainting/ + L1000/
LINCS-Pilot1/             CellPainting/ + L1000/
CDRP-BBBC047-Bray/        CellPainting/ + L1000/   # CDRP-bio trong paper
TA-ORF-BBBC037-Rohban/    CellPainting/ + L1000/
```

---

## 2. Chỉnh nhiễu / benchmark hình thái (SV A) — JUMP + Arevalo

| Nguồn | Vai trò | Link tải / mã |
|-------|---------|----------------|
| **Arevalo 2024** pipeline + số liệu đi kèm | Benchmark ~10 phương pháp batch trên hồ sơ Cell Painting | Code: https://github.com/carpenter-singh-lab/2023_Arevalo_BatchCorrection · Zenodo: https://doi.org/10.5281/zenodo.11644046 · Paper DOI: https://doi.org/10.1038/s41467-024-50613-5 |
| **cpg0016-jump** | JUMP Cell Painting lớn (compound + ORF + CRISPR ở **tầng ảnh/hồ sơ**); Arevalo neo JUMP | Gallery: dòng cpg0016-jump · S3: `s3://cellpainting-gallery/cpg0016-jump/` · **Cảnh báo:** tổng ~358 TB — chỉ sync **profiles** theo README Arevalo/JUMP Hub, **không** tải ảnh thô |
| **JUMP Hub** | Điểm vào metadata / subset | Theo liên kết trên trang complete_datasets (JUMP Hub) |

Lệnh liệt kê (chưa tải hết):

```bash
aws s3 ls --no-sign-request s3://cellpainting-gallery/cpg0016-jump/
```

---

## 3. Đối chiếu ORF / CRISPR / thuốc ở tầng ảnh (mở rộng) — CPJUMP1

| | |
|--|--|
| **ID** | `cpg0000-jump-pilot` (CPJUMP1; Chandrasekaran et al. 2024) |
| **Nội dung** | Compound + ORF + CRISPR knockout trên Cell Painting (**không** thay Rosetta cho cặp L1000) |
| **Paper** | DOI https://doi.org/10.1038/s41592-024-02241-6 |
| **S3** | `s3://cellpainting-gallery/cpg0000-jump-pilot/` (~12 TB tổng; ưu tiên numerical/profiles) |
| **Lệnh xem** | `aws s3 ls --no-sign-request s3://cellpainting-gallery/cpg0000-jump-pilot/` |

PDF nhóm: `literature/papers/2024_Chandrasekaran_CPJUMP1.pdf`

---

## 4. Way complementary (compound) — tùy chọn đối chiếu

| | |
|--|--|
| **ID** | `cpg0004-lincs` (Way et al. 2022; idr0125) |
| **Vai trò** | Compound A549; spherize; complementary — **không** ORF |
| **Paper** | DOI https://doi.org/10.1016/j.cels.2022.10.001 |
| **S3** | `s3://cellpainting-gallery/cpg0004-lincs/` (rất lớn nếu kèm ảnh; ưu tiên numerical ~3,8 TB theo gallery) |
| **Lệnh xem** | `aws s3 ls --no-sign-request s3://cellpainting-gallery/cpg0004-lincs/` |

Trong Rosetta đã có subset **LINCS-Pilot1** (CP+L1000) — đủ cho lõi B/C trước khi đụng cpg0004.

---

## 5. Nguồn ORF/ảnh liên quan (tham chiếu; đã gói một phần trong Rosetta)

| ID / tên | Vai trò | Link |
|----------|---------|------|
| `cpg0017-rohban-pathways` (TA-ORF / BBBC037) | ORF + Cell Painting (Rohban 2017); Rosetta đã có TA-ORF CP+L1000 | S3: `s3://cellpainting-gallery/cpg0017-rohban-pathways/` |
| `cpg0031-caicedo-cmvip` (LUAD) | ORF alleles; liên quan LUAD | S3: `s3://cellpainting-gallery/cpg0031-caicedo-cmvip/` |

---

## 6. Mở rộng RNA ngoài Rosetta (không lõi 4 tháng)

| Nguồn | Nội dung | Link |
|-------|----------|------|
| LINCS L1000 GEO | Signature; có `trt_oe` / `trt_xpr` | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138 · https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742 |
| CLUE.io | Metadata / Level 5 tra cứu | https://clue.io/ |
| Replogle Perturb-seq | scRNA CRISPRi — **phụ lục**, không trụ NCKH | Figshare theo paper Replogle (chỉ khi GVHD duyệt mở rộng) |

---

## 7. Đặt local

```text
projects/gene-rna-protein/data/raw/        # gitignore
projects/gene-rna-protein/data/processed/
```

---

## 8. Checklist tháng 1

- [ ] AWS CLI; sync **Rosetta curated** (§1.1)
- [ ] Mở được CP + L1000 của ít nhất LUAD và TA-ORF bằng pandas
- [ ] Ghi `data/inventory.md`
- [ ] (SV A) Clone / tải Zenodo Arevalo; quyết định có sync subset JUMP profiles không
- [ ] (Tuỳ) `aws s3 ls` CPJUMP1 — chưa bắt buộc sync

## 9. Giấy phép

- Cell Painting Gallery / Rosetta: thường CC0 (theo Haghighi)  
- Code Haghighi: BSD-3  
- Trích dẫn paper gốc trên mọi báo cáo
