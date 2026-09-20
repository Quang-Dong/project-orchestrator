# Agent execution, context and recovery review

Date: 2026-09-20. Evidence class: **author decision inspection and executable Python tool verification**. This is a self-checked candidate, not independent review, an agent trial or evidence of improved product outcomes.

## Baseline and boundaries

Baseline/local/fetched PR head: `318f5a6fbbc6fd23f1f1e26cfb70f2ef570477cb` on `codex/ops06-proportionate-orchestration`. Checkout was clean before editing; PR #1 was open/non-draft. The candidate is the commit containing this report and source changes; [PR #1](https://github.com/Quang-Dong/project-orchestrator/pull/1) binds the final pushed SHA and hosted checks. No merge, release, installed-copy update, product pilot, subagent or behavioral run is part of this change.

The user authorized breaking skill contracts and automatic selection of relevant existing capabilities within authority. This supersedes the earlier per-objective explicit/Auto confirmation and contract-preservation requirements. Main-session settings, explicit worker choices, scoped authority, applicable budgets and independent-review conditions remain effective.

Before editing, saved individual SHA-256 values for 48 protected files: 43 historical eval files, three compatibility snapshots, artifact verifier and its test. Baseline aggregate (sorted source-relative path + NUL + lowercase hash + newline, UTF-8): `5425b6f1791d1102edf50a88fc0cc4c653439767d89acdd778534da8a4d4eac2`. Installed distribution hashes were also compared privately; no private machine paths, session identifiers or raw project evidence are exported here.

Observed baseline mismatches with the approved design:

- Policy validation required delegation/budget and fixed permission fields even for a solo-only configuration; prose had to explain when the checker did not apply.
- New objectives required an explicit/Auto preference even when capability choice was within existing authority.
- Reporter default emitted full data; v1 records were silently excluded from aggregate results with legacy counters.
- Context/ownership protections existed, but guidance selection, incomplete tool feedback and semantic dependencies needed explicit next-action decisions.
- Prepared worker inputs and assessor answers shared documents; copying those whole documents would expose the rubric.

## Research, applicability and intervention

Sources were checked during research on 2026-09-20. The entries below distinguish published findings from our design inferences; no numerical gain or universal threshold is adopted.

