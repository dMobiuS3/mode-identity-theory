# H₀ Local: Hubble Tension as Phase Field

Measurements of the Hubble constant have split into two persistent camps: the cosmic microwave background gives 67.4 km/s/Mpc; local distance ladders give 73. The discrepancy survives every systematic check and every independent method. Mode Identity Theory resolves the tension through the phase field: observers embedded in galactic structure sample from a shifted position on the 120-domain. The shift is one bosonic step, $\Theta_f = 2/120$, and the logarithmic slope of the phase operator at the $H_0$ well converts that step into an 8.4% increase. Both measurements are correct. They sample different positions on the same wave.

**Phase field shift at the H₀ well**

| Quantity | Value |
|---|---|
| Phase shift | $\Theta_f = 2/120$ (one bosonic step) |
| $\Delta C/C$ at $H_0$ well | 8.4% |
| Predicted local $H_0$ | 67.4 x 1.084 ≈ 73 km/s/Mpc |
| Closure identity | $\mathcal{T}/\mathcal{T}_c = 1/\xi \approx 2.2$ (universal) |

## I. The Tension

The Planck satellite infers $H_0 = 67.4 \pm 0.5$ km/s/Mpc from the cosmic microwave background at $z \approx 1100$. The SH0ES collaboration measures $H_0 = 73.0 \pm 1.0$ km/s/Mpc from Cepheid-calibrated Type Ia supernovae at $z \approx 0$. The gap is ~9%, persistent across five independent local methods: Cepheids, tip of the red giant branch, surface brightness fluctuations, megamasers, and time-delay lensing.

Systematic explanations have been scrutinized for a decade. The tension survives. It appears to be real.

Within MIT, the resolution is structural. Both values emerge from the same Fibonacci well ($\Theta_0 = 34/120$), sampled at two different positions. The CMB measures the bare well. Local observations measure the well shifted by one bosonic step. The difference is fixed by the lattice, not fitted to the data.

## II. The Phase Field

The scaling law produces cosmic observables from Fibonacci well positions on the 120-domain. Phase field mechanics extends this to galactic observables: when an observer sits inside a disk galaxy with a flat rotation curve, the sampling position shifts.

### Phase decomposition

The sampled position on the 120-domain is the sum of two terms:

$$\Theta = \Theta_0 + \Theta_f$$

$\Theta_0 = 34/120$ is the Fibonacci well for $H_0$, fixed by the lattice geometry. $\Theta_f$ is the environment-dependent offset. The CMB samples the bare well ($\Theta_f = 0$) because it records a phase epoch before local structure existed. Local observations sample $\Theta_0 + \Theta_f$ from inside a triggered galaxy.

### Coherence scale

The phase field is coherent over a scale set by the galactic rotation curve and the MOND acceleration:

$$L_f = \frac{v_c^2}{a_0}$$

This is the galactocentric radius where the gravitational field drops to $a_0$. For the Milky Way ($v_c \approx 220$ km/s, $a_0 \approx 1.2 \times 10^{-10}$ m/s²): $L_f \approx 13$ kpc. Every calibrator inside this radius shares the same phase shift.

### Trigger and closure

The trigger index $\mathcal{T}$ and critical threshold $\mathcal{T}_c$ are:

$$\mathcal{T} = \frac{2v_c^2}{c^2}, \qquad \mathcal{T}_c = \frac{2\xi\,v_c^2}{c^2}, \quad \xi \approx 0.46$$

The ratio is independent of the galaxy:

$$\frac{\mathcal{T}}{\mathcal{T}_c} = \frac{1}{\xi} \approx 2.2$$

This is a closure identity. It holds for any flat-curve disk galaxy regardless of mass, radius, or rotation speed. Every such galaxy exceeds the threshold. The response is binary: one bosonic step ($\Theta_f = 2/120$), or nothing.

$$\Theta_f = \frac{2}{120} \cdot \mathbf{1}(\mathcal{T} \geq \mathcal{T}_c)$$

The step size $2/120$ is the minimum observable shift on the 60R-grid. The full 120-lattice is set by $\lvert 2I \rvert = 120$ (binary icosahedral group on $S^3$); observation accesses the bosonic projection $\lvert I \rvert = 60$, so the smallest realized step is $2/120 = 1/60$.

## III. Well Sensitivity

The closure identity guarantees the trigger fires. What determines the observable consequence is the logarithmic slope of the phase operator at each Fibonacci well:

$$\frac{d\ln C}{d\Theta} = 2\pi\cot(\pi\Theta), \qquad \frac{\Delta C}{C} = \frac{d\ln C}{d\Theta} \times \frac{2}{120}$$

The same step size produces different fractional shifts depending on where it lands:

