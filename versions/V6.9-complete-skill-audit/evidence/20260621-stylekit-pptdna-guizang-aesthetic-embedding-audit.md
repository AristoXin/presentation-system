# 20260621 StyleKit / PPT-DNA / guizang 审美嵌入审计

## 用户最新要求锁定表

| 字段 | 内容 |
| :--- | :--- |
| 时间 | 2026-06-21 12:51:57 CST |
| 用户原话摘要 | 用户要求全面检查 presentation-system skill，确认 StyleKit、PPT-DNA/design-dna、guizang 已合理嵌入，尤其是审美嵌入、版式/UI部门协作和避免产物很丑的机制。 |
| 禁止事项 | 不创建、不复制、不修改HTML/PPT/PDF/截图包/交付产物；不只做口头确认；不能把Skill调用等同于审美吸收。 |
| 验收标准 | 入口触发、部门职责、工作流、设计标准、Style Frame、QA、版本证据、Skill可用性、manifest/lock、元数据均形成闭环。 |
| 执行理解 | 本次是Skill治理与完整审计，不是产物生产。只允许修改Skill系统文件和治理证据。 |

## 完整Skill审计矩阵

| 审计面 | 结论 | 证据路径 |
| :--- | :--- | :--- |
| 入口触发 | 已覆盖“审美、排版、不要丑、StyleKit、PPT-DNA、guizang、完整Skill审计”等触发 | `presentation-system/SKILL.md`、`presentation-system/AGENTS.md`、`presentation-system/agents/openai.yaml` |
| 视觉参考库 | 已新增StyleKit、PPT-DNA、guizang三条可检索设计库入口，并定义通用/专用、不可照搬、转译规则 | `presentation-system/references/visual/reference-entries.md`、`presentation-system/references/15-visual-reference-library.md` |
| 品牌审美部门 | 已明确负责StyleKit审美意图、PPT-DNA design_style、guizang A/B适配和视觉母线 | `presentation-system/references/01-team-roles.md`、`presentation-system/references/11-aesthetic-anti-ai.md` |
| 版式/UI部门 | 已明确负责StyleKit token/组件、PPT-DNA design_system、guizang layout/Sxx逐页映射 | `presentation-system/references/01-team-roles.md`、`presentation-system/references/04-design-standards.md` |
| 动效部门 | 已补齐PPT-DNA visual_effects、guizang动效recipe/低功耗策略、StyleKit状态转译职责 | `presentation-system/references/01-team-roles.md`、`presentation-system/references/11-aesthetic-anti-ai.md` |
| 部门协同 | Style Frame协同输入表已要求语言内容、品牌审美、版式/UI、动效、交互、QA分别输入并解决冲突 | `presentation-system/references/01-team-roles.md`、`presentation-system/references/11-aesthetic-anti-ai.md` |
| 工作流 | 参考经验转译卡已加入StyleKit、PPT-DNA、guizang吸收字段 | `presentation-system/references/02-workflow.md` |
| QA | 审美QA已检查“已读取未吸收 / 已提取未吸收 / 已选模板未吸收”，并要求截图和人工复核 | `presentation-system/references/07-qa-checklist.md` |
| 版本证据 | 已要求最终版本附StyleKit、PPT-DNA、guizang吸收证据；缺失则不得审美通过或冻结 | `presentation-system/references/10-version-evidence.md` |
| Skill治理 | 已定义调用决策、吸收标准、降级审批和不可用处理 | `presentation-system/references/08-skill-governance.md` |
| manifest/lock | 已把StyleKit、PPT-DNA、guizang锁定到本地真实Skill路径和verify命令 | `presentation-system/skills/skills.manifest.yaml`、`presentation-system/skills/skills.lock.json` |
| 元数据 | 已同步UI触发描述，明确deep aesthetics/layout、StyleKit/PPT-DNA/guizang absorption | `presentation-system/agents/openai.yaml` |

## 规则闭环映射表

