# Workflow records v2 and read-only reporting

Deliver a Python standard-library-only read-only CLI, `report_workflow.py --metrics PATH --improvements PATH`. Emit one JSON object to stdout; exit 0 for valid input, 2 for malformed/unsupported/duplicate records or semantic acceptance errors. Do not create files, caches or network calls. Use python -B in tests. The final script installs beside check_policy.py.

## Metrics JSONL

Each v2 event requires: schemaVersion=2, eventId, taskId, attemptId, eventType, occurredAt (ISO 8601 with timezone), artifactVersion (nonempty string or null), source (nonempty evidence reference), role (lead/worker/reviewer), details (object), missingReasons (object).
All IDs are nonempty strings. Unknown event types/versions are rejected. Reject duplicate JSON keys, non-finite numeric values and duplicate eventIds across BOTH inputs. Blank lines are ignored. If artifactVersion is null, missingReasons.artifactVersion must be a nonempty reason. Unknown optional fields may be preserved/ignored; required meaning must be validated.
Known v1 records: keep count and warn legacy_records_not_aggregated; no migration or guessed data.

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
Known v1 records are counted separately and not rewritten.

## Output

schemaVersion=2; valid boolean; errors array with input/line and reason when available; limitations array; legacyCounts {metrics,improvements}; attempts array; effortByRole; usageSnapshots; experiments array; overdueExperimentIds array. Invalid input returns valid=false and errors; never a success-shaped accepted summary from invalid evidence.
Missing data, legacy exclusions and partial observations must be explicit. Deterministic output ordering by IDs. Empty valid files produce empty arrays and no invented task metrics.

## Acceptance

Tests must cover valid end-to-end metrics/improvement closure; legacy+v2 and null reasons; malformed records/duplicate JSON keys/duplicate IDs across streams; unsupported version/types; invalid/naive time; stale or missing handoff on acceptance; out-of-order records; repeated cumulative usage without double-counting; counters/currency/null/role measurements; trial still open after task acceptance; deferred decision without missing evidence/review trigger; empty inputs; CLI exit codes and read-only input/output-directory hashes. No wording-matching tests.


## v03 query views (additive CLI interface)

Normal reads use --view summary with --task-id or --experiment-id. Use --view detail for records, with --limit (1..200, default 20) and the returned --cursor to continue. Without --view the v2 CLI and report stay unchanged; query switches require an explicit view. Input policy v1 and JSONL v2 do not change.

Views have schemaVersion=2 and viewVersion=1. They include inputHashes, filters, counts, validationScope and legacy limitations. Summary returns state counts, observed repair counts, counts of attempts with unknown observations and overdue trials; it does not invent a total token bill. Detailed results contain typed attempt/experiment/usage items, totalItems, offset, hasMore and nextCursor. An experiment filter returns experiments only; task and experiment filters intersect. Missing matches return empty results, not a guessed task.

Validate all supplied input records and semantic invariants before filtering. Legacy entries remain counted/excluded. Detail order is attempts, experiments, usage, with existing deterministic ordering in each group. Cursors bind to exact input bytes, filters, view and page size. Changed inputs or options require restarting; malformed/stale cursors fail with exit 2, without partial accepted results. A cursor is not an authorization token.

File input is read line by line; parsed records and grouping still require O(n) memory and a full validation pass. This reduces raw-text copies and model output, not all processing cost. No database, background index or automatic log rotation is included. Keep full reports for deliberate audits; never include them by default in startup context. Summary returns the first 20 global limitations with limitationsTotal explicitly showing any remainder; inspect detailed/full audit output when that count requires it.
