# Todos giao diện chung (tối thiểu — không lấy phần khoa học của A/B/C)

Chỉ những việc **cả nhóm** phải làm để ba nhánh khớp nhau. Không chứa chứng minh toán riêng.

### S-01 · Kickoff repo
- [ ] Tạo GitHub `main` + `branch_a|b|c` theo `GITHUB.md`
- **Paper:** không
- **Data:** không
- **Deliverable:** remote URL ghi vào Nhật ký COORDINATION-MAP
- **Không overlap:** không viết bài toán khoa học ở đây

### S-02 · Tải Rosetta curated (một lần)
- [ ] Chạy lệnh trong `data/DATA.md` §1.2
- **Data:** `aws s3 sync --no-sign-request s3://cellpainting-gallery/cpg0003-rosetta/broad/workspace/curated_preprocessed_data ./data/raw/rosetta_curated`
- **Paper:** Haghighi `literature/papers/2022_Haghighi_Rosetta.pdf` · DOI 10.1038/s41592-022-01667-0 · portal https://broad.io/rosetta/
- **Deliverable:** `data/inventory.md` (số file, dung lượng)
- **Phụ thuộc:** S-01

### S-03 · Schema ID nhiễu loạn chung
- [ ] Thống nhất cột metadata khớp CP ↔ L1000 (theo repo Haghighi)
- **Paper / code:** https://github.com/carpenter-singh-lab/2022_Haghighi_NatureMethods
- **Deliverable:** `shared/schema.md`
- **Không overlap:** không implement Lasso hay sphering ở đây

### S-04 · Sync thứ Năm 20:30
- [ ] Mỗi tuần thứ Năm 20:30: A báo profile version; B/C báo blocker
- **Deliverable:** dòng Nhật ký trong `00-COORDINATION-MAP.md`

### S-05 · Tag NCKH
- [ ] Tag `nckh-2027-03` trên `main` khi nộp slides nhóm
- **Phụ thuộc:** todos role A/B/C cổng tháng 4 xong
