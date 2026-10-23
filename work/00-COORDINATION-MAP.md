# Bản đồ phối hợp NCKH — khóa quyền sở hữu (không overlap)

**Bus chung cho mọi agent / người.** Chỉ sửa cột Nhật ký và báo cáo agent; **không** đổi bảng khóa dưới đây trừ khi cả nhóm thống nhất.

## 1. Hai tầng sản phẩm

| Tầng | Thời điểm | Sản phẩm |
|------|-----------|----------|
| **NCKH chung** | 4 tháng từ 22/11/2026 | Todos chi tiết + code + **slides nhóm** |
| **Đồ án riêng** | Sau NCKH (+1 tháng viết đủ +1 tháng BV) | Mỗi role một bộ **slides đồ án** đủ Phần 1–2–3 + KL |

## 2. Bảng khóa — ai sở hữu phần nào (cấm overlap nội dung chính)

| Phần luận văn / NCKH | Role A | Role B | Role C |
|----------------------|--------|--------|--------|
| Phát biểu bài toán (góc riêng) | Nhiễu kỹ thuật làm méo **hình thái** | Hai phép đo có **dự đoán chéo** được không | Hai phép đo **bổ sung** cho bài MoA / alignment |
| Mục đích | So sánh sphering/TVN/batch trên CP | Tái lập Lasso/MLP cross-modal | Fusion MoA + đo lại sau batch A |
| Ứng dụng | Hồ sơ hình thái tin cậy hơn cho so sánh gen/thuốc | Tiết kiệm / suy diễn GE từ ảnh (trong giới hạn paper) | Ghép multimodal cho cơ chế thuốc |
| Phương pháp chính | TVN, sphering, Harmony, ComBat, metric replicate/mAP | Lasso, MLP, percent predictable, shuffle null | Early/late fusion, RGCCA (mức paper), protocol A→B |
| Data chính | CP (+ control) Rosetta; JUMP profiles nếu mở rộng Arevalo | CP+L1000 khớp ID; ưu tiên LUAD/LINCS; TA-ORF đối chiếu | CDRP-bio/LINCS cho MoA; nhận CP đã batch từ A |
| **Cấm làm** | Lasso/MLP đầy đủ; fusion MoA | Benchmark JUMP đa lab thay Arevalo; fusion MoA chính | Viết lại chứng minh SVD/TVN dài; mediation nhân quả làm trụ |

**Được giống tối đa ~3–5 trang / vài slide:** định nghĩa Rosetta, CP, L1000, sơ đồ nhóm — phải ghi đồng thực hiện NCKH.

## 3. Template một todo (bắt buộc đủ trường)

```markdown
### ID · Tiêu đề
- [ ] Trạng thái
- **Mục đích bước:** …
- **Paper (PDF local):** `literature/papers/….pdf` · DOI … · **Hình được phép chụp+cite:** Fig. … (ghi số hình trong paper; không vẽ bịa)
- **Data tải:** lệnh / URL …
- **Toán / mô hình:** công thức hoặc “xem MATH_NOTES §…” + trích giả thiết paper
- **Deliverable:** file/bảng/slide cụ thể
- **Phụ thuộc:** ID khác hoặc role khác
- **Không overlap với:** Role …
```

## 4. Nhật ký phối hợp

| Ngày | Agent / người | Việc | Claim nguồn |
|------|---------------|------|-------------|
| 2026-10-18 | Agent Role-C planner | Viết `work/role-c/TODOS.md` (MoA compound Fig.4, protocol A→B metrics, map Đồ án C D3) | Haghighi Fig.4 + batch/alignment; Way complementary (compound); MATH_NOTES §6 |
| 2026-10-18 | Agent Role-B planner | Tạo `work/role-b/TODOS.md` (Lasso/MLP, 4 subset, map Đồ án B D2); không sở hữu TVN/MoA | Haghighi 2022 Fig.2–3; OUTLINE §0; DATA.md; MATH_NOTES §4–5; COORDINATION-MAP §3 |
| 2026-10-18 | Agent Role-A planner | Viết `work/role-a/TODOS.md` (43 todos, 8 phần; map Đồ án A D1); không Lasso/MoA | Ando TVN; Way spherize; Arevalo; Bray; Moshkov; MATH_NOTES §1–3§5; DATA.md |
| 2026-10-18 | Parent | QC A/B/C ownership OK → launch Integrator (overlap + thesis slide outlines) | COORDINATION-MAP §2 |
| 2026-10-18 | Integrator | `02-OVERLAP-CHECK.md` **PASS**; `thesis-synthesis/thesis-{a,b,c}-SLIDES-OUTLINE.md` (~58–59 slide/role, SPLIT D1–D3) | §2 khóa; A-P6-10→B-901→C-P2-ALIGN; WARN screenshot trùng Haghighi Fig.1/2b |

## 5. Quy tắc chống bịa

1. Mọi số liệu / hình phải trỏ paper hoặc kết quả nhóm tự chạy trên data public.  
2. Không bịa công thức: lấy Ando / Arevalo / Haghighi / Harmony SI / MATH_NOTES.  
3. Hình: **screenshot từ PDF đã tải + caption cite** (tác giả, năm, số hình). Không generate hình “minh họa giả” thay số liệu paper.  
4. Agent chỉ viết file trong thư mục role được giao + Nhật ký.
