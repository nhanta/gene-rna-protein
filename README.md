# NCKH · kiểu hình tế bào × biểu hiện gen (3 người)

**Tên đề:** Áp dụng học máy trong phân tích thông tin chung và thông tin bổ sung giữa hồ sơ kiểu hình tế bào và biểu hiện gen khi tế bào bị quá biểu hiện gen hoặc bị xử lý bằng hợp chất hóa học  

**NCKH 4 tháng** (slides) → **1 tháng** hoàn thiện đồ án → **1 tháng** thủ tục bảo vệ.  
**Giao bài:** **22/11/2026** (dự phòng 23/11). Mã nội bộ repo: Rosetta Cellular.

## Đọc theo thứ tự

| File | Nội dung |
|------|----------|
| [`work/00-COORDINATION-MAP.md`](work/00-COORDINATION-MAP.md) | Khóa ownership 3 roles + template todo + Nhật ký |
| [`work/role-a/TODOS.md`](work/role-a/TODOS.md) · [`role-b`](work/role-b/TODOS.md) · [`role-c`](work/role-c/TODOS.md) | Todos NCKH chi tiết (paper / data / toán / hình) |
| [`work/thesis-synthesis/`](work/thesis-synthesis/) | Map todo → slides đồ án Phần 1–2–3 sau NCKH |
| [`PLAN_4MONTH.md`](PLAN_4MONTH.md) | Lịch 4+1+1, phân vai theo tuần, cổng tháng |
| [`OUTLINE.md`](OUTLINE.md) | Bài toán bám paper, phạm vi A/B/C |
| [`SPLIT_PLAN.md`](SPLIT_PLAN.md) | Tách 3 đồ án + mục lục/trang |
| [`GITHUB.md`](GITHUB.md) | `main` + `branch_a|b|c`, clone & smoke trước BV |
| [`slides/nckh-briefing/index.html`](slides/nckh-briefing/index.html) · [`PDF`](slides/nckh-briefing/nckh-briefing.pdf) | Slides kickoff, 27 trang khổ 16:9 |
| [`data/DATA.md`](data/DATA.md) | Link tải Rosetta |
| [`math/MATH_NOTES.md`](math/MATH_NOTES.md) | Công thức |
| [`literature/README.md`](literature/README.md) | PDF đã tải |

## Ba vai

| Vai | Branch | Việc |
|-----|--------|------|
| **A** | `branch_a` | Sphering/TVN + batch trên Cell Painting |
| **B** | `branch_b` | Lasso/MLP dự đoán chéo CP↔L1000 |
| **C** | `branch_c` | Fusion MoA (compound) + alignment sau batch |

## Clone, pull, push

Remote: `https://github.com/nhanta/gene-rna-protein.git`

`main` là bản chung. Mỗi người làm trên một nhánh: A → `branch_a`, B → `branch_b`, C → `branch_c`. Lệnh dưới viết cho người A; B và C đổi tên nhánh cho đúng vai.

### Clone (một lần)

```bash
git clone https://github.com/nhanta/gene-rna-protein.git
cd gene-rna-protein
git checkout branch_a
```

`git clone` đứng ở `main`. `git checkout branch_a` tạo nhánh local theo `origin/branch_a`.

### Pull `main`

Lấy bản chung mới nhất về máy:

```bash
git checkout main
git pull origin main
```

### Pull nhánh của mình

Đứng trên nhánh được giao, kéo nhánh đó, rồi gộp `main` vào:

```bash
git checkout branch_a
git pull origin branch_a
git pull origin main
```

`git pull origin main` khi đang ở `branch_a` đưa commit mới của bản chung vào nhánh làm việc. Chạy cặp lệnh này trước mỗi buổi code.

### Push nhánh của mình

```bash
git checkout branch_a
git status
git add <file vừa sửa>
git commit -m "Mô tả ngắn việc vừa làm"
git push origin branch_a
```

A push `branch_a`, B push `branch_b`, C push `branch_c`.

Phần chung (`shared/`, slides nhóm, số liệu đã chốt) vào `main` bằng pull request từ nhánh của mình. Trên GitHub: **Compare & pull request**, base `main`, compare đúng nhánh đó. `main` nhận thay đổi sau một lượt review.

## Câu chuyện một dòng

Cùng nhiễu loạn (compound / ORF) → đo **Cell Painting** và **L1000** → shared vs complementary; batch/sphering trên CP đổi kết quả multimodal thế nào (Haghighi, Way, Ando, Arevalo).
