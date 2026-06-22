---
id: R27
title: Anti Template Governance
applies_to:
  - production
  - visual_design
  - html
  - ppt
  - style_frame
  - failure_recovery
gates:
  - G7C
  - G8
required_outputs:
  - AntiTemplateReview
  - PageFamilyDiversityReport
---

# Anti Template Governance

## Principle

A deck is not good because it is consistent. It is good when consistency and variation serve the story.

Template-like output is a production failure when pages feel interchangeable.

## Common Template Failures

Challenge repeated title-plus-card pages, repeated two-column layouts, repeated glass panels, repeated gradient backgrounds, repeated icon-card matrices, repeated left-nav/right-content shells, equal-width cards regardless of hierarchy, generic timelines, generic dashboards, generic consulting decks, generic AI neon/gradient looks, and repeated fade/rise animation.

## Hard Failure

If more than 50% of pages share the same layout family without explicit narrative reason, stop with `TEMPLATE_PATTERN_BLOCKER`.

If all motion uses the same entrance pattern, stop with `MOTION_TEMPLATE_BLOCKER`.
