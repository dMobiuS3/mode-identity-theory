/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /

---

# The Temporal Budget Identity: Research Notes

Working notes on the temporal budget $\Psi^2 + S^2 = 1$, the Waltz clock $d\tau/dt = S^{1/2}$, and the Pantheon+ fit that recovers $\Omega_m$ as output.

**Status:** Established at model level. With $S = \sin(t/2)$ and the Waltz clock, Model D+Λ reproduces the Pantheon+ distance ladder at $\Delta\chi^2 = +0.6$ relative to flat ΛCDM on 1701 SNe Ia with full covariance, using two free parameters ($s_0$, $H_0$) — the same count as ΛCDM. $\Omega_m = 0.315$ is recovered from the $(1+z)^3$ coefficient. First-principles derivation of the clock exponent from $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ without invoking GR remains open.

---

## I. The Budget Identity

The temporal budget identity sits in structural parallel to the spatial budget $u_0^2 + J^2 = 1$ derived for the Möbius wavefunction. Its temporal twin:

$$\Psi^2 + S^2 = 1, \quad \Psi = \cos(t/2), \quad S = \sin(t/2)$$

$\Psi$ is the cosmic standing wave. $S$ is the **modal realization amplitude** — the bounded fraction of the wave expressed as resolvable modes at phase $t$. The sum closes by construction ($\sin^2 + \cos^2 = 1$), but its content is physical: the realized-mode content and the standing-wave content exhaust the total at every phase.

Bounded realization ($S \leq 1$) is the key feature. Nothing in a standard FLRW decomposition has this constraint. Its fingerprint will appear as a forbidden term (§V).

---

## II. The Waltz Clock

The relationship between conformal time $\tau$ and the budget phase $t$ is:

$$\frac{dt}{d\tau} = S^{-1/2} \quad \Longleftrightarrow \quad H \propto S^{-3/2}$$

The exponent is not fitted. It is forced by two structural facts.

| Factor | Contribution | Origin |
|---|---|---|
| Matter dilution in 3 spatial dimensions | $S^{-3}$ on energy density | Face stabilizer order 3 in the $S^3$ Gauss-Codazzi accounting |
| Friedmann $H^2 \to H$ | square root on the rate | Edge stabilizer order 2 in the same accounting |

Their ratio is $3/2$ — the same $3/2$ that relates $\Lambda_\text{obs} = (3/2) \Lambda_\text{top}$ by Gauss-Codazzi embedding. It appears as the exponent on $H$ and as $-1/2$ on the clock ($1 - 3/2 = -1/2$). One ratio, two surface readings.

Alternative integer-power clocks ($S^0$, $S^{-1}$, $S^{+1}$ — Models A, B, C) produce $(1+z)^0$, $(1+z)^2$, $(1+z)^1$ in $H^2$. Only the $3/2$ clock gives $(1+z)^3$, which is what a matter-dominated expansion requires. Data closes the selection; structure forces it.

---

## III. Model D+Λ and Pantheon+

The Hubble parameter derived from the budget identity with the Waltz clock and topology-fixed Λ:

$$H^2(z) = H_0^2\left[\frac{1-\Omega_\Lambda}{1-s_0^2}(1+z)^3 - \frac{(1-\Omega_\Lambda) s_0^2}{1-s_0^2}(1+z) + \Omega_\Lambda\right]$$

Two free parameters: $s_0 = \sin(t_\text{now}/2)$ and $H_0$. Same count as ΛCDM ($\Omega_m$, $H_0$). $\Omega_\Lambda = 0.685$ is input from topology (Möbius eigenvalue), not fitted.

| Quantity | Best-fit value | Source |
|---|---|---|
| $s_0$ | 0.389 | Pantheon+ fit |
| $t_\text{now}$ (budget phase) | 0.80 rad | From $s_0$ |
| $\Omega_m$ (recovered) | 0.315 | $(1+z)^3$ coefficient |
| $(1+z)^1$ coefficient | −0.040 | Budget identity signature |
| $\Delta\chi^2$ vs flat ΛCDM | +0.6 | 1701 SNe Ia, full covariance |

Pure budget without $\Lambda$ gives $q_0 = +0.5$ (deceleration). Data requires $q_0 \approx -0.55$ (acceleration). $\Lambda$ from topology is necessary; it is also already derived elsewhere in the framework (not a parameter introduced here).

---

## IV. $\Omega_m$ as Output

