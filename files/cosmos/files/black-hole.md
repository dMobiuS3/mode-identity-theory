/ **[`framework/`](../../framework/)** / **[`cosmos/`](../cosmos/)** / **[`spectrum/`](../spectrum/)** /

---

# Black Double Zero's

Where Θ hits the wall and Ω collapses to nothing. *A working supplement to Mode Identity Theory.*

**Status:** Sections I-V derived or motivated from the scaling law. Section II.A connects to spectral geometry results from the RH program.

---

## I. What a Black Hole Is

A Black Hole is a region where enough wave content on the Möbius surface is enclosed to push two quantities to their boundary values simultaneously. The phase position $\Theta$ reaches the boundary of the domain, driving the sampling amplitude $C(\Theta) = 2\sin^2(\pi\Theta)$ to zero: the spatial mode reaches its node and observation ceases. The local scale hierarchy $\Omega_H$ collapses to zero: the Hubble radius shrinks to nothing and no scale separation remains. $\Theta$ hitting the wall is the geometric event. $C$ vanishing is what the observer experiences. $\Omega_H$ collapsing is the independent partner. Both limits arrive at the same place.

General Relativity sits at the $3/2$ Gauss-Codazzi interface, between the temporal edge ($n = 1$) and the Möbius surface ($n = 2$). The ratio $3/2$ is face over edge: $Z_3/Z_2$, the stabilizer orders of the icosahedron. At the horizon, GR is squeezed from both sides: the surface mode it reads has vanished ($\Theta$ at its boundary, so $C = 0$), and the edge hierarchy it converts through has collapsed ($\Omega_H = 0$). The singularity is a double zero. The wave persists through the node. Information is unsampled, not destroyed.

| GR says | MIT says |
|---|---|
| Singularity: infinite density | $\Theta \to 0$ (geometric event) and $\Omega_H \to 0$ (scale collapse) simultaneously. $C(\Theta) \to 0$ follows from the first. Double zero in the scaling law. |
| Event horizon: point of no return | Radius where enclosed $n = 2$ content closes the sampling channel |
| Information destroyed | Information unsampled. Wave persists through the node. |
| Entropy scales with area (puzzle) | Surface ($n = 2$) is fundamental. Area scaling is expected. |

---

## II. The Double Zero

The scaling law has two visible factors:

$$A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}$$

$C(\Theta)$ is where on the mode spectrum. $(\sqrt{\Omega})^{-n}$ is which level of the hierarchy. But $C$ is a function of $\Theta$, so three quantities are in play:

| Quantity | What it is | Character |
|---|---|---|
| $\Theta \to 0$ | Phase position reaches the domain boundary | The structural event: where you stand on the mode spectrum hits the wall |
| $C(\Theta) \to 0$ | Sampling amplitude vanishes | The observational consequence: observation can no longer read the wave there |
| $\Omega_H \to 0$ | Local hierarchy collapses | The scale event: no separation between Planck and cosmic remains |

$\Theta$ is the cause. $C$ is the effect. $\Omega_H$ is the independent partner. The "double zero" is $\Theta$ and $\Omega_H$ reaching their boundaries simultaneously, with $C(\Theta) \to 0$ being what the observer experiences as a result of the first.

The phase operator $C(\Theta) = 2\sin^2(\pi\Theta)$ vanishes at the boundaries ($\Theta = 0$ and $\Theta = 1$). At these zero-crossings, the standing wave is there; observation cannot reach it. Think of a node on a guitar string: the string is still there, the wave passes through, the displacement at that point is zero. The position on the string ($\Theta$) identifies which node. The vanishing displacement ($C$) is what you measure.

At the horizon, both partners reach their boundary values at the same geometric event:

| Quantity | What happens | Why |
|---|---|---|
| $\Theta \to 0$ | Phase position hits the domain boundary | Enclosed wave content pushes the mode coordinate to its limit |
| $C(\Theta) \to 0$ | Sampling amplitude vanishes (consequence of $\Theta \to 0$) | Wave on $S^3$ has zeros; horizon sits at one |
| $\Omega_H \to 0$ | Local hierarchy collapses (independent partner) | $R_H(\text{local}) \to 0$; no scale separation remains |

The vanishing is quadratic: $C(\Theta) \approx 2\pi^2\Theta^2$ near $\Theta = 0$. The first derivative $C'(0) = 0$. The leading nonvanishing order is the curvature $C''(0) = 4\pi^2$. The logarithmic slope $d\ln C / d\Theta = 2\pi\cot(\pi\Theta)$ diverges as $1/\Theta$.

