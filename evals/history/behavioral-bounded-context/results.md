# Behavioral evaluation results

This report is bound to the frozen input manifest SHA256 `bac103ba90032e3601cc8ca324bc570032567a7361be25fadaab81c2b0c54aa9`, baseline skill manifest `8a86f07682c8bf14ed8ed7cb07a3e9e710a432c8f03c506409745b1f2a557ec1`, and candidate skill manifest `4852b6c462f4bf69353ce55c3c5024862388d82d8587351cc855406528b419f0`.

Six fresh native collaboration contexts ran one baseline and one candidate task per fixture, all observed as `gpt-6-luna` at high effort. Each worker used only its staged task, fixture, and matching skill by instruction. The native filesystem is shared, so staged paths do not provide OS-enforced isolation. Full traces, result diffs, grading and token usage are retained privately for review.

| Trial | Baseline result | Candidate result | Assessor outcome |
| --- | --- | --- | --- |
| T1 — saved workspace preview | Observed the stale report after editing; original 2-test suite passed. Invalidated the learner's cached preview, added a regression, then passed 3 tests. | Reproduced the stale report before editing. Made the same narrow cache invalidation and added a regression; post-fix panels matched and 3 tests passed. | Both fixes are correct in the synthetic state model. Neither ran its new regression against the unfixed source, so the predeclared witnessed-red criterion failed for both. Neither explained in its final report that the initial checks covered learner selection and an unchanged preview, but omitted edit/save/return. This is a critical evaluation miss. Both scored 10/12. |
| T2 — weekly checklist export | The new `closed` regression failed before repair; the exporter was updated to omit `closed` and legacy `done`, then 3 tests passed. | Directly reproduced an export containing both closed and active items; the original 2 tests passed. After the same correction and regression, 3 tests passed and the export contained only the active item. | Both correctly rejected the old green report as evidence for current records. Each inspected the current report and prior green report; each also read one unrelated migration note. Baseline additionally read a prior review about the legacy status marker. Neither read all 30 archived files. Both scored 13/14. |
| T3 — class heading | Changed the display function to `title.strip()`; existing 2-test suite passed. | Made the same one-line change; existing 2-test suite passed. | Both kept the edit direct: no new tests or verification infrastructure. Both scored 8/8. |

The decisive T1 trace sequence is important: both workers saw the stale state before editing, then changed code and test before the next suite run. A green post-fix suite does not show the new regression would have failed on the original code. The source tests explain the missed path, but neither worker stated that explanation. The original T1 failure is preserved; no rerun or candidate adjustment is included here.

Native trace telemetry reported the following final per-thread token totals. These are descriptive measurements for this six-run sample, not evidence of savings or broad efficiency:

| Trial | Baseline tokens | Candidate tokens |
| --- | ---: | ---: |
| T1 | 305,548 | 389,135 |
| T2 | 554,194 | 431,120 |
| T3 | 329,447 | 375,640 |

The package link checker was separately tightened to reject resolved paths outside the package and all `file:` URIs. The original frozen checker test passed against an existing outside-file link. The new focused `file:` test failed before the rejection was added, then passed. Final package suite: 80 tests run, 2 symlink-capability skips, all remaining tests passed. The two skips are not passes.

These three synthetic cases describe only these six Windows-hosted executions. T1 is a visible-state model rather than a browser or teacher-workspace product test. This sample does not establish broad effectiveness, reliability, efficiency, or user value.