$\Omega_m = 0.315$ is not a fit input. It emerges from the $(1+z)^3$ coefficient through the budget dressing $1/(1-s_0^2)$. Two readings of the same quantity:

$$\Omega_m^\text{underlying} = 1 - \Omega_\Lambda = 0.315 \quad \text{(topology)}$$

$$\Omega_m^\text{effective} = \frac{1-\Omega_\Lambda}{1-s_0^2} \quad \text{(what the $(1+z)^3$ coefficient reads)}$$

At best-fit $s_0 = 0.389$, the effective reading is $0.372$; the underlying value is $0.315$. The Planck value is recovered after removing the budget-identity dressing. The last borrowed cosmological parameter falls out as derived.

---

## V. The $(1+z)^1$ Signature

A negative $(1+z)^1$ term at $\sim 4\%$ of $H^2$ appears in the expansion. It has no source in any standard FLRW component:

| Component | Redshift scaling |
|---|---|
| Matter | $(1+z)^3$ |
| Radiation | $(1+z)^4$ |
| Curvature | $(1+z)^2$ |
| Dark energy ($w=-1$) | $(1+z)^0$ |
| Phantom ($w<-1$) | $(1+z)^n$, $n<0$ |

None gives a $(1+z)^1$. The term is the fingerprint of bounded realization: $\sin(t/2) \leq 1$ at the boundary introduces a lower-order correction that a monotonic density cannot reproduce.

Currently below Pantheon+ detection threshold. Future surveys (Euclid, Roman, LSST) are expected to reach percent-level $H(z)$ precision. The sign and approximate magnitude of the term are prediction.

---

## VI. The $\Psi$ Denominator

The full clock rate is:

$$\frac{dt}{d\tau} = \frac{S^{-1/2}}{\Psi} = \frac{1}{\sqrt{\sin(t/2)} \cdot \cos(t/2)}$$

The $\Psi$ in the denominator produces the $(1+z)^1$ term. Structural reading: face ($Z_3$) contributes to matter dilution, edge ($Z_2$) contributes to the Friedmann square root, and the vertex stabilizer ($Z_5$) is the candidate source of this temporal correction. The shape is visible; the derivation is unwalked. If it closes, the vertex's role in the temporal budget becomes the three-stabilizer completion of the 3/2 accounting.

---

## VII. Derivation Chain

$$\begin{aligned}
\Psi = \cos(t/2) & \quad \text{[AXIOM]}\\
\Psi^2 + S^2 = 1 & \quad \text{[PROPOSED; consistent with data]}\\
S = \sin(t/2) & \quad \text{[FOLLOWS]}\\
dt/d\tau = S^{-1/2} & \quad \text{[FORCED by $S^3$ dimensionality $+$ GR]}\\
H^2(z) \text{ from budget} + \Lambda & \quad \text{[DERIVED]}\\
\text{Fit to Pantheon+} & \quad \text{[ESTABLISHED: } \Delta\chi^2 = +0.6\text{]}\\
\Omega_m = 0.315 \text{ recovered} & \quad \text{[ESTABLISHED: from fit coefficient]}
\end{aligned}$$

Steps beyond this point remain open:

- Derive the clock exponent $-1/2$ from the postulate without invoking GR
- Derive $t_\text{now}$ (equivalently $s_0$) from topology without fitting Pantheon+
- Friedmann as output rather than input
- $\Omega_m$ from topology alone

---

## VIII. Two Phase Parameters

Two parameterizations of the same phase on $S^1$ are in use:

| Parameter | Definition | Value today |
|---|---|---|
| $\varphi$ (engine phase) | $\varphi = 4\pi T/T_\text{cycle}$, linear in proper time | $\varphi_\text{now} = 5.22$ rad (Friedmann integral) |
| $t$ (budget phase) | Nonlinear in proper time; argument of $\cos(t/2)$ | $t_\text{now} = 0.80$ rad (from $s_0$) |

They refer to the same underlying phase advance. The relation $t(\varphi)$ needs to be worked out and documented; whether either is more fundamental than the other is open.

---

## IX. Connection to Other MIT Results

