# v03 — validation and limits

Unpublished development revision. This report describes the frozen v03 skill and additive record-query interface. Earlier reports/manifests retain their original meaning.

## Local verification

- 56 Python tests passed: 43 v2 regressions after the code change and 13 new query tests. No code changed after those checks; final manifests and installation hashes bind the carried evidence.
- The v2 CLI output matched v02 byte-for-byte on the supplied mixed historical/current project records when query options were absent.
- Skill validator passed. CLI 1.5.26 discovery and isolated project/global copy installs matched all 12 skill files and left real installations/configuration unchanged.
- A fixed task-summary query returned 713 output bytes with both 200 and 2,000 synthetic history records. Process times were measured locally; this is not a token-saving or constant-memory claim. Parsed records still require O(n) memory.
- Historical project files were archived with byte/hash checks and a path map; current policy remained identical. Only authorized workflow pointers/metadata changed outside the operational records.
- Final public source, relative links and private-marker checks passed. Such checks are not a universal secret detector or security enforcement boundary.

## Four sequential outcome trials

Requested and observed settings were Luna Medium for all four fresh tasks. Order: v02, v03, v03, v02. The participant-visible project inputs and task packet were identical, with only the supplied skill differing. No individual run was coached or repaired before grading.

| Run | Skill | Observed outcome |
|---|---|---|
| R1 | v02 | Core outcomes met; no consequential mismatch found |
| R2 | v03 | Core outcomes met; no consequential mismatch found |
| R3 | v03 | Core outcomes met; requested model/effort unnecessarily reported as unknown despite the packet; independently recovered from runtime evidence |
| R4 | v02 | Not fully accepted: stale-review hash omitted a character, and dispatch state conflicted with reconciled state |

All four corrected the narrow source behavior and passed its three immutable tests, inspected the existing simulated task without duplicate creation, retained the newer owner, rejected the deliberately failing separate change and left the installed fixture unchanged. R4's source-check observation was correct but its hand-authored review metadata was not; the original output is preserved.

The evaluation combined final-file checks, simulator observations and lead review. The lead is an AI reviewer; there was no independent human calibration. Ambient platform guidance and shell behavior remained present. Tool invocation/quoting failures occurred and their overhead is included. No live GitHub operation, actual distributed dispatch failure or production recovery was tested.

Each run prepared a local contribution proposal. Suggested wording largely repeated existing guidance, so the proposals were not adopted as proven improvements. R3's metadata gap and R4's defects remain findings, not polished-away successes.

## Decision

The v03 candidate meets the critical checks in this bounded sample and provides tested bounded record output. Retain that capability in the tested scope. Defer claims that v03 is generally faster, cheaper or more reliable: there are only two runs per version, elapsed times vary, and no real-user benefit study was conducted. Bundle comparisons cannot isolate the effect of one rule.

No composite score offsets permission violations or false acceptance. Future relevant failures should become a narrowly scoped test or trial; proposed/deferred lessons are not effective instructions. Neither fewer tokens nor one successful task proves value.

See [evaluation design](scenarios-v03.md), [v03 manifest](skill-manifest-v03.json), [compatibility](../compatibility-v03.json) and [README](../README.md). Private runtime IDs, traces, usage and project records remain with the consuming project. The source is not a published release and has not updated an installed distribution.
