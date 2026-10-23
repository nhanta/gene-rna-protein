# Download plan (HUS) — gene-rna-protein

Base: `/work/users/minhnth/projects/gene-rna-protein`

| Folder | Source | Role |
|--------|--------|------|
| `data/raw/rosetta_curated` | cpg0003 curated_preprocessed_data | Neo multimodal (bắt buộc) |
| `data/raw/rosetta_preprocessed` | cpg0003 preprocessed_data | Đầy đủ hơn (DATA.md §1.2) |
| `data/raw/jump/orf_interpretable` | JUMP ORF interpretable parquet | Batch/sphering SV A |
| `data/raw/jump/crispr_interpretable` | JUMP CRISPR interpretable parquet | Batch/sphering SV A |
| `data/raw/jump/compound_interpretable` | JUMP compound interpretable parquet | Mở rộng Arevalo-style |
| `data/raw/arevalo_zenodo` | Zenodo 11644046 metadata | Benchmark Arevalo |

Không tải ảnh thô JUMP/BBBC.

Chạy: `bash scripts/download_all.sh` (hoặc `nohup` trên login node).
