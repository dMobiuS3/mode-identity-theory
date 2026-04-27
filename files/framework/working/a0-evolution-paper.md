/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /

---

# Epoch-Dependent Acceleration Scale from Bounded Topology: Predictions for High-Redshift Galactic Dynamics

**B. Shatto**
Independent Researcher, St. Petersburg, FL, USA
bshatto.pe@gmail.com

---

## Abstract

Modified Newtonian Dynamics rests on a single dimensional parameter, $a_0 \approx 1.20 \times 10^{-10}$ m/s$^2$, whose proximity to the cosmic scale $c H_0$ has remained unexplained for four decades. Within Mode Identity Theory, a measurement-postulate framework on the bounded topology $S^1 = \partial(\text{Mobius}) \subset S^3$, we show that the local Milgrom ratio $a_0/(c H_0)$ reduces to a structural cancellation between two phase-operator values at adjacent Fibonacci wells of the framework's 120-domain, agreeing with observation at the 0.8% level. A combinatorial baseline confirms the match is sparse on the full 120-domain (24 of 7,021 nonzero pairs) and unique within the framework's selected Fibonacci-well subset. The same derivation, under a local-epoch reading of the framework's scaling-law postulate, forces an evolving acceleration scale $a_0(z) = a_0(0)\,E(z)$ with $E(z)$ the standard Friedmann dimensionless Hubble parameter. Five testable predictions follow with no additional free parameter beyond the local SPARC calibration: the baryonic Tully-Fisher normalization shifts as $1/E(z)$; the MOND transition radius contracts as $E(z)^{-1/2}$; the asymptotic flat velocity at fixed baryonic mass rises as $E(z)^{1/4}$; the lensing-inferred dynamical-mass-to-baryonic-mass ratio is enhanced by $\sqrt{E(z)}$; and the gravitational free-fall collapse time shortens as $E(z)^{-1/4}$. The five exponents are not independent predictions: they are distinct observable manifestations of one cosmological input, $a_0(z) \propto E(z)$. Independence between observable classes is tested by confirming consistency across two channels at the same redshift, not by any single measurement. We treat existing observational constraints honestly: the KMOS3D Tully-Fisher analysis shows a non-monotonic trend in tension with the framework's monotonic prediction, and a forward-modeled simulation of the Übler radial pressure-support pipeline does not reproduce the observed pattern, so the tension is genuine and awaits resolution by matched-systematics measurements; the cluster-scale MOND mass discrepancy is inherited from local MOND and unaddressed; CMB consistency requires the framework's edge-mode selection rule to prevent the galactic $a_0(z)$ scaling from propagating into cosmological perturbations; we derive an empirical bound $\varepsilon \lesssim 10^{-5}$ on the leakage coupling from Planck's first-peak amplitude, with the framework's structural prediction $\varepsilon = 0$ consistent by orders of magnitude, and a rigorous first-principles derivation of the decoupling flagged as open work. The Euclid DR1 release in October 2026 will deliver the sharpest near-term test through stacked galaxy-galaxy weak lensing at $z = 0.5\text{–}2$, simultaneously probing the predicted 74% enhancement at $z = 2$ and its mass- and aperture-universality, in a regime where the framework and standard halo-concentration ΛCDM produce quantitatively distinct shifts.

---

## 1. Introduction

### 1.1 Three tensions, one dimensional anchor

For four decades, the empirical success of Modified Newtonian Dynamics (MOND [1]) at galactic scales has rested on a single dimensional parameter $a_0 \approx 1.20 \times 10^{-10}$ m/s$^2$. This acceleration scale, fitted to the local SPARC sample with intrinsic scatter of order 0.1 dex [2,3], satisfies a striking numerical coincidence: $a_0 / (cH_0) \approx 0.18$, with the present-day Hubble rate setting the dimensional scale of the MOND threshold. Milgrom [4], McGaugh [5], and others have remarked on this connection. Within standard MOND it remains a numerical accident with no underlying derivation. Within ΛCDM it is a coincidence with no physical content, since MOND itself has no cosmological foundation in that framework.

JWST has recently delivered a more acute tension. Imaging of the early universe at $z \sim 7\text{–}10$ has identified candidate massive galaxies with stellar masses $M_\star \gtrsim 10^{10}\,M_\odot$ assembled within the first $\sim 600$ Myr of cosmic time [6,7]. Under standard ΛCDM halo growth and star-formation efficiency assumptions, the most extreme candidates require $\varepsilon_\text{SF} \gtrsim 1$, a formal impossibility because no more than the available baryonic budget can be converted into stars. Proposed resolutions invoke modified initial conditions, top-heavy early IMFs, or non-standard early-universe physics, none yet supported by independent evidence.

A third tension comes from intermediate-redshift dark-energy probes. DESI DR2 [8] reports a $\sim 4\sigma$ preference for an evolving dark-energy equation of state $w(z)$ over the constant $w = -1$ assumed by ΛCDM. Phantom-crossing fits to the data require exotic field content; the cosmological constant remains viable only if the apparent evolution can be attributed to systematic effects or template artifacts.

These three tensions, the local Milgrom coincidence, the high-redshift early-galaxy crisis, and the intermediate-redshift dark-energy evolution, are loosely connected by sharing the cosmic acceleration scale $\sim c H_0$ as their common dimensional anchor. None is individually fatal to ΛCDM. None has a satisfactory resolution within either MOND or ΛCDM as conventionally formulated. The hypothesis explored in this paper is that they share an underlying topological origin.

### 1.2 The framework

