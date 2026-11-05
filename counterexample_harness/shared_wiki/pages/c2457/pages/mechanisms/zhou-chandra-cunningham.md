---
title: Zhou-Huang-Xia Chandra-matrix Cunningham boundary
description: The complete IJISM source displays plus-one chains, misreads Green-Tao's finite-length quantifiers, and supplies no fixed-exponential second-kind family.
---

# Zhou-Huang-Xia Chandra-matrix Cunningham boundary

The complete primary source is Mi Zhou, Jun Steed Huang, and Yiwen Xia,
*Infinite Cunningham Chains and Infinite Arithmetic Primes*,
*International Journal of Innovation in Science and Mathematics* 4(2)
(2016), 70-73. The journal-hosted PDF is frozen at
`research/zhou_chandra_cunningham_audit/source/IJISM_522_FINAL.pdf`.

The paper displays
\[
  n,2n+1,4n+3,8n+7,\ldots,
\]
so every displayed term satisfies \(p_{i+1}=2p_i+1\). Its complete numeric
chain rows \(5,11,23,47\), \(41,83,167\), and
\(89,179,359,719,1439,2879\) have the same plus-one recurrence. They do not
satisfy the campaign's second-kind relation \(q_{i+1}=2q_i-1\).

For an arithmetic progression \(A_j=a+jd\), its dyadic-index subsequence
\[
  T_i=A_{2^{i-1}-1}
\]
satisfies the exact identity
\[
  T_{i+1}=2T_i+(d-a).
\]
Thus the paper's plus-one rows require \(d=a+1\), while target minus-one rows
require \(d=a-1\). Green-Tao Theorem 1.1 guarantees finite prime arithmetic
progressions of every requested length but imposes neither relation.

The paper additionally changes those arbitrary finite lengths into one
infinite arithmetic progression of primes. This is a quantifier error:
for \(a\ge2,d\ge1\), the term at index \(a\) is
\[
  a+ad=a(1+d),
\]
which is composite. Its own two finite arithmetic rows also stop at the next
term, \(35=5\cdot7\) and \(539=7^2\cdot11\).

Finally, the Chandra-matrix pseudocode is bounded by one finite `LargeNum`.
No all-length simultaneous-primality theorem, parametric prime certificate,
or bound \(q_1(L)\le D^L\) appears. Hence the source does not establish
\[
  q_L=2^{L-1}(q_1(L)-1)+1\le C^L
\]
for unbounded \(L\) and one fixed \(C\).

This retires only the Zhou-Huang-Xia source transfer. It does not prove that
arbitrarily long second-kind Cunningham chains are absent and does not give
an Erdos counterexample.
