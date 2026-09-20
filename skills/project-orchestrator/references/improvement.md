# Bounded improvement

Use `observe -> diagnose alternatives -> smallest change -> verify -> keep/revise/revert/defer`. Apply the outcome constraints in [SKILL.md](../SKILL.md); more roles, documents or lower token counts are not success by themselves.

## Locate the problem

Start from the [diagnostic evidence](implementation-and-diagnosis.md#diagnose-before-repairing) or observed outcome and distinguish product/requirement, implementation, tooling, verification and coordination causes. Keep an unresolved cause labelled as a hypothesis. A failed product test does not by itself establish a skill defect. A passing package test does not prove useful orchestration.

Place code defects in code/tests, project conventions in project guidance, and generalizable decision or coordination lessons in this skill. Before adding a rule, state when it applies, the recurring cause it addresses and a counterexample where it should not trigger. A user correction can supply a requirement; do not treat one local example as universal evidence or write personal memory without explicit permission.

## Choose the smallest adequate check

A reversible wording correction can use consistency review and relevant existing checks. A CLI change needs deterministic behavior tests. A claim about actual multi-session behavior needs actual authorized sessions; role-play cannot establish it. A claim about comparative efficiency needs suitable comparison and disclosed limits.

Do not automatically open a paired experiment, product pilot, new role or separate retrospective for every change. If required independent review is unavailable, deliver the authorized candidate with that gate pending rather than inventing review.

For a real process trial, use existing v2 records to name one intervention, owner, preserved quality, measurement, rollback condition and closure trigger. Reuse the current handoff and evidence index. Keep candidate guidance separate from installed guidance until an authorized adoption boundary.

## Prepare independent behavioral evaluation when authorized

Package validation, author decision inspection and independent task execution answer different questions. Keep their results separate. If independent execution is outside current authority, record it as not run; prepare useful scenarios without launching sessions, a product pilot or a follow-up schedule.

For a future authorized evaluation, give the evaluator a realistic request, the candidate skill and the minimum raw artifacts in an isolated scope. Keep the expected decision/rubric with the assessor, not in the worker packet; omit the author's preferred diagnosis or verdict. Include cases where guidance is needed and counterexamples where direct work should remain small. Judge the resulting artifact and actual end state against unchanged acceptance; use the trace to diagnose omissions, unnecessary questions, context loss, authority errors and integration failures. Retain failures, intervention and unknown measurements.

An independent review of prose is not an execution test. A comparison claim additionally needs comparable inputs, environments and acceptance on the old/new guidance, with variation and limits disclosed. Do not infer efficiency or reliability from one successful case. Use [evidence](evidence-and-challenge.md#challenge-consequential-premises) for the strength of each claim.

## Measure useful progress

Check the accepted outcome, design tradeoffs, defects, rework, takeover, main intervention, elapsed time and usage where observed. Distinguish technical acceptance, observed user value, process adherence and trial criteria. Use the [product feedback loop](product-delivery.md#observe-value-and-decide-next) for user-value evidence; do not duplicate it in a workflow experiment. Explicit main takeover may rescue a product while failing a delegation-specific criterion.

Apply the [canonical reassessment and repair limits](handoffs.md#review-and-repair). Use the diagnosed cause to continue, revise or stop the approach; do not add a role, process or effort increase merely because one attempt failed.

Inspect whether communication changed a decision or supplied missing proof. Remove demonstrated duplication, obsolete assignment wording or out-of-scope trial detail; keep a rule when it preserves a necessary decision or safeguard. If usefulness is uncertain, state that limit and load the guidance only where applicable rather than claiming a measured benefit from deletion. Reuse valid evidence. For token, cost and allowance accounting, use [records](records.md#metrics-jsonl); missing measurements stay unknown.

## Close once

At the existing task closure, briefly assess diagnosis, adequacy of measurement and whether process work was proportionate. Do not open a separate review of that assessment.

For recorded trials, close with adopted, revised, reverted or deferred as defined in [records](records.md). Adoption must state its demonstrated scope. A deferred result names missing evidence and a future event, not a background schedule. A stopped or accepted task must not leave its trial silently active.

Removing a step, role or rule is a valid outcome. Preserve the prior guidance and reason for the change. Improvement does not authorize weaker acceptance, new permissions, changed model limits, publication or installed-copy updates.
