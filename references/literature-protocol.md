# Literature Protocol

## Purpose

Make literature search auditable, fresh, and useful for writing rather than a citation dump.

## Required Inputs

- `00_intake/research-brief.md`
- `01_questions/research-questions.md`
- Search sources available to the agent

## Required Outputs

- `02_literature/literature-search-log.md`
- `02_literature/literature-matrix.csv`

## Procedure

1. Derive at least five query families: core concepts, method terms, task/dataset terms, failure modes, and recent venue terms.
2. Search multiple source types when available: arXiv, Semantic Scholar, Google Scholar, DBLP, publisher pages, conference proceedings, project pages, and citation graphs.
3. Record query, source, date, result count, inclusion rationale, and exclusions in the search log.
4. Add candidate papers to the literature matrix with stable `paper_id` values.
5. Score each paper from 0-5 on relevance, authority, recency, methodological fit, and centrality.
6. Compute `lqs_total` as the sum of those five scores.
7. Assign one triage category: `must-cite`, `deep-discuss`, `supporting`, `background`, or `exclude`.
8. For `must-cite` and `deep-discuss`, write a summary and relevance rationale.
9. Verify venue metadata for central papers. Mark uncertainty instead of inventing accepted venues.

## Process Constraints

- Search breadth must cover concept, method, task or dataset, failure mode, and recent venue query families unless the brief makes a family irrelevant.
- Every included paper must be traceable to a query, citation-chasing pass, supplied source, or user-provided corpus.
- Central papers require source metadata; uncertain metadata must be marked, not guessed.
- Exclusions must be recorded when they affect scope, novelty, or venue claims.
- Literature triage supports related work and novelty framing; it does not substitute for experiments.

## Literature Quality Score

| Field | Meaning |
| --- | --- |
| `relevance_score` | Directness to the research question |
| `authority_score` | Venue, authorship, adoption, or benchmark centrality |
| `recency_score` | Freshness relative to the field |
| `method_fit_score` | Match to methods, tasks, or evaluation style |
| `centrality_score` | Importance in citation graph or community discourse |

## Blocking Gates

- A literature matrix with only headers does not satisfy triage.
- `must-cite` and `deep-discuss` entries without summaries block related work.
- Missing query/source/date in the search log blocks claims of literature coverage.
- Fabricated metadata blocks all citation use.

## Common Failure Modes

- Searching one query and treating it as coverage.
- Adding citations without explaining why they matter.
- Keeping outdated arXiv metadata when a paper has an accepted venue.
- Omitting negative or contrary literature.
