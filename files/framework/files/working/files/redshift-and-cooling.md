/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Redshift and Cooling

How a static universe reddens light and cools a thermal bath, both read off the temporal budget's state $`S`$. Redshift is the phase-ratio mechanism; cooling is that same ratio applied to a blackbody.

**Status:** Redshift mechanism in outline (the phase ratio on the standing wave); the full derivation from the postulate to the observed $`H(z)`$ is partially walked. Cooling is ESTABLISHED as a kinematic equivalence with the FLRW thermal law. Both are readings of the temporal budget; the distance side rides on the Waltz clock.

**Dependencies:** Temporal budget identity $`\Psi^2 + S^2 = 1`$; the standing wave $`\Psi = \cos(t/2)`$ on the temporal edge; the Waltz clock (distances).

**Related:** [The Budget Map](budget-map.md), [The Temporal Budget Identity](temporal-budget.md), [Entropy as Realization Budget](entropy-as-realization-budget.md), [Dark Energy](../../../../cosmos/files/dark-energy.md) (the distance-redshift relation), [The Waltz](../../../../spectrum/files/the-waltz.md).

---

## I. Redshift is a phase ratio

The space is static. What advances is the observer's phase along the standing wave on the Möbius temporal edge. A photon emitted at phase $`t_\text{emit}`$ and observed at phase $`t_\text{obs}`$ is reddened by the ratio of the realization amplitude $`S = \sin(t/2)`$ at the two phases:

```math
1 + z = \frac{S(t_\text{obs})}{S(t_\text{emit})}, \qquad \frac{E_\text{obs}}{E_\text{emit}} = \frac{\lambda_\text{emit}}{\lambda_\text{obs}} = \frac{S(t_\text{emit})}{S(t_\text{obs})} = \frac{1}{1+z}.
```

No space stretches. The reddening is the difference in phase position between emission and observation on a fixed domain, sampling rather than stretching. The mechanism is understood in outline; the full chain from the postulate to the observed $`H(z)`$ is partially walked (temporal budget §X).

**This is not tired light.** Tired light bleeds photon energy to scattering and smears both the image and the spectrum. Here every wavelength scales by the single factor $`S(t_\text{emit})/S(t_\text{obs})`$, a uniform rescaling that preserves the spectral shape and keeps point sources sharp. The blackbody stays a blackbody (§II); the image stays focused.

## II. Cooling is redshift of the bath

Cooling is the same phase ratio applied to a thermal ensemble instead of a single photon. The domain is static in the framework sense: the $`S^3`$ topology sits at fixed spectral radius $`R_\Lambda`$. A space-filling radiation bath has no exterior to radiate into, so cooling cannot be leakage; it has to be earned by the budget.

The budget earns it. At early phase ($`t \to 0`$), $`\Psi^2 \approx 1`$ and $`S^2 \approx 0`$: nearly all budget weight resides in the standing wave, the unresolved background. As the phase advances, $`S`$ grows and $`\Psi`$ shrinks; weight transfers from $`\Psi^2`$ into $`S^2`$, from unresolved wave into realized modes. The total is conserved ($`\Psi^2 + S^2 = 1`$), but the partition shifts.

The thermal reading rides on the effective metric, where the scale factor $`a_\text{eff} \propto S`$ carries the volume. Every wavelength rescales by $`S`$, photon number density scales as $`n \propto S^{-3}`$ at conserved photon count, and radiation energy density scales as $`\rho \propto S^{-4}`$. That $`n \propto S^{-3}`$ is exactly the blackbody equilibrium condition $`n \propto T^3`$ at $`T \propto 1/S`$, so a Planck blackbody at emission stays a Planck blackbody at observation, only cooler:

```math
T \propto \frac{1}{S} \propto (1 + z).
```

The fixed quantity is the spectral radius $`R_\Lambda`$, which sets $`\Lambda = 3/R_\Lambda^2`$, not the effective thermodynamic volume. The cooling is internal redistribution within a closed budget, carried by the transfer $`\Psi^2 \to S^2`$, and the energy accounting for that transfer stays open (§VI).

