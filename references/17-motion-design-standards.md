---
id: R17
title: Motion Design Standards
applies_to:
  - html
  - motion
  - animation
  - reveal_steps
gates:
  - G1
  - G4
  - G7
  - G8
required_outputs:
  - MotionScript
  - StepStateMatrix
  - OfficialMotionTranslation
  - MotionOpportunityMap
  - MotionStateMatrix
  - StaticPageJustification
---

# 17-motion-design-standards

读取时机：当任务涉及HTML演示、分步呈现、转场、滚动/翻页动效、动画Demo、视频导出、用户提到“动效/动画/节奏/更有现场感/不要静态”时读取。本文件定义动效设计部职责；动效不是交互工程的附属，也不是最后加一点动画。若涉及design-dna、PPT-DNA、guizang或用户质疑审美/UI/动效没有深度集成，同时读取`20-design-dna-guizang-integration.md`。若用户指出动效单一、生硬、像PPT淡入，或涉及stylekit/taste/frontend-slides/html-ppt/huashu-design等Skill集成，同时读取`21-design-skill-stack-integration.md`。

## 动效设计部职责

动效设计副主编必须在正式HTML创建前输出动效脚本，并与语言内容、品牌审美、版式/UI、交互工程并行初审。动效设计部负责判断：

- 当前产物是一个HTML交互文件，而不是PPT的静态翻页模拟；动效必须被设计成DOM状态、用户输入、可访问性、浏览器渲染和导出模式共同约束下的交互系统。
- 这一页为什么需要动。
- 动效帮助观众理解什么：注意力、层级、推理、状态变化、章节转场或现场互动。
- 哪些页面必须静止，避免干扰讲师和阅读。
- 哪些页面需要分步揭示，以匹配讲述节奏。
- 动效是否影响导出截图、PDF、投屏或讲师控场。

没有动效脚本，不得在HTML里随意添加动画。动效脚本未通过副总编和总编审核，不得进入正式HTML创建。

动效必须被设计，而不是被“加上”。正式HTML演示至少要定义一套页间转场语法和一套同页分步语法，并说明它们如何服务讲述节奏。只使用统一淡入、统一上移、默认CSS transition、突兀硬切、机械匀速或每页相同的reveal，不得标为动效通过。

HTML动效不得被理解为“点一下出现下一个图标、表格或文字”。每个可触发动作都必须回答：触发前页面处于什么状态、触发后哪些DOM状态改变、焦点/键盘/滚轮/触摸如何处理、动画期间是否可取消或节流、完成态如何稳定、回退/重播/目录跳转如何恢复、export/print如何落稳。缺少这些交互状态定义时，动效脚本无效，交互工程不得实现。

若项目使用design-dna或guizang，动效脚本必须承接`20-design-dna-guizang-integration.md`中的`visual_effects`和guizang动效recipe。必须额外填写《动效吸收表》，说明每页的讲述动作、页间语法、同页语法、首态/后续态、easing/duration/stagger、低功耗和export稳定策略。没有该表时，不得宣称动效已深度集成DNA或guizang。

若用户指出动效单一，必须按`21-design-skill-stack-integration.md`完成动效单一专项门禁：Motion grammar map、Motion source map、Role variation、Reduced/export stable和Anti-single-motion check。`frontend-slides`的高冲击load/stagger、`html-ppt`的animation/FX、`guizang`的recipe、`huashu-design`的连续运动叙事只能作为来源，必须转译为当前页面角色；不能机械堆动画。

## 官方动效参考基线

动效设计部必须定期参考 Apple Human Interface Guidelines、Google Material Design 和 Microsoft Fluent Design 的官方 motion/design 文档，并把学习结果转译为当前项目可执行的 motion grammar。官方资料不是模板库，不能直接照搬官网页面效果；它们用于建立判断标准。

官方参考入口：

- Apple Human Interface Guidelines / Motion: `https://developer.apple.com/design/human-interface-guidelines/motion`
- Google Material Design 3 / Motion: `https://m3.material.io/styles/motion/overview`
- Microsoft Fluent 2 / Motion: `https://fluent2.microsoft.design/motion`

跨官方体系沉淀出的动效基线：

