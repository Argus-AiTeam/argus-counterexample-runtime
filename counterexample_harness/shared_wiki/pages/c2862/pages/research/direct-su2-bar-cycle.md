---
title: Direct SU(2) bar-cycle rigidity
description: Fixed finite bar templates have locally constant complete Chern--Simons value along representation arcs; only locally constant controlling angles remain viable.
---

# Direct SU(2) bar-cycle rigidity

Let `Gamma` be a fixed finitely presented group and

```text
z = sum_i n_i [g_i|h_i|k_i] in Z_3(Gamma; Z)
```

a fixed finite normalized left bar cycle. For every smooth path
`rho_t: Gamma -> SU(2)`, Dupont's Cheeger--Chern--Simons rigidity theorem
and the closed-flat variation formula give

```text
<C_2-hat, (rho_t)_* z>
  = Vol_S3(sigma (rho_t)_* z)/(2*pi^2) in R/Z
```

independently of `t`. If all retained spherical tetrahedra remain
nondegenerate and their oriented volumes are lifted continuously, the
complete real sum is constant as well, so its Schlaefli derivative is
exactly zero.

Consequently, one fixed face-pairing template cannot have a varying
algebraic angle and a nonconstant polynomial for its **complete** normalized
volume. A nonzero derivative identifies an incomplete local sum, a failed
bar boundary, changing relations or pairings, a boundary contribution, or a
degeneracy/branch crossing.

This does not prove rationality. A direct witness can still exist when its
controlling non-root-of-unity angle is locally constant on the representation
component; an isolated representation is sufficient but not necessary. The
absolute complete value must then be evaluated and proved irrational modulo
integers.

If all boundary cancellations are universal free-word identities, there is
an earlier obstruction: `H_3(F_m; Z)=0`, so the cycle is a bar boundary and
its regulator is zero. Noncommutativity, non-join geometry, and
nondegeneracy do not by themselves prevent this.

The complete proof and exact negative control are in
`research/DIRECT_SU2_BAR_CYCLE.md` and
`research/verify_direct_su2_bar_cycle.py`.