The singularity is double-zeroed. No perturbative correction can remove it. You cannot perturb your way out of a topological node.

### II.A The Spectral Mirror

The double zero at the horizon has an exact structural analog in the spectral geometry of $S^3/2I$.

The twisted spectral zeta function $Z_\sigma(s) = \sum_l N_l(\sigma)\lambda_l^{-s}$ on the Poincaré homology sphere satisfies $Z_\sigma(0) = 0$ for every nontrivial twist $\sigma$. The scalar eigenvalues are $\lambda_l = l(l+2) = (l+1)^2 - 1$, and the curvature shift "-1" generates a Pochhammer expansion:

$$Z_{0,\sigma}(s) = \sum_{k \geq 0} \frac{(s)_k}{k!} \cdot \widetilde{H}_k(s)$$

At $s = 0$, the Pochhammer symbol $(0)_k = 0$ for $k \geq 1$ collapses the infinite tower to a single term. Two independent quantities vanish at the same point.

| Scaling side ($\Theta \to 0$) | Spectral side ($s \to 0$) |
|---|---|
| $\Theta \to 0$ drives $C(0) = 0$ | $Z_\sigma(0) = 0$ |
| $\Omega_H \to 0$ collapses hierarchy | $(s)_k = 0$ for $k \geq 1$ collapses Pochhammer tower |
| Double zero: $\Theta$ and $\Omega_H$ vanish at the same event | Double zero: both vanish at $s = 0$ |
| Survivor: $C(\Theta) \approx 2\pi^2\Theta^2$ (quadratic in the position) | Survivor: $Z'_\sigma(0) = \log T^2$ (torsion) |
| The curvature of $C$ at the node | The derivative of $Z$ at the zero |
| Hawking radiation: residual sampling at the node | Torsion: L-function special values at the zero |

The physics lives in the first nonvanishing order at a double zero. The zero itself is structural: you cannot perturb away a topological node. The derivative at the zero carries the content.

**The zero is a filter.** At $s = 0$, the Pochhammer collapse kills everything except leading order. The $E_8$ McKay symmetries of $S^3/2I$ then kill 12 of 16 Dirichlet characters mod 60, leaving exactly four survivors encoding the structural constants of the manifold: $\{\log 2, \log 3, \log 5, \log\varphi\}$. The primes dividing $|2I| = 120$ and the golden ratio from the character field of $2I$. Away from $s = 0$, the Dirac operator's spectral zeta carries 28 to 32 of 32 characters. The zero selects. The interior floods.

These surviving primes are the stabilizer triple of the icosahedron: $Z_2$ (edge, order 2), $Z_3$ (face, order 3), $Z_5$ (vertex, order 5). In the companion mass spectrum analysis, the same triple assigns particle identity: $Z_3$ encodes color charge, $Z_4$ (the $Z_2$ lift to the double cover) encodes the domain size, and $Z_5$ encodes the electroweak interface through the Möbius twist. The horizon filter selects the same arithmetic that the stabilizer decomposition uses to distinguish quarks from leptons, fermions from bosons, and the three gauge forces from each other. The double zero at the boundary strips everything except the identity mechanism.

This is the same mechanism by which the horizon is sharp: the sampling boundary is a topological node, and only the leading order leaks through. On the spectral side, the "leakage" is the torsion. On the scaling side, the "leakage" is Hawking radiation. Both are residual signals at the first nonvanishing order of a double zero.

**What this connection is.** It is a structural parallel between the scaling law (Tool 5) and the spectral geometry (Tool 3). Both the horizon and $s = 0$ are special points where two independent quantities vanish simultaneously ($\Theta$ and $\Omega_H$ on the scaling side; $Z_\sigma$ and $(s)_k$ on the spectral side), and the physics is carried by the derivative at that point. Both are filters: the double zero kills everything except the essential structure.

