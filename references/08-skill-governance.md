# 08-skill-governance

读取时机：当任务依赖ppt-master、frontend-slides、taste-skill、stylekit-skill、Headroom、html-ppt-skill-main、PPT-Design-DNA-main、humanize-ppt-main、huashu-ppt、guizang-ppt-skill、huashu-design等外部或本地Skill，或需要安装、验证、阻断、锁定版本、检查license时读取。若用户质疑design-dna/guizang/审美/UI/动效没有深度集成，同时读取`20-design-dna-guizang-integration.md`。若用户质疑stylekit/taste/frontend-slides/html-ppt/huashu-design等相关Skill没有集成，或指出排版/UI不好看、动效单一，同时读取`21-design-skill-stack-integration.md`。若用户要求联网搜索、外部参考、当前趋势、最新文档、浏览器视觉验证，或涉及Tavily、Brave、Firecrawl、Context7、Playwright MCP，同时读取`23-online-research-toolchain.md`。

## Skill来源优先级

1. 用户本地已安装Skill，例如`$CODEX_HOME/skills/<skill>/SKILL.md`或`~/.codex/skills/<skill>/SKILL.md`。
2. 当前项目包`skills/vendor/`内嵌Skill。
3. 通过`skills.manifest.yaml`自动安装。
4. 读取远程或本地`SKILL.md`作为单次上下文。
5. 若必要能力仍不可用，停止当前任务，除非用户明确改写任务边界为不再需要该能力。

项目内`vendor=missing`不等于Skill不可用。只要用户本地已安装并能读取`SKILL.md`，就应按“可调用”记录，并在调用前完整读取该Skill正文。只有本地、vendor和真实verify命令均不可用，才算缺失；缺失且必要时必须先按本文件请求安装/启用或内嵌，用户拒绝或权限阻断时停止当前任务。

## Skill调用决策权

不是所有可用Skill都应该被调用。Skill调用必须服从团队协作分派，而不是由主Agent按清单全量加载。

| 决策层级 | 权限 |
| :--- | :--- |
| 总编 | 定义目标、风险、交付路线；批准关键Skill调用或禁用 |
| 能力域副主编 | 根据职责提出需要调用的Skill和用途 |
| 工具链与上下文工程副主编 | 验证Skill是否可用、是否已安装、是否需要安装/内嵌、是否触发阻断 |
| 执行层 | 只按制作工单调用Skill，不自行扩大调用范围 |
| QA副主编 | 检查Skill调用证据和输出是否经过复核，不按“调用过Skill”自动放行 |

调用Skill前必须在《制作工单》或《Skill可用性与版本确认单》中写明：

- 调用原因；
- 触发该调用的能力域副主编；
- 预期输出；
- 是否会替代或只是辅助人工复核；
- 不调用其他可用Skill的理由。

可用但与当前工单无关的Skill必须标记为“可用但不调用”。禁止为了显得流程完整而把所有可用Skill都读入上下文。

## 本地Skill别名映射

manifest中的历史名称可能与用户本地安装目录不同。验证时必须使用以下别名候选：

| manifest名称 | 本地已安装目录候选 | 说明 |
| :--- | :--- | :--- |
| `taste-skill` | `taste-skill` | 全局审美/反AI味前端Skill |
| `stylekit-skill` | `stylekit-skill`、`stylekit-style-prompts` | StyleKit风格提示词设计库、风格候选检索和Style Frame方向辅助 |
| `html-ppt-skill-main` | `html-ppt-skill` | HTML PPT基础框架 |
| `PPT-Design-DNA-main` | `design-dna` | 设计DNA、页面族谱和视觉系统 |
| `humanize-ppt-main` | `humanize-ppt` | 文案自然化与压缩 |
| `huashu-ppt` | `huashu-slides` | 花叔slides/PPT叙事能力 |
| `frontend-slides` | `frontend-slides` | HTML互动演示 |
| `ppt-master` | `ppt-master` | PPT生成与转换 |
| `guizang-ppt-skill` | `guizang-ppt-skill` | 横向翻页网页PPT |
| `headroom` | `headroom` | 上下文压缩和长任务交接；本项目已内嵌vendor版本 |

