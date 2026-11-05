---
title: AK(3) 3-thickenability boundary
description: Exact occurrence-level Neuwirth obstruction and the resulting limit of Lackenby's ordinary-AC theorem.
---

For the exact presentation

\[
AK(3)=\langle a,b\mid a^3b^{-4},\;
abab^{-1}a^{-1}b^{-1}\rangle,
\]

the presentation 2-complex is **not thickenable** in a PL 3-manifold.

The occurrence-labelled signed link has four germs
\(a+,a-,b+,b-\), degrees \(6,6,7,7\), and thirteen corner edges. Its
underlying simple graph is \(K_4\), so abstract Whitehead-graph planarity
passes. The full criterion also pairs the two corner darts bordering every
one of the thirteen signed letter occurrences.

Choose cyclic orders at \(a+\) and \(b+\). There are
\((6-1)!(7-1)!=86400\) choices, and an edge-pairing sign uniquely determines
the orders at \(a-\) and \(b-\). All four sign choices therefore give
345600 exact rotation systems. For each system, the cycles of
\(\rho\alpha\) are its faces. A spherical link requires

\[
F=2-V+E=2-4+13=11.
\]

No system reaches eleven faces. The maximum is nine over all signs and seven
when both generator-end orders are opposite, as required in an orientable
thickening. The two attaching discs additionally force both edge twists to
zero: their mod-two occurrence rows are \((1,0)\) and \((1,1)\).

Lackenby, arXiv:2606.06122v1, Theorem 1.3 proves that a **thickenable**
balanced presentation of the trivial group is ordinary fixed-rank
Andrews--Curtis equivalent to the standard presentation. Its moves (0)--(3)
generate the campaign AC1--AC3 relation; stabilization move (4) is not used.
AK(3) fails the theorem's thickenability premise, so this theorem gives no
ordinary AC conclusion for AK(3) in either direction.

The replayable incidence tables, all face-count distributions, and source
archive are in `research/experiments/ak3-thickenability/`.

