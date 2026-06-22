---
id: R09
title: Context Engineering
applies_to:
  - long_task
  - context_compression
  - headroom
gates:
  - G2
  - G4
required_outputs:
  - ContextPlan
---

# 09-context-engineering

读取时机：当任务跨多轮、输入资料很多、日志很长、截图/导出很多、需要版本归档、或模型开始失焦时读取。

## 上下文治理

- 每次任务只读取与当前目标相关的reference文件。
- 长任务必须定期生成阶段摘要，记录已读文件、已改文件、待办事项和风险。
- 日志、截图、导出文件和QA记录必须按版本归档。
- 当文件很多、日志很长或任务跨多轮时，由工具链与上下文工程副主编判断是否启用`headroom`。本项目内嵌版本位于`skills/vendor/headroom/SKILL.md`。
- `headroom`不是默认必用Skill；只有在长任务、多文件、多subagent、多证据或接近上下文压缩时才调用。

## 操作规则

1. 每轮开始列出已读关键文件和当前目标。
2. 每次大改后记录已改文件、版本号和下一步。
3. 对长文件先检索目录和关键词，再读取相关段落。
4. 版本冻结时，把主文档、证据和QA记录复制到`versions/<version>/`。
5. 根目录只保留最新版，不在根目录堆多个历史版本。
6. 启用`headroom`时，按其模板写入`versions/<version>/evidence/headroom-state.md`；未启用时，在Skill确认单中写明“可用但不调用”的理由。

## 摘要模板

```text
当前目标：
已读文件：
已改文件：
关键决策：
待验证：
风险/阻塞：
下一步：
```
