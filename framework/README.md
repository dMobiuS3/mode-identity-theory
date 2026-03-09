# The Framework

Matter is wave, sampled. A single topological postulate produces one scaling law. It blindly predicts constants of the universe: $\Lambda$, $H_0$, $a_0$, and $\alpha$, spanning 120 orders of magnitude from $\Lambda \cdot \ell_P^2 \sim 10^{-122}$ to $\alpha \sim 10^{-2}$; and 24 fermion mass entries covering all 12 Standard Model fermions.

## Definitions

### Universal Constants

Three quantities are primitive inputs; all Planck-scale references are derived from them.

**Inputs**

| Const. | Value | Role in MIT |
|---|---|---|
| $c$ | 299,792,458 m/s | Propagation rate on the temporal edge $S^1$ |
| $\hbar$ | $1.055 \times 10^{-34}$ J s | Action quantum; converts mode number to energy |
| $G$ | $6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² | Curvature ↔ energy dictionary at the Planck floor ($n = 0$); not derivable from topology |

**Derived**

| Const. | Definition | Value | Role in MIT |
|---|---|---|---|
| $\ell_P$ | $\sqrt{\hbar G/c^3}$ | $1.616 \times 10^{-35}$ m | UV floor of the bounded domain |
| $t_P$ | $\ell_P/c$ | $5.391 \times 10^{-44}$ s | Reference scale for $H_0$ |
| $a_P$ | $c/t_P$ | $5.561 \times 10^{51}$ m/s² | Reference scale for $a_0$ |

### Three Length Scales

Three geometric scales appear in MIT. They are distinct in origin and claim status; the $\Omega$ scales built from them differ by a factor of $10^{61}$ if conflated.

| Scale | Value | Origin | Status |
|---|---|---|---|
| $L_\text{fund}$ | $\approx 2.1$ Gpc | Derived from CMB low-$\ell$ cutoff: $k_{\min} = \pi^2/2L_\text{fund}$, $\ell_\text{cut} \approx k_{\min}\chi_* - 1/2$ | Derived. Arrow runs observation → $L_\text{fund}$. |
| $R$ | $\approx 5.3$ Gpc | Geometric parameter: the de Sitter horizon radius, fixed by the topology before observables are consulted. $\Lambda_\text{obs} = 3/R_\Lambda^2$ is the prediction; $R_\Lambda = \sqrt{3/\Lambda_\text{obs}}$ is the observational check. | Geometric parameter. Not a primitive input alongside $c$, $\hbar$, $G$. |
| $L_\text{strip}$ | $\approx 16.7$ Gpc | One lap of the Möbius boundary: $L_\text{strip} = \pi R_\Lambda$ | Derived from $R_\Lambda$. |

$L_\text{fund}$ is the CMB-derived fundamental domain scale; where $L$ appears without subscript in the Three Length Scales section it means $L_\text{fund}$. In other sections $L$ is used as a generic length variable and carries no subscript meaning. $R$ is the geometric de Sitter horizon radius; $R_\Lambda$ is the same quantity as it appears in the Scale Hierarchy. The observational check is $R_\Lambda = \sqrt{3/\Lambda_\text{obs}}$; the logical direction is $R_\Lambda \to \Lambda_\text{obs}$. $R$ and $L_\text{fund}$ are two independently motivated scales. The spectral derivation (scalar Laplacian on $S^3/2I$, degree-12 Klein invariant, Heun transverse eigenvalue $\mu_1 = 1.021$) gives $L_\text{strip}/L_\text{fund} = 8.17 \pm 0.1$, recovering 8 to within 2.1%. Whether topology forces $R_\Lambda = 8L_\text{fund}/\pi$ from first principles is open.

## The Firing Order

Mode Identity Theory is built upon a specific order of operation. Each step depends on the one before, and nothing later in the sequence exists independently from what came prior:

1. Topology sets what is possible → 

2. Embedding defines the structure → 

3. The cosmic wave expresses the boundary → 

4. Time is phase of the wave → 

5. Sampling resolves position in the domain → 

6. Meaning arises only after realization

## The Nested Topology

The topology had only one choice. The temporal edge bounds the Möbius surface embedded in hypersphere space; the space has no boundary. Two uniqueness theorems force the structure: the classification of compact surfaces forces the Möbius strip, and the Poincaré theorem forces $S^3$.

$$\Large \boxed{S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset}$$

### The Temporal Edge S¹

The 1D boundary of the Möbius surface is the edge with geometric circumference $L_\text{strip} = \pi R_\Lambda \approx 16.7$ Gpc. The Möbius anti-periodic boundary condition means the wavefunction changes sign after one traverse of the boundary; two traverses are required to restore the original sign. This topological property — a consequence of the $\mathbb{Z}_2$ holonomy — is the origin of the $4\pi$ period: the wave must advance through $4\pi$ of phase to return to its initial amplitude. The edge inherits the anti-periodic boundary condition.

The fundamental domain scale $L_\text{fund} \approx 2.1$ Gpc is distinct from $L_\text{strip}$. It is the minimum-wavelength observable mode scale of the bounded 3D cavity ($S^3/2I$), derived from the CMB low-$\ell$ cutoff. The cosmic phase $t \equiv 2\pi s/L_\text{fund}$ uses the fundamental domain as reference length, where $s$ is an abstract phase coordinate running over the mode structure of the cavity; the $S^1$ edge geometric circumference is $L_\text{strip} \approx 16.7$ Gpc.

### The Möbius Surface

The 2D non-orientable manifold bounded by the edge. Let $y$ denote the coordinate along the twisted direction, with period $L_\text{strip}$. The Möbius $\mathbb{Z}_2$ holonomy admits two boundary condition sectors: periodic $\psi(y+L_\text{strip}) = +\psi(y)$ and anti-periodic $\psi(y+L_\text{strip}) = -\psi(y)$. The anti-periodic sector is selected by observation; matter is fermionic. Fields in the selected sector satisfy:

$$\psi(y + L_\text{strip}) = -\psi(y)$$

Along the twisted direction, the eigenproblem is $-\partial_y^2 \psi = \lambda \psi$. The ansatz $\psi \sim e^{iky}$ under the boundary condition requires:

