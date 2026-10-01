# Frozen synthetic T1 comparison fixtures

These tiny fictional Python fixtures are version-controlled test inputs for `evals/compare_regression.py`. The original fixture reuses `evals/behavioral-bounded-context/fixtures/T1`; a hash comparison before migration confirmed it was byte-identical to the 2026-09-30 private original. `corrected-T1/` is the three-file corrected fixture rescued from the private previous-corrected output before local `.data` cleanup.

Each tree contains only `README.md`, `src/workspace.py`, and `tests/test_workspace.py`. No private manifest, task output, trace, command log, or old result is part of these fixtures. The runner validates new manifests generated from these sources at test/runtime; preserving the fixture source does not convert any historical verdict or result.
