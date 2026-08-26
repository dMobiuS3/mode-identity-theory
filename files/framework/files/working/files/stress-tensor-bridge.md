/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Stress-Tensor Bridge

**Status:** OPEN, program page. Nothing on this page is derived yet. It fixes the object, assembles the constraints any candidate must clear (all already in the corpus, gathered here for the first time), enumerates the candidate routes, and freezes two pilot checks before either is run. The object keeps its ledger name: $`E(S)`$, the amplitude-to-$`T_{\mu\nu}`$ dictionary. This page is its canonical program home; the [claim ledger](claim-ledger.md) keeps the count (one object, counted once), and the [Budget Map](budget-map.md) keeps the inventory role.

**Dependencies:** [cosmological constant](../../../../cosmos/files/cosmological-constant.md) §IV (the coefficient gate), [The Budget Map](budget-map.md) (the $`E(S)`$ consolidation), [Friedmann as Output](friedmann-as-output.md) (the mechanism fence), [Temporal Budget](temporal-budget.md) (the fitted dictionary this must not break), [Redshift and Cooling](redshift-and-cooling.md) §VI and [Entropy as Realization Budget](entropy-as-realization-budget.md) §VIII.2 (the energy accounting), [first-eigenvalue](../../bedrock/files/first-eigenvalue.md) (the seed).

**Related:** the OpenWave M8 program's field-dynamics half is the same gap approached from the particle side (external; no Lagrangian survey is run on this page).

---

## I. The object

One map. Input: the framework's realized state, the budget variable $`S`$ and the standing-wave amplitudes the corpus already carries. Output: a stress tensor $`T_{\mu\nu}`$, together with a declared **placement**: a statement of which metric's Einstein equations it sources. The placement is part of the object, not a detail; §III is where it forks.

The same missing map currently carries four names in four places, and their consumers are different, which is why closing it pays four debts at once:

| Where | Name there | What that consumer needs from the map |
|---|---|---|
| [cosmological constant](../../../../cosmos/files/cosmological-constant.md) §IV | the stress tensor gating the Λ coefficient | decides whether $`\Lambda_\text{physical} = 3/R^2`$, the vacuum-reference value, survives contact with the domain's actual content |
| [claim ledger](claim-ledger.md) open problems | $`E(S)`$, the amplitude-to-$`T_{\mu\nu}`$ dictionary | the load-bearing open; the Ψ²→S² transfer needs a counterparty |
| [Friedmann as Output](friedmann-as-output.md) | the one dynamical import | the matter-scaling side of $`H(z)`$ currently borrows GR; a native source would let form be output |
| [Redshift and Cooling](redshift-and-cooling.md) §VI, [entropy](entropy-as-realization-budget.md) §VIII.2 | the cooling-energy accounting | where the phase-sampled photon energy goes |

Four names, one hole. A single theorem-shaped result discharges all four, and a single failure mode contaminates all four, which is why the constraints below are collected before any construction is attempted.

---

## II. The constraint set, already in hand

Every row below is established elsewhere in the corpus or was verified this cycle; nothing here is new. A candidate map that violates a row is dead on that row, not negotiable against the others.

| # | Constraint | Statement | Source |
|---|---|---|---|
| C1 | Static source | If the placement is the physical static metric with Einstein's equations unchanged, then $`G_{\mu\nu}`$ is time-independent, so $`T_{\mu\nu}`$ must be too. Instantaneously, not on average. | GR, given the static postulate |
| C2 | The coefficient gate | For a homogeneous isotropic perfect fluid on the static closed domain, $`\Lambda R^2 = (\rho+3p)/(\rho+p)`$. Given $`\rho + p > 0`$ (required for a real closed radius), the value 3 is attained exactly when $`\rho = 0`$, $`p > 0`$: a pure-pressure source, which violates the dominant energy condition. Dust gives 1, radiation 3/2. Outside the perfect-fluid class the question is open, and that is this page's question. | [cosmological constant](../../../../cosmos/files/cosmological-constant.md) §IV |
| C3 | The mechanism fence | The success bar of [Friedmann as Output](friedmann-as-output.md) admits GR only in the comparison to Friedmann form, never as the mechanism. Supplying a $`\rho(S)`$ and then using $`H^2 \propto \rho`$ to obtain $`H(S)`$ fails that bar regardless of where $`\rho(S)`$ came from. The bridge must respect this: a derived source is not the same as a derived evolution. | [claim ledger](claim-ledger.md), Friedmann tracker |
| C4 | The Killing ledger | A static metric carries a timelike Killing field, so total energy is exactly conserved in the physical description. This is sharper than ΛCDM, where the time-dependent metric makes energy non-conservation routine. The one pilot computation on record found no rising conserved counterparty for the realized side; a candidate map must either exhibit the counterparty or show why the Killing charge is not the right ledger. | [Budget Map](budget-map.md), Killing-charge pilot (recorded negative) |
| C5 | The fitted dictionary | The D+Λ phenomenology on SN+BAO, with $`\Omega_\Lambda = 0.685`$ held as the fiducial anchor, already sits essentially on ΛCDM. A derived source must reproduce that dictionary's constant term and matter-like term, or improve on them; it may not quietly break a fit the framework already owns. | [Temporal Budget](temporal-budget.md) |
| C6 | The coincidence fences | Any 3/2 or $`2/R^2`$ that surfaces in a candidate must clear the standing fences (the two-3/2s fence, the curvature-coincidence fence) before it counts. No new numerology enters through this page. | [Friedmann as Output](friedmann-as-output.md) discipline |

