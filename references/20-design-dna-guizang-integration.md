---
id: R20
title: Design DNA Guizang Integration
applies_to:
  - design_dna
  - guizang
  - visual_production
  - style_frame
gates:
  - G1
  - G4
  - G7
  - G8
required_outputs:
  - PresentationDesignDNA
  - EngineBridgeTable
---

# 20-design-dna-guizang-integration

读取时机：当任务涉及完整视觉生产、Style Frame、HTML/PPT/Slides、审美/UI/动效退回、用户质疑“没有深度集成design-dna/guizang/审美/UI/动效”等情况时读取。本文件是`design-dna`、`guizang-ppt-skill`、UI、审美和动效的统一落地合同；其他reference可以追加要求，不能降低本文件门槛。

## 核心原则

`design-dna`负责定义“这份内容应该长成什么设计身份”，`guizang-ppt-skill`负责在演示版式和横向翻页语法中承接该身份。二者都不是模板捷径。

任何视觉生产必须先完成当前内容关系、页面族谱和Presentation Design DNA，再选择guizang A/B、html-ppt、frontend-slides或客户母版。先选瑞士风、杂志风、IKB、Sxx、模板路径或主题色，再倒推内容，直接判定为硬套模板。

## 四段式强制链路

| 阶段 | 必填产物 | 责任部门 | 阻断条件 |
| :--- | :--- | :--- | :--- |
| 1. 内容源头 | 内容深挖表、页面族谱、内容到UI/动效转译表 | 语言内容、需求/交付 | 页面角色来自模板，而不是来自用户资料 |
| 2. Presentation Design DNA | 三维DNA档案：design_system、design_style、visual_effects | 品牌审美、版式/UI、动效设计 | 只有形容词、JSON或参考名，没有页面级规则 |
| 3. 设计引擎桥接 | guizang/html-ppt/frontend-slides/客户母版适配与弃用表 | 品牌审美、版式/UI、工具链 | 引擎选择早于DNA；没有弃用理由；没有逐页映射 |
| 4. 实现与QA吸收 | 截图、源码、校验、人工审美QA、Skill落地核验 | 交互工程、QA、原责任副主编 | 产物看不出DNA和引擎规则，或只通过工程烟测 |

四段缺任一段，不得进入全稿HTML/PPT/PDF生产；已经误生成的产物只能标为`FAILED_VISUAL_FREEZE`或治理证据。

## Presentation Design DNA档案

每个正式视觉项目必须产出本档案。它可以是表格或JSON，但必须同时包含来源、页面映射和QA字段。仅输出design-dna原始JSON不算完成。

| 维度 | 必填字段 | 来源要求 | 必须落到哪里 |
| :--- | :--- | :--- | :--- |
| design_system | color roles、type scale、spacing rhythm、grid、shape、line/elevation、component families、motion tokens | 用户品牌、素材、内容密度、参考库、观看距离 | CSS变量、PPT母版、组件规范、调色板语义表、Page Spec |
| design_style | mood、genre、personality、visual language、composition strategy、imagery、brand voice | 交付场景、受众、证据强度、品牌气质、参考经验 | 视觉母线、页面族谱、关键页重心、留白策略、标题语气 |
| visual_effects | effect intensity、motion grammar、WebGL/Canvas/SVG/CSS边界、fallback、reduced motion、export stable state | 讲述动作、设备性能、投屏、导出、可读性 | 动效脚本、首态/后续态矩阵、低功耗策略、截图等待策略 |

### DNA来源追踪表

| DNA字段 | 取值 | 来源 | 为什么适合当前项目 | 禁用边界 | QA如何看见 |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 用户资料/品牌/参考库/趋势/交付约束 |  |  | 截图页码、CSS变量、组件名、动效状态 |

如果某个DNA字段无法追溯来源，必须删除或降级，不能用“高级感、科技感、瑞士感、杂志感”补理由。

## guizang桥接合同

使用`guizang-ppt-skill`时，必须先完整读取其`SKILL.md`，再根据选择读取对应主题、布局、校验和组件reference。读取不等于吸收；吸收必须填以下表。

### guizang适配与弃用表

| 项目 | 风格A 电子杂志 | 风格B 瑞士国际主义 | 结论 |
| :--- | :--- | :--- | :--- |
| 受众与场景 | 是否适合 | 是否适合 | 采用A/采用B/两者都弃用 |
| 内容密度 | 是否能承载 | 是否能承载 |  |
| 素材类型 | 图片/证据/截图是否匹配 | 数据/系统/结构是否匹配 |  |
| 品牌气质 | 是否冲突 | 是否冲突 |  |
| 动效语气 | 是否支持讲述节奏 | 是否支持讲述节奏 |  |
| 弃用理由 | 若不用A，写原因 | 若不用B，写原因 |  |

### guizang逐页映射表

| 页码 | 页面角色 | 内容关系 | DNA规则 | guizang layout/Sxx | 选用理由 | 图片槽位 | 动效意图 | 改造差异 | 禁用项 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 封面/问题/框架/数据/案例/系统/练习/收束 |  | design_system/design_style/visual_effects字段 | A-layout 或 S01-S22 |  | 比例/裁切/安全区 |  | 保留/改写/新增/删除 |  |

