# Implementation, integration and diagnosis

## When to apply and what to read

Use the implementation path for a code/configuration change and the diagnosis path for an unexplained failure or repeated failed repair. Start with the agreed behavior and examples, current source revision, relevant repository instructions, actual callers, existing checks and any observed failure evidence. Decide the next implementation or discriminating check and the observation that would support continuing. Enough evidence means the affected outcome is verified or the remaining uncertainty has an explicit next action. For a small known fix, use the relevant inspection, change and check; do not create a new plan or log format.

## Choose an action with useful feedback

For a consequential unknown, identify the smallest observation that could distinguish the plausible explanations or change the next decision. Select the existing tool that can produce it; inspect the relevant interface/help and installed version if inputs or behavior are unclear. A successful call proves neither useful coverage nor a successful product action.

Use scoped searches, filters, ranges or pagination when available. Retrieve enough surrounding context to interpret a match and preserve identifiers needed for the next action. If output is cut off, follow its continuation or narrow the query; do not treat unseen results as absent. Classify an empty complete result, tool error, unavailable environment and ambiguous side effect separately. Use a safe corrected query for invalid arguments, or reconcile side effects through [recovery](handoffs.md#resume-and-communicate) before retrying a mutation.

Read the actual observation, compare it with the expected discriminator, then implement, inspect further, revise the hypothesis or stop dependent work. Prefer existing deterministic checks for mechanically decidable behavior. Missing test access, misleading tool feedback or an unavailable dependency is an environment gap to diagnose, not a reason to repeat prompts or claim success. Add a new tool or dependency only under actual task scope when a concrete recurring need warrants it.

## Implement a complete slice

Inspect current structure, conventions, contracts, dependency/tool versions and affected callers before editing. Use local/version-matched documentation where behavior matters; do not apply remembered API behavior against a different installed version. Preserve unrelated changes and established ownership boundaries. Resolve a material design question through [system design](system-design.md), not an unannounced refactor.

Choose a usable vertical slice through the affected layers. Before broad implementation or a full test matrix, exercise its smallest real caller path and a material failure path. A mock can isolate a hypothesis but cannot establish integration. If the first caller fails, diagnose before expanding. [Product delivery](product-delivery.md#sequence-complete-increments) owns increment priority; [handoffs](handoffs.md#ownership-and-integration) owns write scopes and integration ownership.

For API/schema/dependency changes, identify affected producers/consumers and whether old/new versions can coexist during the intended transition. Keep the current contract where possible; otherwise record the authorized compatibility decision, update affected callers and verify the transition. Data migration and release recovery follow [product operations](product-operations.md#handle-data-and-recovery). A local helper change does not require a versioning platform or migration framework.

Add a mechanism only when the flow or diagnosed cause requires it. Keep the patch readable in the repository's conventions, with a clear owner for rules and errors. The output is the bounded integrated slice plus linked acceptance evidence and known limitations in the existing task record. Select checks through [evidence and challenge](evidence-and-challenge.md#choose-evidence-by-risk); compiling or passing each component separately is not the integrated outcome.

## Diagnose before repairing

Record the symptom, expected behavior, actual behavior, affected scope and conditions: source/environment, inputs, timing or state needed to reproduce. Preserve the initial error or failing check before changing the system. Sanitize evidence according to [evidence rules](evidence-and-challenge.md#research-only-decision-changing-facts).

Develop plausible, falsifiable explanations from that evidence. Choose the smallest check that distinguishes them: inspect a boundary value, trace the real caller, vary one relevant input, compare a working case or measure the suspected resource. State what observation would support or reject the hypothesis. Avoid adding multiple speculative fixes before learning which cause is present.

After a supported repair, repeat the original scenario and the regression checks implied by the cause and affected callers. If the symptom disappears without a discriminating observation, report the remaining causal uncertainty. When reproduction is unavailable, distinguish an **unverified hypothesis**, a **mitigation** that reduces impact, and a **demonstrated cause** supported by evidence. Record what remains needed and its effect on acceptance; never call a workaround a proven root-cause fix.

Use the canonical [review and repair limits](handoffs.md#review-and-repair), including earlier reassessment and the two-failed-repair boundary. Diagnose cause, scope or verification before another attempt; time spent or failure alone does not justify more effort, a new owner or another session. Model/effort choices stay under [policy](policy.md#capability-choice-and-adaptive-allocation).

Carry the evidence into the next decision: continue a supported repair, revise a disproved approach, perform an authorized mitigation, or stop dependent work with a clear owner and missing observation. Feed only generalizable process findings into [improvement](improvement.md#locate-the-problem); a product defect need not become a new orchestration rule.
