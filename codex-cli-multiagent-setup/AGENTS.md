# Repository orientation

This repository maintains a reusable native Codex development setup to copy into new projects and customize in place. Treat the project-role prompts and skills in `project-root/` as templates while maintaining this repository; their CTO-only product restrictions do not prohibit editing the setup itself.

Read [README.md](README.md) for result ownership, agent boundaries, and criticality. Read [project-root/README.md](project-root/README.md) for installation and the Low/Medium/High walkthroughs.

## Design decisions

- GitHub Issues are the persistent record for requests, designs, tasks, implementation notes, testing, reviews, approvals, and delivery. Git stores code/tests.
- Use `$manage-github-issues` directly. Shared comment conventions and recovery guidance live in that skill; shipment stages and gates live in `$ship-feature`; role-specific deliverables live in the corresponding agent definitions and skills.
- End agent-authored GitHub issue/PR bodies, comments, and reviews with a Markdown footer: `---`, a blank line, then 🤖 **Agent:** `agent@<role>`. Separate the footer from the body with a blank line. CTO uses `agent@cto`; each specialist uses its configured role name. Use only your own signature and retain one footer when editing your own post.
- CTO creates the parent issue before Architect. Specialists publish their own Markdown results and return short status messages with links.
- Every shipment requires explicit Low/Medium/High criticality. Low/Medium design acceptance is CTO; High design acceptance is human. Final technical PASS is always required. Final acceptance is CTO for Low and human for Medium/High.
- Approval identifies its design comment/revision or final review/candidate commit. New design/code needs current acceptance and evidence. Material deviations return to design.
- CTO owns stage updates and issue closure after accepted merge delivery. Developer alone delegates Tester. CTO's implementation restriction applies only to the primary product-orchestration role.
- Use one feature branch/PR and sequential writers, with a three-thread cap. Low gets three automatic correction cycles total per feature execution; Medium/High failures await human direction. Record retry counts on the parent issue and preserve them after interruption.
- Configure project-specific repository/branch/test commands in project `AGENTS.md`. Keep ordinary Markdown records with links and relevant revisions; no separate workflow state/configuration or machine-record format is required.

Keep README tables, role prompts, templates, and skills consistent when behavior changes. The source directory names are packaging placeholders; installation maps to project-root `AGENTS.md`, `.codex/`, and `.agents/skills/`.

