# CMB Anomalies from Topology

Three large-angle CMB features have persisted across COBE, WMAP, and Planck with no explanation within ΛCDM. The Möbius embedding in $S^3$ restricts the mode spectrum at large scales, breaks even-odd symmetry through the sign flip, and defines a preferred axis as the normal to the non-orientable surface. What has been called the "axis of evil" may be the universe revealing the geometry of its beginning.

**Three predictions**

| Feature | Predicted | Observed |
|---|---|---|
| Boundary | $\ell \sim 31$ | $\ell \lesssim 30$ |
| Parity sign | $R_{TT} < 1$ | $R_{TT} \approx 0.81$ |
| Alignment | $\sim 13^\circ$ | $\sim 10^\circ$ |

## I. The Anomalies

The cosmic microwave background provides a remarkably clean window into the early universe. Precision measurements from COBE, WMAP, and Planck have confirmed the standard cosmological model across a wide range of angular scales. Yet at the largest angles, multipoles $\ell < 30$, several unexpected features have persisted across all three missions.

**Low-ℓ Boundary.** The angular power spectrum shows less power at low ℓ than the best-fit ΛCDM model predicts. The deficit below $\ell \lesssim 30$ has been documented since COBE and confirmed with increasing precision by each successor.

**Parity asymmetry.** Odd-ℓ multipoles contain more power than even-ℓ multipoles at large scales. The Planck TT parity ratio $R_{TT}(30) \approx 0.81$, where unity indicates no preference, corresponding to a lower-tail probability of approximately 1%.

**Quadrupole-octupole alignment.** The preferred axes of the quadrupole ($\ell = 2$) and octupole ($\ell = 3$) align to within approximately 10°, an arrangement expected in only 1 to 3% of statistically isotropic realizations. This feature is sometimes called the "axis of evil," as though the cosmos owed us uniformity.

Each anomaly is modest in isolation, typically 2 to 3σ. Together, they suggest correlated large-angle structure that statistical isotropy does not anticipate. For two decades, each has been documented with increasing precision and labeled a fluke.

## II. The Geometry

Mode Identity Theory proposes nested topology: temporal edge bounds the Möbius surface, embedded in the hypersphere venue.

$$S^1 = \partial(\text{Mobius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset$$

The hierarchy terminates at $S^3$ because $\partial S^3 = \emptyset$. There is no boundary from which to observe further.

### Scale

The comoving circumference of the fundamental domain is $L \approx 2.1$ Gpc. One lap around the belt brings you to the flip side; two laps bring you home. The transverse width of the Möbius surface follows from the embedding geometry:

$$W = \frac{2L}{\pi} \approx 1.3 \; \text{Gpc}$$

### The Eigenspectrum

For scalar fields on the Möbius surface, Dirichlet boundary conditions at the strip edges (the boundary of the observable domain) set a minimum wavenumber. Modes below $k_\text{min}$ cannot fit inside the cavity.

$$k_\text{min} = \frac{\pi}{W} = \frac{\pi^2}{2L}$$

This is the geometric constraint that bounds the low-ℓ spectrum. The non-orientable identification (one lap flips the sign: $\psi(y + L) = -\psi(y)$) breaks even-odd symmetry. The surface normal defines the preferred axis. Three features, one topology.

## III. Three Predictions

The geometry of Section II implies specific features in the CMB power spectrum.

### A. Low-ℓ Boundary

A bounded cavity has a minimum wavelength. The boundary multipole follows from the eigenspectrum and the comoving distance to last scattering $\chi_\ast \approx 14$ Gpc. The spherical Bessel function $j_\ell(k\chi_\ast)$ peaks near $k\chi_\ast \approx \ell + 1/2$:

$$\ell_\text{cut} \approx k_\text{min} \cdot \chi_\ast - \tfrac{1}{2} = \frac{\pi^2}{2L} \cdot \chi_\ast - \tfrac{1}{2} \approx 31$$

Observed: deficit below $\ell \lesssim 30$.

### B. Parity Asymmetry

Non-orientable topology creates parity correlations without parity-violating microphysics. A signal traversing the identification picks up a sign flip from the twist, breaking even-odd symmetry. The COMPACT collaboration independently confirmed that non-orientable manifolds generically produce parity asymmetry of the observed sign.

Prediction: $R_{TT} < 1$ (odd preference). Observed: $R_{TT} \approx 0.81$.

### C. Quadrupole-Octupole Alignment

Low-ℓ eigenmodes inherit the twist axis; intrinsically, they align perfectly. The BAO sound horizon $r_d \approx 150$ Mpc is the largest coherent structure scale. The observer's fractional displacement within the fundamental domain is:

$$\Delta f = \frac{2r_d}{2L} = 0.071$$

The anti-periodic sign flip maps fractional displacement to frame rotation:

$$\Delta\theta = \pi \times 0.071 \approx 13^\circ$$

Observed: $\sim 10^\circ$.

## IV. On Matched Circles

Standard searches for cosmic topology look for matched circles in the CMB sky. Planck found none above the noise threshold. This null result is consistent: MIT's identification is temporal ($t = 0$), not spatial. The CMB is not an image viewed through topology; it is the resonant pattern of the bounded domain.

We do not see through the boundary because the boundary is the beginning. The CMB is the oldest light, still carrying the shape of the cavity.

## V. Discussion

### What Emerges from Geometry

**Boundary scale.** $W = 2L/\pi$ yields $\ell_\text{cut} \sim 31$, consistent with the observed low-ℓ power deficit.

**Parity preference.** The non-orientable identification produces odd-ℓ preference ($R_{TT} < 1$), consistent with Planck and with the COMPACT collaboration's general result that non-orientable manifolds break parity without parity-violating microphysics.

**Preferred axis.** The twist direction defines the axis; low-ℓ eigenmodes inherit it. The BAO-predicted displacement rotates the observed axis by $\sim 13^\circ$, consistent with the observed $\sim 10^\circ$.

These are not independent fits. They arise together from a topology whose parameters are set by independent considerations: the comoving circumference, spin-statistics, and mode structure.

### What Requires Further Work

**Parity magnitude.** The topology predicts the correct sign (odd preference). The quantitative coupling between displacement and parity ratio requires eigenmode computation on the Möbius surface.

**Axis sky direction.** The topology defines an axis; it does not specify its orientation in galactic coordinates. Matching the observed sky direction would require an independent physical constraint.

## VI. Falsification

This interpretation would be challenged if:

| Prediction | Falsified if |
|---|---|
| Boundary at $\ell \sim 31$ | Onset at $\ell \ll 20$ or $\ell \gg 40$ |
| Odd-ℓ preference | Even-ℓ preference observed |
| Quadrupole-octupole alignment | Axes orthogonal in refined measurements |

CMB-S4 and LiteBIRD will sharpen these tests.

---

**Three anomalies from one topology.** For two decades, each has been documented with increasing precision and labeled a fluke; however, these are not accidents, but three projections of one structure: a nested, non-orientable topology whose eigenspectrum shapes the largest angles of the CMB sky.

*Its axis not evil, the axis of light.*
