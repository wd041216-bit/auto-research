# Artifact Schemas

## Purpose

Define exact fields and minimum completeness standards for all workspace artifacts.

## Required Inputs

- Research workspace
- Mode

## Required Outputs

- Schema-compliant Markdown, CSV, LaTeX, and BibTeX artifacts

## Procedure

Use these fields exactly for CSV files and these headings for Markdown templates. Validators depend on stable names.

Apply the status model and evidence ID rules in `process-constraints.md`. Schema compliance means both the fields exist and their values are specific enough to support downstream gates.

## Artifact State Constraints

- `Status: not-started` is allowed only in untouched templates.
- `Status: draft` means the artifact has content but cannot support final claims.
- `Status: provisional` means the artifact may guide planning but has unresolved gates.
- `Status: complete` means required fields are filled, evidence links are resolvable, and available validators have passed.
- `Status: blocked` means the artifact must name the blocker and next required action.
- `Status: superseded` means the artifact remains for audit history but should not be used as current evidence.

Do not mark an artifact complete because it is well-written. Mark it complete only when its required fields and evidence constraints are satisfied.

## CSV Schemas

`02_literature/literature-matrix.csv`:

```text
paper_id,title,authors,year,venue,source_type,doi,arxiv_id,url,search_query,retrieved_date,relevance_score,authority_score,recency_score,method_fit_score,centrality_score,lqs_total,triage_category,summary,relevance_rationale,venue_verified,metadata_status,notes
```

`05_claims/claims-evidence.csv`:

```text
claim_id,claim_text,claim_type,evidence_ids,evidence_strength,source_artifacts,section_targets,status,wording_risk,notes
```

CSV constraints:

- IDs must be stable and unique within the file.
- Empty rows are ignored by validators but should not be used as placeholders for future evidence.
- `evidence_ids` may contain multiple IDs separated by semicolons or commas, but each ID must be findable in a source artifact.
- Scores must use numeric values in the documented range, not words such as high or medium.
- Uncertain metadata must use explicit uncertainty fields rather than invented values.

## Markdown Schemas

Every required Markdown artifact must include:

- `Status: complete` when the artifact is ready to support gates
- Purpose
- Inputs
- Content
- Evidence links or artifact links
- Open issues

Markdown constraints:

- Each required heading must contain concrete content or an explicit blocker.
- Open issues must not hide blockers; blockers belong in status, gate reports, or review concerns.
- Provisional artifacts must say what would make them complete.
- Complete artifacts must not retain template-only placeholders as their only content.

## Council Artifact Schemas

`00_intake/council-brief.md` must include research direction, research object, fields and adjacent fields, target artifact, venue ambition, constraints, available assets, risk tolerance, and material unknowns.

`03_contribution/proposal-dossier.md` must include `Convergence status: converged|checkpoint|blocked|killed`, thesis, executive decision, frontier map, council composition, idea portfolio, selected proposal, related-work contrast, experiment plan, venue positioning, risk register, 30/60/90 day plan, kill criteria, and continuation state when not converged.

`03_contribution/council-debate-log.md` must include roles, votes, vetoes, adaptive moves, open objections, and final chair decision. Use `Blocking veto: unresolved` or `Veto status: unresolved` only when a veto remains open.

`03_contribution/proposal-scorecard.md` must include eight axis scores, total score, classification, caps applied, and gap-fill actions.

## Results Ledger Fields

Each result entry must include result ID, date, plan reference, artifact path, metric, value, comparison, interpretation, and limitations.

Each result ID cited as `result:<id>` must appear in the results ledger. Result entries should preserve negative, failed, and inconclusive outcomes when they affect claims or limitations.

## Review And Revision Fields

Each review concern needs concern ID, reviewer persona, severity, target artifact, and required action.

Each revision entry needs revision ID, linked concern ID, changed artifact, summary, verification, and closure status.

Review and revision constraints:

- A blocking concern cannot be closed without a linked revision, downgrade, or documented rejection rationale.
- Revision verification must name the artifact, validator, test, or review evidence used for closure.
- Submission readiness requires all blocking review concerns to be closed or explicitly downgraded with rationale.

## Blocking Gates

- Missing CSV columns block validators.
- Duplicate IDs block validators.
- Missing status markers block completion.
- Artifact links that cannot be located block submission readiness.
- A converged proposal dossier with an unresolved veto blocks council convergence.
- A checkpoint dossier without continuation state blocks proposal packaging.

## Common Failure Modes

- Renaming columns for readability and breaking scripts.
- Writing prose where structured IDs are required.
- Leaving artifacts complete in prose but not marked complete.
- Omitting convergence status from a proposal dossier.