Mode Identity Theory (MIT; the framework's foundational structure is summarized in Appendix A) is a measurement-postulate framework on the bounded topology $S^1 = \partial(\text{Mobius}) \subset S^3$ with anti-periodic boundary conditions. The framework's central postulate is the scaling law

$$\frac{A}{A_P} = C(\Theta)\,(\sqrt{\Omega})^{-n}, \quad \text{(1.1)}$$

mapping a Planck-normalized observable $A/A_P$ to a phase position $\Theta \in \{k/120 : k = 0, \ldots, 119\}$ on the 120-domain native to $S^3/2I$, a manifold-mode index $n$ assigned by the embedding hierarchy $S^1 \subset \text{Mobius} \subset S^3$, and a hierarchy ratio $\Omega$ chosen by a selection rule. The phase operator $C(\Theta) = 2\sin^2(\pi\Theta)$ is the squared modulus of the anti-periodic ground mode on the Möbius surface, derived in the framework's foundational papers [22,24].

Two specific assignments are the subject of this paper and its companion. The MOND scale $a_0$ is identified as an edge-mode observable ($n = 1$) referenced to the kinematic horizon ratio $\Omega_H = (c/(H\,\ell_P))^2$, with phase position $\Theta = 13/120$. The cosmological constant Λ is identified as a surface-mode observable ($n = 2$) referenced to the eigenvalue ratio $\Omega_\Lambda$, with phase position $\Theta = 60/120$. The Hubble rate $H$ is itself an edge-mode observable at $\Theta = 34/120$. Both the $(a_0, H_0)$ wells and the Λ position are calibrated against local measurements at percent-level precision [21,22], and their forward-looking implications for cosmic evolution are structurally inverse: the framework predicts that $a_0$ evolves with $H(z)$ while Λ remains constant, the inverse of the standard ΛCDM presumption where Λ is the candidate evolving quantity (DESI's $w(z)$) and $a_0$ is assumed universal.

### 1.3 What this paper does

The present paper makes the edge-sector prediction concrete and testable.

The §2 derivation reduces the local Milgrom coincidence to a structural ratio of two phase-operator values at fixed Fibonacci wells: $a_0/(cH_0) = C(13/120)/C(34/120) = 0.1846$, agreeing with the observed value of 0.1832 at the 0.8% level, and with the match unique within the framework's Fibonacci-well subset (one of ten possible well-pairs). The wells were assigned individually to reproduce the absolute values of $a_0$ and $H_0$ at $z = 0$, two parameters fitting two measurements; their ratio was never tuned to the Milgrom coincidence and emerges as a consequence of the well structure. The same derivation forces, through a local-epoch reading of (1.1), an epoch-dependent evolution

$$a_0(z) = a_0(0)\,E(z), \quad \text{(1.2)}$$

with $E(z) \equiv H(z)/H_0$ the standard Friedmann dimensionless Hubble parameter. This evolution is the one input that drives §§3-7.

§3 tabulates $a_0(z)$ across the redshift range $z = 0$ to $15$. §4 derives the implication for the baryonic Tully-Fisher relation: a redshift-dependent normalization shift $A_\text{BTFR}(z)/A_\text{BTFR}(0) = 1/E(z)$, with the MOND interpolating-function dependence cancelling out of the ratio. §5 extends to galactic rotation-curve structure: the MOND transition radius contracts as $E(z)^{-1/2}$ and the asymptotic flat velocity rises as $E(z)^{+1/4}$, both mass-independent. §6 makes the lensing prediction theory-completion-agnostic by working at the Newtonian-inversion level: the inferred dynamical-mass-to-baryonic-mass ratio is enhanced by $\sqrt{E(z)}$ at fixed aperture and baryonic mass, universally across the deep-MOND regime. §7 applies the corresponding $E(z)^{1/4}$ collapse-time speedup to the JWST early-galaxy tension, reducing the required star-formation efficiency by a uniform factor of $\sim 2$ across the Labbé sample, which can move the most extreme candidates from formally impossible to permitted under standard halo-mass assumptions.

§8 treats the existing constraint landscape honestly: a live tension with the KMOS3D BTFR trend shape, the inherited cluster-scale MOND mass discrepancy at $z \lesssim 0.3$ (where the framework's evolution correction is at the percent level against a factor-five problem), the structurally resolved CMB consistency under the framework's selection rule (where cosmological perturbations sit in a different manifold-mode sector than $a_0$), and below-sensitivity status elsewhere. The framework's monotonic BTFR prediction is in tension with current intermediate-redshift kinematic data [9]; the comparison, including a forward-modeled simulation of the radial pressure-support systematic, is treated in §8. §9 connects to a companion analysis (separately submitted) developing the surface-sector prediction. §10 collects the full predictive content into a single table and identifies the falsification windows. §11 closes.

The §§3-7 predictions are not independent: they all derive from (1.2) and depend on $E(z)$ through different powers ($-1$, $-1/2$, $+1/4$, $+1/2$, $-1/4$ across §§4-7). A single measurement of any one observable at any one redshift tests all five through their shared cosmological dependence. The Euclid DR1 release in October 2026 will deliver the sharpest such test in the form of stacked galaxy-galaxy weak lensing at $z = 0.5\text{–}2$ stratified by baryonic mass and aperture.

### 1.4 Novelty relative to prior literature

The evolving form $a_0(z) \propto H(z)$ has been speculated in the MOND literature as a possible interpretation of the local $a_0 \approx cH_0$ coincidence; Milgrom (1999) [4] explored this in a vacuum-effect framework, and a parallel speculation appears in prior MIT working notes without derivation. The present paper's contribution is not the bare proportionality but three specific results that follow from it.

First, the relation is *derived within the framework* from the scaling-law postulate (§2) as a structural cancellation between two specific Fibonacci-well positions $C(13/120)$ and $C(34/120)$ on the 120-domain of $S^3/2I$, with the local Milgrom ratio recovered at the 0.8% level. The match is sparse on the full 120-domain (24 of 7,021 nonzero pairs match within 1%) and unique within the framework's Fibonacci-well subset (one of ten possible well-pairs). The derivation identifies the topological mechanism by which the proportionality arises and forces a single specific functional form (linear in $E(z)$) rather than admitting a family of speculative possibilities.

Second, the same derivation generates a *coupled five-exponent prediction set* across cosmic time (§§4-7), with all five observables (BTFR normalization, MOND transition radius, asymptotic flat velocity, lensing $M_\text{dyn}/M_b$ enhancement, free-fall collapse time) governed by the same $a_0(z) \propto E(z)$ input through different powers of $E(z) \in \{-1, -1/2, +1/4, +1/2, -1/4\}$. The five predictions are not independent and cannot be tuned separately; any measurement of one tests all five through their shared cosmological dependence.

Third, the prediction set is subjected to *explicit constraint analysis* against existing data (§8), including a forward-model treatment of the Übler 2017 KMOS3D pressure-support pipeline that demonstrates the framework's monotonic BTFR prediction is in genuine tension with the only existing high-$z$ test, and that the tension cannot be dissolved by literature-plausible velocity-correction systematics. The §6 lensing prediction is also made at the level of the Newtonian-inferred dynamical mass, sidestepping the need to commit to a specific relativistic completion of MOND.

The framework's broader prediction set, including the surface-sector Λ prediction developed in a companion analysis on the same scaling-law postulate, is a meta-result whose status accrues across individual tests; the §9 joint-outcome table identifies four enumerated outcomes that the joint pattern across both sectors can produce. The framework's posture throughout is the gauge-theory posture: the $(n, \Omega)$ assignments are postulates of the framework, calibrated at $z = 0$ where applicable, with consequences that are tested rather than assumed.

## 2. Derivation of $a_0(z) \propto H(z)$ from the Scaling Law

### 2.1 Setup: the scaling law

The framework's measurement postulate [21,22,24] is

$$\frac{A}{A_P} = C(\Theta)\,(\sqrt{\Omega})^{-n}$$

where $A$ is a dimensional observable, $A_P$ its Planck reference, $\Theta \in \{k/120 : k = 0, 1, \ldots, 119\}$ a phase position on the 120-domain native to $S^3/2I$, $n$ a manifold-depth index assigned by the embedding hierarchy $S^1 \subset \text{Mobius} \subset S^3$, and $\Omega$ a hierarchy ratio set by the boundary scale relevant to the observable. The phase operator

$$C(\Theta) = 2\sin^2(\pi\Theta)$$

is the squared modulus of the anti-periodic ground mode on the Mobius surface, normalized to unit mean over the domain (Appendix A.2).

Two hierarchy ratios are available to a given observable:

| Symbol | Definition | Physical content |
|---|---|---|
| $\Omega_H$ | $(c / (H\,\ell_P))^2$ | Hubble horizon, $R_H = c/H$ |
| $\Omega_\Lambda$ | $(\Lambda\,\ell_P^2)^{-1}$ | de Sitter horizon, $R_\Lambda = \sqrt{3/\Lambda}$ |

The selection rule (Appendix A.5) assigns each observable to one of these. The rule, as stated:

> If it evolves with epoch → $\Omega_H$. If it is set by the surface → $\Omega_\Lambda$.

This rule is a postulate of the framework, with the same status as the gauge group $SU(3) \times SU(2) \times U(1)$ in the Standard Model: chosen, not derived, with consequences that are tested rather than assumed. The §2 derivation takes the rule as given and shows what follows.

### 2.2 Edge modes use $\Omega_H$

Edge modes are observables tied to the $S^1$ boundary of the Mobius band ($n = 1$ in the embedding hierarchy). The boundary $S^1$ is a kinematic locus: it carries no intrinsic surface eigenvalue (the surface eigenvalue lives one dimension up, on Mobius itself, and produces Λ via the chain summarized in Appendix A.7). What an edge mode references is the embedding scale of $S^1$ in the ambient cosmological geometry. The natural such scale is the Hubble horizon $R_H = c/H$, and its dimensionless Planck ratio is $\Omega_H$.

Therefore, for any edge-mode observable evaluated at cosmic epoch $z$:

$$\frac{A_{\text{edge}}(z)}{A_P} = C(\Theta_A)\,(\sqrt{\Omega_H(z)})^{-1}, \qquad \Omega_H(z) \equiv \left(\frac{c}{H(z)\,\ell_P}\right)^2 \quad \text{(2.1)}$$

The phase position $\Theta_A$ and the manifold index ($n = 1$) are topological assignments and do not evolve. The full epoch dependence sits in $\Omega_H(z)$.

### 2.3 Two edge-mode observables

The well assignments forced by the framework's selection rule (Appendix A.6) place $a_0$ at $\Theta = 13/120$ and $H$ at $\Theta = 34/120$, both edge modes ($n = 1$, $\Omega = \Omega_H$). With $A_P = a_P = c/t_P$ for the acceleration and $A_P = t_P^{-1}$ for the frequency, equation (2.1) gives, at any epoch $z$:

$$\frac{a_0(z)}{a_P} = C(13/120)\,(\sqrt{\Omega_H(z)})^{-1} \quad \text{(2.2)}$$

$$H(z)\,t_P = C(34/120)\,(\sqrt{\Omega_H(z)})^{-1} \quad \text{(2.3)}$$

Two facts about the structure of (2.2)-(2.3) carry the entire derivation:

1. The $C$ factors are pure numbers fixed by the wells: $C(13/120) = 2\sin^2(13\pi/120) = 0.2229$ and $C(34/120) = 2\sin^2(34\pi/120) = 1.2079$. They are topological invariants of the 120-domain on $S^3/2I$ and do not evolve.
2. The full epoch dependence sits in the shared factor $(\sqrt{\Omega_H(z)})^{-1}$, which is identical in both expressions because both observables are edge modes referencing the same hierarchy.

The derivation of $a_0(z) \propto H(z)$ does not require evaluating either expression in isolation. It requires only the ratio.

### 2.4 The ratio (the derivation)

Dividing (2.2) by (2.3), the hierarchy factor cancels identically:

$$\frac{a_0(z)/a_P}{H(z)\,t_P} = \frac{C(13/120)}{C(34/120)}$$

Using $a_P\,t_P = (c/t_P)\,t_P = c$:

$$\boxed{\;\frac{a_0(z)}{c\,H(z)} = \frac{C(13/120)}{C(34/120)} = 0.1846\;} \quad \text{(2.4)}$$

The right-hand side is a pure topological number, independent of $z$. The relation $a_0(z) \propto H(z)$ follows immediately: the ratio is fixed at every epoch by the well positions alone. Equivalently:

$$a_0(z) = a_0(0)\,\frac{H(z)}{H_0} \quad \text{(2.5)}$$

This is the central result of the section. No epoch-dependent quantity other than $H(z)$ enters; no auxiliary scale is introduced; the cancellation is exact at every $z$. The $C$ factors and the hierarchy factor each carry the projection of the topology into observables; in the ratio, both projections are stripped away and what remains is the pure well structure.

The value $0.1846$ is a structural consequence of the framework's well assignments, not an independent free parameter. The wells $13/120$ and $34/120$ were assigned individually to reproduce $a_0(0)$ and $H_0$ at $z = 0$: two parameters fitting two absolute values. Their ratio $C(13/120)/C(34/120)$ was not tuned separately to the observed Milgrom coincidence; it emerges from the well assignments and the shared edge-mode hierarchy factor as a consequence of the algebra. The §2.5 agreement to 0.8% is a test of that structure, with the matching strength quantified against the combinatorial baseline below.

### 2.5 Consistency check on absolute values at $z = 0$

The ratio (2.4) determines the evolution but says nothing about the absolute value of $a_0$ at any single epoch. The absolute values come from the individual scaling-law projections (2.2)-(2.3) evaluated at $z = 0$, and serve as a check that the well assignments themselves match observation. Observed inputs (Planck 2018 [20] $H_0 = 67.4$ km/s/Mpc, SPARC $a_0 = 1.20 \times 10^{-10}$ m/s$^2$):

$$\frac{a_0^{\text{obs}}}{c\,H_0^{\text{obs}}} = \frac{1.20 \times 10^{-10}}{6.55 \times 10^{-10}} = 0.1832$$

Predicted ratio from the wells: 0.1846. Agreement to 0.8%. The Milgrom coincidence $a_0 \approx c\,H_0$ resolves to a ratio of two phase-operator values at fixed wells. The absolute value of $H_0\,t_P$ predicted by (2.3) reproduces the observed $H_0$ at the 2% level (Appendix A.7); the absolute value of $a_0/a_P$ from (2.2) follows by the same factor.

To calibrate the strength of this match, we compute the combinatorial baseline. Of the 7,021 unordered nonzero phase-position pairs $(k_1, k_2)/120$ with $k_1, k_2 \in \{1, \ldots, 119\}$, only 24 produce a ratio $C(k_1/120)/C(k_2/120)$ within 1% of the observed $0.1832$, a fraction of 0.342%. Modulo the reflection symmetry $C(k) = C(120-k)$, these collapse to 6 unique phase-operator value pairs. Within the framework's selected Fibonacci-well subset $\{13, 21, 34, 55, 60\}/120$, exactly one of the ten possible unordered well-pairs matches: the framework's $(13, 34)$. The match is therefore sparse on the full 120-domain (one in $\sim 300$ pairs) and unique within the topologically-selected Fibonacci-well structure (one in 10).

The absolute-value check tests the well assignments (which were calibrated to $z = 0$ measurements). The evolution prediction is independent of this calibration and follows from the cancellation in (2.4).

### 2.6 The local-epoch postulate (load-bearing step)

Equation (2.4) holds at all $z$ if and only if the edge-mode rule (2.1) uses $\Omega_H(z)$ evaluated at the local epoch, not $\Omega_H(0)$ evaluated at present and held fixed. This is the step that elevates the framework from "explains the $a_0/cH_0$ ratio at $z = 0$" to "predicts $a_0(z) \propto H(z)$ at all epochs." It deserves explicit justification.

**Argument from the measurement-postulate reading.** The scaling law is a measurement postulate: it specifies what an observer measures, given the topological structure and the hierarchy at the measurement event. Three sub-claims follow:

1. *The 120-domain is a topological invariant of $S^3/2I$.* The wells $\{13, 21, 34, 55, 60\}/120$ are fixed by the Hurwitz/Fibonacci structure on the binary icosahedral quotient. They do not evolve with cosmic epoch. Therefore $C(\Theta_A)$ in (2.1) is the same number at every $z$.

2. *The manifold index $n$ is a topological assignment.* Edge mode means $n = 1$, and "edge" refers to the embedding $S^1 \subset \text{Mobius} \subset S^3$, which is a topological feature of the framework, not a feature of cosmic evolution. Therefore $n$ in (2.1) is the same at every $z$.

3. *The hierarchy ratio $\Omega$ is the only piece set by external, evolving geometry.* $\Omega_H = (c/(H\,\ell_P))^2$ is built from $H$, which is the local Hubble rate. A measurement performed at epoch $z$ accesses the local geometry at epoch $z$. Therefore $\Omega_H$ in (2.1) is $\Omega_H(z)$, not $\Omega_H(0)$.

Sub-claims 1 and 2 are forced by the topological reading of the wells and the embedding hierarchy. Sub-claim 3 is the genuine postulate. It says: the observer's hierarchy reference is set by the geometry at the observer's spacetime location, not by some privileged past or future epoch.

**The alternative.** One could postulate that $\Omega_H$ in (2.1) is permanently $\Omega_H(0)$, so that all edge-mode observables retain their present-day values at every epoch. Under this alternative, $a_0$ is constant. But this alternative *is* itself the addition of a postulate: it requires a privileged "present" epoch to which the hierarchy reference is anchored, breaking time-translation symmetry within the bounded cosmic domain. The bounded domain offers no structural support for such a slice. The "local-epoch reading" is therefore not a separate postulate added to the framework: it is the refusal to add one. The scaling law evaluated at face value, with $\Omega_H$ defined as $(c/(H(z)\ell_P))^2$, gives the local reading by default; freezing $\Omega_H(0)$ is what would require the addition.

### 2.7 Generalization: any two edge-mode observables

The cancellation in (2.4) is not specific to $(a_0, H)$. For any pair of edge-mode observables $A$ and $B$ at the same epoch:

$$\frac{A(z)/A_P^{(A)}}{B(z)/A_P^{(B)}} = \frac{C(\Theta_A)}{C(\Theta_B)} \cdot \frac{(\sqrt{\Omega_H(z)})^{-1}}{(\sqrt{\Omega_H(z)})^{-1}} = \frac{C(\Theta_A)}{C(\Theta_B)} \quad \text{(2.6)}$$

The shared $(\sqrt{\Omega_H(z)})^{-1}$ divides out whenever both observables are edge modes referencing the same hierarchy. This is the structural reason the framework predicts proportional evolution among all edge-mode kinematic quantities, not just $a_0$ and $H$. Any further edge-mode acceleration scale, frequency, or velocity would track $H(z)$ identically, with its present-epoch ratio to $cH_0$ set by its own well position. The pair $(a_0, H)$ is the cleanest application because both are independently measured to ~1% precision and the corresponding wells $(13, 34)/120$ are adjacent Fibonacci stability points.

### 2.8 Why Λ does not evolve (contrast)

The same scaling-law machinery places Λ at well $60/120$ with $n = 2$ (surface mode) and $\Omega = \Omega_\Lambda$ [21,22]:

$$\frac{\Lambda}{\ell_P^{-2}} = C(60/120)\,(\sqrt{\Omega_\Lambda})^{-2} = 2 \cdot \Omega_\Lambda^{-1}$$

Two structural differences from $a_0$:

1. *Manifold index* $n = 2$ (surface), not $n = 1$ (edge). Λ is the eigenvalue of the Laplace-Beltrami operator on the Mobius surface; the embedding is via Gauss-Codazzi to the spatial slice. This is intrinsic surface geometry, not boundary kinematics.

2. *Hierarchy reference* is $\Omega_\Lambda$, not $\Omega_H$. $\Omega_\Lambda$ is set by Λ itself: it is the de Sitter horizon ratio. The relation $\Lambda \cdot R^2 = 3$ (Appendix A.7) closes the loop with $R$ fixed by the Molien-gap CMB measurement, which is itself an integrated quantity over the cosmic past. The selection rule places surface-mode observables in this class.

Under the local-epoch reading, $\Omega_\Lambda$ is the same at every $z$ (it is a topological-eigenvalue ratio, not a kinematic ratio). Therefore Λ is constant. The phase position $\Theta = 60/120$ is the antinode of $C(\Theta)$, where $d\ln C/d\Theta = 0$ (Appendix A.4), giving topological protection against environmental perturbations as well.

The two predictions are therefore *structurally inverse*: $a_0$ evolves because it references the kinematic horizon $\Omega_H$; Λ does not evolve because it references the surface-eigenvalue $\Omega_\Lambda$. This inversion is not a tuning. It is forced by the selection rule on $(n, \Omega)$ pairs.

### 2.9 Status of the argument

Honest accounting of what is derived vs imported in §2:

| Element | Status | Source |
|---|---|---|
| Scaling law $A/A_P = C(\Theta)\,(\sqrt{\Omega})^{-n}$ | Postulate | Appendix A.5 |
| $C(\Theta) = 2\sin^2(\pi\Theta)$ | Derived | Anti-periodic ground mode on Möbius (Appendix A.2) |
| Edge-mode $\Leftrightarrow$ $\Omega_H$ | Postulate (selection rule) | Appendix A.5 |
| Surface-mode $\Leftrightarrow$ $\Omega_\Lambda$ | Postulate (selection rule) | Appendix A.5 |
| Well assignment $\Theta_{a_0} = 13/120$ | Empirical at $z = 0$ | Appendix A.6 |
| Well assignment $\Theta_{H_0} = 34/120$ | Empirical at $z = 0$ | Appendix A.6 |
| Local-epoch reading of $\Omega_H$ | Default reading of (2.1); §2.6 shows freezing $\Omega_H(0)$ would itself add a postulate | This section |
| Cancellation (2.4), (2.6) | Derived | Algebra of (2.2)-(2.3) at fixed $z$ |
| $a_0(z) = a_0(0)\,H(z)/H_0$ | **Derived**, given the above | This section |

Given the framework's postulates, the wells calibrated at $z = 0$, and the local-epoch reading, the evolution $a_0(z) \propto H(z)$ is forced by the cancellation in (2.4). No additional free parameter is introduced for the evolution; it is fully determined by the structure. The well assignments themselves (13/120 for $a_0$, 34/120 for $H$) are not derived in this paper; they are inputs calibrated to $z = 0$ measurements. A future well-positioning analysis would attempt to derive these from the Hurwitz/Fibonacci structure of the 120-domain. Until then, the well assignments have the same status as fitting two parameters to two measurements at $z = 0$; the predictive content of the present paper is everything that follows at $z > 0$.

The two framework-wide concerns most likely to attract referee attention are:

1. *The selection rule.* The scale-selection rule assigns edge-mode observables ($n = 1$) to the kinematic hierarchy $\Omega_H$ and surface-mode observables ($n = 2$) to the eigenvalue hierarchy $\Omega_\Lambda$. This assignment is a postulate of the framework, with the same status as the gauge group $SU(3) \times SU(2) \times U(1)$ in the Standard Model. Its consequences are tested, not assumed, by the predictions that follow: Λ matches observation at 2%, $\alpha$ at 0.5%, and $H_0 \cdot t_P$ at 2%, across observables of wildly different magnitudes and from a single rule. A future uniqueness result for the $(n, \Omega)$ pairing is the right next step but is not a prerequisite for the present paper, just as Standard-Model phenomenology proceeded for decades before any uniqueness argument for $SU(3) \times SU(2) \times U(1)$ existed.

2. *The local-epoch reading.* §2.6 defends this from symmetry. The argument is structural rather than theorem-like: freezing $\Omega_H$ at $\Omega_H(0)$ would *be* the addition of a postulate (a preferred epoch), and the bounded domain offers no support for one. A referee may push on whether the absence of a preferred epoch is itself sufficient to force the local reading. The framework rejects preferred-epoch postulates elsewhere as well: the surface-sector treatment of cosmic dark-energy evolution (companion analysis) uses a $t$-dependent standing wave precisely because no time slice is privileged in the bounded cosmic domain.

Both are framework-wide concerns shared with the other Sector A papers; neither is unique to this paper, and neither is a defect in the algebra of §2.4.

## 3. H(z) and $a_0(z)$ across cosmic time

The §2 derivation reduces the epoch dependence of $a_0$ to the epoch dependence of $H$:

$$a_0(z) = a_0(0)\,\frac{H(z)}{H_0} = a_0(0)\,E(z) \quad \text{(3.1)}$$

with $E(z) \equiv H(z)/H_0$. The framework introduces no new parameter for the evolution; the only input is the cosmological expansion history. We adopt the flat ΛCDM Friedmann form,

$$E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_\Lambda}, \quad \text{(3.2)}$$

with Planck 2018 parameters [20] $\Omega_m = 0.315$, $\Omega_r = 9.2 \times 10^{-5}$, $\Omega_\Lambda = 0.685$, and $H_0 = 67.4$ km/s/Mpc. The age of the universe at redshift $z$ follows from

$$t_\text{age}(z) = \int_z^\infty \frac{dz'}{(1+z')\,H(z')}. \quad \text{(3.3)}$$

Equations (3.1)-(3.3) determine $a_0(z)$ at every epoch with no remaining freedom.

### 3.1 Table of values

Table 1 lists $E(z)$, $H(z)$, $a_0(z)$, the deep-MOND enhancement factor $\sqrt{a_0(z)/a_0(0)} = \sqrt{E(z)}$, and $t_\text{age}(z)$ at eight reference redshifts spanning the SPARC sample, the intermediate-$z$ rotation-curve regime, the BAO range, and the JWST early-galaxy window. The enhancement factor governs effective gravity, lensing-inferred dynamical mass, and free-fall collapse rates in the deep-MOND limit; it recurs throughout §§5-7 and is anchored here.

**Table 1.** Evolution of the Hubble rate, MOND acceleration scale, deep-MOND enhancement factor, and cosmic age across the redshift range relevant to §§4-7.

| $z$ | $E(z)$ | $H(z)$ [km/s/Mpc] | $a_0(z)$ [m/s²] | $a_0(z)/a_0(0)$ | $\sqrt{a_0(z)/a_0(0)}$ | $t_\text{age}$ [Gyr] |
|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 1.0000 | 67.40 | $1.20 \times 10^{-10}$ | 1.000 | 1.000 | 13.79 |
| 0.5 | 1.3223 | 89.12 | $1.59 \times 10^{-10}$ | 1.322 | 1.150 | 8.58 |
| 1.0 | 1.7906 | 120.69 | $2.15 \times 10^{-10}$ | 1.791 | 1.338 | 5.84 |
| 2.0 | 3.0327 | 204.40 | $3.64 \times 10^{-10}$ | 3.033 | 1.741 | 3.27 |
| 3.0 | 4.5682 | 307.90 | $5.48 \times 10^{-10}$ | 4.568 | 2.137 | 2.14 |
| 5.0 | 8.2972 | 559.23 | $9.96 \times 10^{-10}$ | 8.297 | 2.880 | 1.17 |
| 10.0 | 20.5255 | 1383.42 | $2.46 \times 10^{-9}$ | 20.526 | 4.530 | 0.470 |
| 15.0 | 36.0133 | 2427.29 | $4.32 \times 10^{-9}$ | 36.013 | 6.001 | 0.267 |

Two values fix the magnitude of the prediction. At $z = 2$, $a_0$ is $3.03$ times its local value with deep-MOND enhancement $1.74$; this is the cleanest window for direct rotation-curve and Tully-Fisher tests (§§4-5) and yields a 74% excess in lensing-inferred $M_\text{dyn}/M_b$ over local galaxies of the same baryonic mass (§6). At $z = 10$, $a_0$ reaches $20.5$ times its local value with deep-MOND enhancement $4.53$; this is the regime probed by JWST imaging of the earliest assembled stellar populations (§7), where the corresponding $E(z)^{1/4} \approx 2.13$ collapse-time speedup brings the inferred star-formation efficiencies of the impossibly-early candidates into the physically permitted range. The $a_0(z) = c H(z)$ heuristic implicit in the local Milgrom coincidence becomes a precise epoch-dependent statement rather than a numerical accident.

### 3.2 Figure 1: $a_0(z)/a_0(0)$ across cosmic time

**Figure 1.** $a_0(z)/a_0(0)$ from $z = 0$ to $z = 15$ under the framework prediction (3.1) with the standard flat ΛCDM expansion history (3.2) and Planck 2018 parameters [20]. The curve is the dimensionless Hubble parameter $E(z)$. Inflection from radiation-mediated to matter-dominated growth occurs near $z \sim 3000$ and is irrelevant to the redshift window probed by §§4-7. Log-uniform vertical axis recommended.

The shape of the curve in the regime $z = 0$ to $5$ is dominated by the matter term in (3.2); $E(z) \propto (1+z)^{3/2}$ to leading order. Above $z \sim 100$ radiation matters; this is far above the redshifts where the §§4-7 predictions live, and the parameterization in (3.2) is self-consistent throughout.

### 3.3 Cosmology dependence and consistency with the companion Λcos paper

A companion analysis on the surface sector (separately submitted) develops a topological resolution to the DESI DR2 [8] evidence for evolving dark-energy equation of state, working from the same scaling-law postulate (Appendix A.5). That analysis modifies the Friedmann form (3.2) by a phase-modulated Λ term with a single parameter $s_0 < 0.18$ (95% CL). Within the resulting $\Lambda\text{cos}$ cosmology the modifications to $E(z)$ are concentrated at $z < 1$ where Λ dominates the energy budget, and they fall below 1% for $z > 2$. The §3 table and §§4-7 predictions are therefore essentially independent of the cosmology choice within the redshift window where the present paper makes testable claims. Where the two cosmologies diverge ($z \lesssim 1$), the divergence is well within current observational uncertainties on $E(z)$ and on the §§4-7 observables.

We use the standard ΛCDM form throughout this paper for transparency and to allow direct comparison with published high-$z$ measurements that are typically reported under the same cosmology. The prediction of an evolving $a_0$ is independent of which member of the Λ family is chosen, because the cancellation in §2.4 strips the hierarchy factor regardless of how $H(z)$ itself is parameterized.

### 3.4 What §3 establishes

Equation (3.1), Table 1, and Figure 1 together fix the inputs that the rest of the paper consumes. Each of §§4-7 takes $a_0(z)$ from this section and evaluates a specific observable: the BTFR normalization (§4), galactic rotation curves (§5), galaxy-galaxy lensing (§6), and JWST star-formation efficiencies (§7). All four sections inherit the same epoch dependence from this section; none of them introduces new free parameters. The §§4-7 results are therefore predictions of a single one-parameter relation, calibrated by the local value $a_0(0) = 1.20 \times 10^{-10}$ m/s$^2$ from SPARC.

## 4. The baryonic Tully-Fisher relation across cosmic time

The baryonic Tully-Fisher relation (BTFR) is the empirical statement that the asymptotic flat rotation velocity $v_\text{flat}$ of a disk galaxy is set by its total baryonic mass $M_b$. In the deep-MOND limit it is theoretically forced:

$$v_\text{flat}^4 = G\,M_b\,a_0. \quad \text{(4.1)}$$

Equivalently, $M_b = A_\text{BTFR}\,v_\text{flat}^4$ with normalization $A_\text{BTFR} = (G\,a_0)^{-1}$. The local SPARC sample fits (4.1) with constant $a_0 = 1.20 \times 10^{-10}$ m/s$^2$ to remarkable precision: a single one-parameter relation describes baryonic disks spanning four decades in mass with intrinsic scatter of order 0.1 dex [2].

Under the framework derivation of §2, $a_0$ is epoch-dependent. Substituting (3.1) into (4.1):

$$v_\text{flat}^4(z) = G\,M_b\,a_0(z) = G\,M_b\,a_0(0)\,E(z), \quad \text{(4.2)}$$

so the BTFR normalization evolves as

$$\boxed{\;\frac{A_\text{BTFR}(z)}{A_\text{BTFR}(0)} = \frac{a_0(0)}{a_0(z)} = \frac{1}{E(z)}\;}. \quad \text{(4.3)}$$

The relation (4.3) carries no new free parameter beyond $a_0(0)$ from the local SPARC calibration and the standard cosmological $E(z)$ from §3.

### 4.1 Two equivalent forms of the prediction

Equation (4.2) admits two observationally distinct formulations.

**Form A (fixed baryonic mass).** A galaxy with the same $M_b$ as a local one rotates faster at higher redshift:

$$v_\text{flat}(z) = v_\text{flat}(0)\,E(z)^{1/4}. \quad \text{(4.4)}$$

The exponent $1/4$ is the BTFR exponent inverted; the per-redshift enhancement is mild because the shift is a fourth root.

**Form B (fixed rotation velocity).** A galaxy with the same $v_\text{flat}$ as a local one has less baryonic mass at higher redshift:

$$M_b(z, v_\text{flat}) = M_b(0, v_\text{flat})\,/\,E(z). \quad \text{(4.5)}$$

The exponent here is unity; the per-redshift shift in inferred baryonic mass is larger than the per-redshift shift in $v_\text{flat}$. Form A is the natural prediction for a survey that selects galaxies by stellar mass; Form B is natural for a survey that selects by velocity.

### 4.2 Numerical predictions

Table 2 evaluates (4.3)-(4.5) at six reference redshifts. The fractional shifts apply universally across the BTFR's full mass range; they do not depend on $M_b$.

**Table 2.** BTFR normalization, baryonic-mass shift at fixed velocity, and velocity shift at fixed baryonic mass under the framework prediction (4.3)-(4.5). The local theoretical BTFR normalization is $A_\text{BTFR}(0) = 1/(G\,a_0(0)) = 62.78$ $M_\odot/(\text{km/s})^4$ in the deep-MOND limit; see §4.4 for the relation to the SPARC empirical value.

| $z$ | $E(z)$ | $A_\text{BTFR}(z)\,[M_\odot/(\text{km/s})^4]$ | $A(z)/A(0)$ | $M_b/M_b(0)$ at fixed $v_\text{flat}$ | $v_\text{flat}/v_\text{flat}(0)$ at fixed $M_b$ |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 1.0000 | 62.78 | 1.0000 | 1.000 | 1.000 |
| 0.5 | 1.3223 | 47.48 | 0.7563 | 0.756 | 1.072 |
| 1.0 | 1.7906 | 35.06 | 0.5585 | 0.559 | 1.157 |
| 2.0 | 3.0327 | 20.70 | 0.3297 | 0.330 | 1.320 |
| 5.0 | 8.2972 | 7.57 | 0.1205 | 0.120 | 1.696 |
| 10.0 | 20.5255 | 3.06 | 0.0487 | 0.049 | 2.128 |

Two values anchor the predictive content. At $z = 2$, the BTFR normalization is one-third of its local value; equivalently, a galaxy at $z = 2$ with the same baryonic mass as a local one rotates 32% faster, and a galaxy at $z = 2$ with the same rotation velocity has one-third the baryonic mass. At $z = 1$, the corresponding numbers are 56% normalization, 16% velocity shift, 44% mass deficit. These are the regimes accessible to current and near-term integral-field spectroscopy of intermediate-redshift disks. As a worked example: a Milky Way-mass disk ($M_b \approx 6 \times 10^{10}\,M_\odot$, $v_\text{flat} \approx 220$ km/s at $z = 0$) is predicted under (4.4) to have $v_\text{flat} \approx 290$ km/s at $z = 2$.

### 4.3 Figure 2: BTFR loci at $z = 0$, $1$, $2$

**Figure 2.** Predicted BTFR loci $\log_{10} M_b$ vs $\log_{10} v_\text{flat}$ at $z = 0$, $1$, $2$ from (4.2). Three parallel lines of slope 4 with vertical offsets $\log_{10}(1/E(z))$. The dataset spans $v_\text{flat} = 30$ to $400$ km/s, covering dwarfs to massive disks. The local line is anchored to the theoretical deep-MOND $A_\text{BTFR}(0) = 62.78\,M_\odot/(\text{km/s})^4$.

The slope is identical across redshifts because the framework modifies only the normalization, not the exponent of (4.1). A measurement of slope evolution would constitute a separate test, distinct from the normalization test predicted here.

### 4.4 Theoretical vs empirical $A_\text{BTFR}(0)$

The deep-MOND theoretical value $A_\text{BTFR}(0) = 1/(G\,a_0(0)) = 62.78\,M_\odot/(\text{km/s})^4$ exceeds the empirical SPARC fit value of $A \approx 47\text{–}50$ by roughly a factor 1.3. The discrepancy traces to the choice of MOND interpolating function $\mu(x)$, which determines how the theoretical relation (4.1) is reached asymptotically as $g_N/a_0 \to 0$. Different reasonable choices of $\mu(x)$ shift the empirical normalization within this range without altering the deep-MOND limit [3].

The interpolating-function correction is irrelevant to the §4 prediction. Equation (4.3) is a statement about the *ratio* $A(z)/A(0)$, in which the interpolating-function dependence cancels identically. The framework prediction is observable as a redshift-dependent shift in the BTFR normalization relative to its local value, not as an absolute measurement of $A_\text{BTFR}(z)$. Any reasonable choice of $\mu(x)$ that fits the local SPARC sample inherits the same fractional evolution under (4.3).

A separate caveat applies to galaxies that sit in the intermediate MOND regime ($g_N \sim a_0$) at $z = 0$. Because the MOND transition radius $r_M = \sqrt{G\,M_b/a_0(z)}$ shrinks as $a_0(z)$ grows (§5), a galaxy that was MOND-dominated at large radii at $z = 0$ can be pushed further from the deep-MOND limit at higher $z$, with more of its outer disk falling into the transition or Newtonian regime. The BTFR prediction (4.2) and the ratio prediction (4.3) strictly apply in the deep-MOND limit, which encompasses the majority of the SPARC sample's outer radii but excludes the inner regions of the most massive disks. Precision predictions for intermediate-regime galaxies require the full interpolating function and a model of the baryonic mass distribution, and are beyond the scope of (4.3).

### 4.5 Falsification

The framework predicts a strict monotonic decrease of $A_\text{BTFR}(z)$ with redshift, with magnitude set by (4.3). Falsification at $\geq 2\sigma$ requires either:

- an observed $A_\text{BTFR}(z)$ at any single redshift inconsistent with the predicted value at $\geq 2\sigma$ after matched velocity-definition systematics are propagated, or
- an observed non-monotonic $A_\text{BTFR}(z)$ trend across $z$ that cannot be accommodated by any redshift-dependent systematic in the kinematic pressure-support correction.

The first criterion is testable today with stacked KMOS3D, MOSDEF, and KGES samples and will be sharpened by the Euclid DR1 galaxy catalog (October 2026). The second criterion requires kinematic measurements at a minimum of three redshift bins under matched velocity-correction prescriptions, a sample currently in assembly (see §8).

Existing intermediate-redshift BTFR measurements [9] test the §4 normalization prediction directly; the comparison, the framework's current status against the observed non-monotonic trend, and the next-generation tests that will resolve the constraint are treated in §8.

## 5. Rotation curves: MOND radius and asymptotic velocity across cosmic time

The BTFR prediction of §4 is the asymptotic statement: the flat rotation velocity $v_\text{flat}$ at large radius satisfies $v_\text{flat}^4 = G\,M_b\,a_0(z)$. The full rotation curve carries additional structural information. Two epoch-dependent observables follow from $a_0(z)$ that are not captured by the BTFR alone: the MOND transition radius and the shape of the rise-to-plateau in the rotation curve.

### 5.1 The MOND transition radius

The MOND transition radius $r_M$ is defined as the point where the Newtonian acceleration of a point mass equals $a_0(z)$:

$$g_N(r_M) = \frac{G\,M_b}{r_M^2} = a_0(z) \quad \Longrightarrow \quad r_M(z) = \sqrt{\frac{G\,M_b}{a_0(z)}}. \quad \text{(5.1)}$$

Substituting $a_0(z) = a_0(0)\,E(z)$:

$$\boxed{\;\frac{r_M(z)}{r_M(0)} = \frac{1}{\sqrt{E(z)}}\;}. \quad \text{(5.2)}$$

The transition radius shrinks with redshift as $E(z)^{-1/2}$, independent of galaxy mass. At $z = 2$, $r_M$ is $1/\sqrt{3.03} = 0.574$ times its local value; at $z = 5$, $0.347$; at $z = 10$, $0.221$. The MOND-to-Newtonian transition therefore happens at progressively smaller physical radii as one looks back in cosmic time.

The complement holds for the asymptotic flat velocity. From (4.4):

$$\frac{v_\text{flat}(z)}{v_\text{flat}(0)} = E(z)^{1/4}. \quad \text{(5.3)}$$

Equations (5.2) and (5.3) together state the full epoch dependence of the deep-MOND rotation curve at fixed baryonic distribution: the transition contracts as $E(z)^{-1/2}$ and the plateau rises as $E(z)^{1/4}$.

### 5.2 Numerical predictions for archetype galaxies

Table 3 evaluates (5.1)-(5.3) at $z = 0$ and $z = 2$ for four baryonic-mass archetypes spanning the SPARC range from dwarfs to giants.

**Table 3.** Predicted MOND transition radius and asymptotic flat velocity at $z = 0$ and $z = 2$ for four baryonic-mass archetypes. The shifts $r_M(z=2)/r_M(0) = 0.574$ and $v_\text{flat}(z=2)/v_\text{flat}(0) = 1.320$ are mass-independent and apply identically across the table. Galaxy archetypes are chosen with rounded baryonic masses $M_b$ and disk scale lengths $R_d$ matched to representative SPARC objects (DDO 154, NGC 2403, NGC 6946, UGC 2885).

| Archetype | $M_b$ [$M_\odot$] | $R_d$ [kpc] | $r_M(0)$ [kpc] | $r_M(2)$ [kpc] | $v_\text{flat}(0)$ [km/s] | $v_\text{flat}(2)$ [km/s] |
|---|---:|---:|---:|---:|---:|---:|
| Dwarf (DDO 154-like) | $3.5 \times 10^8$ | 0.5 | 0.64 | 0.37 | 49 | 64 |
| Sub-$L^*$ (NGC 2403-like) | $1.0 \times 10^{10}$ | 1.6 | 3.41 | 1.96 | 112 | 148 |
| $L^*$ (NGC 6946-like) | $6.0 \times 10^{10}$ | 2.5 | 8.35 | 4.79 | 176 | 232 |
| Giant (UGC 2885-like) | $1.5 \times 10^{11}$ | 8.0 | 13.20 | 7.58 | 221 | 292 |

The $L^*$ row provides the worked example. A galaxy with the baryonic distribution of NGC 6946 transitions to the MOND regime at $r_M = 8.35$ kpc at $z = 0$ and at $r_M = 4.79$ kpc at $z = 2$, with the asymptotic flat plateau rising from 176 km/s to 232 km/s. The plateau enhancement of 32% is the §4 BTFR prediction; the new content of §5 is that the plateau is reached at a smaller physical radius at $z = 2$ than at $z = 0$ for the same baryonic distribution.

The Table 3 comparison isolates the effect of $a_0(z)$ at fixed baryonic distribution. Real galaxies at $z = 2$ differ from their local counterparts in structural properties (gas fraction, scale length, velocity dispersion, merger state). §5.5 below gives the observer-facing formulation that uses the measured baryonic properties at each redshift directly, removing the need to assume any particular structural correspondence between local and high-$z$ samples.

### 5.3 Figure 3: $L^*$ rotation curve at $z = 0$ and $z = 2$

**Figure 3.** Predicted circular velocity $v_\text{circ}(r)$ for the $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$, $R_d = 2.5$ kpc) at $z = 0$ (lower curve, asymptote 176 km/s) and $z = 2$ (upper curve, asymptote 232 km/s). Computed using the simple-MOND interpolating function $\mu(x) = x/(1+x)$ with closed-form solution $g_\text{tot} = (g_N + \sqrt{g_N^2 + 4 g_N a_0(z)})/2$ and a point-mass approximation for the Newtonian source, $g_N(r) = G\,M_b/r^2$. The point-mass approximation is valid for $r \gtrsim R_d$ where the disk gravity is well represented by the enclosed-mass formula. The inner curve ($r < R_d$) is not plotted because the point-mass source underestimates the enclosed mass in the inner disk; an exponential-disk treatment with the full Bessel-function gravitational potential is required for accurate inner velocities. The plotted range $r \geq R_d$ is the regime where the present approximation is physically meaningful and is also the regime where the MOND transition lives for the chosen baryonic mass.

The two curves illustrate the structural prediction: at $z = 2$, the rotation curve at the same baryonic distribution rises faster (because the MOND radius is smaller and the deep-MOND regime is reached sooner) and plateaus higher (because $v_\text{flat}$ is larger). Both effects are direct consequences of the increased $a_0(z)$.

### 5.4 Figure 4: $r_M$ vs $z$ across galaxy mass

**Figure 4.** Predicted MOND transition radius $r_M(z)$ from $z = 0$ to $z = 5$ for the four archetype galaxies of Table 3. All four curves follow $r_M(z) = r_M(0)/\sqrt{E(z)}$ with the same fractional shape; they are vertically offset by $\sqrt{G\,M_b/a_0(0)}$ for each $M_b$.

The mass-independence of the fractional scaling is the testable feature: a measurement campaign that traced the MOND transition radius across a sample of galaxies spanning the BTFR's full mass range, at multiple redshifts, would test (5.2) directly. A failure of the fractional-shape universality would falsify the framework prediction more sharply than any single-galaxy measurement.

### 5.5 Application to observed high-$z$ galaxies

Equations (5.1)-(5.3) make a prediction observers can apply directly. Given an observed galaxy at known redshift $z$ with measured baryonic mass $M_b$ and either (i) a measured asymptotic flat velocity $v_\text{flat}^{\text{obs}}$ or (ii) a measured MOND transition radius $r_M^{\text{obs}}$, the framework predicts the corresponding quantity at the local-$a_0$ counterpart:

$$v_\text{flat}^{\text{pred}}(0; M_b) = v_\text{flat}^{\text{obs}}(z) / E(z)^{1/4}, \qquad r_M^{\text{pred}}(0; M_b) = r_M^{\text{obs}}(z)\,\sqrt{E(z)}.$$

These can then be compared to the local SPARC values for galaxies of the same $M_b$. Discrepancy beyond observational uncertainty falsifies (5.2) or (5.3); agreement extends the framework's reach.

The same framework also predicts a structural feature absent from constant-$a_0$ MOND: the rotation curve at $z = 2$ for a fixed baryonic distribution rises more steeply than the local rotation curve, because the MOND radius is smaller. A measurement of rotation-curve shape (rise time, transition slope) at intermediate redshift, controlled for baryonic distribution, tests this directly.

### 5.6 Falsification

Three independent falsification windows live in §5:

1. The asymptotic plateau prediction (5.3) at any single redshift, in tension with (4.5) of §4.
2. The MOND-radius scaling (5.2), tested by tracing the rotation-curve transition across a sample of high-$z$ galaxies.
3. The mass-independence of both (5.2) and (5.3), tested across the full BTFR mass range at the same redshift.

Any of these failing at $\geq 2\sigma$ after matched velocity-correction systematics constitutes falsification. The intermediate-$z$ rotation-curve constraints from KMOS3D and SINS [10,9] probe windows 1 and 3; their treatment is in §8.

## 6. Galaxy-galaxy weak lensing: dynamical mass enhancement across cosmic time

Galaxy-galaxy weak lensing measures the average tangential shear $\gamma_t(R)$ around galaxies of given baryonic mass and converts it to a projected dynamical mass $M_\text{dyn}(<R)$ within an aperture of physical radius $R$. The ratio $M_\text{dyn}/M_b$ inferred from this analysis is the standard observational measure of "missing mass" attributed under ΛCDM to dark matter halos. Under the framework, the same observation traces the evolution of $a_0(z)$.

### 6.1 The Newtonian inversion is theory-completion-agnostic

A relativistic completion of MOND (TeVeS, MOG, generalized Einstein-aether) is required to predict the full convergence profile $\gamma_t(R)$ of an isolated galaxy from first principles. The framework does not currently commit to a specific relativistic completion. The §6 prediction sidesteps this by working at the level of the inferred dynamical mass, which is theory-completion-agnostic in the following precise sense.

Any observer who measures the asymptotic flat velocity $v_\text{flat}$ at radius $R$ (whether by direct dynamics or by lensing) and applies the Newtonian inversion

$$M_\text{dyn}(R) = \frac{v_\text{flat}^2 \cdot R}{G} \quad \text{(6.1)}$$

infers the same $M_\text{dyn}$ regardless of which underlying gravitational theory produces $v_\text{flat}$. The Newtonian inversion (6.1) is the convention used in the published lensing literature; it converts a measured shear or rotation signal into a quoted "dark-matter mass" under standard assumptions. Whatever the relativistic completion, the framework predicts $v_\text{flat}(R, z) = (G\,M_b\,a_0(z))^{1/4}$ in the deep-MOND limit, and (6.1) then maps this to $M_\text{dyn}$ unambiguously.

The §6 prediction is therefore a statement about the *quoted lensing observable*, not about the underlying gravitational theory. Any relativistic extension of MOND that recovers the deep-MOND $v_\text{flat}$ produces the same prediction under (6.1).

### 6.2 The evolving dynamical-mass enhancement

Combining (6.1) with the deep-MOND $v_\text{flat}^4 = G\,M_b\,a_0(z)$:

$$M_\text{dyn}(R, z) = R \cdot \sqrt{\frac{M_b\,a_0(z)}{G}} = M_b \cdot \frac{R}{r_M(z)}, \quad \text{(6.2)}$$

with $r_M(z)$ the MOND radius from §5. The framework prediction follows directly:

$$\boxed{\;\frac{M_\text{dyn}(R, z)}{M_b} = \frac{R}{r_M(0)} \cdot \sqrt{E(z)}\;}. \quad \text{(6.3)}$$

At fixed aperture $R$ and fixed baryonic mass $M_b$, the inferred dynamical-mass-to-baryonic-mass ratio scales as $\sqrt{E(z)}$, which is the deep-MOND enhancement factor anchored in §3 Table 1. The scaling is universal: it does not depend on $M_b$ or on $R$ (provided $R \gg r_M(z)$, the deep-MOND condition).

The mass-aperture-independent enhancement is the defining feature of the §6 prediction. Three current near-term redshifts:

| $z$ | $\sqrt{E(z)}$ | percent excess in $M_\text{dyn}/M_b$ |
|---:|---:|---:|
| 0.5 | 1.150 | 15.0% |
| 1.0 | 1.338 | 33.8% |
| 2.0 | 1.741 | 74.1% |

A 74% excess in stacked $M_\text{dyn}/M_b$ at $z = 2$ relative to local galaxies of the same baryonic mass is the direct, theory-completion-agnostic prediction. It applies identically across galaxy mass and lensing aperture in the deep-MOND regime.

Under ΛCDM, the $M_\text{dyn}/M_b$ ratio at fixed baryonic mass and aperture also evolves with redshift, driven by halo concentration evolution and structural changes in the dark-matter halo population [15,16]. The discriminating test between the two pictures is therefore not the existence of redshift evolution but its functional form. We compute the ΛCDM prediction for an $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$) using a Moster-style stellar-to-halo mass relation [17] and the Duffy concentration $c(M_\text{halo}, z)$ [15], with the NFW enclosed mass at fixed physical aperture giving the inferred dynamical mass under the same Newtonian inversion (6.1). At the canonical $R = 100$ kpc aperture, the ΛCDM prediction is $M_\text{dyn}/M_b = 14.0$ at $z = 0$, $13.6$ at $z = 1$, and $13.7$ at $z = 2$: approximately flat with weak non-monotonicity. The framework prediction at the same aperture is $11.98 \to 16.03 \to 20.86$ across the same redshifts: monotonically increasing as $\sqrt{E(z)}$. The two pictures are quantitatively distinguishable at $z = 2$ by a factor of 1.52 in $M_\text{dyn}/M_b$, large enough to be targeted by a stratified Euclid DR1 stacked analysis (§6.6) once stellar-mass calibration, photometric-redshift uncertainty, aperture definition, and satellite/halo-modeling systematics are propagated.

The mass- and aperture-dependence of the ΛCDM prediction sharpens the discriminator further. At $R = 100$ kpc, the ΛCDM $M_\text{dyn}/M_b$ ratio at $z = 2$ relative to $z = 0$ is 0.76 for a Sub-$L^*$ ($M_b = 10^{10}\,M_\odot$) galaxy, 0.98 for $L^*$, and 1.13 for a Giant ($M_b = 1.5 \times 10^{11}\,M_\odot$). The framework predicts the same factor 1.74 for all three. At fixed $L^*$ baryonic mass, the ΛCDM ratio at $z = 2$ is 1.07 at $R = 30$ kpc, 0.98 at $R = 100$ kpc, and 0.92 at $R = 300$ kpc; the framework predicts the same factor 1.74 across all apertures. The framework's universal $\sqrt{E(z)}$ enhancement, mass-independent and aperture-independent in the deep-MOND regime, is the falsifiable signature that distinguishes the prediction from the ΛCDM halo-evolution picture under any reasonable choice of stellar-to-halo mass relation and concentration parameterization.

A Euclid DR1 stacked analysis at $z = 2$ stratified by both galaxy stellar mass and aperture therefore tests the framework on two independent axes simultaneously: the magnitude of the redshift shift (74% predicted vs $\sim 0\%$ under ΛCDM at $L^*$) and its universality across mass and aperture (universal under MIT vs varying by 36 percentage points across the dwarf-to-giant range under ΛCDM).

### 6.3 Numerical predictions for the $L^*$ archetype

Table 4 evaluates (6.3) for the $L^*$ archetype at three standard galaxy-galaxy lensing apertures (30, 100, 300 kpc) at five redshifts. The $L^*$ block is shown in the main text as the canonical case; the complete table covering all four §5 archetypes (Dwarf, Sub-$L^*$, $L^*$, Giant) is provided as supplementary data and exhibits the same row-by-row fractional scaling.

**Table 4.** Predicted $M_\text{dyn}/M_b$ from (6.3) for the $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$) at three apertures and five redshifts. Values within each row scale as $\sqrt{E(z)}$. The same fractional scaling holds across the Dwarf, Sub-$L^*$, and Giant archetypes, confirming the mass- and aperture-independence of the prediction.

