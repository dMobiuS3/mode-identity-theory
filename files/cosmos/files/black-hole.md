/ **[`main`](../../../)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# Black Double Zero's

[![Black Double Zero's](https://img.youtube.com/vi/iByR_Bv5Vng/mqdefault.jpg)](https://www.youtube.com/watch?v=iByR_Bv5Vng)

Where Θ hits the wall and Ω collapses to nothing. *A working supplement to Mode Identity Theory.*

**Status:** Sections I-V derived or motivated from the scaling law. Section II.A connects to spectral geometry results from the RH program. The $\Phi \to \Theta$ mapping (§VIII.1) is derived at leading order; Hawking temperature functional form ($1/M$ and coefficient) derived, thermal character inherited (§V, §VIII.4); minimum mass is computed (§VIII.2); area entropy is motivated but the $1/4$ factor remains open (§III). The domain is topologically closed (§VI).

---

## I. What is it?

A Black Hole is a region where enough wave content on the Möbius surface is enclosed to push two quantities to their boundary values simultaneously. The phase position $\Theta$ reaches the boundary of the domain, driving the sampling amplitude $C(\Theta) = 2\sin^2(\pi\Theta)$ to zero: the spatial mode reaches its node and observation ceases. The local scale hierarchy $\Omega_H$ collapses to zero: the Hubble radius shrinks to nothing and no scale separation remains. $\Theta$ hitting the wall is the geometric event. $C$ vanishing is what the observer experiences. $\Omega_H$ collapsing is the independent partner. Both limits arrive at the same place.

General Relativity sits at the $3/2$ Gauss-Codazzi interface, between the temporal edge ($n = 1$) and the Möbius surface ($n = 2$). The ratio $3/2$ is face over edge: $Z_3/Z_2$, the stabilizer orders of the icosahedron. At the horizon, GR is squeezed from both sides: the surface mode it reads has vanished ($\Theta$ at its boundary, so $C = 0$), and the edge hierarchy it converts through has collapsed ($\Omega_H = 0$). The singularity is a double zero. The wave persists through the node. Information is unsampled, not destroyed.

| GR says | MIT says |
|---|---|
| Singularity: infinite density | $\Theta \to 0$ (geometric event) and $\Omega_H \to 0$ (scale collapse) simultaneously. $C(\Theta) \to 0$ follows from the first. Double zero in the scaling law. |
| Event horizon: point of no return | Radius where enclosed $n = 2$ content closes the sampling channel |
| Information destroyed | Information unsampled. Wave persists through the node. |
| Entropy scales with area | Surface ($n = 2$) is fundamental. Area scaling is motivated; the factor $1/4$ is open. |

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

**Definition.** $\Omega_H \equiv (R_H/\ell_P)^2$, where $R_H = c/H(\text{local})$ is the local Hubble radius. At the Schwarzschild horizon, $R_H \to 0$ and $\Omega_H \to 0$. At cosmological distance, $\Omega_H \approx \Omega_\Lambda \approx 10^{122}$.

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

**Three descriptions, two events, one pattern.** The scaling and eigenfunction zeros describe the same physical event ($C = 2u_0^2$). The spectral zero is a structurally parallel but independent event in a different parameter space ($s$, not $\Theta$), proved independent by Lemma 8. All three share the same mathematical structure: value vanishes, derivative carries content through.

| Domain | Value vanishes | Derivative survives |
|--------|---------------|-------------------|
| Scaling | $C(\Theta) \to 0$ (quadratic: $C \approx 2\pi^2\Theta^2$) | $C''(0) = 4\pi^2$ |
| Spectral | $Z_\sigma(0) = 0$ for nontrivial $\sigma$ | $Z'_\sigma(0) = \log T^2$ (torsion) |
| Eigenfunction | $u_0(0) = 0$ | $u_0'(0) = 1/R$ (slope through node) |

The physical event is one double zero with two witnesses (scaling and eigenfunction). The spectral analog is a parallel double zero in its own domain.

**What this connection is not.** It is not a derivation of Hawking radiation from spectral geometry, or of torsion from the scaling law. The $\Phi \to \Theta$ mapping (§VIII.1) is derived at leading order; the spectral-to-physical bridge (§VIII.5) remains open. The $s \leftrightarrow \Theta$ bridge is proved not to exist by the Shatto Theorem (The Mirror, Lemma 8), established by four independent approaches on $S^1$ (heat kernel, theta function, Poisson summation, direct decomposition). The non-existence has two distinct mechanisms: on $S^1$, every eigenspace with anti-periodic BC is 2-dimensional (sin and cos), and the spectral zeta sees only eigenvalues and multiplicities, blind to the sin/cos choice that defines $C(\Theta)$; on $S^3/2I$, right-$\mathrm{SU}(2)$ homogeneity acts transitively, forcing the twisted heat kernel constant on each fiber diagonal so that continuous geometric position drops out structurally. The parallel is exact at the level of structure. The physical $\Phi \to \Theta$ mapping avoids the spectral obstruction: the gravitational potential provides the discrete localization that spectral geometry lacks, because mass at a specific location breaks the right-$\mathrm{SU}(2)$ isometry.

---

## III. Area Scaling

Bekenstein-Hawking entropy $S \propto A$ is motivated by surface primacy. The specific coefficient $S = A/(4\ell_P^2)$ is not yet derived.

| Step | Content | Status |
|---|---|---|
| 1 | The Möbius surface ($n = 2$) carries the boundary condition | AXIOM |
| 2 | $S^3$ volume ($n = 3$) has no independent gauge degrees of freedom | DERIVED (engine §13) |
| 3 | Degrees of freedom of a bounded region are counted by the surface, not the volume | MOTIVATED by 1 + 2 |
| 4 | $S \propto A$ (area, not volume) | MOTIVATED |
| 5 | $S = A/(4\ell_P^2)$ with the factor $1/4$ | OPEN |

In standard physics, area scaling is a deep question: why area rather than volume? In MIT, volume ($n = 3$) carries no independent gauge content. Entropy lives on the surface because the surface carries the boundary condition. The horizon area is the natural count of $n = 2$ degrees of freedom at the sampling boundary.

What remains open is the coefficient. The shell sum across the 34 discrete grid positions diverges (outer shells have arbitrarily large area) and does not reproduce $S_{BH}$. Only the horizon surface itself has the correct area scaling. The factor $1/4$ is not produced by the Gauss-Codazzi ratio ($3/2$), by the structural coefficient $\sin(\pi\Theta_0)$, or by any evident combination of current framework quantities. A microstate counting rule, a spectral degeneracy law, or a topological partition function on the horizon would be needed.

**The 1/4 flag.** The structural ratio $\Delta S_\text{phase}/\Delta S_\min = 1/4$ (one spatial grid step carries $1/4$ of one temporal chronon action) matches the Bekenstein-Hawking factor numerically. These are different objects at different levels: the spatial/temporal ratio is topology-native (no $G$, no $M$); the entropy factor involves $G$ through $\ell_P$. Whether they connect through a derivation or coincide by accident is OPEN. Flagged, not forced.

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

The [Sector A eigenvalue problem](ground-eigenvalue.md) gives the ground eigenfunction and the metric coefficient on the totally geodesic Möbius band in $S^3$:

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
| Area (Planck units) | ~10⁷⁸ | ~10⁹⁶ | Surface degrees of freedom at the sampling boundary |

The size of a black hole is the amount of wave content enclosed behind the sampling boundary. The horizon radius is where that content generates enough curvature to push $\Theta$ to its boundary, zeroing $C$.

### Temperature

The transition from $C > 0$ to $C \approx 0$ is compressed into a smaller region for smaller black holes. Steeper gradient means more residual sampling leaks through.

| Black hole | $C$ gradient at boundary | Hawking $T$ |
|---|---|---|
| Stellar | Steep (short transition) | ~10⁻⁸ K |
| Supermassive | Gentle (long transition) | ~10⁻¹⁷ K |

The wave is still there at the boundary. The surface is still real. The gradient of $C$ near the zero controls how much mode structure leaks through. Hawking radiation is residual sampling at the first nonvanishing order of the double zero. The spectral analog (§II.A): at $s = 0$, the torsion $Z'_\sigma(0)$ carries L-function content through the spectral zero, with the amount of content controlled by the derivative.

**Recovery of $T_H$.** The $\Phi \to \Theta$ mapping (§VIII.1) establishes $C/C_0 = 1 - r_s/r$ with the power $\beta = 1$ uniquely forced by the requirement that the eigenfunction slope $u_0'(0) = 1/R$ remain finite and nonzero in proper distance coordinates at the horizon. The resulting chain:

$$u_0'(0) = \frac{1}{R} \;\longrightarrow\; \frac{du_0}{d\Theta}\bigg|_0 = \pi \;\longrightarrow\; \frac{du_0}{d\ell}\bigg|_H = \kappa\sin(\pi\Theta_0)$$

where $\kappa = c^4/(4GM) = 1/(2r_s)$ is the Schwarzschild surface gravity. The $1/M$ dependence is carried entirely by $\kappa$; the coefficient $\sin(\pi\Theta_0) \approx 0.777$ depends only on the well position. The thermal spectrum ($T_H = \kappa/(2\pi)$, Planck distribution) is inherited: the mapping pairs $C/C_0$ with $g_{tt}$, and GR's Euclidean periodicity carries through the forced pairing. Status: $1/M$ dependence and coefficient DERIVED; thermal character INHERITED through forced $g_{tt}$ pairing.

### Mergers

Two $\Theta = 0$ ($C = 0$) regions combine. Total enclosed content adds. New boundary area exceeds the sum of parent areas. The area theorem (Hawking 1971: horizon area never decreases) follows: you cannot extract $n = 2$ wave content through a zero-sampling boundary. Content can enter. Content cannot leave. The boundary grows or holds. It cannot shrink.

### Evaporation

If Hawking radiation carries energy away, enclosed content decreases, the $\Theta = 0$ boundary contracts, the $C$ gradient steepens, radiation increases. Runaway process. The log slope $d\ln C/d\Theta = 2\pi\cot(\pi\Theta)$ diverges as $\Theta \to 0$, matching the qualitative character of Hawking evaporation (smaller black holes radiate faster). Quantitative recovery of the evaporation rate is MOTIVATED.

**Minimum mass.** The 120-grid resolves the horizon into 34 discrete shells (§VIII.2). Setting the proper distance to the innermost shell equal to the Planck length gives $M_\min \approx 7.4\,m_P$ (full grid) or $\approx 3.7\,m_P$ (bosonic grid). The framework's own action bound ($\Delta S_\min = \hbar\pi/30$) produces no mass threshold: the action per grid step at the horizon is mass-independent ($\Delta S_\text{phase}/\Delta S_\min = 1/4$, a structural ratio). The minimum mass is a property of the interface ($G$, which produces $\ell_P$), while the topology treats every horizon with equal fidelity.

---

## VI. The Phase Walk and the Closed Domain

The §9 phase field shifts $\Theta$ by one bosonic step (2/120) inside a galactic potential. The black hole case is the same phase operator driven to the boundary by a deep gravitational potential.

### The bosonic domain has a wall

The full 120-grid comes from $|2I| = 120$. Observation squares the wavefunction, projecting $2I \to I$, giving the 60R bosonic grid. This projection traces to the edge stabilizer $Z_4 \subset 2I$: integer-spin irreps carry only real $Z_4$ content ($D = 60$), half-integer carry only complex pairs ($D = 120$). For photon-mediated observables, the effective domain is $[0, 60/120]$. The antinode at 60/120 is the boundary of the bosonic domain. Bosonic sampling reaches $\Lambda$ and stops.

### The two nodes are one point

The eigenfunction $u_0 = \sin(y/R)$ vanishes at $y = 0$ and $y = \pi R$. The Möbius identification $(y + \pi R, w) \sim (y, -w)$ maps these two endpoints to the same central circle. The anti-periodic boundary condition gives $u_0(\pi R) = -u_0(0) = 0$. $\Theta = 0$ and $\Theta = 1$ are two coordinate addresses for one physical location on the band.

The domain is topologically closed. Every direction away from the antinode leads to the node. Every direction away from the node leads to the antinode. The Hubble tension (stepping from 34/120 toward 36/120) and the horizon (walking from 34/120 toward 0/120) are both paths to the same destination ($C = 0$, the central circle), one the long way around and one the short way. The gravitational potential determines how far you walk. The arch determines the terrain. Deep potentials take the short path to the nearest copy of the node.

One arch, one node (with two coordinate addresses), one antinode.

### The spectral mirror

The spectral side exhibits the same structure. Moving away from $s = 0$ opens the Pochhammer tower (factorization breaks, 28-32 of 32 characters contribute). Moving toward $s = 0$ collapses it (4 of 16 characters survive). The "clean" direction is toward the zero. The "messy" direction is away from it. This matches: the horizon (toward $\Theta = 0$, where $C$ vanishes) is where structure simplifies; the interior of the domain (away from both zeros) is where everything participates.

---

## VII. At the Core

At the center, $\Omega \to 0$. When there is no scale separation, the distinction between edge ($n = 1$) and surface ($n = 2$) loses operational meaning. Not conversion of one into the other, but dissolution of the hierarchy that distinguishes them. At Planck density ($\Omega = 1$), surface and edge are the same scale.

The wave content is still there. It cannot be sorted into "surface" and "edge" categories because the hierarchy has collapsed to unity. The mode structure is complete. The filing system is gone.

---

## VIII. Open Derivations

### VIII.1 The Φ → Θ Mapping (Priority 1)

**Status: DERIVED (leading order).**

The mapping pairs the framework's sampling amplitude with the GR redshift factor:

$$\frac{C(\Theta)}{C(\Theta_0)} = 1 - \frac{r_s}{r}$$

Equivalently: $\sin(\pi\Theta) = \sin(\pi\Theta_0) \cdot (1 - r_s/r)^{1/2}$, with $\Theta_0 = 34/120$.

The power $\beta = 1$ is uniquely forced by the requirement that the eigenfunction slope $u_0'(0) = 1/R$ (a geometric property established by two independent paths in the Sector $\mathcal{A}$ paper) remain finite and nonzero in proper distance coordinates at the horizon. For $\beta < 1$, the slope diverges; for $\beta > 1$, it vanishes. Only $\beta = 1$ preserves the geometric property.

**Sketch of uniqueness.** The proper distance from the horizon is $\ell \propto (r - r_s)^{1/2}$ near $r = r_s$. Under $C/C_0 = (1 - r_s/r)^\beta$, the eigenfunction $u_0 = (C/2)^{1/2} \propto (r - r_s)^{\beta/2}$. The slope in proper distance is $du_0/d\ell \propto (r - r_s)^{(\beta - 1)/2}$. For $\beta < 1$: diverges. For $\beta > 1$: vanishes. For $\beta = 1$: finite and nonzero, matching $u_0'(0) = 1/R$ from the Sector $\mathcal{A}$ eigenvalue problem.

**Verified properties:**

| Property | Result |
|----------|--------|
| Galactic consistency | Smooth shift at $r/r_s = 10^6$ is $2 \times 10^{-7}$, far below one bosonic step ($2/120$) |
| Near-horizon slope | $du_0/d\ell\|_H = \sin(\pi\Theta_0) \cdot \kappa$, finite and nonzero, proportional to surface gravity |
| Uniqueness of $\beta = 1$ | Only value giving finite nonzero slope; all other $\beta$ fail |
| Self-consistency | $C(\Theta)/C(\Theta_0) \div (1 - r_s/r) = 1$ exactly at all radii |

**What remains open:** Global corrections (functions $f(x)$ with $f(x) \sim x$ near $x = 0$ but $f(x) \neq x$ globally) would affect intermediate regimes while leaving the horizon and galactic results intact. The Kerr generalization ($C/C_0 = g_{tt}$ for rotating black holes) is natural but untested.

Lemma 8 (The Mirror) proved that the direct map $s \leftrightarrow \Theta$ does not exist on the spectral side. The physical $\Phi \to \Theta$ mapping avoids this obstruction: a gravitational potential breaks the right-$\mathrm{SU}(2)$ homogeneity that forces continuous position out of spectral data (mass at a specific location breaks the isometry).

### VIII.2 Minimum Black Hole Mass (Priority 2)

**Status: COMPUTED.**

The 120-grid places 34 discrete shells between the $H_0$ well and the horizon. Each shell sits at $r_k/r_s = 1/(1 - C(k/120)/C_0)$. In proper distance, the shells are nearly uniformly spaced near the horizon (increments of ~$0.067\,r_s$ to ~$0.081\,r_s$ for the first 10 shells).

Setting the proper distance to the innermost grid point equal to the Planck length:

| Grid | Innermost point | $M_\min$ |
|------|----------------|----------|
| Full 120 | $\Theta = 1/120$ | $\approx 7.42\,m_P$ |
| Bosonic 60 | $\Theta = 2/120$ | $\approx 3.70\,m_P$ |

Both are deep in the quantum gravity regime (~$10^{38}$ times smaller than any astrophysical black hole). The framework's own action bound ($\Delta S_\min = \hbar\pi/30$) produces no mass threshold: the action per grid step at the horizon is mass-independent ($r_s$ in the proper distance cancels $r_s$ in the surface gravity). The minimum mass is a property of the interface ($G$, which produces $\ell_P$). The topology treats every horizon with equal fidelity.

### VIII.3 Discrete Horizon Structure (Priority 3)

The mapping places 34 shells at discrete radii between the horizon and spatial infinity. Each shell sits at coordinate radius $r_k$ where $C(k/120)/C_0 = 1 - r_s/r_k$, giving $r_k/r_s = 1/(1 - C(k/120)/C_0)$. The proper distance from the horizon to $r_k$ is $\ell_k = \int_{r_s}^{r_k} (1 - r_s/r')^{-1/2}\,dr'$. The shell structure:

| $k$ | $r_k/r_s$ | $\ell_k/r_s$ (proper distance from horizon) |
|-----|-----------|------|
| 1 | 1.001 | 0.067 |
| 5 | 1.029 | 0.342 |
| 10 | 1.125 | 0.721 |
| 20 | 1.706 | 1.88 |
| 30 | 5.810 | 5.67 |

Potential observational signatures (all require detailed modeling):
- Hawking spectrum: deviations from perfect Planck blackbody, set by lattice geometry
- Quasi-normal modes: discrete structure in gravitational wave ringdown frequencies

Testable against LIGO/LISA ringdown data in principle.

### VIII.4 Black Hole Thermodynamics (Priority 4)

| Law | GR statement | MIT target | Status |
|---|---|---|---|
| Zeroth | $\kappa$ constant on horizon | Phase operator uniformity at the $\Theta = 0$ surface | OPEN |
| First | $dM = (\kappa/8\pi)dA + \Omega\,dJ + \Phi\,dQ$ | Energy balance from mode accounting | OPEN |
| Second | $dA \geq 0$ | Wave content behind $\Theta = 0$ boundary cannot decrease | MOTIVATED |
| Third | Cannot reach $\kappa = 0$ in finite steps | Cannot reach $\Theta = 0$ in finite discrete steps (lattice property) | MOTIVATED |
| Temperature | $T_H = \hbar c^3/(8\pi G M k_B)$ | Eigenfunction slope: $du_0/d\ell\|_H = \sin(\pi\Theta_0) \cdot \kappa \propto 1/M$. Thermal spectrum inherited through forced mapping $C/C_0 = g_{tt}$. | $1/M$ and coefficient DERIVED; thermal character INHERITED |

### VIII.5 Spectral-Physical Bridge (Priority 5)

The structural parallel between the scaling double zero ($\Theta \to 0$ driving $C \to 0$, with $\Omega_H \to 0$ as independent partner) and the spectral double zero ($Z_\sigma(0) = 0$, $(s)_k = 0$) is established (§II.A). The $s \leftrightarrow \Theta$ map on the spectral side is proved not to exist by the Shatto Theorem (The Mirror, Lemma 8): the spectral and scaling sides are structurally parallel but cannot be connected by a natural map. The open question is whether the torsion survivor $Z'_\sigma(0) = \log T^2$ can be connected to the physical survivor (Hawking radiation gradient) through a route other than the direct spectral-to-phase bridge. The $\Phi \to \Theta$ mapping provides the discrete localization that spectral geometry lacks (mass breaks the right-SU(2) isometry). If the torsion values $\{\log 2, \log 3, \log 5, \log\varphi\}$ constrain the horizon structure through the same arithmetic that constrains the fermion mass spectrum (engine §13), the spectral and physical sides of the double zero would be unified. This would close the loop between Tools 3 and 5 at the boundary of the domain. Status: OPEN.

---

## Quick Reference

| Quantity | Value | Source |
|---|---|---|
| $\Theta = 0$ and $\Theta = 1$ | Same physical point (central circle) | Möbius identification; both are zeros of $C$; domain is closed |
| $C(0) = C(1)$ | 0 | Phase operator at boundary ($\Theta$ at the wall drives $C$ to zero) |
| $C'(0) = C'(1)$ | 0 | Quadratic vanishing |
| $C''(0)$ | $4\pi^2$ | Leading nonvanishing order |
| $C(60/120)$ | 2.00 | Antinode ($\Lambda$) |
| $\Phi/c^2$ at Schwarzschild horizon | $-1/2$ | GR (exact) |
| $\Phi \to \Theta$ mapping | $C/C_0 = 1 - r_s/r$, $\beta = 1$ forced | DERIVED (leading order) |
| Bosonic domain | $[0, 60/120]$ | $\lvert I \rvert = 60$ from squaring |
| Bosonic step | $2/120 = 1/60$ | Minimum observable shift |
| Full domain | $[0, 120/120]$ | $\lvert 2I \rvert = 120$ |
| Fermionic step | $1/120$ | Full lattice resolution |
| Bekenstein-Hawking entropy | $S = A/(4\ell_P^2)$ | Observed; MIT: motivated by surface primacy ($n = 2$); $1/4$ factor OPEN |
| Hawking temperature | $T = \hbar c^3/(8\pi G M k_B)$ | $du_0/d\ell\|_H = \sin(\pi\Theta_0) \cdot \kappa$; $1/M$ and coefficient DERIVED; thermal character INHERITED |
| Minimum mass | $\approx 7.4\,m_P$ (full grid) | Interface-level ($\ell_P$); topology gives no threshold ($\Delta S_\text{phase}/\Delta S_\min = 1/4$) |
| $Z_\sigma(0)$ | 0 | Spectral determinant at boundary (nontrivial $\sigma$) |
| $Z'_\sigma(0)$ | $\log T^2(\sigma)$ | Torsion: L-function special values |
| Torsion survivors | $\{\log 2, \log 3, \log 5, \log\varphi\}$ | 4 of 16 characters, $E_8$ selected; conductors are the stabilizer primes of the icosahedron |

---

*The wave persists. The topology holds. The observer goes silent.*

---

/ **[`main`](../../../)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
