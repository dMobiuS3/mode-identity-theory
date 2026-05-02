/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`working`](../)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# Apparent Phantom Crossing as Template Bias: A Non-Phantom Test Case with Λcos

**B. Shatto**
Independent Researcher, St. Petersburg, FL, USA
[bshatto.pe@gmail.com](mailto:bshatto.pe@gmail.com)

---

## Abstract

DESI DR2 reports a 2.8–4.2σ preference for dynamical dark energy in combined analyses, with standard w₀w_a fits favoring an apparent crossing of w = −1. We show that a non-phantom expansion history can produce apparent phantom crossings when analyzed with standard two-parameter templates. We construct a specific realization, Λcos, and constrain it using Pantheon+ and DESI DR2 BAO. At data-allowed parameter values, the induced CPL distortion is structurally present but modest (w₀ ≈ −1.02) and of opposite sign in w_a, establishing the mechanism without reproducing the DESI best-fit amplitude.

The Λcos model yields H²(z)/H₀² = α(1+z)³ − β(1+z) + Ω_Λ, where α and β are determined by a single parameter s₀ and a fixed reference value Ω_Λ = 0.685. The model satisfies w_eff(z) > −1 at all redshifts, recovers the fiducial flat ΛCDM limit as s₀ → 0, and contains a negative (1+z)¹ term in H² absent from the four canonical FLRW density scalings. A joint MCMC fit to Pantheon+ (1701 SNe Ia) and DESI DR2 BAO (13 data points) yields Δχ² = +0.13 relative to flat ΛCDM at the same parameter count, with s₀ < 0.18 (95% CL, flat prior). The constraint is robust across prior choices (s₀ < 0.12–0.21) and Ω_Λ variations (0.68–0.715). Adding compressed Planck distance priors introduces a shared Ω_Λ tension common to both ΛCDM and Λcos, resolvable by freeing Ω_Λ (Δχ² = +0.43 at equal parameter count).

---

## 1. Introduction

The DESI collaboration's second data release [1] presents the most precise baryon acoustic oscillation measurements to date, spanning 0.3 < z < 2.3 across seven tracer populations. Combined with Type Ia supernovae (Pantheon+ [2]) and CMB calibration (Planck [3]), the data favor a time-varying dark energy equation of state over the cosmological constant at 2.8–4.2σ within standard two-parameter parameterizations.

The inferred evolution follows the Chevallier-Polarski-Linder (CPL) parameterization w(a) = w₀ + w_a(1−a) [4,5], with best-fit values suggesting w₀ ≈ −0.75 and w_a ≈ −0.86. This implies a crossing of w = −1 near z ≈ 0.5. In minimally coupled canonical single-field dark energy, crossing w = −1 is forbidden; realizing such behavior generally requires additional structure, such as noncanonical dynamics, multiple fields, interactions, or modified gravity [6,7]. Cortês and Liddle [8] flag the crossing location at the center of the observable window as a "substantial and unsettling coincidence." The DESI extended analysis [9] reports consistent phantom-crossing behavior across five additional parameterizations (BA [10], JBP [11], exponential, logarithmic, and model-free binned).

The possibility that apparent phantom crossings can arise from parameterization choice has been recognized. Linder and Huterer [12] demonstrated that the CPL form introduces systematic bias when the true w(z) lies outside its functional family. Shafieloo, Sahni, and Starobinsky [13] showed that model-dependent reconstruction can produce spurious features, including phantom crossings, when applied to models outside the fitting basis. More recently, several groups have examined whether the DESI signal specifically could reflect such artifacts [8,14].

The key question is not whether phantom crossings can be fitted to current data, but whether they are physically required, or instead arise as artifacts of the fitting template applied to a non-phantom expansion history. The present paper contributes to this discussion in two ways. First, we construct a specific one-parameter expansion history, Λcos, whose effective dark-energy sector remains non-phantom, providing a concrete, falsifiable example rather than a generic cautionary argument. The model yields H²(z)/H₀² = α(1+z)³ − β(1+z) + Ω_Λ, for which w_eff(z) > −1 follows analytically at all redshifts (§3), and which recovers the fiducial flat ΛCDM limit as its single new parameter s₀ → 0. Second, we test the template bias mechanism quantitatively: we show that CPL, BA, and JBP all produce apparent phantom crossings when fitted to Λcos distances, and we scan the full parameter range to determine the amplitude of the induced distortion at data-allowed values. At the 95% upper limit s₀ < 0.18 from a joint Pantheon+ and DESI DR2 BAO fit, the CPL recovery gives w₀ ≈ −1.02 with positive w_a, establishing the structural mechanism while falling short of the DESI best-fit amplitude and sign. The goal is not to claim that Λcos explains the full DESI preference, but to provide a controlled test case in which the size and sign of template-induced phantom behavior can be computed and confronted with current data.

