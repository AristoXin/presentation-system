---
name: presentation-system
description: Presentation-system router and three-level production team model for presentation, visual storytelling, and multi-format visual deliverables. Use when Codex must diagnose the real scenario and audience, define deliverables, coordinate 总编/副主编/执行/QA roles, route related Skills, and govern outputs such as client reports, management updates, sales proposals, investor decks, training materials, research reports, product explainers, workshops, conference talks, HTML interactive presentations, editable PPTX, PDFs, screenshot evidence packs, and speaker notes. Also use when the user critiques a deck, says the skill/process/subagents/UI/copy/aesthetics/motion/trend research/online search/external references/latest docs/browser visual validation/design-dna/guizang/stylekit/taste/frontend-slides/html-ppt/huashu-design integration failed, asks for historical audit or skill revision, questions page count sufficiency, or requests failure governance.
---

# Presentation System Skill Router

本文件是入口、路由和团队协作总控。执行任务前先判断用户目标，再读取最小必要reference文件。不要默认用户在做培训课件；必须先根据资料、语言、目标对象、使用场景和交付格式判断真实意图。不要一次性读取全部reference，除非任务本身是全面审计或重构本Skill。

## 任务模式先判定

| 模式 | 场景 | 允许动作 | 禁止动作 |
| :--- | :--- | :--- | :--- |
| 只读审计 | 用户要求检查、评审、指出问题，且未要求改文件 | 读取必要文件、输出问题清单和建议 | 创建协作记录、写evidence、修改Skill或产物 |
| Skill治理可写 | 用户要求修订Skill、补规则、基于历史对话更新治理 | 修改Skill系统文件和治理证据 | 创建或修改HTML/PPT/PDF/截图包/样张目录 |
| 产物生产/修复 | 用户要求生成、修改、恢复、冻结或交付文件 | 按`19`流程创建协作记录、subagent、工单、产物和QA证据 | 跳过生产前放行或用审计口径代替生产证据 |

只读审计不要求创建《团队协作与生产记录》，也不要求Subagent Evidence Lock；一旦需要写入Skill或产物，必须重新判定为Skill治理可写或产物生产/修复。

用户审核流程图硬门禁：任何生产、修复、回退、审稿、QA冻结、用户退回回归、Style Frame生成或HTML/PPT/PDF/截图包创建前，必须先读取并遵守`references/19-approved-production-flow.md`。该文件是当前Skill内强制流程图；若用户后续提出更新，以《用户最新要求锁定表》覆盖旧口径。其他reference只能补充执行细节，不能降低、跳过或改写该流程。修改/回退类任务也必须走“总编分发 → 对应副主编审核 → 执行层修订 → 同一副主编复审 → 全部适用副主编一致审核 → 副总编一致性审核 → 总编二级审核 → QA回归 → 用户复验”闭环；不得只由打回的副主编同意后继续。

核心原则：本Skill不是单人清单，而是一套三级生产团队机制，并在正式生产前设置“副总编+总编”双闸门。正式生产必须由“总编定方向、副总编统筹冲突、能力域副主编定标准并一级复核、执行专员落地、QA冻结、用户验收”的闭环驱动。用户口语中的“主编”等同于本文的“总编”。总编可以由主Agent担任，但总编不得替代副主编一级复核、部门一致意见和QA冻结。凡进入生产、修复、审稿、QA冻结、Style Frame、审美退回恢复或Vx版本动作，subagent建立不需要再次征求用户同意，必须按`references/16-multi-agent-governance.md`创建独立能力域Agent；若不支持或工具不可用，不得自动降级，必须写`SUBAGENT-BLOCKER`并停止在阻断状态。任何退回后的第二轮、第三轮及后续复核，都必须重新回到对应副主编subagent，不得由主Agent或执行层自行宣布问题已解决。

Vx版本原子门禁：创建、命名、复制、修改、导出、截图验证或归档任何`Vx`、`V0.x`、`versions/<version>`、HTML/PPT/PDF/截图包/全稿样张，均属于生产动作。无论称为“未冻结稿”“结构探索”“工作稿”“候选稿”“只做小修”“只跑烟测”，都不能降低门槛。进入任何版本动作前，必须先通过Subagent Evidence Lock：真实subagent创建证据、agent id、能力域、输入文件、输出结论、时间戳齐全。缺少真实subagent证据时只能输出`SUBAGENT-BLOCKER`、阻断审计、Page Spec或Skill治理文本，不得创建、复制、修改、截图或归档产物。

失败修订硬门禁：若用户质疑“subagent没有调用”“副主编没有参与”“Skill写得不可信”“审美没有学习/搜索/趋势总结”“成品很丑/像模板/像资料页”“为什么又套模板”“模板合适也要改造”“联网搜索/外部参考/最新文档/浏览器视觉验证缺失”“design-dna/guizang/stylekit/taste/frontend-slides/html-ppt/huashu-design/审美/UI/动效没有深度集成”“基于历史对话全面修订”，必须立即暂停生产，进入Skill治理与失败复盘模式。第一步不是读现有Skill自证，而是先按`references/18-history-derived-governance.md`输出《历史对话需求整合表》；随后读取`references/00-production-gate.md`、`references/16-multi-agent-governance.md`、`references/11-aesthetic-anti-ai.md`、`references/07-qa-checklist.md`、`references/08-skill-governance.md`、`references/20-design-dna-guizang-integration.md`、`references/21-design-skill-stack-integration.md`、`references/23-online-research-toolchain.md`，必要时读取`skill-creator`，并先修复流程或记录缺口；不得继续补丁式修改产物。

用户最新要求锁：任何生产、修复、QA、Style Frame、恢复生产或Skill治理前，必须先建立《用户最新要求锁定表》。该表必须忠实转写用户最新原话摘要、禁止事项、验收标准、是否覆盖旧要求和执行理解；主Agent只能追加解释，不能用自己的解释替代用户原话。若用户提到“按流程图”“要subagent”“没有按我的框架”“结果不如人意”，这些必须作为最高优先级门禁，不得降级为建议。缺表或表内要求未闭环，不得进入生产、截图、QA或版本动作。

Skill治理范围硬门禁：当用户要求修订Skill文件、完善Skill、补Skill规则、基于历史对话修Skill，或同一请求同时包含“生成新版本 + 补/修Skill”时，默认先归入Skill治理与失败复盘；只允许修改`presentation-system/SKILL.md`、`presentation-system/AGENTS.md`、`presentation-system/agents/openai.yaml`、`presentation-system/references/*.md`和`presentation-system/versions/<version>/evidence/`治理证据。不得创建、复制、修改、命名、导出、截图验证或归档HTML/PPT/PDF/截图包/样张目录等交付产物。若此前误建产物目录，只能标记为失败证据；清理或继续使用都必须先获得用户明确同意。

完整Skill审计硬门禁：当用户要求“完整检查Skill”“全面更新Skill”“检查为什么Skill没有生效”或类似表达时，必须按Skill治理可写处理，并读取`SKILL.md`、`AGENTS.md`、`agents/openai.yaml`、全部`references/*.md`和必要的`references/visual/reference-entries.md`索引。审计不得只补入口规则，必须检查五条闭环：触发路由是否覆盖用户原话、生产流程是否能阻断错误、能力域职责是否有否决权、QA/证据模板是否能证明关闭、经验回写是否跨项目生效。每个新增或修改的硬规则都必须回答：触发条件、必填证据、阻断条件、责任部门、写入文件。缺少这些字段的规则只能算提醒，不算Skill更新完成。