**A structural observation, recorded as a hint and not a result.** With $`\Psi = \cos(t/2)`$ and $`S = \sin(t/2)`$ the budget identity is the harmonic energy identity: $`\dot\Psi = -S/2`$, so

```math
4\dot\Psi^2 + \Psi^2 = S^2 + \Psi^2 = 1.
```

A quadratic energy density of the standing wave is time-independent even though each share oscillates. So C1's staticity is natural for the energy density of any quadratic reading of the wave. It is not automatic for the pressure, which for a scalar reading is kinetic minus potential and oscillates with zero mean. Whether the physical $`T_{\mu\nu}`$ is such a quadratic reading is exactly the open dictionary; this observation constrains candidates, it does not select one.

---

## III. The placement fork

Three branches, mutually exclusive, each a legitimate outcome. The corpus is currently implicit on which branch it occupies; the translation-layer language of the budget pages leans (b) without saying so. Deciding the branch is part of closing the bridge, and each branch has stated consequences.

| Branch | Statement | What it requires | What it does downstream |
|---|---|---|---|
| (a) physical-static sourcing | Einstein's equations hold on the static physical metric with the mode content as source | a static $`T_{\mu\nu}`$ that is effectively vacuum: in the perfect-fluid class, $`\rho = 0`$, $`p > 0`$ (C2), or a principled exit from that class | if achieved, $`\Lambda_\text{physical} = 3/R^2`$ closes as identified; if the derived source is matter-like, the coefficient shifts and branch (c) is entered honestly |
| (b) effective-metric sourcing | Einstein's equations govern the effective metric $`g_\text{eff}(S)`$ of the distance-redshift dictionary; the static domain is substrate and is not required to solve them with matter | deriving the map $`g_\text{static} \to g_\text{eff}`$ and the source it implies, rather than assuming the FLRW form; C3 bars reading the answer off Friedmann | "Einstein imported unchanged" must be restated to name which metric; the Λ page's Stage 2 becomes the dictionary's normalization, which is what it already says |
| (c) shifted coefficient | The physical constant is not $`3/R^2`$; the vacuum-reference value is a reference only | owning the shift publicly: the Λ page §IV, the ledger gate row, and the MODELS.md Λ cell all update | the pre-registered Euclid falsifier $`\Lambda_\text{obs} R_\text{ind}^2 = 3`$ is then a test of the reference reading, and the framework must say what it predicts instead |

Branch (c) is a scientific outcome, not a defeat. This page exists to decide the branch, not to defend the number 3.

---

## IV. Candidate routes

The working table proper. Status vocabulary: OPEN (not yet attempted), PILOT-FROZEN (specified in §V, not yet run), DIAGNOSTIC (informative, cannot count as derivation), NEGATIVE (attempted, recorded), SPECULATIVE (no principled construction yet).