| Well | Θ | Slope | ΔC/C | Consequence |
|---|---|---|---|---|
| $a_0$ | 13/120 | 17.7 | 30% | Constitutive: $a_0$ defines $\mathcal{T}_c$ and $L_f$ |
| $H_0$ | 34/120 | 5.1 | 8.4% | Hubble tension |
| Λ | 60/120 | 0 | 0% | Topologically protected at antinode |

The $a_0$ well sits on a steep slope; it absorbs a 30% shift, which is what makes it constitutive (it defines the threshold itself). The Λ well sits at the antinode where the slope vanishes; the cosmological constant is topologically immune to the phase field. The $H_0$ well sits between: steep enough to produce a measurable shift, shallow enough that it remains a perturbation.

### The numerical closure

At the bare well, $\Theta_0 = 34/120$:

$$C(34/120) = 2\sin^2(34\pi/120) = 1.208$$

Shifted by one bosonic step, $\Theta = 36/120$:

$$C(36/120) = 2\sin^2(36\pi/120) = 1.309$$

The ratio:

$$\frac{C(36/120)}{C(34/120)} = \frac{1.309}{1.208} = 1.084$$

Planck gives $H_0 = 67.4$ km/s/Mpc at the bare well. Multiply by the ratio:

$$67.4 \times 1.084 \approx 73 \;\text{km/s/Mpc}$$

This matches SH0ES. The 8.4% is an output of the lattice geometry at $\Theta_0 = 34/120$, produced by a step whose size is fixed at $2/120$.

## IV. Method Classification

The phase field does not shift all $H_0$ measurements equally. How much of the 8.4% reaches the final answer depends on where the absolute calibration is set. Two channels transmit the bias.

### Calibration inheritance

Local distance ladders anchor their absolute scale to calibrators inside the coherence domain ($L_f \approx 13$ kpc). Every rung inherits the full phase shift. The ruler itself is biased, so every distance measured with it carries the 8.4%.

### Phase-domain averaging

Geometric methods (time-delay lensing, standard sirens) integrate $1/H(z)$ along the line of sight. The phase-shifted segment is only the local coherence domain; the rest of the path samples the bare well. For cosmological baselines ($\chi \sim$ Gpc), the local contribution is a fraction $F = \chi_\text{local}/\chi \sim 10^{-5}$. The bias dilutes over the long baseline.

### Which mechanism applies where

| Method | Calibration | Channel | Expected H₀ |
|---|---|---|---|
| Cepheid/SN ladder (SH0ES) | Local anchors | Inheritance (full shift) | ~73 |
| TRGB | Local anchors | Inheritance (full shift) | ~73 |
| Megamasers | Local geometry | Inheritance (full shift) | ~73 |
| Time-delay lenses | Geometric, late-time | Averaging (partial shift) | Intermediate |
| Standard sirens | Geometric, late-time | Averaging (partial shift) | Intermediate |
| BAO + BBN | Early-universe ruler | Averaging (minimal shift) | ~67 |
| CMB (Planck) | Early-universe physics | Neither (bare well) | ~67 |

The key distinction is where the absolute calibration is set, not the redshift of the observed object. The CMB does not average over $\Theta_f$; it records a phase epoch where local structure had not yet developed. BAO and BBN use an early-universe ruler ($r_d$) that predates the phase field. Local ladders import the full shift because every anchor sits inside the coherence domain.

The prediction is stratification: $H_0$ values should sort by calibration class, with locally-anchored methods clustering near 73 and early-universe methods clustering near 67.

## V. Falsification

The phase field produces a discrete prediction. Local $H_0$ should cluster at quantized values set by the lattice, not vary continuously with environment. The sharpest test is the discrete-vs-continuous fork.

| Observation | Implication |
|---|---|
| Local $H_0$ fills 67 to 73 continuously | Quantized $\Theta_f$ is wrong |
| Local ladders cluster near 73, independent of host environment | Supports quantized response |
| Geometric methods drift toward 67 with increasing $z$ | Supports phase-domain averaging |
| Void-embedded calibrators return $H_0 \approx 70 \pm 1$ | Intermediate state exists; $2/120$ step is incomplete |
| Environment-binned $H_0$ shows smooth gradient | Phase field is continuously sourced, not triggered |

The test is operational now. Ladder calibrations built from hosts in void-like vs overdense regions, late-time geometric methods binned by environment, and histograms of $H_0$ tested for bimodality vs continuous spread all probe the fork directly.

The MIT prediction: all disk galaxies with developed halos select the same quantized state. The $H_0$ distribution should be bimodal (CMB-anchored at ~67, locally-calibrated at ~73), not a continuous spread.

---

Both measurements are correct. The CMB samples the Fibonacci well at $\Theta_0 = 34/120$. Local distance ladders sample from inside a triggered galaxy, shifted by one bosonic step to $\Theta = 36/120$. The closure identity guarantees the trigger fires for every flat-curve disk. The slope of the phase operator at that well converts the step into 8.4%.

*The Hubble tension is not a measurement disagreement. It's phase field mechanics.*
