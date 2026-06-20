# Contributing

Auto Research is built around one principle: research agents should not make final claims before evidence exists.

## Good Contributions

- New validators that catch unsupported claims or weak research artifacts.
- Better templates for reproducible research packages.
- Protocol improvements for literature search, experiments, review, or revision.
- Example workspaces that demonstrate correct gate behavior.
- CI improvements that keep the toolkit easy to trust.

## Development Setup

```bash
git clone https://github.com/wd041216-bit/auto-research.git
cd auto-research
python3 scripts/validate_skill_structure.py .
for s in scripts/*.py; do python3 "$s" --help >/tmp/auto-research-help.txt || exit 1; done
python3 scripts/validate_research_gates.py examples/converged-council-hybrid --mode hybrid
```

## Contribution Rules

- Keep `SKILL.md` compact. Put detailed process in `references/`.
- Keep scripts Python standard-library only unless there is a strong reason.
- Do not add fake citations, fake metrics, or fake benchmark results to examples.
- New gates should have a pressure-test scenario.
- New scripts should expose `--help` and return nonzero on blocking failures.

## Pull Request Checklist

- [ ] `python3 scripts/validate_skill_structure.py .` passes.
- [ ] All scripts compile with `python3 -m py_compile scripts/*.py`.
- [ ] All scripts support `--help`.
- [ ] Example workspace validation still passes.
- [ ] New behavior is documented in `references/` and `README.md` if user-facing.

