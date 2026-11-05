---
title: Characteristic-five R(2) Quinn boundary
description: Exact Adams-operation obstruction to a symmetric stable autonomous categorification of R(2), with all rank and Verlinde-fiber branches.
---

# Characteristic-five \(R(2)\) Quinn boundary

No finite split semisimple symmetric stable autonomous tensor category in
characteristic five has fusion ring
\[
\alpha^2=1,\qquad \rho^2=1+2\rho+2\alpha\rho.
\]
Therefore this branch supplies no Bobtcheva \(Q\)-values on AK(3), unequal or
otherwise.

There are exactly three nonzero categorical-rank homomorphisms:
\[
(1,1,2,2),\quad(1,-1,1,-1),\quad(1,-1,-1,1).
\]
Writing
\[
K_0(\operatorname{Ver}_5)
=\mathbb Z[g,x]/(g^2-1,x^2-1-x),
\]
the corresponding positive fiber-ring maps are exactly
\[
\begin{array}{c|c}
F(\alpha)&F(\rho)\\ \hline
1&1+2x\\
g&1+x+gx\\
g&g+x+gx.
\end{array}
\]

The rational fusion algebra is
\[
R(2)_{\mathbb Q}\cong\mathbb Q(\sqrt5)\oplus\mathbb Q\oplus\mathbb Q.
\]
Of its sixteen unital rational endomorphisms, eight preserve the integral
lattice, and only two satisfy the necessary Adams congruence
\(\psi_2(X)\equiv X^2\pmod2\):
\[
\psi_2(\alpha)=-1,\qquad\psi_2(\rho)=\pm1.
\]
Both are idempotent. Czenky's
arXiv:`2211.13631v3`, Corollary `tannakian`, then forces the category to be
super-Tannakian. A fiber functor to `sVec` makes Frobenius--Perron dimensions
positive integers, contradicting
\[
\operatorname{FPdim}(\rho)=2+\sqrt5.
\]
The all-even Verlinde image is independently incompatible with Adams on
\(\alpha\), while the two mixed images are precisely the two idempotent
branches just excluded.

The same experiment supplies a direct normal-closure certificate for
\[
\operatorname{AK}(3)=
\langle a,b\mid a^3b^{-4},\,aba\,b^{-1}a^{-1}b^{-1}\rangle.
\]
The stored products of relator conjugates freely reduce to \(a\) and \(b\)
under two opposite contraction schedules. This proves presentation
triviality, not Andrews--Curtis equivalence.

The exact proof, explicit factor table, source scope, Jacobian typed replay,
and verifier are in
`research/experiments/quinn-2d2-char5-separator/`.
