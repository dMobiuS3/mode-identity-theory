/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/Mass%20Spectrum.png" width="100%" alt="Mass Spectrum">

The Standard Model contains 12 fundamental fermions spanning 12 orders of magnitude in mass. The Higgs mechanism explains how particles acquire mass. It does not explain why they have the masses they do. This page constructs a mass formula from four ingredients, each traced to a single topological postulate: $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset`$. 

The formula is applied to the 8 nontrivial irreducible representations of the binary icosahedral group across 3 isolated flat connections, producing 24 ranked entries under a uniform topological normalization: 22 acyclic torsion invariants, and 2 non-acyclic diagonal entries set to their canonical topological value (see §4). Lined up against the measured fermions, with the electron taken as the benchmark that sets the absolute scale, 5 of the remaining 8 charged fermions land within a factor of 3 of a quantum-number-compatible entry (the down quark outside ×3, charm unassigned, the bottom quark uncounted, the muon and strange sharing one entry at rank 15); the three neutrinos rest on absolute masses nobody has measured. This is a comparison, not a prediction: the entries and their quantum numbers are fixed a priori, but which entry lands on which measured fermion is read against the data, and at this entry density a measured mass sits near some entry largely by counting (a pre-registered null test quantifies this: random torsion reassignment reproduces the hit rate; see §III). The charm quark is displaced from rank 17 with its assignment open, and in the $`R_1`$ sector the neutrino-generation map is open: rank 1 sits at the wrong scale for $`\nu_1`$, and $`\nu_2`$ has no entry (see §V). The $`(R_2,\text{gal})`$ entry sits at 197 GeV with no compatible fermion; nine entries have no SM match.

| Result | Count |
|---|---|
| Charged fermions within ×3 | 5 of 8 ($`m_e`$ is the benchmark; d outside, c unassigned, b uncounted, μ/s share rank 15) |
| Within 6% | $`u`$, $`\mu`$ ($`m_e`$ is the scale benchmark) |
| Neutrinos | 3 rows; absolute masses unmeasured; rank 1 at the wrong scale for $`\nu_1`$ (generation map open) |
| Unassigned / uncounted | $`c`$ (displaced from rank 17, assignment open); $`b`$ (its $`(R_2,\text{gal})`$ entry at 197 GeV; nearest compatible $`(R_4,\text{gal})`$ at 1.40, not promoted); $`\nu_2`$ (no entry) |
| Nature | comparison, not prediction |

## I. The Formula

```math
\Large \boxed{m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot \left(\sqrt{\Omega_\Lambda}\right)^{\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)}
```

Four factors. Four sources. Each traces independently to the topological postulate.

| Factor | Role | Value |
|---|---|---|
| $`\mu_\Lambda`$ | Vacuum energy floor. Fourth root of cosmological constant energy density. Sets the overall mass scale. | $`\rho_\Lambda^{1/4} \approx 2.25 \text{ meV}`$ |
| $`C_{\text{geom}}(\rho)`$ | Phase factor. Geometric mean of $`C(e/D) = 2\sin^2(\pi e/D)`$ over Kostant exponents. Encodes each irrep's position on the domain. | $`D = 60`$ (integer spin) or 120 (half-integer) |
| $`(\sqrt{\Omega_\Lambda})^{\text{dist}/30}`$ | Hierarchy exponent. McKay graph distance from $`R_0`$ determines orders of magnitude from the vacuum floor. Denominator is $`h(E_8) = 30`$. | $`\sqrt{\Omega_\Lambda} \approx 1.019 \times 10^{61}`$ |
| $`T^2(\rho \otimes \sigma)`$ | Matter-local-system torsion: Reidemeister on the 22 acyclic products, canonical integral-cohomology normalization on the 2 non-acyclic diagonal products. Vacuum-dependent fine structure within each mass shell. | 24 values from 8 irreps × 3 vacua |

## II. The Factors

### 1. Neutrino Floor  $`\mu_\Lambda`$ 

The vacuum energy density of the cosmological constant defines the overall mass scale:

```math
\mu_\Lambda \equiv \rho_\Lambda^{1/4} \approx 2.25 \text{ meV}
```

This is the fourth root of Λ, set by the first positive mode ($`m_h = 0`$) of the Möbius surface. All particle masses trace back to this vacuum energy floor, scaled by the hierarchical factors that place each irrep at its position on the spectrum. The Λ entering here is the measured cosmological constant taken as the surface-sector calibration input, so $`\mu_\Lambda`$ is the mass sector's anchor into that calibration, the scale every ratio multiplies, rather than a quantity the framework predicts (see [Three readings of one hierarchy](../../framework/README.md#three-readings-of-one-hierarchy)).

The neutrino mass sector provides direct access to this scale:

| Splitting | Value | Ratio to $`\mu_\Lambda`$ |
|---|---|---|
| Solar: $`\sqrt{\Delta m^2_{21}}`$ | $`\approx 8.6`$ meV | $`\sim 4\,\mu_\Lambda`$ |
| Atmospheric: $`\sqrt{\Delta m^2_{31}}`$ | $`\approx 50`$ meV | $`\sim 22\,\mu_\Lambda`$ |

The multipliers (4, 22) emerge from parity violation due to the Möbius twist. KATRIN and cosmological bounds provide the falsification window.

### 2. Kostant Sunflower  $`C_{\text{geom}}(\rho)`$ 

Each irrep sits at a specific position on the finite domain, encoded by its Kostant exponents. The geometric mean of the phase factor $`C(e/D) = 2\sin^2(\pi e/D)`$ over these exponents gives the irrep's amplitude on the spectrum.

```math
C_\text{geom}(\rho) = \bigl(\prod_e 2\sin^2(\pi e/D)\bigr)^{1/(2\,\dim\rho)}
```

The domain size depends on spin: $`D = 60`$ for integer-spin, $`D = 120`$ for half-integer. This encodes the fundamental distinction between bosons and fermions in the geometry. The domain size traces to the edge stabilizer $`Z_4 \subset 2I`$: integer-spin irreps carry only real $`Z_4`$ content ($`D = 60 = |I|`$), half-integer carry only complex pairs ($`D = 120 = |2I|`$).

| Irrep | Spin | $`D`$ | $`C_\text{geom}`$ |
|---|---|---|---|
| $`R_1`$ | Half | 120 | 0.0988 |
| $`R_2`$ | Half | 120 | 0.2436 |
| $`R_3`$ | Int | 60 | 0.5553 |
| $`R_4`$ | Int | 60 | 0.7970 |
| $`R_5`$ | Int | 60 | 0.8017 |
| $`R_6`$ | Half | 120 | 0.2098 |
| $`R_7`$ | Int | 60 | 0.7564 |
| $`R_8`$ | Half | 120 | 0.2382 |

### 3. McKay Elevator  $`(\sqrt{\Omega_\Lambda})^{\text{dist}/30}`$ 

The McKay graph encodes the distance of each irrep from the trivial representation $`R_0`$. Distance determines orders of magnitude separation from the vacuum floor via the hierarchy exponent $`(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}`$, where the denominator $`h(E_8) = 30`$ is the Coxeter number.

```
R0(1) -- R1(2) -- R3(3) -- R6(4) -- R7(5) -- R8(6) -- R5(4) -- R2(2)
                                                 |
                                                R4(3)  dist 6
  0        1        2        3        4         5        6        7
