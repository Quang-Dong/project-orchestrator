# Evaluation evidence index

Start here to identify what was checked and which source it applies to. This directory is maintainer evidence; agents using the installed skill do not need to load it for ordinary product work. A report, manifest or passing package test is not a universal acceptance verdict.

## Current candidate and open questions

- [Runtime coordination review](runtime-coordination-review.md): current author inspection and package verification, based on PR head `1b4b42ff6b52e533ec3dace030e56d3f9ed9509e`. The reviewed candidate is the commit containing this update; final pushed SHA and hosted CI are recorded on [PR #1](https://github.com/Quang-Dong/project-orchestrator/pull/1).
- [Six prepared coordination packets](coordination-readiness.md): real-event prerequisites, fixed interventions and separate worker/assessor material. **Not executed.** Unavailable runtime variants remain not run.
- [Five prepared behavioral packets](behavioral-readiness.md): concrete inputs, worker prompts, fixed follow-ups and assessor criteria. **Not executed.** Do not give the whole document or its rubric to a worker.
- Independent behavioral evaluation, independent review of this candidate and measurement of unnecessary gate overhead remain **not run**. No demonstrated efficiency, reliability, token saving or user-value improvement is claimed.

## Executable package tests

Run from the repository root:

```sh
python -B -m unittest discover -s evals -p "test_*.py" -v
python -B -m compileall -q skills evals
```

| Tests | What they establish |
| --- | --- |
| [Policy](test_policy.py) | Checker input/selection contracts and read-only behavior; not consent or live capability. |
| [Reporter](test_report_workflow.py), [acceptance](test_report_acceptance.py), [query views](test_report_views.py) | Record validation, aggregation, revision-aware report acceptance and query semantics; not real product acceptance. |
| [Artifact verifier](test_verify_artifact.py) | Declared-file/path validation within tested conditions; not semantic completeness or a concurrent snapshot. |

These tests exercise Python tools, not agents following the prose. Report actual run counts, failures and skips from the named revision; do not reuse historical totals as a current result. Tests beneath the historical neutral fixture/outcomes belong to those example projects, not additional successes to add to the root suite count.

## Reports by revision and evidence class

| Recorded revision or snapshot | Evidence | What remains limited |
| --- | --- | --- |
| Initial content-hashed skill snapshot, 2026-09-15 | [Initial report](report.md), [decision outputs/rubric grading](results.json), [initial manifest](skill-manifest.json) | Package/isolated installation checks and two fresh contexts answering fictional decisions. Scenario actions were not executed; no current-candidate claim. No evaluated Git SHA is supplied by the initial manifest. |
| Unpublished v02 | [Report](report-v02.md), [workflow decisions](workflow-results-v02.json), [manifest](skill-manifest-v02.json) | Reporter/package checks, fictional decisions and a bounded actual takeover described in the report; local evidence, not production or current behavior. |
| Unpublished v03 | [Report](report-v03.md), [manifest](skill-manifest-v03.json) | Query checks and four sequential outcome trials; the report's task failures and limits remain part of the evidence. No universal efficiency conclusion. |
| Unpublished v04 | [Report](report-v04.md), [manifest](skill-manifest-v04.json) | Package checks, fictional decisions and a bounded local product pilot. Private pilot source is not public reproducible evidence; no production or current-candidate validation. |
| Release v0.1.0; published commit `a20be911054ca8084c510cedf6ebb6cfb1d02d5e` | [Release report](report-v0.1.0.md), [manifest](skill-manifest-v0.1.0.json), [release notes](https://github.com/Quang-Dong/project-orchestrator/releases/tag/v0.1.0) | Report/manifest are the content-hashed prepublication snapshot; release notes bind hosted CI and installation to the published commit. Later guidance is outside that acceptance. |
| OPS06/OPS07 development snapshot, last updated at `766f4d0` | [Report](report-ops07.md) | Author checks and artifact-verifier tests; independent review/adoption pending. Its mention of a prior failed pilot is not acceptance of this source. |
| Adaptive update `a8e0b8f`; baseline `766f4d0` | [Author review](adaptive-orchestration-review.md) | Ten fictional decision inspections and package checks; not agent trials. |
| Nine-capability update `3050382`; baseline `a8e0b8f` | [Author review](capability-coverage-review.md) | Eighteen fictional decision inspections and one walkthrough; not demonstrated product-development effectiveness. |
| Communication update `7a8063b`; baseline `3050382` | [Author review](communication-and-simplification-review.md) | Thirty fictional decision inspections and one walkthrough, with package checks; independent execution not run. |
| Authority/index update `1b4b42f`; baseline `7a8063b` | [Author review](authority-and-gate-review.md) | Source/gate interpretation and package checks only; prepared behavioral cases remain unrun. |
| Current runtime coordination update; baseline `1b4b42f` | [Author review](runtime-coordination-review.md) | Sixteen fictional decisions, one walkthrough and package checks; six coordination packets prepared, not executed. |

Version labels without an evaluated Git SHA refer to their recorded content hashes and report scope. Do not invent a commit identity from a filename or treat a later commit carrying old files as the revision originally evaluated. Historical wording such as “this PR” retains the report's original scope, not every later PR commit.

## Scenario definitions and historical task execution

| Material | Classification and how to read it |
| --- | --- |
| [Initial scenarios](scenarios.json), [scenario notes](scenarios.md), [rubric](rubric.json) | Input definitions and withheld grading criteria. Historical answers are in `results.json`; the scenarios are not proof their actions ran. |
| [Workflow cases](workflow-cases.json), [v03 scenarios](scenarios-v03.md), [v04 scenarios](scenarios-v04.md) | Definitions for the corresponding historical reports; any claimed observation must come from that report, not the scenario text. |
| [Neutral comparison](neutral/README.md), [protocol](neutral/protocol.json), [results](neutral/results.json) | Actual historical control/skill task executions against frozen inputs, with resulting code under `neutral/outcomes/`. Both were functionally correct; more work/tokens in the skill run did not establish overall advantage. Shared platform instructions, one pair and declared isolation limit inference. |
| [Neutral fixture](neutral/fixture/README.md), [existing grader](neutral/grade.py) | Reusable fictional input and deterministic code check. Baseline failure against the new rule is intentional. The grader does not assess authority, truthful reporting or multi-session coordination. |
| [Behavioral readiness](behavioral-readiness.md) | Five solo packets prepared at `1b4b42f`, with no execution results. Preserve worker/assessor separation. |
| [Coordination readiness](coordination-readiness.md) | Six current coordination packets, with no execution results. Real timing/control prerequisites and unsupported variants are explicit; no new harness or grader. |

## Manifests and compatibility

The five historical manifests above identify declared files in their own snapshot: initial, v02, v03, v04 and v0.1.0. They are not manifests for the current candidate. Check them against the matching source, not a moving branch; an expected mismatch after later edits is not evidence that the historical snapshot changed.

Use the associated [v03](../compatibility-v03.json), [v04](../compatibility-v04.json) and [v0.1.0](../compatibility-v0.1.0.json) compatibility records only for the environments they describe. A matching file hash establishes identity, not correct product behavior, review completion, installation authority or runtime support.

Keep historical files immutable. New work adds a scoped report or packet and updates this index; it does not rewrite old results as current passes. Public evidence uses fictional or sanitized material, with private logs and identifiers excluded.