## 能力缺失处理规则

- 任何必要Skill、工具、subagent或部门Agent不可用时，第一动作是暂停正式生产，写入阻断项和原计划，不得直接转入内置流程。
- 工具链与上下文工程副主编先判断是否能安装、启用、内嵌、改任务范围或等待工具恢复；必要能力缺失时，必须向用户说明安装/启用需求并获得同意。
- 用户拒绝安装/启用、拒绝授权、未提供必要凭据或权限阻断时，本Skill停止当前任务。只有用户明确改写任务边界为不再需要该能力时，才可另起新边界任务；新任务不得宣称已完成原能力。
- Tavily、Brave、Firecrawl、Context7、Playwright MCP等联网/浏览器控件属于工具链能力。若当前任务必须使用这些控件，缺失时默认帮助用户安装/启用，但必须先提请用户同意；用户拒绝安装、拒绝授权、未提供必要API key或权限阻断时，本Skill停止当前任务，不得自动降级。
- 只有用户改写任务边界，明确不再要求联网、最新文档或真实浏览器验证时，才可另起降级任务；降级任务不得宣称已完成原能力。
- `ppt-master`不可用且仍需要原生可编辑PPTX：请求安装/启用；拒绝则停止，不承诺原生可编辑PPTX。
- `frontend-slides`不可用且仍需要完整Web演示：请求安装/启用；拒绝则停止，不承诺完整Web演示体验。
- 文案类Skill、`taste-skill`、`headroom`、设计类Skill或PDF导出能力不可用时，先判断是否为当前任务必要能力；必要则请求安装/启用/内嵌，拒绝则停止。
- 所有能力缺失必须写入《Skill可用性与版本确认单》和《阻断记录》。

## 审美Skill门禁

- 使用`taste-skill`时，其输出只能作为审美辅助，不得替代总编确认。
- 若`taste-skill`在用户本地已安装，涉及完整视觉生产、Style Frame、反AI味、审美复核或用户质疑“糊弄/不好看/模板感”时，必须读取并调用其规则，而不是直接降级为内置清单。
- `taste-skill`适用边界必须写清：它偏向landing/portfolio/redesign和前端视觉反AI味；若当前任务是演示文稿，应只转译其审美预检、反AI味、对比度、布局重复、真实视觉资产和pre-flight思想，不机械套用网页landing规则。
- 完整页面生产前必须有Style Frame确认记录。
- 未通过反AI味负面清单审查时，不得进入全稿生产。

## StyleKit设计库门禁

- `stylekit-skill`是风格提示词设计库和视觉方向检索工具，不是模板引擎，也不是最终审美裁决者。
- 当任务涉及Style Frame、视觉方向选择、风格混合、用户要求“更好看/更有审美/参考风格/设计库/风格提示词”，或品牌审美副主编需要候选风格时，必须把`stylekit-skill`写入《Skill调用决策表》，结论只能是“调用/可用但不调用/需安装/需内嵌/阻断”之一。
- 调用前必须先读取`references/visual/reference-entries.md`中的`REF-20260621-01`，并把StyleKit输出转译为《参考经验转译卡》，不得把`hard_prompt`、`style_choice`或style slug直接当成当前deck设计方向。
- 若调用StyleKit，必须记录查询词、候选slug、采用slug、弃用slug及理由、`design_brief`中被采用的规则、`composition_plan`的所有权分配、`quality_gate`状态和QA修正动作。
- 若不调用StyleKit，必须说明原因：例如用户已有严格品牌规范、任务不涉及视觉方向、当前参考库条目已经足够、或StyleKit不可用且用户未批准降级。
- StyleKit输出偏前端语境，必须由品牌审美副主编和版式/UI副主编转译：page/section转为页面族谱，component转为页内视觉模块，state/interaction转为动效脚本或不适用说明。
- StyleKit不可用时，不得宣称已获得StyleKit设计库校准；若当前任务必须使用StyleKit，先请求安装/启用，用户拒绝则停止；若用户明确改写任务边界为不需要StyleKit，只能改用`15-visual-reference-library.md`、`04-design-standards.md`和`11-aesthetic-anti-ai.md`人工筛选，并记录边界变更。