| $R$ [kpc] | $z = 0$ | $z = 0.5$ | $z = 1$ | $z = 2$ | $z = 5$ |
|---:|---:|---:|---:|---:|---:|
| 30 | 3.59 | 4.13 | 4.81 | 6.26 | 10.35 |
| 100 | 11.98 | 13.77 | 16.03 | 20.86 | 34.50 |
| 300 | 35.94 | 41.32 | 48.09 | 62.58 | 103.51 |

The fractional shift from $z = 0$ to $z = 2$ is identical across all three rows: a factor $1.741$ ($\sqrt{E(z=2)}$). The $R = 100$ kpc row provides the canonical galaxy-galaxy lensing example: a quoted $M_\text{dyn}/M_b = 11.98$ at the local Universe (the standard "dark-matter dominated" inference of $\sim 92\%$ dark mass fraction) becomes $20.86$ at $z = 2$ (under the same Newtonian inversion, $\sim 95\%$ inferred dark mass fraction). The 74% excess is the framework prediction, observable directly through stacked lensing at known galaxy redshift. The mass-independence of the same enhancement, verified across the full supplementary table, is what distinguishes the framework prediction from the ΛCDM halo-concentration alternative discussed in §6.2.

### 6.4 Figure 5: $M_\text{dyn}/M_b$ vs aperture for $L^*$ at $z = 0, 1, 2$

