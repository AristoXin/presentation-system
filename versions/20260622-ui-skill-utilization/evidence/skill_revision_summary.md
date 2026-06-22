# Skill Revision Summary: UI Department Skill Utilization

Date: 2026-06-22

## User Requirement Lock

User requirement: "UI设计部门会不会调用huashu-ppt等等，你应该确保skill得到充分的运用。"

Execution understanding:

- UI/layout cannot rely only on generic grid, typography and alignment checks.
- UI/layout must explicitly judge and use or reject relevant presentation skills, including `huashu-ppt` / `huashu-slides` / `huashu-slide-codex`.
- `huashu`-related skills must not be treated as only a language or narrative tool; they also affect brand asset protocol, visual direction candidates, page type density, image-PPT path choice and material handling.
- "Fully used" means adopted skill outputs are translated into Page Specs, production work orders, real artifact paths and QA fields; otherwise the result is only "read, not absorbed."

## Rule Closure Mapping

| Trigger | Required evidence | Blocking condition | Responsible department | Updated files | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| UI/layout department forms initial direction for PPT/Slides/visual storytelling | Department Skill Usage Matrix; huashu applicability decision; adoption/rejection reason | UI does not judge `huashu-ppt`/`huashu-slides` when task involves slides, image PPT, brand assets, visual variants or page density | Layout/UI deputy editor, brand aesthetic deputy editor | `SKILL.md`, `AGENTS.md`, `references/21-design-skill-stack-integration.md`, `references/16-multi-agent-governance.md` | `rg "部门Skill使用矩阵|huashu-ppt|huashu-slides|huashu-slide-codex"` |
| Formal production uses design skills | Page Spec mapping, work order, template adaptation/diff, artifact paths, QA fields | Skill output remains a name, slogan, or unused reference; no production-level proof | Layout/UI, motion, interaction, QA | `references/21-design-skill-stack-integration.md` | `rg "未充分使用|图片PPT路径|品牌资产协议"` |

## Revision Summary

- Added `huashu-ppt` / `huashu-slides` / `huashu-slide-codex` into the Design Skill Stack as a brand-asset and image-PPT path engine.
- Added a Department Skill Usage Matrix covering brand aesthetic, layout/UI, motion, interaction/engineering and QA.
- Updated Layout/UI responsibilities so UI must judge guizang, frontend-slides, html-ppt and huashu-related paths before direction approval.
- Updated entry rules so missing UI skill-use evidence blocks initial direction and production.
