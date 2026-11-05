---
title: First-order Jordan growing-block boundary
description: Uniform obstruction for one affine Jordan quadratic character per simple-spectrum eigenrow.
---

Let \(U,V\) be arbitrary nonempty legal Jacobi--Perron words, let
\(Q=N(U)\) have simple spectrum, and write the full embedding recurrence
in a \(Q\)-eigenbasis as

\[
F_k=D^k S F_{k+1}.
\]

The complete genuine first-order Jordan class

\[
\operatorname{row}_i(F_k)
=(u_i+k v_i)r_i^k s_i^{\binom{k}{2}},
\qquad \text{some }v_i\ne0,
\]

is empty. This holds for all algebraic parameters, all compatible
Galois actions, and all legal \(U,V\); strict branch inequalities and
the marker are not needed for the contradiction.

Each row lies in a fixed plane. Applying the reverse recurrence to a
column annihilating that plane confines \(S^{-1}\), up to simultaneous
permutation, to an isolated \(2\times2\) block or a one-column
triangular support. In either support, a nonzero off-diagonal
two-row coupling yields

\[
s^2=xy,\qquad (s-x)(s-y)=0,
\]

where \(x\ne y\) are inverse eigenvalues of \(Q\). Exact elimination
gives

\[
xy(x-y)^2=0,
\]

contradicting nonzero simple-spectrum weights. Hence \(S\) is diagonal.
The resulting scalar row recurrence would require

\[
\frac{k+z+1}{k+z}=c t^k.
\]

Its consecutive quotient is constant only if \(t=1\), but then
\((k+z+2)(k+z)-(k+z+1)^2=-1\). Therefore every \(v_i\) vanishes.

The deterministic verifier is
`research/routes/jordan-mode-growing-block-lift/verify_jordan_mode_obstruction.py`.
The Jacobian evidence preserves operation
`polynomial.ideal.elimination.compute`, its exact payload and typed
`COMPUTED` output.

This is an exhausted construction class, not a Jacobi--Perron
counterexample and not a proof of the original periodicity conjecture.
Higher Jordan order, sums of modes, infinite-support lifts, and
arbitrary prescribed-word limit rays remain open.
