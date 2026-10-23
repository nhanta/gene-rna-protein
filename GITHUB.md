# GitHub: `main` + 3 nhánh — clone & chạy trước bảo vệ

## 1. Cấu trúc nhánh khuyến nghị

```text
main                 # ổn định: shared/, slides NCKH, data docs, CI nhẹ
├── branch_a         # Đồ án A — sphering/batch CP
├── branch_b         # Đồ án B — Lasso/MLP cross-modal
└── branch_c         # Đồ án C — fusion MoA + alignment
```

**Quy tắc:**

1. Mọi thay đổi vào `shared/` → PR vào **`main`** trước; A/B/C rebase/merge `main` hàng tuần.  
2. Kết quả/bảng số riêng chỉ nằm trong `branch_a|b|c` (hoặc `results/a|b|c/` trên main nếu đã review).  
3. **Không** force-push `main`.  
4. Tag: `nckh-2027-03` khi nộp slides NCKH; `thesis-a-v1` / `thesis-b-v1` / `thesis-c-v1` khi khóa luận văn.

### Layout thư mục (monorepo)

```text
shared/           # loader Rosetta, metrics, config — sở hữu chung
branch_a/         # code + notebook A (cũng có thể chỉ tồn tại trên branch_a)
branch_b/
branch_c/
data/             # DATA.md; raw/ trong .gitignore
slides/
docs/             # OUTLINE, PLAN, SPLIT_PLAN
```

Trên GitHub có thể giữ cả ba thư mục `branch_*` trên `main` (đơn giản cho clone một lần) **hoặc** chỉ có trên nhánh tương ứng. Khuyến nghị cho 3 SV: **giữ cả ba trên `main`**, dùng nhánh git để PR/review — dễ clone một lệnh trước BV.

---

## 2. Tạo repo (một lần, người điều phối)

```bash
# sau khi có remote
git checkout -b main
git push -u origin main

git checkout -b branch_a
git push -u origin branch_a
git checkout main
git checkout -b branch_b && git push -u origin branch_b
git checkout main
git checkout -b branch_c && git push -u origin branch_c
git checkout main
```

Bảo vệ `main`: require PR + 1 review (nếu GitHub cho phép).

---

## 3. Quy trình hàng tuần của mỗi người

```bash
git checkout branch_a   # hoặc b/c
git fetch origin
git merge origin/main   # hoặc: git rebase origin/main nếu nhóm thống nhất
# ... code ...
git push origin branch_a
# mở PR branch_a → main chỉ khi có thay đổi shared/ hoặc kết quả đã chốt
```

---

## 4. Clone sạch & chạy trước bảo vệ (checklist hội đồng)

Làm trên máy **khác** hoặc folder mới (tránh “chạy được vì rác local”):

```bash
git clone <URL_REPO> rosetta-cellular-check
cd rosetta-cellular-check
git checkout main
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt

# Data: theo data/DATA.md (AWS CLI sync curated Rosetta)
# Chỉ tải subset cần cho demo (LUAD hoặc LINCS) nếu máy yếu

# Mục tiêu T1: thêm stub shared/smoke_test.py và branch_*/smoke_test.py
# Hiện repo có thể chưa có module — khi đã có:
python -m shared.smoke_test
git checkout branch_a && python -m branch_a.smoke_test
git checkout branch_b && python -m branch_b.smoke_test
git checkout branch_c && python -m branch_c.smoke_test
```

**Tiêu chí “sạch” (khi đã có smoke):** từ clone → xong A/B/C **≤ 45–60 phút** (không kể lần đầu tải data).  
Ghi thời gian vào `notes/repro-log.md` trước BV. Xem thêm `NOTES_GAPS.md`.

---

## 5. Secrets & data lớn

- Không commit file `.parquet` / profile đầy đủ.  
- `data/raw/` trong `.gitignore`.  
- README ghi **đúng lệnh** `aws s3 sync --no-sign-request ...` (đã có trong `data/DATA.md`).

---

## 6. Sau NCKH — tách đồ án

- Luận văn A/B/C: mỗi người một repo fork **hoặc** giữ monorepo, xóa quyền ghi nhánh người khác.  
- Cite NCKH chung trong lời mở đầu (mẫu trong `SPLIT_PLAN.md`).  
- Số liệu trong luận văn = tag `nckh-2027-03` hoặc commit hash ghi trong phụ lục.
