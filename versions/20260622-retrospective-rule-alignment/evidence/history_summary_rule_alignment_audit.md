# 历史总结新规则对齐矩阵

## 复盘范围

本轮枚举并复盘`versions/*/evidence/*.md`下所有历史总结和治理证据。旧evidence不被重写为“当时已满足新规则”；它们作为历史事实保留，并通过本矩阵标注现行、补强、历史快照或被新规则覆盖。

## 新规则轴

| 规则轴 | 当前承载文件 | 复盘结论 |
| :--- | :--- | :--- |
| 初始方向Skill栈 | `SKILL.md`、`AGENTS.md`、`references/21-design-skill-stack-integration.md`、`references/19-approved-production-flow.md` | 已固化为阶段A和正式生产阶段B的双重证据要求 |
| 全部门Skill矩阵 | `SKILL.md`、`AGENTS.md`、`references/16-multi-agent-governance.md`、`references/21-design-skill-stack-integration.md` | 已覆盖需求/交付、语言内容、品牌审美、版式/UI、动效、交互工程、QA |
| huashu充分使用 | `references/21-design-skill-stack-integration.md`、`references/08-skill-governance.md` | 已从UI单部门扩展为全部门适用性判断 |
| 正向参考图深拆 | `SKILL.md`、`AGENTS.md`、`references/04-design-standards.md`、`references/15-visual-reference-library.md`、`references/21-design-skill-stack-integration.md` | 已要求配色、文字、字体、版面、跨页、替代方案、动效、交互和HTML状态机拆解 |
| HTML状态机与交互合同 | `SKILL.md`、`AGENTS.md`、`references/06-interaction-standards.md`、`references/17-motion-design-standards.md`、`references/07-qa-checklist.md` | 已阻断“点一下出现下一项”的PPT模拟式动效 |
| 历史总结对齐 | `SKILL.md`、`AGENTS.md`、`references/10-version-evidence.md`、`references/18-history-derived-governance.md` | 本轮新增；以后必须逐项枚举历史evidence并标注状态 |

## Evidence逐项对齐

