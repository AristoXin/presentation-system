# V6.3 Failure Hardening Skill Revision Summary

日期：2026-06-20

## 失败承认

- V0.9 不是合格的多轮subagent复核：它有生产前子代理意见，但没有把真实HTML、截图和validation交回同一副主编subagent做实现后复核。
- V0.10 是用户退回后的主线程快速修复，不应被视为有效交付或合格恢复生产。
- 自动验证通过只证明工程烟测，不证明审美、排版舒适度或用户可接受。
- 读取参考库和设计Skill不等于真正使用；缺少页面映射、弃用理由和实现后复核时，不能宣称Skill已生效。

## 本次修订目标

1. 阻断“预审=复核”的漏洞。
2. 阻断“工程烟测通过=QA通过”的漏洞。
3. 阻断“用户退回后快速改CSS继续生产”的漏洞。
4. 增加视觉舒适度门禁，特别是黑/白/高饱和蓝等强反差混用、明度硬切和中文排版压迫。
5. 明确交付措辞：缺少实现后复核、QA冻结或用户验收时，必须写未冻结/未交付/阻断。

## 修改文件

- `presentation-system/SKILL.md`
- `presentation-system/AGENTS.md`
- `presentation-system/references/00-production-gate.md`
- `presentation-system/references/01-team-roles.md`
- `presentation-system/references/04-design-standards.md`
- `presentation-system/references/07-qa-checklist.md`
- `presentation-system/references/08-skill-governance.md`
- `presentation-system/references/10-version-evidence.md`
- `presentation-system/references/11-aesthetic-anti-ai.md`
- `presentation-system/references/15-visual-reference-library.md`
- `presentation-system/references/16-multi-agent-governance.md`
- `presentation-system/references/18-history-derived-governance.md`

## 恢复生产前置条件

除非用户明确要求恢复生产，否则不得继续生成HTML/PPT/PDF或截图包。恢复生产前必须重新建立真实subagent编制、先产出Style Frame或Page Spec，并在实现后完成副主编复核与QA冻结。
