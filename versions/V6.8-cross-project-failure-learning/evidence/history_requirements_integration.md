# 历史对话需求整合表：跨项目失败经验回写

> 日期：2026-06-20  
> 触发原话（已脱敏）：用户指出明显问题没有更新到设计参考文档，且这些问题不应只针对某个客户培训项目修复，而应成为所有后续项目都不能再出现的通用经验。  
> 结论：本次不是修改特定客户培训产物，而是修订`presentation-system`长期reference，使明显失败跨项目生效。

## 用户最新要求锁定表

| 编号 | 用户最新原话摘要 | 禁止事项 | 验收标准 | 是否覆盖旧要求 | 执行理解 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U1 | “明显的问题你没有更新你的设计参考文档” | 不得只在当前项目失败审计里承认问题 | 必须更新长期设计参考/QA/动效/经验库文档 | 是 | 将V0.12/V0.13暴露的问题固化为跨项目规则 | 已执行 |
| U2 | “这不是都应该固化成你的经验吗” | 不得写“下次注意”式总结 | 必须新增可执行门禁、模板和阻断条件 | 是 | 写入reference和版本证据 | 已执行 |
| U3 | “并不是针对某个客户培训项目” | 不得把规则写成特定客户专属 | 后续任何项目都不能出现同类问题 | 是 | 使用跨项目、所有视觉生产、所有HTML/PPT/PDF口径 | 已执行 |

## 历史要求整合表

| 编号 | 用户历史要求/退回原话摘要 | 触发的问题类型 | 必须写入的规则 | 影响文件 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H1 | 上一版明显问题没有解决 | 回归/QA | 下一版前必须建立《上一版问题关闭矩阵》 | `07-qa-checklist.md`、`04-design-standards.md`、`10-version-evidence.md` | 已修 |
| H2 | 明显设计问题没有固化成经验 | 参考库/经验回写 | 用户点名失败必须进入跨项目reference | `15-visual-reference-library.md`、`18-history-derived-governance.md` | 已修 |
| H3 | 别的项目也不能出现这些问题 | 设计硬红线 | 光学失衡、分步提前露出、语义阶段合并、动效生硬、页面丑、部门空转必须跨项目阻断 | `04-design-standards.md`、`11-aesthetic-anti-ai.md`、`17-motion-design-standards.md`、`07-qa-checklist.md` | 已修 |
| H4 | “第12版出现的问题在第13版上也没有得到更新解决，还是一样的存在。” | 跨版本回归失败 | 若上一版点名问题在新版仍存在，新版必须自动标记`FAILED_VISUAL_FREEZE`，不得继续称候选 | `SKILL.md`、`AGENTS.md`、`18-history-derived-governance.md` | 已修 |

## 已固化的跨项目规则

| 规则 | 跨项目适用范围 | 更新位置 |
| :--- | :--- | :--- |
| 用户点名旧问题后，下一版必须先建《上一版问题关闭矩阵》 | 所有HTML/PPT/PDF视觉生产、审美退回修复 | `04-design-standards.md`、`07-qa-checklist.md`、`10-version-evidence.md` |
| 光学失衡不是局部审美偏好，而是通用设计失败 | 封面、章节页、模型页、案例页、工作台页、收束页 | `04-design-standards.md`、`11-aesthetic-anti-ai.md` |
| 第1点/答案/后续阶段提前露出是分步设计硬失败 | 流程、清单、模型、练习、AI复核、行动页 | `17-motion-design-standards.md`、`07-qa-checklist.md` |
| 页间和同页动效生硬是产品级失败 | HTML演示、动画型PPT、互动课件 | `17-motion-design-standards.md`、`11-aesthetic-anti-ai.md` |
| 页面被用户评价为丑且不是单点bug时，必须重写视觉母线和Page Spec | 所有视觉项目 | `04-design-standards.md`、`11-aesthetic-anti-ai.md` |
| 部门记录通过但明显问题仍存在时，协作记录无效 | 多Agent/副主编机制下的所有生产 | `18-history-derived-governance.md`、`07-qa-checklist.md` |
| 用户点名失败必须回写reference，不能只留在项目审计 | 所有失败治理、审美退回、QA退回 | `15-visual-reference-library.md`、`10-version-evidence.md` |
| V12问题在V13仍存在时，V13必须自动失败冻结 | 所有跨版本修复、重做、新版生成 | `SKILL.md`、`AGENTS.md`、`18-history-derived-governance.md` |

## 用户截图原话证据

截图路径：`/var/folders/62/lp13kztd48l67gvsrpnkkzkm0000gn/T/codex-clipboard-6f49e8fd-1d22-4e12-b216-079fdceedaa3.png`

原话摘要：

- 第1页明显头轻脚重、左重右轻。
- 第9页刚好相反，跨页排版重心失衡。
- 页间切换和同页切换动效十分生硬，没有美感。
- 第9页右侧5点中第1点无需用户切换就显示，动效缺失。
- 第5页面试链路/录用后等阶段一起出现。
- 第15页及部分页面丑。
- 类似问题层出不穷，说明Skill层面的UI、内容文案、审美、流行调研、动效等部门全面失效。

## 修改文件

- `presentation-system/references/18-history-derived-governance.md`
- `presentation-system/references/04-design-standards.md`
- `presentation-system/references/11-aesthetic-anti-ai.md`
- `presentation-system/references/07-qa-checklist.md`
- `presentation-system/references/15-visual-reference-library.md`
- `presentation-system/references/17-motion-design-standards.md`
- `presentation-system/references/10-version-evidence.md`

## 边界说明

本次为Skill治理和reference回写，未修改HTML演示产物，未创建新版样张，未运行截图或validation。V0.13仍保持用户退回和`FAILED_VISUAL_FREEZE`状态。
