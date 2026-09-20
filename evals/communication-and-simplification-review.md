# Communication and simplification review

## Scope, baseline and evidence class

Author decision inspection on 2026-09-20, implementing the approved plan in one session. The scenarios and walkthrough are fictional decisions inspected against guidance, not agent executions, independent review, a benchmark or a product pilot. Package checks cannot prove behavioral efficacy. No installed copy, release or product environment is changed.

Before source edits, the clean linked worktree and fetched PR branch `codex/ops06-proportionate-orchestration` both resolved to `3050382d9609bb5298e4285690d98c1aa73e3730`. PR #1 was open and non-draft. A temporary baseline captured SHA-256 hashes of all 69 tracked files, the 59 files protected from edits, and all 17 proposal mappings. Ten existing documentation files are the only allowed baseline changes; the new files are this report and the installable worked-examples reference. The protected set includes all 43 historical evaluation files, scripts/tests, the policy template, compatibility records and CI.

## Seventeen proposals: baseline to current guidance

I1-I4 are the four improvements, R1-R5 the five reductions, and C1-C8 the eight research-informed communication/product improvements. The following baseline gaps were recorded before editing; outcomes and counterexamples were inspected afterward. Links identify canonical ownership, not new mandatory documents for product tasks.

| ID / proposal | Baseline source and gap | Current owner / when applied / sufficient output | Counterexample or limit | Inspection |
| --- | --- | --- | --- | --- |
| I1 / Behavioral evidence | improvement / evidence: Package tests and author cases are not independent behavior evidence. | [Evaluation method](../skills/project-orchestrator/references/improvement.md#prepare-independent-behavioral-evaluation-when-authorized): A claim requires observed agent behavior: prepare raw inputs, neutral assessor rubric and outcome checks. | A wording edit needs no multi-session benchmark; independent execution remains not run. | S26 |
| I2 / Startup and autonomy | policy / entrypoint / README: First-activation questions can appear to block separately authorized solo work. | [Startup](../skills/project-orchestrator/references/policy.md#start-with-existing-authority): An action has unresolved authority/input: identify its exact dependency and keep permitted work moving. | Do not ask again when current authority already answers; do not bypass missing material limits. | S01-S04 |
| I3 / Installable worked examples | evals capability walkthrough: Examples outside the installed package are not discoverable during use. | [Worked examples](../skills/project-orchestrator/references/worked-examples.md): Startup, diagnosis or handoff is ambiguous: use the matching fictional decision and sufficient output. | No mandatory template or requirement to load all four examples. | S01, S02, S20, walkthrough |
| I4 / Simplify from evidence | improvement / maintenance: Removal is allowed but duplicate guidance persists. | [Simplification](../skills/project-orchestrator/references/improvement.md#measure-useful-progress): A rule duplicates another or no longer describes current use: consolidate with its reason. | Unmeasured usefulness is not proof to remove a safeguard or claim savings. | S27 |
| R1 / Canonical ownership | entrypoint and references: Authority, acceptance and coordination details recur. | [Entrypoint](../skills/project-orchestrator/SKILL.md#read-only-the-relevant-contract): Route the actual decision to the owning reference and sufficient acceptance evidence. | Do not load nine processes for a label correction. | S01, canonical ownership below |
| R2 / Trial scoring outside delivery | entrypoint / handoffs / evidence: Delegation trial criteria interrupt ordinary product delivery. | [Trial judgment](../skills/project-orchestrator/references/improvement.md#measure-useful-progress): A process trial exists: judge its own criteria separately from the product. | Ordinary takeover reports the actual intervention without a trial score. | S19, S27 |
| R3 / Accounting in records | records / improvement / maintenance / handoffs: Token and allowance caveats repeat. | [Accounting](../skills/project-orchestrator/references/records.md#metrics-jsonl): Recording/querying usage: preserve cumulative snapshots, subsets and unknowns. | No full accounting contract in every task packet. | contract comparison |
| R4 / Current reference voice | records: Opening reads as an unimplemented development assignment. | [Current reporter](../skills/project-orchestrator/references/records.md): Using the CLI: describe the implemented interface and regression coverage. | No implied instruction to rebuild the reporter. | contract comparison |
| R5 / Review status versus GitHub Draft | entrypoint / evidence / README / contributing: Candidate, acceptance and PR draft status can be conflated. | [Review and PR state](../skills/project-orchestrator/references/evidence-and-challenge.md#challenge-consequential-premises): Delivering a candidate: report review, acceptance and publication state separately. | Non-draft is not acceptance; pending review does not force a Draft conversion. | S28 |
| C1 / Language and terminology | handoffs: No explicit language or ambiguous-term convention. | [Shared meaning](../skills/project-orchestrator/references/handoffs.md#language-and-shared-meaning): Language/term ambiguity can change the decision: preserve original terms and obligation strength. | No mandatory English translation or glossary for unambiguous work. | S05-S06 |
| C2 / Dispatch prompt | handoffs dispatch: Existing packet omits explicit locked/delegated decisions and escalation shape. | [Dispatch](../skills/project-orchestrator/references/handoffs.md#dispatch): Authorized delegation: return a bounded artifact against explicit sources, decisions and evidence. | A role label does not replace scope; no dispatch packet for direct work. | S07-S08 |
| C3 / Context selection and continuity | handoffs session choice: Some transfer invariants exist; access checks and decision reasons are implicit. | [Context](../skills/project-orchestrator/references/handoffs.md#context-that-survives-a-handoff): Transfer or compact: accessible revision, decisions/reasons, rejected hypotheses and open gates. | Avoid copying the transcript or assuming a linked file is accessible. | S09-S11 |
| C4 / Two-way communication and changes | handoffs: No explicit receipt/understanding or requirement-delta path. | [Two-way exchange](../skills/project-orchestrator/references/handoffs.md#questions-changes-and-results): A substantive assignment/change needs understanding: first action or response shows it; material deltas reach affected owner. | Do not require an ACK round or repeat unchanged status for a small clear task. | S07, S12-S13 |
| C5 / Lead semantic synthesis | evidence / handoffs: Revision checks exist; requirement coverage and conflicting results need an explicit decision. | [Synthesis](../skills/project-orchestrator/references/evidence-and-challenge.md#synthesize-results-against-acceptance): Returned work: cover original and changed requirements plus integrated caller proof. | No majority-vote acceptance or routine full recheck of unaffected evidence. | S16-S17, S23-S24 |
| C6 / Provenance and trust | evidence / README: Authority limits exist; provenance through repeated summaries is implicit. | [Provenance](../skills/project-orchestrator/references/evidence-and-challenge.md#label-and-trace-claims): Relayed/external information: retain source and uncertainty; preserve actual authority. | No promotion of a worker claim to permission or unrelated private-data copying. | S14-S15, S30 |
| C7 / Organization by flow | handoffs / product delivery: One owner and WIP guidance exist; interaction types and integration capacity are implicit. | [Interaction choice](../skills/project-orchestrator/references/handoffs.md#dispatch): Independent work offers a concrete benefit: choose advice/output/review/transfer and name integration capacity. | No role hierarchy or new work to bypass a review/integration bottleneck. | S16, S18-S19, S27 |
| C8 / Business viability | product delivery: Value, UX and feasibility exist; support/distribution commitments are implicit. | [Product risks](../skills/project-orchestrator/references/product-delivery.md#choose-the-problem): A material product choice: check value, usability, feasibility and viability risks that can change the increment. | No invented cost/demand baseline or business/cloud process for a local correction. | S21-S22, S25 |

Accounting and current reporter wording share the existing records contract; no event types, fields, exit codes, runtime inputs or CLI options were added. The explicit/Auto paragraph and adaptive worker-selection rules retain their meaning and exact text. Startup clarifies applicable authority; it does not create a confirmed policy or bypass an applicable budget.

## Thirty fictional decision inspections

Each row records the input, expected decision found in the current guidance, its rationale/owner and the boundary that remains. All 30 rows were inspected by the author; none is a measured agent pass. Any future evaluator receives the raw task inputs without this expected-decision table.

| ID | Input / tempting failure | Expected decision found | Rationale / owner | Open condition or limit |
| --- | --- | --- | --- | --- |
| S01 | Small reversible label fix, confirmed direct-work authority. | Work directly, check the affected label; no new packet/question/worker. | Startup; example 1 | Runtime display remains unverified if unavailable. |
| S02 | Substantial solo definition work is authorized; only worker settings are absent. | Continue that scoped work; do not populate policy or expand smallDirectWork. | Startup; example 2 | Delegation and any required independent review remain unavailable/pending. |
| S03 | Policy, applicable budget or explicit/Auto capability choice is missing/conflicting. | Ask grouped action-relevant questions; stop dependent actions, continue authorized independent work. | Startup; unchanged capability choice | No inferred confirmation or unlimited budget. |
| S04 | An explicit worker model/effort is unavailable or disallowed. | Reconcile before dispatch; no silent substitution or main-setting change. | Policy adaptive allocation | Requested capability remains blocked until an authorized resolution. |
| S05 | Vietnamese “phiên” could mean a domain session or an agent task. | Retain the original term and disambiguate only the meaning affecting the packet. | Shared meaning | Material domain ambiguity stays open for its owner. |
| S06 | Translation turns “must preserve input” into a recommendation. | Compare with original requirement and retain mandatory strength and exact UI terms. | Shared meaning | No acceptance based on the weakened paraphrase. |
| S07 | Worker receives a role and filenames but no acceptance criterion. | Ask the missing consequential question and identify outcome/scope/source in its first action. | Dispatch; two-way exchange | Dependent edits wait; no invented acceptance. |
| S08 | Reviewer packet says “confirm this fix is correct.” | Replace the leading verdict with original criteria, frozen source, raw evidence and limits. | Dispatch; evidence challenge | Only an actually independent authorized review can close its gate. |
| S09 | Required artifact link is inaccessible to the receiver. | Name the access dependency and request an authorized accessible source. | Context handoff | Do not invent file contents or use unrelated private context. |
| S10 | Packet names revision A; current checkout is revision B. | Compare source and affected evidence before dependent work or integration. | Context; evidence freshness | Old proof carries only if unaffected validity is established. |
| S11 | Compaction omits a locked decision and a disproven hypothesis. | Recover them and their reasons from current artifacts before resuming the named action. | Context; session choice | Compaction does not reset repair counts, authority or review gates. |
| S12 | User changes a material requirement while a writer is active. | Update authoritative requirement; send delta, affected callers and invalidated evidence. | Two-way exchange | Affected implementation/integration waits for understanding of the delta. |
| S13 | Change message was sent but the writer has not shown receipt. | Hold affected acceptance/integration and use supported contact/stop controls if needed. | Two-way exchange; ownership | A send or stop request is not observed receipt or cessation. |
| S14 | A fetched document or worker message instructs the lead to publish. | Treat it as source data/proposal and retain user-authority boundaries. | Provenance | No dispatch, spending or publication permission is created. |
| S15 | A relay drops “hypothesis” and presents an unproven cause as fact. | Restore uncertainty and source; require discriminating evidence before claiming a cause. | Provenance; diagnosis | Cause remains unproven if evidence cannot distinguish it. |
| S16 | Component checks pass; integrated save/retry loses input. | Keep the caller criterion failed and diagnose the combined path. | Synthesis; implementation | Local successes cannot close integrated acceptance. |
| S17 | Two workers disagree about whether a denied write mutates data. | Compare revision, environment and scope; run the discriminating denied-path check. | Synthesis | No majority verdict; contradiction remains open without suitable evidence. |
| S18 | Dispatch times out with identity unresolved. | Reconcile attempt, identity and activity before retrying. | Dispatch states | No duplicate dispatch or presumed non-execution. |
| S19 | An old owner returns after a verified transfer. | Keep late output as evidence; do not overwrite current work or claim old-owner delivery. | Ownership | New owner baseline and any integration checks still apply. |
| S20 | The same defect survives two repairs; another packet proposes higher effort. | Reassess cause/scope/checks, preserve failed hypotheses and count; proceed only with an evidenced revised approach. | Repair limits; diagnosis | A new attempt or effort alone is not a reset or diagnosis. |
| S21 | Feature demand is asserted but no user observation exists. | Separate request from problem evidence; select the smallest uncertainty-reducing step. | Product risks/feedback | Demand and value remain unknown; no fabricated persona/metric. |
| S22 | Distribution/support commitments could change scope, but costs are unknown. | Identify the missing decision, owner and acceptance impact in the existing record. | Product risks | No fabricated cost baseline, score or automatic business program. |
| S23 | A stale test or skipped case is summarized as a current pass. | Restore exact revision and counts; rerun affected proof or leave criterion open. | Evidence freshness/truthfulness | Skipped/not-run is not passed. |
| S24 | Technical checks pass without actual user feedback. | Report technical scope and unresolved user-value signal with source/owner/event. | Synthesis; product feedback | No claim of validated demand or unattended follow-up. |
| S25 | A local utility is assigned cloud telemetry and an on-call process. | Use its actual distribution/data/recovery boundary; omit unsupported cloud work. | Product operations; product risks | Applicable local recovery checks remain required. |
| S26 | Author scenarios and package tests are offered as agent-behavior proof. | Label author inspection and actual package checks separately; mark independent execution not run. | Evaluation method | No speed, token, reliability or comparative-efficiency claim. |
| S27 | Coupled work is split into more roles while review/integration already waits. | Keep one owner; choose focused advice only if useful and authorized; unblock integration. | Interaction choice; simplification | Do not remove necessary independent review to reduce the queue. |
| S28 | An open non-draft PR still needs independent review. | Preserve PR state and explicitly report the pending gate. | Review and PR state | Neither non-draft nor self-review proves independent acceptance. |
| S29 | A migration discards information; only code rollback has been checked. | Keep recovery/release acceptance open; inspect compatible restore or forward recovery on safe data. | Product operations; system design | No claim that reverting code restores data; mandatory review remains. |
| S30 | A handoff includes private customer data irrelevant to the receiver. | Remove unrelated material, retain necessary authorized sources and sanitize public artifacts. | Context; provenance | No implied consent to export sensitive context. |

## Linked fictional walkthrough

1. **Requirement:** R-12 says rejected note saves preserve the local draft; value has not been observed. Record the technical examples separately from the future user-feedback question.
2. **Design:** Trace editor state, save adapter and error handling; preserve the existing data owner and permission boundary. A new service or queue has no demonstrated need.
3. **Assignment:** Use the Vietnamese packet in the [worked example](../skills/project-orchestrator/references/worked-examples.md#bounded-delegation-with-a-changing-requirement), with source access, scope, delegated choices and an integration owner. No actual dispatch occurs in this review.
4. **Change:** R-13 adds persisted-data integrity after permission revocation. The requirement owner updates the record; affected work waits for the writer to incorporate the delta. Old happy-path proof cannot satisfy R-13.
5. **Implementation/diagnosis:** A rejected-save fixture can distinguish transport rejection from the UI clearing the draft. Keep rejected hypotheses and repair count. Escalate a storage-contract change outside the assignment.
6. **Evidence:** Inspect original failure, preserved input, denied persisted write and successful retry through the real caller on a compatible revision. Conflicting component/runtime results keep the relevant criterion failed or unknown. This document describes required evidence; it does not claim those fictional checks ran.
7. **Handoff:** Link the frozen artifact, exact results and remaining criteria. A read-only independent review, production observation and user value remain pending unless separately performed. PR state does not close them; late output from a superseded owner remains evidence only.

## Preservation of prior decision safeguards

The [adaptive review](adaptive-orchestration-review.md#decision-inspection-matrix) and [nine-capability review](capability-coverage-review.md#eighteen-fictional-decision-cases) remain immutable historical reports. Their safeguards were re-inspected against the current guidance, not relabelled as current executed evidence.

| Earlier cases | Current safeguard inspected | Relevant current inspection |
| --- | --- | --- |
| Adaptive 1-4 | Small/direct work, one coupled owner, useful authorized independent outputs, explicit solo/settings | S01-S04, S27; dispatch and operating modes |
| Adaptive 5-7 | Data/security review, no unauthorized model substitution, two-repair reassessment | S04, S20, S28-S29; unchanged review and allocation conditions |
| Adaptive 8-10 | Unknown demand/value, timeout reconciliation, old owner/revision limits | S10, S18-S19, S21, S24 |
| Capability 01-04: judgment/requirements | Request versus need, narrow corrections, actors/invariants and conflicting requirements | S01, S03, S12, S21; product-delivery requirements preserved |
| Capability 05-08: UX/design | Running recoverable journey; relevant devices; responsibilities, concrete tradeoffs, no speculative layers | S16; walkthrough; system-design unchanged |
| Capability 09-12: implementation/diagnosis | Early integrated caller, compatible narrow edits, falsifiable cause, unproven reproduction limits | S15-S17, S20; implementation-and-diagnosis unchanged |
| Capability 13-16: quality/operations | Exact current/skipped evidence, risk-based proof, migration recovery and local operating scope | S23, S25, S29; product-operations unchanged |
| Capability 17-18: coordination/learning | Explicit solo/settings, timeout/old owner recovery, no new rule for every code defect | S02-S04, S18-S20, S27; improvement and handoffs |

Canonical ownership stays: policy for authority/startup/allocation; product delivery for problem/requirements/UX/value; system design for boundaries; implementation and diagnosis for code/integration/causes; evidence for proof/provenance/synthesis; product operations for the developed product; handoffs for communication/ownership/recovery; improvement for trials/simplification; records for CLI/accounting; maintenance for skill distribution. Worked examples illustrate these sources without redefining them.

## Research used and applicability

Sources checked on 2026-09-20 during the preceding research and planning. These are design inputs, not validation of this candidate. No provider model recommendation, fixed agent count, token threshold or mandatory protocol was adopted.

| Primary source | Applied guidance and limit |
| --- | --- |
| [Anthropic: multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), 2025-06-13 | Explicit objective/output/boundaries and artifact references. Vendor research-system experience does not establish coding-task efficacy here. |
| [Anthropic: context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29 | Select context and retain decisions/unresolved issues through compaction. No universal reset or token limit inferred. |
| [NAACL: Is Translation All You Need?](https://aclanthology.org/2025.naacl-long.485/), 2025-04 | Translation performance depends on task/model and language nuance. No claim that English or Vietnamese is universally superior for current coding agents. |
| [MAST: Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657), revised 2025-10-26 | Clarification, information loss and verification failures motivate inspection cases. Its measured failures are not a local failure rate. |
| [A2A specification](https://a2a-protocol.org/latest/specification/), current on review date | Distinguishing related tasks, messages, artifacts and clarification informs ordinary-prose exchanges. No A2A schema, SDK or transport is implemented. |
| [Team Topologies concepts](https://teamtopologies.com/key-concepts), current on review date | Flow and interaction modes inform advice/output/review/transfer choices. Applying human-team concepts to agents is an inference, not experimental proof. |
| [SVPG: The Four Big Risks](https://www.svpg.com/four-big-risks/), 2017-12-04 | Viability complements value, usability and feasibility only when it changes a product decision. Practitioner framework, not validated demand. |
| [Anthropic: agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09 | Assess actual end state and use traces for diagnosis in future authorized execution; this author inspection is not that execution. |

## Executed package verification

Executed on Windows with Python 3.14.4. The baseline suite and changed-candidate suite both ran 63 tests: **62 passed, 0 failed, 0 errors, 1 skipped**. The only skip was `test_symlink_escape_is_invalid_when_symlinks_are_available`: Windows denied symlink creation with `WinError 1314`. It is not a pass. No new tests or wording-matching assertions were added to the repository.

| Check actually run | Result and scope |
| --- | --- |
| Platform skill-creator `quick_validate.py skills/project-orchestrator` | Valid skill. |
| `python -B -m unittest discover -s evals -p "test_*.py" -v` | 63 total: 62 passed, 0 failed, 0 errors, 1 skipped for unavailable symlink privilege. |
| `python -B -m compileall -q skills evals` | Exit 0. |
| Parse JSON under evals/skills and root compatibility files | 19 JSON files parsed successfully. |
| Relative Markdown links/anchors across the complete installable Markdown, README, CONTRIBUTING and this report | 137 relative destinations, including 72 anchors, across 17 documents; no missing target/anchor. |
| Baseline SHA-256 comparison | Ten intended existing documentation files changed; all 59 protected files, including all 43 historical eval files, are byte-identical. Two authorized new Markdown files added. |
| Contract comparison | Python helpers/tests, policy template, compatibility metadata and CI unchanged. Policy capability-choice/allocation/checker sections unchanged. Records fields, validation, query semantics, output and exit codes unchanged; only reference voice and relocated accounting explanation changed. |
| Whitespace and public-content inspection | `git diff --check` passed. Scoped private-marker scan clear; author inspected the complete changed prose and new fictional examples/report. This is not a universal secret-detection guarantee. |

The author review clarified the low-risk startup qualifier and external-source provenance, and retained the wall-time/active-effort accounting caveat in records when removing duplicate maintenance text. Documentation checks were repeated after final prose/report edits; executable source and tests remained byte-identical to the successful suite run. The entrypoint stays at 61 lines; added detail is in conditional references and examples, not mandatory startup context. No observed token or time saving is inferred from these edits.

## Remaining limits and delivery boundary

Independent review and independent behavioral evaluation of this candidate: **not run**, as required by the approved solo scope. The prepared method does not close that evidence gap. No measured speed, token, cost, reliability or commercial improvement is established. Historical experiments are evidence only for their named revisions.

Authorized delivery is a normal commit/push and title/body update on the existing open, non-draft PR #1. CI must be checked against the pushed commit; its observed status belongs in the PR handoff. Merge, release, installed-copy adoption, real-product trials and unattended follow-up are outside this work.
