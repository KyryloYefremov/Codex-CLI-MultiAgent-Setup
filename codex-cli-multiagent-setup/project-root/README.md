# Project setup and criticality walkthroughs

Use native Codex agents and existing procedural skills to ship features. GitHub Issues hold requests, designs, task results, testing, reviews, approvals, and progress. Git stores source code and tests.

## Install into a project

Merge these templates with existing project conventions rather than blindly overwriting them.

| Source in this package | Destination in the target project |
|---|---|
| `codex-project/AGENTS.md` | Root `AGENTS.md` |
| `codex-project/config.toml` | `.codex/config.toml` |
| `codex-project/agents/*.toml` | `.codex/agents/*.toml` |
| `agents/skills/*` | `.agents/skills/*` |
| `codex-project/backend/AGENTS.md` | Optional `backend/AGENTS.md` customization |
| `codex-project/tests/AGENTS.md` | Optional `tests/AGENTS.md` customization |

Keep the project's README and incorporate or link this guide as needed. Global defaults in `../codex-global/AGENTS.md` are optional personal guidance. Legacy hooks remain excluded from installation and disabled in the baseline while enforcement is discussed.

## Project customization

Record the GitHub repository, intended integration branch (default `main`), test/build commands, and relevant stack skills in the target project's `AGENTS.md`. Confirm the GitHub destination from its Git origin and `gh repo view`; ask when ambiguous. Check CLI authentication and access before live writes.

Confirm native role/skill discovery, model access, and Developer-to-Tester delegation in the installed runtime. Models and execution permissions inherit the parent session. Use one feature branch/PR and sequential writers. Observed authoring CLI is 0.162.1; live compatibility still needs checking in the target project.

## How agents document shipment

Every role uses `$manage-github-issues` directly. CTO uses `$ship-feature` for stage order and approvals. Architect, Task Manager, Tester, and Reviewer use their corresponding skills/templates for their outputs.

- The parent issue holds the request, criticality, current stage, design comments, child-task list, final verification/review, approvals, and delivery.
- Child issues hold atomic work, dependencies, acceptance criteria, implementation notes, and test results.
- Comments use readable Markdown: a descriptive heading, relevant issue/design links, design revision, applicable commit SHA, result/evidence, and next action.
- Designs use numbered revisions such as D1/D2, with superseded versions linked. Approvals link the exact design or final review/candidate.
- After interruption, read the issues/comments and continue from current evidence. Check for existing publications before retrying an ambiguous write.

There is no separate workflow configuration, state database, JSON envelope, hashing requirement, or Python transition checker. CTO follows the instructions and checks stage prerequisites from the issue records.

## Shipment stages

`intake → designing → awaiting-design-acceptance → tasking → implementing-testing → final-review → awaiting-final-acceptance → ready-to-merge → done`

CTO records the current stage on the parent issue. Stages describe progress; they are not an automatically enforced state machine. Missing criteria, required approval, tools, or access means BLOCKED with a reason and next action. Material design changes return to design acceptance; new candidate code needs renewed test/review/final acceptance evidence.

## Low criticality example

Request: `Criticality: Low — add a display preference using the existing settings pattern.`

1. CTO creates the parent issue and records Low.
2. Architect posts design D1. CTO comments `ACCEPT design D1` with its comment link.
3. Task Manager creates linked tasks. Developer implements each ready task and delegates Tester.
4. Tester posts results on each task and verifies the final candidate on the parent. Reviewer posts PASS for that candidate.
5. CTO records final ACCEPT, verifies actual merge into the intended branch, records delivery, and closes issues.

No human approval wait is required. Test/review FAIL allows up to three automatic correction cycles in total per feature execution. CTO records each cycle before retrying; exhaustion becomes BLOCKED and is escalated. A new commit requires refreshed evidence.

## Medium criticality example

Request: `Criticality: Medium — add a backward-compatible API endpoint.`

1. CTO creates the feature; Architect posts D1; CTO records design acceptance.
2. Task Manager creates tasks; Developer/Tester implement and verify; Reviewer posts final PASS on the parent.
3. CTO remains at `awaiting-final-acceptance` until an explicit human accepts the linked review and candidate commit.
4. CTO documents that decision, verifies accepted merge delivery, and closes the issues.

Example human decision: `ACCEPT final review <comment link> for commit <SHA>.` If the human answers in chat, CTO posts that decision to the issue as relayed from the conversation. FAIL requires human fix/revise/cancel direction; a direction to fix does not waive final acceptance.

## High criticality example

Request: `Criticality: High — change payment calculations.`

1. CTO creates the feature with High before delegating.
2. Architect resolves material questions and posts D1. CTO waits at `awaiting-design-acceptance` for human acceptance of this completed design.
3. After the decision is recorded, Task Manager creates tasks and Developer/Tester execute them.
4. Tester verifies the final candidate and Reviewer posts PASS. CTO waits again for human acceptance of that review/candidate.
5. CTO verifies actual merge delivery, records it, and closes issues.

Example design decision: `ACCEPT design D1: <design comment link>.` Approval to start Architect is not design acceptance. A material D2 revision requires renewed human acceptance. Final approval for one commit cannot be reused for changed code.

## Pending decisions

Agent signatures, logical assignment, and lifecycle hook enforcement remain under discussion. A role label does not authenticate a human. Require explicit human decisions, identify their source honestly, and clarify uncertain approval. These walkthroughs explain the intended behavior; they are not claims of completed live shipments or automatic enforcement.