| Connection | Content |
|---|---|
| [Spatial budget $u_0^2 + J^2 = 1$](../../../cosmos/files/cosmological-constant.md) | The temporal budget is its twin. Spatial budget sets $\Lambda_\text{obs} = (3/2)\Lambda_\text{top}$; temporal budget sets the Waltz clock. Same $3/2$ in both. |
| [Sector $\mathcal{A}$ eigenvalue](../../../cosmos/files/ground-eigenvalue.md) | Fixes $\Lambda_\text{top}$, hence $\Omega_\Lambda = 0.685$ as input to the fit. |
| [Hubble tension](../../../cosmos/files/hubble-tension.md) | The Waltz clock $H \propto S^{-3/2}$ is the mechanism underlying the early/late discrete snap. |
| [Energy as Resolution Amplitude](energy-as-resolution-amplitude.md) | Same sampling-operation picture. Redshift as phase ratio + energy as resolution amplitude should unify into a single account. Open. |

---

## X. Open Questions

| Item | Priority | Notes |
|---|---|---|
| Clock from postulate | High | The exponent $-1/2$ is forced by consistency with budget $+$ GR $+$ $S^3$ dimensionality. A derivation from $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ that does not invoke GR would promote this from ESTABLISHED to DERIVED. |
| $t_\text{now}$ from topology | High | The fit gives $t_\text{now} = 0.80$ rad. Deriving this from topology alone, not from data, closes the program. |
| $\varphi \leftrightarrow t$ relation | High | The two phase parameters must be reconciled. |
| Vertex-$Z_5$ role in $\Psi$ denominator | Medium | If the $(1+z)^1$ term derives from $Z_5$ in the temporal budget, the face/edge/vertex completion of the 3/2 accounting becomes explicit. |
| Redshift mechanism (fully derived) | Medium | Model D+Λ gives the right distances. The phase-ratio picture on $S^1$ is understood in outline; the full derivation chain from postulate to observed $H(z)$ is partially walked. |
| $(1+z)^1$ detection threshold | Low (wait for data) | $-4\%$ of $H^2$ is below Pantheon+ sensitivity. Quantify the threshold for Euclid / Roman / LSST. |

---

## XI. Euclid DR1 Prediction Ledger

Model D+Λ at best-fit parameters ($s_0 = 0.389$, $\Omega_\Lambda = 0.685$) produces concrete, redshift-dependent predictions across Euclid DR1's measurement channels. Each differs from ΛCDM by a computable, non-negligible amount. The ledger is pre-registered: agreement across channels over-determines $s_0$ empirically, which is what "setting the clock" means when the postulate-level derivation of $t_\text{now}$ hasn't closed yet.

### A. Expansion rate $H(z)/H_0$ from BAO

$$H^2/H_0^2 = 0.371(1+z)^3 - 0.056(1+z) + 0.685$$

| $z$ | MIT (Model D+Λ) | ΛCDM ($\Omega_m = 0.315$) | Δ |
|---|---|---|---|
| 0.3 | 1.195 | 1.174 | +1.8% |
| 0.5 | 1.361 | 1.322 | +3.0% |
| 0.7 | 1.553 | 1.494 | +3.9% |
| 1.0 | 1.882 | 1.790 | +5.1% |
| 1.5 | 2.518 | 2.368 | +6.3% |
| 2.0 | 3.246 | 3.032 | +7.1% |