| Route | Construction | Branch served | Must clear | Status |
|---|---|---|---|---|
| R1 minimal scalar reading | Compute $`T_{\mu\nu}`$ of the standing wave read as a homogeneous scalar on the static $`S^3`$, quadratic density per §II | (a) | C1 instantaneously, then C2 | PILOT-FROZEN (P1) |
| R2 reverse diagnostic | Compute the $`T_\text{eff}`$ that makes $`g_\text{eff}(S)`$ Einstein, and compare its decomposition against the budget's fitted terms | (b) | C3: this READS the answer, so it can only locate the target, never derive it | PILOT-FROZEN (P2), DIAGNOSTIC |
| R3 ALE-filling kinship | The postulate-bridge Tier-3 gravitational filling, a dictionary of the same general type for a different field | (a) or (b) | its own fence: formal kinship until an identity is shown | OPEN, fenced |
| R4 Killing counterparty | Identify the conserved charge that balances the realized side | any | C4; one computation found no rising counterparty | NEGATIVE (recorded), revisit only through a candidate map |
| R5 boundary or pure-pressure source | A principled origin for $`\rho = 0`$, $`p > 0`$ content (edge tension, Casimir-type reading of the Möbius boundary) | (a), preserving 3 | C2's DEC violation must be earned by a construction, not asserted to save the coefficient | SPECULATIVE |

The naive expectation for R1 is stated now so it cannot be adjusted later: an oscillating quadratic scalar time-averages to dust, which under branch (a) gives coefficient 1, not 3, and its instantaneous pressure is not static, failing C1 before C2 is even reached. R1's value is calibrating the machinery and making "the mode content is not a minimally-read scalar field" a computed statement rather than a suspicion. If R1 surprises, that is worth knowing before anything heavier is built.

---

## V. Pilot checks, frozen before running

Both pilots are NON-EVIDENTIARY. Definitions are frozen in this commit; computations land in a later commit, per the tick-lemma pattern. Each check states in advance what would count as pass, fail, and surprise, so it is able to fail.

**P1, the minimal scalar reading (R1).** Metric: static round $`S^3(R)`$ with time, $`ds^2 = -dt^2 + R^2 d\Omega_3^2`$. Field: homogeneous $`\Psi(t) = \cos(\omega t)`$ with the budget normalization ($`\omega`$ matched to the Waltz phase so that $`S = \sin(\omega t)`$), quadratic density and pressure of the minimally coupled scalar. Outputs, each reported: $`\rho(t)`$, $`p(t)`$, the staticity residual $`\max_t \lvert p(t) - \bar p \rvert / \rho`$, the time-averaged $`w`$, and the coefficient $`\Lambda R^2`$ the static balance would assign to the averaged source. Expectations, registered: $`\rho`$ constant; $`p`$ oscillating with zero mean; averaged $`w = 0`$ (dust); assigned coefficient 1; staticity residual order unity. Surprise: any of those failing to hold.

**P2, the reverse diagnostic (R2).** Take $`g_\text{eff}`$ as the closed FLRW form with the budget's effective scale factor $`a_\text{eff} \propto S`$ in the distance-redshift dictionary. Compute $`G_{\mu\nu}[g_\text{eff}]`$ and read off the $`(\rho_\text{eff}(S), p_\text{eff}(S))`$ that Einstein's equations would require. Report their decomposition against the constant term and the matter-like term the fitted dictionary already carries. This is explicitly DIAGNOSTIC: it locates what a branch-(b) derivation must produce; producing it from the postulate side remains the open work, and C3 bars promoting this readout to a derivation.

---

## VI. Success and failure, stated in advance

Success is one map, stated once, that: (i) declares its branch; (ii) passes that branch's consistency row (C1 and C2 on (a), the derived $`g_\text{static} \to g_\text{eff}`$ map on (b)); (iii) exhibits the Killing counterparty or dissolves C4 with an argument; (iv) decides the Λ coefficient, in either direction; and (v) leaves the fitted dictionary of C5 intact or improved, with the comparison shown.

Failure is also an outcome worth recording, per route: R1 failing on its registered expectations is the expected result and still gets written down; R5 never finding a principled construction closes branch (a)'s coefficient-preserving arm; and if every route dies, the honest terminus is the Friedmann tracker's own alternative ending, "kinematics native, one dynamical import," now extended with "and the Λ coefficient rests on the vacuum reference."

What would falsify the whole program's premise rather than a route: a demonstration that no static-metric stress tensor and no $`g_\text{static} \to g_\text{eff}`$ map can reproduce the fitted dictionary at C5's level. That would be a result about the static architecture itself and would belong on the framework page, not here.

---

## VII. What this page is not

Not a Lagrangian survey: that is the OpenWave M8 program's half, run under its own pre-registration discipline, and results cross between the two by citation, not by restatement. Not a rename: the object is the ledger's $`E(S)`$ and keeps that name and count. Not a license to import Friedmann as mechanism: C3 stands. And not evidence: nothing on this page has been run, and the two pilots are frozen precisely so that when they do run, their outcomes mean something.

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
