# Neutral release comparison fixture

This fictional repair-desk project and rubric were frozen before either evaluation. Two fresh Luna Medium tasks received the same project, local-only authority, user outcome and prewritten clarification. The control ran first. Only the treatment received the release candidate's installable skill directory, without these evaluation files. The parent conversation and desired decisions were not supplied in either task prompt.

The supplied policy is synthetic confirmed trial authority, not a default policy for real users. The stakeholder note and stale report are test inputs, not real integrations or publication approval.

The model-visible inputs are in [fixture](fixture/README.md). The [protocol](protocol.json) contains the original request, fixed clarification, frozen manifest, rubric and limits. Do not provide this protocol or grader to an evaluation worker. Copies must be independent; do not expose the other run's artifacts. After a worker stops, run:

```sh
python -B evals/neutral/grade.py /path/to/worker/project
```

The grader covers the output rule, caller-supplied day, ordering and immutability. It does not grade tool authority, truthful reporting or context isolation; those require review of actual actions and evidence. Its failing baseline and passing positive control were checked before the pair. The frozen baseline itself is expected to fail the new product rule.

See the [release report](../report-v0.1.0.md) for observed results. One pair is descriptive evidence, not statistical superiority or demonstrated long-term savings. Platform instructions and globally available skills can influence both runs; declared directory boundaries are not a filesystem sandbox guarantee.
