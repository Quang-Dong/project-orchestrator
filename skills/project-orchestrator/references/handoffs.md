# Coordination and handoff

Apply the operating modes and priorities in [SKILL.md](../SKILL.md). This reference owns dispatch, ownership and recovery mechanics, not another mandatory workflow.

## One current handoff

Use existing task/status records. Keep one current handoff with the outcome, source revision, owner/write scope, checks and evidence links, remaining gaps and next action. A dispatch packet or checkpoint may link those fields instead of duplicating them. Keep closed evidence immutable and linked; do not rewrite historical results.

A compact handoff can be:

```yaml
task: TASK-7
attempt: attempt-2
owner: writer-1
writeScope: feature/
outcome: complete the approved caller flow
source: candidate@revision
checks: {caller: verified, recovery: not-run}
evidence: [path/to/check-result]
remaining: independent review of the frozen source
next: reviewer inspects affected behavior
```

Add dependencies, exclusions, delegated decisions, escalation conditions, capability choices and requested/observed settings when relevant. They may reference an existing contract. A small direct task does not need dispatch fields or a new metrics experiment.

Update the handoff when ownership, source/evidence status, a material blocker or next action changes; the same artifact serves takeover and integration. Do not generate a new report for an unchanged checkpoint.

## Dispatch

Before dispatch, record the attempt, owner, authorized directory/write scope, versioned input, outcome/acceptance and required settings. Validate capability and policy using [policy](policy.md). Record actual settings only after observing the running task; requested settings are not facts.

Use states only as supported by evidence:

- planned: specified, no dispatch.
- dispatching: call issued, identity unresolved.
- assigned: identity returned, execution not yet observed.
- running: activity observed.
- blocked: a named dependency or authority is missing.
- ready_for_review: frozen self-checked artifact received.
- accepted: the responsible acceptance decision covers that revision.
- cancelled: stopped or superseded, with unfinished work preserved.

A timeout is not proof of non-execution. Reconcile task identity, attempt and activity before retrying. An uncertain identity remains pending; never create a duplicate to bypass uncertainty.

## Ownership and integration

Prefer one end-to-end owner for coupled work. Assign a separate integrator only when distinct results actually need integration; name the baseline, write scope and affected-caller checks. One person/session can implement and integrate its own slice without an extra role.

Before takeover, verify the current source and that the old writer stopped, or isolate scopes so writes cannot collide. Record the new owner and reason before editing. Late output may inform review but cannot overwrite the current owner's work.

A lead may take over within granted authority, including explicit solo work. Record the intervention and its effect on a trial's criteria. Do not automatically classify a valid product result as failed, or describe main reimplementation as successful specialist delivery.

Before integrating, compare the current baseline, preserve unrelated changes and run checks affected by the combination. Passing individual artifacts do not establish integrated acceptance.

## Review and repair

The author hands off a frozen revision with exact commands/results and limitations. Each criterion is verified, failed, blocked, not run or unknown. An independent reviewer receives source, relevant raw evidence, criteria and limitations without an expected verdict. Self-check is useful but not independent review.

Lead reads the handoff first, then decisive checks. Expand inspection for risk, missing evidence or contradiction. Carry unaffected proof only with a source comparison; changed dependencies or acceptance configuration may invalidate it too.

Worker and reviewer exchange one consolidated finding list and close ordinary repairs in scope. When tools or authority prevent direct exchange, lead relays a short packet. After two failed repairs of the same issue, reassess cause, scope or verification before another implementation attempt, or stop. Changing attempt IDs does not reset the count. Continue only under an evidenced revised approach and existing authority; otherwise escalate the unresolved decision.

A missed first usable slice, repeated disproven diagnosis or substantial lead rework is an earlier reassessment trigger. Do not wait for a broad matrix to reveal that the basic caller fails.

## Resume and communicate

A replacement reads the current handoff and necessary contracts/evidence, verifies owner/source and resumes the named next action. It need not reconstruct the whole chat.

Use supported event waits. Send only a meaningful outcome, changed risk, decision, blocker or correction, plus minimum platform-required updates. A stopped task needs a truthful handoff, not a promise of unattended continuation.
