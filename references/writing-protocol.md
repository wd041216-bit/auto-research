# Writing Protocol

## Purpose

Write papers whose claims are tied to evidence and whose confidence matches artifact quality.

## Required Inputs

- Research brief
- Research questions
- Literature matrix
- Contribution plan
- Claims-evidence table
- Experiment artifacts when empirical claims are present

## Required Outputs

- `06_paper/paper.tex`
- `06_paper/refs.bib`
- Figures, tables, appendix, limitations, and reproducibility statement as needed

## Procedure

1. Choose paper type: survey, original, hybrid, or revision.
2. Build an outline from accepted claims, not from desired rhetoric.
3. Write related work only from triaged literature entries.
4. Write method or analysis sections only from contribution and experiment artifacts.
5. Write abstract and conclusion last, using only claims from `claims-evidence.csv`.
6. Use conservative wording for partial evidence.
7. Keep BibTeX entries traceable to verified source metadata.
8. Every figure and table must have source data, generation notes, or a clear manual provenance statement.

## Recommended Structures

Survey: Abstract, Introduction, Scope, Method for Literature Selection, Taxonomy, Comparative Analysis, Open Problems, Limitations, Conclusion.

Original: Abstract, Introduction, Related Work, Method, Experiments, Results, Discussion, Limitations, Reproducibility, Conclusion.

Hybrid: Abstract, Introduction, Literature Gap Analysis, Proposed Contribution, Experiment or Analysis, Results, Discussion, Limitations, Conclusion.

## Process Constraints

- Build prose from `claims-evidence.csv`; do not backfill the table after writing final sections.
- Keep unsupported but useful ideas in notes, future work, or conjecture language.
- Every central citation in the paper must resolve to a literature matrix row and verified or explicitly uncertain BibTeX metadata.
- Figures and tables require provenance before they can be used as evidence.
- If the evidence changes, revise the claim table before polishing prose.

## Blocking Gates

- No final abstract or conclusion without claim-evidence mapping.
- No novelty claim unless the contribution plan and literature triage support it.
- No empirical conclusion without results ledger entries.
- No citation without a literature matrix entry or verified BibTeX source.

## Common Failure Modes

- Citation dumping without synthesis.
- Overclaiming novelty.
- Treating conjecture as evidence.
- Writing polished prose before evidence is organized.