The paper is organized as follows. Section 2 constructs the Λcos model from a one-parameter background ansatz and selects the clock exponent by matter-era scaling. Section 3 proves w_eff > −1 at all redshifts. Section 4 demonstrates the template bias mechanism and scans its amplitude. Section 5 presents observational constraints including prior sensitivity, Ω_Λ robustness, and CMB distance priors. Section 6 collects predictions and falsification criteria. Section 7 discusses the results.

## 2. The Λcos Model

### 2.1 Background ansatz

We construct a one-parameter deformation of the ΛCDM expansion history using a bounded auxiliary variable S ∈ (0, 1], related to redshift by 1 + z = s₀/S, where s₀ is the present-epoch value of S. Setting S = sin(t/2), where t is a phase variable advancing monotonically with cosmic time, satisfies three requirements: S is bounded above by unity, S → 0 at early times (t → 0), and the parameterization introduces exactly one new degree of freedom (s₀). We work on the monotonic branch 0 < t ≤ π, so that S = sin(t/2) increases from 0 to 1.

The redshift relation 1 + z = s₀/S reduces to the standard FLRW form a/a₀ = S/s₀ with the identification a ∝ S. The ΛCDM limit corresponds to s₀ → 0 with S/s₀ held fixed, in which the trigonometric corrections vanish and S/s₀ reduces to a conventional scale factor.

The choice of sin(t/2) over other bounded functions (e.g., tanh, logistic, or polynomial) is motivated by algebraic simplicity: the resulting H²(z) is a finite polynomial in (1+z) with coefficients determined by s₀ alone (§2.3). Alternative bounded parameterizations would generally produce transcendental or infinite-series expressions for H²(z), complicating both the analytic proof of w_eff > −1 (§3) and the comparison with standard FLRW components.

### 2.2 Clock selection

The phase variable t and proper time τ are related by a clock rate. From S = sin(t/2), the non-vacuum scaling of the expansion rate is governed by:

$$\frac{1}{S}\frac{dS}{d\tau} = \frac{\cos(t/2)}{2\sin(t/2)} \cdot \frac{dt}{d\tau}$$

This quantity is not yet the physical Hubble parameter; it defines the redshift scaling assigned to the non-vacuum sector before the cosmological constant is added (§2.3).

For a power-law clock dt/dτ = Sⁿ, the non-vacuum scaling gives (1/S)(dS/dτ) = ½ cos(t/2) Sⁿ⁻¹. The power-law form is the minimal one-parameter family relating phase and proper time; more general clocks dt/dτ = f(S) would introduce functional freedom beyond a single exponent and are not considered here. We adopt the standard Friedmann scaling H² ∝ ρ_m ∝ S⁻³ [15] as a selection criterion, requiring consistency with the observed matter-dominated expansion at high redshift. At high redshift (S → 0), cos(t/2) → 1, and the requirement (1/S)(dS/dτ) ∝ S⁻³/² selects n − 1 = −3/2, giving:

$$\frac{dt}{d\tau} = S^{-1/2} = \sin^{-1/2}(t/2)$$

With this clock, the exact non-vacuum kernel is:

$$\frac{1}{S}\frac{dS}{d\tau} = \frac{\sqrt{1 - S^2}}{2S^{3/2}}$$

The √(1−S²) factor equals unity at high z and generates the (1+z)¹ correction at low z (§2.4). For the tested integer alternatives, n = +1, 0, −1 give (1/S)(dS/dτ) ∝ (1+z)⁰, (1+z)¹, (1+z)², respectively. Only n = −1/2 gives the matter-era scaling (1+z)³/². This was verified against Pantheon+ data, where all three integer-power alternatives exceed Δχ² > 60 relative to ΛCDM [Appendix A].

### 2.3 The Hubble rate

Using 1 + z = s₀/S, we write S = s₀/(1+z). Squaring the non-vacuum kernel from §2.2 and substituting:

$$\mathcal{K}(z;\,s_0) = \frac{(1+z)^3 - s_0^2(1+z)}{1 - s_0^2}$$

where the normalization 𝒦(0; s₀) = 1 is enforced by the denominator. The cosmological constant, as a vacuum energy density independent of the expansion history, enters the Friedmann equation [15] as a separate additive component. The physical dimensionless Hubble rate is then:

$$E^2(z) \equiv \frac{H^2(z)}{H_0^2} = (1 - \Omega_\Lambda)\,\mathcal{K}(z;\,s_0) + \Omega_\Lambda$$

Ω_Λ = 0.685 is taken as a fixed reference value; §5.4 demonstrates stability of all results across the range 0.68–0.715. Expanding:

$$\frac{H^2(z)}{H_0^2} = \frac{1 - \Omega_\Lambda}{1 - s_0^2}(1+z)^3 - \frac{(1 - \Omega_\Lambda)\,s_0^2}{1 - s_0^2}(1+z) + \Omega_\Lambda$$

Defining α ≡ (1−Ω_Λ)/(1−s₀²) and β ≡ (1−Ω_Λ)s₀²/(1−s₀²), the expression reads H²/H₀² = α(1+z)³ − β(1+z) + Ω_Λ, with α − β + Ω_Λ = 1 enforcing E(0) = 1. Radiation (Ω_r ≈ 9 × 10⁻⁵) is omitted; its contribution is below 0.3% at all redshifts probed by the datasets used here (z < 2.4).