### StyleKit吸收标准

StyleKit只有进入以下五类产物，才算被本系统完整吸收：

1. 审美意图：purpose、audience、tone、memorable hook必须写入视觉母线、关键页第一眼落点和收束记忆点。
2. 反泛化测试：swap、squint、signature、token四项测试必须写入Style Frame或审美QA；失败时退回Page Spec或视觉母线。
3. Token层级：Brand→Semantic→Component→State必须被转成调色板语义、正文色阶、组件状态、表格/标注/控件规则。
4. 组件架构：Base→Variant→Size→State→Override必须被转成页面内组件规范，并说明哪些variant适用于哪些页型。
5. 状态/动效转译：hover、focus、disabled、active、reduced-motion等前端概念必须转成首态、揭示态、强调态、静止页、export稳定态或不适用说明。

若记录中只有`style_choice`、slug、`hard_prompt`、风格形容词或“已读取StyleKit”，但没有上述五类转译，必须标记为“已读取未吸收”。“已读取未吸收”不能作为审美通过、Style Frame通过、设计引擎调用成功或QA冻结证据。

## 演示设计Skill门禁

涉及HTML/PPT/Slides视觉生产时，必须选择一个主设计Skill或客户母版作为设计引擎。只读取Skill名称、只借用风格标签、只说“参考了guizang/html-ppt/frontend-slides”都不算调用。

涉及排版/UI不好看、动效单一或用户点名相关Skill未集成时，必须先按`21-design-skill-stack-integration.md`建立Design Skill Stack决策表。`stylekit-skill`、`taste-skill`、`design-dna`、`guizang-ppt-skill`、`frontend-slides`、`html-ppt`、`huashu-design`均必须被标记为调用/不调用/降级/阻断之一；可用但不调用时必须写明理由。

设计Skill后置规则：主设计Skill只能在《部门一致意见表》《参考经验转译卡》《页数充分性判断表》《内容到UI/动效转译表》《动效方向》和QA前置风险完成后选择。Skill、模板、主题色、风格B/风格A、Sxx版式编号都只是实现约束，不是设计结论。若执行记录中先出现“采用某Skill/某风格/某主题色”，再补写内容转译、页数判断或部门意见，该记录无效，产物不得创建或冻结。

深度定制证明：调用任何设计Skill前，必须写明当前用户资料如何生成页数充分性判断和页面族谱，例如哪些页必须新增、拆分、合并或进入附录，哪些页是讲授、哪些页是案例剧场、哪些页是工作台、哪些页是AI复核、哪些页需要静止、哪些页需要分步揭示。若无法说明“为什么当前内容必须这样长出来”，不得调用模板生成全稿。

模板适配性证明：调用任何设计Skill前，必须先证明候选模板/版式适合当前内容；不能只证明它“好看”或“可用”。证明字段至少包含：当前内容需求、候选模板可承载项、无法承载项、弃用模板/趋势、是否会扭曲用户内容、最终是否采用。只要出现“模板不完全合适但先套上再说”的判断，工具链副主编必须阻断调用。

模板改造证明：候选模板被采用后，调用设计Skill前还必须有《模板改造差异表》。字段至少包含：页码、原模板/版式、保留项、改写项、新增项、删除项、内容密度调整、视觉锚点替换、动效调整、责任副主编、是否允许执行层生产。没有该表，工具链副主编不得执行模板复制、模板生成、Sxx套用或全稿HTML/PPT创建。

