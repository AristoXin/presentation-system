# 21-design-skill-stack-integration

读取时机：当任务涉及完整视觉生产、Style Frame、HTML/PPT/Slides、审美退回、排版/UI不好看、动效单一，或用户质疑“stylekit/design-dna/guizang/taste/frontend-slides/html-ppt/huashu-design等Skill没有集成”时读取。本文件定义演示设计相关Skill的分层、调用顺序、吸收证据和QA阻断。

## 核心问题

演示设计失败通常不是因为缺一个模板，而是因为多个设计Skill各自孤立：StyleKit给了风格，DNA给了字段，guizang给了版式，动效Skill给了动画，但没有被统一成页面族谱、UI语法、运动语法和QA证据。本文件要求先完成设计Skill栈决策，再进入Style Frame或全稿生产。

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

## 调用顺序

完整视觉生产和审美退回恢复生产必须按以下顺序判断，不得反向：

1. 当前资料、受众、场景、页数充分性、页面族谱。
2. `stylekit-skill`：生成或人工等价完成风格候选、style ownership、quality_gate。
3. `taste-skill`：完成Design Read、三拨盘和排版/UI反模板预检。
4. `design-dna`：形成Presentation Design DNA档案。
5. 选择演示引擎：`guizang-ppt-skill`、`frontend-slides`、`html-ppt`、`huashu-design`或客户母版，只能承接前面结论。
6. 动效语法：结合`guizang`、`frontend-slides`和`huashu-design`规则，定义页间、同页、分步、低功耗和export稳定态。
7. Style Frame截图或视觉草图。
8. 实现后Skill吸收QA。

任何记录中先出现“采用某主题/某模板/某风格/Sxx编号”，再补StyleKit、taste或DNA，视为顺序违规。

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
