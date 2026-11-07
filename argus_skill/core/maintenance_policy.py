"""Operator switch for in-campaign Argus framework maintenance.

A campaign may route a task to ``argus_maintenance``: the Engineer then edits
the running Argus source in a worktree, the Reviewer accepts it, and the change
waits for operator approval before deployment. In an attended session that is
self-repair. In an unattended fleet it is a trap: the approval never comes, the
Planner then waits on the undeployed patch, and the campaign stops doing the
work it was launched for (live old-draft review campaigns 9200002/03/05/10,
2026-11-07, each opened one to three such missions after their mathematics
had already been accepted).

``ARGUS_FRAMEWORK_MAINTENANCE=off`` lets the operator who owns the fleet say
that framework defects are theirs to fix. Unset keeps the existing behaviour.
"""
from __future__ import annotations

import os
from typing import Mapping

ENV_NAME = "ARGUS_FRAMEWORK_MAINTENANCE"
_DISABLED = frozenset({"off", "0", "false", "no", "disabled"})


def framework_maintenance_enabled(env: Mapping[str, str] | None = None) -> bool:
    """Whether campaigns may open ``argus_maintenance`` missions."""
    env_map = env if env is not None else os.environ
    return str(env_map.get(ENV_NAME, "") or "").strip().lower() not in _DISABLED


DISABLED_PLANNER_GUIDANCE = (
    "- Framework maintenance is disabled for this run by the operator "
    f"(`{ENV_NAME}=off`). Never emit `TASK_VERTICAL=argus_maintenance` and never "
    "plan edits to the Argus runtime. If a framework defect blocks the "
    "objective, return waiting with `operator_action_required=true` and name the "
    "exact diagnostic and events.jsonl line; the operator fixes the framework."
)
