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

## Continue, compact, fork or start fresh

Choose by continuity and evidence needs, not a fixed turn count, duration or token threshold:

| Situation | Default |
| --- | --- |
| Implementing, testing or fixing review findings for the same slice | Continue the writer's session; reuse the independent reviewer's session for affected rechecks |
| Long but coherent work that is still progressing | Continue; use available compaction when needed, with important decisions and state in the existing handoff |
| A completed outcome followed by a distinct objective | Prefer a new session with the relevant contract, artifact and concise handoff |
| Independent review of the current author's work | Use a separate reviewer context when authorized; provide requirements, frozen source, raw evidence and limits without the author's preferred verdict |
| An alternative approach needs the existing reasoning history | Fork if supported and authorized; inherited history is not a clean independent review context |
| Repeated confusion about current decisions/state or persistence with disproven approaches | Reassess the cause; consider a fresh session if context interference is supported, rather than assuming a reset fixes the method |

A compacted conversation preserves continuity but may omit details; verify consequential state against artifacts. A new session must reconstruct enough context, and a fork inherits history, so neither automatically reduces work or improves judgment. A separate reviewer can still be wrong. Do not infer cost savings or weekly allowance from session age or cached-token counts.

Before a new owner writes, apply the ownership checks above. Transfer the objective and authority, checkout/revision, verified state, failed or unrun checks, decisions still in force and next action through the existing handoff. Link necessary raw evidence instead of copying the entire transcript. Starting a new session or compacting does not reset repair counts, permissions or pending acceptance gates. An explicit solo instruction still prohibits creating extra sessions for review or convenience unless the user changes it.

These defaults synthesize [OpenAI's guidance on coherent chats](https://learn.chatgpt.com/guides/best-practices#organize-long-running-chats), [Anthropic's context-engineering discussion](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and its [model-dependent context-reset findings](https://www.anthropic.com/engineering/harness-design-long-running-apps). They are decision guidance, not proof of a universal reset threshold or measured gains for the current model.

## Resume and communicate

A replacement reads the current handoff and necessary contracts/evidence, verifies owner/source and resumes the named next action. It need not reconstruct the whole chat.

Use supported event waits. Send only a meaningful outcome, changed risk, decision, blocker or correction, plus minimum platform-required updates. A stopped task needs a truthful handoff, not a promise of unattended continuation.