**Figure 5.** Predicted $M_\text{dyn}(R)/M_b$ for the $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$) as a function of physical aperture $R$ from 10 to 500 kpc, at $z = 0$, $z = 1$, $z = 2$. The framework prediction (6.3) is plotted as solid lines (lower at $z = 0$, middle at $z = 1$, upper at $z = 2$); three lines of slope unity in $\log R$, vertically offset by $\log_{10}\sqrt{E(z)}$. The ΛCDM prediction under standard halo concentration evolution [15] is plotted as dashed lines for comparison.

The framework's vertical offset is the §6 prediction: constant in $\log_{10} M_\text{dyn}/M_b$ across the full plotted aperture range, growing as $\sqrt{E(z)}$ between redshifts. The ΛCDM curves are nearly degenerate across $z = 0$, $1$, $2$ because halo concentration decreases with $z$ approximately compensates the implicit halo-mass evolution under the SHMR; the residual aperture-dependence and mass-dependence of the ΛCDM prediction are the discriminators against the framework's universal enhancement, as quantified in §6.2.

### 6.5 What the framework does not predict here

Three lensing observables are *not* addressed by §6, and require future work:

1. *The full convergence profile $\gamma_t(R)$ as a function of aperture for an isolated galaxy.* This requires committing to a relativistic completion of MOND, which the framework does not yet do.

