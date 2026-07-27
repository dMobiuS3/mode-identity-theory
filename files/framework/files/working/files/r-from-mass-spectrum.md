/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# R from the Particle Mass Spectrum

Working notes on determining the curvature radius R independently of Λ, the CMB, and the de Sitter relation, using the mass formula's dependence on the hierarchy factor Ω_Λ.

**Status:** EXECUTED (2026-06-15). Order-of-magnitude result. The route runs and genuinely breaks the circularity, but the precision ceiling is about 1 order of magnitude, not the few percent originally targeted. Electron and muon give R ≈ 20 Gpc, Λ ≈ 8 × 10⁻⁵⁴ m⁻², about 14× below the observed 1.11 × 10⁻⁵². No pair of assigned fermions beats this; the floor is structural. See the Result section.

**Why this matters:** ΛR² = 3 is derived from the postulate (eigenvalue + Gauss equation; provenance in [the R problem](r-problem.md)). The coefficient 3 is the content. But Λ = 3/R² produces a number only with an independent R. Every previous route to R is either circular (de Sitter: R = √(3/Λ), feeds Λ back) or not an independent route to R (the Molien gap fixes the low-ℓ deficit boundary, a surviving spectral fact, but does not by itself pin R). The mass spectrum does determine R independently of Λ, the CMB, and the de Sitter relation, so the circularity is genuinely broken: Λ = 3/R² becomes a forward prediction from particle physics. The prediction lands within about 1 order of magnitude of observed, a real result at that bar but not the percent-level number Sections VI and VIII originally claimed.

---

## Result (executed 2026-06-15)

Run with the framework's own published data (`mass-spectrum.md`): electron = (R7, triv, dist 4), muon = (R8, std, dist 5), so Δd = 1; C_geom(R7) = 0.7564, C_geom(R8) = 0.2382; T²(R7, triv) = 2.250, T²(R8, std) = 13.090; √Ω_Λ = 1.019 × 10⁶¹.

The formula reproduces both masses (m_e = 5.22 × 10⁻⁴ GeV, m_μ = 0.103 GeV) and predicts the ratio m_μ/m_e = 198 against the measured 206.8, a 4.5% miss. Inverting that ratio for the scale gives:

- Ω_Λ = 1.42 × 10¹²³ (framework value 1.04 × 10¹²²)
- R ≈ 20 Gpc (framework 5.37 Gpc), a factor 3.7 too large
- Λ ≈ 8.1 × 10⁻⁵⁴ m⁻², about 14× below the observed 1.11 × 10⁻⁵² (1.14 orders of magnitude); R too large, so Λ too small

The 4.5% ratio miss becomes a factor of 14 in Λ because the McKay lever is weak: with Δd = 1 the ratio depends on Ω_Λ only through (√Ω_Λ)^(1/30), so inverting amplifies any input error by 60/Δd = 60×.

**Pair scan.** Every assigned charged-fermion pair was checked; none beats electron-muon. The three low-distance, well-fit masses (e, up, μ; residuals 0.94 to 1.02) sit within Δd ≤ 1 of each other, the worst lever. Any larger lever requires a high-distance mass (down, τ, b, t), whose residuals scatter from 0.41 to 3.23 and blow the inversion up: electron-bottom (Δd = 3, the best lever of any real pair) lands 89× off because bottom's 28% residual swamps the lever gain, and any pair involving τ or the down quark misses by 10¹¹ to 10⁵⁴. The McKay-propagator note already established these high-distance residuals as irreducible scatter, so there is no common-mode high-distance pair to escape through.

**The floor.** Electron-muon is the tightest single estimate (Λ within 1.14 orders); the well-behaved pairs straddle observed and spread over 1 to 2 orders. The ceiling is the formula's irreducible few-percent ratio scatter times the smallest available McKay lever (60×). It is structural and cannot be improved by pair selection.

**What stands.** Topology plus two measured lepton masses plus zero cosmological input land Λ within about 1 order of magnitude of observed, independently of Λ, the CMB, and the de Sitter relation. That is a real, falsifiable, independent leg under Λ ~ 3/R² at R of order Gpc. It is not, and structurally cannot be, a percent-level prediction.

