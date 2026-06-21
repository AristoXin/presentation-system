# 07-qa-checklist

读取时机：当任务进入验收、冻结、截图、回归测试、问题页复盘、同类页联动、交付确认或用户要求“检查/审查/QA”时读取。

## QA检查项

- 全页截图是否完整。
- 是否存在裂图、死链、占位素材、导出失败。
- 页面标题、正文、表格、页脚是否对齐并可读。
- 重点页是否存在明显头轻脚重、头重脚轻、左重右轻、右重左轻、底部堆积或主视觉漂移。
- 是否存在黑底黑字、深底深字、浅底浅字、图片上文字无遮罩等低对比硬伤。
- 文字排版是否专业：标题不压迫、正文不拥挤、行长可读、加粗比例克制。
- 相邻页正文色阶是否稳定。
- 线条颜色、边框厚度和分隔符是否统一且有语义；是否存在无解释的黑/红/绿混用。
- 表格组件是否统一。
- 表格表头是否明显强于正文；正文对齐是否按字段类型统一。
- 中英混排是否使用统一组件。
- 缩写/术语/模型组件是否把首字母、英文全称、中文含义和解释句正确绑定；不得只检查文字是否溢出。
- 类表格和判断清单是否统一对齐，完整短句是否被不合理拆行。
- 动效是否有动效脚本，是否经动效设计副主编、副总编和总编审核。
- 分步页面是否有首态/后续态矩阵，实际HTML初始态和每次触发是否与矩阵一致。
- 页间转场和同页分步是否具备设计过的运动语法，而不是统一淡入/上移或突兀硬切。
- 是否通过Style Frame审美确认。
- 是否附带《参考经验转译卡》，并说明当前设计如何结合用户资料，而不是照搬参考图。
- 若使用或评估StyleKit，是否完成审美组件转译：意图/记忆钩子、token层级、组件架构、状态/动效转译、quality_gate和swap/squint/signature/token测试。
- 若使用或评估PPT-DNA，是否完成三维设计身份转译：design_system、design_style、visual_effects是否进入页面族谱、UI方向、动效脚本和降级策略。
- 若使用或评估guizang，是否完成A/B风格适配、主题节奏、逐页layout/Sxx映射、图片槽位、模板改造差异和截图/校验记录。
- 若涉及design-dna/guizang深度集成，是否按`20-design-dna-guizang-integration.md`完成Presentation Design DNA档案、DNA来源追踪表、设计引擎桥接表、UI吸收表、动效吸收表和QA吸收检查。
- 若涉及stylekit/taste/frontend-slides/html-ppt/huashu-design等Skill栈，是否按`21-design-skill-stack-integration.md`完成Design Skill Stack决策表、StyleKit吸收、TasteSkill预检、演示引擎选择、Motion source map和Skill Stack吸收结论。
- 是否避免通用AI模板感、全页卡片堆叠、伪素材和无语义装饰。
- 关键案例、数据、品牌、二维码等页面是否使用真实素材或明确标注样例性质。
- HTML交互是否支持键盘、滚轮、触摸、目录、全屏、讲者提示。
- 默认打开时控制条是否隐藏或弱化。
- 鼠标靠近底部时控制条是否平滑出现。
- 鼠标离开后控制条是否自动隐藏。
- presenter模式和audience模式是否区分明确。
- export模式是否能输出无控件画面。
- PPTX是否真实可编辑。
- 大屏投影下字号、对比度和视觉层级是否可读。
- 真实视觉舒适度是否通过：黑/白/高饱和蓝等强反差色块是否有语义，连续翻页是否刺眼或割裂。

QA只验收带版本号的冻结稿，不验收临时稿。
未冻结稿若提交用户，只能作为样张或候选方向验收，不得作为正式交付验收。
未通过审美验收的页面不得进入QA终审。
未完成副主编一级复核、后续复审循环和总编二级复核的产物，不得进入QA冻结。自动脚本检查只能证明结构和交互状态，不能替代最终产品级UI核验。
生产前预审不等于实现后复核。QA发现只有预审、没有实现后多轮subagent复核时，必须直接判定“流程阻断”，不得继续做审美通过。

