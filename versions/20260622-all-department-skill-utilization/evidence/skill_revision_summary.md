# 20260622 全部门 Skill 使用闭环修订证据

## 用户最新要求锁定

- “其余的部门难道没有需要调用这些skill的吗？”
- “presentation这个skill是否已经完成全面的修改和同步。”

## 修订结论

此前修订已经覆盖初始方向 Skill 栈、UI 部门对 `huashu-ppt` / `huashu-slides` 的判断责任，以及正式生产阶段二次调用。但它仍可能被误读为主要由 UI、品牌、动效、工程和 QA 承担 Skill 使用责任，需求与交付、语言内容两类部门没有足够硬绑定。

本次修订将 Skill 调用责任扩展为全部适用部门闭环：

- 需求与交付必须判断 `ppt-master`、`frontend-slides`、`html-ppt`、`guizang-ppt-skill`、`huashu-ppt` / `huashu-slides`、`humanize-ppt` 对交付格式、可编辑性、图片PPT路线、讲者备注和降级审批的影响。
- 语言内容必须判断 `humanize-ppt`、`huashu-ppt` / `huashu-slides`、`huashu-design`、`taste-skill` 对叙事结构、页面类型密度、讲师动作、术语组件和内容到UI/动效转译的影响。
- 品牌审美、版式/UI、动效设计、交互工程和 QA 继续保留原 Skill 调用责任，并明确不得把 `huashu-ppt` / `huashu-slides` 视为单一部门事项。
- 任一部门可以判定某 Skill 不适用，但必须给出本部门职责相关的弃用理由；无理由“不适用”视为未充分使用 Skill。

## 修改文件

- `SKILL.md`
  - 将“版式/UI部门必须额外判断”升级为“所有适用部门必须填写《部门Skill使用矩阵》”。
  - 在 Design Skill Stack 集成硬门禁中补充需求/交付和语言内容副主编的必判 Skill。
- `AGENTS.md`
  - 将 4b1 从 UI 重点约束扩展为全部门矩阵约束。
- `references/21-design-skill-stack-integration.md`
  - 在《部门Skill使用矩阵》中新增“需求与交付”“语言内容”两行。
  - 将 `huashu-ppt` / `huashu-slides` 适用责任扩展到需求与交付、语言内容、品牌审美、版式/UI、动效设计、交互/工程和 QA。
  - 在 Design Skill Stack 决策表新增 `humanize-ppt` 和 `ppt-master`。
- `references/16-multi-agent-governance.md`
  - 在最小 Agent 编制中补充需求与交付、语言内容的 Skill 判断责任。
  - 在上传文件协同初审和 Style Frame 协同生成中新增或强化需求/交付、语言内容的 Skill 责任。

## 验收标准

后续任何 HTML/PPT/Slides/视觉叙事任务，在部门初始方向、Style Frame、正式生产平台和 QA 冻结阶段，都必须能回答：

1. 哪些部门适用？
2. 每个适用部门判断了哪些 Skill？
3. 哪些 Skill 被采用、弃用、阻断？
4. 采用结论如何进入 Page Spec、制作工单、真实产物和 QA 字段？
5. 弃用或阻断是否有本部门职责相关理由？

缺任一项时，不得宣称 presentation-system 已完成团队闭环或 Skill 充分使用。