```

Half-integer spin: R₁, R₂, R₆, R₈. Integer spin: R₀, R₃, R₄, R₅, R₇.

| Irrep | dim | Spin | dist | $`j_\text{first}`$ | Kostant exponents | $`E_8`$? |
|---|---|---|---|---|---|---|
| $`R_0`$ | 1 | Int | 0 | 0 | {0, 30} | No |
| $`R_1`$ | 2 | Half | 1 | 1/2 | {1, 11, 19, 29} | All 4 |
| $`R_2`$ | 2 | Half | 7 | 7/2 | {7, 13, 17, 23} | All 4 |
| $`R_3`$ | 3 | Int | 2 | 1 | {2, 10, 12, 18, 20, 28} | No |
| $`R_4`$ | 3 | Int | 6 | 3 | {6, 10, 14, 16, 20, 24} | No |
| $`R_5`$ | 4 | Int | 6 | 3 | {6, 8, 12, 14, 16, 18, 22, 24} | No |
| $`R_6`$ | 4 | Half | 3 | 3/2 | {3, 9, 11, 13, 17, 19, 21, 27} | 4/8 |
| $`R_7`$ | 5 | Int | 4 | 2 | {4, 8, 10, 12, 14, 16, 18, 20, 22, 26} | No |
| $`R_8`$ | 6 | Half | 5 | 5/2 | {5, 7, 9, 11, 13, 15², 17, 19, 21, 23, 25} | 6/12 |

The $`j_\text{first}`$ rule follows from the McKay multiplicity structure: the spin-<i>j</i> representation of $`SU(2)`$, restricted to $`2I`$, first contains irrep $`\rho`$ at exactly $`j = \text{dist}(\rho)/2`$. This holds for both spin parities and is a consequence of the McKay correspondence between the $`2I`$ representation graph and the extended $`E_8`$ Dynkin diagram.

### 4. Torsion Factors  $`T^2(\rho \otimes \sigma)`$

Three flat SU(2) connections on $`S^3/2I`$ label the three vacuum sectors. Each connection has $`H^1 = 0`$, so the flat vacua are infinitesimally rigid, with no continuous moduli. The factor $`T^2(\rho\otimes\sigma)`$ is the torsion of the flat bundle $`E_{\rho\otimes\sigma}`$:

- **$`\rho \neq \sigma`$ (22 of the 24 products): acyclic.** The torsion is an ordinary Ray-Singer scalar, equal to the metric-independent Reidemeister invariant: the fine structure within each mass shell.
- **$`\rho = \sigma`$ (the 2 diagonal products, a particle in its own vacuum): non-acyclic.** The trivial representation appears, $`H^0 = H^3 = \mathbb{C}`$, and the ledger uses the canonical integral-cohomology value $`T^2(R_0) = 1`$. The unit-radius analytic torsion $`\pi^4/3600 = \mathrm{Vol}(S^3/2I)^2`$ is a harmonic zero-mode normalization, metric-dependent, not a topological invariant, and is not used.

A standing check follows, one a reader can apply to the table directly: a genuine topological torsion on this space form is an algebraic (cyclotomic) number, and every elementary value below is algebraic. A transcendental factor would be the fingerprint of a zero mode carrying geometry.

| Irrep | $`j_\text{first}`$ (trivial) | $`j_\text{first}`$ (standard) | $`j_\text{first}`$ (Galois) |
|---|---|---|---|
| $`R_0`$ | 0 | 1 | 3 |
| $`R_1`$ | 1/2 | 1/2 | 5/2 |
| $`R_2`$ | 7/2 | 5/2 | 3/2 |
| $`R_3`$ | 1 | 0 | 2 |
| $`R_4`$ | 3 | 2 | 0 |
| $`R_5`$ | 3 | 2 | 1 |
| $`R_6`$ | 3/2 | 1/2 | 3/2 |
| $`R_7`$ | 2 | 1 | 1 |
| $`R_8`$ | 5/2 | 3/2 | 1/2 |

Integer-spin irreps have exact closed forms. The Galois pair ratio $`T^2(R_3)/T^2(R_4) = \varphi^{-4}`$ is exact to 70+ digits.

| Irrep | $`T^2`$ | $`\log T^2`$ |
|---|---|---|
| $`R_0`$ | $`1`$ | $`0`$ |
| $`R_3`$ | $`(4/5)\varphi^{-2}`$ | -1.186 |
| $`R_7`$ | 9/4 | +0.811 |
| $`R_5`$ | 25/9 | +1.022 |
| $`R_4`$ | $`(4/5)\varphi^{2}`$ | +0.739 |

$`R_0`$ (trivial representation) is non-acyclic; the ledger uses its canonical topological value $`1`$ (§4 above). Every elementary value is an algebraic invariant.

Half-integer irreps ($`R_1`$, $`R_2`$, $`R_6`$, $`R_8`$) are computed from the same spectral data by the same method: the Laplacian eigenvalues and their multiplicities are exact (from $`SU(2)`$ representation theory and the $`2I`$ character table), and the spectral zeta function has a unique meromorphic continuation. The Hurwitz decomposition expresses each torsion as a finite sum of $`L`$-function derivatives at $`s = 0`$, each computable to arbitrary precision. 

The difference is selectivity: integer-spin irreps retain only 4 of 16 Dirichlet characters (conductors 2, 3, 5, 5), producing algebraic closed forms. Half-integer irreps retain 28 to 32 characters. The resulting sums are equally exact and algebraic; they have not yet been simplified to explicit algebraic closed forms, remaining exact finite combinations of $`L'(0, \chi)`$ values. The decimal values displayed throughout this page are truncations of well-defined mathematical constants, computable to any desired precision by the same methods that verified the integer-spin values to 79 digits.

