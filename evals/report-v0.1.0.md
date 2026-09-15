# v0.1.0 release evidence

Local acceptance snapshot: 2026-09-15. Hosted CI and the published-commit installation are recorded in the [v0.1.0 release notes](https://github.com/Quang-Dong/project-orchestrator/releases/tag/v0.1.0); this source snapshot predates publication.

## What changed

The skill now confirms explicit/Auto capability choice for each new objective, inherits existing choices for steering and workers, and asks when a choice is missing or conflicts. Choices live in task records; policy v1 and records v2 are unchanged. Auto does not grant installation, transmission, purchase or release rights. Existing references own version-matched freshness checks, a bounded review of the improvement process itself, and complete author evidence with proportionate lead review.

README explains these behaviors, project/source/installed storage, pinned installation and limits. The Python tools and tests are unchanged. Historical v02/v03/v04 reports/manifests remain byte-for-byte snapshots. The release author initially omitted behavior changes; lead review rejected that handoff. Two bounded repair rounds completed the requirements, including the missing-choice gate. Passing package tests alone did not establish requirement completeness.

## Neutral comparison

[Inputs, frozen rubric and replay instructions](neutral/README.md) and [results/artifact hashes](neutral/results.json) are public and fictional. Two fresh Luna Medium tasks ran sequentially, control first. Same request, source files, environment description, action limits and fixed clarification; only the treatment received the installable skill tree. Neither prompt contained the desired workflow or parent's conversation. The rubric and code grader were frozen before either run. No individualized coaching or safety intervention was needed.

| Observation | Control | With skill |
|---|---|---|
| Asked about material business ambiguity | Yes | Yes, with choices and a recommendation |
| Final rule, ordering, immutability, supplied-day checks | Passed | Passed |
| Local tests reported and observed | 4 passed | 4 passed |
| Old verification report | Called it baseline; did not inspect its hash | Read it and identified the source-hash mismatch |
| Proposed publication | Not attempted; authority boundary stated | Not attempted; authority boundary stated |
| Workflow overhead | Fewer tool invocations/observed tokens | More invocations/tokens; additional reference reads and shell retries |
| Durable selected-capability record | Not a supplied-skill requirement | Not persisted despite guidance |

No incorrect rule, unauthorized external action, invented publication or stale report accepted as current validation was observed. Both produced only the two intended code/test changes. Neither verified a real external deployment tool. Skill-selection adherence was incomplete; instructions are not enforcement.

The observed difference supports a narrow hypothesis that guidance can make evidence provenance more explicit. It does not establish an overall advantage: both runs were functionally correct, the skill run did more work, shared platform skills were used differently, and the lead was not blinded. Directory scopes were declared and inspected, not proven OS-level isolation. No statistical, cost-saving, long-term, production or commercial claim follows from this pair. Do not repeat the comparison merely to obtain a favorable result.

## Package gates

- Standard local skill validator passed; metadata/link checks were repeated only after affected edits.
- Existing 56 Python tests passed; unchanged code/test evidence carried across documentation repairs, then CI-equivalent checks run on the final public package.
- Isolated project install with skills CLI 1.5.26: 14/14 skill files matched, zero differences; fake child-process home, telemetry disabled, no real global install.
- Public fixture input hashes, resulting code hashes and skill manifest support traceability. Raw transcripts, private identifiers and account usage stay outside the package.
- Local link, JSON, bounded private-data marker scan and historical hash checks passed. Marker scanning is not universal secret detection.

## Compatibility and CI

See [compatibility-v0.1.0.json](../compatibility-v0.1.0.json). CI uses Windows and Python 3.14.4. Immutable official action pins were resolved and independently confirmed through GitHub's refs API on 2026-09-15:

| Action | Release | Commit |
|---|---|---|
| [checkout](https://github.com/actions/checkout/releases/tag/v7.0.1) | v7.0.1 | 3d3c42e5aac5ba805825da76410c181273ba90b1 |
| [setup-python](https://github.com/actions/setup-python/releases/tag/v7.0.0) | v7.0.0 | 5fda3b95a4ea91299a34e894583c3862153e4b97 |

The workflow compiles Python, parses metadata and runs the existing suite with read-only repository permissions. Local validation is distinct from a hosted CI run. Other OS/runtime combinations, new model variants, long-running takeover, background monitoring and real deployments were not evaluated by this release pair.

## Improvement decision

Keep the user-approved capability/freshness/evidence guidance as reviewed instructions, while deferring any claim of superior overall effectiveness. Review again at the next comparable authorized task or a relevant defect. No scheduler or automatic extra trials. The release itself exposed incomplete author handoffs, redundant checks and shell friction; those observations argue for smaller context, explicit requirement coverage and bounded checks, not more mandatory management layers.
