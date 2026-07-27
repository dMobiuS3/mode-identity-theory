/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/hubble%20tension%20banner.png?raw=true" width="100%" alt="Hubble Tension">

Measurements of the Hubble constant have split into two persistent camps: the cosmic microwave background gives 67.4 km/s/Mpc; local distance ladders give 73. The discrepancy has persisted across many systematic checks and independent methods. Mode Identity Theory identifies a candidate mechanism through the phase field: a one-step bosonic displacement on the 120-domain, whose size is fixed by the lattice geometry at 8.4%. The lattice calculation is untouched by the empirical failure. The galactic trigger proposed to realize the displacement does not survive its SPARC test.

**Summary**

| Quantity | Status |
|---|---|
| Phase shift required | $`\Theta_f = 2/120`$ |
| $`\Delta C/C`$ at $`H_0`$ well | 8.4%, unchanged |
| Shifted value if physically realized | $`67.4 \times 1.084 \approx 73`$ km/s/Mpc |
| Proposed trigger | $`L_f = v_c^2/a_0`$, falsified by SPARC |

## I. The Tension

The Planck CMB measurement gives $`H_0 = 67.4 \pm 0.5`$ km/s/Mpc at $`z \approx 1100`$. The SH0ES collaboration measures $`H_0 = 73.0 \pm 1.0`$ km/s/Mpc from Cepheid-calibrated Type Ia supernovae at $`z \approx 0`$. The gap is ~9%, persistent across independent local methods: Cepheids, tip of the red giant branch, surface brightness fluctuations, and megamasers. The MIT phase-clock fit to Pantheon+ and DESI DR2 BAO prefers the low, Planck-side $`H_0 \approx 67.4`$ km/s/Mpc ($`H_0`$ is the fitted edge anchor, not a derived output), landing on the CMB side of the tension rather than the SH0ES side.

Systematic explanations have been scrutinized for a decade. The tension survives. It appears to be real.

Within MIT, the candidate resolution is structural. Both values can be represented as neighboring samples of the same Fibonacci well ($`\Theta_0 = 34/120`$), sampled at two different positions. The CMB measures the bare well. The local value corresponds to a one-step bosonic shift. What determines the size of that step is the lattice geometry (§II). The galactic trigger proposed to realize that shift is falsified by the SPARC test in §III.

## II. The Lattice Calculation

Independent of any galactic trigger, the lattice calculation asks what one bosonic step would do at the $`H_0`$ well.

The phase operator $`C(\Theta) = 2\sin^2(\pi\Theta)`$ (the anti-periodic first-positive mode intensity, normalized to unit mean) has a logarithmic slope that differs at each Fibonacci well:

```math
\frac{d\ln C}{d\Theta} = 2\pi\cot(\pi\Theta), \qquad \frac{\Delta C}{C} = \frac{d\ln C}{d\Theta} \times \Delta\Theta
```

where $`\Delta\Theta`$ is the step size (1/120 for dynamical observables, 2/120 for bosonic).

| Well | Θ | Slope sensitivity | Physical shift | Role |
|---|---|---|---|---|
| $`a_0`$ | 13/120 | 17.7 per step | None | Defines the transition threshold |
| $`H_0`$ | 34/120 | 5.1 per step | 8.4% | Measured through the field |
| Λ | 60/120 | 0 per step | 0% | Topologically protected at antinode |

$`\Lambda`$ at slope zero is immovable: topologically protected at the antinode. $`H_0`$ at slope 5.1 absorbs one bosonic step (2/120) as an 8.4% shift. The step size is 2/120 because $`H_0`$ is measured through photon redshifts (bosonic), accessing only the $`|I| = 60`$ projection of the full $`|2I| = 120`$ lattice.

$`a_0`$ at slope 17.7 marks a steep, sensitive well, but the phase field does not shift it. The lattice geometry fixes the well position at $`\Theta = 13/120`$. The scaling law produces $`a_0 = C(13/120) \cdot (\sqrt{\Omega_H})^{-1} \cdot a_P`$ as output. Its steep slope explains why the MOND transition is sharp in the lattice description: a binary on/off behavior rather than a gradual ramp. The failed trigger hypothesis tested in §III used this $`a_0`$ value to define the proposed coherence radius.

### The 8.4% displacement

At the bare well, $`\Theta_0 = 34/120`$:

```math
C(34/120) = 2\sin^2(34\pi/120) = 1.208
```

Shifted by one bosonic step, $`\Theta = 36/120`$:

```math
C(36/120) = 2\sin^2(36\pi/120) = 1.309
```

The ratio:

```math
\frac{C(36/120)}{C(34/120)} = \frac{1.309}{1.208} = 1.084
```

The bare well gives $`H_0 = 67.4`$ km/s/Mpc (the MIT phase-clock best-fit, consistent with Planck). Multiply by the ratio:

```math
67.4 \times 1.084 \approx 73 \;\text{km/s/Mpc}
```

This is the SH0ES-scale value. The 8.4% is an output of the lattice geometry at $`\Theta_0 = 34/120`$, produced by a step whose size is fixed at 2/120. No galactic physics enters this calculation.

## III. The Trigger Hypothesis and SPARC Test

The lattice calculation fixes the size of the required displacement. The remaining question is whether ordinary disk galaxies physically realize that displacement. The trigger below was proposed for that role, then tested against SPARC in a frozen pipeline and falsified.

### Phase decomposition

The sampled position on the 120-domain is the sum of two terms:

```math
\Theta = \Theta_0 + \Theta_f
```

$`\Theta_0 = 34/120`$ is the Fibonacci well for $`H_0`$, fixed by the lattice geometry. $`\Theta_f`$ is the environment-dependent offset. The CMB samples the bare well ($`\Theta_f = 0`$) because it records a phase epoch before local structure existed. In the trigger hypothesis, local observations sample $`\Theta_0 + \Theta_f`$ from inside a triggered galaxy.

### Coherence scale

The proposed coherence scale is set by the galactic rotation curve and the MOND acceleration:

```math
L_f = \frac{v_c^2}{a_0}
```

This is the galactocentric radius where the gravitational field drops to $`a_0`$. For the Milky Way ($`v_c \approx 220`$ km/s, $`a_0 \approx 1.2 \times 10^{-10}`$ m/s²): $`L_f \approx 13`$ kpc. In the trigger model, every calibrator inside this radius shares the same phase shift.

### Trigger and closure

The trigger index $`\mathcal{T}`$ compares the gravitational potential drop across $`L_f`$ to a critical value $`\mathcal{T}_c = 2\xi\,v_c^2/c^2`$, where $`\xi \approx 0.46`$ is the mean potential depth computed from standard halo profiles (isothermal, NFW, and Hernquist all give 0.44 to 0.47):

```math
\mathcal{T} = \frac{2}{c^2 L_f}\int_0^{L_f}\Phi_\text{rel}(l)\,dl
```

where $`\Phi_\text{rel}(l) \equiv \Phi(L_f) - \Phi(l)`$ is the potential difference from the coherence boundary (gauge-invariant). For a flat rotation curve, $`\Phi(r) = v_c^2\ln(r/r_0)`$, so $`\Phi_\text{rel}(l) = v_c^2\ln(L_f/l)`$. The integral evaluates exactly: $`\int_0^{L_f} v_c^2\ln(L_f/l)\,dl = v_c^2 L_f`$ (substituting $`u = l/L_f`$, $`\int_0^1 (-\ln u)\,du = 1`$). Therefore $`\mathcal{T} = 2v_c^2/c^2`$, and the ratio becomes independent of the galaxy.

The flat-curve evaluation is a special case of a general identity. For any circular rotation curve, $`v^2(r) = r\,d\Phi/dr`$, so

```math
\Phi_\text{rel}(l) = \Phi(L_f) - \Phi(l) = \int_l^{L_f}\frac{v^2(s)}{s}\,ds.
```

Switching the order of integration in $`\int_0^{L_f}\Phi_\text{rel}(l)\,dl`$ gives

```math
\int_0^{L_f}\Phi_\text{rel}(l)\,dl = \int_0^{L_f}v^2(l)\,dl.
```

Thus

```math
\mathcal{T} = \frac{2}{c^2 L_f}\int_0^{L_f}v^2(l)\,dl = \frac{2\langle v^2\rangle_{L_f}}{c^2},
```

where $`\langle v^2\rangle_{L_f}`$ is the radial mean-square circular velocity over the coherence interval $`[0, L_f]`$. For a flat curve, $`\langle v^2\rangle_{L_f} = v_c^2`$, recovering the result above. In that limit:

```math
\frac{\mathcal{T}}{\mathcal{T}_c} = \frac{1}{\xi} \approx 2.2
```

In the flat-curve limit, this is a closure identity. Both $`\mathcal{T}`$ and $`\mathcal{T}_c`$ scale as $`v_c^2`$; their ratio is galaxy-independent. Every flat-curve disk crosses the threshold by the same factor.

For a general rotation curve, the threshold ratio becomes

```math
\frac{\mathcal{T}}{\mathcal{T}_c} = \frac{\langle v^2\rangle_{L_f}}{\xi\,v_c^2}.
```

The flat-curve closure value $`1/\xi \approx 2.2`$ is therefore modified only by the ratio $`\langle v^2\rangle_{L_f}/v_c^2`$. For rising-to-flat curves this factor is below unity; for peaked or mildly declining curves it is computed directly from the observed profile. The trigger condition becomes the transparent inequality

```math
\frac{\langle v^2\rangle_{L_f}}{v_c^2} > \xi \approx 0.46
```

where $`v_c`$ is the outer flat-region velocity. In the trigger hypothesis, the phase field remains active whenever the mean-square velocity across the coherence interval exceeds roughly half the flat-curve value. The binary response is:

```math
\Theta_f = \frac{2}{120} \cdot \mathbf{1}(\mathcal{T} \geq \mathcal{T}_c)
```

One bosonic grid step or nothing. The step size 2/120 is the minimum observable shift on the 60R-grid. The full 120-lattice is set by $`\lvert 2I \rvert = 120`$ (binary icosahedral group on $`S^3`$); observation accesses the bosonic projection $`\lvert I \rvert = 60`$, so the smallest realized step is $`2/120 = 1/60`$.

### SPARC result

