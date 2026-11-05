---
name: replan-revision-conflict-triage
description: Diagnose Manager-approved replans that stop as planner errors by correlating settlement, backlog status, and plan-revision CAS evidence.
---

# Replan revision conflict triage

Use this procedure when a reviewed mission requests replanning and the Manager
chooses replacement, but the campaign stops with `planner_error`.

1. Require a `replan_requested` review or mission event, a
   `life.manager.plan_challenge.decided` event with `manager_action=replace`,
   and the subsequent planning outcome. Do not infer a framework defect from a
   scientific strategy failure alone.
2. Inspect the challenged backlog row's exact `plan_id`, `plan_version`, and
   post-settlement `status`, then inspect the matching
   `life.plan.revision.rejected` event.
3. Trace only the settlement transition, revision-intake eligibility filter,
   and atomic revision comparison. A defect is established when settlement
   deterministically makes the just-approved trigger ineligible for the
   immediately following compare-and-swap.
4. Bound any repair to preserving both invariants: a completed
   forward-progress replan trigger is not redispatched, and the accepted
   replacement can atomically supersede that trigger plus every remaining
   active node. Stale or replayed revisions must still fail.
5. Require one regression that runs the real settlement-to-revision path and
   observes a committed replacement, together with the existing no-redispatch
   test.
6. Keep framework and research verdicts separate. A completed review of
   replacement-protocol tests establishes only that replanning can be
   committed safely. Advance a research stage only from campaign-local
   artifacts and a reviewer verdict against that stage's checklist. If the
   campaign reviewer still requests replanning and the target proposition is
   open, hold the current research stage even after the framework repair
   passes.
7. Do not equate a maintenance mission's Reviewer `done` verdict with an
   applied repair. Inspect the subsequent `manager.self_maintenance.*`
   settlement event. A `repair_failed` event means the live framework remains
   unchanged even when the implementation and tests passed in the private
   worktree.
8. If settlement rejects an otherwise reviewed repair for changing a path
   outside Manager authorization, keep the path guard intact. Confirm the
   extra path is causally required in the live source, then issue a bounded
   repair with that exact path added; do not authorize the whole framework or
   unrelated generated changes.
