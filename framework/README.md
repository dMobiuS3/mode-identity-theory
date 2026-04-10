/ **[`main/`](../README.md)** / **[`cosmos/`](../cosmos/)** / **[`spectrum/`](../spectrum/)** /

---

# Mode Identity Theory

MIT was a topological thought formed on philosophical grounds before any prediction was computed. Waves were fundamental before any matter was consulted, and nothing was tuned besides Plato after the fact.

One postulate ($S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$, $\partial S^3 = \emptyset$), three constants ($c$, $\hbar$, $G$), two measured scales, one borrowed parameter, zero free parameters. Einstein's field equations and Standard Model particle content are unchanged. MIT provides what GR leaves undefined: boundary conditions.

From this: $\Lambda$ at 2%, three gauge couplings at 0.5%/1.4%/0.4%, $H_0$ tension at <1%, 10 of 12 fermion masses within $\times 3$, three particle generations from three topological vacua, and a mass gap from positive curvature. Two predictions separate the framework from alternatives: $a_0(z) \propto H(z)$ while $\Lambda$ remains constant. Falsification criteria are pre-registered to Euclid DR1.

## The Firing Order

Each step depends on the one before; nothing later exists independently from what came prior.

1. Topology sets what is possible
2. Embedding defines the structure
3. The cosmic wave expresses the boundary
4. Time is phase of the wave
5. Sampling locates the observer on the domain
6. The observable is the output; no value precedes the sample

## Inputs

Three constants fix the physics. Two measurements set the size. One borrowed parameter locates the time.

**Primitives**

| Const. | Value | Role |
|---|---|---|
| $c$ | 299,792,458 m/s | Propagation rate on the temporal edge $S^1$ |
| $\hbar$ | $1.055 \times 10^{-34}$ J s | Action quantum; converts mode number to energy |
| $G$ | $6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² | Curvature-energy dictionary at the Planck floor ($n = 0$) |

**Measured scales**

| Scale | Value | Role |
|---|---|---|
| $R_\Lambda$ | $\approx 5.3$ Gpc | De Sitter horizon radius; sets the size of the domain |
| $L_\text{fund}$ | $\approx 2.1$ Gpc | CMB low- $\ell$ cutoff; sets the cavity mode. See [cmb-anomalies](../cosmos/cmb-anomalies.md) |

**Concordance parameter**

| Parameter | Value | Role |
|---|---|---|
| $\Omega_m$ | 0.315 | Matter density fraction; used solely to locate the present epoch ($t_\text{now} = 5.22$ rad) |

**Derived**

| Const. | Definition | Value |
|---|---|---|
| $\ell_P$ | $\sqrt{\hbar G/c^3}$ | $1.616 \times 10^{-35}$ m |
| $t_P$ | $\ell_P/c$ | $5.391 \times 10^{-44}$ s |
| $a_P$ | $c/t_P$ | $5.561 \times 10^{51}$ m/s² |
| $\Omega_\Lambda$ | $(R_\Lambda/\ell_P)^2$ | $\approx 10^{122}$ * |

> * $\Omega_\Lambda$ here is the Planck-area count on the de Sitter horizon, not the standard cosmological density fraction ($\Omega_\Lambda^\text{ΛCDM} \approx 0.685$). The two are related by $\Omega_\Lambda = 3/(\Lambda \cdot \ell_P^2) \sim 10^{122}$.

## The Topology

$$\Large {S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset}$$

A temporal edge bounds a non-orientable surface embedded in a closed space. The space has no boundary. Two uniqueness theorems force the manifold triad: the classification of compact surfaces forces the Möbius strip, and the Poincaré theorem forces $S^3$. The postulate has one realization.

**[Visualize the Topology](https://dmobius3.github.io/mode-identity-theory/framework/topology.html)**

### Space

$S^3$ is the only simply connected closed 3-manifold (Poincaré). It is diffeomorphic to SU(2) and admits a spin structure. The space has no boundary:

$$\Large {\partial S^3 = \emptyset}$$

The hierarchy terminates here. "What's outside?" is malformed; there is no boundary from which to observe.

### Surface

The Möbius strip is the minimal non-orientable surface with $S^1$ boundary. By the classification of compact surfaces, a connected non-orientable manifold with a single boundary component is formed by removing a disk from the connected sum of $k$ crosscaps. The Möbius strip is the minimal case ($k = 1$), unique by surface classification. Non-orientability produces three consequences:

| Consequence | Mechanism |
|---|---|
| Anti-periodic BC | Sections of the orientation bundle acquire a sign flip: $\psi(y + \pi R_\Lambda) = -\psi(y)$ |
| Half-integer spectrum | Mode numbers $\nu = 1/2, 3/2, 5/2, \ldots$; the constant mode is forbidden |
| $\mathbb{Z}_2$ holonomy | The normal direction reverses under one traversal |

Orientable surfaces produce none of these.

The eigenvalue problem $-\partial_y^2 \psi = \lambda \psi$ under the anti-periodic BC requires $e^{ik\pi R_\Lambda} = -1$, giving $k = (2m+1)/R_\Lambda$. Defining the mode number $\nu = kR_\Lambda/2$, the allowed values are $\nu = 1/2, 3/2, 5/2, \ldots$: half-integers in this normalization. The constant mode ($k = 0$) is forbidden. The field $\psi$ is a section of the orientation line bundle: the unique nontrivial real line bundle on a non-orientable surface, whose sections pick up a sign flip under the orientation-reversing identification. Matter is fermionic because the surface is non-orientable and the physical field couples to its orientation structure.

### Temporal Edge

$S^1$ is the boundary of the Möbius surface. The strip has longitudinal period $L = \pi R_\Lambda$ (one lap); the boundary $S^1$ traverses the strip twice before closing, giving geometric circumference $2L = 2\pi R_\Lambda$. The edge inherits the anti-periodic boundary condition. This is where time advances and where the observer is anchored.

The chronon and standing wave period operate in the phase parameter $t \in [0, 4\pi]$, not in geometric length. The factor $4\pi$ is the anti-periodic wave period (two sign-flip traversals), dimensionless.

### The Observable Domain

The physical space is $S^3/2I$: the hypersphere modulo the binary icosahedral group $2I$, with $|2I| = 120$. The discrete subgroups of SU(2) $\cong S^3$ are classified: cyclic and binary dihedral families (infinite, parameterized by $n$) and three exceptional groups (binary tetrahedral $|2T| = 24$, binary octahedral $|2O| = 48$, binary icosahedral $|2I| = 120$). The mode spectrum requires the finest discrete partition compatible with $S^3$; $2I$ is selected as the largest exceptional discrete subgroup, giving maximum resolution.

Four auxiliary paths converge on this number (three independent):
1. Group theory of $S^3$ gives $|2I| = 120$ directly
2. The least common multiple of the first five Fibonacci numbers: $\text{lcm}(1,2,3,5,8) = 120$
3. The consonance ratios of musical harmony independently yield $\text{lcm} = 120$
4. The $(2,3,5)$ branch orders of the icosahedron are consecutive Fibonacci numbers satisfying $2+3=5$: the unique Platonic solid whose symmetry orders obey the Fibonacci recurrence

**The 120 domain** is the mode spectrum's resolution. Fermions see all 120 positions but observation squares the wavefunction: $|\psi(\Theta+1)|^2 = |\psi(\Theta)|^2$ erases the anti-periodic sign. The squaring projects $2I \to I$ ($|I| = 60$), halving the resolution.

| Grid | Positions | Minimum step | Observables |
|---|---|---|---|
| Full domain | 120 | $1/120$ | $a_0$ (dynamical) |
| Bosonic projection | 60 | $2/120$ | $H_0$, $\Lambda$, $\alpha$ (photon-mediated) |

**The chronon** is the smallest phase advance the domain can register:

$$\Delta t_{\min} = \frac{4\pi}{120} = \frac{\pi}{30}$$

**The minimum action** $\Delta S_{\min} = \hbar\pi/30$: frame-independent by construction ($\hbar$ is invariant; $\pi/30$ is a pure number set by the topology, not by a coordinate choice).

### Confinement

Positive Ricci curvature on $S^3$ means every coexact gauge fluctuation around a flat connection has a minimum eigenvalue. The Weitzenböck identity on the Hodge Laplacian gives $\lambda \geq 2/R_\Lambda^2 > 0$. The mass gap exists and is at least $2/R_\Lambda^2$; the actual gap at the trivial and standard vacua is $4/R_\Lambda^2$. Confinement is geometric.

### Three Generations

Flat SU(2) connections on $S^3/2I$ are classified by conjugacy classes of homomorphisms from $2I$ into SU(2). Exactly three exist. Each is isolated ($H^1 = 0$): no continuous moduli, no Goldstone bridges between families.

| Vacuum | Mass gap | Source | Role |
|---|---|---|---|
| Trivial | $4/R_\Lambda^2$ | Flat connection | Generation 1 |
| Standard | $4/R_\Lambda^2$ | Irreducible connection | Generation 2 |
| Galois | $36/R_\Lambda^2$ ($9\times$) | Galois conjugate connection | Generation 3 |

Three particle generations from three topological vacua. Full derivation in [Yang-Mills](../spectrum/yang-mills.md).

### The Mass Formula

Four factors, each traced independently to the postulate:

$$\Large m(\rho, \sigma) = \mu_\Lambda \times C_{\text{geom}}(\rho) \times (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \times T^2(\rho \otimes \sigma)$$

| Factor | Role | Source |
|---|---|---|
| $\mu_\Lambda = \rho_\Lambda^{1/4} \approx 2.25$ meV | Vacuum energy floor; overall mass scale | Fourth root of $\Lambda$; ground mode of Möbius surface |
| $C_\text{geom}(\rho)$ | Phase position on the domain | Geometric mean of $C(e/D)$ over Kostant exponents |
| $(\sqrt{\Omega_\Lambda})^{\text{dist}/30}$ | Hierarchy; orders of magnitude from vacuum floor | McKay graph distance; $h(E_8) = 30$ as denominator |
| $T^2(\rho \otimes \sigma)$ | Fine structure within each mass shell; generation splitter | Reidemeister torsion; $T^2(R_3)/T^2(R_4) = \varphi^{-4}$ exact |

Applied to 8 nontrivial irreps across 3 vacua, the formula produces 24 mass entries. 12 map to Standard Model fermions; 10 land within a factor of 3; three (electron, up quark, muon) land within 6%. Full derivation in [mass-spectrum](../spectrum/mass-spectrum.md).

### Particle Identity

The icosahedron carries three stabilizer subgroups. Restricting each irrep to these subgroups assigns physical identity.

| Stabilizer | Order | Physical content | Mechanism |
|---|---|---|---|
| Face ($Z_3$) | 3 | Color: singlet (lepton) vs triplet (quark) | Generation-independent; face geometry identical from all three vacua |
| Edge ($Z_4$) | 4 | Spin-statistics: $D = 120$ (half-int) vs $D = 60$ (int) | Complex vs real $Z_4$ content |
| Vertex ($Z_5$) | 5 | Electroweak interface | Galois conjugate vacua $R_1$, $R_2$ differ in $Z_5$ content |
| Face/Edge | 3/2 | Gravity: Gauss-Codazzi conversion | Surface eigenvalue to space observable |
| Vertex $\times$ twist | $\cos(\pi/10)$ | Weak coupling correction | Dodecahedral defect $\pi/5$, halved by Möbius $\mathbb{Z}_2$ |

The three stabilizer orders are the primes dividing $|2I| = 120$. They generate color, domain, and the electroweak interface. The mass formula computes how heavy. The stabilizer structure says what.

## The Cosmic Standing Wave

Anti-periodicity, the initial-maximum condition ($\Psi(0) = +1$), and ground-state selection ($m_h = 0$) together fix:

$$\Large {\Psi = \cos(t/2)}$$

| Condition | Selects | Why |
|---|---|---|
| Anti-periodic BC | Period $4\pi$ | Two traverses to restore sign |
| $\Psi(0) = +1$ | Cosine over sine | $t = 0$ at amplitude maximum; $\partial_t\Psi\|_{t=0} = 0$ |
| Ground state $m_h = 0$ | No higher harmonics | Isotropy ($10^{-5}$) and orthogonality (Gpc integration) |

The cosmic phase $t = 4\pi\, T/T_\text{cycle}$ where $T$ is cosmic proper time and $T_\text{cycle} \approx 33.2$ Gyr from the Friedmann integral over $L_\text{fund}$.

### The Present Epoch

$$\Large t_\text{now} \approx 5.22 \text{ rad} \qquad \delta \equiv t - 2\pi = -1.06 \text{ rad}$$

| $\Psi$ | Step | $t$ (rad) | Epoch | ~Gyr |
|---|---|---|---|---|
| $+1$ | 0 | 0 | Initial | 0 |
| $0$ | 30 | $\pi$ | First crossing | 8.3 |
| $-0.86$ | ~50 | 5.22 | **Present** | **13.8** |
| $-1$ | 60 | $2\pi$ | Turnaround | 16.6 |
| $0$ | 90 | $3\pi$ | Second crossing | 24.9 |
| $+1$ | 120 | $4\pi$ | Completion | 33 |

The bounded topology implies a standing wave, not heat death. The second half of the cycle is the universe settling into resonance. Turnaround at $t = 2\pi$ produces the same observational signature as phantom crossing in fluid-based dark energy models; the corresponding redshift $z_\text{cross} \approx 0.663$ follows from $\delta$. Full derivation in [dark-energy](../cosmos/dark-energy.md).

## Cosmic Scale

### The Scale Hierarchy

$\Omega_\Lambda$ is fixed by $\Lambda$ and epoch-independent. The Hubble scale evolves:

$$\Omega_H(z) \equiv \left(\frac{R_H(z)}{\ell_P}\right)^2, \quad R_H = c/H(z)$$

At the present epoch, $\Omega_H \approx \Omega_\Lambda \approx 10^{122}$. The coincidence is structural: the observer sits near the temporal midpoint of $\Psi$.

### The Observer

The bounded domain spans from $\Omega \sim 10^{122}$ (horizon) to $10^0$ (Planck). The IR $\leftrightarrow$ UV fixed point $x = \Omega/x$ gives:

$$\Large x = \sqrt{\Omega} \approx 10^{61}$$

The geometric midpoint between Planck and cosmic scale. This is where observation resolves.

### Manifold Index

Mode intensity dilutes as $(\sqrt{\Omega})^{-n}$. The manifold index $n$ specifies which scale governs the mode being sampled.

| $n$ | Manifold | $\Omega$ | $(\sqrt{\Omega})^{-n}$ | Observables |
|---|---|---|---|---|
| 0 | Planck floor | 1 | 1 | $G$ |
| 1 | Temporal edge $S^1$ | $\Omega_H$ | $10^{-61}$ | $H_0$, $a_0$ |
| 3/2 | Gauss-Codazzi | — | — | $\Lambda_\text{obs}/\Lambda_\text{top} = 3/2$ (geometric conversion) |
| 2 | Möbius surface | $\Omega_\Lambda$ | $10^{-122}$ | $\Lambda$ |
| 3 | Space $S^3$ | $\Omega_\Lambda$ | $10^{-183}$ | Null dark matter detection |

**The scale selection rule.** Edge modes ($n = 1$) reference $\Omega_H(z) = (c/H(z)\ell_P)^2$, which evolves: epoch-dependent observables ($H_0$, $a_0$) live here. Surface and space modes ($n = 2, 3$) reference $\Omega_\Lambda = (R_\Lambda/\ell_P)^2$, which is fixed by the boundary condition: epoch-independent observables ($\Lambda$, null DM) live here. Wrong assignments fail by 61 orders of magnitude.

### Selection Rules

| Observable | Character | $n$ | $\Omega$ | $(\sqrt{\Omega})^{-n}$ |
|---|---|---|---|---|
| $\alpha$ | Epoch-independent, dimensionless | $1/30$ | $\Omega_\Lambda$ | $\Omega_\Lambda^{-1/60}$ |
| $H_0$, $a_0$ | Epoch-dependent | 1 | $\Omega_H$ | $10^{-61}$ |
| $\Lambda$ | Epoch-independent, geometric | 2 | $\Omega_\Lambda$ | $10^{-122}$ |
| Dark matter | Gravity-only | 3 | $\Omega_\Lambda$ | $10^{-183}$ |

Dimensionless couplings ($A_P = 1$) bypass manifold dilution; $n$ is fractional.

## The Phase Operator

Different positions on the standing wave carry different observable amplitude:

$$\Large C(\Theta) = 2\sin^2(\pi\Theta)$$

The anti-periodic ground state is $\psi_0(\Theta) = \sin(\pi\Theta)$. Observable intensity is $|\psi|^2$, normalized to unit mean.

| Position | $C(\Theta)$ | Slope $d\ln C/d\Theta$ | Significance |
|---|---|---|---|
| $\Theta = 0$ (boundary) | 0 | $\to \infty$ | No observable amplitude |
| $\Theta = 1/2$ (antinode) | 2 | 0 | Maximum amplitude; topologically protected |
| $\Theta = 1$ (boundary) | 0 | $\to -\infty$ | No observable amplitude |

$\Lambda$ sits at the antinode: slope exactly zero. Environmental perturbations leave it unmoved. The cosmological constant is topologically fixed. Full derivation in [cosmological-constant](../cosmos/cosmological-constant.md).

## Fibonacci Wells

Fibonacci positions minimize destructive interference on the 120 domain (Hurwitz: $\varphi$ is hardest to approximate rationally). Below $F_7$, amplitude is indistinguishable from noise. $F_7 = 13$ is the unique well satisfying Fibonacci stability, amplitude above the noise floor, and $\gcd(13, 120) = 1$.

Three constraints force the observable assignments. First, the manifold index separates edge modes ($n = 1$, epoch-dependent: $H_0$, $a_0$) from surface modes ($n = 2$, epoch-independent: $\Lambda$). Second, the bosonic projection: photon-mediated observables access only the 60-grid (even numerators survive $2I \to I$); dynamical observables access the full 120. Third, $\Lambda$ sits at the antinode (60/120) by eigenvalue identity. Of the remaining wells, only 34/120 has an even numerator and is therefore visible on the bosonic grid, forcing $H_0$. The well 13/120 requires the full 120-grid ($\gcd(13,120) = 1$), making it accessible only to dynamical (non-photon-mediated) observation, forcing $a_0$. The table below summarizes these forced outcomes.

| $F_n$ | Grid | Well | $C(\Theta)$ | Observable | Assignment logic |
|---|---|---|---|---|---|
| $F_7$ | 60R | 13/60 | 0.792 | $\alpha$ | Bosonic projection of 13/120; photon-mediated |
| $F_7$ | 120 | 13/120 | 0.223 | $a_0$ | Coprime ($\gcd(13,120)=1$); dynamical, full domain |
| $F_8$ | 120 | 21/120 | 0.55 | Unassigned | — |
| $F_9$ | 120 | 34/120 | 1.208 | $H_0$ | Even numerator; only remaining edge-mode well on bosonic grid |
| $F_{10}$ | 120 | 55/120 | 1.97 | Unassigned | — |
| — | 120 | 60/120 | 2.00 | $\Lambda_\text{top}$ | Antinode; ground-state maximality; slope zero |

$H_0$ and $a_0$ occupy different wells on the same edge; their ratio is fixed by position.

$H_0$ and $\Lambda$ occupy different manifolds; their 61-order span is fixed by dimension.

## The Phase Field

The phase position decomposes as $\Theta = \Theta_0 + \Theta_f$, where $\Theta_0$ is the Fibonacci well (fixed) and $\Theta_f$ is the local environmental shift.

| Environment | $\Theta_f$ | Effect |
|---|---|---|
| Global (CMB, BAO) | 0 | Gpc integration erases local structure |
| Inside flat-curve disk galaxy | $2/120$ | One bosonic step; minimum shift the 60-grid can register |

The response is binary: below threshold $\Theta_f = 0$; at or above it $\Theta_f = 2/120$. The coherence scale $L_f = v_c^2/a_0 \approx 13$ kpc for the Milky Way. 

The classification index $\mathcal{T}$ compares the gravitational potential drop across $L_f$ to a critical value $\mathcal{T}_c = 2\xi\, v_c^2/c^2$, where $\xi \approx 0.46$ is the mean potential depth computed from standard halo profiles (isothermal, NFW, Hernquist all give 0.44 to 0.47).

**Closure identity.** Both $\mathcal{T}$ and $\mathcal{T}_c$ scale as $v_c^2$; their ratio is galaxy-independent: $\mathcal{T}/\mathcal{T}_c = 1/\xi \approx 2.2$. Every flat-curve disk crosses the threshold by the same factor.

| Well | $\Theta$ | Step | Slope $\times$ Step | Shift |
|---|---|---|---|---|
| $a_0$ | 13/120 | $1/120$ | $17.7 \times 1/120$ | ~15% |
| $H_0$ | 34/120 | $2/120$ | $5.1 \times 2/120$ | 8.4% |
| $\Lambda_\text{top}$ | 60/120 | $2/120$ | $0 \times 2/120$ | 0% |

The 8.4% shift at the $H_0$ well resolves the Hubble tension: $67.4 \times 1.084 \approx 73$ km/s/Mpc. The distance ladder calibration anchor is set inside the Milky Way's phase field; the CMB gives the unshifted value. Full mechanics in [hubble-tension](../cosmos/hubble-tension.md).

## The Scaling Law

$$\Large {\frac{A}{A_P} \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}}$$

$C(\Theta)$ reads the position axis: where the observable sits on the mode spectrum. 

$(\sqrt{\Omega})^{-n}$ reads the time axis through $\Omega_H$ for edge modes, or the boundary condition through $\Omega_\Lambda$ for surface modes. The observer at $\sqrt{\Omega}$ is the structural midpoint where both axes resolve to finite values. 

Their product yields $A/A_P$: the modal realization; the ratio of the observable amplitude over its Planck scale reference.

**The sample occurs at** $(t, \Theta)$.

### The Assembled Engine

| Observable | $A_P$ | Grid | $\Theta$ | $C$ | $n$ | $A/A_P$ |
|---|---|---|---|---|---|---|
| $\alpha$ | 1 | 60R | 13/60 | 0.792 | $1/30$ | $7.33 \times 10^{-3}$ |
| $a_0$ | $a_P$ | 120 | 13/120 | 0.223 | 1 | $2.2 \times 10^{-62}$ |
| $H_0$ | $t_P^{-1}$ | 120 | 34/120 | 1.208 | 1 | $1.2 \times 10^{-61}$ |
| $\Lambda$ | $\ell_P^{-2}$ | 120 | 60/120 | 2.00 | 2 | $2.9 \times 10^{-122}$ * |

> * The surface eigenvalue $\Lambda_\text{top} = 2/R_\Lambda^2$ is computed directly on the curved totally geodesic metric $ds^2 = dy^2 + \cos^2(y/R_\Lambda)\,dw^2$ and confirmed from below by the Bochner identity; equality is unique. The Gauss-Codazzi conversion $\Lambda_\text{obs} = (3/2)\,\Lambda_\text{top} = 3/R_\Lambda^2$ follows under three conditions: totally geodesic embedding ($K_{ij} = 0$), isotropy (CMB-verified to $10^{-5}$), and de Sitter vacuum (late-time ΛCDM attractor). Agreement with observation: ~2%. Gravity in [the-waltz](../spectrum/the-waltz.md).

$\alpha$ occupies the same well as $a_0$ on the 60R-grid; its exponent is fixed by domain resolution. Full derivation in [fine-structure](../spectrum/fine-structure.md).

The $a_0/H_0$ ratio is locked by well positions: $C(13/120)/C(34/120) = 0.184$. Because both are edge modes referencing $\Omega_H(z)$, the ratio holds at every epoch: $a_0(z) \propto H(z)$. Full derivation in [early-galaxies](../cosmos/early-galaxies.md).

**[Run the Calculations for Yourself](https://dmobius3.github.io/mode-identity-theory/framework/calculator.html)**

### The Gauge Ladder

Dimensionless couplings resolve within the hierarchy at the grid level rather than the manifold level. A single principle assigns each gauge force: the phase slot inherits the grid of the carrier, the exponent slot inherits the grid of the confinement target.

| Force | Phase grid | Exponent grid | Formula | Predicted | Observed | Agreement |
|---|---|---|---|---|---|---|
| EM | 60R (bosonic carrier) | 60R (bosonic charge) | $C(13/60) \cdot \Omega_\Lambda^{-1/60}$ | 0.00733 | 0.00730 | 0.5% |
| Strong | 60R (bosonic carrier) | 120 (confined fermions) | $C(17/60) \cdot \Omega_\Lambda^{-1/120}$ | 0.1162 | 0.1179 | 1.4% |
| Weak | 120 (spinorial carrier) | 120 (fermion transitions) | $C(17/120) \cdot \Omega_\Lambda^{-1/120} \cdot \cos(\pi/10)$ | 0.0339 | 0.0338 | 0.4% |

The Coxeter pair $(13, 17)$ under $h(E_8) = 30$ is forced: all alternative conjugate pairs fail by 93% to 770%. The three forces exhaust the grid ladder (monotone in spinorial content). The fourth rung (spinorial carrier, bosonic target) is structurally closed: it would require reconstructing $\psi$ from $|\psi|^2$, inverting the firing order. Three gauge forces, three rungs, no vacancy to fill. Full derivation in [fine-structure](../spectrum/fine-structure.md).

## Pre-Registered Predictions / Falsification

Three predictions separate this framework from alternatives: a₀(z) tracks H(z) while Λ remains constant, and no non-gravitational dark matter signal will ever fire. Everything else raises or lowers credibility. All values deposited on Zenodo before data release.

### Primary (any one kills the framework)

| Prediction | MIT value | Falsified if | Euclid channel |
|---|---|---|---|
| a₀(z) ∝ H(z) | a₀/cH = 0.184 | a₀ consistent with constant at z > 2, ≥2σ | Weak lensing rotation curves across z bins |
| Λ constant | Λ_obs = 3/R_Λ² | Binned ρ_DE(z)/ρ_DE(0) departs from unity at 2σ | SNe + BAO + lensing in redshift bins |
| Null DM detection | Permanent null (n=3 suppressed to 10⁻¹⁸³) | Non-gravitational signal at ≥5σ, replicated | Lensing mass vs. clustering mass comparison |

### Secondary (raise or lower credibility)

| Prediction | MIT value | Falsified if |
|---|---|---|
| Modulation zero-crossing | z_cross = 0.663 | Transition center < 0.4 or > 0.9 at 2σ |
| w(z) shape | Cosine (not linear) | Linear CPL preferred at ΔAIC > 4 |
| No phantom crossing | w_eff > −1 everywhere | Model-independent w < −1 at 2σ |
| H₀ discrete snap | 8.4% shift (67.4 → 73.1) | H₀ distributed continuously across environments |
| 3/2 Gauss-Codazzi | 3Λ_top = 2Λ_obs | Independent R and Λ_obs inconsistent at >3σ |
| Gauge couplings | α, α_s, α_W at 0.5%, 1.4%, 0.4% | Any coupling outside 5% under refined Ω_Λ |
| Three forces only | Fourth rung (120/60) structurally closed | Fourth fundamental force or SUSY partners observed |

**[Judgment Day: October 21, 2026.](https://dmobius3.github.io/mode-identity-theory/framework/euclid-dr1.html)**

Euclid's independent measurement will either end MIT, ΛCDM, or both. Full stop.

---

/ **[`main/`](../README.md)** / **[`cosmos/`](../cosmos/)** / **[`spectrum/`](../spectrum/)** /