若自动验证脚本只检查页数、尺寸、裁切、文字溢出、键盘交互和控件隐藏，不得把结果命名为“QA通过”。它只能命名为“工程烟测通过”。QA冻结必须另有截图非空、可见文字、重点页人工审美复核和副主编签署。

自动验证命名红线：`validation.json`、Playwright、截图像素、键盘交互、页数、尺寸、溢出检查的通过状态只能写“工程烟测通过”。若审美QA、人工重点页复核、Style Frame签署、截图有效性任一失败，整体结论必须写“QA未冻结/审美阻断”，并触发`FAILED_VISUAL_FREEZE`。最终回复、README、版本说明不得出现“已完成、已交付、QA通过、最终版”等措辞。

用户点名问题优先规则：用户点名页码或问题类型后，QA必须把这些页作为最高优先级人工复核对象。若用户指出第1页、第9页排版失衡，QA必须检查光学平衡而不是只看是否溢出；若用户指出第5页、第9页分步缺失，QA必须核对首态/后续态矩阵而不是只看键盘能否翻页；若用户指出第15页丑，QA必须退回Page Spec或视觉母线，不能写“后续优化”。

用户上一版问题关闭规则：用户指出“上一版问题没解决”“一个没解决”“还是那些问题”时，QA必须立即建立《上一版问题关闭矩阵》。该矩阵必须逐项列出旧问题、根因、修复动作、同类页联动、截图/状态证据和关闭结论。没有该矩阵时，任何新版只能标为`FAILED_VISUAL_FREEZE`或`QA未冻结`，不得写“新版已生成”“候选稿”“可验收”。

经验回写规则：QA发现用户点名问题属于跨项目通用问题时，必须检查对应reference是否已更新。未更新`04-design-standards.md`、`11-aesthetic-anti-ai.md`、`17-motion-design-standards.md`、`15-visual-reference-library.md`或其他相关reference时，不得标为治理闭环。QA记录必须列出“经验回写路径”和“从此跨项目生效的规则”。

## 联网搜索与外部参考 QA

- 用户是否要求联网搜索或当前趋势。
- 是否读取 `23-online-research-toolchain.md`。
- 是否完成《Online Research Stack决策表》。
- 是否完成《外部参考搜索记录》。
- 是否至少列出 5 个候选参考。
- 是否至少列出 2 个弃用参考及理由。
- 是否完成《外部视觉参考转译卡》。
- 是否把外部参考转译为页面族谱、CSS token、组件规则、动效脚本或 QA 字段。
- 是否涉及前端库并完成 Context7/官方文档检索。
- 是否有 Playwright 或等价浏览器视觉验证记录。
- 联网工具不可用时，是否有《缺失控件安装提请记录》和《联网/工具阻断记录》。
- 用户拒绝安装、拒绝授权、未提供API key或权限阻断时，是否停止当前任务。
- 是否避免把本地参考库检索冒充为联网搜索。

用户要求联网搜索但缺少外部搜索记录时，不得进入 QA 冻结。用户要求当前/最新/主流趋势但没有外部近期验证或阻断记录时，不得声明已完成趋势调研。使用前端库但没有最新文档依据时，不得声明实现采用最佳实践。没有 Playwright 或等价浏览器截图时，不得声明已完成真实视觉验证。用户拒绝必要工具安装/授权后，不得用模型记忆、本地参考库或静态检查继续完成同一任务。

## UI美学QA

