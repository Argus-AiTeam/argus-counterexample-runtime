---
title: AK(3) cyclic AC boundary
description: Why exact small-overlap and singleton-turn conditions do not survive unrestricted Ivanov CT2.
---

For cyclically reduced rank-two balanced presentations of the trivial group,
Ivanov's Theorem 1.1 (arXiv:1606.08196v1) makes CEN-triviality equivalent to
ordinary AC-triviality. The lower-rank hypothesis is automatic in rank one.
Thus a CEN-closed separator for AK(3) would be a valid standard
Andrews-Curtis obstruction.

For
\[
U=a^3b^{-4},\qquad V=abab^{-1}a^{-1}b^{-1},
\]
the longest common cyclic factor over all independent orientations has length
two. This blocks only Ivanov's stricter complete-cancellation operation
(CCT2). It does not block unrestricted (CT2): \(UV\) is already cyclically
reduced, so
\[
(UV^k,V)\longmapsto(UV^{k+1},V)
\]
is a legal zero-cancellation CT2 move for every \(k\geq0\). From \(k=1\)
the entire word \(V\) is common to both components, so the small-overlap
condition is not closed.

Unsigned letter incidence also gives no separator. Every CT2 output \(Z\)
satisfies
\[
N_x(Z)=N_x(X)+N_x(Y)-2\kappa_x,
\]
where \(\kappa_x\) counts cancelled inverse \(x\)-pairs, including cyclic
cancellation. Parity therefore survives, but its row determinant is one for
both AK(3) and the standard basis.

The stronger condition that no component contain a basis letter exactly once
contains AK(3) and excludes the basis, but is not CT2-closed. For
\[
P_m=(bab^{-1}a^{-1})^m,\quad
U_m=aP_m^{-1},\quad V_m=P_mb,
\]
the balanced presentation \(\langle a,b\mid U_m,V_m\rangle\) is trivial and
both inputs have at least \(2m\) occurrences of each basis letter. Yet the
unrestricted partial-cancellation move sends \(U_m\) to \(ab\), which has one
occurrence of each. Since both input lengths are \(4m+1\) while the output
length is two, this move is not CCT2.

No CEN reduction or CEN-closed separator for AK(3) follows. The exact boundary
retires only local cyclic-overlap and singleton-turn attacks; AK(3)'s standard
AC status remains open.