In the baseline fits, Ω_Λ is fixed to the reference value above, so the cosmological degree of freedom replacing Ω_m is s₀. The baseline Λcos and flat ΛCDM comparisons therefore use the same number of fitted parameters: s₀, H₀r_d, and M_B for Λcos; Ω_m, H₀r_d, and M_B for flat ΛCDM. The fiducial flat ΛCDM expansion history is recovered as s₀ → 0, where α → 1 − Ω_Λ and β → 0.

### 2.4 The (1+z)¹ term

The negative (1+z)¹ term is absent from the four canonical FLRW components:

| Component | Redshift scaling |
|-----------|------------------|
| Radiation | (1+z)⁴ |
| Matter | (1+z)³ |
| Curvature | (1+z)² |
| Cosmological constant | (1+z)⁰ |
| **Λcos correction** | **(1+z)¹** |

A constant-w fluid with w = −2/3 (domain walls) would produce the same redshift scaling. The Λcos term is distinguished here by the tied coefficient −β(s₀), rather than by the scaling alone. Its coefficient is −β = −(1−Ω_Λ)s₀²/(1−s₀²), strictly negative for s₀ > 0 and vanishing in the ΛCDM limit.

---

## 3. w_eff(z) > −1 at All Redshifts

To define a diagnostic effective dark energy equation of state, one must specify a matter subtraction. We adopt the split in which deviations from the fiducial matter scaling are assigned to the effective dark-energy sector, using Ω_m = 1 − Ω_Λ = 0.315 (the fiducial matter fraction, independent of s₀) rather than the dressed coefficient α = Ω_m/(1−s₀²) that appears in the (1+z)³ term.

The effective dark energy density is then:

$$X(z) = E^2(z) - \Omega_m(1+z)^3 = \frac{\Omega_m\, s_0^2}{1 - s_0^2}\left[(1+z)^3 - (1+z)\right] + \Omega_\Lambda$$

Assuming this effective component satisfies the standard continuity equation dρ_DE/dz = 3(1+w_eff)ρ_DE/(1+z), the diagnostic equation of state is:

$$w_{\rm eff}(z) = -1 + \frac{(1+z)}{3X}\frac{dX}{dz}$$

Computing the derivative:

$$\frac{dX}{dz} = \frac{\Omega_m\, s_0^2}{1 - s_0^2}\left[3(1+z)^2 - 1\right]$$

The correction to w = −1 is therefore:

$$w_{\rm eff}(z) + 1 = \frac{\Omega_m\, s_0^2\,(1+z)\left[3(1+z)^2 - 1\right]}{3(1 - s_0^2)\left[\frac{\Omega_m\, s_0^2}{1 - s_0^2}\left((1+z)^3 - (1+z)\right) + \Omega_\Lambda\right]}$$

For z ≥ 0 (corresponding to S ≤ s₀) and s₀ ∈ (0, 1):

- **Numerator:** 3(1+z)² − 1 ≥ 2 (equality at z = 0). Strictly positive.
- **Denominator:** (1+z)³ − (1+z) = (1+z)(z)(2+z) ≥ 0 for z ≥ 0, and the additive Ω_Λ > 0 ensures X(z) is strictly positive at every z.

Therefore:

$$\boxed{w_{\rm eff}(z) > -1 \quad \text{for the fiducial-matter diagnostic split, for all } z \geq 0,\; s_0 \in (0,\,1).}$$

The constraint 0 < s₀ < 1 follows from the definition s₀ = sin(t_now/2) with 0 < t_now ≤ π (§2.1). At s₀ = 0, w_eff = −1 everywhere (the fiducial flat ΛCDM limit). For s₀ > 0, the correction is positive and begins at order s₀².

The decomposition choice matters: had we instead subtracted the dressed coefficient α(1+z)³, the residual would be −β(1+z) + Ω_Λ, which is a decreasing function of z and yields a different w_eff trajectory. The motivation for the adopted diagnostic split is that Ω_m = 1 − Ω_Λ is held fixed as the fiducial matter fraction, independent of s₀. The s₀-dependent excess relative to Ω_m(1+z)³ is therefore assigned to X(z), the effective residual component whose equation of state is being diagnosed.

---

## 4. Template Bias Demonstration

### 4.1 Method

To test whether standard w(z) parameterizations can produce apparent phantom crossings from Λcos distances, we generate noise-free BAO observables (D_M/r_d, D_H/r_d, D_V/r_d) from the Λcos model at the seven DESI DR2 effective redshifts (z = 0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330), using H₀ = 67.4 km/s/Mpc and r_d = 147.1 Mpc. We then fit four w(z) parameterizations to these mock observables using the published DESI covariance structure, with Ω_m = 0.315 held fixed to match the input Λcos model, isolating the effect of the w(z) parameterization. For each effective redshift we use the same observable set and covariance block structure as the DESI DR2 compressed BAO likelihood; when multiple observables are reported at the same redshift, their published correlation coefficients are included.

