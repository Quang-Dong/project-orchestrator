# Adaptive orchestration and product feedback review

Status: self-checked source candidate; independent review and installed-copy adoption remain open.
This is a single-session source update, not an independent review or an agent evaluation.

## Baseline and scope

Baseline: PR #1 head `766f4d04a5150cf3b7b19a8cbb7ed096c8ef8502`, inspected before edits.
The source worktree was clean. The baseline Python suite ran 63 tests: 62 passed,
one skipped because Windows symlink creation was unavailable.

The baseline entrypoint required specialist-first execution for substantial work;
both it and the policy reference defaulted to the highest allowed effort. These
unconditional defaults conflicted with task-proportionate allocation. Product
guidance already covered users, value and technical acceptance, but did not tie
priority and a primary value signal to a feedback owner/event and a next decision.
PR metadata was open and non-draft while its body described keeping it in draft.

The user authorized adaptive allocation, a product feedback loop, single-session
implementation/self-inspection, and commits to the existing PR. No subagents,
multi-session experiment or host-product pilot is included. Existing public
interfaces and historical evidence remain unchanged.

## Change and owning guidance

- [Operating modes](../skills/project-orchestrator/SKILL.md#choose-the-smallest-useful-operating-mode): small direct work, one end-to-end owner, targeted delegation and explicit solo work. Significant size alone no longer mandates another session.
- [Allocation policy](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation): honor explicit settings; otherwise use complexity, uncertainty, consequences and observed runtime support. Start from a permitted observed default when no stronger evidence exists; diagnose before increasing resources.
- [Dispatch](../skills/project-orchestrator/references/handoffs.md#dispatch): link expected output, delegation benefit, independent scope and integration owner in the existing handoff. Reviewer output is a verdict/findings, not another implementation scope.
- [Product decisions](../skills/project-orchestrator/references/product-delivery.md): priority and the riskiest assumption, smallest useful delivery or uncertainty-reducing step, one primary value signal, preserved quality and a named feedback decision.
- [Bounded improvement](../skills/project-orchestrator/references/improvement.md#measure-useful-progress): separate technical acceptance, observed value and workflow-trial criteria; link product feedback rather than duplicate it.

The author clarified two boundaries during inspection: coordination cost cannot
waive required independent review, and closing a technical scope cannot close
unverified user-value criteria or an overall outcome that depends on them.

## Decision inspection matrix

Each row is the author's reading of the baseline and revised instructions against
a fictional situation. Outcomes below describe required decisions, not observed
agent behavior, runtime passes, or comparative performance results.

| Case | Baseline finding | Revised decision and owning section |
| --- | --- | --- |
| 1. A small reversible behavior correction has a relevant existing check. | Already supports direct work; preserve it. | Work directly when policy permits; no extra session or experiment. [Modes](../skills/project-orchestrator/SKILL.md#choose-the-smallest-useful-operating-mode). |
| 2. One feature spans UI, application logic and storage. | End-to-end ownership existed, but substantial work also triggered specialist-first. | Keep one authorized owner; check the smallest real caller plus a material failure before expanding. Required data review remains open until independently satisfied. [Modes](../skills/project-orchestrator/SKILL.md#choose-the-smallest-useful-operating-mode), [sequencing](../skills/project-orchestrator/references/product-delivery.md#sequence-complete-increments). |
| 3. Two authorized workstreams have disjoint writes and distinct outputs. | Independent parallelism existed; expected delegation benefit was not explicit. | Delegate only with a concrete benefit, expected outputs and integration owner; independently passing outputs still need integration checks. [Dispatch](../skills/project-orchestrator/references/handoffs.md#dispatch), [integration](../skills/project-orchestrator/references/handoffs.md#ownership-and-integration). |
| 4. The user requests solo work or an explicit worker effort. | Both instructions already had authority; preserve them. | No additional sessions for solo work; retain required review as pending. Preserve explicit settings and main-session ownership. [Modes](../skills/project-orchestrator/SKILL.md#choose-the-smallest-useful-operating-mode), [allocation](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation). |
| 5. A persistence/security change is under deadline pressure. | Independent review was required. | Keep that gate even when resources are scarce; self-check is not independent acceptance. [Verification](../skills/project-orchestrator/SKILL.md#verify-and-report). |
| 6. Requested settings are unavailable, or the runtime default is unknown/outside policy. | Highest allowed effort was the fallback; recovery wording could be read as replacing an explicit choice. | Reconcile explicit-setting conflicts; never substitute outside policy or fabricate a default. An unspecified setting can use a justified authorized alternative. Otherwise keep dependent dispatch blocked and ask the focused question. [Allocation](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation), [recovery](../skills/project-orchestrator/references/policy.md#change-and-recovery). |
| 7. The same issue survives two repairs; a higher effort is suggested. | Reassessment and repair-count continuity already existed. | Reassess diagnosis/approach before another attempt; elapsed time/failure alone is not proof that more effort helps. [Review and repair](../skills/project-orchestrator/references/handoffs.md#review-and-repair), [allocation](../skills/project-orchestrator/references/policy.md#capability-choice-and-adaptive-allocation). |
| 8. A product idea has no verified need, baseline or target. | Could ask discovery questions and avoid invented demand, but lacked a concrete priority/feedback loop. | Identify the material unknown; choose the smallest useful investigation, including no-code work. Use an agreed qualitative signal or preserve unknown measurements rather than invent numbers. [Problem](../skills/project-orchestrator/references/product-delivery.md#choose-the-problem), [success](../skills/project-orchestrator/references/product-delivery.md#define-success-before-expanding). |
| 9. Technical checks pass but no user has exercised the result. | Real-user evidence was distinguished, but ownership of the next feedback decision was implicit. | Report technical acceptance and unverified value separately. Name source, owner and review event; keep any user-value acceptance criterion open. Continue/adjust/defer/stop only on the applicable evidence, without creating monitoring or communication authority. [Feedback](../skills/project-orchestrator/references/product-delivery.md#observe-value-and-decide-next). |
| 10. Dispatch times out, a late owner returns, or the handoff proves an older revision. | These safeguards already existed. | Reconcile identity and ownership; late output cannot overwrite the current owner. Carry only unaffected proof after source comparison, rerun affected checks and keep unresolved acceptance pending. [Handoffs](../skills/project-orchestrator/references/handoffs.md). |

Additional counterexamples: permission for small direct work does not authorize
all substantial solo work; an allowed maximum is not a target; choosing an allowed
runtime default does not prove it is optimal; a missing default does not imply
maximum effort. A blocked increment can coexist with authorized independent work,
while opening more dependent work needs a reason. Product continue/adjust/defer/stop
decisions do not add events to records v2 or automatically adopt a skill trial.

## Verification

Environment: Windows, Python 3.14.4. Checks below ran after the guidance changes;
the result-recording edit changes only this report. Executable code and tests did
not change. The source identity is the commit containing this report, with the
baseline above identifying the prior revision.

| Check | Executed result |
| --- | --- |
| Platform skill-creator `quick_validate.py` on `skills/project-orchestrator` | Valid; exit 0 |
| `python -B -m unittest discover -s evals -p "test_*.py" -v` | 63 total: 62 passed, 1 skipped; exit 0 |
| `python -B -m compileall -q skills evals` | Exit 0 |
| Parse all JSON under evals/skills plus root compatibility metadata | 19 files valid |
| Relative Markdown destinations and anchors in the seven changed/added documents | 64 local links, including 26 fragment targets, valid |
| Compare all 64 baseline tracked-file hashes | Six intended guidance documents changed; other 58 files unchanged, including all 41 pre-existing eval files |
| Compare policy template, records contract, Python helpers/tests and compatibility records | Byte-identical to baseline; no CLI/schema/dependency change |
| Compare explicit/Auto capability-choice paragraph | Unchanged |
| `git diff --check` | Exit 0; Git emitted only LF/CRLF normalization notices |
| Inspect complete scoped diff and public report; bounded private-marker scan | No private project data, machine paths, account/session identifiers or credentials found; marker scanning is not a universal secret guarantee |

The skipped case is `test_symlink_escape_is_invalid_when_symlinks_are_available`:
Windows denied symlink creation (WinError 1314). It is not a passing test. The
verifier subset remains seven total: six passed and one skipped, already included
in the 63. No test was added to match prose, headings or expected wording.

The link/JSON/hash/privacy checks used temporary read-only inspection scripts;
they add no package dependency or shipped tool. External URLs were not revalidated
by the local-link check. Earlier reports and their declared test counts were not
rewritten. The public report omits local validator/log paths and raw transcripts.

## Limits and delivery

The [prior candidate report](report-ops07.md), historical comparisons, manifests
and failure records retain their original scope. This change does not retroactively
validate them or change a consuming project's installation. Policy v1, records v2,
the policy template, all three executable helpers and their CLIs remain unchanged.
The explicit/Auto capability-choice confirmation and its inheritance are preserved.

The work establishes instruction consistency only to the extent of this author's
inspection and package checks. No independent review, live delegation, product
pilot, user research or before/after performance experiment was run. Faster
delivery, lower resource use, better real-user value and long-term reliability
remain unproven. Deterministic tests validate the helpers, not these behavioral claims.

Delivery is an update to the existing open PR with its non-draft state preserved.
Commit/push and PR metadata updates are authorized; merge, release, deployment and
installed-copy updates are not included. Hosted CI must be inspected on the pushed
commit; this report does not predeclare its outcome. Required independent review
and adoption decisions remain separate from PR delivery.
