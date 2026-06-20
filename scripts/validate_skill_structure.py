#!/usr/bin/env python3
"""Validate the public Auto Research skill repository structure."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_ROOT_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "agents/openai.yaml",
]

REQUIRED_REFERENCES = [
    "artifact-schemas.md",
    "brainstorming-protocol.md",
    "evidence-gates.md",
    "experiment-protocol.md",
    "literature-protocol.md",
    "pressure-tests.md",
    "proposal-maturity-rubric.md",
    "proposal-output-contract.md",
    "quality-rubrics.md",
    "research-council-protocol.md",
    "research-lifecycle.md",
    "review-protocol.md",
    "source-verification.md",
    "submission-package.md",
    "writing-protocol.md",
]

REQUIRED_TEMPLATE_FILES = [
    "00_intake/research-brief.md",
    "00_intake/council-brief.md",
    "01_questions/research-questions.md",
    "02_literature/literature-search-log.md",
    "02_literature/literature-matrix.csv",
    "03_contribution/contribution-plan.md",
    "03_contribution/proposal-dossier.md",
    "03_contribution/council-debate-log.md",
    "03_contribution/proposal-scorecard.md",
    "04_experiments/experiment-plan.md",
    "04_experiments/results-ledger.md",
    "05_claims/claims-evidence.csv",
    "06_paper/paper.tex",
    "06_paper/refs.bib",
    "07_review/review-memo.md",
    "07_review/review-packet.md",
    "08_revision/revision-plan.md",
    "08_revision/revision-ledger.md",
    "09_submission/submission-checklist.md",
    "09_submission/limitations.md",
    "09_submission/reproducibility-statement.md",
]


def fail(message: str) -> None:
    print(f"BLOCKING: {message}")


def parse_frontmatter(skill_text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, flags=re.DOTALL)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", type=Path)
    args = parser.parse_args()

    repo = args.repo.expanduser().resolve()
    blocking: list[str] = []

    for relative in REQUIRED_ROOT_FILES:
        if not (repo / relative).exists():
            blocking.append(f"missing root file: {relative}")

    skill_path = repo / "SKILL.md"
    if skill_path.exists():
        skill_text = skill_path.read_text(encoding="utf-8")
        fields = parse_frontmatter(skill_text)
        if fields.get("name") != "auto-research":
            blocking.append("SKILL.md frontmatter must include name: auto-research")
        if not fields.get("description", "").startswith("Use when"):
            blocking.append("SKILL.md description must start with 'Use when'")
        for reference in REQUIRED_REFERENCES:
            if reference not in skill_text:
                blocking.append(f"SKILL.md does not route reference: {reference}")

    for reference in REQUIRED_REFERENCES:
        path = repo / "references" / reference
        if not path.exists():
            blocking.append(f"missing reference: references/{reference}")
        elif len(path.read_text(encoding="utf-8").strip().split()) < 40:
            blocking.append(f"reference looks too small: references/{reference}")

    for template in REQUIRED_TEMPLATE_FILES:
        path = repo / "assets" / "research-workspace" / template
        if not path.exists():
            blocking.append(f"missing template file: assets/research-workspace/{template}")

    for item in blocking:
        fail(item)

    if blocking:
        return 1
    print(f"Auto Research skill structure is valid: {repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