- 页面是否明显像AI模板？
- 页面是否明显只是在复制某张参考图？
- 是否存在无意义装饰？
- 是否每页结构过度重复？
- 是否信息层级清楚？
- 是否有足够留白？
- 是否颜色克制？
- 是否存在低对比文字或背景导致投屏不可读？
- 是否存在无语义线条颜色混乱？
- 是否存在黑、白、高饱和蓝等强反差色块无语义混用，造成观看不适？
- 是否存在相邻页明度硬切，导致演示翻页时刺眼或割裂？
- 是否存在重点页光学失衡，导致第一眼落点不是主判断？
- 是否存在为了显得丰富而使用的花样线条颜色？
- 表格表头、正文、数字、文本列是否形成稳定对齐规则？
- STAR、SWOT、OKR等缩写模型是否采用记忆组件，而不是把字母、英文、中文随意拼接？
- 是否标题、正文、注释、标签形成稳定字阶，而不是全部大号加粗？
- 是否关键页有真实视觉锚点，而不是大面积“待替换”占位框？
- 是否StyleKit规则已经落地为当前项目的视觉母线、token语义和组件状态，而不是只记录slug或提示词？
- 是否PPT-DNA规则已经落地为可见的色彩、字体、间距、构图、组件和效果降级，而不是只输出JSON？
- 是否guizang规则已经落地为页面级版式选择、主题节奏和动效状态，而不是只套瑞士风/杂志风名义？
- 是否控件破坏画面？
- 是否截图时能得到干净画面？
- 是否投屏时底部按钮不会抢注意力？
- 底部操作栏是否采用中文动作词 + 图标组合，并且`title`/`aria-label`与动作一致？
- 是否打印/PDF导出时隐藏所有交互控件？

## HTML审美QA

针对HTML演示冻结稿，QA不得只跑静态检查。必须完成：

### 截图审查硬门禁

QA截图审查必须包含缩略图总览和重点页放大复核两层。

| 审查层 | 要求 | 硬失败 |
| :--- | :--- | :--- |
| 缩略图总览 | 全页截图按顺序拼成contact sheet，检查跨页节奏、色彩跳变、重复版式 | 连续3页以上同结构；黑/白/蓝等色彩角色突然变化；全稿像同一模板换标题 |
| 重点页放大 | 封面、核心模型、案例/系统、数据/表格、收束页逐张打开 | 主判断不清、标题压迫、文字拥挤、低对比、真实视觉锚点缺失 |
| 光学平衡复核 | 点名页和关键页逐张检查上下/左右重量、主视觉落点和阅读路径 | 头轻脚重、左重右轻、底部堆积、主视觉漂移 |
| 分步状态复核 | 多步骤页逐步触发并记录初始态、每步态、完成态 | 第1点提前显示、步骤合并、触发数不一致、完成态默认外露 |
| 动效美感复核 | 肉眼检查页间与同页切换的节奏、缓动、方向、停顿 | 机械硬切、统一fade/rise、linear感、无讲述目的 |
| 调色板核验 | 对照《调色板语义表》检查每页颜色角色 | 颜色无语义、accent过多、蓝色/黑色/白色角色漂移 |
| 参考落地核验 | 对照《参考证据门禁》检查采用REF是否真的落地 | 只有参考名称，没有页面/CSS/截图证据 |
| Skill落地核验 | 对照Skill规则提取表检查设计Skill是否真的影响产物 | 只读Skill，产物看不出规则执行 |

没有contact sheet、重点页截图、调色板核验和人工审美结论时，QA不得冻结。

