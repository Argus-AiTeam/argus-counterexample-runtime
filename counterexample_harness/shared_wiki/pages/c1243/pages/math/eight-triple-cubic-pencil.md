---
title: Eight-triple-point Lucas cubic pencil
description: Exact incidence, fixed component, and discriminant locus of the cubic pencil through all eight branch-line triple points.
---

# Eight-triple-point Lucas cubic pencil

In Lucas coordinates `[e:x:y]`, the nine entry lines are the zero loci of

```text
e+x, e-x-y, e+y, e-x+y, e, e+x-y, e-y, e+x+y, e-x.
```

Their pairwise incidence consists of twelve double points and eight triple
points. Four triple points, `[0:0:1]`, `[0:1:-1]`, `[0:1:0]`, and
`[0:1:1]`, lie on the central-entry line `e=0`.

The evaluation matrix of homogeneous cubics at all eight triple points has
rank 8 and kernel

```text
span(e*x*y, e*(-e^2+x^2+y^2)).
```

Thus the complete cubic pencil is

```text
e*(u*x*y+v*(x^2+y^2-e^2)).
```

The line `e=0` is a fixed component, so every member is reducible and
singular over the algebraic closure. The classical cubic discriminant is
identically zero, with discriminant locus all of `P^1`. The residual conic
is singular only at `[u:v]=[1:0],[2:1],[-2:1]`; those members factor as
`e*x*y`, `-E*B*H`, and `-E*D*F`, respectively.

There are no irreducible rational singular members, so this pencil has no
eligible normalization or complete nine-root pullback. This is an exact
obstruction to this pencil only, not to cubic images generally and not to
the existence of a square magic square.
