# 规则闭环映射表

| 新规则 | 触发条件 | 必填证据 | 阻断条件 | 责任文件 |
| :--- | :--- | :--- | :--- | :--- |
| 部门会议 | 用户上传文件、旧稿、此前生成稿、失败证据后进入生产/修复/恢复生产 | 部门会议记录；副主编；1-2名员工；员工中文名；输入材料；内部一致结论 | 只有副主编、无员工、无中文名、未内部一致 | `SKILL.md`, `01-team-roles.md`, `02-workflow.md`, `16-multi-agent-governance.md`, `00-production-gate.md` |
| 交付文件初始备忘录 | 全部部门会议有效后 | 输入材料、旧稿可继承/不可继承项、关键页清单、内容/UI/动效/工程/QA口径、冲突解决 | 备忘录缺失或无部门签署 | `SKILL.md`, `01-team-roles.md`, `02-workflow.md`, `10-version-evidence.md` |
| 工作平台关键页试生产 | 初始备忘录完成后，正式全稿生产前 | 关键页工单、平台成员、每个适用部门至少1名员工、关键页输出、文件所有权映射 | 直接生产全稿、平台缺部门员工、无`PROCESS_READY_WORK_PLATFORM` | `19-approved-production-flow.md`, `00-production-gate.md`, `16-multi-agent-governance.md`, `07-qa-checklist.md` |
| 关键页副主编初审/复审 | 关键页试生产后 | 各副主编初审结论、退回项、同一副主编复审、全部一致同意 | 任一副主编未审、退回后未复审、只由打回副主编同意 | `19-approved-production-flow.md`, `01-team-roles.md`, `02-workflow.md` |
| 总编关键页初审 | 全部副主编一致同意后 | 总编同意/退回记录；退回后工作平台修复和副主编复审记录 | 总编未同意就正式生产 | `19-approved-production-flow.md`, `SKILL.md`, `02-workflow.md` |
| 正式生产工作平台 | 总编关键页初审同意后 | 正式全稿制作工单、正式平台编制、交付记录、文件所有权映射 | 缺任一适用部门员工或主Agent直接生产 | `SKILL.md`, `00-production-gate.md`, `01-team-roles.md`, `16-multi-agent-governance.md` |
| 中文名称 | 建立任何subagent、部门员工或平台成员时 | 中文名称 + agent id/专员证据；默认名称清单；“蔻豆码”等职责名 | 使用Agent1、worker、审查员A等泛名 | `01-team-roles.md`, `16-multi-agent-governance.md`, `00-production-gate.md`, `agents/openai.yaml` |
| QA前置阻断 | 进入截图、Playwright、validation、QA冻结前 | 部门会议、初始备忘录、关键页试生产、工作平台、实现后复核、副总编/总编记录 | 缺任一关键流程证据 | `07-qa-checklist.md`, `10-version-evidence.md` |

## 本地检查

- `openai.yaml` 已通过 Ruby YAML 解析。
- Markdown 表格列数检查未发现 header/delimiter 不一致。
- 残留扫描显示旧链路关键词已清理到只保留状态约束语境。
