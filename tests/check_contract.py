#!/usr/bin/env python3
"""Static integrity checks for the Kith AI interviewer contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "INTERVIEWER.md",
    "llms.txt",
    ".github/copilot-instructions.md",
    ".cursor/rules/interviewer.mdc",
    "examples/ai-first-session.md",
    "templates/ai_session_state.md",
    "tests/ai-interviewer-acceptance.md",
}

REQUIRED_CONTRACT_TEXT = {
    "# Kith AI Interviewer",
    "## Assumptions to check",
    "## Fast start",
    "## The turn loop",
    "## Safety filter for every question",
    "## Internal session state",
    "## “Off the record” in an AI chat",
    "## Closing a session",
    "Never answer in the narrator's first person.",
    "Do not write narrator data into this public repository by default",
}

ADAPTER_REFERENCES = {
    "AGENTS.md": "INTERVIEWER.md",
    "CLAUDE.md": "@INTERVIEWER.md",
    "GEMINI.md": "@./INTERVIEWER.md",
    ".github/copilot-instructions.md": "INTERVIEWER.md",
    ".cursor/rules/interviewer.mdc": "@INTERVIEWER.md",
    "llms.txt": "/INTERVIEWER.md",
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check_files(errors: list[str]) -> None:
    for relative in sorted(EXPECTED_FILES):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_contract(errors: list[str]) -> None:
    path = ROOT / "INTERVIEWER.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for fragment in sorted(REQUIRED_CONTRACT_TEXT):
        if fragment not in text:
            errors.append(f"INTERVIEWER.md missing required text: {fragment}")


def check_adapters(errors: list[str]) -> None:
    for relative, fragment in ADAPTER_REFERENCES.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if fragment not in text:
            errors.append(f"{relative} does not reference the canonical contract")
        if relative not in {"AGENTS.md", "llms.txt"} and len(text) > 2_000:
            errors.append(f"{relative} is too large; keep provider adapters thin")


def check_local_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} links outside repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {target}")


def check_example_turns(errors: list[str]) -> None:
    path = ROOT / "examples/ai-first-session.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"\*\*AI interviewer(?: internal state)?\*\*", text)[1:]
    for index, block in enumerate(blocks, start=1):
        response = re.split(r"\n\*\*(?:Narrator|AI interviewer)", block, maxsplit=1)[0]
        if "internal state" in block[:80].lower():
            continue
        question_count = response.count("?")
        if question_count > 1:
            errors.append(
                f"examples/ai-first-session.md AI turn {index} has "
                f"{question_count} question marks"
            )


def check_private_defaults(errors: list[str]) -> None:
    ignore = ROOT / ".gitignore"
    if not ignore.exists():
        errors.append("missing .gitignore privacy defaults")
        return
    text = ignore.read_text(encoding="utf-8")
    for pattern in ("private/", "sessions/", "*.session-state.md", "*.transcript.md"):
        if pattern not in text:
            errors.append(f".gitignore missing narrator-data pattern: {pattern}")


def main() -> int:
    errors: list[str] = []
    check_files(errors)
    check_contract(errors)
    check_adapters(errors)
    check_local_links(errors)
    check_example_turns(errors)
    check_private_defaults(errors)

    if errors:
        print("Kith AI contract checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Kith AI contract checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
