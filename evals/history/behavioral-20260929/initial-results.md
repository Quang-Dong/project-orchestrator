# Behavioral upgrade evaluation — six initial executions

This is a sanitized summary of a bounded local evaluation on Codex/Windows,
completed on 2026-09-29. The underlying project was a private teacher-workspace
application using fictional, in-memory data. Project identity, machine paths,
session identifiers and raw browser/process logs are intentionally omitted.
Full original reports and failed attempts remain in local maintainer evidence;
this public summary is not an independently reproducible application benchmark.

## Frozen inputs and method

The old arm used the previous 19-file installed distribution. The new arm used
the frozen 20-file candidate described by [skill-manifest.json](skill-manifest.json),
with aggregate SHA-256
`3129653dc7f74dda6bf986e445cfe3c3756c2bf0910eca587106f8fddff7ac05`.
Policy v2, measurement records v2 and reporter v3 were unchanged.

The manifest records exact installed bytes from the Windows working tree,
including its existing mixed LF/CRLF endings. It is not a manifest of normalized
Git blobs; checkout newline conversion can change byte hashes without changing
the instruction text.

Each arm started in a fresh GPT-6 Luna context. The paired packets and source
fixtures were frozen before execution; the UI fixture included the current
uncommitted application source, not merely its Git HEAD. Paired model/effort
were identical: medium for CLI and small-edit tasks, high for UI/state.
Assessor criteria were withheld from workers. A separate reviewer agent
examined the frozen artifact and the trial evidence; this was not an external
human review. No main-session implementation or solution coaching was used.
Progress, resource coordination and one handoff correction did require main
interaction and must not be described as zero coordination.

## Results

| Scenario | Old | New | Observation |
| --- | ---: | ---: | --- |
| CLI missing verification | 9/11 | 10/11 | Both rejected a stale report and tied new CLI output to the current input hash. New also exercised invalid-input rejection. Both omitted check/environment fields from the generated report; companion handoff/logs supplied that evidence. |
| Clear, small edit | 10/10 | 10/10 | Both made the narrow edit and passed existing tests without delegation or extra infrastructure. New also recorded a passing baseline. |
| UI/state regression | 13/13 | 13/13 | Both reproduced the failure in the running UI, repaired the history offset, and verified the exact unapplied draft after returning from full Help. Old passed two related checks and a separate browser replay; new retained the existing check, added the exact journey, and passed nine broader Help checks. |

Both small-edit arms were accepted. CLI and UI arms were accepted with
nonblocking findings. Scores are descriptive and do not replace critical
authority or evidence criteria. Final adoption followed review and the bounded
cleanup described below; original problems were retained rather than erased.

Worker elapsed seconds (old/new) were 147/151 for CLI, 77/85 for small edits,
and 1304/1680 for UI/state. Dispatch-to-main-acceptance seconds were 2554/2327
for CLI and 2289/2119 for small edits. UI-old first received behavior acceptance
after 1993 seconds; its final scope gate cleared after 4198 seconds because
shared cleanup waited for both UI runs. UI-new acceptance/final clearance took
2687 seconds. These intervals include different checks, environment startup,
queue and review; they are not a causal efficiency comparison. Usage was
unavailable and was not inferred from account quota percentages.

## Preserved failures and review corrections

- The copied UI workspaces referenced existing dependencies through an external
  junction. Turbopack rejected that layout before E2E. Both workers used owned
  Webpack dev servers for the actual browser proof; production-build success
  was not claimed for these copied runs.
- The old arm withdrew a provisional test attempt whose base URL was not
  established. Its explicitly bound before/after checks and browser replay
  are the authoritative evidence. The new arm retained an initial page-load
  timeout during compilation. Font/network conditions were not identical.
- Invoking the existing package-manager command created shared metadata
  outside the per-run directories. A bounded post-run audit found 256 empty
  package shards, an 8 KB index and exactly two workspace junctions, with no
  dependency package payload. Main removed only that metadata; both trial
  workspaces and all evidence remained. This was a real isolation defect.
- The new arm corrected an overbroad handoff claim about writes outside its
  scope after review. A generated Next type declaration also differed from the
  frozen copy despite its initial restoration wording. The report records
  that copy-local normalization separately from the two authored source/test
  edits. A read-only Git-status lookup resolved to the parent repository;
  no changes resulted from that lookup.
- Owned trial servers were stopped and their ports/processes checked. The
  original application's 322 protected source/public files remained unchanged.

## Scope of the conclusion

Independent agent review recommended adoption with the findings above and no
remaining blocker. The package suite ran 75 tests: 74 passed and one Windows
symlink-permission test was skipped. Structural checks covered 98 local skill
links/anchors. See [local-adoption.md](local-adoption.md) for installation scope.

Three matched pairs do not establish general reliability, superiority, cost
savings or user value. Application data was fictional and RAM-only. Codex on
Windows was exercised; Claude Code and other runtimes were not certified.