1. 目的先行：每个运动必须解释信息关系、导航方向、状态变化、反馈或注意力，不为装饰而动。
2. 连续性：页间和同页运动必须帮助观众理解对象从哪里来、去哪里、和前后内容是什么关系。
3. 响应性：用户触发后的反馈要及时、清楚、轻量；不能让观众等待无意义的展示动画。
4. 自然节奏：避免 linear、默认 transition、突然硬切和统一机械淡入；必须为页面角色定义 duration、easing、stagger 和 settle time。
5. 层级一致：动效强度、方向和速度应与内容层级、品牌气质、页面角色一致；关键判断比装饰元素拥有更清晰的运动权重。
6. 可访问与减动：必须支持 `prefers-reduced-motion` 或等价减动方案；减动后内容完整、顺序清楚、状态可读。
7. 稳定导出：export/print/screenshot 模式必须落在可读稳定态，不出现半透明、中间态、空槽位或动画遮挡。
8. 系统一致：同一份演示应有统一运动语法，但不同页面角色必须有节奏差异，避免“全稿一套 fade/rise”。

每次触发本节时，必须在动效脚本中补充《官方参考转译记录》：

```text
官方参考转译记录
- 参考来源：Apple / Google Material / Microsoft Fluent / 其他官方文档
- 检索日期：
- 采用原则：
- 弃用原则：
- 当前项目改写方式：
- 影响页面/页组：
- 对应 duration/easing/stagger/settle time：
- 减动与导出稳定策略：
- QA 可见证据：
```

## 克制还是多元

动效不默认克制，也不默认多元。按页面角色设定动效强度：

| 页面角色 | 默认动效 | 强度 |
| :--- | :--- | :--- |
| 封面/开场 | 标题、主视觉、关键承诺短促入场 | 中-强 |
| 章节页 | 清晰转场，提示进入新阶段 | 中 |
| 概念页 | 核心概念先出，解释后出 | 低-中 |
| 流程页 | 按步骤逐项出现，强调路径 | 中 |
| 案例页 | 证据先出现，判断后出现，模拟推理 | 中 |
| 表格/清单页 | 行或列轻微进入，不做花哨运动 | 低 |
| 互动/练习页 | 问题先出现，规则后出现，答案可延迟 | 中 |
| AI/系统页 | 状态、模块、边界分层出现 | 中 |
| 收束页 | 行动项递进，最终结论稳定停留 | 低-中 |

## Motion Opportunity First

动效设计不是实现阶段的 CSS 增强。

正式 HTML/PPT 动效生产前，必须先完成 Motion Opportunity Map。

每页必须被分类为：

- motion-required
- motion-optional
- intentionally-static

若页面属于 motion-required，但最终没有动效或状态变化，必须说明阻断原因或退回设计。

若页面属于 intentionally-static，必须写明静止理由。

禁止把“所有元素淡入/上移”作为全稿动效方案。

## 动效脚本强制三要素矩阵

动效脚本不得只写 `fadeIn`、`slideUp`、`淡入`、`上移`、`更丝滑` 等模糊词。每个运动必须落到 transform、easing、duration、trigger 和稳定态。

| 页面角色 | 推荐 transform | 推荐 easing | 推荐 duration | 禁止或慎用 |
| :--- | :--- | :--- | :--- | :--- |
| 封面 / 章节页 | `scale(0.95) -> scale(1)` + `opacity`，或主视觉轻微视差 | `cubic-bezier(0.34, 1.56, 0.64, 1)` | 800ms - 1000ms | 大幅 `translateY`、长延迟 |
| 数据 / 指标页 | `clip-path: inset(0 100% 0 0) -> inset(0 0 0 0)`，数字用计数或遮罩显影 | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | 600ms - 800ms | 数字只靠 `opacity` 淡入 |
| 流程 / 步骤页 | `translateX(40px) -> translateX(0)` 或路径节点逐步激活 | `cubic-bezier(0.22, 1, 0.36, 1)` | 350ms - 500ms | 无意义缩放、一次全显 |
| 案例 / 证据页 | 证据先 `clip-path` 或 mask 显影，判断后用轻量位移进入 | `cubic-bezier(0.2, 0.8, 0.2, 1)` | 500ms - 750ms | 判断先于证据出现 |
| 结论 / 静止页 | 无动效或仅切页完成态 | N/A | N/A | 任何持续循环动画 |

