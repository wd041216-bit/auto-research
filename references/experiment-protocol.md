# Experiment Protocol

## Purpose

Design and record experiments, analyses, case studies, or theoretical checks before using results as evidence.

## Required Inputs

- `03_contribution/contribution-plan.md`
- Relevant literature matrix entries
- Available code, data, benchmarks, models, or analysis materials

## Required Outputs

- `04_experiments/experiment-plan.md`
- `04_experiments/results-ledger.md`

## Procedure

1. State the hypothesis or analysis question.
2. Define independent variables, dependent variables, controls, baselines, and metrics.
3. Name datasets, tasks, prompts, model versions, hardware, seeds, and evaluation scripts when applicable.
4. Define ablations and failure cases before seeing final results.
5. Record expected limitations and invalidation criteria.
6. Execute the smallest meaningful check first.
7. Log every result in the results ledger with date, artifact link, metric, and interpretation.
8. Record negative and inconclusive results.
9. Do not rewrite the original hypothesis to fit observed results. Add a new follow-up hypothesis instead.

## Process Constraints

- Freeze hypotheses, metrics, baselines, controls, and invalidation criteria before interpreting results.
- Record model versions, prompt versions, datasets, seeds, hardware, scripts, and manual steps when they affect reproducibility.
- A result without an artifact path or explicit evidence location cannot support a final claim.
- Negative, failed, and inconclusive runs must stay in the ledger when they affect interpretation or limitations.
- Exploratory findings require new follow-up hypotheses rather than retroactive edits to the original plan.

## Blocking Gates

- Empirical claims require a prior experiment plan.
- Result entries require artifact links or a clear explanation of where evidence lives.
- Claims of improvement require a baseline.
- Claims of robustness require ablations, stress tests, or explicit scope limits.

## Common Failure Modes

- Treating a demo as an experiment.
- Choosing metrics after seeing results.
- Hiding negative results.
- Reporting percentage gains without denominators or baselines.
- Using model-generated estimates as empirical measurements.
