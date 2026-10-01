# Authorized local adoption — 2026-09-29

The maintainer accepted the frozen candidate at 15:02:06 UTC after separate
agent review returned `accepted-with-nonblocking-findings`. The global skill
was installed at 15:02:29 UTC and the native Codex host discovered it at
15:02:45 UTC. Installation was explicitly authorized and remains separate
from any public release or repository merge.

## Installed artifact and recovery

- The complete 20-file skill matched [skill-manifest.json](skill-manifest.json)
  exactly. Aggregate SHA-256:
  `3129653dc7f74dda6bf986e445cfe3c3756c2bf0910eca587106f8fddff7ac05`.
- Raw manifest SHA-256:
  `0ece20cf5e1bd3318297d074ba3e5af57e1a1f2db516708ee207d91267d623f3`.
- These are exact installation-byte hashes, including existing Windows line
  endings, rather than normalized Git-object hashes.
- The previous 19-file distribution and its verified manifest were retained
  locally for rollback. Recovery moves the current distribution aside,
  restores that backup to the original location, and checks its manifest.
- No evaluation files, raw logs or caches were included in the installed set.
- Native read-only `skills/list` with `forceReload` found the global skill and
  the project-local verifier enabled at their intended locations, without
  discovery errors or creating another task/thread.
- Policy v2, measurement records v2, reporter v3 and GPT-6 Luna worker policy
  remain unchanged. The main-session model was not changed.

## Verification scope

The skill package had 74 passing tests and one skipped Windows symlink test,
plus structural and local-link checks. The project-local verifier had four
passing unit tests, typecheck, scoped lint and documentation checks.

In the original application checkout, isolated production builds and browser
runs completed: smoke 6/6, teacher suite 74/74, account suite 12/12. After a
reviewer repaired one journey mapping and added selector-validity coverage,
the two affected browser checks each passed. Prior full/smoke evidence was
reused only after a source comparison; it was not represented as a new full
run. Native application tests were not rerun for that tooling update.

All 322 original protected source/public files matched their starting hashes.
Project tooling, tests and local verification documentation are maintained in
that project and are not exported in this skill PR.

The [six-execution report](initial-results.md) preserves copied-workspace
Turbopack limitations, isolated dev-server proof, package-manager metadata
cleanup, handoff corrections and unknown usage. This local adoption does not
certify arbitrary dependency-junction layouts, production application behavior,
durable storage, Claude Code or any other untested runtime.

Detailed original installation, rollback and trial evidence remains in private
local maintainer artifacts. This source-relative summary omits machine paths,
private project names and account/session identifiers for public review.
