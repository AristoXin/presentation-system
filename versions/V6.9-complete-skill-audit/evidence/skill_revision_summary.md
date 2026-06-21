# V6.9 Skill修订摘要

## 修订目标

把“完整检查和更新Skill”固化为可重复执行的Skill治理路径，避免未来只在入口文档补规则，却没有贯穿reference、QA和版本证据。

## 已完成更新

| 文件 | 更新内容 |
| :--- | :--- |
| `SKILL.md` | 新增完整Skill审计硬门禁、路由行和最低交付标准 |
| `AGENTS.md` | 新增Skill治理工作顺序和治理结论口径 |
| `00-production-gate.md` | 新增完整Skill审计任务等级、检查项和审计矩阵 |
| `10-version-evidence.md` | 新增完整Skill审计证据字段和证据规则 |
| `18-history-derived-governance.md` | 新增H-V014-01，记录用户本轮完整检查要求 |
| `agents/openai.yaml` | 更新描述和默认提示，使完整审计成为明确触发场景 |

## 从此跨项目生效的新增经验

1. 用户要求完整检查Skill时，不能只补入口规则，必须查入口、流程、部门、内容、UI、审美、动效、QA、证据、经验回写、元数据和验证脚本。
2. 每条硬规则必须绑定触发条件、必填证据、阻断条件、责任部门、更新文件和验证方式。
3. Skill治理任务不得创建或修改交付产物；如果需要恢复生产，必须重新获得用户明确批准并通过生产门禁。

## 验证结果

| 检查 | 结果 |
| :--- | :--- |
| `bash presentation-system/skills/verify-skills.sh` | 通过 |
| 安装PyYAML | 通过：已向Codex捆绑Python安装`PyYAML 6.0.3` |
| `quick_validate.py presentation-system` | 通过：返回`Skill is valid!` |
| frontmatter解析 | 通过 |
| `agents/openai.yaml`解析 | 通过 |
| 关键词贯通检查 | 通过 |
