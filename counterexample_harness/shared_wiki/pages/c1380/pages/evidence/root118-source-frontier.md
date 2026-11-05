---
title: Root118 source frontier
description: Authoritative 175-leaf source inventory and reviewed exact reductions leaving 19 unresolved native leaves.
---

# Root118 source frontier

The authoritative source for the root118 unresolved frontier is
`research/global/three_corner_eight_insertion/joint_u5l3_root118/exact_upper0/certificate.json.gz`,
with SHA-256
`5110c81117b7519c0584d99e1caf36b75f9c33fbf045337dcb8ad15e017476f1`.
It has 177 unresolved-budget leaves. The adjacent uncompressed
`certificate.json` is an older, non-equivalent artifact and must not be used as
an unpacked substitute: its file SHA-256 is
`8924b28d35914a2633716251794c7bc43c5b75a400fc1376ac25359b0bba2907`,
while the SHA-256 of the authoritative gzip's decompressed bytes is
`7de434b2dcb10ab6cf1ba915b6a96c2101a41315fa7ed31095716a66bb6c0924`.

`research/global/three_corner_eight_insertion/joint_u5l3_root118/source_frontier_manifest.json`
is the deterministic compact projection of that source after removing exactly
the two independently reviewed joint-cell exclusions. It contains 175 open
leaves, each with its normalized four-token state, source child-index path,
partition and factor depths, boundary reason, and exact five-upper-area
product. It sorts by descending exact area product and then by state and source
path. Under that ranking, the next open leaf is source path `[3]` with state
`["upper:0", "upper:1", "upper:20", "upper:23"]` and exact product
`95367431640625/107946249863639334912`.

The manifest is provenance and route-selection data, not a counterexample or
an exclusion. Its deterministic replay is:

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/three_corner_joint_u5l3_next_projection.py \
  check-source-manifest \
  --artifact research/global/three_corner_eight_insertion/joint_u5l3_root118/source_frontier_manifest.json
```

## Reviewed paths [3] through [9]

Independent review accepted
`research/global/three_corner_eight_insertion/joint_u5l3_root118/path3_exact_decision/certificate.json.gz`
for path `[3]`. Its checker recomputes all eight closed domain triangles, all
165 original strict determinant constraints, 717 cover nodes, 170 complete
midpoint partitions, and zero uncovered frontier:

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/three_corner_joint_u5l3_path3.py check \
  --artifact research/global/three_corner_eight_insertion/joint_u5l3_root118/path3_exact_decision/certificate.json.gz
```

Independent review also accepted
`research/global/three_corner_eight_insertion/joint_u5l3_root118/rank1_sibling_union/certificate.json.gz`.
That aggregate certificate restores both labels of every off-diagonal
`p8,p9` domain pair and exactly excludes paths `[4]` through `[9]` with
77,111 cover nodes, 19,181 complete partitions, and zero frontier. These two
reviewed results remove exactly seven manifest leaves. They do not exclude
any other source leaf, TCS8, or C1.

Independent review subsequently replayed
`research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/leaf_covers/leaf_018.json.gz`.
Its single exact six-factor determinant stress enumerates all 729 endpoint
assignments and has maximum `2075/46656 < 2/27`; both label transports
preserve the complete 165-triple inventory. This removes native leaf 18 and
leaves 167 source leaves before the new screen.

## Path-[1] parent attempts

All 168 leaves present before the leaf-18 review descend from source child path
`[1]`. Their
four upper-factor triangles are factorwise contained in the common parent
state
`["upper:0", "upper:1", "upper:20", "upper:21"]`; every remaining
`p8,p9` pair is off-diagonal, so both labelings must still be retained.

The aggregate complete-eight-factor attempt at
`research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/parent_cover_attempt.json.gz`
is exact but incomplete. Its first bounded continuation had 637 nodes, 156
partitions, and 10 frontier cells. A second continuation produced 1,213 nodes
and 300 partitions but 15 frontier cells. This branch growth is not an
exclusion.

A materially different source-aligned `p4` closed-orientation route verified
an initial 137-node checkpoint with 37 frontier cells. A later 10,133-node
structure reduced its structural frontier only to 33 before exact replay was
interrupted; that file remains marked `mathematical_evidence=false` and is not
used as mathematical evidence. No exact witness or zero-frontier certificate
is recorded for the complete path-[1] parent, so
`TCS8_ROOT118_REMAINING_UNION`, TCS8, and C1 remain open.

## Native-root screen

`research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/root_screen/certificate.json.gz`
is an isolated exact screen of exactly the other 167 native source leaves. It
does not inherit either partial parent tree and performs zero source-domain
partitions. Every leaf receives the same ordered root tests: exact p4 and p3
finite-orientation tests, the best projected single-determinant bound, fixed
projected/six-factor/full-factor rational stresses, and an exact p7
finite-orientation test. Numerical LP values are discarded during stress
discovery; only rational supports are persisted, and every claimed stress
exclusion is recomputed over exact endpoint products.

The exact replay closes 141 new leaves, precisely ordinals 35 through 175.
The primary certificates are 134 p4 finite-orientation exclusions and seven
additional full-factor rational-stress exclusions. The full-factor stress test
also independently closes all 141, while the six-factor stress test closes 104.
Every exclusion retains both p8,p9 labelings and the original 165 determinant
indices. Independent Reviewer replay accepted all 141 exclusions, so the
reviewed root118 residual now consists of the 26 leaves below.