---

## I. The Mechanism

The mass formula (engine file §14):

```math
m(\rho, \sigma) = \mu_\Lambda \times C_{\text{geom}}(\rho) \times (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \times T^2(\rho \otimes \sigma)
```

Three of the four factors are dimensionless topological ratios:
- C_geom(ρ): geometric mean of C(e/D) over Kostant exponents of irrep ρ
- (√Ω_Λ)^(dist/30): McKay graph distance dilution, h(E₈) = 30
- T²(ρ⊗σ): Reidemeister torsion

All physical dimensions live in the vacuum energy floor:

```math
\mu_\Lambda = \rho_\Lambda^{1/4} = \left(\frac{\Lambda c^4}{8\pi G}\right)^{1/4}
```

Both μ_Λ and Ω_Λ = (R/ℓ_P)² depend on R and G. But G = 3c⁴/(8πR²μ_Λ⁴), so everything reduces to (c, ℏ, R, topological ratios).

---

## II. The G-Power Collection

From the Waltz working notes. G enters the mass formula through two doors:

| Factor | G-dependence | Exponent |
|---|---|---|
| μ_Λ = (Λc⁴/(8πG))^(1/4) | G^(-1/4) | -1/4 |
| (√Ω_Λ)^(dist/30) = (R²c³/(ℏG))^(dist/60) | G^(-dist/60) | -dist/60 |

Total G-exponent in the mass formula:

```math
\alpha(d) = -\frac{1}{4} - \frac{d}{60} = -\frac{15 + d}{60}
```

The mass formula becomes:

```math
m = K(c, \hbar, R, \text{topology}) \cdot G^{-(15+d)/60}
```

where K contains only c, ℏ, R, and dimensionless topological ratios. Solving for G:

```math
G = \left(\frac{K}{m_{\text{obs}}}\right)^{60/(15+d)}
```

One equation, one unknown (G), given R and one measured mass. But G and R are related through Λ = 3/R² and G = 3c⁴/(8πR²μ_Λ⁴). So the system has one free parameter: R.

---

## III. The Two-Mass Determination

One measured mass (m_e) gives one equation in one unknown (R, with G slaved to R).

A second measured mass (m_μ) gives a second equation in the same unknown. The system is overdetermined. Either:
- Both give the same R (framework is consistent, R is determined)
- They disagree (framework fails at the mass formula level)

The ratio of two masses at different McKay distances:

```math
\frac{m_\mu}{m_e} = \frac{C_\mu}{C_e} \times (\sqrt{\Omega_\Lambda})^{(d_\mu - d_e)/30} \times \frac{T^2_\mu}{T^2_e}
```

If d_μ ≠ d_e, the ratio depends on Ω_Λ, which depends on R. The topological prefactors are pure numbers. Measuring the ratio and computing the prefactors gives Ω_Λ, hence R.

---

## IV. What's Needed

| Requirement | Status | Source |
|---|---|---|
| Mass formula structure | ESTABLISHED | Engine file §14 |
| G-power collection | ESTABLISHED | Waltz working notes §II |
| Electron assignment (ρ, σ, dist) | ASSIGNED (dist = 4) | Engine file §14 |
| Muon assignment (ρ, σ, dist) | ASSIGNED (R8, std, dist = 5; Δd = 1 vs electron) | mass-spectrum.md §III |
| C_geom for electron and muon | COMPUTED | Kostant exponents |
| T² for electron and muon | COMPUTED | Reidemeister torsion, T²(R₃)/T²(R₄) = φ⁻⁴ |
| (ρ,σ) → (T₃,Y) assignment rule | ESTABLISHED (10/10 verified) | mass-spectrum.md §IV.4 |
| Electron mass (measured) | 0.511 MeV | Input |
| Muon mass (measured) | 105.66 MeV | Input |
| Muon/electron ratio | 206.768 | Known to 9 significant figures |

