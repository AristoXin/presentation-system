---
id: R21
title: Design Skill Stack Integration
applies_to:
  - design_skill_stack
  - stylekit
  - taste
  - frontend_slides
  - layout_failure
gates:
  - G1
  - G4
  - G7
  - G8
required_outputs:
  - DesignSkillStackDecision
  - SkillAvailabilityScan
  - SkillInvocationLedger
  - SkillAbsorptionMatrix
---

# 21-design-skill-stack-integration

读取时机：当任务涉及部门初始确认方向、完整视觉生产、Style Frame、HTML/PPT/Slides、审美退回、排版/UI不好看、动效单一，或用户质疑“stylekit/design-dna/guizang/taste/frontend-slides/html-ppt/huashu-design等Skill没有集成”时读取。本文件定义演示设计相关Skill的分层、双阶段调用顺序、吸收证据和QA阻断。

## 核心问题

演示设计失败通常不是因为缺一个模板，而是因为多个设计Skill各自孤立：StyleKit给了风格，DNA给了字段，guizang给了版式，动效Skill给了动画，但没有被统一成页面族谱、UI语法、运动语法和QA证据。本文件要求在部门初始确认方向时先完成设计Skill栈调用与吸收，再进入Style Frame或全稿生产；正式生产平台启动前还必须二次调用/复核，不能把初始方向记录当作生产证据。

## Named Skill Invocation Is Mandatory

本文件中列出的 Skill 不是风格参考，也不是概念标签。

当某 Skill 被判定为当前任务相关时，必须进入以下四态之一：

- called
- manual_equivalent
- not_applicable
- blocked

禁止第五种状态：Codex 自己做了但声称等价调用。

以下情况视为失败：

- 没有调用 guizang，却声称 guizang 已吸收。
- 没有 design-dna 输出，却声称已有 Design DNA。
- 没有 Taste 预检，却声称完成反模板审美。
- 没有 last30days 搜索，却声称结合最新趋势。
- 没有 frontend-slides/html-ppt 适配表，却声称 HTML 体验已承接。
- 没有 Skill Absorption Matrix，却声称 Skill 栈已集成。

Skill 调用必须先于 Style Frame、Page Spec、HTML/CSS/JS/PPT/PDF 实现。

## 双阶段调用硬门禁

### 阶段A：部门初始确认方向

在需求与交付、语言内容、品牌审美、版式/UI、动效设计、交互工程和QA形成《部门一致意见表》之前，必须调用或人工等价吸收构成当前视觉方向的相关Skill。默认需要判断并记录：

- `stylekit-skill`：给出风格候选、采用/弃用理由、style ownership和quality_gate。
- `taste-skill`：调用其内部审美策略，完成Design Read、三拨盘、反模板排版预检、重复版式禁用和动效/色彩/卡片红线。
- `PPT-Design-DNA-main` / `design-dna`：形成Presentation Design DNA、来源追踪、UI吸收和动效吸收。
- `guizang-ppt-skill`：在方向层判断主题节奏、版式语法、A/B路线适配与弃用边界；此时不得直接套模板。
- `frontend-slides`、`html-ppt`、`huashu-design`、`huashu-ppt` / `huashu-slides`、客户母版或其他实现Skill：按交付路线判断是否参与方向候选、页面族谱、动画语法、图片PPT路径或交互约束。

阶段A的必填证据是《初始方向Skill调用记录》《内部审美策略吸收表》和带Skill证据列的《部门一致意见表》。可用但未调用必须写“为什么当前方向不需要”；不可用但方向依赖它时，必须按`08-skill-governance.md`记录安装/启用请求或阻断。缺少阶段A证据时，副总编不得接收部门初始方向，总编不得批准进入交付定义、页面族谱或Style Frame。

### 阶段B：正式生产平台

在制作工单下发、HTML/PPT/PDF/截图包创建、Style Frame扩展为全稿或任何Vx版本动作前，必须基于已确定的Page Spec、内容到UI/动效转译表和模板改造差异表，二次调用/复核阶段A采用的Skill。阶段B必须证明：