2. *Cluster-scale lensing.* The MOND-cluster mass discrepancy [12] is an inherited problem from local MOND that evolving $a_0$ does not resolve, because clusters are observed at $z \lesssim 0.3$ where $a_0(z)/a_0(0) \leq 1.17$. The framework's contribution at cluster scales is at the percent level, well below the factor $\sim 5$ cluster discrepancy. §8 treats this in full.

3. *The sign and magnitude of any non-deep-MOND-regime corrections to (6.3).* For galaxies at intermediate accelerations ($g_N \sim a_0$) at $z = 0$, the same caveat from §4.4 applies: the deep-MOND ratio prediction may not extend cleanly into the transition region, where the interpolating function matters. (6.3) strictly applies in the deep-MOND limit.

These three are open. The $M_\text{dyn}/M_b$ scaling (6.3) is what the framework predicts directly and unambiguously; the rest is acknowledged outside the scope.

### 6.6 Falsification

The §6 prediction (6.3) admits two independent falsification windows:

1. The $\sqrt{E(z)}$ scaling at any single redshift, tested by stacked galaxy-galaxy lensing of mass-controlled galaxy samples at that redshift. A measured $M_\text{dyn}/M_b$ at $z = 2$ that is *not* enhanced by $\sim 74\%$ relative to $z = 0$ at the same baryonic mass and aperture, beyond systematic uncertainty, falsifies (6.3).

2. The mass- and aperture-independence of the enhancement, tested by stratifying the lensing analysis by both galaxy stellar mass and aperture. The fractional shift must be $\sqrt{E(z)}$ in every cell.

Both windows are accessible to Euclid DR1 (October 2026) galaxy-galaxy lensing at $z = 0.5\text{–}2$ with stacked samples of $\sim 10^5$ galaxies. The expected statistical sensitivity at fixed $M_b$ stratification is at the few-percent level on $M_\text{dyn}/M_b$, which is well below the 15-74% predicted shifts across the $z = 0.5$ to $2$ window.

The forward reference to §8 covers the inherited cluster-MOND discrepancy and any current intermediate-$z$ lensing constraints.

## 7. JWST early galaxies: collapse-time speedup at $z \sim 7\text{–}9$

JWST imaging of the early universe has revealed candidate galaxies at $z = 7\text{–}10$ with stellar masses $M_\star \gtrsim 10^{10}\,M_\odot$ assembled within $\sim 600$ Myr of the Big Bang [6]. Under ΛCDM with standard halo growth and star-formation efficiency assumptions, the most massive of these candidates require $\varepsilon_\text{SF} \gtrsim 1$, formally impossible because no more than the cosmic-baryon-fraction-times-halo-mass can be converted into stars. The tension has prompted proposals invoking modified initial conditions, high primordial density peaks, or non-standard early IMFs. The framework offers a different resolution: under evolving $a_0(z)$, the effective gravitational acceleration in collapsing baryonic perturbations is enhanced by $\sqrt{a_0(z)/a_0(0)} = \sqrt{E(z)}$, and the corresponding free-fall collapse time is shortened by $E(z)^{1/4}$.

### 7.1 The collapse-speedup prediction

In the deep-MOND regime, the effective gravitational acceleration on a perturbation is

$$g_\text{eff}(z) = \sqrt{g_N \cdot a_0(z)}, \quad \text{(7.1)}$$

so that $g_\text{eff}(z)/g_\text{eff}(0) = \sqrt{a_0(z)/a_0(0)} = \sqrt{E(z)}$ at fixed Newtonian source $g_N$. The free-fall collapse time scales as $t_\text{ff} \propto 1/\sqrt{g_\text{eff}}$, so

$$\boxed{\;\frac{t_\text{ff}(z)}{t_\text{ff}(0)} = \frac{1}{E(z)^{1/4}}\;}, \quad \text{(7.2)}$$

i.e. the framework predicts that gravitational collapse at high redshift completes faster by a factor $E(z)^{1/4}$ than the constant-$a_0$ MOND benchmark. To order of magnitude, if collapse timescale sets the duty cycle of star formation, then the same stellar mass can be assembled with a star-formation efficiency lower by $E(z)^{1/4}$. Equivalently, the required $\varepsilon_\text{SF}$ to produce a given $M_\star$ at observed redshift $z$ is reduced from the ΛCDM value by

$$\varepsilon_\text{SF}^\text{MIT}(z) = \varepsilon_\text{SF}^{\Lambda\text{CDM}}(z) \cdot \frac{1}{E(z)^{1/4}}. \quad \text{(7.3)}$$

The factor $E(z)^{1/4}$ is anchored in §3 Table 1 (the deep-MOND enhancement column $\sqrt{E(z)}$ is its square; the speedup is the fourth root of $E(z)$). It is universal across galaxy mass and source distribution. The fourth-root dependence also makes the speedup robust against uncertainties in the expansion history at high redshift: a 10% change in $E(z)$ shifts the predicted efficiency correction by less than 3%, so the §7.2 sample-level result does not depend critically on the precision of the assumed cosmology.

### 7.2 Application to the Labbé et al. 2023 candidate sample

Table 5 lists the six central-value massive candidates ($\log_{10}(M_\star/M_\odot) > 10$) from the public Labbé sample [6], together with the framework speedup factor $E(z)^{1/4}$ at each candidate's photometric redshift.

**Table 5.** Framework collapse-speedup factor $E(z)^{1/4}$ for the six massive central-value candidates from Labbé et al. 2023 [6]. Photometric redshifts and stellar masses from the public catalog associated with the Nature publication. The speedup factor is the multiplicative reduction in required star-formation efficiency under (7.3).

| ID | $z_\text{phot}$ | $\log_{10}(M_\star/M_\odot)$ | $E(z)^{1/4}$ |
|---:|---:|---:|---:|
| 11184 | 7.318 | 10.18 | 1.917 |
| 38094 | 7.477 | 10.89 | 1.931 |
| 2859 | 8.106 | 10.03 | 1.983 |
| 13050 | 8.137 | 10.14 | 1.986 |
| 14924 | 8.831 | 10.02 | 2.041 |
| 35300 | 9.077 | 10.40 | 2.060 |

The speedup factor is uniformly $\sim 1.92\text{–}2.06$ across the sample, varying by less than 8% across the full $z = 7.3\text{–}9.1$ range. The framework therefore reduces the required star-formation efficiency by approximately a factor of two for every massive candidate in the sample, with no per-galaxy tuning. The published Labbé analysis reports $\varepsilon_\text{SF}^{\Lambda\text{CDM}}$ ranging from $\sim 0.4$ to $\geq 1$ across the sample; under (7.3), the framework reduces these required efficiencies by a uniform factor of $E(z)^{1/4} \approx 1.9\text{–}2.1$, which can move the most extreme cases ($\varepsilon_\text{SF}^{\Lambda\text{CDM}} \geq 1$) from formally impossible to permitted under the published halo-mass assumptions.

The per-object ε_SF analysis with explicit halo abundance matching, which requires assumptions about the halo mass function and survey volume that vary across published prescriptions, is reserved for the companion Zenodo preprint to this paper.

### 7.3 Status, caveats, and falsification

**Status.** The §7 prediction is the universal speedup factor $E(z)^{1/4}$, not the per-galaxy efficiency. The latter inherits its uncertainty from the ΛCDM-side modeling (halo mass function, abundance matching, survey volume, photometric-redshift uncertainty). The framework contribution is the multiplicative correction.

**Caveats.** The prediction (7.2) is a free-fall scaling argument, not a full simulation of structure formation under modified gravity. Two physical effects are not captured: (i) the back-reaction of the modified collapse rate on the baryon-to-dark-matter ratio in the collapsing region, and (ii) any modification to the initial-condition power spectrum from the §8 mode-selection question regarding cosmological perturbations. Both are open work and would refine but not overturn the order-of-magnitude estimate.

**Falsification.** A measurement that confirms the Labbé candidates are genuine ($z \sim 7\text{–}9$, $M_\star \sim 10^{10}\,M_\odot$) but inconsistent with $\varepsilon_\text{SF} \sim 0.5$ at the $\geq 2\sigma$ level after halo-mass uncertainty is propagated would falsify (7.2). Spectroscopic confirmation of the central-value masses and redshifts of the impossible candidates with JWST/NIRSpec is the immediate test. The full sample-level test will follow with the COSMOS-Web spectroscopic complete to $z \sim 10$ in the next two years, well in advance of the Euclid DR1 weak-lensing window of §6.

The §7 prediction is therefore a near-term, falsifiable corollary of the §3-§6 framework that addresses an existing ΛCDM tension without invoking new physics beyond the same $a_0(z) \propto E(z)$ scaling already required by §§4-6. It is supporting evidence in the present paper rather than the centerpiece, because the per-object analysis depends on ΛCDM-side modeling that the framework does not improve directly.

## 8. Existing constraints and consistency

The framework predictions of §§4-7 are tested against existing measurements in five regimes: local galactic dynamics ($z \approx 0$), intermediate-redshift kinematics ($z = 0.5\text{–}2.5$), galaxy clusters ($z \lesssim 0.3$), the cosmic microwave background ($z \approx 1090$), and strong gravitational lensing time delays. Each regime is treated separately because the constraints are independent and the framework's status differs across them.

### 8.1 Local galactic dynamics: SPARC and THINGS

The framework reproduces local MOND phenomenology by construction. The well assignments in §2 were calibrated against the local values $a_0(0) = 1.20 \times 10^{-10}$ m/s$^2$ and $H_0 = 67.4$ km/s/Mpc, and the BTFR normalization, rotation-curve fits, and lensing inferences at $z \approx 0$ inherit the standard MOND results documented in the SPARC and THINGS analyses [18,2,3]. No independent test at $z = 0$ is provided by the present paper; the §3 calibration is what the §§4-7 predictions are extrapolations from.

### 8.2 Intermediate-redshift Tully-Fisher: KMOS3D

The KMOS3D analysis of Übler et al. 2017 [9] reports the baryonic Tully-Fisher relation at two redshift bins, drawing on VLT/KMOS integral-field spectroscopy of $\sim 240$ star-forming galaxies. Their fixed-slope zero-points are $b = 10.68 \pm 0.04$ at $z \approx 0.9$ and $b = 10.85 \pm 0.05$ at $z \approx 2.3$. Relative to the local Lelli et al. baseline [2], their fiducial pressure-support-corrected analysis reports zero-point offsets

$$\Delta b^\text{obs}(z=0.9) = -0.44~\text{dex}, \qquad \Delta b^\text{obs}(z=2.3) = -0.27~\text{dex}.$$

The framework prediction (4.3) gives

$$\Delta b^\text{MIT}(z=0.9) = -\log_{10} E(0.9) = -0.227~\text{dex}, \qquad \Delta b^\text{MIT}(z=2.3) = -0.540~\text{dex}.$$