团队分工硬门禁：任何生产类任务在创建、修改、复制、命名、导出、截图验证或归档HTML/PPTX/PDF/截图包/Vx目录之前，必须先创建或更新本版本的《团队协作与生产记录》文件。推荐路径为`<交付目录>/团队协作与生产记录_<version>.md`，若尚未确定交付目录，则使用`versions/<version>/evidence/team-collaboration.md`。该文件必须至少包含项目诊断、RACI矩阵、Agent编制表、制作工单、能力域一级复核记录、总编二级复核记录、QA冻结/未冻结记录。只在对话中口头说明、只在最终回复中补表、或生产后倒填记录，均视为未执行团队分工。

多Agent硬门禁：生产、修复、审稿、QA冻结、Style Frame或任何Vx版本动作必须先检测subagent能力，并在协作记录中写入《Agent编制表》。subagent可用时，至少为需求/交付、语言内容、品牌审美、版式/UI、动效设计、交互工程、QA建立独立副主编或专项Agent，并执行“执行层产出 → 副主编一级复核 → 执行层修复 → 副主编复审”的循环；只有所有适用副主编subagent一致同意，并经过副总编与总编双闸门，才允许进入HTML/PPT/PDF/Vx目录/截图包等任何创建或修改动作。只创建泛化审查Agent、只写RACI表、由主Agent自证通过、或退回后绕过副主编复审，均视为未完成团队协作。

实现后复核硬门禁：生产前预审、方向建议、Style Frame建议、探索性意见都不等于实现后复核。任何HTML/PPT/PDF/截图包/样张在执行层生成后，必须把真实文件、源码路径、截图和验证结果重新交给原责任副主编subagent做至少一轮实现后复核；若任一副主编退回，修复后必须回到同一副主编subagent复审。没有真实subagent证据时，不得创建Vx全稿；没有实现后复核记录时，不得称为V版、候选稿、冻结稿、可验收版本或团队闭环产物，只能标为`BLOCKED_BY_SUBAGENT`、失败审计或文字Page Spec。

失败后停产硬门禁：用户明确退回“丑/难看/恶心/像模板/没有审美/没复核/浪费token/Skill不可信/没有调用subagent/没有按流程图/脱离我设定的框架/结果不如人意”后，当前版本立即判定为未通过用户验收，并进入`FAILED_VISUAL_FREEZE`。下一步只能做失败审计、旧版否决、Skill/流程修订、用户最新要求锁定、产物冻结锁和文字Page Spec；不得由主Agent快速改CSS、换配色、复制旧版、创建Vx目录、重命名为候选稿、导出新截图、跑Playwright验证、生成validation、或继续生成下一版全稿。恢复分三段：失败审计期只能交付文字审计/Page Spec；用户明确批准Style Frame探索期后，才可生成受控的1-3页局部视觉证据，但不得命名Vx、不得扩展全稿、不得运行冻结QA；用户再次明确回复“同意恢复生产/同意进入下一版全稿”后，才可进入正式HTML/PPT/PDF全稿生产。“继续优化/再来一版/可以改”不自动等同恢复授权。

用户点名失败专项硬门禁：若用户点名某些页面存在排版失衡、动效生硬、分步缺失、页面“丑”或某些部门全面失效，当前任务不得被解释为“修几页”。必须先把这些页和问题写入《用户最新要求锁定表》和失败审计，作为下一轮Skill治理的最高优先级验收项。点名页必须进入Page Spec重写清单，不能只调CSS、间距、颜色或动画参数。若用户点名第1页/第9页这类跨页重心问题，版式/UI和品牌审美部门必须共同补做光学平衡判断；若用户点名第5页/第9页这类分步缺失，动效部门必须补做首态/后续态矩阵；若用户点名第15页这类整体审美失败，必须退回视觉母线或页面族谱，不得标记为条件通过。

上一版问题关闭硬门禁：若用户已经点名上一版存在问题，下一版生产前必须先建立《上一版问题关闭矩阵》，逐项列出用户原话、页码/范围、根因、Page Spec重写动作、同类页联动、修后截图/状态矩阵/复核证据和关闭结论。只列“新版变化”“新版差异”“视觉命题已调整”“局部组件增强”不算关闭。若任一上一版点名问题仍存在，当前新版必须立即标为`FAILED_VISUAL_FREEZE`，不得称为新版候选、样张、工作稿、工程烟测通过版本或可验收版本。用户明确指出“上一版问题一个没解决”“V12出现的问题V13也没有解决”“还是一样存在”时，主Agent不得继续生成下一版或补丁式修复，必须先回写`references/*.md`和版本治理证据。

V12/V13已固化失败样例：用户明确指出第12版出现的问题在第13版仍未解决，包括：第1页头轻脚重、左重右轻；第9页与第1页相反的重心失衡；页间和同页动效生硬无美感；第9页右侧5点中第1点无需触发即显示；第5页多个语义阶段一起出现；第15页及部分页面“丑得要死”；并指出这说明Skill层面存在UI、内容文案、审美、流行调研、动效等部门全面失效。该样例是跨项目硬失败，不是任何特定客户项目的专属问题。后续任何项目出现同类问题，必须触发设计、动效、QA和团队治理阻断，并进入经验回写。

条件通过失效硬门禁：对用户可见的基础质量问题，任何“条件通过”“工程烟测通过”“基本可用”“后续优化”都不能放行。以下任一问题存在时，结论只能写“退回/阻断/FAILED_VISUAL_FREEZE”：页面重心明显偏移、头轻脚重或左重右轻；分步页面初始态提前露出应由用户触发的内容；多个语义阶段无理由一起出现；页间或同页动效只有机械淡入/位移且无讲述节奏；关键页被副主编或用户评价为丑、模板、没有审美；内容文案为了适配版式被压扁、空泛或失去讲述动作。

subagent默认授权判定：使用本Skill进入生产、修复、审稿、QA冻结、Style Frame、审美退回恢复或Vx版本动作时，建立subagent不需要用户另行同意，必须创建真实能力域Agent；不得以“未明确要求subagent”为由降级。若仍因工具不可用、权限阻断或部门Agent不可创建而无法建立，必须写入`SUBAGENT-BLOCKER`并停止当前生产/复核链路。

组织扩编硬门禁：若执行中发现现有部门不足（例如需要动效设计部、语言内容设计部、数据可视化部、法律合规部等），主Agent或任一副主编只能提交《新增部门申请》，说明职责、边界、交付物和否决权；总编批准后必须创建对应独立subagent并写入Agent编制表。未经总编批准和子agent组建，不得由主Agent临时扮演新部门。若无法创建该子agent，必须写入`SUBAGENT-BLOCKER`并停止当前生产/复核链路。