1. 必须逐页截图并生成contact sheet；浏览器肉眼复核只能补充，不能替代截图证据。至少重点记录封面、核心模型页、案例页、系统/工具页、收束页。
2. 统计连续重复版式。连续3页以上使用同一“标题 + 卡片/面板/网格”结构，标为审美风险。
3. 检查文字密度。单页正文、标签、注释过多，或大号粗体面积过大，标为Typography风险。
4. 检查占位素材。正式冻结稿中，Logo、系统截图、案例截图、二维码、关键品牌素材仍“待替换”的页面，不得审美通过。
5. 检查导出干净度。audience和export模式下截图不得出现抢眼控制条、编辑按钮、讲者提示或帮助面板。
6. 检查截图方法。必须等待reveal动画完成，或使用export模式禁用动效；半透明入场态、空白页或仅改CSS类得到的截图不得作为通过证据。
7. 检查实际视觉一致性：线条颜色、边框厚度、表格基线、卡片背景、标题字阶、页脚位置、强调色语义必须逐页记录。
8. 检查对比度硬伤：黑底黑字、深底深字、浅底浅字、图片上文字无遮罩、表格文字与底色相近，均直接退回。
9. 检查表格硬伤：表头不显眼、同列对齐混乱、数字和文本对齐规则混用、普通分隔线使用红/绿风险色，均直接退回。
10. 检查术语组件硬伤：模型、法则、术语缩写不得只出现字母或标题，必须显示含义或解释入口；字母和英文全称不得被中文解释拆开。
11. 检查动效硬伤：没有动效脚本、未经动效部审核、export模式截到中间态、动效造成阅读延迟或遮挡，均直接退回。
11a. 检查分步硬伤：所有多步骤页面必须按首态/后续态矩阵逐步触发。第1项默认显示、后续内容提前出现、多个语义阶段无理由同显、触发次数与脚本不一致，均直接退回。
11b. 检查动效美感硬伤：页间和同页切换若只有统一淡入、上移、突兀切换、机械匀速或无空间连续性，标记为Motion退回，不得以“动画可运行”通过。
12. 检查元素关系：脚注、标签、面板、说明文字、二维码/入口、按钮和图示不得重叠或互相遮挡。
13. 检查截图非空：每页导出图必须包含足够非背景像素和可见文字；连续多页截图MD5一致、近乎空白、只剩背景纹理或截到动画前态，直接退回。
14. 检查重点页真实内容：封面、核心模型页、案例页、工作台页、AI/系统页、收束页必须逐张打开肉眼复核，不能只相信脚本。
15. 检查阅读模式：讲授页3秒内能抓住主判断，练习页10秒内知道填哪里，案例页能看出“发生了什么、证据在哪、怎么判断”；不满足即退回Page Spec。
16. 检查视觉舒适度：黑/白/强蓝等大面积色块必须有统一视觉母线和语义；无语义混用、刺眼硬切、正文压迫、窄栏中文拥挤，均退回审美和Page Spec。

如果Playwright、浏览器或截图工具不可用，不得把“截图QA/审美QA”标为通过；只能记录为“未完成/阻断”，并给出需要人工浏览器复核的页面清单。

## HTML演示QA

- 默认打开时控制条是否隐藏或弱化？
- 鼠标靠近底部时控制条是否平滑出现？
- 鼠标离开后控制条是否自动隐藏？
- 底部操作栏按钮是否为“上一页/下一页/目录/讲者/帮助”等中文动作词 + 图标组合？若只显示`‹`、`›`、`M`、`?`等符号，交互QA直接退回。
- 键盘翻页是否不受隐藏控制条影响？
- 触控设备是否仍可操作？
- presenter模式和audience模式是否区分明确？
- export模式是否能输出无控件画面？

## 判断标准

控件不破坏画面：audience模式首屏截图中控制条不可抢注意力；export/print截图中不得出现任何交互chrome；投屏时底部按钮不遮挡主体内容、不像后台管理按钮。

视觉不再AI化：页面有明确主视觉、主结论和阅读路径；组件系统统一；不同页面结构服务不同内容关系；没有通用渐变、玻璃拟态、随机装饰线、重复卡片矩阵等模板库痕迹；关键页有真实视觉锚点或明确标为未冻结样张；文字层级稳定，不靠普遍放大加粗制造“设计感”。

参考不被照搬：页面能说明借鉴了哪些参考经验，也能说明哪些参考图表层被主动舍弃；主品牌色、用户资料、真实素材和业务证据优先于参考图配色、装饰、文案和行业语汇。

