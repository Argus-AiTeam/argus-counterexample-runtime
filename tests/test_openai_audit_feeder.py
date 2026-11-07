import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from counterexample_harness import launch_campaign_argus as launcher
from counterexample_harness import openai_audit_feeder as feeder


@pytest.fixture
def audit_fleet(tmp_path, monkeypatch):
    monkeypatch.setattr(feeder, "BATCH_ROOT", tmp_path)
    monkeypatch.setattr(feeder, "QUEUE_PATH", tmp_path / "queue.json")
    monkeypatch.setattr(feeder, "STATE_PATH", tmp_path / "state.json")
    monkeypatch.setattr(feeder, "TARGET_CONCURRENCY", 1)
    monkeypatch.setattr(feeder, "sync_project_evolution_library", lambda *args: None)
    feeder.QUEUE_PATH.write_text(json.dumps([{"campaign_id": "9100001"}]))
    monkeypatch.setattr(
        feeder, "vertical_completion_certificate_status", lambda *args: {"ok": False}
    )
    return tmp_path / "campaigns" / "9100001"


@pytest.mark.parametrize("verdict", ["supports", "refutes", "inconclusive"])
def test_evidence_count_is_not_completion(audit_fleet, verdict):
    research = audit_fleet / "research"
    research.mkdir(parents=True)
    (research / "MATH_STATE.json").write_text(json.dumps({
        "evidence": [{"produced_by": "reviewer:test", "verdict": verdict}] * 20,
    }))
    reviewer = audit_fleet / "roles" / "reviewer"
    reviewer.mkdir(parents=True)
    (reviewer / "progress.json").write_text('{"status": "bounded_review_complete"}')
    assert not feeder.is_campaign_finished("9100001")


def test_unbound_pipeline_flags_are_not_completion(audit_fleet):
    state = audit_fleet / ".argus"
    state.mkdir(parents=True)
    (state / "PIPELINE_STATE.json").write_text(
        '{"completed": true, "current_stage": "complete"}'
    )
    assert not feeder.is_campaign_finished("9100001")


def test_native_certificate_is_authoritative(audit_fleet, monkeypatch):
    monkeypatch.setattr(
        feeder, "vertical_completion_certificate_status", lambda *args: {"ok": True}
    )
    assert feeder.is_campaign_finished("9100001")


def test_draining_prior_phase_keeps_its_capacity_reserved(audit_fleet, monkeypatch):
    feeder.STATE_PATH.write_text(json.dumps({"draining_campaigns": ["old-campaign"]}))
    monkeypatch.setattr(
        feeder, "get_daemon_pid", lambda cid: 123 if cid == "old-campaign" else None
    )
    monkeypatch.setattr(
        feeder.subprocess, "run", lambda *args, **kwargs: pytest.fail("capacity is occupied")
    )

    state = feeder.tick()

    assert state["active"] == []
    assert state["draining_campaigns"] == ["old-campaign"]
    assert state["occupied_count"] == 1


def test_exited_prior_phase_releases_capacity_without_becoming_a_result(
    audit_fleet, monkeypatch,
):
    feeder.STATE_PATH.write_text(json.dumps({"draining_campaigns": ["old-campaign"]}))
    launches = []

    def launch(*args, **kwargs):
        launches.append(args[0])
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(feeder.subprocess, "run", launch)
    monkeypatch.setattr(
        feeder, "get_daemon_pid",
        lambda cid: 123 if cid == "9100001" and launches else None,
    )

    state = feeder.tick()

    assert state["active"] == ["9100001"]
    assert state["draining_campaigns"] == []
    assert state["completed"] == []