The coherence-scale trigger was tested against 123 quality-filtered SPARC rotation curves in a frozen, pre-registered pipeline ([dmobius3/phase-field](https://github.com/dmobius3/phase-field), archived at DOI: [10.5281/zenodo.20271702](https://doi.org/10.5281/zenodo.20271702)). The pipeline was locked before data contact and executed once.

The result falsifies the coherence-scale trigger mechanism. The observed transition-radius slope is 0.23 (registered interval: 0.7 to 1.3); the flat-onset slope is 0.33; the median $`r_t/L_f`$ is 0.38; and 53.7% of flat-curve galaxies fall below $`\mathcal{T}/\mathcal{T}_c = 1`$ (registered limit: 5%). All verdicts are stable across the registered 27-cell sensitivity grid.

The general identity makes the failure precise. Real SPARC rotation curves are not flat over $`[0, L_f]`$. For most disks, $`L_f`$ extends into the rising inner rotation curve, so $`\langle v^2\rangle_{L_f} < v_c^2`$. The typical mean-square suppression is near 0.41, below the trigger threshold $`\xi \approx 0.46`$. The flat-curve closure identity is not realized by the observed galaxy population.

No revised coherence scale is introduced here. Any replacement trigger must be derived independently and tested separately.

## IV. Propagation Model

The failed SPARC trigger does not invalidate the propagation logic; it removes the specific mechanism that was supposed to activate it. If an independently derived trigger is found, the shift would propagate through measurement classes as follows.

How much of the 8.4% reaches the final answer depends on where the absolute calibration is set. Two channels would transmit the displacement.

### Calibration inheritance

Local distance ladders anchor their absolute scale to calibrators inside a phase-active coherence domain. Every rung would inherit the full phase shift. The ruler itself would be shifted, so every distance measured with it would carry the 8.4%.

### Phase-domain averaging

Geometric methods (time-delay lensing, standard sirens) integrate $`1/H(z)`$ along the line of sight. The phase-shifted segment is only the local coherence domain; the rest of the path samples the bare well. For cosmological baselines ($`\chi \sim`$ Gpc), the local contribution is a fraction $`F = \chi_\text{local}/\chi \sim 10^{-5}`$. The direct averaging displacement is negligible (~ppm). If geometric methods return values above ~67, the source would be calibration inheritance through local priors in the analysis chain, not path averaging.

### Which mechanism applies where

| Method | Calibration | Channel | Expected H₀ if triggered |
|---|---|---|---|
| Cepheid/SN ladder (SH0ES) | Local anchors | Inheritance (full shift) | ~73 |
| TRGB | Local anchors | Inheritance (full shift) | ~73 |
| Megamasers | Local geometry | Inheritance (full shift) | ~73 |
| Time-delay lenses | Geometric, late-time | Averaging (negligible) | ~67 |
| Standard sirens | Geometric, late-time | Averaging (negligible) | ~67 |
| BAO + BBN | Early-universe ruler | Neither (bare well) | ~67 |
| CMB (Planck) | Early-universe physics | Neither (bare well) | ~67 |

The key distinction is where the absolute calibration is set. The CMB records a phase epoch before local structure existed ($`\Theta_f = 0`$ by construction). BAO and BBN use an early-universe ruler ($`r_d`$) that predates the phase field. In the trigger model, local ladders would import the full shift because their anchors sit inside the coherence domain. The propagation prediction is stratification: if a trigger exists, $`H_0`$ values should sort by calibration class rather than by a continuous environmental gradient.

## V. Test Outcomes

Two tests have been run against the phase-field predictions. The SPARC test (§III) addressed the trigger mechanism. The bimodality test addressed the downstream observable: whether $`H_0`$ measurements cluster into two discrete populations.

### [Trigger: falsified](https://github.com/dmobius3/mode-identity-theory/blob/main/files/framework/files/working/files/sparc-phase-field.md)

The coherence-scale trigger $`L_f = v_c^2/a_0`$ does not produce the predicted coherence radius in observed galaxies. The transition radius tracks $`L_f`$ at slope 0.23, not the registered 0.7 to 1.3. The closure identity fails for 53.7% of flat-curve galaxies. The failure is diagnosed by the general identity: real rotation curves are not flat over $`[0, L_f]`$, so the mean-square velocity falls below the trigger threshold.

### [Discrete H₀ structure: not supported](https://github.com/dmobius3/mode-identity-theory/blob/main/files/framework/files/working/files/h0-bimodality-test.md)

The original discrete-vs-continuous prediction was that $`H_0`$ should cluster at two quantized values (67 and 73) with a clean gap in between. An exploratory compilation of 18 published $`H_0`$ measurements (13 independent) was tested against this prediction.

| Pre-stated outcome | Observed |
|---|---|
| Continuous or intermediate spread rather than clean quantized clusters | Dip test cannot reject unimodality; intermediate values are present |
| Two clusters at wrong values | GMM gives 68.4 / 73.5 where it picks 2 components; BIC is a statistical tie |
| TRGB or JAGB land near 70 | TRGB/CCHP at 69.8, in the predicted gap |
| Local methods near 73, early-universe near 67 | Holds: class stratification is real |

The first three rows register against the discrete picture. The fourth holds, but method-class stratification is the Hubble tension restated, not evidence of a quantized step.

### What the tests do not address

The 8.4% lattice calculation (§II) is geometry. Neither test probes that calculation directly. The well sensitivity, the step size, and the arithmetic match to the observed tension scale are unaffected by the trigger failure or the bimodality result. What failed are the proposed physical realization of the step and the predicted discrete population structure in current $`H_0`$ compilations.

## VI. What Survives

The lattice calculation remains sharp: a one-step bosonic displacement from $`\Theta_0 = 34/120`$ to $`\Theta = 36/120`$ converts the bare value $`H_0 = 67.4`$ km/s/Mpc into $`H_0 \approx 73`$ km/s/Mpc through the phase-operator slope. That arithmetic is topology, not a fitted parameter, and neither test touches it.

What failed is the proposed galactic mechanism that would force ordinary disk galaxies to realize that displacement, and the predicted discrete two-population structure that realization would produce.

The physical realization of the 8.4% remains open: the lattice produces the right step size, but no tested trigger delivers it. Any future trigger must come from first principles, not from fitting to the data that falsified the previous one. The SPARC result constrains its form: any viable coherence scale likely has to be smaller than $`v_c^2/a_0`$ (the observed transition radius is roughly $`0.4\,L_f`$), and the closure identity must account for rising inner rotation curves rather than assuming flatness over the full interval. The bimodality result constrains its observable signature: current $`H_0`$ data does not show clean quantized clustering.

*The Hubble tension is real. The lattice arithmetic matches its scale. The mechanism remains open.*

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