$$e^{ikL_\text{strip}} = -1 \quad \Rightarrow \quad kL_\text{strip} = (2m + 1)\pi$$

Defining $\nu \equiv kL_\text{strip}/(2\pi)$, then $kL_\text{strip} = (2m+1)\pi$ implies $\nu = m + 1/2$. The mode numbers are half-integers: $\nu = 1/2, 3/2, 5/2, \ldots$ The Möbius surface is the simplest non-orientable 2D manifold with boundary.

| Symbol | Name | Values | Role |
|---|---|---|---|
| $m$ | Harmonic | $0, 1, 2, \ldots$ | Harmonic count |
| $\nu$ | Mode number | $m + 1/2$ | Half-integer from BC |

**Ground state selection.** The structure selects the fundamental harmonic ($m = 0$) by operational definition. Cosmological parameters ($\Lambda$, $H_0$) describe the homogeneous, isotropic background. The ground state is the unique mode with no internal nodes; excited modes ($m > 0$) possess spatial nodes and oscillating polarity. Two arguments fix $m = 0$ for background observables:

| Argument | Mechanism |
|---|---|
| Isotropy | $m > 0$ nodes create $O(1)$ anisotropy; CMB is isotropic to $10^{-5}$ |
| Orthogonality | Cosmological measurements integrate over Gpc volumes; oscillating modes average to zero |

Higher harmonics are excluded for background observables but carry perturbation structure.

### The Hypersphere Space S³

The 3D volume containing the surface. Gravitational coupling only; all other cross-manifold couplings are absent from the derivation.

$$\Large \boxed{\partial S^3 = \emptyset}$$

The hierarchy terminates here. "What's outside?" is malformed; there is no boundary from which to observe.

| Manifold | Boundary | Description |
|---|---|---|
| $S^1$ | $\partial S^1 = \emptyset$ | Closed loop; boundary of Möbius |
| Möbius | $\partial M = S^1$ | Non-orientable; embedded in $S^3$ |
| $S^3$ | $\partial S^3 = \emptyset$ | Orientable space; boundless |

**Uniqueness.** Spin compatibility and non-orientability together force a single topological choice:

*The Edge and Surface* ($S^1$, Möbius): By the classification of compact surfaces, a connected non-orientable manifold with a single boundary component ($S^1$) is formed by removing a disk from the connected sum of $k$ crosscaps. The Möbius strip is the minimal case ($k = 1$), unique by surface classification.

*The Space* ($S^3$): By the Poincaré theorem, $S^3$ is the only simply connected closed 3-manifold. It is diffeomorphic to $\text{SU}(2)$ and admits a spin structure.

*The Terminus* ($\partial S^3 = \emptyset$): The space has no boundary. The hierarchy terminates here.

The physical space is the quotient $S^3/2I$: $S^3$ modulo the binary icosahedral group acting by deck transformations. $S^3$ is the simply connected universal cover; $S^3/2I$ is the multiply connected space whose 120 fundamental domains generate the mode spectrum. The postulate selects the cover; the $2I$ structure is carried by $S^3$ itself as its largest exceptional discrete subgroup. The embedding $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ is formulated on the cover; observables and the mode spectrum live on the quotient $S^3/2I$.

## The Cosmic Standing Wave Ψ

Anti-periodicity, the initial-maximum condition, and ground-state selection together determine the cosmic standing wave. Anti-periodicity is inherited from the Möbius $\mathbb{Z}_2$ holonomy (established above). The initial condition $\Psi(0) = +1$ fixes $t = 0$ as an amplitude maximum. At any maximum of a smooth function, the first derivative vanishes: $\partial_t \Psi|_{t=0} = 0$. This selects cosine over sine — sine has $\partial_t \sin(t/2)|_{t=0} \neq 0$ and would place $t=0$ at zero amplitude. Ground-state selection picks $m = 0$. The three conditions together fix $\Psi = \cos(t/2)$ up to overall sign; the sign is set by the convention $\Psi(0) = +1$.

### Wavelength

A period of $4\pi$ is required to carry the sign from positive through negative and back to positive: $\Psi(t + 4\pi) = \Psi(t)$.

Let $t \equiv 2\pi s/L_\text{fund}$ denote cosmic phase, where $s$ is an abstract phase coordinate running over the mode structure of the 3D cavity; the $S^1$ edge has geometric circumference $L_\text{strip} \approx 16.7$ Gpc. $L_\text{fund}$ is the fundamental domain scale. (At Planck scale, the boundary condition manifests as the spin-1/2 sign flip under $2\pi$ rotation. Their correspondence is the dimensional projection of the same topological constraint.) The standing wave takes the form:

  $$\Large \boxed{\Psi = \cos(t/2)}$$

Cosine is inherited because the universe initiates at maximum amplitude $\Psi = +1$ rather than mid-slope.

### The Present Epoch

The phase definition $t \equiv 2\pi s/L_\text{fund}$ means a full $4\pi$ cycle corresponds to $\Delta s = 2L_\text{fund}$ in the phase coordinate: the mode structure is traversed twice. $L_\text{fund}$ is a comoving scale, derived from the CMB low-$\ell$ cutoff; $s$ therefore maps directly to comoving distance, and the Friedmann integral applies. The fundamental domain scale $L_\text{fund} \approx 2.1$ Gpc translates to a cycle duration $T_\text{cycle} \approx 33.2$ Gyr through the standard Friedmann expansion history ($\Omega_m = 0.315$, $\Omega_\Lambda = 0.685$, $H_0 = 67.4$ km/s/Mpc); the integral is in the companion paper. The topology sets the cycle structure; the expansion history converts comoving distance to cosmic time. With $t_\text{age} = 13.8$ Gyr:

$$t = 4\pi \times \frac{13.8}{33.2} \approx 5.22 \text{ rad}$$

The epoch offset $\delta \equiv t - 2\pi$ measures angular distance from turnaround: $\delta = 5.22 - 6.28 = -1.06$ rad. In the native clock of the 120 domain, the observer sits at step ~50 of 120, approximately 10 chronon steps (2.8 Gyr) before turnaround at step 60.

| $\Psi$ | Step | $t$ (rad) | Epoch | ~Gyr |
|---|---|---|---|---|
| $+1$ | 0 | 0 | Initial | 0 |
| $0$ | 30 | $\pi$ (3.14) | First crossing | 8.3 |
| $-0.86$ | *~50* | $2\pi + \delta$ (5.22) | *Present* | *13.8* |
| $-1$ | 60 | $2\pi$ (6.28) | Turnaround | 16.6 |
| $0$ | 90 | $3\pi$ (9.42) | Second crossing | 24.9 |
| $+1$ | 120 | $4\pi$ (12.57) | Completion | 33 |

**Bounded completion.** The bounded topology implies a different end state than heat death. Anti-periodic boundary conditions select standing-wave solutions. The second half of the cycle ($2\pi \to 4\pi$) is the universe settling into resonance rather than dissipating into void.

**Wave turnaround and phantom crossing.** Turnaround occurs at $t = 2\pi$, where $\Psi = \cos(\pi) = -1$: the wave reaches its amplitude minimum and reverses. This is a turning point of the amplitude; $\Psi = 0$ occurs at $t = \pi$ and $t = 3\pi$. In fluid-based dark energy models, the equation-of-state parameter $w_\text{eff}$ crossing $-1$ is called a phantom crossing. That label attaches to a parameter in those models; MIT's amplitude minimum produces the same observational signature through a different mechanism. The derivation of the corresponding redshift $z_\text{cross} \approx 0.66$ from the phase gap $|\delta| = 1.06$ rad via the Friedmann integral is in the companion paper. Both predictions are pre-registered to Euclid DR1.

## Cosmic Scale

### The Scale Hierarchy

Two scales govern the structure. The de Sitter scale:

$$\Omega_\Lambda \equiv \left(\frac{R_\Lambda}{\ell_P}\right)^2 \approx 10^{122}$$

where $R_\Lambda \approx 5.3$ Gpc is the de Sitter horizon radius, fixed observationally; the framework predicts the coefficient 3, and $\Lambda_\text{obs} = 3/R_\Lambda^2$ is the consistency check. The observational check is $R_\Lambda = \sqrt{3/\Lambda_\text{obs}}$; the logical direction is $R_\Lambda \to \Lambda_\text{obs}$. And the Hubble scale:

$$\Omega_H(z) \equiv \left(\frac{R_H(z)}{\ell_P}\right)^2 \approx 10^{122}\ (z \approx 0)$$

where $R_H(z) = c/H(z)$ is the Hubble radius at redshift $z$, whose scale evolves with time. At the present epoch $t \approx 5.22$ rad, the Hubble horizon converges on the de Sitter horizon: $\Omega_H \approx \Omega_\Lambda$. The coincidence is structural: the observer sits near the temporal midpoint of $\Psi$.

The squared definition reflects horizon area: the relevant degrees of freedom scale with boundary. $\Omega_\Lambda$ is the asymptotic limit; $\Omega_H$ evolves with the Hubble radius.

### The Observer √Ω

The observer occupies $\sqrt{\Omega_H} \approx 10^{61}$ at the present epoch: the geometric mean between cosmic scale ($10^{122}$) and Planck scale ($\sim 10^0$).

**Derivation.** The bounded domain spans from $\Omega \approx 10^{122}$ (horizon) to $10^0$ (Planck). On this domain, consider the IR↔UV symmetry $x \mapsto \Omega/x$. The fixed point satisfies:

$$x = \Omega/x \quad \Rightarrow \quad x^2 = \Omega \quad \Rightarrow \quad x = \sqrt{\Omega}$$

On a log scale, $\sqrt{\Omega} \approx 10^{61}$ is the midpoint: $(122 + 0)/2 = 61$. This is a structural position.

### Structural vs. temporal midpoint

The structural midpoint $\sqrt{\Omega_H} \approx 10^{61}$ is constitutive; it defines *where* observation resolves. The temporal midpoint $t \approx 2\pi$ is contingent; it describes *when* we happen to observe. Both coincide near the present epoch. $S^1$ is the anchor manifold for phase; "observer at $S^1$" means temporal existence is parametrized by the 1D edge.

**Notation.** The dilution factor $\Omega^{-n/2}$ becomes $(\sqrt{\Omega})^{-n}$: the observer's position raised to power $-n$.

### The Scale Factor

Mode intensity dilutes in an embedded manifold:

$$(\sqrt{\Omega})^{-n}$$

The scale $\Omega = (\mathcal{R}/\ell_P)^2$ counts Planck areas on the horizon, where $\mathcal{R}$ is the relevant horizon radius for the observable: $R_H$ for edge modes, $R_\Lambda$ for surface modes (see Selection Rules). The characteristic linear scale of the domain is $\sqrt{\Omega}$. The volume of an $n$-dimensional manifold scales as $V_n \sim (\sqrt{\Omega})^n$. A normalized scalar mode has local intensity $|\psi|^2 \sim (\sqrt{\Omega})^{-n}$.

### Manifold Index

The manifold index $n$ specifies which scale governs the mode being sampled.

| $n$ | Manifold | $\Omega$ | $(\sqrt{\Omega})^{-n}$ | Observables |
|---|---|---|---|---|
| 0 | Planck floor | 1 | $(\sqrt{\Omega})^{0} = 1$ | $G$ (curvature ↔ energy dictionary) |
| 1 | Temporal edge | $\Omega_H$ | $10^{-61}$ | $H_0$, $a_0$, $\Delta t_{\min} = \pi/30$, $\Delta S_{\min} = \hbar\pi/30$ |
| 2 | Möbius surface | $\Omega_\Lambda$ | $10^{-122}$ | $\Lambda$ |
| 3/2 | Gauss-Codazzi conversion | N/A | N/A | Gravity: converts surface eigenvalue $\Lambda_\text{top} = 2/R_\Lambda^2$ to space observable $\Lambda_\text{obs} = 3/R_\Lambda^2$ (geometric conversion, not dilution) |
| 3 | Space | $\Omega_\Lambda$ | $10^{-183}$ | Null "dark matter" |

