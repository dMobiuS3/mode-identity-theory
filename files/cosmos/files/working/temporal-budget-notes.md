/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /

---

# The Temporal Budget Identity: Research Notes

Working notes on the temporal budget $\Psi^2 + S^2 = 1$, the Waltz clock $d\tau/dt = S^{1/2}$, and the Pantheon+ fit that recovers $\Omega_m$ as output.

**Status:** Established at model level. With $S = \sin(t/2)$ and the Waltz clock, Model D+$\Lambda$ reproduces the Pantheon+ distance ladder at $\Delta\chi^2 = +0.6$ relative to flat $\Lambda$CDM on 1701 SNe Ia with full covariance, using two free parameters ($s_0$, $H_0$) — the same count as $\Lambda$CDM. $\Omega_m = 0.315$ is recovered from the $(1+z)^3$ coefficient. First-principles derivation of the clock exponent from $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ without invoking GR remains open.

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

## III. Model D+$\Lambda$ and Pantheon+

The Hubble parameter derived from the budget identity with the Waltz clock and topology-fixed $\Lambda$:

$$H^2(z) = H_0^2\left[\frac{1-\Omega_\Lambda}{1-s_0^2}(1+z)^3 \;-\; \frac{(1-\Omega_\Lambda) s_0^2}{1-s_0^2}(1+z) \;+\; \Omega_\Lambda\right]$$

Two free parameters: $s_0 = \sin(t_\text{now}/2)$ and $H_0$. Same count as $\Lambda$CDM ($\Omega_m$, $H_0$). $\Omega_\Lambda = 0.685$ is input from topology (Möbius eigenvalue), not fitted.

| Quantity | Best-fit value | Source |
|---|---|---|
| $s_0$ | 0.389 | Pantheon+ fit |
| $t_\text{now}$ (budget phase) | 0.80 rad | From $s_0$ |
| $\Omega_m$ (recovered) | 0.315 | $(1+z)^3$ coefficient |
| $(1+z)^1$ coefficient | $-0.040$ | Budget identity signature |
| $\Delta\chi^2$ vs flat $\Lambda$CDM | $+0.6$ | 1701 SNe Ia, full covariance |

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
| [Spatial budget $u_0^2 + J^2 = 1$](../cosmological-constant.md) | The temporal budget is its twin. Spatial budget sets $\Lambda_\text{obs} = (3/2)\Lambda_\text{top}$; temporal budget sets the Waltz clock. Same $3/2$ in both. |
| [Sector $\mathcal{A}$ eigenvalue](../ground-eigenvalue.md) | Fixes $\Lambda_\text{top}$, hence $\Omega_\Lambda = 0.685$ as input to the fit. |
| [Hubble tension](../hubble-tension.md) | The Waltz clock $H \propto S^{-3/2}$ is the mechanism underlying the early/late discrete snap. |
| [Energy as Resolution Amplitude](../../../spectrum/files/working/energy-as-resolution-amplitude.md) | Same sampling-operation picture. Redshift as phase ratio + energy as resolution amplitude should unify into a single account. Open. |

---

## X. Open Questions

| Item | Priority | Notes |
|---|---|---|
| Clock from postulate | High | The exponent $-1/2$ is forced by consistency with budget $+$ GR $+$ $S^3$ dimensionality. A derivation from $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ that does not invoke GR would promote this from ESTABLISHED to DERIVED. |
| $t_\text{now}$ from topology | High | The fit gives $t_\text{now} = 0.80$ rad. Deriving this from topology alone, not from data, closes the program. |
| $\varphi \leftrightarrow t$ relation | High | The two phase parameters must be reconciled. |
| Vertex-$Z_5$ role in $\Psi$ denominator | Medium | If the $(1+z)^1$ term derives from $Z_5$ in the temporal budget, the face/edge/vertex completion of the 3/2 accounting becomes explicit. |
| Redshift mechanism (fully derived) | Medium | Model D+$\Lambda$ gives the right distances. The phase-ratio picture on $S^1$ is understood in outline; the full derivation chain from postulate to observed $H(z)$ is partially walked. |
| $(1+z)^1$ detection threshold | Low (wait for data) | $-4\%$ of $H^2$ is below Pantheon+ sensitivity. Quantify the threshold for Euclid / Roman / LSST. |

---

*The budget balances. The clock keeps time. The waltz continues.*

---

/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /
