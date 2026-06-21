# V6.9 历史需求整合

## 用户最新要求锁定表

| 编号 | 用户最新原话摘要 | 禁止事项 | 验收标准 | 是否覆盖旧要求 | 执行理解 | 冲突/阻断 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U1 | “请你对skill进行完整检查和更新。” | 不只修当前特定客户项目；不得只补一两条入口规则；不得继续生成新版产物 | 完整检查Skill入口、reference、QA、动效、审美、文案、团队协作、证据链和元数据，并更新可复用规则 | 是 | 本轮只做Skill治理和证据回写，不创建/修改HTML/PPT/PDF/截图包 | 无 | 已闭环 |

## 历史对话需求整合表

| 编号 | 用户历史要求/退回原话摘要 | 触发的问题类型 | 必须写入的Skill规则 | 影响文件 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H1 | 上一版提出的问题一个没解决 | 跨版本回归/QA | 下一版前必须有《上一版问题关闭矩阵》；未关闭则`FAILED_VISUAL_FREEZE` | `SKILL.md`、`AGENTS.md`、`07-qa-checklist.md`、`10-version-evidence.md` | 已修 |
| H2 | 明显问题没有更新设计参考文档 | 经验回写 | 用户点名明显失败必须回写长期reference，而不是当前项目记录 | `15-visual-reference-library.md`、`18-history-derived-governance.md` | 已修 |
| H3 | 别的项目也不能出现这些问题 | 跨项目硬红线 | 光学失衡、分步提前露出、动效生硬、页面丑和部门空转成为所有视觉项目通用否决项 | `04-design-standards.md`、`11-aesthetic-anti-ai.md`、`17-motion-design-standards.md` | 已修 |
| H4 | V12问题到V13仍存在 | 失败冻结/流程阻断 | 旧问题未逐项关闭时，不得称新版候选或可验收 | `00-production-gate.md`、`19-approved-production-flow.md` | 已修 |
| H5 | 完整检查和更新Skill | Skill治理/完整审计 | 完整审计必须覆盖入口、流程、部门、内容、UI、审美、动效、QA、证据、经验回写、元数据和验证脚本 | `SKILL.md`、`AGENTS.md`、`00-production-gate.md`、`10-version-evidence.md`、`agents/openai.yaml` | 已修 |

## 产物范围确认

本轮为Skill治理可写任务。允许修改Skill系统文件和治理证据；不得创建、复制、修改、截图或导出交付产物目录。
