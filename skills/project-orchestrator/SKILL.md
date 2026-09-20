---
name: project-orchestrator
description: Organize product-development sessions around useful outcomes, clear ownership, proportionate coordination and revision-bound evidence. Use when dependencies, takeover or consequential review need coordination; keep small low-risk work direct.
---

# Project Orchestrator

Organize product work around a useful, verified outcome. Correct user outcome, authority, truthfulness and data safety are mandatory. Choose sufficient design, verify usable slices early, and reduce avoidable coordination, rework and resource use on the path to acceptance. Judge allocation by outcome and observed cost, not the number of agents or their effort setting.

Design starts from the outcome and constraints; it is not a requirement to design the whole system before testing. This skill grants no model access, spending, dispatch, release or installation authority.

## Choose the smallest useful operating mode

- **Direct:** a clear, bounded, reversible change with low consequence and a relevant check may stay with one session when policy permits. A small behavior change is not automatically coordinated work. Data/security/shared-contract risk, uncertain recovery or ownership conflict requires the corresponding safeguards.
- **One end-to-end owner:** keep substantial, coupled work with one authorized owner across discovery, design, implementation and integration. Size alone does not require delegation or a new session.
- **Targeted delegation:** use independent review when required and authorized. For other delegation, identify an independent workstream or specific expertise/context need whose expected benefit justifies the coordination cost. Record that reason through the [dispatch contract](references/handoffs.md#dispatch); parallelize only independent work with disjoint writes within granted authority.
- **Explicit solo work:** honor a user's instruction to work alone without starting other sessions. Implement, self-check and hand off within authority. Self-review is not independent review; required independent acceptance remains pending.

The lead owns direction, consequential contracts, exceptions and acceptance. The end-to-end owner may be the lead or a worker only within the authority actually granted. Permission for `smallDirectWork` does not authorize all substantial solo work. If the chosen mode lacks authority or capability, stop its dependent actions and report the gap; keep separately authorized work moving. Ordinary coordination and short handoff inspection do not need another specialist.

## Read only the relevant contract

Use the project's confirmed policy, current status and linked requirement/evidence records. For model/effort selection and actual runtime support, read [policy](references/policy.md). The user controls the main session's settings. Honor explicit worker settings; otherwise use the task-based selection rule in that reference, without defaulting to maximum effort.

Keep three responsibilities distinct in existing records: the **project contract** owns goals and acceptance; the **coordination checkpoint** owns current owner, attempt and next action; the **artifact and evidence** establish what works at a specific revision. Conversation supplies context, not proof. Do not create a competing backlog, registry, SDK or background engine.

For product work, read [product delivery](references/product-delivery.md) to choose the problem, smallest useful step and feedback decision. Technical acceptance and observed user value are separate claims. Select only the lifecycle work the task needs; the reference owns early caller checks and increment sequencing.

## Own, hand off and recover

Use one writer per scope and one current handoff with linked evidence. Read [handoffs](references/handoffs.md) for dispatch, timeout, takeover and integration. Record an attempt before dispatch; observe actual settings after execution starts. Reuse unchanged capability evidence; refresh it when relevant conditions change.

Reuse a session while the work remains one coherent outcome. Prefer a new session for a distinct objective, independent review or demonstrated context confusion; use a fork for a genuine branch that needs inherited history. Length, elapsed time or compaction alone is not a restart trigger. Follow the [session-choice guidance](references/handoffs.md#continue-compact-fork-or-start-fresh) within the user's session-creation authority.

Authorized lead takeover is possible after stopping the old writer or isolating its scope, verifying the baseline and recording the reason. Report intervention honestly; it does not by itself fail product acceptance. A trial specifically measuring delegation may still fail its separate criterion.

Reassess when the first usable slice fails, diagnosis repeatedly proves wrong, or the lead must substantially redo specialist work. After two unsuccessful repairs of the same issue, diagnose again or stop with a handoff; a renamed packet or attempt does not reset that boundary. Do not lower acceptance to escape it.

## Verify and report

Authors self-check and freeze the artifact. Independent review is required for persisted-data/security/shared-contract changes, difficult recovery, contradictory evidence or other policy-defined risks. If unavailable, authorized implementation and a draft handoff/PR may proceed, but the required review and acceptance remain open.

The lead reads the short handoff and decisive evidence first; inspect further for risk, missing proof or contradiction rather than repeating all checks. Changed source invalidates affected proof. A green validator, a report or agreement among sessions does not prove product acceptance. Use [evidence and challenge](references/evidence-and-challenge.md).

Report meaningful outcomes, decisions, blockers and corrections. Keep unchanged optional narration quiet; comply minimally with mandatory platform updates. Do not hide failure or claim an unrun check.

## Improve only what evidence supports

Use [improvement](references/improvement.md) for a bounded reusable lesson; code defects belong in code/tests and project conventions in project records. Choose the smallest adequate validation, close once, and permit removal of rules or roles. Do not automatically require a paired multi-session experiment or product pilot for a skill edit. No silent skill update, personal-memory write or background follow-up.

Read [records](references/records.md) for policy v1/records v2 reporting, [maintenance](references/maintenance.md) for compatibility or installation, and [contributing](references/contributing.md) for an authorized source contribution. Draft PR delivery, independent acceptance, release and installed-copy adoption are separate outcomes.