The Übler measurement is the only existing quantitative test of the §4 framework prediction at intermediate redshift. The other intermediate-$z$ kinematic samples treated below (Genzel et al. 2017 [10]) do not report a BTFR zero-point, and the next quantitative tests will arrive with Euclid DR1.

**Magnitude.** The framework predictions and the Übler observations are in the same envelope: both are large negative shifts, both place the high-$z$ BTFR substantially below the local relation. Neither value rules out the framework at $\geq 2\sigma$ when systematic uncertainties on the velocity-correction prescription are propagated.

**Trend shape.** The observed offsets are non-monotonic in redshift ($-0.44 \to -0.27$ dex), while the framework predicts a strict monotonic decrease ($-0.227 \to -0.540$ dex). This is the core of the tension: the framework's evolution prediction is monotonic, the observation is not.

Quantitatively, the residuals (observed minus MIT prediction) are $-0.216$ dex at $z \approx 0.9$ and $+0.270$ dex at $z \approx 2.3$, with opposite signs reflecting the non-monotonic trend. Translating to $\sigma$ tensions under three uncertainty budgets:

| Uncertainty budget | $T(z=0.9)$ [σ] | $T(z=2.3)$ [σ] | Joint [σ] |
|---|---|---|---|
| Übler statistical only | $-5.4$ | $+5.4$ | $7.6$ |
| + Lelli local-baseline (0.05 dex) | $-3.4$ | $+3.8$ | $5.1$ |
| + velocity-correction systematic (0.10 dex) | $-1.8$ | $+2.2$ | $2.9$ |

Even under the most conservative budget, with a generous 0.10 dex velocity-correction systematic added in quadrature, the joint tension is $2.9\sigma$ and the $z = 2.3$ point individually sits at $2.2\sigma$. Both exceed the $\geq 2\sigma$ falsification threshold stated in §10 Table 8. Under more defensible Budget B (statistical plus the standard SPARC local-baseline uncertainty), the joint tension is $5.1\sigma$. The current Übler data therefore constitutes a genuine quantitative tension with the framework's monotonic prediction at the trend-shape level, not a marginal disagreement that conservative systematics could absorb.

The Übler pressure-support correction is a radial thick-disk expression $v_\text{circ}^2(r) = v_\text{rot}^2(r) + 2\,\sigma_0^2\,r/R_d$ [19], with the effective coefficient $\alpha(r) = 2r/R_d$ depending on the radial position at which $v_\text{rot}$ is measured and on the disk scale length $R_d$. Both quantities evolve systematically with redshift. A fixed-coefficient surrogate, with $\alpha$ chosen to grow plausibly across the literature range $\alpha \in [1.5, 3.4]$, fails to reproduce the observed non-monotonic offset pattern: such a model can match the $z \approx 2.3$ point but cannot simultaneously drive the $z \approx 0.9$ point down to $-0.44$ dex without requiring an unphysical $\alpha(z=0.9) \approx 0$. A full simulation under Übler's actual radial systematic, with sample-realistic distributions of $R_d$ and the radius at which the circular velocity is measured, is reported below as the H10 forward-model analysis.

The framework's posture toward this constraint is to state the prediction without retreating to a softer claim. The §4 prediction is a monotonic decrease in the BTFR normalization with redshift, with magnitude set by $1/E(z)$. The Übler measurement is currently the only quantitative test of that prediction at intermediate redshift, and it is in tension at the trend-shape level.

We tested whether the Übler radial pressure-support correction can produce the observed non-monotonic offset pattern from a monotonic underlying BTFR. Mock galaxies at $z = 0.9$ and $z = 2.3$ were generated under the framework's BTFR (4.3) with literature-realistic distributions of baryonic mass, disk scale length, and intrinsic velocity dispersion (Wisnioski et al. 2015 [11] medians of $\sigma_0 \approx 25$ km/s at $z = 0.9$ and $\sigma_0 \approx 50$ km/s at $z = 2.3$). The Übler radial thick-disk correction $v_\text{circ}^2(r) = v_\text{rot}^2(r) + 2\sigma_0^2 r/R_d$ was applied at $r_\text{max} \approx 2.2\,R_d$ together with the published $v_\text{rot,max}/\sigma_0 > 4.4$ selection cut. We swept four bias models (radial-position uncertainty, beam-smearing of $\sigma_0$ at high $z$, non-asymptotic rotation curves at low $z$, and selection-induced mass-distribution shifts) over literature-plausible parameter ranges. None of the models produces the observed $(-0.44, -0.27)$ dex pattern. The closest combined model recovers $(-0.295, -0.472)$ dex, leaving the $z = 0.9$ point still 0.15 dex above observed.

The Übler tension is therefore not a velocity-correction artifact under any literature-plausible bias model. It is a genuine tension between the framework's monotonic prediction and the observed non-monotonic trend, and it cannot be dissolved by the simple systematic the §8.2 defense initially proposed.

Two concrete resolution paths remain:

(i) The Euclid DR1 NISP grism survey (October 2026) delivers H$\alpha$ kinematics at $z = 0.7\text{–}1.8$ and [OIII] at $z = 1.1\text{–}2.4$ from a single instrument under uniform selection, providing the first self-consistent cross-redshift BTFR comparison free of the matched-tracer systematic that limits existing ground-based analyses. The expected sample size is $\sim 10^5$ galaxies in the wide survey, more than two orders of magnitude beyond the Übler sample, with statistical sensitivity to $\Delta b$ at the 0.02-dex level after mass stratification.

(ii) JWST follow-up of resolved kinematics at $z \approx 0.9$ and $z \approx 2.3$ in matched samples (COSMOS-Web NIRSpec IFU and NIRCam grism programs already underway) allows a direct test of (4.3) under controlled velocity-correction prescriptions applied identically across both redshift bins, removing the cross-instrument systematic that affects the existing ground-based comparison.

The framework's evolution prediction stands as the §4 derivation requires; its status against the present Übler measurement is one of genuine tension on the trend shape, and resolution awaits the next-generation matched-systematics measurements named above. The framework neither retreats from the prediction nor pretends to have explained the tension away.

### 8.3 Intermediate-redshift rotation curves: SINS and KMOS3D

The Genzel et al. 2017 sample [10] of six massive star-forming disks at $z = 0.85\text{–}2.38$ reports declining outer rotation curves with low inferred dark-matter fractions, interpreted as baryon-dominated disks with pressure support. Because no BTFR zero-point is reported, the measurement is qualitatively consistent with §§4-5 but does not directly test the framework's normalization prediction (4.3). A joint re-analysis of the Genzel and Übler samples under matched velocity-correction prescriptions would convert this into a sharper constraint.

### 8.4 Galaxy clusters: the Pointecouteau-Silk discrepancy

Local MOND analyses of galaxy clusters report a residual mass discrepancy beyond what MOND alone provides. Pointecouteau & Silk (2005) [12] find that eight nearby relaxed X-ray clusters require an effective $a_0 = (4.75 \pm 1.24) \times 10^{-8}$ m/s$^2$, approximately five times the galaxy-scale value, to reproduce the observed dynamical mass with MOND alone. Equivalently, MOND with the standard galactic $a_0$ underpredicts the cluster dynamical mass by roughly a factor of $\sim 5$ at $r \approx 0.5\,R_\text{vir}$.

The framework's evolving $a_0(z)$ does not resolve this discrepancy. The Pointecouteau-Silk sample lives at $z \lesssim 0.15$, where $E(z) \leq 1.08$ and the framework $a_0(z)$ exceeds the local value by less than 8%. Even at $z = 0.3$, the upper end of the cluster lensing literature, the framework correction is at most $\sim 17\%$. A factor of $\sim 5$ residual discrepancy is not addressed by a $\lesssim 17\%$ correction.

The cluster discrepancy is therefore an inherited problem from local MOND that the framework's epoch dependence does not address at the relevant cluster redshifts. The standard local-MOND interpretations of the discrepancy (residual gravitational sources at cluster scales, undetected baryonic components, or a breakdown of MOND in the cluster regime) apply unchanged. The cluster-scale mass discrepancy is an open problem shared by all MOND-class theories [13,14,3] and predates the present framework. The framework's epoch-dependent modification operates at the percent level in the cluster redshift range and neither introduces nor resolves this discrepancy.

### 8.5 The cosmic microwave background at recombination

A naive application of the framework's $a_0(z)$ scaling to cosmological perturbations at recombination produces large modifications to the predicted CMB acoustic peak structure. At $z = 1090$, $a_0(z) \approx 2.79 \times 10^{-6}$ m/s$^2$, approximately 23,000 times the local value. The Newtonian gravitational acceleration of perturbations at the sound-horizon scale (133 kpc physical at recombination, corresponding to the comoving sound horizon of $\sim 145$ Mpc) with amplitude $\delta\rho/\rho \sim 10^{-5}$ is $g_N^\text{pert} \sim 4 \times 10^{-11}$ m/s$^2$, roughly five orders of magnitude below $a_0(z)$ at the same epoch. Under this naive reading, perturbations at recombination would be deeply in the MOND regime and the acoustic-peak amplitudes would deviate significantly from the well-fit ΛCDM prediction.

The naive reading misapplies the framework's selection rule. The rule, introduced in §2 and detailed in Appendix A.5, assigns observables to manifold-mode classes by the index $n$ in the embedding hierarchy $S^1 \subset \text{Mobius} \subset S^3$:

| Mode | $n$ | References | Evolves? | Governs |
|---|---:|---|---|---|
| Edge | 1 | $\Omega_H(z)$ | Yes | Galactic dynamics ($a_0$, $H$) |
| Surface | 2 | $\Omega_\Lambda$ | No | Vacuum energy (Λ) |
| Space | 3 | $\Omega_\Lambda$ | No | Cosmological perturbations |

The selection rule is not a free choice introduced to escape the CMB constraint. It is the same rule that produces Λ at the 2% level (surface mode), $H_0$ at the 2% level (edge mode), the Milgrom ratio $a_0/(cH_0)$ at 0.8% (the §2.5 cancellation), and the fine-structure constant $\alpha$ at 0.5% (separate sector); the four percent-level matches are tabulated in Appendix A.7. Each is a successful prediction from a single $(n, \Omega)$ rule applied to a different observable. The rule's correctness across four independent observables of wildly different magnitudes is direct empirical validation; it predates the $a_0(z)$ derivation in §2 and was not constructed to address the CMB constraint.

Under the rule, cosmological perturbations are a space-mode observable ($n = 3$): they live on the spatial slice $S^3$ and propagate through it. The hierarchy reference for the space mode is $\Omega_\Lambda$, the same fixed eigenvalue ratio that fixes Λ in the surface sector. The framework therefore predicts that the dynamical evolution of cosmological perturbations is governed by space-mode physics referenced to a constant $\Omega_\Lambda$, with no $a_0(z)$ modification. This is structurally distinct from the edge sector ($n = 1$) where $a_0$ lives.

The framework's CMB prediction is therefore identical to ΛCDM's CMB prediction. The $a_0(z)$ scaling derived in §2 governs the edge sector, where galactic dynamics live at $r \sim r_M$ and the kinematic horizon $\Omega_H(z)$ sets the hierarchy. Recombination physics is a space-mode phenomenon, governed by $\Omega_\Lambda$, and inherits ΛCDM's predictions for the acoustic peak structure, the polarization spectra, the lensing reconstruction, and the integrated Sachs-Wolfe imprint. The success of ΛCDM in fitting Planck 2018 [20] at sub-percent precision is empirical confirmation that the framework's $n = 3$ assignment for cosmological perturbations is correct: the ΛCDM fit *is* the validation of the framework's space-mode physics, not a competitor to it.

We now make this consistency condition quantitative. Writing a minimal leakage ansatz for any residual edge-mode coupling into cosmological perturbations,

$$g_\text{eff}(R, z) = g_N(R, z) + \varepsilon \cdot \sqrt{g_N(R, z) \cdot a_0(z)},$$

the sound-horizon perturbation at recombination ($R \approx 0.13$ Mpc physical, $g_N \approx 4 \times 10^{-11}$ m/s$^2$) and the sub-horizon BAO scale ($R \approx 0.05$ Mpc, $g_N \approx 1.5 \times 10^{-11}$ m/s$^2$) have $\sqrt{a_0(z=1090)/g_N} = 264$ and $430$, respectively. Under the Sachs-Wolfe relation $\Delta T/T \approx \Phi/3$, any leakage at level $\varepsilon$ produces a fractional first-peak amplitude shift $\delta C_\ell^\text{peak}/C_\ell^\text{peak} \approx \varepsilon \cdot \sqrt{a_0/g_N}$. The Planck 2018 first-peak amplitude precision (literal value $39/5733 \approx 0.68\%$, conservative reading $0.5\%$) bounds the leakage to

$$\varepsilon \lesssim 1.2 \times 10^{-5} \quad (0.5\% \text{ tolerance}), \qquad \varepsilon \lesssim 1.6 \times 10^{-5} \quad (\text{literal Planck}),$$

with the sub-horizon BAO scale providing the most-constraining bound. The bound is robust against ansatz choice (modified interpolation function, scale-dependent coupling) within an order of magnitude. The framework's selection rule predicts $\varepsilon = 0$ exactly under the $n = 3$ space-mode assignment for cosmological perturbations, satisfying the empirical bound by every margin Planck currently provides.

The remaining open question is a first-principles perturbation-theoretic derivation of the edge/space-mode decoupling at recombination-relevant scales, working from the Boltzmann hierarchy or equivalent under the manifold-mode framework. Such a derivation would replace the structural argument plus empirical bound with a closed-form proof and is flagged as future work for the framework's perturbation-theory development. The §8.5 position is that the apparent CMB tension under the naive over-application of $a_0(z)$ dissolves under the framework's own selection rule, that the rule has independent empirical validation across four observables of wildly different magnitudes, that any residual edge-mode leakage into cosmological perturbations is bounded to $\varepsilon \lesssim 10^{-5}$ by Planck consistency with the framework's structural prediction $\varepsilon = 0$ satisfying the bound exactly, and that the framework's CMB prediction coincides with ΛCDM's at every observable Planck has measured.

### 8.6 Strong gravitational lensing time delays

Strong-lensing time-delay cosmography (TDCOSMO, H0LiCOW) probes $H_0$ at sub-percent precision but is not currently sensitive to $a_0(z)$ at the level of the framework's predictions, because the time-delay signal lives at lens-galaxy scales where the MOND interpolating function matters and the deep-MOND ratio prediction (4.3) does not strictly apply. Existing time-delay analyses are consistent with both the framework and standard ΛCDM at current precision; no live constraint exists in this regime.

### 8.7 Summary of constraint status

**Table 6.** Summary of existing constraint status across the five regimes treated above.