The residual manifest contains 26 unresolved leaves, ordinals 8 through 34
except reviewed leaf 18. It records two exact failed-mechanism clusters:

- ordinals 8 through 13 reach the p4 cell limit and the p7 cell limit;
- ordinals 14 through 34 except 18 reach the p4 cell limit, while all p7
  orientation pairs leave a nonempty closed sign cell.

In both clusters the projected direct bound and all three retained rational
stress candidates remain above `2/27`; the p3 test is skipped by its
preregistered depth gate. These are residual classifications, not witnesses,
route exclusions, or evidence that deeper certificates cannot exist.

The standalone replay is:

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/three_corner_joint_u5l3_remaining_union.py \
  check-root-screen \
  --artifact research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/root_screen/certificate.json.gz \
  --minimum-new-exclusions 1
```

## Shallow-cluster checkpoint

The bounded follow-up route targeted exactly source ordinals 8 through 14.
It refined every source factor shallower than depth three through all four
closed midpoint children. At each terminal it first applied exact necessary
determinant halfplanes: four sweeps using relaxations fixed on the complete
source triangles, followed by two adaptive sweeps. A terminal left open by
that contractor entered an uncapped partition of all 21 determinant signs for
`p3`, followed by exact rational coupled-stress tests.

This route did **not** produce a seven-leaf exclusion. The durable run completed
ordinals 8 through 11, comprising 1,600 terminal source cells, and retained 79
uncovered terminal cells. It was stopped with exit 143 after 1,559.8 seconds
while an ordinal-12 contractor underwent severe exact-denominator growth. No
complete `certificate.json.gz` was written, and these partial counts are not an
exclusion.

The first persisted exact residual is
`research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/shallow_cluster/first_exact_residual.json`.
For the leaf-8 descendant
`["upper:011","upper:132","upper:202","upper:210"]`, the source contractor
returns no empty domain. Complete branching of all 21 `p3` determinant signs
then leaves deterministic sign-cell index 63 as a nonempty closed rational
hexagon. The artifact is deliberately marked `complete=false` and
`mathematical_evidence=false`: it is neither an eleven-point witness nor proof
that the cell is feasible. It records the exact obstruction that retires this
contractor-plus-stress route.

Its bounded replay is:

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/three_corner_joint_u5l3_remaining_union.py \
  check-shallow-residual \
  --artifact research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/shallow_cluster/first_exact_residual.json
```

### Exact decision of leaf-8 cell 63

The residual polygon is only a relaxation of its recorded 21-orientation
branch, not a feasibility result. The exact follow-up adds the seven omitted
`p3`-`p7` determinant orientations. Branching both signs by exact necessary
halfplanes leaves four closed rational subcells. On each subcell, a positive
rational stress combines the 56 absolute determinants among
`p0,p1,p2,p6,p7,p8,p9,p10` with all 28 signed determinants involving `p3`.
The weights sum to one, while exact evaluation on all 243 source endpoint
assignments and every `p3` polygon vertex gives a maximum at most `2/27`.
Thus the selected 84 strict inequalities are inconsistent, which excludes the
full eleven-point cell independently of `p4` and `p5`.

The exact certificate is
`research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/shallow_cluster/cell63_exact_certificate.json.gz`.
Its standalone replay is:

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/three_corner_joint_u5l3_remaining_union.py \
  check-cell63-exact \
  --artifact research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/shallow_cluster/cell63_exact_certificate.json.gz
```

This exact result excludes only leaf-8 cell 63. It does not by itself exclude
the other shallow sign cells or any entire source leaf.

### Complete exact exclusion of source ordinals 8 through 14

The cell-63 mechanism was extended without treating any solver result as
evidence. Four fixed-domain contractor sweeps close a terminal source cell only
on an exact empty determinant range or exact empty forced-sign domain.
Remaining cells branch all 21 original `p3` signs and, where needed, all seven
`p3`-`p7` signs. A failed 84-column stress triggers a complete local midpoint
partition of `p10` through depth at most four; every retained `p10` leaf must
have its own positive rational stress with exact maximum at most `2/27`.

The final certificate covers all seven source leaves and both `p8,p9` label
transports. Pinned replay verifies 4,936 terminal source cells, 49,952 initial
`p3` sign cells, 4,220 source-contractor exclusions, 48,126 projected stress
cells, 3,842 `p7`-extended or `p10`-refined stress leaves, 1,041 deduplicated
rational stress definitions, and zero uncovered frontier.

The certificate is
`research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/shallow_cluster/certificate.json.gz`.
Its acceptance replay is:

```bash
/home/argustest/zimo/argus-latest/.venv/bin/python \
  scripts/three_corner_joint_u5l3_remaining_union.py \
  check-shallow-cluster \
  --artifact research/global/three_corner_eight_insertion/joint_u5l3_root118/remaining_union/shallow_cluster/certificate.json.gz
```

Engineer evidence and independent Reviewer replay therefore refute exactly the
seven-leaf existence claim. Together with the previously reviewed path, leaf-18,
and native-root exclusions, the reviewed root118 residual is exactly the 19
source ordinals 15 through 34 except 18. Those 19 leaves, TCS8, and C1 remain
open.
