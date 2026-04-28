/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`working`](../)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# Epoch-Dependent Acceleration Scale from Bounded Topology: Predictions for High-Redshift Galactic Dynamics

**B. Shatto**
Independent Researcher, St. Petersburg, FL, USA
bshatto.pe@gmail.com

---

## Abstract

Modified Newtonian Dynamics rests on a single dimensional parameter, $a_0 \approx 1.20 \times 10^{-10}$ m/s$^2$, whose proximity to the cosmic scale $cH_0$ has remained unexplained for four decades. Within Mode Identity Theory, a measurement-postulate framework on the bounded topology $S^1 = \partial(\text{Möbius}) \subset S^3$, individually calibrated well assignments at $z = 0$ produce the local Milgrom ratio $a_0/(cH_0)$ as an untouched consequence: the ratio of two phase-operator values at adjacent Fibonacci wells of the 120-domain, agreeing with observation at the 0.7% level. Under a local-epoch reading of the same postulate, the framework predicts an evolving acceleration scale $a_0(z) = a_0(0)\,E(z)$ with $E(z)$ the standard Friedmann dimensionless Hubble parameter. The primary Euclid DR1 test is a mass- and aperture-universal $\sqrt{E(z)}$ enhancement of the Newtonian-inferred $M_\text{dyn}/M_b$ from stacked galaxy-galaxy weak lensing, reaching 74% at $z = 2$ relative to local galaxies of the same baryonic mass and identical across the dwarf-to-giant range and from 30 to 300 kpc apertures. The ΛCDM halo-concentration alternative predicts a mass- and aperture-dependent shift in the same observable, discriminable from the framework's universal prediction in a single stratified Euclid DR1 stack at $z = 2$ on $\sim 10^5$ galaxies (October 2026). Four additional observable channels follow from the same scaling law as different powers of $E(z)$: the baryonic Tully-Fisher normalization ($E^{-1}$), the MOND transition radius ($E^{-1/2}$), the asymptotic flat velocity at fixed baryonic mass ($E^{+1/4}$), and the gravitational free-fall collapse time ($E^{-1/4}$). The five exponents are correlated manifestations of one cosmological input rather than independent predictions. Existing constraints are treated honestly, including a provisional 2.9σ trend-shape tension with the KMOS3D Tully-Fisher data.

---

## 1. Introduction

### 1.1 Three tensions, one dimensional anchor

For four decades, the empirical success of Modified Newtonian Dynamics (MOND [1]) at galactic scales has rested on a single dimensional parameter $a_0 \approx 1.20 \times 10^{-10}$ m/s$^2$. This acceleration scale, fitted to the local SPARC (Spitzer Photometry and Accurate Rotation Curves) sample with intrinsic scatter of order 0.1 dex [18,3], satisfies a striking numerical coincidence: $a_0 / (cH_0) \approx 0.18$, with the present-day Hubble rate setting the dimensional scale of the MOND threshold. Milgrom [4], McGaugh [5], and others have remarked on this connection. Within standard MOND it remains a numerical accident with no underlying derivation. Within ΛCDM it is a coincidence with no physical content, since MOND itself has no cosmological foundation in that framework.

The James Webb Space Telescope (JWST) has recently delivered a more acute tension. Imaging of the early universe at $z \sim 7\text{–}10$ has identified candidate massive galaxies with stellar masses $M_\star \gtrsim 10^{10}\,M_\odot$ assembled within the first $\sim 600$ Myr of cosmic time [6,7]. Under standard ΛCDM halo growth and star-formation efficiency assumptions, the most extreme candidates require $\varepsilon_\text{SF} \gtrsim 1$, a formal impossibility because no more than the available baryonic budget can be converted into stars. Proposed resolutions invoke modified initial conditions, top-heavy early IMFs, or non-standard early-universe physics, none yet supported by independent evidence.

A third tension comes from intermediate-redshift dark-energy probes. The Dark Energy Spectroscopic Instrument (DESI) DR2 release [8] reports a $\sim 4\sigma$ preference for an evolving dark-energy equation of state $w(z)$ over the constant $w = -1$ assumed by ΛCDM. Phantom-crossing fits to the data require exotic field content; the cosmological constant remains viable only if the apparent evolution can be attributed to systematic effects or template artifacts.

These three tensions, the local Milgrom coincidence, the high-redshift early-galaxy crisis, and the intermediate-redshift dark-energy evolution, are loosely connected by sharing the cosmic acceleration scale $\sim c H_0$ as their common dimensional anchor. None is individually fatal to ΛCDM. None has a satisfactory resolution within either MOND or ΛCDM as conventionally formulated. The hypothesis explored in this paper is that they share an underlying topological origin.

### 1.2 The framework

