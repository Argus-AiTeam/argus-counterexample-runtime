---
title: "Amortized prime-path supercritical cutoff"
description: "At R_L=3^L, the complete retained-main versus absolute-tail comparison reduces to a stronger unresolved inequality between genuine prime-path masses."
---

# Amortized prime-path supercritical cutoff

In the reviewed \(D=4\) all-word domain, retain every square-divisor
coordinate and exactly the von Mangoldt divisors \(d_j\leq R_L=3^L\).
Partition genuine prime trajectories by whether their endpoint is at most
\(3^L\) or lies in \((3^L,4^L]\), and denote their positive log-weights by
\(G_L\) and \(H_L\).

If \(A_L\) is the total signed retained contribution of non-prime states
and \(B_L\) is their omitted termwise-absolute mass, the complete
statewise partition gives

\[
M_L=G_L+A_L,\qquad
E_L^{\mathrm{sgn}}=H_L-A_L,\qquad
E_L^{\mathrm{abs}}=H_L+B_L.
\]

For every non-prime state the full prime weight is zero, so its omitted
signed term is the negative of its retained term and its omitted absolute
mass is at least the retained magnitude.  Hence \(B_L-A_L\geq0\) and

\[
M_L-E_L^{\mathrm{abs}}
=G_L-H_L-(B_L-A_L)
\leq G_L-H_L.
\]

Therefore \(M_L>E_L^{\mathrm{abs}}\) already requires the stronger
genuine-prime assertion \(G_L>H_L\), in particular \(G_L>0\).  Composite
artifacts cannot furnish a primality-independent positive main term:
nonabsolute regrouping cancels them exactly and recovers
\(W_L(4)=G_L+H_L\).

This is a uniform algebraic reduction, not a finite numerical
observation.  It rules out only the cutoff \(R_L=3^L\) as an independent
retained-main versus termwise-absolute-tail mechanism.  It does not rule
out unbounded \(D=4\) positivity, an independent estimate for the genuine
prime masses, or a materially different nonabsolute organization.

The proof and exact replay are in
`research/amortized_prime_path_supercritical_cutoff/`.
