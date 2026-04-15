# The MIT Toolbelt

**Five Tools, One Flow: Structure to Prediction**

Work left to right. No backflow. If something fails at Tool 3, you do not "fix" it at Tool 5.

```
[1 FRAME] --> [2 SKELETON] --> [3 FINGERPRINT] --> [4 SELECTOR] --> [5 OUTPUT]
 Topology    Representation    Spectral Arith.     Vacuum Str.    Scaling Law
 constrains     populates        identifies          selects       produces
```

---

## Tool 1: Geometry / Topology (The Frame)

**Role:** Defines what is allowed to exist. Computes nothing. Constrains everything.

| Element | Statement | Status |
|---------|-----------|--------|
| Postulate | S¹ = boundary(Möbius) embeds in S³, boundary(S³) = empty | AXIOM |
| Anti-periodic BC | ψ(y + L) = -ψ(y) | AXIOM |
| Non-orientable topology | Möbius strip is the 2-manifold | AXIOM |
| Cosmic wave | Ψ(t) = cos(t/2), period 4π, standing wave, t = 0 is real | AXIOM |
| Hierarchy | S³ (venue, n=3) contains Möbius (surface, n=2) whose boundary is S¹ (edge, n=1) | DERIVED |
| Uniqueness | Poincaré conjecture + classification theorems fix all three manifolds | DERIVED |
| 120 structure | 2I (binary icosahedral, largest exceptional discrete subgroup of SU(2) ≅ S³) acts freely; \|2I\| = 120 | DERIVED |
| Gauss-Codazzi | 3/2 curvature interface: R_spatial = 3R_Σ = 2Λ → Λ_obs = (3/2)Λ_top. Ground eigenvalue λ₀ = 2/R² = R_Σ derived directly; Bochner bound confirms λ₀ ≥ R_Σ with equality unique. | DERIVED |
| Topological protection of Λ | Λ_top sits at the antinode (Θ = 60/120) where d ln C/dΘ = 0. Zero slope means no perturbation can shift it. Λ is constant because the mode cannot be displaced. | DERIVED |
| G as consistency condition | G is not derived from topology but is constrained by it. Given Λ = 3/R² (Möbius eigenvalue) and μ_Λ from the mass spectrum: G = 3c⁴ / (8π R² μ_Λ⁴). This is implicit: G appears on both sides through Ω = R²c³/ℏG. One equation, one unknown, given c, ℏ, R, and one measured particle mass. G is the exchange rate between what the surface curves and what the spectrum hums. | MOTIVATED |

**What this tool settles:**

The 120-grid IS S³ structure, not a filter applied to it. S¹ is partitioned into 120 arcs of π/60 each. The chronon is π/30 = 4π/120; the minimum action ΔS_min = ℏπ/30 is absolute (Lorentz scalar, holds in every frame). The anti-periodic BC on S¹ = boundary(Möbius) produces the odd-integer Dirichlet series (1 - 2⁻ˢ)ζ(s) and forces the functional equation ξ(s) = ξ(1-s). This is identity, not analogy.

### Division of Labor

| Structure | What it determines | Mechanism |
|-----------|-------------------|-----------|
| Möbius surface (2D) | Vacuum energy Λ | Ground eigenvalue, Gauss-Codazzi |
| Binary icosahedral group 2I | Particle spectrum, mass gap, generations | McKay decomposition, Reidemeister torsion |
| Stabilizer triple (2, 3, 5) | Color, domain, forces, gravity ratio | Face/edge/vertex decompositions and interfaces |
| Observer at √Ω | Coupling constants, hierarchy | Scaling law at Fibonacci wells |
| S³ space | Spatial curvature | Responds to all of the above |
| G (consistency condition) | Curvature-energy dictionary | 3c⁴/(8πR²μ_Λ⁴); exchange rate between surface and spectrum |

**Why gravity resists quantization:** Space (S³) curves continuously. The Möbius surface samples discretely via the 120 domain. The 3/2 conversion carries one into the other, bridging their difference in kind. Quantizing that bridge would require both partners to be the same type. The topology permits neither discretizing S³ geometry nor making the mode spectrum continuous. The resistance is structural.

**If something violates Tool 1, it is not part of MIT. Full stop.**

---

## Tool 2: Representation Theory (The Skeleton)