The four parameterizations are CPL [4,5], Barboza-Alcaniz (BA) [10], Jassal-Bagla-Padmanabhan (JBP) [11], and a three-parameter polynomial in (1−a). Each is a standard fitting form used in the DESI extended analysis [9].

The mock exercise uses s₀ = 0.389 to maximize visibility of the effect. The template bias mechanism operates at any s₀ > 0 (see §4.3). The fits minimize χ² = ΔᵀC⁻¹Δ, where Δ is the difference between model and mock BAO observables and C is the DESI DR2 covariance matrix constructed from the published uncertainties and correlations. The χ² values reported below reflect fits to noise-free mock data with DESI covariance weighting.

### 4.2 Results

| Parameterization | Best-fit parameters | χ² | Crosses w = −1? |
|-----------------|--------------------|----|----------------|
| CPL: w₀ + w_a(1−a) | w₀ = −1.056, w_a = 0.951 | 1.0 | Yes |
| BA: w₀ + w_a a(1−a)/(a²−2a+2) | w₀ = −1.295, w_a = 3.315 | 10.8 | Yes |
| JBP: w₀ + w_a a(1−a) | w₀ = −1.226, w_a = 2.551 | 6.1 | Yes |
| Polynomial: w₀ + w₁(1−a) + w₂(1−a)² | w₀ = −0.927, w₁ = −0.162, w₂ = 1.637 | 0.2 | No |

[Figure 1: Exact Λcos w_eff(z) (solid, always > −1) overlaid with recovered w(z) from all four parameterizations. CPL, BA, and JBP dip below w = −1 at low z. The three-parameter polynomial tracks the true curve without crossing.]

Three of four parameterizations produce phantom crossings from input that satisfies w > −1 everywhere (§3). The polynomial, with one additional free parameter, does not produce a phantom crossing in this case. The effect arises from projecting the curvature of the Λcos distance-redshift relation onto a restricted two-parameter basis, absorbing the residual into phantom-crossing parameter values.

### 4.3 Threshold scan

To determine the amplitude of the template bias at data-allowed values of s₀, we repeat the CPL fit across s₀ ∈ [0.01, 0.40] in steps of 0.01. The CPL recovery produces an apparent phantom-crossing trajectory at every s₀ tested, including the smallest value s₀ = 0.01: the fitted w₀ < −1 at low redshift, with the positive w_a driving w back above −1 at higher redshift. Representative results:

| s₀ | w₀ | w_a | w₀ deviation from −1 |
|----|----|----|---------------------|
| 0.01 | −1.00007 | +0.001 | 7 × 10⁻⁵ |
| 0.06 | −1.002 | +0.021 | 0.002 |
| 0.18 | −1.022 | +0.261 | 0.022 |
| 0.39 | −1.044 | +0.928 | 0.044 |
| DESI observed | −0.75 | −0.86 | 0.25 |

[Figure 2: Recovered CPL parameters w₀ (circles) and w_a (squares) as a function of s₀. The phantom crossing (w₀ < −1) persists at every s₀ > 0. The horizontal dashed line marks w = −1.]

Two features are evident. First, the crossing persists at every s₀ > 0, confirming that the template bias is a structural property of the CPL basis applied to non-phantom models of this type, not an artifact of a particular parameter value. Second, at the SN+BAO 95% upper limit s₀ < 0.18 (§5), the induced distortion is modest: w₀ ≈ −1.02 with w_a ≈ +0.26.

### 4.4 Comparison with the DESI best fit

The DESI CPL best fit reports w₀ ≈ −0.75 and w_a ≈ −0.86. The Λcos-induced distortion at data-allowed s₀ differs in both amplitude (|w₀ + 1| = 0.02 vs 0.25, a factor of ~12) and sign (w_a = +0.26 vs −0.86). The template bias mechanism is therefore established as a structural effect, but the Λcos model at its current constraint does not reproduce the DESI best-fit parameters quantitatively. Bridging the amplitude gap would require either a larger bounded deformation (s₀ ≳ 0.4, ruled out by current data) or a different functional form for the effective dark-energy sector.

This distinction is important. The paper demonstrates that a non-phantom expansion history (Λcos) produces apparent phantom crossings under standard two-parameter templates. The claim is not that Λcos at s₀ < 0.18 explains the specific amplitude of the DESI signal.

---

## 5. Observational Constraints

### 5.1 Data

We fit jointly to the Pantheon+ supernova compilation (1701 SNe Ia with full statistical and systematic covariance [2]) and DESI DR2 BAO measurements (1 isotropic D_V/r_d at z = 0.295 and 6 anisotropic D_M/r_d, D_H/r_d pairs at z = 0.51–2.33, with published cross-correlations [1]). The total dataset comprises 1714 observables (1701 supernova magnitudes and 13 BAO measurements).