| Skill | 真正调用的最低证据 |
| :--- | :--- |
| `guizang-ppt-skill` | 完整读取SKILL正文；在部门输入完成后选择风格A或B；若选瑞士风，读取`themes-swiss.md`、`layouts-swiss.md`，建立页码→内容角色→版式/主题节奏/图片槽位/动效意图映射；再建立Sxx改造差异表；必要时运行或等价执行Swiss验证 |
| `html-ppt` | 完整读取SKILL正文；在部门输入完成后选择主题或full-deck模板；建立页码→内容角色→layout/theme/动画映射和模板改造差异表；不得从零手写所有页面，也不得让模板决定内容角色 |
| `frontend-slides` | 完整读取SKILL正文；保留固定16:9舞台；产出Style Preview或等价Style Frame；全稿生成前确认密度、视觉方向和内容到UI转译已完成 |
| `taste-skill` | 完整读取SKILL正文；提取适合演示文稿的反AI味、布局重复、真实资产和pre-flight规则；不机械套landing页规则 |
| `stylekit-skill` | 完整读取SKILL正文和`REF-20260621-01`；记录查询词、候选slug、采用/弃用理由、`design_brief`、`composition_plan`、`quality_gate`；把输出转译为参考经验转译卡、页面族谱、UI方向和动效脚本约束 |
| `taste-skill` | 完整读取SKILL正文；转译Design Read、DESIGN_VARIANCE/MOTION_INTENSITY/VISUAL_DENSITY、layout repetition ban、卡片/色彩/字体/动效pre-flight；不得机械套网页landing规则 |
| `huashu-design` | 完整读取SKILL正文；在方向模糊或审美退回时吸收三方向真实视觉探索、品牌资产协议、反AI slop、动画导演/连续运动叙事和五维评审；不得把它当普通HTML模板 |

若没有上述映射表，不得在协作记录、README或最终回复中宣称“已调用/已结合该Skill”。只能写“已读取但未落实，不能作为审美通过证据”。若映射表没有当前用户资料、内容关系和部门意见来源，只写模板编号或主题色，同样无效。

### PPT-DNA与guizang吸收标准

`PPT-Design-DNA-main`/`design-dna`和`guizang-ppt-skill`属于品牌审美与版式/UI的深度设计能力，不是执行层快捷模板。

具体执行合同见`20-design-dna-guizang-integration.md`。本节的吸收标准必须落入`20`要求的Presentation Design DNA档案、DNA来源追踪表、设计引擎桥接表、UI吸收表、动效吸收表和QA吸收检查；否则只能记录为“已读取未落实”。

PPT-DNA只有满足以下条件才算吸收：

1. `design_system`转译为调色板语义、字阶、网格、间距、组件、表格、图表和动效token。
2. `design_style`转译为视觉母线、页面族谱、视觉重心、留白策略、构图方法和品牌语气。
3. `visual_effects`转译为HTML/PPT/PDF可实现边界、性能层级、fallback、reduced motion和截图/导出策略。
4. 每个关键token都能追溯到用户资料、品牌规范、参考图、内容关系或交付约束。
5. QA能从最终截图或产物中看到这些规则被执行。

guizang只有满足以下条件才算吸收：

1. 品牌审美副主编明确A电子杂志或B瑞士国际主义的适配理由，并说明弃用另一方向的原因。
2. 版式/UI副主编建立页码→页面角色→内容关系→layout/Sxx→选用理由→图片槽位→动效意图映射。
3. 若选瑞士风，必须保留S01-S22正文版式登记、`data-layout`、单一accent、中文标题分档、字号/字重阶梯和直角纯色规则。
4. 必须有主题节奏表、模板适配性审查表和模板改造差异表；不得把模板骨架直接当成成品。
5. 实现后必须有类名/版式校验、截图视觉核对和QA人工复核；无法运行校验脚本时写等价人工检查。

若PPT-DNA只有JSON、字段摘要或形容词，必须标记为“已提取未吸收”。若guizang只有风格名、模板路径、Sxx编号或主题色，必须标记为“已选模板未吸收”。两者都不能作为审美通过、Style Frame通过、设计引擎调用成功或QA冻结证据。

### Skill真实使用证据门禁

完整读取Skill正文只是前置动作，不构成使用证据。设计类Skill必须额外证明：

