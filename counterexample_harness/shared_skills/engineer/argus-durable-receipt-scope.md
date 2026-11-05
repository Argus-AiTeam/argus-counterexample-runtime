---
name: argus-durable-receipt-scope
description: Preserve the submission directory as well as the durable Argus task receipt.
---

Record the exact directory from which `subagent submit` was invoked alongside
`state`, `task_id`, `run_id`, and `check_with`. The command's `--cwd` is a
separate value and does not replace the submission directory.

Run the stored status or reply command from that submission directory.
In a verified same-task comparison, the campaign-root lookup reported
`task not found`, while the identical lookup from the submission directory
reported the existing running task and later its completed result.

A scope-mismatched lookup is not evidence that a worker was lost. Preserve
the error, correct the directory, and use the known handle; do not resubmit
the command or rediscover a new task. After confirming a healthy run,
continue independent work and collect its terminal result without foreground
polling.
