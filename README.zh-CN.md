# Argus Counterexample Runtime（冻结版 Argus + `math` Vertical 一体化仓库）

本仓库将 **Live Counterexample Lab（开放猜想反例与状态审计实验，2026.08–2026.09）** 所使用的 **冻结版 Argus 运行时（`argus-skill 0.1.2`）** 与 **`math` Vertical（数学垂直领域插件）**、**命题账本/证明图校验器**、**Jacobian 适配器**、**注入规则（Special Prompts）** 以及 **集群调度脚本（Harness）** 完整打包在同一个公开仓库中，可直接安装、运行与对照参考。

- **顶层规格（权威）：**[`docs/MATH_SPEC.zh-CN.md`](docs/MATH_SPEC.zh-CN.md)。提示、campaign 契约和工具都从它派生；与它冲突时以它为准。
- [English README](README.md)
- 数学成果归档仓库（72 个结果包 + 独立论文 PDF）：<https://github.com/Argus-AiTeam/argus-mathematics>

---

## 1. 仓库内的核心模块直达入口

| 模块 | 路径 | 说明 |
|---|---|---|
| **`math` Vertical（核心）** | [`argus_skill/verticals/math/`](argus_skill/verticals/math/)（根目录镜像：[`math_vertical/`](math_vertical/)） | 实验实际运行的完整 `math` Vertical |
| ↳ 阶段状态机与硬门禁 | [`argus_skill/verticals/math/stages.py`](argus_skill/verticals/math/stages.py) | `scope` → `solve` → `review` 三阶段 Checklist 与 `stage_completion_issues` 硬门禁 |
| ↳ 命题与假设账本 | [`argus_skill/verticals/math/math_state.py`](argus_skill/verticals/math/math_state.py) | 维护与校验 `research/MATH_STATE.json`（Claim / Assumption / Route / Judgement） |
| ↳ 证明依赖图与 Gap 检查 | [`argus_skill/verticals/math/proof_graph.py`](argus_skill/verticals/math/proof_graph.py) · [`proof_graph_check.py`](argus_skill/verticals/math/proof_graph_check.py) | 维护与校验 `research/PROOF_GRAPH.json`，强制 targeted 目标 gap 为 0 |
| ↳ 原始文献引用核验 | [`argus_skill/verticals/math/citation_check.py`](argus_skill/verticals/math/citation_check.py) | 强制所有引用定理在 `review` 结项前完成原文核对与归属 |
| ↳ Lean 4 形式化证据核验 | [`argus_skill/verticals/math/lean_evidence.py`](argus_skill/verticals/math/lean_evidence.py) · [`lean_async.py`](argus_skill/verticals/math/lean_async.py) | Lean 4 编译回执校验、公理审计与 `sorryAx` 零容忍检查 |
| ↳ 角色 Prompts（Skills） | [`argus_skill/verticals/math/skills/`](argus_skill/verticals/math/skills/) | Manager / Planner / Engineer / Reviewer / Scientist 五角色数学科研指令 |
| **Proof Ledger 内核** | [`argus_skill/proof_ledger/`](argus_skill/proof_ledger/) | `math_state` 底层依赖的账本存储与状态推导内核 |
| **Jacobian MCP 适配器** | [`argus_skill/tools/jacobian.py`](argus_skill/tools/jacobian.py) | 连接 Jacobian `0.14.0` 精确符号/有理LP/SMT/整数矩阵算子的类型化适配器 |
| **終态与结项门禁** | [`argus_skill/life/terminal_state.py`](argus_skill/life/terminal_state.py) | 区分 `targeted` 与 `exploratory` 模式的终审结项判定 |
| **注入规则（Special Prompts）** | [`counterexample_special_prompts/`](counterexample_special_prompts/) | 运行时通过 `ARGUS_SKILL_SPECIAL_PROMPTS_DIR` 注入的 4 条反例搜索铁律 |
| **集群启动与监管脚本** | [`counterexample_harness/`](counterexample_harness/) | `launch_campaign_argus.py`、`supervise_argus_fleet.py` 及审计验证脚本 |

---

## 2. 冻结版本与分支对应关系

本仓库包含实验全周期使用的全部 3 个冻结版本分支：

1. **`main` 分支（默认，完整在线运行版）**
   - 对应服务器上 `/home/argustest/zimo/argus-live-update` 的最终完整状态，截至 2026-11-07（`feature/counterexample-lab-jacobian-update` @ `cad2bb44` + 工作区热修补丁 [`docs/live-runtime/working-tree-20261107.patch`](docs/live-runtime/working-tree-20261107.patch)；campaign 自进化出的 skill 放在 `counterexample_harness/shared_skills/`，不在 `argus_skill/` 里），并附带 `counterexample_harness/` 与 `counterexample_special_prompts/`。
2. **`feature/counterexample-lab-jacobian-update` 分支**
   - 2026 年 9 月 live 运行时（`60a7a2b6`）的快照线，之后同步到 2026-11-04。当前 live 的 HEAD 是 `cad2bb44`，其精确状态以 `main` 加上方补丁为准。
3. **`baseline-33da786` 分支**
   - 对应 `/home/argustest/zimo/argus-latest` 的固定基线版本（`33da786bbc6787a2eeb63a5f492498eae87c78c7`），实验中用于统一 pinned 账本校验。
   - 对比基线版与完整运行版的全部代码改动：<https://github.com/Argus-AiTeam/argus-counterexample-runtime/compare/baseline-33da786...main>

---

## 3. 快速安装与使用

```bash
git clone https://github.com/Argus-AiTeam/argus-counterexample-runtime.git
cd argus-counterexample-runtime
python3 -m venv .venv
.venv/bin/pip install -e .
```

### 运行 `math` Vertical 的四个核心检查器

```bash
# 1. 校验数学命题与假设账本 (research/MATH_STATE.json)
.venv/bin/python -m argus_skill.verticals.math.math_state check --project-root <CAMPAIGN_DIR>

# 2. 校验有向证明图完整性 (research/PROOF_GRAPH.json)
.venv/bin/python -m argus_skill.verticals.math.proof_graph_check check --project-root <CAMPAIGN_DIR>

# 3. 检查距离目标命题的未证 Gap
.venv/bin/python -m argus_skill.verticals.math.proof_graph_check gap --project-root <CAMPAIGN_DIR>

# 4. 检查文献引用核对状态
.venv/bin/python -m argus_skill.verticals.math.citation_check status --project-root <CAMPAIGN_DIR>
```

### 启动单个反例战役 Daemon

```bash
export ARGUS_SKILL_VERTICAL=math
export ARGUS_SKILL_SPECIAL_PROMPTS_DIR="$(pwd)/counterexample_special_prompts"
.venv/bin/argus --daemon --continuous --objective-file LAUNCH.md --bounded --mission-width 1
```
