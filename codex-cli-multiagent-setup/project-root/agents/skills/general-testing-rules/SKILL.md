---
name: general-testing-rules
description: Design and execute adversarial tests against acceptance criteria and publish reproducible verification evidence.
---

# Testing and evidence

Independently read the task and accepted design through `$manage-github-issues`. Test observable acceptance criteria, relevant boundary/negative cases, state changes, and integration behavior. Use isolated tests with clear Arrange/Act/Assert structure. Select unit, integration, and regression coverage based on the change rather than adding every category mechanically.

Do not weaken criteria or fix production code. Coordinate exclusive test-file ownership with Developer. Tests must be included in the final candidate commit before final PASS is published. If you add tests, publish a test-preparation note and return NEEDS_CANDIDATE_COMMIT; Developer commits the tests and re-invokes you. This preparation handoff is not a failed/blocked verification or a correction cycle. Recheck the revision and clean worktree before and after execution; concurrent edits invalidate the run.

Publish the result yourself on the corresponding issue as a Markdown comment with these fields:

- Verdict: PASS, FAIL (demonstrated failure), or BLOCKED (verification unavailable).
- Feature/task and accepted design comment link and revision.
- Exact tested head SHA and applicable base SHA.
- Commands, environment/runtime, exit codes, passed/failed/skipped counts.
- Acceptance ID to test/check mapping, including unverified criteria.
- Concise failing traces and durable CI/log references when available.

A PASS requires actual execution and all required criteria verified. Keep large raw logs out of handoff messages. Return the evidence link, tested SHA, and short failure/blocker summary.

For consolidated feature verification, publish to the parent issue and cover the final candidate, not only the last atomic task. Any change to source/tests invalidates evidence for the previous SHA.
