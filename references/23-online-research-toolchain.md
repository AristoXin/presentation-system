---
id: R23
title: Online Research Toolchain
applies_to:
  - latest_information
  - user_requests_online_search
  - official_sources
  - current_trends
gates:
  - G6
  - G7
  - G8
required_outputs:
  - ResearchEvidence
  - SourceList
  - ResearchBlocker
---

# 23-online-research-toolchain

读取时机：当任务涉及 HTML Pre、HTML PPT、HTML interactive presentation、网页幻灯片、视觉生产、Style Frame、审美退回、用户要求“联网搜索”“搜索参考”“查找优秀案例”“当前主流审美”“最新UI趋势”“最新组件库文档”“页面不好看”“AI味重”“像模板”“动效单一”时必须读取。

本文件定义联网搜索、外部参考提取、最新文档检索和真实浏览器视觉验证的工具链规则。

它不是替代 `15-visual-reference-library.md`，而是为参考库提供外部新鲜输入。它不是替代 `21-design-skill-stack-integration.md`，而是让 Design Skill Stack 能获得真实案例、最新文档和浏览器验证。它不是替代 QA，而是为 QA 提供截图、引用、提取记录和工具链证据。

## 核心原则

不能只依赖模型记忆或本地旧参考库来判断“当前主流审美”。当用户要求联网、趋势、当前、最新、主流、外部参考、优秀案例，或发生审美退回时，必须优先尝试外部搜索。

联网搜索结果必须被转译为设计经验，不能直接照搬页面。搜索不是为了找模板，而是为了回答：

1. 当前同类优秀作品如何组织信息？
2. 它们的视觉母线是什么？
3. 哪些结构经验可复用？
4. 哪些表层风格不适合当前项目？
5. 当前项目应如何改写？
6. QA 如何验证这些经验真的落地？

## 工具分层

| 工具/能力 | 主要用途 | 必须沉淀为 | 不合格信号 |
| :--- | :--- | :--- | :--- |
| Tavily Search | 搜索优秀网页、案例、设计趋势、竞品页面 | 外部参考候选表、搜索证据、采用/弃用理由 | 只说“搜索过”但没有 URL/标题/摘要/弃用理由 |
| Brave Search | 通用网页、图片、新闻、资料搜索 | 候选参考、趋势交叉验证 | 只找一条结果，没有对比 |
| Tavily Extract / Firecrawl | 提取网页正文、结构、设计系统页面、案例页面 | 页面结构分析、组件/布局/文案模式提取 | 复制网页表层视觉或文案 |
| Context7 | 获取 Tailwind、React、Vite、shadcn/ui、Framer Motion、GSAP 等最新文档 | 官方文档引用、API 使用依据、版本说明 | 使用过时 API 或凭记忆写代码 |
| Playwright MCP | 打开真实页面、截图、检查响应式、hover/focus、presentation chrome | 截图证据、视觉复核记录、交互状态证据 | 只做静态代码检查或工程 smoke test |
| last30days-skill | 检索最近30天跨 Reddit、X、YouTube、HN、Polymarket、GitHub、Web 等社区和趋势信号 | Last30Days 趋势脉冲、社区声音、采用/弃用判断 | 把它当普通搜索关键词；未运行引擎却声称已做近30天趋势研究 |
| 本地参考库 `15` | 沉淀长期设计经验和失败经验 | REF 记录、经验回写 | 外部搜索结果没有回写 |

## 缺失控件与安装同意

“控件”在本文件中包含 MCP 工具、插件、连接器、CLI、浏览器自动化能力、API key 或本地依赖。

使用本 Skill 时，若 Tavily、Brave、Firecrawl、Context7、Playwright MCP 或等价工具缺失，默认动作不是降级，而是由工具链与上下文工程副主编发起安装/启用路径：

1. 先判断该工具是否是当前任务的必需能力，并写入 Online Research Stack 决策表。
2. 若必需且可安装、可启用或可请求连接器，必须向用户提请同意，说明工具名称、用途、需要的权限/API key、可能费用或账号要求、安装后能完成什么证据。
3. 用户同意后，才可调用安装、启用、插件/连接器请求或本地依赖安装流程。
4. 用户拒绝、未提供必要 API key、或安装被权限阻断时，本 Skill 对该任务直接停止在阻断状态；不得自动降级为模型记忆、本地参考库或手工猜测。
5. 若用户改写任务边界，明确不再要求联网、最新文档或真实浏览器验证，才能另起降级任务；降级后不得宣称“已联网搜索”“已用最新文档”“已完成真实浏览器验证”。

