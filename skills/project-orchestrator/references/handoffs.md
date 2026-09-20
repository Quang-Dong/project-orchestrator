# Coordination and handoff

Apply the operating modes and outcome constraints in [SKILL.md](../SKILL.md). This reference owns dispatch, ownership and recovery mechanics, not another mandatory workflow.

## One current handoff

For coordinated work or takeover, use existing task/status records. Keep one current handoff with the outcome, source revision, owner/write scope, checks and evidence links, remaining gaps and next action. A dispatch packet or checkpoint may link those fields instead of duplicating them. Keep closed evidence immutable and linked; do not rewrite historical results.

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

## Language and shared meaning

Use the user's chosen language with the user. Internal assignments inherit the task language unless explicitly changed; code and maintained documentation follow repository conventions. Do not assume translating every packet into English improves performance. Preserve identifiers, exact UI labels, units, state names and consequential domain terms. When a term has competing meanings, retain the original and a short clarification, such as domain “session” versus agent task. Explain only ambiguity that can change a decision; no mandatory glossary.

Preserve obligation strength when translating or summarizing: required, recommended and optional are different. Link the original consequential requirement alongside a paraphrase. Resolve material ambiguity with its owner before dependent changes; do not infer a new requirement from a translation.

## Context that survives a handoff

Select context by the receiving task: current outcome and acceptance, authority and exclusions, checkout/revision, decisions still in force with reasons, rejected hypotheses, unresolved defects/gates and next action. Link source artifacts and relevant raw evidence instead of repeatedly rewriting the transcript. Verify that the receiver can access the required source at the named revision; an unavailable file or mismatched baseline is a named dependency, not permission to guess.

