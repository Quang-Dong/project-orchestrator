# Authorized subagents and lead responsibility: author review

Date: 2026-09-22. Baseline: `7bd89b42cb91a2ad671539c5840aaaeb608d86fa`, the fetched default branch after PR #1 merged. The source checkout was clean before creating `codex/subagent-default-orchestration`. The new PR binds the final commit and hosted checks; this report does not relabel earlier evaluations as current results.

Scope: guidance, examples, metadata and evaluation preparation only. Work was performed solo under the explicit instruction for this update. No worker, independent reviewer, behavioral run or product pilot was created. This report's scenario outcomes are **author decision inspection**, not agent passes.

## Problem and decision

The reported failure mode was a main session choosing to implement substantive work itself when the user wanted orchestration. The earlier proportional-work guidance could be read as preferring direct execution whenever work was tightly coupled. That observation motivates a clearer default; it is not a measured failure rate across agents.

The new default is authorized subagents for substantial work when configuration, budget and actual runtime suffice. A worker can execute a coupled slice end to end while the main session retains strategy, user communication, common decisions, integration and acceptance. Small work remains direct. Explicit solo, a chosen mechanism or granted discretion remains authoritative; uncovered switches to independent sessions or all-main implementation require a concrete explanation and user choice.

## Baseline and preserved contracts

Before editing, a local SHA-256 snapshot captured all 79 tracked source files and all 19 files of the global installed skill. Seven existing documentation/metadata/index files are in scope; the other 72 tracked files are protected. The snapshot is local verification material, not a new public manifest or runtime schema. Three new evaluation documents are added.

Protected scope includes scripts and tests, policy v2 and its unconfirmed template, records v2, reporter output v3, artifact-verifier CLI, workflow configuration, and all historical evaluation reports, packets, results and manifests. The global skill and unrelated project remain outside the edit scope. No automatic policy migration or installation occurs.

## Canonical ownership of changes

