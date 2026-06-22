---
id: R25
title: Design Synthesis Governance
applies_to:
  - production
  - visual_design
  - html
  - ppt
  - style_frame
  - failure_recovery
gates:
  - G5
  - G7A
  - G7E
  - G8
required_outputs:
  - DesignSynthesisContract
  - PageFamilySystem
  - PreCodeVisualFreeze
---

# Design Synthesis Governance

## Principle

Visual production is not coding-first. Content Creation, UI Design, Aesthetic Review, Motion Design, Interaction Engineering, and QA must be integrated into one coherent design system before implementation begins.

A design is not approved merely because each department says pass. It is approved only when their decisions form a unified narrative, UI, visual, motion, and interaction system.

## Required Department Inputs

| Department | Required Input | Must Answer |
| --- | --- | --- |
| Content Creation | Narrative spine, page intent, message hierarchy | What should the audience understand, feel, compare, decide, or remember? |
| UI Design | Page family system, layout grammar, component grammar | What UI structure best expresses the content relationship? |
| Aesthetic Review | Visual thesis, taste direction, anti-AI flavor risks | What should this look and feel like, and what must it not look like? |
| Motion Design | Motion purpose, reveal strategy, motion grammar | Where should motion serve understanding, attention, pacing, or surprise? |
| Interaction Engineering | State model, navigation model, export mode | How does HTML behave as an experience system rather than static slides? |
| QA / Records | Evidence requirements and blockers | How will the design be verified before final delivery? |

## No Parallel Checklist Rule

Invalid: each department writes notes separately, then Codex writes HTML directly.

Valid sequence: department inputs -> Design Synthesis Contract -> conflict resolution -> page family system -> motion opportunity map -> anti-template review -> HTML experience contract -> editorial approval -> pre-code visual freeze -> implementation.

## Blocker

If Design Synthesis Contract, Page Family System, Motion Opportunity Map, and Anti-Template Review are missing, stop with `DESIGN_SYNTHESIS_BLOCKER`.
