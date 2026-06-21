# Comprehensive Skill Audit

Version: V6.7-comprehensive-skill-governance

## Audit Conclusions

| Area | Finding | Revision |
| :--- | :--- | :--- |
| Entry routing | The skill entry had become too heavy and could over-trigger full production governance. | Added task modes and made OpenAI invocation explicit/conservative. |
| Progressive disclosure | "Read minimally" conflicted with broad mandatory preloads. | Clarified read-only audit vs writable governance vs production requirements. |
| Failure recovery | Failure freeze, Style Frame evidence, and recovery production were semantically mixed. | Added three recovery states and synchronized them across `SKILL`, `00`, `11`, and `19`. |
| Production gates | Pre-production and post-production evidence were mixed into one circular final gate. | Split `00-production-gate` into production-before release and freeze/delivery release. |
| Page count | Page count could still be inherited from old versions/templates. | Strengthened page sufficiency as cross-department blocker before Page Spec and design engine. |
| UI aesthetics | Optical balance was named but lacked evidence format. | Required marked screenshots or three-zone records with visual-weight evidence. |
| Motion | Motion rules did not require verifiable specs. | Added duration/easing/delay/trigger/settle time and step-state evidence. |
| QA | QA step 0 incorrectly required real subagent evidence and blocker evidence simultaneously. | Corrected to either `SEL-real` or complete downgraded blocker route. |
| Delivery route | Default HTML rule was duplicated across many files. | Consolidated authority in `03-delivery-routing.md`; other files reference it. |
| Visual references | The detailed reference library lived outside top-level references. | Added `references/visual/reference-entries.md` to Skill audit routing. |
| Failure evidence | Failure archive could be confused with new Vx versions. | Added `versions/failed-evidence/<timestamp>/` as non-Vx evidence path. |

## Residual Cleanup Recommendation

After V6.7, the next maintenance pass should reduce duplicated table definitions for Style Frame, subagent evidence, and QA boundary fields. V6.7 prioritized behavioral correctness and user-reported failure modes first.
