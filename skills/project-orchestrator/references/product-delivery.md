# Product delivery from idea to outcome

Use when a request changes product behavior, business rules, a user journey or the evidence of value. Inputs are the current user request, observed need, affected flow and constraints. Decide the smallest useful delivery or uncertainty-reducing step, with acceptance and a feedback source; this is enough to proceed. A small defect needs its outcome and relevant check, not every section below.

Keep consequential decisions in the existing product/task record. If none exists and continuity requires it, use one minimal record in the project's normal location; do not create a competing backlog or mandatory form. [Handoffs](handoffs.md) owns coordination; [evidence](evidence-and-challenge.md) owns proof strength. Product knowledge guides the result without requiring an agent to imitate organizational roles.

## Choose the problem

Separate the requested solution from the problem it is meant to solve. State who acts, who benefits, the observed problem or opportunity, and the evidence with its date and limits. A requested feature is evidence of a request, not proof of demand or the best solution. Explain why this problem merits the next increment relative to current work: expected user value, urgency, uncertainty, dependencies and cost of delay where known. A short qualitative reason is sufficient; do not invent scores to rank uncertain work.

Identify the assumption most likely to change the solution or make it unnecessary. Ask about missing material authority, requirements or irreversible tradeoffs before implementation. Do not invent a persona, metric, customer need or production constraint. Interviews, observed usage and authorized experiments have their own populations and limits; simulated users, fixtures and role-play do not establish real demand.

For a consequential product choice, distinguish value (will it solve a supported need?), usability (can the intended user complete and recover the journey?), technical feasibility (can the constraints be met?) and business/operational viability (can it be distributed, supported and maintained within actual commitments?). Examine only the risks that can change this increment; a small local fix does not need a business case or cloud operating model. Unknown support cost or organizational constraints stay unknown, with their acceptance impact and the owner of the missing decision. This selectively applies [SVPG's four-risk framework](https://www.svpg.com/four-big-risks/), not evidence of demand or a requirement to invent a business model.

## Choose the smallest useful step

Choose the smallest step that delivers the intended value or resolves the most consequential uncertainty. A focused research result, prototype or no-code experiment can be a complete increment with an observable answer; it need not produce production code. State how that answer changes the next decision, and keep any external research/contact within existing authority.

## Resolve requirements and business rules

Apply when a slice changes behavior, permissions, state or data. Read the existing product contract and actual caller behavior before resolving:

- Who can act, on which resource, with what preconditions and permissions?
- What is the main flow, and which alternate, refusal or failure paths matter?
- What state changes, who owns it, and which data rules must hold before and after the action?
- Which exceptions, exclusions and deferred behavior constrain this slice?

Attach a concrete acceptance example to each consequential rule: starting state and actor, action, expected result and what must remain unchanged. For example, an unauthorized edit must leave stored data unchanged. Use fictional fixtures and label assumptions; examples clarify the contract rather than silently add requirements.

When two requirements conflict or a missing decision changes permissions, irreversible behavior or acceptance, identify the conflict and stop its dependent edits until resolved. Keep independent authorized work moving. Do not infer a new permission from a UI control, or broaden a small correction into a new business flow.

## Check the user journey

Apply to a new or changed interaction, using the affected actor, target device and entry state from the product contract. Trace entry point -> action -> feedback -> resulting state -> next action. Check whether the user can understand progress, finish the task and recover from a consequential failure.

Select relevant empty, loading, denied and error states; preserve entered work where required and make retry, cancel or recovery consequences clear. Include keyboard navigation, focus placement and layout on the target devices when affected. A working happy path alone does not establish a usable journey. A wording-only edit does not require redesigning unrelated screens.

For UI changes, inspect the running interface through the affected journey and material failure/recovery state. Link the observed result and remaining gaps to the acceptance examples, following [evidence selection](evidence-and-challenge.md#choose-evidence-by-risk). A screenshot or component test alone cannot establish interaction, focus or input preservation. If the runtime is unavailable, retain the unverified UI criteria rather than calling the journey accepted.

## Define success before expanding

For substantial product work, identify one primary signal of user value, the technical acceptance checks, and the quality conditions that must not regress. The value signal describes an observable user/operator outcome and its evidence source. If its baseline or target is unknown, record that gap and how to observe it; do not fabricate a percentage, time saving or business result. Use an agreed qualitative observation when numerical measurement is not appropriate.

Keep these decisions in the product contract. The coordination checkpoint owns the current owner, attempt, source revision, write scope and recovery; the artifact/proof owns actual behavior and caller checks. Use the existing boundaries, not another schema or registry. Apply the [source distinctions](evidence-and-challenge.md#distinguish-instructions-records-and-observed-behavior): a current user decision can change this contract; an agent completion claim needs evidence.

## Sequence complete increments

Give each increment one authorized owner, a bounded scope and observable acceptance. Prefer finishing or unblocking current increments before starting more dependent work. When existing work is blocked, an authorized independent increment can proceed if its owner, priority and integration path are clear. Use [handoffs](handoffs.md) for assignment, disjoint writes and takeover.

For material design decisions, use [system design](system-design.md); for an implementation slice and its early real-caller check, use [implementation and diagnosis](implementation-and-diagnosis.md#implement-a-complete-slice). Individual layer passes do not prove the combined result.

## Observe value and decide next

At handoff, report technical acceptance and observed user value separately. A technically accepted increment can close within its technical scope while value remains unverified. User-value criteria and any overall acceptance that depends on them stay open; do not narrow the agreed contract to claim completion. Retain the open product question without relabelling technical evidence. Pending technical or independent-review gates remain pending.

For the primary value signal, name the feedback source, responsible owner and next observable review event in the existing product record. Examples include an authorized usage observation, a support finding or the next customer review. If access or authority is missing, state the dependency. This is a handoff for a future authorized action, not a scheduler or permission to contact users, collect telemetry or monitor unattended.

Use the observed signal and preserved quality to decide: continue when evidence supports the next step; adjust when the need remains but the approach misses it; defer when evidence or authority is missing; stop when the premise is disproved or further investment is not justified. Record the reason and any unresolved question. These are product decisions, not new workflow-record event types or an automatic adoption of a skill experiment.

## Release and lifecycle, only when applicable

For a change that can reach users or affect operations, use [product operations](product-operations.md) for release, observation and recovery decisions. Its technical/operational checks do not replace the user-value feedback loop above. Skill distribution and installation have their own [maintenance](maintenance.md) boundary.
