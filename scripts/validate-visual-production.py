#!/usr/bin/env python3
"""Detect obvious visual-production bypasses.

Run from the skill root, or pass a project/artifact directory:

    python scripts/validate-visual-production.py [target_dir]

The check is intentionally conservative. It proves required pre-code evidence
exists before formal HTML/PPT/PDF artifacts, and warns about static-PPT HTML,
template-like layout, and one-note motion patterns.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "templates",
    "references",
    "scripts",
    "tests",
    "skills",
    "agents",
}

FORMAL_EXTS = {".html", ".ppt", ".pptx", ".pdf"}
EVIDENCE_FILES = {
    "skill-availability-scan.md": "PRE_CODE_VISUAL_BLOCKER",
    "skill-invocation-ledger.md": "PRE_CODE_VISUAL_BLOCKER",
    "skill-absorption-matrix.md": "PRE_CODE_VISUAL_BLOCKER",
    "source-material-intake.md": "PRE_CODE_VISUAL_BLOCKER",
    "design-synthesis-contract.md": "PRE_CODE_VISUAL_BLOCKER",
    "motion-opportunity-map.md": "MOTION_DESIGN_BLOCKER",
    "anti-template-review.md": "TEMPLATE_PATTERN_BLOCKER",
    "html-experience-contract.md": "STATIC_PPT_HTML_RISK",
    "editorial-design-board.md": "EDITORIAL_APPROVAL_BLOCKER",
    "pre-code-visual-freeze.md": "PRE_CODE_VISUAL_BLOCKER",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(TARGET))
    except ValueError:
        return str(path)


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts[:-1]):
            continue
        files.append(path)
    return files


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def emit(kind: str, code: str, message: str) -> None:
    print(f"{kind} {code}: {message}")


def find_named(files: list[Path], name: str) -> list[Path]:
    return [path for path in files if path.name == name]


def analyze_html(path: Path, warnings: list[str], failures: list[str]) -> None:
    text = read(path)
    if not text:
        return

    slide_count = len(re.findall(r"\bslide\b|class=[\"'][^\"']*slide", text, re.I))
    has_next_prev = bool(re.search(r"\bnextSlide\s*\(|\bprevSlide\s*\(", text))
    has_reveal_state = bool(re.search(r"reveal|data-step|data-state|aria-expanded", text, re.I))
    has_reduced_motion = "prefers-reduced-motion" in text
    has_export_print = bool(re.search(r"@media\s+print|export-mode|data-export", text, re.I))
    has_inputs = bool(re.search(r"keydown|wheel|touchstart|pointerdown|click", text, re.I))
    has_page_specific = bool(re.search(r"page-\w+|slide-\w+|data-page|data-family", text, re.I))

    if slide_count >= 3 and has_next_prev and not has_reveal_state:
        warnings.append("STATIC_PPT_RISK")
        emit("WARN", "STATIC_PPT_RISK", f"{rel(path)} only appears to toggle slides with next/prev.")
    if slide_count >= 3 and not has_reduced_motion:
        warnings.append("REDUCED_MOTION_MISSING")
        emit("WARN", "REDUCED_MOTION_MISSING", f"{rel(path)} lacks prefers-reduced-motion handling.")
    if slide_count >= 3 and not has_export_print:
        warnings.append("EXPORT_PRINT_STABLE_MISSING")
        emit("WARN", "EXPORT_PRINT_STABLE_MISSING", f"{rel(path)} lacks print/export stable-state evidence.")
    if slide_count >= 3 and not has_inputs:
        warnings.append("INPUT_MODEL_MISSING")
        emit("WARN", "INPUT_MODEL_MISSING", f"{rel(path)} lacks keyboard/wheel/touch/click input handling.")
    if slide_count >= 3 and not has_page_specific:
        warnings.append("PAGE_STATE_MISSING")
        emit("WARN", "PAGE_STATE_MISSING", f"{rel(path)} lacks page-specific state or family markers.")

    keyframes = re.findall(r"@keyframes\s+([\w-]+)", text, re.I)
    fade_hits = len(re.findall(r"fadeIn|opacity\s*:", text, re.I))
    translate_y_hits = len(re.findall(r"translateY\s*\(", text, re.I))
    durations = re.findall(r"animation(?:-duration)?\s*:\s*[^;]*?([\d.]+m?s)", text, re.I)
    easings = re.findall(r"animation-timing-function\s*:\s*([^;]+)|\bcubic-bezier\([^)]*\)|\bease-[\w-]+", text, re.I)

    if slide_count >= 3 and len(set(keyframes)) <= 1 and (fade_hits + translate_y_hits) >= 8:
        warnings.append("MOTION_TEMPLATE_RISK")
        emit("WARN", "MOTION_TEMPLATE_RISK", f"{rel(path)} appears to rely on one fade/translate motion pattern.")
    if slide_count >= 3 and len(set(durations)) == 1 and len(durations) >= 6:
        warnings.append("UNIFORM_DURATION_RISK")
        emit("WARN", "UNIFORM_DURATION_RISK", f"{rel(path)} reuses one animation duration across many elements.")
    if slide_count >= 3 and len(set(filter(None, easings))) <= 1 and len(easings) >= 6:
        warnings.append("UNIFORM_EASING_RISK")
        emit("WARN", "UNIFORM_EASING_RISK", f"{rel(path)} reuses one easing pattern across many elements.")

    card_hits = len(re.findall(r"\bcard\b|class=[\"'][^\"']*card", text, re.I))
    grid_hits = len(re.findall(r"\bgrid\b|class=[\"'][^\"']*grid", text, re.I))
    if slide_count >= 3 and (card_hits >= slide_count * 3 or grid_hits >= slide_count * 2):
        warnings.append("TEMPLATE_PATTERN_RISK")
        emit("WARN", "TEMPLATE_PATTERN_RISK", f"{rel(path)} has repeated card/grid layout markers.")


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    files = iter_files(TARGET)
    artifacts = [path for path in files if path.suffix.lower() in FORMAL_EXTS]

    if not artifacts:
        emit("PASS", "NO_FORMAL_ARTIFACTS", f"No HTML/PPT/PDF artifacts found under {TARGET}.")
        print("Summary: 0 FAIL, 0 WARN")
        return 0

    emit("PASS", "FORMAL_ARTIFACTS_FOUND", f"Found {len(artifacts)} formal artifact(s).")

    for name, code in EVIDENCE_FILES.items():
        matches = find_named(files, name)
        if not matches:
            failures.append(code)
            emit("FAIL", code, f"Formal artifacts exist but {name} is missing.")
        else:
            emit("PASS", "EVIDENCE_FOUND", f"{name} -> {rel(matches[0])}")

    for path in artifacts:
        if path.suffix.lower() == ".html":
            analyze_html(path, warnings, failures)

    print()
    print(f"Summary: {len(failures)} FAIL, {len(warnings)} WARN")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
