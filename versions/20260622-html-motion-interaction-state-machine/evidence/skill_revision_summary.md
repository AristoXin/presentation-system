# 2026-06-22 HTML Motion Interaction State Machine Revision

## 用户最新要求锁定

用户指出：动效设计绝不是点一下就出现下一个图标、表格或文字；动效还涉及交互设计。系统必须理解生成物是HTML文件，而不是传统PPT。

## 规则结论

presentation-system必须把HTML演示视为浏览器交互系统，而不是PPT点击动画模拟。凡涉及分步呈现、目录跳转、局部展开、口播Demo、练习页或互动页，生产前必须建立《HTML状态机与交互合同》，并由动效设计、交互工程和QA共同验收。

## 新增必填证据

- 《HTML状态机与交互合同》：覆盖`idle`、`reveal(n)`、`completed`、`reverse/back`、`skip/nav`、`export/print`等状态。
- 输入事件约束：覆盖键盘、鼠标、触摸、滚轮、目录跳转、回退、重播和快速连点。
- 可访问性约束：覆盖focus、aria-current、aria-expanded、aria-hidden和屏幕阅读状态。
- 输入节流/取消规则：防止连点、滚轮惯性或快速导航导致状态错乱。
- 截图/export稳定态：确保导出和截图不会截到半动画或中间态。

## 修改文件

- `SKILL.md`：新增HTML状态机与交互硬红线，并把《HTML状态机与交互合同》纳入HTML演示最低交付标准。
- `AGENTS.md`：新增入口流程和协作原则，禁止把HTML演示当作PPT点击动画模拟。
- `references/17-motion-design-standards.md`：新增HTML状态机门禁、动效脚本字段和动效QA否决项。
- `references/06-interaction-standards.md`：新增HTML不是PPT模拟、状态机、焦点/可访问性和输入节流要求。
- `references/07-qa-checklist.md`：新增HTML状态机、分步交互、focus/aria和export稳定QA项。
- `references/21-design-skill-stack-integration.md`：要求动效设计和交互工程在Skill吸收矩阵中共同判断HTML状态机与输入合同。
- `references/16-multi-agent-governance.md`：把HTML状态机与交互合同纳入动效设计、交互工程和Style Frame协同输入。

## 验收口径

若HTML页面只是点击后顺序出现图标、表格或文字，没有状态机、输入合同、焦点/aria、节流、回退/重播和export稳定态，动效设计、交互工程和QA均必须否决，不得进入QA冻结或用户验收。
