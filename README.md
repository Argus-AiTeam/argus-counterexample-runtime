# Argus Counterexample Runtime (Frozen Argus + `math` Vertical Unified Repository)

This repository packages the exact **frozen Argus runtime (`argus-skill 0.1.2`)** together with the **`math` vertical**, **claim-ledger / proof-graph checkers**, **Jacobian MCP adapter**, **injected special prompts**, and **fleet supervision harness** used in the **Argus Live Counterexample Lab** campaigns (August–September 2026) in a single unified repository.

- [中文说明 (Chinese README)](README.zh-CN.md)
- Public mathematical results archive (72 result packages + standalone AMS LaTeX papers): <https://github.com/Argus-AiTeam/argus-mathematics>

---

## 1. Key Components in This Repository

| Component | Path | Purpose |
|---|---|---|
| **`math` Vertical (Core)** | [`argus_skill/verticals/math/`](argus_skill/verticals/math/) (root mirror: [`math_vertical/`](math_vertical/)) | Complete `math` vertical executed by the counterexample campaigns |
| ↳ Stage Machine & Gates | [`argus_skill/verticals/math/stages.py`](argus_skill/verticals/math/stages.py) | `scope` → `solve` → `review` checklists and deterministic `stage_completion_issues` gates |
| ↳ Mathematical Claim Ledger | [`argus_skill/verticals/math/math_state.py`](argus_skill/verticals/math/math_state.py) | CLI & validator for `research/MATH_STATE.json` (claims, assumptions, routes, judgements) |
| ↳ Proof Dependency Graph | [`argus_skill/verticals/math/proof_graph.py`](argus_skill/verticals/math/proof_graph.py) · [`proof_graph_check.py`](argus_skill/verticals/math/proof_graph_check.py) | Validator & gap analyzer for `research/PROOF_GRAPH.json` |
| ↳ Primary-Source Citation Gate | [`argus_skill/verticals/math/citation_check.py`](argus_skill/verticals/math/citation_check.py) | Enforces primary-source lookup and proposition attribution before `review` completion |
| ↳ Lean 4 Evidence Gate | [`argus_skill/verticals/math/lean_evidence.py`](argus_skill/verticals/math/lean_evidence.py) · [`lean_async.py`](argus_skill/verticals/math/lean_async.py) | Hash-bound Lean 4 compilation receipt and zero-`sorryAx` verifier |
| ↳ Role Skill Prompts | [`argus_skill/verticals/math/skills/`](argus_skill/verticals/math/skills/) | Markdown role skills for Manager, Planner, Engineer, Reviewer, and Scientist |
| **Proof Ledger Kernel** | [`argus_skill/proof_ledger/`](argus_skill/proof_ledger/) | Underlying store and status derivation kernel for `math_state` |
| **Jacobian MCP Adapter** | [`argus_skill/tools/jacobian.py`](argus_skill/tools/jacobian.py) | Typed adapter connecting Argus to Jacobian `0.14.0` exact symbolic/LP/SMT/matrix operations |
| **Terminal State Gate** | [`argus_skill/life/terminal_state.py`](argus_skill/life/terminal_state.py) | Terminal settlement rules for `targeted` vs. `exploratory` math missions |
| **Special Prompts** | [`counterexample_special_prompts/`](counterexample_special_prompts/) | 4 operator prompt rules injected via `ARGUS_SKILL_SPECIAL_PROMPTS_DIR` |
| **Fleet Launch & Supervision** | [`counterexample_harness/`](counterexample_harness/) | `launch_campaign_argus.py`, `supervise_argus_fleet.py`, and catalog validators |

---

## 2. Frozen Branches in This Repository

1. **`main` (Default — Complete Live Runtime + Vertical + Harness)**
   - Exact snapshot of `/home/argustest/zimo/argus-live-update` (`feature/counterexample-lab-jacobian-update` @ `60a7a2b6` + the 10 live working-tree patches) together with `math_vertical/`, `counterexample_special_prompts/`, and `counterexample_harness/`.
2. **`feature/counterexample-lab-jacobian-update`**
   - Clean Git HEAD (`60a7a2b6`) of `/home/argustest/zimo/argus-live-update`.
3. **`baseline-33da786`**
   - Exact frozen baseline snapshot (`33da786bbc6787a2eeb63a5f492498eae87c78c7`) from `/home/argustest/zimo/argus-latest`.
   - Full diff from `baseline-33da786` to `main`: <https://github.com/Argus-AiTeam/argus-counterexample-runtime/compare/baseline-33da786...main>

---

## 3. Installation & Usage

```bash
git clone https://github.com/Argus-AiTeam/argus-counterexample-runtime.git
cd argus-counterexample-runtime
python3 -m venv .venv
.venv/bin/pip install -e .
```

### Run the `math` Vertical Verifiers

```bash
.venv/bin/python -m argus_skill.verticals.math.math_state check --project-root <CAMPAIGN_DIR>
.venv/bin/python -m argus_skill.verticals.math.proof_graph_check check --project-root <CAMPAIGN_DIR>
.venv/bin/python -m argus_skill.verticals.math.proof_graph_check gap --project-root <CAMPAIGN_DIR>
.venv/bin/python -m argus_skill.verticals.math.citation_check status --project-root <CAMPAIGN_DIR>
```