**What this connection is not.** It is not a derivation of Hawking radiation from spectral geometry, or of torsion from the scaling law. The $\Phi \to \Theta$ mapping (§VIII.1) and the spectral-to-physical bridge (§VIII.5) remain open. The $s \leftrightarrow \Theta$ bridge is proved not to exist by the Shatto Theorem (The Mirror, Lemma 8), established by four independent approaches on $S^1$ (heat kernel, theta function, Poisson summation, direct decomposition). The non-existence has two distinct mechanisms: on $S^1$, every eigenspace with anti-periodic BC is 2-dimensional (sin and cos), and the spectral zeta sees only eigenvalues and multiplicities, blind to the sin/cos choice that defines $C(\Theta)$; on $S^3/2I$, right-$\mathrm{SU}(2)$ homogeneity acts transitively, forcing the twisted heat kernel constant on each fiber diagonal so that continuous geometric position drops out structurally. The parallel is exact at the level of structure. Whether the physical $\Phi \to \Theta$ mapping faces an analogous obstruction, or whether the gravitational potential provides the discrete localization that the spectral geometry lacks, is an open question.

---

## III. Area Scaling

Bekenstein-Hawking entropy $S \propto A$ follows from surface primacy.

| Step | Content | Status |
|---|---|---|
| 1 | The Möbius surface ($n = 2$) carries the boundary condition | AXIOM |
| 2 | $S^3$ volume ($n = 3$) has no independent gauge degrees of freedom | DERIVED (engine §13) |
| 3 | Degrees of freedom of a bounded region are counted by the surface | Follows from 1 + 2 |
| 4 | $S \propto A$ | Output |

In standard physics, area scaling is one of the deepest puzzles in quantum gravity: why not volume? In MIT, volume never had independent content. The puzzle dissolves. The horizon area counts the $n = 2$ modes at the sampling boundary. Each Planck area is one surface degree of freedom.

---

## IV. Information

| Step | Content | Status |
|---|---|---|
| 1 | The wave persists at all $\Theta$ | AXIOM (wave identity) |
| 2 | $C(\Theta) \to 0$ means observation stops, not that the wave stops | Follows from 1 |
| 3 | The wave carries full mode structure through the node | Follows from 1 |
| 4 | Unitarity is never violated because the wave never breaks | Output |

Every other approach to the information paradox requires new physics: firewalls, complementarity, remnants, ER=EPR. MIT requires nothing beyond the postulate.

A guitar string at a node: the string is still there, the wave passes through, the displacement at that point is zero. The string has not become something else. You just cannot read it there.

