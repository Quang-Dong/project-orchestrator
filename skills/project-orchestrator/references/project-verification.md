# Project verification bootstrap

Use when a substantial change needs a real user-facing journey and the repository's current checks do not prove it. The goal is a repeatable, local proof path, not a new product environment.

## Discover before creating

Inspect the repository's current scripts, docs, environment setup, fixtures, authentication path, browser/API runner and retained evidence. Check versions and actual readiness before reuse. Prefer an existing command, fixture, account flow and output location; identify the journey each check proves and any gap. Do not copy unrelated environment files, invent credentials or assume a command starts a ready server.

If the task is substantial and no existing setup can prove the needed journey, create the smallest local `verify-<project>` skill in the repository's established skill location (default `.agents/skills/`). Record the minimum version/readiness checks, authorized local start command, required port and test-data setup, journey, runner, cleanup and evidence output. Add a proportionate feature map of changed paths, entrypoints, user action, expected result and side effects. Keep project-specific commands in that local skill. This reference supplies method only and no project commands or environment values.

## Prove one complete journey

Execute the reused or newly written verification instructions yourself from startup through one complete journey and owned cleanup. Exercise real user-facing operations and observable selectors or responses through the relevant UI/API entrypoints; include the consequential state change and effect. A feature map links changed paths to entrypoints, actions, results and side effects so omissions are visible. Unit tests and direct database writes can support the result, but do not replace the journey when user behavior is the criterion.

Keep test data, browser profile, output directory and processes isolated from user or shared data. Use fictional/local data or an existing authorized fixture. Observe version, readiness, port ownership and data target before acting. Store screenshots, traces, responses or other decisive artifacts at the existing evidence location; keep them after process cleanup and confirm they still exist. Identify the checked source plus relevant configuration and fixture versions or hashes so evidence remains tied to the actual inputs.

Stop only processes and remove only data/output that this verification run created and still owns. If ownership is uncertain, leave it and report the limitation. Do not create a verifier or local service for read-only work or a small task already covered by adequate checks. Do not add dependencies, services, production access or authority as part of verification; if the journey requires any of these, report the missing prerequisite and keep that proof pending.
