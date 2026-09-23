# GPT-6 Luna worker selection: author review

Date: 2026-09-23. Baseline: `4bd98b3b5c386cb196429458e3549459ebaee06a` on `codex/subagent-default-orchestration`. The checkout was clean and matched the fetched PR #2 head before editing. [PR #2](https://github.com/Quang-Dong/project-orchestrator/pull/2) binds the final commit and hosted CI for this update.

## Change and evidence boundaries

The current user decision replaces the Luna/Spark family preference with **`gpt-6-luna` only for workers**, subject to confirmed policy and observed runtime support. It also clarifies that workers make implementation decisions in their packet, while the main session resolves consequential decisions outside that scope. Difficulty is not an automatic reason to choose a stronger worker model, duplicate implementation or take over ownership. This selection follows user intent; it is not a benchmark conclusion.

Canonical model/effort rules remain in [policy](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation). The [handoff decision loop](../skills/project-orchestrator/references/handoffs.md#questions-changes-and-results) owns the evidence/question returned by a worker and the main session's decision sent back. The [entrypoint](../skills/project-orchestrator/SKILL.md), README and [examples](../skills/project-orchestrator/references/worked-examples.md#substantive-work-defaults-to-an-authorized-subagent) summarize those rules. Metadata already describes authorized subagents and remains unchanged.

An exact model ID must be allowed and exposed; a family name, another Luna version or a broader old allowlist does not satisfy it. Main-session settings stay user-owned. The user can explicitly change the worker choice later; no routine fallback or automatic allowlist update is granted. Effort remains adaptive without mandatory High/max. Requested settings and effective execution settings remain distinct.

Work was performed solo. No worker, reviewer, pilot or behavioral run was created. The cases below are **author decision inspection**, not agent passes. The earlier [review](subagent-default-review.md), [packets](subagent-default/worker-packets.md) and [rubric](subagent-default/assessor.md) remain byte-for-byte historical evidence/preparation for `4bd98b3`; their model-family variants do not validate this revision. No new harness, grader or current behavioral packet was added.

## Author decision inspection

| Case | Expected decision under the revised guidance | Evidence boundary |
| --- | --- | --- |
| Exact `gpt-6-luna` permitted and exposed; substantial work | Dispatch the bounded subagent assignment without another mode question. | Configuration validity still does not prove effective settings or task acceptance. |
| Small clear correction | Direct edit and relevant check. | No new delegation or process record. |
| Explicit solo or covered independent-session choice | Preserve the choice through continuation/compaction. | Independent-session workers still follow the applicable model choice; solo needs no worker inventory. |
| Only GPT-5.6 Luna, Spark or Sol available | Keep dependent dispatch pending; name the missing exact model. | No equivalent-family assumption or automatic substitute. |
| Model available but absent from confirmed allowlist | Resolve the policy conflict without editing the project's policy automatically. | Runtime access does not authorize selection. |
| Missing delegation authority or applicable budget | Ask a grouped question; continue only bounded discovery or independent authorized work. | No implied spending and no all-main fallback. |
| User-specified effort unsupported | Identify the unsupported setting before dispatch. | Do not replace it with High or the inherited effort. |
| Effort unspecified | Start from the permitted observed default; adapt only with task evidence and authority. | No blanket High/max requirement. |
| Full-history fork blocks required overrides | Use a supported context mode with the necessary packet if authorized; otherwise report the gap. | No inherited wrong model or omitted consequential context. |
| Routine implementation uncertainty within the packet | Worker investigates, chooses and self-checks within scope. | No question for every implementation detail. |
| Caller contradicts a shared business/contract decision | Worker sends source/revision, observed conflict, relevant hypotheses and acceptance impact with a concrete decision needed. Main checks requirement/context/task boundary, settles the shared decision or asks the user, then returns the delta to the owner. | Dependent edits wait; independent authorized work can continue. No stronger model or duplicate writer follows automatically. |
| Two unsuccessful repairs of the same issue | Retain attempts and rejected hypotheses; re-diagnose before another repair. | No reset by new packet/owner or automatic model escalation. |
| User later explicitly changes worker model | Treat it as a scoped user decision and check the new choice against policy/runtime. | Does not authorize unrelated settings or an agent-invented fallback. |
| Dispatch timeout or uncertain side effect | Reconcile identity/attempt and actual result before retry. | No duplicate execution based only on missing output. |
| Writer still active during proposed takeover | Verify stop or safe isolation before transferring ownership and editing. | Main-session strategy ownership is not permission to conflict with the writer. |
| Late output from an old owner | Keep identity/attempt/revision and inspect applicability to current source. | No stale overwrite or automatic acceptance. |
| Technical checks pass but mandatory review is open | Report the self-checked candidate and remaining review separately. | Main integration or same-model agreement is not independent review. |

## Verification and preservation

Before editing, local SHA-256 snapshots recorded all 82 tracked files and all 19 installed skill files. Six existing guidance/index files are editable; the other **76 tracked files** are protected, including scripts, tests, policy template, metadata, CI and all historical evidence. The only new source file is this report. Policy v2, records v2, reporter output v3 and CLI behavior remain unchanged; no model ID is hardcoded into executable validation.

| Local check | Actual result | Limit |
| --- | --- | --- |
| Platform skill validator | 1 pass; 0 fail/error/skipped. | Structural validation only. |
| Full root Python suite | 74 tests: **73 pass, 0 fail, 0 error, 1 skipped**. | Symlink-escape test skipped because Windows symlink creation was unavailable (WinError 1314); not a pass. |
| Compile | 15 Python files under skills/evals; command exit 0. | Syntax/compilation only. |
| JSON | 19 files parsed; 0 errors. | No claim of historical outcome revalidation. |
| Relative links/anchors | 309 local links, including 146 anchor references; 0 missing targets/anchors. | External URLs excluded from this check. |
| Metadata | Existing YAML parses and retains valid description, invocation and skill mention. | Metadata was not edited. |
| Whitespace/public content | Diff and new-file whitespace clear; bounded private-path/credential scan found 0 flags; changed prose manually inspected. | No private logs or account identifiers published. |
| Source preservation | 76/76 protected files unchanged by SHA-256. | Includes scripts/CLI, schemas, template and all historical evidence. |
| Global preservation | 19/19 installed files unchanged; no additions. | No installation/update performed. |

Checks used the platform's `quick_validate.py`, the complete `unittest discover -s evals -p "test_*.py"` suite through a runner retaining exact counts, `python -B -m compileall -q skills evals`, and `git diff --check`. Temporary audit code parsed JSON, checked local links/anchors and metadata, and compared hashes; no package dependency or phrase-matching test was added.

Hosted CI is recorded against the new pushed SHA in PR #2, separately from local verification. Any local skip remains a skip even if a hosted environment can exercise that case.

## Open conditions

Independent review and behavioral effectiveness on Codex/Claude Code remain unverified. Tool tests exercise the unchanged contracts, not compliance with prose. No price, quota, time/token saving or quality-improvement claim is added to the runtime guidance. The global skill and unrelated project are outside this update; installation requires a separate user request.
