/ **[`main`](/README.md)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/geometric%20code%20banner.png?raw=true" width="100%" alt="The Geometric Code: Mode Identity Theory">

Mode Identity Theory is a boundary-condition framework. It keeps Einstein's field equations governing local gravitational dynamics and the Standard Model particle content unchanged, but supplies a global topological domain:

```math
S^1 = \partial(\text{Möbius}) \hookrightarrow S^3,
\qquad
\partial S^3 = \emptyset .
```

In plain terms, before the formal names arrive: twist a strip into a Möbius band, scale its single edge up to the size of the universe, and set the whole thing inside $`S^3`$, the one closed three-dimensional space with no boundary and no holes. That shape is the entire theory. The particles, the forces, and the constants arise from the shape itself, read off as values at positions.

That shape has two layers: the smooth space $`S^3`$ underneath, and the structure built on it where the physics is read off. The topology lives in that built structure; $`S^3`$ itself is smooth and hole-free.

The postulate says that time is the boundary of a non-orientable surface embedded in a closed three-space. The observable domain is the Poincaré homology sphere,

```math
M = S^3/2I,
```

where $`2I`$ is the binary icosahedral group of order 120. From that shape the topology fixes the mode domain, boundary condition, stabilizers, and McKay graph, and the relations that follow: well positions, hierarchy exponents, grid assignments, dimensionless ratios, and spectral filters. Measured anchors set only the absolute scales.

## The Firing Order

Each layer follows from the one before.

1. Topology sets what is possible.
2. Embedding defines the structure.
3. The Cosmic Wave expresses the boundary.
4. Time is phase of the wave.
5. Sampling resolves position in the domain.
6. Meaning arises only after realization.

