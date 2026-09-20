# Product delivery from idea to outcome

Use this reference when a request changes a user-facing flow, product behavior, data/state, acceptance, or an operational outcome. A small defect may need a short outcome statement and one relevant check. For substantial product work, use the decision loop below in the existing requirement/task record, referencing what is already known. If no registry exists, create one minimal authoritative outcome/spec record in the project's normal documentation location with an owner and acceptance; do not create a second backlog or mandatory form.

Apply the outcome constraints and operating modes in [SKILL.md](../SKILL.md). This reference owns product decisions, early caller checks and increment sequencing; [handoffs](handoffs.md) owns coordination mechanics.

## Choose the problem

State who acts, who benefits, the observed problem or opportunity, and the evidence with its date and limits. Explain why this problem merits the next increment relative to current work: expected user value, urgency, uncertainty, dependencies and cost of delay where known. A short qualitative reason is sufficient; do not invent scores to rank uncertain work.

Identify the assumption most likely to change the solution or make it unnecessary. Ask about missing material authority, requirements or irreversible tradeoffs before implementation. Do not invent a persona, metric, customer need or production constraint. Interviews, observed usage and authorized experiments have their own populations and limits; simulated users, fixtures and role-play do not establish real demand.

## Choose the smallest useful step

Choose the smallest step that delivers the intended value or resolves the most consequential uncertainty. A focused research result, prototype or no-code experiment can be a complete increment with an observable answer; it need not produce production code. State how that answer changes the next decision, and keep any external research/contact within existing authority.

For a software increment, specify observable behavior:

1. Primary flow and important alternate/error flows.
2. Data, state transitions, invariants and ownership of each state.
3. Exclusions, non-goals and deferred behavior.
4. Acceptance checks against the real artifact or a clearly labelled local fixture.

Acceptance covers relevant negative paths such as refusal, missing data or stale state. A passing mock, prototype or unit test proves only its layer, not integration, deployment or user value.

## Define success before expanding

For substantial product work, identify one primary signal of user value, the technical acceptance checks, and the quality conditions that must not regress. The value signal describes an observable user/operator outcome and its evidence source. If its baseline or target is unknown, record that gap and how to observe it; do not fabricate a percentage, time saving or business result. Use an agreed qualitative observation when numerical measurement is not appropriate.

Keep these decisions in the product contract. The coordination checkpoint owns the current owner, attempt, source revision, write scope and recovery; the artifact/proof owns actual behavior and caller checks. Use the existing boundaries, not another schema or registry. Chat history supplies context, not acceptance evidence.

## Choose sufficient architecture

Prefer the smallest design that satisfies the current flow and preserves a clear boundary for likely change. Name a material alternative only when it changes risk, cost, quality, reversibility or ownership. For a risky design assumption, identify an observable check. A measured experiment may express it as:

`If [bounded change], then [quality or cost signal] will change by [measurable direction/threshold] for [scope], while [quality to preserve] does not regress.`

Do not add a framework, service, schema, queue, persistence layer or coordination role without a demonstrated need in the specified flow. Keep product rules in their owner; use replaceable adapters for storage or external systems when that is the existing boundary.

## Sequence complete increments

Give each increment one authorized owner, a bounded scope and observable acceptance. Keep coupled work with an end-to-end owner; add an integrator only when distinct outputs need it. Before broad implementation or a full matrix, exercise the smallest real caller path across the affected boundaries, including a material failure path. If it fails, diagnose before expanding.

Prefer finishing or unblocking current increments before starting more dependent work. When existing work is blocked, an authorized independent increment can proceed if its owner, priority and integration path are clear. Parallelize only independent work with disjoint writes. Use [handoffs](handoffs.md) for ownership and takeover; individual passes do not prove the combined result.

## Observe value and decide next

At handoff, report technical acceptance and observed user value separately. A technically accepted increment can close within its technical scope while value remains unverified. User-value criteria and any overall acceptance that depends on them stay open; do not narrow the agreed contract to claim completion. Retain the open product question without relabelling technical evidence. Pending technical or independent-review gates remain pending.

For the primary value signal, name the feedback source, responsible owner and next observable review event in the existing product record. Examples include an authorized usage observation, a support finding or the next customer review. If access or authority is missing, state the dependency. This is a handoff for a future authorized action, not a scheduler or permission to contact users, collect telemetry or monitor unattended.

Use the observed signal and preserved quality to decide: continue when evidence supports the next step; adjust when the need remains but the approach misses it; defer when evidence or authority is missing; stop when the premise is disproved or further investment is not justified. Record the reason and any unresolved question. These are product decisions, not new workflow-record event types or an automatic adoption of a skill experiment.

## Release and lifecycle, only when applicable

For a change that can reach users or affect operations, identify the authorized release gate, rollback/recovery action, monitoring signal, support owner and retirement or migration obligation. If none applies, say so. Release, production mutation, external communication, spending and installation updates require their own authority; a product design or worker handoff cannot grant it.
