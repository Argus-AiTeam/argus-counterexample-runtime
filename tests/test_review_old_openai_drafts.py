import json

import pytest

from counterexample_harness.review_old_openai_drafts import inventory, materialize


def test_all_old_artifacts_are_inputs_not_predetermined_results(tmp_path):
    old = tmp_path / "campaigns/9000001"
    proof = old / "research/unit/proof.md"
    proof.parent.mkdir(parents=True)
    proof.write_text("Old proof whose validity has not been decided.")
    (proof.parent / "Main.lean").write_text("theorem substantive : True := True.intro")
    source = old / "research/openai_manuscript"
    source.mkdir()
    (source / "upstream.tex").write_text("reference, not an Argus draft")
    snapshot = tmp_path / "snapshot.json"
    snapshot.write_text(json.dumps({
        "files": [{"path": "9000001/research/unit/proof.md", "bytes": proof.stat().st_size}],
    }))

    queue = materialize(tmp_path, snapshot)

    assert [row["campaign_id"] for row in queue] == ["9200001"]
    root = tmp_path / "campaigns/9200001"
    manifest = json.loads((root / "PRIOR_DRAFTS.json").read_text())
    assert {row["path"] for row in manifest["artifacts"]} == {
        "research/unit/proof.md", "research/unit/Main.lean",
    }
    assert manifest["reference_inputs_and_tooling"] == [{
        "path": "research/openai_manuscript", "kind": "reference_input_or_tooling",
    }]
    assert "status" not in manifest
    assert proof.read_text() == "Old proof whose validity has not been decided."
    assert json.loads((root / "campaign.json").read_text())["math_objective_mode"] == "exploratory"
    assert "One reviewed unit is not" in (root / "OBJECTIVE.md").read_text()
    assert materialize(tmp_path, snapshot) == queue


def test_missing_preserved_draft_is_not_silently_removed(tmp_path):
    old = tmp_path / "9000001"
    (old / "research").mkdir(parents=True)
    with pytest.raises(FileNotFoundError, match="Preserved draft unavailable"):
        inventory(old, [{"path": "9000001/research/missing-proof.md"}])


def test_changed_inventory_does_not_overwrite_an_existing_review(tmp_path):
    old = tmp_path / "campaigns/9000001/research"
    old.mkdir(parents=True)
    (old / "proof.md").write_text("original")
    snapshot = tmp_path / "snapshot.json"
    snapshot.write_text('{"files": []}')
    materialize(tmp_path, snapshot)
    verdict = tmp_path / "campaigns/9200001/research/verdict.json"
    verdict.parent.mkdir()
    verdict.write_text("preserved review evidence")
    (old / "second-proof.md").write_text("additional draft")

    with pytest.raises(ValueError, match="different input inventory"):
        materialize(tmp_path, snapshot)

    assert verdict.read_text() == "preserved review evidence"
