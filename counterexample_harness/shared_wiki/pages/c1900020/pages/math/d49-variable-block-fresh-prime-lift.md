---
title: D49 variable-block fixed-lattice boundary
description: The mod-769 bound has survivors, but the B(u), strict-digit, and cone-conditioned weak-digit monoids all fail the first exact overlapping determinant test.
---

For
\[
K=\mathbf Q(\theta),\qquad
\theta^3-\theta^2-2\theta+1=0,
\]
at the root \(\theta\in(2/5,1/2)\), set
\[
\Xi_k=\theta^{2^{k+1}}(1+\theta^{2^k}),\qquad k\geq1.
\]
All these elements lie in
\[
H=\mathbf Z+2\mathbf Z\theta+2\mathbf Z\theta^2.
\]
The first four coefficient rows have two \(3\)-by-\(3\) minors
\[
-45481,\qquad -62590621210
\]
with gcd one.  A transformation-certified Smith computation therefore
shows that the \(\Xi_k\) generate \(H\).  Every \(\Xi_k\) is primitive in
\(H\): odd rational divisibility contradicts the norm of
\(\theta^{2^k}=-1\) modulo that prime, while the exact order-seven cycle
modulo \(2\) excludes divisibility by \(2\).  Consequently content,
primitive row completion, and individual admissibility do not obstruct a
fixed-lattice lift.

There is an exact eventual restriction in this lattice:
\[
\theta^{256}=1\pmod {769\mathbf Z[\theta]},
\qquad
[\Xi_k]_H=(2,0,0)\pmod {769}\quad(k\geq8).
\]
For an \(H\)-basis transition \(A_k=W_kA_{k+1}\), this forces
\[
e_1^TW_k=e_1^T\pmod {769}.
\]
The first rows of one- and two-digit inverse products have respectively
third and second coordinate \(1\), so \(|w_k|\geq3\) for \(k\geq8\).

This restriction is sharp and cannot be promoted to a universal
obstruction.  For every \(D\geq1\),
\[
N(0,D)N(0,1)^2=
\begin{pmatrix}
D+1&D&D\\
1&1&1\\
1&0&1
\end{pmatrix}.
\]
Every suffix is a true standard Jacobi--Perron branch for every reduced
positive terminal state.  At \(D=769\), its first row is \(e_1^T\) modulo
\(769\).

Writing \(\epsilon=\theta^{-1}\) and
\(T_n=\operatorname{Tr}(\epsilon^n)\), the exact boundary quotient is
\[
\left\lfloor\frac{\Xi(m)}{\Xi(2m)}\right\rfloor
=
\begin{cases}
29,&m=2,\\
T_m+T_{2m}-2,&m\geq4\text{ even}.
\end{cases}
\]
This follows from
\[
\frac{\Xi(m)}{\Xi(2m)}
=E^2+E-1-\frac{E-1}{E^2+1},\qquad E=\epsilon^m,
\]
and a uniform Pisot-defect bound below one.  The quotient does not determine
the two companion rows of a fixed-lattice basis.  Two natural trace blocks
are excluded modulo \(769\), while an explicit four-block product already
crosses that congruence, so this trace identity also remains a scoped
diagnostic rather than a lift or universal obstruction.

The reviewed pairwise-coprime nonunit ideals \((\Xi_k)\) still give the
complete nonperiodicity implication conditional on a lift: two boundary
times in one eventual-period phase would differ by a lattice unit and
would have equal principal ideals.  What remains unavailable is either a
coherent all-\(k\) basis-and-word rule outside the block monoid below.
Fixed word lengths, finite digit boxes, canonical completions, and the
mod-\(769\) observation do not settle that broader question.

## Exact arbitrary-word \(B(u)\)-monoid obstruction

For the universal true-floor blocks
\[
B(u)=
\begin{pmatrix}
u&u-1&u-1\\
1&1&1\\
1&0&1
\end{pmatrix},\qquad u\geq2,
\]
the route with arbitrary nonempty word lengths is now excluded without a
length cutoff.  If \(e_1W=(a,b,c)\) and \(W\) joins two normalized positive
bases with first entries \(\Xi(m)\) and \(\Xi(2m)\), positivity forces
\[
a<\frac{\Xi(m)}{\Xi(2m)}<a+b+c.
\]
Appending another block changes the first coordinate to \(ua+b+c\).
This is strictly increasing both down the word tree and in \(u\), so the
inequality gives a complete finite pruning proof for every word.

