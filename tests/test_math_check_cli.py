"""``math check`` is the delivery gate run early, not a second rulebook (spec §4, §10.1)."""
from __future__ import annotations

import io
import json
from contextlib import redirect_stdout
from pathlib import Path

from argus_skill.verticals.math import math_state
from argus_skill.verticals.math.check import main
from argus_skill.verticals.math.objective_mode import set_objective
from argus_skill.verticals.math.stages import stage_completion_issues


def _check(root: Path) -> tuple[int, dict]:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        code = main(["--project-root", str(root)])
    return code, json.loads(buffer.getvalue())


def _ledger(root: Path, *argv: str) -> None:
    with redirect_stdout(io.StringIO()):
        math_state.main([argv[0], "--project-root", str(root), *argv[1:]])


def test_unchosen_objective_is_refused(tmp_path: Path) -> None:
    code, report = _check(tmp_path)
    assert code == 1 and report["ok"] is False
    assert report["issues"] == list(stage_completion_issues("review", tmp_path))


def test_clean_exploratory_project_passes(tmp_path: Path) -> None:
    set_objective(tmp_path, mode="exploratory")
    assert _check(tmp_path) == (0, {"ok": True, "stage": "review", "issues": []})


def test_an_unread_citation_blocks_delivery(tmp_path: Path) -> None:
    set_objective(tmp_path, mode="exploratory")
    _ledger(tmp_path, "context", "--id", "ctx", "--statement", "Setting.")
    _ledger(tmp_path, "claim", "--id", "C1", "--context", "ctx", "--statement", "A bound.")
    _ledger(
        tmp_path, "assume", "--claim", "C1", "--id", "K", "--by", "engineer:e",
        "--statement", "The cited bound.", "--source", "K 2020",
        "--source-id", "arxiv:2001.00001v1", "--locator", "Theorem 3.2",
    )

    code, report = _check(tmp_path)

    assert code == 1
    assert any("C1" in issue and "K" in issue for issue in report["issues"])
    assert report["issues"] == list(stage_completion_issues("review", tmp_path))
