#!/usr/bin/env python3
"""Initialize an auto-research workspace from the bundled template."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


MODES = ("survey", "original", "hybrid", "iteration")


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_template(template: Path, output: Path, force: bool) -> None:
    if output.exists():
        if any(output.iterdir()) and not force:
            raise SystemExit(f"BLOCKING: output exists and is not empty: {output}")
        if force:
            shutil.rmtree(output)
    shutil.copytree(template, output)


def artifact_paths(output: Path) -> dict[str, str]:
    return {
        "research_brief": "00_intake/research-brief.md",
        "council_brief": "00_intake/council-brief.md",
        "research_questions": "01_questions/research-questions.md",
        "literature_search_log": "02_literature/literature-search-log.md",
        "literature_matrix": "02_literature/literature-matrix.csv",
        "contribution_plan": "03_contribution/contribution-plan.md",
        "proposal_dossier": "03_contribution/proposal-dossier.md",
        "council_debate_log": "03_contribution/council-debate-log.md",
        "proposal_scorecard": "03_contribution/proposal-scorecard.md",
        "experiment_plan": "04_experiments/experiment-plan.md",
        "results_ledger": "04_experiments/results-ledger.md",
        "claims_evidence": "05_claims/claims-evidence.csv",
        "paper": "06_paper/paper.tex",
        "refs": "06_paper/refs.bib",
        "review_memo": "07_review/review-memo.md",
        "review_packet": "07_review/review-packet.md",
        "revision_plan": "08_revision/revision-plan.md",
        "revision_ledger": "08_revision/revision-ledger.md",
        "submission_checklist": "09_submission/submission-checklist.md",
        "limitations": "09_submission/limitations.md",
        "reproducibility_statement": "09_submission/reproducibility-statement.md",
    }


def write_manifest(output: Path, mode: str, title: str) -> None:
    manifest = {
        "schema": "auto-research-workspace-v1",
        "mode": mode,
        "title": title,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": artifact_paths(output),
    }
    (output / "auto-research-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=MODES)
    parser.add_argument("--title", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    template = skill_root() / "assets" / "research-workspace"
    if not template.exists():
        raise SystemExit(f"BLOCKING: template not found: {template}")

    output = args.output.expanduser().resolve()
    copy_template(template, output, args.force)
    write_manifest(output, args.mode, args.title)
    print(f"Initialized auto-research workspace: {output}")
    print(f"Mode: {args.mode}")
    print(f"Title: {args.title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
