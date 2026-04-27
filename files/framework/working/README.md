/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# 📝 Working Notes

Research-in-progress across the framework. Ordered by current empirical pressure: papers gated by the Euclid DR1 falsification window first, long-horizon proofs and interpretive notes after.

---

## [Phantom Crossing as Template Artifact](./phantom-crossing-template-artifact.md)

**Priority:** Before Euclid DR1.

**Problem:** DESI DR2's apparent phantom crossing ($w < -1$ near $z \approx 0.5$) appears to require negative kinetic energy or ghost fields under standard CPL templates.

**Methodology:** Derive Λcos $H^2(z)/H_0^2 = \alpha(1+z)^3 - \beta(1+z) + \Omega_\Lambda$ from the temporal budget identity; jointly fit Pantheon+ (1701 SNe Ia) and DESI DR2 BAO (13 points); show CPL recovery produces an apparent phantom crossing while $w_\text{eff}(z) > -1$ holds at every redshift.

**Dependencies:** Temporal Budget Identity, Sector $\mathcal{A}$ eigenvalue ($\Omega_\Lambda = 0.685$ as input).

---

## [Epoch-Dependent Acceleration Scale from Bounded Topology](./a0-evolution-paper.md)

**Priority:** Before Euclid DR1.

**Problem:** The MOND acceleration scale $a_0 \approx 1.20 \times 10^{-10}$ m/s$^2$ satisfies a numerical coincidence with $cH_0$ that has remained unexplained for four decades; in standard MOND it is a free parameter, in $\Lambda$CDM it carries no physical content, and the JWST early-massive-galaxy crisis at $z \sim 7\text{-}10$ has no resolution within either framework.

**Methodology:** Derive $a_0(z) = a_0(0)\,E(z)$ as a zero-parameter ratio cancellation in the scaling law ($a_0$ at well $13/120$ and $H$ at well $34/120$, both edge modes); generate five distinct testable predictions across cosmic time as different powers of $E(z) \in \{-1, -1/2, +1/4, +1/2, -1/4\}$ governing BTFR normalization, MOND transition radius, asymptotic flat velocity, lensing $M_\text{dyn}/M_b$ enhancement, and free-fall collapse time; forward-model the Übler 2017 radial pressure-support pipeline against the framework's monotonic prediction; identify the Euclid DR1 stacked galaxy-galaxy lensing measurement as the sharpest near-term test of both magnitude (74% predicted enhancement at $z = 2$) and universality (mass- and aperture-independence).

**Dependencies:** Scaling law $A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}$, well assignments at $z = 0$ ($a_0$ at $13/120$, $H_0$ at $34/120$), Sector $\mathcal{A}$ surface-mode eigenvalue $\Omega_\Lambda$ for §8.5 CMB consistency, Λcos companion paper for the joint-outcome §9 prediction set.

---

## [Phase Field Coherence Scale (SPARC)](./sparc-phase-field-notes.md)

**Priority:** Before Euclid DR1.

**Problem:** The Hubble-tension mechanism predicts a binary phase shift inside a coherence scale $L_f = v_c^2/a_0$, but it has no test outside the cosmological distance ladder.

**Methodology:** Run three component-isolating tests on the 175-galaxy SPARC sample: (1) verify the gravitational transition radius tracks $L_f$; (2) verify the threshold $\mathcal{T}/\mathcal{T}_c \approx 2.2$ is universally crossed for all flat-rotation-curve galaxies; (3) verify $H_0$ measurements cluster bimodally rather than varying continuously with $v_c$.

**Dependencies:** Hubble-tension well assignment ($\Theta = 34/120 \to 36/120$), MOND scale $a_0$ from $C(13/120)$, closure identity $\mathcal{T}_c = 2\xi v_c^2/c^2$.

---

## [The Temporal Budget Identity](./temporal-budget-notes.md)

**Priority:** Before Euclid DR1.

**Problem:** The Λcos derivation rests on $\Psi^2 + S^2 = 1$ and the Waltz clock $d\tau/dt = S^{1/2}$, which already recovers $\Omega_m = 0.315$ at $\Delta\chi^2 = +0.6$ vs flat ΛCDM under a Pantheon+ fit; the clock exponent $n = 1/2$ is still selected by self-consistency with $H \propto S^{-3/2}$ rather than derived from the embedding.

**Methodology:** Derive $n = 1/2$ directly from $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ without invoking GR; verify the derivation against the existing Pantheon+ fit as a consistency check.

**Dependencies:** Möbius spatial budget $u_0^2 + J^2 = 1$, Sector $\mathcal{A}$ eigenvalue.

---

## [McKay Propagator Correction](./mckay-propagator-correction.md)

**Priority:** Before Euclid DR1.

**Problem:** Two of twelve SM fermions overshoot at high McKay distance (down $\times 3.2$, top $\times 3.9$); the misses split across vacua, and the Coxeter-Galois gate separately excludes charm from $R_4$.

**Methodology:** Test vacuum-dependent corrections at the $R_8$ branch point where the McKay graph forks to $R_4$ and $R_5$; compute $\Pi_T = \prod T^2(i \otimes \sigma)$ along intermediate nodes for all 24 entries; require the correction reverse sign across vacua to fix both misses with one mechanism.

**Dependencies:** McKay graph for binary icosahedral group, $C_\text{geom}$ values for all irreps, torsion table $T^2(\rho \otimes \sigma)$ across vacua, Coxeter-Galois gate.

---

## [The Scaling Law as Forced Measurement Postulate on S³/2I](./scaling-law-uniqueness.md)

**Priority:** Post-Euclid DR1.

**Problem:** $A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}$ is currently a declared measurement postulate; every downstream result (couplings, masses, Hubble mechanism) inherits that DECLARED status.

**Methodology:** Prove uniqueness in the style of Gleason's theorem: enumerate the topological constraints (anti-periodic BC, bounded domain, 120-discreteness, observer at $\sqrt{\Omega}$, dimensionless output, factorization) and show the scaling law is the only sampling rule compatible with all of them.

**Dependencies:** Sector $\mathcal{A}$ eigenvalue paper, Lemma 8 (spectral inaccessibility), Möbius topology axioms.

---

## [Energy as Resolution Amplitude](./energy-as-resolution-amplitude.md)

**Priority:** Post-Euclid DR1.

**Problem:** SR's $E^2 = (mc^2)^2 + (pc)^2$ is an empirical Pythagorean relation in the standard reading; MIT may permit reading it as the orthogonal mode decomposition of $\Psi$ at an observer's sampling coordinates.

**Methodology:** Identify $mc^2$ as the temporal-mode content of the sampling operation and $pc$ as the spatial-mode content along a trajectory through $S^3$; verify orthogonality and consistency with the rest of the sampling picture.

**Dependencies:** Standing wave $\Psi = \cos(t/2)$, scaling law for amplitude resolution.

---

## [Black Hole Phase Behavior](./black-hole-phase-notes.md)

**Priority:** Post-Euclid DR1.

**Problem:** GR splits the black-hole story across two observers (exterior vs infalling) and produces a metric singularity; MIT's standing-wave picture should give one consistent account.

**Methodology:** Apply the budget identity and the $C(\Theta)$ sampling rule at and inside the horizon; identify the interior as a double zero where $\Theta = 0$ and $\Omega_H = 0$ dissolve the scale hierarchy while wave content persists.

**Dependencies:** Sector $\mathcal{A}$ eigenvalue paper, [Black Double Zero](../../cosmos/files/black-hole.md) §§II, IV.A, VI.

---

/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
