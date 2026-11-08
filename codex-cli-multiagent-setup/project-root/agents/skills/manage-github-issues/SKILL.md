---
name: manage-github-issues
description: Read and update GitHub issues to document feature requests, designs, tasks, implementation, verification, reviews, and approvals.
---

# Document feature shipment in GitHub Issues

Use GitHub Issues as the persistent record. Read the project's `AGENTS.md` for repository and integration-branch settings. Resolve an unambiguous repository from Git origin and `gh repo view --json nameWithOwner,url` if needed; ask if the destination is uncertain. Pass the resolved `--repo owner/repo` on every issue/PR operation. Verify authentication with `gh auth status`; never print tokens.

## What goes where

- CTO creates the parent feature issue before Architect starts, with the user request, explicit Low/Medium/High criticality, current stage, and relevant links.
- Architect posts clarification questions and versioned designs (D1, D2, etc.) as parent-issue comments. Keep prior versions and link the new version instead of silently changing an accepted design.
- Task Manager creates linked child issues from the accepted design, with area, dependencies, inherited criticality, and acceptance criteria. Post the task list on the parent.
- Developer posts implementation/deviation notes on the child issue, linking the design, PR, and base/head commits.
- Tester posts test results on the child issue; post consolidated final-candidate verification on the parent.
- Reviewer posts the final review on the parent. CTO records acceptance decisions, stage changes, retry counts, and merged delivery there.
- Git stores source code/tests. Local scratch/body files are disposable transport, not persistent plans or results.

## Simple comment format

Use readable Markdown and the corresponding design/task/review template. Give each comment a descriptive heading such as `Design D1 — Architect`, `Verification — Tester`, or `Design acceptance — CTO`.

Include the relevant issue/design/result links, design revision, and exact code SHA for implementation/testing/review. State PASS/FAIL/BLOCKED when applicable, then the result, evidence, or required next action. No JSON envelope, content hashes, or separate state file is required. Role headings describe responsibility; use the Markdown signature footer below.

An acceptance comment must say ACCEPT or REJECT and link the specific design comment/revision, or final review and candidate SHA. High design acceptance and Medium/High final acceptance require an explicit human decision. If the human responds in chat, CTO records the decision as relayed from that conversation and links the subject; do not present it as a direct human-authored GitHub comment. Never infer approval from silence or a role label. If the source or meaning is uncertain, ask for clarification.

A changed design needs renewed acceptance; a changed candidate needs current verification/review/final acceptance. Human acknowledgement of FAIL does not turn it into technical PASS. The `$ship-feature` skill owns the stage order and criticality gates; each specialist's skill owns its detailed deliverable.

## Agent signatures

End every GitHub issue/PR body, comment, or review you author with the Markdown footer below, separated from the body by a blank line. Use lowercase configured role names:

| Role | Signature |
|---|---|
| CTO | agent@cto |
| Architect | agent@architect |
| Task Manager | agent@task-manager |
| Developer | agent@developer |
| Tester | agent@tester |
| Reviewer | agent@reviewer |

Example comment:

```markdown
Verification: PASS
Tested commit: <SHA>
Results: 12 tests passed.

---

🤖 **Agent:** `agent@tester`
```

Check the body before posting. When editing your own post, keep exactly one footer for your role. Preserve quoted material and other authors' posts; do not relabel them. A CTO comment relaying a human approval still ends with `agent@cto` and states the human decision's source in its body. Never use another role's signature or manufacture a human signature. Humans do not need a new signing step for this convention.

## GitHub CLI operations

Prepare multiline Markdown in a temporary file and pass it with `--body-file`.

```bash
# Read the issue and its results.
gh issue view ISSUE --repo OWNER/REPO --json number,url,title,body,state,comments
# Read all comment pages when necessary.
gh api --paginate repos/OWNER/REPO/issues/NUMBER/comments
# Create the parent feature or a child task.
gh issue create --repo OWNER/REPO --title TITLE --body-file /tmp/issue-body.md
# Publish a design, result, approval, or stage update.
gh issue comment ISSUE --repo OWNER/REPO --body-file /tmp/result-body.md
# Refresh the parent's concise status/link index.
gh issue edit ISSUE --repo OWNER/REPO --body-file /tmp/feature-index.md
# Read actual merge evidence.
gh pr view PR --repo OWNER/REPO --json url,state,baseRefName,headRefOid,mergedAt,mergeCommit
# CTO closes issues after accepted merge delivery.
gh issue close ISSUE --repo OWNER/REPO --reason completed
```

Use safe quoting/argument arrays; never interpolate issue content into shell code. Use existing project labels only. Preserve actual author identity and timestamps when reading decisions. Shared GitHub credentials do not make role signatures proof of human authorship.

## Recovery and completion

After interruption, read the parent and linked tasks/results to find the latest accepted design, candidate, verification, review, approvals, stage, and retry count. After an ambiguous write/timeout, check for an existing matching issue/comment before retrying. Reuse a completed publication; ask if duplicate/conflicting records cannot be reconciled.

Missing criticality, required approval, evidence, auth, tools, or readable GitHub state means BLOCKED with a reason and next action. Do not fall back to a local task store. CTO alone records delivery and closes issues after the reviewed/accepted head is actually merged into the intended branch. Avoid PR closing keywords that could close issues before this check.
