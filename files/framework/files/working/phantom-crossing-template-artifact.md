/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /

---

# Phantom Crossing as Template Artifact: The Λcos Distance-Redshift Model from Bounded Topology

**B. Shatto**
Independent Researcher, St. Petersburg, FL, USA
bshatto.pe@gmail.com

---

## Abstract

DESI DR2 reports 2.8–4.2σ evidence that the dark energy equation of state w evolves with redshift, including an apparent phantom crossing through w = −1. We show that bounded dark energy sectors (finite departures from Λ) produce apparent phantom crossings under standard two-parameter templates. We derive a specific realization (Λcos) from a temporal budget identity on S³ and constrain it with Pantheon+ and DESI DR2 BAO. At data-allowed parameter values, the induced CPL distortion is structurally present but modest (w₀ ≈ −1.02) and of opposite sign in w_a, establishing the mechanism without reproducing the DESI best-fit amplitude.

The Λcos model yields H²(z)/H₀² = α(1+z)³ − β(1+z) + Ω_Λ, where α and β are determined by a single parameter s₀ = sin(t_now/2) and the cosmological constant Ω_Λ = 0.685 is taken as input from a companion topological analysis. The model satisfies w_eff(z) > −1 at all redshifts, recovers ΛCDM exactly as s₀ → 0, and predicts a novel negative (1+z)¹ term in H² absent from the four canonical FLRW components. A joint MCMC fit to Pantheon+ (1701 SNe Ia) and DESI DR2 BAO (13 data points) yields Δχ² = +0.13 relative to flat ΛCDM at the same parameter count, with s₀ < 0.18 (95% CL, flat prior). The constraint is robust across prior choices (s₀ < 0.12–0.21) and Ω_Λ variations (0.68–0.70). Adding compressed Planck distance priors introduces a shared Ω_Λ tension common to both ΛCDM and Λcos, resolvable by freeing Ω_Λ (Δχ² = +0.43).

---

## 1. Introduction

The DESI collaboration's second data release [1] presents the most precise baryon acoustic oscillation measurements to date, spanning 0.3 < z < 2.3 across seven tracer populations. Combined with Type Ia supernovae (Pantheon+ [2]) and CMB calibration (Planck [3]), the data favor a time-varying dark energy equation of state over the cosmological constant at 2.8–4.2σ within standard two-parameter parameterizations.

The inferred evolution follows the Chevallier-Polarski-Linder (CPL) parameterization w(a) = w₀ + w_a(1−a) [4,5], with best-fit values suggesting w₀ ≈ −0.75 and w_a ≈ −0.86. This implies a phantom crossing through w = −1 near z ≈ 0.5, a transition requiring negative kinetic energy or coupled ghost fields in single-field models [6,7]. Cortês and Liddle [8] flag the crossing location at the center of the observable window as a "substantial and unsettling coincidence." The DESI extended analysis [9] reports consistent phantom-crossing behavior across five additional parameterizations (BA [10], JBP [11], exponential, logarithmic, and model-free binned).

The possibility that apparent phantom crossings can arise from parameterization choice has been recognized. Linder and Huterer [12] demonstrated that the CPL form introduces systematic bias when the true w(z) lies outside its functional family. Shafieloo, Sahni, and Starobinsky [13] showed that model-dependent reconstruction can produce spurious features, including phantom crossings, when applied to models outside the fitting basis. More recently, several groups have examined whether the DESI signal specifically could reflect such artifacts [8,14].

