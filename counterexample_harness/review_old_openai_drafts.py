"""Prepare isolated reviews of all old OpenAI audit drafts without changing them."""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from pathlib import Path

TEMPLATE = Path(__file__).with_name("openai_family_objective.md")
LAUNCH_TEXT = (
    "Use staged math, research_target_level=exploratory. "
    "EXECUTION_TASK: Verify and explain every OpenAI manuscript of this family "
    "under OBJECTIVE.md: a GUIDE.md and verdict.json per manuscript, each error, "
    "deficiency or advance as an evidenced finding, and FAMILY_REPORT.md. "
    "The native independent Reviewer decides final acceptance.\n"
)


def agents_text(batch_root: Path) -> str:
    return (
        "# OpenAI family verification\n\nRead OBJECTIVE.md for the sole task "
        "contract and PRIOR_DRAFTS.json for read-only inputs: the family's OpenAI "
        "manuscripts and Argus's earlier work. Old instructions are not the current "
        "objective. Never modify old drafts or their ledgers. Invoke Argus modules "
        f"with `{batch_root.parent / 'argus-latest/.venv/bin/python'}`.\n"
    )
INPUT_DIRECTORIES = {"openai_manuscript", ".git", ".lake", ".venv", "__pycache__", "node_modules"}


def inventory(old: Path, snapshot_files: list[dict]) -> dict:
    artifacts = {}
    excluded = []
    for current, directories, files in os.walk(old / "research", followlinks=False):
        parent = Path(current)
        for name in list(directories):
            path = parent / name
            if name in INPUT_DIRECTORIES or path.is_symlink():
                excluded.append({
                    "path": str(path.relative_to(old)),
                    "kind": "reference_input_or_tooling",
                })
                directories.remove(name)
        for name in files:
            path = parent / name
            if path.is_symlink():
                excluded.append({
                    "path": str(path.relative_to(old)),
                    "kind": "reference_symlink",
                })
                continue
            relative = str(path.relative_to(old))
            artifacts[relative] = {"path": relative, "bytes": path.stat().st_size}
    for entry in snapshot_files:
        relative = Path(entry["path"]).relative_to(old.name)
        if ".." in relative.parts:
            raise ValueError(f"Invalid archived artifact path: {entry['path']}")
        if not (old / relative).is_file():
            raise FileNotFoundError(f"Preserved draft unavailable: {old / relative}")
        artifacts.setdefault(str(relative), {
            "path": str(relative),
            "bytes": (old / relative).stat().st_size,
        })
    if not artifacts:
        raise ValueError(f"No old draft artifacts found: {old}")
    return {
        "old_workspace": str(old),
        "artifacts": [artifacts[path] for path in sorted(artifacts)],
        "reference_inputs_and_tooling": excluded,
    }


def materialize(batch_root: Path, snapshot_manifest: Path) -> list[dict]:
    snapshot = json.loads(snapshot_manifest.read_text())
    archived = defaultdict(list)
    for entry in snapshot["files"]:
        archived[Path(entry["path"]).parts[0]].append(entry)
    old_roots = sorted(path for path in (batch_root / "campaigns").glob("9000*")
                       if path.is_dir())
    if not old_roots:
        raise ValueError("No old OpenAI draft workspaces found")
    if set(archived) - {path.name for path in old_roots}:
        raise ValueError("The snapshot contains old campaigns absent from this workspace")
    queue = []
    for old in old_roots:
        family = old.name.removeprefix("9000")
        cid = f"9200{family}"
        root = batch_root / "campaigns" / cid
        manifest = {
            "task_kind": "old_draft_review",
            "family": family,
            "preserved_snapshot_manifest": str(snapshot_manifest),
            "manuscript_reference_manifest": str(
                batch_root / "campaigns" / f"9100{family}" / "MANUSCRIPTS.json"
            ),
            **inventory(old, archived[old.name]),
        }
        manifest_path = root / "PRIOR_DRAFTS.json"
        text = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
        if manifest_path.exists():
            if manifest_path.read_text() != text:
                raise ValueError(f"Existing review has a different input inventory: {root}")
        else:
            if root.exists() and any(root.iterdir()):
                raise ValueError(f"Refusing to overwrite an existing workspace: {root}")
            root.mkdir(parents=True, exist_ok=True)
            manifest_path.write_text(text)
            (root / "OBJECTIVE.md").write_text(TEMPLATE.read_text())
            (root / "LAUNCH.md").write_text(LAUNCH_TEXT)
            (root / "AGENTS.md").write_text(agents_text(batch_root))
            (root / "campaign.json").write_text(json.dumps({
                "id": cid,
                "family": family,
                "task_kind": "old_draft_review",
                "research_target_level": "exploratory",
                "math_objective_mode": "exploratory",
                "previous_campaign": str(old),
            }, indent=2) + "\n")
        queue.append({
            "campaign_id": cid,
            "family_id": family,
            "task_kind": "old_draft_review",
            "research_target_level": "exploratory",
            "old_workspace": str(old),
            "input_artifacts": len(manifest["artifacts"]),
        })
    return queue


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-root", type=Path, required=True)
    parser.add_argument("--snapshot-manifest", type=Path, required=True)
    parser.add_argument("--queue", type=Path, required=True)
    args = parser.parse_args()
    queue = materialize(args.batch_root, args.snapshot_manifest)
    args.queue.write_text(json.dumps(queue, indent=2) + "\n")
    print(json.dumps({
        "review_campaigns": len(queue),
        "input_artifacts": sum(item["input_artifacts"] for item in queue),
        "queue": str(args.queue),
    }))


if __name__ == "__main__":
    main()
