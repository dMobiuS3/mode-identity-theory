/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Calibration Structure (draft for the framework engine)

**Dependencies:** a0 paper Appendix A.2 (selection rule), first positive eigenvalue $`2/R^2`$, scaling law.

**Notation.** Use $`\sqrt{\Omega}`$ where a quantity dilutes from the observer, since the observer sits at $`\sqrt{\Omega} = R/\ell_P`$: the master law and the mass elevator. Use bare $`\Omega`$ when stating the hierarchy as a quantity (its definition, its value) and for the coupling grid step $`\Omega^{-1/|\mathrm{grid}|}`$, which quantizes the full $`\Omega`$ rather than diluting from the observer. In these framework pages $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2 \approx 10^{122}`$ is the surface hierarchy, the native ledger variable. The cosmological vacuum density fraction $`\rho_\Lambda/\rho_c \approx 0.685`$ is a different quantity, about 122 orders away, and is written $`f_\Lambda`$ when disambiguation is needed. The distance-fit pages state the FLRW background in conventional ΛCDM notation, where that fraction is $`\Omega_\Lambda`$; each says so and identifies its $`\Omega_\Lambda`$ with $`f_\Lambda`$.

---

## Calibration Structure

The framework is a calibration scheme, not an oracle that produces every absolute scale without input. One measured reference observable anchors each sector's normalization. What the framework supplies are the sector exponents, grid assignments, well locations, and dimensionless ratios. In other words, the measured anchor fixes the ruler; the topology fixes where the marks on the ruler fall.

This is the same logic used throughout effective physical theory. The Standard Model does not derive the numerical values of the gauge couplings from first principles; it measures them at reference scales and predicts how they run and relate across processes. In the same way, $`H_0`$ is not a failed prediction when it is used as the edge-sector anchor. It plays the role of a measured reference input. The prediction is not the existence of a number called $`H_0`$; the prediction is that the same calibrated edge hierarchy also fixes $`a_0`$ through a parameter-free ratio.

| Sector | Locus | Hierarchy | Anchor | Status |
|---|---|---|---|---|
| Edge $`(n=1)`$ | $`S^1`$ boundary; kinematic locus, no intrinsic eigenvalue | $`\Omega_H = (c/H\ell_P)^2`$ | $`H_0`$ measured | Live |
| Surface $`(n=2)`$ | Möbius strip; carries first positive eigenvalue $`2/R^2`$ | $`\Omega_\Lambda = (R/\ell_P)^2`$ | $`\Lambda`$ measured, fixing $`R`$ (and $`\Omega_\Lambda`$ once the Planck scale is set) | Live as calibration |
| Space $`(n=3)`$ | $`S^3`$ slice; inherits surface eigenvalue | $`\Omega_\Lambda`$ | Via surface sector | Live with surface |
| Mass | 120-wells, McKay distance, torsion | $`\mu_\Lambda`$ and $`(\sqrt{\Omega_\Lambda})^{\mathrm{dist}/30}`$ | $`\Omega_\Lambda`$ from surface; one mass-sector normalization if needed | Live |
| Couplings | Grid wells and fractional hierarchy steps | $`\Omega_\Lambda^{-1/60}`$, $`\Omega_\Lambda^{-1/120}`$ | $`\Omega_\Lambda`$ from surface | Live |

The prediction/calibration split is sector-by-sector. In the edge sector, the measured value of $`H_0`$ calibrates the edge hierarchy. The acceleration scale then follows from the ratio of wells:

```math
\frac{a_0}{cH_0}=\frac{C(13/120)}{C(34/120)}.
```

Thus $`H_0`$ is the anchor, while $`a_0/H_0`$ is the prediction.

In the surface sector, the eigenvalue statement remains intact. The first positive eigenvalue is

```math
\frac{2}{R^2},
```

with the ground state the extension-dependent zero mode (Friedrichs zero gives the $`m_h = 0`$ background).

What failed was the independent over-determination of $`R`$ through the CMB-Molien path. Without an independent value of $`R`$, that path no longer predicts $`\Lambda`$ absolutely; two other routes do (below). Instead, measured $`\Lambda`$ calibrates the surface radius $`R`$ through $`\Lambda = 3/R^2`$, and hence the surface hierarchy

```math
\Omega_\Lambda = (R/\ell_P)^2
```

once the Planck scale is fixed by the second dial.

The eigenvalue structure survives; the absolute surface radius is the open piece. Two paths return $`\Lambda`$ to a prediction. The first anchors on measured $`\alpha`$: it fixes $`\Omega_\Lambda`$ directly, needs no independent $`R`$, and returns $`\Lambda\ell_P^2`$ to within 24%. The second is the mass-spectrum route, where two masses at different McKay distances overdetermine $`R`$ but currently land $`\Lambda`$ about 14x low. The coupling route is the tighter of the two; the gap between them is an open consistency item. See the two-dial reading below.

More fully, the scaling law has one hierarchy variable $`\Omega_\Lambda`$ with three independent readings of it. Inverting any one fixes $`\Omega_\Lambda`$ and predicts the rest; which one you invert is calibration, the relationships between them are physics:

| Anchor | Reads $`\Omega_\Lambda`$ from | $`\Lambda`$ | $`\alpha`$ | Role |
|---|---|---|---|---|
| Measured $`\Lambda`$ (sets $`R`$) | the radius $`R`$ | circular | 0.5% | current default |
| Measured $`\alpha`$ | the coupling | 24% (genuine) | circular | best-conditioned |
| Mass spectrum ($`m_\mu/m_e`$) | the mass ratio | ~14x (genuine) | ~few % | independent cross-check |

The three readings are one inversion through the same 60-fold lever; they differ only in input conditioning ($`\alpha`$ to ~0.5%, the mass ratio to ~4.5%), so the ~10x spread between the $`\alpha`$ and mass-spectrum values for $`\Lambda`$ is a mass-formula precision limit, not a structural inconsistency.

This localizes the blast radius. Losing the independent CMB-Molien anchor demotes exactly one claim: $`\Lambda`$ is no longer an absolute prediction. It becomes the measured surface-sector calibration input. Downstream mass and coupling calculations do not collapse, because they require the value of $`\Omega_\Lambda`$, which is fixed once $`R`$ (from measured $`\Lambda`$) and the Planck scale (the second dial) are specified. The McKay mass elevator uses powers of $`\sqrt{\Omega_\Lambda}`$; the gauge couplings use fractional powers of $`\Omega_\Lambda`$ such as $`\Omega_\Lambda^{-1/60}`$. They do not require $`R`$ to be independently predicted, only consistently calibrated.

The edge sector is untouched by this correction. It references $`\Omega_H`$, not $`\Omega_\Lambda`$, and is anchored by $`H_0`$. The surface and space sectors reference $`\Omega_\Lambda`$, now set through measured $`\Lambda`$ (which fixes $`R`$) and the Planck scale. The mass and coupling sectors inherit that calibrated hierarchy. Thus the correction does not propagate as a global failure; it changes the status of one surface-sector claim from prediction to calibration.

This also clarifies the role of measured inputs. The framework predicts structural relations: the integer floors $`n=1,2,3`$, the McKay exponents, the grid fractions, the well assignments, and the dimensionless ratios between observables at the same depth, where the hierarchy factor cancels. It does not claim that every absolute normalization is derived without empirical reference. A measured anchor per sector is part of the calibration architecture. $`\mu_\Lambda = \rho_\Lambda^{1/4}`$ is the vacuum floor inherited from the calibrated surface sector; $`m_e`$ is a mass-sector normalization/benchmark, not a second vacuum floor.

The status is therefore honest. The selection rules and well assignments were fixed before this calibration reinterpretation, so the downstream agreements are not produced by retuning them after the fact. But the selection rule itself remains a postulate of the framework, not yet a theorem derived from the topology alone. A first-principles derivation from the Hurwitz/Fibonacci structure of the 120-domain remains open.

---

## Proposed Inputs table patch

Replaces the current "Measured scales" table in the engine.

| Input | Role | Status |
|---|---|---|
| $`H_0`$ | Edge-sector anchor; fixes $`\Omega_H`$ | Measured calibration |
| $`\Lambda`$ | Surface-sector anchor; fixes $`R`$ through $`\Lambda = 3/R^2`$ | Measured calibration |
| $`\alpha`$ | Alternative surface anchor; measured $`\alpha`$ fixes $`\Omega_\Lambda`$ directly | Measured (dimensionless); returns $`\Lambda\ell_P^2`$ as a prediction to 24% |
| $`R`$ | Surface radius in the first positive eigenvalue $`2/R^2`$ and $`\Omega_\Lambda=(R/\ell_P)^2`$ | Calibrated from $`\Lambda`$ today; measured $`\alpha`$ pins $`\Omega_\Lambda`$ (hence $`R`$) to 24%, and the mass-spectrum route (two masses at different distances) is a further, looser path to an independent $`R`$ |
| $`m_e`$ or one measured mass | Mass-sector normalization / second dial for the mass-gravity system | Measured calibration or benchmark |

---

## Mass/gravity reading: the two dials (draft for the-waltz.md §II)

The mass-and-gravity sector is one closed system. The topology fixes the dimensionless ratios between observables at the same depth; two dimensionful dials, $`\Lambda`$ (equivalently $`R`$) and $`G`$, set the absolute scales. Ratios across depths carry $`R`$, which is what lets the spectrum read $`R`$ back. The mass-spectrum reading and the gravity-constant reading are the same system read from different dials, not competing claims.

| Anchors used | Solves for | Reading |
|---|---|---|
| $`\Lambda`$ and $`G`$ | Absolute fermion masses | Mass-spectrum reading |
| $`\Lambda`$ and one measured mass | $`G`$ and the remaining masses | Gravity-constant reading |
| Two masses at different McKay distances | $`R`$, hence $`\Lambda`$ as a prediction, and $`G`$ | R-from-spectrum reading (open; needs the $`(\rho,\sigma)\to(T_3,Y)`$ rule) |
| Measured $`\alpha`$ (dimensionless) | $`\Omega_\Lambda`$, hence $`\Lambda\ell_P^2`$ as a prediction | $`\alpha`$ route; $`\Lambda\ell_P^2 \propto \alpha^{60}`$, within 24% (the 60-fold lever) |
| Same-distance or same-exponent ratios | $`m_i/m_j`$ at fixed distance; $`\alpha_s/\alpha_W`$ | Anchor-free structural core |

The anchor-free core is narrower than "all ratios." A mass ratio drops the overall floor $`\mu_\Lambda`$, which cancels in any ratio, but it keeps the McKay elevator $`(\sqrt{\Omega_\Lambda})^{\mathrm{dist}/30}`$ unless both particles sit at the same distance. Across distances the elevator survives, so the ratio carries $`(R/\ell_P)^{\Delta\mathrm{dist}/30}`$, and the mass hierarchy itself is that surviving factor. The same holds in the coupling sector: $`\alpha_s/\alpha_W`$ is anchor-free because both forces share the confinement grid, while $`\alpha_s/\alpha_{EM}`$ carries $`R`$ because the grids differ. So the genuinely anchor-free predictions are the same-depth ratios, and the cross-depth ratios are the lever for reading $`R`$.

Key phrase: **same two-dial system, different readout.**

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
