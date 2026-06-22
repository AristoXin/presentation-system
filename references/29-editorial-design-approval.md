---
id: R29
title: Editorial Design Approval
applies_to:
  - production
  - visual_design
  - html
  - ppt
  - style_frame
  - failure_recovery
gates:
  - G5
  - G7E
  - G8
required_outputs:
  - EditorialDesignBoard
  - DepartmentDraftRecords
  - DeputyEditorConsensusRecord
  - EditorInChiefApprovalRecord
  - FormalProductionHandoff
---

# Editorial Design Approval

## Principle

Visual production must follow editorial approval, not single-agent self-approval.

The main agent must not directly create final artifacts before the editorial design chain has produced and approved a non-final reference draft.

## Required Sequence

Input intake -> Department drafts -> Deputy editor review -> Deputy editor consensus -> Editor-in-chief review -> Non-final reference draft -> Formal Production handoff -> Implementation -> Post-implementation review -> QA Freeze or return.

## Departments

| Department | Required Output | Veto Power |
| --- | --- | --- |
| Content Creation | Narrative map, page intent, copy hierarchy | Can block unclear story |
| UI Design | UI direction, page family system, component grammar | Can block template-like layout |
| Aesthetic Review | Visual thesis, anti-AI flavor review | Can block ugly/generic visuals |
| Motion Design | Motion grammar, state matrix | Can block static-PPT behavior |
| Interaction Engineering | HTML experience model | Can block unstable/non-interactive HTML |
| QA / Records | Evidence checklist, screenshot plan | Can block unsupported claims |

## Invalid Bypass

Invalid bypasses include direct final HTML before department drafts, CSS first and rationale afterward, department roles only in final summary, deputy editors approving without artifacts, editor-in-chief approval without record, or Formal Production without handoff.

Invalid bypass output may be kept only as failure evidence or rough scratch, not deliverable.
