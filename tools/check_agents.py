"""Verify local agent policy provenance and integrity without network access."""

import hashlib
import json
import re
from pathlib import Path


def validate(root: Path) -> None:
    contract = json.loads((root / ".clear-solutions/project.json").read_text())
    manifest = json.loads((root / ".clear-solutions/policy-manifest.json").read_text())
    if not re.fullmatch(r"[a-f0-9]{40}", contract["policy_commit"]):
        raise ValueError("Policy commit must be a full SHA")
    for key in ["policy_repository", "policy_commit"]:
        if contract[key] != manifest[key]:
            raise ValueError("Policy snapshot does not match contract: " + key)
    if not manifest["files"]:
        raise ValueError("Policy snapshot is empty")
    snapshot = (root / "docs/policy").resolve()
    for name, digest in manifest["files"].items():
        path = (snapshot / name).resolve()
        if not path.is_relative_to(snapshot) or not path.is_file():
            raise ValueError("Missing or unsafe policy path: " + name)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("Modified policy snapshot: " + name)
    for name in ["AGENTS.md", "CLAUDE.md", ".agents/rules/project.md", "docs/agent-workflow.md", ".cursorignore"]:
        if not (root / name).is_file():
            raise ValueError("Missing agent entry point: " + name)
    rules = (root / ".cursor/rules/project.mdc").read_text()
    if "alwaysApply: true" not in rules or "@AGENTS.md" not in rules:
        raise ValueError("Cursor must load the canonical AGENTS.md")

    if "@AGENTS.md" not in (root / "CLAUDE.md").read_text().splitlines():
        raise ValueError("Claude Code must import the canonical AGENTS.md")
    antigravity = (root / ".agents/rules/project.md").read_text()
    if not antigravity.startswith("---\n"):
        raise ValueError("Antigravity requires valid frontmatter")
    frontmatter = antigravity.split("---", 2)[1]
    if "trigger: always_on" not in frontmatter.splitlines():
        raise ValueError("Antigravity must use the always_on trigger")
    if "@../../AGENTS.md" not in antigravity:
        raise ValueError("Antigravity must reference the canonical AGENTS.md")


if __name__ == "__main__":
    validate(Path(__file__).resolve().parents[1])
    print("PASS: pinned local policy and agent entry points")
