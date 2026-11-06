"""Create a source-pinned, per-manuscript audit continuation without changing old drafts."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

REVISION = "4eaee87548250b2682affda7d05d947c05554bae"
PRE_WITHDRAWAL_REVISION = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
WORKSPACE = Path(os.environ.get("ARGUS_AUDIT_WORKSPACE", Path.home() / "zimo"))
AUDIT_DIR = WORKSPACE / "openai-math-audit"
BATCH_ROOT = WORKSPACE / "counterexample-batch-1"
OBJECTIVE_TEMPLATE = Path(__file__).with_name("openai_audit_objective.md")
WITHDRAWN = (
    "Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026",
    "Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026",
    "The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026",
)


def parse_manuscripts(contents: str) -> dict[str, list[dict]]:
    families = defaultdict(list)
    family = None
    seen = set()
    for line_number, line in enumerate(contents.splitlines(), 1):
        heading = re.match(r"\*\*(\d{3})\.", line)
        if heading:
            family = heading.group(1)
        for slug, pdf in re.findall(r"\]\(preprints/([^/]+)/([^)]*\.pdf)\)", line):
            if family is None or slug in seen:
                raise ValueError(f"Unbound or duplicate manuscript at CONTENTS.md:{line_number}")
            seen.add(slug)
            families[family].append({
                "manuscript_id": slug,
                "pdf": pdf,
                "contents_line": line_number,
                "source_status": "active",
            })
    if not families:
        raise ValueError("No manuscripts found in the pinned official index")
    return dict(families)


def describe_sources(source_repo: Path, paper: dict) -> dict:
    directory = source_repo / "preprints" / paper["manuscript_id"]
    if not directory.is_dir():
        raise FileNotFoundError(f"Missing manuscript source: {directory}")
    files = sorted(directory.rglob("*.tex"))
    if not files and not list(directory.glob("*.pdf")):
        raise FileNotFoundError(f"No TeX or PDF available: {directory}")
    return {
        **paper,
        "source_directory": str(directory),
        "tex_sources": [
            {"path": str(path.relative_to(directory)),
             "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in files
        ],
        "pdf_sources": [
            {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in sorted(directory.glob("*.pdf"))
        ],
        "report": f"research/papers/{paper['manuscript_id']}/report.md",
        "verdict": f"research/papers/{paper['manuscript_id']}/verdict.json",
    }


def withdrawn_snapshot(source_repo: Path, audit_dir: Path, slug: str) -> Path:
    snapshot = audit_dir / "source-snapshots" / PRE_WITHDRAWAL_REVISION
    destination = snapshot / "preprints" / slug
    if not destination.exists():
        archive = subprocess.check_output([
            "git", "-C", str(source_repo), "archive", PRE_WITHDRAWAL_REVISION,
            f"preprints/{slug}",
        ])
        audit_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=audit_dir) as temporary:
            with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
                stream.extractall(temporary, filter="data")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(Path(temporary) / "preprints" / slug), destination)
    return snapshot


def audit_objective(manifest: dict, prior: Path | None) -> str:
    prior_text = (
        f"Reuse prior work read-only at `{prior}`, after checking its source and scope."
        if prior else
        "Distinguish the upstream withdrawal and its archived proof from new findings."
    )
    return OBJECTIVE_TEMPLATE.read_text().format(
        revision=manifest["upstream_commit"], prior=prior_text,
    )


def write_audit_instructions(workdir: Path, manifest: dict, prior: Path | None) -> None:
    (workdir / "OBJECTIVE.md").write_text(audit_objective(manifest, prior))
    (workdir / "AGENTS.md").write_text(
        "# Audit execution\n\nRead OBJECTIVE.md for the sole task contract and "
        "MANUSCRIPTS.json for sources and output paths. Preserve old drafts. "
        f"Invoke Argus modules with `{WORKSPACE / 'argus-latest/.venv/bin/python'}`.\n"
    )
    (workdir / "LAUNCH.md").write_text(
        "Use staged math, research_target_level=exploratory. "
        "EXECUTION_TASK: Follow OBJECTIVE.md and MANUSCRIPTS.json. "
        "Seek a source-bound erroneous lemma, not full-paper certification. "
        "The native independent Reviewer judges the result.\n"
    )


def materialize(source_repo: Path, batch_root: Path, audit_dir: Path, revision: str) -> dict:
    head = subprocess.check_output(
        ["git", "-C", str(source_repo), "rev-parse", "HEAD"], text=True
    ).strip()
    dirty = subprocess.check_output(
        ["git", "-C", str(source_repo), "status", "--porcelain", "--untracked-files=no"],
        text=True,
    )
    if head != revision or dirty:
        raise ValueError("Source checkout must be clean and match the pinned revision")
    groups = parse_manuscripts((source_repo / "CONTENTS.md").read_text())
    described = {
        family: [describe_sources(source_repo, {**paper, "source_revision": revision})
                 for paper in papers]
        for family, papers in groups.items()
    }
    for i, slug in enumerate(WITHDRAWN, 1):
        notice = source_repo / "preprints" / slug / "README.md"
        paper = {
            "manuscript_id": slug, "source_status": "withdrawn_upstream",
            "withdrawal_source": "history.md, October 7, 2026",
            "source_revision": PRE_WITHDRAWAL_REVISION,
            "withdrawal_notice": {
                "path": str(notice), "revision": revision,
                "sha256": hashlib.sha256(notice.read_bytes()).hexdigest(),
            },
        }
        snapshot = withdrawn_snapshot(source_repo, audit_dir, slug)
        described[f"W{i:02d}"] = [describe_sources(snapshot, paper)]
    queue = []
    for family, papers in described.items():
        cid = f"9101{int(family[1:]):03d}" if family.startswith("W") else f"9100{family}"
        old = None if family.startswith("W") else batch_root / "campaigns" / f"9000{family}"
        workdir = batch_root / "campaigns" / cid
        manifest = {
            "schema_version": 2, "upstream_commit": revision, "family": family,
            "previous_campaign": str(old) if old else None, "manuscripts": papers,
        }
        manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
        manifest_path = workdir / "MANUSCRIPTS.json"
        if manifest_path.exists():
            if manifest_path.read_text() != manifest_text:
                raise ValueError(f"Existing continuation has a different source manifest: {workdir}")
        else:
            source_links = workdir / "research" / "openai_manuscript"
            source_links.mkdir(parents=True, exist_ok=True)
            for paper in papers:
                (source_links / paper["manuscript_id"]).symlink_to(
                    paper["source_directory"], target_is_directory=True
                )
            manifest_path.write_text(manifest_text)
            write_audit_instructions(workdir, manifest, old)
            (workdir / "campaign.json").write_text(json.dumps({
                "id": cid, "family": family, "research_target_level": "exploratory",
                "math_objective_mode": "exploratory", "model": "gpt-6.1-sol",
                "upstream_commit": revision, "paper_count": len(papers),
                "previous_campaign": str(old) if old else None,
            }, indent=2) + "\n")
        queue.append({
            "campaign_id": cid, "family_id": family, "paper_count": len(papers),
            "research_target_level": "exploratory", "upstream_commit": revision,
        })
    priority = {f: i for i, f in enumerate(["341", "032", "337", "376", "318", "247", "320"])}
    queue.sort(key=lambda item: (priority.get(item["family_id"], 1000), item["family_id"]))
    audit_dir.mkdir(parents=True, exist_ok=True)
    state_path = audit_dir / "fleet_state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if state.get("audit_generation") != "per-manuscript-v2":
        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        for name in ["fleet_state.json", "openai_373_queue.json"]:
            path = audit_dir / name
            if path.exists():
                shutil.copy2(path, audit_dir / f"{name}.before-reopen-{stamp}")
        state = {
            "audit_generation": "per-manuscript-v2", "upstream_commit": revision,
            "completed": [], "active": [], "launched_history": [],
        }
        state_path.write_text(json.dumps(state, indent=2) + "\n")
    (audit_dir / "openai_373_queue.json").write_text(json.dumps(queue, indent=2) + "\n")
    summary = {
        "audit_generation": "per-manuscript-v2", "upstream_commit": revision,
        "campaigns": len(queue),
        "active_manuscripts": sum(len(v) for k, v in described.items() if not k.startswith("W")),
        "withdrawn_manuscripts": len(WITHDRAWN),
        "total_manuscripts": sum(len(v) for v in described.values()),
        "previous_drafts_preserved": True,
    }
    (audit_dir / "paper_audit_v2_manifest.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repo", type=Path, default=AUDIT_DIR / "openai-math")
    parser.add_argument("--batch-root", type=Path, default=BATCH_ROOT)
    parser.add_argument("--audit-dir", type=Path, default=AUDIT_DIR)
    parser.add_argument("--revision", default=REVISION)
    parser.add_argument("--refresh-instructions", action="store_true")
    args = parser.parse_args()
    if args.refresh_instructions:
        queue = json.loads((args.audit_dir / "openai_373_queue.json").read_text())
        for item in queue:
            workdir = args.batch_root / "campaigns" / item["campaign_id"]
            manifest = json.loads((workdir / "MANUSCRIPTS.json").read_text())
            prior = manifest.get("previous_campaign")
            write_audit_instructions(workdir, manifest, Path(prior) if prior else None)
        print(json.dumps({"instructions_refreshed": len(queue)}))
        return
    print(json.dumps(materialize(
        args.source_repo, args.batch_root, args.audit_dir, args.revision
    ), indent=2))


if __name__ == "__main__":
    main()
