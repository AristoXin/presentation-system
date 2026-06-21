# Skill修订摘要

版本：V6.5-visual-motion-failure-governance

## 修改范围

- `presentation-system/SKILL.md`
- `presentation-system/references/04-design-standards.md`
- `presentation-system/references/07-qa-checklist.md`
- `presentation-system/references/11-aesthetic-anti-ai.md`
- `presentation-system/references/16-multi-agent-governance.md`
- `presentation-system/references/17-motion-design-standards.md`

## 核心修订

1. 新增用户点名失败专项硬门禁：点名页必须进入失败审计和Page Spec重写，不得按局部CSS修复处理。
2. 新增条件通过失效硬门禁：用户可见基础失败存在时，所有“条件通过/工程烟测通过/后续优化”均不能放行。
3. 新增光学平衡门禁：检查上下/左右重量、主视觉落点、阅读路径和跨页节奏。
4. 新增首态/后续态矩阵：多步骤页必须证明初始态、逐步触发态和完成态正确。
5. 新增动效美感门禁：页间和同页切换必须有运动语法、空间连续性、节奏差异和自然缓动。
6. 扩展QA：把光学平衡、分步状态、动效美感纳入HTML审美QA和用户点名问题优先级。
7. 扩展多Agent治理：部门复核必须有页码、风险/反对项和硬失败检查，空泛通过无效。

## 未执行事项

- 未创建新HTML版本。
- 未修改`html演示样张_V0.12`。
- 未运行Playwright、截图、导出或validation。

## 恢复生产条件

- 用户明确批准恢复生产。
- 新版本生产前先生成文字Page Spec或Style Frame候选方向。
- UI、内容文案、审美、流行调研、动效、交互工程、QA均按新门禁提供逐页证据。
