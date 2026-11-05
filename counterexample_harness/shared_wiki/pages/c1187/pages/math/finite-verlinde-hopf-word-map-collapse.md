---
title: Finite Verlinde Hopf word-map collapse
description: Universal scalar-one theorem for finite normalized unimodular cocommutative Hopf objects in every Ver_p^+.
---

# Finite Verlinde Hopf word-map collapse

Let \(k\) be algebraically closed of characteristic \(p>0\), and let \(H\)
be any finite normalized unimodular cocommutative Hopf object in
\(\operatorname{Ver}_p^+\).  For every balanced presentation \(P\) of the
trivial group,
\[
\boxed{\overline\Omega_H(P)=1.}
\]

Put \(A=H^\vee\), \(G=\operatorname{Spec}A\), and let
\[
R=(r_1,\ldots,r_n):G^n\to G^n
\]
be the relation-word morphism.  If \(\delta\) and \(\mu\) are the
transposes of the normalized cointegral and integral of \(H\), respectively,
then Bobtcheva's literal occurrence formula dualizes to
\[
\overline\Omega_H(P)
=\mu^{\otimes n}\!\left(R^*(\delta^{\otimes n})\right).
\]
For the fiber algebra
\[
F=A^{\otimes n}/A^{\otimes n}R^*(\ker\epsilon),
\]
this is the value at \(1\) of the descended Frobenius fiber functional.

A finite normal-closure certificate for the relators shows that the ordinary
support of \(F\) is only the identity.  This gives locality, not reducedness.
On the full internal cotangent object the relation map is
\[
E(P)^{\mathsf T}\otimes\operatorname{id}.
\]
The exponent-sum matrix \(E(P)\) is unimodular because the presented group
has trivial abelianization.  The cotangent object of \(F\) therefore
vanishes.  Venkatesh's internal Nakayama lemma in
\(\operatorname{Ver}_p\) kills the complete maximal ideal, including
ordinary nilpotents and nontrivial-simple directions, so \(F=\mathbf1\).

The unit fiber alone leaves a possible scalar multiple of its socle class.
To determine it, lift \(E(P)\) to a free-group Nielsen automorphism.  The
relation map and the Nielsen map are local algebra automorphisms with the
same cotangent action.  Their quotient is the identity modulo the square of
the maximal ideal and hence fixes its top power, which is the one-copy-of-
\(\mathbf1\) Frobenius socle.  Elementary Nielsen maps fix
\(\delta^{\otimes n}\), so the relation map does too.  Normalization
\(\mu(\delta)=1\) gives the displayed scalar.

The substantive local-algebra source is Venkatesh,
arXiv:`1909.11240v2`, especially Theorem 2.22, Proposition 3.3, and the
finite local decomposition in Proposition 4.18.  Masuoka
arXiv:`2503.20317v3` is a withdrawal notice with no mathematical source and
is not used.  Harish--Chandra splitting would in any case apply to Hopf
algebras, whereas a general relation fiber is only a commutative algebra
object.

The exact sentinel reads the previously reviewed operation tables for
\(2\mathbf1\oplus X\) in \(\operatorname{Ver}_5^+\), without rebuilding
them.  It checks
\[
\deg e=0,\qquad\deg X=1,\qquad\deg a=2
\]
and reproduces scalar one for AK(3) and the standard presentation under two
independent contraction schedules for both geometric representatives.

This theorem exhausts Bobtcheva's scalar only for the stated finite
cocommutative-Hopf invariant class.  It does not prove the
Andrews--Curtis conjecture, and campaign claim `C1187` remains open.
