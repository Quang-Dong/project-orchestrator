# Project-owned policy and runtime gate

The user owns model/effort choices for the lead. Worker means any separate implementation or review session. Never treat a more capable model as permission to lead, spend or deploy.

## Files and ownership

Use `docs/orchestration/policy.json` for confirmed limits; `status.md` for current role/owners/version/next action; `improvements.jsonl` for experiments; `metrics.jsonl` for dated observations. Policy retains `schemaVersion: 1`; new metric/trial events use v2 in [records](records.md). Legacy events stay immutable. Link the existing registry/evidence; do not build another backlog. Do not store secrets or account identifiers.

The packaged [policy template](../assets/policy.template.json) is deliberately UNCONFIRMED. Copy/adapt only in an authorized project; ask the user rather than treating its empty fields as defaults.

Required policy:
- `schemaVersion`: 1; `projectId`: nonempty stable project label.
- `mainSession.modelEffortOwner`: user.
- `delegation.mechanism`: sessions or subagents, explicitly confirmed; `delegation.models`: nonempty unique list of model IDs with effort policy.
- Each model has `effort.mode`: allowlist with nonempty unique `values`, or all_supported with no values. The latter must be expressly approved; it does not mean every runtime supports every effort.
- `budget.mode`: unconfirmed, no_self_imposed_cap or capped. Unconfirmed blocks. Capped requires nonempty `limits`: metric tokens or money, positive finite amount, unit token for tokens or a three-letter currency for money, and scope task or increment. No-self-imposed-cap takes no limits. Limits do not authorize purchases; monetary and token quantities cannot be converted by this checker.
- `permissions.smallDirectWork`: boolean; `permissions.externalActions`: separate_authorization.
- `confirmation.status`: confirmed, with nonempty timestamp `at` (timezone required) and `evidence` identifying the user's actual decision. A timestamp or user-looking string alone is not authenticated consent.

The schema intentionally contains no hardcoded models, machine paths, glossary or global budget. User-confirmed project policy can vary. Unknown fields/versions are rejected rather than silently changing meaning.

## Per-objective capability choice

Policy v1 governs authority and worker limits; it does not own the skill/plugin selection for a task. For every new user objective, the lead records a capability choice in the existing task record or packet, without changing policy v1 or records v2. Record whether the choice was explicit or `Auto`, the smallest selected skill/plugin set, observed versions and capabilities, conflicts checked, and the fit reason. `Auto` means the smallest appropriate set that is actually available in the current environment; it is not permission to install anything.

Follow-up steering, ordinary follow-ups and internal dispatch inherit the parent objective's choice. If no user-confirmed explicit choice or `Auto` choice exists, or the recorded choice conflicts with the current objective, ask the user for explicit skills/plugins or `Auto` before dependent work; do not assume `Auto`. Re-select only when the objective, requirements, environment or availability materially changes. A selection must not grant installation, data transmission, spending, deployment or release authority; those remain separately authorized. If an explicitly requested capability is unavailable or conflicts with a required constraint, preserve the failed check and ask about the material scope choice rather than silently expanding permissions.

## Read-only checker

Run with a policy path:
```sh
python scripts/check_policy.py --policy /project/docs/orchestration/policy.json
```
A valid config result is `policy_valid`; it is NOT a dispatch permit.

Before dispatch, supply all four selection options (including the expected project ID):
```sh
python scripts/check_policy.py --policy /project/docs/orchestration/policy.json --model model-a --effort high --runtime /temporary/runtime.json --project-id example-project
```

Runtime inventory is an observed, current tool/model capability snapshot:
```json
{"mechanisms":["sessions"],"models":[{"id":"model-a","efforts":["medium","high"]}]}
```
The orchestrator obtains this from the actual environment, not from policy or model-name guesses. Keep capture time, source/version and observed capability in the task evidence. For consequential choices, use a version-matched current source and actual runtime behavior; a check date or version label alone is not a freshness guarantee. The checker cannot prove an inventory is fresh or authentic.

Exit/status:
- 0: policy_valid, or selection_valid when expected project ID, selection and supplied runtime match.
- 2: needs_input — missing/malformed/unconfirmed policy, conflicting fields or incomplete selection arguments.
- 3: rejected — policy belongs to another expected project, or worker model/effort is outside confirmed limits.
- 4: unavailable — no valid runtime inventory, mechanism or selected model/effort is available.

Evaluation output is JSON to stdout; the checker never writes project files, dispatches or changes settings. It checks configuration consistency, not sandbox enforcement, approval authenticity, spend forecasts, role assignment or deployed capabilities. Do not use a successful result to bypass these responsibilities.

## Missing limits, change and recovery

At first activation, group only unresolved policy questions: allowed models, effort limits, coordination mechanism and budget stance. The user may explicitly allow all runtime-supported efforts or decline a self-imposed cap; do not infer either. Save confirmed answers with a decision reference before execution. Do not ask again when valid policy already answers.

If an explicit current instruction changes policy, reconcile before dispatch; do not continue from stale approval. Session workers cannot expand policy. If a path/identity is uncertain, resolve it read-only before acting.

After a runtime error, stale snapshot or version mismatch, refresh relevant capabilities from the actual runtime and version-matched source, then revalidate. Stable facts do not require repeated research merely because time passed. An unavailable allowed model may be replaced only by another allowed, available choice. Keep requested and observed model/effort distinct. Never change the lead's configuration.

## Selection result v2

Selection calls require --project-id from the actual task/project, not copied blindly from an arbitrary policy. A successful selection_valid is not a dispatch permit. Results include hashes of the exact policy/runtime bytes evaluated and notVerified fields for approval authenticity, runtime freshness, remaining budget and task creation authority. Errors retain distinct needs_input/rejected/unavailable statuses.

For capped policy, budgetCheckRequired remains true: obtain adequate actual usage/remaining-capacity evidence before a capacity-consuming start. Missing data is a blocker for that decision, not zero usage or permission to spend; read-only preparation may continue. No self-imposed cap means no invented cap, never purchase/reset authority.

Before dispatch, record runtime capture time/source in task evidence and reconcile against currently exposed capabilities. The checker cannot establish freshness or trust. Historical dispatch_allowed outputs belong to the initial unpublished checker; do not reinterpret them as v2 evidence.