The access hierarchy follows from boundary structure: $S^1$ is the observer's anchor (direct); Möbius is accessed through its non-orientable twist; $S^3$ has no boundary ($\partial S^3 = \emptyset$). Spatial degrees of freedom enter only through reconstruction.

The $n=3/2$ row is a geometric conversion, distinct from manifold dilution. The coefficient 2 in $\Lambda_\text{top} = 2/R_\Lambda^2$ is the ground-state eigenvalue of the 2D surface scalar Laplacian (established by the Weitzenböck bound and saturated by the ground state). The coefficient 3 in $\Lambda_\text{obs} = 3/R_\Lambda^2$ is the trace of the de Sitter vacuum Einstein equations in 3D space ($R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = 0$ implies $\Lambda = 3/R_\Lambda^2$ for a de Sitter geometry with radius $R_\Lambda$). The Gauss-Codazzi equations at vacuum embedding ($K_{ij}=0$) connect the two eigenvalue problems. The ratio $\Lambda_\text{obs}/\Lambda_\text{top} = 3/2$ follows from these two independent computations; stating it as "ratio of dimensions (3/2)" is a mnemonic for the coefficient values. Full derivation in companion paper. The conversion is purely geometric; $\Omega$ plays no role.

### Why edge uses Ω\_H while surface uses Ω\_Λ

The temporal edge $S^1$ is where time happens; only the edge can reference a quantity that evolves with cosmic time. The Hubble horizon $R_H(z) = c/H(z)$ evolves; therefore epoch-dependent observables ($H_0$, $a_0$) reference $\Omega_H$. The Möbius surface and $S^3$ space are defined by $\Lambda$, which sets the boundary condition itself. Boundary conditions are fixed; therefore epoch-independent observables reference $\Omega_\Lambda$. The space ($n = 3$) scaling of $(\sqrt{\Omega})^{-3} \sim 10^{-183}$ suppresses any non-gravitational signal to observational null.

### Selection Rules

The manifold index, scale, and dilution are determined by the character of the observable:

| Observable | Character | $n$ | $\Omega$ | Why this $\Omega$ | $(\sqrt{\Omega})^{-n}$ |
|---|---|---|---|---|---|
| $\alpha$ | Epoch-ind., dimensionless | $1/30$ | $\Omega_\Lambda$ | Grid-resolution exponent | $\Omega_\Lambda^{-1/60}$ |
| $H_0$, $a_0$ | Epoch-dependent | 1 | $\Omega_H$ | Edge references evolving horizon | $10^{-61}$ |
| $\Lambda$ | Epoch-ind., geometric | 2 | $\Omega_\Lambda$ | Surface BC is fixed | $10^{-122}$ |
| "Dark matter" | Gravity-only | 3 | $\Omega_\Lambda$ | Space has no gauge coupling | $10^{-183}$ |

> Dimensionless couplings ($A_P = 1$) bypass manifold dilution; $n$ is fractional.

**Exclusion test.** Wrong manifold assignments fail by 61 orders of magnitude. $\Lambda$ as an edge mode ($n = 1$) would give $10^{-61}$, not $10^{-122}$. $H_0$ as a surface mode ($n = 2$) would give $10^{-122}$, not $10^{-61}$. The assignments are consistent with selection rules (epoch-dependence, coupling character); wrong assignments fail catastrophically.

## The Phase Operator

### The Phase Operator C(Θ)

Different locations on the standing wave carry different observable amplitude. The phase operator $C(\Theta)$ encodes this variation:

$$C(\Theta) = 2\sin^2(\pi\Theta)$$

This function vanishes at $\Theta = 0$ and $\Theta = 1$ (the boundaries), and reaches maximum $C = 2$ at $\Theta = 1/2$ (the antinode).

**Derivation.** The Möbius $\mathbb{Z}_2$ holonomy admits periodic and anti-periodic sectors. Matter is fermionic; this selects the anti-periodic sector. The constant mode is excluded: $\psi = \text{const}$ requires $\psi(\Theta+1) = +\psi(\Theta)$. The ground state is the lowest allowed mode, with eigenvalue $\lambda_0 = (\pi/L)^2 \neq 0$. The ground state wavefunction satisfying $\psi(\Theta+1) = -\psi(\Theta)$ is:

$$\psi_0(\Theta) = \sin(\pi\Theta)$$

Observable intensity is $|\psi|^2$. The mean is $\int_0^1 \sin^2(\pi\Theta)\,d\Theta = 1/2$. Normalizing to unit mean intensity sets the peak amplitude to 2, yielding $C(\Theta) = 2\sin^2(\pi\Theta)$.

$H_0$ and $a_0$ are both edge modes ($n=1$) with different magnitudes, so the wave must vary with position. Only the anti-periodic sector does; the periodic sector would give $C(\Theta) = 1$ everywhere with no variation.

### Phase Position Θ

Phase position parametrizes where an observable resolves on the mode spectrum; it is distinct from the cosmic phase $t$. The cosmic phase $t$ locates the observer in the standing wave (*when*); the domain position $\Theta$ locates the observable (*where*).

$\Theta$ decomposes as:

$$\Theta = \Theta_0 + \Theta_f$$

where $\Theta_0$ is the Fibonacci well (fixed, geometric) and $\Theta_f$ is the phase field (local, varies by environment). These positions live on a structure with three levels of resolution.

**Resolution Terminology.** The domain is the space and the grid is the sampling. The 60R-grid is what survives to observation, where each level is derived from the topology. The remainder of this section builds them in order.

| Term | What it is | Resolution | Source |
|---|---|---|---|
| 120 domain | Topological structure | 120 positions | $\lvert 2I \rvert = 120$ native to $S^3$ |
| Grid | Discrete sampling of the domain | 120 (fermionic) | Half-integer modes on the domain |
| 60R-grid | Realized observable lattice | 60 positions (even only) | $\lvert\psi\rvert^2$ projects $2I \to I$ |

### The 120 Domain

$C(\Theta)$ is continuous, but the mode spectrum is discrete. Half-integer modes sample discrete positions, and at generic positions they interfere destructively. By Hurwitz's theorem, the golden ratio $\varphi$ is the positive real most poorly approximated by rationals. Its convergents are the Fibonacci sequence. Fibonacci positions are where destructive interference is minimized: the stable sampling points.