[![One Shape](https://img.youtube.com/vi/U3VtY8GZox8/mqdefault.jpg)](https://www.youtube.com/watch?v=U3VtY8GZox8)

---

### Contents

The page moves in one line, each section following from the one before:

- **[The Firing Order](#the-firing-order)** · the six-step order of operations
- **[One Shape](#one-shape)** · the postulate, and the manifold triad it forces
- **[One Wave](#one-wave)** · the static standing wave, and the phase clock on its edge
- **[One Equation](#one-equation)** · the scaling law, its phase operator and Fibonacci wells
- **[One Formula](#one-formula)** · confinement, three generations, and the mass ladder
- **[One Identity](#one-identity)** · 120 = 2³·3·5, sorting charge, spin, and isospin
- **[One Interface](#one-interface)** · the two seams, and what gravity is across them
- **[Inputs and Calibration](#inputs-and-calibration)** · the ledger of what is measured and what is derived

---

<a id="one-shape"></a>

## :stadium: One Shape

```math
\Large {S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset}
```

A temporal edge bounds a non-orientable surface embedded in a closed space. The space has no boundary. The manifold triad is pinned by a theorem and a minimality choice: surface classification plus minimality selects the Möbius strip (the minimal non-orientable surface with one boundary), and the simply connected closed cover is $`S^3`$ by the Poincaré theorem, with the observable domain its quotient $`S^3/2I`$. With minimality, the postulate has one realization.

### Space

$`S^3`$ is the only simply connected closed 3-manifold (Poincaré). It is diffeomorphic to SU(2) and admits a spin structure. Its curvature radius is $`R_\Lambda`$. The space has no boundary:

```math
\Large {\partial S^3 = \emptyset}
```

The hierarchy terminates here. "What's outside?" is malformed; there is no boundary from which to observe.

### Surface

A Möbius strip has one side and one edge. Carry the normal once around it and it returns reversed, and that single sign flip is the topological source of the spinorial structure that matter on this domain rides on. It is also the simplest surface that does this: by the classification of compact surfaces, a connected non-orientable surface with one boundary component is a disk removed from a connected sum of $`k`$ crosscaps, and the Möbius strip is the minimal case ($`k = 1`$), the one minimality selects. Non-orientability produces three consequences:

| Consequence | Mechanism |
|---|---|
| Anti-periodic BC | Sections of the orientation bundle acquire a sign flip: $`\psi(y + \pi R_\Lambda) = -\psi(y)`$ |
| Half-integer spectrum | Mode numbers $`\nu = 1/2, 3/2, 5/2, \ldots`$; the constant mode is forbidden |
| $`Z_2`$ holonomy | The normal direction reverses under one traversal |

Orientable surfaces produce none of these.

The eigenvalue problem $`-\partial_y^2 \psi = \lambda \psi`$ under the anti-periodic BC requires $`e^{ik\pi R_\Lambda} = -1`$, giving $`k = (2m+1)/R_\Lambda`$. Defining the mode number $`\nu = kR_\Lambda/2`$, the allowed values are $`\nu = 1/2, 3/2, 5/2, \ldots`$: half-integers in this normalization. The constant mode ($`k = 0`$) is forbidden. 

The field $`\psi`$ is a section of the orientation line bundle: the unique nontrivial real line bundle on a non-orientable surface, whose sections pick up a sign flip under the orientation-reversing identification. Coupling the physical field to that orientation structure gives matter its spinorial character: the $`Z_2`$ sign and half-integer spectrum that matter's fermionic character rides on.

### Temporal Edge

$`S^1`$ is the boundary of the Möbius surface. The strip has longitudinal period $`L = \pi R_\Lambda`$ (one lap); the boundary $`S^1`$ traverses the strip twice before closing, giving geometric circumference $`2L = 2\pi R_\Lambda`$. The anti-periodic flip acts per lap, $`\psi(y + \pi R_\Lambda) = -\psi(y)`$, on the one-lap lift of the orientation-twisting core loop, not on the closed edge itself. Over two laps the field returns to $`+\psi`$, so the closed edge is globally periodic with trivial total orientation holonomy, while the $`4\pi`$ wave period lives on the lifted phase coordinate. This is where time advances and where the observer is anchored. The $`S^1`$ here is the phase cycle of the standing wave, not a closed timelike coordinate of the Lorentzian metric; proper time along an observer history is monotone over the epoch.

The chronon and standing wave period operate in the phase parameter $`t \in [0, 4\pi]`$, not in geometric length. The factor $`4\pi`$ is the anti-periodic wave period (two sign-flip laps of the strip), dimensionless.

### The Observable Domain

The physical space is $`S^3/2I`$: the hypersphere modulo the binary icosahedral group $`2I`$, with $`\lvert 2I\rvert = 120`$. The discrete subgroups of SU(2) $`\cong S^3`$ are classified: open families (cyclic $`Z_n`$ and binary dihedral $`2D_n`$, parameterized by $`n`$) and three closed exceptional groups (binary tetrahedral $`\lvert 2T\rvert = 24`$, binary octahedral $`\lvert 2O\rvert = 48`$, binary icosahedral $`\lvert 2I\rvert = 120`$). 

Open families require external choice of $`n`$ and are excluded by the framework's input-minimization. Among the closed exceptional cases, $`2I`$ is terminal: largest in order and maximal under the McKay correspondence ($`2I \leftrightarrow E_8`$, the largest exceptional Lie algebra). And it is the unique *perfect* subgroup, the only one carrying the 9× Galois gap the three generations require (below). So the selection rests on a framework requirement and a uniqueness theorem, not on minimization alone.

**The 120 domain** is the mode spectrum's representation resolution. Fermions access the full 120-label domain, but observation squares the wavefunction: $`\lvert\psi(\Theta+1)\rvert^2 = \lvert\psi(\Theta)\rvert^2`$ erases the anti-periodic sign. At the representation and intensity level, the squaring passes from the $`2I`$ labels to the $`I`$ labels ($`\lvert I\rvert = 60`$), halving the observable label resolution.

| Grid | Labels | Minimum step | Observables |
|---|---|---|---|
| Full domain | 120 | 1/120 | $`a_0`$ (dynamical) |
| Bosonic projection | 60 | 2/120 | $`H_0`$, $`\Lambda`$, $`\alpha`$ (photon-mediated) |

Group theory of $`S^3`$ gives $`\lvert 2I\rvert = 120`$ directly, and the same factorization $`120 = 2^3 \cdot 3 \cdot 5`$ surfaces across several domains:
1. $`\text{lcm}(1,2,3,5,8) = 120`$, the first five Fibonacci numbers
2. the consonance ratios of musical harmony resolve to the same $`\text{lcm} = 120`$
3. the $`(2,3,5)`$ branch orders of the icosahedron are consecutive Fibonacci numbers satisfying $`2+3=5`$, the unique Platonic solid whose symmetry orders obey the Fibonacci recurrence

The group order is the source; the arithmetic keeps returning to the same factorization.

**The chronon** is the smallest phase advance the 120-label sampling can register:

```math
\Delta t_{\min} = \frac{4\pi}{120} = \frac{\pi}{30}
```

**The minimum action** $`\Delta\mathcal{S}_{\min} = \hbar\pi/30`$: frame-independent by construction ($`\hbar`$ is invariant; $`\pi/30`$ is a pure number set by the topology, not by a coordinate choice).

[↑ Contents](#contents)

<a id="one-wave"></a>

## Ψ One Wave

The universe is static, a standing wave, and what we read as cosmic time is the observer's phase along it. The wave sits on the Möbius temporal edge, so the same sign flip that gives matter its spinorial character acts on it: one lap of the strip flips the wave, and the edge closes only after a second, bringing it home, which is why its fundamental period is $`4\pi`$ rather than $`2\pi`$, the wave-level face of the spin-1/2 double cover. It opens at full amplitude, holds its lowest mode, and where the observer samples it, matter appears.

Anti-periodicity, the initial-maximum condition ($`\Psi(0) = +1`$), and selection of the lowest temporal harmonic ($`m = 0`$) together fix:

```math
\Large {\Psi = \cos(t/2)}
```

| Condition | Selects | Why |
|---|---|---|
| Anti-periodic BC | Period $`4\pi`$ | Sign flips per lap; two laps to restore it |
| $`\Psi(0) = +1`$ | Cosine over sine | $`t = 0`$ at amplitude maximum; $`\partial_t\Psi\big\vert_{t=0} = 0`$ |
| Lowest temporal harmonic $`m = 0`$ | No higher harmonics | Isotropy ($`10^{-5}`$) and orthogonality (Gpc integration) |

The cosine has a complement. Write $`S = \sin(t/2)`$; then $`\Psi^2 + S^2 = 1`$ partitions the total amplitude into two shares at every phase. The budget reading: $`\Psi^2`$ is standing-wave content, $`S^2`$ is realized-mode content, and cosmic evolution is this partition rotating, weight transferring $`\Psi^2 \to S^2`$ as the phase advances while the space stays static and the resolved fraction grows. That single state variable $`S`$ is what the cosmological observables read.

**One state, several readings.** The clock below turns $`S`$ into the Hubble rate $`H(z)`$, which with the topological $`\Lambda`$ supplying the vacuum term fits Pantheon+ and DESI DR2 BAO at $`\Delta\chi^2 = +0.11`$ versus flat ΛCDM at the same parameter count: a static universe recovering the distance ladder. The same $`S`$ answers the two questions a static cosmos invites. Redshift is a phase ratio, $`1 + z = S(t_\text{obs})/S(t_\text{emit})`$, the observer reading the wave from farther along it rather than space carrying source and observer apart. Static scopes to the $`S^3`$ topology and its fixed radius $`R_\Lambda`$, the domain where the eigenvalue problem and $`\Lambda = 3/R_\Lambda^2`$ live; the effective distance relation carries the scale factor $`a_\text{eff} \propto S`$, and in that effective metric the phase ratio is the ordinary null-geodesic result, so the standard FLRW distance relation is recovered. That FLRW form is the translation layer for comparison with observations. Cooling applies the same ratio to the bath in the effective metric, where $`a_\text{eff} \propto S`$ carries the volume: every wavelength rescales by $`S`$, photon number density by $`S^{-3}`$ at conserved photon count, and radiation energy density by $`S^{-4}`$, so the Planck blackbody is preserved at $`T \propto 1/S`$. The fixed quantity is that spectral radius, not the effective volume, and the energy accounting for the transfer that earns the cooling stays open. The [budget map](files/working/files/budget-map.md) keeps the full accounting.

The Waltz clock advances budget phase in two steps set by $`a \propto S`$ (the [budget note](files/working/files/temporal-budget.md) convention): the registered interface tick accumulates as $`d\mu_{\text{tick}} = S^{3/2}\,dt`$, and dividing by the scale factor (the kinematic dictionary, not a free definition) gives the Hubble clock $`d\tau_H = d\mu_{\text{tick}}/a = S^{1/2}\,dt`$ that the distance model runs on, with $`dt/d\tau_H = S^{-1/2}`$. The fitted rate is read on the Hubble clock, $`H = (1/S)\,dS/d\tau_H \propto \Psi/S^{3/2}`$; using $`d\mu_{\text{tick}}`$ in its place would give the discarded $`S^{-5/2}`$ branch. Because $`S`$ is small early, the clock accrues slowly per unit phase, so the early universe spans a long stretch of phase for little clock time, and the present age is read only after the clock map is calibrated.

The exponent $`-1/2`$ is the one that makes the phase clock reproduce the matter scaling the distance ladder requires. Matter dilution contributes the three-dimensional factor $`S^{-3}`$, while the Friedmann relation reads the square root of the rate, leaving the clock with the $`S^{-1/2}`$ power. Integer-power alternatives miss the Pantheon+ and DESI DR2 BAO distances by wide margins, and a purely boundary-geometric derivation of the same exponent remains open.

The observed distances need the topological $`\Lambda`$, not the wave budget alone: the budget by itself matches a matter-only history, and $`\Lambda`$, fixed through the surface eigenvalue, carries the rest. Read through the $`\Lambda`$CDM expansion frame that difference is the familiar shift from $`q_0 = +0.5`$ to $`q_0 = -0.55`$, a translation of the static domain's distance relation rather than a motion of the domain itself.

[![Time](https://img.youtube.com/vi/9N6g-kDgUDc/mqdefault.jpg)](https://www.youtube.com/watch?v=9N6g-kDgUDc)

### The Present Epoch

Two phase parameterizations meet at the present epoch. The engine phase $`\Phi = 4\pi\, T/T_\text{cycle}`$ is linear in the Hubble-clock age $`T`$, with $`\Phi_\text{now}`$ under re-derivation (the $`\approx 5.22`$ rad reading folds in a borrowed reference age and moves once inverted on the Hubble clock); the budget phase $`t`$, the argument of $`\Psi = \cos(t/2)`$, is nonlinear in it through that same clock, and distance data pin $`s_0 = \sin(t_\text{now}/2) < 0.19`$ (95% CL). The mapping $`t(\Phi)`$ between them is still open, though both give the same distance-redshift relation, and the $`4\pi`$ period and 120-step chronon are topology-native, independent of the choice.

[↑ Contents](#contents)

<a id="one-equation"></a>

## :balance_scale: One Equation

```math
\Large {\frac{A}{A_P} \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}}
```

Every constant in the universe is one quantity, asked at one place. The scaling law reads: **how big is this thing compared to the natural Planck unit for its kind;** $`A/A_P`$, equals **where it sits on the wave;** $`C(\Theta)`$, times **how far the geometry has diluted it from the Planck scale;** $`(\sqrt{\Omega})^{-n}`$.

### What the ratio means

$`A_P`$ is the Planck reference: the natural scale for that *kind* of quantity, built from nothing but $`G`$, $`\hbar`$, and $`c`$.

| Planck unit | Value | What it sets |
|---|---|---|
| $`\ell_P \approx 1.6 \times 10^{-35}`$ m | length | smallest meaningful distance |
| $`t_P \approx 5.4 \times 10^{-44}`$ s | time | smallest meaningful duration |
| $`m_P \approx 2.2 \times 10^{-8}`$ kg | mass | where gravity and quantum mechanics meet |

So $`A/A_P`$ just asks how big the measured thing is in those units. For the Hubble rate the reference is $`t_P^{-1}`$, and $`H_0 / t_P^{-1} \approx 10^{-61}`$: the Hubble rate is about $`10^{61}`$ times slower than the Planck rate. For the cosmological constant the reference is $`\ell_P^{-2}`$ (a curvature), and $`\Lambda / \ell_P^{-2} \approx 10^{-122}`$: the vacuum curves space, and stores energy, about $`10^{122}`$ times more weakly than the Planck scale would suggest.

**The classical mystery is why these ratios are so absurdly small.** MIT answers it structurally: the smallness is the dilution factor $`(\sqrt{\Omega})^{-n}`$, the price of living on the edge ($`n = 1`$) or the surface ($`n = 2`$) of the geometry instead of at the Planck floor. That factor sets the orders of magnitude; the position factor $`C(\Theta)`$ sets the leading digits. The rest of this section is just those two questions: where on the wave, and how deep in the geometry. The form is dimensional before it is numerical: dimensions multiply, so hierarchy depth appears as a power, and $`R_\Lambda/\ell_P`$ is the only available length ratio. The exponent records which geometric layer the observable lives on.

**The sample occurs at** $`(t, \Theta)`$: a moment in the wave's phase, at a position on the grid.

### The Phase Operator

$`C(\Theta)`$ is set by the topology in two steps. The anti-periodic boundary condition (the Möbius sign flip) forces the sinusoidal family: the eigenbasis is the half-integer tower, with no polynomial, exponential, or rational profile surviving (the [uniqueness argument](files/working/files/scaling-law-uniqueness.md) carries the detail). Background symmetry then selects the member: isotropy and orthogonality pick the lowest harmonic, the first-positive mode, and the boundary node picks sine over cosine, giving $`\psi_1(\Theta) = \sin(\pi\Theta)`$, zero at the two boundaries and peaking at the antinode. An observer registers intensity, the squared amplitude, so the weight is $`\lvert\psi_1\rvert^2 = \sin^2(\pi\Theta)`$, normalized to unit mean over the domain:

```math
\Large C(\Theta) = 2\sin^2(\pi\Theta)
```

The temporal anti-periodic tower and this positional profile are distinct eigenproblems sharing the sinusoidal form: the tower lives on the lifted phase lap of the temporal edge, while $`C(\Theta)`$ here is the first-positive intensity read across the sampling interval. One operator, read at every position: zero at the boundaries, maximal ($`C = 2`$) at the antinode, the same across all sectors (cosmology reads it at a single well, the mass sector across Kostant-exponent sets). The two factors of the scaling law then carry different, honest jobs. For the dimensional constants the powers of ten are units, $`R_\Lambda/\ell_P`$ raised to the observable's dimension, and the dimensionless physics is the value of $`C(\Theta)`$. For the dimensionless couplings the same hierarchy enters as a fractional power that is itself the content: $`\alpha`$ is one grid step of it.

| Position | $`C(\Theta)`$ | Slope $`d\ln C/d\Theta`$ | Significance |
|---|---|---|---|
| $`\Theta = 0`$ (boundary) | 0 | $`\to \infty`$ | No observable amplitude |
| $`\Theta = 1/2`$ (antinode) | 2 | 0 | Maximum amplitude; stationary to first order |
| $`\Theta = 1`$ (boundary) | 0 | $`\to -\infty`$ | No observable amplitude |

$`\Lambda_\text{top}`$ sits at the antinode: slope exactly zero.

The boundary zeros are physical: the framework reads a black-hole horizon as this $`C \to 0`$ wall, where sampling fails entirely (the [black-hole supplement](../cosmos/files/black-hole.md)).

### The Hierarchy and the Observer

$`\Omega_\Lambda`$ is fixed by $`\Lambda`$ and epoch-independent. The phase-gradient scale changes with epoch:

```math
\Omega_H(z) \equiv \left(\frac{\ell_\text{phase}(z)}{\ell_P}\right)^2, \quad \ell_\text{phase} = c/\lvert d\ln\Psi/d\tau\rvert
```

At the present epoch $`\Omega_H`$ and $`\Omega_\Lambda`$ are numerically close, both of order $`10^{122}`$. In the current calibration structure this coincidence is observed, not derived: $`\Omega_H`$ is anchored by the measured Hubble rate, $`\Omega_\Lambda`$ by measured $`\Lambda`$.

The domain runs from the Planck floor ($`\Omega = 1`$) up to the cosmic ceiling ($`\Omega \approx 10^{122}`$). Ask where the observer sits, and the geometry answers with its own midpoint: the self-dual point $`x = \Omega/x`$, where the climb to the ceiling equals the drop to the floor.

```math
\Large x = \sqrt{\Omega} \approx 10^{61}
```

That is us, the self-dual center: in $`\Omega`$ the observer sits at $`\sqrt{\Omega} = 10^{61}`$, 61 orders from the floor and 61 from the ceiling. This is where observation resolves.

In physical units the same center is a length, the geometric mean of the Planck length and the curvature radius:

```math
\sqrt{\ell_P \, R_\Lambda} \approx 50\ \mu\text{m}.
```

Because $`\Omega = (R_\Lambda/\ell_P)^2`$, distances in length are half those in $`\Omega`$: 50 μm sits about 30 orders of magnitude above the Planck length and 30 below the curvature radius. The geometric mean of any theory's smallest and largest length is bound to land somewhere macroscopic; the content here is the specific value, the scale of a living cell. Why observers should sit at the center rather than anywhere else is an open question, not something the framework derives. But the midpoint is the midpoint, and the cell is where it lands.

### Manifold Index

Mode intensity dilutes as $`(\sqrt{\Omega})^{-n}`$. The manifold index $`n`$ specifies which scale governs the mode being sampled.

| $`n`$ | Manifold | $`\Omega`$ | $`(\sqrt{\Omega})^{-n}`$ | Observables |
|---|---|---|---|---|
| 0 | Planck floor | 1 | 1 | $`G`$ |
| 1 | Temporal edge $`S^1`$ | $`\Omega_H`$ | $`10^{-61}`$ | $`H_0`$, $`a_0`$ |
| 3/2 | Gauss lift + de Sitter | — | — | $`\Lambda_\text{obs}/\Lambda_\text{top} = 3/2`$ (3 the Gauss/Ricci lift, 1/2 the de Sitter vacuum; the vacuum seam, see One Interface) |
| 2 | Möbius surface | $`\Omega_\Lambda`$ | $`10^{-122}`$ | $`\Lambda`$ |
| 3 | Space $`S^3`$ | $`\Omega_\Lambda`$ | $`10^{-183}`$ | Null dark matter detection |

**The scale selection rule.** The index $`n`$ is read from where the quantity lives and whether it evolves with epoch: edge rates take $`n = 1`$ on the evolving $`\Omega_H`$, surface and space quantities take $`n = 2`$ and $`n = 3`$ on the fixed $`\Omega_\Lambda`$, and dimensionless couplings bypass manifold dilution at fractional $`n`$.

The index $`n`$ has two compatible readings in the dilution sector: the length-dimension of the observable, and the geometric layer on which the mode lives. They agree for the edge, surface, and space rows. The exceptions are explicit: $`G`$ is the Planck anchor, the $`3/2`$ row is a vacuum-reference conversion (3 Gauss/Ricci, 1/2 de Sitter) rather than dilution, and the dimensionless couplings use fractional grid exponents.

### Fibonacci Wells

The first-positive wave shape is selected, but not every position on it is a stable place to sample. The stable candidates continue a sequence the domain already carries. The icosahedron's branch orders $`(2,3,5)`$ are consecutive Fibonacci numbers obeying $`2+3=5`$, and the same recurrence, run forward on the fixed 120-grid, gives the well sequence. The sequence does double duty: its early terms build the domain, its later terms sample it. The terms that build it are exactly the Fibonacci divisors of 120, namely $`\{1,2,3,5,8\}`$, whose least common multiple is 120; these tile the grid rather than mark new sampling positions. The first Fibonacci term that is not a divisor is $`F_7 = 13`$, the seam between the Fibonacci structure that makes the domain and the Fibonacci structure that lives on it. The upper end is the wave's own reflection symmetry, $`C(\Theta) = C(1 - \Theta)`$, about the antinode, so no new intensity well appears beyond $`\Theta = 1/2`$. The wells therefore fall between the seam and the antinode at $`13, 21, 34, 55`$, with spacings $`8, 13, 21`$, again consecutive Fibonacci. The golden ratio behind this recurrence is not imported from outside; it is already present in the binary icosahedral character field $`\mathbb{Q}(\sqrt5)`$, the same $`\sqrt5`$ that fixes the exact torsion ratio $`\varphi^{-4}`$ between the Galois-paired generations.

Three constraints force the observable assignments. First, the manifold index separates edge modes ($`n = 1`$, epoch-dependent: $`H_0`$, $`a_0`$) from surface modes ($`n = 2`$, epoch-independent: $`\Lambda`$). Second, the bosonic projection: photon-mediated observables access only the 60R(realized)-grid (even numerators survive $`2I \to I`$); dynamical observables access the full 120. Third, $`\Lambda`$ sits at the antinode (60/120) by eigenvalue identity. Together these place $`\alpha`$ on the 60R-grid image of 13 (photon-mediated), $`a_0`$ on its full-120 image (coprime, dynamical), $`H_0`$ on the next even-numerator edge well at 34, and $`\Lambda`$ at the antinode 60; 21 and 55 are wells too but carry no observable, so the wells come first and the four land on them. 

The recurrence is stable in the golden-ratio sense: its ratios converge to the hardest number to approximate by rationals, so its spacing is the natural candidate for least-resonant boundary sampling. In this formulation the golden ratio is internal to the $`2I`$ character field rather than imposed as an external Diophantine postulate. What remains open is now sharper and dynamical: why the anti-periodic boundary sampling follows this recurrence, an interference principle that the [mirror](../spectrum/files/the-mirror.md) locates on the edge but does not yet derive.

### The Assembled Engine

Evaluating the scaling law at each well:

| Observable | $`F_n`$ | Grid | $`\Theta`$ | $`C`$ | $`n`$ | $`A_P`$ | $`A/A_P`$ | Role |
|---|---|---|---|---|---|---|---|---|
| [α](../spectrum/files/fine-structure.md) | $`F_7`$ | 60R | 13/60 | 0.792 | 1/30 | 1 | $`7.33 \times 10^{-3}`$ | Prediction |
| [a₀](../cosmos/files/early-galaxies.md) | $`F_7`$ | 120 | 13/120 | 0.223 | 1 | $`a_P`$ | $`2.2 \times 10^{-62}`$ | Prediction |
| — | $`F_8`$ | 120 | 21/120 | 0.55 | — | — | — | unassigned |
| [H₀](../cosmos/files/hubble-tension.md) | $`F_9`$ | 120 | 34/120 | 1.208 | 1 | $`t_P^{-1}`$ | $`1.2 \times 10^{-61}`$ | Calibration |
| — | $`F_{10}`$ | 120 | 55/120 | 1.97 | — | — | — | unassigned |
| [Λ](../cosmos/files/cosmological-constant.md) | — | 120 | 60/120 | 2.00 | 2 | $`\ell_P^{-2}`$ | $`2.9 \times 10^{-122}`$ * | Surface calibration / geometric relation |

> * The surface eigenvalue $`\Lambda_\text{top} = 2/R_\Lambda^2`$ is computed directly on the curved totally geodesic metric $`ds^2 = dy^2 + \cos^2(y/R_\Lambda)\,dw^2`$ and confirmed from below by the Bochner identity; equality is unique. The Gauss equation conversion $`\Lambda_\text{obs} = (3/2)\,\Lambda_\text{top} = 3/R_\Lambda^2`$ follows under three conditions: totally geodesic embedding of the underlying great-$`S^2`$ band ($`K_{ij} = 0`$), isotropy (CMB-verified to $`10^{-5}`$), and de Sitter vacuum (late-time ΛCDM attractor).
>
> The numerical $`\Lambda`$ is therefore a surface-sector calibration rather than an independent prediction. The [first-eigenvalue paper](files/bedrock/files/first-eigenvalue.md) establishes the geometric side: the twisted Laplacian on the constant-curvature Möbius band has first positive eigenvalue $`2/R_\Lambda^2`$, stable across the cone's self-adjoint extensions even though none has a positive ground state. The framework reads that eigenvalue as $`\Lambda_\text{top}`$, the physics worked through on the [cosmological constant](../cosmos/files/cosmological-constant.md) page.

**Calibration structure.** $`H_0`$ is the measured edge anchor: it defines the edge normalization $`N = H_0 t_P / C(34/120)`$, so the $`H_0`$ row fixes the ruler rather than testing the law against it, and substituting $`\Omega_H = (H_0 t_P)^{-2}`$ back into that row returns the calibration identity, not a prediction. The other edge observables follow from $`N`$; the falsifiable content is any ratio of two edge-mode $`C`$ factors, in which $`N`$ cancels, the sharpest being $`a_0/(cH_0) = C(13/120)/C(34/120)`$. The $`\approx`$ in the scaling law marks this single calibration.

$`\alpha`$ and $`a_0`$ share the Fibonacci index 13 but live on different grids ($`\alpha`$ at 13/60, $`a_0`$ at 13/120), reference different scales ($`\Omega_\Lambda`$ vs $`\Omega_H`$), and carry different exponents (1/30 vs 1). The shared index reflects Fibonacci stability operating at the topological level for both. Each prediction is independent.

The $`a_0/(cH_0)`$ ratio is locked by well positions: $`C(13/120)/C(34/120) = 0.184`$. Because both are edge modes sharing the same calibrated normalization $`N`$, the ratio holds at every epoch: $`a_0(z) \propto H(z)`$.

### The Phase Field

The phase position decomposes as $`\Theta = \Theta_0 + \Theta_f`$, where $`\Theta_0`$ is the Fibonacci well (fixed) and $`\Theta_f`$ is the local environmental shift.

| Well | Θ | Slope | Finite change at $`+2/120`$ | Character |
|---|---|---|---|---|
| $`a_0`$ | 13/120 | 17.74 | $`+31.4\%`$ | steepest of the three |
| $`H_0`$ | 34/120 | 5.09 | $`+8.4\%`$ | measured through the field |
| $`\Lambda_\text{top}`$ | 60/120 | 0 | $`-0.27\%`$ | stationary to first order |

The slope at each well determines its character. $`\Lambda`$ sits at the antinode where the derivative vanishes, so it is stationary to first order in $`\Theta`$, but it is not invariant under a finite step: $`C(62/120)/C(60/120) = \cos^2(\pi/60) = 0.99726`$, a change of $`-0.27\%`$. $`H_0`$ at slope 5.09 takes the same step as an 8.4% shift, $`C(36/120)/C(34/120) = 1.0837`$, giving $`67.4 \times 1.0837 = 73.04`$ km/s/Mpc. The differential between the two wells is a factor of about thirty, and that differential rather than any protection is what lets the framework move $`H_0`$ while holding $`\Lambda`$ nearly fixed. The ratio is fixed by well positions and independent of any galactic mechanism, but it is fixed only once the phase operator, the well assignment, the sublattice assignment, and the displacement orientation are stipulated, all four of which are imported. The trigger that would have realized the shift is withdrawn (the SPARC test, detailed on the [Hubble tension](../cosmos/files/hubble-tension.md) page), so the 8.4% is a correspondence without an active mechanism.

$`a_0`$ at slope 17.74 marks a steep, sensitive well, but the phase field does not shift it. The acceleration scale where MOND behavior turns on is the well position $`C(13/120) \cdot (\sqrt{\Omega_H})^{-1} \cdot a_P`$. The derivative alone says nothing about the character of the MOND transition: a large derivative produces a sensitive continuous response, not a threshold, and the binary mechanism that would have discretized it is the one the SPARC test falsified.

### The Gauge Ladder

Everything in this sector lives at two phase slots, the Fibonacci well 13 and its $`E_8`$ Coxeter conjugate 17, the residue $`30 - 13`$ rather than a Fibonacci well of its own. The Coxeter pair $`(13, 17)`$ sums to the Coxeter number of $`E_8`$: $`13 + 17 = 30 = h(E_8)`$. That is not a coincidence. The McKay correspondence ties $`2I`$ directly to $`E_8`$, so the domain's natural arithmetic runs modulo 30, and 13 and 17 are the conjugate exponents that pair across it.

**What lives at each well:**

| Well | Grid | Observable | What it represents |
|---|---|---|---|
| 13/60 | 60R | $`\alpha`$ | electromagnetic coupling; photon-mediated, bosonic |
| 13/120 | 120 | $`a_0`$ | matter acceleration scale; dynamical, full domain |
| 17/60 | 60R | strong coupling | bosonic carrier, confined fermions |
| 17/120 | 120 | weak coupling | fermion-changing carrier, flavor transitions |

**13 is where matter and electromagnetism anchor.** The fine-structure constant and the MOND acceleration scale both sit at index 13, on different grids: the 60R-grid version is what the photon sees, the 120-grid version is what matter dynamics sees.

**17 is where the short-range forces anchor.** Strong and weak both take 17 as their phase slot; the grid difference between them, identity-preserving versus fermion-changing action, is what separates confinement from flavor-changing transitions. Here the 120 grid labels the action on the full orientation-sensitive fermion domain, not the spin of the mediator: the $`W`$ and $`Z`$ remain spin-1 bosons, their 120 assignment coming from that action, a motivated selection rule rather than a derived one.

**Why the split is real.** The 60R-grid is what survives the bosonic projection $`2I \to I`$, so it is what freely-propagating, photon-mediated quantities see. Fermions need the full 120-grid because they couple to the orientation structure of the Möbius strip directly. So 13 connects to what propagates freely through the domain, and 17 to what binds or transforms within it.

The couplings then follow one assignment rule: the phase slot inherits the grid of the carrier, the exponent slot the grid of the confinement target.

| Force | Phase grid | Exponent grid | Formula | Predicted | Observed | Agreement |
|---|---|---|---|---|---|---|
| EM ($`\alpha`$) | 60R (bosonic carrier) | 60R (bosonic current) | $`C(13/60) \cdot \Omega_\Lambda^{-1/60}`$ | 0.00733 | 0.00730 | 0.4% |
| Strong ($`\alpha_s`$) | 60R (bosonic carrier) | 120 (confined fermions) | $`C(17/60) \cdot \Omega_\Lambda^{-1/120}`$ | 0.1162 | 0.1180 | 1.5% |
| Weak ($`\alpha_W`$) | 120 (fermion-changing action) | 120 (fermion transitions) | $`C(17/120) \cdot \Omega_\Lambda^{-1/120} \cdot \cos(\pi/10)`$ | 0.0339 | 0.0338 | 0.3% |
| SUSY rung (vacant) | 120 (fermionic carrier) | 60R (bosonic target) | none: would change fermion/boson class | — | no superpartners | vacant (ladder rule) |

**Scale caveat.** The displayed values compare $`\alpha`$ at low energy with $`\alpha_s`$ and $`\alpha_W`$ in their conventional $`Z`$-mass normalizations. The grid returns base assignments; reconciling the reference scales, or deriving the running from the topology, remains open.

**Reading note.** These percent-level agreements are predictions *from the $`\Lambda`$ reading*: with $`\Omega_\Lambda`$ fixed by a surface anchor, the scaling law returns the couplings. When a coupling is instead the anchor that fixes $`\Omega_\Lambda`$ (the best-conditioned route, since $`\alpha`$ is the most precisely measured input), its own 0.4% becomes a consistency check rather than an independent prediction, and the genuine output of that route is $`\Lambda`$ to 23% ($`\alpha \to \Omega_\Lambda \to \Lambda = 3/R_\Lambda^2`$). The three interchangeable anchors are laid out under [Three readings of one hierarchy](#three-readings-of-one-hierarchy).

The Coxeter pair $`(13, 17)`$ under $`h(E_8) = 30`$ is forced: all alternative conjugate pairs fail by 93% to 770%. The three forces exhaust the grid ladder, monotone in spinorial content. There are only four ways to pair a carrier grid with a target grid, and the table shows three of them filled.

**The fourth rung is supersymmetry's, and it is empty.** The one missing pairing would turn a fermion into a boson, exactly the move a superpartner symmetry asks for. Every real gauge rung acts within a statistics class: EM, strong, and weak change phase, charge, or representation but leave the fermion or boson character of what they act on intact. A superpartner rung would instead identify the fermionic 120-grid (the section $`\psi`$) with the bosonic 60R-grid (the intensity $`\lvert\psi\rvert^2`$), the split that the central element $`-I`$ and the Möbius sign flip carry, and no gauge rung crosses it. The obstruction is the ladder's own rule, not a spin-statistics prohibition (ordinary quantum field theory permits fermionic mediators between fermions and bosons), not an attempted inverse of $`\psi \to \lvert\psi\rvert^2`$: that projection is well-defined but non-invertible, which is the measurement-level reason the two grids stay distinct. So the missing superpartner force is not an unreached energy scale but the closed fourth chair at a table set for exactly four.

[↑ Contents](#contents)

<a id="one-formula"></a>

## :atom_symbol: One Formula

The mass spectrum assembles in three moves, each set by the same topology: the curvature gap that confines, the three flat vacua that become the generations, and the four-factor formula that ranks the fermion masses.

### Confinement

Confinement is usually told as a story about energy: pull two quarks apart and the cost keeps rising until the field snaps. On $`S^3`$ it is a story about curvature instead. Positive Ricci curvature forces a positive gap on the coexact gauge fluctuations around a flat connection; the twisted harmonic 1-forms vanish ($`H^1 = 0`$), so every mode is lifted off zero. The exact value is the coexact form spectrum read through the McKay distance: the adjoint-valued gap is $`4/R_\Lambda^2`$ at the trivial and standard vacua, with the Galois vacuum the one exception (below). The gap is geometric, the bottom eigenvalue of the linearized coexact $`1`$-form operator on the compact space, fixed by curvature rather than tuned into the dynamics. It is a spectral gap on that compact curved background, not the physical flat-space confinement scale $`\Lambda_{\text{QCD}}`$, which stays a separate, open problem. The fermion mass ladder is a distinct McKay-structured object, neither setting this gauge gap nor set by it.

### Three Generations

Why three generations, and not two or seven? Because the space has exactly three ways to hold a flat field still, with no path leading from one to another. Flat SU(2) connections on $`S^3/2I`$ are classified by conjugacy classes of homomorphisms from $`2I`$ into SU(2), and exactly three exist. Each is isolated ($`H^1 = 0`$): no continuous moduli, no Goldstone bridges between families.

| Vacuum | Mass gap | Source |
|---|---|---|
| Trivial | $`4/R_\Lambda^2`$ | Flat connection |
| Standard | $`4/R_\Lambda^2`$ | Irreducible connection |
| Galois | $`36/R_\Lambda^2`$ ($`9\times`$) | Galois conjugate connection |

Three topological vacua give three particle generations; the count is forced. Trivial and Standard are degenerate in gap, while Galois is distinguished by the 9× enhancement: the gap is the square of the adjoint's McKay distance, and the Galois adjoint sits at distance 6 against the standard adjoint's 2, so $`36/4 = (6/2)^2 = 9`$. The Galois vacuum is a genuine third connection, not a twist of the standard one, because $`2I`$ is perfect (equal to its own commutator subgroup): its only one-dimensional character is trivial, so the standard connection $`Q`$ and its Galois conjugate $`Q^\prime`$ stay distinct under every twist. The specific generation-to-vacuum mapping is open.

The [coexact gap paper](files/bedrock/files/coexact-gap.md) establishes the spectral side: across the entire ADE classification of finite subgroups of SU(2) the adjoint coexact gap is uniformly $`4/R_\Lambda^2`$, with a single break, the Galois connection on $`S^3/2I`$ at $`36/R_\Lambda^2`$, and that break is forced by perfectness, the property that distinguishes $`2I`$ alone among the finite subgroups of SU(2). The framework reads this exception as selection evidence, converging with the input-minimization argument that independently terminates on $`2I`$, so $`S^3/2I`$ is taken as the physical quotient on two grounds rather than one. The [galois-pair paper](files/bedrock/files/galois-pair.md) ("The Filling") adds the boundary side: the adjoint $`\rho`$-invariant asymmetry between the standard and Galois connections, supported on the Galois-sensitive conjugacy classes and carried through the tautological bundles on the $`E_8`$ ALE filling of $`S^3/2I`$. It establishes that filling structure; it does not identify the gauge decoration with the standing-wave sector, so the Möbius-to-ALE bridge stays open.

### The Mass Formula

The formula reads left to right as one motion: start at the floor, choose a seat, ride the elevator, then turn the dial. Four factors, each traced independently to the postulate, each doing exactly one thing:

```math
\Large m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)
```

**The Neutrino Floor.** $`\mu_\Lambda = \rho_\Lambda^{1/4} \approx 2.25`$ meV sets the overall scale. It is not the smallest fermion mass but the floor beneath all of them: the lowest energy the geometry can resolve, the fourth root of the vacuum energy density $`\rho_\Lambda`$, the first positive mode of the Möbius surface. Every mass in the spectrum is built up from this one hum.

**The Kostant Sunflower.** $`C_\text{geom}(\rho)`$ chooses the seat. It is the same phase weight $`C(\Theta)`$ from the One Equation, read now as the geometric mean of $`C(e/D)`$ over the Kostant exponents of the irrep $`\rho`$: which well on the domain the particle occupies.

**The McKay Elevator.** $`(\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30}`$ raises the seat through orders of magnitude. Each step out along the McKay graph multiplies the mass by a fixed factor, and the denominator is the Coxeter number $`h(E_8) = 30`$: the same exceptional geometry that selected $`2I`$ sets the height of one floor.

**The Reidemeister Torsion.** $`T^2(\rho \otimes \sigma)`$ is the fine dial within a shell, the one factor that changes across the three vacua. It is the torsion of the flat connection, and its exact structure is fixed by the geometry alone: every irrep carries a closed form in $`\mathbb{Q}(\varphi)`$, the Galois-paired generations satisfy $`T^2(R_3)/T^2(R_4) = \varphi^{-4}`$ and $`T^2(R_1)/T^2(R_2) = \varphi^{-8}`$, and the two spin-parity sector products, $`4`$ and $`1/4`$, are exact inverses. The eight nontrivial values are computed here analytically, from the spectral zeta functions, and have since been reproduced by an independent method that never sees the spectrum at all: a combinatorial torsion built from a based chain complex of the space form, carried out in a context isolated from this artifact and its numbers, agreeing exactly in $`\mathbb{Q}(\varphi)`$ once the one convention the two routes can differ on, the direction of the torsion, is fixed at a single reference value. That the analytic and combinatorial routes meet at the same algebraic numbers is what makes the dial a topological invariant of the vacuum rather than a feature of how it was computed ([the adjudication record](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_8_adjudication_record.md)).

**What the formula delivers, and what it does not.** Applied to the 8 nontrivial irreps across 3 vacua, the formula produces 24 entries across the fermion band. Lined up against the measured fermions, and treating $`m_e`$ as the benchmark rather than a counted hit, five of the remaining eight charged fermions land within a factor of 3 of a quantum-number-compatible entry, four of them surviving sector-first adjudication; the down quark is assigned but lies outside the factor-of-3 window, the up quark and charm are unassigned, the bottom quark's nearest compatible entry falls outside its own structural sector and stays uncounted, and the muon and strange share a single entry at rank 15. That is a comparison, not a prediction, and it is softer than the old "9 of 10" headline, which added the three unmeasured neutrinos and reused entries more freely. It is also helped by density: wherever the charged entries cluster, the factor-of-3 window is wider than the gaps between them, so a measured mass sits near some entry largely by counting.

Whether the specific torsion values add fit beyond that quantum-number-constrained density was the open question, and a pre-registered null test (`mass-null-v1.1`) has settled it. Randomly reassigning the torsions across the fixed slots reproduced or exceeded the observed coverage in 69% of draws ($`p_A = 0.690`$), the null distribution now centered on the observed count: the factor-of-3 count is uninformative about whether the specific torsion values occupy the correct slots. The mass table's evidential weight rests on the exact structural outputs, the 24-entry construction, the $`T_3`$ gate evaluations, and the closed-form torsion algebra, together with the falsifiable outliers, not on the factor-of-3 count; the test does not independently validate those structural outputs, it removes the proximity scorecard as evidence for the torsion dial. The entry-to-fermion assignment is read against the measured masses, not fixed before them; what the topology fixes without the data is the count and the quantum-number content of each entry.

The Yang-Mills gap above (geometry, $`\sim 1/R_\Lambda^2`$ from the form spectrum) and this mass ladder ($`(\sqrt{\Omega_\Lambda})^{\,\text{dist}/30}`$) share the McKay structure but are different objects: the gap is proved, the ladder is the comparison, and the one does not lend its standing to the other.

[↑ Contents](#contents)

<a id="one-identity"></a>

## :small_red_triangle: One Identity

```math
\Large {\lvert 2I\rvert = 120 = 2^3 \cdot 3 \cdot 5}
```

The binary icosahedral group is the largest exceptional discrete subgroup of SU(2), and its order factors into exactly three primes: $`120 = 2^3 \cdot 3 \cdot 5`$. The factorization is not bookkeeping. The primes 3 and 5 are the orders of the face and vertex stabilizers of the icosahedron, and the factor of 2 is carried by the central element $`-I`$ of order 2 that the edge stabilizer contains. Each sorts one piece of physical identity: restrict an irrep to it and the topology says what the particle is.

**Faces sort color.** The three-fold face stabilizer $`Z_3`$ splits every irrep into a singlet or a triplet: leptons and quarks, the three color charges of QCD. It is the decomposition $`Z_3`$ uniquely produces, and the face geometry is identical from all three vacua, so color is generation-independent.

**Edges sort spin.** The four-fold edge stabilizer $`Z_4`$ contains the central element $`-I`$, which acts as $`+1`$ on integer-spin irreps and $`-1`$ on half-integer ones, cleanly separating the $`D = 60`$ bosons from the $`D = 120`$ fermions. Spin-statistics is the edge doing its one job.

**Vertices set the electroweak address.** The five-fold vertex stabilizer $`Z_5`$ is the only stabilizer that tells the Galois-conjugate pair $`R_1`$, $`R_2`$ apart, so it is what carries weak isospin across the electroweak interface.

Two further entries are not primes but corrections derived from the same stabilizers, each tying back to a section of its own:

| Combination | Value | Role | Mechanism |
|---|---|---|---|
| Face / Edge | 3/2 | Gravity: 3/2 vacuum-reference conversion (3 Gauss/Ricci, 1/2 de Sitter) | Surface eigenvalue carried to a space observable |
| Vertex $`\times`$ twist | $`\cos(\pi/10)`$ | Weak coupling correction | Dodecahedral defect $`\pi/5`$, halved by the Möbius $`Z_2`$ |

The 3/2 gravity entry is the conjectural one: its derived content is the Gauss conversion (3 = isotropic Ricci trace, 2 = de Sitter normalization; see [cosmological constant](../cosmos/files/cosmological-constant.md)), and reading the same 3/2 as a face-to-edge stabilizer ratio is a suggested correspondence, not a derived identity.

The stabilizer structure says what each entry is; the formula says where each entry sits; both come from the topology. The comparison is the last step: which entry lands on which measured fermion, read against the data rather than fixed ahead of it.

[↑ Contents](#contents)

<a id="one-interface"></a>

## 🪡 One Interface

All of it, the wells, the spectrum, the stabilizer sorting, lives on a smooth space that knows none of it. The last question is how that discrete structure sits on the $`S^3`$ underneath, and what gravity is across the seam. The answer is not one operation but two.

Underneath everything is $`S^3`$: smooth, continuous, every point equivalent, with uniform Ricci curvature. $`S^3`$ knows nothing about 120. The discrete structure is built on top of it, and it is built in two distinct ways.

### The two seams

| Seam | Operation | Produces | Carries |
|---|---|---|---|
| Möbius $`\hookrightarrow S^3`$ | totally geodesic great-$`S^2`$ band (Möbius as its quotient) | the vacuum, $`\Lambda`$ | the 3/2 vacuum-reference factor (3 Gauss/Ricci, 1/2 de Sitter) |
| $`S^3 \to S^3/2I`$ | quotient (point identification) | the 120-domain: wells, gauge ladder, mass gap | the grid |

These are different operations doing different jobs. Embedding a 2-surface in the 3-space converts surface curvature into spatial curvature and fixes the vacuum; the quotient identifies points and produces the discrete grid. The [Waltz](../spectrum/files/the-waltz.md) reading draws the same line: the Möbius surface sets $`\Lambda`$, the binary icosahedral group sets matter. The wells and the three gauge forces come from the quotient, not the embedding.

The 3/2 belongs to the vacuum seam. It is the cost of converting the Möbius surface's curvature into the spatial curvature of $`S^3`$: the numerator 3 is the Gauss factor, derived geometry from the totally geodesic great-$`S^2`$ band the surface is built on, in an isotropic $`S^3`$, with the Möbius entering as the edge-identified quotient of that band rather than a smooth totally geodesic submanifold; the denominator 2 is the de Sitter normalization, imported from general relativity. The [cosmological constant](../cosmos/files/cosmological-constant.md) page keeps that derived-vs-imported split explicit. The grid carries no such factor; it is the separate $`2I`$ structure.

### Gravity is what crosses

The gauge ladder closes the possible couplings inside the grid. Gravity is different in kind. It is not a vacant grid position, and it is not a fourth gauge force waiting for its rung.

Gravity couples to stress-energy on either layer, so it is the one interaction that translates between the smooth substrate and every discrete structuring of it, the Möbius vacuum and the $`2I`$ grid alike. In MIT's reading, that translation is what gravity is: not a graviton on the grid, but the conversion across the interface, with the Gauss factor as the cost it pays on the vacuum seam.

On the grid seam it pays nothing special, only the ordinary stress-energy coupling at $`8\pi G`$. Einstein's field equations are unchanged. What the framework adds is why gravity sits outside the gauge ladder, and why its signature is a geometric conversion rather than a coupling on the grid.

It also reframes why gravity resists quantization. In this reading, gravity is not one more object inside a single sector; it is the interface between two different kinds of structure, continuous geometry and discrete sampling. Quantizing it in the usual way would mean pushing one side into the form of the other: discretizing $`S^3`$, which removes the smooth source of $`\Lambda`$, or continualizing the 120-domain, which dissolves the spectrum, the mass gap, and the three generations. The resistance is therefore not just a missing technique; it is the signature of an interface no single-sector quantization can cross.

[↑ Contents](#contents)

---

<a id="inputs-and-calibration"></a>

## :control_knobs: Inputs and Calibration

The scaling law is one equation with one hierarchy variable, $`\Omega_\Lambda`$. Every observable on the law is a different reading of that one variable. Invert any single observable and you fix $`\Omega_\Lambda`$, which then predicts all the others. Which observable you invert is calibration. The relationships between them are physics.

### The Ω ledger

The symbol $`\Omega`$ is a hierarchy ledger, not always an independent prediction: its status depends on the sector row.

| Sector | Hierarchy | How $`\Omega`$ is fixed | What is tested |
|---|---|---|---|
| Edge | $`\Omega_H = (c/H_0\ell_P)^2 = (H_0 t_P)^{-2}`$ | read from measured $`H_0`$ | the well ratio $`a_0/(cH_0) = C(13/120)/C(34/120)`$ |
| Surface, space | $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2`$ | one surface anchor: measured $`\Lambda`$, or read from $`\alpha`$ or the mass spectrum | cross-read consistency, and the downstream mass and coupling structure |
| Couplings | powers $`\Omega_\Lambda^{-1/60}`$, $`\Omega_\Lambda^{-1/120}`$ | inherited from the surface hierarchy | grid relations and same-depth ratios |
| Masses | powers $`(\sqrt{\Omega_\Lambda})^{\text{dist}/30}`$ | inherited from the surface hierarchy, plus one mass-sector normalization where needed | McKay distances and ratios |

At an anchor row, substituting that row's own definition of $`\Omega`$ back into the scaling law returns the anchor identity: that is calibration, not prediction. The content is in reading the same $`\Omega`$ ledger at different wells, depths, and sectors. In the edge sector, $`\Omega_H = (H_0 t_P)^{-2}`$ is read from measured $`H_0`$, which fixes the edge reference at the $`34/120`$ row; the prediction is then the acceleration ratio $`a_0/(cH_0) = C(13/120)/C(34/120) = 0.184`$.

### Unit constants

| Constant | Value | Role |
|---|---|---|
| $`c`$ | 299,792,458 m/s | Propagation rate on the temporal boundary |
| $`\hbar`$ | $`1.055 \times 10^{-34}`$ J s | Converts dimensionless mode structure into physical action and energy |

Neither is predicted. They define the unit system, nothing more.

### The dimensionless core

In a ratio of two observables at the same depth, $`\Omega_\Lambda`$ cancels: no anchor enters and the number is parameter-free. Anchor-free predictions occur when the same hierarchy depth, grid, or calibrated edge normalization cancels; cross-depth or cross-grid comparisons are the levers that read the hierarchy. These hold under every choice of anchor below.

| Quantity | Value | Status |
|---|---|---|
| Force count | 3 | exact |
| Generation count | 3 | exact |
| $`T_3`$ gate evaluations | 11 featured (5 assigned + 2 neutrino-proxy + 4 structural) | exact (Coxeter-Galois gate) |
| Galois torsion ratios | $`\varphi^{-4}`$, $`\varphi^{-8}`$ | exact ($`T^2(R_3)/T^2(R_4)`$, $`T^2(R_1)/T^2(R_2)`$) |
| torsion sector products | $`4`$, $`1/4`$ | exact inverses |
| $`\alpha_s/\alpha_W`$ | 3.43 | prediction (1.8%), $`\Omega`$ cancels |
| $`a_0/(cH_0)`$ | 0.184 | prediction (<1%), normalization cancels |

### Three readings of one hierarchy

To attach a scale you invert one observable for $`\Omega_\Lambda`$. Three are independent, and the framework is over-determined: each fixes the same hierarchy, and they agree to within their amplified input residuals.

| Anchor | Determines | $`\Lambda`$ | $`\alpha`$ | Precision driver |
|---|---|---|---|---|
| Measured $`\Lambda`$ (sets $`R_\Lambda`$) | $`\Omega_\Lambda`$ from $`R_\Lambda`$ | circular | 0.4% | current default |
| Measured $`\alpha`$ | $`\Omega_\Lambda`$ from the coupling | 23% (genuine) | circular | best-conditioned |
| Mass spectrum ($`m_\mu/m_e`$) | $`\Omega_\Lambda`$ from the mass ratio | ~14x (genuine) | ~few % | independent cross-check |

The headline is the second row: from one measured coupling, with no $`R_\Lambda`$ and no further calibration, the scaling law fixes the cosmological constant to 23%. The 122 orders of magnitude are not predicted here; they enter through $`\Omega_\Lambda`$, read from $`\alpha`$. What this route adds is the residual coefficient, to 23%. QFT, which does try to predict the magnitude from first principles, overshoots by $`10^{120}`$.

All three are the same inversion through the same 60-fold McKay/grid lever ($`\Lambda\ell_P^2 \propto \alpha^{60}`$), so they differ only in input conditioning: $`\alpha`$ matches its formula to ~0.4% and lands $`\Lambda`$ at 23%, the mass ratio matches to ~4.5% and lands ~14× off; the gap is amplified input error, not a structural inconsistency.

The mass reading earns its independent-cross-check label structurally: a same-depth ratio cancels $`R_\Lambda`$, but the electron and muon sit at different McKay distances, so their mass ratio keeps a net power of $`\sqrt{\Omega_\Lambda}`$ through the elevator and reads the scale rather than dividing it out.

### Sector anchors

| Sector | Anchor | Role |
|---|---|---|
| Edge | measured $`H_0`$ | Fixes the present edge hierarchy $`\Omega_H = (c/H_0\ell_P)^2`$ |
| Surface / space | any one of $`\Lambda`$, $`\alpha`$, or the mass ratio | Fixes $`\Omega_\Lambda`$; the three readings agree to within their input residuals |
| Mass | normalization tied to $`m_e`$ | Fixes the absolute mass scale once ratios are known |
| Phase clock | $`s_0`$ from distance data | Locates the current observer phase |

Edge observables reference the evolving $`\Omega_H(z)`$; surface and space observables reference the fixed $`\Omega_\Lambda`$. The mass sector inherits $`\mu_\Lambda = \rho_\Lambda^{1/4}`$ from $`\Omega_\Lambda`$; $`m_e`$ is the benchmark, not a second floor. Compute $`m_e`$ from $`\Lambda`$ instead, carrying both the $`\mu_\Lambda`$ scale and the hierarchy feedback ($`m_e \propto \Lambda^{11/60}`$), and it lands within 2%; inverting, that 2% is ~11% in $`\Lambda`$. The closure is the loop, run from either end, the web holding whichever you pick.

### Predicted and calibrated

| Quantity | Status |
|---|---|
| dimensionless ratios (couplings, $`a_0/cH_0`$, counts, $`T_3`$) | parameter-free, anchor-independent |
| $`\Omega_\Lambda`$ | over-determined by three independent readings |
| $`\Lambda`$ (absolute) | prediction from the $`\alpha`$ reading (23%) or the mass reading (~14x); circular from the $`\Lambda`$ reading |
| $`\alpha`$, $`\alpha_s`$, $`\alpha_W`$ (absolute) | prediction from the $`\Lambda`$ reading (0.4%); the anchor when $`\alpha`$ is the input |
| first positive eigenvalue $`2/R_\Lambda^2`$ | surface spectral result |
| fermion mass ratios | structural predictions (McKay / torsion) |
| absolute fermion masses | set by the $`m_e`$ benchmark |
| three generations, Yang-Mills gap | structural results on $`S^3/2I`$ |

[↑ Contents](#contents)

---

[![Resonant Universe](https://img.youtube.com/vi/I3AOKh-RRTA/mqdefault.jpg)](https://www.youtube.com/watch?v=I3AOKh-RRTA)

*Topology holds. Wave is. Particle samples.*

---

/ **[`main`](/README.md)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