瑞士风必须保留`data-layout="Sxx"`、单一accent、中文标题分档、字号/字重阶梯、直角纯色、底部安全区和图片槽位规则。电子杂志风必须保留图片/证据第一、衬线标题与无衬线正文分工、hero与正文页节奏、克制WebGL背景和主题色一致性。

## UI与动效联合落地

UI不能只负责“排整齐”，动效不能只负责“加动画”。二者必须共同承接DNA。

### UI吸收表

| 页面/页组 | 视觉重心 | 网格/版心 | 字阶 | 组件族 | 色彩语义 | 光学平衡策略 | 禁止长成 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 第一眼落点 |  |  | 卡片/表格/标注/截图/图表 |  | 上下/左右/主次重量 |  |

### 动效吸收表

| 页面/页组 | 讲述动作 | 页间语法 | 同页语法 | 首态/后续态 | easing/duration/stagger | 静止/低功耗/export | 禁用动效 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 提问/等待/揭示/对照/标注/收束 | 进入下一层/硬切/滑移/显影等 | 数字、bar、SVG、证据、节点 |  |  |  |  |

全稿统一`opacity + translateY`、统一fade/rise、默认transition、linear、突兀硬切或没有页面角色差异，均判定为动效吸收失败。

## Style Frame前置证据

正式视觉生产或审美退回后的Style Frame探索，必须在截图前完成以下证据：

| 证据 | 最低要求 |
| :--- | :--- |
| 用户最新要求锁定表 | 忠实转写用户原话，尤其是审美/UI/动效/Skill集成质疑 |
| 历史失败吸收 | 当前失败如何改变DNA、页面族谱、UI和动效 |
| Presentation Design DNA档案 | 三维字段、来源追踪、页面映射 |
| guizang/设计引擎桥接 | 采用/弃用理由、逐页映射、改造差异 |
| UI吸收表 | 光学平衡、组件语法、调色板语义 |
| 动效吸收表 | 运动语法、首态矩阵、export稳定态 |
| QA前置风险 | 哪些截图和人工复核能证明吸收成功 |

截图早于这些证据完成时，不得追认为Style Frame。

## QA吸收检查

QA必须逐项检查“读过”和“落地”之间的差距。

| 检查项 | 通过条件 | 失败结论 |
| :--- | :--- | :--- |
| design-dna | 截图、源码或PPT母版可见token、构图、组件和效果降级 | 已提取未吸收 |
| guizang | 逐页layout/Sxx、主题节奏、图片槽位、动效recipe和改造差异可追溯 | 已选模板未吸收 |
| UI | 重点页有清楚主视觉、阅读路径、光学平衡和组件语义 | 退回Page Spec/视觉母线 |
| 动效 | 页面角色有不同节奏，分步状态与矩阵一致，导出稳定 | Motion退回 |
| 跨页节奏 | contact sheet显示页面族谱变化，不是同一模板换标题 | Style Frame退回 |

自动脚本只能辅助检查类名、`data-layout`、截图非空和交互状态。脚本不能签署DNA吸收、guizang吸收、审美通过或QA冻结。

## 硬失败信号

出现以下任一情况，必须停止生产并退回：

1. 记录中写了design-dna/guizang，但没有DNA来源追踪表和逐页映射。
2. 先宣布风格A/B、瑞士风、杂志风、IKB或Sxx，再补内容转译。
3. 视觉截图仍是卡片矩阵、浅底面板、标签堆叠或同一模板换标题。
4. 动效只有统一淡入、上移、硬切或没有讲述动作。
5. 关键页排版失衡、没有主视觉、标题压迫正文或底部堆积。
6. guizang瑞士风没有`data-layout`/Sxx登记，或自造未登记版式。
7. design-dna visual_effects没有fallback、reduced-motion和export稳定态。
8. QA只记录“工程烟测通过”，没有人工审美、DNA吸收和guizang吸收结论。

## 交付记录字段

所有团队协作记录、Style Frame记录、QA记录或`validation.json`等价证据，应包含以下字段或对应表格路径：

| 字段 | 含义 |
| :--- | :--- |
| `presentationDesignDnaPath` | Presentation Design DNA档案路径 |
| `dnaSourceTracePath` | DNA来源追踪表 |
| `engineBridgePath` | guizang/html-ppt/frontend-slides/客户母版桥接表 |
| `guizangPageMapPath` | guizang逐页映射表；不使用guizang时写不适用及原因 |
| `uiAbsorptionPath` | UI吸收表 |
| `motionAbsorptionPath` | 动效吸收表 |
| `skillAbsorptionQaPath` | QA吸收检查记录 |
| `absorptionDecision` | absorbed / extracted_not_absorbed / template_selected_not_absorbed / blocked |

缺少这些字段时，不得在README、QA记录或最终回复中写“已深度集成design-dna/guizang”。