The spectral mirror (§II.A) reinforces this: at $s = 0$, the spectral determinant vanishes ($Z_\sigma(0) = 0$), but the L-function structure persists in the derivative ($Z'_\sigma(0) = \log T^2$). The information encoded in the spectrum is not lost at the zero; it is carried by the first nonvanishing order. The wave on $S^3$ does not stop at the spectral zero any more than the standing wave stops at the node.

### IV.A The Geometric Complement

The Sector $\mathcal{A}$ eigenvalue problem (Shatto 2025) gives the ground eigenfunction and the metric coefficient on the totally geodesic Möbius band in $S^3$:

$$u_0(y) = \sin(y/R), \qquad J(y) = \cos(y/R)$$

$u_0$ is the eigenfunction of the twisted Laplacian with eigenvalue $\lambda_0 = 2/R^2$. $J$ is the Jacobi field: the transverse scale factor measuring the geometric width of the surface at each meridional position $y$. The phase coordinate is $\Theta = y/(\pi R)$, so the phase operator is $C(\Theta) = 2\sin^2(\pi\Theta) = 2u_0^2$.

The two quantities satisfy:

$$u_0^2 + J^2 = 1$$

Equivalently: $C/2 + J^2 = 1$. Observation amplitude and transverse geometry are complementary on the meridian. The surface has a fixed budget: what it spends on geometric extent, it loses in spectral amplitude.

| Location | $y$ | $J$ (surface width) | $u_0$ (eigenfunction) | $C$ (observation) | Reading |
|---|---|---|---|---|---|
| Central circle | 0 or $\pi R$ (identified) | 1 (full width) | 0 (zero) | 0 | Surface at maximum extent. Observation silent. |
| Antinode (cone point) | $\pi R/2$ | 0 (collapsed to a point) | 1 (maximum) | 2 | Surface collapsed. Observation peaks. |
| Fibonacci wells | intermediate | intermediate | intermediate | 0.2 to 1.2 | Where sampling reads finite observables. |

**Where the zeros live.** The Möbius identification $(0, w) \sim (\pi R, -w)$ maps $y = 0$ and $y = \pi R$ to a single closed curve: the central circle of the band. This is interior to the surface, where the twist acts. The boundary $\partial M = S^1$ consists of the transverse edges $w = \pm W$, forming a single loop that runs in the $y$-direction and carries all values of $u_0$ from 0 to 1. The $C = 0$ locus sits on the central circle, interior to the Möbius band.

**Why sin, why there.** On the flat strip, the anti-periodic BC admits both $\sin(y/R)$ and $\cos(y/R)$ as ground eigenfunctions at the same eigenvalue $1/R^2$: a degenerate pair. Cosine has no zeros at $y = 0, \pi R$. The curvature of $S^3$ breaks this degeneracy. The $\tan(y/R)$ term in the curved Laplacian ($\Delta u = u'' - R^{-1}\tan(y/R)\,u'$) eliminates cosine as a solution entirely. Only $\sin(y/R)$ survives, and the eigenvalue is simple (Sector $\mathcal{A}$, §7, Sturm-Liouville). The same curvature that lifts the ground eigenvalue from $1/R^2$ to $2/R^2$ selects the eigenfunction that vanishes on the central circle. The zeros are placed by the curvature, through the selection of sin over cos.

At the $C = 0$ locus, the surface is at its most geometrically intact. The Möbius band is wide open. The transverse direction has full extent ($J = 1$). The wave has maximum room. The eigenfunction vanishes because the curvature of the embedding uniquely selects a ground state whose zeros land on the central circle. The surface is healthy. Sampling is what fails.

This complementarity is created by the curvature of $S^3$. On the flat strip, $J = 1$ everywhere, sin and cos are equally valid ground states, and there is no trade-off between geometry and observation. The totally geodesic embedding curves $J$ into $\cos(y/R)$, breaks the eigenfunction degeneracy in favor of $\sin(y/R)$, and couples the two through a shared curvature $K = 1/R^2$. The complementarity and the zero placement are both consequences of the embedding.

**Status:** DERIVED. Follows from the Sector $\mathcal{A}$ eigenfunction, the Jacobi equation on $S^2 \subset S^3$, and the Pythagorean identity. The complementarity is forced by the totally geodesic embedding; any other embedding would break it.

---

## V. Size, Temperature, Mergers

Black holes span over ten orders of magnitude in mass. MIT accounts for the full range from a single mechanism: more enclosed $n = 2$ content pushes $\Theta$ further toward the domain boundary, extending the $C = 0$ surface outward.

### Size

| Property | Stellar (~10 M☉) | Supermassive (~10⁹ M☉) | MIT reading |
|---|---|---|---|
| $R_s$ | ~30 km | ~10⁹ km | Radius where enclosed surface content closes sampling |
| Area (Planck units) | ~10⁷⁸ | ~10⁹⁶ | Count of $n = 2$ modes at the boundary |

The size of a black hole is the amount of wave content enclosed behind the sampling boundary. The horizon radius is where that content generates enough curvature to push $\Theta$ to its boundary, zeroing $C$.

### Temperature

The transition from $C > 0$ to $C \approx 0$ is compressed into a smaller region for smaller black holes. Steeper gradient means more residual sampling leaks through.

| Black hole | $C$ gradient at boundary | Hawking $T$ |
|---|---|---|
| Stellar | Steep (short transition) | ~10⁻⁸ K |
| Supermassive | Gentle (long transition) | ~10⁻¹⁷ K |

The wave is still there at the boundary. The surface is still real. The gradient of $C$ near the zero controls how much mode structure leaks through. Hawking radiation is residual sampling at exponentially suppressed amplitude. The spectral analog (§II.A): at $s = 0$, the torsion $Z'_\sigma(0)$ carries L-function content through the spectral zero, with the amount of content controlled by the derivative.

Recovery of $T = \hbar c^3 / (8\pi G M k_B)$ from the phase operator: OPEN.

### Mergers

Two $\Theta = 0$ ($C = 0$) regions combine. Total enclosed content adds. New boundary area exceeds the sum of parent areas. The area theorem (Hawking 1971: horizon area never decreases) follows: you cannot extract $n = 2$ wave content through a zero-sampling boundary. Content can enter. Content cannot leave. The boundary grows or holds. It cannot shrink.

### Evaporation

If Hawking radiation carries energy away, enclosed content decreases, the $\Theta = 0$ boundary contracts, the $C$ gradient steepens, radiation increases. Runaway process. The final state is an open question: does the 120-grid impose a minimum remnant?

---

## VI. The Phase Walk and the Directional Problem

The §9 phase field shifts $\Theta$ by one bosonic step (2/120) inside a galactic potential. The black hole case looks like the same mechanism driven to the boundary. But there is a constraint.

### The bosonic domain has a wall

The full 120-grid comes from $|2I| = 120$. Observation squares the wavefunction, projecting $2I \to I$, giving the 60R bosonic grid. This projection traces to the edge stabilizer $Z_4 \subset 2I$: integer-spin irreps carry only real $Z_4$ content ($D = 60$), half-integer carry only complex pairs ($D = 120$). For photon-mediated observables, the effective domain is $[0, 60/120]$. The antinode at 60/120 is the boundary of the bosonic domain. Bosonic sampling reaches $\Lambda$ and stops.

### The Hubble tension walks toward Λ

The galactic phase field adds $\Theta_f = 2/120$ to the $H_0$ well at 34/120, stepping it to 36/120. Toward the antinode. $C$ increases. This is the Hubble tension: one bosonic step on a slope, producing 8.4%.

### The horizon requires Θ → 0

$C = 0$ lives at $\Theta = 0$, the opposite end of the domain from $\Lambda$. The Hubble tension steps $\Theta$ away from zero. The horizon requires $\Theta$ arriving at zero. These point in opposite directions.

| Phenomenon | $\Theta$ direction | $C$ behavior |
|---|---|---|
| Hubble tension | Away from 0, toward $\Lambda$ | $C$ increases |
| Black hole horizon | Toward $\Theta = 0$ | $C$ decreases to zero |

This is the directional problem. The perturbative regime (galaxies: small $\Phi/c^2$, one discrete step) and the non-perturbative regime (horizons: $\Phi/c^2 \to -1/2$, complete sampling closure) may share the phase operator as common language without sharing the same pathway on the domain.

The spectral side exhibits the same directional asymmetry. Moving away from $s = 0$ opens the Pochhammer tower (factorization breaks, 28-32 of 32 characters contribute). Moving toward $s = 0$ collapses it (4 of 16 characters survive). The "clean" direction is toward the zero. The "messy" direction is away from it. This matches: the horizon (toward $\Theta = 0$, where $C$ vanishes) is where structure simplifies; the interior of the domain (away from both zeros) is where everything participates.

---

## VII. At the Core

At the center, $\Omega \to 0$. When there is no scale separation, the distinction between edge ($n = 1$) and surface ($n = 2$) loses operational meaning. Not conversion of one into the other, but dissolution of the hierarchy that distinguishes them. At Planck density ($\Omega = 1$), surface and edge are the same scale.

The wave content is still there. It cannot be sorted into "surface" and "edge" categories because the hierarchy has collapsed to unity. The mode structure is complete. The filing system is gone.

---

## VIII. Open Derivations

### VIII.1 The Φ → Θ Mapping (Priority 1)

Everything gates on this. A function mapping gravitational potential to phase position:

$$\Theta_f(r) = f\!\left(\frac{\Phi(r)}{c^2}\right)$$

**Requirements:**
- Weak-field limit: reproduces the §9 binary trigger (one bosonic step for galactic potentials)
- Strong-field limit: reaches $\Theta = 0$ (and therefore $C = 0$) at $\Phi/c^2 = -1/2$ (Schwarzschild horizon)
- Respects the 120-grid (discrete steps)

**Boundary condition:** $\Phi/c^2 = -1/2$ is dimensionless, exact, and given by GR. The mapping must land $\Theta$ at the domain boundary (a zero of $C$) when this value is reached.

The RH program's Shatto Theorem (The Mirror, Lemma 8) proved that the direct map $s \leftrightarrow \Theta$ does not exist on the spectral side: continuous position drops out of the spectral data on $S^3/2I$ due to right-$\mathrm{SU}(2)$ homogeneity, and the direct bridge between the phase operator and the spectral zeta is structurally impossible. Whether the $\Phi \to \Theta$ mapping on the physical side faces an analogous obstruction, or whether the gravitational potential provides the "discrete localization" that the spectral geometry lacks, is an open question.

### VIII.2 Minimum Black Hole Mass (Priority 2)

If $\Theta$ advances in discrete steps, there may be a minimum enclosed mass required to push $\Theta$ all the way to the domain boundary (and therefore $C$ to zero). Below that mass, the potential never accumulates enough steps to reach a node. GR allows black holes of any mass. A minimum mass from the lattice spacing would be a new quantitative prediction that GR does not make.

### VIII.3 Discrete Horizon Structure (Priority 3)

If the approach to $\Theta = 0$ is stepped rather than smooth, the horizon has fine structure set by the 120-grid:

- Hawking spectrum: deviations from perfect Planck blackbody, set by lattice geometry
- Horizon area: quantized in units related to grid spacing
- Quasi-normal modes: discrete structure in gravitational wave ringdown frequencies

Testable against LIGO/LISA ringdown data. Requires the $\Phi \to \Theta$ mapping first.

### VIII.4 Black Hole Thermodynamics (Priority 4)

| Law | GR statement | MIT target |
|---|---|---|
| Zeroth | $\kappa$ constant on horizon | Phase operator uniformity at the $\Theta = 0$ surface |
| First | $dM = (\kappa/8\pi)dA + \Omega\,dJ + \Phi\,dQ$ | Energy balance from mode accounting |
| Second | $dA \geq 0$ | Wave content behind $\Theta = 0$ boundary cannot decrease |
| Third | Cannot reach $\kappa = 0$ in finite steps | Cannot reach $\Theta = 0$ (and therefore $C = 0$) in finite discrete steps (lattice property) |

The third law is interesting: the 120-grid may force an asymptotic approach to $\Theta = 0$, never exactly reached in finite steps. The third law becomes a topological statement about lattice resolution.

### VIII.5 Spectral-Physical Bridge (Priority 5, new)

The structural parallel between the scaling double zero ($\Theta \to 0$ driving $C \to 0$, with $\Omega_H \to 0$ as independent partner) and the spectral double zero ($Z_\sigma(0) = 0$, $(s)_k = 0$) is established (§II.A). The $s \leftrightarrow \Theta$ map on the spectral side is proved not to exist by the Shatto Theorem (The Mirror, Lemma 8): the spectral and scaling sides are structurally parallel but cannot be connected by a natural map. The open question is whether the torsion survivor $Z'_\sigma(0) = \log T^2$ can be connected to the physical survivor (Hawking radiation gradient) through a route other than the direct spectral-to-phase bridge. If the torsion values $\{\log 2, \log 3, \log 5, \log\varphi\}$ constrain the horizon structure through the same arithmetic that constrains the fermion mass spectrum (engine §13), the spectral and physical sides of the double zero would be unified. This would close the loop between Tools 3 and 5 at the boundary of the domain.

---

## Quick Reference

| Quantity | Value | Source |
|---|---|---|
| $\Theta = 0$ and $\Theta = 1$ | Boundary of domain | Phase position at the wall; both are zeros of $C$ |
| $C(0) = C(1)$ | 0 | Phase operator at boundary ($\Theta$ at the wall drives $C$ to zero) |
| $C'(0) = C'(1)$ | 0 | Quadratic vanishing |
| $C''(0)$ | $4\pi^2$ | Leading nonvanishing order |
| $C(60/120)$ | 2.00 | Antinode ($\Lambda$) |
| $\Phi/c^2$ at Schwarzschild horizon | $-1/2$ | GR (exact) |
| Bosonic domain | $[0, 60/120]$ | $\lvert I \rvert = 60$ from squaring |
| Bosonic step | $2/120 = 1/60$ | Minimum observable shift |
| Full domain | $[0, 120/120]$ | $\lvert 2I \rvert = 120$ |
| Fermionic step | $1/120$ | Full lattice resolution |
| Bekenstein-Hawking entropy | $S = A/(4\ell_P^2)$ | Observed; MIT: surface mode count |
| Hawking temperature | $T = \hbar c^3/(8\pi G M k_B)$ | Observed (indirectly); MIT: $C$ gradient (OPEN) |
| $Z_\sigma(0)$ | 0 | Spectral determinant at boundary (nontrivial $\sigma$) |
| $Z'_\sigma(0)$ | $\log T^2(\sigma)$ | Torsion: L-function special values |
| Torsion survivors | $\{\log 2, \log 3, \log 5, \log\varphi\}$ | 4 of 16 characters, $E_8$ selected; conductors are the stabilizer primes of the icosahedron |

---

*The wave persists. The topology holds. The observer goes silent.*

---

/ **[`framework/`](../framework/)** / **[`cosmos/`](../cosmos/)** / **[`spectrum/`](../spectrum/)** /
