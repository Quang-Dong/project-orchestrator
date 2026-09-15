# Product delivery from idea to outcome

Use this reference when a request changes a user-facing flow, product behavior, data/state, acceptance, or an operational outcome. Keep it proportional: a small defect may need a short outcome statement and one acceptance check; a larger change needs each section below. The existing requirement registry remains authoritative. If no registry exists, create one minimal authoritative outcome/spec record in the project's normal documentation location, name its owner and acceptance, and do not create a second backlog. This is a delivery frame, not a competing specification or backlog.

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

## Choose sufficient architecture

Prefer the smallest design that satisfies the current flow and preserves a clear boundary for likely change. Name the material alternative only when it changes risk, cost, quality, reversibility or ownership. For each meaningful choice, record a falsifiable hypothesis:

`If [bounded change], then [quality or cost signal] will change by [measurable direction/threshold] for [scope], while [quality to preserve] does not regress.`

Do not add a framework, service, schema, queue, persistence layer or coordination role without a demonstrated need in the specified flow. Keep product rules in their owner; use replaceable adapters for storage or external systems when that is the existing boundary.

## Sequence complete increments

Each increment has one owner, a bounded write scope, dependencies, a definition of done and a next handoff. Prefer an end-to-end slice that a user can exercise over disconnected layers. Parallelize only independent work with disjoint writes; reconcile any ambiguous dispatch before retrying. After a change, re-run affected checks and invalidate evidence that was tied to an older revision.

## Release and lifecycle, only when applicable

For a change that can reach users or affect operations, identify the authorized release gate, rollback/recovery action, monitoring signal, support owner and retirement or migration obligation. If none applies, say so. Release, production mutation, external communication, spending and installation updates require their own authority; a product design or worker handoff cannot grant it.
