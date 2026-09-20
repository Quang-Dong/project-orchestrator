# Product release and operations

## When to apply and what to read

Use this reference when an authorized change can reach users, alter persisted data, or affect an operated product. Start with the affected flow, release environment and authority, acceptance evidence, compatibility obligations and known operational constraints. Keep the result in the existing task/release record; this creates no new release schema or automatic monitoring.

For a local tool or prototype, use its actual distribution, data and recovery boundary. A local file-changing tool may still need recovery checks; it does not automatically need cloud deployment, telemetry, service-level objectives or an on-call system. [Maintenance](maintenance.md) separately owns the skill's versions, distribution and installation.

## Decide release and stop conditions

Before an authorized release, name the owner, applicable acceptance/review gates, intended scope and conditions to proceed or stop. A green build cannot close integration, user-value or required independent-review gates; use [evidence](evidence-and-challenge.md#choose-evidence-by-risk) and the existing product contract. If a prerequisite is missing, state the dependent release limit and next action.

Choose the smallest post-release check that exercises the affected real flow and the signal that would reveal material harm. Name who inspects it and the next observable event, such as the authorized release smoke check or an existing operator review. Use existing logs, support reports or measurements where adequate. Define the response to failure: stop rollout, disable the affected path, roll back compatible code, restore data or apply a forward repair as actually supported. Do not promise recovery that has not been checked at the needed scope.

Release, production data changes, external communication, telemetry collection, spending and unattended scheduling each remain subject to existing authority. A plan, worker handoff or this reference grants none of them. Record an owner/event for future work without claiming monitoring will run by itself.

## Handle data and recovery

For a data change, inspect old/new reader and writer compatibility, migration preconditions, partial failure behavior and what happens to writes during the transition. Identify any irreversible transformation or loss of information before execution. Decide the recovery path and stopping point with the responsible owner; do not assume rolling back code restores migrated or deleted data.

When acceptance depends on recovery, verify the relevant restore, reversible migration or forward-repair path on representative safe data and record its scope and limits. A backup file's existence is not proof that restoration works. If recovery is unavailable or unproven, leave that condition open and resolve the release decision before dependent mutation. The design, migration and recovery evidence must refer to compatible revisions; see [system design](system-design.md) for the data owner and failure boundaries.

Retain only needed recovery artifacts under the product's data/privacy rules. Address support, retirement or migration obligations when this change creates them; do not invent a separate lifecycle program for a bounded edit.

## Observe impact and decide the response

Use relevant measurements to assess runtime reliability, performance and cost, with source, workload, environment and measurement limits. Keep estimates separate from observed results. When no baseline or access exists, record the gap and acceptance impact; do not infer production savings from a local check or introduce new infrastructure merely to collect a number.

At the agreed event, compare the affected flow and preserved quality with expectations. A harmful signal leads to the authorized stop/recovery action and [diagnosis](implementation-and-diagnosis.md#diagnose-before-repairing). Operational health and technical acceptance do not prove usefulness: route user-value evidence through the [product feedback decision](product-delivery.md#observe-value-and-decide-next). Record what happened, remaining limits and the next owner/action in the same task/release record.