Keep facts, assumptions, inferences and unknowns attached to their sources under [evidence rules](evidence-and-challenge.md#label-and-trace-claims). Preserve these distinctions through compaction and relays. Share only necessary authorized context; private data unrelated to the task does not belong in a packet. The current handoff is the continuity record, not a second backlog.

## Match the observed runtime

Before using a new coordination mechanism, or after a material environment change, identify only what the assignment needs: receiving context, actual checkout/revision, effective model/effort and permissions, and supported send, wait, stop and resume behavior. Record or link this observation in the current packet. Reuse unchanged evidence; a small direct task does not need a tool inventory. A capability described in vendor documentation is not proof it is exposed in this client, version or account. Do not automatically enable experimental features or silently substitute a delegation mechanism.

| Mechanism | Context and control distinction |
| --- | --- |
| Delegated subagent | Inspect the actual spawn options. Codex settings can inherit or be overridden; a Claude non-fork subagent starts from its definition and supplied context. Neither the name nor a new agent ID proves a clean context or restricted tools. |
| Conversation fork | Codex thread forks and Claude conversation forks carry earlier history. Confirm the copied scope and current files separately; inherited author reasoning is not a clean independent review context. |
| Teammate | Claude agent teams have their own coordination mechanism and context rules. Do not assume a teammate inherited the lead's conversation or survived a lead resume. Team availability and experimental limits must be checked. |
| Independent session | Treat identity, source access and permissions separately. Claude cross-session messages carry text, not the sender's files/history. Use whatever supported session controls the actual client exposes; a similarly named tool elsewhere is not a compatibility guarantee. |

These examples draw on [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Codex thread/turn controls](https://learn.chatgpt.com/docs/app-server#lifecycle-overview), [Claude subagents](https://code.claude.com/docs/en/sub-agents), [Claude teams](https://code.claude.com/docs/en/agent-teams) and [Claude messaging](https://code.claude.com/docs/en/cross-session-messaging). They are portability guidance, not instructions to call an unavailable API. Keep requested and effective settings distinct under [policy](policy.md#capability-choice-and-adaptive-allocation); a material mismatch blocks dependent work until resolved within authority.

## Dispatch

Before dispatch, record the attempt, owner, authorized directory/write scope, versioned input, outcome/acceptance and required settings. Complete the existing packet with the product outcome and requirement source, expected artifact/evidence, reason delegation helps, independent scope/exclusions and integration owner. Distinguish decisions already settled from choices delegated to the worker; name the conflict, contract change or missing evidence that requires escalation. Reference existing fields rather than creating another form. Validate capability and policy using [policy](policy.md); record actual settings only after observing execution.

Choose the interaction needed: **advice** returns findings without write ownership; **independent output** delivers a bounded artifact; **independent review** returns findings/verdict on a frozen artifact with read-only scope and no preferred verdict; **ownership transfer** uses the takeover checks below. Reading a packet does not appoint a worker as lead. Before opening more work, check that its review/integration can be handled; finish or unblock the limiting dependency instead of adding management roles or a fixed agent quota.

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

## Questions, changes and results

For a substantive assignment, the receiver's first response or first substantive action should show the understood outcome, scope and source. Check material inputs before editing. Ask a focused question when missing or contradictory information changes the solution or acceptance; continue independent authorized work. This can happen in the normal first action, without a separate acknowledgment round for a small clear task.

Make message intent explicit in ordinary prose: assignment, question, finding, change, result or stop. Include the affected task/attempt, source and required next action when ambiguity is possible. These are communication conventions, not new record event types or a transport protocol. Use the supported direct channel when authorized; otherwise the lead relays the relevant information without changing its meaning.

When the user changes a requirement, apply the [instruction and record distinctions](evidence-and-challenge.md#distinguish-instructions-records-and-observed-behavior), update the affected requirement record, identify affected owners/callers and send the delta with its source, superseded decision and acceptance impact. Invalidate affected proof under [evidence rules](evidence-and-challenge.md#label-and-trace-claims). For a material change, establish that the affected owner received and understood it before dependent actions resume; a sent message alone is insufficient. If receipt is uncertain, keep affected integration/acceptance pending and use supported stop/contact controls where needed. Stopping is not proven until observed; use the ownership checks before another writer takes over.

Distinguish transport success, observed receipt/understanding, execution and acceptance. A delivered message may wait behind an active tool; a held or refused message has not supplied the change to its recipient. For an uncertain send, reconcile recipient/attempt and actual delivery state before a bounded retry; do not create a duplicate worker or repeat messages indefinitely. Unresolved delivery keeps dependent work pending. Use the material-change receipt rule above without adding acknowledgments to every small exchange.

An idle notification or completed turn reports runtime activity, not task acceptance. Inspect the returned result and outstanding work. A stop request or cancellation label does not prove that subprocesses stopped; apply [ownership checks](#ownership-and-integration) before a conflicting writer resumes.

Return results with the artifact/revision, criterion-level evidence, unresolved questions and next owner/action. Report a finding as soon as it changes scope, authority or correctness; routine unchanged progress does not require another message or handoff copy.

## Ownership and integration

Prefer one end-to-end owner for coupled work. Assign a separate integrator only when distinct results actually need integration; name the baseline, write scope and affected-caller checks. One person/session can implement and integrate its own slice without an extra role.

Check the resources the actual commands can affect, not only file paths: shared Git refs, test databases, server ports, output directories and background processes. Name an owner or isolate/serialize conflicting use in the existing handoff when needed. Do not require this inventory for a direct edit with no shared-resource interaction. A worktree is a separate checkout, not a security sandbox or an independent database/service environment; repository metadata can still be shared.

When creating or selecting a worktree, compare its actual revision and uncommitted state with the intended baseline before writes. Do not assume the platform starts at the parent's HEAD or carries local changes and ignored configuration. Provide only necessary authorized setup; avoid copying unrelated private configuration. [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) and [Claude worktrees](https://code.claude.com/docs/en/worktrees) document different defaults and sharing behavior; verify the relevant path in the current runtime.

Before takeover, verify the current source and that the old writer and relevant processes stopped, or isolate affected resources so writes cannot collide. A stopped model turn alone is insufficient. Record the new owner and reason before editing. Match late output to its original identity, attempt and revision; it may inform review but cannot overwrite the current owner's work. Integrate only still-applicable changes after checking the current baseline.

A lead may take over within granted authority, including explicit solo work. Record who changed what and why; do not describe main reimplementation as worker delivery. If a process trial exists, use [improvement](improvement.md#measure-useful-progress) for its separate criteria.

Before integrating, compare the current baseline, preserve unrelated changes and run checks affected by the combination. The lead applies [result synthesis](evidence-and-challenge.md#synthesize-results-against-acceptance), including original requirements and affected caller flows; passing individual artifacts does not establish integrated acceptance.

## Review and repair

The author hands off a frozen revision with exact commands/results and limitations. Each criterion is verified, failed, blocked, not run or unknown. An independent reviewer receives source, relevant raw evidence, criteria and limitations without an expected verdict. Self-check is useful but not independent review.

Lead reads the handoff first, then decisive checks. Expand inspection for risk, missing evidence or contradiction. Carry unaffected proof only with a source comparison; changed dependencies or acceptance configuration may invalidate it too.

Worker and reviewer exchange one consolidated finding list and close ordinary repairs in scope. When tools or authority prevent direct exchange, lead relays a short packet. After two failed repairs of the same issue, reassess cause, scope or verification before another implementation attempt, or stop. Changing attempt IDs does not reset the count. Continue only under an evidenced revised approach and existing authority; otherwise escalate the unresolved decision.

A missed first usable slice, repeated disproven diagnosis or substantial lead rework is an earlier reassessment trigger. Use the [diagnosis path](implementation-and-diagnosis.md#diagnose-before-repairing) to distinguish causes and carry the resulting evidence, rejected hypotheses and next check into the current handoff. Do not wait for a broad matrix to reveal that the basic caller fails.

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

A compacted conversation preserves continuity but may omit details; verify consequential state against artifacts. A new session must reconstruct enough context, and a fork inherits history, so neither automatically reduces work or improves judgment. A separate reviewer can still be wrong. Use [records](records.md#metrics-jsonl) only when accounting is needed; session age is not a reason to reset context.

Before a new owner writes, apply the ownership checks above. Use the [context handoff](#context-that-survives-a-handoff), preserving verified state and failed or unrun checks. Verify consequential state against source artifacts after compaction instead of trusting a shortened conversation alone. Starting a new session or compacting does not reset repair counts, permissions or pending acceptance gates. An explicit solo instruction still prohibits creating extra sessions for review or convenience unless the user changes it.

These defaults synthesize [OpenAI's guidance on coherent chats](https://learn.chatgpt.com/guides/best-practices#organize-long-running-chats), [Anthropic's context-engineering discussion](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and its [model-dependent context-reset findings](https://www.anthropic.com/engineering/harness-design-long-running-apps). They are decision guidance, not proof of a universal reset threshold or measured gains for the current model.

The language convention is a portability choice, not an English-versus-native performance claim; [NAACL 2025 research](https://aclanthology.org/2025.naacl-long.485/) finds translation benefits depend on the model and task. For a concrete packet and requirement delta, read the [delegation example](worked-examples.md#bounded-delegation-with-a-changing-requirement).

## Resume and communicate

A replacement reads the current handoff and necessary contracts/evidence, verifies owner/source and resumes the named next action. It need not reconstruct the whole chat or load complete logs; retrieve decisive artifacts as needed.

After resume or an environment move, verify the consequential state that may have changed: working directory/revision, uncommitted work, needed tools/configuration, effective settings and relevant processes. Restored conversation is not restored execution. For example, [Claude session restoration](https://code.claude.com/docs/en/sessions#what-a-resumed-session-restores) does not restore every launch option or finish an interrupted tool. Reconcile whether a side effect already happened before replaying it. Recover within existing authority; unavailable explicit settings or unsafe uncertainty keep dependent work blocked, without restarting unrelated decisions.

Use supported event waits or completion notifications instead of repeated status queries. Receiving a message may start a turn and consume resources, so avoid ping-pong updates without a new outcome, decision or actionable gap. Send only a meaningful outcome, changed risk, decision, blocker or correction, plus minimum platform-required updates. A stopped task needs a truthful handoff, not a promise of unattended continuation.
