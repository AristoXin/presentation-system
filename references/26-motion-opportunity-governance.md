---
id: R26
title: Motion Opportunity Governance
applies_to:
  - production
  - html
  - interactive_slides
  - motion
  - failure_recovery
gates:
  - G7B
  - G7D
  - G8
required_outputs:
  - MotionOpportunityMap
  - MotionStateMatrix
  - StaticPageJustification
---

# Motion Opportunity Governance

## Principle

Motion is not decoration. Motion is a narrative instrument.

Every page must be classified before implementation.

| Classification | Meaning |
| --- | --- |
| motion-required | Without motion, the page loses meaning, pacing, attention guidance, or comprehension |
| motion-optional | Motion can improve experience but is not required |
| intentionally-static | Static composition better supports reading, comparison, pause, or emphasis |

## Motion-Required Situations

Check motion opportunity for process evolution, before/after comparison, cause-effect chains, timelines, layered architectures, data/insight reveal, risk escalation, decision paths, user journeys, competitive comparison, story turning points, progressive teaching, model construction, spatial relationships, and concept discovery.

## Static Can Be Designed

Static can be correct when the audience must compare items simultaneously, the page is dense reference material, the speaker needs a pause, the page functions as an anchor, motion would distract from reading, or export/print quality is more important.

Static pages still require design. Static does not mean default layout.

## Blocker

If a page is motion-required but implemented as static without justification, the artifact fails.

If more than 40% of pages are motion-required but no page-specific state matrix exists, stop with `MOTION_DESIGN_BLOCKER`.
