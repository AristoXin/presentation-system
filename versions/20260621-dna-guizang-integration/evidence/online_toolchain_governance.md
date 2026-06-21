# Skill治理证据：Online Research Toolchain 与 subagent默认建立

> 日期：2026-06-21  
> 状态：Skill治理可写 / 未创建产物 / 未恢复生产

## 用户最新要求锁定表

| 编号 | 用户最新原话摘要 | 禁止事项 | 验收标准 | 是否覆盖旧要求 | 执行理解 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U3 | “请继续修订 presentation-system，补齐‘联网搜索 / 外部参考 / 最新文档 / 浏览器视觉验证’能力。这是补丁，不是生成产物任务。” | 不得创建、修改、截图、导出任何HTML/PPT/PDF交付物 | 新增`23-online-research-toolchain.md`，并接入入口、HTML Pre视觉导演、参考库、Skill治理、Design Skill Stack、生产门禁、QA和verify | 是 | 本轮只修Skill系统文件、reference、manifest/lock/verify脚本和治理记录 | 已闭环 |
| U4 | “里面缺少的控件如果用户缺少，你应该是直接帮用户进行安装，只要使用本skill的都默认此规则，但是应该提请用户同意，如果用户拒绝，则该skill直接停止。建立subagent不需要经过用户同意，必须建立。” | 不得自动降级；不得用户拒绝后继续；不得询问是否允许创建subagent | 必要控件缺失时有安装/启用提请；用户拒绝则停止；subagent在生产/复核/Style Frame/QA链路中默认必建 | 是 | 需要同时修订`23`、`08`、`16`、`00`、`07`、入口和验证脚本 | 已闭环 |

## 规则闭环映射表

| 新增/修改规则 | 触发条件 | 必填证据 | 阻断条件 | 责任部门 | 写入文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Online Research Stack硬门禁 | 联网搜索、外部参考、当前趋势、最新文档、浏览器视觉验证、HTML Pre审美退回 | Online Research Stack决策表、外部参考搜索记录、外部视觉参考转译卡、最新文档检索记录、Playwright视觉验证记录或工具阻断记录 | 用户要求联网但无搜索记录；本地参考库冒充联网；工具不可用却假装完成 | 品牌审美、工具链、交互工程、QA | `SKILL.md`、`23-online-research-toolchain.md`、`00-production-gate.md`、`07-qa-checklist.md` |
| 缺失控件安装提请 | Tavily/Brave/Firecrawl/Context7/Playwright等必要控件缺失 | 缺失控件安装提请记录、用户结论、联网/工具阻断记录 | 用户拒绝安装/授权/提供API key后继续执行 | 工具链与上下文工程副主编 | `23-online-research-toolchain.md`、`08-skill-governance.md`、`skills.manifest.yaml`、`skills.lock.json` |
| HTML Pre视觉导演 | HTML Pre、HTML PPT、网页幻灯片、排版/UI失败、动效单一、控件破坏画面 | HTML Pre视觉导演合同、联网搜索证据、浏览器验证计划、presentation chrome复盘 | 只跑静态验证或自动validation；无Playwright/等价浏览器记录却宣称真实验证 | 版式/UI、动效、交互工程、QA | `22-html-pre-visual-director.md` |
| subagent默认建立 | 生产、修复、审稿、QA冻结、Style Frame、审美退回恢复、Vx动作 | SEL-real：真实Agent id、线程证据、能力域、输入、输出、同一Agent复审 | 询问是否允许创建subagent；主Agent分角色；`SUBAGENT-BLOCKER`冒充放行证据 | 总编、副总编、各能力域副主编 | `16-multi-agent-governance.md`、`00-production-gate.md`、`SKILL.md`、`07-qa-checklist.md` |

## 本轮未做事项

- 未创建、复制、修改、截图、导出任何HTML/PPT/PDF/截图包/样张目录。
- 未安装任何联网工具、MCP、连接器或依赖。
- 未恢复V0.14A/B生产。
- 未运行Playwright截图或validation。