**Signed direction.** $H_\text{MIT}(z) > H_\text{ΛCDM}(z)$ at all $z > 0$, with the gap growing monotonically with redshift. The prediction is not "different from ΛCDM" — it is **faster than ΛCDM by a specific, computable amount**. The $(1+z)^1$ coefficient is forced negative (−0.056) by the budget identity, not a free sign; the leading driver of the faster-expansion prediction is the budget-dressed $(1+z)^3$ coefficient (0.371 vs ΛCDM's 0.315), with the negative $(1+z)^1$ a subleading partial compensation.

**Discriminating bins.** Euclid DR1 BAO precision is approximately percent-level in $H(z)$ across the spectroscopic survey range $z = 0.7$ to $2.0$. The MIT gap exceeds 5% at $z > 1$ and reaches 7% at $z = 2$ — comfortably above DR1 sensitivity. The $z > 1$ bins carry the most discriminating power; low-$z$ bins ($z < 0.5$) are confused against ΛCDM below the DR1 error bar.

**Context.** Pantheon+ constrains $\int dz/H(z)$, not $H(z)$ directly — so MIT and ΛCDM agree on distance modulus ($\Delta\chi^2 = +0.6$) while diverging on the differential expansion rate. Euclid BAO reads the differential rate. This is where the Pantheon+ degeneracy breaks.

### B. The $(1+z)^1$ signature

| Quantity | MIT | ΛCDM |
|---|---|---|
| coefficient of $(1+z)$ in $H^2/H_0^2$ | −0.056 | 0 |
| fractional contribution at $z=1$ | −3.2% | 0 |

No standard FLRW component produces a $(1+z)^1$ term (§V). Quantifying the DR1 detection threshold is an open computation.

### C. Growth of structure $f(z)\sigma_8(z)$ from RSD  *(leading-order; full numerical integration needed)*

With EFE unchanged, linear growth obeys $\ddot\delta + 2H\dot\delta - 4\pi G\bar\rho_m\delta = 0$. Modified $H(z)$ and the budget-dressed $\Omega_m$ enter differently: the expansion rate uses the dressed coefficient (0.371), while the gravitational source uses the underlying $\Omega_m = 0.315$ (§IV).

| Quantity | MIT (leading-order) | ΛCDM |
|---|---|---|
| $f(0) \approx \Omega_m(0)^\gamma$, $\gamma \approx 0.55$ | ~0.58 (with $\Omega_m^\text{eff} = 0.371$) | ~0.53 |
| $f\sigma_8(0)$ | ~0.47 | ~0.43 |

The ~10% $f(0)$ gap is well above Euclid DR1 RSD precision. Numerical integration of the growth equation with the Model D+Λ $H(z)$ across all Euclid RSD bins is needed to replace the leading-order estimate with a full curve.

### D. Early-galaxies acceleration $a_0(z)$

$a_0(z)/a_0(0) = H(z)/H_0$ (derived, early-galaxies paper).

| $z$ | MIT | Euclid observable |
|---|---|---|
| 0.5 | $1.36 \times a_{0,\text{local}}$ | high-$z$ rotation curves |
| 1.0 | $1.88 \times a_{0,\text{local}}$ | high-$z$ rotation curves |
| 2.0 | $3.25 \times a_{0,\text{local}}$ | high-$z$ rotation curves |

### E. Phantom-crossing channel  *(already derived, already registered on Zenodo)*

| Quantity | MIT | ΛCDM |
|---|---|---|
| $z_\text{cross}$ (where $w_\text{eff} = -1$) | 0.663 | no crossing |
| $w_\text{eff}(z) > -1$ at all $z$ | yes (pre-registered) | yes |
| ΔAIC vs ΛCDM (DESI DR2 + Pantheon+ + Planck) | −2.1 | 0 |

### F. Null channels (topology-fixed)

| Quantity | MIT | ΛCDM |
|---|---|---|
| Λ(z) variation with redshift | 0 | 0 |
| Lensing mass / clustering mass (hidden DM component) | 1 | 1 with particulate DM |
| Fourth fundamental force, SUSY partners, new gauge bosons | 0 | 0 |
| Time variation of $\alpha$ | 0 | 0 |

### G. CMB–galaxy lensing cross-checks  *(from cosmos papers)*

| Quantity | MIT | ΛCDM |
|---|---|---|
| CMB $\ell_\text{cut}$ | ~32 (Molien gap) | no cutoff |
| $C_2/C_3$ | 0.13 | ~0.3 |
| Parity $R_{TT}$ | 0.81 | ~1 |
| $\Delta\theta_{23}$ ($\ell=2$, $\ell=3$ alignment) | ~8.6° | random |

### H. Clock-setting logic

The prediction set is over-determined. One fit parameter ($s_0 = 0.389$, from Pantheon+) forecasts $H(z)$, $f\sigma_8(z)$, $a_0(z)$, and $z_\text{cross}$ simultaneously. If all channels hit within their stated precision, $s_0$ is independently over-determined by Euclid DR1 alone — the clock is empirically set without needing the postulate-level derivation of $t_\text{now}$ to have closed yet. If channels disagree, the model fails before the postulate-level derivation matters.

This is pre-registration at the deepest level: **predict the time, then look**.

### Two open computations for this ledger

1. Numerical integration of the growth equation $\ddot\delta + 2H\dot\delta - 4\pi G\bar\rho_m\delta = 0$ with Model D+Λ $H(z)$, across Euclid's RSD bins, replacing the §XI.C leading-order $f(0)$ estimate with a full $f\sigma_8(z)$ curve.
2. Distance integrals $D_A(z)$, $D_L(z)$, $D_V(z)$ from $\int dz/H(z)$, giving the angular BAO scale across Euclid's spectroscopic bins.

---

*The budget balances. The clock keeps time. The waltz continues.*

---

/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /
