/ **[`main`](../../../)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# Phase Field Coherence Scale Predictions Across the SPARC Galaxy Sample

**Status:** Working draft. Predictions registered; analysis pending.
**Priority:** Pre-Euclid DR1 (October 2026 target).
**Dependencies:** Hubble tension mechanism (Θ = 34/120 → 36/120 shift), MOND scale a₀ from scaling law C(13/120), closure identity T_c = 2ξ v_c²/c².

---

## The Question

Mode Identity Theory predicts a binary phase field that shifts the local sampling position of the Hubble parameter by one bosonic grid step (2/120) inside a coherence scale $L_f = v_c^2/a_0$. Does the SPARC sample of 175 galaxies bear this out?

Three independent tests, each separable from the others:

1. Does the gravitational transition radius track $L_f$ across the sample?
2. Is the phase-field threshold universally crossed for all flat-rotation-curve galaxies?
3. Do H₀ measurements correlate with being inside or outside $L_f$ rather than with density, metallicity, or other environmental variables?

The point of separating the tests is component-level falsification: failure isolates whether the binary threshold, the closure identity, or $L_f$ itself is the broken piece.

---

## I. The Hubble Tension as a Phase Field Effect

Two classes of H₀ measurement persistently disagree:

| Method | H₀ (km/s/Mpc) | Environment |
|---|---|---|
| CMB (Planck) | 67.4 ± 0.5 | Global; unphased |
| Local distance ladder (SH0ES) | 73.0 ± 1.0 | Inside disk galaxies; phased |

MIT resolves this as a phase-field effect. The standing wave $\Psi = \cos(t/2)$ on $S^3/2I$ is sampled at Fibonacci wells on the 120-domain. The H₀ well sits at $\Theta = 34/120$ with $C(34/120) = 1.208$. Inside a disk galaxy, the local gravitational potential shifts the sampling position by one bosonic step (2/120) to $\Theta = 36/120$ with $C(36/120) = 1.309$. The ratio:

$$\frac{C(36/120)}{C(34/120)} = \frac{1.309}{1.208} = 1.084$$

Predicted shift: 8.4%. Observed tension: 67.4 → 73.0 ≈ 8.3%. Agreement < 1%.

---

## II. The Coherence Scale and the Trigger

The phase field is active within a coherence scale:

$$L_f = \frac{v_c^2}{a_0}$$

For the Milky Way ($v_c \approx 220$ km/s, $a_0 \approx 1.2 \times 10^{-10}$ m/s²): $L_f \approx 13$ kpc.

The phase field activates when the trigger index exceeds a critical threshold:

$$\mathcal{T} \equiv \frac{2}{c^2 L_f} \int_0^{L_f} \Phi_\text{rel}(l)\, dl, \qquad \mathcal{T}_c = \frac{2\xi\, v_c^2}{c^2}$$

Geometry factor $\xi \approx 0.46$ (insensitive to halo profile: isothermal/NFW/Hernquist give 0.44–0.47).

For flat-rotation-curve galaxies: $\mathcal{T}/\mathcal{T}_c = 1/\xi \approx 2.2$. The threshold is always crossed. The phase field is always active. The response is binary:

$$\Theta_f = \frac{2}{120} \cdot \mathbf{1}(\mathcal{T} \geq \mathcal{T}_c)$$

One bosonic grid step or nothing. No continuous tuning.

### Closure identity

$a_0$ cancels in the threshold:

$$\mathcal{T}_c = \frac{2\xi\, a_0\, L_f}{c^2} = \frac{2\xi\, v_c^2}{c^2}$$

The MOND scale sets the coherence radius but drops out of the threshold condition. Any galaxy with a flat rotation curve crosses the threshold regardless of mass, size, or luminosity.

---

## III. Data: The SPARC Sample

SPARC (Spitzer Photometry and Accurate Rotation Curves): Lelli, McGaugh, Schombert (2016).

- 175 galaxies
- Measured rotation curves from HI/Hα observations
- Spitzer 3.6μm photometry for stellar mass
- Well-characterized $v_c$ (flat rotation velocity)
- Publicly available: astroweb.cwru.edu/SPARC

### Per-galaxy parameters used

| Parameter | Source | Use |
|---|---|---|
| $v_c$ (flat) | Rotation curve outer region | Compute $L_f$ |
| $R_\text{last}$ | Last measured point on rotation curve | Compare to $L_f$ |
| Quality flag | SPARC catalog | Filter sample |
| Hubble type | SPARC catalog | Check for systematics |
| Distance | SPARC catalog | Anchor measurements |
| Inclination | SPARC catalog | Rotation curve reliability |

### Sample selection

- Include: galaxies with well-defined flat rotation region (quality flag 1 or 2).
- Exclude: galaxies with rising or falling rotation curves at the last measured point.
- Exclude: face-on galaxies with poorly constrained $v_c$ (inclination < 30°).

Expected usable sample: ~120–140 galaxies.

---

## IV. Predictions

### Predicted L_f range across galaxy types

Using $a_0 = 1.2 \times 10^{-10}$ m/s²:

| Galaxy type | Typical $v_c$ (km/s) | Predicted $L_f$ (kpc) |
|---|---|---|
| Massive spiral | 250–300 | 17–24 |
| Milky Way-class | 200–230 | 11–14 |
| Low-mass spiral | 100–150 | 3–6 |
| Dwarf irregular | 30–70 | 0.2–1.3 |

### Universal threshold crossing

Every galaxy with a flat rotation curve should satisfy $\mathcal{T}/\mathcal{T}_c \approx 1/\xi \approx 2.2$ regardless of mass or size. Compute $\mathcal{T}_c$ for each galaxy; verify $\mathcal{T}/\mathcal{T}_c > 1$ for all flat-curve galaxies.

### Transition radius tracks L_f

The radius at which gravitational behavior transitions from Newtonian to "anomalous" (the MOND transition) should correlate with $L_f = v_c^2/a_0$. For each SPARC galaxy, identify the radius $r_t$ where observed acceleration crosses $a_0$. Plot $r_t$ against $L_f$. Prediction: linear correlation with slope ≈ 1.

### Dwarf galaxies without flat curves

Galaxies with rising rotation curves (no flat region) may fail to cross the threshold and would be unphased, predicting no H₀ shift in their environment. Identify these galaxies in SPARC; check if their environmental H₀ measurements differ from disk galaxies.

### No continuous spread

H₀ measurements should cluster in two populations (67 and 73), not form a continuous distribution correlated with $v_c$ or $L_f$. If H₀ varied continuously with $v_c$, you would see a gradient. MIT predicts binary: inside $L_f$ = shifted, outside = unshifted. No intermediate values.

---

## V. Analysis Methods

### Computing L_f

For each galaxy with measured $v_c$:

```
a_0 = 1.2e-10  # m/s²
v_c = [from SPARC]  # m/s
L_f = v_c**2 / a_0  # meters, convert to kpc
```

### Identifying the transition radius

For each rotation curve, compute the observed centripetal acceleration:

$$g_\text{obs}(r) = \frac{v(r)^2}{r}$$

And the baryonic (Newtonian) acceleration from the mass model:

$$g_\text{bar}(r) = \frac{v_\text{bar}(r)^2}{r}$$

The transition radius $r_t$ is where $g_\text{obs}$ begins to exceed $g_\text{bar}$ systematically, or equivalently where $g_\text{obs}$ crosses $a_0$.

### Correlation analysis

- Pearson/Spearman correlation between $r_t$ and $L_f$.
- Residual analysis: check if scatter correlates with distance, inclination, Hubble type, surface brightness, or metallicity.
- If scatter correlates with a non-MIT variable, the phase field mechanism is in trouble.

### Threshold verification

```
T_c = 2 * xi * v_c**2 / c**2
T = T_c / xi  # for flat rotation curves
ratio = T / T_c  # should be ≈ 2.2 for all flat-curve galaxies
```

Verify ratio > 1 for all flat-curve galaxies. Identify any exceptions.

### Binary vs. continuous

If local H₀ estimates exist for SPARC galaxies (or for galaxies in similar environments):
- Bin by inside/outside $L_f$.
- Test for bimodality vs. unimodal spread.
- KS test or Hartigan's dip test for bimodality.

---