视觉原则：任何参考图、模板、风格链接、历史样张或流行趋势都只能作为经验输入，不能作为可照搬的页面答案。每次设计必须先把过往经验转译为适合当前用户资料、品牌色、受众、场景、内容证据和交付格式的设计判断；若无法说明“当前方案如何来自用户资料而不是来自参考图表层”，不得进入页面生产。

初始方向Skill栈硬门禁：部门初始确认方向不是主Agent凭经验定风格，也不是先选模板再让部门补章。任何HTML/PPT/Slides/视觉叙事任务，在《部门一致意见表》提交副总编前，必须读取`references/21-design-skill-stack-integration.md`并调用或人工等价吸收构成方向的Skill：`stylekit-skill`、`taste-skill`内部审美策略、`PPT-Design-DNA-main`/`design-dna`、`guizang-ppt-skill`及交付路线相关Skill。所有适用部门都必须填写《部门Skill使用矩阵》：需求/交付判断`ppt-master`、`frontend-slides`、`html-ppt`、`guizang-ppt-skill`、`huashu-ppt`/`huashu-slides`、`humanize-ppt`；语言内容判断`humanize-ppt`、`huashu-ppt`/`huashu-slides`、`huashu-design`、`taste-skill`；品牌审美判断`stylekit-skill`、`taste-skill`、`PPT-Design-DNA-main`和huashu品牌资产协议；版式/UI判断页面族谱、layout/Sxx、页面类型密度和图片PPT/HTML/PPTX路径；动效、交互工程和QA也必须分别记录适用Skill的采用、弃用、阻断和吸收结果。不能只由UI或语言部门判断huashu相关Skill，也不能用“不是本部门职责”跳过可用Skill。必须产出《初始方向Skill调用记录》《内部审美策略吸收表》《部门Skill使用矩阵》；缺少这些证据时，初始方向无效，不得进入副总编/总编闸门、Style Frame或页面生产。进入正式生产平台前还必须二次调用/复核已采用Skill，把方向结论落入逐页Page Spec、制作工单、模板改造差异表、真实产物路径和QA字段；不得用初始方向记录替代正式生产证据。

深度定制硬门禁：用户每次提供的内容都必须被视为新的设计对象，不得直接套用上一次的母版、某个Skill模板、某个流行风格或历史样张。任何“采用某某风格/主题色/模板编号/版式库”都只能是工具候选，不是设计方向；必须先由语言内容、品牌审美、版式/UI、动效设计、交互工程、QA和必要的流行趋势调研部门分别完成内容关系、页面角色、视觉锚点、动效脚本、实现约束和风险判断，并在《部门一致意见表》中达成一致后，才能选择设计引擎和具体模板承接。若先宣布风格、主题色或模板，再倒推页面结构，视为套模板生产，必须暂停并退回Skill治理。

模板适配性否决：用户提供了内容，不等于允许套模板；内容越具体，越必须先判断模板是否适合。参考库检索和流行调研部门不是装饰性步骤，拥有否决权：如果候选模板、历史样张、流行趋势或Skill版式无法承载当前内容的受众、证据、训练动作、讲述节奏和品牌语气，必须明确写入“弃用原因”，不得为了使用某个模板而压缩、改写或扭曲用户内容。不适配时，应先自定义页面族谱和Page Spec，再选择更合适的实现方式。

模板改造硬门禁：模板即使通过适配性审查，也只代表“大方向可借用”，不得直接调用生成。必须先输出《模板改造差异表》，逐页说明：保留的模板结构、必须改写的内容区、必须新增的组件、必须删除的模板装饰、为当前用户资料调整的字号/密度/留白/动效/交互，以及调整责任部门。没有改造差异表时，任何模板调用都视为硬套；模板只能作为原材料，不能作为成品路径。

页数充分性硬门禁：页数不是用户已给版本、样本、模板或历史产物的附属属性，而是跨部门判断结果。任何正式视觉生产、重做、审稿、修复或恢复生产前，必须输出《页数充分性判断表》，由需求/交付、语言内容、品牌审美、版式/UI、动效设计、交互/交付和QA共同判断当前页数是否足够承载目标。若内容链路、案例证据、练习动作、讲述节奏、审美呼吸、分步揭示或投屏可读性要求更多页面，必须主动提出新增页、拆分页、附录页或讲者备注；若现有页数冗余，必须提出合并页或删除页。不得把“用户之前给过的页数/样本页数/旧版页数/模板页数”当成默认最终页数；除非用户明确写死页数，否则总编必须允许页数随内容和设计判断调整。

页数不足阻断：若页面因为页数不足而出现正文拥挤、标题压缩、多个核心观点同页竞争、案例和判断混在一起、流程阶段被合并、动效步骤提前露出、练习缺少操作区或审美留白不足，不得由UI排版强行消化，也不得用缩小字号、增加卡片密度、降低行距或隐藏内容解决。必须回到内容、文案、UI、审美和动效部门，重新判断拆页、增页、附录化或讲者备注承载。

## 默认工作顺序

