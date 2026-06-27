# 规则闭环映射表

| 触发条件 | 必填证据 | 阻断条件 | 责任部门 | 更新文件 |
| :--- | :--- | :--- | :--- | :--- |
| 用户质疑HTML排版、UI、动效、subagent复检或提出工作平台 | 用户最新要求锁、失败审计、规则闭环映射 | 继续生成产物、截图或validation | 总编、工具链与上下文工程副主编 | `SKILL.md`、`AGENTS.md`、`00-production-gate.md` |
| 制作工单准备进入真实产物生成 | 工作平台编制表、工作平台交付记录、文件所有权映射、`PROCESS_READY_WORK_PLATFORM` | 未启用工作平台、无跨部门员工、主Agent直接生产 | 总编、工作平台协调员、各能力域副主编 | `01-team-roles.md`、`16-multi-agent-governance.md`、`19-approved-production-flow.md` |
| 工作平台完成产物 | 真实文件路径、源码路径、截图/验证证据、交回副主编记录 | 工作平台自审、自签、越权改标准 | 工作平台协调员、原责任副主编 | `16-multi-agent-governance.md`、`07-qa-checklist.md` |
| QA准备截图、Playwright、validation或冻结 | Subagent Evidence Lock、实现后复核、工作平台证据 | 缺少subagent或工作平台证据 | QA副主编 | `07-qa-checklist.md`、`00-production-gate.md` |
| 修改/退回/用户复验失败 | 副主编问题归因、工作平台修订工单、同一副主编复审、全部适用副主编一致审核 | 主Agent直接修、只由打回副主编同意后继续 | 总编、对应副主编、工作平台 | `19-approved-production-flow.md`、`AGENTS.md` |

## 验证方式

使用`rg`检查`工作平台`、`PROCESS_BLOCKED_NO_WORK_PLATFORM`和`PROCESS_READY_WORK_PLATFORM`是否贯穿入口、团队职责、流程图、生产门禁、QA和Agent提示文件。

## 本轮产物边界

本轮未创建、修改、截图或验证HTML/PPT/PDF交付产物。所有新增文件均为Skill治理证据。

## 跨项目生效声明

自本治理版本起，工作平台门禁跨项目生效，适用于后续所有HTML/PPT/PDF/Slides/Vx正式生产、修复、Style Frame探索、截图、Playwright、validation、归档和候选交付。任何项目只要缺少真实subagent证据、制作工单、工作平台编制表、工作平台交付记录或文件所有权映射，都必须停止为`PROCESS_BLOCKED_NO_WORK_PLATFORM`或`BLOCKED_BY_SUBAGENT`，不得以“样张”“工作稿”“小修”“工程烟测”“未冻结稿”为名继续生成或提交。
