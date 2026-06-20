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

## CSV Schemas

`02_literature/literature-matrix.csv`:

```text
paper_id,title,authors,year,venue,source_type,doi,arxiv_id,url,search_query,retrieved_date,relevance_score,authority_score,recency_score,method_fit_score,centrality_score,lqs_total,triage_category,summary,relevance_rationale,venue_verified,metadata_status,notes
```

`05_claims/claims-evidence.csv`:

```text
claim_id,claim_text,claim_type,evidence_ids,evidence_strength,source_artifacts,section_targets,status,wording_risk,notes
```

## Markdown Schemas

Every required Markdown artifact must include:

- `Status: complete` when the artifact is ready to support gates
- Purpose
- Inputs
- Content
- Evidence links or artifact links
- Open issues

## Council Artifact Schemas

`00_intake/council-brief.md` must include research direction, research object, fields and adjacent fields, target artifact, venue ambition, constraints, available assets, risk tolerance, and material unknowns.

`03_contribution/proposal-dossier.md` must include `Convergence status: converged|checkpoint|blocked|killed`, thesis, executive decision, frontier map, council composition, idea portfolio, selected proposal, related-work contrast, experiment plan, venue positioning, risk register, 30/60/90 day plan, kill criteria, and continuation state when not converged.

`03_contribution/council-debate-log.md` must include roles, votes, vetoes, adaptive moves, open objections, and final chair decision. Use `Blocking veto: unresolved` or `Veto status: unresolved` only when a veto remains open.

`03_contribution/proposal-scorecard.md` must include eight axis scores, total score, classification, caps applied, and gap-fill actions.

## Results Ledger Fields

Each result entry must include result ID, date, plan reference, artifact path, metric, value, comparison, interpretation, and limitations.

## Review And Revision Fields

Each review concern needs concern ID, reviewer persona, severity, target artifact, and required action.

Each revision entry needs revision ID, linked concern ID, changed artifact, summary, verification, and closure status.

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