The supernova likelihood is χ²_SN = ΔᵀC⁻¹Δ, where Δᵢ = m_{b,i} − M_B − μ(zᵢ) and C is the 1701 × 1701 covariance matrix. The BAO likelihood is constructed from the published uncertainties and inter-observable correlations at each redshift bin, with bins treated as independent. The total likelihood is χ² = χ²_SN + χ²_BAO.

### 5.2 Primary fit: SN+BAO

MCMC sampling uses an affine-invariant ensemble sampler (32 walkers, 5000 steps, 1000 burn-in). Convergence is confirmed via integrated autocorrelation time (τ < 50 for all parameters in both models).

Flat ΛCDM free parameters: Ω_m, H₀r_d, M_B.
Λcos free parameters: s₀, H₀r_d, M_B (with Ω_Λ = 0.685 fixed).
Both models have three free parameters. The primary results are reported at the fixed reference value Ω_Λ = 0.685; §5.4 demonstrates stability of the s₀ constraint across the range 0.68–0.715, and §5.5 confirms the model remains competitive when Ω_Λ is freed entirely (Δχ² = +0.43 at equal parameter count).

| | Flat ΛCDM | Λcos |
|-|-----------|------|
| **Primary parameter** | Ω_m = 0.312 [0.304, 0.321] | s₀ = 0.075 [0.024, 0.143] |
| **H₀r_d (km/s)** | 10046 [9978, 10113] | 10010 [9973, 10041] |
| **M_B** | −19.355 [−19.359, −19.350] | −19.353 [−19.357, −19.350] |
| **χ²_min** | 1772.4 | 1772.6 |
| **χ²_SN / χ²_BAO** | 1759.9 / 12.6 | 1759.0 / 13.5 |

Uncertainties are posterior median and 68% credible intervals. The Λcos best-fit sits at s₀ = 0.001 (the numerical lower bound of the prior; the analytic ΛCDM limit is s₀ = 0). The posterior median of 0.075 reflects prior volume at s₀ > 0. The 95th percentile gives:

$$s_0 < 0.18 \quad (95\% \text{ CL, flat prior}).$$

The Δχ² = +0.13 at equal parameter count corresponds to ΔAIC = ΔBIC = +0.13: no preference for either model.

[Figure 3: Corner plot of the Λcos posterior in (s₀, H₀r_d, M_B) space from the SN+BAO fit.]

[Figure 4: Pantheon+ binned residuals (μ_data − μ_model) for ΛCDM and Λcos at joint best-fit parameters. The two models are indistinguishable.]

### 5.3 Prior sensitivity

Since the Λcos posterior is concentrated near the lower prior boundary, the 95% upper limit is prior-sensitive. We test two alternative priors by reweighting the baseline chain:

| Prior on s₀ | s₀ median | s₀ 95% UL | χ²_min |
|-------------|-----------|-----------|--------|
| Flat s₀ ∈ [0.001, 0.99] (baseline) | 0.075 | 0.184 | 1772.6 |
| Flat in s₀² (more weight at larger s₀) | 0.118 | 0.211 | 1772.6 |
| Flat in log₁₀(s₀) (scale-invariant) | 0.012 | 0.119 | 1772.6 |

The χ²_min is identical across all three priors (the likelihood is unchanged; only the posterior weighting differs). The 95% upper limit ranges from 0.12 to 0.21, a factor of ~1.8. The constraint is prior-sensitive in detail but data-driven in character: all three priors yield s₀ ≪ 1.

### 5.4 Ω_Λ sensitivity

The primary fit uses Ω_Λ = 0.685 as a fixed reference value. To test robustness, we repeat the SN+BAO fit at four alternative values spanning the range between the SN+BAO-preferred and CMB-preferred regions:

| Ω_Λ | s₀ median | s₀ 95% UL | Δχ² vs ΛCDM |
|-----|-----------|-----------|-------------|
| 0.680 | 0.064 | 0.163 | +0.78 |
| 0.685 (baseline) | 0.075 | 0.184 | +0.13 |
| 0.690 | 0.088 | 0.204 | +0.04 |
| 0.700 | 0.149 | 0.262 | +0.93 |
| 0.715 (CMB-preferred) | 0.277 | 0.348 | +2.39 |

The s₀ constraint varies smoothly with Ω_Λ, with the 95% upper limit ranging from 0.16 to 0.35 across the tested interval. The best Δχ² occurs near Ω_Λ = 0.69. At the CMB-preferred value Ω_Λ = 0.715, the best-fit s₀ shifts to 0.288 (nonzero) and the model is mildly disfavored (Δχ² = +2.39). The results are stable across the tested range; no fine-tuning of Ω_Λ is required.

### 5.5 CMB distance priors