| Regime | Constraint | Framework status |
|---|---|---|
| Local ($z = 0$) | SPARC, THINGS | Consistent by construction (§2 calibration) |
| Intermediate-$z$ BTFR | Übler 2017 [9] | Live tension on trend shape; H10 forward-model confirms not a velocity-correction artifact |
| Intermediate-$z$ rotation curves | Genzel 2017 [10] | Qualitatively consistent; not a sharp quantitative test |
| Galaxy clusters | Pointecouteau-Silk 2005 [12] | Inherited problem unaddressed by epoch-dependent $a_0$; not worsened by the framework |
| CMB ($z \approx 1090$) | Naive over-application | Resolved structurally by the §2 selection rule; minimal-leakage Planck bound $\varepsilon \lesssim 10^{-5}$ confirms consistency with the framework's structural $\varepsilon = 0$ prediction; rigorous derivation open |
| Strong-lens time delays | TDCOSMO, H0LiCOW | Below current sensitivity; consistent at present |

The status column reads as one live tension (Übler, with the velocity-correction systematic explanation tested and ruled out by forward-modeling), one inherited open problem (clusters, neither caused nor resolved by the framework), one structurally resolved apparent tension (CMB, with rigorous derivation flagged), one qualitative consistency (Genzel), and two consistencies by construction or below sensitivity.

The framework is therefore consistent with the existing constraint landscape at the level of the present paper's claims, except for the Übler trend-shape tension which is acknowledged and held against the framework's explicit prediction. The Euclid DR1 galaxy-galaxy lensing measurement (§6) and the matched-velocity-correction Tully-Fisher analysis (§4, §8.2) are the two near-term tests that will sharpen the constraint into a definitive result, in either direction, on a timescale of approximately two years.

## 9. Connection to the companion Λcos prediction and the broader framework

### 9.1 Two predictions from one scaling law

The framework derivation of §2 makes two structurally independent predictions about cosmic evolution, both following from the same measurement postulate $A/A_P = C(\Theta)\,(\sqrt{\Omega})^{-n}$ but addressing different sectors of the manifold-mode hierarchy.

**§§3-7 (this paper).** The MOND acceleration scale is an edge-mode observable ($n = 1$) referenced to the kinematic horizon ratio $\Omega_H = (c/(H\,\ell_P))^2$. The local-epoch reading of (2.1) gives $a_0(z) = a_0(0)\,E(z)$, governing galactic-scale dynamics across cosmic time and tested through the five-exponent prediction set summarized in §10.

**Surface-sector prediction (separately submitted companion analysis).** The cosmological constant Λ is a surface-mode observable ($n = 2$) referenced to the eigenvalue ratio $\Omega_\Lambda$ (Appendix A.5). The local-epoch reading of (2.1) gives $\Lambda = \text{const.}$ at every epoch, while the apparent equation-of-state evolution $w(z)$ reported by DESI DR2 [8] arises as a template artifact from the observer's phase position $t \approx 5.22$ rad on the underlying standing wave $\Psi(t) = \cos(t/2)$.

