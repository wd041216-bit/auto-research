# Submission Package

## Purpose

Define what must exist before a research package can be called submission-ready.

## Required Inputs

- Paper package
- Claims-evidence table
- Literature matrix
- Review and revision artifacts
- Reproducibility and limitations artifacts

## Required Outputs

- `09_submission/submission-checklist.md`
- `09_submission/limitations.md`
- `09_submission/reproducibility-statement.md`

## Procedure

1. Confirm paper, references, figures, tables, appendix, and supplementary artifacts exist.
2. Confirm every major claim maps to evidence.
3. Confirm limitations are explicit and match evidence weaknesses.
4. Confirm reproducibility statement lists code, data, environment, seeds, prompts, and unavailable assets.
5. Confirm review concerns are closed or explicitly deferred.
6. Mark submission checklist complete only after validators pass.

## Process Constraints

- Submission-ready means gates passed, not that the draft is polished.
- Deferred review concerns must be nonblocking or accompanied by an explicit downgrade.
- Limitations must cover evidence, scope, external validity, unavailable assets, and known negative results.
- Reproducibility must name code, data, environment, seeds, prompts, manual steps, and unavailable components.
- Venue compliance may be claimed only after target venue requirements are checked.

## Blocking Gates

- Missing claims-evidence table.
- Missing review and revision closure.
- Missing limitations.
- Missing reproducibility statement for empirical, engineering, or dataset work.
- Any blocking validator failure.

## Common Failure Modes

- Calling a polished draft submission-ready.
- Omitting limitations to sound stronger.
- Leaving supplemental material implied but not packaged.
