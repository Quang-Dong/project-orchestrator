---
name: project-orchestrator
description: Lead multi-step product work from a user idea to a verified outcome across sessions, ownership changes, consequential review, or measured workflow improvement. Do not activate for ordinary trivial edits that need no coordination or evidence workflow.
---

# Project Orchestrator

Version v0.1.0. Use the compatibility record when available; do not assume every environment, tool or model is supported.

Turn a user's idea into a useful, maintainable and verified product outcome. This skill supplies a method, not project authority, model access or guaranteed correctness. It is for work that benefits from an explicit outcome, durable context, bounded ownership and proportionate review.

## Select capabilities for each new objective

For each genuinely new user objective, record the scoped skill/plugin choice in the existing task record or packet before dependent work. A choice is either the user's explicit selection or `Auto`, where the lead selects the smallest appropriate available capability set. Record the selected names, observed versions/capabilities, conflicts checked, and the reason they fit the objective. Do not add these fields to policy schema v1 or records schema v2.

Steering messages, follow-ups and internal dispatch inherit the parent objective's choice. If no user-confirmed explicit choice or `Auto` choice exists, or the recorded choice conflicts with the current objective, ask the user before dependent work; do not assume `Auto`. Re-select only when the objective, requirements, environment or capability availability materially changes. A version label or check date is not proof of current capability; use the actual runtime and version-matched sources for consequential choices. Selection never grants installation, data transmission, spending, deployment or release authority.

## Start with the user's outcome

Classify the request before adding process:

- **Small direct work:** a narrow, reversible edit with no shared-contract, migration, access-control, release or ownership consequence. Do it directly when policy permits; keep the normal project checks.
- **Product work:** a user idea, feature, defect or change whose value depends on a real flow, state, error, acceptance or operational outcome. Use [product delivery](references/product-delivery.md) to shape the smallest sufficient increment.
- **Coordinated work:** multiple dependent increments, separate sessions, a takeover, a consequential review, or a workflow experiment. Add only the records and handoffs needed to preserve ownership and evidence.

Identify the real project and assigned role. Read its confirmed `docs/orchestration/policy.json` and current `status.md`, then only the linked task, active trial and evidence needed now. Another worktree must use the canonical sources in its packet. A worker reading this skill remains a worker.

Before implementation or dispatch, follow [policy gate](references/policy.md). Missing/conflicting limits require a focused user question and recorded confirmation; read-only discovery is allowed. Reuse confirmed choices. The user controls the lead model/effort; workers stay within confirmed limits and actual runtime capabilities. Do not infer authority from a model name, a capability selection, a version/date check or a successful checker result.

Use [evidence and challenge](references/evidence-and-challenge.md) throughout discovery, implementation and review. Label fact, assumption, inference and unknown. Verify consequential tools, APIs, versions and runtime behavior. Challenge premises that could change scope, safety, cost, acceptance or reversibility; ask immediately about material conflicts, authority, requirements or irreversible tradeoffs. Solve ordinary reversible technical issues within authority and continue independent work while waiting on an answer.

For product work, make the user/problem/value, assumptions, concrete flows, errors, data/state, exclusions and acceptance visible before implementation. Choose the simplest sufficient architecture, state material alternatives and measurable quality/cost hypotheses, then split work into complete increments with owners and dependencies. Use the existing requirement registry; do not create a competing spec or backlog.

## Coordinate and accept

Use [coordination and handoff](references/handoffs.md) when assigning, resuming, receiving results or reviewing. Record the attempt before dispatch; reconcile ambiguous outcomes before retrying. Never let a stale attempt replace the current owner.

Require independent review for persisted-data/security/shared-contract changes, difficult recovery or contradictory evidence. If review is unavailable, keep acceptance pending. Authors self-check and freeze source; completion reports enter review, not acceptance. Repeat affected checks after changes and carry unaffected proof with source comparison.

Reviewers receive raw relevant evidence, not a desired answer; acceptance is based on the artifact, outcome and current checks, not votes or a self-report. Apply release, recovery, operations, support or retirement guidance only when the product and risk make it applicable. Authorization for release or external action stays separate. Do not turn a prototype, mock, emulator or local test into integration, production or real-user evidence.

After two repair rounds with the same defect, change specification, granularity or reviewer within authority. Do not simply repeat the request or increase effort. Communicate purposeful results, blockers and required decisions; use available event waits while active, not promises of unattended monitoring.

## Maintain, measure and improve

Keep current status limited to active work, blockers, effective guidance and the latest accepted checkpoint. Move closed work to linked history. Query metrics/experiments with reporter --view summary and relevant IDs, then paginated --view detail only as needed; legacy full reports are for deliberate audit, not startup context. Private records stay in the project; trial/candidate code belongs in a separate temporary workspace.

Use [maintenance and compatibility](references/maintenance.md) when preparing a release, changing environment/authority, responding to a relevant defect or retiring support. Freeze task versions; instructions and worker reports never grant permission. Store task records in the project, candidate code in a separate temporary workspace, and never silently edit an installed distribution.

Use [records and reporting](references/records.md) for metrics and trial records; the reporter validates and summarizes supplied evidence, not reality itself. Measure all roles' quality, intervention, elapsed time and usage where available; unknown remains unknown, and allowance is not a bill. Low allowance never justifies weaker acceptance, outside models or unapproved purchases/resets.

Use [improvement protocol](references/improvement.md) for a reusable finding: observe, diagnose, run one bounded change, measure, then evaluate the diagnosis, measurement quality and process overhead before adopting, revising, reverting or deferring. Keep one attributable intervention and its rollback condition. A smaller report or lower token count is not evidence of value by itself. No finding means no extra ceremony; a bounded improvement may remove a rule when evidence supports simplification.

For a potentially general fix, follow [contribution workflow](references/contributing.md): local trial within granted scope, evidence, sanitized source patch, then authorized publication. Never silently edit installed/global copies. Project decisions and private logs stay in the project. Improvements cannot broaden product requirements, acceptance, model limits, spending or release authority.