The key question is not whether phantom crossings can be fitted to current data, but whether they are physically required, or instead arise as artifacts of the fitting template applied to a bounded expansion history. The present paper contributes to this discussion in two ways. First, we derive a specific bounded dark energy sector from a temporal budget identity on S³ (the Λcos model), providing a concrete, falsifiable example rather than a generic cautionary argument. The model yields H²(z)/H₀² = α(1+z)³ − β(1+z) + Ω_Λ, satisfies w_eff(z) > −1 at all redshifts by construction, and recovers ΛCDM exactly as its single new parameter s₀ → 0. Second, we test the template bias mechanism quantitatively: we show that CPL, BA, and JBP all produce apparent phantom crossings when fitted to Λcos distances, and we scan the full parameter range to determine the amplitude of the induced distortion at data-allowed values. At the 95% upper limit s₀ < 0.18 from a joint Pantheon+ and DESI DR2 BAO fit, the CPL recovery gives w₀ ≈ −1.02 with positive w_a, establishing the structural mechanism while falling short of the DESI best-fit amplitude and sign.

The paper is organized as follows. Section 2 derives the Λcos model from the budget identity and the budget clock. Section 3 proves w_eff > −1 at all redshifts. Section 4 demonstrates the template bias mechanism and scans its amplitude. Section 5 presents observational constraints including prior sensitivity, Ω_Λ robustness, and CMB distance priors. Section 6 collects predictions. Section 7 discusses the results.

## 2. The Λcos Model

### 2.1 The budget identity

On a closed three-sphere S³ with a non-orientable identification (Möbius-type boundary condition), anti-periodic boundary conditions require ψ(t + 2π) = −ψ(t), selecting half-integer harmonics [15]. The ground state satisfying ψ(0) = +1 (maximum amplitude at the initial epoch) and dψ/dt|₀ = 0 (standing wave) is Ψ = cos(t/2), with period 4π. A companion spatial budget identity u₀² + J² = 1 is established on this surface [16]; we propose the temporal direction carries the same structure:

$$\Psi^2 + S^2 = 1, \qquad \Psi = \cos(t/2), \qquad S = \sin(t/2)$$

where S is the modal realization amplitude: the fraction of the standing wave expressed as resolvable structure at phase t. At t = 0, Ψ = 1 and S = 0 (full wave, nothing realized). As phase advances, wave amplitude trades into realization. S plays the role of a normalized scale factor, with the redshift relation 1 + z = s₀/S, where s₀ = S(t_now) is the present-epoch value.

The identity Ψ² + S² = 1 is the Pythagorean theorem on the phase circle; its mathematical content is trivial. The physical content resides in the proposal that S = sin(t/2) governs the expansion history, with the identity acting as a constraint that couples wave amplitude to realization at every epoch.

### 2.2 The budget clock

The budget phase t and proper time τ are related by a clock rate. From S = sin(t/2), the Hubble parameter is:

$$H = \frac{1}{S}\frac{dS}{d\tau} = \frac{\cos(t/2)}{2\sin(t/2)} \cdot \frac{dt}{d\tau}$$

For a power-law clock dt/dτ = Sⁿ, this gives H = cos(t/2) · Sⁿ⁻¹/2. We adopt the standard Friedmann scaling H² ∝ ρ_m ∝ S⁻³ [18] as a selection criterion, requiring consistency with the observed matter-dominated expansion at high redshift. At high redshift (S → 0), cos(t/2) → 1, and the requirement H ∝ S⁻³/² selects n − 1 = −3/2, giving:

$$\frac{dt}{d\tau} = S^{-1/2} = \sin^{-1/2}(t/2)$$

With this clock, the exact Hubble rate at all redshifts is:

$$H = \frac{\sqrt{1 - S^2}}{2S^{3/2}}$$

The cos(t/2) = √(1−S²) factor equals unity at high z and generates the (1+z)¹ correction at low z (§2.4). The exponent −1/2 is the only power-law choice among the integer and half-integer alternatives tested that reproduces the matter-era scaling: integer exponents (0, −1, +1) produce H ∝ (1+z)⁰, (1+z)², or (1+z)¹ at high z. Only −1/2 gives the (1+z)³/² scaling that matter domination requires. This was verified against Pantheon+ data, where all three integer-power alternatives exceed Δχ² > 60 relative to ΛCDM [Appendix A].