At the first required overlap,
\[
A_2=U_2A_4,\qquad A_4=U_4A_8,
\]
exact root-sign arithmetic leaves 47 possible \(U_2\) words and 5769
possible \(U_4\) words.  With
\[
R(U,V)=
\begin{pmatrix}e_1UV\\e_1V\\e_1\end{pmatrix},
\qquad
V_2=\begin{pmatrix}v_2\\v_4\\v_8\end{pmatrix},
\]
overlap requires \(V_2=R(U_2,U_4)A_8\).  But
\[
\det V_2=-45481,
\]
whereas all 271143 exact candidate pairs have
\[
-18844\leq\det R(U_2,U_4)\leq2408.
\]
None can make \(R(U_2,U_4)^{-1}V_2\) unimodular.  This excludes the entire
normalized positive \(B(u)\)-word monoid, not merely a fixed tail.

Modulo 13, by contrast, the complete legal-block row automaton reaches all
\(13^3-1=2196\) nonzero rows in shortest length at most six.  The old
fixed-tail contradiction is therefore a residue artifact; the decisive
new obstruction is the exact integral determinant at an overlapping true
positive transition.  Since the coherent lift does not exist in this
monoid, the fresh-ideal unit-return implication is not activated and no
counterexample follows.

## Full strict-digit monoid obstruction

The larger family
\[
N(a,b)=
\begin{pmatrix}b&0&1\\1&0&0\\a&1&0\end{pmatrix},
\qquad 0\leq a<b,
\]
is also exhausted without a digit or word-length cutoff. For every
\(0<y,z<x\),
\[
N(a,b)(x,y,z)^t=(bx+z,x,ax+y)^t
\]
has true floors \((a,b)\) and remains in the same normalized cone. Thus this
is the full digit family that preserves the entire cone uniformly.

For \(e_1W=(r,s,t)\), appending a digit gives
\[
(r,s,t)\mapsto(br+s+at,t,r).
\]
With \(F=\lfloor\Xi(m)/\Xi(2m)\rfloor\), endpoint compatibility is exactly
\[
r\leq F,\qquad r+s+t\geq F+1.
\]
At each row this gives finite explicit bounds on \(b\) and \(a\). The first
coordinate is nondecreasing; equality can occur only for the first two
\((0,1)\) transitions, and thereafter it rises by at least one. Hence the
enumeration terminates without imposing a depth.

The complete multiplicity counts are 7771 words for \(U_2\) and 66065352
words for \(U_4\). They would form 513393850392 first-overlap pairs, but a
uniform exact argument avoids materializing them. If
\[
x=e_1U_2=(r,s,t),\qquad
e_1U_4^{-1}=(\alpha,\beta,\gamma),
\]
then
\[
\det R(U_2,U_4)=t\beta-s\gamma.
\]
An induction on the projected rows of \(U_4^{-1}\) proves
\[
|\beta|+|\gamma|\leq674,
\]
while every \(U_2\) candidate has \(s,t\leq29\). Therefore every pair
satisfies
\[
|\det R|\leq29\cdot674=19546<45481=|\det V_2|.
\]
No normalized integral \(A_2,A_4,A_8\) overlap survives, so the reviewed
fresh-ideal implication is again not activated. This result does not cover
digits with \(a=b\), words legal only on a smaller cone, or a different
scalar recurrence.

## Cone-conditioned weak-digit obstruction

The omitted equality digits are now also covered. For \(0<y,z<x\),
\[
N(a,b)(x,y,z)^t=(bx+z,x,ax+y)^t
\]
has a normalized output exactly when \(0\leq a<b\), or when
\(a=b\geq1\) and \(y<z\). If \(a>b\), the difference between the first
and third output coordinates is at most \(-x+z-y<0\); \(a=b=0\) also
fails because \(z<x\). Thus all true normalized words lie in the weak
superset \(b\geq1,\ 0\leq a\leq b\), with the equality-suffix condition
temporarily discarded.

The same exact endpoint recursion, now with \(a\leq b\), terminates without
a word-depth or coefficient cutoff. It contains \(31504\) words for
\(U_2\) and \(570552305\) words for \(U_4\), hence
\(17974679816720\) first-overlap pairs. Words with one first row need not
have one inverse row, so the determinant argument uses a separate
all-word theorem. If
\[
e_1W=(r,s,t),\qquad e_1W^{-1}=(\alpha,\beta,\gamma),
\]
a shifted-continuant induction valid for every \(0\leq a\leq b\) gives
\[
|\beta|+|\gamma|\leq s+t\leq2r.
\]
Consequently every weak overlap satisfies
\[
|\det R|\leq29(2\cdot674)=39092<45481.
\]
No pair can yield \(A_8=R^{-1}V_2\in GL_3(\mathbf Z)\). Because the
enumeration is a superset of every suffix-legal equality word, this
cutoff-free obstruction excludes every normalized true word for the D49
first overlap. It does not exclude a different scalar recurrence and does
not itself produce a counterexample.