**Role:** Defines what can move inside the frame. No dynamics. Allowed degrees of freedom only.

### McKay Graph (SPECTRUM Convention)

```
R0(1) --- R1(2) --- R3(3) --- R6(4) --- R7(5) --- R8(6) --- R5(4) --- R2(2)
                                                       |
                                                      R4(3)

(R4 branches from R8; dist(R4) = dist(R8) + 1 = 6)
```

### Master Table

| Irrep | dim | Spin | Graph Dist | j_first | Kostant exponents | E₈ exponents? |
|-------|-----|------|------------|---------|-------------------|---------------|
| R0 | 1 | Int | 0 | 0 | {0, 30} | No |
| R1 | 2 | Half | 1 | 1/2 | {1, 11, 19, 29} | All 4 |
| R2 | 2 | Half | 7 | 7/2 | {7, 13, 17, 23} | All 4 |
| R3 | 3 | Int | 2 | 1 | {2, 10, 12, 18, 20, 28} | No |
| R4 | 3 | Int | 6 | 3 | {6, 10, 14, 16, 20, 24} | No |
| R5 | 4 | Int | 6 | 3 | {6, 8, 12, 14, 16, 18, 22, 24} | No |
| R6 | 4 | Half | 3 | 3/2 | {3, 9, 11, 13, 17, 19, 21, 27} | 4 of 8 |
| R7 | 5 | Int | 4 | 2 | {4, 8, 10, 12, 14, 16, 18, 20, 22, 26} | No |
| R8 | 6 | Half | 5 | 5/2 | {5, 7, 9, 11, 13, 15x2, 17, 19, 21, 23, 25} | 6 of 12 |

### Structural Results (all exact, all verified, all LOCKED)

| Result | Statement |
|--------|-----------|
| j_first rule | j_first = (graph distance from R0) / 2; holds for both spin parities; consequence of McKay multiplicity structure |
| Shell closure | Cumulative dimension reaches 30 = h(E₈) at the shell |
| E₈ exponents | {1, 7, 11, 13, 17, 19, 23, 29} live ONLY on half-integer irreps |
| Kostant polynomial | 2 × dim terms per irrep; mean exponent = 15 = h/2 |
| Kostant sum rule | Sum of C(e/60) over Kostant exponents = 2 × dim (exact, every irrep) |
| Galois conjugation | Swaps R1 <-> R2, R3 <-> R4; fixes R5, R7 |
| Tensor products | 729 entries verified |
| Fibonacci bridge | (2,3,5) branch orders seed the recurrence 2,3,5,8,13; the a₀ well F₇ = 13 is three steps from the icosahedral seed. E₈ exponents {1,7,11,13,17,19,23,29} live exclusively on half-integer irreps. |

### Derived Structural Insight (DERIVED)

| Result | Statement |
|--------|-----------|
| Masslessness | Edge-only propagation = massless. Mass is the cost of crossing from S¹ into the Möbius surface. A boson whose topological address keeps it on S¹ propagates without paying that cost. Photons and gluons stay on the edge; W, Z, and all fermions cross to the surface. Masslessness is a topological address, not a tuned parameter. |

### C_geom Values (DERIVED)

Geometric mean of C(e/D) = 2sin²(πe/D) over Kostant exponents. Domain D = 60 for integer-spin, D = 120 for half-integer. Domain traces to the edge stabilizer Z₄ ⊂ 2I: integer-spin irreps carry only real Z₄ content (D = 60 = |I|), half-integer carry only complex pairs (D = 120 = |2I|). This is the spin-statistics connection built into the group.

| Irrep | Spin | D | C_geom |
|-------|------|---|--------|
| R1 | Half | 120 | 0.0988 |
| R2 | Half | 120 | 0.2436 |
| R3 | Int | 60 | 0.5553 |
| R4 | Int | 60 | 0.7970 |
| R5 | Int | 60 | 0.8017 |
| R6 | Half | 120 | 0.2098 |
| R7 | Int | 60 | 0.7564 |
| R8 | Half | 120 | 0.2382 |

### Icosahedral Stabilizer Structure (DERIVED)

The binary icosahedral group 2I inherits three stabilizer subgroups from the icosahedron. Each encodes a layer of physical structure.