## QA执行步骤

0. QA第0步流程阻断检查：在确认版本、截图、运行Playwright、导出、生成`validation.json`或写工程烟测结论之前，先检查《用户最新要求锁定表》和Subagent Evidence Lock。必须有真实subagent id、真实工具/线程证据、同一副主编实现后复审记录。缺少真实subagent证据时，立即输出`PROCESS_BLOCKED_NO_SUBAGENT`或对应流程阻断记录；不得继续截图、像素、键盘、控件、导出、validation或工程烟测。
1. 确认版本号和冻结稿路径。
2. 确认生产前卡片齐全：资料盘点、交付定义、内容差距、参考经验转译、UI方向、Style Frame确认。
3. 确认Agent编制表、副主编一级复核记录、副主编复审循环记录、总编二级复核记录已完成。
4. 逐页截图或导出全页图。
5. 检查截图有效性：非空白、非过渡帧、可见文字、MD5/像素差异合理；失败时不得继续宣称QA通过。
6. 检查硬伤：裂图、死链、遮挡、重叠、占位、错别字、导出失败。
7. 检查审美硬伤：模板感、重复卡片、文字压迫、占位承重、无意义装饰。
8. 检查视觉硬红线：低对比文字、无语义多色线条、表头不显眼、表格对齐混乱。
9. 检查跨页一致：正文色、表格组件、英文组件、线条颜色、页脚和章节节奏。
10. 检查内容完整：STAR、模型维度、流程阶段、练习要求是否有必要解释。
11. 检查交互或PPTX可编辑性。
12. 对HTML演示检查audience/presenter/export模式和截图状态。
13. 对问题建立问题ID，写入`10-version-evidence.md`规定字段。
14. 修复后回归，并同步检查同类页。

无subagent阻断规则：工程烟测不是QA的前置补救。无真实subagent证据或无用户明确降级批准时，QA不得生成`validation.json`，不得写“工程烟测通过”，不得创建新的截图证据。只能生成《流程阻断记录》，列明缺失的subagent、缺失轮次、是否有用户降级批准和下一步恢复条件。

## 问题页复盘模板

| 字段 | 内容 |
| :--- | :--- |
| 问题ID |  |
| 页面 |  |
| 问题类型 | 内容/版式/交互/审美/素材/导出 |
| 修前证据 |  |
| 根因 |  |
| Page Spec重写 |  |
| 修复动作 |  |
| 同类页联动 |  |
| 修后证据 |  |
| 回归结论 |  |

## 上一版问题关闭矩阵模板

| 字段 | 内容 |
| :--- | :--- |
| 上一版路径 |  |
| 新版路径 |  |
| 用户原话 |  |
| 问题ID列表 |  |
| 逐项关闭表 | 问题ID、页码、旧问题、根因、修复动作、修后证据、同类页联动、关闭/未关闭 |
| 未关闭项 | 必须写`FAILED_VISUAL_FREEZE`或阻断，不能写候选稿 |
| 经验回写路径 | 修改了哪些`presentation-system/references/*.md` |
| QA结论 | 全部关闭/部分关闭/全部未关闭/流程阻断 |

## 审美QA记录模板