The 24 vacuum torsion values follow from $`\log T^2(\rho \otimes \sigma) = \sum_\tau N_{\rho\sigma\tau} \log T^2(\tau)`$:

| $`\rho`$ | $`T^2(\rho,`$ triv$`)`$ | $`T^2(\rho,`$ std$`)`$ | $`T^2(\rho,`$ gal$`)`$ |
|---|---|---|---|
| $`R_1`$ | 15.887 | 0.306 | 2.778 |
| $`R_2`$ | 0.473 | 2.778 | 2.094 |
| $`R_3`$ | 0.306 | 68.765 | 0.257 |
| $`R_4`$ | 2.094 | 0.257 | 2.048 |
| $`R_5`$ | 2.778 | 0.122 | 4.089 |
| $`R_6`$ | 4.328 | 0.688 | 4.712 |
| $`R_7`$ | 2.250 | 1.114 | 1.114 |
| $`R_8`$ | 0.257 | 13.090 | 1.910 |

The two diagonal products contain the trivial representation, $`R_1 \otimes \text{std} = R_0 + R_3`$ and $`R_2 \otimes \text{gal} = R_0 + R_4`$, so both carry the factor $`T^2(R_0) = 1`$: $`T^2(R_1,\text{std}) = 0.306`$ and $`T^2(R_2,\text{gal}) = 2.094`$.

## III. The 24 Entries

24 entries from the formula. The table below shows the comparison to Standard Model (SM) fermions and the entries with no SM match. Bold rows are the preferred SM assignments counted in the headline scorecard. Unbolded repeated labels show nearby candidate entries or mass-shell clusters; they are not counted as separate assignments.

The assignment is constrained, not free. The formula produces 24 ranked entries; four structural filters narrow which entries can correspond to which fermions. The Coxeter-Galois gate (§IV.4) assigns weak isospin $`T_3 = \pm 1/2`$ to each entry. The $`Z_3`$ face decomposition (§IV.1) restricts color-charged assignments to irreps carrying colored pairs. The $`Z_4`$ edge decomposition (§IV.2) fixes the domain for each spin parity. The eta sign gate (§IV.3) restricts positive electric charge to negative-eta entries. Together these filters determine the quantum numbers $`(T_3, Y, Q)`$ at each $`(\rho, \sigma)`$ pair before any mass comparison is made.

A pre-registered null test (`mass-null-v1.0`, July 11, 2026) quantified the table's counting caveat. Randomly reassigning the 24 torsion factors across the fixed quantum-number slots reproduced or exceeded the observed compatible-coverage score in 17.4% of draws ($`p_A = 0.174`$). The ×3 proximity count is therefore uninformative about whether the specific torsion values occupy the correct slots.

Random torsion reassignment reproduces the published hit rate. The mass table's evidential weight rests on the exact structural outputs, the 24-entry construction, the $`T_3`$ gate with its ten correct evaluations, and the $`\varphi^{-4}`$ ratio, together with the falsifiable outliers, not on the ×3 proximity count. This test does not independently validate those structural outputs; it removes the proximity scorecard as evidence for the torsion dial.

The three counts answer progressively stricter questions: raw mass density covers 8 of 8 charged fermions within ×3; enforcing the frozen quantum-number gates reduces compatible coverage to 6 of 8; retaining the adjudicated no-slide assignments gives the public ledger's 5 of 8.

```math
8 = \text{raw density}, \qquad 6 = \text{compatible density}, \qquad 5 = \text{adjudicated assignments}
```