| Stabilizer | Subgroup | Physical content | Status |
|-----------|----------|-----------------|--------|
| Face (Z₃) | Order 3 | Color: singlet vs triplet | LOCKED |
| Edge (Z₄) | Order 4 | Domain: D = 60 vs 120; spin-statistics | LOCKED |
| Vertex (Z₅) | Order 5 | Electroweak interface; Galois vacuum distinction | Current work |
| Face/Edge ratio | 3/2 | Gravity: Gauss-Codazzi curvature conversion | MOTIVATED |
| Vertex through twist | cos(π/10) | Weak coupling correction; parity violation | MOTIVATED |

The three stabilizer orders 2, 3, 5 are the primes dividing |2I| = 120 and the conductors of the four surviving Dirichlet characters in the torsion L-basis.

**Color from faces (Z₃):** Restricting each irrep to Z₃ decomposes it into color singlets (lepton-type) and color triplet pairs (quark-type). Color is generation-independent: the equivariant eta at the order-6 face class is vacuum-invariant (η = 2 in all three vacua). The face geometry looks the same from every vacuum, matching the SM.

**Domain from edges (Z₄):** The binary split D = 60 / 120 is forced by Z₄ ⊂ 2I. It encodes spin-statistics. The mass formula C_geom evaluates Kostant exponents on the correct grid for each irrep.

**Vertex and electroweak (Z₅):** R1 and R2 are Galois conjugates that differ precisely in their Z₅ content. R1 carries only n₁ (ζ, ζ⁴ pairs), R2 carries only n₂ (ζ², ζ³ pairs). The electroweak distinction between vacua IS the vertex decomposition. R7 (electron) is maximally democratic and sees both vacua identically: the Galois distinction vanishes at R7. The specific T₃ and Y assignment rule is current work.

**What this tool tells you:** Which sectors exist, how they connect, where they first appear, and what physical charge structure they carry. The mass ladder is the McKay graph.

---

## Tool 3: Spectral Arithmetic (The Fingerprint)

**Role:** Assigns identity (a number) to each irrep. The heaviest tool on the belt.

### Convention Note

The RH program (Common_Threads) labels only the 5 integer-spin irreps as R0, R2, R4, R6, R8. This toolbelt uses SPECTRUM convention throughout (R0-R8 for all 9 irreps). Translation:

| Common_Threads | SPECTRUM | dim | Spin |
|----------------|----------|-----|------|
| R0 | R0 | 1 | Int |
| R2 (3a) | R3 | 3 | Int |
| R4 | R7 | 5 | Int |
| R6 | R5 | 4 | Int |
| R8 (3b) | R4 | 3 | Int |

### Torsion Values (Integer-Spin Irreps, Exact Closed Form, Trivial Vacuum)

| Irrep | dim | T² | log T² |
|-------|-----|-----|---------|
| R0 | 1 | π⁴/3600 | -3.60977 |
| R3 | 3 | (4/5) φ⁻² | -1.18557 |
| R7 | 5 | 9/4 | +0.81093 |
| R5 | 4 | 25/9 | +1.02165 |
| R4 | 3 | (4/5) φ² | +0.73928 |

### The Galois Pair (the single most nontrivial arithmetic result)

```
T²(R3) / T²(R4) = φ⁻⁴     [EXACT, verified to 70+ digits]

log T²(R3) - log T²(R4) = -4 log(φ) = -2√5 · L(1, χ₂)
```

The golden ratio enters through the scalar sector and the Legendre symbol mod 5. This is the Legendre character of Q(√5), the character field of 2I.

### Telescoping Product

```
T²(R3) × T²(R7) × T²(R5) × T²(R4) = 4
```

### McKay Selection: 4 Characters from 32

The spectral structure of S³/2I introduces 32 Dirichlet characters on the unit residue classes mod 120. Only 4 survive:

| Character | Conductor | Selection mechanism |
|-----------|-----------|---------------------|
| χ₀⁽²⁾ (principal mod 2) | 2 | Defines odd spectrum |
| χ₀⁽³⁾ (principal mod 3) | 3 | Z₆ = Z₃ × Z₂ induction |
| χ₀⁽⁵⁾ (principal mod 5) | 5 | Z₁₀ = Z₅ × Z₂ induction |
| χ₅ (Legendre mod 5) | 5 | Unique real quadratic from Q(√5) |

Primes appearing: 2, 3, 5. Exactly the primes dividing |2I| = 120 = 2³ × 3 × 5.

