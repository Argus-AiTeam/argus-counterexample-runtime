#!/usr/bin/env python3
"""Maintain 14 concurrent Argus daemons (gpt-6.1-sol) across all 373 OpenAI families."""

from __future__ import annotations

import glob
import json
import os
import signal
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

AUDIT_DIR = Path("/home/argustest/zimo/openai-math-audit")
BATCH_ROOT = Path("/home/argustest/zimo/counterexample-batch-1")
ZIMO = Path("/home/argustest/zimo")
PYTHON_BIN = "/home/argustest/zimo/argus-latest/.venv/bin/python"
LAUNCH_SCRIPT = str(BATCH_ROOT / "scripts" / "launch_campaign_argus.py")
QUEUE_PATH = AUDIT_DIR / "openai_373_queue.json"
STATE_PATH = AUDIT_DIR / "fleet_state.json"
TARGET_CONCURRENCY = 14

sys.path.insert(0, "/home/argustest/argustest2/argus-counterexample-runtime")
from argus_skill.skills.builtins import sync_project_evolution_library

MASTER_HOME = Path("/home/argustest/.argus-skill")


def get_daemon_pid(cid: str) -> int | None:
    pfiles = sorted(glob.glob(str(ZIMO / f".argus-campaign-{cid}" / "projects" / "*" / "daemon.pid")))
    if not pfiles:
        return None
    try:
        pid = int(Path(pfiles[-1]).read_text().strip())
        if os.path.exists(f"/proc/{pid}"):
            return pid
    except Exception:
        return None
    return None


def is_campaign_finished(cid: str) -> bool:
    wdir = BATCH_ROOT / "campaigns" / cid
    pipe_p = wdir / ".argus" / "PIPELINE_STATE.json"
    if pipe_p.is_file():
        try:
            pipe = json.loads(pipe_p.read_text())
            if pipe.get("completed") is True or pipe.get("current_stage") == "complete":
                return True
        except Exception:
            pass
    rev_p = wdir / "roles" / "reviewer" / "progress.json"
    eng_p = wdir / "roles" / "engineer" / "progress.json"
    if rev_p.is_file() and eng_p.is_file():
        try:
            rev = json.loads(rev_p.read_text())
            eng = json.loads(eng_p.read_text())
            r_stat = str(rev.get("status") or "").lower()
            e_stat = str(eng.get("status") or "").lower()
            if r_stat in {"done", "completed", "certified"} and e_stat in {
                "done",
                "completed",
                "certified",
                "bounded_mission_complete",
            }:
                return True
        except Exception:
            pass
    return False


def tick() -> dict:
    queue = json.loads(QUEUE_PATH.read_text())
    state = (
        json.loads(STATE_PATH.read_text())
        if STATE_PATH.is_file()
        else {"completed": ["9000321"], "active": [], "launched_history": ["9000048", "9000059", "9000209", "9000321", "9000340", "9000032", "9000201", "9000053", "9000319", "9000046", "9000285", "9000063", "9000366", "9000067", "9000031"]}
    )
    completed = set(state.get("completed", []))
    launched_history = list(dict.fromkeys(state.get("launched_history", [])))

    # 1. Check all launched campaigns for live PIDs and completion
    currently_running = []
    for cid in launched_history:
        if cid in completed:
            continue
        pid = get_daemon_pid(cid)
        if is_campaign_finished(cid):
            if pid is not None:
                try:
                    os.kill(pid, signal.SIGTERM)
                except OSError:
                    pass
            completed.add(cid)
            sync_project_evolution_library(MASTER_HOME, BATCH_ROOT / "campaigns" / cid)
            continue
        if pid is not None:
            currently_running.append(cid)
            sync_project_evolution_library(MASTER_HOME, BATCH_ROOT / "campaigns" / cid)
        else:
            # Check if it produced Reviewer evidence before exiting
            ms_p = BATCH_ROOT / "campaigns" / cid / "research" / "MATH_STATE.json"
            if ms_p.is_file():
                try:
                    ms = json.loads(ms_p.read_text())
                    if len(ms.get("evidence", [])) >= 5:
                        completed.add(cid)
                        sync_project_evolution_library(MASTER_HOME, BATCH_ROOT / "campaigns" / cid)
                        continue
                except Exception:
                    pass

    # 2. Fill slots up to TARGET_CONCURRENCY (14) using gpt-6.1-sol
    slots_needed = max(0, TARGET_CONCURRENCY - len(currently_running))
    newly_launched = []
    if slots_needed > 0:
        for item in queue:
            cid = item["campaign_id"]
            if cid in completed or cid in currently_running:
                continue
            env = os.environ.copy()
            env["ARGUS_CAMPAIGN_MODEL"] = "gpt-6.1-sol"
            res = subprocess.run(
                [PYTHON_BIN, LAUNCH_SCRIPT, cid],
                env=env,
                capture_output=True,
                text=True,
                timeout=90,
                check=False,
            )
            if res.returncode == 0:
                currently_running.append(cid)
                if cid not in launched_history:
                    launched_history.append(cid)
                newly_launched.append(cid)
                slots_needed -= 1
                if slots_needed <= 0:
                    break

    state = {
        "updated_at": datetime.now(UTC).isoformat(),
        "target_concurrency": TARGET_CONCURRENCY,
        "model": "gpt-6.1-sol",
        "active_count": len(currently_running),
        "active": currently_running,
        "completed_count": len(completed),
        "completed": sorted(completed),
        "newly_launched": newly_launched,
        "total_queue": len(queue),
        "launched_history": launched_history,
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
                f"completed={st['completed_count']}/{st['total_queue']} newly_launched={st['newly_launched']}",
                flush=True,
            )
        except Exception as exc:
            print(f"[ERROR] {exc}", flush=True)
        time.sleep(60)


if __name__ == "__main__":
    main()
