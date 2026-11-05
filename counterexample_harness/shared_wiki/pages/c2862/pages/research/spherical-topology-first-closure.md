---
title: Spherical topology-first squared-twist boundary
description: Exact mapping-torus chain and all-parameter stable-relation obstruction for the first axis-mixed topology-first family.
---

# Spherical topology-first squared-twist boundary

Fix the closed genus-three surface

```text
<a,b,c,d,e,f | [a,b][c,d][e,f]=1>
```

and the nonperiodic mapping class `F(d)=dcc` fixing the other generators.
For the based lift `F'=Inn(c)oF`, the standard Fox/mapping-cone
fundamental cycle has 60 normalized terms and zero exact boundary.
With `a=h,b=k,c=g,t=q`, its local prism contains

```text
-[g|h|k] + [q|h|k],
```

so the new stable label participates in cancellation of the seed face
`[h|k]`.

The family has no `SU(2)` mapping-torus holonomy.  The stable relations
for `a,b` imply that `g^-1 q` centralizes both `h,k`.  Their exact
imaginary-axis Gram matrix is

```text
(1/25) * [[16,-6],[-6,16]]
```

with determinant `44/125`, so their common `SU(2)` centralizer is
`{I,-I}` and `q=+/-g`.  The stable `d` relation then forces `g^2=I`,
contradicting `Re(g^2)=-7/25`.

This is an all-parameter exclusion for this fixed squared-twist family,
not for other monodromies or seed placements.  The retained-spectrum,
local-rigidity, and complete-regulator gates are not reached, and no
Chern--Simons candidate is emitted.

The proof and replay are
`research/SPHERICAL_TOPOLOGY_FIRST_CLOSURE.md` and
`research/verify_spherical_topology_first_closure.py`.
