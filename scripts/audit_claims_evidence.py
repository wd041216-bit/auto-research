#!/usr/bin/env python3
"""Audit an auto-research claims-evidence table."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REQUIRED_COLUMNS = [
    "claim_id",
    "claim_text",
    "claim_type",
    "evidence_ids",
    "evidence_strength",
    "source_artifacts",
    "section_targets",
    "status",
    "wording_risk",
    "notes",
]

VALID_TYPES = {
    "empirical",
    "literature-backed",
    "theoretical",
    "conjecture",
    "engineering",
    "negative-result",
}

VALID_STRENGTH = {"weak", "moderate", "strong", "verified"}
STRONG_WORDS = re.compile(
    r"\b(prove|guarantee|state-of-the-art|outperform|best|novel|significant|robust|causal)\b",
    re.IGNORECASE,
)


def resolve_path(path: Path) -> Path:
    path = path.expanduser().resolve()
    if path.is_file():
        return path
    return path / "05_claims" / "claims-evidence.csv"


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = [
            {key: (value or "").strip() for key, value in row.items()}
            for row in reader
            if any((value or "").strip() for value in row.values())
        ]
        return list(reader.fieldnames or []), rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace_or_csv", type=Path)
    args = parser.parse_args()

    path = resolve_path(args.workspace_or_csv)
    blocking: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        print(f"BLOCKING: claims-evidence file missing: {path}")
        return 1

    columns, rows = read_rows(path)
    missing = [column for column in REQUIRED_COLUMNS if column not in columns]
    if missing:
        blocking.append(f"missing required columns: {', '.join(missing)}")

    if not rows:
        blocking.append("claims-evidence table has no claim rows")

    seen_ids: set[str] = set()
    for index, row in enumerate(rows, start=2):
        claim_id = row.get("claim_id", "")
        claim_type = row.get("claim_type", "")
        evidence_ids = row.get("evidence_ids", "")
        strength = row.get("evidence_strength", "")
        text = row.get("claim_text", "")

        if not claim_id:
            blocking.append(f"row {index}: missing claim_id")
        elif claim_id in seen_ids:
            blocking.append(f"row {index}: duplicate claim_id {claim_id}")
        seen_ids.add(claim_id)

        if claim_type not in VALID_TYPES:
            blocking.append(f"{claim_id or f'row {index}'}: invalid claim_type {claim_type!r}")

        if strength not in VALID_STRENGTH:
            blocking.append(f"{claim_id or f'row {index}'}: invalid evidence_strength {strength!r}")

        if claim_type != "conjecture" and not evidence_ids:
            blocking.append(f"{claim_id}: non-conjecture claim lacks evidence_ids")

        if claim_type == "empirical" and "result:" not in evidence_ids:
            blocking.append(f"{claim_id}: empirical claim must reference result: IDs")

        if claim_type == "negative-result" and "result:" not in evidence_ids:
            blocking.append(f"{claim_id}: negative-result claim must reference result: IDs")

        if claim_type == "literature-backed" and "lit:" not in evidence_ids:
            blocking.append(f"{claim_id}: literature-backed claim must reference lit: IDs")

        if STRONG_WORDS.search(text) and strength not in {"strong", "verified"}:
            warnings.append(f"{claim_id}: strong wording with evidence_strength={strength}")

    for item in blocking:
        print(f"BLOCKING: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    if blocking:
        return 1
    print(f"Claims-evidence audit passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