- 初始方向中的StyleKit/Taste/DNA/guizang等结论已经落到逐页Page Spec、主题节奏、layout/Sxx映射、动效语法和QA字段。
- 生产引擎只承接已确认方向，不重新替代方向；若生产阶段发现Skill输出与内容冲突，必须退回阶段A重新协商，而不是执行层自行改CSS或换模板。
- 阶段B证据不能复用阶段A截图或摘要，必须引用当前版本的真实Page Spec、工单、源码路径、截图或验证结果。

缺少阶段B证据时，不得创建全稿产物，不得称为候选稿、冻结稿或可验收版本。

## 相关Skill分层

| 层级 | Skill | 主要作用 | 必须吸收为 | 不合格信号 |
| :--- | :--- | :--- | :--- | :--- |
| 风格候选与质量门 | `stylekit-skill` / `stylekit-style-prompts` | 检索/选择/混合StyleKit风格，生成design_brief、composition_plan、quality_gate | 风格候选表、采用/弃用理由、风格所有权、quality_gate修复项 | 只记录slug、prompt或“用了StyleKit” |
| 反模板排版预检 | `taste-skill` / `design-taste-frontend` | Design Read、DESIGN_VARIANCE/MOTION_INTENSITY/VISUAL_DENSITY三拨盘、layout repetition ban、pre-flight | 排版/UI反模板预检表、拨盘、重复版式禁用、字体/色彩/卡片/动效红线 | 继续用居中hero、三卡片、统一动效、通用紫渐变 |
| 设计身份 | `design-dna` / `PPT-Design-DNA-main` | design_system、design_style、visual_effects三维身份 | Presentation Design DNA档案、DNA来源追踪、UI吸收表、动效吸收表 | 只有JSON或形容词，没有页面级落地 |
| 演示版式引擎 | `guizang-ppt-skill` | 电子杂志/瑞士国际主义、主题节奏、layout/Sxx、分步演示语法 | A/B适配与弃用表、逐页layout/Sxx映射、主题节奏、改造差异 | 只说瑞士风/杂志风，或自造未登记版式 |
| HTML动画演示引擎 | `frontend-slides` | 固定1920x1080舞台、3个Style Preview、动画丰富的单文件HTML演示 | 16:9固定舞台规则、3方向视觉预览、density模式、动画pattern | 做成长网页、没有视觉预览、内容溢出或动效单薄 |
| 模板型HTML PPT引擎 | `html-ppt` | 36主题、31 layout、full-deck templates、27 CSS动画和20 canvas FX | 主题/layout/animation映射、模板适配和改造表、演讲者模式规则 | 从零手写、随意换主题、动画类随便套 |
| 高保真变体/动画专家 | `huashu-design` | 设计方向顾问、三套逻辑并行视觉、反AI slop、动画/MP4/GIF、专家评审 | 三方向可视化探索、品牌资产协议、动画导演/连续运动叙事、五维评审 | 只出一版、无真实视觉对比、动画像PPT淡入 |
| 图片PPT/品牌资产协议引擎 | `huashu-ppt` / `huashu-slides` / `huashu-slide-codex` | 内容结构化、品牌资产协议、3个设计方向、图片PPT/Keynote/HTML图片deck、封面/配图路径 | 品牌资产协议、页面类型密度分级、3方向候选、图片/HTML/PPTX路径选择、项目内素材归档规则 | UI部门只说“不用图片PPT”、没有判断品牌资产协议、没有页面类型密度分级、没有路径弃用理由 |

## 部门Skill使用矩阵

部门不是只签署“通过”，而是要证明自己调动了对应Skill能力。每个适用部门在阶段A和阶段B都必须填写本矩阵；可用但不调用必须写理由，不可用但必要必须阻断。

