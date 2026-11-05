---
title: Bouchard IPA Schinzel-Dickson Cunningham carrier boundary
description: Finite CRT compatibility survives, but the maximal-carrier theorem assumes nonempty realization and gives no growing-length bound.
---

The complete public dependency chain is available on Zenodo:

| Role | DOI | Exact contract |
|---|---|---|
| IPA rule | `10.5281/zenodo.21747414` | Preserves a property after its generating mechanism is established. |
| Local presence | `10.5281/zenodo.21562296` | A global target requiring a mechanism must have a local occurrence carrying it. |
| Maximal carrier | `10.5281/zenodo.21776401` | Theorem 3.1 asserts maximal compatible realization; Theorem 5.1 uses `Cmax` to infer existence. |
| Prime-pair specialization | `10.5281/zenodo.21812612` | Imports Erdos-66 maximality and Beal local presence. |
| Every-tail specialization | `10.5281/zenodo.21813243` | Imports Erdos-66, Beal, and Goldbach. |
| Dickson | `10.5281/zenodo.21779684` | Equation (48) imports the preceding chain into Theorems 8.1-8.2. |
| Schinzel H | `10.5281/zenodo.21779680` | Section 6.2 imports Dickson into Theorems 7.1-7.2. |

Erdos-66 Theorem 3.1 is the first unsupported implication. Prime
factorization represents an integer after it is chosen, and a complete carrier
can contain every compatible realization that exists, but neither fact proves
that the set of compatible realizations is nonempty. Theorem 5.1 then treats
the asserted `Cmax` as a nonempty realization and derives existence from it.
IPA and the Beal lemma are preservation and non-creation implications; they do
not supply the missing existence premise.

The one-form model \(L(n)=n\) isolates the quantifier failure. It has
\[
c_p=p-1,\qquad \kappa_p=1,
\]
and every finite prime set \(Q\) has arbitrarily large survivors
\[
n\equiv1\pmod{\prod_{p\in Q}p}.
\]
Nevertheless no \(n>1\) survives every local corrector, because a prime divisor
\(r\mid n\) makes \(S_r(n)=0\). The printed primality detector is a different
predicate: for prime \(n=13\),
\[
D(13)=\prod_{p<13}S_p(13)=1,\qquad S_{13}(13)=0.
\]
Its value-dependent proper-divisor cutoff is therefore not the common closure
of all \(S_p\).

For the Cunningham forms
\[
F_j(n)=2^j(n-1)+1,
\]
the recurrence \(F_{j+1}=2F_j-1\), strict growth for \(n>1\), and local
admissibility are exact. For odd \(p\), the number of forbidden residues is
\(\min\{L,\operatorname{ord}_p(2)\}<p\), while it is one at \(p=2\). If
\(n\le A^L\), then \(F_{L-1}(n)<(2A)^L\). None of the audited sources gives an
upper bound for the first realization that is uniform as \(L\) grows, so even
their claimed qualitative fixed-family infinitude would not yield one fixed
\(A\).

This retires only the available Bouchard IPA carrier specialization. It does
not refute Dickson's conjecture, Schinzel's Hypothesis H, Cunningham-row
existence, or the Erdos target.