**Status.** ESTABLISHED as a kinematic equivalence with the FLRW thermal redshift law, where $`T \propto 1/a_\text{eff}`$ and the effective scale factor $`a_\text{eff} \propto S`$. At the kinematic level the equivalence is exact: if one variable governs both photon redshift and temperature, a blackbody stays a blackbody with $`T \propto 1/S`$. First-principles derivation from the postulate, including the photon phase-space density, remains OPEN. The entropy that accompanies the cooling is a separate reading of $`S`$, handled in [Entropy as Realization Budget](entropy-as-realization-budget.md).

## III. The observable side: distances

The phase ratio gives $`1 + z`$; turning it into observed distances and $`H(z)`$ needs the clock. The Waltz clock $`dt/d\tau = S^{-1/2}`$ converts budget phase to conformal time, the distance-redshift relation is worked out in [dark-energy §II](../../../../cosmos/files/dark-energy.md), and the joint fit to Pantheon+ and DESI DR2 BAO sits in [temporal budget §II-III](temporal-budget.md). The mechanism here supplies $`1 + z`$; the clock supplies the map from $`1 + z`$ to distance.

## IV. What this is not

**Expansion.** The space is static $`S^3`$. Redshift is the observer's phase advance on the standing wave, and cooling is that advance applied to the bath. Neither invokes a growing scale factor; the FLRW forms are recovered kinematically, with $`S`$ in the role $`a`$ plays.

**Tired light.** The shift is a uniform energy rescaling, not a scattering loss, so it preserves the blackbody spectrum and the sharpness of the image (§I).

## V. Where it stands

| Piece | Status |
|---|---|
| Redshift as phase ratio, $`1 + z = S(t_\text{obs})/S(t_\text{emit})`$ | mechanism in outline; full derivation partially walked |
| Blackbody preserved, $`T \propto 1/S`$ | ESTABLISHED as kinematic equivalence (FLRW thermal law) |
| Distance-redshift and $`H(z)`$ | ESTABLISHED at model level via the clock; the SN+BAO fit is in [temporal budget](temporal-budget.md) |
| Cooling from the postulate (photon phase-space density) | OPEN |

## VI. Open questions

**Where the redshifted energy goes.** In the effective FLRW reading, radiation carries the usual conformal conserved charge: for a traceless radiation stress tensor, the conformal Killing field inherited from the static $`S^3`$ frame gives $`\rho\, a_\text{eff}^4 = \text{const}`$. The comoving photon-energy reading $`\rho\, a_\text{eff}^3 \propto 1/S`$ therefore measures the frame's cooling bookkeeping, not by itself a missing spacetime-energy sink.

The budget still suggests a transfer $`\Psi^2 \to S^2`$, but turning that amplitude transfer into stress-energy requires an amplitude-to-$`T_{\mu\nu}`$ dictionary. Writing that dictionary is the open problem: it would decide whether the realization sector carries a genuine energy counterparty, and the same dictionary feeds the entropy reading ([Entropy as Realization Budget](entropy-as-realization-budget.md) §VIII). Highest-leverage open question for the budget.

**A thermal observable: distortion or $`T(z)`$ deviation.** For exactly conformal radiation with conserved photon number, the conformal map preserves a Planck spectrum: wavelengths scale by $`S`$, number density by $`S^{-3}`$, and $`\rho`$ by $`S^{-4}`$, so $`\mu = 0`$ at the kinematic level. The clean FIRAS-consistent claim now follows from the conformal map rather than being asserted, conditional on exact conformal radiation and conserved photon count. A measured $`\mu`$ or $`y`$ distortion within reach of PIXIE-class experiments, or a bend in the temperature law to $`T(z) = T_0 (1+z)^{1-\beta}`$ (tested by SZ clusters and quasar absorption lines), would test failures of exact conformal radiation, photon conservation, or the still-open energy dictionary. Either way the thermal sector gains a falsifiable handle.

---

*The universe does not stretch the light. The observer reads it from farther along the wave.*

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
