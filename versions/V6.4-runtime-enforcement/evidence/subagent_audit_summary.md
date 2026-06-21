# Subagent审计汇总 - V6.4 Runtime Enforcement

> 日期：2026-06-20  
> 触发：用户指出主Agent未调用subagent、未按流程图、违背Skill强制规定并导致结果不如人意。  
> 范围：只审计Skill系统文件和治理证据；不修改HTML/PPT/PDF/截图包。

## 真实Subagent记录

| 角色 | Agent id | 结论摘要 | 是否修改文件 |
| :--- | :--- | :--- | :--- |
| 多Agent治理副主编 | `019ee529-d947-77a1-8cc9-51e67a4588be` | 没有真实subagent证据就没有Vx版本；未冻结/候选/样张不能降低生产门槛 | 否 |
| 生产恢复与失败停产副主编 | `019ee52a-08f2-7b01-9222-32712a75de6a` | `FAILED_VISUAL_FREEZE`后必须执行产物冻结锁；旧HTML和截图包只能作为失败证据 | 否 |
| 用户要求一致性与QA副主编 | `019ee52a-2390-77c1-af6c-74079c02d541` | 必须新增用户最新要求锁；QA第0步发现无subagent应立即阻断，不得跑烟测 | 否 |

## 合并后的修订方向

| 漏洞 | 修订动作 | 文件 |
| :--- | :--- | :--- |
| 用“未冻结/样张/小修”绕过流程 | 新增Vx版本原子门禁，任何Vx/HTML/PPT/PDF/截图动作都视为生产 | `SKILL.md`, `00-production-gate.md`, `10-version-evidence.md` |
| RACI表或口头角色冒充subagent | 新增Subagent Evidence Lock和Agent编制扩展字段 | `SKILL.md`, `16-multi-agent-governance.md`, `00-production-gate.md` |
| 用户最新要求被主Agent解释替代 | 新增《用户最新要求锁定表》 | `SKILL.md`, `18-history-derived-governance.md`, `00-production-gate.md` |
| 无subagent仍继续工程烟测 | 新增QA第0步流程阻断，禁止Playwright/截图/validation | `07-qa-checklist.md`, `00-production-gate.md` |
| FAILED_VISUAL_FREEZE后继续派生旧版 | 新增产物冻结锁，旧产物只能作为失败证据 | `19-approved-production-flow.md`, `18-history-derived-governance.md`, `10-version-evidence.md` |

## 当前V0.11处理建议

V0.11应登记为`V0.11-invalidated / FAILED_VISUAL_FREEZE / FROZEN_FAILED_EVIDENCE`。在用户明确要求前，不删除、不覆盖、不继续小修；后续生产不得以V0.11为母版或起点。

