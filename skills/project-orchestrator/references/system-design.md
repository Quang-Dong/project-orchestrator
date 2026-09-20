# System design for a bounded product outcome

## When to apply and what to read

Use this reference when a change crosses responsibility or trust boundaries, changes data ownership/contracts, introduces difficult recovery, or has a material quality or scaling constraint. A local reversible fix that preserves those boundaries normally needs only a short rationale and affected checks. Do not require a system redesign or separate architecture document for every task.

Start with the [product flow and business rules](product-delivery.md#resolve-requirements-and-business-rules), existing implementation/contracts, applicable quality conditions and observed constraints. Separate measured load and concrete expected changes from guesses. Missing baselines stay unknown under [evidence rules](evidence-and-challenge.md#choose-evidence-by-risk); do not invent capacity or availability targets to justify a design.

## Decide boundaries and tradeoffs

Choose the smallest understandable design that meets the required behavior and quality. In the existing task/design record, make the relevant relationships explicit:

- **Responsibilities and dependencies:** where each business rule belongs, who calls whom, and which module may depend on which. Keep related rules together and avoid cycles or a new layer that only forwards calls.
- **Data and state ownership:** the authoritative state, who may mutate it, invariants, and how derived/cached copies stay consistent where present. Preserve existing storage/external adapters when they are the established boundary; abstraction needs a concrete replacement or isolation benefit.
- **Interfaces and trust:** inputs, outputs, error semantics, permissions and validation at actual trust boundaries. Describe affected callers and compatibility obligations without prescribing a new public API.
- **Failure and recovery:** how refusal, partial success, timeout or interruption propagates, what state remains, and who can retry or restore it safely. Consider duplicate work or concurrency when the real flow permits them; do not add a generic distributed-systems mechanism without that need.

Distinguish three reasons to scale: **functionality** (a known new rule or flow), **load** (measured or required volume/latency/resource limits), and **teams** (actual ownership and change coordination). One does not imply the others. More users do not alone require microservices, and a possible future team does not alone require a service boundary.

Compare alternatives only when a real tradeoff affects correctness, clarity, change scope, coupling, security, recovery or lifecycle cost. Include retaining the current design. State why the selected option meets the mandatory quality conditions, what cost it introduces and which evidence would warrant revisiting it. Do not trade away those conditions for speed. Avoid speculative queues, frameworks, services and configurable abstractions; a simpler option must still satisfy the contract.

## Walk a plausible change and a material failure

Before broad implementation, trace the proposed flow across its owners and interfaces. Try one grounded change that matters to this task: name the modules/data/callers it would affect and how a future maintainer would verify it. Then trace a consequential failure: where it is detected, what the user/caller sees, how invariants survive and what recovery is possible. Scale the walkthrough to the actual risk, not a catalogue of hypothetical failures.

Use a short explanation, sketch or existing design note as the output: chosen boundaries, material tradeoff, affected scope, unresolved assumption and how to check it. A risky assumption needs an observable check such as a contract probe, real caller slice, representative measurement or recovery rehearsal. Follow [implementation](implementation-and-diagnosis.md#implement-a-complete-slice) and [evidence](evidence-and-challenge.md#choose-evidence-by-risk) for execution and proof; a diagram is not runtime evidence.

If a boundary cannot preserve a required rule or has no viable recovery for a required scenario, revise it or keep that acceptance condition open. Use [product operations](product-operations.md#handle-data-and-recovery) for migration and release recovery. Design guidance does not authorize contract expansion, production mutation or bypassing required independent review.