These stable sampling points live at $F_n/120$. The maximum resolution the space provides is 120. $S^3$ is diffeomorphic to $\text{SU}(2)$; the binary icosahedral group $2I$ is its largest exceptional discrete subgroup, with $|2I| = 120$.

**Why 120 and no other number?** Five paths converge on the domain; three are independent, one is geometrically restated, and one is a consistency check:

- *Group-theoretic:* $|2I| = 120$, largest discrete spinor symmetry on $S^3$
- *Number-theoretic:* $\text{lcm}(1,2,3,5,8) = 120$, minimal domain for Fibonacci structure
- *Musical:* Consonance ratios $\{1,2,3,4,5,6,8\}$ independently yield $\text{lcm} = 120$. The ear is a physical phase detector; every musical tradition but Gamelan converges on these ratios without cultural transmission.
- *Angular:* Icosahedral symmetry partitions $S^2$ into 60 fundamental domains; the binary cover on $S^3$ doubles to 120.
- *Mode Identity Theory:* The scaling law requires irreducible fraction $13/120$ ($\gcd(13, 120) = 1$); no coarser domain accommodates the observed well structure.

The $(2,3,5)$ branch orders of the icosahedron are consecutive Fibonacci numbers satisfying $2 + 3 = 5$. This is why the group-theoretic and number-theoretic paths converge: the icosahedron is the unique Platonic solid whose symmetry orders obey the Fibonacci recurrence.

### The Chronon

If the domain has 120 positions and the wave has period $4\pi$, the smallest step is fixed. The smallest phase advance in cosmic phase $t$:

$$\Delta t_{\min} = \frac{4\pi}{120} = \frac{\pi}{30}$$

The chronon is the domain's phase resolution: the smallest phase advance the domain can register, measured in radians of the cosmic phase $t$. For any mode with period $T$, the chronon is $\tau = T/120$. The resolution is scale-dependent. Time itself remains continuous; only the phase resolution is discrete.

The corresponding minimum action increment:

$$\Delta S_{\min} = \hbar\Delta t_{\min} = \frac{\hbar\pi}{30}$$

This is the smallest action the domain can resolve. Unlike the chronon, which scales with the mode, the action bound is absolute: action is a Lorentz scalar, so $\Delta S_{\min} = \hbar\pi/30$ holds in every frame.

### The Bosonic Filter

Fermions see the full 120. Observation squares the wavefunction, and half the resolution vanishes.

The wavefunction $\psi_0$ satisfies $\psi(\Theta+1) = -\psi(\Theta)$: it carries the sign flip from the anti-periodic boundary condition. The fermion distinguishes all 120 positions on the domain. Observation squares the wavefunction. $C = |\psi|^2$ erases the sign: $|\psi(\Theta+1)|^2 = |-\psi(\Theta)|^2 = |\psi(\Theta)|^2$. What was distinct to the fermion becomes identical to any measurement.

The consequence is halved resolution. The minimum step any observable can resolve is $2/120$, not $1/120$. The squaring projects $2I \to I$, where $I$ is the icosahedral rotation group ($|I| = 60$). The filter is a projection rule extending to all boson-projected observables: observables realized through boson-projected intensity channels must sit at even positions on the 120 domain. Even positions on the 120 domain and the 60R-grid (R for realized) are the same lattice — two notations for the same 60 positions. Cosmographic observables ($H_0$, $\Lambda$, $\alpha$) are realized through photon-mediated distance and intensity measurements and belong to this class. Dynamical observables ($a_0$) are realized through acceleration response and retain full 120-domain access. The realization channel determines the grid, not the experimental technology used to estimate it.

Two notational conventions appear in the tables below, both denoting the same 60R lattice. Dimensionless couplings ($A_P = 1$) are written in reduced form: the bosonic projection maps the fermionic well $13/120$ to $13/60$ on the 60R-grid. Dimensionful cosmographic observables ($H_0$, $\Lambda$) are written in 120-domain notation with even numerators ($34/120$, $60/120$); the equivalent 60R positions are $17/60$ and $30/60$. The Grid column in the Fibonacci Wells table records which convention is used for each entry.

### Fibonacci Wells (Θ₀)

The Bosonic Filter established the 60R-grid; only certain positions carry observable amplitude. Fibonacci selects the stable wells; the antinode ($60/120$) is included as the amplitude maximum. The well at $13/120$ is irreducible: $\gcd(13, 120) = 1$. No coarser domain can represent it.

Not all Fibonacci wells survive to observation. The phase field carries microfluctuations $\delta\Theta_f^\text{micro} \lesssim 10^{-4}$, setting a noise floor. Below $F_7$, the amplitude is indistinguishable from noise: $C(8/120) = 0.087$. At $F_7$, the wave resolves: $C(13/120) = 0.22$.

The well assignments (which observable maps to which well) are identified by coprimality and observable character; the wells themselves are enumerated. Among edge modes, $a_0$ occupies the coprime well ($13/120$), forced by irreducibility. $\Lambda$ occupies the antinode ($60/120$), forced by ground-state maximality. Among the remaining Fibonacci wells, only $34/120$ carries an even numerator and therefore survives the bosonic filter for cosmographic observables; $H_0$ occupies it by exclusion. The surviving wells become:

| $F_n$ | Grid | Well | $C(\Theta)$ | Observable |
|---|---|---|---|---|
| $F_7$ | 60R | 13/60 | 0.79 | $\alpha$ (fine structure constant) |
| $F_7$ | 120 | 13/120 | 0.22 | $a_0$ (acceleration scale) |
| $F_8$ | 120 | 21/120 | 0.55 | Unassigned |
| $F_9$ | 120 | 34/120 | 1.21 | $H_0$ (Hubble parameter) |
| $F_{10}$ | 120 | 55/120 | 1.97 | Unassigned |
| -- | 120 | 60/120 | 2.00 | $\Lambda_\text{top}$ (cosmological constant) |

The Bosonic Filter projects $13/120 \to 13/60$ on the 60R-grid; the Grid column distinguishes the two $F_7$ rows.