def test_reviewed_negative_audit_certifies_and_releases_a_fleet_slot(audit_fleet, monkeypatch):
    from argus_skill.core.models import ReviewDecision
    from argus_skill.manager import Manager
    from argus_skill.skills.stage_machine import advance_stage
    from argus_skill.skills.vertical_select import (
        persist_vertical,
        vertical_completion_certificate_status,
    )
    from argus_skill.verticals.math.objective_mode import set_objective

    persist_vertical(
        audit_fleet, "math", workflow_mode="staged", research_target_level="exploratory"
    )
    set_objective(audit_fleet, mode="exploratory")
    advance_stage(audit_fleet, target_stage="solve", reason="scope reviewed")
    advance_stage(audit_fleet, target_stage="review", reason="investigation reviewed")
    review = ReviewDecision(
        status="done",
        reason="The source-bound investigation is complete, not the manuscript theorem.",
        next_action="",
        research_result={
            "result_class": "honest_final_report",
            "correctness_status": "verified",
            "novelty_status": "not_applicable",
            "significance_status": "exploratory",
            "statement_fidelity_status": "verified",
            "evidence": ["The proposed counterexample fails an original hypothesis."],
            "limitations": ["Unexamined manuscript claims remain unresolved."],
        },
    )
    decision = Manager(
        project_root=audit_fleet, execution_workdir=audit_fleet, runner=object()
    ).decide_stage_transition(
        review=review,
        project_root=audit_fleet,
        mission_scope="final_submission",
        open_ended=False,
        run_exec=lambda _prompt: SimpleNamespace(
            last_agent_message=(
                '{"action":"complete","target_stage":"review","reason":"scoped audit accepted"}'
            )
        ),
    )
    assert decision.action == "complete"
    monkeypatch.setattr(
        feeder, "vertical_completion_certificate_status", vertical_completion_certificate_status
    )
    feeder.QUEUE_PATH.write_text(json.dumps([
        {"campaign_id": "9100001"}, {"campaign_id": "9100002"},
    ]))
    feeder.STATE_PATH.write_text(json.dumps({"launched_history": ["9100001"]}))
    launches = []

    def launch(command, **kwargs):
        launches.append(command[-1])
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(feeder.subprocess, "run", launch)
    monkeypatch.setattr(
        feeder, "get_daemon_pid",
        lambda cid: 123 if cid == "9100002" and launches else None,
    )

    state = feeder.tick()

    assert state["completed"] == ["9100001"]
    assert state["active"] == ["9100002"]
    assert launches == ["9100002"]


def test_feeder_reads_the_daemons_runtime_not_the_interpreters_install(tmp_path):
    skills = tmp_path / "argus-live-update/argus_skill/skills"
    skills.mkdir(parents=True)
    (skills.parent / "__init__.py").write_text("")
    (skills / "__init__.py").write_text("")
    (skills / "builtins.py").write_text(
        "def sync_project_evolution_library(*args): pass\n"
    )
    (skills / "vertical_select.py").write_text(
        "def vertical_completion_certificate_status(*args): return {'runtime': 'daemon'}\n"
    )
    code = (
        "import importlib.util;"
        f"s=importlib.util.spec_from_file_location('feeder',{str(Path(feeder.__file__))!r});"
        "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
        "print(m.vertical_completion_certificate_status('', '')['runtime'])"
    )
    output = subprocess.check_output(
        [sys.executable, "-c", code],
        cwd=tmp_path,
        env={**os.environ, "ARGUS_AUDIT_WORKSPACE": str(tmp_path)},
        text=True,
    )
    assert output.strip() == "daemon"


@pytest.mark.parametrize("matching_home", [False, True])
def test_pid_must_belong_to_this_campaign(audit_fleet, monkeypatch, tmp_path, matching_home):
    monkeypatch.setattr(feeder, "ZIMO", tmp_path)
    home = tmp_path / ".argus-campaign-9100001"
    project = home / "projects" / "test"
    project.mkdir(parents=True)
    (project / "daemon.pid").write_text("123")

    def read_bytes(path):
        if path.name == "cmdline":
            return b"/venv/bin/python\0/venv/bin/argus\0--daemon\0"
        actual_home = home if matching_home else tmp_path / ".argus-campaign-other"
        return f"ARGUS_SKILL_HOME={actual_home}\0".encode()

    monkeypatch.setattr(Path, "read_bytes", read_bytes)
    assert feeder.get_daemon_pid("9100001") == (123 if matching_home else None)


