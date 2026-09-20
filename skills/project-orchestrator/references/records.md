# Optional workflow measurements and reporter v3

Use this reference only to record or query measurements for a concrete question. Inputs are recorded v2 events and their evidence sources. Decide what the observations establish and what remains unknown; stop once the needed summary or page answers that question. A task does not need metrics, an experiment or JSONL files merely to start, continue or finish.

Keep the current requirement and recovery checkpoint in existing project records under [handoffs](handoffs.md#one-current-handoff). Measurements are optional evidence, not authority, process control or a substitute for actual runtime state. Record a process trial only when one is actually authorized.

`report_workflow.py --metrics PATH --improvements PATH` is a standard-library-only read-only reporter. Inputs remain v2 JSONL; **output is v3 and defaults to summary**. Exit 0 means valid input; 2 means malformed/unsupported/duplicate records, invalid query or semantic acceptance error. Errors are JSON with no partial accepted results. `--help` displays usage. No files, caches or network calls are created.

## Metrics JSONL

Elapsed wall time is not measured active effort. Session age or cached-token counts do not establish remaining allowance or billed cost.

Each v2 event requires: schemaVersion=2, eventId, taskId, attemptId, eventType, occurredAt (ISO 8601 with timezone), artifactVersion (nonempty string or null), source (nonempty evidence reference), role (lead/worker/reviewer), details (object), missingReasons (object).
All IDs are nonempty strings. Unknown event types/versions are rejected. Reject duplicate JSON keys, non-finite numeric values and duplicate eventIds across BOTH inputs. Blank lines are ignored. If artifactVersion is null, missingReasons.artifactVersion must be a nonempty reason. Unknown optional fields may be preserved/ignored; required meaning must be validated.
Version 1 and other unsupported records reject the entire input; no migration, exclusion count or guessed data.

Event types:
- task_started, handoff, accepted: details may be empty.
- repair: details.reason is nonempty.
- observation: details has avoidableQuestions, lateDefects (nonnegative integers or null), effortSeconds (nonnegative finite number or null). Each null requires missingReasons for that field.
- usage_snapshot: details has inputTokens, cachedInputTokens, outputTokens, reasoningOutputTokens (nonnegative integers or null), billedCost (null or {amount: nonnegative finite number,currency: three uppercase letters}), allowance (null or object). Each null requires missingReasons for that field. Cached tokens are a subset of input; reasoning tokens a subset of output. Reject known subset > known total. Do not sum overlapping components. Usage is cumulative within taskId/attemptId/role: retain latest snapshot per group, never sum snapshots. Forward allowance separately; do not turn it into task cost. Report currency-bearing costs separately; no exchange-rate calculations.
Observations are deltas, counted once by eventId; do not assume no observations means zero.

Group metrics by taskId + attemptId. Sort events by parsed time. A handoff requires non-null artifactVersion. An accepted event requires an earlier-or-same-time handoff with EXACT matching artifactVersion in that attempt. The matching handoff must be the latest handoff before acceptance. Accepted before start or handoff is an error. Multiple accepted events in an attempt are an error. Equal-time conflicting handoffs or cumulative snapshots must not be arbitrarily ordered: reject ambiguous conflicts.
For each attempt return role information, status accepted/handed_off/in_progress (only evidence in records), startedAt, acceptedAt, elapsedToAcceptanceSeconds or null with reason, repairRounds (count actual repair events; 0 is observed count, not proof of no unrecorded repair), firstPassAccepted (accepted with zero repair events; null before acceptance), avoidableQuestions, lateDefects, effortSeconds and completeness limitations. Unknown observations keep null/partial markers rather than complete totals. Also output effort grouped by role and latest usage snapshots (not a combined token bill).
Missing start with no acceptance is allowed as incomplete historical/checkpoint evidence; accepted without start is invalid.

## Improvements JSONL

Each v2 event requires: schemaVersion=2, eventId, experimentId, occurredAt (timezone), taskId (the bound task), owner, state (proposed/trial/closed), change (one bounded intervention), reviewTrigger, qualityToPreserve (nonempty string list), measurement (nonempty string list), revertWhen (nonempty string list), previousGuidance, evidence (string list), decision, missingEvidence (string list), nextReview.
Strings other than nullable fields must be nonempty. decision must be null for proposed/trial; closed decision is adopted/revised/reverted/deferred. A deferred decision requires nonempty missingEvidence and nextReview. Other closed decisions require nonempty evidence. A trial requires nextReview (the close/review event trigger). Keep the latest event per experiment by time; reject ambiguous equal-time different states. Return active trials and closed/deferred decisions, with a warning when an active trial's bound task has an accepted attempt and no closure event. Do not invent adoption.
Unsupported versions in either stream reject the report, even outside a requested filter.

## Output

The explicit full audit has schemaVersion=3, view=full, inputHashes, valid boolean, errors array with input/line and reason when available, limitations array, attempts array, effortByRole, usageSnapshots, experiments array and overdueExperimentIds array. Invalid input returns valid=false and errors; never a success-shaped accepted summary from invalid evidence.
Missing data and partial observations must be explicit. Deterministic output ordering by IDs. Empty valid files produce empty arrays and no invented task metrics.

## Acceptance

Regression coverage includes valid end-to-end metrics/improvement closure; old-version rejection in both streams and null reasons; malformed records/duplicate JSON keys/duplicate IDs across streams; unsupported version/types; invalid/naive time; stale or missing handoff on acceptance; out-of-order records; repeated cumulative usage without double-counting; counters/currency/null/role measurements; trial still open after task acceptance; deferred decision without missing evidence/review trigger; empty inputs; CLI exit codes and read-only input/output-directory hashes. No wording-matching tests.


## Summary, detail and full audit

Normal reads default to summary; optional `--task-id` or `--experiment-id` narrows the question. `--view summary` is equivalent. Use `--view detail` for typed attempt/experiment/usage items, with `--limit` (1..200, default 20) and the returned `--cursor` for the next page. Task/experiment filters intersect; experiment queries return experiments only, never imply unrelated task metrics belong to a trial. Missing matches produce empty results.

Use `--view full` deliberately for the entire audit. Full rejects filters and pagination. `--cursor` and `--limit` are detail-only; silently ignoring them could hide missing evidence. Calls without `--view` no longer return the unbounded full report. There is no v1 reader, `legacyCounts`, `viewVersion` or legacy `build` compatibility helper.

All CLI outputs have `schemaVersion=3`. Valid views identify `view` and exact `inputHashes`. Summary/detail include filters, counts and `validationScope`. Summary returns attempt/experiment state counts, recorded repair rounds, attempts with unknown observations and overdue trial count; it does not create a combined token bill. Detail adds items, totalItems, offset, hasMore and nextCursor. Its order is attempts, experiments, then usage, with deterministic ID ordering within each group.

Validate all supplied records and semantic invariants before filtering. Invalid input never produces a partial success summary. Cursors bind to output version, exact input bytes, filters, view and page size; changed inputs/options require restarting. Malformed or stale cursors return exit 2. A cursor is not an authorization token.

Inputs are read line by line, but parsed grouping still uses O(n) memory and full validation. Summary/detail expose the first 20 global limitations and their total; use the explicit full audit when further limitations matter. Reduced response size is not a measured end-to-end efficiency gain. No database, index, telemetry or automatic rotation is included.