| Rank | $`\rho`$ | dist | $`\sigma`$ | Mass (GeV) | SM | Observed (GeV) | Ratio |
|---|---|---|---|---|---|---|---|
| 1 | $`R_1`$ | 1 | std | $`7.33 \times 10^{-12}`$ | neutrino sector (generation open) | $`\sim 10^{-13}`$ | 73 |
| gap | | | | — | $`\nu_2`$ (observed position; no entry, see §V) | $`8.6 \times 10^{-12}`$ | — |
| 2 | $`R_1`$ | 1 | gal | $`6.67 \times 10^{-11}`$ | $`\nu_3`$ | $`5.06 \times 10^{-11}`$ | 1.32 |
| 3 | $`R_1`$ | 1 | triv | $`3.81 \times 10^{-10}`$ | | excluded | |
| 4 | $`R_3`$ | 2 | gal | $`3.75 \times 10^{-9}`$ | | dead zone | |
| 5 | $`R_3`$ | 2 | triv | $`4.45 \times 10^{-9}`$ | | dead zone | |
| 6 | $`R_6`$ | 3 | std | $`4.09 \times 10^{-7}`$ | | dead zone | |
| 7 | $`R_3`$ | 2 | std | $`1.00 \times 10^{-6}`$ | | dead zone | |
| 8 | $`R_6`$ | 3 | triv | $`2.57 \times 10^{-6}`$ | | dead zone | |
| 9 | $`R_6`$ | 3 | gal | $`2.80 \times 10^{-6}`$ | | dead zone | |
| 10 | $`R_7`$ | 4 | std | $`2.58 \times 10^{-4}`$ | $`e`$ candidate | $`5.11 \times 10^{-4}`$ | 1.98 |
| 11 | $`R_7`$ | 4 | gal | $`2.58 \times 10^{-4}`$ | $`e`$ candidate | $`5.11 \times 10^{-4}`$ | 1.98 |
| **12** | **$`R_7`$** | **4** | **triv** | $`\mathbf{5.21 \times 10^{-4}}`$ | **$`e`$** | $`\mathbf{5.11 \times 10^{-4}}`$ | **1.02** (benchmark) |
| **13** | **$`R_8`$** | **5** | **triv** | $`\mathbf{2.03 \times 10^{-3}}`$ | **$`u`$** | $`\mathbf{2.16 \times 10^{-3}}`$ | **1.06** |
| 14 | $`R_8`$ | 5 | gal | $`1.51 \times 10^{-2}`$ | $`d`$ | $`4.67 \times 10^{-3}`$ | 3.22 |
| **15** | **$`R_8`$** | **5** | **std** | $`\mathbf{1.03 \times 10^{-1}}`$ | **$`\mu`$ / $`s`$** | $`\mathbf{1.057 \times 10^{-1}}`$ / $`\mathbf{9.34 \times 10^{-2}}`$ | **1.02** / **1.10** |
| 16 | $`R_5`$ | 6 | std | $`3.49 \times 10^{-1}`$ | | target | |
| 17 | $`R_4`$ | 6 | std | $`7.34 \times 10^{-1}`$ | $`\tau`$ | 1.777 | 2.42 |
| 18 | $`R_4`$ | 6 | gal | 5.84 | $`b`$ nearest (uncounted) | 4.18 | 1.40 |
| 19 | $`R_4`$ | 6 | triv | 5.97 | $`b`$ neighborhood | 4.18 | 1.43 |
| 20 | $`R_5`$ | 6 | triv | 7.96 | $`b`$ neighborhood | 4.18 | 1.91 |
| 21 | $`R_5`$ | 6 | gal | 11.72 | $`b`$ neighborhood | 4.18 | 2.80 |
| 22 | $`R_2`$ | 7 | triv | 44.54 | $`t`$ candidate | 172.7 | 3.88 |
| 23 | $`R_2`$ | 7 | gal | 197 | $`b`$ (uncounted) | 4.18 | 47 |
| **24** | **$`R_2`$** | **7** | **std** | **261.46** | **$`t`$** | **172.7** | **1.51** |

**Notes on the table:**

*The electron (rank 12).* $`m_e`$ is the benchmark that sets the absolute mass scale, so its 1.02 is not a forward comparison but the $`m_e \leftrightarrow \Lambda`$ loop closing: entering instead from $`\Lambda`$ through $`\mu_\Lambda = \rho_\Lambda^{1/4}`$ reproduces $`m_e`$ to 2%, which inverts to ~11% in $`\Lambda`$. The forward comparisons are the other charged fermions; neither end of the loop is privileged. See the calibration web on the [framework](../../framework/) page.

*Neutrino masses.* The $`\nu_1`$ observed value is inferred from $`\Delta m^2_{21}`$ assuming normal hierarchy with a near-zero lightest mass; the absolute mass scale is experimentally unknown. KATRIN, JUNO, and Project 8 will constrain this. The $`\nu_3`$ value uses $`\sqrt{\Delta m^2_{31}}`$ as a proxy. The rank-1 neutrino-sector entry $`(R_1,\text{std})`$ is a non-acyclic diagonal product at 7.3 meV, 73× the $`\nu_1`$ scale, so it does not pin the $`\nu_1`$ generation (see §V); its absolute mass is unmeasured, and it is not a scorecard hit.

*The down quark (rank 14).* The ratio of 3.22 is the weakest assigned hit after $`\nu_2`$, and the only charged fermion outside the ×3 window. The down quark mass itself carries large uncertainty (4.67 $`\pm`$ 0.5 MeV from lattice QCD), but even at the upper end of the allowed range the tension remains. Whether this reflects a systematic residual at high McKay distance or a needed correction in the $`R_8`$ Galois vacuum sector is open.

*Rank 15 resolution.* Rank 15 sits between the muon (105.7 MeV) and strange quark (93.4 MeV). The Coxeter-Galois gate (§IV.4) assigns $`T_3 = -1/2`$ to this entry. The $`Z_3`$ face decomposition then splits the mass shell: the singlet component carries the muon ($`Q = -1`$), the colored component carries the strange quark ($`Q = -1/3`$). Both particles occupy the same $`(\rho, \sigma)`$ address in different color sectors.

*Rank 17 resolution.* Rank 17 ($`R_4`$, std) has $`j_\text{first} = 2`$ (integer). Stage 1 of the Coxeter-Galois gate assigns $`T_3 = -1/2`$, resolving the former $`c/\tau`$ ambiguity in favor of the tau lepton ($`Q = -1`$, from the singlet $`Z_3`$ sector). The charm quark ($`T_3 = +1/2`$) does not occupy rank 17; its assignment within the 24-entry table is open (see §VI).

*The tau (rank 17), weakest surviving hit.* At ratio 2.42 the tau is the largest counted ratio, and it is the sole quantum-number-compatible entry within ×3 only because its nearest charged-lepton-compatible competitors (the $`R_4`$/$`R_5`$ entries at ranks 18–19) sit just past the ×3 boundary. It is counted, since it passes the ledger's stated isolation criterion, but it is the first entry that would fall under any tightening of that criterion. Whether ×3 is the right isolation window is a policy question for the whole table at once, not settled here.