Mode Identity Theory (MIT; the framework's foundational structure is summarized in Appendix A) is a measurement-postulate framework on the bounded topology $S^1 = \partial(\text{Möbius}) \subset S^3$ with anti-periodic boundary conditions. The framework's central postulate is the scaling law

$$\frac{A}{A_P} = C(\Theta) \cdot N^n, \quad \text{(1.1)}$$

mapping a Planck-normalized observable $A/A_P$ to a phase position $\Theta \in \{k/120 : k = 0, \ldots, 119\}$ on the 120-domain native to $S^3/2I$, a manifold-mode index $n$ assigned by the embedding hierarchy $S^1 \subset \text{Möbius} \subset S^3$, and a dimensionless hierarchy normalization $N \equiv (\sqrt{\Omega})^{-1}$ fixed empirically by calibrating one observable per manifold-mode class (§2.3). The phase operator $C(\Theta) = 2\sin^2(\pi\Theta)$ is the squared modulus of the anti-periodic ground mode on the Möbius surface, derived in §2.1.

Two specific assignments are the subject of this paper and its companion. The MOND scale $a_0$ is identified as an edge-mode observable ($n = 1$) referenced to the kinematic horizon ratio $\Omega_H \approx (c/(H\,\ell_P))^2$, with phase position $\Theta = 13/120$. The cosmological constant Λ is identified as a surface-mode observable ($n = 2$) referenced to the eigenvalue ratio $\Omega_\Lambda$, with phase position $\Theta = 60/120$. The Hubble rate $H$ is itself an edge-mode observable at $\Theta = 34/120$. Both the $(a_0, H_0)$ wells and the Λ position are calibrated against local measurements at percent-level precision, and their forward-looking implications for cosmic evolution are structurally inverse: the framework predicts that $a_0$ evolves with $H(z)$ while Λ remains constant, the inverse of the standard ΛCDM presumption where Λ is the candidate evolving quantity (DESI's $w(z)$) and $a_0$ is assumed universal.

### 1.3 What this paper does

The present paper makes the edge-sector prediction concrete and testable.

The §2 derivation reduces the local Milgrom coincidence to a structural ratio of two phase-operator values at fixed Fibonacci wells: $a_0/(cH_0) = C(13/120)/C(34/120) = 0.1846$, agreeing with the observed value of 0.1832 at the 0.8% level, and with the match unique within the framework's Fibonacci-well subset (one of ten possible well-pairs). The wells were assigned individually to reproduce the absolute values of $a_0$ and $H_0$ at $z = 0$, two parameters fitting two measurements; their ratio was never tuned to the Milgrom coincidence and emerges as a consequence of the well structure. The same derivation, under a local-epoch reading of (1.1), predicts an epoch-dependent evolution

$$a_0(z) = a_0(0)\,E(z), \quad \text{(1.2)}$$

with $E(z) \equiv H(z)/H_0$ the standard Friedmann dimensionless Hubble parameter. This evolution is the one input that drives §§3-6.

§3 tabulates $a_0(z)$ across the redshift range $z = 0$ to $15$. §4 derives the implication for the baryonic Tully-Fisher relation: a redshift-dependent normalization shift $A_\text{BTFR}(z)/A_\text{BTFR}(0) = 1/E(z)$, with the MOND interpolating-function dependence cancelling out of the ratio. §5 extends to galactic rotation-curve structure: the MOND transition radius contracts as $E(z)^{-1/2}$ and the asymptotic flat velocity rises as $E(z)^{+1/4}$, both mass-independent. §6 frames the lensing prediction as a Newtonian-inversion proxy: the inferred dynamical-mass-to-baryonic-mass ratio under the standard inversion convention is enhanced by $\sqrt{E(z)}$ at fixed aperture and baryonic mass, universally across the deep-MOND regime, sidestepping the need to commit to a specific relativistic completion of MOND. §7.7 applies the corresponding $E(z)^{1/4}$ collapse-time speedup to the JWST early-galaxy tension, reducing the required star-formation efficiency by a uniform factor of $\sim 2$ across the Labbé sample. Whether this resolves the impossibility constraint for any specific candidate depends on halo-mass priors and is reserved for future per-object analysis.

§7 treats the existing constraint landscape honestly: a live tension with the KMOS3D BTFR trend shape (§7.2), the inherited cluster-scale MOND mass discrepancy at $z \lesssim 0.3$ (§7.4), the structurally resolved CMB consistency under the framework's selection rule (§7.5), the JWST early-galaxy collapse-time speedup as supporting evidence (§7.7), and below-sensitivity status elsewhere. The framework's monotonic BTFR prediction is in tension with current intermediate-redshift kinematic data [9]; the comparison, including a forward-modeled simulation of the radial pressure-support systematic, is treated in §7.2. §8 connects to a companion analysis (separately submitted) developing the surface-sector prediction. §9 collects the full predictive content into a single table and identifies the falsification windows. §10 closes.

The §§4-6 and §7.7 predictions are not independent: they all derive from (1.2) and depend on $E(z)$ through different powers ($-1$, $-1/2$, $+1/4$, $+1/2$ across §§4-6; $-1/4$ in §7.7). A measurement in any one channel tests $E(z)$ via that channel; verifying consistency across multiple channels at the same redshift tests the universality of the deep-MOND scaling across observable classes. The Euclid DR1 release [31] in October 2026 will deliver the sharpest such test in the form of stacked galaxy-galaxy weak lensing at $z = 0.5\text{–}2$ stratified by baryonic mass and aperture.

### 1.4 Novelty relative to prior literature

The evolving form $a_0(z) \propto H(z)$ has been speculated in the MOND literature as a possible interpretation of the local $a_0 \approx cH_0$ coincidence; Milgrom (1999) [4] explored this in a vacuum-effect framework, additional cosmological consequences of varying $a_0$ are discussed in Zhao & Famaey (2012) [30], and the broader MOND landscape is surveyed in the Milgrom (2014) Scholarpedia review [29]. The present paper's contribution is not the bare proportionality but three specific results that follow from it.

First, the relation is *derived within the framework* from the scaling-law postulate (§2) as a structural cancellation between two specific Fibonacci-well positions $C(13/120)$ and $C(34/120)$ on the 120-domain of $S^3/2I$, with the local Milgrom ratio recovered at the 0.8% level. The match is sparse on the full 120-domain (24 of 7,021 nonzero pairs match within 1%) and unique within the framework's Fibonacci-well subset (one of ten possible well-pairs). The derivation identifies the topological mechanism by which the proportionality arises and yields a single specific functional form (linear in $E(z)$) rather than admitting a family of speculative possibilities.

Second, the same derivation generates a *coupled five-exponent prediction set* across cosmic time (§§4-6 plus §7.7), with all five observables (BTFR normalization, MOND transition radius, asymptotic flat velocity, lensing $M_\text{dyn}/M_b$ enhancement, free-fall collapse time) governed by the same $a_0(z) \propto E(z)$ input through different powers of $E(z) \in \{-1, -1/2, +1/4, +1/2, -1/4\}$. The five predictions are not independent and cannot be tuned separately; any measurement of one tests all five through their shared cosmological dependence.

Third, the prediction set is subjected to *explicit constraint analysis* against existing data (§7), including a forward-model treatment of the Übler 2017 KMOS3D pressure-support pipeline that demonstrates the framework's monotonic BTFR prediction is in genuine tension with the only existing high-$z$ test, and that the tension cannot be dissolved by literature-plausible velocity-correction systematics. The §6 lensing prediction is also made at the level of the Newtonian-inferred dynamical mass, sidestepping the need to commit to a specific relativistic completion of MOND.

The framework's broader prediction set, including the surface-sector Λ prediction developed in a companion analysis on the same scaling-law postulate, is a meta-result whose status accrues across individual tests; the §8.2 joint-outcome table identifies four enumerated outcomes that the joint pattern across both sectors can produce.

## 2. Deriving $a_0(z) \propto H(z)$ within the framework

The result $a_0(z) = a_0(0)\,E(z)$ is conditional on three framework inputs documented in Appendix A: (i) the scaling-law postulate (§2.1), (ii) the well assignments at $z = 0$ (Appendix A.3), and (iii) the local-epoch reading of the postulate's hierarchy factor, defended in §2.6 below. Within the framework these are postulates rather than first-principles derivations; their successful match to the Milgrom coincidence at the 0.8% level (§2.5) is what motivates taking them seriously in the present paper. The §2 derivation shows what follows from these inputs through algebra alone, and is in this conditional sense a derivation rather than an axiomatic theorem.

### 2.1 Setup: topology, phase operator, scaling law

Mode Identity Theory takes as its single postulate the bounded topology

$$S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \qquad \partial S^3 = \emptyset.$$

A temporal edge $S^1$ bounds a non-orientable 2-surface (the Möbius strip) embedded in a closed 3-space. The space has no boundary. Within the framework, three structural requirements motivate this choice. (i) By the Poincaré theorem, $S^3$ is the unique simply connected closed 3-manifold; it is diffeomorphic to $\text{SU}(2)$ and admits a spin structure, accommodating fermionic matter. (ii) By the classification of compact surfaces, the Möbius strip is the unique minimal non-orientable surface with a single $S^1$ boundary component, whose $\mathbb{Z}_2$ holonomy under one traversal produces the anti-periodic boundary condition selected by fermionic matter. (iii) The terminus $\partial S^3 = \emptyset$ closes the embedding hierarchy: there is no further boundary from which to observe.

The Möbius identification $(y + L, w) \sim (y, -w)$ with longitudinal period $L = \pi R$ produces anti-periodic boundary conditions for any field $\psi$ defined on the surface, $\psi(y + L) = -\psi(y)$. Applied to the ground mode of the Laplace-Beltrami operator on the totally geodesic Möbius surface in $S^3$, this selects a half-integer spectrum with ground eigenfunction $\psi_0(y) = \sin(y/R) = \sin(\pi\Theta)$, where $\Theta = y/L \in [0, 1]$ is the dimensionless phase coordinate. Observable intensity is the squared modulus, normalized to unit mean over the domain:

$$C(\Theta) = 2\sin^2(\pi\Theta).$$

This is the framework's *phase operator*: it specifies how observable amplitude depends on phase position.

The framework's measurement postulate maps any dimensional observable $A$ to its Planck reference $A_P$ via

$$\frac{A}{A_P} = C(\Theta) \cdot N^n,$$

with $C(\Theta)$ above, $\Theta \in \{k/120 : k = 0, 1, \ldots, 119\}$ a phase position on the 120-domain native to the binary-icosahedral quotient $S^3/2I$ (Appendix A.1), $n$ a manifold-mode index assigned by the embedding hierarchy $S^1 \subset \text{Möbius} \subset S^3$, and $N \equiv (\sqrt{\Omega})^{-1}$ a dimensionless hierarchy normalization fixed empirically by calibration (§2.3 below).

Two hierarchy ratios are available to a given observable:

| Symbol | Kinematic expression (leading-order) | Physical content |
|---|---|---|
| $\Omega_H$ | $(c / (H\,\ell_P))^2$ | Hubble horizon, $R_H = c/H$ |
| $\Omega_\Lambda$ | $(\Lambda\,\ell_P^2)^{-1}$ | de Sitter horizon, $R_\Lambda = \sqrt{3/\Lambda}$ |

The selection rule assigns each observable to one of these by the manifold-mode index $n$:

| Mode | $n$ | Manifold | Hierarchy normalization | Evolves? | Observables |
|---|---:|---|---|---|---|
| Edge | 1 | $S^1$ | $N_H(z)$ | Yes | $H_0$, $a_0$ |
| Surface | 2 | Möbius | $N_\Lambda$ | No | $\Lambda$ |
| Space | 3 | $S^3$ | $N_\Lambda$ | No | Cosmological perturbations |

For edge modes the relevant normalization is $N_H \equiv (\sqrt{\Omega_H})^{-1}$, with the kinematic identification $N_H \approx Ht_P$ (using $\ell_P/c = t_P$) holding at leading order. The two expressions differ by a well-position factor $C(34/120) = 1.208$: the calibration relation in §2.3 fixes $N_H$ precisely as $N_H = Ht_P/C(34/120)$, and every subsequent use of $N_H$ in this paper refers to the calibrated value, not the leading-order kinematic approximation. For surface modes the corresponding $N_\Lambda \equiv (\sqrt{\Omega_\Lambda})^{-1}$. The framework does not derive the absolute hierarchy normalization from topology; it uses an external measurement to set the scale, then predicts all other observables in the class relative to that scale, with the relative dimensionless ratios fixed by the well-position $C$ factors.

The selection rule is a postulate of the framework, with the same status as the gauge group $SU(3) \times SU(2) \times U(1)$ in the Standard Model: chosen, not derived, with consequences that are tested rather than assumed. The §2 derivation takes the rule as given and shows what follows.

### 2.2 Edge modes use $\Omega_H$

Edge modes are observables tied to the $S^1$ boundary of the Möbius band ($n = 1$ in the embedding hierarchy). The boundary $S^1$ is a kinematic locus: it carries no intrinsic surface eigenvalue (the surface eigenvalue lives one dimension up, on Möbius itself, where the framework places Λ; see §2.8 contrast). What an edge mode references is the embedding scale of $S^1$ in the ambient cosmological geometry. The natural such scale is the Hubble horizon $R_H = c/H$, and its dimensionless Planck ratio is $\Omega_H$.

Therefore, for any edge-mode observable evaluated at cosmic epoch $z$:

$$\frac{A_{\text{edge}}(z)}{A_P} = C(\Theta_A) \cdot N_H(z), \qquad N_H(z) \equiv (\sqrt{\Omega_H(z)})^{-1} \approx H(z)\,t_P \quad \text{(2.1)}$$

with the kinematic identification $\Omega_H(z) \approx (c/(H(z)\ell_P))^2$ leading-order; the precise value of $N_H(z)$ is fixed by the calibration relation introduced in §2.3. The phase position $\Theta_A$ and the manifold index ($n = 1$) are topological assignments and do not evolve. The full epoch dependence sits in $N_H(z)$.

### 2.3 Calibration through $H$, prediction for $a_0$

The well assignments calibrated at $z = 0$ under the framework's eligibility conditions (Appendix A.3) place $a_0$ at $\Theta = 13/120$ and $H$ at $\Theta = 34/120$, both edge modes ($n = 1$). The scaling law applied to each gives, at any epoch $z$:

$$\frac{a_0(z)}{a_P} = C(13/120) \cdot N_H(z) \quad \text{(2.2)}$$

$$H(z)\,t_P = C(34/120) \cdot N_H(z) \quad \text{(2.3)}$$

with $a_P = c/t_P$ and $H_P = 1/t_P$. Equations (2.2) and (2.3) play different roles in the framework's prediction structure.

Equation (2.3) is the *calibration relation*. The framework does not derive $H$ from topology; $H$ is the measured observable through which the dimensionless hierarchy normalization $N_H(z)$ is fixed empirically at every epoch:

$$N_H(z) = H(z)\,t_P / C(34/120)$$

The role of $H$ here is the role of the QCD coupling $\alpha_s$ measured at a reference process in particle physics: it is the input that sets the dimensional scale, after which all other observables in its class are predictions. The kinematic identification $N_H \approx (\sqrt{\Omega_H})^{-1} \approx H\,t_P$ is leading-order; the framework's precise $N_H$ differs from the kinematic value by the well-position factor $C(34/120) = 1.208$, absorbed into the calibration. The kinematic expression is the approximation, and the calibration relation (2.3) is the exact framework statement. The surface-mode counterpart $N_\Lambda$ is calibrated independently in the companion analysis through the cosmological curvature scale derived from CMB measurements, by the same prediction-from-calibration pattern; the two sectors do not share normalization, and the present paper's predictions depend only on $N_H$.

Equation (2.2) is the *prediction*. Given $N_H(z)$ from (2.3), the well at $\Theta = 13/120$ produces $a_0(z)$ as the framework's output for the acceleration scale at every epoch. Two facts about (2.2) and (2.3) carry the rest of the derivation:

1. The $C$ factors are pure numbers fixed by the wells: $C(13/120) = 2\sin^2(13\pi/120) = 0.2229$ and $C(34/120) = 2\sin^2(34\pi/120) = 1.2079$. They are topological invariants of the 120-domain on $S^3/2I$ and do not evolve.
2. The hierarchy normalization $N_H(z)$ is shared between (2.2) and (2.3), set by the calibration through $H$ at every epoch.

The relation $a_0(z) \propto H(z)$ follows by substituting (2.3) into (2.2).

### 2.4 The prediction

Substituting the calibration (2.3) into the prediction (2.2):

$$\frac{a_0(z)}{a_P} = C(13/120) \cdot \frac{H(z)\,t_P}{C(34/120)}$$

Using $a_P = c/t_P$:

$$\boxed{\;\frac{a_0(z)}{c\,H(z)} = \frac{C(13/120)}{C(34/120)} = 0.1845\;} \quad \text{(2.4)}$$

The right-hand side is a pure topological number, independent of $z$. The wells $13/120$ and $34/120$ were calibrated individually to fit the absolute values of $a_0(0)$ and $H_0$ at $z = 0$: two parameters fitting two measurements. Their ratio $C(13/120)/C(34/120) = 0.1845$ was not tuned separately; it is a consequence of the calibration structure, with the well-position factors fixed by the 120-domain. The relation $a_0(z) \propto H(z)$ follows immediately, with the proportionality constant set by this ratio. Equivalently:

$$a_0(z) = a_0(0)\,\frac{H(z)}{H_0} \quad \text{(2.5)}$$

This is the central result of the section. No epoch-dependent quantity other than $H(z)$ enters; no auxiliary scale is introduced; the calibration through $H(z)$ absorbs the hierarchy-normalization piece, and what remains is the pure well-position ratio. The §2.5 agreement between 0.1845 and the observed 0.1833 (0.7%) is a test of the well-assignment structure, with the matching strength quantified against the combinatorial baseline below.

### 2.5 Consistency check on absolute values at $z = 0$

The ratio (2.4) determines the evolution but says nothing about the absolute value of $a_0$ at any single epoch. The absolute values are calibration inputs: the wells $13/120$ and $34/120$ were assigned individually to fit the observed $a_0(0)$ and $H_0$ at $z = 0$. Observed inputs (Planck 2018 [20] $H_0 = 67.4$ km/s/Mpc, SPARC $a_0 = 1.20 \times 10^{-10}$ m/s$^2$):

$$\frac{a_0^{\text{obs}}}{c\,H_0^{\text{obs}}} = \frac{1.20 \times 10^{-10}}{6.548 \times 10^{-10}} = 0.1833$$

Predicted ratio from the wells: 0.1845. Agreement to 0.7%. The Milgrom coincidence $a_0 \approx c\,H_0$ resolves to a ratio of two phase-operator values at fixed wells. The ratio is the testable structural claim of the well assignments; the individual absolute values of $a_0$ and $H_0$ are the calibration inputs that fix $\Theta_{a_0} = 13/120$ and $\Theta_{H_0} = 34/120$, not independent predictions.

To calibrate the strength of this match, we compute the combinatorial baseline. Of the 7,021 unordered nonzero phase-position pairs $(k_1, k_2)/120$ with $k_1, k_2 \in \{1, \ldots, 119\}$, only 24 produce a ratio $C(k_1/120)/C(k_2/120)$ within 1% of the observed $0.1833$, a fraction of 0.342%. Modulo the reflection symmetry $C(k) = C(120-k)$, these collapse to 6 unique phase-operator value pairs. Within the framework's selected Fibonacci-well subset $\{13, 21, 34, 55, 60\}/120$, exactly one of the ten possible unordered well-pairs matches: the framework's $(13, 34)$. The match is therefore sparse on the full 120-domain (one in $\sim 300$ pairs) and unique within the topologically-selected Fibonacci-well structure (one in 10).

The absolute-value check tests the well assignments (which were calibrated to $z = 0$ measurements). The evolution prediction is independent of this calibration and follows from the structural ratio (2.4).

### 2.6 The local-epoch postulate (load-bearing step)

Equation (2.4) holds at all $z$ if and only if the edge-mode rule (2.1) uses $\Omega_H(z)$ evaluated at the local epoch, not $\Omega_H(0)$ evaluated at present and held fixed. This is the step that elevates the framework from "explains the $a_0/cH_0$ ratio at $z = 0$" to "predicts $a_0(z) \propto H(z)$ at all epochs." It deserves explicit justification.

**Argument from the measurement-postulate reading.** The scaling law is a measurement postulate: it specifies what an observer measures, given the topological structure and the hierarchy at the measurement event. Three sub-claims follow:

1. *The 120-domain is a topological invariant of $S^3/2I$.* The wells $\{13, 21, 34, 55, 60\}/120$ are fixed by the Hurwitz/Fibonacci structure on the binary icosahedral quotient. They do not evolve with cosmic epoch. Therefore $C(\Theta_A)$ in (2.1) is the same number at every $z$.

2. *The manifold index $n$ is a topological assignment.* Edge mode means $n = 1$, and "edge" refers to the embedding $S^1 \subset \text{Möbius} \subset S^3$, which is a topological feature of the framework, not a feature of cosmic evolution. Therefore $n$ in (2.1) is the same at every $z$.

3. *The hierarchy normalization $N_H$ is the only piece set by external measurement.* $N_H(z) = H(z)\,t_P / C(34/120)$ is built from the measured $H$ through the calibration relation (2.3). A measurement performed at epoch $z$ accesses the local Hubble rate $H(z)$. Therefore $N_H$ in the scaling law is $N_H(z)$, calibrated through the local $H(z)$, not $N_H(0)$.

Sub-claims 1 and 2 are forced by the topological reading of the wells and the embedding hierarchy. Sub-claim 3 is the genuine postulate. It says: the observer's hierarchy reference is calibrated through the local measurement at the observer's spacetime location, not anchored to some privileged past or future epoch.

**The alternative.** One could postulate that $N_H$ in (2.2) is permanently $N_H(0)$, so that all edge-mode observables retain their present-day values at every epoch. Under this alternative, $a_0$ is constant. But this alternative *is* itself the addition of a postulate: it requires a privileged "present" epoch to which the calibration is anchored, breaking time-translation symmetry within the bounded cosmic domain. The bounded domain offers no structural support for such a slice. The "local-epoch reading" is therefore not a separate postulate added to the framework: it is the refusal to add one. The scaling law evaluated at face value, with $N_H$ calibrated through the local $H(z)$, gives the local reading by default; freezing $N_H(0)$ is what would require the addition.

### 2.7 Generalization: any two edge-mode observables

The structural ratio (2.4) is not specific to $(a_0, H)$. For any pair of edge-mode observables $A$ and $B$ at the same epoch:

$$\frac{A(z)/A_P^{(A)}}{B(z)/A_P^{(B)}} = \frac{C(\Theta_A) \cdot N_H(z)}{C(\Theta_B) \cdot N_H(z)} = \frac{C(\Theta_A)}{C(\Theta_B)} \quad \text{(2.6)}$$

The shared $N_H(z)$ divides out whenever both observables are edge modes referencing the same hierarchy through the same calibration. This is the structural reason the framework predicts proportional evolution among all edge-mode kinematic quantities, not just $a_0$ and $H$. Any further edge-mode acceleration scale, frequency, or velocity would track $H(z)$ identically, with its present-epoch ratio to $cH_0$ set by its own well position. The pair $(a_0, H)$ is the cleanest application because both are independently measured to ~1% precision and the corresponding wells $(13, 34)/120$ are adjacent Fibonacci stability points.

### 2.8 Why Λ does not evolve (contrast)

The same scaling-law machinery places Λ at well $60/120$ with $n = 2$ (surface mode) and $\Omega = \Omega_\Lambda$ (§2.1):

$$\frac{\Lambda}{\ell_P^{-2}} = C(60/120) \cdot N_\Lambda^2 = 2 \cdot \Omega_\Lambda^{-1}$$

Two structural differences from $a_0$:

1. *Manifold index* $n = 2$ (surface), not $n = 1$ (edge). Λ is the eigenvalue of the Laplace-Beltrami operator on the Möbius surface; the embedding is via Gauss-Codazzi to the spatial slice. This is intrinsic surface geometry, not boundary kinematics.

2. *Hierarchy reference* is $\Omega_\Lambda$, not $\Omega_H$. $\Omega_\Lambda$ is set by Λ itself: it is the de Sitter horizon ratio, fixed by the surface-mode eigenvalue and the curvature radius $R$ of $S^3$. The selection rule places surface-mode observables in this class, structurally distinct from the kinematic edge sector that produces $a_0$ and $H$.

Under the local-epoch reading, $\Omega_\Lambda$ is the same at every $z$ (it is a topological-eigenvalue ratio, not a kinematic ratio). Therefore Λ is constant. The phase position $\Theta = 60/120$ is the antinode of $C(\Theta)$, where $d\ln C/d\Theta = 0$ (Appendix A.2), giving topological protection against environmental perturbations as well.

The two predictions are therefore *structurally inverse*: $a_0$ evolves because it references the kinematic horizon $\Omega_H$; Λ does not evolve because it references the surface-eigenvalue $\Omega_\Lambda$. This inversion is not a tuning. It follows from the selection rule on $(n, \Omega)$ pairs.

### 2.9 Status of the argument

Honest accounting of what is derived vs imported in §2:

| Element | Status | Source |
|---|---|---|
| Scaling law $A/A_P = C(\Theta) \cdot N^n$ with $N \equiv (\sqrt{\Omega})^{-1}$ | Postulate | §2.1 |
| $C(\Theta) = 2\sin^2(\pi\Theta)$ | Derived | Anti-periodic ground mode on Möbius (§2.1) |
| Edge-mode $\Leftrightarrow$ $N_H$ | Postulate (selection rule) | §2.1 |
| Surface-mode $\Leftrightarrow$ $N_\Lambda$ | Postulate (selection rule) | §2.1 |
| Well assignment $\Theta_{a_0} = 13/120$ | Empirical at $z = 0$ | Appendix A.3 |
| Well assignment $\Theta_{H_0} = 34/120$ | Empirical at $z = 0$ | Appendix A.3 |
| Local-epoch reading of $N_H$ | Default reading of the calibration relation; §2.6 shows freezing $N_H(0)$ would itself add a postulate | This section |
| Calibration (2.3): $H\,t_P = C(34/120) \cdot N_H$ | Calibration (defines $N_H$ through measured $H$) | This section |
| Prediction (2.2): $a_0/a_P = C(13/120) \cdot N_H$ | Derived (scaling law applied to the $a_0$ well) | This section |
| Substitution (2.4) | Derived | Algebra of (2.2) with (2.3) substituted |
| $a_0(z) = a_0(0)\,H(z)/H_0$ | Derived, given the above | This section |

Given the framework's postulates, the wells calibrated at $z = 0$, and the local-epoch reading, the evolution $a_0(z) \propto H(z)$ follows from the prediction-from-calibration structure of §2.3-§2.4. No additional free parameter is introduced for the evolution; it is fully determined by the well-position factors and the calibration through measured $H(z)$. The well assignments themselves (13/120 for $a_0$, 34/120 for $H$) are not derived in this paper; they are inputs calibrated to $z = 0$ measurements. A future well-positioning analysis would attempt to derive these from the Hurwitz/Fibonacci structure of the 120-domain. Until then, the well assignments have the same status as fitting two parameters to two measurements at $z = 0$; the predictive content of the present paper is everything that follows at $z > 0$.

Two framework-level open questions bear on the §2 argument:

1. *The selection rule.* The scale-selection rule assigns edge-mode observables ($n = 1$) to the kinematic hierarchy $\Omega_H$ and surface-mode observables ($n = 2$) to the eigenvalue hierarchy $\Omega_\Lambda$. This assignment is a postulate, not derived from the topology. Its empirical support within the present paper is the §2.4 ratio that recovers the Milgrom coincidence at 0.8% and locates the framework's $a_0$ uniquely among the Fibonacci wells. A uniqueness result for the $(n, \Omega)$ pairing is future work.

2. *The local-epoch reading.* §2.6 defends this from symmetry: freezing $N_H$ at $N_H(0)$ would require a privileged present epoch, which the bounded domain does not support. Whether the absence of a preferred epoch is sufficient to force the local reading is a structural argument, not a theorem.

Both are shared with the broader framework; neither is unique to this paper, and neither affects the algebra of §2.4.

## 3. H(z) and $a_0(z)$ across cosmic time

The §2 derivation reduces the epoch dependence of $a_0$ to the epoch dependence of $H$:

$$a_0(z) = a_0(0)\,\frac{H(z)}{H_0} = a_0(0)\,E(z) \quad \text{(3.1)}$$

with $E(z) \equiv H(z)/H_0$. The framework introduces no new parameter for the evolution; the only input is the cosmological expansion history. $H(z)$ is imported from standard cosmology rather than predicted by the scaling law: the framework's edge-mode assignment of $H$ (Appendix A.3) classifies $H$ within its observable hierarchy, and the predictive content of (3.1) is the structural ratio $a_0(z)/H(z) = a_0(0)/H_0$ that holds for any $H(z)$ history. The §2.4 substitution of the calibration (2.3) into the prediction (2.2) eliminates the hierarchy normalization $N_H(z)$ from the ratio regardless of how $H(z)$ is parameterized. We adopt the flat ΛCDM Friedmann form,

$$E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_\Lambda}, \quad \text{(3.2)}$$

with Planck 2018 parameters [20] $\Omega_m = 0.315$, $\Omega_r = 9.2 \times 10^{-5}$, $\Omega_\Lambda = 0.685$, and $H_0 = 67.4$ km/s/Mpc. The age of the universe at redshift $z$ follows from

$$t_\text{age}(z) = \int_z^\infty \frac{dz'}{(1+z')\,H(z')}. \quad \text{(3.3)}$$

Equations (3.1)-(3.3) determine $a_0(z)$ at every epoch with no remaining freedom.

### 3.1 Table of values

Table 1 lists $E(z)$, $H(z)$, $a_0(z)$, the deep-MOND enhancement factor $\sqrt{a_0(z)/a_0(0)} = \sqrt{E(z)}$, and $t_\text{age}(z)$ at eight reference redshifts spanning the SPARC sample, the intermediate-$z$ rotation-curve regime, the BAO range, and the JWST early-galaxy window. The enhancement factor governs effective gravity, lensing-inferred dynamical mass, and free-fall collapse rates in the deep-MOND limit; it recurs throughout §§5-6 and is anchored here.

**Table 1.** Evolution of the Hubble rate, MOND acceleration scale, deep-MOND enhancement factor, and cosmic age across the redshift range relevant to §§4-6 and §7.7.

| $z$ | $E(z)$ | $H(z)$ [km/s/Mpc] | $a_0(z)$ [m/s²] | $a_0(z)/a_0(0)$ | $\sqrt{a_0(z)/a_0(0)}$ | $t_\text{age}$ [Gyr] |
|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 1.0000 | 67.40 | $1.20 \times 10^{-10}$ | 1.000 | 1.000 | 13.79 |
| 0.5 | 1.3223 | 89.13 | $1.59 \times 10^{-10}$ | 1.322 | 1.150 | 8.58 |
| 1.0 | 1.7907 | 120.69 | $2.15 \times 10^{-10}$ | 1.791 | 1.338 | 5.84 |
| 2.0 | 3.0327 | 204.41 | $3.64 \times 10^{-10}$ | 3.033 | 1.741 | 3.27 |
| 3.0 | 4.5682 | 307.90 | $5.48 \times 10^{-10}$ | 4.568 | 2.137 | 2.14 |
| 5.0 | 8.2972 | 559.23 | $9.96 \times 10^{-10}$ | 8.297 | 2.880 | 1.17 |
| 10.0 | 20.5255 | 1383.42 | $2.46 \times 10^{-9}$ | 20.525 | 4.530 | 0.470 |
| 15.0 | 36.0133 | 2427.29 | $4.32 \times 10^{-9}$ | 36.012 | 6.001 | 0.268 |

Two values fix the magnitude of the prediction. At $z = 2$, $a_0$ is $3.03$ times its local value with deep-MOND enhancement $1.74$; this is the cleanest window for direct rotation-curve and Tully-Fisher tests (§§4-5) and yields a 74% excess in lensing-inferred $M_\text{dyn}/M_b$ over local galaxies of the same baryonic mass (§6). At $z = 10$, $a_0$ reaches $20.5$ times its local value with deep-MOND enhancement $4.53$; this is the regime probed by JWST imaging of the earliest assembled stellar populations (§7.7), where the corresponding $E(z)^{1/4} \approx 2.13$ collapse-time speedup reduces the required star-formation efficiency for the impossibly-early candidates by approximately a factor of two, with the per-candidate verdict deferred to future analysis (§7.7). The $a_0(z) = c H(z)$ heuristic implicit in the local Milgrom coincidence becomes a precise epoch-dependent statement rather than a numerical accident.

### 3.2 Figure 1: $a_0(z)/a_0(0)$ across cosmic time

**Figure 1.** $a_0(z)/a_0(0)$ from $z = 0$ to $z = 15$ under the framework prediction (3.1) with the standard flat ΛCDM expansion history (3.2) and Planck 2018 parameters [20]. The curve is the dimensionless Hubble parameter $E(z)$. Inflection from radiation-mediated to matter-dominated growth occurs near $z \sim 3000$ and is irrelevant to the redshift window probed by §§4-6. Log-uniform vertical axis recommended.

The shape of the curve in the regime $z = 0$ to $5$ is dominated by the matter term in (3.2); $E(z) \propto (1+z)^{3/2}$ to leading order. Above $z \sim 100$ radiation matters; this is far above the redshifts where the §§4-6 predictions live, and the parameterization in (3.2) is self-consistent throughout.

### 3.3 Cosmology dependence

We adopt the standard flat ΛCDM expansion history (3.2) with Planck 2018 [20] parameters throughout this paper. The §§4-6 predictions are robust to reasonable variations in the cosmological parameters within their current observational uncertainties: at $z > 1$ the matter term in (3.2) dominates the energy budget and the fractional sensitivity of $E(z)$ to $\Omega_m$ within current Planck and DESI constraints stays at the percent level; at $z < 1$ the late-time energy budget enters but the corresponding shifts in the §§4-6 observables remain well within current measurement uncertainties at intermediate redshift.

The prediction of an evolving $a_0$ is independent of which Friedmann form is chosen for $H(z)$. The substitution in §2.4 absorbs the hierarchy normalization $N_H(z)$ into the calibration regardless of how $H(z)$ is parameterized: $a_0(z) \propto H(z)$ holds for any expansion history. Adopting the standard ΛCDM form is therefore a transparency choice that allows direct comparison with published high-$z$ measurements typically reported under the same cosmology, not a load-bearing assumption of the framework's evolution prediction.

### 3.4 What §3 establishes

Equation (3.1), Table 1, and Figure 1 together fix the inputs that the rest of the paper consumes. Each downstream section takes $a_0(z)$ from this section and evaluates a specific observable: the BTFR normalization (§4), galactic rotation curves (§5), galaxy-galaxy lensing (§6), and JWST star-formation efficiencies (§7.7). All four inherit the same epoch dependence from this section; none of them introduces new free parameters. The §§4-6 and §7.7 results are therefore predictions of a single one-parameter relation, calibrated by the local value $a_0(0) = 1.20 \times 10^{-10}$ m/s$^2$ from SPARC.

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

Table 2 evaluates (4.3)-(4.5) at six reference redshifts. The fractional shifts apply universally across the BTFR's full mass range in the deep-MOND limit; they do not depend on $M_b$ for galaxies whose outer dynamics sit in that limit. Galaxies that sit in the intermediate MOND regime ($g_N \sim a_0$) at $z = 0$ may shift further from the deep-MOND limit at higher $z$, requiring the full interpolating function for precise predictions (§4.4).

**Table 2.** BTFR normalization, baryonic-mass shift at fixed velocity, and velocity shift at fixed baryonic mass under the framework prediction (4.3)-(4.5). The local theoretical BTFR normalization is $A_\text{BTFR}(0) = 1/(G\,a_0(0)) = 62.78$ $M_\odot/(\text{km/s})^4$ in the deep-MOND limit; see §4.4 for the relation to the SPARC empirical value.

| $z$ | $E(z)$ | $A_\text{BTFR}(z)\,[M_\odot/(\text{km/s})^4]$ | $A(z)/A(0)$ | $M_b/M_b(0)$ at fixed $v_\text{flat}$ | $v_\text{flat}/v_\text{flat}(0)$ at fixed $M_b$ |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 1.0000 | 62.78 | 1.0000 | 1.000 | 1.000 |
| 0.5 | 1.3223 | 47.48 | 0.7563 | 0.756 | 1.072 |
| 1.0 | 1.7907 | 35.06 | 0.5585 | 0.558 | 1.157 |
| 2.0 | 3.0327 | 20.70 | 0.3298 | 0.330 | 1.320 |
| 5.0 | 8.2972 | 7.57 | 0.1205 | 0.121 | 1.697 |
| 10.0 | 20.5255 | 3.06 | 0.0487 | 0.049 | 2.128 |

Two values anchor the predictive content. At $z = 2$, the BTFR normalization is one-third of its local value; equivalently, a galaxy at $z = 2$ with the same baryonic mass as a local one rotates 32% faster, and a galaxy at $z = 2$ with the same rotation velocity has one-third the baryonic mass. At $z = 1$, the corresponding numbers are 56% normalization, 16% velocity shift, 44% mass deficit. These are the regimes accessible to current and near-term integral-field spectroscopy of intermediate-redshift disks. As a worked example consistent with the §5.2 archetype table, an $L^*$ disk on the deep-MOND BTFR ($M_b = 6 \times 10^{10}\,M_\odot$, $v_\text{flat}(0) = 176$ km/s under the theoretical normalization $A_\text{BTFR}(0) = 62.78\,M_\odot/(\text{km/s})^4$) is predicted by (4.4) to have $v_\text{flat}(2) \approx 232$ km/s at $z = 2$, a 32% increase at fixed baryonic mass.

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

The first criterion is testable today with stacked KMOS3D, MOSDEF [32], and KGES [33] samples and will be sharpened by the Euclid DR1 galaxy catalog (October 2026). The second criterion requires kinematic measurements at a minimum of three redshift bins under matched velocity-correction prescriptions, a sample currently in assembly (see §7).

Existing intermediate-redshift BTFR measurements [9] test the §4 normalization prediction directly; the comparison, the framework's current status against the observed non-monotonic trend, and the next-generation tests that will resolve the constraint are treated in §7.

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

**Table 3.** Predicted MOND transition radius and asymptotic flat velocity at $z = 0$ and $z = 2$ for four baryonic-mass archetypes. The shifts $r_M(z=2)/r_M(0) = 0.574$ and $v_\text{flat}(z=2)/v_\text{flat}(0) = 1.320$ are mass-independent in the deep-MOND limit and apply identically across the table; real-sample applications inherit the §4.4 caveat for galaxies in the intermediate MOND regime. Galaxy archetypes are chosen with rounded baryonic masses $M_b$ and disk scale lengths $R_d$ matched to representative SPARC objects (DDO 154, NGC 2403, NGC 6946, UGC 2885).

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

1. The asymptotic plateau prediction (5.3) at any single redshift, equivalent to (4.4)/(4.5) of §4.
2. The MOND-radius scaling (5.2), tested by tracing the rotation-curve transition across a sample of high-$z$ galaxies.
3. The mass-independence of both (5.2) and (5.3), tested across the full BTFR mass range at the same redshift.

Any of these failing at $\geq 2\sigma$ after matched velocity-correction systematics constitutes falsification. The intermediate-$z$ rotation-curve constraints from KMOS3D and SINS [10,9] probe windows 1 and 3; their treatment is in §7.

## 6. Galaxy-galaxy weak lensing: dynamical mass enhancement across cosmic time

Galaxy-galaxy weak lensing measures the average tangential shear $\gamma_t(R)$ around galaxies of given baryonic mass and converts it to a projected dynamical mass $M_\text{dyn}(<R)$ within an aperture of physical radius $R$. The ratio $M_\text{dyn}/M_b$ inferred from this analysis is the standard observational measure of "missing mass" attributed under ΛCDM to dark matter halos. Under the framework, the same observation traces the evolution of $a_0(z)$.

### 6.1 The Newtonian-inversion proxy

A relativistic completion of MOND (TeVeS [21], MOG [24], generalized Einstein-aether [25]) is required to predict the full convergence profile $\gamma_t(R)$ of an isolated galaxy from first principles. The framework does not currently commit to a specific relativistic completion. Different completions of MOND that recover the same deep-MOND $v_\text{flat}$ in the local SPARC sample would in general produce different actual lensing signals, due to differences in gravitational slip, external-field effects, and the precise relation between the baryonic potential and the lensing potential. The §6 prediction sidesteps the relativistic-completion question by working not at the level of the actual lensing signal but at the level of the *Newtonian-inversion proxy* that observers actually quote.

Specifically: any observer who measures the asymptotic flat velocity $v_\text{flat}$ at radius $R$ (whether by direct dynamics, by stacked weak lensing, or by satellite kinematics) and applies the Newtonian inversion

$$M_\text{dyn}(R) = \frac{v_\text{flat}^2 \cdot R}{G} \quad \text{(6.1)}$$

infers the same $M_\text{dyn}$ regardless of which underlying gravitational theory produced $v_\text{flat}$. The inversion (6.1) is the convention used in the published galaxy-galaxy lensing literature; it converts a measured shear or rotation signal into a quoted "dark-matter mass" under standard assumptions. The framework predicts $v_\text{flat}(R, z) = (G\,M_b\,a_0(z))^{1/4}$ in the deep-MOND limit (4.1), and (6.1) then maps this to a specific $M_\text{dyn}(R, z)$ at fixed $M_b$.

The §6 prediction is therefore a statement about the *quoted lensing observable under the Newtonian-inversion convention*, not a prediction of the actual relativistic lensing signal. The relation between the actual signal and the Newtonian-inversion proxy is supplied by the relativistic completion through the slip parameter and external-field corrections; we assume this relation reduces to identity in the deep-MOND limit, the working assumption of most modified-gravity lensing analyses, but rigorous demonstration requires committing to a specific completion. The strength of (6.1) as the framework's lensing test is precisely that it is the convention the data-analysis pipelines apply: the measured $M_\text{dyn}$ values that emerge from Euclid DR1 stacked galaxy-galaxy lensing analysis are the Newtonian-inferred proxy quantities the framework predicts, before any relativistic-completion-specific corrections are folded in.

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

A 74% excess in stacked $M_\text{dyn}/M_b$ at $z = 2$ relative to local galaxies of the same baryonic mass is the framework prediction at the Newtonian-inversion proxy level. It applies identically across galaxy mass and lensing aperture in the deep-MOND regime.

Under ΛCDM, the $M_\text{dyn}/M_b$ ratio at fixed baryonic mass and aperture also evolves with redshift, driven by halo concentration evolution and structural changes in the dark-matter halo population [15,16]. The discriminating test between the two pictures is therefore not the existence of redshift evolution but its functional form.

For an $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$) at the canonical $R = 100$ kpc aperture, the ΛCDM prediction under representative Moster-style stellar-to-halo mass relation (SHMR) [17] and Duffy-style concentration [15] inputs is $M_\text{dyn}/M_b = 14.0$ at $z = 0$, $13.6$ at $z = 1$, and $13.8$ at $z = 2$: approximately flat with weak non-monotonicity. The framework prediction at the same aperture is $11.98 \to 16.03 \to 20.86$ across the same redshifts: monotonically increasing as $\sqrt{E(z)}$. The two pictures are quantitatively distinguishable at $z = 2$ by a factor of 1.52 in $M_\text{dyn}/M_b$, large enough to be targeted by a stratified Euclid DR1 stacked analysis (§6.6) once stellar-mass calibration, photometric-redshift uncertainty, aperture definition, and satellite/halo-modeling systematics are propagated. The factor 1.52 is reported here as a benchmark discriminator at representative Appendix B inputs, not a precision Euclid DR1 forecast; SHMR/concentration uncertainty bands and the Euclid measurement-error budget are not propagated in this paper. Different reasonable choices for the SHMR or concentration relation shift the absolute ΛCDM curve values, but the qualitative mass- and aperture-dependence of the ΛCDM shift persists across reasonable parameterizations and is the structural feature that distinguishes the ΛCDM picture from the framework's universal $\sqrt{E(z)}$ enhancement. The ΛCDM comparison methodology, including the specific $(M_\text{halo}, c)$ values and the Navarro-Frenk-White (NFW) enclosed-mass definition, is detailed in Appendix B.

The mass- and aperture-dependence of the ΛCDM prediction sharpens the discriminator further. At $R = 100$ kpc, the ΛCDM $M_\text{dyn}/M_b$ ratio at $z = 2$ relative to $z = 0$ for $L^*$ is 0.98, while reasonable Moster-style SHMR variants for Sub-$L^*$ ($M_b = 10^{10}\,M_\odot$) and Giant ($M_b = 1.5 \times 10^{11}\,M_\odot$) archetypes shift the ratio in opposite directions: Sub-$L^*$ ratios fall below unity as mass-dependent halo concentration evolution dominates, and Giant ratios rise above unity as halo-mass evolution dominates. The framework predicts the same factor 1.74 for all three. At fixed $L^*$ baryonic mass, the ΛCDM ratio shifts from slightly above unity at $R = 30$ kpc to slightly below unity at $R = 300$ kpc, while the framework predicts the same factor 1.74 across all apertures. The framework's universal $\sqrt{E(z)}$ enhancement, mass-independent and aperture-independent in the deep-MOND regime, is the falsifiable signature that distinguishes the prediction from the ΛCDM halo-evolution picture under any reasonable choice of stellar-to-halo mass relation and concentration parameterization.

A Euclid DR1 stacked analysis at $z = 2$ stratified by both galaxy stellar mass and aperture therefore tests the framework on two independent axes simultaneously. First, the magnitude of the redshift shift (74% predicted vs $\sim 0\%$ under ΛCDM at $L^*$). Second, its universality across mass and aperture (universal under MIT vs mass- and aperture-dependent under ΛCDM).

### 6.3 Numerical predictions for the $L^*$ archetype

Table 4 evaluates (6.3) for the $L^*$ archetype at three standard galaxy-galaxy lensing apertures (30, 100, 300 kpc) at five redshifts. The $L^*$ block is shown in the main text as the canonical case; the complete table covering all four §5 archetypes (Dwarf, Sub-$L^*$, $L^*$, Giant) is provided as supplementary data and exhibits the same row-by-row fractional scaling.

**Table 4.** Predicted $M_\text{dyn}/M_b$ from (6.3) for the $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$) at three apertures and five redshifts. Values within each row scale as $\sqrt{E(z)}$. The same fractional scaling holds across the Dwarf, Sub-$L^*$, and Giant archetypes, confirming the mass- and aperture-independence of the prediction.

