# Data inventory

**Canonical copy (đang tải):** HUS  
`/work/users/minhnth/projects/gene-rna-protein/data/`

## Dung lượng HUS (lúc khởi tạo tải)

| Mục | Giá trị |
|-----|---------|
| User used `/work` | ~6.726 T |
| Filesystem `/work` free | ~1.2 T |
| Quota block limit | default (0 = không giới hạn cứng hiển thị) |

## Layout

```text
/work/users/minhnth/projects/gene-rna-protein/
  data/raw/rosetta_curated/          # cpg0003 curated
  data/raw/rosetta_preprocessed/     # cpg0003 preprocessed
  data/raw/jump/orf_interpretable/
  data/raw/jump/crispr_interpretable/
  data/raw/jump/compound_interpretable/
  data/raw/arevalo_zenodo/
  scripts/download_all.sh
  logs/
```

## Theo dõi download

```bash
ssh hus-direct   # hoặc hus với key
tail -f /work/users/minhnth/projects/gene-rna-protein/logs/download_all.log
du -sh /work/users/minhnth/projects/gene-rna-protein/data/raw/*
ps -ef | grep download_all
```

Sau khi xong, file `inventory.md` trên HUS sẽ được ghi lại với kích thước thực tế.
