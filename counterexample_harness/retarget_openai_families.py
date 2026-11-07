#!/usr/bin/env python3
"""Move existing 9200 family workspaces onto the current family contract.

The workspaces were created under the old-draft review contract, which spec
docs/MATH_SPEC.zh-CN.md lists as a deviation from §1. This rewrites only the
contract files (OBJECTIVE.md, LAUNCH.md, AGENTS.md) of families that have not
completed; inputs (PRIOR_DRAFTS.json), research output and ledgers are not
touched, and completed families keep the contract they were accepted under.
A running daemon sees the change as an OBJECTIVE.md change at its next turn.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

try:
    from .review_old_openai_drafts import LAUNCH_TEXT, TEMPLATE, agents_text
except ImportError:  # run as a script
    from review_old_openai_drafts import LAUNCH_TEXT, TEMPLATE, agents_text


def _write(path: Path, text: str) -> bool:
    if path.is_file() and path.read_text() == text:
        return False
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(text)
    os.replace(tmp, path)
    return True


def retarget(batch_root: Path, completed: set[str], *, dry_run: bool = False) -> dict:
    objective = TEMPLATE.read_text()
    files = {
        "OBJECTIVE.md": objective,
        "LAUNCH.md": LAUNCH_TEXT,
        "AGENTS.md": agents_text(batch_root),
    }
    report = {"retargeted": [], "unchanged": [], "completed_kept": []}
    for root in sorted((batch_root / "campaigns").glob("9200*")):
        if not (root / "PRIOR_DRAFTS.json").is_file():
            continue
        if root.name in completed:
            report["completed_kept"].append(root.name)
            continue
        if dry_run:
            stale = any(
                not (root / name).is_file() or (root / name).read_text() != text
                for name, text in files.items()
            )
            report["retargeted" if stale else "unchanged"].append(root.name)
            continue
        changed = [_write(root / name, text) for name, text in files.items()]
        report["retargeted" if any(changed) else "unchanged"].append(root.name)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-root", type=Path, required=True)
    parser.add_argument("--fleet-state", type=Path, required=True,
                        help="fleet_state.json; its `completed` families are left alone")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    completed = set(json.loads(args.fleet_state.read_text()).get("completed", []))
    report = retarget(args.batch_root, completed, dry_run=args.dry_run)
    print(json.dumps({key: len(value) for key, value in report.items()}))


if __name__ == "__main__":
    main()