| $R$ [kpc] | $z = 0$ | $z = 0.5$ | $z = 1$ | $z = 2$ | $z = 5$ |
|---:|---:|---:|---:|---:|---:|
| 30 | 3.59 | 4.13 | 4.81 | 6.26 | 10.35 |
| 100 | 11.98 | 13.77 | 16.03 | 20.86 | 34.50 |
| 300 | 35.93 | 41.32 | 48.08 | 62.57 | 103.50 |

The fractional shift from $z = 0$ to $z = 2$ is identical across all three rows: a factor $1.741$ ($\sqrt{E(z=2)}$). The $R = 100$ kpc row provides the canonical galaxy-galaxy lensing example: a quoted $M_\text{dyn}/M_b = 11.98$ at the local Universe (the standard "dark-matter dominated" inference of $\sim 92\%$ dark mass fraction) becomes $20.86$ at $z = 2$ (under the same Newtonian inversion, $\sim 95\%$ inferred dark mass fraction). The 74% excess is the framework prediction, accessible through stacked lensing at known galaxy redshift. The mass-independence of the same enhancement, verified across the full supplementary table, is what distinguishes the framework prediction from the ΛCDM halo-concentration alternative discussed in §6.2.

### 6.4 Figure 5: $M_\text{dyn}/M_b$ vs aperture for $L^*$ at $z = 0, 1, 2$