1. 从Skill中提取了哪些具体规则，而不是只写Skill名称或风格标签。
2. 哪些规则被采用，哪些规则因当前内容/受众/品牌/观看距离被弃用。
3. 采用规则如何进入页面族谱、模板改造差异表、CSS变量、组件命名、动效脚本或截图策略。
4. 产物截图能否看出这些规则被执行。
5. QA副主编是否逐项核对“Skill规则已落地/未落地/不适用”。
6. 设计Skill是否改变了页数、页面族谱或内容密度；如有改变，是否回到页数充分性和部门一致意见复核。

若只有“已读取SKILL.md”“采用某风格”“使用某模板编号”，但没有规则提取、页面映射、实现证据和截图核验，只能记录为“已读取未落实”，不得作为审美通过或设计引擎调用成功证据。

实现后Skill复核：设计Skill参与生产后，工具链副主编必须把最终产物与该Skill的关键规则逐项对照，至少检查版式映射、色彩策略、字体/字阶、动效脚本、截图验证和禁用项。对照未完成时，不得写“Skill已生效”；对照发现偏离时，必须退回对应副主编和执行层。

## 外部Skill合理调用规则

| Skill | 可用时调用场景 | 不可用时审批后可选边界 |
| :--- | :--- | :--- |
| `ppt-master` | 用户明确要原生可编辑PPTX、母版、备注、动画 | 输出PPTX page spec、HTML preview、人工母版说明 |
| `frontend-slides` | 用户明确要HTML互动演示、Web slides、浏览器播放 | 输出静态HTML或page spec |
| `taste-skill` | 用户要求更美观、反AI味、Style Frame审美评审 | 使用`11-aesthetic-anti-ai.md`人工评审 |
| `stylekit-skill` | Style Frame方向检索、风格候选比较、风格混合、设计库校准、风格提示词转译 | 使用`15-visual-reference-library.md`和`REF-20260621-01`的人工规则筛选，不宣称StyleKit校准 |
| `headroom` | 工具链与上下文工程副主编判断任务长、文件多、日志长、跨多轮生产、subagent输出多或接近上下文压缩 | 使用上下文摘要、文件索引、版本日志 |
| `huashu-ppt` | 叙事结构、会议讲稿、培训讲述、路演话术、销售提案话术 | 使用`14-narrative-patterns.md`手工构建叙事 |
| `guizang-ppt-skill` | 分步呈现、藏露节奏、主动触发、讲师/演讲者控制 | 使用基础分步呈现规则；禁用不可控自动延迟 |
| `humanize-ppt-main` | 文案提纯、去模板话、自然表达、金句压缩 | 语言内容副主编手工提炼 |
| `PPT-Design-DNA-main` | 栅格、组件、页面族谱、PPT视觉系统 | 使用`04-design-standards.md`手工定义组件系统 |
| `tavily-search` / Tavily | 用户要求联网搜索、当前趋势、优秀案例、外部参考、竞品页面 | 必需时先提请用户同意安装/启用；用户拒绝则停止，不得宣称已联网搜索 |
| `tavily-extract` / `firecrawl` | 需要提取网页正文、结构、设计系统页面或案例网页 | 必需时先提请用户同意安装/启用；用户拒绝则停止，不得用标题摘要冒充结构提取 |
| `brave-search` | 通用网页、图片、新闻、资料交叉搜索 | 必需时先提请用户同意安装/启用；未使用时写明未做Brave交叉验证 |
| `context7` | 需要最新前端库、组件库、动画库文档 | 必需时先提请用户同意安装/启用；不可查时不得凭记忆写最新 API |
| `playwright-mcp` | HTML Pre真实浏览器截图、hover/focus、响应式、presentation chrome验证 | 必需时先提请用户同意安装/启用；不可用时不得声明截图验证完成 |

调用外部或vendor Skill前必须先运行或记录可用性检查。验证为不可用时，不得在交付说明中宣称已使用该Skill。上表所有“不可用时”动作都不是自动降级；必要Skill或联网/浏览器控件被用户拒绝安装、启用或授权时必须停止当前任务。

