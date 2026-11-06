import io
import tarfile

import pytest

from counterexample_harness import reopen_openai_audit
from counterexample_harness.reopen_openai_audit import (
    audit_objective,
    describe_sources,
    parse_manuscripts,
)


def test_official_map_handles_nonstandard_pdf_names_and_keeps_each_paper():
    contents = """**032. A family.**
&emsp;[First](preprints/first/main.pdf)
&emsp;[Second](preprints/second/custom-name.pdf)
**341. Another family.**
&emsp;[Third](preprints/third/paper.pdf)
"""
    families = parse_manuscripts(contents)
    assert [p["manuscript_id"] for p in families["032"]] == ["first", "second"]
    assert families["341"][0]["pdf"] == "paper.pdf"


def test_duplicate_paper_association_is_not_silently_double_counted():
    with pytest.raises(ValueError, match="duplicate"):
        parse_manuscripts(
            "**001. First.**\n[a](preprints/same/paper.pdf)\n"
            "**032. Second.**\n[b](preprints/same/paper.pdf)\n"
        )


def test_missing_source_is_not_silently_skipped(tmp_path):
    with pytest.raises(FileNotFoundError, match="Missing manuscript"):
        describe_sources(tmp_path, {"manuscript_id": "missing"})


def test_source_manifest_binds_actual_files_and_separate_reports(tmp_path):
    source = tmp_path / "preprints" / "paper"
    source.mkdir(parents=True)
    (source / "main.tex").write_text("first version")
    first = describe_sources(tmp_path, {"manuscript_id": "paper"})
    (source / "main.tex").write_text("second version")
    second = describe_sources(tmp_path, {"manuscript_id": "paper"})
    assert first["tex_sources"] != second["tex_sources"]
    assert first["report"] == "research/papers/paper/report.md"


def test_withdrawn_snapshot_restores_archived_source_without_changing_notice(tmp_path, monkeypatch):
    source = tmp_path / "source"
    notice = source / "preprints" / "paper"
    notice.mkdir(parents=True)
    (notice / "README.md").write_text("withdrawal notice")
    data = b"original proof"
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w") as archive:
        info = tarfile.TarInfo("preprints/paper/main.tex")
        info.size = len(data)
        archive.addfile(info, io.BytesIO(data))
    calls = []

    def git_archive(command):
        calls.append(command)
        return buffer.getvalue()

    monkeypatch.setattr(reopen_openai_audit.subprocess, "check_output", git_archive)
    snapshot = reopen_openai_audit.withdrawn_snapshot(source, tmp_path / "audit", "paper")
    assert (snapshot / "preprints/paper/main.tex").read_bytes() == data
    assert not (notice / "main.tex").exists()
    assert (notice / "README.md").read_text() == "withdrawal notice"
    assert reopen_openai_audit.withdrawn_snapshot(source, tmp_path / "audit", "paper") == snapshot
    assert len(calls) == 1


def test_objective_requires_all_papers_without_prejudging_their_mathematics(tmp_path):
    manifest = {
        "upstream_commit": "revision",
        "manuscripts": [
            {"manuscript_id": slug, "report": f"{slug}/report.md", "verdict": f"{slug}/verdict.json"}
            for slug in ["first", "second"]
        ],
    }
    objective = audit_objective(manifest, tmp_path / "old")
    assert "first/report.md" in objective and "second/report.md" in objective
    assert "not production of a publishable new theorem" in objective
    assert "unresolved assessment is not proof" in objective
