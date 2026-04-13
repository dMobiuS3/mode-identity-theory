/ **[`main/`](../../../README.md)** / **[`framework/`](../../framework/)** / **[`cosmos/`](../../cosmos/)** / **[`spectrum/`](../../spectrum/)** /

---

# Fermion Mass Formula from Spectral Geometry on $S^3/2I$

[![Mass Spectrum](https://img.youtube.com/vi/eYO7BNcjxQI/mqdefault.jpg)](https://www.youtube.com/watch?v=eYO7BNcjxQI)

The Standard Model contains 12 fundamental fermions spanning 12 orders of magnitude in mass. The Higgs mechanism explains how particles acquire mass. It does not explain why they have the masses they do. This paper constructs a mass formula from four ingredients, each traced to a single topological postulate: $S^1 = \partial(\text{Mobius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset$. 

The formula is applied to the 8 nontrivial irreducible representations of the binary icosahedral group across 3 isolated flat connections, producing 24 mass predictions. Of these, 11 correspond to Standard Model fermions: 10 are reproduced within a factor of 3 and all 11 within a factor of 4. One SM fermion ($\nu_2$) falls between adjacent entries with no assignment. Eight predictions have no SM assignments.

| Result | Count |
|---|---|
| Assigned | 11 of 12 Standard Model fermions |
| Within ×3 | 10 of 11 |
| Within 6% | 3 ($e$ electron, $u$ up quark, $\mu$ muon) |
| Unassigned | $\nu_2$ (8.6 meV falls between rank 1 and rank 2; no $(\rho, \sigma)$ pair) |

## I. The Formula

$$\Large \boxed{m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot \left(\sqrt{\Omega_\Lambda}\right)^{\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)}$$

Four factors. Four sources. Each traces independently to the topological postulate.

| Factor | Role | Value |
|---|---|---|
| $\mu_\Lambda$ | Vacuum energy floor. Fourth root of cosmological constant energy density. Sets the overall mass scale. | $\rho_\Lambda^{1/4} \approx 2.25 \text{ meV}$ |
| $C_{\text{geom}}(\rho)$ | Phase factor. Geometric mean of $C(e/D) = 2\sin^2(\pi e/D)$ over Kostant exponents. Encodes each irrep's position on the domain. | $D = 60$ (integer spin) or $120$ (half-integer) |
| $(\sqrt{\Omega_\Lambda})^{\text{dist}/30}$ | Hierarchy exponent. McKay graph distance from $R_0$ determines orders of magnitude from the vacuum floor. Denominator is $h(E_8) = 30$. | $\sqrt{\Omega_\Lambda} \approx 1.019 \times 10^{61}$ |
| $T^2(\rho \otimes \sigma)$ | Reidemeister torsion, vacuum-twisted via tensor product. Provides fine structure within each mass shell. The generation mechanism. | 24 values from 8 irreps × 3 vacua |

## II. The Factors

### 1. Neutrino Floor  $\mu_\Lambda$ 

The vacuum energy density of the cosmological constant defines the overall mass scale:

$$\mu_\Lambda \equiv \rho_\Lambda^{1/4} \approx 2.25 \text{ meV}$$

This is the fourth root of Λ, set by the ground mode ($m_h = 0$) of the Mobius surface. All particle masses trace back to this vacuum energy floor, scaled by the hierarchical factors that place each irrep at its position on the spectrum.

The neutrino mass sector provides direct access to this scale:

| Splitting | Value | Ratio to $\mu_\Lambda$ |
|---|---|---|
| Solar: $\sqrt{\Delta m^2_{21}}$ | $\approx 8.6$ meV | $\sim 4\,\mu_\Lambda$ |
| Atmospheric: $\sqrt{\Delta m^2_{31}}$ | $\approx 50$ meV | $\sim 22\,\mu_\Lambda$ |

The multipliers (4, 22) emerge from parity violation due to the Mobius twist. KATRIN and cosmological bounds provide the falsification window.

### 2. Kostant Sunflower  $C_{\text{geom}}(\rho)$ 

Each irrep sits at a specific position on the finite domain, encoded by its Kostant exponents. The geometric mean of the phase factor $C(e/D) = 2\sin^2(\pi e/D)$ over these exponents gives the irrep's amplitude on the spectrum.

$$C_\text{geom}(\rho) = \bigl(\prod_e 2\sin^2(\pi e/D)\bigr)^{1/(2\,\dim\rho)}$$

The domain size depends on spin: $D = 60$ for integer-spin, $D = 120$ for half-integer. This encodes the fundamental distinction between bosons and fermions in the geometry. The domain size traces to the edge stabilizer $Z_4 \subset 2I$: integer-spin irreps carry only real $Z_4$ content ($D = 60 = |I|$), half-integer carry only complex pairs ($D = 120 = |2I|$).

| Irrep | Spin | $D$ | $C_\text{geom}$ |
|---|---|---|---|
| $R_1$ | Half | 120 | 0.0988 |
| $R_2$ | Half | 120 | 0.2436 |
| $R_3$ | Int | 60 | 0.5553 |
| $R_4$ | Int | 60 | 0.7970 |
| $R_5$ | Int | 60 | 0.8017 |
| $R_6$ | Half | 120 | 0.2098 |
| $R_7$ | Int | 60 | 0.7564 |
| $R_8$ | Half | 120 | 0.2382 |

### 3. McKay Elevator  $(\sqrt{\Omega_\Lambda})^{\text{dist}/30}$ 

The McKay graph encodes the distance of each irrep from the trivial representation $R_0$. Distance determines orders of magnitude separation from the vacuum floor via the hierarchy exponent $(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}$, where the denominator $h(E_8) = 30$ is the Coxeter number.

```
R0(1) -- R1(2) -- R3(3) -- R6(4) -- R7(5) -- R8(6) -- R5(4) -- R2(2)
                                                 |
                                                R4(3)  dist 6
  0        1        2        3        4         5        6        7
```

Half-integer spin: R₁, R₂, R₆, R₈. Integer spin: R₀, R₃, R₄, R₅, R₇.

| Irrep | dim | Spin | dist | $j_\text{first}$ | Kostant exponents | $E_8$? |
|---|---|---|---|---|---|---|
| $R_0$ | 1 | Int | 0 | 0 | {0, 30} | No |
| $R_1$ | 2 | Half | 1 | 1/2 | {1, 11, 19, 29} | All 4 |
| $R_2$ | 2 | Half | 7 | 7/2 | {7, 13, 17, 23} | All 4 |
| $R_3$ | 3 | Int | 2 | 1 | {2, 10, 12, 18, 20, 28} | No |
| $R_4$ | 3 | Int | 6 | 3 | {6, 10, 14, 16, 20, 24} | No |
| $R_5$ | 4 | Int | 6 | 3 | {6, 8, 12, 14, 16, 18, 22, 24} | No |
| $R_6$ | 4 | Half | 3 | 3/2 | {3, 9, 11, 13, 17, 19, 21, 27} | 4/8 |
| $R_7$ | 5 | Int | 4 | 2 | {4, 8, 10, 12, 14, 16, 18, 20, 22, 26} | No |
| $R_8$ | 6 | Half | 5 | 5/2 | {5, 7, 9, 11, 13, 15², 17, 19, 21, 23, 25} | 6/12 |

The $j_\text{first}$ rule follows from the McKay multiplicity structure: the spin-$j$ representation of $SU(2)$, restricted to $2I$, first contains irrep $\rho$ at exactly $j = \text{dist}(\rho)/2$. This holds for both spin parities and is a consequence of the McKay correspondence between the $2I$ representation graph and the extended $E_8$ Dynkin diagram.

### 4. Reidemeister Torsion  $T^2(\rho \otimes \sigma)$ 

Three flat SU(2) connections on $S^3/2I$ provide the generation mechanism. Each has $H^1 = 0$: no moduli, no mixing between vacua. The Reidemeister torsion encodes the fine structure within each mass shell.

| Irrep | $j_\text{first}$ (trivial) | $j_\text{first}$ (standard) | $j_\text{first}$ (Galois) |
|---|---|---|---|
| $R_0$ | 0 | 1 | 3 |
| $R_1$ | 1/2 | 1/2 | 5/2 |
| $R_2$ | 7/2 | 5/2 | 3/2 |
| $R_3$ | 1 | 0 | 2 |
| $R_4$ | 3 | 2 | 0 |
| $R_5$ | 3 | 2 | 1 |
| $R_6$ | 3/2 | 1/2 | 3/2 |
| $R_7$ | 2 | 1 | 1 |
| $R_8$ | 5/2 | 3/2 | 1/2 |

Integer-spin irreps have exact closed forms. The Galois pair ratio $T^2(R_3)/T^2(R_4) = \varphi^{-4}$ is exact to 70+ digits.

| Irrep | $T^2$ | $\log T^2$ |
|---|---|---|
| $R_0$ | $\pi^4/3600$ | $-3.610$ |
| $R_3$ | $(4/5)\varphi^{-2}$ | $-1.186$ |
| $R_7$ | $9/4$ | $+0.811$ |
| $R_5$ | $25/9$ | $+1.022$ |
| $R_4$ | $(4/5)\varphi^{2}$ | $+0.739$ |

Half-integer irreps ($R_1$, $R_2$, $R_6$, $R_8$) are computed from the same spectral data by the same method: the Laplacian eigenvalues and their multiplicities are exact (from $SU(2)$ representation theory and the $2I$ character table), and the spectral zeta function has a unique meromorphic continuation. The Hurwitz decomposition expresses each torsion as a finite sum of $L$-function derivatives at $s = 0$, each computable to arbitrary precision. 

The difference is selectivity: integer-spin irreps retain only 4 of 16 Dirichlet characters (conductors 2, 3, 5, 5), producing algebraic closed forms. Half-integer irreps retain 28 to 32 characters. The resulting sums are equally exact; they remain as finite combinations of $L'(0, \chi)$ values rather than reducing to algebraic expressions. The decimal values displayed throughout this paper are truncations of well-defined mathematical constants, computable to any desired precision by the same methods that verified the integer-spin values to 79 digits.

The 24 vacuum torsion values follow from $\log T^2(\rho \otimes \sigma) = \sum_\tau N_{\rho\sigma\tau} \log T^2(\tau)$:

| $\rho$ | $T^2(\rho,$ triv$)$ | $T^2(\rho,$ std$)$ | $T^2(\rho,$ gal$)$ |
|---|---|---|---|
| $R_1$ | 15.887 | 0.00827 | 2.778 |
| $R_2$ | 0.473 | 2.778 | 0.0567 |
| $R_3$ | 0.306 | 68.765 | 0.257 |
| $R_4$ | 2.094 | 0.257 | 2.048 |
| $R_5$ | 2.778 | 0.122 | 4.089 |
| $R_6$ | 4.328 | 0.688 | 4.712 |
| $R_7$ | 2.250 | 1.114 | 1.114 |
| $R_8$ | 0.257 | 13.090 | 1.910 |

## III. The 24 Predictions

24 predictions from the mass formula. The table below shows assignments to Standard Model (SM) fermions and unassigned predictions.

The assignment is constrained, not free. The formula produces 24 ranked entries; three structural filters narrow which entries can correspond to which fermions. The eta sign gate (§IV.3) restricts positive electric charge to negative-eta entries. The $Z_3$ face decomposition (§IV.1) restricts color-charged assignments to irreps carrying colored pairs. The $Z_4$ edge decomposition (§IV.2) fixes the domain for each spin parity. Together these filters eliminate most of the $24 \times 12$ possible pairings before any mass comparison is made, leaving a constrained mapping in which each SM fermion lands at its correct mass shell.

| Rank | $\rho$ | dist | $\sigma$ | Mass (GeV) | SM | Observed (GeV) | Ratio |
|---|---|---|---|---|---|---|---|
| 1 | $R_1$ | 1 | std | $1.98 \times 10^{-13}$ | $\nu_1$ | $\sim 10^{-13}$ | 1.98 |
| 2 | $R_1$ | 1 | gal | $6.67 \times 10^{-11}$ | $\nu_3$ | $5.06 \times 10^{-11}$ | 1.32 |
| gap | | | | — | $\nu_2$ | $8.6 \times 10^{-12}$ | — |
| 3 | $R_1$ | 1 | triv | $3.81 \times 10^{-10}$ | | excluded | |
| 4 | $R_3$ | 2 | gal | $3.75 \times 10^{-9}$ | | dead zone | |
| 5 | $R_3$ | 2 | triv | $4.45 \times 10^{-9}$ | | dead zone | |
| 6 | $R_6$ | 3 | std | $4.09 \times 10^{-7}$ | | dead zone | |
| 7 | $R_3$ | 2 | std | $1.00 \times 10^{-6}$ | | dead zone | |
| 8 | $R_6$ | 3 | triv | $2.57 \times 10^{-6}$ | | dead zone | |
| 9 | $R_6$ | 3 | gal | $2.80 \times 10^{-6}$ | | dead zone | |
| 10 | $R_7$ | 4 | std | $2.58 \times 10^{-4}$ | $e$ | $5.11 \times 10^{-4}$ | 1.98 |
| 11 | $R_7$ | 4 | gal | $2.58 \times 10^{-4}$ | $e$ | $5.11 \times 10^{-4}$ | 1.98 |
| **12** | **$R_7$** | **4** | **triv** | $\mathbf{5.21 \times 10^{-4}}$ | **$e$** | $\mathbf{5.11 \times 10^{-4}}$ | **1.02** |
| **13** | **$R_8$** | **5** | **triv** | $\mathbf{2.03 \times 10^{-3}}$ | **$u$** | $\mathbf{2.16 \times 10^{-3}}$ | **1.06** |
| 14 | $R_8$ | 5 | gal | $1.51 \times 10^{-2}$ | $d$ | $4.67 \times 10^{-3}$ | 3.22 |
| **15** | **$R_8$** | **5** | **std** | $\mathbf{1.03 \times 10^{-1}}$ | **$\mu$ / $s$** | $\mathbf{1.057 \times 10^{-1}}$ / $\mathbf{9.34 \times 10^{-2}}$ | **1.02** / **1.10** |
| 16 | $R_5$ | 6 | std | $3.49 \times 10^{-1}$ | | target | |
| 17 | $R_4$ | 6 | std | $7.34 \times 10^{-1}$ | $c$ / $\tau$ | 1.27 / 1.777 | 1.73 / 2.42 |
| 18 | $R_2$ | 7 | gal | 5.33 | $b$ | 4.18 | 1.28 |
| 19 | $R_4$ | 6 | gal | 5.84 | $b$ | 4.18 | 1.40 |
| 20 | $R_4$ | 6 | triv | 5.97 | $b$ | 4.18 | 1.43 |
| 21 | $R_5$ | 6 | triv | 7.96 | $b$ | 4.18 | 1.91 |
| 22 | $R_5$ | 6 | gal | 11.72 | $b$ | 4.18 | 2.80 |
| 23 | $R_2$ | 7 | triv | 44.54 | $t$ | 172.7 | 3.88 |
| 24 | $R_2$ | 7 | std | 261.46 | $t$ | 172.7 | 1.51 |

**Notes on the table.**

*Neutrino masses.* The $\nu_1$ observed value is inferred from $\Delta m^2_{21}$ assuming normal hierarchy with a near-zero lightest mass; the absolute mass scale is experimentally unknown. KATRIN, JUNO, and Project 8 will constrain this. The $\nu_3$ value uses $\sqrt{\Delta m^2_{31}}$ as a proxy. The ratio 1.98 for $\nu_1$ depends on this assumption.

*The down quark (rank 14).* The ratio of 3.22 is the weakest assigned hit after $\nu_2$, and the only charged fermion outside the ×3 window. The down quark mass itself carries large uncertainty (4.67 $\pm$ 0.5 MeV from lattice QCD), but even at the upper end of the allowed range the tension remains. Whether this reflects a systematic residual at high McKay distance or a needed correction in the $R_8$ Galois vacuum sector is open.

*Ambiguities at ranks 15 and 17.* Rank 15 sits between the muon (105.7 MeV) and strange quark (93.4 MeV), particles with different quantum numbers. Rank 17 sits between the charm quark (1.27 GeV) and tau lepton (1.777 GeV). The mass formula places each rank at the correct mass shell but does not yet resolve which particle occupies it. The electroweak selection rule (Section IV.4) is the mechanism intended to break these degeneracies; that derivation is in progress.

*The b-quark cluster.* Five entries (ranks 18-22) from four distinct $(\rho, \sigma)$ pairs cluster near the b mass at 4.18 GeV, with ratios from 1.28 to 2.80. This is a dense region of the spectrum where multiple irrep-vacuum combinations land in the same mass shell. The closest entry is rank 18 ($R_2$, gal, ratio 1.28). Whether the remaining entries represent structural redundancy, mixing contributions, or unassigned states is open.

## IV. Particle Identity

The mass formula assigns each Standard Model fermion to a pair $(\rho, \sigma)$. The mass comes from the torsion. The identity comes from the stabilizer structure of the icosahedron.

The binary icosahedral group $2I$ inherits three stabilizer subgroups from the icosahedron: face ($Z_3$, order 3), edge ($Z_2$, lifting to $Z_4$ in the double cover), and vertex ($Z_5$, order 5). Each irrep of $2I$ restricts to these subgroups, producing three independent decompositions. Two encode known Standard Model structure. The third connects to the electroweak sector through the Möbius twist.

### 1. Color from Faces

The face stabilizer $Z_3 \subset 2I$ is generated by order-3 elements. Restricting each irrep to $Z_3$ decomposes it into color singlets (lepton-type) and color triplet/anti-triplet pairs (quark-type):

| Irrep | dim | Singlets | Colored pairs | SM assignment |
|---|---|---|---|---|
| $R_1$ | 2 | 0 | 1 | $\nu_1$, $\nu_3$ |
| $R_3$ | 3 | 1 | 1 | (dead zone) |
| $R_6$ | 4 | 2 | 1 | (dead zone) |
| $R_7$ | 5 | 1 | 2 | $e$ |
| $R_8$ | 6 | 2 | 2 | $u$, $d$, $\mu/s$ |
| $R_5$ | 4 | 2 | 1 | $b$ |
| $R_4$ | 3 | 1 | 1 | $c/\tau$, $b$ |
| $R_2$ | 2 | 0 | 1 | $b$, $t$ |

Every assigned fermion's color charge is accommodated by the $Z_3$ decomposition of its irrep. The electron (color singlet) sits on $R_7$, which carries 1 singlet. The quarks sit on irreps with colored pairs. The neutrinos sit on $R_1$, which has no singlet content at the irrep level; the tensor product $R_1 \otimes \sigma$ with the vacuum connection generates the singlet channel through which the neutrino propagates as a color-neutral state.

The face stabilizer $Z_3$ corresponds to the $SU(3)$ color factor under the McKay correspondence: removing $R_3$ (the node killed by $Z_3$ alongside $R_4$ and $R_8$) from the extended $E_8$ Dynkin diagram produces the maximal subalgebra $SU(3) \times E_6$.

Color is generation-independent. The equivariant eta at the order-6 face class is perfectly vacuum-invariant: $\eta = 2$ in all three vacua. The face geometry looks the same from every vacuum. This matches the Standard Model: color charge is the same across generations.

### 2. Domain from Edges

The domain size $D = 60$ vs $120$ introduced in §II.2 traces to a deeper structure. The edge stabilizer $Z_2$ lifts to $Z_4 \subset 2I$, generated by order-4 elements. The $Z_4$ decomposition enforces an exact binary:

- Half-integer irreps $\{R_1, R_6, R_8, R_2\}$: all $Z_4$ content is complex pairs. Domain $D = 120$.
- Integer-spin irreps $\{R_0, R_3, R_7, R_5, R_4\}$: all $Z_4$ content is real. Domain $D = 60$.

This is the spin-statistics connection, built into the group. The mass formula encodes it through $C_\text{geom}$, which evaluates the Kostant exponents on the $D = 60$ or $D = 120$ grid.

### 3. The Eta Sign Gate

The Dirac eta invariant $\eta(\rho, \sigma)$ varies with the vacuum. Across all SM-assigned entries in the mass formula, a strict constraint holds:

$$\eta(\rho, \sigma) > 0 \implies Q \leq 0$$

Equivalently: positive electric charge requires negative eta. All entries with $Q = +2/3$ ($u$, $c$, $t$) have $\eta < 0$. All entries with $\eta > 0$ (ranks 1, 14, 18, 22) carry fermions with $Q = 0$ or $Q = -1/3$.

The eta invariant measures spectral asymmetry: the parity content of the mode. This gate connects parity to electric charge through the spectral geometry.

### 4. Vacuum as Electroweak Selector

The same irrep carries different fermions in different vacua. $R_8$ produces the up quark (trivial vacuum), down quark (Galois), and muon or strange (standard). The vacuum $\sigma$ selects the electroweak identity.

The mechanism is structural: the two nontrivial vacua ($R_1$ and $R_2$) are half-integer irreps. Tensoring a half-integer $\rho$ with a half-integer $\sigma$ produces integer-spin components, which carry none of the eight $E_8$ exponents. The Coxeter conjugate pair $(13, 17)$ under $h(E_8) = 30$, which governs all three SM gauge coupling strengths in the companion analysis, is preserved by the trivial vacuum and completely stripped by the nontrivial vacua.

For $R_8$ specifically: the trivial vacuum preserves the $(13, 17)$ pair $\to$ up quark ($Q = +2/3$, highest charge). The nontrivial vacua erase it $\to$ down quark or lepton ($Q \leq -1/3$).

The specific rule mapping each $(\rho, \sigma)$ to weak isospin $T_3$ and hypercharge $Y$ is the primary open problem in particle identity. The spectral data $(\eta, j_\text{first}, T^2)$ track electric charge within individual irreps, with the vacuum providing the selection. The eta sign gate and the exponent stripping mechanism are the two sharpest structural constraints identified so far.

### 5. The Vertex and the Twist

The vertex stabilizer $Z_5 \subset 2I$ produces a well-defined decomposition of each irrep into three components $(n_0, n_1, n_2)$, where $n_1$ counts $(\zeta, \zeta^4)$ pairs and $n_2$ counts $(\zeta^2, \zeta^3)$ pairs under the fifth roots of unity. The Galois conjugation $\sqrt{5} \to -\sqrt{5}$ swaps $n_1 \leftrightarrow n_2$.

| Irrep | dim | $Z_5$: $n_0$ / $n_1$ / $n_2$ |
|---|---|---|
| $R_1$ | 2 | 0 / 1 / 0 |
| $R_3$ | 3 | 1 / 0 / 1 |
| $R_6$ | 4 | 0 / 1 / 1 |
| $R_7$ | 5 | 1 / 1 / 1 |
| $R_8$ | 6 | 2 / 1 / 1 |
| $R_5$ | 4 | 0 / 1 / 1 |
| $R_4$ | 3 | 1 / 1 / 0 |
| $R_2$ | 2 | 0 / 0 / 1 |

$R_1$ (neutrinos) and $R_2$ (top/bottom) are pure and complementary under the Galois action. $R_7$ (electron) is maximally democratic. The two nontrivial vacua are $R_1$ and $R_2$ themselves, Galois conjugates that differ precisely in their $Z_5$ content: $R_1$ carries only $n_1$, $R_2$ carries only $n_2$. The electroweak distinction between vacua IS the vertex decomposition.

The dodecahedral angular defect $\pi/5$ at each vertex, halved by the Möbius $\mathbb{Z}_2$ holonomy to $\pi/10$, enters the weak coupling constant as $\cos(\pi/10) = \sqrt{(2+\varphi)}/2$. In the companion gauge coupling analysis, this correction uniquely improves $\alpha_W$ (from 5.6% to 0.4% error) and uniquely degrades $\alpha$ and $\alpha_s$ if misapplied. The vertex geometry reaches the observer through the Möbius twist, and only the parity-violating force carries the projection.

$R_7$ occupies a special position in this structure. $R_7 \otimes R_1 = R_7 \otimes R_2 = R_6 + R_8$: the two nontrivial vacua produce identical torsion at $R_7$. The Dirac eta invariant captures this through the antisymmetric vacuum combination $(5/2)(\eta_\text{std} - \eta_\text{gal})$, which equals an integer for every irrep and is uniquely zero at $R_7$. The irrep that carries the electron sees both vacua identically. It sits at the center of the vertex structure, where the Galois distinction vanishes.

### 6. Summary

| Stabilizer | Subgroup | Physical content | Status |
|---|---|---|---|
| Face ($Z_3$) | Order 3 | Color: singlet vs triplet | Locked |
| Edge ($Z_4$) | Order 4 | Domain: $D = 60$ vs $120$ | Locked |
| Vertex ($Z_5$) | Order 5 | Electroweak interface | Current work |
| Face/Edge ratio | $3/2$ | Gravity: Gauss-Codazzi | Motivated |
| Vertex through twist | $\cos(\pi/10)$ | Weak coupling correction | Motivated |

The three stabilizer orders 2, 3, 5 are the primes dividing $|2I| = 120$ and the conductors of the four surviving Dirichlet characters in the torsion L-basis. They generate color, domain, and (through their interfaces) gravity and the weak force. The mass formula computes how heavy. The stabilizer structure says what.

---

## V. Dead Zone, Targets, and Exclusions

Eight entries have no Standard Model assignments. Six fall in the "dead zone" (ranks 4-9), the mass range between $10^{-9}$ and $10^{-6}$ GeV (eV to keV) where no known fundamental fermion exists and experimental sensitivity to new states is limited. One is a target (rank 16) in a normal mass range where a particle could exist but has no current SM assignment. One is excluded (rank 3) by existing data.

The dead zone is actively probed by sterile neutrino and warm dark matter searches. Physical states at these masses require extremely suppressed non-gravitational couplings. The framework is agnostic about whether these entries correspond to propagating particles or are structural residuals of the spectrum with no physical realization. If physical, they are candidates for sterile neutrino or warm dark matter searches in the eV-keV window.

Rank 16 ($R_5$, std) at 349 MeV sits in a normal mass range between the strange quark and charm quark. No SM fermion occupies this mass. If the entry is physical, it predicts an undiscovered state; if not, it joins the dead zone as a structural residual. Either outcome is informative.

| Rank | $\rho$ | dist | $\sigma$ | Mass (GeV) | Range | Status |
|---|---|---|---|---|---|---|
| 3 | $R_1$ | 1 | triv | $3.81 \times 10^{-10}$ | ~0.4 eV | excluded |
| 4 | $R_3$ | 2 | gal | $3.75 \times 10^{-9}$ | ~4 eV | dead zone |
| 5 | $R_3$ | 2 | triv | $4.45 \times 10^{-9}$ | ~4 eV | dead zone |
| 6 | $R_6$ | 3 | std | $4.09 \times 10^{-7}$ | ~0.4 keV | dead zone |
| 7 | $R_3$ | 2 | std | $1.00 \times 10^{-6}$ | ~1 keV | dead zone |
| 8 | $R_6$ | 3 | triv | $2.57 \times 10^{-6}$ | ~3 keV | dead zone |
| 9 | $R_6$ | 3 | gal | $2.80 \times 10^{-6}$ | ~3 keV | dead zone |
| 16 | $R_5$ | 6 | std | $3.49 \times 10^{-1}$ | ~349 MeV | target |

### Rank 3 Exclusion

Rank 3 ($R_1$, triv) predicts ~0.4 eV. Cosmological bounds constrain the sum of neutrino masses to $\Sigma m_\nu \lesssim 0.1$ eV, and solar neutrino data place a lower bound of ~10 meV on $\nu_2$ via the matter effect. A single eigenstate at 0.4 eV would saturate or exceed the cosmological sum by itself. Rank 3 is excluded as a SM neutrino. Whether it corresponds to a non-SM state with suppressed couplings (similar to the dead zone entries) or signals a structural correction needed in the $R_1$ triv vacuum remains OPEN.

### The $\nu_2$ Gap

$\nu_2$ at 8.6 meV sits between rank 1 (0.2 meV) and rank 2 (66.7 meV), a ratio gap of ~7.75× from rank 2. This is the mass formula's only genuine miss among the twelve SM fermions. The experimentally allowed window for $\nu_2$ is roughly 10-50 meV, constrained from below by solar neutrino data and from above by the cosmological mass sum. The normal vs. inverted hierarchy remains experimentally undetermined; JUNO and DUNE are expected to resolve this. Whether vacuum mixing between $R_1$ entries or additional structure at the neutrino scale closes the gap remains OPEN.

---

## VI. Open Problems

| Item | Status |
|------|--------|
| $(\rho, \sigma) \to (T_3, Y)$ assignment rule | Primary open problem. Eta sign gate and exponent stripping constrain but do not complete the mapping. |
| $\nu_2$ gap | 8.6 meV falls between ranks 1 and 2. Vacuum mixing or neutrino-scale structure could close it. |
| Down quark tension | Rank 14 ratio 3.22; see Section III notes. Systematic residual at high McKay distance or $R_8$ Galois correction needed. |
| Fermion mass residual | Systematic overshoot growing with McKay distance. One-parameter correction pattern identified, not derived. |
| Dead zone physical status | 6 entries in eV-keV range. Propagating states or structural residuals: experimentally distinguishable. |
| Rank 16 target | 349 MeV prediction with no SM assignment. Standing prediction. |

---

*The topology permits and Ψ settles. The formula composes and the masses land.*

---

/ **[`main/`](../../../README.md)** / **[`framework/`](../../framework/)** / **[`cosmos/`](../../cosmos/)** / **[`spectrum/`](../../spectrum/)** /
