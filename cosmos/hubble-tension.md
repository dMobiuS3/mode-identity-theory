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

The Planck satellite infers $H_0 = 67.4 \pm 0.5$ km/s/Mpc from the cosmic microwave background at $z \approx 1100$. The SH0ES collaboration measures $H_0 = 73.0 \pm 1.0$ km/s/Mpc from Cepheid-calibrated Type Ia supernovae at $z \approx 0$. The gap is ~9%, persistent across independent local methods: Cepheids, tip of the red giant branch, surface brightness fluctuations, and megamasers.

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

The trigger index $\mathcal{T}$ compares the gravitational potential drop across $L_f$ to a critical value $\mathcal{T}_c = 2\xi\,v_c^2/c^2$, where $\xi \approx 0.46$ is the mean potential depth computed from standard halo profiles (isothermal, NFW, and Hernquist all give 0.44 to 0.47):

$$\mathcal{T} = \frac{2}{c^2 L_f}\int_0^{L_f}\Phi_\text{rel}(l)\,dl$$

where $\Phi_\text{rel}(l) \equiv \Phi(L_f) - \Phi(l)$ is the potential difference from the coherence boundary (gauge-invariant). For a flat rotation curve, $\Phi(r) = v_c^2\ln(r/r_0)$, so $\Phi_\text{rel}(l) = v_c^2\ln(L_f/l)$. The integral evaluates exactly: $\int_0^{L_f} v_c^2\ln(L_f/l)\,dl = v_c^2 L_f$ (substituting $u = l/L_f$, $\int_0^1 (-\ln u)\,du = 1$). Therefore $\mathcal{T} = 2v_c^2/c^2$, and the ratio becomes independent of the galaxy:

$$\frac{\mathcal{T}}{\mathcal{T}_c} = \frac{1}{\xi} \approx 2.2$$

This is a closure identity. Both $\mathcal{T}$ and $\mathcal{T}_c$ scale as $v_c^2$; their ratio is galaxy-independent. Every flat-curve disk crosses the threshold by the same factor. The response is binary: below threshold $\Theta_f = 0$; at or above it, one bosonic step ($\Theta_f = 2/120$).

The identity is robust to realistic rotation curves. The exact integral $\int_0^1(-\ln u)\,du = 1$ holds for a perfectly flat curve; deviations from flatness (rising inner regions, mild outer declines) perturb the integral at the few-percent level, leaving $\mathcal{T}/\mathcal{T}_c$ well above unity. The trigger margin ($\approx 2.2\times$ threshold) absorbs realistic profile variations without changing the binary outcome.

$$\Theta_f = \frac{2}{120} \cdot \mathbf{1}(\mathcal{T} \geq \mathcal{T}_c)$$

The step size $2/120$ is the minimum observable shift on the 60R-grid. The full 120-lattice is set by $\lvert 2I \rvert = 120$ (binary icosahedral group on $S^3$); observation accesses the bosonic projection $\lvert I \rvert = 60$, so the smallest realized step is $2/120 = 1/60$.

## III. Well Sensitivity

The closure identity guarantees the trigger fires. What determines the observable consequence is the logarithmic slope of the phase operator $C(\Theta) = 2\sin^2(\pi\Theta)$ (the anti-periodic ground mode intensity, normalized to unit mean) at each Fibonacci well:

$$\frac{d\ln C}{d\Theta} = 2\pi\cot(\pi\Theta), \qquad \frac{\Delta C}{C} = \frac{d\ln C}{d\Theta} \times \Delta\Theta$$

where $\Delta\Theta$ is the step size (1/120 for dynamical observables, 2/120 for bosonic).

The same step size produces different fractional shifts depending on where it lands:

| Well | Θ | Slope | Step | ΔC/C | Consequence |
|---|---|---|---|---|---|
| $a_0$ | 13/120 | 17.7 | 1/120 | ~15% | Constitutive: $a_0$ defines $\mathcal{T}_c$ and $L_f$ |
| $H_0$ | 34/120 | 5.1 | 2/120 | 8.4% | Hubble tension |
| Λ | 60/120 | 0 | 2/120 | 0% | Topologically protected at antinode |

The $a_0$ well sits on a steep slope; it absorbs a 15% shift from a single step (1/120). The step sizes differ because the two observables access the lattice differently. The full 120-lattice ($|2I| = 120$) contains both fermionic and bosonic representations. Dynamical observables like $a_0$ (measured through accelerations, which couple to the full gravitational field) resolve the full lattice; the minimum step is 1/120. Cosmographic observables like $H_0$ (measured through photon redshifts, which are bosonic) access only the bosonic projection $|I| = 60$; the minimum step doubles to 2/120.

