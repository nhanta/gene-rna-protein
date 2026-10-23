# Subagents & phối hợp

## Vai trò agent

| Agent | Output | Không được sửa |
|-------|--------|----------------|
| Role-A planner | `work/role-a/TODOS.md` | role-b, role-c |
| Role-B planner | `work/role-b/TODOS.md` | role-a, role-c |
| Role-C planner | `work/role-c/TODOS.md` | role-a, role-b |
| Integrator | `work/02-OVERLAP-CHECK.md` + `work/thesis-synthesis/*` | không đổi ownership lock trong `00-COORDINATION-MAP.md` trừ Nhật ký |
| Slide writer (sau) | `slides/thesis-a|b|c/` | chỉ sau khi TODOS + overlap check PASS |

## Bus

Mọi agent đọc `00-COORDINATION-MAP.md` trước. Ghi Nhật ký §4 sau khi xong.

## Thứ tự

1. Ba Role planner **song song**  
2. Integrator (chống overlap + map → slides đồ án)  
3. (Sau khi user duyệt TODOS) mới viết slides đồ án từng role  

## Skill tham chiếu (repo ngoài)

- BioAlgo: `bioalgo-content-qc`, `bioalgo-vi-prose-repair`, `outlook-vi-glossary`  
- UI slides nhóm: Bio-Infras Pitch Deck  
