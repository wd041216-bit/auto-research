# Process Constraints

## Purpose

Define the constraints that govern every Auto Research stage and cross-stage process. Use this file when deciding what an agent may do, what it must not do, and when it is allowed to advance.

## Required Inputs

- User request, workspace path, and selected mode
- Current workspace artifacts
- Relevant stage protocol from `references/`
- Available papers, data, code, results, drafts, reviews, or external constraints

## Required Outputs

- A stage decision: `advance`, `advance-with-warning`, `provisional-only`, `blocked`, or `killed`
- Updated artifacts with stable IDs and status markers
- Explicit missing-evidence list when a stage cannot advance
- Downgraded wording when evidence is partial

## Universal Stage Contract

Every stage follows the same contract.

1. Load the earliest incomplete required artifact for the selected mode.
2. Name the current stage, mode, artifact targets, and gate being attempted.
3. Check prior-stage artifacts before producing downstream claims.
4. Record all new evidence with stable IDs before citing it in prose.
5. Separate observations from interpretations.
6. Mark provisional outputs as provisional in the artifact and in the response.
7. Run the available validator before declaring the gate passed.
8. Stop at a blocking gate instead of filling gaps by inference.

Stage outputs may advance only when all of these are true:

- Required inputs exist or the output is explicitly provisional.
- Required artifact fields are populated with concrete content.
- Status markers match reality.
- Evidence IDs resolve to the artifact where the evidence lives.
- No blocking issue is hidden in notes, limitations, or review text.

## Global Invariants

- No final claim without traceable evidence.
- No fabricated papers, venues, DOIs, arXiv IDs, datasets, metrics, results, reviewer outcomes, or implementation artifacts.
- No empirical claim without `04_experiments/experiment-plan.md`, `04_experiments/results-ledger.md`, and `result:` evidence IDs.
- No literature-backed claim without `lit:` IDs from `02_literature/literature-matrix.csv`.
- No top-venue, novelty, SOTA, or benchmark-fit claim without current frontier grounding.
- No council convergence while a blocking veto remains unresolved.
- No submission-ready language without review memo, revision plan, revision ledger, limitations, reproducibility statement, and submission checklist.
- No overwriting negative or inconclusive results; record them and adjust the claim.
- No hidden mode switch. If the work changes from survey to original, or original to iteration, update the manifest or artifact notes and re-check required gates.

## Status Model

Use status labels consistently.

| Status | Meaning | Allowed downstream use |
| --- | --- | --- |
| `not-started` | Template placeholder only | Blocks all non-provisional downstream work |
| `draft` | Contains early content but missing required fields | May guide planning, not final claims |
| `provisional` | Useful but evidence-gated or unresolved | Must be labeled and cannot support final paper language |
| `complete` | Fields filled, evidence linked, validator checked when available | May support downstream gates |
| `blocked` | Cannot progress without missing input or decision | Must name blocker and next action |
| `superseded` | Replaced by a later artifact or decision | Keep for audit trail; do not cite as current evidence |

Templates use `Status: not-started`; agents may use `Status: draft`, `Status: provisional`, `Status: complete`, `Status: blocked`, or `Status: superseded` when the artifact state changes. Existing validators treat only `Status: complete` as completion.

## Evidence ID Rules

- Literature IDs use `lit:<paper_id>`.
- Result IDs use `result:<result_id>`.
- Council decisions use `council:<move_or_decision_id>`.
- Review concerns use `review:<concern_id>`.
- Revision closures use `revision:<revision_id>`.
- Implementation or data artifacts use `artifact:<path_or_id>`.

Evidence IDs must be stable, unique within their namespace, and findable in the referenced artifact. Do not cite a paper title, result description, or reviewer persona as a substitute for an ID.

## Stage Constraints

### Stage 0: Proposal / Council Gate

Use for rough original or hybrid ideas, top-tier proposal requests, AI-for-Science directions, method hypotheses, interdisciplinary ideas, and competing research directions.

Required inputs:

- Research direction or `00_intake/council-brief.md`
- Candidate field, artifact, constraints, and venue ambition
- Any available frontier notes

Allowed actions:

- Generate, compare, recombine, narrow, and kill candidate ideas.
- Run simulated or subagent council roles.
- Produce checkpoint artifacts when convergence is not reached.

Forbidden actions:

- Declaring final novelty without literature grounding.
- Treating council agreement as empirical evidence.
- Suppressing reviewer, replication, ethics, or data vetoes.
- Calling a checkpoint a final proposal.

Exit criteria:

- `converged`: all convergence conditions in `research-council-protocol.md` pass.
- `checkpoint`: useful but unresolved; contribution plan must say `Provisional: yes`.
- `blocked`: missing source, dataset, decision, resource, or permission.
- `killed`: idea fails feasibility, novelty, ethics, or evidence-path tests.

### Stage 1: Intake

Required inputs:

- User request or existing package
- Mode candidate and workspace location
- Available assets and constraints

Allowed actions:

- Ask one targeted question when mode or scope changes required artifacts.
- Create a workspace from the template.
- Record known unknowns instead of resolving them prematurely.

Forbidden actions:

- Starting literature, experiment, or writing work without a research brief.
- Hiding constraints because they make the project weaker.
- Assuming compute, data, API, or timeline budgets.

Exit criteria:

- `00_intake/research-brief.md` has `Status: complete`.
- Mode, target artifact, available assets, known constraints, and success criteria are explicit.

### Stage 2: Research Question

Required inputs:

- Complete research brief
- Mode and artifact target
- Any council checkpoint or converged proposal when required

Allowed actions:

- Split broad directions into scoped questions.
- Mark hypotheses as conjectural until evidence exists.
- Define out-of-scope boundaries.

Forbidden actions:

- Writing questions that cannot be evaluated or surveyed.
- Hiding novelty assumptions in question wording.
- Combining multiple unrelated aims into one question.

Exit criteria:

- Each question has scope, novelty angle, evidence path, success criteria, and out-of-scope notes.
- At least one question can be answered by the planned literature, experiment, analysis, or theory path.

### Stage 3: Literature Recall

Required inputs:

- Complete research brief and research questions
- Search sources available to the agent
- Current date and retrieval date discipline

Allowed actions:

- Search multiple query families and source types.
- Use citation chasing, venue proceedings, project pages, and benchmark leaderboards when relevant.
- Record failed or low-yield searches.

Forbidden actions:

- Treating model memory as literature search.
- Inventing metadata for inaccessible sources.
- Claiming coverage from a single query family.

Exit criteria:

- `02_literature/literature-search-log.md` records source, query, date, result count, inclusion rationale, and exclusions.
- The search log is complete enough for another agent to repeat or challenge coverage.

### Stage 4: Literature Triage

Required inputs:

- Search log
- Candidate papers and metadata

Allowed actions:

- Score relevance, authority, recency, method fit, and centrality.
- Assign triage categories.
- Mark metadata uncertainty explicitly.

Forbidden actions:

- Using unverified central papers as verified support.
- Keeping citations that are irrelevant except for name-dropping.
- Ignoring contrary or negative literature.

Exit criteria:

- `02_literature/literature-matrix.csv` has at least one real paper row for non-empty research outputs.
- `must-cite` and `deep-discuss` entries include summary and relevance rationale.
- Central metadata is verified or labeled uncertain.

### Stage 5: Contribution Plan

Required inputs:

- Research questions
- Literature matrix
- Council checkpoint or convergence when required

Allowed actions:

- Compare candidate contributions.
- Choose a primary plan and backup path.
- Name evidence required to support each intended claim.

Forbidden actions:

- Calling a proposal final when council status is checkpoint, blocked, or killed.
- Planning claims without evidence paths.
- Ignoring feasibility, reproducibility, or ethical constraints.

Exit criteria:

- `03_contribution/contribution-plan.md` names selected contribution, rejected alternatives, evidence path, required experiments or analysis, risks, and provisional status.
- For original or hybrid work, the next required artifact is experiment or analysis planning.

### Stage 6: Experiment / Analysis

Required inputs:

- Contribution plan
- Relevant literature entries
- Available code, data, benchmarks, models, prompts, or analysis materials

Allowed actions:

- Plan minimal meaningful checks before running larger studies.
- Record baselines, metrics, seeds, versions, data, prompts, scripts, and invalidation criteria.
- Log all results, including negative and inconclusive results.

Forbidden actions:

- Choosing metrics after seeing results.
- Rewriting the original hypothesis to fit observed results.
- Reporting improvements without denominators, variance, or baselines when applicable.
- Treating demos, anecdotes, or model estimates as measurements.

Exit criteria:

- `04_experiments/experiment-plan.md` is complete before results are interpreted.
- `04_experiments/results-ledger.md` records result IDs, artifact links, metrics, comparisons, interpretations, limitations, and supported claim IDs.

### Stage 7: Claim-Evidence Mapping

Required inputs:

- Literature matrix
- Results ledger for empirical or negative-result claims
- Contribution plan and paper sections

Allowed actions:

- Classify claims as empirical, literature-backed, theoretical, conjecture, engineering, or negative-result.
- Downgrade wording based on evidence strength.
- Split compound claims when evidence differs by part.

Forbidden actions:

- Putting a claim into abstract, introduction, discussion, or conclusion before it appears in `05_claims/claims-evidence.csv`.
- Using weak evidence with strong words such as prove, guarantee, state-of-the-art, outperform, best, novel, significant, robust, or causal unless strength is strong or verified.
- Treating conjectures as findings.

Exit criteria:

- Every non-conjecture claim has evidence IDs.
- Empirical and negative-result claims include `result:` IDs.
- Literature-backed claims include `lit:` IDs.
- Wording risk is marked and downgraded where needed.

### Stage 8: Paper Package

Required inputs:

- Complete claim-evidence table
- Literature matrix and references
- Experiment or analysis artifacts when claims require them