The ratio 3/2 appearing in the scaling exponent numerically matches the Gauss-Codazzi conversion Λ_obs = (3/2)Λ_top between surface curvature and spatial curvature on S³ [16,17].

### 2.3 The Hubble rate

Using 1 + z = s₀/S, we write S = s₀/(1+z). Substituting into the matter-sector Hubble rate H² = (1−S²)/(4S³):

$$H^2 = \frac{1 - s_0^2/(1+z)^2}{4\,s_0^3/(1+z)^3} = \frac{(1+z)^3 - s_0^2(1+z)}{4s_0^3}$$

Normalizing to H₀ at z = 0 gives H₀² = (1−s₀²)/(4s₀³), so:

$$\frac{H^2}{H_0^2} = \frac{(1+z)^3 - s_0^2(1+z)}{1 - s_0^2}$$

The cosmological constant enters the Friedmann equation additively as a separate constant component, with Ω_Λ = 0.685 taken as input from a companion topological analysis, derived independently of CMB data [16]. Scaling the matter sector to (1 − Ω_Λ) at z = 0:

$$\frac{H^2(z)}{H_0^2} = \frac{1 - \Omega_\Lambda}{1 - s_0^2}(1+z)^3 - \frac{(1 - \Omega_\Lambda)\,s_0^2}{1 - s_0^2}(1+z) + \Omega_\Lambda$$

Defining α ≡ (1−Ω_Λ)/(1−s₀²) and β ≡ (1−Ω_Λ)s₀²/(1−s₀²), the expression reads H²/H₀² = α(1+z)³ − β(1+z) + Ω_Λ, with α − β + Ω_Λ = 1 enforcing E(0) = 1. Radiation (Ω_r ≈ 9 × 10⁻⁵) is omitted; its contribution is below 0.3% at all redshifts probed by the datasets used here (z < 2.4).

The model has two free parameters: s₀ and H₀ (or equivalently s₀ and M_B in supernova fits), the same count as flat ΛCDM (Ω_m, H₀). ΛCDM is recovered exactly as s₀ → 0, where α → 1 − Ω_Λ = Ω_m and β → 0.

### 2.4 The (1+z)¹ term

The negative (1+z)¹ term is absent from the four canonical FLRW components:

| Component | Redshift scaling |
|-----------|-----------------|
| Radiation | (1+z)⁴ |
| Matter | (1+z)³ |
| Curvature | (1+z)² |
| Cosmological constant | (1+z)⁰ |
| **Λcos budget term** | **(1+z)¹** |

A constant-w fluid with w = −2/3 (domain walls) would produce the same redshift scaling. The Λcos term is distinguished by its origin: it arises from the bounded realization constraint S ≤ 1, with coefficient −β tied to s₀ through the budget identity, rather than from an independent fluid component. Its coefficient is −β = −(1−Ω_Λ)s₀²/(1−s₀²), strictly negative for s₀ > 0 and vanishing in the ΛCDM limit.

## 3. w_eff(z) > −1 at All Redshifts

To define an effective dark energy equation of state, we must choose how to split H²(z) into matter and dark energy contributions. We adopt the split in which the budget-induced dressing is attributed to the dark energy sector, using the physical matter density Ω_m = 1 − Ω_Λ = 0.315 (the topology-determined matter fraction, independent of s₀) rather than the dressed coefficient α = Ω_m/(1−s₀²) that appears in the (1+z)³ term.

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

$$\boxed{w_{\rm eff}(z) > -1 \quad \text{at all } z \geq 0, \quad \text{for any } s_0 \in (0,\,1).}$$

The constraint 0 < s₀ < 1 follows from the definition s₀ = sin(t_now/2) with t_now > 0. At s₀ = 0, w_eff = −1 everywhere (ΛCDM). For s₀ > 0, the dark energy density receives a positive correction from the budget identity, lifting w above −1 by an amount proportional to s₀².