| evidence路径 | 原始主题 | 新规则覆盖项 | 当前状态 | 处理结论 |
| :--- | :--- | :--- | :--- | :--- |
| `versions/20260621-dna-guizang-integration/evidence/online_toolchain_governance.md` | 联网工具链和HTML Pre治理 | 联网/浏览器验证、HTML Pre、正式生产阻断 | 仍然现行，已被HTML状态机规则补强 | 保留；由`06`、`17`、`23`继续约束 |
| `versions/20260621-dna-guizang-integration/evidence/public-sanitization-audit.md` | 对外发布脱敏 | GitHub公开同步与敏感信息边界 | 仍然现行 | 保留；不直接承担新设计规则 |
| `versions/20260621-dna-guizang-integration/evidence/skill-governance.md` | Design DNA、guizang、StyleKit等集成 | 初始方向Skill栈、正式生产二次调用、全部门矩阵 | 已被新规则补强 | 保留；由`21`和本轮矩阵覆盖更细部门责任 |
| `versions/20260622-all-department-skill-utilization/evidence/skill_revision_summary.md` | 全部门Skill使用 | 全部门矩阵、huashu跨部门适用、正式生产二次调用 | 现行 | 保留，作为当前规则证据 |
| `versions/20260622-html-motion-interaction-state-machine/evidence/skill_revision_summary.md` | HTML动效与交互状态机 | HTML状态机、焦点/aria、输入节流、export稳定态 | 现行 | 保留，作为当前规则证据 |
| `versions/20260622-initial-direction-skill-stack/evidence/skill_revision_summary.md` | 初始方向Skill调用 | taste、guizang、PPT-DNA、内部审美策略、阶段B复核 | 现行 | 保留，作为阶段A/B规则证据 |
| `versions/20260622-positive-campaign-deck-reference/evidence/skill_revision_summary.md` | 正向多页参考学习 | 多页视觉系统拆解、UI/动效等多部门协同 | 现行，已被深拆表补强 | 保留；与正向深拆证据共同使用 |
| `versions/20260622-positive-reference-deep-analysis/evidence/skill_revision_summary.md` | 正向参考图详细拆解 | 配色、文字、字体、版面、跨页、替代方案、动效、交互 | 现行 | 保留，作为当前规则证据 |
| `versions/20260622-ui-skill-utilization/evidence/skill_revision_summary.md` | UI部门huashu等Skill使用 | huashu、guizang、frontend-slides、html-ppt由UI判断 | 已被全部门规则补强 | 保留历史事实；由`all-department`证据覆盖“不能只由UI判断” |
| `versions/V6.2-skill-governance-hardening/evidence/skill_revision_summary.md` | 早期Skill治理硬化 | 入口、证据、治理闭环 | 历史快照，已被V6.9和本轮补强 | 保留，不单独作为最新完成证明 |
| `versions/V6.3-failure-hardening/evidence/skill_revision_summary.md` | 失败治理硬化 | 失败冻结、阻断、复盘 | 历史快照，已被V6.5/V6.8/V6.9补强 | 保留 |
| `versions/V6.4-runtime-enforcement/evidence/history_requirements_integration.md` | 历史要求整合 | subagent、运行时阻断 | 历史快照，仍可引用 | 保留 |
| `versions/V6.4-runtime-enforcement/evidence/subagent_audit_summary.md` | subagent审计 | 多Agent硬门禁 | 历史快照，已被`16`和`19`补强 | 保留 |
| `versions/V6.4-runtime-enforcement/evidence/user_latest_requirements_lock.md` | 用户要求锁 | 用户最新要求优先 | 仍然现行 | 保留 |
| `versions/V6.5-visual-motion-failure-governance/evidence/failure_audit_v012.md` | V12/V13视觉和动效失败 | 光学平衡、分步状态、动效美感、部门失效 | 仍然现行 | 保留为跨项目失败样例 |
| `versions/V6.5-visual-motion-failure-governance/evidence/history_requirements_integration.md` | 失败要求整合 | 设计/动效/QA硬红线 | 仍然现行 | 保留 |
| `versions/V6.5-visual-motion-failure-governance/evidence/skill_revision_summary.md` | 视觉动效失败治理 | 动效美感、首态/后续态、QA否决 | 现行，已被HTML状态机补强 | 保留 |
| `versions/V6.5-visual-motion-failure-governance/evidence/user_latest_requirements_lock.md` | 用户失败反馈锁 | 用户点名问题优先级 | 仍然现行 | 保留 |
| `versions/V6.6-page-sufficiency-governance/evidence/page_sufficiency_gap_audit.md` | 页数充分性缺口 | 跨部门页数判断 | 仍然现行 | 保留 |
| `versions/V6.6-page-sufficiency-governance/evidence/skill_revision_summary.md` | 页数充分性规则 | 页数不足阻断、增拆合删页判断 | 仍然现行 | 保留 |
| `versions/V6.6-page-sufficiency-governance/evidence/user_latest_requirements_lock.md` | 用户页数要求锁 | 页数不默认沿用旧版 | 仍然现行 | 保留 |
| `versions/V6.7-comprehensive-skill-governance/evidence/comprehensive_skill_audit.md` | 综合Skill审计 | 入口、部门、QA、证据链 | 历史快照，已被V6.9和本轮补强 | 保留 |
| `versions/V6.7-comprehensive-skill-governance/evidence/history_requirements_integration.md` | 历史要求整合 | 跨项目治理 | 历史快照，仍可引用 | 保留 |
| `versions/V6.7-comprehensive-skill-governance/evidence/skill_revision_summary.md` | 综合治理修订 | 多部门和证据闭环 | 历史快照，已补强 | 保留 |
| `versions/V6.7-comprehensive-skill-governance/evidence/subagent_audit_summary.md` | subagent审计 | 多Agent责任 | 历史快照，已被`16`/`19`补强 | 保留 |
| `versions/V6.7-comprehensive-skill-governance/evidence/user_latest_requirements_lock.md` | 用户要求锁 | 用户原话优先 | 仍然现行 | 保留 |
| `versions/V6.8-cross-project-failure-learning/evidence/history_requirements_integration.md` | 跨项目失败学习 | 失败经验回写 | 仍然现行 | 保留 |
| `versions/V6.8-cross-project-failure-learning/evidence/skill_revision_summary.md` | 跨项目规则沉淀 | 参考库、QA、动效跨项目硬红线 | 仍然现行 | 保留 |
| `versions/V6.9-complete-skill-audit/evidence/20260621-stylekit-pptdna-guizang-aesthetic-embedding-audit.md` | StyleKit/PPT-DNA/guizang审美嵌入 | 深度审美、UI、动效、技能吸收 | 现行，已被初始方向和全部门规则补强 | 保留 |
| `versions/V6.9-complete-skill-audit/evidence/comprehensive_skill_audit.md` | 完整Skill审计 | 完整审计矩阵 | 现行，已被本轮加入历史总结对齐项 | 保留并补强 |
| `versions/V6.9-complete-skill-audit/evidence/history_requirements_integration.md` | 历史需求整合 | 完整检查、跨项目硬红线 | 现行 | 保留 |
| `versions/V6.9-complete-skill-audit/evidence/skill_revision_summary.md` | 完整Skill审计修订摘要 | 入口、流程、部门、证据、元数据 | 现行，已被本轮复盘矩阵补强 | 保留 |

## 结论

所有历史总结均已被重新整理到当前规则轴下：旧证据不被伪造为“当时已满足新规则”，而是通过本矩阵明确其现行状态和覆盖关系。当前可作为最新规则证明的证据集中在`20260622-*`、`V6.9-*`和本轮`20260622-retrospective-rule-alignment`；更早版本作为历史快照保留。