| 部门/副主编 | 默认必须判断的Skill | 阶段A吸收证据 | 阶段B生产证据 | 未充分使用信号 |
| :--- | :--- | :--- | :--- | :--- |
| 需求与交付 | `ppt-master`、`frontend-slides`、`html-ppt`、`guizang-ppt-skill`、`huashu-ppt`/`huashu-slides`、`humanize-ppt` | 交付格式矩阵、受众/使用场景、可编辑性、图片PPT/HTML/PPTX/PDF/Keynote路线、讲者备注需求、降级审批 | 交付定义卡、制作工单、格式/导出/素材路径、可编辑性声明、弃用理由、降级审批记录 | 只按默认HTML或PPTX生产，没有判断可编辑、图片PPT、讲者备注、导出或降级路线 |
| 语言内容 | `humanize-ppt`、`huashu-ppt`/`huashu-slides`、`huashu-design`、`taste-skill`、`PPT-Design-DNA-main`/`design-dna` | AST/叙事结构、每页核心句、页面类型密度、讲师或使用者动作、术语组件、内容密度与拆页建议；正向参考中文字、标题、注释、口播和标签如何配合画面 | slide plan、内容到UI/动效转译表、讲者备注、标题判断、页面角色、密度控制、术语归一、正向参考文字协同结论 | 文案只是资料压缩或卡片标题并列，没有决定每页为什么存在、怎么讲、何时分步出现；正向参考只看视觉不看文字 |
| 品牌审美 | `stylekit-skill`、`taste-skill`、`PPT-Design-DNA-main`/`design-dna`、`huashu-design`、`huashu-ppt`/`huashu-slides` | 风格候选与弃用、内部审美策略、Design DNA、品牌资产协议、3方向审美判断；正向参考的配色原因、字体气质、情绪和品牌适配 | 视觉母线、token、品牌色/禁用风格、参考转译落到截图或真实页面、正向参考配色/字体深拆 | 只写“高级感/瑞士风/杂志风”，没有候选和弃用；正向参考只写好看不解释为什么成立 |
| 版式/UI | `taste-skill`、`guizang-ppt-skill`、`PPT-Design-DNA-main`/`design-dna`、`frontend-slides`、`html-ppt`、`huashu-ppt`/`huashu-slides` | Design Read、三拨盘、页面族谱、layout/Sxx或页面类型密度分级、图片PPT/HTML/PPTX路径判断；正向参考的版面规划、视觉重心、留白、跨页切换和替代方案 | 逐页Page Spec、网格/字阶/组件语法、模板改造差异、项目内素材槽位或图片路径、真实产物截图、正向参考2-3个可选设计方案 | UI部门没有判断huashu图片PPT路径、没有guizang映射、没有taste预检，直接画页面；把正向参考降级为方块、配色和文字填充 |
| 动效设计 | `taste-skill`、`guizang-ppt-skill`、`frontend-slides`、`html-ppt`、`huashu-design`、`huashu-ppt`/`huashu-slides` | MOTION_INTENSITY、分步节奏、页间/同页/静止页语法、图片PPT是否适合动效、HTML是否需要状态机；正向参考的页面切换和动效方案 | Motion source map、首态/后续态矩阵、HTML状态机与交互合同、export稳定态、动画与页面角色绑定、正向参考动效重设计 | 全稿统一fade/translate、只点击出现下一项，或图片PPT/HTML动效路线未比较；正向参考没有动效假设 |
| 交互/工程 | `frontend-slides`、`html-ppt`、`guizang-ppt-skill`、`ppt-master`、`huashu-ppt`/`huashu-slides` | 交付路径、可编辑性、图片PPT/HTML/PPTX/Keynote适配与弃用、HTML状态机与输入合同；正向参考若做成HTML时的输入、焦点、回退、重播和export稳定策略 | 工具链可行性、导出方式、素材复制到项目内、截图/验证路径、键盘/鼠标/触摸/滚轮/目录跳转/回退/重播/focus/aria/节流/export稳定态、正向参考交互实现边界 | 只按一个默认格式生产，或把HTML当PPT点击动画，没有记录为什么不用其他已安装Skill；正向参考只做静态复刻 |
| QA | 全部被采用或弃用的设计/生产Skill | Stage-A调用完整性、每个部门矩阵行、可用但未调用理由、阻断记录 | Stage-B吸收字段、真实产物路径、截图/源码/validation是否证明Skill落地、部门复核闭环 | QA只看文件存在和页数，不查每个部门是否充分使用Skill |

`huashu-ppt`/`huashu-slides`不得只被语言或叙事部门使用。只要任务涉及PPT/Slides、图片PPT、封面图、品牌资产、视觉方向候选、页面类型密度或图片生成路径，需求与交付、语言内容、品牌审美、版式/UI、动效设计、交互/工程和QA都必须按本部门职责判断它是否适用；适用时必须吸收其品牌资产协议、3方向候选、页面类型密度分级和项目内素材归档规则。不适用时必须写明弃用原因，例如用户强制要求可编辑矢量PPTX、禁止图片PPT、内容需要实时交互或当前交付路线不允许位图页。

