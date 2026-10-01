# Local evaluation data

Evaluation material under repository `.data/` is local maintainer data, not source code or a public report. Keep reusable synthetic fixtures, manifests, and evaluation definitions in the relevant `evals/` tree. Do not treat retained run logs as reusable input fixtures.

The regression comparison runner stores retained records and logs in `.data/artifacts/regression-comparison/<run-id>/`. It creates disposable baseline and corrected copies under `.data/workspaces/regression-comparison/<run-id>/` and removes that exact workspace run when the checks finish. The runner refuses an existing run ID and rejects path traversal, symlinks, Windows junctions, and other reparse points at checked path components and inside snapshots. Use a new safe run ID for every invocation; never manually clean a parent directory to make an ID reusable.

Other tools may define their own owned artifact or workspace roots under `.data/`. Follow their local instructions and keep retained evidence separate from disposable workspaces. Only clean an exact run directory that the current tool/task owns. Do not delete the `.data` root or another tool's records as part of evaluation cleanup.

The prior local regression-comparison history was removed during the 2026-10-01 data categorization. The public historical verdicts remain unchanged, but the old private logs, manifests, task records, and outputs are no longer available and must not be described as retained or reconstructed. The small synthetic source fixtures and current source manifests live in versioned `evals/` directories.