*The bottom quark.* Its $`R_2`$-sector entry $`(R_2, \text{gal})`$ is a non-acyclic diagonal product sitting at $`\approx 197`$ GeV (rank 23), 47× the bottom mass, so it is not a hit. The nearest quantum-number-compatible entry to 4.18 GeV is $`(R_4, \text{gal})`$ at ratio 1.40 (rank 18), and the $`R_4`$/$`R_5`$ shell brackets 4.18 GeV (1.40, 1.43, 1.91, 2.80). That entry is recorded but **not** promoted to hold the count: the ledger assigns each fermion to its nearest quantum-number-compatible entry, and sliding onto a next-nearest address to fill a gap would switch selection rules. The observed mass sitting inside an acyclic fan of compatible entries is, at this entry density, what counting produces. Recorded, visible, uncounted.

## IV. Particle Identity

The mass formula assigns each Standard Model fermion to a pair $`(\rho, \sigma)`$. The mass-formula factor is the torsion; the identity comes from the stabilizer structure of the icosahedron.

The binary icosahedral group $`2I`$ inherits three stabilizer subgroups from the icosahedron: face ($`Z_3`$, order 3), edge ($`Z_2`$, lifting to $`Z_4`$ in the double cover), and vertex ($`Z_5`$, order 5). Each irrep of $`2I`$ restricts to these subgroups, producing three independent decompositions. Two encode known Standard Model structure. The third connects to the electroweak sector through the Möbius twist.

### 1. Color from Faces

The face stabilizer $`Z_3 \subset 2I`$ is generated by order-3 elements. Color is read off the propagating mode $`\rho \otimes \sigma`$, the same object that carries weak isospin in §IV.4. Restricting it to $`Z_3`$ splits it into color singlets (the channel a lepton can occupy) and color triplet/anti-triplet pairs (the channel a quark can occupy). The channel columns below are the $`\sigma = \text{triv}`$ slice, where $`\rho \otimes R_0 = \rho`$, so they read off each bare irrep. This shows which color channels are available, not by itself whether an entry is a lepton or a quark: the full $`(\rho, \sigma)`$ assignment fixes that, with the charge closed in §IV.4 by Gell-Mann-Nishijima.

| Irrep | dim | Singlets | Colored pairs | SM assignment |
|---|---|---|---|---|
| $`R_1`$ | 2 | 0 | 1 | neutrino sector: $`\nu_3`$-scale + one generation-open entry (singlet via $`\rho\otimes\sigma`$) |
| $`R_3`$ | 3 | 1 | 1 | (dead zone) |
| $`R_6`$ | 4 | 2 | 1 | (dead zone) |
| $`R_7`$ | 5 | 1 | 2 | $`e`$ |
| $`R_8`$ | 6 | 2 | 2 | $`u`$, $`d`$, $`\mu/s`$ |
| $`R_5`$ | 4 | 2 | 1 | $`b`$ |
| $`R_4`$ | 3 | 1 | 1 | $`\tau`$, $`b`$ |
| $`R_2`$ | 2 | 0 | 1 | $`b`$, $`t`$ |

The $`b`$ label on $`R_5`$, $`R_4`$, $`R_2`$ marks color-compatible candidates, not three assignments; the bottom quark is uncounted (see §III). Every assigned fermion has the color channel it needs in its propagating mode $`\rho \otimes \sigma`$. The electron (color singlet) sits on $`R_7`$, which already carries 1 singlet at the bare level. The quarks sit on irreps with colored pairs. The neutrinos sit on $`R_1`$, which has no singlet content as a bare irrep; the singlet channel appears only once $`R_1`$ is tensored with the vacuum connection, and this is where reading from $`\rho \otimes \sigma`$ rather than bare $`R_1`$ does real work. It does so without special pleading, because the whole $`R_1`$ sector falls out at once: $`R_1 \otimes \text{std} = R_0 + R_3`$ carries $`1 + 1 = 2`$ singlets, $`R_1 \otimes \text{gal} = R_5`$ carries 2 singlets, and the one $`R_1`$ mode with no singlet channel, $`R_1 \otimes \text{triv} = R_1`$ itself, is exactly rank 3, the entry excluded on cosmological grounds in §V. The mode rule admits the two propagating neutrinos and forbids the non-propagating one, so the apparent clash between $`R_1`$ having zero bare singlets and carrying neutrinos is a consistency check the assignment passes. (This is a *channel* argument: $`R_1`$ carries the neutrino singlet content, independent of mass. The mass is separate: the $`R_1 \otimes \text{std}`$ mode sits at 7.3 meV, 73× the $`\nu_1`$ scale, so it does not pin the $`\nu_1`$ generation; the $`R_1`$ neutrino-generation map is open, see §V.)

The face stabilizer $`Z_3`$ corresponds to the $`SU(3)`$ color factor under the McKay correspondence: removing $`R_3`$ (the node killed by $`Z_3`$ alongside $`R_4`$ and $`R_8`$) from the extended $`E_8`$ Dynkin diagram produces the maximal subalgebra $`SU(3) \times E_6`$.

Color is generation-independent. The equivariant eta at the order-6 face class is perfectly vacuum-invariant: $`\eta = 2`$ in all three vacua. The face geometry looks the same from every vacuum. This matches the Standard Model: color charge is the same across generations.

### 2. Domain from Edges

The domain size $`D = 60`$ vs 120 introduced in §II.2 traces to a deeper structure. The edge stabilizer $`Z_2`$ lifts to $`Z_4 \subset 2I`$, generated by order-4 elements. The $`Z_4`$ decomposition enforces an exact binary:

- Half-integer irreps $`\{R_1, R_6, R_8, R_2\}`$: all $`Z_4`$ content is complex pairs. Domain $`D = 120`$.
- Integer-spin irreps $`\{R_0, R_3, R_7, R_5, R_4\}`$: all $`Z_4`$ content is real. Domain $`D = 60`$.

