# Project-owned policy and runtime gate

The user owns lead model/effort choices. A worker is any separate implementation or review session. A more capable model is not permission to lead, spend, install or deploy.

## Start with existing authority

Read the current instruction and relevant confirmed limits first. Resolve only the missing decision that changes the next action:

| Current situation | Next action |
| --- | --- |
| Clear, small, low-risk reversible work within confirmed direct-work authority | Make the bounded change and relevant check; no extra dispatch packet, handoff or repeated permission question. |
| Substantial work with current policy/status | Read the current owner, source and linked acceptance/evidence needed for this outcome; reuse valid decisions instead of loading all history. |
| Explicitly authorized substantial solo work, with only delegation-specific settings missing | Continue within that task's authority and applicable limits; leave delegation unavailable. Do not fill in policy, broaden `smallDirectWork` or treat solo permission as authority for external actions. |
| Missing/conflicting authority, material requirement, applicable budget or capability choice | Group the unresolved questions, explain which action depends on the answer and stop that action; continue separately authorized work. |

An absent policy file does not manufacture defaults or erase a current scoped user instruction. Establish the authority needed for the actual action; missing worker settings alone do not block separately authorized solo work. The explicit/Auto capability confirmation below still applies. Reading a skill is neither confirmation nor permission to create project records outside the authorized task.

## Files and unchanged schemas

Use `docs/orchestration/policy.json` for confirmed limits, `status.md` for current role/owners/version/next action, `improvements.jsonl` for trials and `metrics.jsonl` for dated observations. Existing requirement registries remain authoritative. Do not store secrets or account identifiers, create a competing backlog, or add capability-choice fields to policy v1 or records v2.

The packaged [policy template](../assets/policy.template.json) is deliberately **UNCONFIRMED**. Copy or adapt it only in an authorized project; empty fields are not defaults.

Required policy fields:

- `schemaVersion`: `1`; `projectId`: nonempty stable project label.
- `mainSession.modelEffortOwner`: `user`.
- `delegation.mechanism`: explicitly confirmed sessions or subagents; `delegation.models`: nonempty unique model IDs with effort policy.
- Each model's effort is an allowlist with nonempty unique `values`, or expressly approved `all_supported` with no values. The latter does not mean every runtime supports every effort.
- `budget.mode`: `unconfirmed`, `no_self_imposed_cap` or `capped`. `unconfirmed` blocks. `capped` requires positive finite token or three-letter-currency limits scoped to a task or increment. Limits do not authorize purchases or convert tokens to money.
- `permissions.smallDirectWork`: boolean; `permissions.externalActions`: `separate_authorization`.
- `confirmation.status`: `confirmed`, with timezone-bearing `at` and evidence naming the user's actual decision. A timestamp or user-looking string alone is not consent.

The schema intentionally has no hardcoded models, machine paths, glossary or global budget. Unknown fields or versions are rejected rather than silently changing meaning.

## Capability choice and adaptive allocation

For each new objective, record in its existing task record or packet whether the capability choice was explicit or `Auto`, the smallest selected skill/plugin set, observed versions/capabilities, conflicts checked and fit reason. `Auto` means the smallest appropriate set available now; it is not permission to install. Follow-ups and internal dispatch inherit the choice. Ask the user before dependent work when no valid choice exists or the objective materially conflicts with it; re-select only after a material objective, requirement, environment or availability change.

Use the operating modes in [SKILL.md](../SKILL.md) within existing authority. Model allowlists, effort limits and budget remain constraints on allocation, not targets to exhaust. `smallDirectWork` grants only its named scope; substantial solo work needs its own authority. A current solo instruction is task-scoped authority, not a rewrite of the delegation allowlist.

For an authorized worker selection:

1. Honor the user's explicit model and effort. If unavailable or inconsistent with confirmed limits, reconcile the conflict before dependent dispatch; do not silently substitute settings.
2. If effort is unspecified, assess complexity, uncertainty and the consequence of a wrong result. Use the observed runtime default as a starting point when it is permitted and no stronger task evidence exists. Straightforward, well-checked work can justify a lower supported effort; consequential uncertainty can justify a higher one. Maximum effort is not the default, and minimum effort is not a goal by itself.
3. If the runtime default is unknown or outside policy, select another allowed, available setting only when authority and task evidence justify it; otherwise ask a focused question. Do not assume the order of an allowlist ranks capability or cost. No universal model names or effort tiers are prescribed.
4. Record the selection reason in the current handoff. Before increasing effort or changing allocation, diagnose the evidence that the current approach is insufficient; elapsed time or a failed repair alone does not establish that. Keep [repair boundaries](handoffs.md#review-and-repair) in force.

Validate capability before relying on it; link capture source and exact policy/runtime bytes in the current handoff. If a runtime default informed selection, link its observed source separately; do not add fields to the checker runtime inventory. Reuse unchanged evidence. Record requested settings before dispatch and actual settings after observation. Missing mechanism, identity or capability blocks dependent dispatch, not separately authorized solo work. Do not change lead settings, buy/reset capacity or duplicate a dispatch. Changing an existing assignment requires the ownership checks in [handoffs](handoffs.md#ownership-and-integration).

## Read-only checker

Run with a policy path:

```sh
python scripts/check_policy.py --policy /project/docs/orchestration/policy.json
```

Before relying on a new or changed worker selection, supply the actual project identity and observed runtime. Reuse a valid result for an unchanged selection and unchanged evidence:

```sh
python scripts/check_policy.py --policy /project/docs/orchestration/policy.json --model model-a --effort high --runtime /temporary/runtime.json --project-id example-project
```

Runtime inventory is an observed, current tool/model snapshot obtained from the actual environment, for example:

```json
{"mechanisms":["sessions"],"models":[{"id":"model-a","efforts":["medium","high"]}]}
```

Keep capture time, source/version and observed capabilities in task evidence. A check date or version label alone is not freshness or authenticity proof. The checker validates configuration consistency; it does not prove sandbox enforcement, consent, freshness, role assignment, spend, or deployed capability.

Exit/status:

- `0`: `policy_valid`, or `selection_valid` when project, selection and supplied runtime match.
- `2`: `needs_input` — missing, malformed or unconfirmed policy; conflict; or incomplete selection arguments.
- `3`: `rejected` — wrong project or worker model/effort outside confirmed limits.
- `4`: `unavailable` — no valid runtime inventory, mechanism or selected capability.

The checker emits JSON and never writes project files, dispatches or changes settings. A successful result is not a dispatch permit.

## Change and recovery

Use the [startup paths](#start-with-existing-authority) to ask only action-relevant unresolved questions. Save actual confirmed answers with their decision reference before dependent execution; do not ask again when valid policy or current scoped authority already answers. If an explicit current instruction changes policy, reconcile before dispatch.

After a runtime error, stale snapshot or version mismatch, refresh the relevant actual capability evidence and revalidate. When the user has authorized alternative selection, an unavailable model may be replaced only by another allowed, available choice under the selection rule above. An explicit model/effort choice is not silently replaced. Keep requested and observed model/effort distinct. When identity or authority is uncertain, resolve it read-only and leave dependent work blocked.

Selection v2 includes hashes of the exact policy/runtime bytes and `notVerified` fields for approval authenticity, runtime freshness, remaining budget and task-creation authority. For capped policy, `budgetCheckRequired` remains true: missing capacity data is a blocker, not zero usage or spend permission. Historical `dispatch_allowed` outputs from the initial checker are not v2 evidence.