Allowed actions:

- Write sections from mapped claims.
- Keep placeholders for missing evidence instead of inventing content.
- Add limitations and reproducibility details as first-class sections.

Forbidden actions:

- Writing final abstract, introduction, discussion, or conclusion from unmapped claims.
- Adding references not present in verified BibTeX or literature artifacts.
- Omitting negative results that affect interpretation.

Exit criteria:

- `06_paper/paper.tex` and `06_paper/refs.bib` are complete or explicitly provisional.
- Claims in high-level sections map to `05_claims/claims-evidence.csv`.
- Figures, tables, appendices, and references have provenance.

### Stage 9: Peer Review, Revision, And Submission

Required inputs:

- Paper package
- Review packet
- Review memo
- Revision plan and ledger
- Limitations and reproducibility statement

Allowed actions:

- Simulate skeptical review with distinct personas.
- Convert concerns into revision items.
- Close revisions with verification evidence.
- Build a submission package only after closure.

Forbidden actions:

- Saying submission-ready after copyediting only.
- Closing reviewer concerns without changed artifacts or explicit rationale.
- Hiding limitations, unavailable assets, or reproducibility gaps.

Exit criteria:

- `07_review/review-memo.md`, `08_revision/revision-plan.md`, and `08_revision/revision-ledger.md` are complete.
- Blocking review concerns are closed or the package is downgraded.
- `09_submission/submission-checklist.md`, `limitations.md`, and `reproducibility-statement.md` are complete.

## Process Constraints

### Mode Selection

- `survey` may skip experiment artifacts only when no empirical or experimental claims are made.
- `original` and `hybrid` require experiment or analysis artifacts before final empirical claims.
- `iteration` starts by validating existing artifacts and resumes at the earliest failed gate.
- If mode is ambiguous and changes required artifacts, ask one short question; otherwise choose the conservative mode and state it.

### Workspace Creation

- Use `scripts/init_research_workspace.py` instead of hand-creating the directory tree.
- Do not delete an existing non-empty workspace unless `--force` is explicitly requested.
- Preserve `auto-research-manifest.json`; update mode or title only when the research scope truly changes.

### Council Operation

- Assign roles with mandates, acceptance criteria, and veto scope.
- Record each adaptive move, open objection, vote, and chair decision.
- Use `checkpoint` when useful progress exists but convergence conditions are not met.
- Use `blocked` when external input is required.
- Use `killed` when the idea should be abandoned or redirected.

### Source Verification

- Verify central sources against primary metadata when possible.
- Record retrieval dates.
- Mark `metadata_status` as `uncertain` or `needs-check` rather than inventing.
- Do not cite inaccessible or unverified sources as confirmed support.

### Experiment Execution

- Freeze the experiment plan before interpreting results.
- Record environment details needed for reproduction.
- Keep raw or derived artifact paths in the ledger.
- Record failed runs if they affect interpretation.

### Claim-Evidence Mapping

- Map every final claim before paper polishing.
- Prefer smaller claims when evidence is uneven.
- Keep conjectures explicit and future-facing.
- If a claim cannot be mapped, remove it, downgrade it, or add the missing evidence task.

### Review And Revision

- Reviewers must be allowed to block, not only suggest edits.
- Each blocking concern needs a revision item or a documented downgrade decision.
- Revision closure requires verification, not just a claim that the text was improved.
- A review packet generated before major changes should be regenerated.

### Submission Packaging

- Submission package status is blocked until validators pass or remaining issues are labeled nonblocking with rationale.
- Limitations and reproducibility statements must mention unavailable data, code, prompts, seeds, proprietary assets, and manual steps.
- Do not claim venue compliance unless the target venue requirements were checked.

## Downgrade Rules

Use downgraded language when evidence is partial.

| Evidence state | Allowed wording |
| --- | --- |
| No evidence yet | hypothesis, candidate, proposed, intended |
| Literature only | appears consistent with, prior work suggests |
| Single weak result | preliminary, in this setting, suggests |
| Missing baseline | observed behavior, not improvement |
| Missing ablation | possible mechanism, not causal explanation |
| Unresolved review concern | draft, under revision, not submission-ready |

Block instead of downgrade when the user asks to fabricate, hide negative evidence, skip required evidence for final claims, or misrepresent package readiness.

## Gate Decision Format

When reporting stage status, use this compact format:

```text
Stage:
Mode:
Decision:
Passed:
Blocking:
Warnings:
Next artifact:
Validator:
```

Use `Decision: blocked` when any blocking item remains. Use `Decision: provisional-only` when useful output can continue but must not be final.

## Common Failure Modes

- Advancing because the prose sounds mature rather than because gates passed.
- Treating a missing artifact as a note instead of a blocker.
- Letting the user waive scientific-integrity constraints.
- Mixing evidence IDs and prose citations.
- Revising claims after results without preserving the original hypothesis and negative findings.
- Forgetting that checkpoint council outputs are planning artifacts, not proof.