The DESI DR2 phantom-crossing result was obtained jointly with Planck CMB data. To test whether Λcos is compatible with CMB constraints, we add compressed Planck 2018 distance priors (shift parameter R = 1.7502 ± 0.0046, acoustic scale l_A = 301.47 ± 0.09, treated as independent Gaussians) to the SN+BAO likelihood. These quantities constrain the integral ∫dz/E(z) to the last-scattering surface at z* = 1090. Radiation (Ω_r = 9.15 × 10⁻⁵) is included for this integral. Non-flat ΛCDM includes a curvature term Ω_k = 1 − Ω_m − Ω_Λ. Since the Planck distance priors are derived within a restricted background model space, their use here should be understood as a consistency diagnostic rather than a full CMB likelihood evaluation.

The four-parameter Λcos fit with Ω_Λ free and the four-parameter non-flat ΛCDM fit provide the primary comparison:

| | Λcos (Ω_Λ free) | Non-flat ΛCDM |
|-|------------------|---------------|
| **Free params** | s₀, Ω_Λ, H₀r_d, M_B | Ω_m, Ω_Λ, H₀r_d, M_B |
| **Best-fit Ω_Λ** | 0.715 [0.711, 0.718] | 0.722 |
| **χ²_min** | 1817.8 | 1817.3 |
| **Δχ²** | +0.43 | 0 (reference) |

The two models are indistinguishable at Δχ² = +0.43 with the same parameter count.

For comparison, fixing Ω_Λ = 0.685 introduces a penalty of Δχ² = +67.9 relative to flat ΛCDM (3 parameters each). This tension is driven by the BAO sector (χ²_BAO = 125 vs 31), not by the CMB priors themselves (χ²_CMB = 1.4 for Λcos vs 16.2 for ΛCDM). The effect is not specific to Λcos: adding CMB priors shifts the preferred Ω_Λ from 0.685–0.688 (SN+BAO) to ~0.715 in both ΛCDM and Λcos. Flat ΛCDM absorbs the shift through Ω_m (which moves from 0.312 to 0.285). Λcos at fixed Ω_Λ cannot absorb it. The shift from Ω_Λ ≈ 0.685 to Ω_Λ ≈ 0.715 should therefore be interpreted as a background-distance consistency issue in the compressed-prior setup, rather than as a failure mode unique to Λcos.

The compressed-prior test used here is an approximate background-level consistency check, not a substitute for the full correlated Planck likelihood.

### 5.6 Parameter accounting

The matter fraction in Λcos is set through Ω_m = 1 − Ω_Λ at the chosen reference value. The (1+z)³ coefficient α = Ω_m/(1−s₀²) is a dressed version of this input. As a consistency check: at any s₀, α(1 − s₀²) returns Ω_m = 0.315. The dressing is algebraically self-consistent and does not introduce additional freedom.

### 5.7 Model comparison

To contextualize the Λcos result, we compare against wCDM (constant w as a free parameter, 4 free parameters: Ω_m, w, H₀r_d, M_B) fitted to the same SN+BAO dataset:

| Model | Free params | χ²_min | Δχ² | ΔAIC | ΔBIC |
|-------|-----------|--------|-----|------|------|
| Flat ΛCDM | 3 | 1772.4 | 0 | 0 | 0 |
| Λcos (Ω_Λ = 0.685) | 3 | 1772.6 | +0.13 | +0.13 | +0.13 |
| Λcos (Ω_Λ = 0.715) | 3 | 1774.8 | +2.39 | +2.39 | +2.39 |
| wCDM | 4 | 1759.4 | −13.0 | −11.0 | −5.6 |

The wCDM fit yields w = −0.854 [−0.91, −0.80] (68% CI), preferring a quintessence-like (w > −1) departure from ΛCDM at ΔAIC = −11.0. This is the same qualitative signal underlying the DESI phantom-crossing result: the SN+BAO data favor some departure from w = −1. The distinction is that wCDM captures this as a constant shift toward w > −1, while CPL projects it into a crossing through w = −1. The Λcos model, for which w_eff > −1 at all redshifts (§3), is consistent with the wCDM direction but does not achieve the same χ² improvement because the data-allowed s₀ is too small to produce a detectable departure.

For the baseline flat prior in s₀, a Savage-Dickey density ratio at s₀ = 0 gives B₀₁ = 6.8 (stable across KDE bandwidths from 6.7 to 6.8), corresponding to moderate evidence for ΛCDM over Λcos on the Jeffreys scale. This Bayes factor should be interpreted conditional on the baseline prior choice. The result confirms the Δχ² finding: current data do not require the ansatz's correction term.

---

## 6. Predictions and Falsification Criteria

### 6.1 The (1+z)¹ signature

The joint SN+BAO fit constrains |β| < 0.011 at 95% CL (from s₀ < 0.18 with Ω_m = 0.315). The predicted fractional contribution to H²(z) at z = 1 is:

$$\frac{|\beta|(1+z)}{E^2(z)} < 0.7\% \quad (95\% \text{ CL at } z = 1).$$

