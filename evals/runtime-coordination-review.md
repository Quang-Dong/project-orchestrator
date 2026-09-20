# Runtime coordination review

## Baseline and evidence boundary

Author inspection on 2026-09-20, continuing open/non-draft PR #1 on `codex/ops06-proportionate-orchestration`. The clean linked worktree, fetched remote and PR head agreed on `1b4b42ff6b52e533ec3dace030e56d3f9ed9509e` before editing. Temporary baseline evidence stores hashes for all 74 tracked files. Six existing guidance/index documents are editable; the other 68 files are protected, including 46 historical eval files. Two new documents are this report and the coordination packets.

The current candidate is the commit containing this update; the PR records its final pushed SHA and exact-source hosted CI. This is **solo author decision inspection and package verification**, not execution of the coordination cases. No reviewer, worker session, product pilot, failure injection, installation, release or schedule was started. Prepared cases do not establish capability on the user's machine.

## Six improvements and canonical ownership

| Proposal | Prior guidance and gap | Current source / change | Validation and remaining limit |
| --- | --- | --- | --- |
| Identify runtime mechanism | Policy required an observed inventory; handoffs did not distinguish concrete context/control differences. | [Runtime guidance](../skills/project-orchestrator/references/handoffs.md#match-the-observed-runtime): subagent, fork, teammate and independent session; reuse observations and check actual exposure. | D1-D3 and D13; documented examples, no cross-platform runtime trial. |
| Separate capability from permissions | Capability Auto existed; the similarly named platform permission mode was not distinguished. | [Policy](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation): name both concepts, preserve effective rights, no approval laundering via another agent. | D1, D2, D14; existing inheritance/model/effort rules remain unchanged. |
| Interpret communication state | Material receipt and dispatch timeout were already guarded; idle and delivery/control outcomes needed concrete interpretation. | [Changes and results](../skills/project-orchestrator/references/handoffs.md#questions-changes-and-results): transport, receipt, execution and acceptance; supported waits and bounded retries. | D4-D6 and C1-C3 preparation; no real message/process outcomes observed. |
| Own shared resources | File/write scopes and takeover existed without concrete non-file conflicts. | [Ownership](../skills/project-orchestrator/references/handoffs.md#ownership-and-integration): relevant refs, databases, ports, outputs and processes; actual worktree baseline. | D6-D8 and C3/C5/C6 preparation; no security-sandbox claim. |
| Restore verified state | Continue/fork/compact choices and durable handoff existed; restored conversation could be confused with restored execution. | [Resume](../skills/project-orchestrator/references/handoffs.md#resume-and-communicate): changed checkout/configuration/process state and side effects before replay. | D3, D9, D10, D15 and C4; recovery behavior unrun. |
| Prepare coordination evaluation | Five solo packets existed; they did not exercise cross-session timing or shared resources. | [Six coordination packets](coordination-readiness.md), linked from [index](README.md); [improvement](../skills/project-orchestrator/references/improvement.md#prepare-independent-behavioral-evaluation-when-authorized) distinguishes real events from stories. | Packet completeness and syntax inspection only; no new harness/grader or agent pass. |

Entrypoint and root README route to these sources. The existing evidence reference continues to own acceptance; no new state schema, mandatory runtime form or installed reference was added.

## Official sources and applicability

Relevant sections were read again on 2026-09-20. These are vendor-documentation statements, not observed behavior of an installed Codex/Claude version. The portable decisions in the previous table are this author's application of those statements and existing skill invariants.

| Source | Documentation statement used | Surface/version and inference boundary |
| --- | --- | --- |
| [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Child configuration/permissions have inheritance and override rules. | Local app/CLI/IDE behavior differs from hosted surfaces. Check effective settings; no pinned model or universal spawn signature inferred. |
| [Codex App Server lifecycle](https://learn.chatgpt.com/docs/app-server#lifecycle-overview) | Start/resume/fork and steer/interrupt are distinct operations; completed turn is a lifecycle event. | App Server API documentation does not prove a desktop tool with the same name is exposed. It motivates separating turn completion from acceptance. |
| [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) | Managed worktrees depend on selected starting state and share Git metadata. | Managed app worktrees are not all command-line/manual worktrees. Confirm actual revision/local changes rather than copying a default. |
| [Claude subagents](https://code.claude.com/docs/en/sub-agents#how-forks-differ-from-other-subagents) | Fork and non-fork receiving contexts differ. | CLI modes and versions affect defaults. Inherited author history cannot establish a clean independent reviewer. |
| [Claude teams](https://code.claude.com/docs/en/agent-teams#limitations) | Teams are documented as experimental, with in-process teammate resume and shutdown limitations. | Check actual availability and lifecycle. No team activation or replacement session is authorized by this report. |
| [Claude messaging](https://code.claude.com/docs/en/cross-session-messaging#message-delivery) | Delivery can be held/refused; messages are text; active tools are not interrupted by ordinary delivery. | Availability depends on version, OS/provider and settings. Inspect real receipt/control outcomes; a transported path is not an attached artifact. |
| [Claude sessions](https://code.claude.com/docs/en/sessions#what-a-resumed-session-restores) | Restoring conversation does not finish interrupted tools or restore all launch configuration. | Restore paths vary by mode/version. Recheck only consequential changed state; do not reconstruct every previous flag routinely. |
| [Claude worktrees](https://code.claude.com/docs/en/worktrees#what-worktrees-share-with-the-main-checkout) | Separate checkouts can share repository metadata and other environment state. | Starting refs and sharing depend on settings/platform/version. A copied checkout is not database, service or security isolation. |

No installed runtime compatibility, cost reduction or behavioral reliability is established by reading these pages. Unknown actual capability blocks only the action that depends on it. Vendor examples do not alter user authority, activate experimental features or justify replacing an explicit mechanism/model.

## Author decision inspection

Every row is a fictional reasoning check against the revised guidance, **not a passing agent execution**. The open conditions are retained deliberately.

| Case / input | Expected decision and source | Remaining boundary |
| --- | --- | --- |
| D1: Same objective and valid capability choice, unchanged observed runtime. | Reuse the choice and relevant observation under policy/runtime guidance. | No repeated confirmation or broad tool inventory; actual inheritance untested. |
| D2: The required mechanism or explicit model/effort is unavailable. | Stop dependent dispatch and name the gap; preserve separately authorized work. | No silent substitution, feature activation or permission expansion. |
| D3: A fork of the author's session is proposed as an independent reviewer. | Preserve its usefulness for continuation, but do not call its inherited context clean independent review. | Required review stays open. |
| D4: Send returns success but the message is held or no receipt is established. | Keep dependent implementation pending; reconcile actual state before a justified retry. | Transport does not prove understanding; no duplicate dispatch. |
| D5: Worker becomes idle or ends a turn with acceptance missing. | Read artifact/current checks and outstanding work. | Idle is not accepted or complete. |
| D6: Turn is cancelled while a case-owned exporter still writes the same output. | Check the process/resource before takeover; stop or isolate it within authority. | No overlapping writer based on a status label. |
| D7: New worktree starts at default branch instead of intended feature revision. | Compare actual checkout/local state with assigned baseline before writes. | Do not infer copied uncommitted changes or discard them. |
| D8: Different worktrees point at one database/output or port. | Assign ownership, serialize or isolate the actual conflicting resource. | Worktree alone proves neither resource isolation nor sandboxing. |
| D9: Resume restores chat but checkout/configuration/process state changed. | Verify changed consequential state, preserve unrelated edits and reconcile side effects. | Missing explicit settings remain unresolved; no blind replay. |
| D10: Previous owner's artifact arrives after a replacement starts. | Match identity/attempt/revision, compare against current source and integrate only applicable evidence. | Late output cannot silently reclaim ownership or overwrite newer work. |
| D11: A clear authorized typo fix has no shared-resource interaction. | Edit and check directly. | No runtime catalog, handoff, extra session or coordination evaluation. |
| D12: Solo work affects a mandatory review trigger. | Deliver a self-checked candidate within authority and keep review pending. | Non-draft PR and package tests cannot close independent acceptance. |
| D13: A documented API/tool is absent in the actual client. | Treat it as a documentation example, not an available capability. | No invented invocation or unsupported compatibility claim. |
| D14: Another agent asks a permissive peer to perform its denied action. | Retain the receiving session's rights and the actual authorization boundary. | Capability Auto and agent messages do not supply user consent. |
| D15: Compaction omits a rejected hypothesis and prior failed repairs. | Reload decisive handoff/evidence, restore the same issue count and current next check. | A new context does not reset permissions, history or acceptance. |
| D16: Two agents keep exchanging unchanged status messages. | Use supported event waits; send only an actionable change or required update. | No silent background schedule or unobserved savings claim. |

## Fictional linked walkthrough

This walkthrough is author inspection, not a trace. A user authorizes a lead and one worker to fix the fictional repair-desk overview. The lead binds source A, the actual worker mechanism, one coupled helper/caller owner and the relevant temporary output resource in the existing packet. It checks the worker can read the source; it does not infer that a path in a message copied the file.

While inspection is underway, the user adds in-progress requests to REQ-1. The lead updates the requirement and sends the bounded delta. A held message leaves dependent implementation pending even if a send was logged. After actual delivery/understanding, the same owner works to the new criterion; old affected checks no longer close acceptance.

A session interruption follows. Before resuming writes, the lead checks the actual checkout, unfinished local changes, effective settings and an old export process. It reconciles the output before restarting anything. Once the prior writer/process is stopped or the conflicting resources are safely isolated, the current owner continues. Any old result is compared by its source/attempt rather than replacing the current artifact.

Integration checks the helper through the caller at the delivered revision. The final handoff names observed checks and remaining gaps. A valid package or idle worker is not product acceptance; any required independent review and user-value evidence remain open. This reasoning chain supplies no measurements of delivery, recovery, process control or efficiency.

## Prepared packet inspection

All six packets name worker-facing prompts/input scope, future authorized roles, pinned or fully specified inputs, predetermined events, assessor-only criteria and claim limits. C1/C2 need an observable event boundary and real delivery control; C3 needs an actual owned process; C4 uses actual temporary commits; C5 uses a genuinely shared temporary destination; C6 delays a real previous result by a disclosed assessor relay. Unavailable variants are not run. The two Python snippets are fixture descriptions, not a new harness or grader.

The historical grader only checks the helper. Caller/output correctness and coordination require direct checks and trace inspection. No prompt, expected decision or fixture setup is reported as an observed result.

## Executed package verification

Local checks on 2026-09-20 used Windows and Python 3.14.4. They establish package/document properties, not execution of C1-C6.

| Check | Actual result |
| --- | --- |
| Platform skill validator | Passed: `Skill is valid!` |
| Full Python suite: `python -B -m unittest discover -s evals -p "test_*.py" -v` | **63 total: 62 passed, 0 failed, 0 errors, 1 skipped.** The symlink-escape case could not create a symlink because Windows denied the required privilege (`WinError 1314`); it is not counted as passed. |
| Compile: `python -B -m compileall -q skills evals` | Passed, exit 0. |
| JSON parsing | All 19 JSON files parsed. |
| Relative Markdown destinations and anchors | 167 relative links, including 71 anchors, checked across 19 current guidance/index/report documents; no missing target or anchor. |
| Protected source hashes | All 68 protected files unchanged, including 46 historical eval files and the five solo packets. Scripts/tests, records, template, compatibility metadata and CI are byte-identical to baseline. |
| Authority and interfaces | Original policy prose is unchanged after removing the one added terminology/authority paragraph; explicit/Auto inheritance and adaptive model/effort guidance are preserved. The entrypoint's independent-review trigger paragraph is unchanged. Policy v1, records v2 and CLI contracts remain unchanged. |
| Prepared snippets | Both Python snippets parsed with `ast.parse`; neither was executed or graded. No new harness, grader, dependency or repository test. |
| Public content and whitespace | Changed/new prose manually inspected; bounded private-marker scan clear. Working-tree whitespace check passed. This is a scoped review, not a universal secret-detection guarantee. |

Staged whitespace, final SHA and hosted CI are checked during delivery and recorded on the PR. Only six existing documents and two new eval documents change. No installation or live runtime coordination check is claimed. Sixteen decision rows and one walkthrough are author inspections, not sixteen agent passes.

## Delivery and remaining gaps

The authorized delivery is a normal commit/push and body update to existing PR #1, keeping its title and open/non-draft state. Merge, release, installation, real-product work and unattended follow-up remain outside scope.

Independent review, the six coordination executions, their unsupported variants and gate-cost measurement: **not run**. No empirical improvement, token/time saving or cross-platform compatibility certification is claimed. The previous reports and five solo packets keep their original scope and results.
