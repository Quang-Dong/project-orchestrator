# Product delivery from idea to outcome

Use this reference when a request changes a user-facing flow, product behavior, data/state, acceptance, or an operational outcome. Keep it proportional: a small defect may need a short outcome statement and one acceptance check; a larger change selects the sections that can affect its decisions. The existing requirement registry remains authoritative. If no registry exists, create one minimal authoritative outcome/spec record in the project's normal documentation location, name its owner and acceptance, and do not create a second backlog. This is a delivery frame, not a competing specification or backlog.

Apply the priorities and invariants in [SKILL.md](../SKILL.md). This reference expands product decisions only; it does not require extra roles or records for every behavior change.

## Discover the value

State, in plain language:

- **Users:** who acts, who benefits, and who is affected.
- **Problem:** the observed pain or opportunity, with the evidence and date.
- **Value:** the useful outcome and how a user or operator will recognize it.
- **Assumptions:** beliefs that could change the solution, separated from facts.

Ask about missing material authority, requirements or irreversible tradeoffs before implementation. Do not invent a persona, metric, customer need or production constraint to make a vague idea look complete. Simulated users, fixtures and role-play can test a flow or grader; they are not evidence of real demand validation. Treat interviews, observed usage or an authorized experiment as separate evidence, with its population and limits stated.

## Specify the smallest complete increment

Describe observable behavior rather than a component list:

1. Primary flow and important alternate/error flows.
2. Data, state transitions, invariants and ownership of each state.
3. Explicit exclusions, non-goals and deferred behavior.
4. Acceptance checks that can be run against the real artifact or a clearly labelled local fixture.

Acceptance must cover the negative path when failure, refusal, missing data or stale state matters. A passing mock, prototype or unit test is evidence only for that layer; it does not prove integration, deployment or real-user value.

Keep the product contract, coordination checkpoint and product artifact/proof distinct. The contract owns outcome, exclusions and acceptance; the checkpoint owns current owner, attempt, source revision, write scope and recovery; the artifact/proof owns product state and caller checks. Chat history is context, not product state or acceptance authority. Do not create a competing schema or registry to hold this boundary.

## Choose sufficient architecture

Prefer the smallest design that satisfies the current flow and preserves a clear boundary for likely change, after the outcome and quality are protected. Name the material alternative only when it changes risk, cost, quality, reversibility or ownership. Use speed or extra resources only when they preserve the higher priorities. For a risky design assumption, identify an observable check. A measured experiment may express it as:

`If [bounded change], then [quality or cost signal] will change by [measurable direction/threshold] for [scope], while [quality to preserve] does not regress.`

Do not add a framework, service, schema, queue, persistence layer or coordination role without a demonstrated need in the specified flow. Keep product rules in their owner; use replaceable adapters for storage or external systems when that is the existing boundary.

## Sequence complete increments

Give each increment one owner, a bounded scope and observable acceptance. Keep coupled work with an end-to-end owner; add an integrator only when distinct outputs need it. Before broad implementation or a full matrix, exercise the smallest real caller path across the affected boundaries, including a material failure path. If it fails, diagnose before expanding. Parallelize only independent work with disjoint writes and a clear integration path. Use [handoffs](handoffs.md) for ownership and authorized takeover; individual passes do not prove the combined result.

## Release and lifecycle, only when applicable

For a change that can reach users or affect operations, identify the authorized release gate, rollback/recovery action, monitoring signal, support owner and retirement or migration obligation. If none applies, say so. Release, production mutation, external communication, spending and installation updates require their own authority; a product design or worker handoff cannot grant it.