This is below the per-bin precision of current BAO measurements (~2–3%) but potentially within reach of next-generation BAO measurements at the ~1% level across z = 0.9–1.8 [16]. A statistically significant detection of a negative (1+z)¹ component in H²(z) would constitute evidence for a non-standard contribution to the expansion history. While a domain-wall fluid (w = −2/3) produces the same scaling, the Λcos term is distinguished by the tied coefficient −β(s₀) rather than by an independent energy density.

### 6.2 Falsification criteria

| Observable | Λcos prediction | Falsified if |
|-----------|----------------|-------------|
| (1+z)¹ coefficient in H² | Non-positive, with magnitude tied to s₀ | A positive coefficient is robustly detected, or a negative coefficient is measured with magnitude inconsistent with the fitted s₀ relation |
| Diagnostic w_eff(z) | > −1 for the fiducial-matter split at any s₀ > 0 | The same split robustly requires w_eff < −1 at ≥ 2σ |
| ΛCDM limit | s₀ = 0 recovers fiducial flat ΛCDM exactly | No additional test required |

---

## 7. Discussion

### 7.1 Template bias

The central result of this paper is that a non-phantom expansion history can produce apparent phantom crossings when fitted with standard two-parameter w(z) templates. We have demonstrated this explicitly for CPL, BA, and JBP parameterizations applied to Λcos distances: all three recover w₀ < −1 from Λcos distances for which w_eff > −1 at every redshift under the fiducial-matter diagnostic split (§3). A three-parameter polynomial does not produce the crossing, confirming that the effect arises from basis restriction rather than from the underlying expansion history.

This finding has precedent. Linder and Huterer [12] identified CPL template bias, Shafieloo, Sahni, and Starobinsky [13] demonstrated spurious phantom crossings from model-dependent reconstruction, and recent work [8,14] has raised similar concerns about the DESI signal specifically. The present contribution is to provide a concrete one-parameter non-phantom model (rather than a generic cautionary argument), to test multiple parameterizations, and to scan the template bias amplitude across the full parameter range allowed by current data.

The DESI extended analysis [9] itself tests five parameterizations beyond CPL and finds consistent phantom-crossing behavior across all of them. This might seem to rule out template bias as an explanation. However, the DESI analysis fits each parameterization to real data, which may contain a genuine departure from ΛCDM (as the wCDM comparison in §5.7 suggests). The mock exercise in §4 asks a different question: can a model that provably satisfies w > −1 produce phantom crossings across the same family of templates? The answer is yes, confirming that template agreement across parameterizations is necessary but not sufficient evidence for a true crossing.

At data-allowed values (s₀ < 0.18), the induced CPL distortion is w₀ ≈ −1.02 with positive w_a, structurally present but modest in amplitude and opposite in sign to the DESI best fit (w₀ ≈ −0.75, w_a ≈ −0.86). The paper establishes the mechanism without claiming to reproduce the DESI signal quantitatively.

### 7.2 Status of Λcos

The Λcos model rests on three inputs: a bounded auxiliary variable S = sin(t/2) with redshift relation 1 + z = s₀/S (§2.1), the power-law clock rate dt/dτ = S⁻¹/² selected by matter-era asymptotic scaling (§2.2), and a fixed reference value Ω_Λ = 0.685 (§2.3). The resulting H²(z) is derived algebraically from these inputs. The fiducial flat ΛCDM expansion history is recovered as s₀ → 0.

The present analysis constrains only background observables (distances and expansion rates). The Λcos modification to H(z) also affects the linear growth rate f(z)σ₈(z), which provides an independent test. However, predicting growth requires specifying the perturbation-level sound speed of the effective dark energy component, which the background ansatz does not constrain. A comparison with redshift-space distortion data (e.g., fσ₈ from DESI or earlier surveys) is deferred to future work.

Current combined data (Pantheon+ and DESI DR2 BAO) constrain s₀ < 0.18 at 95% CL, consistent with the ΛCDM limit. Λcos matches ΛCDM at Δχ² = +0.13 across the SN+BAO dataset. Adding compressed Planck distance priors shifts the preferred Ω_Λ, a background-distance consistency issue that is removed when Ω_Λ is freed (Δχ² = +0.43 at equal parameter count). The model is a minimal one-parameter deformation of the fiducial flat ΛCDM expansion history, with a specific falsifiable signature (the negative (1+z)¹ term) testable by next-generation BAO measurements.

---

## 8. Conclusions

A non-phantom expansion history can produce apparent phantom crossings under standard two-parameter templates. The Λcos model, constructed as a one-parameter deformation of the fiducial flat ΛCDM expansion history using a bounded auxiliary variable, provides a concrete realization for which w_eff(z) > −1 at all redshifts under the fiducial-matter diagnostic split, while matching the Pantheon+ and DESI DR2 BAO distance-redshift relation at Δχ² = +0.13 relative to flat ΛCDM. Current data constrain the model's single new parameter to s₀ < 0.18 at 95% confidence, and the predicted negative (1+z)¹ contribution to H²(z) is a target for next-generation BAO measurements.

---

## Data and Code Availability