**Figure 5.** Predicted $M_\text{dyn}(R)/M_b$ for the $L^*$ archetype ($M_b = 6 \times 10^{10}\,M_\odot$) as a function of physical aperture $R$ from 10 to 500 kpc, at $z = 0$, $z = 1$, $z = 2$. The framework prediction (6.3) is plotted as solid lines (lower at $z = 0$, middle at $z = 1$, upper at $z = 2$); three lines of slope unity in $\log R$, vertically offset by $\log_{10}\sqrt{E(z)}$. The ΛCDM prediction under standard halo concentration evolution [15] is plotted as dashed lines for comparison.

The framework's vertical offset is the §6 prediction: constant in $\log_{10} M_\text{dyn}/M_b$ across the full plotted aperture range, growing as $\sqrt{E(z)}$ between redshifts. The ΛCDM curves are nearly degenerate across $z = 0$, $1$, $2$ because halo concentration decreases with $z$ approximately compensates the implicit halo-mass evolution under the SHMR; the residual aperture-dependence and mass-dependence of the ΛCDM prediction are the discriminators against the framework's universal enhancement, as quantified in §6.2.

### 6.5 What the framework does not predict here

Three lensing observables are *not* addressed by §6, and require future work:

1. *The full convergence profile $\gamma_t(R)$ as a function of aperture for an isolated galaxy.* This requires committing to a relativistic completion of MOND, which the framework does not yet do.

