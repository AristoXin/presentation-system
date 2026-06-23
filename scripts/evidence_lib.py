#!/usr/bin/env python3
"""Shared helpers for presentation-system validators.

Only the Python standard library is used. Runtime evidence is JSON; files with
`.yaml` extensions in this repository may be JSON-compatible YAML.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALID_ROUTES = {
    "html_interactive",
    "pptx_editable",
    "pdf_static",
    "screenshot_pack",
    "review_only",
    "skill_governance",
}
VALID_STAGES = {
    "startup",
    "intake",
    "design",
    "editorial_review",
    "implementation",
    "post_build_qa",
    "qa_freeze",
    "failure_recovery",
}
FORMAL_EXTS = {".html", ".ppt", ".pptx", ".pdf"}


class ValidationIssue:
    def __init__(self, level: str, code: str, message: str) -> None:
        self.level = level
        self.code = code
        self.message = message

    def to_dict(self) -> dict[str, str]:
        return {"level": self.level, "code": self.code, "message": self.message}


class IssueLog:
    def __init__(self) -> None:
        self.issues: list[ValidationIssue] = []

    def fail(self, code: str, message: str) -> None:
        self.issues.append(ValidationIssue("FAIL", code, message))
        print(f"FAIL {code}: {message}")

    def warn(self, code: str, message: str) -> None:
        self.issues.append(ValidationIssue("WARN", code, message))
        print(f"WARN {code}: {message}")

    def pass_(self, code: str, message: str) -> None:
        self.issues.append(ValidationIssue("PASS", code, message))
        print(f"PASS {code}: {message}")

    @property
    def failures(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "FAIL"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "WARN"]

    def summary(self) -> dict[str, int]:
        return {
            "fail": len(self.failures),
            "warn": len(self.warnings),
            "pass": len([issue for issue in self.issues if issue.level == "PASS"]),
        }


def load_json(path: Path, log: IssueLog | None = None, code: str = "JSON_INVALID") -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        if log:
            log.fail("FILE_MISSING", f"{path} does not exist")
        raise
    except json.JSONDecodeError as exc:
        if log:
            log.fail(code, f"{path} is not valid JSON-compatible evidence: {exc}")
        raise


def write_report(path: Path | None, payload: dict[str, Any]) -> None:
    if not path:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        stripped = value.strip()
        return bool(stripped) and stripped not in {"...", "<placeholder>", "TBD", "TODO", "N/A"}
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def resolve_evidence_dir(target: Path, run_id: str | None) -> tuple[Path, dict[str, Any]]:
    candidates: list[Path] = []
    if run_id:
        candidates.extend([target / "evidence" / run_id, target])
    candidates.append(target)
    if target.name == "evidence":
        candidates.append(target)
    if (target / "evidence").exists() and not run_id:
        candidates.extend(path for path in (target / "evidence").iterdir() if path.is_dir())

    for candidate in candidates:
        run_path = candidate / "run.json"
        if not run_path.exists():
            continue
        run = load_json(run_path)
        if run_id and run.get("run_id") != run_id:
            continue
        return candidate, run
    raise FileNotFoundError(f"No run.json found for run_id={run_id!r} under {target}")


def evidence_path(evidence_dir: Path, name: str) -> Path:
    return evidence_dir / name


def path_from_ref(base: Path, evidence_dir: Path, ref: str | None) -> Path | None:
    if not ref:
        return None
    raw = Path(ref)
    candidates = []
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.extend([evidence_dir / raw, base / raw])
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0] if candidates else None


def has_field_path(data: Any, field_path: str) -> bool:
    current = data
    for part in field_path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.isdigit() and int(part) < len(current):
            current = current[int(part)]
        else:
            return False
    return non_empty(current)


def formal_artifacts(target: Path) -> list[Path]:
    excluded = {".git", "templates", "references", "scripts", "tests", "skills", "agents"}
    artifacts: list[Path] = []
    for path in target.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in FORMAL_EXTS:
            continue
        try:
            parts = path.relative_to(target).parts[:-1]
        except ValueError:
            parts = path.parts
        if any(part in excluded for part in parts):
            continue
        artifacts.append(path)
    return artifacts


def load_registry() -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    registry_path = ROOT / "skills" / "visual-skill-registry.json"
    registry = load_json(registry_path)
    skills: dict[str, dict[str, Any]] = {}
    aliases: dict[str, str] = {}
    for skill in registry.get("skills", []):
        skill_id = skill["id"]
        skills[skill_id] = skill
        aliases[skill_id.lower()] = skill_id
        for alias in skill.get("aliases", []):
            aliases[str(alias).lower()] = skill_id
    return skills, aliases


def canonical_skill_id(value: str, aliases: dict[str, str]) -> str:
    return aliases.get(value.lower(), value)


def current_machine_context() -> dict[str, str]:
    return {
        "hostname": os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME") or "unknown",
        "platform": os.name,
        "session": os.environ.get("CODEX_SESSION_ID", "unavailable"),
    }