The MCMC chains, analysis scripts, and figure-generation code that reproduce all results in this paper are publicly available at [github.com/dmobius3/lambda-cos](https://github.com/dmobius3/lambda-cos) and archived at Zenodo ([DOI:10.5281/zenodo.19798852](https://doi.org/10.5281/zenodo.19798852)). The Pantheon+ supernova compilation [2] is available at [pantheonplussh0es.github.io](https://pantheonplussh0es.github.io/) and the DESI DR2 BAO measurements [1] at [data.desi.lbl.gov](https://data.desi.lbl.gov/).

---

## Appendix A: Clock Exponent Selection

Three alternative clock rates were tested against the joint Pantheon+ + DESI DR2 BAO dataset using the same MCMC setup as the primary Λcos fit (§5.2): identical priors on H₀r_d and M_B, identical sampler configuration, identical likelihood construction.

| Model | n | High-z scaling | Best-fit s₀ | H₀r_d (km/s) | χ²_SN | χ²_BAO | χ²_total | Δχ² vs ΛCDM |
|---|---|---|---|---|---|---|---|---|
| A (proper time) | 0 | (1+z)¹ | 0.823 | 9280 | 1814.8 | 176.4 | 1991.2 | +218.8 |
| B (conformal) | −1 | (1+z)² | 0.001* | 8555 | 1834.5 | 1759.9 | 3594.4 | +1822.0 |
| C (symmetric) | +1 | (1+z)⁰ | 0.962 | 9219 | 2737.6 | 6311.5 | 9049.1 | +7276.7 |
| **D (Λcos)** | **−1/2** | **(1+z)³/²** | **0.001†** | **10010** | **1759.0** | **13.5** | **1772.6** | **+0.13** |
| ΛCDM (baseline) | — | — | (Ω_m = 0.312) | 10046 | 1759.9 | 12.6 | 1772.4 | 0 |

*Model B saturates at the s₀ prior floor. The likelihood is monotonic toward s₀ → 0 under the (1+z)² scaling, so the reported value reflects the boundary, not a posterior peak.

†For Λcos, the likelihood maximum lies at the numerical prior floor s₀ = 0.001; the posterior median is 0.075, as reported in §5.2.

Acceptance fractions: A 0.71, B 0.69, C 0.72; all chains converged with stable autocorrelation times.

Each integer alternative fails for a distinct reason. Model A's (1+z)¹ scaling is too soft to reproduce matter dilution; the supernova sector tolerates this within Δχ²_SN ≈ 55, but the BAO sector adds a 164 penalty as the high-redshift bins (z = 1.32, 1.48, 2.33) reject the soft scaling. Model B saturates against the s₀ floor because the (1+z)² scaling offers no improvement over ΛCDM at any positive s₀; the BAO sector dominates the rejection at Δχ²_BAO ≈ 1747. Model C's (1+z)⁰ scaling at high redshift is the most dramatic failure: with no decay of the matter-like term, both sectors reject the model (Δχ²_SN ≈ 980, Δχ²_BAO ≈ 6300).

Within the power-law clock family, the exponent n = −1/2 is selected analytically by three-dimensional matter dilution (ρ_m ∝ S⁻³) through the Friedmann square root, giving the non-vacuum scaling 𝒦¹/² ∝ S⁻³/² at high z and the exact two-term non-vacuum kernel of §2.3 at all z. The empirical fits confirm the analytic selection: among the alternatives tested, only n = −1/2 is viable.

---

## References

[1] DESI Collaboration, arXiv:2503.14738 (2025).

[2] D. Brout et al., Astrophys. J. 938, 110 (2022).

[3] Planck Collaboration VI, Astron. Astrophys. 641, A6 (2020).

[4] M. Chevallier and D. Polarski, Int. J. Mod. Phys. D 10, 213 (2001).

[5] E. V. Linder, Phys. Rev. Lett. 90, 091301 (2003).

[6] A. Vikman, Phys. Rev. D 71, 023515 (2005).

[7] Y.-F. Cai, E. N. Saridakis, M. R. Setare, and J.-Q. Xia, Phys. Rep. 493, 1 (2010).

[8] M. Cortês and A. R. Liddle, arXiv:2504.15336 (2025).

[9] DESI Collaboration, arXiv:2503.14743 (2025).

[10] E. J. Barboza and J. S. Alcaniz, Phys. Lett. B 666, 250 (2008).

[11] H. K. Jassal, J. S. Bagla, and T. Padmanabhan, Mon. Not. R. Astron. Soc. 356, L11 (2005).

[12] E. V. Linder and D. Huterer, Phys. Rev. D 72, 043509 (2005).

[13] A. Shafieloo, V. Sahni, and A. A. Starobinsky, Phys. Rev. D 80, 101301 (2009).

[14] R. E. Keeley, A. Shafieloo, and W. L. Matthewson, arXiv:2506.15091 (2025).

[15] S. Weinberg, *Gravitation and Cosmology* (Wiley, New York, 1972).

[16] Euclid Collaboration, Astron. Astrophys. 662, A112 (2022).

---

/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`working`](../)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