def test_exited_partial_campaign_is_relaunched_not_graduated(audit_fleet, monkeypatch):
    audit_fleet.mkdir(parents=True)
    feeder.STATE_PATH.write_text(json.dumps({
        "completed": ["9100001"], "launched_history": ["9100001"],
        "audit_generation": "per-manuscript-v2",
    }))
    calls = []
    monkeypatch.setattr(feeder, "get_daemon_pid", lambda cid: 123 if calls else None)

    def launch(*args, **kwargs):
        calls.append(args[0])
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(feeder.subprocess, "run", launch)
    state = feeder.tick()
    assert calls
    assert state["completed"] == []
    assert state["active"] == ["9100001"]
    assert state["audit_generation"] == "per-manuscript-v2"


def test_certified_daemon_is_allowed_to_exit_without_killing(audit_fleet, monkeypatch):
    feeder.STATE_PATH.write_text(json.dumps({"launched_history": ["9100001"]}))
    monkeypatch.setattr(
        feeder, "vertical_completion_certificate_status", lambda *args: {"ok": True}
    )
    monkeypatch.setattr(feeder, "get_daemon_pid", lambda cid: 123)
    monkeypatch.setattr(feeder.os, "kill", lambda *args: pytest.fail("must not kill daemon"))
    state = feeder.tick()
    assert state["completed"] == ["9100001"]
    assert state["active"] == ["9100001"]


def test_zero_exit_without_daemon_is_not_active_or_complete(audit_fleet, monkeypatch):
    monkeypatch.setattr(feeder, "get_daemon_pid", lambda cid: None)
    monkeypatch.setattr(
        feeder.subprocess, "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0, stdout="", stderr=""),
    )
    state = feeder.tick()
    assert state["completed"] == []
    assert state["active"] == []
    assert "9100001" in state["launch_failures"]


@pytest.mark.parametrize("target", ["exploratory", "publishable", "doctoral"])
def test_launcher_respects_explicit_target(tmp_path, monkeypatch, target):
    monkeypatch.setenv("ARGUS_SKILL_RESEARCH_TARGET_LEVEL", target)
    assert launcher.campaign_research_target_level(tmp_path) == target


@pytest.mark.parametrize("target", ["exploratory", "publishable", "doctoral"])
def test_launcher_preserves_existing_target(tmp_path, monkeypatch, target):
    from argus_skill.core import research_contract

    monkeypatch.delenv("ARGUS_SKILL_RESEARCH_TARGET_LEVEL", raising=False)
    monkeypatch.delenv("ARGUS_SKILL_MATH_RESEARCH_TARGET_LEVEL", raising=False)
    monkeypatch.setattr(research_contract, "resolve_research_target_level", lambda _: target)
    assert launcher.campaign_research_target_level(tmp_path) == target


def test_launcher_applies_declared_audit_mode_before_manager_startup(tmp_path, monkeypatch):
    from argus_skill.skills.vertical_select import persist_vertical
    from argus_skill.verticals.math.objective_mode import (
        adopt_operator_objective,
        resolve_objective,
    )

    workdir = tmp_path / "campaigns" / "9100001"
    workdir.mkdir(parents=True)
    (workdir / "OBJECTIVE.md").write_text("Search for a source-bound erroneous lemma.")
    (workdir / "LAUNCH.md").write_text("One source-bound erroneous lemma suffices.")
    (workdir / "campaign.json").write_text('{"math_objective_mode": "exploratory"}')
    persist_vertical(workdir, "math", research_target_level="exploratory")
    adopt_operator_objective(workdir, "Old full-paper audit goal")
    monkeypatch.setattr(launcher, "ROOT", tmp_path)
    monkeypatch.setattr(launcher.sys, "argv", ["launch", "9100001"])
    monkeypatch.setattr(launcher.shutil, "copytree", lambda *args, **kwargs: None)
    monkeypatch.setenv("ARGUS_SKILL_RESEARCH_TARGET_LEVEL", "exploratory")
    monkeypatch.setattr(
        launcher.subprocess, "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0, stdout="", stderr=""),
    )

    launcher.main()

    assert resolve_objective(workdir).mode == "exploratory"
    assert resolve_objective(workdir).goal == "One source-bound erroneous lemma suffices."
