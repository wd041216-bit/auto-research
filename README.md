# Auto Research

**Evidence-gated research workflows for AI agents.**

Auto Research is a Codex skill and standalone research toolkit for turning rough ideas into paper-ready research packages without losing evidence discipline. It gives agents a structured path through proposal councils, literature triage, experiment planning, claim-evidence mapping, simulated review, revision closure, and submission packaging.

> Research agents need judgment, but they also need brakes. Auto Research gives them gates.

## Why This Exists

AI agents can write polished research prose before they have earned the claims. That is dangerous: fake citations, weak novelty, missing baselines, hidden negative results, and "submission-ready" drafts that never survived real critique.

Auto Research makes the agent stop at the right places:

- No final claim without traceable evidence.
- No related work without a literature matrix.
- No empirical conclusion without a prior experiment plan and results ledger.
- No top-venue proposal without frontier grounding and unresolved-veto checks.
- No submission-ready language without review and revision closure.

## What It Does

- **Proposal / Council Gate**: turns rough ideas into scored, adversarially reviewed proposal dossiers.
- **Literature Protocol**: records search logs, source metadata, triage categories, and literature quality scores.
- **Experiment Protocol**: requires hypotheses, baselines, metrics, ablations, negative controls, and result ledgers.
- **Claim-Evidence Audit**: checks whether claims are empirical, literature-backed, theoretical, conjectural, engineering, or negative-result claims.
- **Review Packet Builder**: packages the current state for skeptical review.
- **Process Constraints**: defines stage contracts, evidence ID rules, status states, downgrade rules, and allowed gate decisions for every workflow step.
- **Workspace Templates**: creates a complete paper-package workspace with all required artifacts.

## Quick Start

Clone the repository:

```bash
git clone https://github.com/wd041216-bit/auto-research.git
cd auto-research
```

Create a research workspace:

```bash
python3 scripts/init_research_workspace.py \
  --mode hybrid \
  --title "My Research Direction" \
  --output ./my-research
```

Validate gates:

```bash
python3 scripts/validate_research_gates.py ./my-research --mode hybrid
```

An empty workspace should fail. That is the point. Fill artifacts as evidence becomes available, then rerun validators.

## Use As A Codex Skill

Copy or symlink this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)" ~/.codex/skills/auto-research
```

Then invoke:

```text
Use $auto-research to turn this research direction into a publication-quality paper package.
```

## Lifecycle

```text
0. Proposal / Council Gate
1. Intake
2. Research Question
3. Literature Recall
4. Literature Triage
5. Contribution Plan
6. Experiment / Analysis
7. Claim-Evidence Mapping
8. Paper Package
9. Peer Review & Revision
```

## Repository Layout

```text
SKILL.md                         Codex skill entrypoint
references/                      Protocols and rubrics
references/process-constraints.md Stage and process constraints
scripts/                         Deterministic validators and workspace tools
assets/research-workspace/       Blank research package template
examples/                        Minimal passing example workspace
agents/openai.yaml               Skill UI metadata
```

## Core Commands

```bash
python3 scripts/check_literature_matrix.py ./my-research
python3 scripts/audit_claims_evidence.py ./my-research
python3 scripts/build_review_packet.py ./my-research
python3 scripts/validate_research_gates.py ./my-research --mode hybrid
```

## The Council Gate

For rough original or hybrid research ideas, Auto Research runs a proposal council before letting the idea harden into a contribution plan.

Council roles include:

- Chair
- Domain scientist
- Methods inventor
- Data and benchmark specialist
- Reviewer skeptic
- Replication engineer
- Venue strategist
- Ethics and safety critic

The council can end as:

- `converged`
- `checkpoint`
- `blocked`
- `killed`

Only `converged` permits final proposal packaging.

## Validation Philosophy

Auto Research is intentionally strict. A validator failure is a useful research signal, not a bad user experience.

Examples:

- Empty workspaces fail because no evidence exists yet.
- Empirical claims fail unless they reference `result:` IDs.
- Literature-backed claims fail unless they reference `lit:` IDs.
- Converged proposals fail if the debate log still has unresolved vetoes.

## Example

Run validation against the bundled example:

```bash
python3 scripts/validate_research_gates.py examples/converged-council-hybrid --mode hybrid
python3 scripts/build_review_packet.py examples/converged-council-hybrid
```

## Roadmap

- arXiv / DBLP / Semantic Scholar metadata helpers
- LaTeX compilation helper
- Citation graph expansion
- More example research packages
- Optional multi-agent council orchestration
- GitHub Action artifacts for review packets

## License

MIT. Use it, fork it, remix it, and make research agents more honest.
