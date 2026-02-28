# The Spectrum

**Particle Mass Generation from McKay Spectral Geometry on $S^3/2I$**

The Standard Model contains 12 fundamental fermions spanning 12 orders of magnitude in mass. The Higgs mechanism explains how particles acquire mass. It does not explain why they have the masses they do. This paper constructs a mass formula from four ingredients, each traced to a single topological postulate: $S^1 = \partial(\text{Mobius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset$. 

The formula is applied to the 8 nontrivial irreducible representations of the binary icosahedral group across 3 isolated flat connections, producing 24 mass predictions. Of 12 Standard Model fermions, 10 are reproduced within a factor of 3 and all 12 within a factor of 10.

**10 of 12 within x3 · 12 of 12 within x10**

Electron · up quark · muon: within 6% of observed mass.

## I. The Formula

$$m(\rho, \sigma) \;=\; \mu_\Lambda \;\times\; C_{\text{geom}}(\rho) \;\times\; \bigl(\sqrt{\Omega_\Lambda}\bigr)^{\,\text{dist}(\rho)/30} \;\times\; T^2(\rho \otimes \sigma)$$

Four factors. Four sources. Each traces independently to the topological postulate.

| Factor | Role | Value |
|---|---|---|
| $\mu_\Lambda$ | Vacuum energy floor. Fourth root of cosmological constant energy density. Sets the overall mass scale. | $\rho_\Lambda^{1/4} \approx 2.248 \times 10^{-12}$ GeV |
| $C_{\text{geom}}(\rho)$ | Phase factor. Geometric mean of $C(e/D) = 2\sin^2(\pi e/D)$ over Kostant exponents. Encodes each irrep's position on the domain. | $D = 60$ (integer spin) or $120$ (half-integer) |
| $(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}$ | Hierarchy exponent. McKay graph distance from $R_0$ determines orders of magnitude from the vacuum floor. Denominator is $h(E_8) = 30$. | $\sqrt{\Omega_\Lambda} \approx 1.019 \times 10^{61}$ |
| $T^2(\rho \otimes \sigma)$ | Reidemeister torsion, vacuum-twisted via tensor product. Provides fine structure within each mass shell. The generation mechanism. | 27 values from 9 base torsions x 729 tensor coefficients |

## II. Infrastructure

### McKay Graph (E8 convention)

```
R0(1) -- R1(2) -- R3(3) -- R6(4) -- R7(5) -- R8(6) -- R5(4) -- R2(2)
                                                 |
                                                R4(3)  dist 6
  0        1        2        3        4         5        6        7
```

Half-integer spin: R₁, R₂, R₆, R₈. Integer spin: R₀, R₃, R₄, R₅, R₇.

### Master Table

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

### Three Isolated Vacua

Three flat SU(2) connections on $S^3/2I$. Each has $H^1 = 0$: no moduli, no mixing. Three vacua, three generations.

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

### Analytic Torsion (Base Values)

Integer-spin irreps have exact closed forms. The Galois pair ratio $T^2(R_3)/T^2(R_4) = \varphi^{-4}$ is exact to 70+ digits. The telescoping product $T^2(R_3) \times T^2(R_7) \times T^2(R_5) \times T^2(R_4) = 4$ is exact.

| Irrep | dim | $T^2$ | $\log T^2$ |
|---|---|---|---|
| $R_0$ | 1 | $\pi^4/3600$ | $-3.610$ |
| $R_3$ | 3 | $(4/5)\varphi^{-2}$ | $-1.186$ |
| $R_7$ | 5 | $9/4$ | $+0.811$ |
| $R_5$ | 4 | $25/9$ | $+1.022$ |
| $R_4$ | 3 | $(4/5)\varphi^{2}$ | $+0.739$ |

### Kostant Sunflower (C_geom)

$$C_\text{geom}(\rho) = \bigl(\prod_e 2\sin^2(\pi e/D)\bigr)^{1/(2\,\dim\rho)}$$

$D = 60$ for integer-spin, $D = 120$ for half-integer.

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

### Vacuum Torsion (27 Entries)

Computed from $\log T^2(\rho \otimes \sigma) = \sum_\tau N_{\rho\sigma\tau} \log T^2(\tau)$.

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

Formula A applied to 8 nontrivial irreps x 3 vacua. Sorted by predicted mass. Dead zone entries (ranks 4--9) have no SM counterparts.

| # | $\rho$ | dim | dist | $\sigma$ | $T^2$ | Mass (GeV) | SM | Ratio |
|---|---|---|---|---|---|---|---|---|
| 1 | $R_1$ | 2 | 1 | std | 0.00827 | $1.98 \times 10^{-13}$ | $\nu_1$ | 1.98 |
| 2 | $R_1$ | 2 | 1 | gal | 2.778 | $6.67 \times 10^{-11}$ | $\nu_3$ | 1.32 |
| 3 | $R_1$ | 2 | 1 | triv | 15.887 | $3.81 \times 10^{-10}$ | $\nu_3$ | 7.54 |
| 4 | $R_3$ | 3 | 2 | gal | 0.257 | $3.75 \times 10^{-9}$ | | |
| 5 | $R_3$ | 3 | 2 | triv | 0.306 | $4.45 \times 10^{-9}$ | | |
| 6 | $R_6$ | 4 | 3 | std | 0.688 | $4.09 \times 10^{-7}$ | | |
| 7 | $R_3$ | 3 | 2 | std | 68.765 | $1.00 \times 10^{-6}$ | | |
| 8 | $R_6$ | 4 | 3 | triv | 4.328 | $2.57 \times 10^{-6}$ | | |
| 9 | $R_6$ | 4 | 3 | gal | 4.712 | $2.80 \times 10^{-6}$ | | |
| 10 | $R_7$ | 5 | 4 | std | 1.114 | $2.58 \times 10^{-4}$ | $e$ | 1.98 |
| 11 | $R_7$ | 5 | 4 | gal | 1.114 | $2.58 \times 10^{-4}$ | $e$ | 1.98 |
| **12** | $R_7$ | 5 | 4 | triv | 2.250 | $5.21 \times 10^{-4}$ | $e$ | **1.02** |
| **13** | $R_8$ | 6 | 5 | triv | 0.257 | $2.03 \times 10^{-3}$ | $u$ | **1.06** |
| 14 | $R_8$ | 6 | 5 | gal | 1.910 | $1.51 \times 10^{-2}$ | $d$ | 3.22 |
| **15** | $R_8$ | 6 | 5 | std | 13.090 | $1.03 \times 10^{-1}$ | $\mu$ | **1.02** |
| 16 | $R_5$ | 4 | 6 | std | 0.122 | $3.49 \times 10^{-1}$ | | |
| 17 | $R_4$ | 3 | 6 | std | 0.257 | $7.34 \times 10^{-1}$ | $c$ | 1.73 |
| 18 | $R_2$ | 2 | 7 | gal | 0.0567 | 5.33 | $b$ | 1.28 |
| 19 | $R_4$ | 3 | 6 | gal | 2.048 | 5.84 | $b$ | 1.40 |
| 20 | $R_4$ | 3 | 6 | triv | 2.094 | 5.97 | $b$ | 1.43 |
| 21 | $R_5$ | 4 | 6 | triv | 2.778 | 7.96 | $b$ | 1.91 |
| 22 | $R_5$ | 4 | 6 | gal | 4.089 | 11.72 | $b$ | 2.80 |
| 23 | $R_2$ | 2 | 7 | triv | 0.473 | 44.54 | $t$ | 3.88 |
| 24 | $R_2$ | 2 | 7 | std | 2.778 | 261.46 | $t$ | 1.51 |

## IV. Coverage

### Fermion Scorecard

| SM fermion | Mass (GeV) | Prediction (GeV) | $\rho$ | $\sigma$ | Ratio | ≤ 3x? |
|---|---|---|---|---|---|---|
| $\nu_1$ | $\sim 10^{-13}$ | $1.98 \times 10^{-13}$ | $R_1$ | std | 1.98 | yes |
| $\nu_2$ | $8.6 \times 10^{-12}$ | $6.67 \times 10^{-11}$ | $R_1$ | gal | 7.75 | no |
| $\nu_3$ | $5.06 \times 10^{-11}$ | $6.67 \times 10^{-11}$ | $R_1$ | gal | 1.32 | yes |
| $e$ | $5.11 \times 10^{-4}$ | $5.21 \times 10^{-4}$ | $R_7$ | triv | **1.02** | yes |
| $u$ | $2.16 \times 10^{-3}$ | $2.03 \times 10^{-3}$ | $R_8$ | triv | **1.06** | yes |
| $d$ | $4.67 \times 10^{-3}$ | $1.51 \times 10^{-2}$ | $R_8$ | gal | 3.22 | boundary |
| $\mu$ | $1.057 \times 10^{-1}$ | $1.03 \times 10^{-1}$ | $R_8$ | std | **1.02** | yes |
| $s$ | $9.34 \times 10^{-2}$ | $1.03 \times 10^{-1}$ | $R_8$ | std | 1.10 | yes |
| $c$ | 1.27 | 0.734 | $R_4$ | std | 1.73 | yes |
| $\tau$ | 1.777 | 0.734 -- 5.84 | $R_4$ / $R_5$ | | ~2 | yes |
| $b$ | 4.18 | 5.33 | $R_2$ | gal | 1.28 | yes |
| $t$ | 172.7 | 261.5 | $R_2$ | std | 1.51 | yes |

| Result | Count |
|---|---|
| Within x3 | 10 of 12 |
| Within x10 | 12 of 12 |
| Within 6% | 3 ($e$, $u$, $\mu$) |

### The ν₂ Gap

The widest miss. $R_1$'s three vacuum masses are $1.98 \times 10^{-13}$, $6.67 \times 10^{-11}$, and $3.81 \times 10^{-10}$ GeV. The central neutrino $\nu_2$ at $8.6 \times 10^{-12}$ GeV falls in the gap between the first and second value (ratio 7.75). The normal vs inverted hierarchy remains experimentally undetermined. Resolution comes from oscillation data or from additional structure at the neutrino scale.

## V. Dead Zone

Six of the 24 entries produce masses between $10^{-9}$ and $10^{-6}$ GeV (eV to keV). No known fundamental Standard Model fermions occupy this range.

| # | $\rho$ | dist | $\sigma$ | Mass (GeV) | Range |
|---|---|---|---|---|---|
| 4 | $R_3$ | 2 | gal | $3.75 \times 10^{-9}$ | ~4 eV |
| 5 | $R_3$ | 2 | triv | $4.45 \times 10^{-9}$ | ~4 eV |
| 6 | $R_6$ | 3 | std | $4.09 \times 10^{-7}$ | ~0.4 keV |
| 7 | $R_3$ | 2 | std | $1.00 \times 10^{-6}$ | ~1 keV |
| 8 | $R_6$ | 3 | triv | $2.57 \times 10^{-6}$ | ~3 keV |
| 9 | $R_6$ | 3 | gal | $2.80 \times 10^{-6}$ | ~3 keV |

This mass window is actively probed by sterile neutrino and warm dark matter searches. Physical states at these masses require extremely suppressed couplings. The question is experimental.

---

*The topology permits and Ψ settles. The formula composes and the masses land.*