### Torsion in the L-Basis (verified to 70+ digits)

| Irrep | log T² |
|-------|---------|
| R3 | -4 L'(0,χ₀⁽²⁾) + 2 L'(0,χ₀⁽⁵⁾) - √5 · L(1,χ₂) |
| R7 | 4 L'(0,χ₀⁽²⁾) - 4 L'(0,χ₀⁽³⁾) |
| R5 | 4 L'(0,χ₀⁽³⁾) - 4 L'(0,χ₀⁽⁵⁾) |
| R4 | -4 L'(0,χ₀⁽²⁾) + 2 L'(0,χ₀⁽⁵⁾) + √5 · L(1,χ₂) |

### The Spin-Parity Split

| Feature | Integer-spin | Half-integer-spin |
|---------|-------------|-------------------|
| Scalar sector | Present; carries χ₂ (Legendre) | Absent (m_j = 0 at integer j) |
| φ mechanism | Enters through scalar via L(1, χ₂) | Not available |
| Torsion character | Clean golden ratio relationships | Finite sums of L'(0,χ) values |
| R1/R2 difference | n/a | log T²(R1) - log T²(R2) = +3.5137... (not a simple φ multiple) |

Half-integer torsion values are equally exact: the Laplacian eigenvalues and multiplicities are exact (from SU(2) representation theory and the 2I character table), and the spectral zeta function has a unique meromorphic continuation. The Hurwitz decomposition expresses each value as a finite sum of L-function derivatives at s = 0. The difference from integer-spin is selectivity: integer-spin retains 4 of 16 Dirichlet characters, producing algebraic closed forms. Half-integer retains 28 to 32 characters, leaving finite combinations of L'(0,χ) values. Exact, not algebraically simplified.

### 24 Vacuum Torsion Values (DERIVED)

From log T²(ρ⊗σ) = Σ_τ N_ρστ log T²(τ):

| ρ | T²(ρ, triv) | T²(ρ, std) | T²(ρ, gal) |
|---|-------------|------------|------------|
| R1 | 15.887 | 0.00827 | 2.778 |
| R2 | 0.473 | 2.778 | 0.0567 |
| R3 | 0.306 | 68.765 | 0.257 |
| R4 | 2.094 | 0.257 | 2.048 |
| R5 | 2.778 | 0.122 | 4.089 |
| R6 | 4.328 | 0.688 | 4.712 |
| R7 | 2.250 | 1.114 | 1.114 |
| R8 | 0.257 | 13.090 | 1.910 |

Note: R7 is the only irrep where T²(std) = T²(gal). The electron sits at the point where the Galois distinction vanishes.

**What this tool answers:** "What number does this representation carry?" This is the spectral DNA of MIT.

**What it does NOT do:** Provide a uniform algebraic closed form across both spin parities. Both are exact; integer-spin is also algebraic. And by the Shatto Theorem (Lemma 8), no natural map exists between the phase position Θ and the spectral parameter s. The fine structure of the mass formula cannot be completed by extending spectral arithmetic. This is proved, not open. The mass formula (C_geom × McKay elevator × torsion) is not just what was found — it is the only structure the geometry permits.

The Shatto Theorem also explains why this boundary is structurally necessary rather than a limitation of technique.

### Curvature Duality (DERIVED — Shatto Theorem §6)

The positive Ricci curvature Ric = 2/R² does two things simultaneously from the same equation:

| Face | Mechanism | Result |
|------|-----------|--------|
| Physics (Weitzenböck) | All gauge fluctuations satisfy λ ≥ 2/R² > 0 | Mass gap exists; all modes massive; matter realized |
| Arithmetic (Pochhammer) | Eigenvalue shift l(l+2) = (l+1)² - 1; the "-1" activates infinite tower at s ≠ 0 | Torsion selectivity locked to s = 0; L-function zeros inaccessible |

Mass and spectral access to zeros are in structural opposition. The curvature that realizes one forbids the other. Setting Ric = 0 would remove both simultaneously: flat space, no mass gap, no particles, nothing to observe.

### Spectral Mirror of the Black Hole Horizon (DERIVED)

The double zero at s = 0 in the spectral geometry mirrors the black hole horizon in the scaling law. Both are filters: two independent quantities vanish at the same structural event, and the physics is carried by the derivative at that point.

