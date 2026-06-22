---
id: R24
title: User Asset Intake and Adaptation
applies_to:
  - production
  - visual_design
  - html
  - ppt
  - user_uploaded_files
  - failure_recovery
gates:
  - G3
  - G7A
  - G7C
  - G8
required_outputs:
  - SourceMaterialIntake
  - AssetToPageMapping
  - AssetStyleExtraction
  - AssetGapAndFallbackPlan
---

# User Asset Intake and Adaptation

## Principle

User-provided files are not passive references. Uploaded PPT/PDF/Word/Excel/images/logos/screenshots/templates must affect page structure, visual anchors, UI grammar, motion decisions, and QA evidence.

The agent must not ignore source files and produce a generic deck.

## Required Tables

### Source Material Intake

| Asset | Type | Source | Quality | Usability | Limitation | Used in final? |
| --- | --- | --- | --- | --- | --- | --- |

### Asset to Page Mapping

| Asset | Supports content | Page / family | Page role | Visual anchor | Motion implication | QA evidence |
| --- | --- | --- | --- | --- | --- | --- |

### Asset Style Extraction

| Source | Extractable style | Must not copy | Influence on color/type/layout/motion | Applies to |
| --- | --- | --- | --- | --- |

### Asset Gap and Fallback Plan

| Page | Missing asset | Design impact | Fallback | QA blocker? |
| --- | --- | --- | --- | --- |

## Failure

If user assets do not affect the design system, stop with `ASSET_ABSORPTION_BLOCKER`.