The decomposition choice matters: had we instead subtracted the dressed coefficient α(1+z)³, the residual would be −β(1+z) + Ω_Λ, which is a decreasing function of z and yields a different w_eff trajectory. The physical motivation for the adopted split is that Ω_m = 1 − Ω_Λ is the topology-determined matter fraction, independent of s₀, while the dressing factor 1/(1−s₀²) is a property of the budget identity acting on the dark energy sector.

## 4. Template Bias Demonstration

### 4.1 Method

To test whether standard w(z) parameterizations can produce apparent phantom crossings from Λcos distances, we generate noise-free BAO observables (D_M/r_d, D_H/r_d, D_V/r_d) from the Λcos model at the seven DESI DR2 effective redshifts (z = 0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330), using H₀ = 67.4 km/s/Mpc and r_d = 147.1 Mpc. We then fit four w(z) parameterizations to these mock observables using the published DESI covariance structure, with Ω_m = 0.315 held fixed to match the input Λcos model, isolating the effect of the w(z) parameterization.

The four parameterizations are CPL [4,5], Barboza-Alcaniz (BA) [10], Jassal-Bagla-Padmanabhan (JBP) [11], and a three-parameter polynomial in (1−a). Each is a standard fitting form used in the DESI extended analysis [9].

The mock exercise uses s₀ = 0.389 to maximize visibility of the effect. The template bias mechanism operates at any s₀ > 0 (see §4.3). The fits minimize χ² = ΔᵀC⁻¹Δ, where Δ is the difference between model and mock BAO observables and C is the DESI DR2 covariance matrix constructed from the published uncertainties and correlations. The χ² values reported below reflect fits to noise-free mock data with DESI covariance weighting.

### 4.2 Results

| Parameterization | Best-fit parameters | χ² | Crosses w = −1? |
|-----------------|--------------------|----|----------------|
| CPL: w₀ + w_a(1−a) | w₀ = −1.056, w_a = 0.951 | 1.0 | Yes |
| BA: w₀ + w_a a(1−a)/(a²−2a+2) | w₀ = −1.295, w_a = 3.315 | 10.8 | Yes |
| JBP: w₀ + w_a a(1−a) | w₀ = −1.226, w_a = 2.551 | 6.1 | Yes |
| Polynomial: w₀ + w₁(1−a) + w₂(1−a)² | w₀ = −0.927, w₁ = −0.162, w₂ = 1.637 | 0.2 | No |

[**Figure 1**: Exact Λcos w_eff(z) (solid, always > −1) overlaid with recovered w(z) from all four parameterizations. CPL, BA, and JBP dip below w = −1 at low z. The three-parameter polynomial tracks the true curve without crossing.]

Three of four parameterizations produce phantom crossings from input that satisfies w > −1 everywhere (§3). The polynomial, with one additional free parameter, does not produce a phantom crossing in this case. The effect arises from projecting the curvature of a bounded function onto a restricted two-parameter basis, absorbing the residual into phantom-crossing parameter values.

### 4.3 Threshold scan

To determine the amplitude of the template bias at data-allowed values of s₀, we repeat the CPL fit across s₀ ∈ [0.01, 0.40] in steps of 0.01. The CPL recovery produces a formal phantom crossing (w₀ < −1) at every s₀ tested, including the smallest value s₀ = 0.01. Representative results:

| s₀ | w₀ | w_a | w₀ deviation from −1 |
|----|----|----|---------------------|
| 0.01 | −1.00007 | +0.001 | 7 × 10⁻⁵ |
| 0.06 | −1.002 | +0.021 | 0.002 |
| 0.18 | −1.022 | +0.261 | 0.022 |
| 0.39 | −1.044 | +0.928 | 0.044 |
| DESI observed | −0.75 | −0.86 | 0.25 |

[**Figure 2**: Recovered CPL parameters w₀ (circles) and w_a (squares) as a function of s₀. The phantom crossing (w₀ < −1) persists at every s₀ > 0. The horizontal dashed line marks w = −1.]

