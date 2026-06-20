# Proposal Output Contract

## Purpose

Define the proposal dossier shape for converged and checkpointed council runs.

## Required Inputs

- Council brief
- Debate log
- Proposal scorecard
- Literature or frontier notes
- Candidate experiment plan

## Required Outputs

- `03_contribution/proposal-dossier.md`

## Procedure

Write a concise dossier with these sections:

1. Thesis
2. Executive Decision
3. Frontier Map
4. Council Composition
5. Idea Portfolio
6. Selected Proposal
7. Related-Work Contrast
8. Experiment Plan
9. Venue Positioning
10. Risk Register
11. 30/60/90 Day Plan
12. Kill Criteria
13. Continuation State

Use this thesis form:

```text
We propose <method/system/study> to solve <bottleneck> by <mechanism>, evaluated through <evidence plan>, targeting <venue/community>.
```

## Blocking Gates

- A final dossier requires `Convergence status: converged`.
- A checkpoint dossier must say `Convergence status: checkpoint` and include continuation state.
- Do not fabricate related-work rows. Mark unverified sources as `to verify`.
- Do not omit open vetoes, risks, or kill criteria.

## Common Failure Modes

- Dumping raw debate instead of a decision-ready dossier.
- Hiding objections to make the idea look stronger.
- Naming top venues without reviewer expectation analysis.
- Writing a final proposal when the council is still checkpointed.

