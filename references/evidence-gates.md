# Evidence Gates

## Purpose

Define blocking gates, warning gates, and claim downgrade rules for research artifacts.

## Required Inputs

- Workspace artifacts
- Current mode
- Current stage

## Required Outputs

- Gate decision: pass, warning, or blocking
- Missing artifact list
- Required downgrade language when evidence is partial

## Procedure

1. Identify the current mode.
2. Check required artifacts for the current stage and all prior stages.
3. Check whether each artifact is complete rather than just initialized.
4. Match each claim to one claim type.
5. Downgrade unsupported claims or block final writing.

## Claim Types

| Type | Required evidence |
| --- | --- |
| `empirical` | Result ledger entry and experiment plan |
| `literature-backed` | Literature matrix IDs |
| `theoretical` | Argument, proof sketch, or formal derivation artifact |
| `conjecture` | Explicit uncertainty and future validation path |
| `engineering` | Implementation artifact, benchmark, or reproducibility note |
| `negative-result` | Result ledger entry and interpretation |

## Blocking Gates

- Missing required artifact.
- Artifact still marked `Status: not-started`.
- Claim type missing.
- Empirical claim without result evidence.
- Literature-backed claim without literature IDs.
- Submission-ready claim without review and revision closure.
- Original or hybrid contribution plan from a rough idea without a council checkpoint or converged proposal dossier.
- Final proposal dossier without council convergence.
- Top-venue, novelty, SOTA, or benchmark-fit claim without current frontier grounding.
- Council convergence while any blocking veto remains unresolved.

## Warning Gates

- Missing DOI when URL or arXiv ID exists.
- Partial metadata for non-central papers.
- Weak evidence strength with downgraded wording.
- Figures without automated generation script but with manual provenance.
- Council checkpoint artifacts used as provisional planning inputs.

## Common Failure Modes

- Treating warnings as blockers when a clear caveat is enough.
- Treating blockers as warnings because the deadline is near.
- Leaving conjectures unlabeled.
- Treating council consensus as evidence rather than a proposal-selection artifact.