Two features are evident. First, the crossing persists at every s₀ > 0, confirming that the template bias is a structural property of the CPL basis applied to bounded models, not an artifact of a particular parameter value. Second, at the SN+BAO 95% upper limit s₀ < 0.18 (§5), the induced distortion is modest: w₀ ≈ −1.02 with w_a ≈ +0.26.

### 4.4 Comparison with the DESI best fit

The DESI CPL best fit reports w₀ ≈ −0.75 and w_a ≈ −0.86. The Λcos-induced distortion at data-allowed s₀ differs in both amplitude (|w₀ + 1| = 0.02 vs 0.25) and sign (w_a positive vs negative). The template bias mechanism is therefore established as a structural effect, but the Λcos model at its current constraint does not reproduce the DESI best-fit parameters quantitatively.

This distinction is important. The paper's claim is that bounded dark energy sectors generically produce apparent phantom crossings under standard two-parameter templates, and Λcos provides a concrete, falsifiable example. The claim is not that Λcos at s₀ < 0.18 explains the specific amplitude of the DESI signal.

## 5. Observational Constraints

### 5.1 Data

We fit jointly to the Pantheon+ supernova compilation (1701 SNe Ia with full statistical and systematic covariance [2]) and DESI DR2 BAO measurements (1 isotropic D_V/r_d at z = 0.295 and 6 anisotropic D_M/r_d, D_H/r_d pairs at z = 0.51–2.33, with published cross-correlations [1]). The total dataset comprises 1714 observables (1701 supernova magnitudes and 13 BAO measurements).

The supernova likelihood is χ²_SN = ΔᵀC⁻¹Δ, where Δᵢ = m_{b,i} − M_B − μ(zᵢ) and C is the 1701 × 1701 covariance matrix. The BAO likelihood is constructed from the published uncertainties and inter-observable correlations at each redshift bin, with bins treated as independent. The total likelihood is χ² = χ²_SN + χ²_BAO.

### 5.2 Primary fit: SN+BAO

MCMC sampling uses an affine-invariant ensemble sampler (32 walkers, 5000 steps, 1000 burn-in). Convergence is confirmed via integrated autocorrelation time (τ < 50 for all parameters in both models).

Flat ΛCDM free parameters: Ω_m, H₀r_d, M_B.
Λcos free parameters: s₀, H₀r_d, M_B (with Ω_Λ = 0.685 fixed).
Both models have three free parameters.

| | Flat ΛCDM | Λcos |
|-|-----------|------|
| **Primary parameter** | Ω_m = 0.312 [0.304, 0.321] | s₀ = 0.075 [0.024, 0.143] |
| **H₀r_d (km/s)** | 10046 [9978, 10113] | 10010 [9973, 10041] |
| **M_B** | −19.355 [−19.359, −19.350] | −19.353 [−19.357, −19.350] |
| **χ²_min** | 1772.4 | 1772.6 |
| **χ²_SN / χ²_BAO** | 1759.9 / 12.6 | 1759.0 / 13.5 |

Uncertainties are posterior median and 68% credible intervals. The Λcos best-fit sits at s₀ = 0.001 (the prior boundary); the posterior median of 0.075 reflects prior volume at s₀ > 0. The 95th percentile gives:

$$s_0 < 0.18 \quad (95\% \text{ CL, flat prior}).$$

The Δχ² = +0.13 at equal parameter count corresponds to ΔAIC = ΔBIC = +0.13: no preference for either model.

[**Figure 3**: Corner plot of the Λcos posterior in (s₀, H₀r_d, M_B) space from the SN+BAO fit.]

[**Figure 4**: Pantheon+ binned residuals (μ_data − μ_model) for ΛCDM and Λcos at joint best-fit parameters. The two models are indistinguishable.]

### 5.3 Prior sensitivity

Since the Λcos posterior is concentrated near the lower prior boundary, the 95% upper limit is prior-sensitive. We test two alternative priors by reweighting the baseline chain:

| Prior on s₀ | s₀ median | s₀ 95% UL | χ²_min |
|-------------|-----------|-----------|--------|
| Flat s₀ ∈ [0.001, 0.99] (baseline) | 0.075 | 0.184 | 1772.6 |
| Flat in s₀² (more weight near zero) | 0.118 | 0.211 | 1772.6 |
| Flat in log₁₀(s₀) (scale-invariant) | 0.012 | 0.119 | 1772.6 |

The χ²_min is identical across all three priors (the likelihood is unchanged; only the posterior weighting differs). The 95% upper limit ranges from 0.12 to 0.21, a factor of ~1.8. The constraint is prior-sensitive in detail but data-driven in character: all three priors yield s₀ ≪ 1.

### 5.4 Ω_Λ sensitivity

The primary fit fixes Ω_Λ = 0.685 from a companion analysis [16]. To test robustness, we repeat the SN+BAO fit at three alternative values:

| Ω_Λ | s₀ median | s₀ 95% UL | Δχ² vs ΛCDM |
|-----|-----------|-----------|-------------|
| 0.680 | 0.064 | 0.163 | +0.78 |
| 0.685 (baseline) | 0.075 | 0.184 | +0.13 |
| 0.690 | 0.088 | 0.204 | +0.04 |
| 0.700 | 0.149 | 0.262 | +0.93 |

The s₀ constraint varies smoothly with Ω_Λ, with the 95% upper limit ranging from 0.16 to 0.26 across the tested interval. The best Δχ² occurs near Ω_Λ = 0.69. The results are stable: no fine-tuning of Ω_Λ is required.

### 5.5 CMB distance priors

The DESI DR2 phantom-crossing result was obtained jointly with Planck CMB data. To test whether Λcos is compatible with CMB constraints, we add compressed Planck 2018 distance priors (shift parameter R = 1.7502 ± 0.0046, acoustic scale l_A = 301.47 ± 0.09, treated as independent Gaussians) to the SN+BAO likelihood. These quantities constrain the integral ∫dz/E(z) to the last-scattering surface at z* = 1090. Radiation (Ω_r = 9.15 × 10⁻⁵) is included for this integral. Non-flat ΛCDM includes a curvature term Ω_k = 1 − Ω_m − Ω_Λ.

| | Flat ΛCDM | Λcos (Ω_Λ = 0.685) | Λcos (Ω_Λ free) | Non-flat ΛCDM |
|-|-----------|--------------------|--------------------|---------------|
| **Free params** | Ω_m, H₀r_d, M_B | s₀, H₀r_d, M_B | s₀, Ω_Λ, H₀r_d, M_B | Ω_m, Ω_Λ, H₀r_d, M_B |
| **Best-fit Ω_Λ** | 0.715 | 0.685 (fixed) | 0.715 | 0.722 |
| **χ²_min** | 1817.8 | 1885.7 | 1817.8 | 1817.3 |
| **χ²_BAO** | 30.8 | 125.3 | 30.7 | 31.3 |
| **Δχ² vs ΛCDM** | 0 | +67.9 | +0.43* | — |

*Relative to non-flat ΛCDM at equal parameter count (4 each).

With Ω_Λ = 0.685 fixed, Λcos is strongly disfavored (Δχ² = +67.9). The tension is driven by the BAO sector (χ²_BAO = 125 vs 31), not by the CMB priors themselves (χ²_CMB = 1.4 for Λcos vs 16.2 for ΛCDM). The CMB priors pull H₀r_d to a value incompatible with BAO at fixed Ω_Λ = 0.685.

This tension is not specific to Λcos. Adding CMB priors shifts the preferred Ω_Λ from 0.685–0.688 (SN+BAO) to ~0.715 in both ΛCDM and Λcos. Flat ΛCDM absorbs the shift through Ω_m (which moves from 0.312 to 0.285). Λcos at fixed Ω_Λ cannot absorb it. Freeing Ω_Λ restores full consistency: the Λcos fit with Ω_Λ free yields Ω_Λ = 0.715 [0.711, 0.718] and Δχ² = +0.43 relative to non-flat ΛCDM at the same parameter count.