必须记录：

```text
缺失控件安装提请记录
- 缺失工具：
- 任务用途：
- 是否必需：
- 安装/启用方式：
- 需要用户提供的授权/API key：
- 用户结论：同意/拒绝/未响应
- 结果：已安装/已启用/停止/任务边界已改写
- 降级后禁止宣称的能力：
```

## subagent 强制规则

联网搜索、外部参考转译、最新文档检索和浏览器视觉验证均属于可被副主编复核的能力域。凡进入生产、修复、审稿、QA冻结、Style Frame、审美退回恢复、HTML Pre视觉导演或Vx版本动作，subagent 建立不需要再次征求用户同意，必须按 `16-multi-agent-governance.md` 建立真实能力域 Agent。

若 subagent 工具不可用，必须写 `SUBAGENT-BLOCKER` 并停止生产。不得用“等待用户授权创建subagent”作为绕过理由。

## 什么时候必须联网搜索

以下情况必须执行联网搜索。若工具不可用，必须先提请用户同意安装/启用；用户拒绝或无法授权时写入阻断并停止，不得假装完成。

1. 用户明确说“联网搜索”“搜索一下”“查找参考”“找优秀案例”。
2. 用户要求“当前主流审美”“最新UI趋势”“流行趋势”。
3. 用户说页面“不好看”“AI味重”“像模板”“审美不行”。
4. 完整视觉生产前需要 Style Frame。
5. 旧参考库不足以支撑当前行业或项目类型。
6. 需要判断某个前端库、组件库、动画库的最新用法。
7. HTML Pre 需要对标真实优秀演示网页或产品发布页。
8. 审美退回后需要重做视觉方向。
9. 用户质疑是否真的学习了外部参考。
10. 需要验证当前设计趋势是否适合或应当弃用。

## Last30Days 趋势脉冲

当任务涉及“最近趋势”“当前审美”“社区正在讨论什么”“新工具/新框架/新设计范式反应”“某个品牌、产品、行业、演示风格最近30天舆情”时，优先把 `last30days-skill` 作为 G6 的条件性工具候选。

接入原则：

1. `last30days-skill` 不是普通 Web 搜索关键词。若安装并可用，必须读取其 `SKILL.md` 并按其 runtime contract 调用，不得临时改写为几次泛搜索。
2. 该工具适合捕捉近期社区声音、真实互动热度、争议点、用户语言、设计/产品趋势和工具采用信号；不适合替代官方文档、品牌规范、法律/合规来源或本项目 QA。
3. 若涉及设计审美趋势，结果必须转译为可执行设计判断：采用原则、弃用原则、页面族谱影响、motion/UI/copy 影响和 QA 可见证据。
4. 若工具未安装、缺少 API key、缺少平台授权或运行失败，必须写入 `ResearchBlocker`，不得声称已完成最近30天趋势扫描。
5. 若用户只要求只读审计，缺少 `last30days-skill` 不阻断分析；若用户要求正式生产并明确依赖最近趋势，缺失会影响 G6，必要时进入 Mode E。

必须输出：

```text
Last30Days 趋势脉冲
- 研究主题：
- 触发原因：最近趋势/当前审美/社区声音/工具反应/用户明确要求
- 工具状态：可用/不可用/未安装/授权缺失/运行失败
- 调用方式或阻断原因：
- 覆盖来源：
- 近30天高信号结论：
- 社区原话或高互动信号：
- 对当前项目的采用原则：
- 对当前项目的弃用原则：
- 影响页面/组件/动效/文案：
- 回写位置：
- 不能宣称的能力：
```

## 搜索范围

根据项目类型搜索不同参考。

| 项目类型 | 推荐关键词 |
| :--- | :--- |
| HTML Pre / HTML PPT | `best html presentation design examples`, `interactive web presentation design`, `modern keynote web presentation`, `HTML slide deck design examples`, `web slides presentation UI`, `网页幻灯片 设计 案例`, `HTML 演示稿 设计` |
| 客户汇报 / 商务汇报 | `consulting presentation design examples`, `business report presentation design`, `executive summary deck design`, `B2B SaaS report design` |
| 产品介绍 / SaaS | `SaaS product launch presentation design`, `product demo web presentation`, `SaaS landing page feature section design`, `modern product storytelling website` |
| 教育 / 培训 | `training deck design examples`, `education presentation visual design`, `courseware slide design examples`, `workshop slide design` |
| 技术 / AI / 系统架构 | `technical presentation design examples`, `AI product presentation design`, `developer conference slides design`, `system architecture slide design` |