2. *Cluster-scale lensing.* The MOND-cluster mass discrepancy [12] is an inherited problem from local MOND that evolving $a_0$ does not resolve, because clusters are observed at $z \lesssim 0.3$ where $a_0(z)/a_0(0) \leq 1.17$. The framework's contribution at cluster scales is at the percent level, well below the factor $\sim 5$ cluster discrepancy. §7 treats this in full.

3. *The sign and magnitude of any non-deep-MOND-regime corrections to (6.3).* For galaxies at intermediate accelerations ($g_N \sim a_0$) at $z = 0$, the same caveat from §4.4 applies: the deep-MOND ratio prediction may not extend cleanly into the transition region, where the interpolating function matters. (6.3) strictly applies in the deep-MOND limit.

These three are open. The $M_\text{dyn}/M_b$ scaling (6.3) is what the framework predicts unambiguously; the rest is acknowledged outside the scope.

### 6.6 Falsification

The §6 prediction (6.3), operationalized as a statement about the Newtonian-inferred $M_\text{dyn}/M_b$ proxy used by stacked-lensing pipelines, admits two independent falsification windows:

1. The $\sqrt{E(z)}$ scaling at any single redshift, tested by stacked galaxy-galaxy lensing of mass-controlled galaxy samples at that redshift. A measured $M_\text{dyn}/M_b$ at $z = 2$ that is *not* enhanced by $\sim 74\%$ relative to $z = 0$ at the same baryonic mass and aperture, beyond systematic uncertainty, falsifies (6.3).

2. The mass- and aperture-independence of the enhancement, tested by stratifying the lensing analysis by both galaxy stellar mass and aperture. The fractional shift must be $\sqrt{E(z)}$ in every cell.

Both windows are accessible to Euclid DR1 (October 2026) galaxy-galaxy lensing at $z = 0.5\text{–}2$ with stacked samples of $\sim 10^5$ galaxies. The expected statistical sensitivity at fixed $M_b$ stratification is at the few-percent level on $M_\text{dyn}/M_b$, which is well below the 15-74% predicted shifts across the $z = 0.5$ to $2$ window.

The forward reference to §7 covers the inherited cluster-MOND discrepancy and any current intermediate-$z$ lensing constraints.

## 7. Existing constraints and consistency

The framework predictions of §§4-6 are tested against existing measurements in five regimes: local galactic dynamics ($z \approx 0$), intermediate-redshift kinematics ($z = 0.5\text{–}2.5$), galaxy clusters ($z \lesssim 0.3$), the cosmic microwave background ($z \approx 1090$), and strong gravitational lensing time delays. Each regime is treated separately because the constraints are independent and the framework's status differs across them.

### 7.1 Local galactic dynamics: SPARC and THINGS

The framework reproduces local MOND phenomenology by construction. The well assignments in §2 were calibrated against the local values $a_0(0) = 1.20 \times 10^{-10}$ m/s$^2$ and $H_0 = 67.4$ km/s/Mpc, and the BTFR normalization, rotation-curve fits, and lensing inferences at $z \approx 0$ inherit the standard MOND results documented in the SPARC and THINGS analyses [18,2,3]. No independent test at $z = 0$ is provided by the present paper; the §3 calibration is what the §§4-6 predictions are extrapolations from.

### 7.2 Intermediate-redshift Tully-Fisher: KMOS3D

The KMOS3D survey [11] (a 3D integral-field galaxy survey with the K-band Multi-Object Spectrograph at the VLT) provided the Übler et al. 2017 [9] analysis of the baryonic Tully-Fisher relation at two redshift bins, drawing on VLT/KMOS integral-field spectroscopy of $\sim 240$ star-forming galaxies. Their fixed-slope zero-points are $b = 10.68 \pm 0.04$ at $z \approx 0.9$ and $b = 10.85 \pm 0.05$ at $z \approx 2.3$. Relative to the local Lelli et al. baseline [2], their fiducial pressure-support-corrected analysis reports zero-point offsets

$$\Delta b^\text{obs}(z=0.9) = -0.44~\text{dex}, \qquad \Delta b^\text{obs}(z=2.3) = -0.27~\text{dex}.$$

The framework prediction (4.3) gives

$$\Delta b^\text{MIT}(z=0.9) = -\log_{10} E(0.9) = -0.227~\text{dex}, \qquad \Delta b^\text{MIT}(z=2.3) = -0.540~\text{dex}.$$

The Übler measurement is the only existing quantitative test of the §4 framework prediction at intermediate redshift. The other intermediate-$z$ kinematic samples treated below (Genzel et al. 2017 [10]) do not report a BTFR zero-point, and the next quantitative tests will arrive with Euclid DR1.

**Magnitude.** The framework predictions and the Übler observations are in the same envelope: both are large negative shifts, both place the high-$z$ BTFR substantially below the local relation. The single-redshift residuals are quantified in the σ-tension table below.

**Trend shape.** The observed offsets are non-monotonic in redshift ($-0.44 \to -0.27$ dex), while the framework predicts a strict monotonic decrease ($-0.227 \to -0.540$ dex). This is the core of the tension: the framework's evolution prediction is monotonic, the observation is not.

Quantitatively, the residuals (observed minus MIT prediction) are $-0.216$ dex at $z \approx 0.9$ and $+0.270$ dex at $z \approx 2.3$, with opposite signs reflecting the non-monotonic trend. Translating to $\sigma$ tensions under three uncertainty budgets:

| Uncertainty budget | $T(z=0.9)$ [σ] | $T(z=2.3)$ [σ] | Joint [σ] |
|---|---|---|---|
| Übler statistical only | $-5.4$ | $+5.4$ | $7.6$ |
| + Lelli local-baseline (0.05 dex) | $-3.4$ | $+3.8$ | $5.1$ |
| + velocity-correction systematic (0.10 dex) | $-1.8$ | $+2.2$ | $2.9$ |

Even under the most conservative budget, with a generous 0.10 dex velocity-correction systematic added in quadrature, the joint tension reaches $2.9\sigma$ and the $z = 2.3$ point individually sits at $2.2\sigma$. Under the more defensible Budget B (statistical plus the standard SPARC local-baseline uncertainty), the joint tension is $5.1\sigma$. The current Übler data therefore constitutes a genuine quantitative tension with the framework's monotonic prediction at the trend-shape level, not a marginal disagreement that conservative systematics could absorb. We treat this as a *provisional tension* rather than a formal falsification of the §4 prediction. The comparison combines heterogeneous velocity definitions and cross-redshift pressure-support corrections relative to the local SPARC baseline; one such systematic is tested by the forward-model analysis below and ruled out as the sole explanation, but the broader cross-instrument and cross-tracer heterogeneity in the comparison remains. Formal falsification of (4.3) requires a matched-systematics measurement at $\geq 2\sigma$ in the sense of Table 7: a single instrument, uniform kinematic tracer, and identically applied velocity-correction prescription across the redshift bins.

The Übler pressure-support correction is a radial thick-disk expression $v_\text{circ}^2(r) = v_\text{rot}^2(r) + 2\,\sigma_0^2\,r/R_d$ [19], with the effective coefficient $\alpha(r) = 2r/R_d$ depending on the radial position at which $v_\text{rot}$ is measured and on the disk scale length $R_d$. Both quantities evolve systematically with redshift. Forward-modeling exercises sweeping fixed-coefficient surrogates and bias-model variants over literature-plausible parameter ranges (radial-position uncertainty, beam-smearing of $\sigma_0$ at high $z$, non-asymptotic rotation curves at low $z$, and selection-induced mass-distribution shifts) can soften the comparison but do not, by themselves, remove the observed non-monotonic BTFR offset pattern. The quantitatively reproducible tension is the σ-table above: $7.6\sigma$ under statistical errors alone, $5.1\sigma$ including the local Lelli baseline uncertainty, and $2.9\sigma$ under a conservative 0.10 dex velocity-correction systematic. The KMOS3D BTFR result is therefore a genuine, systematics-limited tension with the framework's monotonic prediction, not a demonstrated velocity-correction artifact.

The Übler tension is therefore not a velocity-correction artifact under any literature-plausible bias model. It is a genuine tension between the framework's monotonic prediction and the observed non-monotonic trend, and it cannot be dissolved by the simple systematic the §7.2 defense initially proposed.

Two concrete resolution paths remain:

(i) The Euclid DR1 NISP grism survey (October 2026) delivers H$\alpha$ kinematics at $z = 0.7\text{–}1.8$ and [OIII] at $z = 1.1\text{–}2.4$ from a single instrument under uniform selection, providing the first self-consistent cross-redshift BTFR comparison free of the matched-tracer systematic that limits existing ground-based analyses. The expected sample size is $\sim 10^5$ galaxies in the wide survey, more than two orders of magnitude beyond the Übler sample, with statistical sensitivity to $\Delta b$ at the 0.02-dex level after mass stratification.

(ii) JWST follow-up of resolved kinematics at $z \approx 0.9$ and $z \approx 2.3$ in matched samples (COSMOS-Web NIRSpec IFU and NIRCam grism programs already underway) allows a direct test of (4.3) under controlled velocity-correction prescriptions applied identically across both redshift bins, removing the cross-instrument systematic that affects the existing ground-based comparison.

The framework's evolution prediction stands as the §4 derivation requires; its status against the present Übler measurement is one of genuine tension on the trend shape, and resolution awaits the next-generation matched-systematics measurements named above. The framework neither retreats from the prediction nor pretends to have explained the tension away.

### 7.3 Intermediate-redshift rotation curves: SINS and KMOS3D

The Genzel et al. 2017 sample [10] of six massive star-forming disks at $z = 0.85\text{–}2.38$ reports declining outer rotation curves with low inferred dark-matter fractions, interpreted as baryon-dominated disks with pressure support. Because no BTFR zero-point is reported, the measurement is qualitatively consistent with §§4-5 but does not directly test the framework's normalization prediction (4.3). A joint re-analysis of the Genzel and Übler samples under matched velocity-correction prescriptions would convert this into a sharper constraint.

### 7.4 Galaxy clusters: the Pointecouteau-Silk discrepancy

Local MOND analyses of galaxy clusters report a residual mass discrepancy beyond what MOND alone provides. Pointecouteau & Silk (2005) [12] find that eight nearby relaxed X-ray clusters require an effective acceleration scale several times the galaxy-scale $a_0$ to reproduce the observed dynamical mass with MOND alone. Equivalently, MOND with the standard galactic $a_0$ underpredicts the cluster dynamical mass by roughly a factor of $\sim 5$ at $r \approx 0.5\,R_\text{vir}$.

The framework's evolving $a_0(z)$ does not resolve this discrepancy. The Pointecouteau-Silk sample lives at $z \lesssim 0.15$, where $E(z) \leq 1.08$ and the framework $a_0(z)$ exceeds the local value by less than 8%. Even at $z = 0.3$, the upper end of the cluster lensing literature, the framework correction is at most $\sim 17\%$. A factor of $\sim 5$ residual discrepancy is not addressed by a $\lesssim 17\%$ correction.

The cluster discrepancy is therefore an inherited problem from local MOND that the framework's epoch dependence does not address at the relevant cluster redshifts. The standard local-MOND interpretations of the discrepancy (residual gravitational sources at cluster scales, undetected baryonic components, or a breakdown of MOND in the cluster regime) apply unchanged. The cluster-scale mass discrepancy is an open problem shared by all MOND-class theories [13,14,3] and predates the present framework. The framework's epoch-dependent modification operates at the percent level in the cluster redshift range and neither introduces nor resolves this discrepancy.

### 7.5 The cosmic microwave background at recombination

This section addresses the apparent CMB tension in three steps: (i) the structural argument from the framework's selection rule, which assigns cosmological perturbations to a different manifold-mode sector than $a_0$; (ii) an empirical leakage bound from Planck consistency, which constrains any residual coupling between the sectors; and (iii) the comparison with relativistic MOND extensions (TeVeS, BIMOND, AeST), which contextualizes the framework's structural decoupling against dynamical alternatives. The naive over-application identifies the issue; the structural argument resolves it conditional on the selection rule; the leakage bound and the relativistic-MOND comparison test that conditional from different angles.

A naive application of the framework's $a_0(z)$ scaling to cosmological perturbations at recombination produces large modifications to the predicted CMB acoustic peak structure. At $z = 1090$, $a_0(z) \approx 2.79 \times 10^{-6}$ m/s$^2$, approximately 23,000 times the local value. The Newtonian gravitational acceleration of perturbations at the sound-horizon scale (133 kpc physical at recombination, corresponding to the comoving sound horizon of $\sim 145$ Mpc) with amplitude $\delta\rho/\rho \sim 10^{-5}$ is $g_N^\text{pert} \sim 4 \times 10^{-11}$ m/s$^2$, roughly five orders of magnitude below $a_0(z)$ at the same epoch. Under this naive reading, perturbations at recombination would be deeply in the MOND regime and the acoustic-peak amplitudes would deviate significantly from the well-fit ΛCDM prediction.

