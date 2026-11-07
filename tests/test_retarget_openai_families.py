"""Retargeting rewrites only the contract of unfinished families (spec §1)."""
from __future__ import annotations

from pathlib import Path

from counterexample_harness.retarget_openai_families import retarget
from counterexample_harness.review_old_openai_drafts import LAUNCH_TEXT, TEMPLATE


def _family(batch: Path, cid: str) -> Path:
    root = batch / "campaigns" / cid
    (root / "research").mkdir(parents=True)
    (root / "PRIOR_DRAFTS.json").write_text('{"family": "x"}\n')
    (root / "OBJECTIVE.md").write_text("# Review the old Argus drafts\n")
    (root / "LAUNCH.md").write_text("old launch\n")
    (root / "AGENTS.md").write_text("old agents\n")
    (root / "research" / "OLD_ROUND_REVIEW.md").write_text("work in progress\n")
    return root


def test_unfinished_family_gets_the_current_contract_and_keeps_its_work(tmp_path: Path) -> None:
    running = _family(tmp_path, "9200002")
    done = _family(tmp_path, "9200001")

    report = retarget(tmp_path, {"9200001"})

    assert report["retargeted"] == ["9200002"]
    assert report["completed_kept"] == ["9200001"]
    assert (running / "OBJECTIVE.md").read_text() == TEMPLATE.read_text()
    assert (running / "LAUNCH.md").read_text() == LAUNCH_TEXT
    assert (running / "research" / "OLD_ROUND_REVIEW.md").read_text() == "work in progress\n"
    assert (running / "PRIOR_DRAFTS.json").read_text() == '{"family": "x"}\n'
    assert (done / "OBJECTIVE.md").read_text() == "# Review the old Argus drafts\n"
    # Idempotent: a second run changes nothing.
    assert retarget(tmp_path, {"9200001"})["retargeted"] == []


def test_dry_run_writes_nothing(tmp_path: Path) -> None:
    root = _family(tmp_path, "9200003")
    assert retarget(tmp_path, set(), dry_run=True)["retargeted"] == ["9200003"]
    assert (root / "OBJECTIVE.md").read_text() == "# Review the old Argus drafts\n"