## Context7 文档检索规则

当 HTML Pre 使用 Tailwind CSS、React、Vue、Svelte、Vite、shadcn/ui、Radix UI、Framer Motion、GSAP、Three.js、Reveal.js、Slidev、MDX 或 Playwright 时，必须优先用 Context7 或官方文档确认最新 API 和最佳实践。

必须输出：

```text
最新文档检索记录
- 目标库：
- 文档来源：
- 版本/日期：
- 采用 API：
- 弃用 API：
- 为什么适合当前 HTML Pre：
- 代码落地点：
```

禁止凭记忆使用可能过时的 API。禁止把组件库默认样式直接套进演示稿而不做视觉转译。

## 外部参考搜索记录

每次联网搜索后必须填写：

```text
外部参考搜索记录
- 搜索时间：
- 搜索工具：
- 搜索关键词：
- 搜索范围：
- 候选链接：
- 每个候选的标题/来源/访问状态：
- 采用候选：
- 弃用候选：
- 弃用理由：
- 可借鉴结构：
- 可借鉴组件：
- 可借鉴动效：
- 不可照搬项：
- 当前项目改写方式：
- 是否回写参考库：
```

候选链接至少 5 个。采用参考通常 1-3 个。至少要有 2 个弃用参考及弃用理由。没有弃用判断，说明没有真正做适配。

## 外部视觉参考转译卡

外部参考必须进入 `15-visual-reference-library.md` 的经验转译体系。

```text
外部视觉参考转译卡
- 参考来源：
- 类型：通用型/专用型/混合型
- 适用场景：
- 默认禁用场景：
- Design System 可借鉴：
- Design Style 可借鉴：
- Visual Effects 可借鉴：
- 页面族谱映射：
- 当前项目改写：
- 禁止照搬：
- QA可见证据：
```

如果参考图只是“好看”，但不能说明如何服务当前受众、内容和演示场景，应弃用。

## Playwright 视觉验证规则

HTML Pre 实现后必须使用 Playwright MCP 或等价浏览器工具进行真实渲染检查。

必须检查：1440px 桌面、1280px 笔记本、768px 平板、390px 移动端；cover、section divider、text-heavy slide、process/timeline slide、table/matrix slide、data/metric slide、summary slide；控件默认状态、hover/focus 状态、audience/presenter/export 模式；分步页面首态、过程态、完成态。

必须输出：

```text
Playwright视觉验证记录
- 工具：
- 页面路径：
- 检查尺寸：
- 截图路径：
- 检查页码：
- 控件默认状态：
- hover/focus状态：
- export模式：
- 分步状态：
- 发现问题：
- 修复动作：
- 复查结论：
```

Playwright 检查不能替代审美 QA。Playwright 截图、像素、键盘交互通过，只能叫“工程烟测通过”。必须另有人工审美复核，才能进入 QA 冻结。

## 联网失败处理

如果 Tavily、Brave、Firecrawl、Context7、Playwright MCP 或其他外部工具不可用，必须输出：

```text
联网/工具阻断记录
- 不可用工具：
- 预期用途：
- 失败原因：
- 是否可安装/启用：
- 安装提请记录：
- 是否可替代：
- 替代方案：
- 是否需要用户改写任务边界：
- 用户是否拒绝安装或授权：
- 任务边界改写后不能宣称的能力：
```

禁止：

- 工具不可用却说“已联网搜索”；
- 只用模型记忆冒充当前趋势；
- 只用旧参考库冒充外部近期验证；
- 只截图不做人工审美判断；
- 只跑 validation 就宣称 QA 通过；
- 用户拒绝安装/授权后继续执行依赖该工具的 Skill 路径。

## 与其他 reference 的关系

- 与 `15-visual-reference-library.md`：本文件负责外部搜索和提取，`15` 负责沉淀和转译。
- 与 `21-design-skill-stack-integration.md`：本文件负责为 Skill Stack 提供外部输入、最新文档和浏览器验证。
- 与 `22-html-pre-visual-director.md`：HTML Pre 视觉导演必须调用本文件完成外部参考搜索和 Playwright 验证。
- 与 `07-qa-checklist.md`：QA 必须检查本文件要求的搜索记录、文档记录和浏览器验证记录。
- 与 `08-skill-governance.md`：联网工具不可用时，必须按 Skill/工具安装提请和阻断处理；只有用户改写任务边界后才可另起降级路线。
