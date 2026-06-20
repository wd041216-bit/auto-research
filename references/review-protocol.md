# Review Protocol

## Purpose

Simulate peer review, convert concerns into revisions, and close revisions with artifact evidence.

## Required Inputs

- Paper package
- Claims-evidence table
- Literature matrix
- Experiment artifacts when applicable
- Review packet

## Required Outputs

- `07_review/review-memo.md`
- `07_review/review-packet.md`
- `08_revision/revision-plan.md`
- `08_revision/revision-ledger.md`

## Procedure

1. Build or refresh the review packet.
2. Review from five personas: area expert, methods expert, experimental skeptic, writing editor, and reproducibility reviewer.
3. Score novelty, correctness, evidence, clarity, positioning, and reproducibility from 1-10.
4. Write concrete concerns with artifact references.
5. Convert each blocking concern into a revision item.
6. After edits, update the revision ledger with changed artifact, summary, and verification.
7. Re-run validators before marking concerns closed.

## Process Constraints

- Reviewer personas must be allowed to block acceptance, not only suggest improvements.
- Each blocking concern must become a revision item, downgrade decision, or documented rejection rationale.
- A revision closure must name the changed artifact and verification method.
- Refresh the review packet after material changes to paper, claims, experiments, literature, limitations, or reproducibility.
- Submission readiness is a gate decision, not a tone judgment.

## Blocking Gates

- Submission-ready status requires review memo, revision plan, revision ledger, and submission checklist.
- A revision item is not closed unless it names the changed artifact.
- A reviewer concern about missing evidence cannot be closed by wording alone unless the claim is downgraded.

## Common Failure Modes

- Asking reviewers only for praise.
- Treating a language edit as a methodological fix.
- Closing all revisions without revalidating claims.
- Ignoring reproducibility concerns because the paper reads well.
