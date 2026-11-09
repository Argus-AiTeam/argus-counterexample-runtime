# Argus Math

Argus Math 把一个数学问题变成别人能读懂、也能复核的结论：核验并讲清一篇论文，证明或推翻一个命题，在已有结果上更进一步。
它运行在 Argus 内核（[`lbx154/Argus`](https://github.com/lbx154/Argus) 的 `feat/ts-core` 分支）上，通过本仓库的数学 pack 工作。

| 路径 | 内容 |
|---|---|
| [`docs/MATH_SPEC.zh-CN.md`](docs/MATH_SPEC.zh-CN.md) | 规格：Argus Math 的唯一权威 |
| [`docs/MIGRATION_TS_CORE.zh-CN.md`](docs/MIGRATION_TS_CORE.zh-CN.md) | 为什么、怎样迁到 TypeScript 内核 |
| [`pack/math/`](pack/math/) | 数学 pack：`SKILL.md`（团队怎么做、怎么写），setup（Lean 4.31.0、Mathlib、Jacobian），工具 `math-lean-verify`、`math-cite`、`math-ops`，测试 |
| [`ops/`](ops/) | 运行：Argus 的用户服务，以及为 OpenAI 论文集的一个家族准备工作区的脚本 |

## 使用

1. 安装 Argus（见它的 getting-started），把 `pack/math/` 复制到 `~/.argus/skill-packs/math`；Argus 会运行一次 pack 的 setup。
2. 启动 Argus，例如用 [`ops/argus-ts.service`](ops/argus-ts.service)。
3. 审一个 OpenAI 家族：`ops/openai-family/make-workspace 127 ~/workspaces --lang zh`，在它给出的工作区上开项目，贴入 `REQUEST.md`。

成果发布在 [`Argus-AiTeam/argus-mathematics`](https://github.com/Argus-AiTeam/argus-mathematics)。
退役的 Python runtime 保存在 `backup/python-runtime` 分支。
