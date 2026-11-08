---
name: review-implementation
description: Independently audit a candidate revision against its accepted design and publish a technical verdict.
---

# Review implementation

Use `$manage-github-issues` to read the parent issue, accepted design, complete task manifest, implementation notes, and verification evidence. Use [review-template.md](review-template.md).

Compare the recorded base SHA to the candidate head SHA, including committed changes. Require a clean candidate and consolidated PASS evidence for this exact head and design. A working-tree-only diff or earlier task test results are insufficient.

Check completeness against acceptance IDs, relevant regressions/security risks, missing requirements, unauthorized scope, and deviation rationale. Distinguish minor implementation choices from material scope/contract changes. Material changes require Architect revision and renewed design acceptance even when technically justified.

Publish your own review on the parent issue. PASS means the current accepted design is satisfied and required checks pass. FAIL means demonstrated defects, missing criteria, unauthorized scope, or failing required checks. BLOCKED means insufficient evidence or inability to review. Include base/head and exact design/result references in every verdict.

Return verdict and result links. Human acceptance is a later CTO-controlled gate. Do not modify code/tests, grant human approval, close issues, or merge.
