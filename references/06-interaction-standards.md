# 06-interaction-standards

读取时机：当任务涉及HTML交互演示、Web slides、前端演示框架、快捷键、滚轮、触摸、目录、全屏、讲者备注、控制栏、presentation chrome、audience/presenter/export模式时读取。若涉及动效、动画、分步呈现、转场节奏，同时读取`17-motion-design-standards.md`；动效策略由动效设计部负责，交互工程只负责实现。

HTML交互演示必须支持：

- 键盘翻页：左右键、PageUp/PageDown、空格、Home/End。
- 鼠标滚轮翻页：平滑且节流。
- 触摸滑动：移动端可用。
- 全屏模式：适配全屏下的交互。
- 目录：缩略图或章节跳转。
- 讲者提示：当前页备注、计时和下一页标题。
- 帮助面板：快捷键说明。
- 动效脚本：若页面含动画或分步出现，必须来自动效设计部审核通过的脚本。

红线：

- 翻页完成时核心内容必须完整可见。
- 控制栏不得遮挡正文、图表或关键按钮。
- 自动动效不得造成空页、半页或阅读滞后。
- 未经动效设计部批准，不得由工程实现层临时添加动画。
- 翻页、目录、帮助、全屏、提示、编辑等控制按钮不得默认强显示。
- export/print模式必须隐藏全部交互chrome。

## 实现要求

| 能力 | 要求 |
| :--- | :--- |
| 舞台 | 默认16:9固定舞台，按视口等比缩放 |
| 键盘 | 左右键、PageUp/PageDown、空格、Home/End |
| 滚轮 | 节流处理，避免一次滚动连翻多页 |
| 触摸 | 支持横向滑动，避免与页面滚动冲突 |
| 目录 | 可从缩略图或章节列表跳转 |
| 讲者提示 | 当前页备注、计时和下一页标题 |
| 控制栏 | 默认隐藏、透明或极弱化，靠近底部或触控唤起，不遮挡关键内容；底部操作栏按钮必须采用“中文动作词 + 图标”的组合，不得只显示符号、英文缩写或问号 |

## Presentation Chrome规则

HTML演示中的翻页、目录、帮助、全屏、提示、编辑等控制按钮不得默认强显示。

默认状态必须满足：

1. 控制条默认隐藏、透明或极弱化。
2. 鼠标进入底部控制区域附近时再显示。
3. 鼠标离开后自动淡出。
4. 控制条不得遮挡主体内容。
5. 控制条视觉必须轻量，不能像网页后台按钮。
6. 控制条按钮必须使用中文标签加图标，例如“上一页 ‹”“下一页 ›”“目录 ▦”“讲者 ◐”“帮助 ?”；图标只做识别辅助，中文动作用于降低现场误操作。
7. 控制条必须有清晰的`title`/`aria-label`，且标签文案与实际动作一致。
8. 控制条必须支持键盘翻页，因此即使隐藏也不能影响可用性。
9. 移动端可通过轻触或滑动唤起控制。
10. 打印模式必须隐藏全部控制条。
11. 截图导出模式必须隐藏全部控制条。
12. audience模式默认隐藏；presenter模式可显示更多工具，但也不能破坏画面。

推荐CSS机制：

```css
.deck-controls {
  opacity: 0;
  transform: translateX(-50%) translateY(14px);
  pointer-events: none;
  transition: opacity .22s ease, transform .22s ease;
}

.deck-controls.is-visible,
.deck-controls:hover,
.chrome-hotzone:hover + .deck-controls {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
  pointer-events: auto;
}

.chrome-hotzone {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  height: 96px;
  z-index: 999;
}

.deck-controls button {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.deck-controls .icon {
  font-family: var(--mono, monospace);
}

@media print {
  .deck-controls,
  .chrome-hotzone {
    display: none !important;
  }
}

body[data-mode="export"] .deck-controls,
body[data-mode="export"] .chrome-hotzone {
  display: none !important;
}
```

推荐JS机制：

```js
const controls = document.querySelector(".deck-controls");
let chromeTimer;

window.addEventListener("mousemove", (event) => {
  const nearBottom = window.innerHeight - event.clientY < 120;
  if (!nearBottom) return;

  controls.classList.add("is-visible");
  clearTimeout(chromeTimer);
  chromeTimer = setTimeout(() => {
    controls.classList.remove("is-visible");
  }, 1400);
});
```

这只是参考实现，不要求逐字照抄；最终效果必须满足默认不破坏页面美感、靠近时可用。

## audience / presenter / export模式

| 模式 | 用途 | Chrome规则 |
| :--- | :--- | :--- |
| `audience` | 默认模式，面向观众播放 | 隐藏讲者提示、编辑入口，控制条弱化或隐藏 |
| `presenter` | 演示者模式 | 可显示讲者提示、编辑按钮、目录等，但必须低干扰 |
| `export` | 截图、PDF、交付预览 | 必须隐藏所有交互chrome |

URL参数可使用`?mode=audience`、`?mode=presenter`、`?mode=export`。未指定时默认`audience`。

## QA步骤

1. 打开首屏，确认核心内容首帧可见。
2. 逐页键盘翻页。
3. 逐页滚轮翻页，确认节流。
4. 打开目录并跳转到中间页和末页。
5. 开关全屏和讲者提示。
6. 检查默认打开时控制条是否隐藏或弱化。
7. 鼠标靠近底部，确认控制条平滑出现；鼠标离开后自动淡出。
8. 检查底部操作栏是否为中文动作词 + 图标，并具备`title`/`aria-label`；只显示图标、英文缩写或问号时退回交互工程。
9. 检查audience、presenter、export模式差异。
10. 截取所有页面，检查是否有空页、遮挡、裂图、动效延迟或chrome残留。
11. 若有动效，核对`17-motion-design-standards.md`的动效脚本、静止页清单和export稳定策略。

## 截图测试接口

HTML演示必须提供可靠的测试路径，避免QA脚本只能手动切换CSS类：

- 优先暴露全局只读/受控测试接口，例如`window.__deck.showSlide(index)`、`window.__deck.count`、`window.__deck.mode("export")`。
- 若不暴露接口，截图脚本必须通过真实键盘、目录或按钮导航逐页截图，不能直接改`.active/.visible`后宣称通过。
- 截图前必须等待入场动效完成，或在export模式下禁用/跳过reveal动画；不得截取半透明、半入场状态作为审美证据。
- 若动效脚本要求分步讲述，截图证据必须明确是完成态、首态还是指定步骤态，并记录触发方式、duration/easing/delay和完成态等待时间；不得用随机中间态宣称通过。
- export模式截图必须隐藏控制条、讲者提示、编辑入口和帮助面板。