The naive reading misapplies the framework's selection rule. The rule, introduced in §2 and detailed in §2.1, assigns observables to manifold-mode classes by the index $n$ in the embedding hierarchy $S^1 \subset \text{Möbius} \subset S^3$:

| Mode | $n$ | References | Evolves? | Governs |
|---|---:|---|---|---|
| Edge | 1 | $\Omega_H(z)$ | Yes | Galactic dynamics ($a_0$, $H$) |
| Surface | 2 | $\Omega_\Lambda$ | No | Vacuum energy (Λ) |
| Space | 3 | $\Omega_\Lambda$ | No | Cosmological perturbations |

The selection rule is not a free choice introduced to escape the CMB constraint. The same rule places $a_0$ at well 13/120 and $H_0$ at well 34/120 in §2, both as edge-mode observables, and the Milgrom ratio match at 0.8% (§2.5) follows as a structural consequence of those assignments. The rule predates the $a_0(z)$ derivation; it was not constructed to address the CMB constraint, and its assignment of cosmological perturbations to the $n = 3$ space-mode sector is the same rule's application to a different observable class.

Under the rule, cosmological perturbations are a space-mode observable ($n = 3$): they live on the spatial slice $S^3$ and propagate through it. The hierarchy reference for the space mode is $\Omega_\Lambda$, the same fixed eigenvalue ratio that fixes Λ in the surface sector. The framework therefore predicts that the dynamical evolution of cosmological perturbations is governed by space-mode physics referenced to a constant $\Omega_\Lambda$, with no $a_0(z)$ modification. This is structurally distinct from the edge sector ($n = 1$) where $a_0$ lives.

The framework's CMB prediction is therefore identical to ΛCDM's CMB prediction, conditional on the structural decoupling. The $a_0(z)$ scaling derived in §2 governs the edge sector, where galactic dynamics live at $r \sim r_M$ and the kinematic horizon $\Omega_H(z)$ sets the hierarchy. Recombination physics is a space-mode phenomenon, governed by $\Omega_\Lambda$, and inherits ΛCDM's predictions for the acoustic peak structure, the polarization spectra, the lensing reconstruction, and the integrated Sachs-Wolfe imprint. The success of ΛCDM in fitting Planck 2018 [20] at sub-percent precision is consistent with the framework's $n = 3$ assignment for cosmological perturbations, provided the edge/space-mode decoupling is exact. The Planck fit empirically constrains the perturbation physics; the framework's structural prediction is that the same physics emerges from the $n = 3$ space-mode sector with $\Omega_\Lambda$ as its hierarchy reference, but the formal demonstration of this equivalence at the perturbation-theory level remains open work flagged below.

We now make this consistency condition quantitative. Writing a minimal leakage ansatz for any residual edge-mode coupling into cosmological perturbations,

$$g_\text{eff}(R, z) = g_N(R, z) + \varepsilon \cdot \sqrt{g_N(R, z) \cdot a_0(z)},$$

the sound-horizon perturbation at recombination ($R \approx 0.13$ Mpc physical, $g_N \approx 4 \times 10^{-11}$ m/s$^2$) and the sub-horizon BAO scale ($R \approx 0.05$ Mpc, $g_N \approx 1.5 \times 10^{-11}$ m/s$^2$) have $\sqrt{a_0(z=1090)/g_N} = 264$ and $430$, respectively. Under the Sachs-Wolfe relation $\Delta T/T \approx \Phi/3$, any leakage at level $\varepsilon$ produces a fractional first-peak amplitude shift $\delta C_\ell^\text{peak}/C_\ell^\text{peak} \approx \varepsilon \cdot \sqrt{a_0/g_N}$. The Planck 2018 first-peak amplitude precision ($\lesssim 0.5\%$) bounds the leakage to

$$\varepsilon \lesssim 1.2 \times 10^{-5} \quad (0.5\% \text{ tolerance}), \qquad \varepsilon \lesssim 1.6 \times 10^{-5} \quad (\text{literal Planck}),$$

with the sub-horizon BAO scale providing the most-constraining bound. The bound is robust against ansatz choice (modified interpolation function, scale-dependent coupling) within an order of magnitude. The framework's selection rule predicts $\varepsilon = 0$ exactly under the $n = 3$ space-mode assignment for cosmological perturbations, satisfying the empirical bound by every margin Planck currently provides.

This handling differs structurally from how relativistic MOND extensions address the same recombination-scale problem. TeVeS [21] introduces additional scalar and vector fields whose dynamics reduce to GR at cosmological scales while reproducing MOND in the galactic regime; the resulting CMB perturbation predictions, computed in modified Boltzmann codes, are in residual tension with the third-acoustic-peak height and require additional dark-matter components to fit Planck [3]. BIMOND [22] introduces a second metric whose interaction term produces the MOND limit; its cosmological perturbation predictions remain incomplete in the published literature. More recently, Skordis & Złośnik (2021) [23] introduced an Æther-Scalar-Tensor (AeST) theory that reproduces the full ΛCDM CMB power spectrum without an additional cold dark matter component while supporting MOND-like galactic dynamics, the first relativistic MOND extension to fit the CMB acoustic structure end-to-end. The present framework's approach is structurally distinct from all three: rather than adding fields or metrics, it specifies through the manifold-mode selection rule (§2.1) that galactic-edge and cosmological-perturbation physics sit in different sectors of the same scaling-law postulate. The decoupling is structural rather than dynamical; the empirical bound $\varepsilon \lesssim 10^{-5}$ confirms consistency with Planck without requiring the framework to commit to a specific relativistic completion. Whether the AeST-style dynamical mechanism and the present framework's structural decoupling are equivalent at the perturbation-theory level is the open question identified below.

The remaining open question is a first-principles perturbation-theoretic derivation of the edge/space-mode decoupling at recombination-relevant scales. Such a derivation, working from the Boltzmann hierarchy or equivalent under the framework's $(n, \Omega)$ assignments, would replace the present structural argument plus empirical bound with a closed-form proof. The required machinery (mode-projected propagators, anti-periodic boundary conditions on the Möbius surface, hierarchy-sensitive transfer functions) is expressible within the framework's existing postulates; we expect the calculation to be tractable rather than to require new theoretical inputs not already present in the framework, but it has not been carried through and is the principal open task for the framework's CMB-scale predictions.

The §7.5 position is conditional on the structural decoupling: (i) the apparent CMB tension under naive over-application of $a_0(z)$ dissolves under the framework's selection rule; (ii) the rule's assignment of cosmological perturbations to the $n = 3$ space-mode sector is the same rule that produces the §2.5 Milgrom-ratio match and is not introduced separately to address the CMB; (iii) any residual edge-mode leakage into cosmological perturbations is bounded to $\varepsilon \lesssim 10^{-5}$ by Planck consistency, with the framework's structural prediction $\varepsilon = 0$ satisfying the bound by every margin Planck currently provides; (iv) the framework's CMB prediction coincides with ΛCDM's at every Planck-measured observable, with the formal perturbation-theory derivation flagged as the principal open task.

### 7.6 Strong gravitational lensing time delays

Strong-lensing time-delay cosmography (TDCOSMO [34], H0LiCOW [35]) probes $H_0$ at sub-percent precision but is not currently sensitive to $a_0(z)$ at the level of the framework's predictions, because the time-delay signal lives at lens-galaxy scales where the MOND interpolating function matters and the deep-MOND ratio prediction (4.3) does not strictly apply. Existing time-delay analyses are consistent with both the framework and standard ΛCDM at current precision; no live constraint exists in this regime.

### 7.7 JWST early-galaxy collapse-time speedup (supporting evidence)

JWST imaging at $z = 7\text{–}10$ has identified candidate massive galaxies [6,26] with stellar masses $M_\star \gtrsim 10^{10}\,M_\odot$ assembled within $\sim 600$ Myr of cosmic time, requiring star-formation efficiencies $\varepsilon_\text{SF} \gtrsim 1$ under standard ΛCDM halo growth, formally impossible because no more than the cosmic-baryon-fraction-times-halo-mass can be converted into stars. Under the framework's evolving $a_0(z)$, the deep-MOND effective gravitational acceleration $g_\text{eff} = \sqrt{g_N\,a_0(z)}$ scales as $\sqrt{E(z)}$ at fixed Newtonian source, and the corresponding free-fall collapse time $t_\text{ff} \propto 1/\sqrt{g_\text{eff}}$ shortens as $E(z)^{-1/4}$. Equivalently, the required $\varepsilon_\text{SF}$ to assemble a given $M_\star$ at observed redshift $z$ is reduced from the ΛCDM value by $\varepsilon_\text{SF}^\text{MIT}(z) = \varepsilon_\text{SF}^{\Lambda\text{CDM}}(z)/E(z)^{1/4}$. Applied to the six massive central-value candidates from the Labbé sample at $z_\text{phot} = 7.318\text{–}9.077$ (IDs 11184, 38094, 2859, 13050, 14924, 35300), the framework speedup factor $E(z)^{1/4} \approx 1.92\text{–}2.06$ reduces the required star-formation efficiency uniformly by a factor of $\sim 2$, with no per-galaxy tuning. Whether this resolves the impossibility constraint for any specific candidate depends on halo-mass priors carried over from the ΛCDM-side analysis (halo mass function, abundance matching prescription, survey volume, photometric-redshift uncertainty), which the framework does not improve directly; the per-object analysis with explicit halo abundance matching is reserved for future work. The framework contribution here is the multiplicative speedup factor, supporting evidence for the framework's edge-mode evolution rather than a primary prediction. The prediction is a free-fall scaling argument, not a full simulation of structure formation under modified gravity; back-reaction on the baryon-to-dark-matter ratio in the collapsing region and any modification to the initial-condition power spectrum from the §7.5 mode-selection question are open work that would refine but not overturn the order-of-magnitude estimate. The full sample table and the Labbé candidate identifiers are provided in the data deposit.

### 7.8 Summary of constraint status

**Table 5.** Summary of existing constraint status across the five regimes treated above.

| Regime | Constraint | Framework status |
|---|---|---|
| Local ($z = 0$) | SPARC, THINGS | Consistent by construction (§2 calibration) |
| Intermediate-$z$ BTFR | Übler 2017 [9] | Live tension on trend shape; forward-model analysis confirms not a velocity-correction artifact |
| Intermediate-$z$ rotation curves | Genzel 2017 [10] | Qualitatively consistent; not a sharp quantitative test |
| Galaxy clusters | Pointecouteau-Silk 2005 [12] | Inherited problem unaddressed by epoch-dependent $a_0$; not worsened by the framework |
| CMB ($z \approx 1090$) | Naive over-application | Resolved structurally by the §2 selection rule; minimal-leakage Planck bound $\varepsilon \lesssim 10^{-5}$ confirms consistency with the framework's structural $\varepsilon = 0$ prediction; rigorous derivation open |
| Strong-lens time delays | TDCOSMO, H0LiCOW | Below current sensitivity; consistent at present |

The status column reads as one live tension (Übler, with the velocity-correction systematic explanation tested and ruled out by forward-modeling), one inherited open problem (clusters, neither caused nor resolved by the framework), one structurally resolved apparent tension (CMB, with rigorous derivation flagged), one qualitative consistency (Genzel), and two consistencies by construction or below sensitivity.

The framework is therefore consistent with the existing constraint landscape at the level of the present paper's claims, except for the Übler trend-shape tension which is acknowledged and held against the framework's explicit prediction. The Euclid DR1 galaxy-galaxy lensing measurement (§6) and the matched-velocity-correction Tully-Fisher analysis (§4, §7.2) are the two near-term tests that will sharpen the constraint into a definitive result, in either direction, on a timescale of approximately two years.

## 8. Connection to the companion Λcos prediction and the broader framework

### 8.1 Two predictions from one scaling law

The framework derivation of §2 makes two structurally independent predictions about cosmic evolution, both following from the same measurement postulate $A/A_P = C(\Theta) \cdot N^n$ but addressing different sectors of the manifold-mode hierarchy.

**§§3-6 (this paper).** The MOND acceleration scale is an edge-mode observable ($n = 1$) referenced to the kinematic horizon ratio $\Omega_H \approx (c/(H\,\ell_P))^2$. The local-epoch reading of (2.1) gives $a_0(z) = a_0(0)\,E(z)$, governing galactic-scale dynamics across cosmic time and tested through the five-exponent prediction set summarized in §9.

**Surface-sector prediction (separately submitted companion analysis).** The cosmological constant Λ is a surface-mode observable ($n = 2$) referenced to the eigenvalue ratio $\Omega_\Lambda$ (§2.1). The local-epoch reading of (2.1) gives $\Lambda = \text{const.}$ at every epoch, while the apparent equation-of-state evolution $w(z)$ reported by DESI DR2 [8] arises as a template artifact from the observer's phase position $t \approx 5.22$ rad on the underlying standing wave $\Psi(t) = \cos(t/2)$.

