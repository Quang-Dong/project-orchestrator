# Authority, capability and allocation

Use this reference when choosing how to execute substantive work, authority is unclear, a capability choice matters, or a worker selection needs checking. Inputs are current user instructions, applicable project limits and actual runtime observations. Decide which action is permitted and supported; continue once its relevant constraints are resolved. A clear authorized solo edit does not need a delegation inventory or a policy file.

## Start with existing authority

The user owns main-session model/effort and scoped permissions. Read current instructions and relevant confirmed limits first. An absent policy does not erase direct user authority or manufacture delegation, spending or external-action permission. A skill, agent message, successful checker or platform capability cannot grant authority.

| Situation | Action |
| --- | --- |
| Clear small authorized task | Perform the bounded change and relevant check; no extra permission question or process files. |
| Substantial task with a current checkpoint | Read its requirement, execution choice, owner, revision and decisive evidence; inherit applicable choices under [execution mode](#execution-mode-and-lead-responsibility). |
| Authorized solo work without worker configuration | Continue solo within scope and applicable limits; do not invent delegation settings or create policy for this purpose. |
| Missing/conflicting authority, material requirement or applicable budget | Group the unresolved decisions; stop dependent actions and continue separately authorized work. |
| A policy file uses an unsupported schema | Preserve and read its confirmed limits; do not reinterpret rejection as permission. The new checker rejects it. Obtain an authorized replacement before relying on it for worker selection; no silent conversion. |

External actions follow their actual scoped authorization. A valid existing authorization does not require repeated confirmation; unrelated publication, release, deployment, installation, purchases or transmission is not implied by task completion. Native tool permissions remain enforced separately. An agent cannot approve a prompt on the user's behalf or transfer a denied action to another session to evade that boundary.

## Execution mode and lead responsibility

For substantive work, default to subagents once task authority, delegation configuration, applicable budget and actual runtime support are sufficient. This is an instruction to coordinate within those limits, not consent to spending, policy changes or additional external actions. Do not ask for an execution-mode choice at every new objective when this default is usable. Substantive work involves consequential product/design/integration/acceptance decisions or sustained implementation; a short factual answer or a clear bounded low-risk correction stays direct.

| Current choice or condition | Next action |
| --- | --- |
| No applicable choice; substantive work; prerequisites satisfied | Delegate a bounded output to subagents and retain overall direction and acceptance. One worker is enough when the work is coupled; concurrency is optional. |
| User explicitly chose solo, a mechanism/worker, or discretion over execution mode | Apply that instruction within its scope. Choosing the skill does not erase a no-subagent restriction or an existing authorized session workflow. |
| A follow-up, compaction or resume continues the same scope | Reuse the choice, rationale, authority and limits in the current conversation/checkpoint; do not ask again merely because context was shortened. |
| An independent session or doing all implementation in the main session would be preferable | Explain the concrete reason and ask for the change unless an applicable user choice already covers it. Do not silently replace the default. |
| Required authority, budget, supported configuration or runtime is missing | Group the missing decisions in one focused question. Continue only bounded read-only discovery and independently authorized work while waiting, not the whole implementation by default. Silence is not a choice. |
| A small clear authorized correction | Edit and check directly; no worker, execution-mode question or new process record. |

Ask again only when a material change is outside the choice's scope or makes it unusable. The question should name feasible alternatives and why one fits; do not present unsupported models or mechanisms as ready to run. For independent sessions, distinguish using an existing task from creating a new user-owned task. Obtain applicable authority and identify the intended task before sending work; inspect its current owner, active work and scope conflicts. Do not repurpose another task or create a standalone task merely to obtain a different model. Native restrictions on task creation and delegation still apply.

The main session owns product strategy, user communication, decomposition, shared decisions, integration and acceptance. It may inspect, plan, check and perform scoped integration itself; these activities are not permission to absorb all delegated implementation. Assign coupled execution to one worker when appropriate. Use [handoff ownership](handoffs.md#ownership-and-integration) for actual writers, transfer and evidence. Keep the execution choice in the existing conversation/checkpoint; no new schema, mandatory form or measurement stream.

## Capability choice and adaptive allocation

Select the smallest useful set of available skills/plugins within current authority. Honor explicit user choices and exclusions; otherwise choose by the unresolved decision, task/version fit and actual exposed tools. Do not ask for an explicit/Auto choice on every objective. Capability selection is separate from a platform permission mode named `auto`; it does not authorize installation or weaker permissions.

Inspect the relevant guidance before relying on it, but omit instructions that do not apply to the task/runtime. Use current project or primary-source evidence where version mismatch matters. Record a selection reason only when it affects a material decision or handoff. Revisit after a relevant objective, environment or capability change; unchanged evidence can be reused. Ask only when missing authority, a material conflict or an unavailable user-required capability changes the next action.

For authorized worker selection:

1. Use **`gpt-6-luna` as the sole worker model** under this selection. Require that exact model in the confirmed allowlist and actual exposed inventory; another Luna generation is not equivalent. Do not select GPT-5.6 Luna, Spark, Sol or another model as a fallback. This instruction does not amend a project's allowlist or grant runtime access.
2. Keep main-session model/effort user-controlled and preserve explicit worker effort. A clear user instruction can change the worker-model choice later; neither an allowlist containing other models nor task difficulty is such an instruction. If the required model, specified effort, authority or budget is unavailable or conflicts with confirmed limits, group the missing decisions and keep dependent dispatch pending. Do not routinely propose a stronger model or silently take all implementation into the main session.
3. Model choice is separate from effort. Start effort from the selected model's observed runtime default when allowed and no stronger task evidence exists. Otherwise choose a supported, permitted level only when allocation authority and task evidence support it; identify the missing decision if they do not. Honor explicit effort; neither High nor maximum effort is mandatory.
4. Check context inheritance and model/effort override restrictions before spawning. A full-history fork may enforce parent settings. Use a supported context mode and provide the required packet when a permitted override needs it; do not silently inherit the main model, drop required context or equate copied author history with independent review.
5. Diagnose inadequate progress before increasing effort, changing ownership or allocating another session. Check the requirement, available context, task boundary and rejected hypotheses; difficulty or a failed repair is not permission to change model. Use the [worker-to-main decision loop](handoffs.md#questions-changes-and-results) for unresolved decisions and keep the [repair boundary](handoffs.md#review-and-repair).

Before a new or changed selection, observe only the required mechanism/model/effort and validate the configuration. Link capture source, time/version and the exact policy/runtime bytes in the current packet. Record requested settings before dispatch and observed settings after execution starts. The checker cannot prove freshness, remaining budget or actual task-creation authority. A capped budget with unavailable capacity data keeps dependent dispatch blocked. Reuse a valid result only while its constraints and evidence still apply.

## Policy v2

Use an existing project policy location, conventionally `docs/orchestration/policy.json`, only when durable configuration is needed. Do not create a second live policy, backlog or capability registry. The [template](../assets/policy.template.json) is deliberately unconfirmed; filling it out is not user consent.

All five fields are required; unknown fields and unsupported versions are rejected:

| Field | Contract |
| --- | --- |
| `schemaVersion` | Integer `2`. Policy v1 is unsupported. |
| `projectId` | Nonempty stable project label. |
| `delegation` | `null`, or `{mechanism, models}` with `mechanism` equal to `sessions` or `subagents` and a nonempty unique model list. Null supplies no worker selection. |
| `budget` | `null` only when delegation is null, or `{mode, limits}` with a confirmed stance. A solo policy may still retain explicit limits. |
| `confirmation` | `{status: "confirmed", at, evidence}` with timezone-bearing timestamp and a nonempty reference to the actual user decision. Authenticity is not mechanically proved. |

Each model has `id` and `effort`: either `{mode: "allowlist", values: [...]}` with nonempty unique settings, or `{mode: "all_supported"}`. The latter still requires observed runtime support. The schema and checker impose no hardcoded model names or effort tiers; the worker-model selection above does not change this contract.

Budget `no_self_imposed_cap` requires empty limits; `capped` requires at least one positive finite limit `{metric, amount, unit, scope}`. Metric is `tokens` with integral amount/unit `token`, or `money` with a three-uppercase-letter currency. Scope is `task` or `increment`; duplicate metric/unit/scope limits are invalid. Limits constrain use; neither null nor a confirmed stance grants spending or resets capacity.

There are no `mainSession` or `permissions` fields and no `smallDirectWork` switch. Main-session choices remain user-owned; actual task scope and native permissions govern actions. Unsupported older fields are errors, not silently ignored defaults. Replace a project's policy only at an authorized adoption boundary; historical files remain unchanged.

## Read-only checker

Configuration check, without requiring runtime data:

```sh
python -B scripts/check_policy.py --policy /project/docs/orchestration/policy.json
```

Worker selection check requires all of model, effort, runtime and expected project:

```sh
python -B scripts/check_policy.py --policy /project/docs/orchestration/policy.json --project-id example-project --model model-a --effort high --runtime /temporary/runtime.json
```

The runtime input describes an actual observed inventory, for example `{"mechanisms":["sessions"],"models":[{"id":"model-a","efforts":["medium","high"]}]}`. Keep provenance in the existing packet. No checker file is needed for separately authorized solo work.

Exit `0`: `policy_valid` or `selection_valid`; `2`: `needs_input` for malformed, unconfirmed or unsupported input; `3`: `rejected` for project mismatch, no configured delegation or disallowed selection; `4`: `unavailable` for missing/invalid runtime or unsupported selection. `--help` displays usage. Operational errors return JSON, including input hashes when bytes were read, output `schemaVersion: 2`, `notVerified` and `budgetCheckRequired` (null when no budget stance could be assessed).

A valid result checks supplied configuration only. It never writes files, dispatches, authenticates consent or enforces budget. An unsupported policy does not cancel its user's instructions. No migration, compatibility shim or automatic installed-project edit is provided.

## Change and recovery

On actual requirement or authority changes, reconcile affected records and dependent assignments under [handoffs](handoffs.md). On runtime error or stale capability evidence, refresh only the relevant observation and revalidate. A user instruction changing the worker-model choice must be explicit and remain within confirmed limits; an available alternative or old broader allowlist is not permission to replace the selected model. Resolve identity or side-effect uncertainty before retrying.
