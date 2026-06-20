# Proposal Maturity Rubric

## Purpose

Score research proposal candidates consistently before they become contribution plans.

## Required Inputs

- Proposal dossier
- Council debate log
- Frontier map or literature notes
- Experiment or evaluation sketch

## Required Outputs

- `03_contribution/proposal-scorecard.md`
- Classification: `go`, `revise`, `redirect`, or `kill`
- Gap-fill actions for weak axes

## Procedure

Score each axis from 0-10:

| Axis | 0-3 | 4-6 | 7-8 | 9-10 |
| --- | --- | --- | --- | --- |
| Novelty | duplicate or obvious | interesting but incremental | clear new mechanism or benchmark | field-framing surprise |
| Significance | low impact | useful but narrow | recognized bottleneck | practice-changing potential |
| Positioning | unclear audience | plausible but weak contrast | clear contribution type | strong venue-reviewer fit |
| Feasibility | unavailable resources | major narrowing needed | practical with milestones | ready with contingencies |
| Evidence Design | no baselines or metrics | partial evaluation | strong baselines and controls | skeptical-reviewer grade |
| Reproducibility | not reproducible | partial protocol | code/data/environment plan | release plan built in |
| Risk And Ethics | major unmitigated risk | shallow mitigation | concrete mitigation | risk handling strengthens work |
| Narrative Clarity | cannot state thesis | understandable but soft | strong story | memorable and reviewer-ready |

Calculate:

```text
total = sum(axis_scores) / 80 * 100
```

Classify:

- `go`: 90+ and no axis below 8
- `revise`: 75-89 or one to two axes below 8
- `redirect`: below 75 or feasibility below 6
- `kill`: near-duplicate, impossible evidence, or unacceptable risk

## Blocking Gates

- If literature search is incomplete, cap novelty and positioning at 7.
- If evaluation is incomplete, cap top-venue readiness at 85.
- If feasibility is below 6, do not recommend flagship submission as the next step.
- For any axis below 8, write a concrete gap-fill action.

## Common Failure Modes

- Rewarding buzzwords.
- Scoring narrative polish as evidence.
- Giving 9 or 10 without concrete supporting artifacts.
- Ignoring feasibility because the idea is exciting.