This is the spin-statistics connection, built into the group. The mass formula encodes it through $`C_\text{geom}`$, which evaluates the Kostant exponents on the $`D = 60`$ or $`D = 120`$ grid.

### 3. The Eta Sign Gate

The Dirac eta invariant $`\eta(\rho, \sigma)`$ varies with the vacuum. Across the mass-formula entries, a strict constraint links it to the charge slot the gates fix:

```math
\eta(\rho, \sigma) > 0 \implies Q \leq 0
```

Equivalently: positive electric charge requires negative eta. All entries with $`Q = +2/3`$ ($`u`$, $`c`$, $`t`$) have $`\eta < 0`$. All entries with $`\eta > 0`$ (ranks 1, 14, 21, 23) sit in $`Q = 0`$ or $`Q = -1/3`$ slots; rank 23 is such a down-type slot but carries no assigned fermion (the bottom quark's entry is a 47× miss, see §III).

The eta invariant measures spectral asymmetry: the parity content of the mode. This gate connects parity to electric charge through the spectral geometry.

### 4. Weak Isospin from the Coxeter-Galois Gate

The same irrep carries different fermions in different vacua. $`R_8`$ produces the up quark (trivial vacuum), down quark (Galois), and muon or strange (standard). The vacuum $`\sigma`$ selects the electroweak identity. The rule determining weak isospin $`T_3`$ at each $`(\rho, \sigma)`$ is a two-stage filter, computable entirely from Tools 2-4 before any mass is evaluated.

**Stage 1: Spectral parity.** If $`j_\text{first}(\rho, \sigma) \in \mathbb{Z}`$ (integer), the mode enters the Dirac spectrum through the bosonic channel: $`T_3 = -1/2`$.

**Stage 2: Coxeter-Galois gate.** For half-integer $`j_\text{first}`$, evaluate two conditions. First: does $`\rho`$ carry the Coxeter conjugate pair $`(13, 17)`$ under $`h(E_8) = 30`$, and is it stripped by the vacuum? The pair lives in the Kostant exponents of $`R_2`$, $`R_6`$, and $`R_8`$ (all half-integer). The trivial vacuum preserves it ($`\rho \otimes R_0 = \rho`$). The nontrivial vacua strip it (half-integer $`\otimes`$ half-integer $`\to`$ integer-spin components, which carry none of the eight $`E_8`$ exponents). Second: does the tensor product $`\rho \otimes \sigma`$ contain a Galois-nonfixed irrep? The four Galois-nonfixed irreps are $`\{R_1, R_2, R_3, R_4\}`$, whose characters involve $`\sqrt{5}`$; the Galois-fixed irreps $`\{R_0, R_5, R_6, R_7, R_8\}`$ are invariant under $`\sqrt{5} \to -\sqrt{5}`$.

Both conditions must hold for $`T_3 = -1/2`$. If either $`(13, 17)`$ is preserved (trivial vacuum, or $`\rho`$ lacks the pair) or the product is entirely Galois-fixed, then $`T_3 = +1/2`$.

In one line:

```math
T_3 = -\tfrac{1}{2} \iff j_\text{first} \in \mathbb{Z},\ \text{or}\ (13,17)\ \text{stripped and}\ \rho \otimes \sigma\ \text{has Galois-nonfixed content.}
```

**Gate evaluation at ten addresses:**

| Rank | $`\rho`$ | $`\sigma`$ | $`j_\text{first}`$ | $`(13,17)`$ | $`\rho \otimes \sigma`$ | Galois-nonfixed? | Path | $`T_3`$ |
|---|---|---|---|---|---|---|---|---|
| 1 | $`R_1`$ | std | 1/2 | N/A | $`R_0 + R_3`$ | (irrelevant) | no pair $`\to`$ +1/2 | +1/2 ✓ |
| 2 | $`R_1`$ | gal | 5/2 | N/A | $`R_5`$ | (irrelevant) | no pair $`\to`$ +1/2 | +1/2 ✓ |
| 12 | $`R_7`$ | triv | 2 | N/A | $`R_7`$ | — | $`j_\text{first} \in \mathbb{Z}`$ | -1/2 ✓ |
| 13 | $`R_8`$ | triv | 5/2 | kept | $`R_8`$ | — | pair kept $`\to`$ +1/2 | +1/2 ✓ |
| 14 | $`R_8`$ | gal | 1/2 | stripped | $`R_7 + R_5 + R_3`$ | $`R_3`$ yes | both $`\to`$ -1/2 | -1/2 ✓ |
| 15 | $`R_8`$ | std | 3/2 | stripped | $`R_7 + R_5 + R_4`$ | $`R_4`$ yes | both $`\to`$ -1/2 | -1/2 ✓ |
| 17 | $`R_4`$ | std | 2 | N/A | $`R_8`$ | — | $`j_\text{first} \in \mathbb{Z}`$ | -1/2 ✓ |
| 22 | $`R_2`$ | triv | 7/2 | kept | $`R_2`$ | — | pair kept $`\to`$ +1/2 | +1/2 ✓ |
| 23 | $`R_2`$ | gal | 3/2 | stripped | $`R_0 + R_4`$ | $`R_4`$ yes | both $`\to`$ -1/2 | -1/2 ✓ |
| 24 | $`R_2`$ | std | 5/2 | stripped | $`R_5`$ | all fixed | Galois-fixed $`\to`$ +1/2 | +1/2 ✓ |

Ten entries through the gate, ten correct evaluations. Eight carry an assigned fermion; the other two are structural checks: rank 22 ($`R_2`$ triv) is an unassigned top-shell candidate (the top is rank 24), and rank 23 ($`R_2`$ gal) is the rule-validation case: at $`\approx 197`$ GeV it is numerically near the top yet correctly held as down-type ($`T_3 = -1/2`$), so the gate refuses the tempting reassignment. Rank 17 is resolved as $`\tau`$ ($`T_3 = -1/2`$). Rank 24 is resolved as $`t`$ ($`T_3 = +1/2`$): $`R_2 \otimes R_1 = R_5`$, and $`R_5`$ is Galois-fixed, so the Galois involution has nothing to act on and the state retains upper isospin by structural inertia.

**Hypercharge and electric charge follow from $`Z_3`$.** Once $`T_3`$ is fixed, the $`Z_3`$ face decomposition (§IV.1) determines color, and the Gell-Mann-Nishijima formula $`Q = T_3 + Y/2`$ closes the circuit:

| $`Z_3`$ sector | $`T_3`$ | $`Q`$ | $`Y`$ |
|---|---|---|---|
| Singlet (lepton) | +1/2 | 0 (neutrino) | -1 |
| Singlet (lepton) | -1/2 | -1 (charged lepton) | -1 |
| Triplet (quark) | +1/2 | +2/3 (up-type) | +1/3 |
| Triplet (quark) | -1/2 | -1/3 (down-type) | +1/3 |

All ingredients are representation-theoretic: $`j_\text{first}`$ from SU(2) $`\to`$ 2I branching rules, Kostant exponents from the McKay correspondence, tensor product decompositions from the character table, and Galois-fixed/nonfixed status from Gal($`\mathbb{Q}(\sqrt{5})/\mathbb{Q}`$). The quantum numbers $`(T_3, Y, Q)`$ are determined before mass. Particle identity is not: fermions in one family share every quantum number the gates can see (the three charged leptons are all $`Q = -1`$, $`T_3 = -1/2`$, color singlet), so which entry is the electron, muon, or tau is settled by the measured mass, not by the gates. The gates fix the kind; the mass fixes the generation.

### 5. The Vertex and the Twist

The vertex stabilizer $`Z_5 \subset 2I`$ produces a well-defined decomposition of each irrep into three components $`(n_0, n_1, n_2)`$, where $`n_1`$ counts $`(\zeta, \zeta^4)`$ pairs and $`n_2`$ counts $`(\zeta^2, \zeta^3)`$ pairs under the fifth roots of unity. The Galois conjugation $`\sqrt{5} \to -\sqrt{5}`$ swaps $`n_1 \leftrightarrow n_2`$.

| Irrep | dim | $`Z_5`$: $`n_0`$ / $`n_1`$ / $`n_2`$ |
|---|---|---|
| $`R_1`$ | 2 | 0 / 1 / 0 |
| $`R_3`$ | 3 | 1 / 0 / 1 |
| $`R_6`$ | 4 | 0 / 1 / 1 |
| $`R_7`$ | 5 | 1 / 1 / 1 |
| $`R_8`$ | 6 | 2 / 1 / 1 |
| $`R_5`$ | 4 | 0 / 1 / 1 |
| $`R_4`$ | 3 | 1 / 1 / 0 |
| $`R_2`$ | 2 | 0 / 0 / 1 |

$`R_1`$ (neutrinos) and $`R_2`$ (top/bottom) are pure and complementary under the Galois action. $`R_7`$ (electron) is maximally democratic. The two nontrivial vacua are $`R_1`$ and $`R_2`$ themselves, Galois conjugates that differ precisely in their $`Z_5`$ content: $`R_1`$ carries only $`n_1`$, $`R_2`$ carries only $`n_2`$. The electroweak distinction between vacua IS the vertex decomposition.

The dodecahedral angular defect $`\pi/5`$ at each vertex, halved by the Möbius $`Z_2`$ holonomy to $`\pi/10`$, enters the weak coupling constant as $`\cos(\pi/10) = \sqrt{(2+\varphi)}/2`$. In the companion gauge coupling analysis, this correction uniquely improves $`\alpha_W`$ (from 5.6% to 0.4% error) and uniquely degrades $`\alpha`$ and $`\alpha_s`$ if misapplied. The vertex geometry reaches the observer through the Möbius twist, and only the parity-violating force carries the projection.

$`R_7`$ occupies a special position in this structure. $`R_7 \otimes R_1 = R_7 \otimes R_2 = R_6 + R_8`$: the two nontrivial vacua produce identical torsion at $`R_7`$. The Dirac eta invariant captures this through the antisymmetric vacuum combination $`(5/2)(\eta_\text{std} - \eta_\text{gal})`$, which equals an integer for every irrep and is uniquely zero at $`R_7`$. The irrep that carries the electron sees both vacua identically. It sits at the center of the vertex structure, where the Galois distinction vanishes.

### 6. Summary

| Stabilizer | Subgroup | Physical content | Status |
|---|---|---|---|
| Face ($`Z_3`$) | Order 3 | Color: singlet vs triplet | Locked |
| Edge ($`Z_4`$) | Order 4 | Domain: $`D = 60`$ vs 120 | Locked |
| Vertex ($`Z_5`$) | Order 5 | Electroweak: $`T_3`$ via Coxeter-Galois gate | Established |
| Face/Edge ratio | 3/2 | Gravity: Gauss-Codazzi | Motivated |
| Vertex through twist | $`\cos(\pi/10)`$ | Weak coupling correction | Motivated |

The three stabilizer orders 2, 3, 5 are the primes dividing $`|2I| = 120`$ and the conductors of the four surviving Dirichlet characters in the torsion L-basis. They generate color, domain, and (through their interfaces) gravity and the weak force. The stabilizer structure says what each entry is; the formula says where it sits, both from the topology. Which entry lands on which measured fermion is the comparison, read against the data.

---

## V. Dead Zone, Targets, and Exclusions

Nine entries have no Standard Model assignments. Six fall in the "dead zone" (ranks 4-9), the mass range between $`10^{-9}`$ and $`10^{-6}`$ GeV (eV to keV) where no known fundamental fermion exists and experimental sensitivity to new states is limited. One is a target (rank 16) in a normal mass range where a particle could exist but has no current SM assignment. One is excluded (rank 3) by existing data. One is rank 23 ($`R_2`$ gal) at 197 GeV, which has no quantum-number-compatible SM assignment: it is numerically near $`t`$ (172.7 GeV), but the pre-mass isospin gate rejects it as down-type ($`T_3 = -1/2`$), exactly the structural behavior a genuine gate should show when a mass coincidence tempts a wrong assignment.

The dead zone is actively probed by sterile neutrino and warm dark matter searches. Physical states at these masses require extremely suppressed non-gravitational couplings. The framework is agnostic about whether these entries correspond to propagating particles or are structural residuals of the spectrum with no physical realization. If physical, they are candidates for sterile neutrino or warm dark matter searches in the eV-keV window.

Rank 16 ($`R_5`$, std) at 349 MeV sits in a normal mass range between the strange quark and charm quark. No measured fermion occupies this mass. If it is physical rather than a residual of the dense entry structure, it would be an undiscovered state; if not, it joins the dead zone as a structural residual. Either outcome is informative.

| Rank | $`\rho`$ | dist | $`\sigma`$ | Mass (GeV) | Range | Status |
|---|---|---|---|---|---|---|
| 3 | $`R_1`$ | 1 | triv | $`3.81 \times 10^{-10}`$ | ~0.4 eV | excluded |
| 4 | $`R_3`$ | 2 | gal | $`3.75 \times 10^{-9}`$ | ~4 eV | dead zone |
| 5 | $`R_3`$ | 2 | triv | $`4.45 \times 10^{-9}`$ | ~4 eV | dead zone |
| 6 | $`R_6`$ | 3 | std | $`4.09 \times 10^{-7}`$ | ~0.4 keV | dead zone |
| 7 | $`R_3`$ | 2 | std | $`1.00 \times 10^{-6}`$ | ~1 keV | dead zone |
| 8 | $`R_6`$ | 3 | triv | $`2.57 \times 10^{-6}`$ | ~3 keV | dead zone |
| 9 | $`R_6`$ | 3 | gal | $`2.80 \times 10^{-6}`$ | ~3 keV | dead zone |
| 16 | $`R_5`$ | 6 | std | $`3.49 \times 10^{-1}`$ | ~349 MeV | target |
| 23 | $`R_2`$ | 7 | gal | $`197`$ | ~197 GeV | no compatible SM (near $`t`$, gate-rejected as down-type) |

### Rank 3 Exclusion

Rank 3 ($`R_1`$, triv) predicts ~0.4 eV. Cosmological bounds constrain the sum of neutrino masses to $`\Sigma m_\nu \lesssim 0.1`$ eV, and solar neutrino data place a lower bound of ~10 meV on $`\nu_2`$ via the matter effect. A single eigenstate at 0.4 eV would saturate or exceed the cosmological sum by itself. Rank 3 is excluded as a SM neutrino. Whether it corresponds to a non-SM state with suppressed couplings (similar to the dead zone entries) or signals a structural correction needed in the $`R_1`$ triv vacuum remains OPEN.

### The Neutrino-Generation Ambiguity

Rank 1 $`(R_1, \text{std})`$ is a non-acyclic diagonal product; it sits at 7.3 meV, 73× the provisional $`\nu_1`$ scale, so it does not pin the $`\nu_1`$ generation. Its value falls near the solar scale associated with $`\nu_2`$ (8.6 meV), but this is two experimentally unmeasured numbers landing close and carries no evidential weight: all three neutrino absolute masses are unknown, none is a scorecard hit, so no generation is assigned to rank 1 and nothing is inferred from the proximity. The ledger assigns each fermion to its nearest quantum-number-compatible entry and does not slide a generation onto a next-nearest address to fill a gap. Together with the charm quark (displaced by the $`\tau`$ resolution at rank 17), the neutrino-generation map across the $`R_1`$ sector is open. The experimentally allowed window for $`\nu_2`$ is roughly 10-50 meV, constrained from below by solar neutrino data and from above by the cosmological mass sum; the normal vs. inverted hierarchy remains undetermined, and JUNO and DUNE, by fixing the hierarchy and scale, would constrain the map.

---

## VI. Open Problems

| Item | Status |
|------|--------|
| $`T_3`$ assignment rule | Established. Two-stage filter: $`j_\text{first}`$ parity + Coxeter-Galois gate. Ten gate evaluations correct (eight assigned fermions, plus two structural checks at ranks 22 and 23). See §IV.4. |
| $`\mu`$/$`s`$ single-entry count | Rank 15 supplies both the muon and the strange via the $`R_8`$ singlet/triplet color split, so two fermions are credited to one $`(\rho,\sigma)`$ address. Whether that is one hit or two is a standing convention question (a strict one-entry-one-hit reading would give 4 of 8). |
| Charm quark assignment | OPEN. $`T_3`$ rule resolves rank 17 as $`\tau`$, displacing charm. All $`R_4`$ entries have integer $`j_\text{first}`$ ($`T_3 = -1/2`$ at every vacuum), so charm cannot live on $`R_4`$. Candidate entries under investigation. |
| $`R_1`$ neutrino-generation map | OPEN. Rank 1 ($`R_1`$ std) sits at 7.3 meV, the wrong scale to pin $`\nu_1`$; $`\nu_2`$ (8.6 meV) has no entry. All three neutrino masses are unmeasured, so no generation is assigned. See §V. |
| Down quark tension | Rank 14 ratio 3.22; see Section III notes. Systematic residual at high McKay distance or $`R_8`$ Galois correction needed. |
| Fermion mass residual | Systematic overshoot growing with McKay distance. One-parameter correction pattern identified, not derived. |
| Dead zone physical status | 6 entries in eV-keV range. Propagating states or structural residuals: experimentally distinguishable. |
| Rank 16 target | 349 MeV entry with no measured match. Real state or residual, open. |

---

*The topology permits and Ψ settles. The formula composes and the entries line up.*

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
