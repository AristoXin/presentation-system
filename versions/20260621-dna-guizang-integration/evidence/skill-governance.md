# Skill治理证据：Design DNA × guizang 深度集成

> 日期：2026-06-21  
> 状态：Skill治理可写 / 未创建产物 / 未恢复生产

## 用户最新要求锁定表

| 编号 | 用户最新原话摘要 | 禁止事项 | 验收标准 | 是否覆盖旧要求 | 执行理解 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U1 | “还是skill写的不好，审美、ui等等还是没有深度集成guizang dna等skill。” | 不得继续生成新版本；不得只在入口写“调用guizang/design-dna”；不得用读取Skill冒充吸收 | Skill必须把design-dna、guizang、审美、UI、动效变成统一的必填证据、阻断条件和QA字段 | 是 | 需要新增深度集成合同，并接入入口、生产总闸门、审美/UI、动效、Skill治理和QA | 已闭环 |
| U2 | “stylekit-skill。这些skill不是也要集成进去吗？你先看一下有哪些skill是相关的吧。而且应该集成进去。现在最大的问题还是排版、ui不好看/动效设计十分单一。” | 不得只集成guizang/design-dna；不得忽略stylekit/taste/frontend-slides/html-ppt/huashu-design；不得用单一动效继续生产 | 先盘点相关Skill，再把相关Skill写入决策表、吸收合同、生产闸门和QA字段 | 是 | 需要新增Design Skill Stack合同，明确stylekit、taste、design-dna、guizang、frontend-slides、html-ppt、huashu-design的职责和吸收证据 | 已闭环 |
| U3 | “补齐联网搜索 / 外部参考 / 最新文档 / 浏览器视觉验证能力。” | 不得生成产物；不得只依赖本地参考库冒充联网 | Tavily/Brave/Firecrawl/Context7/Playwright工具链进入reference、门禁、QA和verify | 是 | 新增Online Research Toolchain合同并接入Design Skill Stack和HTML Pre视觉导演 | 已闭环 |
| U4 | “缺少的控件…直接帮用户进行安装…提请用户同意…用户拒绝，则该skill直接停止。建立subagent不需要经过用户同意，必须建立。” | 不得自动安装；不得拒绝后继续；不得再问是否允许创建subagent | 缺失控件安装提请记录；拒绝即阻断；subagent默认必建 | 是 | 收紧工具缺失和subagent治理口径 | 已闭环 |

## 历史对话需求整合表

| 编号 | 用户历史要求/退回原话摘要 | 触发的问题类型 | 必须写入的Skill规则 | 影响文件 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H-V014-02 | “审美、ui等等还是没有深度集成guizang dna等skill。” | design-dna/guizang/UI/审美/动效集成失败 | 新增Presentation Design DNA档案、DNA来源追踪、guizang桥接、UI吸收、动效吸收、QA吸收检查；只读取Skill、写风格名、写Sxx编号不算深度集成 | `20-design-dna-guizang-integration.md`及入口/门禁文件 | 已修 |
| H-V014-03 | “stylekit-skill…有哪些skill是相关的…现在最大的问题还是排版、ui不好看/动效设计十分单一。” | 设计Skill栈未成体系 | 新增Design Skill Stack决策表；stylekit/taste/frontend-slides/html-ppt/huashu-design必须有调用/不调用/降级和吸收证据；动效单一必须有Motion source map | `21-design-skill-stack-integration.md`及入口/门禁文件 | 已修 |

## 规则闭环映射表

| 新增/修改规则 | 触发条件 | 必填证据 | 阻断条件 | 责任部门 | 写入文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Design DNA × guizang深度集成硬门禁 | HTML/PPT/Slides、Style Frame、审美退回、用户质疑DNA/guizang未集成 | Presentation Design DNA档案、DNA来源追踪、UI吸收表、动效吸收表、设计引擎桥接表 | 只有JSON/风格名/Sxx编号/读过Skill | 品牌审美、版式/UI、动效、QA | `SKILL.md`、`20-design-dna-guizang-integration.md` |
| 生产总闸门接入 | 完整视觉生产或Style Frame | `20`规定的吸收证据 | 未完成吸收合同不得生产 | 总编、副总编、工具链 | `00-production-gate.md` |
| 审美/UI接入 | 视觉系统、版式、审美、Style Frame | DNA和guizang落到页面族谱、组件、视觉重心 | 只停留在形容词或模板标签 | 品牌审美、版式/UI | `04-design-standards.md`、`11-aesthetic-anti-ai.md` |
| 动效接入 | HTML演示、分步、转场、guizang动效 | 动效吸收表、运动语法、首态/后续态、export稳定态 | 统一fade/rise或默认transition | 动效设计 | `17-motion-design-standards.md` |
| QA接入 | 冻结、审美QA、截图验证 | 深度集成合同字段和吸收结论 | 工程烟测冒充DNA/guizang吸收 | QA | `07-qa-checklist.md` |
| 历史治理固化 | 用户指出Skill没集成 | H-V014-02历史要求 | 只写当前失败审计，不改跨项目reference | 总编、Skill治理 | `18-history-derived-governance.md` |
| Design Skill Stack集成 | 排版/UI不好看、动效单一、stylekit等Skill未集成 | Design Skill Stack决策表、StyleKit吸收合同、TasteSkill吸收合同、Motion source map、Skill Stack QA字段 | 只列Skill名称；只写style slug；只写读过Skill；动效来源不清 | 品牌审美、版式/UI、动效、工具链、QA | `21-design-skill-stack-integration.md`、`SKILL.md`、`00-production-gate.md`、`07-qa-checklist.md` |
| Online Research Toolchain集成 | 联网搜索、外部参考、当前趋势、最新文档、浏览器视觉验证、HTML Pre审美退回 | Online Research Stack决策表、外部参考搜索记录、外部视觉参考转译卡、最新文档检索记录、Playwright视觉验证记录、缺失控件安装提请记录 | 工具不可用却假装完成；用户拒绝安装/授权后继续；本地参考库冒充联网搜索 | 工具链、品牌审美、交互工程、QA | `22-html-pre-visual-director.md`、`23-online-research-toolchain.md`、`08-skill-governance.md`、`skills/verify-skills.sh` |

## 本轮未做事项

- 未创建或修改任何HTML/PPT/PDF/截图包。
- 未恢复V0.14A/B生产。
- 未运行Playwright截图或validation。
