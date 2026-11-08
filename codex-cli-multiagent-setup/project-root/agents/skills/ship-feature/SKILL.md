---
name: ship-feature
description: Coordinate feature shipment through GitHub-documented design, tasks, implementation, testing, review, approval, and merge.
---

# Feature shipment

This procedure applies to CTO. Use `$manage-github-issues` directly for persistent records. Specialist roles own their detailed deliverables. Stages are simple status entries on the parent issue; CTO checks their prerequisites from linked comments.

1. **Intake.** Require explicit Low/Medium/High criticality. Confirm the GitHub destination, integration branch, available roles/tools, and test commands. Create or recover the parent feature issue before Architect, recording the request, criticality, and `intake` stage.
2. **Designing.** Set `designing` and invoke Architect with the parent issue. Architect posts questions and design D1 (or the next revision). Relay material questions and record answers; do not advance with unresolved requirements.
3. **Design acceptance.** Set `awaiting-design-acceptance`. Low/Medium: CTO posts ACCEPT for the exact design comment/revision. High: wait for explicit human acceptance, then record it on the issue. A human chat response may be relayed by CTO with its source stated. REJECT returns to design. Starting Architect is not design approval.
4. **Tasking.** After acceptance, set `tasking` and invoke Task Manager. It creates linked atomic tasks and a parent task list, with inherited criticality, acceptance IDs, areas, and dependencies. Only ready tasks are dispatched.
5. **Implementing/testing.** Set `implementing-testing`. Use one branch/PR and sequential Developers. Developer alone invokes Tester and pauses edits while Tester writes tests. Tester returns NEEDS_CANDIDATE_COMMIT when new tests need committing; Developer commits and re-invokes Tester. Each role posts its own implementation/testing notes. Keep issues open.
6. **Final verification.** Once tasks are implemented, Developer prepares the final clean candidate including tests and invokes Tester for consolidated feature verification. Tester posts commands, results, acceptance mapping, and the exact tested head on the parent. Earlier task test results do not establish final-candidate PASS.
7. **Final review.** With all tasks implemented and current consolidated Tester PASS, set `final-review`. Reviewer compares the recorded base/head against the accepted design and posts PASS/FAIL/BLOCKED on the parent.
8. **Final acceptance.** After Reviewer PASS, set `awaiting-final-acceptance`. Low: CTO posts ACCEPT. Medium/High: wait for an explicit human decision and record it. The acceptance links the review, design, and candidate head. Acknowledgement of FAIL cannot authorize shipment.
9. **Ready to merge.** Check that the latest design/candidate still match verification, review, and acceptance. Set `ready-to-merge`. Merge only under the project's integration authorization. If the head changes, refresh testing/review/acceptance.
10. **Done.** Read actual PR merge evidence: reviewed head, intended target branch, merged status, and resulting merge commit. Record delivery and set `done`; CTO closes the child/parent issues.

## Correction, blocked work, and recovery

- Low: record each automatic correction on the parent before dispatch, up to three cycles per feature execution across test and review failures. Fix, rerun tests, and review again. On exhaustion, record BLOCKED and escalate.
- Medium/High: record FAIL and await human fix/revise/cancel direction. Direction to fix does not waive the later acceptance gates.
- Material design deviations return to Architect, renewed design acceptance, and affected task updates. Reviewer can accept minor implementation choices, not independently change scope/contracts.
- Record BLOCKED/CANCELLED with the reason, previous stage, and next action. Recover to the earliest stage whose prerequisites need renewal. Auth/tool/environment errors are BLOCKED, not product FAIL.
- After interruption, read the existing parent/tasks/comments, preserve retry counts, and continue from current evidence. Check ambiguous writes before retrying. Release completed agent threads.

## Approval rules

| Gate | Low | Medium | High |
|---|---|---|---|
| Request | Explicit criticality | Explicit criticality | Explicit criticality |
| Completed design | CTO ACCEPT | CTO ACCEPT | Human ACCEPT |
| Final technical review | Reviewer PASS | Reviewer PASS | Reviewer PASS |
| Final acceptance | CTO ACCEPT | Human ACCEPT | Human ACCEPT |

Approval comments identify their subject and decision. Never infer approval from silence or a role label. Legacy hooks and automatic signature enforcement remain deferred; CTO follows the recorded decisions directly.
