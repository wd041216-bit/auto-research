# Research Council Protocol

## Purpose

Run a multi-role, adversarial, convergence-driven council for rough ideas that need proposal maturation before research execution.

## Required Inputs

- Council brief or research direction
- Frontier map or current literature notes when available
- Candidate venue ambition and constraints

## Required Outputs

- `03_contribution/council-debate-log.md`
- `03_contribution/proposal-scorecard.md`
- `03_contribution/proposal-dossier.md`

## Procedure

1. Form a minimum viable council: chair, domain scientist, methods inventor, data/benchmark specialist, reviewer skeptic, replication engineer, venue strategist, and ethics/safety critic.
2. Assign each role a lens, mandate, veto power, and acceptance criteria.
3. Start with the chair's kickoff brief: direction, frontier map, candidate venues, known gaps, constraints.
4. Use adaptive moves rather than fixed rounds:
   - expand: generate diverse candidates
   - recombine: combine strong partial ideas
   - sharpen: make hypotheses falsifiable and measurable
   - red-team: attack novelty, feasibility, leakage, baselines, ethics, and venue fit
   - advocate-rescue: narrow or reframe promising weak ideas
   - gap-fill: perform targeted literature, evaluation, reproducibility, venue, or risk work
   - add-role: add a missing perspective
   - vote: score candidates and select primary, backup, and optional moonshot
5. The chair chooses exactly one state after each move: `continue-expand`, `continue-recombine`, `continue-sharpen`, `continue-red-team`, `continue-gap-fill`, `add-role`, `converged`, `checkpoint`, `blocked`, or `killed`.
6. Use subagents for independent council groups when available. If not, run a simulated council and mark it in the debate log.

## Convergence Conditions

Declare `converged` only when all are true:

- Proposal reaches `go` under `proposal-maturity-rubric.md`.
- No blocking veto remains.
- Literature and benchmark checks do not reveal a likely near-duplicate.
- At least one serious alternative was tested and rejected with reasons.
- Evaluation names baselines, metrics, ablations, negative controls, and failure criteria.
- Feasibility covers data, compute, timeline, implementation, and reproducibility.
- Venue fit names primary and backup venues plus reviewer standards.
- The thesis can be stated in one sentence without hidden assumptions.

## Blocking Gates

- Any unresolved veto blocks convergence.
- Missing baseline, dataset, metric, or negative control blocks top-tier proposal language.
- Unverified novelty or venue claims block final proposal packaging.
- Ethical, privacy, safety, or scientific-integrity risks block convergence until mitigated or accepted as residual risk.

## Common Failure Modes

- Ending after a fixed number of rounds instead of convergence.
- Letting advocates overrule unresolved reviewer or replication objections.
- Treating Tier C inspiration as evidence.
- Calling a checkpoint a final proposal.

