# 22-html-pre-visual-director

读取时机：当任务涉及 HTML Pre、HTML PPT、HTML interactive presentation、web slides、网页幻灯片、HTML演示审美专项、Style Frame、审美退回、页面不好看、AI味重、像模板、排版/UI失败、动效单一、presentation chrome碍眼时读取。若用户明确要求联网搜索、搜索参考、当前主流审美、最新UI趋势、优秀案例、最新组件库文档，或发生审美退回，必须同时读取 `23-online-research-toolchain.md`。

本文件定义 HTML Pre 视觉导演的最小工作面。它不替代 `00-production-gate.md`、`16-multi-agent-governance.md`、`21-design-skill-stack-integration.md` 或 QA，只负责把 HTML 演示的审美、UI、动效、控件和浏览器验证组织成可复核的导演合同。

## 导演目标

HTML Pre 不能只是“能翻页的网页”。它必须像一个可被现场讲述、可被截图审美复核、可被投屏阅读、可被导出干净画面的演示系统。

视觉导演必须先完成：

1. 页面族谱：cover、section divider、framework、case、process、table/matrix、data/metric、summary。
2. 视觉母线：来自用户资料、参考经验、Design DNA 和 Design Skill Stack，而不是模板表层。
3. 运动语法：页间、同页、分步、静止页、export 稳定态。
4. presentation chrome：audience、presenter、export、print 的控件状态。
5. 浏览器验证：真实渲染、响应式、hover/focus、分步状态。

## 视觉参考转译

HTML Pre 审美专项必须先读取 `15-visual-reference-library.md`，并结合 `21-design-skill-stack-integration.md`、`20-design-dna-guizang-integration.md` 输出参考经验转译。

最低证据：

- 参考库检索记录；
- 外部视觉参考转译卡，若读取了 `23`；
- 页面族谱映射；
- 参考不可照搬项；
- 当前项目改写方式；
- QA 可见证据。

只说“参考某某风格”“用了瑞士风”“参考了优秀网页”不算转译。

## 联网搜索与外部参考

HTML Pre 审美专项不得只依赖本地参考库。

当用户要求联网搜索、搜索参考、当前主流审美、最新UI趋势，或页面因不好看/AI味重/像模板被退回时，必须读取 `23-online-research-toolchain.md`，并完成：

- 外部参考搜索记录；
- 外部视觉参考转译卡；
- 最新文档检索记录，若涉及前端库；
- Playwright视觉验证记录，若已有可运行HTML；
- 联网/工具阻断记录，若工具不可用；
- 缺失控件安装提请记录，若必要工具未安装或未授权。

没有外部搜索证据时，不得宣称“已结合最新趋势”或“已参考优秀案例”。用户拒绝安装/授权必要联网或浏览器工具时，本 Skill 必须停止在阻断状态；不能在同一任务中继续产出依赖联网、最新文档或真实浏览器验证的 HTML Pre 视觉结论。

## 浏览器视觉验证

有可运行 HTML 后，视觉导演必须把 Playwright MCP 或等价浏览器工具的检查结果交给 QA。浏览器检查包括：

- 1440、1280、768、390 四类视口；
- cover、章节、正文密集、流程、表格/矩阵、数据、收束页；
- audience、presenter、export、print；
- 控件默认、hover、focus；
- 分步页面首态、过程态、完成态。

浏览器通过只能说明工程烟测通过。审美通过仍需品牌审美、版式/UI、动效和 QA 副主编复核。

## QA 阻断条件

以下任一情况出现，HTML Pre 不得冻结：

- 用户要求联网搜索但没有外部参考搜索记录；
- 用户要求当前/最新/主流趋势但没有趋势校准或外部近期验证；
- 涉及前端库但没有 Context7/官方文档检索记录；
- 有可运行HTML但没有 Playwright 或等价浏览器截图验证；
- 联网工具不可用但没有阻断记录和安装/启用提请；
- 必要控件缺失但没有安装提请记录；
- 用户拒绝安装/授权必要工具后仍继续执行；
- 无真实 subagent 证据或 `SUBAGENT-BLOCKER`；
- 只做静态代码检查或 validation，却声明完成视觉验证；
- 只有统一 fade/rise、机械位移动效或无首态/后续态矩阵；
- presentation chrome 默认抢画面，或 export/print 截图不干净。