| Decision | Source and change | Verification and applicability boundary |
| --- | --- | --- |
| Default mechanism and when to ask | [Policy execution mode](../skills/project-orchestrator/references/policy.md#execution-mode-and-lead-responsibility) owns the default, explicit overrides, inherited choices, missing prerequisites and proposed mechanism changes. | Inspect ready/missing/override cases below. A small correction has no new dispatch or question. |
| Model family and effort | [Adaptive allocation](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation) prefers allowed observed Luna/Spark, preserves explicit settings and checks context/override constraints. | Observe inventory before selection; no IDs or family preference are hardcoded into checker/template. |
| Overall responsibility and execution owner | [Handoffs](../skills/project-orchestrator/references/handoffs.md#ownership-and-integration) separates main responsibility from a worker's coupled slice and records takeover/writer state. | One execution owner may be a worker. Scoped main checks/integration are allowed without redoing the assignment. |
| Entry and discoverability | [Entrypoint](../skills/project-orchestrator/SKILL.md), [metadata](../skills/project-orchestrator/agents/openai.yaml), [README](../README.md) and [examples](../skills/project-orchestrator/references/worked-examples.md) summarize and route to policy. | Small, solo, default-subagent and independent-session examples; no additional schema or mandatory paperwork. |
| Evidence and future evaluation | [Index](README.md), [packets](subagent-default/worker-packets.md) and physically separate [assessor rubric](subagent-default/assessor.md). | Prepared, not executed. Historical packets keep their original contracts and revisions. |

## Runtime grounding and limits

The official [Codex subagents guide](https://learn.chatgpt.com/docs/agent-configuration/subagents), checked 2026-09-22, supports model/effort configuration and warns that parallel writes can conflict. It does not establish that a particular model is available on every host or that delegation saves resources. The skill's preferred family and execution default are user decisions, not conclusions derived from a benchmark.

The tool declarations exposed during this update offered a Luna model and did not expose Spark. They also specified that full-history forks inherit parent settings and do not accept overrides, whereas supported narrower context modes can accept them. This is **observed tool-interface metadata**, not a worker execution or proof of effective settings. No dispatch tested either model. The durable rule is to inspect the current mechanism and inventory, not to freeze this host's availability in the skill.

Requested and effective settings, main settings and worker settings, and user authority and runtime capability remain separate. Other runtimes, including Claude Code, must use their actual mechanisms and allowed models; an unavailable preferred family is a decision to resolve, not a guessed alias. No fixed slots, prices, limits or savings are published.

## Author decision inspection

Each row states the decision the revised guidance supports and its boundary. These fictional inspections do not show an agent making or executing that decision.

| ID | Input | Supported decision and source | Condition still open / scope boundary |
| --- | --- | --- | --- |
| A01 | Substantial work; all prerequisites satisfied; no override | Dispatch a bounded subagent output without another mode question; policy execution mode. | Main still checks integrated acceptance. |
| A02 | Small, clear, authorized correction | Direct edit and relevant check; policy startup. | No new handoff or delegation policy. |
| A03 | Explicit solo choice | Main works within solo scope; policy overrides. | Required independent review is not waived. |
| A04 | User chose an independent session | Apply the covered choice and verify intended task/owner before use. | Task-creation and scoped authority remain required. |
| A05 | User granted choice of execution mode | Choose within that discretion and confirmed limits. | Discretion is not a new budget or model allowlist. |
| A06 | Same-scope follow-up, compaction or resume | Inherit the applicable choice and checkpoint. | Material uncovered change may require a new decision. |
| A07 | Only allowed Luna exposed; no specific Spark instruction | Select Luna with supported permitted effort; allocation rule. | Do not report Spark execution or claim cost advantage. |
| A08 | User specifically requires unavailable Spark | Clarify before dependent dispatch. | Luna is not an automatic substitute. |
| A09 | Neither preferred family usable | Resolve model choice before dispatch. | An already authorized specific alternative is valid; no silent fallback. |
| A10 | Explicit effort unsupported | Preserve the request as unresolved; no substitution. | Required and effective settings cannot be equated. |
| A11 | Full-history fork disallows required override | Use a supported context mode with necessary packet, if authorized. | Do not drop context or claim inherited author history is independent review. |
| A12 | Budget or authority missing | Group the actual missing decisions; bounded read-only work only while waiting unless another part is independently authorized. | No template confirmation or whole-task solo fallback. |
| A13 | Delegation runtime unavailable | Explain missing capability and feasible authorized alternatives. | No pretending dispatch occurred; implementation mode not silently changed. |
| A14 | Coupled formatter, caller and state logic | Give one worker end-to-end execution; main retains overall decisions/acceptance. | No artificial parallel workers or ownership fragmentation. |
| A15 | Independent outputs with shared integration boundary | Assign bounded outputs and identify integration owner/checks. | Independence includes contracts and resources, not only different files. |
| A16 | Existing independent task has active unrelated owner | Inspect scope; ask for appropriate task choice before assignment. | No repurposing or conflicting writes. |
| A17 | Dispatch times out with unknown outcome | Reconcile identity/attempt/execution before retry; existing timeout rule. | Timeout is not failure proof or authorization for duplicate dispatch. |
| A18 | Stop acknowledged but writer/process remains live | Wait for verified stop or safe isolation before transfer. | Stopping a turn is not stopping side effects. |
| A19 | Superseded owner returns an older revision | Retain provenance and inspect applicability; current owner stays authoritative. | No stale overwrite or automatic acceptance. |
| A20 | Main proposes taking over all implementation | Explain and ask if no existing choice covers takeover; record transfer and verify writers. | Honest attribution; do not call main rewrite worker delivery. |
| A21 | Two repairs of the same failure did not work | Retain attempts/hypotheses and re-diagnose before further repair. | Extra effort/worker is not an automatic remedy. |
| A22 | Worker self-checks pass but required review remains open | Main can assess technical evidence and report the open review separately. | No completion claim that closes the mandatory condition. |
| A23 | Artifact is old or a check was skipped | Verify current revision/criterion or report the missing evidence. | New default changes no evidence-acceptance rule. |

The current source retains the timeout, writer, old-owner, uncertain-effect, revision and repair protections. No mandatory independent-review condition was relaxed. Eight future evaluation cases cover these decisions through staged variants; they are physically separated from their assessor criteria and remain **prepared, not executed**.

## Verification

Local checks on the candidate working tree, 2026-09-22:

| Check | Actual result | Limit |
| --- | --- | --- |
| Platform skill validator | 1 pass; 0 fail/error/skipped. | Structural skill validation, not agent behavior. |
| Full root Python suite | 74 tests: **73 pass, 0 fail, 0 error, 1 skipped**. | The symlink-escape case was skipped because Windows did not grant symlink creation (WinError 1314). A skipped case is not a pass. |
| Python compile | 15 Python files under skills/evals; command exit 0. | Syntax/compilation only. |
| JSON metadata | 19 files parsed; 0 errors. | Includes historical metadata; parsing does not revalidate historical outcomes. |
| Relative links and anchors | 298 relative links, including 141 anchor references; 0 missing targets/anchors. | External sites are outside the local-link check. |
| Codex metadata | YAML parsed; description length, skill mention and implicit-invocation setting valid. | Does not establish runtime settings after dispatch. |
| Whitespace and public content | Diff/new-file whitespace clear; bounded private-path/credential scan returned 0 flags; scoped content manually inspected. | No private runtime logs or account identifiers published. |
| Contract/history preservation | 72/72 protected tracked files unchanged by SHA-256. | Scripts, CLI/schema, template, tests, CI and historical evidence unchanged. |
| Installed-copy preservation | 19/19 global files unchanged; no additions. | No installation/update was performed. |

Commands used were the platform's `quick_validate.py`, `python -B -m unittest discover -s evals -p "test_*.py"` through a runner retaining exact counts, `python -B -m compileall -q skills evals`, and `git diff --check`. Temporary read-only audit code checked JSON, relative targets/anchors, metadata, protected hashes and changed-file content; it is not a new package dependency or phrase-matching test. The fetched default branch still matched the recorded baseline before commit. Hosted CI is separately bound to the pushed SHA in the PR; no local result is called hosted CI.

## Remaining limits

Independent review and agent behavior on Codex/Claude Code have not been evaluated for this candidate. The Python tools are unchanged, so their tests establish their existing contracts rather than compliance with new prose. No cost, allowance, speed, quality or reliability improvement has been measured. The global installation remains at its existing revision until a separately authorized update.
