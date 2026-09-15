# Close the improvement loop

Observe → diagnose → one bounded trial → measure → adopt, revise, revert or defer.

Improve task boundaries, ownership, model/effort within policy, context, tools, communication purpose/content/language/length, handoff, tests, review and measurement. A reusable finding merits a short record; otherwise add no procedure. Distinguish requirements, communication, implementation, tooling, verification and coordination causes.

## Evaluate the improvement itself

Before closing a trial, evaluate three separate premises using the existing evidence, measurement and decision fields: whether the diagnosis is supported and alternatives were challenged; whether the measurement actually fits the claimed outcome, preserves acceptance, accounts for missingness and distinguishes shared checks from per-cell checks; and whether the added process cost (authoring, coordination, review, waiting and runtime usage) was proportionate to the value. Preserve unfavorable evidence and unknowns. A successful outcome with an unsupported diagnosis, weak measurement or excessive overhead is not proof that the process should be adopted.

Keep this meta-evaluation bounded: perform one process-quality review per trial closure, record the next observable review event, and defer or revert when the evidence is insufficient. Do not create an endless review-of-the-review loop. If the evidence supports simplification, removing a rule or choosing no delegation is a valid improvement; retain the reason and prior guidance so the change is reversible.

Use the [v2 record contract](records.md). Use [evidence and challenge](evidence-and-challenge.md) as the authority for fact/assumption/inference/unknown labels, decision-changing research and independent review. Use [product delivery](product-delivery.md) when a workflow improvement changes a user-facing outcome, acceptance or product boundary. Each trial has a bound task, owner, one intervention, preserved quality, measurement, rollback condition and reviewTrigger. Link active trial guidance from current project status so a replacement session can apply it without old chat.

When the bound task ends (accepted, cancelled or stopped), record a decision:
- adopted: evidence supports the stated scope and quality.
- revised: bounded approach needs a change; retain prior event and link the replacement.
- reverted: restore previous guidance because quality/meaning/authority regressed.
- deferred: missing evidence is listed and nextReview names the next observable review event; never imply success.

A task may finish while an inconclusive trial is deferred. Do not leave an applied trial indefinitely open without a reason. The reporter flags an accepted task whose latest trial event remains active; cancellation/stoppage also requires lead review.

Keep one attributable intervention per trial. Split combined proposals and link their origin. Compare suitable work with unchanged acceptance. Unknown/no baseline limits the conclusion; fewer tokens or one success alone does not establish superiority.
Do not overwrite unfavorable events. Remove redundant/obsolete rules when evidence supports simplification.

Within granted scope, a project may trial reversible guidance and restore it. It cannot alter product requirements, quality gates, model allowlists, budget or release authority. For reusable source changes, use [contributing](contributing.md); installations remain distributions, not the development source. This changes instructions and practices, not model weights.
