# AK(3) depth-three arbitrary-\(K\) atlas

## Exact result

For every

\[
K\in\operatorname{GL}_2(\mathbb Z),\qquad
\max_{i,j}|K_{ij}|\leq4,
\]

the complete unrestricted \(S_2\) Laurent fiber of the normalized
AK(3) cell

\[
G_2,\ H,\ K,\ I
\]

has no lift to \(S_3\). The exclusion covers all eight ordered
component patterns, all five relation-cycle freedoms, all terminal
axis powers, and arbitrary finite Laurent support.

This finite-height theorem has passed independent replay. It is not
an arbitrary-\(K\) theorem and not an Andrews--Curtis counterexample.

## Atlas

Exact signed-basis canonicalization partitions the 360 unimodular
matrices in the height-four box into 45 cell keys. Four previously
reviewed keys are reused without regenerating their certificates:
the \(G_2\) return loop and the cells represented by \(K_0,K_1,K_*\).

For each of the other 41 keys, an actual free Nielsen lift and exact
inverse are used to construct four necessary first-jet equations over
\(\mathbb F_3\). Every distinct component-pattern system is exhausted
over all \(3^8=6561\) assignments. Thirty-seven keys have no common
zero.

Exactly four keys survive the jet filter:

| Cell | Representative \(K\) | Common zeros |
|---|---|---:|
| 32 | \(\left(\begin{smallmatrix}-3&-1\\-1&0\end{smallmatrix}\right)\) | 243 |
| 34 | \(\left(\begin{smallmatrix}-2&-1\\-1&0\end{smallmatrix}\right)\) | 486 |
| 44 | \(\left(\begin{smallmatrix}-3&1\\-1&0\end{smallmatrix}\right)\) | 243 |
| 45 | \(\left(\begin{smallmatrix}-4&1\\-1&0\end{smallmatrix}\right)\) | 486 |

A jet survivor is only a necessary local solution, not an \(S_3\)
lift.

## Shared cyclotomic exclusion

Substitution of the complete \(S_2\) fiber into the original AK(3)
words gives a nine-coefficient first residual for each survivor. At
\(A=B=t\), where \(t\) is a primitive seventh root, exact arithmetic
shows that all four residuals become literally the same Hermitian
quadratic form after the same nonzero multiplier.

With \(s=t+t^{-1}\) in the isolated real embedding

\[
-\frac{223}{500}<s<-\frac{89}{200},
\]

the leading minor, determinant, and completed-square numerator are

\[
13+33s+17s^2,\qquad
-56-175s-91s^2,\qquad
-1583-4318s-1703s^2.
\]

Exact rational endpoint bounds make all three strictly positive.
The completed square is therefore positive for every pair of complex
values of the two arbitrary Laurent parameters. The third arbitrary
parameter is absent from this residual, so none of the four survivor
cells lifts.

Original-word replays separately cover every relation-cycle column,
terminal conjugator, and component pattern. The augmentation-ideal
argument makes the replay independent of the chosen fiber point, and
terminal powers act only by Laurent units.

## Evidence and boundary

The main proof is
[`HEIGHT_FOUR_THEOREM.md`](../../../../../research/experiments/ak3-depth-three-arbitrary-k-atlas/HEIGHT_FOUR_THEOREM.md).
The completed partition and systems are in
`integral-cell-search-height-4-completed.json`; the shared exact
certificate is in
`remaining-survivor-cyclotomic-obstruction.json`. The aggregate
`height-four-boundary-certificate.json` freshly replays the 45-key
partition, every free lift, and all 269001 stored first-jet
assignments before checking survivor-certificate coverage.

Matrices of height at least five remain unresolved. A finite atlas
cannot by itself establish a congruence period or a universal
arbitrary-\(K\) exclusion.