The 3% shift from 0.685 to 0.715 is a known DESI-era tension between BAO and CMB distance scales [1]. Whether the topology-derived Ω_Λ = 0.685 or the combined-data value 0.715 is closer to the true value requires the full Planck TTTEEE+lowE likelihood, which is beyond the scope of this letter.

### 5.6 Internal consistency

The matter fraction in Λcos is set by construction through Ω_m = 1 − Ω_Λ. The (1+z)³ coefficient α = Ω_m/(1−s₀²) is a dressed version of this input. As a consistency check: at any s₀, α(1 − s₀²) returns Ω_m = 0.315. The dressing is algebraically self-consistent and does not introduce additional freedom.

## 6. Predictions

### 6.1 The (1+z)¹ signature

The joint SN+BAO fit constrains |β| < 0.011 at 95% CL (from s₀ < 0.18 with Ω_m = 0.315). The predicted fractional contribution to H²(z) at z = 1 is:

$$\frac{|\beta|(1+z)}{E^2(z)} < 0.7\% \quad (95\% \text{ CL at } z = 1).$$

This is below the precision of current BAO measurements (~2–3% per bin) but within reach of Euclid DR1 (~1% level at z = 0.9–1.8 [19]). A detection of a negative (1+z)¹ component in H²(z) at any significance would constitute evidence for a bounded or non-standard dark energy component. While a domain-wall fluid (w = −2/3) produces the same scaling, the Λcos term is distinguished by its coefficient being set by s₀ through the budget identity rather than by an independent energy density.

### 6.2 Pre-registered predictions

Two predictions from the broader framework are registered on Zenodo [20] prior to Euclid DR1 (expected October 2026):

| Prediction | Value | Falsified if |
|-----------|-------|-------------|
| a₀(z) ∝ H(z) | Epoch-dependent MOND scale [21] | a₀ constant at high z at ≥ 2σ |
| Λ constant | Ω_Λ independent of z | ρ_DE(z) evolves at ≥ 2σ |

The first prediction (epoch-dependent acceleration scale) is derived from the same framework that produces the Λcos model [21] and is independent of s₀. The second is identical to ΛCDM.

### 6.3 Falsification criteria

| Observable | Λcos prediction | Falsified if |
|-----------|----------------|-------------|
| (1+z)¹ coefficient in H² | Negative, magnitude set by s₀ | Positive (1+z)¹ term detected |
| w_eff(z) | > −1 for all z at any s₀ > 0 | True phantom crossing confirmed at ≥ 2σ by non-parametric reconstruction |
| ΛCDM limit | s₀ = 0 recovers ΛCDM exactly | No additional test required |

## 7. Discussion

### 7.1 Template bias

The central result of this paper is that bounded dark energy sectors produce apparent phantom crossings when fitted with standard two-parameter w(z) templates. We have demonstrated this explicitly for CPL, BA, and JBP parameterizations: all three recover w₀ < −1 from Λcos distances that satisfy w_eff > −1 at every redshift. A three-parameter polynomial does not produce the crossing, confirming that the effect arises from basis restriction rather than from the underlying physics.

This finding has precedent. Linder and Huterer [12] identified CPL template bias, Shafieloo, Sahni, and Starobinsky [13] demonstrated spurious phantom crossings from model-dependent reconstruction, and recent work [8,14] has raised similar concerns about the DESI signal specifically. The present contribution is to provide a concrete, topology-derived bounded model (rather than a generic cautionary argument), to test multiple parameterizations, and to scan the template bias amplitude across the full parameter range allowed by current data.

