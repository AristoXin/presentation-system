# Skill Revision Summary: Initial Direction Skill Stack

Date: 2026-06-22

## User Requirement Lock

User requirement: "我认为在部门初始确认方向时，就应该调用构成的skill，比如应该@taste-skill @guizang-ppt-skill @PPT-Design-DNA-main等等，这样才能保证初始方向不走偏（注意，内部审美策略也需要调用），后续进入正式生产平台时也需要调用这些skill。"

Execution understanding:

- Department initial direction confirmation must call or equivalently absorb the constituent design skills before the direction is accepted.
- `taste-skill` must contribute its internal aesthetic strategy, not only a surface-level anti-template label.
- The formal production platform must call or verify those skills again against concrete Page Specs, work orders, artifacts and QA fields.
- Initial direction evidence and production evidence are separate; one cannot replace the other.

## Rule Closure Mapping

| Trigger | Required evidence | Blocking condition | Responsible department | Updated files | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Department initial direction for HTML/PPT/Slides/visual storytelling | Initial direction skill call record, internal aesthetic strategy absorption table, department consensus table with skill evidence | Missing stage-A skill evidence, available relevant skill not called without reason, unavailable required skill without install/blocker record | Chief editor, deputy editor, brand aesthetic, layout/UI, motion, interaction, QA | `SKILL.md`, `AGENTS.md`, `references/21-design-skill-stack-integration.md`, `references/19-approved-production-flow.md` | `rg "阶段A|初始方向Skill|内部审美策略"` |
| Formal production platform before work order/artifact creation | Stage-B skill verification, Page Spec links, work order links, template adaptation/diff, artifact paths, QA fields | Reusing initial direction notes as production proof, production engine replacing rather than carrying the accepted direction | Deputy editor, execution lead, QA | `SKILL.md`, `AGENTS.md`, `references/21-design-skill-stack-integration.md`, `references/19-approved-production-flow.md` | `rg "阶段B|正式生产平台Skill|二次调用"` |

## Revision Summary

- Added a two-stage hard gate to the Design Skill Stack reference.
- Added required Stage A artifacts: initial direction skill call record and internal aesthetic strategy absorption table.
- Added required Stage B proof: production skill re-call/verification against Page Specs, work orders, real artifacts and QA fields.
- Updated the production flow diagram so both stages are explicit nodes in the mandatory flow.
