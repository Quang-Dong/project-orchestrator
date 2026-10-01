# Measurement correction — 2026-09-30

The earlier statement that worker traces and usage were unavailable was
premature. On 2026-09-30, the native Codex session files were recovered using
exact agent path and parent thread ID, with one unique match for each worker.
This correction supplements the historical report; its criteria, verdicts,
failed results and installation decision are unchanged.

| Historical execution | Observed model/effort | Input tokens | Cached input subset | Output tokens | Trace duration | Tool calls |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| T1 control | gpt-6-luna / high | 410,025 | 396,032 | 1,912 | 87.075 s | 8 |
| T1 candidate | gpt-6-luna / high | 347,417 | 335,872 | 2,177 | 83.481 s | 7 |
| T3 candidate | gpt-6-luna / medium | 252,202 | 205,568 | 620 | 33.740 s | 5 |

These are observed cumulative worker-thread fields, not estimates. Cached
input is already included in input tokens. Trace duration covers the first
through last retained native record, not preparation, review or time to
acceptance. The table does not account for all main/reviewer/setup usage, nor
convert tokens to money or an account-limit percentage. One descriptive pair
does not establish general resource savings or a quality advantage; the two
T1 output artifacts were identical under the historical verdict.

## Control identity correction

The historical staging script selected `before/source-skill` for T1 control,
and `candidate/skill` for T1 candidate. It did not select
`before/installed-skill`. The reported comparison therefore must not be
described as an installed-global versus candidate comparison. The new
The teacher-workspace evaluation freezes the actually installed global skill as its
control before edits.

The historical T3 dispatch requested medium effort and the trace confirms
medium; the new teacher-workspace C protocol's low effort does not retroactively
change that execution.

## Evidence identity

Host-local recovery artifacts are retained under
`.data/teacher-workspace-quality/2026-09-30/telemetry/`.
Raw session data and ordered tool calls are not included in the distributable
skill or public evidence package.

| Recovered raw trace | SHA-256 |
| --- | --- |
| T1 control | `0dd7770c3c565335d1604e613de2b831d201351a53d03ec47c7e5d4523507c50` |
| T1 candidate | `12b6d6819c009bac84b6dff3f38b27924fef40dca6a8931ef88f6f03427fbc45` |
| T3 candidate | `b58f7ae8a2d29dd9bda9858ab64bd7430af92f75d01174d84544f0de19f825fb` |

The retained historical T3 dispatch has SHA-256
`1e99c60a93c820bb0ce4342be1262cbec04c2f3d5b805c560e4109fa850f1241`.
The recovery record also binds the original source paths, matching parent,
observed turn contexts and other historical artifact hashes. Missing telemetry
outside these three workers remains unmeasured; this correction is not a
reconstruction of the complete earlier task cost.
