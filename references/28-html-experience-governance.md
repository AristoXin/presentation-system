---
id: R28
title: HTML Experience Governance
applies_to:
  - production
  - html
  - interactive_slides
  - html_ppt
  - failure_recovery
gates:
  - G7D
  - G8
required_outputs:
  - HTMLExperienceContract
  - HTMLStateModel
  - InteractionModel
  - ExportPrintStableState
---

# HTML Experience Governance

## Principle

HTML presentation is not a static PPT simulation. Formal HTML implementation requires an HTML Experience Contract.

At minimum, define slide state, reveal state, navigation state, keyboard behavior, wheel/touch behavior, replay/back behavior, reduced-motion behavior, and export/print stable state.

## Static PPT Risk

If implementation only contains `.slide.active`, `nextSlide()`, `prevSlide()`, static slide divs, uniform fade-in, no page-specific state, no reduced-motion, and no export/print mode, mark `STATIC_PPT_HTML_RISK`.

Do not QA Freeze until corrected or explicitly justified.
