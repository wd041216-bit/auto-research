---
name: auto-research
description: Use when conducting academic or technical research, creating survey papers, developing original research contributions, planning experiments, writing papers, building paper packages, simulating peer review, revising manuscripts, or iterating research projects toward publication-quality artifacts.
---

# Auto Research

## Overview

Use this skill to run disciplined research-to-paper workflows. It turns a research direction, draft, repo, or review memo into evidence-tracked artifacts: literature matrix, contribution plan, experiment plan, claims-evidence map, paper package, review memo, and revision ledger.

Core rule: no final research claim without traceable evidence.

## Start Every Run

1. Decide whether the Proposal / Council Gate applies before choosing or refining a research direction.
2. Identify the mode: `survey`, `original`, `hybrid`, or `iteration`.
3. Locate or create a research workspace. To create one, run `scripts/init_research_workspace.py`.
4. Read `references/research-lifecycle.md` before choosing stage order.
5. Read `references/process-constraints.md` for the current stage and cross-stage process constraints.
6. Read the reference file for the current stage before writing artifacts.
7. Run the relevant validator before claiming a gate is satisfied.
8. Mark incomplete outputs as provisional; do not use final-paper confidence language before gates pass.

## Mode Selection

Use `survey` for literature reviews, field maps, taxonomies, and related work.
Use `original` for new methods, experiments, benchmarks, datasets, theory, tools, or empirical findings.
Use `hybrid` when literature review should locate a gap before original contribution work.
Use `iteration` when the user provides a draft, repo, review feedback, or existing research package.

If the mode is ambiguous and different modes require different artifacts, ask one short question. If the context is clear, choose the mode and state it.

## Proposal / Council Gate

Use the Proposal / Council Gate when the user brings a rough scientific or technical idea, original or hybrid research ambition, AI-for-Science direction, interdisciplinary proposal, method hypothesis, top-tier proposal request, or several competing ideas that need selection.

Skip it when the user only wants a survey, a complete brief and contribution plan already exist, the task is a narrow revision of an existing package, or the user explicitly accepts a provisional brainstorm.

When this gate applies:

1. Read `references/brainstorming-protocol.md`.
2. Read `references/research-council-protocol.md`.
3. Use `references/proposal-maturity-rubric.md` for scoring.
4. Package outputs with `references/proposal-output-contract.md`.

A council may end as `converged`, `checkpoint`, `blocked`, or `killed`. Only `converged` permits a final proposal dossier. `checkpoint` artifacts can guide the next research step, but must remain labeled interim.

## Hard Gates

These gates are mandatory:

- No original or hybrid contribution plan from a rough idea until a council checkpoint or converged proposal dossier exists.
- No final proposal dossier until council convergence conditions pass.
- No top-venue, novelty, SOTA, or benchmark-fit claim without current frontier grounding.
- No council convergence while any blocking veto remains unresolved.
- No council output may be used as empirical evidence unless later backed by `04_experiments/experiment-plan.md` and `04_experiments/results-ledger.md`.
- No research direction without `00_intake/research-brief.md`.
- No research question without scope, novelty angle, evidence path, and success criteria.
- No related work or survey taxonomy without `02_literature/literature-matrix.csv` triage.
- No empirical conclusion without a prior `04_experiments/experiment-plan.md` and `04_experiments/results-ledger.md`.
- No abstract, introduction, discussion, or conclusion claim unless it appears in `05_claims/claims-evidence.csv`.
- No submission-ready claim without `07_review/review-memo.md`, `08_revision/revision-plan.md`, `08_revision/revision-ledger.md`, and `09_submission/submission-checklist.md`.
- No stage may advance unless the applicable contract in `references/process-constraints.md` is satisfied or the output is explicitly labeled provisional or blocked.

When a gate is missing, name the missing artifact and offer a provisional output or the next gate-satisfying step.

## Lifecycle

Follow these stages unless `references/research-lifecycle.md` allows a mode-specific skip:

0. Proposal / Council Gate
1. Intake
2. Research Question
3. Literature Recall
4. Literature Triage
5. Contribution Plan
6. Experiment / Analysis
7. Claim-Evidence Mapping
8. Paper Package
9. Peer Review & Revision

For `original` and `hybrid`, stages 6 and 7 are blocking before final paper writing. For `survey`, stage 6 may be omitted only if no empirical or experimental claims are made.

## Reference Routing

Read only the reference files needed for the current stage:

- Direction shaping and option discipline: `references/brainstorming-protocol.md`
- Multi-role proposal council and convergence: `references/research-council-protocol.md`
- Proposal maturity scoring: `references/proposal-maturity-rubric.md`
- Proposal dossier structure: `references/proposal-output-contract.md`
- Lifecycle and mode control: `references/research-lifecycle.md`
- Stage contracts, process constraints, evidence ID rules, status model, and downgrade rules: `references/process-constraints.md`
- Literature search, recall, scoring, triage, citation freshness: `references/literature-protocol.md`
- Experiment design, baselines, metrics, results ledger: `references/experiment-protocol.md`
- Paper structure, wording gates, LaTeX/BibTeX standards: `references/writing-protocol.md`
- Review personas, scoring, revision closure: `references/review-protocol.md`
- Stage gates and downgrade rules: `references/evidence-gates.md`
- Exact artifact fields and file schemas: `references/artifact-schemas.md`
- Scoring rubrics: `references/quality-rubrics.md`
- Source verification and anti-fabrication rules: `references/source-verification.md`
- Submission package contents: `references/submission-package.md`
- Pressure scenarios for validating agent behavior: `references/pressure-tests.md`

## Operational Scripts

Use these scripts from the skill directory:

```bash
python3 scripts/init_research_workspace.py --mode hybrid --title "My Research" --output ./my-research
python3 scripts/validate_research_gates.py ./my-research --mode hybrid
python3 scripts/check_literature_matrix.py ./my-research
python3 scripts/audit_claims_evidence.py ./my-research
python3 scripts/build_review_packet.py ./my-research
```

Script conventions:

- `BLOCKING:` means the gate is not satisfied.
- `WARNING:` means the artifact can exist but needs attention.
- A nonzero exit from a validator means do not claim completion.

## Completion Rules

All modes require:

```text
00_intake/research-brief.md
01_questions/research-questions.md
02_literature/literature-search-log.md
02_literature/literature-matrix.csv
03_contribution/contribution-plan.md
05_claims/claims-evidence.csv
06_paper/paper.tex
06_paper/refs.bib
07_review/review-memo.md
08_revision/revision-plan.md
08_revision/revision-ledger.md
09_submission/submission-checklist.md
09_submission/limitations.md
09_submission/reproducibility-statement.md
```

`original` and `hybrid` also require:

```text
04_experiments/experiment-plan.md
04_experiments/results-ledger.md
```

## Refusal And Downgrade Rules

Refuse or downgrade when asked to:

- invent references, venues, DOIs, arXiv IDs, results, or reviewer outcomes
- hide negative results
- write strong novelty or empirical claims without evidence
- call a draft submission-ready before review and revision closure
- skip claim-evidence mapping for final writing

Use downgraded language such as "preliminary", "suggests", "hypothesis", "appears consistent with", or "requires validation" when evidence is partial.

## Verification Before Completion

Before saying the research package is complete:

1. Run `validate_research_gates.py`.
2. Run `check_literature_matrix.py`.
3. Run `audit_claims_evidence.py`.
4. Run `build_review_packet.py` if review has not been packaged.
5. Verify there are no `Status: not-started` markers in required artifacts.
6. State any remaining warnings explicitly.