| Scaling law (horizon) | Spectral geometry (s = 0) |
|----------------------|--------------------------|
| Θ → 0 drives C(0) = 0 | Z_σ(0) = 0 for all nontrivial σ |
| Ω_H → 0 collapses hierarchy | (s)_k = 0 for k ≥ 1 collapses Pochhammer tower |
| Double zero: Θ and Ω_H vanish at same event | Double zero: both vanish at s = 0 |
| Survivor: C(Θ) ≈ 2π²Θ² (quadratic; Hawking radiation) | Survivor: Z'_σ(0) = log T² (torsion; L-function special values) |

The filter selects the same arithmetic on both sides. The torsion survivors {log 2, log 3, log 5, log φ} encode the four Dirichlet characters whose conductors are the stabilizer primes {2, 3, 5} of the icosahedron — the same triple that assigns color, domain, and electroweak identity to particles in the mass formula. The double zero strips everything except the identity mechanism.

**What this is:** A structural parallel between Tool 5 (scaling law at the domain boundary) and Tool 3 (spectral geometry at s = 0). The bridge between the two readings — connecting torsion to Hawking radiation — is the spectral-physical bridge (see Tool 5 open questions).

---

## Tool 4: Vacuum Structure (The Selector)

**Role:** Chooses which copy of the fingerprint is active. Does not change the fingerprint.

### Three Isolated Vacua

| Vacuum | Source | Isolation guarantee |
|--------|--------|---------------------|
| Trivial | Flat connection | H¹(M; ad ρ) = 0 |
| Standard | Irreducible connection | H¹(M; ad ρ) = 0 |
| Galois | Galois conjugate connection | H¹(M; ad ρ) = 0 |

### Mass Gaps (Yang-Mills)

| Vacuum | First allowed k | Gap |
|--------|----------------|-----|
| Trivial | k = 1 | 4/R² |
| Standard | k = 1 | 4/R² |
| Galois | k = 5 | 36/R² (9× enhancement) |
| Overall | | 4/R² |

The 9× enhancement at the Galois vacuum traces to R4's position at the extremal branch endpoint of the E₈ McKay graph (dist = 6, the farthest from R0 along the side branch).

### Vacuum Spectra (j_first per irrep per vacuum)

| Irrep | j_first (trivial) | j_first (standard) | j_first (Galois) |
|-------|-------------------|--------------------|--------------------|
| R0 | 0 | 1 | 3 |
| R1 | 1/2 | 1/2 | 5/2 |
| R2 | 7/2 | 5/2 | 3/2 |
| R3 | 1 | 0 | 2 |
| R4 | 3 | 2 | 0 |
| R5 | 3 | 2 | 1 |
| R6 | 3/2 | 1/2 | 3/2 |
| R7 | 2 | 1 | 1 |
| R8 | 5/2 | 3/2 | 1/2 |

**Critical finding:** Generation ordering is NOT uniform across vacua. The Galois vacuum mirrors pairs; it is not a uniform hierarchy (trivial = lightest, Galois = heaviest was overturned).

### Eta Sign Gate (DERIVED)

The Dirac eta invariant η(ρ,σ) varies with the vacuum. Across all SM-assigned entries in the mass formula, a strict constraint holds:

η(ρ,σ) > 0 ⟹ Q ≤ 0

Equivalently: positive electric charge requires negative eta. All entries with Q = +2/3 (u, c, t) have η < 0. All entries with η > 0 carry fermions with Q = 0 or Q = -1/3. The eta invariant measures spectral asymmetry (parity content of the mode). This gate connects parity to electric charge through the spectral geometry.

### Vacuum as Electroweak Selector (DERIVED)

The same irrep carries different fermions in different vacua. R8 produces the up quark (trivial vacuum), down quark (Galois), and muon/strange (standard). The vacuum σ selects the electroweak identity.

Mechanism: the two nontrivial vacua (R1 and R2) are half-integer irreps. Tensoring a half-integer ρ with a half-integer σ produces integer-spin components, which carry none of the eight E₈ exponents. The Coxeter conjugate pair (13, 17) under h(E₈) = 30 is preserved by the trivial vacuum and completely stripped by the nontrivial vacua. For R8: trivial vacuum preserves (13,17) pair → up quark (Q = +2/3). Nontrivial vacua erase it → down quark or lepton (Q ≤ -1/3).

