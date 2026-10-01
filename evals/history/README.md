# Evaluation history

This archive keeps historical reports, execution packets, scenario inputs, manifests, compatibility records and run outputs available to Git. Each verdict remains tied to its original candidate and stated limits. A prepared packet stays unrun; a historical adoption does not certify the current source or a current installed copy.

## Archive groups

- [Reports and recorded results](reports/report-v0.1.0.md): versioned author and trial reports with their original result files.
- [Reviews](reviews/subagent-default-review.md): historical author reviews of earlier source revisions.
- [Scenarios and rubrics](scenarios/scenarios.md): historical task definitions and grading criteria.
- [Prepared packets](packets/behavioral-readiness.md), [agent-execution material](agent-execution/worker-packets.md) and [subagent-default material](subagent-default/worker-packets.md): execution inputs and assessor documents. Their recorded not-run status remains in the documents.
- [Behavioral evaluation, 2026-09-29](behavioral-20260929/initial-results.md): frozen reports, adoption record and manifest.
- [Bounded-context evaluation](behavioral-bounded-context/results.md): setup, results, recheck, adoption decision and manifest. Original failures and limits remain unchanged.
- [Regression-comparison historical results](behavioral-regression-comparison/results.md): verdict, protocol, measurement correction, adoption record and manifest. The current runner setup and synthetic fixtures remain under `evals/behavioral-regression-comparison/`.
- [Neutral comparison history](neutral/protocol.json): protocol, outcomes and results. The reusable fixture and grader remain under `evals/neutral/`.
- [Historical environment records](environment/compatibility-v04.json): compatibility evidence for the environments those records describe.
- [Historical manifests](manifests/skill-manifest.json): source manifests retained byte-for-byte for their original snapshots.

## Reading limits

Do not infer a Git revision from a filename, treat a matching hash as acceptance, or carry historical wording such as “this PR” onto later revisions. Reports keep their original verdicts, failures, unrun conditions and evidence limits. Private local records removed from the repository are not recreated from these public materials.

## Public-copy path handling

Host-specific absolute paths, private project names, article slugs, source revisions and application-specific environment identifiers in the published evaluation copy were redacted or generalized. The local `markdown-before.json` artifact under `.data/artifacts/maintenance/history-cleanup-20261001/` preserves earlier path text; exact pre-export versions of current evaluation Markdown are kept under ignored `.data/artifacts/pr3-publication/20261001-current-source/private-export-original/`. The old host-local trial artifacts were deleted and are not included in this public copy. Historical results, measurements, verdicts and limits are unchanged.

## Historical v0.1.0 installation example

These commands install the **historical v0.1.0 release**, with its older contracts. They are retained as historical instructions and do not install or validate the current source candidate. Verify the selected tag and its [historical manifest](manifests/skill-manifest-v0.1.0.json); global installation affects other projects.

```sh
npx skills add https://github.com/Quang-Dong/project-orchestrator/tree/v0.1.0 --skill project-orchestrator --agent codex --copy
npx skills add https://github.com/Quang-Dong/project-orchestrator/tree/v0.1.0 --skill project-orchestrator --agent codex --copy -g
```
