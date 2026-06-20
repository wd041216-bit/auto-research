#!/usr/bin/env python3
"""Audit an auto-research literature matrix."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_COLUMNS = [
    "paper_id",
    "title",
    "authors",
    "year",
    "venue",
    "source_type",
    "doi",
    "arxiv_id",
    "url",
    "search_query",
    "retrieved_date",
    "relevance_score",
    "authority_score",
    "recency_score",
    "method_fit_score",
    "centrality_score",
    "lqs_total",
    "triage_category",
    "summary",
    "relevance_rationale",
    "venue_verified",
    "metadata_status",
    "notes",
]

SCORE_COLUMNS = [
    "relevance_score",
    "authority_score",
    "recency_score",
    "method_fit_score",
    "centrality_score",
]

VALID_CATEGORIES = {"must-cite", "deep-discuss", "supporting", "background", "exclude"}
VALID_METADATA = {"verified", "uncertain", "needs-check"}
VALID_VERIFIED = {"true", "false", "uncertain"}


def resolve_path(path: Path) -> Path:
    path = path.expanduser().resolve()
    if path.is_file():
        return path
    return path / "02_literature" / "literature-matrix.csv"


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = [
            {key: (value or "").strip() for key, value in row.items()}
            for row in reader
            if any((value or "").strip() for value in row.values())
        ]
        return list(reader.fieldnames or []), rows


def parse_score(value: str, maximum: float = 5.0) -> float | None:
    try:
        score = float(value)
    except ValueError:
        return None
    if score < 0 or score > maximum:
        return None
    return score


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace_or_csv", type=Path)
    args = parser.parse_args()

    path = resolve_path(args.workspace_or_csv)
    blocking: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        print(f"BLOCKING: literature matrix missing: {path}")
        return 1

    columns, rows = read_rows(path)
    missing = [column for column in REQUIRED_COLUMNS if column not in columns]
    if missing:
        blocking.append(f"missing required columns: {', '.join(missing)}")

    if not rows:
        blocking.append("literature matrix has no paper rows")

    seen_ids: set[str] = set()
    for index, row in enumerate(rows, start=2):
        paper_id = row.get("paper_id", "")
        label = paper_id or f"row {index}"

        if not paper_id:
            blocking.append(f"row {index}: missing paper_id")
        elif paper_id in seen_ids:
            blocking.append(f"row {index}: duplicate paper_id {paper_id}")
        seen_ids.add(paper_id)

        for field in ("title", "authors", "year", "source_type", "search_query", "retrieved_date"):
            if not row.get(field):
                blocking.append(f"{label}: missing {field}")

        category = row.get("triage_category", "")
        if category not in VALID_CATEGORIES:
            blocking.append(f"{label}: invalid triage_category {category!r}")

        scores: list[float] = []
        for field in SCORE_COLUMNS:
            parsed = parse_score(row.get(field, ""))
            if parsed is None:
                blocking.append(f"{label}: invalid {field}; expected number from 0 to 5")
            else:
                scores.append(parsed)

        total = parse_score(row.get("lqs_total", ""), maximum=25.0)
        if total is None:
            blocking.append(f"{label}: invalid lqs_total; expected number from 0 to 25")
        elif scores and abs(total - sum(scores)) > 0.25:
            warnings.append(f"{label}: lqs_total differs from score sum")

        if category in {"must-cite", "deep-discuss"}:
            if not row.get("summary"):
                blocking.append(f"{label}: {category} entry missing summary")
            if not row.get("relevance_rationale"):
                blocking.append(f"{label}: {category} entry missing relevance_rationale")

        if not (row.get("doi") or row.get("arxiv_id") or row.get("url")):
            warnings.append(f"{label}: missing DOI, arXiv ID, and URL")

        if not row.get("venue"):
            warnings.append(f"{label}: missing venue")

        if row.get("metadata_status") and row["metadata_status"] not in VALID_METADATA:
            warnings.append(f"{label}: unusual metadata_status {row['metadata_status']!r}")

        if row.get("venue_verified") and row["venue_verified"] not in VALID_VERIFIED:
            warnings.append(f"{label}: unusual venue_verified {row['venue_verified']!r}")

    for item in blocking:
        print(f"BLOCKING: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    if blocking:
        return 1
    print(f"Literature matrix audit passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