若页面角色不在表内，动效设计副主编必须自定义等价三要素，并说明为什么适合当前内容。全稿超过 30% 页面使用同一 transform 类型时，触发 Anti-single-motion check。

### 动效脚本必须包含的字段

每页动效脚本应写入 `evidence/<run_id>/motion-script.json` 或等价表格，并至少包含：

```json
{
  "pageId": "P05",
  "pageRole": "data",
  "motionPurpose": "reveal_metric_evidence",
  "elements": [
    {
      "selector": ".metric-number",
      "transform": "clip-path: inset(0 100% 0 0) -> inset(0 0 0 0)",
      "easing": "cubic-bezier(0.25, 0.46, 0.45, 0.94)",
      "duration": "700ms",
      "delay": "0ms",
      "trigger": "on_enter",
      "stateFrom": "idle",
      "stateTo": "revealed",
      "settleTime": "150ms",
      "exportState": "completed"
    }
  ],
  "reducedMotion": "show completed state without transition",
  "evidence": {
    "initial": "",
    "completed": ""
  }
}
```

交互工程必须按脚本实现，不得自行改写 duration、easing、trigger 或 export 稳定态。若实现需要变更，必须退回动效设计副主编更新脚本。

## HTML状态机门禁

任何HTML演示中的分步、翻页、目录跳转、局部展开、Tab/滑动、悬浮提示、口播Demo或互动练习，都必须先定义状态机，再写CSS/JS动画。状态机不是工程附录，而是动效设计、交互工程和QA的共同合同。

| 状态/事件 | 必须定义 | 硬失败 |
| :--- | :--- | :--- |
| `idle` 首态 | 页面刚进入时哪些内容可见、焦点在哪里、哪些元素等待触发 | 首态已经露出第1点、答案或后续阶段 |
| `reveal(n)` 分步态 | 第n次触发出现哪些内容、哪些内容仍隐藏、动效目的是什么 | 点击后突然全显，或多个语义阶段一起出现 |
| `completed` 完成态 | 全部触发后稳定画面、讲者继续讲述时是否可读 | 完成态仍在动、重叠、遮挡或无法截图 |
| `reverse/back` 回退态 | 上一步、上一页、重新进入页面时恢复到哪一态 | 返回后状态混乱、重复触发或内容丢失 |
| `skip/nav` 跳转态 | 目录跳转、Home/End、快速翻页时是否跳过动画或落稳 | 快速导航截到半动画或空白页 |
| `export/print` 导出态 | 是否禁用动画、强制完成态或指定首态 | PDF/截图出现半透明、中间态、控制条或空白 |
| 输入事件 | 键盘、鼠标、触摸、滚轮、点击目标和节流策略 | 连点/连滚导致越级、错乱或失控 |

状态机必须写入《动效脚本》或《首态/后续态矩阵》。只在JS里临时维护计数器、CSS类或`setTimeout`，但没有状态机记录和QA证据，视为未完成动效设计。

## 首态/后续态矩阵

任何多步骤、清单、流程、链路、阶段、评分、5点/4点/3点讲解页面，必须补充本矩阵。没有矩阵时，动效设计和交互工程均不得进入实现。

| 字段 | 内容 |
| :--- | :--- |
| 页面/页组 |  |
| 可见静止骨架 | 背景、标题、坐标、空槽位、提示语等始终可见元素 |
| 初始态允许显示 | 打开页面不触发时允许出现的内容 |
| 初始态禁止显示 | 必须等待用户触发的步骤、答案、判断、阶段 |
| 触发序列 | 第1次/第2次/第3次...每次出现哪些元素 |
| 每步讲述目的 | 本次揭示帮助讲师完成什么推理或互动 |
| 不得合并项 | 哪些语义阶段不能一起出现，例如面试链路与录用后动作 |
| 完成态 | 全部触发后的稳定画面 |
| 每步截图/视频证据 | 首态、每次触发后和完成态的截图或视频路径 |
| 每步duration/easing/delay | 每次揭示的运动规格 |
| 每步settle time | 截图或继续讲述前需要等待的稳定时间 |
| 回退/重播策略 | 上一步、重新进入页面、导出模式如何处理 |

硬失败条件：第1个要点在未触发时已经完整显示；触发次数少于内容点数量且无脚本说明；后续答案、判断、阶段提前露出；多个语义阶段为省事合并出现；导出模式以外的演示模式默认展示完成态。

