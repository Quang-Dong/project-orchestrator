# Coordination and handoff

## One current record, one writer

Use the existing registry IDs; do not create another backlog. The lead alone updates the current coordination table in project status.md. A worker writes its own handoff in its assigned scope. Each row records task ID, owner, actual write directory/scope, input revision, attempt ID, state, latest event/evidence and next action. Keep the table small: active work and the last accepted checkpoint; link older evidence.

States:
- planned: authorized work specified, no dispatch started.
- dispatching: attempt ID recorded before a create/send call.
- assigned: tool returned a task identity, execution not yet observed.
- running: actual execution/owner activity observed.
- blocked: known missing dependency, authority, capacity or execution failure; owner and recovery action recorded.
- ready_for_review: frozen handoff with self-checks received.
- accepted: acceptance evidence on that revision reviewed by the responsible lead/reviewer.
- cancelled: explicitly stopped/superseded attempt; preserve reason and any unfinished work.

Write attempt ID into the dispatched packet. On an uncertain tool response or timeout, inspect available task state and reconcile identity/attempt before retrying. An ambiguous outcome stays unresolved, never a second blind dispatch. No known ID: inspect recent tasks for the attempt marker; inability to resolve means record the blocker. Do not treat no response as cancellation.
Before changing owner, establish the old writer has stopped or isolate the new scope. Keep the old attempt as historical. Late output from it is evidence for review, never authority to overwrite current state.
Reconcile at assignment, result, tool failure and takeover. Use supported event waits while a lead is active; no scheduler or background monitoring is implied.

## Packet and handoff

Packet: existing task ID, attempt ID, owner, observable outcome, risk, authorized directory/changes, versioned inputs, dependencies, unchanged acceptance, escalation conditions and requested model/effort. For product work, link the outcome frame in [product delivery](product-delivery.md); for material evidence disputes, link the raw sources and labels from [evidence and challenge](evidence-and-challenge.md). Ambiguous/high-risk work needs a brief receiver restatement; routine reversible choices inside scope do not need approval.

Before judging a result, identify the lifecycle stage and artifact/revision under review: discovery, specification, implementation, release, operations or retirement. Planned but unimplemented behavior is not an implementation regression; record a specification or scope gap separately. This is a review guardrail, not evidence that it prevents reviewer mistakes.

Handoff: actual directory, frozen revision/manifest, changed scope, commands/results, evidence links, remaining gaps, affected acceptance, carried evidence with source comparison, observed settings and source (or unknown), stopped-writer confirmation and next action. Distinguish checkpoint, ready for review, blocked, failed and not run. Missing revision/proof cannot establish acceptance.

The author owns a complete artifact at the frozen revision before requesting `ready_for_review`. For every acceptance criterion, provide the relevant source/revision, check or observation, result and limitation; if it was not checked, mark it unknown or pending rather than implying completion. Use one shared-check entry when a criterion applies identically to the artifact, and per-cell evidence only when the criterion varies across a declared matrix. A matrix used in one task is not a universal requirement for unrelated work.

Default internal messages to plain technical English and user communication to the user's language. Preserve glossary, IDs and authored content. Link only relevant sources; don't paste full logs/history. Language and length may be trialled without losing meaning. Do not omit revision, failure, local-fixture or unknown markers to make a handoff sound complete.

## Review and resume

The lead reads the short handoff first, then expands inspection depth according to risk, affected criteria, gaps and contradictions. Independent reviewers read frozen files and do not race author edits. A later change invalidates affected evidence; either recheck it or keep acceptance pending. Do not change tests to fit results.

A new lead/worker verifies role, actual directory, current owner/attempt, policy and source revision before edits. Read current state and linked active trials, not all historical logs. Do not promote local tests, emulators, prototypes or AI roleplay into production or real-user evidence.

For a repetitive context problem, shorten the linked current record or start a fresh authorized task with a frozen handoff. Do not open extra sessions solely to avoid reading the critical evidence.

## Current state and evidence storage

Record an ownership/start event before the first edit after transfer, not during final reporting. Keep only active rows and the latest accepted checkpoint in status; link a closed attempt instead of copying its narrative forward. Effective project guidance must name its adopted scope and evidence; proposed/deferred trials are not active instructions. Workers read their packet and necessary policy; do not require every worker to load the entire project log.

During a documented path migration, keep exactly one writable policy/status. Preserve original bytes in a verified archive and provide an old-path-to-archive-entry map for historical evidence. Do not rewrite old evidence references to pretend they were originally produced at the new location. Candidate code and one-off build scripts belong in temporary development workspaces, not normal project records.