| 用户关注 | 触发条件 | 必填证据 | 阻断条件 | 责任部门 | 写入文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| StyleKit是审美组件 | Style Frame、风格候选、设计库校准、用户点名StyleKit | 查询词、候选slug、采用/弃用理由、design_brief、composition_plan、quality_gate、意图/token/状态转译 | 只有slug、prompt、style_choice，标记“已读取未吸收” | 品牌审美、版式/UI、动效、QA | `04`、`07`、`08`、`10`、`11`、`reference-entries` |
| PPT-DNA深入审美/UI | 用户提供参考图、旧稿、品牌规范、要求深度审美或不要丑 | design_system、design_style、visual_effects、页面族谱、组件规范、动效/降级映射 | 只有JSON或形容词，标记“已提取未吸收” | 品牌审美、版式/UI、动效、QA | `01`、`02`、`04`、`07`、`08`、`10`、`11` |
| guizang深入版式/主题节奏 | HTML/PPT视觉生产、瑞士风/杂志风、分步演示、主题节奏 | A/B适配理由、弃用方向理由、主题节奏、逐页layout/Sxx映射、图片槽位、模板改造差异、校验/截图 | 只有风格名、模板路径、Sxx编号，标记“已选模板未吸收” | 品牌审美、版式/UI、动效、交互、QA | `01`、`02`、`04`、`07`、`08`、`10`、`11` |
| 部门协作真实发生 | 完整视觉生产、Style Frame、用户质疑部门失效 | 部门一致意见、Style Frame部门协同输入、冲突解决、一级复核、同一副主编复审 | 缺任一适用部门输入，只能称视觉草图或流程阻断 | 副总编、全部副主编、QA | `01`、`02`、`07`、`11`、`16`、`19` |
| 避免很丑/模板感 | 审美退回、完整视觉生产、用户要求提升审美 | 参考经验转译、视觉母线、页面族谱、光学平衡、主题节奏、截图人工复核 | 卡片套皮、低对比、光学失衡、无真实锚点、连续模板页 | 品牌审美、版式/UI、QA | `04`、`07`、`10`、`11`、`15` |

## 修订影响面清单

| 文件 | 本次确认/修订 |
| :--- | :--- |
| `presentation-system/references/01-team-roles.md` | 补齐动效设计副主编对PPT-DNA visual_effects和guizang动效recipe/低功耗策略的职责。 |
| `presentation-system/skills/skills.manifest.yaml` | 将PPT-DNA与guizang从占位源更新为真实本地路径、local install、verify命令和非license阻断。 |
| `presentation-system/skills/skills.lock.json` | 新增PPT-DNA与guizang锁定记录。 |
| `presentation-system/agents/openai.yaml` | 更新触发描述，加入deep aesthetics/layout和StyleKit/PPT-DNA/guizang absorption。 |
| 其他核心reference | 审计确认已覆盖入口、审美、UI、工作流、QA和证据链。 |

## 本地验证记录

| 验证项 | 结果 |
| :--- | :--- |
| `bash presentation-system/skills/verify-skills.sh` | 通过；StyleKit、PPT-DNA/design-dna、guizang均为`availability=available`且verify已配置。 |
| `ruby -rjson -e "JSON.parse(File.read('presentation-system/skills/skills.lock.json'))"` | 通过；lock JSON合法。 |
| `rg`覆盖检查 | 通过；StyleKit、PPT-DNA、guizang、吸收失败标记、部门协同、Style Frame、QA、证据规则均在入口和reference中可检索。 |
| 产物边界 | 本次未创建、复制、修改、截图、导出任何HTML/PPT/PDF/截图包或正式交付物。 |

## 审计结论

当前skill已形成闭环：审美组件不是只被“调用”，而是必须被品牌审美、版式/UI、动效、交互和QA转译、复核、留证。若后续项目只记录Skill名称、风格名、JSON或模板编号，而没有当前用户资料驱动的页面族谱、组件语法、主题节奏、动效脚本和截图QA，将被规则标记为未吸收并阻断。
