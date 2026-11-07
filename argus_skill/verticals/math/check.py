"""``math check``: the delivery gate, runnable before delivery.

Spec ``docs/MATH_SPEC.zh-CN.md`` §4 and §9.1: a delivery with open issues is
refused. The refusal itself is ``stages.stage_completion_issues`` at the final
stage; this command runs exactly that function, so an Engineer or Reviewer sees
what the gate will say before submitting instead of learning it from a hold.
There is one gate and this is a view of it, not a second set of rules.

Exit status 0 means the gate has nothing to report; 1 means it would refuse.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .stages import STAGE_ORDER, stage_completion_issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--stage",
        default=STAGE_ORDER[-1],
        choices=STAGE_ORDER,
        help="stage whose completion gate to run (default: the delivery stage)",
    )
    args = parser.parse_args(argv)
    root = args.project_root.expanduser().resolve()
    issues = list(stage_completion_issues(args.stage, root))
    print(
        json.dumps(
            {"ok": not issues, "stage": args.stage, "issues": issues},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
