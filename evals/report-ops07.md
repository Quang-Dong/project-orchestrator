# OPS06/OPS07 candidate validation

Status: **self-checked development candidate; independent review and adoption pending**.
This report applies to the source in this PR, not to historical release manifests.
All work and decision inspection for this revision used one session by explicit user direction.
No independent reviewer or new multi-session/product trial was run.

## Source and change

Base: v0.1.0 commit `a20be911054ca8084c510cedf6ebb6cfb1d02d5e`.
The candidate carries the prior OPS05/OPS06 guidance delta plus its artifact verifier
and tests, then simplifies direct/solo work, authorized takeover, handoffs and
bounded improvement. Historical evidence and release manifests are unchanged.
The prior local product pilot failed; it is not acceptance evidence for this source.
Private pilot records and transcripts are not exported.

Policy v1, records v2, the policy template, `check_policy.py` and
`report_workflow.py` retain their base content and CLI interfaces.
The additive verifier reads a path/hash mapping (optionally under `files`) or a
list of `{path, sha256}`; it emits JSON with exit 0 verified, 1 mismatch or 2 invalid.
It checks declared static files, not manifest completeness, acceptance, or a
transactional snapshot against concurrent writers.

## Executed local checks

Environment: Windows, Python 3.14.4.

| Check | Result |
| --- | --- |
| Platform skill validator against `skills/project-orchestrator` | Valid |
| `python -B -m unittest discover -s evals -p "test_*.py"` | 63 total: 62 passed, 1 skipped; exit 0 |
| Verifier tests included in that suite | 7 total: 6 passed, 1 skipped; not additional tests |
| `python -B -m compileall -q skills evals` | Exit 0 |
| JSON parsing of eval/compatibility metadata and policy template | 14 files valid |
| Base comparison of policy template, record contract and existing checker/reporter | No diff |
| Relative Markdown file links in changed documentation | Checked locally; external URLs not revalidated |
| Final patch whitespace and public-content inspection | Checked before commit |

The verifier tests exercise mapping/list input, deterministic output, missing
files, mismatched content, missing/invalid hashes, duplicate keys/normalized paths,
absolute and parent-escaping paths, malformed inputs and self-declared manifests.
The read-only assertion compares both directory entries and content hashes.
The symlink-escape case was explicitly skipped because local creation was denied;
local symlink execution coverage is not claimed.

## Decision inspection, not agent evaluation

The same author inspected the resulting guidance against these situations.
These are self-review conclusions, not runtime multi-session test passes.

| Situation | Decision required by this revision |
| --- | --- |
| Small reversible behavior correction with a relevant check | Direct work when policy permits; behavior alone does not force delegation |
| User explicitly requests solo implementation | No extra sessions; self-check and draft delivery; required independent acceptance stays open |
| Persistence/security/shared-contract risk | Preserve independent-review requirement; do not turn solo work into independent acceptance |
| Authorized lead takeover | Stop old writer or isolate writes, verify source, record intervention; assess product and delegation trial separately |
| Dispatch times out | Reconcile identity/attempt/activity before retry; no duplicate dispatch |
| Handoff references an older source | Carry only demonstrably unaffected evidence; recheck affected behavior |
| Two repairs fail and packet is renamed | Same issue still requires evidenced reassessment or stopped handoff |
| First real caller fails before a large matrix | Diagnose and restore that path before broadening verification |
| Usage or deadline pressure | Preserve acceptance, permission and failed results; simplify process, not truth |
| Draft PR without independent review or product adoption proof | Deliver as draft with open gates; do not release or install |
| A wording correction or small CLI regression | Use relevant local checks; no mandatory paired trial or product pilot |

The inspection found duplicated priorities and absolute takeover prohibitions in
supporting references; they were reconciled with the entrypoint. Contribution and
maintenance guidance no longer requires a matched trial for every change.
Specialist-first and user-controlled main settings remain intact for authorized
coordinated work. No universal model or project-specific allowlist is added.

## Limits and adoption

Package validity and instruction consistency are established only to the extent
of the checks above. Real multi-session behavior, recovery under live contention,
customer value, long-term reliability, resource savings and faster delivery remain
unproven for this revision. Self-review may miss defects.

Hosted CI is tracked on the PR at its exact head commit; this report does not
predeclare its outcome. This draft does not authorize merge, release, global
installation or updates to a consuming project's installed skill. A future
adoption decision must use the evidence and independent review its risk requires.