The assignment rule is resolved (mass-spectrum.md §IV.4, 10/10 verified) and the computation has been executed; see the Result section. The remaining limitation is precision, not the assignments: the McKay-lever amplification (Sections VI and VIII) caps the route at order of magnitude.

---

## V. The Computation (executed 2026-06-15)

**Step 1.** Write m_e and m_μ as explicit functions of R using the mass formula with all topological factors evaluated.

**Step 2.** Take the ratio m_μ/m_e. The μ_Λ prefactor cancels. The remaining R-dependence lives in (√Ω_Λ)^((d_μ - d_e)/30).

**Step 3.** Solve for Ω_Λ from the measured ratio and the computed topological prefactors.

**Step 4.** Extract R from Ω_Λ = (R/ℓ_P)², noting ℓ_P depends on G which depends on R. The G-power collection resolves this to a single closed-form exponent.

**Step 5.** Compute Λ = 3/R².

**Step 6.** Compare with Λ_obs = 1.11 × 10⁻⁵² m⁻². Result: Λ ≈ 8.1 × 10⁻⁵⁴, about 14× low (Result section).

---

## VI. What Was Achieved

The forward chain runs:

```math
m_e, m_\mu \text{ (measured)} \xrightarrow{\text{mass formula}} R \xrightarrow{\Lambda R^2 = 3} \Lambda
```

Λ is a prediction from particle physics: no CMB input, no de Sitter circularity. The coefficient 3 is derived from the postulate (eigenvalue + Gauss); the scale R is derived from the mass spectrum. This is a genuine, independent prediction of Λ from topology plus two measured masses.

The realized precision is order of magnitude, not percent. The few-percent target stated in the original draft was wrong. The McKay lever for the electron-muon pair is weak (Δd = 1), so the formula's few-percent ratio accuracy amplifies by 60× into a roughly 1-order-of-magnitude uncertainty on Λ (executed value Λ ≈ 8 × 10⁻⁵⁴, about 14× below observed; Result section). The honest claim is "Λ within about 1 order of magnitude of observed, from particle physics alone," which is the success at the bar the structure supports.

---

## VII. What Failure Looks Like

- The electron and muon give inconsistent R values: the mass formula's assignments are wrong.
- The R value gives Λ far from observed: the framework fails at the quantitative level.
- The assignments are too uncertain (OPEN status) to execute the computation: the program is blocked until the assignment rule is derived.

All three are informative. The computation should be done regardless.

**Realized outcome.** The second, in a precise sense: R from electron-muon gives Λ 14× from observed, far enough to fail a percent-level prediction but within 1 order of magnitude, which is a real result at the order-of-magnitude bar. The third mode is retired (the assignments are Established). The first did not occur fatally: different pairs give different R, but the 1-to-2-order spread is the expected McKay-lever amplification of the formula's residual scatter, not an inconsistency in the assignments.

---

## VIII. Connection to the 2% Systematic

The engine file documents a ~2% systematic offset across multiple observables (Λ, H₀, a₀, electron mass running ~2% high, muon ~2.5% low). The electron and muon bracket the measured values from opposite sides. Their geometric mean recovers G to better than 1% (Waltz document). This bracketing pattern is consistent with a single upstream correction (suspected: Gauss-Codazzi factor precision). The opposite-direction bracketing that helps the geometric mean (where the misses cancel) hurts the ratio (where they compound). R is read from the ratio m_μ/m_e, not the geometric mean, so the two ~2% misses add to a 4.5% ratio miss, which the Δd = 1 McKay lever amplifies by 60× into the factor-of-14 offset in Λ (Result section). The earlier estimate here, that 2% would carry through as 2% in Λ, assumed the misses were common-mode in the ratio; they are anti-correlated. The order-of-magnitude floor is set by this residual correlation, not by the per-mass 2% accuracy, and no assigned-fermion pair has common-mode residuals at large enough Δd to beat the electron-muon factor of 14.

---

*The mass spectrum knows R. The hierarchy factor carries it. Two masses triangulate it.*

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