The logical direction for $a_0$: the lattice geometry fixes the well position at $\Theta = 13/120$ and the step size at 1/120. These produce $a_0$ as an output of the scaling law. That value of $a_0$ then enters the coherence scale $L_f = v_c^2/a_0$ and the threshold $\mathcal{T}_c$, which determine whether the phase field triggers. The well defines the observable; the observable defines the trigger. There is no circularity because the lattice comes first.

The Λ well sits at the antinode where the slope vanishes; the cosmological constant is topologically immune to the phase field. The $H_0$ well sits between: steep enough to produce a measurable shift, shallow enough that it remains a perturbation.

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

The phase field shifts $H_0$ measurements differently depending on calibration class. How much of the 8.4% reaches the final answer depends on where the absolute calibration is set. Two channels transmit the bias.

### Calibration inheritance

Local distance ladders anchor their absolute scale to calibrators inside the coherence domain ($L_f \approx 13$ kpc). Every rung inherits the full phase shift. The ruler itself is biased, so every distance measured with it carries the 8.4%.

### Phase-domain averaging

Geometric methods (time-delay lensing, standard sirens) integrate $1/H(z)$ along the line of sight. The phase-shifted segment is only the local coherence domain; the rest of the path samples the bare well. For cosmological baselines ($\chi \sim$ Gpc), the local contribution is a fraction $F = \chi_\text{local}/\chi \sim 10^{-5}$. The direct averaging bias is negligible (~ppm). If geometric methods return values above ~67, the source would be calibration inheritance through local priors in the analysis chain, not path averaging.

### Which mechanism applies where

| Method | Calibration | Channel | Expected H₀ |
|---|---|---|---|
| Cepheid/SN ladder (SH0ES) | Local anchors | Inheritance (full shift) | ~73 |
| TRGB | Local anchors | Inheritance (full shift) | ~73 |
| Megamasers | Local geometry | Inheritance (full shift) | ~73 |
| Time-delay lenses | Geometric, late-time | Averaging (negligible) | ~67 |
| Standard sirens | Geometric, late-time | Averaging (negligible) | ~67 |
| BAO + BBN | Early-universe ruler | Neither (bare well) | ~67 |
| CMB (Planck) | Early-universe physics | Neither (bare well) | ~67 |

The key distinction is where the absolute calibration is set. The CMB records a phase epoch before local structure existed ($\Theta_f = 0$ by construction). BAO and BBN use an early-universe ruler ($r_d$) that predates the phase field. Local ladders import the full shift because every anchor sits inside the coherence domain.

The prediction is stratification: $H_0$ values should sort by calibration class, with locally-anchored methods clustering near 73 and early-universe methods clustering near 67. Current TDCOSMO time-delay results sit near 73, above the predicted ~67 for geometric methods. The phase field interpretation is that these analyses inherit local priors (lens model calibrations anchored to local distance scales) rather than measuring the bare well directly. If future analyses with purely geometric calibration (no local anchors) still return ~73, the averaging prediction is falsified.

## V. Falsification

The phase field produces a discrete prediction. Local $H_0$ should cluster at quantized values set by the lattice, not vary continuously with environment. The sharpest test is the discrete-vs-continuous fork.

| Observation | Implication |
|---|---|
| Local $H_0$ fills 67 to 73 continuously | Quantized $\Theta_f$ is wrong |
| Local ladders cluster near 73, independent of host environment | Supports quantized response |
| Geometric methods return ~67 regardless of environment | Supports negligible averaging bias |
| Void-embedded calibrators return $H_0 \approx 70 \pm 1$ | Intermediate state exists; $2/120$ step is incomplete |
| Environment-binned $H_0$ shows smooth gradient | Phase field is continuously sourced, not triggered |

The test is operational now. Ladder calibrations built from hosts in void-like vs overdense regions, late-time geometric methods binned by environment, and histograms of $H_0$ tested for bimodality vs continuous spread all probe the fork directly.

The MIT prediction: all disk galaxies with developed halos select the same quantized state. The $H_0$ distribution should be bimodal (CMB-anchored at ~67, locally-calibrated at ~73), not a continuous spread.

---

Both measurements are correct. The CMB samples the Fibonacci well at $\Theta_0 = 34/120$. Local distance ladders sample from inside a triggered galaxy, shifted by one bosonic step to $\Theta = 36/120$. The closure identity guarantees the trigger fires for every flat-curve disk. The slope of the phase operator at that well converts the step into 8.4%.

*The Hubble tension is phase field mechanics.*
