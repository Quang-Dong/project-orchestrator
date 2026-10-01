# Maintainer evaluations

This index records the current executable checks and open evaluations. It is maintainer material; agents using the installed skill do not need it for ordinary product work. A passing package test or a small trial does not establish general effectiveness.

## Current work

- [Teacher-workspace quality comparison](behavioral-teacher-workspace-quality/setup.md) and [latest recorded result](behavioral-teacher-workspace-quality/results.md): approved 12-task control/candidate evaluation of the installed skill plus project verification profiles. The latest recorded preflight executed selected golden and seeded profiles: golden cases passed and seeded defects reproduced. Independent readiness and trial dispatch remain pending at 0/12. Earlier dependency and verifier blockers remain recorded as historical preparation. Improvement is unproven and the global skill remains unchanged.
- [Regression-comparison runner setup](behavioral-regression-comparison/setup.md): the current narrow Python fixture runner and its retained synthetic fixture. Its separate evaluation verdict is historical; detailed private records were removed on 2026-10-01 and have not been reconstructed. This is not evidence of general semantic judgment or current-source adoption.
- [Local data convention](local-data.md): retained evaluation artifacts and disposable workspaces have separate `.data` roots. Do not recreate historical local evidence from public verdicts.

## Package checks

Run from the repository root:

```sh
python -B -m unittest discover -s evals -p "test_*.py" -v
python -B -c "from pathlib import Path; [compile(path.read_bytes(), str(path), 'exec') for root in (Path('skills'), Path('evals')) for path in root.rglob('*.py')]; print('Python syntax valid')"
```

The suite checks policy v2, v1 measurement-record rejection, reporter v3 views and acceptance, artifact verification, the regression-comparison runner, and repository Markdown links. These checks exercise deterministic tools and repository paths; they do not show that agents followed the skill or that users received value. Report the actual run count, failures and skips from the tested revision.

Historical evidence remains grouped by reports, reviews, scenarios, packets, manifests, trials, and environment records in the [evaluation history](history/README.md). Its results, limitations, failures and not-run statuses remain scoped to the original revisions.
