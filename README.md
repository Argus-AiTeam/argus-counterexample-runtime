# Argus Math

Argus Math turns a mathematical question into a conclusion another person can understand and
check: a paper verified and explained, a statement proved or refuted, a result pushed further.
It runs on the Argus core ([`lbx154/Argus`](https://github.com/lbx154/Argus), branch
`feat/ts-core`) through the math pack in this repository.

| Path | What it is |
|---|---|
| [`docs/MATH_SPEC.zh-CN.md`](docs/MATH_SPEC.zh-CN.md) | The spec: the single authority for Argus Math |
| [`docs/MIGRATION_TS_CORE.zh-CN.md`](docs/MIGRATION_TS_CORE.zh-CN.md) | Why and how Argus Math moved to the TypeScript core |
| [`pack/math/`](pack/math/) | The math pack: `SKILL.md` (how the team works and writes), setup (Lean 4.31.0, Mathlib, Jacobian), tools `math-lean-verify`, `math-cite`, `math-ops`, tests |
| [`ops/`](ops/) | Running it: a user service for Argus, and a script that prepares a workspace for one family of OpenAI's mathematics collection |

## Use

1. Install Argus (see its getting-started guide) and copy `pack/math/` to `~/.argus/skill-packs/math`.
   Argus runs the pack's setup once.
2. Start Argus, for example with [`ops/argus-ts.service`](ops/argus-ts.service).
3. For an OpenAI family: `ops/openai-family/make-workspace 127 ~/workspaces --lang zh`, open a
   project on the workspace it prints, and paste its `REQUEST.md`.

Results are published in [`Argus-AiTeam/argus-mathematics`](https://github.com/Argus-AiTeam/argus-mathematics).
The retired Python runtime is kept on the branch `backup/python-runtime`.
