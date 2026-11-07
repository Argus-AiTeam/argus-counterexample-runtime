#!/usr/bin/env python3
"""Schedule manuscript audits using native completion certificates, not evidence counts."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

ZIMO = Path(os.environ.get("ARGUS_AUDIT_WORKSPACE", Path.home() / "zimo"))
AUDIT_DIR = ZIMO / "openai-math-audit"
BATCH_ROOT = ZIMO / "counterexample-batch-1"
PYTHON_BIN = str(ZIMO / "argus-latest/.venv/bin/python")
LAUNCH_SCRIPT = str(BATCH_ROOT / "scripts" / "launch_campaign_argus.py")
QUEUE_PATH = AUDIT_DIR / "openai_373_queue.json"
STATE_PATH = AUDIT_DIR / "fleet_state.json"
TARGET_CONCURRENCY = 24

sys.path.insert(0, str(ZIMO / "argus-live-update"))
from argus_skill.skills.builtins import sync_project_evolution_library
from argus_skill.skills.vertical_select import vertical_completion_certificate_status

MASTER_HOME = Path.home() / ".argus-skill"


def get_daemon_pid(cid: str) -> int | None:
    home = ZIMO / f".argus-campaign-{cid}"
    pfiles = sorted(
        (home / "projects").glob("*/daemon.pid"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    for path in pfiles:
        try:
            pid = int(path.read_text().strip())
            command = Path(f"/proc/{pid}/cmdline").read_bytes().split(b"\0")
            environment = Path(f"/proc/{pid}/environ").read_bytes().split(b"\0")
            if (
                pid > 0
                and b"--daemon" in command
                and any(Path(os.fsdecode(arg)).name in {"argus", "argus-skill"} for arg in command)
                and os.fsencode(f"ARGUS_SKILL_HOME={home}") in environment
            ):
                return pid
        except (OSError, ValueError):
            continue
    return None


def is_campaign_finished(cid: str) -> bool:
    result = vertical_completion_certificate_status(BATCH_ROOT / "campaigns" / cid, "math")
    return result.get("ok") is True


def tick() -> dict:
    queue = json.loads(QUEUE_PATH.read_text())
    state = (
        json.loads(STATE_PATH.read_text())
        if STATE_PATH.is_file()
        else {"completed": [], "active": [], "launched_history": []}
    )
    campaign_ids = {item["campaign_id"] for item in queue}
    completed = {
        cid for cid in state.get("completed", [])
        if cid in campaign_ids and is_campaign_finished(cid)
    }
    launched_history = list(dict.fromkeys(state.get("launched_history", [])))

    currently_running = []
    for cid in launched_history:
        if cid not in campaign_ids:
            continue
        pid = get_daemon_pid(cid)
        if is_campaign_finished(cid):
            completed.add(cid)
            sync_project_evolution_library(MASTER_HOME, BATCH_ROOT / "campaigns" / cid)
        if pid is not None:
            currently_running.append(cid)
            sync_project_evolution_library(MASTER_HOME, BATCH_ROOT / "campaigns" / cid)

    draining = [
        cid for cid in state.get("draining_campaigns", [])
        if get_daemon_pid(cid) is not None
    ]
    slots_needed = max(0, TARGET_CONCURRENCY - len(currently_running) - len(draining))
    newly_launched = []
    launch_failures = {}
    if slots_needed > 0:
        for item in queue:
            cid = item["campaign_id"]
            if cid in completed or cid in currently_running:
                continue
            env = os.environ.copy()
            env["ARGUS_CAMPAIGN_MODEL"] = "gpt-6.1-sol"
            target = item.get("research_target_level")
            if target:
                env["ARGUS_SKILL_RESEARCH_TARGET_LEVEL"] = target
            try:
                res = subprocess.run(
                    [PYTHON_BIN, LAUNCH_SCRIPT, cid],
                    env=env,
                    capture_output=True,
                    text=True,
                    timeout=90,
                    check=False,
                )
            except subprocess.TimeoutExpired:
                launch_failures[cid] = "launcher timed out; completion not established"
                continue
            if res.returncode == 0:
                if cid not in launched_history:
                    launched_history.append(cid)
                if get_daemon_pid(cid) is None:
                    if is_campaign_finished(cid):
                        completed.add(cid)
                    else:
                        launch_failures[cid] = "launcher exited zero without a live daemon"
                    continue
                currently_running.append(cid)
                sync_project_evolution_library(MASTER_HOME, BATCH_ROOT / "campaigns" / cid)
                newly_launched.append(cid)
                slots_needed -= 1
                if slots_needed <= 0:
                    break
            else:
                launch_failures[cid] = (res.stdout + res.stderr).strip()[-2000:]

    state = {
        **state,
        "updated_at": datetime.now(UTC).isoformat(),
        "target_concurrency": TARGET_CONCURRENCY,
        "model": "gpt-6.1-sol",
        "active_count": len(currently_running),
        "active": currently_running,
        "draining_campaigns": draining,
        "draining_count": len(draining),
        "occupied_count": len(currently_running) + len(draining),
        "completed_count": len(completed),
        "completed": sorted(completed),
        "newly_launched": newly_launched,
        "total_queue": len(queue),
        "launched_history": launched_history,
        "launch_failures": launch_failures,
    }
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
    return state


def main() -> None:
    if "--once" in sys.argv:
        print(json.dumps(tick(), indent=2, ensure_ascii=False))
        return
    while True:
        try:
            st = tick()
            print(
                f"[{st['updated_at']}] active={st['active_count']}/{st['target_concurrency']} "
                f"completed={st['completed_count']}/{st['total_queue']} "
                f"draining={st['draining_count']} newly_launched={st['newly_launched']}",
                flush=True,
            )
        except Exception as exc:
            print(f"[ERROR] {exc}", flush=True)
        time.sleep(60)


if __name__ == "__main__":
    main()
