---
title: Diagonal-symmetric one-corner exclusion
description: Exact zero-frontier certificate for the preregistered diagonal-symmetric one-corner family, pending independent review.
---

# Diagonal-symmetric one-corner exclusion

The bounded claim `OC2222_DIAGONAL_SYMMETRIC_COMPLETION` asks whether parameters
`0<a<1` and `0<b<c<1`, together with four unrestricted pairwise distinct
strict-interior points, can complete
`S(a,b,c)={(0,0),(a,0),(1,b),(1,c),(b,1),(c,1),(0,a)}` while making all 165
absolute doubled triangle determinants strictly greater than `2/27`.

`research/global/one_corner_balanced_2222/diagonal_symmetric_completion/parameter_cell_pass_192grid.json`
is an exact parameter-first exclusion certificate. Its standalone replay
regenerates the full `32^3` base-cell inventory as 15,872 outside-domain cells,
14,460 boundary-blocked cells, 260 exact splits, and 4,256 completion leaves.
It retains all topology-transition and coordinate-tie strata, checks the
24-label quotient, represents all 165 determinant constraints, and has zero
uncovered frontier.

The Engineer replay exited 0 with `ok=true`, `complete=true`, and
`uncovered_frontier=0`. Independent Reviewer replay is still required. This
excludes only the diagonal-symmetric family; the global counterexample claim
`C1` remains open.

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/one_corner_diagonal_symmetric_completion.py check \
  --certificate research/global/one_corner_balanced_2222/diagonal_symmetric_completion/parameter_cell_pass_192grid.json
```