**Coprimality note:** $\gcd(13, 120) = 1$. The $13/120$ well shares no factors with the domain, making it maximally detached from the domain's own symmetry. Matter lives there. The structural observables ($\Lambda$, $H_0$) occupy wells with shared factors, coupled to the domain structure itself.

### Phase Field (Θ\_f)

The wells are locked by topology. The observer's position is local. The local gravitational environment shifts the sampling position away from the well center.

For global observations (CMB, BAO), the shift averages out: $\Theta_f \approx 0$. Integration over gigaparsec volumes erases local structure. For local observations, $\Theta_f$ reflects the observer's environment. The phase field decomposes as:

$$\Theta_f = \Theta_f^{\text{env}} + \delta\Theta_f^{\text{micro}}$$

The environmental component $\Theta_f^\text{env}$ is the coherent offset from local structure. The microfluctuation $\delta\Theta_f^\text{micro}$ is noise that averages out ($\lesssim 10^{-4}$).

For the Milky Way, $\Theta_f^\text{env} \approx 2/120$, the minimum bosonic step: the smallest shift the 60R-grid can register. At $\Theta_0 = 34/120$, this step shifts $C(\Theta)$ by 8.4%:

$$\frac{C(36/120)}{C(34/120)} = \frac{1.309}{1.208} = 1.084$$

This 8.4% resolves the Hubble tension. The distance ladder calibration anchor — Cepheid period-luminosity zero-points, geometric parallax distances — is established within the Milky Way's phase field. That anchor carries the 8.4% shift into every subsequent rung. Supernovae at 500 Mpc are measured correctly relative to the shifted anchor; the shift propagates through calibration. Local measurements of $H_0$ inherit the phase field through calibration rather than proximity. CMB-derived values integrate over gigaparsec volumes where $\Theta_f \approx 0$. The discrepancy is a calibration offset.

### A. Phase Field Mechanics

The Fibonacci wells have different sensitivities to environmental shifts. Wells near the boundary of the domain are steep; wells near the antinode are flat. This determines how much each observable changes when the phase field is active. The remainder of the section builds the classification mechanism: what gravitational conditions activate the phase field, over what spatial scale, and why the shift locks at exactly one bosonic step.

### B. Logarithmic Slope

The sensitivity of $C(\Theta)$ to small shifts:

$$\frac{d \ln C}{d\Theta} = 2\pi \cot(\pi\Theta)$$

The cotangent diverges near the boundary and vanishes at the antinode. $\Lambda$ sits at the antinode ($\Theta = 60/120$): its slope is exactly zero. The cosmological constant is topologically fixed; environmental shifts leave it unmoved.

| Well | $\Theta$ | $C(\Theta)$ | Slope |
|---|---|---|---|
| $a_0$ | 13/120 | 0.22 | 17.7 |
| $H_0$ | 34/120 | 1.21 | 5.1 |
| $\Lambda_\text{top}$ | 60/120 | 2.00 | 0 |

### C. Shift Amplification

The Bosonic Filter fixed $\Delta\Theta_{\min} = 2/120$. Multiplying slope by step ($\Delta C/C = (d\ln C/d\Theta) \times \Delta\Theta_{\min}$) gives the fractional shift at each well:

| Well | Slope x 2/120 | Shift |
|---|---|---|
| $a_0$ | 17.7 x 2/120 | 30% |
| $H_0$ | 5.1 x 2/120 | 8.4% |
| $\Lambda_\text{top}$ | 0 x 2/120 | 0% |

The $a_0$ well is steep (one bosonic step would shift its amplitude by 30%), but $a_0$ is constitutive: it defines $\mathcal{T}_c$ and $L_f$, and is only measurable inside above-threshold environments. The observed $a_0$ corresponds to the Fibonacci well. $H_0$ shifts by 8.4%, matching the Hubble tension. $\Lambda$ remains unmoved.

### D. Coherence Scale

Dimensional analysis admits exactly one length from $v_c$ and $a_0$:

$$L_f = \frac{v_c^2}{a_0}$$

For the Milky Way ($v_c \approx 220$ km/s), $L_f \approx 13$ kpc.

### E. Classification Index

The phase field state is determined by the gravitational potential drop across $L_f$. Defining $\Phi_{\text{rel}}(l) \equiv \Phi(l_{\text{out}}) - \Phi(l)$, the dimensionless classification index is:

$$\mathcal{T} \equiv \frac{2}{c^2 L_f} \int_0^{L_f} \Phi_{\text{rel}}(l)\,dl$$

### F. Threshold

The critical value separating the two classes. The geometry factor $\xi \approx 0.46$ captures the mean potential depth (isothermal, NFW, and Hernquist all give 0.44 to 0.47):

$$\mathcal{T}_c = \frac{2\xi\,a_0\,L_f}{c^2}$$

### G. Response

The phase field state is binary: below the critical value $\Theta_f = 0$; at or above it $\Theta_f = 2/120$. The Closure Identity establishes that every flat-curve disk sits above the critical value by the same factor $1/\xi \approx 2.2$, so the classification reduces to a type test: flat-curve disk or not.

$$\Theta_f = \frac{2}{120} \cdot \mathbf{1}(\mathcal{T} \geq \mathcal{T}_c)$$

where $\mathbf{1}(\cdot)$ is the indicator function. No continuous slide; the 60R-grid fixes the step. Higher-order transitions ($4/120$, $6/120$, $\ldots$) are inaccessible within a single coherence scale.

**Closure Identity.** Substituting $L_f = v_c^2/a_0$ into $\mathcal{T}_c$, the acceleration scale cancels: $\mathcal{T}_c = 2\xi v_c^2/c^2$. Both $\mathcal{T}$ and $\mathcal{T}_c$ scale as $v_c^2$; the ratio is galaxy-independent:

$$\frac{\mathcal{T}}{\mathcal{T}_c} = \frac{1}{\xi} \approx 2.2$$

The profile-dependent integral in $\mathcal{T}$ evaluates to the same $v_c^2$-controlled quantity for flat-curve disks across all standard profiles (isothermal, NFW, Hernquist all give $\xi \in [0.44, 0.47]$); $\xi$ absorbs this variation. For flat-curve disk galaxies, crossing the threshold is a class property: $\mathcal{T}/\mathcal{T}_c = 1/\xi \approx 2.2$ in every such system. Systems without flat rotation curves — dwarf spheroidals, pressure-supported systems — are outside this closure and require separate treatment.