## VI. Falsification at the Component Level

The key advantage of the test. If it fails, we know which piece broke:

| Failure mode | What broke | Implication |
|---|---|---|
| $r_t$ does not correlate with $L_f$ | $L_f = v_c^2/a_0$ is wrong | Phase field coherence scale is incorrect |
| Threshold not universally crossed | Closure identity fails | $\mathcal{T}_c$ formulation or $\xi$ value is wrong |
| H₀ varies continuously with $v_c$ | Binary response is wrong | Phase field is graded, not snapping |
| Scatter correlates with metallicity or density | Environmental variable dominates | Phase field is not the primary mechanism |
| $r_t$ correlates with $L_f$ but with wrong slope | $a_0$ value or formula structure is off | Specific coefficient needs correction |

---

## VII. Relation to Existing Work

### McGaugh's Radial Acceleration Relation

McGaugh et al. (2016) established a tight correlation between observed and baryonic acceleration in galaxies (the RAR). MIT's phase field mechanism reproduces the RAR as a consequence: inside $L_f$, the shifted sampling position mimics additional mass. The RAR is real but is a geometric effect, not a modified force law.

Key distinction: the RAR alone does not predict H₀ bimodality. MIT does. This is the additional prediction that separates the frameworks.

### MOND

Milgrom (1983) identified $a_0$ as a fundamental acceleration scale. MIT derives $a_0$ from the scaling law: $a_0/a_P = C(13/120) \times (\sqrt{\Omega_H})^{-1}$. The value is not fitted. The coincidence $a_0 \approx cH_0$ is explained: both are edge modes on the standing wave, and their ratio $C(13/120)/C(34/120) = 0.184$ is fixed by the topology.

Key distinction: MOND modifies the force law. MIT does not. Gravity remains inverse-square everywhere. The "missing mass" is a curvature conversion, not a force modification. Recent pairwise cluster data (Gallardo et al., PRL 136, 2026) confirms inverse-square at cluster scales, consistent with MIT, inconsistent with MOND.

### ΛCDM + Dark Matter Particles

ΛCDM fits rotation curves by adding a dark matter halo. MIT fits them through the Gauss-Codazzi 3/2 curvature conversion from the embedded Möbius surface. Both reproduce the data. The discriminant is direct detection: MIT predicts permanent null. Every null result from LUX, XENON, PandaX, SuperCDMS, and future experiments is consistent with MIT and increasingly difficult for particle dark matter.

---

## VIII. Timeline and Submission

| Step | Target |
|---|---|
| Download SPARC data | Week 1 |
| Compute $L_f$ for all galaxies | Week 1 |
| Identify transition radii | Week 2 |
| Correlation analysis | Week 2–3 |
| Write results | Week 3–4 |
| Submit | Before Euclid DR1 (October 2026) |

Target journal: MNRAS Letters or ApJ Letters.

---

## IX. Connection to MIT Framework

This paper tests one specific component of Mode Identity Theory: the phase field mechanism that resolves the Hubble tension. It does not require the full framework to be accepted. The test is:

1. $L_f = v_c^2/a_0$ predicts a coherence scale for each galaxy.
2. The gravitational transition radius should track $L_f$ across the sample.
3. The threshold should be universally crossed for flat-rotation-curve galaxies.
4. The H₀ shift should be binary, not continuous.

If all four hold across 175 galaxies, the phase field mechanism is confirmed independently of Euclid. If any fail, the specific failure mode tells you what to fix.

---

## References

- Lelli, F., McGaugh, S. S., Schombert, J. M. (2016). SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves. AJ, 152, 157.
- McGaugh, S. S., Lelli, F., Schombert, J. M. (2016). The Radial Acceleration Relation in Rotationally Supported Galaxies. PRL, 117, 201101.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. ApJ, 270, 365.
- Gallardo, P. A., et al. (2026). Pairwise kinematic Sunyaev-Zel'dovich effect with DESI galaxies and Planck. PRL, 136, 151002.
- Shatto, B. (2026). Mode Identity Theory engine file. github.com/dmobius3/mode-identity-theory

---

*Topology holds. Wave is. Particle samples.*

---

/ **[`main`](../../../)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
