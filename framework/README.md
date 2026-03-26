# Mode Identity Theory

MIT is a shape formed on philosophical grounds before any prediction was computed. Topology determines the structure; observation supplies the scale; every coefficient is a consequence.

## The Shape

$$\Large \boxed{S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset}$$

A temporal edge bounds a non-orientable surface embedded in a closed space. The space has no boundary. Two uniqueness theorems force the structure: the classification of compact surfaces forces the Möbius strip, and the Poincaré theorem forces $S^3$. There was only one choice.

**[Visualize the Shape](https://dmobius3.github.io/mode-identity-theory/tools/topology.html)**

This single choice produces one scaling law that blindly predicts $\Lambda$, $H_0$, $a_0$, and $\alpha$ across 122 orders of magnitude, and 24 fermion mass entries covering all 12 Standard Model fermions.

## The Firing Order

Each step depends on the one before; nothing later exists independently from what came prior.

1. Topology sets what is possible
2. Embedding defines the structure
3. The cosmic wave expresses the boundary
4. Time is phase of the wave
5. Sampling resolves position in the domain
6. Meaning arises only after realization

## Inputs

Three primitive constants and one measured scale. Everything else is accounting.

| Input | Value | Role |
|---|---|---|
| $c$ | 299,792,458 m/s | Propagation rate on the temporal edge $S^1$ |
| $\hbar$ | $1.055 \times 10^{-34}$ J s | Action quantum; converts mode number to energy |
| $G$ | $6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² | Curvature-energy dictionary at the Planck floor ($n = 0$) |
| $R_\Lambda$ | $\approx 5.3$ Gpc | Curvature radius of $S^3$, fixed from the CMB low-$\ell$ cutoff |

### Derived

| Const. | Definition | Value |
|---|---|---|
| $\ell_P$ | $\sqrt{\hbar G/c^3}$ | $1.616 \times 10^{-35}$ m |
| $t_P$ | $\ell_P/c$ | $5.391 \times 10^{-44}$ s |
| $a_P$ | $c/t_P$ | $5.561 \times 10^{51}$ m/s² |
| $\Omega_\Lambda$ | $(R_\Lambda/\ell_P)^2$ | $\approx 10^{122}$ |

## The Topology

### Space

$S^3$ is the only simply connected closed 3-manifold (Poincaré). It is diffeomorphic to SU(2) and admits a spin structure. The space has no boundary:

$$\Large \boxed{\partial S^3 = \emptyset}$$

The hierarchy terminates here. "What's outside?" is malformed; there is no boundary from which to observe.

### Surface

The Möbius strip is the minimal non-orientable surface with $S^1$ boundary (surface classification). Non-orientability is required:

| Requirement | Why non-orientable |
|---|---|
| Anti-periodic BC | $\psi(y + \pi R_\Lambda) = -\psi(y)$; the sign flip requires a surface that reverses orientation |
| Half-integer spectrum | Mode numbers $\nu = 1/2, 3/2, 5/2, \ldots$; orientable surfaces produce only integers |
| $\mathbb{Z}_2$ holonomy | The normal direction cannot be globally defined |

Orientable surfaces satisfy none of these. The Möbius strip is the unique surface satisfying all three.

The eigenvalue problem $-\partial_y^2 \psi = \lambda \psi$ under the anti-periodic BC requires $e^{ik\pi R} = -1$, giving $k\pi R = (2m+1)\pi$. The constant mode is forbidden. Matter is fermionic because the surface is non-orientable.

### Temporal Edge

$S^1$ is the boundary of the Möbius surface: a closed loop with geometric circumference $\pi R_\Lambda$. The edge inherits the anti-periodic boundary condition. This is where time advances and where the observer is anchored.

### The Observable Domain

The physical space is $S^3/2I$: the hypersphere modulo the binary icosahedral group $2I$, the largest exceptional discrete subgroup of SU(2), with $|2I| = 120$.

Four auxiliary paths converge on this number (three independent):
1. Group theory of $S^3$ gives $|2I| = 120$ directly
2. The least common multiple of the first five Fibonacci numbers: $\text{lcm}(1,2,3,5,8) = 120$
3. The consonance ratios of musical harmony independently yield $\text{lcm} = 120$
4. The $(2,3,5)$ branch orders of the icosahedron are consecutive Fibonacci numbers satisfying $2+3=5$: the unique Platonic solid whose symmetry orders obey the Fibonacci recurrence

The 120 domain is the mode spectrum's resolution. The smallest phase advance the domain can register is the chronon:

$$\Delta t_{\min} = \frac{4\pi}{120} = \frac{\pi}{30}$$

The corresponding minimum action $\Delta S_{\min} = \hbar\pi/30$ is absolute: a Lorentz scalar that holds in every frame.

Fermions see all 120 positions but observation squares the wavefunction: $|\psi(\Theta+1)|^2 = |\psi(\Theta)|^2$ erases the anti-periodic sign. The squaring projects $2I \to I$ ($|I| = 60$), halving the resolution.

| Grid | Positions | Minimum step | Observables |
|---|---|---|---|
| Full domain | 120 | $1/120$ | $a_0$ (dynamical) |
| Bosonic projection | 60 | $2/120$ | $H_0$, $\Lambda$, $\alpha$ (photon-mediated) |

### Confinement

Positive Ricci curvature on $S^3$ means every gauge fluctuation has a minimum eigenvalue. The Weitzenböck identity gives $\lambda \geq 2/R_\Lambda^2 > 0$ for all modes. The mass gap exists and equals $2/R_\Lambda^2$. Confinement is geometric. Full derivation in [Yang-Mills on $S^3/2I$](../spectrum/yang-mills.md).

### Three Generations

Flat SU(2) connections on $S^3/2I$ are classified by conjugacy classes of homomorphisms from $2I$ into SU(2). Exactly three exist. Each is isolated ($H^1 = 0$): no continuous moduli, no Goldstone bridges between families.

| Vacuum | Source | Role |
|---|---|---|
| Trivial | Flat connection | Generation 1 |
| Standard | Irreducible connection | Generation 2 |
| Galois | Galois conjugate connection | Generation 3 |

Three particle generations from three topological vacua.

### The Mass Formula

Four factors, each traced independently to the postulate:

$$m(\rho, \sigma) = \mu_\Lambda \times C_{\text{geom}}(\rho) \times (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \times T^2(\rho \otimes \sigma)$$

| Factor | Role | Source |
|---|---|---|
| $\mu_\Lambda = \rho_\Lambda^{1/4} \approx 2.25$ meV | Vacuum energy floor; overall mass scale | Fourth root of $\Lambda$; ground mode of Möbius surface |
| $C_\text{geom}(\rho)$ | Phase position on the domain | Geometric mean of $C(e/D)$ over Kostant exponents |
| $(\sqrt{\Omega_\Lambda})^{\text{dist}/30}$ | Hierarchy; orders of magnitude from vacuum floor | McKay graph distance; $h(E_8) = 30$ as denominator |
| $T^2(\rho \otimes \sigma)$ | Fine structure within each mass shell; generation splitter | Reidemeister torsion; $T^2(R_3)/T^2(R_4) = \varphi^{-4}$ exact |

Applied to 8 nontrivial irreps across 3 vacua, the formula produces 24 mass entries. 12 map to Standard Model fermions; 10 land within a factor of 3; three (electron, up quark, muon) land within 6%. Full predictions and assignments in [spectrum.md](spectrum.md).

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

$$\Large \boxed{\Psi = \cos(t/2)}$$

| Condition | Selects | Why |
|---|---|---|
| Anti-periodic BC | Period $4\pi$ | Two traverses to restore sign |
| $\Psi(0) = +1$ | Cosine over sine | $t = 0$ at amplitude maximum; $\partial_t\Psi\|_{t=0} = 0$ |
| Ground state $m_h = 0$ | No higher harmonics | Isotropy ($10^{-5}$) and orthogonality (Gpc integration) |

The cosmic phase $t = 4\pi\, T/T_\text{cycle}$ where $T$ is cosmic proper time and $T_\text{cycle} \approx 33.2$ Gyr from the Friedmann integral. The concordance matter fraction $\Omega_m = 0.315$ enters solely to locate the present epoch; it appears in no prediction.

### The Present Epoch

$$t_\text{now} \approx 5.22 \text{ rad} \qquad \delta \equiv t - 2\pi = -1.06 \text{ rad}$$

| $\Psi$ | Step | $t$ (rad) | Epoch | ~Gyr |
|---|---|---|---|---|
| $+1$ | 0 | 0 | Initial | 0 |
| $0$ | 30 | $\pi$ | First crossing | 8.3 |
| $-0.86$ | ~50 | 5.22 | **Present** | **13.8** |
| $-1$ | 60 | $2\pi$ | Turnaround | 16.6 |
| $0$ | 90 | $3\pi$ | Second crossing | 24.9 |
| $+1$ | 120 | $4\pi$ | Completion | 33 |

The bounded topology implies a standing wave, not heat death. The second half of the cycle is the universe settling into resonance. Turnaround at $t = 2\pi$ produces the same observational signature as phantom crossing in fluid-based dark energy models; the corresponding redshift $z_\text{cross} \approx 0.663$ follows from $\delta$. Full derivation in [dark-energy.md](../cosmos/dark-energy.md).

## Cosmic Scale

### The Scale Hierarchy

Two scales govern the structure:

| Scale | Definition | Value | Character |
|---|---|---|---|
| $\Omega_\Lambda$ | $(R_\Lambda/\ell_P)^2$ | $\approx 10^{122}$ | Fixed by $\Lambda$; epoch-independent |
| $\Omega_H(z)$ | $(R_H(z)/\ell_P)^2$, where $R_H = c/H(z)$ | $\approx 10^{122}$ at $z \approx 0$ | Evolves with epoch |

At the present epoch, $\Omega_H \approx \Omega_\Lambda$. The coincidence is structural: the observer sits near the temporal midpoint of $\Psi$.

### The Observer

The bounded domain spans from $\Omega \sim 10^{122}$ (horizon) to $10^0$ (Planck). The IR$\leftrightarrow$UV fixed point $x = \Omega/x$ gives:

$$x = \sqrt{\Omega} \approx 10^{61}$$

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

The edge references $\Omega_H$ because the edge is where time happens: epoch-dependent observables evolve. The surface and space reference $\Omega_\Lambda$ because boundary conditions are fixed. Wrong manifold assignments fail by 61 orders of magnitude.

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

$$C(\Theta) = 2\sin^2(\pi\Theta)$$

The anti-periodic ground state is $\psi_0(\Theta) = \sin(\pi\Theta)$. Observable intensity is $|\psi|^2$, normalized to unit mean.

| Position | $C(\Theta)$ | Slope $d\ln C/d\Theta$ | Significance |
|---|---|---|---|
| $\Theta = 0$ (boundary) | 0 | $\to \infty$ | No observable amplitude |
| $\Theta = 1/2$ (antinode) | 2 | 0 | Maximum amplitude; topologically protected |
| $\Theta = 1$ (boundary) | 0 | $\to -\infty$ | No observable amplitude |

$\Lambda$ sits at the antinode: slope exactly zero. Environmental perturbations leave it unmoved. The cosmological constant is topologically fixed.

## Fibonacci Wells

Fibonacci positions minimize destructive interference on the 120 domain (Hurwitz: $\varphi$ is hardest to approximate rationally). Below $F_7$, amplitude is indistinguishable from noise. $F_7 = 13$ is the unique well satisfying Fibonacci stability, amplitude above the noise floor, and $\gcd(13, 120) = 1$.

| $F_n$ | Grid | Well | $C(\Theta)$ | Observable | Assignment logic |
|---|---|---|---|---|---|
| $F_7$ | 60R | 13/60 | 0.792 | $\alpha$ | Bosonic projection of 13/120; photon-mediated |
| $F_7$ | 120 | 13/120 | 0.223 | $a_0$ | Coprime ($\gcd(13,120)=1$); dynamical, full domain |
| $F_8$ | 120 | 21/120 | 0.55 | Unassigned | — |
| $F_9$ | 120 | 34/120 | 1.208 | $H_0$ | Even numerator; only remaining edge-mode well on bosonic grid |
| $F_{10}$ | 120 | 55/120 | 1.97 | Unassigned | — |
| — | 120 | 60/120 | 2.00 | $\Lambda_\text{top}$ | Antinode; ground-state maximality; slope zero |

$H_0$ and $a_0$ occupy different wells on the same edge; their ratio is fixed by position. $H_0$ and $\Lambda$ occupy different manifolds; their 61-order span is fixed by dimension.

## The Phase Field

The phase position decomposes as $\Theta = \Theta_0 + \Theta_f$, where $\Theta_0$ is the Fibonacci well (fixed) and $\Theta_f$ is the local environmental shift.

| Environment | $\Theta_f$ | Effect |
|---|---|---|
| Global (CMB, BAO) | 0 | Gpc integration erases local structure |
| Inside flat-curve disk galaxy | $2/120$ | One bosonic step; minimum shift the 60-grid can register |

The response is binary: below threshold $\Theta_f = 0$; at or above it $\Theta_f = 2/120$. The coherence scale $L_f = v_c^2/a_0 \approx 13$ kpc for the Milky Way. The classification index $\mathcal{T}$ compares the gravitational potential drop across $L_f$ to a critical value $\mathcal{T}_c = 2\xi\, v_c^2/c^2$, where $\xi \approx 0.46$.

**Closure identity.** Both $\mathcal{T}$ and $\mathcal{T}_c$ scale as $v_c^2$; their ratio is galaxy-independent: $\mathcal{T}/\mathcal{T}_c = 1/\xi \approx 2.2$. Every flat-curve disk crosses the threshold by the same factor.

| Well | $\Theta$ | Step | Slope $\times$ Step | Shift |
|---|---|---|---|---|
| $a_0$ | 13/120 | $1/120$ | $17.7 \times 1/120$ | ~15% |
| $H_0$ | 34/120 | $2/120$ | $5.1 \times 2/120$ | 8.4% |
| $\Lambda_\text{top}$ | 60/120 | $2/120$ | $0 \times 2/120$ | 0% |

The 8.4% shift at the $H_0$ well resolves the Hubble tension: $67.4 \times 1.084 \approx 73$ km/s/Mpc. The distance ladder calibration anchor is set inside the Milky Way's phase field; the CMB gives the unshifted value. Full mechanics in [hubble-tension.md](../cosmos/hubble-tension.md).

## The Scaling Law

$$\Large \boxed{\frac{A}{A_P} \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}}$$

$C(\Theta)$ reads the position: where the observable sits on the mode spectrum. $(\sqrt{\Omega})^{-n}$ reads the scale: which manifold, which horizon. The observer at $\sqrt{\Omega}$ is the structural midpoint where both resolve to finite values. Their product is the modal realization ratio.

**The sample occurs at** $(t, \Theta)$.

**[Hear the Engine](https://dmobius3.github.io/mode-identity-theory/tools/engine.html)**

### The Assembled Engine

| Observable | $A_P$ | Grid | $\Theta$ | $C$ | $n$ | $A/A_P$ |
|---|---|---|---|---|---|---|
| $\alpha$ | 1 | 60R | 13/60 | 0.792 | $1/30$ | $7.33 \times 10^{-3}$ |
| $a_0$ | $a_P$ | 120 | 13/120 | 0.223 | 1 | $2.2 \times 10^{-62}$ |
| $H_0$ | $t_P^{-1}$ | 120 | 34/120 | 1.208 | 1 | $1.2 \times 10^{-61}$ |
| $\Lambda$ | $\ell_P^{-2}$ | 120 | 60/120 | 2.00 | 2 | $(3/2) \times 1.95 \times 10^{-122} \approx 2.9 \times 10^{-122}$ |

$\alpha$ occupies the same well as $a_0$ on the 60R-grid; its exponent is fixed by domain resolution.

**[Run the Calculations](https://dmobius3.github.io/mode-identity-theory/tools/calculator.html)**
