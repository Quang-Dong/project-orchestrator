# Post-adjustment behavioral recheck

This report records the single authorized candidate adjustment recheck for T1 and T2. The original pilot remains unchanged in [the initial results report](results.md). The recheck used the frozen baseline skill (manifest `8a86f07682c8...`) and candidate-adjusted skill (manifest `acc9a2ba21b8...`), the same task packets and pristine fixtures, and fresh `gpt-6-luna` / `high` contexts. The staged-input manifest is retained in the local ignored evaluation data with SHA256 `2baa248c8ab878906193a37f3f31ac070f0f9196e588d709e65910984130596e`.

## Findings

| Trial | Baseline | Candidate-adjusted | Result |
| --- | --- | --- | --- |
| T1, saved-note preview | Observed the editor/report mismatch. The new regression failed against the original fixture, then passed with the focused cache invalidation; the 3-test suite passed. | Observed the mismatch and explained why the original two tests missed it. The worker applied the new test and source fix in one patch, so the regression was never run red; the 3-test suite passed. | The baseline met the red-regression criterion. The adjusted candidate still missed this critical method criterion. This remains synthetic state/API evidence, not browser or teacher-workspace product verification. |
| T2, closed checklist export | Fixed the `closed` status behavior and passed all 3 tests. The worker rejected the prior green report as evidence for the current source and format. | Witnessed the new `closed` regression fail before the source change, fixed the behavior, and passed all 3 tests. The worker rejected the prior green report as evidence for the current source and format. | Both sides corrected the fixture behavior. Baseline opened one unrelated archived review note. The adjusted candidate's user-memory lookup followed inherited memory guidance; reviewers classify it as a context/scope confound, not an intentional authority breach. That read means the run does not prove selective retrieval confined to the staged workspace. |

For T1, the baseline first ran the existing two tests successfully, then ran the added regression against unchanged code and observed it fail, followed by a three-test pass after the source change. The adjusted candidate first reproduced the mismatch and saw the two-test suite pass, then applied its test and implementation changes together; its only later test run was green. Thus the adjustment did not close the red-before-fix gap in this execution.

The T1 baseline also queried the user-memory index under inherited memory guidance. This is a context/scope confound; no edits outside its staged fixture appear in the diff, and it does not change the observed regression sequence.

The original T3 result is reused only as scoped evidence: both original T3 runs read the same task fixture files and made the same one-line title-whitespace change using the existing tests. Neither opened either tuned reference (`implementation-and-diagnosis.md` or `improvement.md`), and the tuned content did not change the T3 task or fixture path. This supports reuse for that observed tiny-edit case; it does not establish broader behavior.

## Native execution telemetry

The durations below are elapsed spans between timestamps in each exact native session trace. Token counts come from the final observed `thread_token_usage` record. `cached input` is a subset of `input`, not an additional token amount. These records do not establish quota consumption, cost, or general efficiency.

| Run | Trace elapsed | Input tokens | Cached input subset | Output tokens | Total tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| T1 baseline | 136.8 s | 457,309 | 439,808 | 3,403 | 460,712 |
| T1 candidate-adjusted | 81.2 s | 341,693 | 274,688 | 2,074 | 343,767 |
| T2 baseline | 72.7 s | 370,380 | 337,920 | 1,886 | 372,266 |
| T2 candidate-adjusted | 170.2 s | 557,750 | 536,576 | 3,459 | 561,209 |

Detailed scores, exact trace hashes, fixture diffs, native timestamps, and raw trace references are retained in the private evaluation record under `.data/bounded-context-20260929/evaluation/`. The T2 staging mistake and failed staging attempt are preserved separately; the executed pair was rebuilt from the pristine public fixture and checked against the original input manifest before launch.

## Limits and status

T1 exercises a small synthetic in-memory state model. T2 exercises a synthetic exporter and supplied JSON data. Neither demonstrates browser behavior, live weekly exports, or product acceptance. Each side has one fresh context per affected trial; these paired results do not establish broad or causal effectiveness. The initial pilot and its result remain retained.

**Adoption remains withheld.** In particular, the adjusted T1 execution still did not demonstrate a failing regression before its source fix. This report records the bounded recheck; it does not approve the adjusted skill for installation or claim general effectiveness.