1. 识别项目类型：客户汇报、内部管理汇报、销售提案、投融资路演、培训课件、研究报告、产品介绍、工作坊材料、项目复盘、招投标材料、会议讲稿等。
2. 识别受众：客户、高管、员工、学员、投资人、合作方、内部团队、公众等。
3. 识别使用方式：现场讲、线上发、打印、归档、二次编辑、会议投屏、网页展示等。
4. 识别交付格式：若用户未特别声明格式，只说“创建文件/生成文件/做一个版本”，读取`references/03-delivery-routing.md`判断交付路线；PPTX/PDF/截图包/讲者备注/讲义均按交付定义和用户要求确认。
5. 识别输入约束：模板、旧稿、品牌规范、页数、参考样式、保密要求、可编辑性要求。
6. 任何生产、修复、回退、审稿、QA冻结或Style Frame生成先读取`references/19-approved-production-flow.md`和`references/00-production-gate.md`，再读取`references/01-team-roles.md`和`references/16-multi-agent-governance.md`，为本版本创建《团队协作与生产记录》骨架；小任务也必须按production gate分级，并填写RACI矩阵和Agent编制表。若任务是Skill治理或用户要求基于历史对话修订，必须先读取`references/18-history-derived-governance.md`并完成《历史对话需求整合表》。
7. 用户上传文件、旧稿、模板或参考素材后，需求/交付、语言内容、品牌审美、版式/UI、动效设计、交互/交付等部门必须并行提出初步方案，并在《部门一致意见表》中全部同意后提交副总编。
8. 副总编先审核部门意见是否真实一致、是否存在被压下的反对意见、是否需要新增部门；副总编通过后提交总编。总编执行初审方案闸门；未通过时退回对应副主编重新协商，未通过不得进入后续Page Spec、Style Frame或制作工单。
9. 在《团队协作与生产记录》中写入总编目标、交付定义、责任人、Agent id或降级说明、验收标准、证据要求和冻结条件；该记录未存在或字段为空时，不得进入页面、代码、PPTX或PDF生产。
10. 若涉及视觉设计，读取并检索`references/15-visual-reference-library.md`，输出《参考经验转译卡》和《趋势适用性判定卡》，说明可借鉴、不可照搬、当前项目如何改写参考经验，以及是否需要外部近期验证。若需要风格候选、风格混合、设计库校准或用户提到StyleKit/风格提示词/设计库，必须按`references/08-skill-governance.md`检测`stylekit-skill`，并读取`references/21-design-skill-stack-integration.md`和`references/visual/reference-entries.md`中的`REF-20260621-01`；StyleKit输出必须转译为风格候选表、采用/弃用理由、style ownership、composition_plan和quality_gate修复项，不能直接替代设计结论。若任务涉及排版/UI不好看、动效单一或审美退回，必须同时将`taste-skill`、`frontend-slides`、`html-ppt`、`huashu-design`、`huashu-ppt`/`huashu-slides`纳入Design Skill Stack决策表，记录调用/不调用/降级理由。版式/UI副主编必须判断huashu相关Skill是否用于品牌资产协议、三方向候选、页面类型密度分级、图片PPT/HTML/PPTX路径选择或素材归档规则；未使用时必须写弃用理由。若用户提供视觉参考、旧稿、品牌规范，或任务要求深度审美、排版设计、避免很丑的结果，品牌审美副主编和版式/UI副主编必须读取`references/20-design-dna-guizang-integration.md`，判断是否调用`PPT-Design-DNA-main`/`design-dna`和`guizang-ppt-skill`，并读取`REF-20260621-03`与`REF-20260621-02`；PPT-DNA必须形成Presentation Design DNA档案、DNA来源追踪表、页面映射、UI吸收表和动效吸收表，guizang必须形成A/B适配与弃用表、主题节奏、逐页layout/Sxx映射、模板改造差异和QA吸收检查。若用户要求“当前/主流/流行/最新审美”，或用户质疑审美学习、趋势调研、模板套用，品牌审美副主编必须完成《主流审美趋势调研卡》，总结近期趋势、适用边界和不适合本项目的流行做法，不能只复用历史样张。参考库和趋势调研必须同时列出候选经验、弃用经验和弃用理由；没有弃用判断，说明没有真正完成适配性审查。
11. 输出交付定义卡、内容差距清单、叙事蓝图、页数充分性判断表、内容到UI/动效转译表、UI方向和动效方向；UI/动效方向必须同时绑定当前用户资料、内容关系、参考库经验、观看距离和讲述节奏，并写回《团队协作与生产记录》。内容到UI/动效转译表必须先定义每页“为什么必须这样长出来”，再允许讨论用哪个模板或版式实现。页数充分性判断必须先于逐页Page Spec和设计引擎选择完成。
12. 若是HTML/PPT/Slides视觉生产，必须在完成第10-11步、Presentation Design DNA档案和部门一致意见通过后，才允许选择并读取一个主设计引擎Skill：`guizang-ppt-skill`、`html-ppt`、`frontend-slides`或项目指定模板。选择理由必须写入《Skill可用性确认单》和`20`规定的《设计引擎桥接表》，并说明该Skill如何承接已经形成的DNA、页面族谱和内容到UI/动效转译，而不是替代页面族谱。若选择`guizang-ppt-skill`瑞士风，必须遵守其登记版式、主题节奏、单一accent、字号/字重阶梯和截图验证要求；不得只借用“瑞士风”名义后自造卡片网格，也不得先选IKB/版式编号再倒推内容结构。设计引擎确定后必须先产出《模板适配性审查表》《模板改造差异表》和逐页Page Spec，再允许执行层写HTML/PPT/PDF。
13. 完整视觉生产前必须先产出Style Frame截图，不少于2个方向，且至少覆盖封面、核心模型/工具页、案例页、收束页中的3类。Style Frame不是视觉部门单独出图后让其他部门盖章，必须先完成语言内容、品牌审美、版式/UI、动效设计、交互工程、QA前置风险的协同输入：每个方向都要有内容一句话判断、页面信息载荷、UI版式语法、动效脚本或静止理由、实现/导出约束、QA风险清单。存在冲突时先由副主编协商修订，再截图。Style Frame必须由品牌审美、版式/UI、语言内容、动效、交互工程、QA副主编分别签署通过或退回。未经Style Frame协同生成与截图复核，不得创建全稿HTML/PPT/PDF。
14. 根据交付定义选择生产路径和相关Skills；若依赖外部、全局或vendor Skill，读取`references/08-skill-governance.md`，由总编/能力域副主编/工具链副主编决定调用范围并检测可用性。可用但与当前工单无关的Skill必须标记为“可用但不调用”，不得全量加载。
15. 交付定义、页数充分性、页面族谱、内容到UI/动效转译、模板适配/改造和Style Frame协同输入完成并通过生产前放行后，才由子agent建立制作工单并下发执行层，按能力域进入内容、审美、版式、交互、工具链、多格式生产。
16. 生产前通过Style Frame / 视觉方向 / 动效脚本确认；确认记录必须写入《团队协作与生产记录》。未通过副总编和总编双闸门，不得创建HTML、PPTX、PDF或截图包。
17. 执行层完成后必须经过能力域副主编一级复核；未通过则退回执行层，不得直接进入总编复核。
18. 任一副主编退回后，必须由副主编subagent建立修复任务并下发执行层；执行层修复后回到同一副主编subagent复审。无论循环多少轮，都必须保留轮次、退回项、修复证据和复审结论。
19. 只有全部适用副主编subagent一致签署“可交总编”，总编才可二级复核；总编若提出新意见，必须下发给对应副主编subagent，再由副主编下发执行层，重复闭环。
20. 总编二级复核通过后，生产后执行QA、版本归档和证据链记录；若QA未冻结，交付物只能标为样张或工作稿。QA冻结后必须提交用户验收。
21. 若QA、审美QA、用户验收或任一副主编复审结论为退回/阻断，流程不自动进入下一版本生产；必须先写入`FAILED_VISUAL_FREEZE`、归档失败证据、提交恢复生产申请，并等待用户明确批准。

不要在第1步前直接进入页面生产。

## 项目类型识别矩阵

先用此矩阵判断材料意图，再读取`references/12-project-type-patterns.md`获取完整操作规则。

| 项目类型 | 典型信号 | 内容结构重点 | 视觉策略 | 常见交付物 |
| :--- | :--- | :--- | :--- | :--- |
| 客户汇报 | 客户、方案、汇报、领导、评审 | 背景-问题-洞察-方案-证据-建议 | 稳重、可信、证据导向 | PPTX / PDF / HTML |
| 培训课件 | 学员、课程、练习、讲师、学习目标 | 学习路径-概念-案例-练习-工具 | 节奏清晰、互动友好 | PPTX / HTML / 讲义 / notes |
| 投融资路演 | 投资人、融资、BP、商业模式 | 痛点-机会-产品-增长-模式-团队-融资需求 | 高张力、简洁、有记忆点 | PPTX / PDF |
| 销售提案 | 客户痛点、解决方案、报价、合作 | 痛点-方案-价值-案例-实施-下一步 | 商务、清晰、行动导向 | PPTX / PDF |
| 内部复盘 | 项目、问题、原因、行动项 | 事实-原因-影响-责任-动作-时间表 | 克制、结构化、可执行 | PPTX / PDF |
| 研究报告 | 数据、趋势、分析、结论 | 问题-方法-发现-分析-结论 | 信息密度高、图表规范 | PDF / PPTX |
| 产品介绍 | 产品、功能、场景、用户价值 | 场景-问题-功能-价值-案例 | 视觉化、场景化 | HTML / PPTX / PDF |