任一部门不得把“这是UI的事”“这是文案的事”“这是工程格式问题”作为不调用Skill的理由。部门可以判定某Skill不适用，但必须写出和本部门职责相关的弃用理由；没有理由的“不适用”视为未充分使用Skill，副总编不得接收该部门意见。

## 调用顺序

部门初始确认方向、完整视觉生产和审美退回恢复生产必须按以下顺序判断，不得反向：

1. 当前资料、受众、场景、页数充分性、页面族谱。
2. 阶段A初始方向Skill调用：`stylekit-skill`、`taste-skill`、`design-dna`/`PPT-Design-DNA-main`、`guizang-ppt-skill`及交付路线相关Skill必须调用、人工等价吸收或记录阻断。
3. `stylekit-skill`：生成或人工等价完成风格候选、style ownership、quality_gate。
4. `taste-skill`：完成Design Read、三拨盘、内部审美策略和排版/UI反模板预检。
5. `design-dna`：形成Presentation Design DNA档案。
6. 选择演示引擎：`guizang-ppt-skill`、`frontend-slides`、`html-ppt`、`huashu-design`或客户母版，只能承接前面结论。
7. 动效语法：结合`guizang`、`frontend-slides`和`huashu-design`规则，定义页间、同页、分步、低功耗和export稳定态。
8. Style Frame截图或视觉草图。
9. 阶段B正式生产平台Skill复核：把已采用Skill结论落入Page Spec、制作工单、真实产物和QA字段。
10. 实现后Skill吸收QA。

任何记录中先出现“采用某主题/某模板/某风格/Sxx编号”，再补StyleKit、taste或DNA，视为顺序违规。任何方向确认记录没有阶段A Skill调用证据，或正式生产记录没有阶段B Skill复核证据，也视为顺序违规。

## Design Skill Stack决策表

| Skill | 当前任务是否相关 | 调用/不调用/降级 | 采用规则 | 弃用规则 | 吸收产物 | 阻断条件 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| stylekit-skill | 是/否 |  |  |  | 风格候选表、quality_gate | 只有slug/prompt |
| taste-skill | 是/否 |  |  |  | 三拨盘、pre-flight | 排版仍模板化 |
| design-dna | 是/否 |  |  |  | DNA档案、来源追踪 | 只有JSON |
| guizang-ppt-skill | 是/否 |  |  |  | 逐页layout/Sxx映射 | 只写风格名 |
| frontend-slides | 是/否 |  |  |  | 固定舞台、3预览、动画pattern | 变成长网页或无预览 |
| html-ppt | 是/否 |  |  |  | theme/layout/animation映射 | 从零手写或乱套动画 |
| huashu-design | 是/否 |  |  |  | 三方向探索、动画导演/评审 | 只出一版或动画无叙事 |
| huashu-ppt / huashu-slides | 是/否 |  |  |  | 品牌资产协议、3方向候选、页面类型密度分级、图片PPT/HTML/PPTX路径判断 | UI部门未判断图片PPT路径或无弃用理由 |
| humanize-ppt | 是/否 |  |  |  | AST叙事结构、页面媒体决策、逐页生产brief、讲者/使用者动作 | 语言内容未做叙事和密度判断，只把资料压缩成页面 |
| ppt-master | 是/否 |  |  |  | PPTX可编辑性、模板/图表能力、交付格式约束 | 需求与交付未判断PPTX路线或可编辑需求 |

可用但不调用也必须写理由。不可用时必须按`08-skill-governance.md`走降级审批；不得假装已使用。

## Online Research Stack 决策表

当任务涉及 HTML Pre 审美、Style Frame、趋势、外部参考或最新前端实现时，必须填写：

| 工具 | 当前任务是否相关 | 调用/不调用/安装提请/阻断 | 采用规则 | 弃用规则 | 吸收产物 | 阻断条件 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Tavily Search | 是/否 |  |  |  | 外部参考搜索记录 | 用户要求联网但未搜索 |
| Tavily Extract / Firecrawl | 是/否 |  |  |  | 页面结构提取记录 | 只看标题不提取结构 |
| Brave Search | 是/否 |  |  |  | 交叉验证结果 | 趋势判断来源单一 |
| Context7 | 是/否 |  |  |  | 最新文档检索记录 | 使用过时API |
| Playwright MCP | 是/否 |  |  |  | 视觉验证记录 | 只做代码检查 |

