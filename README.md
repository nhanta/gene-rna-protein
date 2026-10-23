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
| [`work/AGENTS.md`](work/AGENTS.md) | Subagents & bus phối hợp |
| [`PLAN_4MONTH.md`](PLAN_4MONTH.md) | Lịch 4+1+1, phân vai theo tuần, cổng tháng |
| [`OUTLINE.md`](OUTLINE.md) | Bài toán bám paper, phạm vi A/B/C |
| [`SPLIT_PLAN.md`](SPLIT_PLAN.md) | Tách 3 đồ án + mục lục/trang |
| [`GITHUB.md`](GITHUB.md) | `main` + `branch_a|b|c`, clone & smoke trước BV |
| [`slides/nckh-briefing/index.html`](slides/nckh-briefing/index.html) | Slides kickoff (không thay todos chi tiết) |
| [`data/DATA.md`](data/DATA.md) | Link tải Rosetta |
| [`math/MATH_NOTES.md`](math/MATH_NOTES.md) | Công thức |
| [`literature/README.md`](literature/README.md) | PDF đã tải |

## Ba vai

| Vai | Branch | Việc |
|-----|--------|------|
| **A** | `branch_a` | Sphering/TVN + batch trên Cell Painting |
| **B** | `branch_b` | Lasso/MLP dự đoán chéo CP↔L1000 |
| **C** | `branch_c` | Fusion MoA (compound) + alignment sau batch |

## Câu chuyện một dòng

Cùng nhiễu loạn (compound / ORF) → đo **Cell Painting** và **L1000** → shared vs complementary; batch/sphering trên CP đổi kết quả multimodal thế nào (Haghighi, Way, Ando, Arevalo).
