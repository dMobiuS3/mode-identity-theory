/ **[`main/`](../../../README.md)** / **[`framework/`](../../framework/)** / **[`cosmos/`](../../cosmos/)** / **[`spectrum/`](../../spectrum/)** /

---

# w Evolving: Λ Topological Resolution

[![Dark Energy](https://img.youtube.com/vi/CGFTYpJY3j8/mqdefault.jpg)](https://www.youtube.com/watch?v=CGFTYpJY3j8)

DESI reports mounting evidence (2.8--4.2σ) that the dark energy equation of state $w$ evolves with redshift. If true, it would overturn the cosmological constant and reshape modern physics. 

Mode Identity Theory says the change is an illusion: Λ is fixed by the geometry of the universe, and what looks like evolution is the observer's phase position on a standing wave. The "phantom crossing" through $w = -1$ arises as a template artifact rather than exotic physics.

Tested against DESI DR2 baryon acoustic oscillation data, the Pantheon+ supernova compilation, and a Planck-calibrated CMB ruler prior, MIT with locked parameters achieves $\Delta\text{AIC} = -2.1$ over ΛCDM at the same parameter count.

**DESI DR2 + Pantheon+ + Planck**

| Quantity | Value |
|---|---|
| MIT vs ΛCDM | $\Delta\text{AIC} = -2.1$ |
| Profiled coupling | $\Delta\chi^2 = -7.9$ ($\Delta\text{AIC} = -5.9$ at $k = 3$) |
| Zero-crossing | $z_\text{cross} = 0.663$ (registered blind prediction) |
| Phantom crossing | $w_\text{eff}(z) > -1$ at all redshifts |

## I. The Observational Landscape

The DESI DR2 results present the most precise baryon acoustic oscillation measurements to date, drawing from over 14 million galaxies and quasars across 11 billion years of cosmic history. When combined with CMB data and supernova compilations, the results indicate that dark energy's equation of state $w$ may not equal $-1$ as assumed in ΛCDM.

The emerging picture: present value $w_0 \approx -0.85$ to $-0.70$ (less negative than Λ), past behavior $w < -1$ at higher redshifts (phantom-like), and a "phantom crossing" through $w = -1$ near $z \approx 0.5$. Single-field models face fundamental difficulties crossing $w = -1$; proposed solutions require exotic field content.

This presents sharp tension for any framework treating the cosmological constant as fundamental. MIT derives Λ from surface-mode projection on bounded topology. If Λ itself evolved, the framework would face direct structural contradiction. However, DESI constrains the inferred equation of state $w(z)$, not vacuum energy Λ directly. While related in standard cosmology, these quantities separate in a topological framework.

## II. The Mechanism

MIT's anti-periodic boundary conditions admit a standing wave on the bounded domain:

$$\Psi = \cos(t/2)$$

The full cycle spans $4\pi$ (~33 Gyr). The present epoch sits at $t \approx 5.22$ rad, approximately 2.8 Gyr before the geometric turnaround at $t = 2\pi$.

MIT identifies Λ as a surface-mode eigenvalue. The topological protection established in the $\Lambda$ derivation is against displacement in $\Theta$, the position coordinate on the mode spectrum. The logarithmic slope $d\ln C/d\Theta$ vanishes exactly at the antinode; no environmental perturbation can shift $\Lambda$ to a different well. The modulation here acts in $t$, the observer's phase within the cosmic cycle. $\Lambda$ occupies a fixed position (the antinode); what varies is the standing wave amplitude $\Psi(t) = \cos(t/2)$ at the observer's epoch. The surface-mode eigenvalue is constant; its projection into the expansion history carries the temporal phase of $\Psi$.

The cosmic wave therefore modulates the dark energy sector, with an amplitude set by the projection into Friedmann variables (see The Coupling ε below), leaving matter and radiation untouched. The Friedmann equation becomes:

$$E_{\text{MIT}}^2(z) = \Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_\Lambda^{\text{bare}}\bigl[1 + \varepsilon\cos\theta(z)\bigr]$$

where $\theta(z) = (2\pi + \delta)/\bigl(2(1+z)\bigr)$: the standing wave phase is $t(z) = (2\pi + \delta) \cdot a = (2\pi + \delta)/(1+z)$ (linear in scale factor $a$, the minimal ansatz keeping the topological phase independent of the dynamics it modulates), and $\theta = t/2$ because $\Psi = \cos(t/2)$. The bare cosmological constant $\Omega_\Lambda^{\text{bare}} = (1 - \Omega_m - \Omega_r)/(1 + \varepsilon\cos\theta_0)$ with $\theta_0 = (2\pi + \delta)/2$ enforces $E^2(0) = 1$. The ΛCDM limit is recovered at $\varepsilon \to 0$.

The surface-mode coupling is invisible to the CMB by construction. At recombination ($z_* \approx 1090$), $E^2(z_*) \approx \Omega_m(1091)^3 \approx 4 \times 10^8$, so $\Omega_\Lambda^{\text{bare}} / E^2(z_*) \approx 1.7 \times 10^{-9}$; the modulation contributes $\varepsilon \times 1.7 \times 10^{-9} \approx 4 \times 10^{-10}$ to $E^2$, far below observational sensitivity. At low redshift, where Λ dominates the energy budget, the full BAO and supernova signatures are preserved.

### The Phase Offset δ

The observer's position within the cosmic cycle is measured from the geometric turnaround ($t = 2\pi$, where $\Psi = -1$; $t$ increases monotonically from $t = 0$). The derivation:

$$\Omega_m, \Omega_\Lambda, H_0 \xrightarrow{\text{Friedmann}} T_\text{cycle} \approx 33.2 \text{ Gyr} \xrightarrow{t = 4\pi\, T/T_\text{cycle}} t_\text{now} = 4\pi \times \frac{13.8}{33.2} = 5.22 \text{ rad} \xrightarrow{\delta \equiv t - 2\pi} \delta = -1.06 \text{ rad}$$

All inputs are prior to any BAO dataset. The resulting $z_\text{cross} = 0.663$ coincides with the center of DESI's non-parametric $w(z)$ transition region. This coincidence is a consistency check, not a calibration. The prediction is registered on Zenodo prior to Euclid DR1.

### The Coupling ε

ε is a translation coefficient, measuring how the MIT standing wave projects into the Friedmann equation. It belongs to the interface between the two frameworks: MIT's own structure (boundary conditions, standing wave, surface-mode eigenvalue) contains no free amplitude parameter. The projection into standard Friedmann variables requires one because the two descriptions parameterize the expansion history differently.

The CMB topology analysis independently determines the observer's geodesic distance from the domain center: $d = 2.1$ Gpc, corresponding to $\chi = d/R = 0.40$ rad in $S^3$ (constrained by four CMB observables). The profiled coupling $\varepsilon \approx 0.16$ is numerically consistent with $(d/R)^2 = 0.160$ to better than 1%. This suggests the modulation amplitude may trace to the standing wave energy density at the observer's position, whose lowest spatially-varying mode scales as $\chi^2$ at small $\chi$. A first-principles derivation equating the local mode amplitude with the Friedmann-sector coupling remains open; the functional form of the $z$-dependence has not been verified from this geometric picture.

The calibration proceeds by inject-and-recover: MIT distances are generated at trial ε, a CPL template is fitted, and the recovered $w_0$ is matched to the target $w_0 = -0.773$ from DES-SN5YR + Planck + SDSS BAO, which contains no DESI data. This yields ε = 0.255 and is locked before the DESI analysis (prediction mode, $k = 2$). Separately, profiling ε on the DESI combination yields a best-fit of ε = 0.16 (profile mode, $k = 3$; see Results). The residual difference between the two values likely reflects dataset-dependent systematics and the distortion introduced by fitting a cosine modulation through a linear CPL template.

## III. The Phantom Crossing

Standard cosmology treats "phantom" behavior ($w < -1$) as exotic, requiring negative kinetic energy or ghost fields. MIT requires no such machinery.

The effective equation of state from Friedmann inversion is:

$$w_{\text{eff}}(z) = -1 + \frac{\varepsilon\,(2\pi + \delta)\,\sin\theta(z)}{6(1+z)\bigl[1 + \varepsilon\cos\theta(z)\bigr]}$$

The correction term is strictly positive for all $z \geq 0$: with $\theta_0 \approx 2.61 < \pi$, the phase satisfies $\theta(z) \in (0, \theta_0)$ so $\sin\theta > 0$ throughout, and $1 + \varepsilon\cos\theta > 0$ for $\varepsilon < 1$. Therefore $w_\text{eff}(z) > -1$ at all physical redshifts. MIT's effective dark energy never goes phantom.

The modulation $\varepsilon\cos\theta(z)$ changes sign where $\cos\theta = 0$, i.e. $\theta = \pi/2$:

$$\frac{2\pi + \delta}{2(1 + z_\text{cross})} = \frac{\pi}{2} \implies 1 + z_\text{cross} = \frac{2\pi + \delta}{\pi} \implies z_{\text{cross}} = 1 + \frac{\delta}{\pi} = 0.663$$

This is the zero-crossing of the modulation function $\varepsilon\cos\theta$. The deviation of $E_\text{MIT}$ from $E_\Lambda\text{CDM}$ peaks near this redshift (~4.6% in $E(z)$) because the flatness normalization sets $\Omega_\Lambda^\text{bare} > \Omega_\Lambda$: absorbing the negative modulation at $z = 0$ raises the bare value, so when $\cos\theta$ passes through zero the bare excess is fully exposed. When observers fit these distances using CPL templates ($w_0 + w_a(1-a)$), the linear form cannot capture the cosine shape. CPL compensates by placing $w_0 > -1$ and $w_a < 0$. The phantom crossing is not in the expansion history but in the template used to fit it.

When CPL is fit to noise-free MIT distances, the recovered sum $w_0 + w_a = -1.00$ sits at the ΛCDM value. The template does not cross $w = -1$. The crossing in DESI's fit arises from the CPL template interacting with data scatter.

## IV. Results

Tested against DESI DR2 BAO (13 observables, 7 redshift bins), Pantheon+ (~1590 Type Ia supernovae), and a Planck-calibrated CMB ruler prior ($H_0 r_d = 9908 \pm 81$ km/s). MIT parameters are locked prior to fitting; only the shared cosmological parameters ($\Omega_m$, $H_0 r_d$) are adjusted.

| Model | $k$ | $\chi^2_\text{BAO}$ | $\Omega_m$ | ΔAIC |
|---|---|---|---|---|
| ΛCDM | 2 | 13.54 | 0.313 | 0 |
| MIT ($\varepsilon = 0.255$) | 2 | 11.21 | 0.294 | $-2.1$ |
| CPL | 4 | 8.58 | 0.307 | $-4.0$ |

MIT improves on ΛCDM by $\Delta\chi^2 = -2.1$ at the same parameter count. The improvement comes from a better BAO fit ($\Delta\chi^2_\text{BAO} = -2.3$) and a substantially better match to the CMB-calibrated ruler. MIT's $H_0 r_d = 9860$ sits 0.6σ from the Planck center; ΛCDM's $H_0 r_d = 10023$ sits 1.4σ away.

**Coupling Amplitude Profile (profile mode, $k = 3$).** Profiling $\varepsilon$ over a grid while fitting $\Omega_m$ and $H_0 r_d$, the data prefer $\varepsilon = 0.16$ with $\Delta\chi^2 = -7.9$ relative to ΛCDM. Counting $\varepsilon$ as a third parameter yields $\Delta\text{AIC} = -5.9$. Both prediction mode ($\varepsilon = 0.255$ locked, $k = 2$, $\Delta\text{AIC} = -2.1$) and profile mode ($\varepsilon = 0.16$ fitted, $k = 3$, $\Delta\text{AIC} = -5.9$) favor nonzero modulation over ΛCDM.

## V. Falsification

All predictions are registered on Zenodo prior to Euclid DR1 (expected October 2026):

| Prediction | MIT Value | Falsified if |
|---|---|---|
| $z_\text{cross}$ | 0.663 | Transition center < 0.4 or > 0.9 (2σ) |
| $w(z)$ form | Phase modulation | Linear preferred at $\Delta\text{AIC} > 4$ |
| Λ | Constant, $w_\text{eff} > -1$ | True phantom confirmed at 2σ |

MIT predicts $w(z)$ has curvature. A purely linear $w(z)$ at high precision would falsify the phase modulation signature. The inverse prediction: $a_0(z) \propto H(z)$ while Λ remains constant.

---

The cosmological constant remains what the framework requires: a surface mode fixed by boundary conditions.

*What "evolves" is not Λ, but perspective.*

---

/ **[`main/`](../../../README.md)** / **[`framework/`](../../framework/)** / **[`cosmos/`](../../cosmos/)** / **[`spectrum/`](../../spectrum/)** /