## 模板处理规则

若用户提供模板、旧PPT、参考deck或客户母版，先读取`references/13-template-intake.md`，再生产。模板页数不是最终页数，模板风格不是必须照抄，模板结构不是必须沿用。先判断模板用途：品牌母版、内容参考、结构参考、视觉参考、历史版本、客户强制模板。若是强制母版，优先保留版心、Logo、安全区、页眉页脚和品牌规范；若只是参考，提炼可复用元素，不机械套版。必须输出页数预算表：原始页数、建议页数、合并页、拆分页、新增页、删除页、原因。

## 用途到叙事结构

根据项目类型选择叙事结构，不套用固定结构。读取`references/14-narrative-patterns.md`选择或组合叙事骨架。

## 路由规则

路由硬规则：任何“生产/修复/审稿/QA冻结/用户退回回归/Style Frame生成”都必须先读`references/00-production-gate.md`。下表的具体场景reference只能追加，不能替代production gate、团队协作和多Agent门禁。

| 用户目标或输入信号 | 必读reference | 按需读取 | 优先检测/动作 |
| :--- | :--- | :--- | :--- |
| 任意正式生产、修复或冻结任务 | `references/19-approved-production-flow.md` + `references/00-production-gate.md` + `references/01-team-roles.md` + `references/16-multi-agent-governance.md` + `references/02-workflow.md` | `references/10-version-evidence.md` | 先按强制流程图执行，再检测subagent能力，建立Agent编制表、RACI、制作工单、一级复核/二级复核/QA冻结路径 |
| 输入不完整或用途不明 | `references/01-team-roles.md` + `references/02-workflow.md` + `references/12-project-type-patterns.md` | `references/05-content-standards.md` | 先做交付定义和RACI，不生产 |
| 明确是客户汇报 | `references/01-team-roles.md` + `references/12-project-type-patterns.md` + `references/14-narrative-patterns.md` | `references/05-content-standards.md` | 检查证据链、决策信息和执行建议 |
| 明确是培训 | `references/01-team-roles.md` + `references/12-project-type-patterns.md` + `references/14-narrative-patterns.md` | `references/06-interaction-standards.md` | 检查学习路径、练习、讲师备注和带走工具 |
| 明确是路演/BP | `references/12-project-type-patterns.md` + `references/14-narrative-patterns.md` | `references/11-aesthetic-anti-ai.md` | 检查故事张力、商业逻辑和关键页 |
| 明确是内部复盘 | `references/12-project-type-patterns.md` + `references/14-narrative-patterns.md` | `references/05-content-standards.md` | 检查事实、责任、行动项和时间表 |
| 明确是研究报告 | `references/12-project-type-patterns.md` + `references/14-narrative-patterns.md` | `references/05-content-standards.md` | 检查数据、图表、来源和结论可信度 |
| 用户提供模板、旧PPT、参考deck、客户母版、页数要求 | `references/13-template-intake.md` + `references/02-workflow.md` | `references/04-design-standards.md` | 输出模板解析表、页数预算表，并同步完成通用页数充分性判断 |
| 用户质疑页数是否足够、要求不要受旧版/样本限制，或资料明显被压缩 | `references/02-workflow.md` + `references/05-content-standards.md` + `references/04-design-standards.md` | `references/01-team-roles.md` + `references/10-version-evidence.md` | 输出《页数充分性判断表》，由内容、文案、审美、UI、动效、QA共同判断增页/拆页/合页/附录 |
| 用户提供视觉参考图、设计风格链接、审美参考、灵感板 | `references/15-visual-reference-library.md` + `references/04-design-standards.md` | `references/11-aesthetic-anti-ai.md` | 先按通用型/专用型分类，再输出《参考经验转译卡》：借鉴什么、不照搬什么、如何结合用户资料改写；关键结论必须回写视觉参考库 |
| 用户要求搜索/总结当前主流审美、流行趋势或前沿UI | `references/23-online-research-toolchain.md` + `references/15-visual-reference-library.md` + `references/11-aesthetic-anti-ai.md` + `references/08-skill-governance.md` | `references/04-design-standards.md` | 品牌审美副主编先完成《主流审美趋势调研卡》和《外部参考搜索记录》；外部搜索工具缺失时先提请用户同意安装/启用，用户拒绝则本Skill停止在阻断状态 |
| 明确要HTML互动演示 | `references/03-delivery-routing.md` + `references/06-interaction-standards.md` + `references/22-html-pre-visual-director.md` + `references/08-skill-governance.md` | `references/07-qa-checklist.md` | 检测`frontend-slides`和浏览器验证工具；必要控件不可用时先提请安装/启用，用户拒绝则停止当前任务 |
| 用户要求联网搜索、外部参考、最新文档、浏览器视觉验证，或质疑未联网/未浏览器验证 | `references/23-online-research-toolchain.md` + `references/08-skill-governance.md` + `references/07-qa-checklist.md` | `references/15-visual-reference-library.md`、`references/21-design-skill-stack-integration.md`、`references/22-html-pre-visual-director.md` | 建立Online Research Stack决策表；Tavily/Brave/Firecrawl/Context7/Playwright缺失时先请求用户同意安装/启用；用户拒绝则停止，不得用本地参考库冒充联网或最新文档 |
| 用户只说创建/生成文件、做一个版本，未指定格式 | `references/03-delivery-routing.md` + `references/01-team-roles.md` + `references/16-multi-agent-governance.md` | `references/06-interaction-standards.md` | 按`03-delivery-routing.md`判断默认交付路线，不在入口重复定义 |
| 明确要PPTX可编辑母版/可编辑交付 | `references/03-delivery-routing.md` + `references/08-skill-governance.md` | `references/04-design-standards.md` + `references/07-qa-checklist.md` | 检测`ppt-master`；不可用时请求安装/启用或内嵌，用户拒绝则停止 |
| 明确要PDF/讲义/文档化输出 | `references/03-delivery-routing.md` + `references/05-content-standards.md` | `references/10-version-evidence.md` | 进入文档化输出路径，确认打印/归档要求 |
| 明确要截图包/证据包/speaker notes | `references/03-delivery-routing.md` + `references/10-version-evidence.md` | `references/05-content-standards.md` | 明确命名、版本和证据字段 |
| 需要叙事结构、会议讲稿、销售/路演话术 | `references/14-narrative-patterns.md` + `references/08-skill-governance.md` | `references/05-content-standards.md` | 检测`huashu-ppt`；不可用且必要时请求安装/启用或内嵌，用户拒绝则停止 |
| 需要分步呈现、藏露节奏、主动触发 | `references/06-interaction-standards.md` + `references/08-skill-governance.md` | `references/14-narrative-patterns.md` | 检测`guizang-ppt-skill`；不可用且必要时请求安装/启用或内嵌，用户拒绝则停止 |
| 涉及动效、动画、转场节奏、分步显隐 | `references/17-motion-design-standards.md` + `references/06-interaction-standards.md` | `references/07-qa-checklist.md` | 先由动效设计部输出动效脚本；未经审核不得进入HTML实现 |
| 提升审美、避免AI味、优化视觉 | `references/04-design-standards.md` + `references/11-aesthetic-anti-ai.md` + `references/15-visual-reference-library.md` | `references/08-skill-governance.md`、`references/visual/reference-entries.md` | 检测`taste-skill`、`stylekit-skill`、`PPT-Design-DNA-main`/`design-dna`和`guizang-ppt-skill`；StyleKit作为设计库候选源，PPT-DNA作为三维设计身份系统，guizang作为演示版式/主题节奏系统，均必须记录调用/不调用理由和吸收证据 |
| 用户质疑design-dna/guizang/审美/UI/动效没有深度集成 | `references/18-history-derived-governance.md` + `references/20-design-dna-guizang-integration.md` + `references/08-skill-governance.md` | `skill-creator`、`references/04-design-standards.md`、`references/11-aesthetic-anti-ai.md`、`references/17-motion-design-standards.md`、`references/07-qa-checklist.md` | 先进入Skill治理，不生成产物；补齐Presentation Design DNA、guizang桥接、UI/动效吸收、QA吸收字段和阻断条件 |
| 用户质疑stylekit/taste/frontend-slides/html-ppt/huashu-design等相关Skill没有集成，或指出排版/UI不好看、动效单一 | `references/18-history-derived-governance.md` + `references/21-design-skill-stack-integration.md` + `references/08-skill-governance.md` | `skill-creator`、`references/20-design-dna-guizang-integration.md`、`references/17-motion-design-standards.md`、`references/07-qa-checklist.md` | 先盘点相关Skill并建立Design Skill Stack决策表；补StyleKit吸收、TasteSkill预检、演示引擎选择和Motion source map；不生成产物 |
| 用户指出HTML Pre/HTML PPT排版丑、控件破坏画面、动效单一，或要求审美专项重做 | `references/22-html-pre-visual-director.md` + `references/23-online-research-toolchain.md` + `references/21-design-skill-stack-integration.md` | `references/06-interaction-standards.md`、`references/17-motion-design-standards.md`、`references/07-qa-checklist.md` | 先做HTML Pre视觉导演合同、外部搜索/阻断记录、浏览器验证计划和presentation chrome复盘；不得直接继续生成全稿 |
| 用户指出AI味重、不好看、像模板 | `references/04-design-standards.md` + `references/11-aesthetic-anti-ai.md` + `references/07-qa-checklist.md` | `references/10-version-evidence.md` | 优先进入设计系统与Style Frame复盘；必须做截图/肉眼审美复核和问题页Page Spec重写，不只改局部CSS |
| 用户质疑Skill、subagent、副主编、审美学习、搜索趋势、模板套用、模板改造或要求基于历史对话全面修订 | `references/18-history-derived-governance.md` + `references/16-multi-agent-governance.md` + `references/08-skill-governance.md` + `references/11-aesthetic-anti-ai.md` + `references/07-qa-checklist.md` | `skill-creator`、`references/15-visual-reference-library.md` | 先从历史对话整理需求表，暂停所有产物生产，只修Skill系统文件；若用户提到subagent即视为持续授权创建；输出失败审计和Skill修订 |
| 用户要求完整检查/全面更新本Skill | `SKILL.md` + `AGENTS.md` + `agents/openai.yaml` + 全部`references/*.md` + `references/18-history-derived-governance.md` | `skill-creator`、`references/visual/reference-entries.md`、`skills/skills.manifest.yaml` | 输出《完整Skill审计矩阵》：入口触发、流程阻断、部门职责、QA证据、经验回写、元数据和验证脚本逐项检查；每项修订必须绑定触发、证据、阻断、责任和文件路径 |
| 用户指出旧版只是参考、没有大刀阔斧变化、部门只套旧模板 | `references/11-aesthetic-anti-ai.md` + `references/04-design-standards.md` + `references/16-multi-agent-governance.md` | `references/15-visual-reference-library.md` | 必须先过旧版否决门，明确不可继承项和新版不可逆改变 |
| 用户指出控件碍眼、底部按钮破坏画面 | `references/06-interaction-standards.md` + `references/07-qa-checklist.md` | `references/11-aesthetic-anti-ai.md` | 优先进入presentation chrome复盘 |
| 点名某页有问题、要求修某页 | `references/04-design-standards.md` + `references/07-qa-checklist.md` + `references/10-version-evidence.md` | `references/11-aesthetic-anti-ai.md` | 进入问题页复盘和同类页联动 |
| 修改、回退、用户退回后的局部修订 | `references/19-approved-production-flow.md` + `references/16-multi-agent-governance.md` + `references/07-qa-checklist.md` | `references/10-version-evidence.md` | 必须走总编分发、对应副主编审核、执行层修订、同一副主编复审、全部适用副主编一致审核、副总编一致性审核、总编二级审核、QA回归、用户复验 |
| 要求审查团队分工、RACI、多Agent或执行责任 | `references/01-team-roles.md` + `references/16-multi-agent-governance.md` | `references/02-workflow.md` | 输出三级团队、Agent编制、一级/二级复核与责任调整 |
| 需要新增部门或发现现有部门不足 | `references/01-team-roles.md` + `references/16-multi-agent-governance.md` | `references/02-workflow.md` | 先提交新增部门申请；总编批准并创建子Agent后才成立 |
| 任务跨多轮、文件很多、日志很长 | `references/09-context-engineering.md` | `references/10-version-evidence.md` | 检测`headroom`；不可用且影响质量时请求安装/启用或内嵌，用户拒绝则停止或改写任务边界 |
| 要求审计或修改本Skill本身 | `SKILL.md` + `AGENTS.md` + `agents/openai.yaml` + 全部`references/*.md` | `references/visual/reference-entries.md`、`skills/skills.manifest.yaml` | 检查路由、层级、可执行性和验证脚本；审计视觉参考库时必须读取条目库 |