### Galactic Disk Phase Shift

For every disk galaxy with a flat rotation curve, $\mathcal{T} > \mathcal{T}_c$; edge observables sampled from inside are shifted by the phase field. The Milky Way ($v_c \approx 220$ km/s):

**Coherence scale.**

$$L_f = \frac{v_c^2}{a_0} = \frac{(2.2 \times 10^5)^2}{1.2 \times 10^{-10}} \approx 4 \times 10^{20}\text{ m} \approx 13\text{ kpc}$$

**Threshold.**

$$\mathcal{T}_c = \frac{2\xi\,v_c^2}{c^2} = \frac{2(0.46)(2.2 \times 10^5)^2}{(3 \times 10^8)^2} \approx 4.9 \times 10^{-7}$$

**Classification index.**

$$\mathcal{T}_\text{MW} \approx 1.1 \times 10^{-6} \quad \Rightarrow \quad \mathcal{T}_\text{MW} > \mathcal{T}_c$$

Above threshold. The shifted well:

$$H_0^{\text{local}} = H_0^{\text{CMB}} \times \frac{C(36/120)}{C(34/120)} = 67.4 \times 1.084 \approx 73\text{ km/s/Mpc}$$

| Quantity | Value | Source |
|---|---|---|
| $v_c$ | 220 km/s | Milky Way circular velocity |
| $a_0$ | $1.2 \times 10^{-10}$ m/s$^2$ | $F_7 = 13/120$ well |
| $L_f$ | 13 kpc | $v_c^2/a_0$ |
| $\xi$ | 0.46 | Geometry factor (profile-insensitive) |
| $\mathcal{T}_c$ | $4.9 \times 10^{-7}$ | Critical threshold |
| $\mathcal{T}_\text{MW}$ | $1.1 \times 10^{-6}$ | Milky Way classification index |
| $\mathcal{T}/\mathcal{T}_c$ | 2.2 | $= 1/\xi$, galaxy-independent |
| $\Theta_f$ | $2/120$ | One bosonic step (locked) |
| $\Delta H_0$ | 8.4% | $C(36/120)/C(34/120) = 1.084$ |

The distance ladder calibration anchor is set inside the Milky Way's phase field. The CMB gives the true value of $H_0$.

## The Scaling Law

The framework reduces to one equation:

  $$\Large \boxed{\frac{A}{A_P} \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}}$$

$C(\Theta)$ reads the position axis: where the observable sits on the mode spectrum. $(\sqrt{\Omega})^{-n}$ reads the time axis through $\Omega_H$ for edge modes, or the boundary condition through $\Omega_\Lambda$ for surface modes. The observer at $\sqrt{\Omega}$ is the structural midpoint where both axes resolve to finite values. Their product yields $A/A_P$: the modal realization; the ratio of the observable amplitude over its Planck scale reference. 

**The sample occurs at** $(t, \Theta)$.

### The assembled engine

| Observable | $A_P$ | Grid | $\Theta$ | $C$ | $n$ | $A/A_P$ |
|---|---|---|---|---|---|---|
| $\alpha$ | 1 | 60R | 13/60 | 0.79 | $1/30$ † | $7.33 \times 10^{-3}$ |
| $a_0$ | $a_P$ | 120 | 13/120 | 0.22 | 1 | $2.2 \times 10^{-62}$ |
| $H_0$ | $t_P^{-1}$ | 120 | 34/120 | 1.21 | 1 | $1.2 \times 10^{-61}$ |
| $\Lambda$ | $\ell_P^{-2}$ | 120 | 60/120 | 2.00 | 2 | $(3/2) \times 2.0 \times 10^{-122} = 3.0 \times 10^{-122}$ ‡ |

> †For dimensionless couplings ($A_P = 1$), manifold dilution does not apply directly — there is no Planck-scale reference to dilute against. Instead, the running from the Planck-scale value $C(13/60) \approx 0.79$ to the observed $\alpha \approx 7.3 \times 10^{-3}$ is controlled by the domain resolution. The exponent $n = 1/30$ is set equal to the minimum grid step $1/|I| = 1/60$ on the bosonic domain, giving $\Omega_\Lambda^{-1/60} = (\sqrt{\Omega_\Lambda})^{-1/30}$.
> ‡ $\Lambda_\text{top} = 2/R_\Lambda^2$ is the surface eigenvalue (Weitzenböck / eigenvalue chain). $\Lambda_\text{obs} = (3/2)\Lambda_\text{top} = 3/R_\Lambda^2$ via the vacuum Gauss-Codazzi embedding ($K_{ij}=0$). The coefficient 2 is the 2D surface ground-state eigenvalue; the coefficient 3 is the de Sitter trace in 3D space. The Gauss-Codazzi equations connect the two eigenvalue problems; the ratio 3/2 follows from those two independent computations. Full derivation in companion paper.

$H_0$ and $a_0$ occupy different wells on the same edge; their ratio is fixed by position. $H_0$ and $\Lambda$ occupy different manifolds; their 61-order span is fixed by dimension. $\alpha$ occupies the same well as $a_0$ on the 60R-grid; its exponent is fixed by resolution.

### Derivation chain

Each component traces to the single topological postulate:

| Component | Source | Status |
|---|---|---|
| $m = 0$ | Isotropy + orthogonality | Derived |
| $(\sqrt{\Omega})^{-n}$ | IR↔UV fixed point + volume scaling | Derived |
| $n = 0, 1, 2, 3/2, 3$ | Epoch-dependence + coupling character; $n = 0$ is the Planck input ($G$), $n = 3/2$ is the Gauss-Codazzi interface (gravity) | Derived |
| Anti-periodic BC selected | Matter is fermionic; half-integer modes on $2I$ reproduce 10/12 SM fermion masses within ×3 | Motivated |
| $\Psi(0) = +1$ | Initial condition selecting the branch where $t=0$ is amplitude maximum; $\Psi(0) = -1$ is the same wave phase-shifted by $2\pi$ | Convention |
| $C(\Theta) = 2\sin^2(\pi\Theta)$ | Anti-periodic BC + unit normalization | Derived |
| $\Theta$ on 120 domain | $S^3 \cong \text{SU}(2)$ polyhedral subgroup resolution + irreducibility | Derived |
| $\Theta \in \{13, 21, 34, 55, 60\}/120$ | Hurwitz stability + amplitude threshold | Derived |
| $\Delta\Theta_{\min} = 2/120$ | Bosonic Filter (spinor → scalar) | Derived |
| $\alpha$ exponent $n = 1/30$ | Equals minimum grid step $1/|I| = 1/60$ on bosonic domain; supported by three independent paths; connection between dilution exponent and grid resolution step is the open link | Motivated |
| $L_\text{strip}/L_\text{fund} = 8.17 \pm 0.1$ | Spectral derivation: scalar Laplacian on $S^3/2I$, degree-12 Klein invariant, Heun transverse eigenvalue $\mu_1 = 1.021$; exact closure open | Motivated |
| $L_f = v_c^2/a_0$ | Coherence scale | Derived |
| $\mathcal{T}$, $\mathcal{T}_c$, $\Theta_f$ response | Gauge-invariant classification index + critical value + binary step function | Derived |
| $\Lambda_\text{top} = 2/R_\Lambda^2$ | Weitzenböck gives lower bound $\lambda_{\min} \geq 2/R_\Lambda^2$; eigenvalue chain gives equality independently; ground state saturates the bound. Conversion to $\Lambda_\text{obs}$ via vacuum Gauss-Codazzi is a separate step | Structural convergence |

### Symbol Glossary

Observables are located in time on the edge and positioned on the mode spectrum. Cosmic phase $t$ sets *when*; phase position $\Theta$ sets *where*. Three scales complete the framework.

| Symbol | Name | Domain | Description |
|---|---|---|---|
| $t$ | Cosmic phase | $[0, 4\pi]$ | Observer's phase location on $\Psi$; time in MIT is phase |
| $\delta$ | Epoch offset | $\sim -1.06$ rad | How far from turnaround |
| $\Omega$ | Scale | $(\mathcal{R}/\ell_P)^2$ | Planck areas on horizon $\sim 10^{122}$; $\mathcal{R}$ is $R_H$ or $R_\Lambda$ per manifold |
| $\Omega_H$ | Hubble scale | $(R_H/\ell_P)^2$ | Evolves with epoch |
| $\Omega_\Lambda$ | de Sitter scale | $(R_\Lambda/\ell_P)^2$ | Fixed by $\Lambda$ |
| $\Theta$ | Phase position | $[0,1]$ on 120 | Observable's position on mode spectrum |
| $\Theta_0$ | Fibonacci well | $\{13, 21, 34, 55, 60\}/120$ | Fixed geometric position |
| $\Theta_f$ | Phase field | 0 or $2/120$ | Local environmental shift |

## Predictions and Falsification

MIT has no loose knobs; predictions are locked and every component is placed by the postulate. Derivation status for each component is in the table below. The framework stands or falls on population-level agreement with those predictions.

### Falsification hierarchy

(1) Single-object disagreement: tension. (2) Multiple independent measurements: severe tension. (3) Statistical-sample exclusion at ≥ 2σ with controlled systematics: falsification.

### Primary predictions

Failure of any one falsifies the framework.

| Prediction | Falsified if | Threshold |
|---|---|---|
| $a_0(z) \propto H(z)$ | $a_0$ consistent with constant at high $z$ | ≥ 2σ, $z > 2$ |
| $\Lambda$ constant | $\rho_{\text{DE}}(z)$ shows significant evolution | ≥ 2σ |
| CMB boundary | Wrong boundary scale | $\ell_{\text{cut}} \notin [15, 50]$ |

### Secondary predictions

These do not individually falsify MIT but meaningfully raise or lower credibility.

| Prediction | Falsified if | Note |
|---|---|---|
| Null particle dark matter | Non-gravitational interaction confirmed | ≥ 5σ, replicated |
| $H_0$ discrete | Continuous environmental variation confirmed | Histogram test |
| $z_{\text{cross}} \approx 0.66$ | Phantom crossing outside locked range | below 0.4 or above 0.9 |
| $w_{\text{eff}} > -1$ at all $z$ | True phantom behavior confirmed | Euclid, Rubin |
| $\mu_\Lambda \approx 2.25$ meV | Lightest $\nu$ mass inconsistent | KATRIN, cosmological bounds |
| $L_\text{strip}/L_\text{fund} = 8.17 \pm 0.1$ | CMB data pins ratio to 8.00 at $> 1\sigma$ | Spectral derivation; exact closure is open |

## Scope and Position

MIT is a topological framework: it specifies boundary conditions and permitted mode structure. Boundary conditions are prior to dynamics. Standard dynamics describes the music; MIT defines the instrument.

**What MIT does claim.** One postulate (topology), three primitive inputs ($c$, $\hbar$, $G$), one scaling law. The Fibonacci wells are fixed positions on the 120-domain, determined by the group structure of $2I$ before any observable is consulted. The identification of which observable sits at which well is a matching exercise; the wells are fixed in advance. The scaling law $A/A_P \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}$ and every component in it trace to the topology postulate.

**What MIT leaves intact.** Einstein's field equations and the Standard Model particle content are unchanged. MIT addresses why observables take their values and why gauge fields confine into three generations.

**Parallel work.** Topological cosmology has been explored since Friedmann. Luminet, Weeks, and collaborators proposed the Poincaré dodecahedral space ($S^3/2I$) as the spatial topology of the universe, matching CMB low-ℓ boundary. MIT adopts the same manifold and extends it from CMB anomalies to particle structure.

The COMPACT collaboration calculates eigenmodes of non-orientable Euclidean manifolds, closely overlapping the mathematics MIT requires; their analysis of parity asymmetry from topology alone aligns with MIT's derivation of odd-ℓ preference.

Milgrom's MOND established $a_0$ as a fundamental acceleration scale; MIT derives it as an edge mode and predicts its evolution with $H(z)$, the central fork test against MOND's constant $a_0$.
