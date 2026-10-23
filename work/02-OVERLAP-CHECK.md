# Kiểm tra overlap (Integrator)

**Trạng thái:** DONE — 2026-10-18  
**Nguồn:** `work/role-a/TODOS.md` (43 todos), `work/role-b/TODOS.md` (48), `work/role-c/TODOS.md` (32) · `work/00-COORDINATION-MAP.md` §2 · `SPLIT_PLAN.md` D1–D3 · `OUTLINE.md` §0

## Checklist

| Kiểm tra | Kết quả | Ghi chú (evidence) |
|----------|---------|---------------------|
| A không sở hữu Lasso/MLP / MoA fusion | **PASS** | Khóa đầu file + mọi todo ghi «Không overlap»: B cross-modal, C MoA (vd. A-P1-01, A-P5-07 vs B percent predictable). Chỉ **cite** Haghighi alignment ở A-P3-02; không deliverable Lasso/fusion. A-P8-02 cấm claim Lasso. |
| B không sở hữu chứng minh TVN/sphering dài / JUMP Arevalo chính | **PASS** | Cover B §1: «không deep-dive batch/sphering»; B-101, B-901–902: **không triển khai** TVN/sphering, chỉ đọc MATH_NOTES §1–3 + nhận `shared/cp_profiles_post_batch_*`. B-201: JUMP benchmark **cấm** (Role A). Không todo Harmony/ComBat/TVN implement. |
| C không sở hữu implement Lasso / mediation làm trụ / MoA trên TA-ORF | **PASS** | Header C + bảng §5: TA-ORF **cấm** MoA; C-P2-ALIGN-01 gọi **API B**, không `lasso_mlp_*`. C-GUARD-02 / C-P3-MOA-02: mediation **không** PP chính (MATH_NOTES §8). Không todo TVN proof (chỉ nhận CP từ A). |
| Giới thiệu Rosetta/CP+L1000 chung (~3–5 tr) — OK, không chiếm đề | **PASS** | A-P8-01 (shared, không L1000 sâu); B-101 Fig.1 mức 1 slide; C-P1-03/04 pipeline A/B/C. SPLIT_PLAN §B + COORDINATION-MAP §2 cho phép; mỗi role có bảng số riêng (A benchmark batch, B Fig.2–3, C Fig.4). |
| Interface phụ thuộc A → B → C được document | **PASS** | **A→B:** A-P1-04 export schema; A-P3-02 handoff; A-P6-10 `cp_profiles_spherized_v0/v1` → B-901–902. **B→C:** B-304 `shared/perturbation_keys_*` → C-P2-MOA-01; B-601 metric → C-P2-ALIGN-01 API. **C orchestrate:** C-P2-ALIGN-03/04 trước/sau CP version A. |
| Mọi todo có PDF local + DOI hoặc «xác nhận Fig khi mở PDF» | **PASS** | Spot-check 43+48+32: mọi block có `Paper (PDF local)` + DOI hoặc placeholder Fig (A-P1-02, A-P5-04 SI). B-304/B-901 thiếu paper — đúng deliverable nội bộ; không vi phạm khóa nội dung. |
| Mọi todo phương pháp trỏ MATH_NOTES hoặc công thức paper | **PASS** | A: §1–3, §5 (A-P5-*, A-P7-02). B: §4 (B-401–601, B-804). C: §6–7, §8 guard (C-P2-MOA-*, C-P2-SIM-*). |
| Data có lệnh/URL từ DATA.md hoặc Haghighi portal | **PASS** | A-P1-01, A-P6-01: `aws s3 sync` + DATA.md §1.2; B-201 cùng lệnh; C-P2-MOA-01; A-P8-01 broad.io/rosetta. |
| Map → Đồ án Phần 1/2/3 đủ mục SPLIT_PLAN D1–D3 | **PASS** | A-P7-01…03 + map §VIII → D1 1.1–1.5, 2.1–2.6, 3.1–3.5. B PHẦN 11 bảng → D2 đủ + B-1001–1003. C §7 bảng C-P1/P2/P3 → D3 1.1–1.5, 2.1–2.6, 3.1–3.5. |
| Không số liệu bịa ngoài OUTLINE §0 / paper | **PASS** | TA-ORF ~4,7%/5,5% chỉ B-704, B-602, B-1004 với Fig.2b/OUTLINE §0; A không gán số Way cho Rosetta (A-P2-01, A-P8-02); C-P2-ALIGN-05 «không generate số giả». |

## Rủi ro dư (WARN — không FAIL)

| WARN | Mitigation |
|------|------------|
| **Screenshot trùng** Haghighi Fig.1 (layout Rosetta): A-P8-01, B-101, slide ĐA mở đầu B/C | Mỗi deck ≤1 slide; caption khác góc (A=CP scope, B=subset, C=pipeline); ưu tiên 1 bản trong slides NCKH chung. |
| **Fig. 2b** percent predictable: B owns bảng tái lập; C-P2-ALIGN-* cite cùng hình cho API | C slide chỉ mô tả metric + bảng **Δ trước/sau batch** nhóm; không copy cột Rosetta của B. |
| **Way complementary**: A-P1-03, B-105, C-P1-02 | B-105 gắn nhãn «Way = compound»; C không claim MoA Way; không dùng Way cho ORF (OUTLINE §0). |
| **`data/inventory.md` chung** A-P6-01 / B-202 | Cột/section theo role (A CP, B L1000+4 subset); Integrator giữ 1 file, 3 section headers. |
| **CDRP/LINCS subset** A benchmark CP vs C MoA | Cùng path gallery; bảng metric khác (A: mAP/percent replicating; C: Jaccard/F1). |
| **Complementary định nghĩa** lặp Phần 1 B vs C | B: shared subspace + prediction; C: fusion MoA + alignment — SPLIT_PLAN 1.4 B vs 1.2–1.3 C. |

## Verdict cuối

**PASS** — Khóa COORDINATION-MAP §2 được tuân trong ba file TODOS; không có todo **sở hữu chính** vi phạm (A/B/C cấm). Interface A→B→C và Rosetta intro chung đã gắn todo cụ thể. Rủi ro còn lại là trùng **minh họa** (WARN), xử lý khi duyệt outline slides ĐA.

**Không có FAIL cần parent sửa TODOS** — tiếp tục NCKH + outline slides ĐA tại `work/thesis-synthesis/thesis-*-SLIDES-OUTLINE.md`.