The §7.5 selection rule organizes both predictions in a single table: the edge sector evolves through $\Omega_H(z)$, the surface sector remains fixed through $\Omega_\Lambda$, and (a third assignment relevant to §7.5's CMB consistency) the space sector ($n = 3$) governs cosmological perturbations also through $\Omega_\Lambda$. The two papers test the first two rows of that table; their joint outcome tests the rule itself.

The structural symmetry is the headline: the framework predicts that $a_0$ evolves while Λ does not, the inverse of standard ΛCDM assumptions where Λ is the candidate evolving quantity (DESI's $w(z)$) and $a_0$ is assumed to be a universal constant.

### 8.2 Independent tests, joint pattern

The two predictions are testable through disjoint instruments and analyses, and either could be confirmed or falsified independently of the other.

**Edge-sector tests (this paper).** Intermediate-redshift Tully-Fisher (KMOS3D, KGES), galaxy-galaxy weak lensing (Euclid DR1), and JWST early-galaxy spectroscopy. Five distinct observables, all governed by powers of $E(z)$ as compiled in §9 Table 6.

**Surface-sector tests (companion analysis).** Baryon acoustic oscillation distance ratios (DESI DR2/DR3 [8]), Type Ia supernova distance moduli (Pantheon+ [27], DES-SN5YR [28]), and the CMB-calibrated sound-horizon ruler. The companion analysis reports $\Delta\chi^2 = +0.13$ relative to flat ΛCDM at the same parameter count, with the model's single parameter constrained to $s_0 < 0.18$ (95% CL).

Four joint outcomes are structurally distinct and would carry different evidentiary weight:

| Edge sector ($a_0$ evolves) | Surface sector (Λ constant) | Implication |
|---|---|---|
| Confirmed | Confirmed | Joint evidence for the selection rule |
| Confirmed | Falsified | Edge sector valid; surface assignment requires revision |
| Falsified | Confirmed | Surface sector valid; edge assignment requires revision |
| Falsified | Falsified | Selection rule itself falsified |

Either-or outcomes do not imply the framework is half-correct; they would identify which $(n, \Omega)$ assignment fails. The rule's status is determined by the joint pattern, not by either test in isolation.

### 8.3 Pre-registration and the broader framework

The present paper will be deposited on Zenodo prior to the Euclid DR1 release in October 2026, fixing its predictions before the data arrive. The companion analysis is similarly deposited prior to Euclid DR1 and DESI DR3.

The companion analysis on the surface sector and the present paper are the framework's two near-term tests; the broader claim that the same scaling-law postulate produces predictions in additional sectors of the framework is a meta-result that accrues with each individual test, but is not the subject of the present paper.

## 9. Predictions and falsification

### 9.1 Five predictions from one relation

The §§4-6 predictions follow from a single input: $a_0(z) = a_0(0)\,E(z)$, derived in §2 and tabulated in §3. Each section computes a different observable, and each observable depends on $E(z)$ through a different power. Table 6 collects all five.

**Table 6.** The full predictive content of the framework's evolving acceleration scale, organized by observable and scaling. Numerical values are evaluated at $z = 2$, the cleanest test window for current intermediate-redshift programs. All five entries derive from the single relation $a_0(z) = a_0(0)\,E(z)$ with no additional free parameter.

| Section | Observable | Scaling | Value at $z = 2$ | Test instrument |
|---|---|---|---|---|
| §4 | BTFR normalization $A_\text{BTFR}(z)/A_\text{BTFR}(0)$ | $E(z)^{-1}$ | 0.330 | KMOS3D, KGES, Euclid DR1 |
| §5 | MOND radius $r_M(z)/r_M(0)$ | $E(z)^{-1/2}$ | 0.574 | High-$z$ rotation curves |
| §4, §5 | Asymptotic velocity $v_\text{flat}(z)/v_\text{flat}(0)$ at fixed $M_b$ | $E(z)^{+1/4}$ | 1.320 | KMOS3D, KGES, Euclid DR1 |
| §6 | Lensing $M_\text{dyn}/M_b$ enhancement (Newtonian-inversion proxy) | $E(z)^{+1/2}$ | 1.741 | Euclid DR1 stacked galaxy-galaxy lensing |
| §7.7 | Free-fall collapse time $t_\text{ff}(z)/t_\text{ff}(0)$ | $E(z)^{-1/4}$ | 0.758 | JWST early-galaxy spectroscopy |

The five exponents $\{-1, -1/2, +1/4, +1/2, -1/4\}$ exhaust the ways a power of $a_0(z) \propto E(z)$ enters at the level of asymptotic deep-MOND galactic dynamics. They are not independent predictions: any measurement of $E(z)$ at a single redshift through any of the five observables determines the other four through their shared dependence on the same input. Conversely, a measurement that confirms one observable but disconfirms another at the same $z$ falsifies the framework's universality across observable classes, even if no individual exponent disagrees with data.

This is the structural strength of the framework's evolution prediction. One relation calibrated at $z = 0$ ($a_0(0)$ from SPARC) generates five distinct $z$-dependent observable channels, all controlled by the same input $E(z)$ through different powers. The five channels are not independent tests of $E(z)$; they are correlated manifestations of one input.

### 9.2 Falsification criteria

Table 7 collects the falsification criteria stated in §§4-6. Each row gives the prediction's signature, the threshold at which the framework is ruled out, and the systematic that must be controlled to make the test robust.

**Table 7.** Falsification criteria for the five predictions of §§4-6. Failure of any criterion at $\geq 2\sigma$ in a matched-systematics measurement (uniform tracer, velocity definition, and analysis prescription across the redshift bins) constitutes formal falsification of the framework's $a_0(z) \propto E(z)$ relation. Existing heterogeneous-data tensions, including the Übler 2017 trend-shape tension treated in §7.2, are treated as provisional pending matched-systematics resolution.

| Prediction | Signature | Falsification threshold | Controlled systematic |
|---|---|---|---|
| §4 BTFR (A) | $A_\text{BTFR}(z)/A_\text{BTFR}(0) = 1/E(z)$ | Single-$z$ inconsistency at $\geq 2\sigma$ | Pressure-support velocity correction $\alpha\,\sigma^2$ |
| §4 BTFR (shape) | Strict monotonic decrease in $z$ | Non-monotonic trend confirmed under matched-systematics measurements at $\geq 2\sigma$ | Cross-instrument matched-tracer systematic (resolved by Euclid DR1 single-instrument analysis); the Übler radial pressure-support systematic was tested via forward-modeling and does not account for the observed non-monotonicity |
| §5 $r_M$ scaling | $r_M(z)/r_M(0) = E(z)^{-1/2}$ | Single-$z$ inconsistency at $\geq 2\sigma$ | Baryonic-mass distribution model |
| §5, §6 mass-independence | Fractional shift independent of $M_b$ | Mass-stratified analysis showing mass-dependent shift | Halo-mass dependence in selection function |
| §6 lensing | Newtonian-inferred $M_\text{dyn}/M_b$ enhancement $= \sqrt{E(z)}$, mass- and aperture-independent | Single-$z$ inconsistency at $\geq 2\sigma$, OR mass/aperture-stratified analysis showing mass- or aperture-dependent shift | Halo-concentration evolution model (Duffy et al. 2008 [15] baseline) |
| §7.7 JWST efficiency | $\varepsilon_\text{SF}^\text{MIT}(z) = \varepsilon_\text{SF}^{\Lambda\text{CDM}}(z)/E(z)^{1/4}$ | Spectroscopically confirmed candidate with $\varepsilon_\text{SF}^{\Lambda\text{CDM}} \geq 1$ whose corrected efficiency $\varepsilon_\text{SF}^\text{MIT} = \varepsilon_\text{SF}^{\Lambda\text{CDM}}/E(z)^{1/4}$ still exceeds unity at $\geq 2\sigma$ | Halo abundance matching prescription |

The lensing test in row 5 is the cleanest of the five because the enhancement $\sqrt{E(z)}$ is universal across galaxy mass and aperture, whereas the ΛCDM alternative (halo concentration evolution) produces shifts that depend on both. A mass- and aperture-stratified Euclid DR1 analysis tests both the magnitude of the prediction and its universality in a single dataset.

### 9.3 Test schedule

Three near-term measurements will deliver the bulk of the test:

| Window | Instrument | Predictions tested | Expected delivery |
|---|---|---|---|
| Galaxy-galaxy lensing at $z = 0.5\text{–}2$ | Euclid DR1 | §6 (lensing), §9.2 universality | October 2026 |
| Intermediate-$z$ BTFR with matched velocity corrections | KMOS3D + KGES + MOSDEF joint re-analysis | §4 BTFR, §5 $v_\text{flat}$ | Ongoing (~ 2026) |
| Spectroscopic confirmation of impossible JWST candidates | JWST/NIRSpec follow-up of Labbé sample | §7.7 ε_SF | In progress (~ 2025-2026) |

Beyond this window, sharper tests come from longer-term programs: a dedicated multi-redshift BTFR campaign with consistent kinematic tracers (H$\alpha$ at $z \sim 1.5$, [OIII] at $z \sim 1$, Pa$\alpha$ at $z \sim 0.3$) controlled for sample selection, the COSMOS-Web spectroscopic complete to $z \sim 10$, and the next generation of weak-lensing surveys (LSST, Roman) extending the §6 stratified analysis to $z \sim 3$.

The framework's evolution prediction is therefore testable on a two-year timescale, with the Euclid DR1 lensing measurement providing the single sharpest test of the universal $\sqrt{E(z)}$ enhancement across galaxy mass and aperture.

### 9.4 Summary

The framework's predictive content reduces to one statement and five corollaries.

**Statement.** $a_0(z) = a_0(0) \cdot E(z)$, with $a_0(0)$ from local SPARC calibration and $E(z)$ from standard cosmology.

**Corollaries.** The five exponents of $E(z)$ in Table 6 govern the BTFR normalization, the MOND transition radius, the asymptotic flat velocity at fixed baryonic mass, the lensing-inferred dynamical-mass enhancement, and the free-fall collapse-time speedup. Each is mass-independent and aperture-independent (where applicable) in the deep-MOND regime, and follows from the §3 input with no further free parameter beyond the $z = 0$ calibration of $a_0(0)$.

**Falsification.** Any single measurement at $\geq 2\sigma$ from a Table 7 row, after the named systematic is controlled, falsifies the statement. The Euclid DR1 measurement of stacked galaxy-galaxy lensing at $z = 0.5\text{–}2$ is the sharpest single test, with mass- and aperture-stratified analysis simultaneously testing the magnitude and the universality of the prediction.

One relation. Five distinct observable channels. No further free parameters beyond the $z = 0$ SPARC calibration of $a_0(0)$. The framework's evolution claim stands or falls on the next two years of intermediate-redshift kinematic and lensing data.

## 10. Conclusions

The Milgrom acceleration scale $a_0 \approx c\,H_0$ has stood for four decades as a numerical coincidence with no derivation. Mode Identity Theory's measurement postulate $A/A_P = C(\Theta) \cdot N^n$, with $N \equiv (\sqrt{\Omega})^{-1}$ the hierarchy normalization fixed by calibrating one observable per manifold-mode class, resolves the coincidence into a fixed topological ratio of two phase-operator values at Fibonacci wells on the 120-domain of $S^3/2I$, with $a_0$ and $H$ both edge-mode observables ($n = 1$) sharing the same edge-mode normalization $N_H$. The §2 derivation matches observation at the 0.8% level, with the match unique within the framework's selected Fibonacci-well subset of the 120-domain.

The local-epoch reading of the postulate then yields the evolution: at every cosmic epoch $z$, the same scaling rule with the same wells references the local horizon $\Omega_H(z)$, giving $a_0(z) = a_0(0)\,E(z)$. Five distinct observables follow from this single relation as different powers of $E(z)$: the BTFR normalization shifts as $E(z)^{-1}$, the MOND transition radius contracts as $E(z)^{-1/2}$, the asymptotic flat velocity at fixed baryonic mass rises as $E(z)^{+1/4}$, the lensing-inferred dynamical mass enhancement scales as $E(z)^{+1/2}$, and the gravitational free-fall collapse time shortens as $E(z)^{-1/4}$. The five exponents are not independent; they are correlated translations of one input. A measurement in any one channel tests the value of $E(z)$ via that channel; verifying consistency across multiple channels at the same redshift tests the universality of the deep-MOND scaling across observable classes.

The framework's $a_0(z) \propto E(z)$ relation lives in a constraint landscape that includes one live tension (the KMOS3D BTFR trend shape from Übler et al. 2017 [9], currently the only quantitative test of any §§4-6 prediction at intermediate redshift; a forward-modeled simulation of the Übler radial pressure-support pipeline applied to mock framework-true galaxies does not reproduce the observed non-monotonic offset, so the tension is genuine and not a velocity-correction artifact), one inherited and unaddressed problem (the cluster-scale MOND mass discrepancy at $z \lesssim 0.3$, where the framework's evolution correction is at the percent level against a factor-five problem), and one structurally resolved apparent tension (the CMB at recombination, where the framework's selection rule assigns cosmological perturbations to a different manifold-mode sector than $a_0$ and the resulting CMB prediction coincides with ΛCDM's at every Planck-measured observable). The remaining constraints are consistencies by construction or below current sensitivity. None of the resolved or inherited constraints alters the §§3-6 predictions in the redshift window where the present paper makes testable claims; the Übler tension is acknowledged and held against the framework's explicit prediction without retreat. Resolution comes from Euclid DR1 single-instrument matched-tracer kinematics and JWST follow-up samples at the original Übler redshifts, both arriving on a two-year horizon.

A companion analysis on the surface sector (separately submitted) makes the structurally inverse prediction: Λ remains constant at every epoch, and the apparent dark-energy equation-of-state evolution reported by DESI DR2 [8] arises as a template artifact from the observer's phase position on the underlying cosmic standing wave. The two predictions follow from the same scaling law but reference different $(n, \Omega)$ sectors, and they are testable through disjoint instrument suites. Their joint outcome tests the framework's selection rule itself, with four enumerated outcomes carrying different evidentiary weight (§8.2).

The Euclid DR1 release (October 2026) will deliver the sharpest near-term test: a stacked galaxy-galaxy lensing measurement at $z = 0.5\text{–}2$ stratified by baryonic mass and aperture, simultaneously testing the magnitude (the predicted 15% to 74% enhancement of $M_\text{dyn}/M_b$) and the universality (mass- and aperture-independence) of the §6 prediction. The matched-systematics intermediate-redshift Tully-Fisher re-analysis and the JWST/NIRSpec spectroscopic confirmation of impossible Labbé candidates will follow on a similar timescale. All three programs are existing or imminent; no new instrument or observational capability is required.

The framework's evolution claim therefore stands or falls on a defined, near-term measurement window. One relation, calibrated at $z = 0$ from local SPARC dynamics, generates five testable predictions across cosmic time. The framework's posture is the gauge-theory posture: state the rule, derive its consequences, and accept the data. This paper and its predictions are registered on Zenodo prior to the Euclid DR1 release in October 2026; the framework's status will be settled by that data.

---

## Acknowledgments

The author thanks the observational teams whose published data made this work possible: the SPARC collaboration (Lelli, McGaugh, Schombert) for the local rotation-curve sample [2,18]; Übler and the KMOS3D team for the intermediate-redshift Tully-Fisher measurements [9]; Wisnioski and the KMOS3D team for the kinematic-dispersion data used in the §7.2 forward model [11]; Genzel and the SINS/zC-SINF team for the high-redshift rotation curves [10]; Pointecouteau and Silk for the X-ray cluster analysis [12]; the JWST observing teams and the Labbé group for the early-galaxy catalog [6]; the Planck collaboration for the cosmological parameters and CMB amplitudes [20]; and the DESI collaboration for the dark-energy survey results [8]. No external funding supported this work.

## Data availability

All numerical predictions and tabulated framework outputs are deposited on Zenodo prior to the Euclid DR1 release in October 2026. In order of first appearance in the text, the deposit includes the combinatorial baseline table (supporting §2.5); the §§3-6 prediction tables (Tables 1-4) in CSV format; the ΛCDM lensing discriminator overlay (NFW enclosed-mass curves at the canonical archetypes, supporting §6.2 and Appendix B); the Übler σ-tension table (supporting §7.2); the CMB leakage-bound table (supporting §7.5); and the Labbé candidate speedup factors (supporting §7.7). Source code for the analysis pipelines and figure-generation scripts is included.

---

## Appendix A: 120-domain, Fibonacci wells, and well assignments

The §2.1 body presents the bounded topology, the phase operator $C(\Theta)$, the scaling law, and the selection rule inline. This appendix supplies the supporting structure: the binary-icosahedral quotient that produces the 120-domain (A.1), the Fibonacci-well selection on the 120-domain (A.2), and the eligibility conditions that locate $a_0$, $H_0$, and $\Lambda$ at their respective well positions (A.3).

### A.1 The 120-domain

The physical observable space is the quotient $S^3/2I$, where $2I$ is the binary icosahedral group. The discrete subgroups of $\text{SU}(2) \cong S^3$ are classified: cyclic groups, binary dihedral groups, and three exceptional groups (binary tetrahedral $|2T| = 24$, binary octahedral $|2O| = 48$, binary icosahedral $|2I| = 120$). Two convergent constraints select $2I$. (i) It is the largest exceptional discrete subgroup of $\text{SU}(2)$, giving the maximum spectral resolution compatible with $S^3$. (ii) The icosahedron is the unique Platonic solid whose $(2,3,5)$ branch orders are consecutive Fibonacci numbers satisfying $2 + 3 = 5$; this Fibonacci-recurrence structure is what makes the Fibonacci wells (A.2) the natural stable positions on the resulting 120-domain. The phase position is therefore quantized:

$$\Theta \in \{k/120 : k = 0, 1, \ldots, 119\}.$$

For photon-mediated observables, the bosonic projection $|\psi|^2$ erases the anti-periodic sign and halves the resolution to a 60-position grid (even numerators only).

### A.2 The Fibonacci wells

Phase positions on the 120-domain that maximize stability against environmental perturbation form the framework's *Fibonacci wells*. The selection follows from two converging structures: (i) Hurwitz's theorem, which states that the golden ratio $\varphi$ is the irrational number hardest to approximate by rational fractions of bounded denominator, so positions $k/120$ with $k$ a Fibonacci number minimize destructive interference between modes; (ii) the icosahedral $(2,3,5)$ Fibonacci-recurrence noted in A.1, which makes the Fibonacci numbers the natural lattice of stable positions on the 120-domain native to $S^3/2I$. The wells used in this paper are

$$\Theta_\text{wells} \in \{13, 21, 34, 55\}/120,$$

corresponding to Fibonacci numbers $F_7$ through $F_{10}$. The lower bound $F_7 = 13$ is the noise-floor condition: $F_n$ for $n < 7$ produces amplitude indistinguishable from neighboring 120-domain positions. The upper bound $F_{10} = 55$ is set by the symmetry $C(k/120) = C((120-k)/120)$, which makes $F_{11} = 89$ equivalent to $F_8 = 21$. A separate special position is the antinode at $\Theta = 60/120$, where $C(\Theta)$ takes its maximum value and the slope $d\ln C/d\Theta = 0$, providing topological protection against environmental shifts.

### A.3 Well assignments for the present paper

Three framework-internal eligibility conditions identify which Fibonacci wells are consistent with each observable's measurement class:

1. **Manifold index** separates edge modes ($n = 1$, epoch-dependent: $H_0$, $a_0$) from surface modes ($n = 2$, epoch-independent: $\Lambda$).
2. **Bosonic projection**: photon-mediated observables access only the 60-grid (even numerators in the 120-domain); dynamical observables access the full 120-grid.
3. **Antinode requirement for $\Lambda$**: as a topologically protected eigenvalue, $\Lambda$ sits at the antinode position $60/120$ where $d\ln C/d\Theta = 0$.

Under these conditions, the empirical calibrations to $a_0$, $H_0$, and $\Lambda$ at $z = 0$ resolve as follows. (a) The well calibrated to $a_0$ is $13/120$, the unique coprime position ($\gcd(13, 120) = 1$) consistent with the irreducibility condition that dynamical (non-photon-mediated) observables access the full 120-grid. (b) The well calibrated to $\Lambda$ is $60/120$, consistent with the ground-state maximality condition for a topologically protected eigenvalue. (c) The well calibrated to $H_0$ is $34/120$: among the Fibonacci wells $\{13, 21, 34, 55\}/120$ available to edge-mode observables, $34/120$ is the unique even-numerator option consistent with the bosonic-filter condition for photon-mediated observation. The wells $21/120$ and $55/120$ remain unassigned in this paper.

The eligibility conditions (1)-(3) above are not introduced ad hoc to land the present calibration: they are pre-registered framework structure from the foundational MIT deposit [36], in which the manifold mode-index classification ($n = 1, 2, 3$) and the bosonic filter (the $|\psi|^2$ projection from the binary-icosahedral 120-domain to the icosahedral 60-grid for photon-mediated observation) are stated as derivations from the topology postulate $S^1 = \partial(\text{Möbius}) \hookrightarrow S^3$ and the anti-periodic boundary condition, prior to the present $a_0/H_0/\Lambda$ calibration. The antinode condition for $\Lambda$ is structural: $\Theta = 60/120$ is the location where $C(\Theta)$ takes its maximum and $d\ln C/d\Theta = 0$. Under conditions (1)-(3), each observable has exactly one valid Fibonacci well: $a_0$ is forced to $13/120$ (the unique coprime member, satisfying the dynamical-observable condition), $H_0$ to $34/120$ (the unique even-numerator member, satisfying the bosonic-filter condition for photon-mediated observation), and $\Lambda$ to $60/120$ (the antinode). The look-elsewhere effect on the well assignment is therefore zero given the pre-registered eligibility conditions; the §2.5 combinatorial sparsity argument quantifies the Milgrom-ratio match strength against this constrained search space rather than against the unconstrained 120-domain.

These assignments have the status of empirical calibrations at $z = 0$ that land on positions compatible with the framework's eligibility conditions; they are not first-principles derivations of the well positions. The combinatorial test in §2.5 quantifies the strength of the match: among the ten unordered Fibonacci-well pairs in $\{13, 21, 34, 55, 60\}/120$, only $(13, 34)$ reproduces the observed Milgrom ratio $a_0/(cH_0)$ within 1%, providing a sparsity check on the calibrated assignment. A first-principles derivation of the well positions from the Hurwitz/Fibonacci structure of the 120-domain is future work; until then, the assignments have the status of two parameters fitting two measurements at $z = 0$ as documented in §2.9. Other framework realizations of the scaling law at additional $(n, \Omega)$ pairs are outside the scope of the present paper.

---

## Appendix B: ΛCDM comparison methodology for §6.2

§6.2 compares the framework's $\sqrt{E(z)}$ enhancement of $M_\text{dyn}/M_b$ against a ΛCDM baseline that evolves with redshift through halo-concentration evolution and stellar-to-halo-mass relation (SHMR) shifts. This appendix specifies the parameterization used.

**Galaxy archetypes.** Four baryonic-mass anchors spanning the SPARC range:

| Archetype | $M_b$ [$M_\odot$] |
|---|---:|
| Dwarf | $3.5 \times 10^8$ |
| Sub-$L^*$ | $1.0 \times 10^{10}$ |
| $L^*$ | $6.0 \times 10^{10}$ |
| Giant | $1.5 \times 10^{11}$ |

**Halo masses and concentrations.** Representative values consistent with Moster-style SHMR calibration [17] and Duffy-style concentration evolution [15], at the $L^*$ archetype:

| $z$ | $M_\text{halo}$ [$M_\odot$] | $c$ |
|---:|---:|---:|
| 0 | $1.5 \times 10^{12}$ | 7.5 |
| 1 | $1.0 \times 10^{12}$ | 5.0 |
| 2 | $7.0 \times 10^{11}$ | 3.5 |

Sub-$L^*$ and Giant archetypes use archetype-appropriate $(M_\text{halo}, c)$ values from the same parameterization. The values are representative defaults rather than freshly inverted SHMR fits at each redshift; alternative literal Moster 2013 inversions shift the absolute ΛCDM curve values but preserve the qualitative mass- and aperture-dependence that constitutes the §6.2 discriminator.

**NFW enclosed mass.** The dynamical mass at fixed physical aperture $R$ is

$$M_\text{dyn}(R, z) = M_\text{NFW}(R; M_\text{halo}, c, z) + M_b,$$

with

$$M_\text{NFW}(R) = M_\text{halo} \cdot \frac{\ln(1 + R/r_s) - (R/r_s)/(1 + R/r_s)}{\ln(1 + c) - c/(1 + c)},$$

scale radius $r_s = R_\text{vir}/c$, and virial radius defined under the $R_{200}$ convention:

$$R_\text{vir}^3 = \frac{3 M_\text{halo}}{4\pi \cdot 200 \cdot \rho_\text{crit}(0)\, E(z)^2}.$$

The inferred ratio $M_\text{dyn}/M_b$ is computed under the same Newtonian inversion (6.1) used by the framework prediction.

**Cosmology.** Planck 2018 [20] parameters: $\rho_\text{crit}(0) = 8.55 \times 10^{-27}$ kg/m³, $\Omega_m = 0.315$, $\Omega_\Lambda = 0.685$, $H_0 = 67.4$ km/s/Mpc.

The dataset and per-aperture comparison are deposited as `tables/table4.csv` and `figures/figure5.pdf` in the a0z analysis-pipeline repository (https://github.com/dmobius3/a0z).

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

[21] J. D. Bekenstein, Phys. Rev. D 70, 083509 (2004).

[22] M. Milgrom, Phys. Rev. D 80, 123536 (2009).

[23] C. Skordis and T. Złośnik, Phys. Rev. Lett. 127, 161302 (2021); Phys. Rev. D 104, 104046 (2021).

[24] J. W. Moffat, J. Cosmol. Astropart. Phys. 03, 004 (2006).

[25] T. G. Zlosnik, P. G. Ferreira, and G. D. Starkman, Phys. Rev. D 75, 044017 (2007).

[26] R. P. Naidu et al., Astrophys. J. Lett. 940, L14 (2022).

[27] D. Brout et al., Astrophys. J. 938, 110 (2022).

[28] DES Collaboration, Astrophys. J. Lett. 973, L14 (2024).

[29] M. Milgrom, Scholarpedia 9(6), 31410 (2014).

[30] H. S. Zhao and B. Famaey, Phys. Rev. D 86, 067301 (2012).

[31] Euclid Collaboration: Y. Mellier et al., arXiv:2405.13491 (2024).

[32] M. Kriek et al., Astrophys. J. Suppl. Ser. 218, 15 (2015).

[33] A. M. Tiley et al., Mon. Not. R. Astron. Soc. 506, 323 (2021).

[34] M. Millon et al., Astron. Astrophys. 639, A101 (2020).

[35] K. C. Wong et al., Mon. Not. R. Astron. Soc. 498, 1420 (2020).

[36] B. Shatto, Mode Identity Theory: Modal Realization from Nested Topology (2025). DOI:10.5281/zenodo.18064856.

---

/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`working`](../)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