## 强制门禁

1. 未完成项目意图识别，不得进入页面生产。
2. 未完成交付定义，不得承诺HTML、PPTX、PDF等具体交付物。
3. 未创建并填写本版本《团队协作与生产记录》，不得进入生产；该记录必须包含RACI矩阵、Agent编制表和制作工单，且不能只在最终回复中补写。
4. 未检测关键Skill可用性，不得承诺依赖该Skill的能力。
5. 未完成Skill调用决策，不得调用或宣称已调用相关Skill；所有相关Skill必须被标记为“调用/可用但不调用/需安装/需内嵌/阻断”之一。
6. Skill输出不得直接交付，必须经过能力域副主编一级复核、总编二级复核和QA冻结；审查结论必须写入《团队协作与生产记录》。
7. 未通过Vx版本原子门禁和Subagent Evidence Lock，不得生成新版本，也不得归档、复制旧版、创建Vx目录、导出截图或生成validation。每次合规生成新版本后必须归档到`versions/<version>/`；根目录只保留最新版。
8. 完整视觉生产前必须通过Style Frame与anti-AI aesthetic gate；未通过不得进入全稿HTML或PPTX生产。
8c. Style Frame必须有真实截图证据，不能只写文字描述。若用户此前退回“丑/像模板/没有审美”，下一版本必须先交Style Frame或3-5页样张，由副主编复核后再扩展全稿。
8a. 用户提供视觉参考图、风格链接或审美方向时，必须先沉淀到`references/15-visual-reference-library.md`或其子文件，并标注通用型/专用型；不得只在对话中临时引用。
8b. 任何视觉方案必须附带参考经验转译结论：参考来源、通用/专用判断、可复用经验、明确不照搬项、当前用户资料绑定点、品牌色/趋势取舍、页面族谱映射。缺少该结论时，不得宣称“已参考过往经验”。
8b1. 若用户提供的参考图中包含多页PPT内容，必须先建立《多页视觉系统拆解表》，逐页拆出页面角色、跨页视觉语法、信息层级、真实视觉锚点、组件语义、动效/静止策略和交付路线。不得把长图当作单张海报参考，也不得只学习配色、网格、贴纸、斜切块或表层热闹感。
8b2. 正向参考图深拆硬门禁：任何被判定为“正向/优秀/可学习”的参考图，都必须追加《正向参考图深拆与经验总结表》。该表至少回答：为什么这样配色、颜色承担什么语义；文字如何配合画面、标题/正文/注释/口播文案如何分工；字体、字号、字重、字距、行距和样式为什么适合；版面如何规划、视觉重心和留白如何组织；页面之间如何切换、跨页节奏如何延续；如果由当前团队重新设计，会提出哪2-3个替代方案；动效如何服务讲述、交互和HTML状态机；哪些经验能迁移，哪些表层元素必须舍弃。缺少该表时，不得进入Style Frame、Page Spec或正式生产，也不得宣称“已学习正向参考”。
8d. 若使用`guizang-ppt-skill`，必须明确选择风格A或B；风格B必须写入`data-layout`/版式映射表、主题节奏表和单一accent策略。没有版式映射，不得宣称使用了guizang瑞士风。
8e. Style Frame部门协同硬门禁：Style Frame生成记录必须包含《内容到UI/动效转译表》《部门协同输入表》和《冲突解决记录》。语言内容负责每页核心判断、教学/演示动作、内容关系和文案密度；品牌审美负责参考趋势转译和视觉母线；版式/UI负责网格、组件、字阶、控件与状态；动效设计负责分步显隐、转场、静止页和export稳定态；交互工程负责实现可行性、浏览器行为和导出模式；QA负责截图有效性、可读性和冻结风险。缺少任一适用部门输入，不得称为“Style Frame已生成”。
8f. Design DNA × guizang深度集成硬门禁：任何HTML/PPT/Slides视觉生产、Style Frame或审美退回恢复生产，必须先读取`references/20-design-dna-guizang-integration.md`并产出Presentation Design DNA档案、DNA来源追踪表、UI吸收表、动效吸收表和设计引擎桥接表。若使用guizang，还必须产出A/B适配与弃用表、逐页layout/Sxx映射、主题节奏、图片槽位和模板改造差异。只有“读过design-dna/guizang”“采用瑞士风/杂志风”“生成DNA JSON”“写了Sxx编号”均不算集成；缺少吸收证据不得进入全稿生产、Style Frame通过或QA冻结。
8g. Design Skill Stack集成硬门禁：任何HTML/PPT/Slides视觉生产、Style Frame、审美退回恢复生产，或用户指出排版/UI不好看、动效单一时，必须读取`references/21-design-skill-stack-integration.md`并完成Design Skill Stack决策表和《部门Skill使用矩阵》。`stylekit-skill`必须输出或人工等价输出风格候选、style ownership、composition_plan和quality_gate；`taste-skill`必须转译为Design Read、DESIGN_VARIANCE/MOTION_INTENSITY/VISUAL_DENSITY和排版/UI pre-flight；`frontend-slides`/`html-ppt`/`guizang`/`huashu-design`/`huashu-ppt`/`huashu-slides`必须记录引擎选择、弃用理由和动效来源。需求/交付副主编必须判断`ppt-master`、`frontend-slides`、`html-ppt`、`guizang-ppt-skill`、`huashu-ppt`/`huashu-slides`、`humanize-ppt`对交付格式、可编辑性、讲者备注和降级审批的影响；语言内容副主编必须判断`humanize-ppt`、`huashu-ppt`/`huashu-slides`、`huashu-design`、`taste-skill`对叙事结构、页面密度和讲者动作的影响。缺少任一适用部门证据时，不得宣称“相关Skill已集成”。
8h. Online Research Stack硬门禁：任何HTML Pre/HTML PPT/Slides视觉生产、Style Frame、审美退回恢复生产、用户要求联网搜索/外部参考/当前趋势/最新文档/浏览器视觉验证，必须读取`references/23-online-research-toolchain.md`并完成Online Research Stack决策表、外部参考搜索记录、外部视觉参考转译卡、最新文档检索记录或联网/工具阻断记录。Tavily/Brave/Firecrawl/Context7/Playwright等必要控件缺失时，必须先提请用户同意安装/启用；用户拒绝则本Skill停止在阻断状态。缺少这些证据时，不得宣称“已联网搜索”“已结合最新趋势”“已用最新官方文档”或“已完成真实浏览器视觉验证”。
9. anti-AI检查必须确认：是否存在过度通用的渐变、玻璃拟态、网格背景、随机装饰线；是否每页都是“标题 + 卡片 + 图标”；是否颜色过多、阴影过重、留白不稳；是否装饰多于信息；是否标题很大但信息组织薄弱；是否图标和色块没有业务含义；是否缺少与具体项目材料绑定的视觉证据；是否像模板库作品而非为当前受众和场景定制。
10. HTML演示若翻页、目录、帮助、全屏、提示、编辑等控制条默认强显示，不得通过QA。
11. 若用户明确指出“AI味重”“不好看”“控件碍眼”“像模板”，必须优先进入设计系统与presentation chrome复盘，不得只修改局部CSS。
12. 若已有HTML版本被用作改进依据，必须抽查关键页源码与截图证据，记录“重复版式、文字密度、真实素材、控件状态、页面重心”五项结论；没有全页截图、contact sheet或重点页截图证据时，不得写“审美通过”。浏览器肉眼复核只能补充截图证据，不能替代截图证据。
13. 完整交付前必须检查截图状态，确保页面在audience/export模式下视觉干净。
13a. HTML/PPT截图QA必须检查非空像素、可见文字和重点页截图内容；只检查页数、尺寸、裁切、键盘交互不得标记为QA通过。
14. 任何冻结稿若仍存在大面积占位框、连续卡片矩阵、标题字号压过内容、关键页没有真实视觉锚点，必须退回Style Frame或Page Spec重写，不得只在QA表里标“后续替换”。
15. 若用户指出未按团队分工执行，必须立即暂停当前生产任务，先修复Skill或协作记录缺口，再由总编重新下发工单；不得继续补丁式修改产物。
16. 若subagent工具可用但未创建独立能力域Agent，不得声称“团队协作已执行”；使用本Skill进入生产/修复/审稿/QA冻结/Style Frame/Vx动作时，subagent建立不需要用户另行同意，必须建立；若subagent工具不可用，必须写入`SUBAGENT-BLOCKER`并停止正式生产或复核链路。
17. 工具、外部搜索控件、浏览器验证控件或必要部门不可用时，不得自动降级。必要工具缺失时必须先提请用户同意安装/启用；用户拒绝安装、拒绝授权或不提供API key时，本Skill停止在阻断状态。只有用户改写任务边界，不再要求该能力时，才可另起降级任务。
18. 任意轮次的复核不得由执行层自审、主Agent代签或最终回复补签；缺少副主编subagent复审记录时，副总编不得接收，总编不得接收，QA不得冻结。
19. 用户上传文件后的初步方案必须由需求/交付、语言内容、品牌审美、版式/UI、动效设计、交互/交付等部门并行审查，并在《部门一致意见表》中全部通过后提交副总编；副总编通过后才可提交总编。存在冲突时先由副主编协商形成一致方案，不得把未达成一致的方案交给总编拍板。
19a. 页数充分性硬红线：完整视觉生产、既有版本重做、用户审美退回恢复生产前，必须完成跨部门页数充分性判断。缺少该表，或表中只引用旧版/模板/用户样本页数而没有内容、文案、审美、UI、动效和QA判断，不得进入Page Spec、Style Frame或全稿生产。
20. 视觉硬红线：黑底黑字或任何低对比文字、无语义的多色线条、同一页面混用黑/白/高饱和蓝或黑/红/绿等冲突色块和线条、大面积纯黑/纯白/强蓝硬切换造成观看不适、表格表头不显眼、表格正文对齐规则混乱、术语缩写组件关系错误、动效无脚本或影响导出，均为QA否决项，不得标记审美通过。
20a. 光学平衡硬红线：封面、章节页、核心模型页、案例页、工作台页和收束页必须逐页检查上/下、左/右、主/次视觉重量与阅读路径。出现明显头轻脚重、头重脚轻、左重右轻、右重左轻、底部堆积、单侧过密、主视觉漂移或留白无组织时，UI和审美副主编必须退回Page Spec或视觉母线；不得用“截图非空”“文字未溢出”或“工程烟测通过”覆盖。
20b. 分步呈现硬红线：任何包含“5点/多步骤/阶段/链路/录用后/面试链路/逐项讲解”等结构的页面，必须附《首态/后续态矩阵》，列明初始可见内容、每次触发出现内容、不得提前出现内容、最终完成态。若第1项无需触发就显示、后续步骤提前露出、多个语义阶段无理由合并出现、或触发次数与内容点数量不一致，动效和交互QA均必须否决。
20c. 动效美感硬红线：HTML演示动效不得只满足“能切换”。页间转场和同页分步必须有明确运动语法、方向逻辑、节奏差异、缓入缓出、停顿与完成态；全稿统一`opacity + translateY`、机械匀速、突兀硬切、无空间连续性、无讲述目的或只靠CSS默认transition，均视为动效设计失败。动效失败时不得进入QA冻结。
20c1. HTML状态机与交互硬红线：HTML演示不是PPT点击动画模拟。任何分步呈现、目录跳转、局部展开、口播Demo、练习页或互动页，必须附《HTML状态机与交互合同》，定义`idle`、`reveal(n)`、`completed`、`reverse/back`、`skip/nav`、`export/print`等状态，说明键盘、鼠标、触摸、滚轮、目录跳转、焦点、aria、输入节流、回退、重播和截图/export稳定态。若只是点击后出现下一个图标、表格或文字，交互工程和动效QA均必须否决。
20d. 内容文案硬红线：语言内容副主编必须逐页检查标题是否承担判断、正文是否口语可讲、步骤命名是否匹配讲师动作、页面是否有可被学员记住的带走句。若文案只是资料压缩、卡片标题并列、缺少讲述钩子或为了模板牺牲内容关系，不得交给UI排版，更不得由UI/动效掩盖内容失败。
21. 发现需要新部门时，必须提交新增部门申请，经副总编预审、总编批准并创建独立subagent后才可成立。不得由主Agent临时扮演。
22. QA冻结后必须提交用户验收并记录结论；用户退回时必须由总编分发给对应副主编，重新进入副主编复审、总编复核、QA回归和用户复验闭环。
23. 交付措辞硬门禁：未完成实现后副主编复核、QA人工审美冻结和用户验收记录时，最终回复不得使用“已交付”“完成”“最终版”“通过QA”“多轮复核完成”等措辞；必须明确写“未冻结/未交付/阻断”，并列出缺失门禁。自动验证通过只能写“工程烟测通过”。
24. 预审不抵扣复核：生产前子代理建议、探索报告、内容/审美/动效/QA预检，只能作为输入；不能抵扣执行后对真实截图和文件的复核轮次。协作记录必须分开记录“生产前输入”“实现后一级复核”“退回复审”“QA冻结”。

