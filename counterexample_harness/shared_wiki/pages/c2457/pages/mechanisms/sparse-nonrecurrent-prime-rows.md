---
title: Sparse nonrecurrent prime rows
description: Sparse unbounded multipliers evade return obstructions but leave an unproved recursive-frontier prime-distribution input.
---

# Sparse nonrecurrent prime rows

For a prime row

\[
q_{i+1}=m_iq_i-1,\qquad q_L\le C^L,
\]

the exact telescoping identity implies
\(\sum_i\log m_i=O(L)\). This permits unbounded multipliers at sparse
positions, so periodic, uniformly recurrent, and regular finite-state return
theorems do not cover the mechanism.

That freedom does not remove simultaneous primality. If all but
\(s_L=o(L)\) edges use one fixed finite multiplier alphabet, deleting the
injury edges leaves a clean all-prime block of at least

\[
\left\lceil\frac{L-1-s_L}{s_L+1}\right\rceil
\]

edges. Its length tends to infinity. With baseline multiplier \(2\), these
are numerical Cunningham chains of the second kind; with any finite
baseline alphabet, every fixed window length forces one fixed affine word to
take all-prime values at infinitely many distinct starts.

Recent one-generation sources do not close this gap. Li
(`arXiv:2508.18285v3`) proves infinitely many genuine edges
\(r\mid P+1\) with \(r=P^+(P+1)>P^{0.679-\varepsilon}\). Cloitre
(`arXiv:2510.18891v3`) inventories the same negative-residue edges and proves
a density-one theorem for ambient LCM-recurrence indices. Neither theorem
puts the selected predecessor on a recursively certified frontier.

Gorodetsky's general Kubilius theorem (`arXiv:2608.14190v1`) makes the
application boundary explicit: the weighted discrepancy \(D_2\) is an input
encoding the level of distribution of the sampled variable. For a terminal
prime \(Q\) selected by all previous chain conditions, this input requires
uniform control of

\[
\frac{\#\{Q\text{ in the frontier}:Q\equiv-1\pmod d\}}
     {\#\{\text{frontier}\}},
\]

which no inspected theorem supplies in the growing-block,
fixed-exponential regime.

The route therefore ends at an unproved recursive-frontier
level-of-distribution lemma. It constructs no fixed-\(C\) family and does not
negate the Erdos divergence prediction.