| 字段 | 内容 |
| :--- | :--- |
| 版本与文件 |  |
| 截图证据 | 全页截图包/重点页截图/人工浏览器复核 |
| 截图有效性 | 非空白、非过渡帧、可见文字、连续页像素差异 |
| 重复版式风险 | 页码与组件族 |
| 文字排版风险 | 页码、问题、处理建议 |
| 光学平衡风险 | 上下/左右重量失衡、主视觉漂移、阅读路径错误的页码与处理建议 |
| 光学平衡证据 | 标注截图或三分区记录路径；上/下重量、左/右重量、第一眼落点、主视觉路径 |
| 对比度硬伤 | 黑底黑字/深底深字/浅底浅字/图片上文字不可读的页码与处理建议 |
| 线条系统硬伤 | 无语义多色线条、边框厚度混乱、黑/红/绿混用的页码与处理建议 |
| 视觉舒适度硬伤 | 黑/白/高饱和蓝硬切、强反差色块无语义混用、页面压迫或割裂的页码与处理建议 |
| 表格组件硬伤 | 表头不显眼、正文对齐混乱、字段类型对齐不一致的页码与处理建议 |
| 术语/缩写组件硬伤 | STAR/SWOT/OKR等模型的字母、英文、中文和解释关系是否错误 |
| Style Frame协同输入 | 语言内容、品牌审美、版式/UI、动效设计、交互工程、QA是否均有生成前输入和冲突解决记录 |
| 动效设计硬伤 | 是否有动效脚本、审核记录、export稳定态和讲述节奏说明 |
| 分步状态硬伤 | 首态/后续态矩阵、初始态、逐步触发、完成态是否一致 |
| 真实素材风险 | 页码、缺失素材、是否可冻结 |
| 参考经验转译 | 是否有参考来源、可借鉴经验、不照搬项、用户资料改写、品牌色取舍 |
| StyleKit设计库证据 | 是否记录`stylekit-skill`调用/不调用/降级结论；若调用，是否有查询词、候选slug、采用/弃用理由、`quality_gate`状态和演示语境转译 |
| StyleKit审美吸收证据 | 是否有purpose/audience/tone/memorable hook转译；是否建立Brand→Semantic→Component→State token层级；是否定义Base→Variant→Size→State→Override组件边界；是否完成state/interaction到演示状态的转译 |
| StyleKit反泛化测试 | swap、squint、signature、token四项测试结论；若只记录slug、prompt或style_choice，必须写“已读取未吸收”并退回审美/UI链路 |
| PPT-DNA吸收证据 | 是否记录`PPT-Design-DNA-main`/`design-dna`调用或不调用结论；design_system/design_style/visual_effects是否转成当前deck的token、页面族谱、组件规范、动效脚本和效果降级 |
| guizang吸收证据 | 是否记录`guizang-ppt-skill`调用或不调用结论；是否有A/B适配、主题节奏、逐页layout/Sxx映射、图片槽位、模板改造差异、类名/版式校验和截图核验 |
| 深度集成合同证据 | 是否有`20-design-dna-guizang-integration.md`要求的`presentationDesignDnaPath`、`dnaSourceTracePath`、`engineBridgePath`、`guizangPageMapPath`、`uiAbsorptionPath`、`motionAbsorptionPath`、`skillAbsorptionQaPath`和`absorptionDecision` |
| Design Skill Stack证据 | 是否有`21-design-skill-stack-integration.md`要求的`designSkillStackDecisionPath`、`stylekitAbsorptionPath`、`tastePreflightPath`、`engineSelectionPath`、`motionSourceMapPath`和`skillStackAbsorptionDecision` |
| Online Research Stack证据 | 是否有`23-online-research-toolchain.md`要求的`onlineResearchStackDecisionPath`、`externalSearchRecordPath`、`externalReferenceTranslationPath`、`latestDocsRetrievalPath`、`playwrightVisualValidationPath`、`missingToolInstallRequestPath`、`onlineToolBlockerPath`和`onlineResearchDecision` |
| 设计引擎吸收结论 | 若只有DNA JSON、风格标签、Sxx编号、瑞士风/杂志风名称或模板路径，必须写“已提取未吸收/已选模板未吸收”并退回品牌审美和版式/UI链路 |
| 控件干净度 | audience/presenter/export结论 |
| 一级/复审/二级复核 | 副主编一级复核、副主编复审循环、总编二级复核是否完成 |
| 实现后复核 | 真实产物生成后，哪些副主编基于文件/截图/validation做了复核，哪些退回项已由同一副主编复审 |
| 内容完整性风险 | 模型、法则、缩写、训练动作是否缺解释 |
| 文案QA | 页码、标题是否承担判断、证据是否足够、讲者动作、带走句、是否模板化压缩、结论 |
| 元素重叠风险 | 页码、截图、页面区域、修复结论 |
| 审美结论 | 通过/退回Style Frame/退回Page Spec/阻断 |