At data-allowed values (s₀ < 0.18), the induced CPL distortion is w₀ ≈ −1.02 with positive w_a, structurally present but modest in amplitude and opposite in sign to the DESI best fit (w₀ ≈ −0.75, w_a ≈ −0.86). The paper establishes the mechanism without claiming to reproduce the DESI signal quantitatively.

### 7.2 Status of Λcos

The Λcos model rests on three inputs: the budget identity Ψ² + S² = 1 (proposed), the power-law clock rate dt/dτ = S⁻¹/² (selected by matter-era asymptotic scaling), and the cosmological constant Ω_Λ = 0.685 (taken from a companion analysis [16]). The resulting H²(z) is derived algebraically from these inputs. The model recovers ΛCDM exactly as s₀ → 0.

Current combined data (Pantheon+ and DESI DR2 BAO) constrain s₀ < 0.18 at 95% CL, consistent with the ΛCDM limit. Λcos matches ΛCDM at Δχ² = +0.13 across the SN+BAO dataset. Adding CMB distance priors introduces a shared Ω_Λ tension resolvable by freeing Ω_Λ (Δχ² = +0.43 at equal parameter count). The model is a minimal bounded extension of ΛCDM, with a specific falsifiable signature (the negative (1+z)¹ term) testable by Euclid DR1.

### 7.3 Broader framework

The budget identity and the budget clock derive from a topological framework on S³ [15] that independently addresses the cosmological constant [16] and the fermion mass spectrum. The present paper is self-contained: the Λcos H²(z), the template bias argument, and the observational constraints depend only on the budget identity and the budget clock.

## 8. Conclusions

Bounded dark energy sectors produce apparent phantom crossings under standard two-parameter templates. The Λcos model, derived from a temporal budget identity on S³, provides a concrete realization satisfying w_eff(z) > −1 at all redshifts while matching the Pantheon+ and DESI DR2 BAO distance-redshift relation at Δχ² = +0.13 relative to flat ΛCDM. Current data constrain the model's single new parameter to s₀ < 0.18 (95% CL), and the predicted negative (1+z)¹ contribution to H²(z) is a standing target for Euclid DR1.

---

## Appendix A: Clock Exponent Selection

Three alternative clock rates were tested against the SN+BAO dataset:

| Model | Clock rate dt/dτ | High-z H scaling | Δχ² vs ΛCDM |
|-------|-----------------|-----------------|-------------|
| A (proper time) | S⁰ = 1 | (1+z)¹ | > +400 |
| B (conformal) | S⁻¹ | (1+z)² | > +11,000 |
| C (symmetric) | S⁺¹ | (1+z)⁰ | > +60 |
| **D (budget)** | **S⁻¹/²** | **(1+z)³/²** | **+0.13** |

Among the tested alternatives, only the half-integer exponent −1/2 reproduces the matter-dominated asymptotic scaling required by the data. The exponent is selected by three-dimensional matter dilution (ρ ∝ S⁻³) through the Friedmann square root (H ∝ ρ¹/²), giving H ∝ S⁻³/² at high z and the exact two-term H²(z) at all z.

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

[14] arXiv:2506.15091 (2025).

[15] B. Shatto, Mode Identity Theory: Modal Realization on Nested Topology (2025). DOI:10.5281/zenodo.18064856.

[16] B. Shatto, Λ Ground Mode of the Cosmic Boundary (2026). DOI:10.5281/zenodo.18307314.

[17] C. F. Gauss, Comment. Soc. Reg. Sci. Gott. 6, 99 (1828); D. Codazzi, Ann. Math. Pura Appl. 2, 101 (1868).

[18] S. Weinberg, Gravitation and Cosmology (Wiley, New York, 1972).

[19] Euclid Collaboration, Astron. Astrophys. 662, A112 (2022).

[20] B. Shatto, Pre-registered Predictions for Euclid DR1 (2026). DOI:10.5281/zenodo.18189078.

[21] B. Shatto, Epoch-Dependent a₀ (2026). Submitted.

---

/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /
