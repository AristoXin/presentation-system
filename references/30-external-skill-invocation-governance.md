---
id: R30
title: External Skill Invocation Governance
applies_to:
  - production
  - visual_design
  - style_frame
  - html
  - ppt
  - motion
  - design_dna
  - guizang
  - last30days
  - failure_recovery
gates:
  - G4
  - G5
  - G6
  - G6A
  - G7
  - G8
required_outputs:
  - SkillAvailabilityScan
  - SkillInvocationLedger
  - SkillAbsorptionMatrix
  - ManualEquivalentRecord
  - SkillCapabilityBlocker
---

# External Skill Invocation Governance

## Principle

Named Skills are not decorative references. If the production system says a task requires design-dna, PPT DNA, guizang, StyleKit, Taste, frontend-slides, html-ppt, huashu, ppt-master, humanize-ppt, or last30days search, Codex must not silently replace those Skills with its own default implementation.

Canonical IDs come from `skills/visual-skill-registry.json`. Aliases such as
PPT DNA, StyleKit, Taste, html-ppt-skill-main, humanize-ppt-main, huashu-ppt,
huashu-slides, last30days, and last30days-skill are input aliases only. Runtime
ledger, absorption, manifest, installer, and verifier records must use the
canonical IDs.

Every required Skill must be resolved into one state.

| State | Meaning |
| --- | --- |
| called | The Skill/tool was actually invoked and produced output |
| manual_equivalent | The Skill was unavailable, but an approved manual equivalent record was produced |
| not_applicable | The Skill was considered and rejected with a task-specific reason |
| blocked | The Skill is required but unavailable; production must stop or ask for capability setup |

## No Self-Implementation Rule

Invalid: claiming guizang without output, design-dna without DNA fields, Taste without anti-template preflight, last30days without query/source list, motion design without state matrix, or writing HTML first and inventing a Skill absorption table afterward.

## Absorption Requirement

A Skill output is not absorbed until it affects downstream production fields.

| Skill | Minimum absorption evidence |
| --- | --- |
| design-dna | DNA mapped to visual tokens, page family, motion grammar |
| guizang | layout/Sxx or equivalent route mapped to pages |
| Taste | anti-template review, design dials, forbidden patterns |
| StyleKit | style candidates, adopted/rejected style, quality gate |
| frontend-slides | HTML stage, animation pattern, interaction assumptions |
| html-ppt | theme/layout/animation mapping |
| huashu-design | visual direction exploration and motion review |
| last30days | source list, extracted patterns, adopt/reject table |

Reading a Skill description is not absorption. Mentioning a Skill name is not absorption. Copying a template is not absorption.

## Installation Assistance

If a user downloads `presentation-system` without the companion Skills installed, Codex must help resolve the missing capabilities before Production.

Minimum sequence:

1. Run or ask the user to run `bash skills/verify-skills.sh`.
2. For public GitHub-backed Skills known to this repository, run or offer `bash skills/install-skills.sh --install-missing`.
3. For local, private, connector, MCP, API-key, or account-bound capabilities, explain the exact missing item and ask for user consent or credentials before setup.
4. Re-run `bash skills/verify-skills.sh` after installation.
5. Record each Skill as `called`, `manual_equivalent`, `not_applicable`, or `blocked`.

If installation is declined, unavailable, or cannot be verified, do not continue as if the Skill was available. Use `SkillCapabilityBlocker` or an approved `ManualEquivalentRecord`.