The §8.5 selection rule organizes both predictions in a single table: the edge sector evolves through $\Omega_H(z)$, the surface sector remains fixed through $\Omega_\Lambda$, and (a third assignment relevant to §8.5's CMB consistency) the space sector ($n = 3$) governs cosmological perturbations also through $\Omega_\Lambda$. The two papers test the first two rows of that table; their joint outcome tests the rule itself.

The structural symmetry is the headline: the framework predicts that $a_0$ evolves while Λ does not, the inverse of standard ΛCDM assumptions where Λ is the candidate evolving quantity (DESI's $w(z)$) and $a_0$ is assumed to be a universal constant.

### 9.2 Independent tests, joint pattern

The two predictions are testable through disjoint instruments and analyses, and either could be confirmed or falsified independently of the other.

**Edge-sector tests (this paper).** Intermediate-redshift Tully-Fisher (KMOS3D, KGES), galaxy-galaxy weak lensing (Euclid DR1), and JWST early-galaxy spectroscopy. Five distinct observables, all governed by powers of $E(z)$ as compiled in §10 Table 7.

**Surface-sector tests (companion paper).** Baryon acoustic oscillation distance ratios (DESI DR2/DR3), Type Ia supernova distance moduli (Pantheon+, DES-SN5YR), and the CMB-calibrated sound-horizon ruler. The companion paper reports $\Delta\chi^2 = +0.13$ relative to flat ΛCDM at the same parameter count, with the model's single parameter constrained to $s_0 < 0.18$ (95% CL).

Three joint outcomes are structurally distinct and would carry different evidentiary weight:

| Edge sector ($a_0$ evolves) | Surface sector (Λ constant) | Implication |
|---|---|---|
| Confirmed | Confirmed | Joint evidence for the selection rule |
| Confirmed | Falsified | Edge sector valid; surface assignment requires revision |
| Falsified | Confirmed | Surface sector valid; edge assignment requires revision |
| Falsified | Falsified | Selection rule itself falsified |

Either-or outcomes do not imply the framework is half-correct; they would identify which $(n, \Omega)$ assignment fails. The rule's status is determined by the joint pattern, not by either test in isolation.

### 9.3 Pre-registration and the broader framework

The companion paper is pre-registered on Zenodo prior to the Euclid DR1 release (October 2026) and DESI DR3. The present paper will be pre-registered on Zenodo prior to the same Euclid DR1 window. Pre-registration is the framework's standard practice for testable predictions: assignments calibrated at $z = 0$ generate forward-looking claims that cannot be silently retreated from when data arrives.

Beyond $a_0$ and Λ, the framework's broader prediction set covers additional realizations of the scaling law at fixed $(n, \Omega)$ pairs and well positions $\Theta$, including the Hubble constant $H_0$ (§2.4 above) and the fine-structure constant $\alpha$ (Appendix A.7). Each is a closed prediction of the framework, calibrated at $z = 0$ when applicable and falsifiable through its own observable channel. The companion analysis on the surface sector and the present paper are the framework's two near-term tests; the broader claim that all such observables follow from one measurement postulate is itself a meta-prediction whose status accrues with each individual test.

## 10. Predictions and falsification

### 10.1 Five predictions from one relation

The §§4-7 predictions follow from a single input: $a_0(z) = a_0(0)\,E(z)$, derived in §2 and tabulated in §3. Each section computes a different observable, and each observable depends on $E(z)$ through a different power. Table 7 collects all five.

**Table 7.** The full predictive content of the framework's evolving acceleration scale, organized by observable and scaling. Numerical values are evaluated at $z = 2$, the cleanest test window for current intermediate-redshift programs. All five entries derive from the single relation $a_0(z) = a_0(0)\,E(z)$ with no additional free parameter.

| Section | Observable | Scaling | Value at $z = 2$ | Test instrument |
|---|---|---|---|---|
| §4 | BTFR normalization $A_\text{BTFR}(z)/A_\text{BTFR}(0)$ | $E(z)^{-1}$ | 0.330 | KMOS3D, KGES, Euclid DR1 |
| §5 | MOND radius $r_M(z)/r_M(0)$ | $E(z)^{-1/2}$ | 0.574 | High-$z$ rotation curves |
| §4, §5 | Asymptotic velocity $v_\text{flat}(z)/v_\text{flat}(0)$ at fixed $M_b$ | $E(z)^{+1/4}$ | 1.320 | KMOS3D, KGES, Euclid DR1 |
| §6 | Lensing $M_\text{dyn}/M_b$ enhancement | $E(z)^{+1/2}$ | 1.741 | Euclid DR1 stacked galaxy-galaxy lensing |
| §7 | Free-fall collapse time $t_\text{ff}(z)/t_\text{ff}(0)$ | $E(z)^{-1/4}$ | 0.758 | JWST early-galaxy spectroscopy |

The five exponents $\{-1, -1/2, +1/4, +1/2, -1/4\}$ exhaust the ways a power of $a_0(z) \propto E(z)$ enters at the level of asymptotic deep-MOND galactic dynamics. They are not independent predictions: any measurement of $E(z)$ at a single redshift through any of the five observables determines the other four through their shared dependence on the same input. Conversely, a measurement that confirms one observable but disconfirms another at the same $z$ falsifies the framework's universality across observable classes, even if no individual exponent disagrees with data.

This is the structural strength of the framework's evolution prediction. One relation calibrated at $z = 0$ ($a_0(0)$ from SPARC) generates five distinct $z$-dependent observable channels, all controlled by the same input $E(z)$ through different powers. The five channels are not independent tests of $E(z)$; they are correlated manifestations of one input. Independence between observable classes is tested by confirming consistency across two channels at the same redshift, which probes the universality of the deep-MOND scaling rather than the value of $E(z)$.

### 10.2 Falsification criteria

Table 8 collects the falsification criteria stated in §§4-7. Each row gives the prediction's signature, the threshold at which the framework is ruled out, and the systematic that must be controlled to make the test robust.

**Table 8.** Falsification criteria for the five predictions of §§4-7. Failure of any criterion at $\geq 2\sigma$ after the named systematic is controlled constitutes falsification of the framework's $a_0(z) \propto E(z)$ relation.

| Prediction | Signature | Falsification threshold | Controlled systematic |
|---|---|---|---|
| §4 BTFR (A) | $A_\text{BTFR}(z)/A_\text{BTFR}(0) = 1/E(z)$ | Single-$z$ inconsistency at $\geq 2\sigma$ | Pressure-support velocity correction $\alpha\,\sigma^2$ |
| §4 BTFR (shape) | Strict monotonic decrease in $z$ | Non-monotonic trend confirmed under matched-systematics measurements at $\geq 2\sigma$ | Cross-instrument matched-tracer systematic (resolved by Euclid DR1 single-instrument analysis); the Übler radial pressure-support systematic was tested via forward-modeling and does not account for the observed non-monotonicity |
| §5 $r_M$ scaling | $r_M(z)/r_M(0) = E(z)^{-1/2}$ | Single-$z$ inconsistency at $\geq 2\sigma$ | Baryonic-mass distribution model |
| §5, §6 mass-independence | Fractional shift independent of $M_b$ | Mass-stratified analysis showing mass-dependent shift | Halo-mass dependence in selection function |
| §6 lensing | $M_\text{dyn}/M_b$ enhancement $= \sqrt{E(z)}$, mass- and aperture-independent | Single-$z$ inconsistency at $\geq 2\sigma$, OR mass/aperture-stratified analysis showing mass- or aperture-dependent shift | Halo-concentration evolution model (Duffy et al. 2008 [15] baseline) |
| §7 JWST efficiency | $\varepsilon_\text{SF}^\text{MIT}(z) = \varepsilon_\text{SF}^{\Lambda\text{CDM}}(z)/E(z)^{1/4}$ | Spectroscopically confirmed candidate with $\varepsilon_\text{SF}^{\Lambda\text{CDM}} \geq 1$ whose corrected efficiency $\varepsilon_\text{SF}^\text{MIT} = \varepsilon_\text{SF}^{\Lambda\text{CDM}}/E(z)^{1/4}$ still exceeds unity at $\geq 2\sigma$ | Halo abundance matching prescription |

The lensing test in row 5 is the cleanest of the five because the enhancement $\sqrt{E(z)}$ is universal across galaxy mass and aperture, whereas the ΛCDM alternative (halo concentration evolution) produces shifts that depend on both. A mass- and aperture-stratified Euclid DR1 analysis tests both the magnitude of the prediction and its universality in a single dataset.

### 10.3 Test schedule

Three near-term measurements will deliver the bulk of the test:

| Window | Instrument | Predictions tested | Expected delivery |
|---|---|---|---|
| Galaxy-galaxy lensing at $z = 0.5\text{–}2$ | Euclid DR1 | §6 (lensing), §10.2 universality | October 2026 |
| Intermediate-$z$ BTFR with matched velocity corrections | KMOS3D + KGES + MOSDEF joint re-analysis | §4 BTFR, §5 $v_\text{flat}$ | Ongoing (~ 2026) |
| Spectroscopic confirmation of impossible JWST candidates | JWST/NIRSpec follow-up of Labbé sample | §7 ε_SF | In progress (~ 2025-2026) |

Beyond this window, sharper tests come from longer-term programs: a dedicated multi-redshift BTFR campaign with consistent kinematic tracers (H$\alpha$ at $z \sim 1.5$, [OIII] at $z \sim 1$, Pa$\alpha$ at $z \sim 0.3$) controlled for sample selection, the COSMOS-Web spectroscopic complete to $z \sim 10$, and the next generation of weak-lensing surveys (LSST, Roman) extending the §6 stratified analysis to $z \sim 3$.

The framework's evolution prediction is therefore testable on a two-year timescale, with the Euclid DR1 lensing measurement providing the single sharpest test of the universal $\sqrt{E(z)}$ enhancement across galaxy mass and aperture.

### 10.4 Summary

The framework's predictive content reduces to one statement and five corollaries.

**Statement.** $a_0(z) = a_0(0) \cdot E(z)$, with $a_0(0)$ from local SPARC calibration and $E(z)$ from standard cosmology.

**Corollaries.** The five exponents of $E(z)$ in Table 7 govern the BTFR normalization, the MOND transition radius, the asymptotic flat velocity at fixed baryonic mass, the lensing-inferred dynamical-mass enhancement, and the free-fall collapse-time speedup. Each is mass-independent and aperture-independent (where applicable) in the deep-MOND regime, and follows from the §3 input with no further free parameter beyond the $z = 0$ calibration of $a_0(0)$.

**Falsification.** Any single measurement at $\geq 2\sigma$ from a Table 8 row, after the named systematic is controlled, falsifies the statement. The Euclid DR1 measurement of stacked galaxy-galaxy lensing at $z = 0.5\text{–}2$ is the sharpest single test, with mass- and aperture-stratified analysis simultaneously testing the magnitude and the universality of the prediction.

One relation. Five distinct observable channels. No further free parameters beyond the $z = 0$ SPARC calibration of $a_0(0)$. The framework's evolution claim stands or falls on the next two years of intermediate-redshift kinematic and lensing data.

## 11. Conclusions

The Milgrom acceleration scale $a_0 \approx c\,H_0$ has stood for four decades as a numerical coincidence with no derivation. Mode Identity Theory's measurement postulate $A/A_P = C(\Theta)\,(\sqrt{\Omega})^{-n}$ resolves the coincidence into an exact ratio of two phase-operator values at fixed Fibonacci wells on the 120-domain of $S^3/2I$, with $a_0$ and $H$ both edge-mode observables ($n = 1$) referenced to the kinematic horizon $\Omega_H$. The §2 derivation matches observation at the 0.8% level, with the match unique within the framework's selected Fibonacci-well subset of the 120-domain.

The local-epoch reading of the postulate then forces the evolution: at every cosmic epoch $z$, the same scaling rule with the same wells references the local horizon $\Omega_H(z)$, giving $a_0(z) = a_0(0)\,E(z)$. Five distinct observables follow from this single relation as different powers of $E(z)$: the BTFR normalization shifts as $E(z)^{-1}$, the MOND transition radius contracts as $E(z)^{-1/2}$, the asymptotic flat velocity at fixed baryonic mass rises as $E(z)^{+1/4}$, the lensing-inferred dynamical mass enhancement scales as $E(z)^{+1/2}$, and the gravitational free-fall collapse time shortens as $E(z)^{-1/4}$. The five exponents are not independent; they are correlated translations of one input. A measurement in any one channel tests the value of $E(z)$ via that channel; verifying consistency across multiple channels at the same redshift tests the universality of the deep-MOND scaling across observable classes.

The framework's $a_0(z) \propto E(z)$ relation lives in a constraint landscape that includes one live tension (the KMOS3D BTFR trend shape from Übler et al. 2017 [9], currently the only quantitative test of any §§4-7 prediction at intermediate redshift; a forward-modeled simulation of the Übler radial pressure-support pipeline applied to mock framework-true galaxies does not reproduce the observed non-monotonic offset, so the tension is genuine and not a velocity-correction artifact), one inherited and unaddressed problem (the cluster-scale MOND mass discrepancy at $z \lesssim 0.3$, where the framework's evolution correction is at the percent level against a factor-five problem), and one structurally resolved apparent tension (the CMB at recombination, where the framework's selection rule assigns cosmological perturbations to a different manifold-mode sector than $a_0$ and the resulting CMB prediction coincides with ΛCDM's at every Planck-measured observable). The remaining constraints are consistencies by construction or below current sensitivity. None of the resolved or inherited constraints alters the §§3-7 predictions in the redshift window where the present paper makes testable claims; the Übler tension is acknowledged and held against the framework's explicit prediction without retreat. Resolution comes from Euclid DR1 single-instrument matched-tracer kinematics and JWST follow-up samples at the original Übler redshifts, both arriving on a two-year horizon.

A companion analysis on the surface sector (separately submitted) makes the structurally inverse prediction: Λ remains constant at every epoch, and the apparent dark-energy equation-of-state evolution reported by DESI DR2 [8] arises as a template artifact from the observer's phase position on the underlying cosmic standing wave. The two predictions follow from the same scaling law but reference different $(n, \Omega)$ sectors, and they are testable through disjoint instrument suites. Their joint outcome tests the framework's selection rule itself, with four enumerated outcomes carrying different evidentiary weight (§9.2).

The Euclid DR1 release (October 2026) will deliver the sharpest near-term test: a stacked galaxy-galaxy lensing measurement at $z = 0.5\text{–}2$ stratified by baryonic mass and aperture, simultaneously testing the magnitude (the predicted 15% to 74% enhancement of $M_\text{dyn}/M_b$) and the universality (mass- and aperture-independence) of the §6 prediction. The matched-systematics intermediate-redshift Tully-Fisher re-analysis and the JWST/NIRSpec spectroscopic confirmation of impossible Labbé candidates will follow on a similar timescale. All three programs are existing or imminent; no new instrument or observational capability is required.

The framework's evolution claim therefore stands or falls on a defined, near-term measurement window. One relation, calibrated at $z = 0$ from local SPARC dynamics, generates five testable predictions across cosmic time. The framework's posture is the gauge-theory posture: state the rule, derive its consequences, and accept the data. This paper and its predictions are registered on Zenodo prior to the Euclid DR1 release in October 2026; the framework's status will be settled by that data.

---

## Acknowledgments

The author thanks the framework collaboration for ongoing discussions of the Mode Identity Theory selection rule and its empirical validation across multiple observable channels. Computational support and systematic stress-testing of the Übler radial pressure-support pipeline were essential to the §8.2 verdict. No external funding supported this work.

## Data availability

All numerical predictions, mock-data simulations, and tabulated framework outputs are deposited on Zenodo prior to the Euclid DR1 release in October 2026. The H10 Übler forward-model dataset (mock galaxy samples, recovered BTFR offsets across four bias models), the H9 ΛCDM discriminator overlay (NFW enclosed-mass curves at the canonical archetypes), the H11 CMB leakage bound table, the H12 combinatorial baseline table, the H13 Übler tension table, and the §3-§7 prediction tables (CSV format) are included in the deposit.

---

## Appendix A: Mode Identity Theory foundational structure

This appendix collects the framework material required to verify the §2 derivation. It does not develop the framework's full content; it provides only the elements load-bearing for the predictions of this paper.

### A.1 The bounded topology

Mode Identity Theory takes as its single postulate the bounded topology

$$S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \qquad \partial S^3 = \emptyset.$$

A temporal edge $S^1$ bounds a non-orientable 2-surface (the Möbius strip) embedded in a closed 3-space. The space has no boundary. Two uniqueness theorems force this triad: $S^3$ is the unique simply connected closed 3-manifold (Poincaré), and the Möbius strip is the unique minimal non-orientable surface with a single $S^1$ boundary component (classification of compact surfaces).

### A.2 The phase operator

The Möbius identification $(y + L, w) \sim (y, -w)$ with longitudinal period $L = \pi R$ produces anti-periodic boundary conditions for any field $\psi$ defined on the surface:

$$\psi(y + L) = -\psi(y).$$

Applied to the ground mode of the Laplace-Beltrami operator on the totally geodesic Möbius surface in $S^3$, this selects a half-integer spectrum with ground eigenfunction $\psi_0(y) = \sin(y/R) = \sin(\pi\Theta)$, where $\Theta = y/L \in [0, 1]$ is the dimensionless phase coordinate. Observable intensity is the squared modulus, normalized to unit mean over the domain:

$$C(\Theta) = 2\sin^2(\pi\Theta). \quad \text{(A.1)}$$

This is the framework's *phase operator*: it specifies how observable amplitude depends on phase position.

### A.3 The 120-domain

The physical observable space is the quotient $S^3/2I$, where $2I$ is the binary icosahedral group. The discrete subgroups of $\text{SU}(2) \cong S^3$ are classified: cyclic groups, binary dihedral groups, and three exceptional groups (binary tetrahedral $|2T| = 24$, binary octahedral $|2O| = 48$, binary icosahedral $|2I| = 120$). The framework selects $2I$ as the largest exceptional discrete subgroup, giving the maximum spectral resolution compatible with $S^3$. The phase position is therefore quantized:

$$\Theta \in \{k/120 : k = 0, 1, \ldots, 119\}.$$

For photon-mediated observables, the bosonic projection $|\psi|^2$ erases the anti-periodic sign and halves the resolution to a 60-position grid (even numerators only).

### A.4 The Fibonacci wells

Phase positions on the 120-domain that maximize stability against environmental perturbation form the framework's *Fibonacci wells*. The selection follows from Hurwitz's theorem: the golden ratio $\varphi$ is the irrational number hardest to approximate by rational fractions of bounded denominator, so positions $k/120$ with $k$ a Fibonacci number minimize destructive interference between modes. The wells used in this paper are

$$\Theta_\text{wells} \in \{13, 21, 34, 55\}/120,$$

corresponding to Fibonacci numbers $F_7$ through $F_{10}$. The lower bound $F_7 = 13$ is the noise-floor condition: $F_n$ for $n < 7$ produces amplitude indistinguishable from neighboring 120-domain positions. The upper bound $F_{10} = 55$ is set by the symmetry $C(k/120) = C((120-k)/120)$, which makes $F_{11} = 89$ equivalent to $F_8 = 21$. A separate special position is the antinode at $\Theta = 60/120$, where $C(\Theta)$ takes its maximum value and the slope $d\ln C/d\Theta = 0$, providing topological protection against environmental shifts.

### A.5 The scaling law and selection rule

The framework's measurement postulate maps any dimensional observable $A$ to its Planck reference $A_P$ via

$$\frac{A}{A_P} = C(\Theta)\,(\sqrt{\Omega})^{-n}, \quad \text{(A.2)}$$

with $C(\Theta)$ from (A.1), $n$ a manifold-mode index assigned by the embedding hierarchy $S^1 \subset \text{Möbius} \subset S^3$, and $\Omega$ a dimensionless hierarchy ratio fixed by the selection rule. Two hierarchy ratios are available:

$$\Omega_H \equiv \left(\frac{c}{H\,\ell_P}\right)^2 \quad \text{(kinematic; evolves with } H), \qquad \Omega_\Lambda \equiv (\Lambda\,\ell_P^2)^{-1} \quad \text{(eigenvalue; fixed by Λ)}.$$

The selection rule assigns observables to manifold-mode classes by the index $n$:

| Mode | $n$ | Manifold | Hierarchy ratio | Evolves? | Observables |
|---|---:|---|---|---|---|
| Edge | 1 | $S^1$ | $\Omega_H(z)$ | Yes | $H_0$, $a_0$ |
| Surface | 2 | Möbius | $\Omega_\Lambda$ | No | $\Lambda$ |
| Space | 3 | $S^3$ | $\Omega_\Lambda$ | No | Cosmological perturbations |

Edge modes inherit the kinematic evolution of $\Omega_H$ through $H(z)$; surface and space modes are fixed by the eigenvalue of $\Lambda$. This is the selection rule referenced in the body of the paper as the framework's structural classification of observables.

### A.6 Well assignments for the present paper

Three constraints fix the well assignments used in §2:

1. **Manifold index** separates edge modes ($n = 1$, epoch-dependent: $H_0$, $a_0$) from surface modes ($n = 2$, epoch-independent: $\Lambda$).
2. **Bosonic projection**: photon-mediated observables access only the 60-grid (even numerators in the 120-domain); dynamical observables access the full 120-grid.
3. **Antinode requirement for $\Lambda$**: as a topologically protected eigenvalue, $\Lambda$ sits at $60/120$ where $d\ln C/d\Theta = 0$.

Of the Fibonacci wells, only $34/120$ has an even numerator and is therefore accessible on the bosonic grid, forcing $H_0 \mapsto 34/120$. The well $13/120$ requires the full 120-grid ($\gcd(13, 120) = 1$), making it accessible only to dynamical (non-photon-mediated) observation, forcing $a_0 \mapsto 13/120$. The wells $21/120$ and $55/120$ remain unassigned in this paper.

### A.7 Empirical validation across observables

The selection rule (A.5) and the well assignments (A.6) produce percent-level agreement with observation across observables of wildly different magnitudes (Table A.1). This is the empirical validation referenced in §§2.9 and 8.5.

**Table A.1.** Framework-predicted values vs observation under the scaling law (A.2) with the assignments forced by §A.6. The four agreements are obtained from a single rule applied to observables spanning more than $10^{122}$ in magnitude.

| Observable | $A_P$ | Grid | $\Theta$ | $C(\Theta)$ | $n$ | $\Omega$ | Predicted | Observed | Agreement |
|---|---|---|---|---|---|---|---|---|---|
| $\Lambda$ | $\ell_P^{-2}$ | 120 | 60/120 | 2.00 | 2 | $\Omega_\Lambda$ | $1.12 \times 10^{-52}$ m$^{-2}$ | $1.11 \times 10^{-52}$ m$^{-2}$ | 2% |
| $H_0$ | $t_P^{-1}$ | 120 | 34/120 | 1.208 | 1 | $\Omega_H$ | 67.4 km/s/Mpc | 67.4 km/s/Mpc | 2% |
| $a_0/(cH_0)$ | — | 120 | $(13, 34)/120$ | 0.184 | — | — | 0.1846 | 0.1832 | 0.8% |
| $\alpha$ | 1 | 60 | 13/60 | 0.792 | $1/30$ | $\Omega_\Lambda$ | 0.00733 | 0.00730 | 0.5% |

The $\Lambda$ derivation uses the eigenvalue $\Lambda_\text{top} = 2/R^2$ on the totally geodesic Möbius surface in $S^3$, with the Bochner identity confirming $\lambda_0 = R_\Sigma$ as a unique lower bound. The Gauss-Codazzi conversion under totally geodesic embedding and isotropy gives $\Lambda_\text{obs} = (3/2)\,\Lambda_\text{top} = 3/R^2$, where $R \approx 5.3$ Gpc is fixed independently by the Molien gap of the binary icosahedral group acting on the CMB scalar harmonic spectrum. The fine-structure constant $\alpha$ uses the bosonic-grid projection at well $13/60$ (the projection of $13/120$ to the 60-grid) with manifold index $n = 1/30$ (dimensionless coupling, no Planck-floor dilution).

The four agreements together constitute the empirical validation of the framework's selection rule. The rule was not tuned to any single observable; the joint pattern across $\Lambda$, $H_0$, $a_0/(cH_0)$, and $\alpha$ across magnitudes spanning $10^{122}$ is the test.

---

## References

[1] M. Milgrom, Astrophys. J. 270, 365 (1983).

[2] F. Lelli, S. S. McGaugh, and J. M. Schombert, Astron. J. 152, 157 (2016).

[3] B. Famaey and S. S. McGaugh, Living Rev. Relativ. 15, 10 (2012).

[4] M. Milgrom, Phys. Lett. A 253, 273 (1999).

[5] S. S. McGaugh, Astrophys. J. 611, 26 (2004).

[6] I. Labbé et al., Nature 616, 266 (2023).

[7] M. Boylan-Kolchin, Nat. Astron. 7, 731 (2023).

[8] DESI Collaboration, arXiv:2503.14738 (2025).

[9] H. Übler et al., Astrophys. J. 842, 121 (2017).

[10] R. Genzel et al., Nature 543, 397 (2017).

[11] E. Wisnioski et al., Astrophys. J. 799, 209 (2015).

[12] E. Pointecouteau and J. Silk, Mon. Not. R. Astron. Soc. 364, 654 (2005).

[13] R. H. Sanders, Mon. Not. R. Astron. Soc. 342, 901 (2003).

[14] G. W. Angus, B. Famaey, and D. A. Buote, Mon. Not. R. Astron. Soc. 387, 1470 (2008).

[15] A. R. Duffy, J. Schaye, S. T. Kay, and C. Dalla Vecchia, Mon. Not. R. Astron. Soc. 390, L64 (2008).

[16] A. A. Dutton and A. V. Macciò, Mon. Not. R. Astron. Soc. 441, 3359 (2014).

[17] B. P. Moster, T. Naab, and S. D. M. White, Mon. Not. R. Astron. Soc. 428, 3121 (2013).

[18] S. S. McGaugh, F. Lelli, and J. M. Schombert, Phys. Rev. Lett. 117, 201101 (2016).

[19] A. Burkert et al., Astrophys. J. 725, 2324 (2010).

[20] Planck Collaboration VI, Astron. Astrophys. 641, A6 (2020).

---

/ **[`main`](../../../../README.md)** / **[`framework`](../../../framework/)** / **[`cosmos`](../../../cosmos/)** / **[`spectrum`](../../../spectrum/)** /