Online Research Stack 必须服务 Design Skill Stack。外部搜索结果必须转译为 StyleKit 候选、Taste 预检、Design DNA、页面族谱、动效来源或 QA 证据之一。否则只能算“搜索过”，不能算“已吸收”。

必要控件缺失时，先按`23-online-research-toolchain.md`输出《缺失控件安装提请记录》并请求用户同意安装/启用；用户拒绝、未提供 API key 或权限阻断时，当前任务停止在阻断状态。只有用户改写任务边界，不再要求联网、最新文档或真实浏览器验证时，才可另起降级任务。

## StyleKit吸收合同

`stylekit-skill`的输出必须转译为演示文稿字段。

| StyleKit字段 | 演示转译 | QA检查 |
| :--- | :--- | :--- |
| `style_choice` | 当前方向、候选方向、弃用方向 | 是否有采用和弃用理由 |
| `design_brief` | 受众、tone、memorable hook、页面第一眼落点 | 关键页3秒内是否能看出hook |
| `composition_plan` | 页面族谱、布局家族、组件所有权 | 是否避免连续重复layout |
| `tag_bundle` | 风格标签和禁用标签 | 是否没有混入冲突风格 |
| `quality_gate` | 反泛化、对比度、layout、component-fill、motion修复项 | fail项是否已修复或阻断 |
| `ai_rules` | 可执行UI规则 | 是否进入Page Spec/CSS/组件命名 |

若不能运行StyleKit脚本，允许人工等价完成，但必须写“降级/人工等价”，并保留查询词、候选风格、采用/弃用理由和quality gate。

## TasteSkill吸收合同

`taste-skill`偏前端，但其反slop和排版预检必须被转译进演示。

| TasteSkill规则 | 演示转译 | 阻断条件 |
| :--- | :--- | :--- |
| Design Read | 一句话说明项目类型、受众、视觉语言、系统倾向 | 没有读场景就选风格 |
| DESIGN_VARIANCE | 页面族谱和版式变化幅度 | 全稿同一结构 |
| MOTION_INTENSITY | 动效强度、是否需要高级编排 | 声称动效丰富但实际静态/统一fade |
| VISUAL_DENSITY | 单页信息密度和拆页策略 | 为塞内容缩字号/压卡片 |
| Section/Layout Repetition Ban | 同类页不得连续复用同一结构 | 连续3页标题+卡片/面板 |
| Card/Shape/Color discipline | 卡片、圆角、色彩、强调色统一且有语义 | 混合组件库、随机accent、同页多风格 |
| Motion motivated | 每个动画说明其传达什么 | “为了好看”而动 |

## 动效单一专项门禁

当用户指出“动效单一/生硬/没有美感”时，必须同时读取`17-motion-design-standards.md`和本文件，并完成：

| 证据 | 要求 |
| :--- | :--- |
| Motion grammar map | 每个页组的页间语法、同页语法、触发反馈和完成态 |
| Motion source map | 哪些规则来自guizang、frontend-slides、html-ppt、huashu-design或自定义 |
| Role variation | 封面、章节、案例、流程、练习、收束至少有不同节奏 |
| Reduced/export stable | 低功耗、reduced-motion和截图导出稳定态 |
| Anti-single-motion check | 不得全稿统一`opacity + translateY`或同一duration/easing |

若无法证明“不同页面为什么以不同方式运动”，不得进入HTML实现。

## QA吸收字段

QA记录和`validation.json`等价证据应增加：

| 字段 | 含义 |
| :--- | :--- |
| `designSkillStackDecisionPath` | Design Skill Stack决策表路径 |
| `stylekitAbsorptionPath` | StyleKit候选、采用/弃用和quality_gate |
| `tastePreflightPath` | Design Read、三拨盘和排版/UI反模板预检 |
| `presentationDesignDnaPath` | 20规定的DNA档案路径 |
| `engineSelectionPath` | guizang/frontend-slides/html-ppt/huashu-design/客户母版选择理由 |
| `motionSourceMapPath` | 动效来源映射和反单一动效检查 |
| `skillStackAbsorptionDecision` | absorbed / partially_absorbed / read_not_absorbed / blocked |

缺少这些字段时，不得写“相关Skill已集成”。自动烟测不能替代本表。
