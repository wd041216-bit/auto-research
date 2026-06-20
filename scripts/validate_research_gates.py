#!/usr/bin/env python3
"""Validate auto-research workspace evidence gates."""

from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path


MODES = ("survey", "original", "hybrid", "iteration")

COMMON_REQUIRED = [
    "00_intake/research-brief.md",
    "01_questions/research-questions.md",
    "02_literature/literature-search-log.md",
    "02_literature/literature-matrix.csv",
    "03_contribution/contribution-plan.md",
    "05_claims/claims-evidence.csv",
    "06_paper/paper.tex",
    "06_paper/refs.bib",
    "07_review/review-memo.md",
    "08_revision/revision-plan.md",
    "08_revision/revision-ledger.md",
    "09_submission/submission-checklist.md",
    "09_submission/limitations.md",
    "09_submission/reproducibility-statement.md",
]

EXPERIMENT_REQUIRED = [
    "04_experiments/experiment-plan.md",
    "04_experiments/results-ledger.md",
]

COUNCIL_REQUIRED = [
    "00_intake/council-brief.md",
    "03_contribution/proposal-dossier.md",
    "03_contribution/council-debate-log.md",
    "03_contribution/proposal-scorecard.md",
]


def script_dir() -> Path:
    return Path(__file__).resolve().parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def is_complete_text(path: Path) -> bool:
    text = read_text(path)
    if "Status: not-started" in text:
        return False
    if path.suffix in {".md", ".tex", ".bib"}:
        return "Status: complete" in text
    return bool(text.strip())


def check_required_files(workspace: Path, mode: str) -> tuple[list[str], list[str]]:
    blocking: list[str] = []
    warnings: list[str] = []
    required = list(COMMON_REQUIRED)
    if mode in {"original", "hybrid"}:
        required.extend(EXPERIMENT_REQUIRED)

    for relative in required:
        path = workspace / relative
        if not path.exists():
            blocking.append(f"missing required artifact: {relative}")
            continue
        if path.is_file() and path.suffix == ".csv":
            if not read_text(path).strip():
                blocking.append(f"empty CSV artifact: {relative}")
            continue
        if path.is_file() and not is_complete_text(path):
            blocking.append(f"artifact is not complete: {relative}")

    for relative in ["06_paper/figures", "06_paper/tables", "06_paper/appendix"]:
        if not (workspace / relative).exists():
            warnings.append(f"missing optional paper directory: {relative}")

    return blocking, warnings


def council_artifacts_exist(workspace: Path) -> bool:
    return any((workspace / relative).exists() for relative in COUNCIL_REQUIRED)


def convergence_status(text: str) -> str | None:
    for line in text.splitlines():
        if line.lower().startswith("convergence status:"):
            return line.split(":", 1)[1].strip().lower()
    return None


def check_council_files(workspace: Path, mode: str) -> tuple[list[str], list[str]]:
    blocking: list[str] = []
    warnings: list[str] = []

    if mode == "survey" or not council_artifacts_exist(workspace):
        return blocking, warnings

    initial_failure_count = len(blocking)
    for relative in COUNCIL_REQUIRED:
        path = workspace / relative
        if not path.exists():
            blocking.append(f"missing required council artifact: {relative}")
            continue
        if path.is_file() and not is_complete_text(path):
            blocking.append(f"artifact is not complete: {relative}")

    if len(blocking) > initial_failure_count:
        return blocking, warnings

    dossier_path = workspace / "03_contribution" / "proposal-dossier.md"
    debate_path = workspace / "03_contribution" / "council-debate-log.md"
    contribution_path = workspace / "03_contribution" / "contribution-plan.md"

    if not dossier_path.exists():
        return blocking, warnings

    dossier_text = read_text(dossier_path)
    status = convergence_status(dossier_text)
    if status is None:
        blocking.append("proposal-dossier.md missing Convergence status")
        return blocking, warnings

    if status == "converged":
        if debate_path.exists():
            debate_text = read_text(debate_path)
            unresolved_markers = ("Blocking veto: unresolved", "Veto status: unresolved")
            if any(marker in debate_text for marker in unresolved_markers):
                blocking.append("converged proposal has unresolved council veto")
    elif status == "checkpoint":
        contribution_text = read_text(contribution_path) if contribution_path.exists() else ""
        if "Provisional: yes" not in contribution_text:
            warnings.append("checkpoint proposal should keep contribution plan provisional with `Provisional: yes`")
    elif status in {"blocked", "killed"}:
        blocking.append(f"proposal dossier convergence status is {status}")
    else:
        blocking.append(f"invalid proposal dossier Convergence status: {status}")

    return blocking, warnings


def run_subcheck(name: str, workspace: Path) -> int:
    script = script_dir() / name
    old_argv = sys.argv[:]
    sys.argv = [str(script), str(workspace)]
    try:
        runpy.run_path(str(script), run_name="__main__")
    except SystemExit as exc:
        code = exc.code
        if code is None:
            return 0
        if isinstance(code, int):
            return code
        return 1
    finally:
        sys.argv = old_argv
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--mode", choices=MODES, default=None)
    args = parser.parse_args()

    workspace = args.workspace.expanduser().resolve()
    mode = args.mode or "hybrid"
    if not workspace.exists():
        print(f"BLOCKING: workspace does not exist: {workspace}")
        return 1

    blocking, warnings = check_required_files(workspace, mode)
    council_blocking, council_warnings = check_council_files(workspace, mode)
    blocking.extend(council_blocking)
    warnings.extend(council_warnings)
    for item in blocking:
        print(f"BLOCKING: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    subcheck_failed = False
    for script in ("check_literature_matrix.py", "audit_claims_evidence.py"):
        if run_subcheck(script, workspace) != 0:
            subcheck_failed = True

    if blocking or subcheck_failed:
        return 1

    print(f"Research gates passed for mode={mode}: {workspace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