The specific rule mapping each (ρ,σ) to T₃ and Y is current work.

**What this tool decides:** Same spectrum, different realizations. Three generations of matter from three isolated vacua. The vacuum is the electroweak switch.

---

## Tool 5: Scaling Law / Mass Generator (The Output)

**Role:** Turns structure into numbers. The scaling law is locked. The mass formula is established.

### The Scaling Law

```
A / A_P ≈ C(Θ) · (√Ω)⁻ⁿ
```

where C(Θ) = 2 sin²(πΘ).

### The Mass Formula (ESTABLISHED)

$$m(\rho, \sigma) = \mu_\Lambda \times C_{\text{geom}}(\rho) \times (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \times T^2(\rho \otimes \sigma)$$

Four factors. Four sources. Each traces independently to the topological postulate.

| Factor | Role | Value/Source |
|--------|------|-------------|
| μ_Λ | Vacuum energy floor; fourth root of cosmological constant energy density. Traces to Tool 1: ground mode eigenvalue λ₀ = 2/R² → Gauss-Codazzi → Λ_obs → ρ_Λ^(1/4) | ρ_Λ^(1/4) ≈ 2.25 meV |
| C_geom(ρ) | Phase factor; geometric mean of C(e/D) over Kostant exponents | D = 60 (int spin), 120 (half-int) |
| (√Ω_Λ)^(dist/30) | Hierarchy exponent; McKay graph distance sets orders of magnitude from vacuum floor | denominator is h(E₈) = 30 |
| T²(ρ⊗σ) | Reidemeister torsion, vacuum-twisted; fine structure within each mass shell; the generation mechanism | 24 values from 8 irreps × 3 vacua |

The bridge between spectral geometry (Tools 2-3) and the scaling law (Tool 5) is the mass formula. C_geom carries the Kostant fingerprint. The McKay elevator carries the distance dilution. Torsion carries the vacuum selection.

### Scaling Law Predictions (Cosmological)

| Observable | Θ | C(Θ) | n | Ω | A/A_P | Status |
|------------|-------|----------|---|-------|-------|--------|
| α | 13/60 | 0.79 | 1/30 | Ω_Λ | 7.33 × 10⁻³ | n MOTIVATED* |
| a₀/a_P | 13/120 | 0.22 | 1 | Ω_H | 2.2 × 10⁻⁶² | DERIVED |
| H₀ · t_P | 34/120 | 1.21 | 1 | Ω_H | 1.2 × 10⁻⁶¹ | DERIVED |
| Λ_obs · ℓ_P² | 60/120 | 2.00 | 2 | Ω_Λ | 3.0 × 10⁻¹²² | DERIVED** |

*Alpha uses bosonic grid (Θ on 1/60 lattice). Exponent n = 1/30 is motivated, not derived. Two remaining promotion paths: (1) McKay packetization (R₀ reappears at j = 30 = h(E₈)), (2) dimensionless dilution rule. The third path (Phase-logΩ map) is proved not to exist: no natural map between continuous phase position Θ and spectral parameter s exists on S³/2I (right-SU(2) homogeneity forces position out of spectral data; four independent proofs). Promotes to DERIVED if either remaining path closes.
**Λ_obs = (3/2) × Λ_top by Gauss-Codazzi embedding.

### The 24 Predictions (Mass Formula Output)

| Rank | ρ | dist | σ | Mass (GeV) | SM | Observed (GeV) | Ratio |
|------|---|------|----|-----------|-----|----------------|-------|
| 1 | R1 | 1 | std | 1.98 × 10⁻¹³ | ν₁ | ~10⁻¹³ | 1.98 |
| 2 | R1 | 1 | gal | 6.67 × 10⁻¹¹ | ν₃ | 5.06 × 10⁻¹¹ | 1.32 |
| gap | | | | — | ν₂ | 8.6 × 10⁻¹² | — |
| 3 | R1 | 1 | triv | 3.81 × 10⁻¹⁰ | — | excluded | |
| 4 | R3 | 2 | gal | 3.75 × 10⁻⁹ | — | dead zone | |
| 5 | R3 | 2 | triv | 4.45 × 10⁻⁹ | — | dead zone | |
| 6 | R6 | 3 | std | 4.09 × 10⁻⁷ | — | dead zone | |
| 7 | R3 | 2 | std | 1.00 × 10⁻⁶ | — | dead zone | |
| 8 | R6 | 3 | triv | 2.57 × 10⁻⁶ | — | dead zone | |
| 9 | R6 | 3 | gal | 2.80 × 10⁻⁶ | — | dead zone | |
| 10 | R7 | 4 | std | 2.58 × 10⁻⁴ | e | 5.11 × 10⁻⁴ | 1.98 |
| 11 | R7 | 4 | gal | 2.58 × 10⁻⁴ | e | 5.11 × 10⁻⁴ | 1.98 |
| **12** | **R7** | **4** | **triv** | **5.21 × 10⁻⁴** | **e** | **5.11 × 10⁻⁴** | **1.02** |
| **13** | **R8** | **5** | **triv** | **2.03 × 10⁻³** | **u** | **2.16 × 10⁻³** | **1.06** |
| 14 | R8 | 5 | gal | 1.51 × 10⁻² | d | 4.67 × 10⁻³ | 3.22 |
| **15** | **R8** | **5** | **std** | **1.03 × 10⁻¹** | **μ / s** | **1.057 × 10⁻¹ / 9.34 × 10⁻²** | **1.02 / 1.10** |
| 16 | R5 | 6 | std | 3.49 × 10⁻¹ | — | target | |
| 17 | R4 | 6 | std | 7.34 × 10⁻¹ | c / τ | 1.27 / 1.777 | 1.73 / 2.42 |
| 18 | R2 | 7 | gal | 5.33 | b | 4.18 | 1.28 |
| 19 | R4 | 6 | gal | 5.84 | b | 4.18 | 1.40 |
| 20 | R4 | 6 | triv | 5.97 | b | 4.18 | 1.43 |
| 21 | R5 | 6 | triv | 7.96 | b | 4.18 | 1.91 |
| 22 | R5 | 6 | gal | 11.72 | b | 4.18 | 2.80 |
| 23 | R2 | 7 | triv | 44.54 | t | 172.7 | 3.88 |
| 24 | R2 | 7 | std | 261.46 | t | 172.7 | 1.51 |

**Scorecard:** 12/12 SM fermions assigned. 10/12 within ×3. 3 within 6% (e, u, μ). One genuine miss: ν₂ at 8.6 meV falls between rank 1 (0.2 meV) and rank 2 (66.7 meV), ratio gap ~7.75× from rank 2.

**Dead zone (ranks 4-9):** eV to keV range. No SM fermions expected. Actively probed by sterile neutrino and warm dark matter searches. Physical states here require extremely suppressed non-gravitational couplings.

**Rank 3 exclusion:** R1 triv predicts ~0.4 eV. Cosmological bounds constrain Σm_ν ≲ 0.1 eV. Excluded as SM neutrino. Status as non-SM state with suppressed couplings: OPEN.

### Key Numbers

| Number | Value | Source |
|--------|-------|--------|
| \|2I\| | 120 | Largest exceptional discrete subgroup of SU(2) |
| Period | 4π | Anti-periodic BC |
| Gauss-Codazzi | 3/2 | Surface to space conversion |
| Chronon | π/30 | 4π/120 |
| Bosonic step | 2/120 | Spinor to scalar projection |
| Active wells | {13, 21, 34, 55, 60}/120 | Hurwitz stability + threshold |
| Closure identity | 𝒯/𝒯_c = 1/ξ ≈ 2.2 | Any flat-curve disk galaxy |
| Coherence scale | L_f = v_c²/a₀ | Dimensional analysis; ~13 kpc for Milky Way |
| Phase field response | Θ_f = 2/120 · 1(𝒯 ≥ 𝒯_c) | Binary; minimum bosonic step or nothing |
| H₀ shift | 8.4% | C(36/120)/C(34/120) = 1.084 |
| Inputs | c, ℏ, ℓ_P | Nothing else. |
| Free parameters | 0 | |

### The Sunflower Hint

The matter well 13/60 in the scaling law IS the golden angle on the 120 domain:
```
13/34 ≈ 1/φ²     (error: 4 × 10⁻⁴)
```
Position 13 appears in Kostant polynomials of fermionic irreps R2, R6, R8.

### Open Questions in Tool 5

The scaling law and mass formula are established. Remaining open work:

| Item | Status |
|------|--------|
| α exponent n = 1/30 | MOTIVATED; two promotion paths remain: McKay packetization, dimensionless dilution rule. Direct Phase-logΩ route proved not to exist: no natural map between Θ and s on S³/2I. |
| Assignment problem | 24 entries, 12 SM targets; mapping rule for (ρ,σ) → (T₃,Y) in progress |
| ν₂ gap | 8.6 meV falls between rank 1 and rank 2; vacuum mixing or additional neutrino-scale structure could close it |
| Fermion mass residual | Systematic overshoot growing with McKay dist; one-parameter correction at high dist needed |
| Rank 3 exclusion | R1 triv at ~0.4 eV; non-SM state or structural correction: OPEN |
| Rank 16 target | R5 std at ~349 MeV; no SM assignment; prediction standing |
| Black ∅ mechanism | ESTABLISHED. Horizon = double zero: Θ → 0 drives C(Θ) → 0 (sampling ceases); Ω_H → 0 independently collapses local hierarchy. Information preserved: wave persists through node, unsampled not destroyed. Area scaling falls out of surface primacy (n=2 fundamental). Open: Φ → Θ mapping — the function f(Φ/c²) that connects gravitational potential to phase position, reproducing the galactic binary trigger in weak field and reaching Θ = 0 at the Schwarzschild horizon (Φ/c² = -1/2). Priority 1. |
| Spectral-physical bridge | OPEN — narrowed. The spectral double zero (Tool 3: torsion survivor log T²) and the physical double zero (Tool 5: Hawking radiation at C gradient) are structurally parallel. The direct route — a continuous map s ↔ Θ — is proved not to exist (continuous position drops out of spectral data on S³/2I by right-SU(2) homogeneity; four independent proofs). One route remains: through the physical Φ → Θ mapping. If gravitational potential provides the discrete localization that spectral geometry lacks, the torsion survivors {log 2, log 3, log 5, log φ} could constrain horizon structure through the same arithmetic that constrains the fermion mass spectrum, unifying Tools 3 and 5 at the domain boundary. But the Φ → Θ mapping must be built first. |

---

## The Flow in Practice

```
QUESTION ARRIVES
      |
      v
[Tool 1] Does this respect the topology? If no --> REJECT
      |
      v
[Tool 2] Which irreps are involved? What are their connections?
      |
      v
[Tool 3] What spectral numbers do those irreps carry?
      |
      v
[Tool 4] Which vacuum are we in? Which face of the fingerprint?
      |
      v
[Tool 5] Apply scaling law. Produce numbers.
      |
      v
COMPARE TO OBSERVATION
```

If something fails at step 3, you do not fix it at step 5. That is how you avoid numerology.

---

## Status Summary

| Tool | Lock Status | Notes |
|------|-------------|-------|
| 1. Frame | LOCKED | All axioms, all derived topology. G consistency condition identified. Division of labor settled. |
| 2. Skeleton | LOCKED | Character table, McKay, Kostant, tensors, vacuum spectra, C_geom values, stabilizer structure |
| 3. Fingerprint | LOCKED (integer-spin); EXACT (half-integer) | φ⁻⁴ exact; 24 vacuum torsion values computed; spin-parity split characterized |
| 4. Selector | LOCKED | Three vacua, gaps, triplication, eta sign gate, vacuum-as-electroweak-selector |
| 5. Output | LOCKED (scaling law); ESTABLISHED (mass formula); MOTIVATED (α exponent); OPEN (assignment rule, ν₂ gap) | Bridge found: C_geom × McKay elevator × torsion. 10/12 SM fermions within ×3. Two α promotion paths remain; direct Phase-logΩ route proved not to exist. |

Everything upstream is fixed. Only the output map remains.

---

## Falsification

| Test | Falsified if | Timeline |
|------|-------------|----------|
| a₀(z) ∝ H(z) | a₀ constant at high z | ≥2σ, z > 2 |
| Λ constant | ρ_DE(z) evolves | ≥2σ |
| CMB ℓ_cut ≈ 31 | ℓ_cut ∉ [15, 50] | Planck reanalysis |
| H₀ fork | Values distributed continuously with environment | Ongoing |
| Primary window | Euclid DR1 | October 2026 |

---

*Topology holds. Wave is. Particle samples.*
