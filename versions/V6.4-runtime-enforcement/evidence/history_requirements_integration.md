# 历史对话需求整合表 - V6.4 Runtime Enforcement

> 日期：2026-06-20  
> 触发原因：用户指出主Agent未调用subagent、未按流程图、违背skill强制规定，并在未完成团队流程时继续生成V0.11。

## 结论

当前失败不是单个HTML版本质量问题，而是Skill运行时执行约束失败：已有规则写了“必须”，但没有在每次文件修改、样张创建、截图验证前形成不可绕过的停止条件。后续修订必须把“无真实subagent即不得改产物”升级为运行时硬锁，而不是最终回复里的状态说明。

## 历史对话需求整合表

| 编号 | 用户历史要求/退回原话摘要 | 触发的问题类型 | 必须写入的Skill规则 | 影响文件 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H1 | “你没有调用subagent，你完全没有按照流程图的要求来” | subagent/流程图 | 用户质疑subagent后，同项目任何生产、修复、小修、截图、验证都必须先创建真实subagent；未创建时禁止改产物 | `SKILL.md`, `00-production-gate.md`, `16-multi-agent-governance.md`, `18-history-derived-governance.md` | 已修 |
| H2 | “不是你一句没有冒充的问题” | 降级/状态口径 | 不允许用“未冻结/结构探索稿/工程样张/未冒充”作为绕过流程的解释；若流程缺失，必须回滚到失败审计和Skill治理，不得保留为有效新版本 | `00-production-gate.md`, `10-version-evidence.md`, `18-history-derived-governance.md` | 已修 |
| H3 | “你在脱离我设定的框架” | 用户要求一致性 | 每次用户新增要求必须先进入《用户最新要求锁定表》，由subagent和QA核对后才能执行；主Agent不得自行解释为小修并跳过流程 | `SKILL.md`, `07-qa-checklist.md`, `18-history-derived-governance.md` | 已修 |
| H4 | “最终导致结果不如人意” | QA/复核 | QA发现无subagent实现后复核时，应立即判定流程阻断，不得继续跑截图验证或把烟测结果写入可验收版本 | `07-qa-checklist.md`, `10-version-evidence.md`, `16-multi-agent-governance.md` | 已修 |
| H5 | “根据新的完善后的skill，生成新的版本” | 生产恢复 | 用户要求生成新版本不等于批准跳过流程；在已有失败/质疑历史下，恢复生产必须先有真实subagent编制和恢复生产批准记录 | `19-approved-production-flow.md`, `00-production-gate.md`, `18-history-derived-governance.md` | 已修 |
| H6 | “下方操作栏应该是中文+图标……一并更新skill” | 小修/Skill治理混合 | 当请求同时包含产物修改和Skill修订时，必须先分流：Skill治理可继续；产物修改必须等subagent与流程图闭环完成。不得边修Skill边创建HTML版本 | `SKILL.md`, `18-history-derived-governance.md`, `08-skill-governance.md` | 已修 |

## 当前V0.11状态判定

| 项目 | 判定 |
| :--- | :--- |
| 是否按流程图创建真实subagent闭环 | 否 |
| 是否应作为有效新版本 | 否，仅可作为流程失败证据 |
| 是否允许继续基于V0.11生产 | 否，进入`FAILED_VISUAL_FREEZE` |
| 下一步允许动作 | Skill治理、失败审计、流程硬锁修订、等待用户明确恢复生产 |
