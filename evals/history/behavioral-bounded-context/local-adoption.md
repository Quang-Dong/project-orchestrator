# Local adoption decision

Status: **withheld**. The bounded-context candidate was implemented and checked, but it did not meet the predeclared behavioral acceptance conditions after the one permitted adjustment. The installed global skill remains the preceding PR #3 artifact.

## Source and evidence

- Baseline: `5cc31487efd6da748a4a0206efccde6b13a2a6b8`; its 20-file skill manifest SHA256 is `8a86f07682c8bf14ed8ed7cb07a3e9e710a432c8f03c506409745b1f2a557ec1`.
- Final candidate: the uncommitted source tree bound by [skill-manifest.json](skill-manifest.json), SHA256 `acc9a2ba21b8ba1d336cdc44115669e42be7f4ed9638b5c6ee7aa00cfebac594`. The frozen skill contains 20 files. Evaluation fixtures, traces, logs, caches and reports are outside the installable package.
- [Initial six-run results](results.md) retain the original T1 failure and T2 partial result. The single adjustment moved the conditional before/after regression procedure into the diagnosis path and linked closure evidence to it. T1 and T2 were then rechecked in four fresh contexts with the same task inputs, model, effort and rubric. T3 evidence was reused after confirming neither original execution read the two modified references.
- [Post-adjustment results](recheck-results.md) retain the four additional executions. Independent review confirmed the remaining T1 failure. It classified T2's external memory read as a context/scope confound under inherited runtime instructions, rather than an intentional authority breach; T2 does not demonstrate fully confined context selection.
- On the final candidate, the T1 repair and resulting tests were correct, but the new test and implementation were changed together. Only the post-fix run was observed. This fails the required witnessed regression on the unfixed source and blocks adoption irrespective of the remaining scores.
- Package tests on the final source: 80 run, 78 passed, 2 skipped because this Windows environment could not create the tested symlinks. Skill structure validation, scoped link checks and `git diff --check` passed. Policy v2, records v2, reporter v3, artifact-verifier code and model policy were unchanged.

## Installation state

On 2026-09-29 at 17:49 UTC (2026-09-30 locally), all 20 installed global file hashes still matched the pre-change baseline. No promotion, replacement or rollback was performed. An earlier read-only check found that baseline skill through the actual Windows user's Codex runtime; sandbox-only discovery did not expose the same user skill. The new candidate has not been installed or runtime-certified.

The baseline source and installed files, initial candidate, adjusted candidate, manifests, failed setups and exact trial traces are retained in the authorized local evaluation artifacts. Installation preparation was dry-run only. The public manifest identifies the candidate; it is not evidence of semantic correctness or authorization to install.

Main and independent review corrected two premature summary claims against ordered tool traces and rejected a T2 stage accidentally copied from completed outputs before execution. The stage was rebuilt and hash-compared with original inputs. These are retained evaluation defects and interventions; they must not be presented as uninterrupted successful delegation. No main-session implementation replaced any trial worker's code.

## Limits and remaining decision

No further tuning or behavioral retries were performed after the one allowed adjustment. Adopting this candidate requires a separately authorized correction and new evidence for the unresolved condition; the current task does not silently extend into another benchmark. No commit, push, merge or release was performed, and no teacher workspace project file was changed.

These are synthetic Codex/Windows trials. They do not certify teacher workspace project browser behavior, Claude Code, another runtime, or general reliability and savings. Native token totals include repeated and cached input; they are not account-allowance percentages, billing estimates or total project cost. Source guidance grew from 117,084 to 121,001 UTF-8 bytes; the intended reduction is selective routine reading, and no measured reduction in reading or total resource use has been established.
