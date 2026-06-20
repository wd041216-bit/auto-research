# Research Lifecycle

## Purpose

Define how `survey`, `original`, `hybrid`, and `iteration` runs move from idea to paper package without bypassing evidence gates.

## Required Inputs

- User request or existing research package
- Chosen mode
- Workspace path
- Any supplied papers, repos, drafts, data, results, or reviews

## Required Outputs

- Updated stage artifacts in the research workspace
- Clear statement of current stage, next gate, and blocked artifacts
- Gate decision using the format in `process-constraints.md`

## Procedure

1. Decide whether stage 0, Proposal / Council Gate, applies.
2. Choose mode.
3. Confirm or create a workspace.
4. Start at the earliest incomplete required stage.
5. Apply the Universal Stage Contract in `process-constraints.md`.
6. Load the reference file for the current stage.
7. Produce or revise the stage artifact.
8. Run the validator for that artifact when available.
9. Move forward only when the gate passes or the next output is explicitly provisional.

Mode order:

| Mode | Required path |
| --- | --- |
| `survey` | Intake -> Questions -> Literature Recall -> Literature Triage -> Contribution Plan -> Claims -> Paper -> Review -> Revision |
| `original` | Council Gate when rough -> Intake -> Questions -> Literature Recall -> Literature Triage -> Contribution Plan -> Experiment -> Claims -> Paper -> Review -> Revision |
| `hybrid` | Council Gate when rough -> Intake -> Questions -> Literature Recall -> Literature Triage -> Contribution Plan -> Experiment -> Claims -> Paper -> Review -> Revision |
| `iteration` | Intake existing assets -> Validate current gates -> Resume at earliest failed gate -> Review -> Revision |

Survey mode may skip experiment artifacts only when no empirical claim is made. Iteration mode must not trust existing claims until the claims-evidence table and validators pass.

Use the Council Gate for rough original or hybrid ideas, top-tier proposal requests, AI-for-Science directions, interdisciplinary ambitions, method hypotheses without evaluation paths, and competing research ideas. Skip it for pure surveys, narrow revisions, or workspaces with complete brief and contribution plan.

Council states:

- `converged`: proposal may feed final contribution planning.
- `checkpoint`: proposal may feed provisional planning only.
- `blocked`: required source, dataset, user decision, or resource is missing.
- `killed`: idea should be abandoned or redirected.

## Stage Constraint Summary

Use `process-constraints.md` as the full contract. This table is the lifecycle-level routing summary.

| Stage | Must have before starting | Must not do | Exit gate |
| --- | --- | --- | --- |
| 0. Council | Rough original or hybrid direction | Treat council consensus as evidence | `converged`, `checkpoint`, `blocked`, or `killed` recorded |
| 1. Intake | User request or existing package | Start downstream work without a brief | Complete research brief |
| 2. Questions | Complete brief | Hide novelty or evaluation assumptions | Scoped questions with evidence paths |
| 3. Literature Recall | Brief and questions | Treat memory as search | Search log with repeatable query records |
| 4. Literature Triage | Search log and candidate papers | Cite unverified central sources as confirmed | Matrix rows scored and categorized |
| 5. Contribution Plan | Questions, matrix, council output when required | Plan claims without evidence paths | Selected contribution and risks |
| 6. Experiment / Analysis | Contribution plan | Choose metrics after seeing results | Plan and results ledger |
| 7. Claims | Matrix and results as applicable | Put unmapped claims in final sections | Claims-evidence audit passes |
| 8. Paper | Claims table and references | Write final prose from unsupported claims | Paper and refs complete or provisional |
| 9. Review / Revision / Submission | Paper package | Say submission-ready before closure | Review, revisions, limitations, reproducibility, and checklist complete |

## Blocking Gates

- Missing brief blocks all non-provisional work.
- Rough original or hybrid ideas without a council checkpoint or converged proposal block final contribution planning.
- Council checkpoint blocks final proposal language unless a later contribution plan resolves open objections.
- Missing literature triage blocks related work and survey taxonomy.
- Missing experiment plan blocks empirical conclusions.
- Missing claims-evidence blocks final abstract, introduction, discussion, and conclusion.
- Missing review and revision closure blocks submission-ready status.

## Common Failure Modes

- Starting from paper writing because the user asks for a paper.
- Treating model memory as literature search.
- Writing a contribution before the evidence path is defined.
- Marking a draft ready because it is polished rather than reviewed.