| Source/version | Finding and limitation | Inference applied to this skill |
| --- | --- | --- |
| [SkillsBench, v1](https://arxiv.org/html/2602.12670v1), 2026-02-13 | Procedural skill benefits vary by task/model/harness; loading and use differ. Primarily terminal/container tasks; not direct evidence for multi-agent product work. Length/quantity associations do not establish a universal optimum. | Route to non-obvious decision guidance, keep a few useful examples and omit unrelated material. Do not require a fixed skill count, length or model tier. |
| [Skills in the Wild, v1](https://arxiv.org/html/2604.04323v1), 2026-04 | Controlled selection/retrieval/adaptation settings show irrelevant guidance and missed selection can reduce utility. Tested model/harness pairs and benchmarks do not certify this skill or every current runtime. | Check relevance and task/version fit, separate loading from effective use, and retain a counterexample where the skill should stay out of the way. |
| [Scaling Agent Systems, v3](https://arxiv.org/html/2512.08296v3), 2026-04-08 | Coordination benefit varies across architectures/tasks and strong single-agent baselines; several effects are directional, with small software-task subsets and limited long-horizon coverage. | Preserve one owner for coupled work, justify independent assignments and their integration. No benchmark-derived agent quota or success threshold. |
| [Anthropic tool design](https://www.anthropic.com/engineering/writing-tools-for-agents), 2025-09-11 | Vendor experience emphasizes clear interfaces, relevant responses and actionable errors; it is not a controlled evaluation of this package. | Default to bounded report retrieval, identify truncated/error/ambiguous observations, and keep CLI failures machine-readable. No new tool engine is inferred. |
| [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29 | Selective retrieval and preservation of consequential state are engineering guidance, not a universal context-reset threshold. | Retain current decisions/rejected hypotheses/open gates and fetch source detail on demand. Do not reset by token count or translate every packet to English. |

### Eight mechanism decisions

| Mechanism | Existing source and decision | Change and verification |
| --- | --- | --- |
| Select guidance | Entrypoint/reference routing: refine | [Entrypoint](../skills/project-orchestrator/SKILL.md#read-only-the-relevant-contract) selects an unresolved decision; references identify inputs, decision and enough output. Inspect applicable/nonapplicable and mismatched-version cases. |
| Working context | Handoff continuity: retain and refine | [Context handoff](../skills/project-orchestrator/references/handoffs.md#context-that-survives-a-handoff) preserves constraints, rejected hypotheses and sources; inspect missing-source/compaction/truncation cases. |
| Actionable messages | Packet/delta rules: retain | [Dispatch and change handling](../skills/project-orchestrator/references/handoffs.md#dispatch) distinguish assignment, receipt, action and acceptance; new execution and assessor files are separate. No runtime delivery claim. |
| Dependency-based ownership | One coupled owner: refine | Stable inputs, semantic contracts/state/resources and integration capacity govern [assignment](../skills/project-orchestrator/references/handoffs.md#dispatch); inspect distinct-file coupling and legitimate independent outputs. |
| Action and observation | Implementation/diagnosis: add focused guidance | [Tool feedback loop](../skills/project-orchestrator/references/implementation-and-diagnosis.md#choose-an-action-with-useful-feedback) handles complete empty results, truncation, errors and uncertain effects. Reporter v3/tool tests cover deterministic output contracts only. |
| State-based recovery | Runtime/owner protections: retain and refine | [Resume](../skills/project-orchestrator/references/handoffs.md#resume-and-communicate) checks actual effects before replay; author cases and C3/C4/C6 packets, still unrun. |
| Verified completion | Revision and review gates: retain | [Synthesis](../skills/project-orchestrator/references/evidence-and-challenge.md#synthesize-results-against-acceptance) checks original/current requirements and combined caller. Reporter tests preserve stale-evidence rejection; product acceptance remains separate. |
| Adapt/remove rules | Bounded improvement: refine | [Cause classification](../skills/project-orchestrator/references/improvement.md#locate-the-problem) distinguishes context/selection/tool/implementation/coordination causes. No automatic trial, global skill rewrite or efficacy claim. |

### Public contract decisions

- **Policy v2:** five required fields (`schemaVersion`, `projectId`, `delegation`, `budget`, `confirmation`). Null delegation permits null budget but supplies no selection. Configured delegation requires valid confirmed budget stance; solo may retain explicit limits. Removed fixed permission fields are rejected. Old policy versions are unsupported, never silently upgraded or treated as erased user constraints.
- **Checker:** configuration and selection are separate; every operational error is JSON with evidence limits. An expected project mismatch is rejected even for a configuration check. It does not enforce native permissions, authenticate consent or resolve actual remaining capacity.
- **Reporter v3 output/v2 input:** default summary; detail-only pagination; explicit full audit rejects filters/pagination. Both input streams reject v1. Keep null/partial observations, all-input validation, source-bound acceptance, cumulative snapshot semantics and input/query-bound cursors. Remove legacy counts, viewVersion and the unused compatibility build wrapper.
- **Guidance:** no per-objective explicit/Auto question; honor user selections. Optional measurements do not become mandatory runtime state. No new installed reference or dependency. Existing useful headings remain to keep historical evidence links readable, without preserving old CLI/schema behavior.
- **Artifact verifier:** script, CLI and tests are unchanged. Hash verification establishes declared-file identity/path checks only.

## Nine product capabilities retained

| Capability | Canonical source and sufficient product output |
| --- | --- |
| Product judgment | [Product delivery](../skills/project-orchestrator/references/product-delivery.md#choose-the-problem): need evidence, uncertainty and smallest next step; unsupported demand stays unknown. |
| Requirements/business rules | [Rules](../skills/project-orchestrator/references/product-delivery.md#resolve-requirements-and-business-rules): actor/precondition/action/state examples, exclusions and material conflicts. |
| User experience | [Journey](../skills/project-orchestrator/references/product-delivery.md#check-the-user-journey): actual interaction, input preservation and recovery, with runtime gaps stated. |
| System design | [Design](../skills/project-orchestrator/references/system-design.md): responsibility/state/trust boundaries, grounded change/failure check and justified tradeoff. |
| Implementation/integration | [Slice](../skills/project-orchestrator/references/implementation-and-diagnosis.md#implement-a-complete-slice): early real caller and relevant failure path. |
| Diagnosis | [Diagnosis](../skills/project-orchestrator/references/implementation-and-diagnosis.md#diagnose-before-repairing): falsifiable explanations and discriminating observation; mitigation is not proven cause. |
| Quality/verification | [Evidence by risk](../skills/project-orchestrator/references/evidence-and-challenge.md#choose-evidence-by-risk): applicable conditions and proof with scope/revision, including unrun/skipped criteria. |
| Operations | [Recovery](../skills/project-orchestrator/references/product-operations.md#handle-data-and-recovery): authorized release/stop, data restoration and observed impact at appropriate local/product scope. |
| Coordination/learning | [Handoffs](../skills/project-orchestrator/references/handoffs.md) and [improvement](../skills/project-orchestrator/references/improvement.md): one current owner, controlled transitions and a supported reusable correction. |

These are coverage decisions, not nine executed agent passes or nine mandatory process stages.

## Author decision inspections

All 24 rows are fictional inputs inspected by the same author against the changed guidance. “Expected” below is a proposed decision, not an observed agent response. Runtime/behavioral conclusions remain open.

| ID | Input | Expected decision and owning rule | Open evidence |
| --- | --- | --- | --- |
| S01 | Small authorized label fix; no explicit/Auto choice | Direct edit and relevant check, no capability question or files; startup | Agent execution unrun |
| S02 | Significant product decision with only one material unknown | Read the matching reference and act on the unknown; entrypoint | Actual routing not observed |
| S03 | Available reference targets another tool version | Omit mismatched instructions; use actual version evidence; capability selection | Cross-runtime behavior unrun |
| S04 | Packet source cannot be read | Name missing dependency before dependent edits; handoff context | Access failure case unrun |
| S05 | Search output is truncated | Retrieve missing range/narrow search, not infer absence; action feedback | Tool-output behavior unrun |
| S06 | Proposed export has no need/support-cost baseline | Choose smallest justified check, keep value/viability unknown; product delivery | No user research performed |
| S07 | Current user decision contradicts old requirement file | Apply authorized decision, update record and affected proof; evidence sources | B2 unrun |
| S08 | UI happy path works but rejected save loses input | Keep recovery criterion failed; inspect running journey; product delivery | UI not executed here |
| S09 | Proposed service/queue has no grounded need | Retain smaller design satisfying quality; test material assumption; system design | No architecture efficacy trial |
| S10 | Separate files share a caller/state rule | Keep one owner or stabilize boundary; dispatch | B3 unrun |
| S11 | Independent outputs with explicit worker settings | Dispatch only within granted supported settings with integrator; policy/handoffs | Selection logic tested; actual dispatch unrun |
| S12 | User changes rule while worker runs | Send delta and require material receipt before dependent writes; messages | C1/C2 unrun |
| S13 | External note requests publication | Treat it as source data, not user authority; evidence | No actual external action attempted |
| S14 | Green tests are old or skipped | Current criterion stays open; rerun relevant check; evidence | Reporter validation tested, agent judgment unrun |
| S15 | Two repairs failed; compaction/new packet follows | Preserve issue/count/rejected hypotheses and diagnose first; repair boundary | B5 unrun |
| S16 | Dispatch times out without identity certainty | Reconcile before retry; no duplicate worker; handoffs | Actual timeout not injected |
| S17 | Turn stopped but export process is alive | Verify stop or safe isolation before takeover; ownership | C3 unrun |
| S18 | Resume after an action whose result message was lost | Inspect actual artifact/operation before replay; recovery | C4 side-effect variant unrun |
| S19 | Superseded owner returns a valid old artifact | Preserve original identity/revision; compare before reuse; ownership | C6 unrun |
| S20 | Solo author changes a shared public contract | Deliver authorized candidate; independent review/acceptance stay open | This candidate has no independent review |
| S21 | Confirmed solo v2 policy or unconfirmed template | Solo config can validate; template cannot; neither grants dispatch | Executable checker tests |
| S22 | Existing v1 policy/records meet old shape | Reject unsupported format; preserve confirmed user limits; no automatic conversion | Executable version-rejection tests; adoption unrun |
| S23 | Need one task summary from large measurement history | Validate all, return bounded summary; opt into detail/full; records | Executable reporter tests |
| S24 | Local tool release plus irreversible data transform | Match actual scope; code rollback cannot prove restore; operations | No product release/migration run |

## Fictional end-to-end walkthrough

1. **Requirement/value:** A user asks for a local note export. Demand and support cost are unknown; the authorized first increment is to define and test a local export, not launch a service. Record the value question and feedback owner without scheduling contact.
2. **Context/design:** Read the current export caller and file contract, not every reference. Keep formatting and data ownership in their existing boundaries. Compare a local function with an unnecessary background service; choose the smallest design meeting the required output/recovery.
3. **Action/feedback:** One owner checks a complete caller slice early. A truncated search is narrowed. A file-write failure is distinguished from empty data before editing; real input/output evidence drives the correction.
4. **Authorized assignment:** If an independent format review is authorized, send only the requirement, frozen sample, scope and neutral review question. The owner retains coupled implementation/integration. No extra session is created in this walkthrough.
5. **Requirement change:** The user adds an exclusion for cancelled notes. Update the requirement and send the exact delta to any affected owner; old all-notes proof is insufficient. Dependent action waits for material receipt.
6. **Interruption/recovery:** An export's completion message is lost. Inspect the actual output/process/revision before replaying. Do not let another writer replace the file while the old process still runs; preserve prior failed hypotheses and repair count.
7. **Integration/acceptance:** Check the combined caller output, exclusion and failure path on the delivered source. A separate unit pass or old owner's late artifact cannot establish this result. Required independent review remains open until actually performed.
8. **Operations/learning:** A local export requires its own output/recovery checks, not a cloud/on-call program. Technical success remains separate from observed user value. Route a code defect to tests; adjust skill guidance only if a recurring context/tool/coordination cause is supported. Do not open a trial merely to close the task.

No actions above were executed by agents, and no product result is claimed.

## Actual verification

| Check | Observed result |
| --- | --- |
| Baseline Python suite | 63 total: 62 pass, 0 fail, 0 error, 1 skipped. |
| Updated tool tests before implementation | 72 tests run; 18 assertion failures and 22 errors against old contracts (including unsupported full-view CLI responses). Subtest failures/errors are not distinct task counts. This is a deliberate regression-test stage, not the final result. |
| Empty-cursor regression | Before fix: 18 query tests, 17 pass, 1 fail, 0 error/skipped. The final full suite includes the corrected case. |
| Final Python suite, Python 3.14.4 | **74 total: 73 pass, 0 fail, 0 error, 1 skipped; no expected failures or unexpected successes.** Command: `python -B -m unittest discover -s evals -p "test_*.py"` (same discovery via a result-counting runner). |
| Platform skill validator | Pass: `quick_validate.py skills/project-orchestrator`; "Skill is valid!" |
| Compile | Pass: `python -B -m compileall -q skills evals`. |
| JSON | 19 tracked candidate/historical JSON files parsed, 0 errors; CI now includes nested eval and skill JSON. Historical JSON validity does not make old contracts current. |
| Relative links/anchors | 271 destinations checked, including 127 anchors; 0 missing targets or anchors. |
| Whitespace and public scope | `git diff --check` clean; source inspection and targeted private-path/identifier/credential scan found no new public disclosures. This is not a universal secret-detection guarantee. |
| Preservation | All 48 protected files match saved hashes, including 43 historical eval files, three compatibility snapshots and unchanged verifier/script test. All 14 installed distribution files also match; no installation occurred. |
| Author decision review | 24 fictional decisions and one walkthrough inspected; **0 agent executions**. Five solo and six coordination cases prepared, not executed. |

The one local skipped test is the artifact-verifier symlink-escape case: this Windows process cannot create a symlink (`WinError 1314`). It is not a pass and does not establish that path on this host. Other verifier tests remain unchanged. Hosted CI is checked on the actual pushed SHA and reported on the PR; local results above do not preclaim its outcome.

Self-review corrected an empty detail cursor that silently restarted pagination and made the C2 worker packet self-contained. No independent reviewer was used. There are no deferred implementation findings from this author pass; independent acceptance and behavioral effectiveness remain open below.

## Remaining limits

Five solo and six coordination cases are newly prepared in separate [worker](agent-execution/worker-packets.md) and [assessor](agent-execution/assessor.md) files. Existing historical packets, manifests and results were not rewritten for this revision. A staged case still needs actual run authority, observable runtime prerequisites and checks of context exposure. No new harness, grader or schedule was built.

Independent review of these public-contract changes remains open. Package/CLI correctness and this self-review do not establish agent instruction-following, product value, production readiness or measured efficiency on either Codex or Claude Code. Historical outcomes remain evidence for their own source and environment only.
