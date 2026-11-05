---
title: "Terminal-index Type-II feedback"
description: "The exact endpoint-slack recurrence factors the actual terminal candidate, but fixed block lengths have zero-kernel prime rows at every sufficiently large geometric height."
---

# Terminal-index Type-II feedback

For the reviewed \(D=4\) trajectory domain, write

\[
\Psi(n)=\Lambda(n)\mu^2(n).
\]

If \(X\) is the final cap and \(r\) extensions remain, the exact
geometric prefix cap and first-multiplier slack index are

\[
S_r(X)=1+\left\lfloor\frac{X-1}{2^r}\right\rfloor,
\qquad
h_r(q;X)=
\left\lfloor\frac{S_{r-1}(X)+1}{q}\right\rfloor.
\]

Thus the block kernel

\[
K_r(q;X)=
\sum_{\substack{2\le m\le h_r(q;X)\\2\mid m}}
\Psi(mq-1)K_{r-1}(mq-1;X)
\]

gives a duplicate-free recurrence over every length-\(L\) prefix below
\(S_b(X)\).  Restricting to old prefixes below \(4^L\) leaves a
nonnegative lower sum weighted by the actual terminal prime-path
coefficients.

The exact Vaughan identity

\[
\Lambda
=\Lambda_{\le V}
+\mu_{\le U}*\log
-\mu_{\le U}*\Lambda_{\le V}*\mathbf1
+\mu_{>U}*\Lambda_{>V}*\mathbf1
\]

puts the Type-II variables on

\[
uv=N=mq-1,\qquad uv\equiv-1\pmod q.
\]

Multiplication by \(\mu^2(N)\) removes prime powers exactly.  On an
individual congruent factor pair the nonprincipal Fourier modes have
total mass \((q-1)/q\), versus principal mass \(1/q\); a saving must
therefore come from aggregate coefficient cancellation.

For each fixed block length \(b\), a top-band index
\(4^{L-1}<q\le4^L\) permits only
\(m\le2^{b+3}\) at the first step.  Assign the successive primes above
\(2^{b+3}\) to the even multipliers in order and use CRT to force
\(r_m\mid mq-1\), with resulting modulus \(R_b\).
Bennett--Martin--O'Bryant--Rechnitzer Theorem 1.2 gives the
unconditional explicit bound

\[
\left|\theta(x;R_b,a_b)-\frac{x}{\varphi(R_b)}\right|
<\frac{x}{160\log x}
\]

for \(x\ge\exp(0.03\sqrt{R_b}(\log R_b)^3)\).  Applying it at \(x\)
and \(4x\) shows that every interval \((x,4x]\) contains a prime in the
CRT class once \(\log x\ge\varphi(R_b)/96\).  The fully explicit
integer threshold \(L\ge R_b^4+1\), with \(x=4^{L-1}\), satisfies both
conditions.  Hence every sufficiently large height has a top-band
prime row with every first candidate composite and
\(K_b(q;4^{L+b})=0\).

This excludes pointwise feedback and every estimate uniform over
coefficients constrained only by nonnegative prime support and trivial
norms, independently of the Vaughan cutoffs.  It does not show that the
actual prime-path coefficients put mass on a dead row.  A
coefficient-sensitive Type-II estimate would need a new
nonconcentration or residue-distribution theorem derived from the
complete prefix domain.  Unbounded \(D=4\) positivity remains open.

The proof, finite exact replay, primary-source excerpt, and bounded
Jacobian CRT record are in
`research/amortized_prime_path_typeii_feedback/`.