## 自动验证最低字段

HTML验证脚本若生成`validation.json`，至少应包含以下字段；缺失时只能算工程烟测，不能算QA：

| 字段 | 含义 |
| :--- | :--- |
| `status` | 工程烟测状态 |
| `versionId` | 版本号或版本目录 |
| `artifactPath` | 被验证主文件路径 |
| `artifactHash` | 主文件hash |
| `generatedAt` | 产物生成时间 |
| `browserOrToolVersion` | 浏览器、渲染器或验证工具版本 |
| `viewport` | 截图视口尺寸 |
| `mode` | audience/presenter/export/print等模式 |
| `expectedSlideCount` | 预期页数 |
| `actualSlideCount` | 实际页数 |
| `captureCommand` | 截图命令或脚本路径 |
| `nonBlankScreenshots` | 每页截图非空白检查 |
| `visibleTextBySlide` | 每页可见文字数量或抽样文本 |
| `screenshotSimilarity` | 连续截图相似度或哈希差异，识别多页空白/同图 |
| `screenshots` | 每页截图结构化记录，含slideId、path、尺寸、文件大小、前景像素比例、OCR/文本样本、perceptualHash、captureState |
| `animationState` | animationDisabled、waitStrategy、waitMs、exportModeConfirmed、capturedAfterRevealComplete |
| `styleFrameEvidence` | directionId、coveredPageTypes、screenshotPaths、departmentInputsByDirection、conflictItems、signoffsByDepartment |
| `agentEvidence` | agentInvocationId、createdAt、closedAt、inputArtifactRefs、outputArtifactRefs、sameAgentRecheck |
| `postImplementationReview` | reviewerAgentId、domain、artifactRefs、screenshotRefs、decision、blockers、sameAgentRecheck、reviewRound |
| `visualComfortGate` | brightnessRhythm、colorRoleMap、forbiddenColorMixes、readingComfortNotes、decision |
| `styleKitAbsorption` | stylekitDecision、query、candidateSlugs、adoptedRules、rejectedRules、intentHook、tokenHierarchy、componentArchitecture、stateTranslation、qualityGate、swapSquintSignatureTokenTests、decision |
| `designDnaAbsorption` | decision、sourceReferences、designSystemTokens、designStyleRules、visualEffectsRules、pageTaxonomyMapping、componentMapping、motionAndFallbackMapping、qaDecision |
| `guizangAbsorption` | decision、styleAorB、fitRationale、themeRhythm、pageToLayoutMapping、imageSlots、templateAdaptationDiff、validationCommandOrEquivalent、screenshotReview、qaDecision |
| `onlineResearchAbsorption` | onlineResearchStackDecision、searchTools、candidateCount、adoptedReferences、rejectedReferences、externalReferenceTranslation、latestDocsRetrieval、playwrightVisualValidation、missingToolInstallRequest、onlineToolBlocker、decision |
| `focusPageManualQa` | 重点页人工复核记录，至少封面、模型、案例、工作台、AI/系统、收束 |
| `manualQa` | reviewerAgentId、reviewTimestamp、focusPagesReviewed、blockers、decision、signoffEvidencePath |
| `aestheticGate` | 通过/退回Style Frame/退回Page Spec/阻断，不得由脚本自签通过 |
| `qaClaimPolicy` | 必须声明：自动验证不得自称QA通过，只能声明工程烟测状态 |
| `visualFreezeStatus` | frozen / not_frozen / failed_visual_freeze |
| `resumeProductionApproval` | userApproved、approvalTimestamp、approvalText；未获批准时为空且不得继续生产 |
