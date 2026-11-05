# Cubed-mixed ordinary Bloch class

The complete reviewed 194-term `SL_2(F)` bar cycle now has an explicit
ordinary cross-ratio image over

```text
F=Q(r,s,t),
r^6-4r^4+5r^2-1=0,
(1-3r^2+r^4)s^4-(1+2r^4)s^2+4r^2-3r^4=0,
t^2=r^2-4.
```

This field has degree 48 and signature `(0,24)`.  Seven simplices of
the original cycle have a repeated `[1:1]` projective vertex because
two cumulative matrices differ by the central sign.  Dupont--Zickert
Section 1.3 defines the ordinary cross-ratio on the full configuration
complex by sending exactly these repeated tuples to zero.  An exact
52-pattern degenerate-five-point check proves that this is a chain map.
The other 187 terms, with unchanged coefficients and exact
cross-ratios, are the previous chain `beta0`.

```text
h=[[1,0],[1,1]],  h infinity=[1:1]
```

binds the source's standard infinity map to this basepoint.  The
explicit right-translation prism proves that the resulting inner
conjugation induces the identity on homology.  Thus `beta0` is the
image of the full 194-term class; the seven-term subset and its
complement need not be cycles.

The raw Dehn boundary of `beta0` has exactly fourteen
`(-1) wedge u` terms.  Hence `delta(2 beta0)=0`, and the corresponding
Suslin boundary in `S^2_Z(F^*)` also vanishes exactly.  Doubling the
reviewed 24 Borel balls leaves indices `0--7` strictly positive,
indices `16--23` strictly negative, and indices `8--15` containing
zero.  Therefore sixteen coordinates of `2 beta0` are rigorously
nonzero, so the original class has non-torsion Suslin Bloch image by
Neumann--Yang, Theorem 9.1.

An independent exact cross-check remains available: a 22-term
homogeneous four-chain identifies the original cycle with a 205-term
`[1:1]`-good cycle whose Dehn boundary vanishes before any
two-primary reduction.

This closes the ordinary-Bloch node but is not the campaign
counterexample.  The nonzero Borel coordinates occur at noncompact
Galois embeddings and do not prove that the physical compact `SU(2)`
Cheeger--Chern--Simons value is irrational in `R/Z`.

Full construction and replay:
[`CLOSED_SURFACE_CUBED_MIXED_BLOCH_GALOIS.md`](../../../../../research/CLOSED_SURFACE_CUBED_MIXED_BLOCH_GALOIS.md).
