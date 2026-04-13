/ **[`framework/`](../../framework/)** / **[`cosmos/`](../../cosmos/)** / **[`spectrum/`](../../spectrum/)** /

---

# a₀ Evolving: High-Redshift Galaxy Masses

James Webb has found galaxies too massive, too early. Stellar masses of $\sim 10^{10}\,M_\odot$ within 600 Myr of the Big Bang require star formation efficiencies exceeding unity under ΛCDM, a physical impossibility. 

Mode Identity Theory predicts that the MOND acceleration scale $a_0$ is an edge mode ($n = 1$) referencing the evolving Hubble horizon: $a_0(z) = a_0(0) \times H(z)/H_0$. At $z = 10$, this gives $a_0 \approx 20 \times$ the local value, enhancing gravitational binding and accelerating structure formation without new physics.

Critically, MIT predicts $a_0$ evolves while Λ remains fixed: the inverse of standard assumptions. Both predictions are independently testable.

**Edge mode scaling**

| Quantity | Value |
|---|---|
| Scaling law | $a_0(z) = a_0(0) \times H(z)/H_0$ |
| $a_0/(cH_0)$ ratio | predicted: 0.184 / observed: 0.183 |
| At $z = 10$ | $a_0 \approx 2.4 \times 10^{-9}$ m/s<sup>2</sup> (20x local) |
| Binding enhancement | $\sqrt{20} \approx 4.5$ x (collapse ~2.1x faster) |

## I. The Observational Tension

Observations by Labbé et al. reveal stellar masses $M_\star \sim 10^{10}\,M_\odot$ formed within ~600 Myr after the Big Bang. These masses approach or exceed the maximal baryon abundance permitted in standard dark matter halos under ΛCDM, creating the "impossibly early galaxy" problem. Resolving this within standard physics requires star formation efficiencies exceeding unity, a physical impossibility suggesting either systematic observational errors or incomplete theoretical understanding.

## II. Epoch-Dependent Acceleration Scale

Standard MOND treats $a_0 \approx 1.2 \times 10^{-10}$ m/s<sup>2</sup> as a fundamental constant. The observed coincidence $a_0 \approx cH_0$ suggests a connection to horizon physics. Within MIT, both $a_0$ and $H_0$ are edge modes ($n = 1$) referencing the Hubble horizon. The Planck acceleration $a_P = c/t_P = 5.56 \times 10^{51}$ m/s<sup>2</sup> is the reference scale, and $C(\Theta) = 2\sin^2(\pi\Theta)$ is the phase operator (derived from the anti-periodic ground mode on the Möbius surface, normalized to unit mean). The scaling law gives:

$$\frac{a_0}{a_P} = C(13/120) \cdot (\sqrt{\Omega_H})^{-1}, \qquad \frac{H_0}{t_P^{-1}} = C(34/120) \cdot (\sqrt{\Omega_H})^{-1}$$

Since both reference the same $(\sqrt{\Omega_H})^{-1}$, the ratio is parameter-free: $a_0/(cH_0) = C(13/120)/C(34/120) = 0.223/1.208 = 0.184$. With $H_0 = 67.4$ km/s/Mpc (Planck 2018), $cH_0 = 6.55 \times 10^{-10}$ m/s<sup>2</sup>, giving observed $a_0/(cH_0) = 1.2/6.55 = 0.183$.

The phase coefficient $C(\Theta)$ occupies a Fibonacci stability well, a topological feature motivating epoch-independence. The scaling relation follows:

$$a_0(z) = a_0(0) \times \frac{H(z)}{H_0}$$

## III. Quantitative Estimate at z = 10

For a standard flat cosmology with $\Omega_m \approx 0.3$ (total gravitating matter density inferred from expansion data; MIT does not modify the expansion history, only galactic-scale dynamics via the $a_0$ threshold) and $\Omega_\Lambda \approx 0.7$:

$$\frac{H(z)}{H_0} = \sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$$

At $z = 10$: $(1+z)^3 = 1331$, giving $\Omega_m(1+z)^3 + \Omega_\Lambda = 0.3(1331) + 0.7 \approx 400$.

$$\frac{H(z{=}10)}{H_0} = \sqrt{400} = 20$$

Applying the scaling:

$$a_0(z{=}10) \approx 20 \times a_0(0) \approx 2.4 \times 10^{-9} \;\text{m/s}^2$$

## IV. Implications for Structure Formation

In the deep-MOND regime ($g \ll a_0$), effective gravitational acceleration scales as $g_\text{eff} \propto \sqrt{g_N \times a_0}$. Comparing epoch-dependent $a_0$ to the standard constant assumption:

$$\frac{g_\text{eff}(z{=}10)}{g_\text{eff}(\text{standard})} = \sqrt{\frac{a_0(z{=}10)}{a_0(0)}} = \sqrt{20} \approx 4.5$$

A factor of ~4.5 enhancement in effective gravitational binding significantly alters collapse dynamics. This comparison is at fixed epoch: both MIT and constant-$a_0$ MOND face identical expansion rates at $z = 10$; the difference is solely the effective gravitational acceleration. Since free-fall timescale scales as $t_\text{ff} \propto 1/\sqrt{g}$, structures at $z = 10$ could collapse approximately 2.1x faster than standard MOND would predict. For the Labbé et al. observations requiring $\varepsilon_\text{SF} > 1$ under standard assumptions, the 2.1x faster collapse approximately halves the required star formation rate to assemble the same stellar mass, reducing the implied efficiency to $\varepsilon_\text{SF} \sim 0.5$, within the physically permitted range.

## V. Contrasting Predictions

MIT's dimensional hierarchy makes a sharp distinction between edge modes and surface modes:

| Observable | $n$ | $\Omega_\text{ref}$ | Prediction |
|---|---|---|---|
| $a_0$ (acceleration) | 1 | $\Omega_H$ (evolves) | Scales with $H(z)$ |
| Λ (cosmo. const.) | 2 | $\Omega_\Lambda$ (fixed) | Constant across epochs |

This is an inversion of standard assumptions, where Λ is often treated as potentially evolving while $a_0$ is assumed constant. Observations of both quantities at high redshift provide independent, complementary tests.

## VI. Falsification

| Prediction | Test | Falsified if |
|---|---|---|
| $a_0(z) \propto H(z)$ | Rotation curves at $z > 2$ | $a_0(z)/a_0(0) = 1$ at ≥2σ |
| Λ constant | SNe Ia / BAO at high $z$ | Λ evolves while $a_0$ stays constant |

At $z = 2$, the prediction is $a_0(z{=}2) \approx 3 \times a_0(0)$. These predictions distinguish MIT from both standard MOND (constant $a_0$) and ΛCDM (no acceleration threshold).

---

In 1983, Milgrom identified $a_0$ as a fundamental acceleration scale. Four decades the coincidence $a_0 \approx cH_0$ had no explanation. Both are edge modes; the ratio is fixed by where they sit on the standing wave. $a_0$ evolves with $H(z)$.

*The galaxies found too early were simply formed under a stronger age.*

---

/ **[`framework/`](../../framework/)** / **[`cosmos/`](../../cosmos/)** / **[`spectrum/`](../../spectrum/)** /
