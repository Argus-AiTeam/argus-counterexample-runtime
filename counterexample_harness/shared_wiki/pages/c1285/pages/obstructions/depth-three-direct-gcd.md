---
title: Depth-three direct quotient/remainder gcd obstruction
description: Exact floor-fiber counting makes H3 exponentially weak on balanced semiprimes, while the R3 gcd is inherited from X and H2.
---

# Depth-three direct quotient/remainder gcd obstruction

For uniform \(X,Y\in\{0,\ldots,N-1\}\), define

\[
H_1=\lfloor XY/N\rfloor,\quad
H_2=\lfloor XH_1/N\rfloor,\quad
H_3=\lfloor XH_2/N\rfloor,
\]

and \(R_3=XH_2-NH_3\). For fixed \(X=x>0\), every fiber of
\(t\mapsto\lfloor xt/N\rfloor\) has at most \(\lceil N/x\rceil<2N/x\)
members, while \(H_k<x^k/N^{k-1}\). The number of positive multiples of
a CRT prime \(r\) in that range is below \(x^k/(N^{k-1}r)\). Therefore

\[
\Pr(r\mid H_k,\ H_k>0)<2^k/r
\]

for \(k=1,2,3\), including all half-open floor boundaries. In particular,
the new \(H_3\) test contributes less than \(8/p+8/q\).

The remainder has no independent factor path:

\[
\gcd(R_3,N)=\gcd(XH_2,N).
\]

If inherited tests on \(X\) and \(H_2\) have not returned a proper factor,
then either one value is zero and the \(R_3\) gcd is \(N\), or both are
units and it is \(1\). Thus the direct tests on
\(X,Y,H_1,H_2,H_3,R_3\) have total probability below
\(16(1/p+1/q)\).

On the reviewed canonical exact-length balanced family this is
\(2^{-n/2+O(1)}\). Adding only the \(H_3,R_3\) gcd tests to the reviewed
two-mulhi postprocessor preserves its \(2^{-\Omega(n)}\) bound under every
fixed polynomial adaptive schedule with fresh conditionally uniform
source pairs.

This obstruction does not cover placing \(H_3\) or \(R_3\) in terminal
formulas, further nested quotients, nonuniform source laws, unrestricted
HECM, or general factoring.
