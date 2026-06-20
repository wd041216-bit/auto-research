#!/usr/bin/env python3
"""Build an auto-research review packet from current artifacts."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path


ARTIFACTS = [
    ("Research Brief", "00_intake/research-brief.md"),
    ("Council Brief", "00_intake/council-brief.md"),
    ("Research Questions", "01_questions/research-questions.md"),
    ("Literature Search Log", "02_literature/literature-search-log.md"),
    ("Contribution Plan", "03_contribution/contribution-plan.md"),
    ("Proposal Dossier", "03_contribution/proposal-dossier.md"),
    ("Council Debate Log", "03_contribution/council-debate-log.md"),
    ("Proposal Scorecard", "03_contribution/proposal-scorecard.md"),
    ("Experiment Plan", "04_experiments/experiment-plan.md"),
    ("Results Ledger", "04_experiments/results-ledger.md"),
    ("Paper Draft", "06_paper/paper.tex"),
    ("Limitations", "09_submission/limitations.md"),
    ("Reproducibility Statement", "09_submission/reproducibility-statement.md"),
]


def read_limited(path: Path, limit: int = 1800) -> tuple[str, bool]:
    if not path.exists():
        return "Unavailable.", False
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    if not text:
        return "Empty.", False
    if len(text) > limit:
        return text[:limit].rstrip() + "\n\n[truncated]", True
    return text, True


def count_csv_rows(path: Path) -> tuple[int, list[str]]:
    if not path.exists():
        return 0, []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = [row for row in reader if any((value or "").strip() for value in row.values())]
        return len(rows), list(reader.fieldnames or [])


def build_packet(workspace: Path) -> str:
    lit_rows, lit_columns = count_csv_rows(workspace / "02_literature" / "literature-matrix.csv")
    claim_rows, claim_columns = count_csv_rows(workspace / "05_claims" / "claims-evidence.csv")
    warnings: list[str] = []

    if lit_rows == 0:
        warnings.append("Literature matrix has no paper rows.")
    if claim_rows == 0:
        warnings.append("Claims-evidence table has no claim rows.")

    lines = [
        "# Review Packet",
        "",
        "Status: complete",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Workspace: {workspace}",
        "",
        "## Evidence Summary",
        "",
        f"- Literature rows: {lit_rows}",
        f"- Literature columns: {', '.join(lit_columns) if lit_columns else 'unavailable'}",
        f"- Claim rows: {claim_rows}",
        f"- Claim columns: {', '.join(claim_columns) if claim_columns else 'unavailable'}",
        "",
        "## Missing-Evidence Warnings",
        "",
    ]

    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- No packet-level missing-evidence warnings.")

    for title, relative in ARTIFACTS:
        path = workspace / relative
        text, available = read_limited(path)
        lines.extend(
            [
                "",
                f"## {title}",
                "",
                f"Artifact: `{relative}`",
                f"Available: {'yes' if available else 'no'}",
                "",
                "```text",
                text,
                "```",
            ]
        )

    lines.extend(
        [
            "",
            "## Reviewer Instructions",
            "",
            "Assess novelty, correctness, evidence, clarity, positioning, and reproducibility.",
            "Treat missing evidence as a blocking concern rather than filling gaps by inference.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    args = parser.parse_args()

    workspace = args.workspace.expanduser().resolve()
    if not workspace.exists():
        print(f"BLOCKING: workspace does not exist: {workspace}")
        return 1

    output = workspace / "07_review" / "review-packet.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_packet(workspace), encoding="utf-8")
    print(f"Review packet written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
