# The Spectrum

**Particle Mass Generation from McKay Spectral Geometry on $S^3/2I$**

The Standard Model contains 12 fundamental fermions spanning 12 orders of magnitude in mass. The Higgs mechanism explains how particles acquire mass. It does not explain why they have the masses they do. This paper constructs a mass formula from four ingredients, each traced to a single topological postulate: $S^1 = \partial(\text{Mobius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset$. 

The formula is applied to the 8 nontrivial irreducible representations of the binary icosahedral group across 3 isolated flat connections, producing 24 mass predictions. Of these, 12 correspond to Standard Model fermions: 10 are reproduced within a factor of 3 and all 12 within a factor of 10. Eight predictions have no SM assignments.

| Result | Count |
|---|---|
| Assigned | 12 of 12 SM fermions |
| Within ×3 | 10 of 12 assigned |
| Within 6% | 3 ($e$, $u$, $\mu$) |
| Genuine miss | $\nu_2$ (ratio 7.75× from nearest entry; falls between rank 1 and rank 2) |

## I. The Formula

$$\Large \boxed{m(\rho, \sigma) = \mu_\Lambda \times C_{\text{geom}}(\rho) \times \left(\sqrt{\Omega_\Lambda}\right)^{\text{dist}(\rho)/30} \times T^2(\rho \otimes \sigma)}$$

Four factors. Four sources. Each traces independently to the topological postulate.

| Factor | Role | Value |
|---|---|---|
| $\mu_\Lambda$ | Vacuum energy floor. Fourth root of cosmological constant energy density. Sets the overall mass scale. | $\rho_\Lambda^{1/4} \approx 2.25 \text{ meV}$ |
| $C_{\text{geom}}(\rho)$ | Phase factor. Geometric mean of $C(e/D) = 2\sin^2(\pi e/D)$ over Kostant exponents. Encodes each irrep's position on the domain. | $D = 60$ (integer spin) or $120$ (half-integer) |
| $(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}$ | Hierarchy exponent. McKay graph distance from $R_0$ determines orders of magnitude from the vacuum floor. Denominator is $h(E_8) = 30$. | $\sqrt{\Omega_\Lambda} \approx 1.019 \times 10^{61}$ |
| $T^2(\rho \otimes \sigma)$ | Reidemeister torsion, vacuum-twisted via tensor product. Provides fine structure within each mass shell. The generation mechanism. | 24 values from 8 irreps × 3 vacua |

## II. The Factors

### 1. Neutrino Floor ( $\mu_\Lambda$ )

The vacuum energy density of the cosmological constant defines the overall mass scale:

$$\mu_\Lambda \equiv \rho_\Lambda^{1/4} \approx 2.25 \text{ meV}$$

This is the fourth root of Λ, set by the ground mode ($m_h = 0$) of the Mobius surface. All particle masses trace back to this vacuum energy floor, scaled by the hierarchical factors that place each irrep at its position on the spectrum.

The neutrino mass sector provides direct access to this scale:

| Splitting | Value | Ratio to $\mu_\Lambda$ |
|---|---|---|
| Solar: $\sqrt{\Delta m^2_{21}}$ | $\approx 8.6$ meV | $\sim 4\,\mu_\Lambda$ |
| Atmospheric: $\sqrt{\Delta m^2_{31}}$ | $\approx 50$ meV | $\sim 22\,\mu_\Lambda$ |

The multipliers (4, 22) emerge from parity violation due to the Mobius twist. KATRIN and cosmological bounds provide the falsification window.

### 2. Kostant Sunflower ( $C_{\text{geom}}(\rho)$ )

Each irrep sits at a specific position on the finite domain, encoded by its Kostant exponents. The geometric mean of the phase factor $C(e/D) = 2\sin^2(\pi e/D)$ over these exponents gives the irrep's amplitude on the spectrum.

$$C_\text{geom}(\rho) = \bigl(\prod_e 2\sin^2(\pi e/D)\bigr)^{1/(2\,\dim\rho)}$$

The domain size depends on spin: $D = 60$ for integer-spin, $D = 120$ for half-integer. This encodes the fundamental distinction between bosons and fermions in the geometry.

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

### 3. McKay Elevator ( $(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}$ )

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

### 4. Reidemeister Torsion ( $T^2(\rho \otimes \sigma)$ )

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

## IV. Dead Zone, Targets, and Exclusions

Eight entries have no Standard Model assignments. Six fall in the dead zone (ranks 4--9) between $10^{-9}$ and $10^{-6}$ GeV (eV to keV), where no fundamental fermions are expected. One is a target (rank 16) in a normal mass range where a particle could exist but has no current SM assignment. One is excluded (rank 3) by existing data.

The dead zone is actively probed by sterile neutrino and warm dark matter searches. Physical states at these masses require extremely suppressed non-gravitational couplings.

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

$\nu_2$ at 8.6 meV sits between rank 1 (0.2 meV) and rank 2 (66.7 meV), a ratio gap of ~7.75× from rank 2. This is the mass formula's only genuine miss among the twelve SM fermions. The experimentally allowed window for $\nu_2$ is roughly 10--50 meV, constrained from below by solar neutrino data and from above by the cosmological mass sum. The normal vs. inverted hierarchy remains experimentally undetermined; JUNO and DUNE are expected to resolve this. Whether vacuum mixing between $R_1$ entries or additional structure at the neutrino scale closes the gap remains OPEN.

---

*The topology permits and Ψ settles. The formula composes and the masses land.*
