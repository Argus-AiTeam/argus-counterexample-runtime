---
name: "Campaign-Local Proof Gap Check"
description: "Run and interpret proof-graph gap checks for one campaign without accidentally selecting a repository-level graph."
---

# Campaign-Local Proof Gap Check

When a Manager decision depends on `research/PROOF_GRAPH.json`:

1. Run the authoritative math-state check with the dataset root required by
   the project contract.
2. Run `proof_graph_check gap` with the individual campaign directory as
   `--project-root`, not the multi-campaign dataset root.
3. Confirm the reported goal belongs to the intended campaign before using
   the listed readable proposition statements as stage evidence.
4. Treat a clean structural check as validation of the graph format, not as
   proof that the campaign objective or any listed open proposition is solved.
5. For a bounded route result, identify the exact proposition whose status
   changed. A refuted non-goal candidate can justify advancing that bounded
   result to review even when the goal gap is unchanged; keep the campaign
   objective open and do not mistake route exhaustion for completion.
