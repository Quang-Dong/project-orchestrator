# Project Orchestrator

A skill for turning a user's objective into a useful, maintainable and verified outcome. Small, clear work stays direct. Consequential work uses the execution mode allowed by the user's current choices, actual runtime, budget and project constraints. The main session owns strategy, integration and acceptance.

## Current source status

This is the current source candidate. It is separate from installed skill copies; the 2026-09-29 local adoption record covers an earlier artifact and does not certify this source. No general improvement in agent behavior, efficiency or user value is established.

The current contracts accept policy v2 and optional measurement records v2. The read-only reporter emits v3, defaults to summary, and rejects unsupported v1 records. Policy v1 and removed legacy reporter fields have no automatic converter or compatibility layer. A skill contract change does not authorize changing a product's policy or data.

## Use the skill

Start with [the skill entrypoint](skills/project-orchestrator/SKILL.md). Load its focused references only when their decisions matter. For consequential work, clarify the desired outcome and authority, inspect the current project and runtime, make the smallest useful change, observe the actual result, and report remaining limits. Keep coupled implementation with one owner and preserve unresolved decisions in a useful handoff.

Project instructions and the user's current choices control whether work is direct, delegated or paused. A missing delegation prerequisite remains unresolved. A task report, package test or installed copy does not establish user acceptance or product value.

## Verify

Run the package tests and syntax checks from the repository root:

```sh
python -B -m unittest discover -s evals -p "test_*.py" -v
python -B -c "from pathlib import Path; [compile(path.read_bytes(), str(path), 'exec') for root in (Path('skills'), Path('evals')) for path in root.rglob('*.py')]; print('Python syntax valid')"
```

CI checks JSON validity and runs the Python package and Markdown link tests. Whitespace and public-content scope require separate review. Repository checks do not measure agent outcomes.

## Evaluation status

The [current evaluation index](evals/README.md) lists a teacher-workspace quality comparison and the regression-comparison runner. The latest recorded quality-evaluation preflight passed selected golden profiles and reproduced the intended seeded failures, but independent readiness and trial dispatch remain pending at 0/12. The regression comparison status is historical; detailed private records were removed and are not reconstructed. Neither result establishes current-source adoption or broad improvement.

Read the [evaluation history](evals/history/README.md) for prior reports, packets, manifests, compatibility records and run artifacts. Historical verdicts, limits and unrun statuses remain attached to their original evidence.

For contribution and maintenance boundaries, see [CONTRIBUTING](CONTRIBUTING.md) and [maintenance guidance](skills/project-orchestrator/references/maintenance.md).
