---
name: project-orchestrator
description: Use when product work has consequential requirements, design, integration, diagnosis or acceptance decisions, or needs coordination, takeover or recovery across sessions. Defaults to authorized subagent coordination; honor solo choices and keep clear low-risk edits direct.
---

# Project Orchestrator

Turn the user's objective into a useful, well-designed, verified outcome. Quality, authority, truthfulness and data safety are mandatory; optimize time, resources and maintenance cost within them. This skill grants no permissions or model access and creates no background work.

## Execute the next useful step

A small, clear, bounded, authorized change needs an edit, a relevant check and a truthful result. Do not manufacture delegation, policy files, handoffs or measurements for ceremony.

For substantive work, use this decision loop; it is not a requirement to write a report at every step:

1. **Establish the outcome:** current user requirement, scope, authority, applicable execution choice, consequential quality conditions and evidence needed to finish. Use [startup](references/policy.md#start-with-existing-authority) to resolve action-relevant gaps and [execution mode](references/policy.md#execution-mode-and-lead-responsibility) before substantive implementation.
2. **Get the needed context:** current source/caller, applicable constraints and the unresolved decision. Load only the matching reference below. Add context when a new decision, missing input or contradiction requires it; do not read the entire skill or project history by default.
3. **Act and observe:** choose the smallest useful implementation or uncertainty-reducing step. For a consequential unknown, identify what observation would change the next action; inspect the actual result before expanding. Use [implementation and diagnosis](references/implementation-and-diagnosis.md).
4. **Decide from evidence:** continue, repair using a supported explanation, revise the approach, or stop dependent work with its missing input and next action. Check the integrated outcome against the current requirement before declaring completion.

Keep the requirement in the existing product/task record, continuity in one current checkpoint when needed, and proof in versioned artifacts. A current user instruction can establish a requirement or scoped authority immediately; [agent claims still need evidence](references/evidence-and-challenge.md#distinguish-instructions-records-and-observed-behavior).

## Read only the relevant contract

| Decision that needs support | Read |
| --- | --- |
| Need, priority, business rules, usable journey or value feedback | [Product delivery](references/product-delivery.md) |
| Responsibilities, contracts, state, trust, scale or recovery boundaries | [System design](references/system-design.md) |
| Repository change, useful tool feedback, integrated slice or unexplained failure | [Implementation and diagnosis](references/implementation-and-diagnosis.md) |
| Evidence strength, quality criteria, conflicting claims or acceptance | [Evidence and challenge](references/evidence-and-challenge.md) |
| Authorized release, migration, operated-product impact or restoration | [Product operations](references/product-operations.md) |
| Assignment, shared context/resources, interruption or takeover | [Handoffs](references/handoffs.md) |

Select relevant available skills/plugins within current authority without asking for an explicit/Auto preference. Honor user selections and exclusions. Inspect fit to the task, version and tool environment; omit mismatched guidance and use current primary evidence. Missing specialist guidance does not remove the decisions above. See [capability and effort selection](references/policy.md#capability-choice-and-adaptive-allocation) for consequential gaps. Reading or loading a skill is not evidence it helped.

## Choose the smallest useful operating mode

Choose the route by the outcome and dependencies:

- Read-only investigation or a clear, bounded small edit: act directly and run only the relevant check.
- UI bug: one owner reproduces the visible failure, fixes its cause and checks the affected journey.
- Feature, state or contract change: give one owner the coupled caller, state and contract work end to end; split only work with independent inputs and useful outputs.
- Refactor: preserve the current behavior first, then check each affected caller against the refactored boundary.

For substantive work, [default to subagents when prerequisites are satisfied](references/policy.md#execution-mode-and-lead-responsibility), without a repeated mode question. The main session retains overall direction, shared decisions, integration and acceptance; a worker can own a bounded outcome through implementation and checks. Parallelize only work with independent inputs and outputs. See [handoffs](references/handoffs.md) for packet contents, shared-resource ownership, review and continuation.

Honor explicit solo work, chosen mechanisms and user-granted discretion. A worker owns its assigned scope and decisions, not overall direction. Ask before changing to independent sessions or taking on all implementation unless an applicable choice already covers it; missing prerequisites do not silently select solo. The user controls main-session model/effort. Workers use [`gpt-6-luna` with adaptive effort](references/policy.md#capability-choice-and-adaptive-allocation), subject to confirmed policy/runtime and a later explicit user change. They resolve implementation details in scope and return decisions beyond the packet with evidence; uncertainty does not automatically select a stronger model or maximum effort. Keep dispatch scope, source, delegated decisions, shared resources and evidence compact in the existing [packet](references/handoffs.md#dispatch).

Use [handoffs](references/handoffs.md) for one writer per conflicting scope/resource, uncertain dispatch, requirement changes and recovery. Reconcile identity and side effects before retrying. A stopped turn need not stop a writer process; late results retain their original attempt and revision. Compaction or new IDs do not reset authority, open failures, acceptance or repair history.

## Verify and report

Match each material criterion to relevant evidence on the applicable revision. For substantive changes, the owner selects checks for affected objects, sources, entrypoints and related risk branches, then returns the project's [source-bound verification summary](references/project-verification.md#select-checks-and-hand-over-results). Use actual compact tool results, relevant selectors and exact commands to establish what ran and what it covered; a worker's “done” summary is a claim, not evidence. A successful call alone does not prove the intended action or outcome. For confirmed mechanically checkable material bugs, the regression must fail for the defect on the original source snapshot and pass on the corrected snapshot; see the [canonical procedure](references/implementation-and-diagnosis.md#diagnose-before-repairing) and put that outcome in the dispatch packet. Individual component passes, agreement among agents and an idle notification do not establish integrated acceptance. Changed source, requirements, dependencies or check configuration invalidate affected proof; reuse unaffected proof only with a supported comparison.

Independent review remains required for persisted-data/security/shared-contract changes, difficult recovery, contradictory evidence or project-defined risks. Solo work may produce an authorized self-checked candidate or PR while required review and acceptance remain open. Keep technical verification, independent review, release and observed user value distinct. See [handoffs](references/handoffs.md#review-and-repair) for the reviewer repair loop. GitHub Draft/non-draft is a separate publication choice.

Report meaningful results, material decisions/blockers and evidence limits; keep unchanged optional narration quiet and honor platform-required updates. Never relabel failed, skipped, stale or unrun checks as passes.

At task closure, when the user, main session or reviewer confirms a material miss, apply [miss closure](references/improvement.md#close-once). A new or changed requirement is not itself a miss.

## Supporting decisions, only when needed

Use [worked examples](references/worked-examples.md) for an unclear decision, [records](references/records.md) for optional measurement/reporting, [improvement](references/improvement.md) for a reusable workflow defect, [maintenance](references/maintenance.md) for skill lifecycle and [contributing](references/contributing.md) for an authorized source change. Research reports and evaluation rubrics are maintainer evidence, not routine execution context. No automatic installed-copy update, personal-memory write or follow-up schedule.

For substantial product work whose existing checks do not prove a real user journey, follow [project verification bootstrap](references/project-verification.md). Small edits and read-only work use adequate existing evidence without creating a verifier or local infrastructure.