## 最低交付标准

- 诊断类任务：交付《项目类型判断卡》《受众与使用场景卡》《原始资料盘点表》《交付定义卡》《内容差距清单》《页数充分性判断表》《叙事结构建议》《UI方向卡》《交付格式与降级审批路径》，小任务可合并为简表。
- 模板类任务：追加《模板解析表》和《页数预算表》。
- 完整视觉生产任务：追加《参考经验转译卡》；若采用正向参考，追加《正向参考图深拆与经验总结表》；再追加《内容到UI/动效转译表》《Style Frame部门协同输入表》《视觉风险清单》和Style Frame确认记录。
- HTML演示任务：追加presentation chrome模式检查记录和《HTML状态机与交互合同》，确认audience/presenter/export模式、输入事件、焦点/aria、回退/重播、节流和截图/export稳定态。
- 生产类任务：交付主文件、必要附件、QA记录和版本归档。
- 团队协作类任务：交付《团队协作与生产记录》文件，内含RACI矩阵、Agent编制表、部门一致意见表、制作工单、能力域一级复核记录、副主编复审循环记录、总编二级复核记录、QA冻结/未冻结记录、用户验收记录。
- Skill治理类任务：交付可用性确认、阻断记录、版本锁定和必要的manifest/lock更新。
- 完整Skill审计任务：追加《用户最新要求锁定表》《历史对话需求整合表》《完整Skill审计矩阵》《规则闭环映射表》《修订影响面清单》和验证记录；必须证明本次未创建或修改交付产物目录。
- 审美类任务：交付Style Frame确认记录、反AI味检查结论、截图/肉眼复核结论和需要重写的Page Spec清单。

最低交付标准只在对应门禁全部完成后才可称为交付；缺少实现后复核或QA冻结时，只能交付失败审计、修订记录、Page Spec或阻断说明，不能交付视觉版本。

## 能力缺失处理路径

- 任何工具、subagent或必要部门不可用时，第一动作都是暂停正式生产，写入阻断项，而不是直接降级。
- 总编必须先判断该能力是否必要、是否可安装、启用、内嵌、修复、改范围或等待恢复。
- 必要控件或Skill缺失时，必须先提请用户同意安装/启用或提供授权；用户拒绝、未响应、未提供必要凭据或权限阻断时，本Skill停止当前任务。
- subagent和必要部门Agent不走用户同意流程；建立失败时写入`SUBAGENT-BLOCKER`并停止生产/复核链路。
- 只有用户明确改写任务边界为不再需要该能力时，才可另起新边界任务；新任务不得宣称已完成原能力。