该规则跨项目生效，不只适用于培训课件。任何销售演示、客户汇报、研究报告、产品发布、工作坊、路演或HTML互动演示中，只要存在步骤、阶段、清单、模型、判断、答案、风险项、AI标注或行动项，都必须判断哪些内容属于首态、哪些必须由用户触发。为了“页面看起来完整”而默认露出第1项，仍属于硬失败。

## 页间与同页动效美感门禁

| 检查项 | 要求 | 硬失败 |
| :--- | :--- | :--- |
| 运动语法 | 至少定义方向、速度、缓动、停顿和完成态 | 全稿统一fade/rise或硬切 |
| 空间连续性 | 页间转场应让观众感到进入下一层、下一章或下一判断 | 每页像独立网页刷新 |
| 节奏差异 | 封面、章节、案例、流程、练习和收束有不同强度 | 所有页面同一时长同一动画 |
| 缓动曲线 | 使用自然的ease-out、expo/cubic等节奏，避免机械匀速 | linear或默认transition造成生硬感 |
| 讲述停顿 | 关键判断出现后有稳定停留，不抢讲师节奏 | 元素连续飞入，观众无法读完 |
| 触发反馈 | 用户触发分步时有轻微、明确、克制的反馈 | 点击后突然全显或无反馈 |
| 减动模式 | `prefers-reduced-motion`和export/print能落稳 | 减动后内容缺失或截图中间态 |

用户可见的动效生硬属于产品级失败，不是“后续优化”。如果用户指出页间或同页切换没有美感，下一版前必须重写运动语法：方向、速度、缓动、停顿、完成态、触发反馈和不同页面角色的节奏差异。只把duration调长、把`opacity`改平滑或统一加`translateY`，不得标为已修复。

## 否决项

动效设计副主编可否决以下情况：

1. 动效没有内容目的，只是为了“看起来高级”。
2. 每页使用相同入场动画，形成模板感。
3. 动效遮挡、延迟或打断核心信息。
4. 动效导致讲师无法控场，或观众需要等动画结束才能读页面。
5. 动效让截图/PDF/export模式出现半透明、半入场或空白状态。
6. 分步呈现破坏页面整体理解。
7. 动效与页面语气冲突，例如正式汇报中使用跳动、弹性、过度旋转或娱乐化节奏。
8. 动效被交互工程直接实现，未经过动效部、UI部、审美部和语言内容部并行审核。
9. 多步骤页面没有首态/后续态矩阵，或矩阵与实际HTML状态不一致。
10. 页间和同页切换缺少运动语法，只是机械淡入、上移或硬切。
11. 用户需要主动触发的第一点、答案或阶段在初始态已经显示。
12. 为了减少实现成本，把不同语义阶段合并到同一次出现。
13. 把HTML动效当成PPT点击动画，只实现“下一项出现”，没有状态机、输入节流、焦点/可访问性、回退/跳转和export稳定设计。

## 与其他部门的边界

| 部门 | 与动效关系 |
| :--- | :--- |
| 语言内容 | 决定讲述顺序、藏露节奏、术语解释顺序 |
| 品牌审美 | 判断动效气质是否符合品牌和场景 |
| 版式/UI | 确认动效不会破坏网格、对齐、层级和组件关系 |
| 交互工程 | 与动效设计共同定义HTML状态机、输入事件、焦点、节流、回退、目录跳转和export模式；按合同实现，不自行发明动效策略 |
| QA | 检查动效状态机、完成态、回退态、export模式、截图状态和动效是否造成遮挡 |

## QA检查

- 是否有动效脚本。
- 动效脚本是否经动效设计副主编、副总编和总编审核。
- 动效是否按页面角色变化，而不是全页同一效果。
- export/print模式是否禁用或稳定到完成态。
- 截图是否等待动效完成，或使用稳定模式。
- 动效是否造成重叠、遮挡、延迟阅读、分步缺信息。
- 动效是否服务讲述节奏，而不是工程炫技。
- 多步骤页面是否逐页核对首态/后续态矩阵。
- 用户触发次数、可见内容、最终完成态是否与脚本一致。
- 页间转场是否有空间连续性和节奏差异，而不是机械切页。
- HTML状态机是否可验证：键盘/鼠标/触摸/滚轮/目录跳转/回退/export是否都能落到预期状态。
