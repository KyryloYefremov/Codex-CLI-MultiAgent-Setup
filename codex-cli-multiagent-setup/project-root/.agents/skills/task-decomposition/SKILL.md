---
name: task-decomposition
description: Decompose an accepted design into linked atomic tracker tasks with acceptance mappings and dependencies.
---

# Task decomposition

Use `$manage-github-issues`. Verify an accepted current design before writing tasks. Reuse the existing parent feature issue; Architect's design already lives there.

Create atomic tasks grouped by relevant area (Backend, Frontend, Database, DevOps, etc.). Add an area tracking issue only when it helps navigate multiple tasks. V1 has one feature branch/PR and sequential implementation; an atomic task is a cohesive implementation unit, not a mandatory separate PR.

Use [task-template.md](task-template.md). Each task links its parent, design result/revision, relevant design sections, stable acceptance IDs, dependencies, and inherited criticality. Describe the task-specific work without copying the complete design. Dependency cycles and missing acceptance coverage are BLOCKED.

Publish a complete manifest on the parent issue: task references grouped by area, dependencies, acceptance coverage, and READY/BLOCKED states. Check existing issues/comments before retrying writes.

Return the manifest/task references, status, and brief blockers. Do not pass full task descriptions through CTO chat, change the design, or close issues.
