---
name: design-solution
description: Produce and revise a feature's technical design as a versioned result in its existing parent issue.
---

# Design solution

Architect reads the feature issue and uses `$manage-github-issues`. Ask clarification questions only when a material gap prevents a sound design; post questions to the parent issue and return their link as BLOCKED. Record answers there before proceeding.

Use [template.md](template.md). Keep the design concrete enough for implementation: interfaces, affected areas, data changes, error behavior, scope boundaries, acceptance IDs, and verification expectations. Prefer established project patterns and simple designs. Use Mermaid where it clarifies a flow.

Publish the design yourself as a new Markdown parent-issue comment with a numbered revision (D1, D2, etc.). Keep prior versions; corrections create a superseding result rather than silently editing an accepted design. Return the result reference and revision, not the design body.

Do not self-approve. Low/Medium require a recorded CTO acceptance; High requires a human acceptance for this exact design comment and revision. A material deviation requires another revision and renewed acceptance. Do not create local design documents as the workflow record.