联网工具不可用时，必须写入《联网/工具阻断记录》和《缺失控件安装提请记录》。用户明确要求联网、最新文档或浏览器视觉验证时，未获得用户同意安装/启用或用户拒绝后，不得降级为本地参考库。任何最终回复、README、QA记录中不得把“本地参考库检索”写成“联网搜索”。

## 缺失Skill处理流程

当某个副主编提出需要调用某个Skill，但该Skill未安装且vendor缺失时，按以下顺序处理：

1. 工具链与上下文工程副主编确认该Skill是否真的必要；若只是可有可无，记录“可用性缺失，不调用”，不得阻塞生产。
2. 若必要，先使用`skill-installer`查询可安装来源；用户授权后安装到`$CODEX_HOME/skills`。
3. 若官方或指定来源无法安装，但Skill可以由本项目稳定复用，则按`skill-creator`规范内嵌到`presentation-system/skills/vendor/<skill-name>/SKILL.md`，并更新`skills.manifest.yaml`。
4. 若既不能安装也不能内嵌，先暂停并提交总编；用户若拒绝安装/授权或权限阻断，停止当前任务。只有用户明确改写任务边界为不再需要该Skill时，才可另起新边界任务，并把原因写入《Skill可用性与版本确认单》和《阻断记录》。
5. 安装或内嵌后必须重新运行`skills/verify-skills.sh`，验证为可用后才能在工单中调用。

## 缺失联网控件处理流程

当当前任务需要 Tavily、Brave、Firecrawl、Context7、Playwright MCP 或等价控件，但运行环境缺失时，按以下顺序处理：

1. 工具链与上下文工程副主编确认该控件是否为当前任务必需能力；非必需时记录“不调用”及理由。
2. 若必需，输出《缺失控件安装提请记录》，说明工具名称、用途、安装/启用方式、需要的API key或账号授权、可能费用、安装后产出的证据。
3. 用户同意后，才可调用安装、启用、插件/连接器请求或本地依赖安装流程。
4. 用户拒绝、未响应、未提供API key或权限阻断时，写入《联网/工具阻断记录》并停止当前任务。
5. 不得用模型记忆、本地参考库、旧截图或静态代码检查冒充联网搜索、最新文档或真实浏览器验证。

## 版本存储规则

- 每次生成新版本后，必须将完整版本文件包存入专门版本目录。
- 项目根目录只保留最新版本文件，作为默认入口。
- 历史版本建议放入`versions/<version>/`，并保留对应Skill确认单、QA记录和证据链。
- 冻结版本不可直接覆盖；如需修复，生成新的版本目录。

## Skill可用性确认步骤

1. 读取`skills/skills.manifest.yaml`。
2. 检查用户本地是否已安装目标Skill：优先查`$CODEX_HOME/skills/<name>/SKILL.md`，再查`~/.codex/skills/<name>/SKILL.md`，并应用“本地Skill别名映射”。
3. 检查`skills/vendor/<skill-name>/`是否存在本地副本。
4. 若manifest有真实安装命令且用户允许，执行安装；若仍是占位命令，不得假装已安装。
5. 执行verify命令或人工检查`SKILL.md`存在性；本地`SKILL.md`存在并完整可读时，记录为“可用/本地已安装”。
6. 记录版本、commit、来源、license、验证结论和降级审批状态。
7. 只有验证为可用时，才承诺对应能力。

## Skill可用性确认单

| 字段 | 结论 |
| :--- | :--- |
| Skill名称 |  |
| 项目用途 |  |
| 来源 | 本地已安装/vendor/manifest/单次读取/缺失 |
| 版本或commit |  |
| license状态 |  |
| 验证方式 |  |
| 验证结论 | 可用/部分可用/不可用 |
| 调用决策 | 调用/可用但不调用/缺失需安装/缺失需内嵌/阻断 |
| 决策人 | 总编/对应副主编/工具链副主编 |
| 阻断记录 | 阻断项、总编意见、用户结论、停止范围或用户改写后的新任务边界 |
