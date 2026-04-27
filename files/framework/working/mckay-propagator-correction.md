/ **[`main`](../../../)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# McKay Propagator Correction to the Fermion Mass Formula

**Status:** OPEN. Priority A.
**Dependencies:** Fermion mass formula (engine file), C_geom and torsion tables, Coxeter-Galois gate, McKay graph for binary icosahedral group.

---

## 1. The Problem

The fermion mass formula systematically overshoots at high McKay distance.

$$m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot (\sqrt{\Omega_\Lambda})^{\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)$$

Current scorecard: 10/12 SM fermions within ×3. The two misses both sit at high McKay distance:

| Fermion | Irrep | Vacuum | dist | Predicted (GeV) | Observed (GeV) | Ratio |
|---|---|---|---|---|---|---|
| Down quark | R8 | gal | 5 | 1.51 × 10⁻² | 4.67 × 10⁻³ | 3.22 |
| Top quark | R2 | triv | 7 | 44.54 | 172.7 | 3.88 |

Initial assessment: overshoot grows with McKay distance. But detailed examination reveals the correction is **not purely distance-dependent**. At the same distance, some vacua hit while others miss.

### 1.1 Full Residual Table (SM-assigned entries)

| Fermion | Irrep | Vacuum | dist | Predicted/Observed | Notes |
|---|---|---|---|---|---|
| electron | R7 | triv | 4 | 1.02 | hit |
| up | R8 | triv | 5 | 1.06 | hit |
| muon | R8 | std | 5 | 1.02 | hit |
| **down** | **R8** | **gal** | **5** | **3.22** | **miss: same irrep, same dist as up and muon** |
| tau | R4 | std | 6 | 2.42 | moderate miss |
| bottom (best) | R2 | gal | 7 | 1.28 | hit |
| **top** | **R2** | **triv** | **7** | **3.88** | **miss: same irrep, same dist as bottom** |

**Key finding:** At dist = 5, triv and std hit within 6%. Gal misses by ×3.2. At dist = 7, gal hits within 28%. Triv misses by ×3.9. The correction is not a function of distance alone. It interacts with the vacuum label.

---

## 2. The Hypothesis (Revised)

The correction is vacuum-dependent and concentrated at the branch point of the McKay graph.

### 2.1 Original Hypothesis (Superseded)

The McKay graph is the actual structure through which modes propagate. Each intermediate node along the path from R0 to the target irrep contributes a cumulative correction. The current formula treats the elevator as a single exponential step. The correction accounts for what happens at each floor the elevator passes through.

This hypothesis predicted a correction monotonic in distance. The data rules this out: at the same distance, different vacua produce different residuals. The correction must be vacuum-dependent.

### 2.2 Revised Hypothesis

The Galois vacuum has a 9× enhanced gap (first allowed k = 5 vs k = 1 for triv and std). At low McKay distance, this enhancement is invisible because the elevator hasn't climbed far enough for the accumulated difference to manifest. At high distance, the Galois vacuum's different spectral structure produces a measurable deviation.

**The pattern:**

| dist | Vacuum that misses | Vacuum(s) that hit | Galois gap relevance |
|---|---|---|---|
| 5 (R8) | gal (×3.2) | triv (×1.06), std (×1.02) | Galois enhanced gap accumulates over 5 steps |
| 7 (R2) | triv (×3.9) | gal (×1.28), std (×1.51) | At dist 7, the path passes through R5 (Galois-fixed irrep); triv is now the outlier |

The reversal at dist 7 (gal hits, triv misses) is the strongest constraint. A pure "Galois penalty" would predict gal always misses. Instead, the miss swaps vacuum at the branch point. This points to the branch structure itself as the source.

### 2.3 The Branch Point at R8

```
R0(1) --- R1(2) --- R3(3) --- R6(4) --- R7(5) --- R8(6) --- R5(4) --- R2(2)
                                                       |
                                                      R4(3)
```

R8 is the fork. R4 and R5 branch off in different directions. The path to R2 goes through R5 (which is Galois-fixed: R5 maps to itself under Galois conjugation). The path to R4 branches directly from R8.

R5 and R4 are the only irreps reached through a fork rather than a straight chain. The single-path approximation may break down precisely here, because the mode "sees" two possible exits at R8 and the branching ratio depends on the vacuum.

### 2.4 Lattice Propagator Analogy (Updated)

On a lattice graph, propagators pick up vertex corrections at each node traversed. At a branch point, the propagator splits. The relative weight of each branch depends on the coupling structure at the node, which in MIT is vacuum-dependent through T²(ρ ⊗ σ).

The correction should be:

- Multiplicative (each node contributes a factor)
- Vacuum-dependent (torsion varies with σ at each intermediate node)
- Sensitive to branching (different behavior at the R8 fork)
- Computable from existing data (C_geom and torsion values are known for all nodes and all vacua)

### 2.5 The McKay Graph (SPECTRUM Convention)

```
R0(1) --- R1(2) --- R3(3) --- R6(4) --- R7(5) --- R8(6) --- R5(4) --- R2(2)
                                                       |
                                                      R4(3)
```

Unique shortest paths from R0:

| Target | Path | dist | Intermediate nodes |
|---|---|---|---|
| R0 | — | 0 | none |
| R1 | R0→R1 | 1 | none |
| R3 | R0→R1→R3 | 2 | R1 |
| R6 | R0→R1→R3→R6 | 3 | R1, R3 |
| R7 | R0→R1→R3→R6→R7 | 4 | R1, R3, R6 |
| R8 | R0→R1→R3→R6→R7→R8 | 5 | R1, R3, R6, R7 |
| R5 | R0→R1→R3→R6→R7→R8→R5 | 6 | R1, R3, R6, R7, R8 |
| R4 | R0→R1→R3→R6→R7→R8→R4 | 6 | R1, R3, R6, R7, R8 |
| R2 | R0→R1→R3→R6→R7→R8→R5→R2 | 7 | R1, R3, R6, R7, R8, R5 |

Note: R4 branches from R8, not from R5. Both R4 and R5 are at dist = 6 but take different paths from R8.

---

## 3. C_geom Values Along Each Path

| Irrep | dim | Spin | D | C_geom |
|---|---|---|---|---|
| R0 | 1 | Int | 60 | — (trivial, no Kostant exponents) |
| R1 | 2 | Half | 120 | 0.0988 |
| R3 | 3 | Int | 60 | 0.5553 |
| R6 | 4 | Half | 120 | 0.2098 |
| R7 | 5 | Int | 60 | 0.7564 |
| R8 | 6 | Half | 120 | 0.2382 |
| R5 | 4 | Int | 60 | 0.8017 |
| R4 | 3 | Int | 60 | 0.7970 |
| R2 | 2 | Half | 120 | 0.2436 |

---

## 4. Candidate Correction Forms

### 4.1 Product of Intermediate C_geom (ELIMINATED)

The simplest candidate: multiply C_geom of each intermediate node along the path.

$$\Pi(\rho) = \prod_{i \in \text{path}(R0 \to \rho)} C_{\text{geom}}(i)$$

| Target | Intermediate nodes | Π |
|---|---|---|
| R1 | none | 1 |
| R3 | R1 | 0.0988 |
| R6 | R1, R3 | 0.0988 × 0.5553 = 0.0549 |
| R7 | R1, R3, R6 | 0.0549 × 0.2098 = 0.01152 |
| R8 | R1, R3, R6, R7 | 0.01152 × 0.7564 = 0.00871 |
| R5 | R1, R3, R6, R7, R8 | 0.00871 × 0.2382 = 0.00207 |
| R4 | R1, R3, R6, R7, R8 | 0.00871 × 0.2382 = 0.00207 |
| R2 | R1, R3, R6, R7, R8, R5 | 0.00207 × 0.8017 = 0.00166 |

Problem: Π drops fast with distance. If this enters as a direct multiplicative correction, it would crush high-distance masses rather than correct an overshoot. The correction needs to go in the right direction.

### 4.2 Inverse Product (Denominator Correction, ELIMINATED)

If the propagator correction appears in the denominator:

$$m_{\text{corrected}} = \frac{m_{\text{current}}}{\Pi(\rho)^{p}}$$

For some power p. This would increase high-distance masses, which is the wrong direction (the formula already overshoots).

### 4.3 Ratio or Logarithmic Form

Perhaps the correction is logarithmic:

$$\delta(\rho) = \sum_{i \in \text{path}} \ln C_{\text{geom}}(i)$$

| Target | δ |
|---|---|
| R1 | 0 |
| R3 | -2.315 |
| R6 | -5.222 |
| R7 | -4.945 |
| R8 | -6.373 |
| R5 | -7.800 |
| R4 | -7.800 |
| R2 | -8.021 |

Note: δ is monotonically decreasing (more negative) with distance, except R7 which is slightly less negative than R6 due to R6's low C_geom. The pattern is approximately linear in distance.

### 4.4 Normalized Path Correction

Perhaps what matters is the ratio of the target's C_geom to the geometric mean of the intermediate C_geom values:

$$\kappa(\rho) = \frac{C_{\text{geom}}(\rho)}{\left(\prod_{i \in \text{path}} C_{\text{geom}}(i)\right)^{1/\text{dist}}}$$

This normalizes the correction per step. Compute and check if κ correlates with the mass residual.

### 4.5 Torsion Along the Path (NOW PRIMARY CANDIDATE)

The correction involves torsion at each intermediate node, making it vacuum-dependent:

$$\Pi_T(\rho, \sigma) = \prod_{i \in \text{path}} T^2(i \otimes \sigma)$$

This is now the primary candidate because:

1. The residual pattern is vacuum-dependent (same dist, different vacua, different misses).
2. Torsion is the only factor in the mass formula that varies with vacuum.
3. The Galois vacuum has distinct spectral structure (9× enhanced gap).
4. The reversal at dist 7 (gal hits, triv misses) requires the correction to swap sign across vacua, which torsion can do.

### 4.6 Branch-Point Splitting

At R8, the propagator encounters a fork. The effective correction may involve a weighted sum over branches rather than a single path:

$$\Pi_{\text{branch}}(\rho, \sigma) = \Pi_{\text{chain}}(R0 \to R8, \sigma) \cdot \left[ w_{R5}(\sigma) \cdot T^2(R5 \otimes \sigma) + w_{R4}(\sigma) \cdot T^2(R4 \otimes \sigma) \right]$$

where the weights w depend on the vacuum through the branching ratio at R8. This would produce different corrections for modes that pass through R5 (path to R2) vs modes that terminate at R4 or R5 directly.

### 4.7 Galois Conjugation Correction

The Galois conjugation swaps R1 ↔ R2 and R3 ↔ R4 while fixing R5 and R7. At the branch point, R4 is the Galois conjugate of R3. The path from R0 to R4 (through R8) passes through R3's conjugate territory. The Galois vacuum may experience an additional phase or sign at nodes where conjugation is active.

---

## 5. The Charm Displacement

### 5.1 The Problem

The Coxeter-Galois gate locks all R4 entries to T₃ = -1/2 (all R4 entries have integer j_first). Charm requires T₃ = +1/2. The framework's own assignment rules exclude charm from its obvious candidate slot at R4 std (~734 MeV, within ×1.73 of charm's 1.27 GeV).

### 5.2 Why This Matters

This is the most informative kind of failure. A framework that bends its rules to fit every particle is less credible. MIT's rules actively exclude the obvious candidate. Either:

1. There is a subtlety at the R4 branch point that modifies the gate (the fork may carry different j_first behavior than the main chain).
2. Charm's assignment involves a mechanism the current formula doesn't capture.
3. Charm is telling you something about the limits of the branch-point approximation.

### 5.3 Connection to Branch-Point Correction

R4 is one of only two irreps reached through the fork at R8. If the branch-point splitting (§4.6) modifies the effective j_first or the Coxeter-Galois gate behavior at branched nodes, this could open a T₃ = +1/2 slot for charm without breaking the gate elsewhere. The correction and the charm assignment may be the same problem.

### 5.4 Status

OPEN. The charm displacement is the tightest constraint on any branch-point correction. Any proposed fix to the mass residual at high distance must simultaneously address (or at minimum not worsen) the charm assignment problem.

---

## 6. Test Protocol

### 6.1 Compute the Residual

For each of the 24 mass formula entries, compute:

$$r(\rho, \sigma) = \log_{10}\left(\frac{m_{\text{predicted}}}{m_{\text{observed}}}\right)$$

Positive r = overshoot. Negative r = undershoot.

### 6.2 Correlate with Candidate Corrections

Plot r against (in priority order):

1. Π_T (product of intermediate torsion along path). **PRIMARY: vacuum-dependent.**
2. Branch-point splitting factor. **PRIMARY: fork-sensitive.**
3. Combined Π_T × branch correction. **PRIMARY: full propagator.**
4. Π (product of intermediate C_geom). Secondary: vacuum-independent.
5. δ (sum of log C_geom along path). Secondary: distance-only.
6. κ (normalized path correction). Secondary.
7. dist alone. Baseline: check if simple linear correction suffices.

**Critical check:** For each candidate, verify that the correction reverses sign between the two misses. Down (R8 gal, dist 5) overshoots. Top (R2 triv, dist 7) also overshoots but from a different vacuum. The correction must overshoot gal at dist 5 while overshooting triv at dist 7. A correction that only works for one is wrong.

### 6.3 Evaluate

| Outcome | Interpretation |
|---|---|
| r correlates tightly with one candidate | Correction identified; apply and recompute scorecard |
| r correlates with dist but no candidate improves over linear | One-parameter linear correction in dist is sufficient |
| r shows no pattern | Residual is not from propagation; look elsewhere |
| Correction improves some fermions but worsens others | Multiple effects at play; decompose further |

---

## 7. What Success Looks Like

If a single multiplicative correction computable from the McKay graph structure closes the systematic overshoot at high distance:

- 10/12 within ×3 could become 12/12.
- The three best hits (electron 2%, up quark 6%, muon 3%) should remain unchanged (low dist, correction ≈ 1).
- The correction is parameter-free (computed from known C_geom and torsion values).
- The mass formula becomes fully determined by topology with no residual trend.

---

## 8. What Failure Looks Like

| Failure mode | Implication |
|---|---|
| No vacuum-dependent correction improves the fit | The overshoot is not from propagation or branching; the mass formula structure itself may need revision |
| Correction requires a fitted parameter | Not parameter-free; reduces to curve fitting |
| Correction fixes down quark but breaks top quark (or vice versa) | The vacuum reversal at the branch point is not captured; branching mechanism is wrong |
| Correction fixes masses but breaks charm assignment further | The branch-point gate modification is inconsistent; charm's exclusion is real and permanent |
| Torsion product diverges or vanishes along path | Intermediate torsion values may need regularization; check if T² = 0 at any node for any vacuum |
| Distance-only correction works as well as vacuum-dependent | Vacuum dependence was a red herring; simpler model preferred |

---

## 9. Connection to Open Items in Engine File

| Engine file item | Relevance |
|---|---|
| Fermion mass residual (OPEN) | Direct target of this work |
| dist/30 hierarchy exponent (ESTABLISHED) | Correction modifies the elevator without changing the exponent |
| Assignment problem (OPEN) | Charm displacement is the tightest constraint; branch-point correction may open a new slot |
| ν₂ gap (OPEN) | If correction affects low-distance entries, neutrino predictions change |
| Dead zone (OPEN) | Six entries between eV and keV with no SM occupants. If the branch-point correction modifies the dead zone masses, some entries might shift into or out of the experimentally probed range. The dead zone is the most interesting region strategically: any propagating state found there is a discovery |
| Charm as homeless (NEW) | R4 entries locked to T₃ = -1/2 by Coxeter-Galois gate. Charm needs T₃ = +1/2. Either the gate has a subtlety at the branch point or charm signals a limit of the current formula |
| Galois vacuum enhanced gap (ESTABLISHED) | 9× enhancement at Galois (first allowed k = 5) is the likely source of vacuum-dependent residual at high dist |

---

## 10. Key Constraints (Revised)

The correction must satisfy:

1. Computed from graph structure and torsion alone (no fitted parameters).
2. Vacuum-dependent (matching the observed pattern: different vacua miss at different distances).
3. Negligible at low distance (preserving electron 2%, up quark 6%, muon 3%).
4. Significant at dist = 5 gal and dist = 7 triv (fixing down quark and top quark).
5. Consistent with the reversal (gal misses at dist 5 but hits at dist 7; triv hits at dist 5 but misses at dist 7).
6. Sensitive to the branch point at R8 (R4 and R5 are reached through a fork).
7. Compatible with (or resolves) the charm displacement at R4.

If constraints 1-6 are satisfied, the correction is structural. If constraint 7 is also satisfied, the charm assignment opens and 10/12 could become 11/12 or 12/12. If any of 1-6 require tuning, it's a fit.

---

## 11. Next Steps

1. Compute residuals r(ρ,σ) for all 24 entries against observed masses.
2. Tabulate T²(i ⊗ σ) for all intermediate nodes along each path, for all three vacua.
3. Compute Π_T for each (ρ,σ) entry and check correlation with residual r.
4. Check if the vacuum reversal (gal misses at dist 5, triv misses at dist 7) is explained by intermediate torsion products.
5. Examine the R8 branch point: compute effective branching ratios for R4 vs R5 exit in each vacuum.
6. Check if the branch-point correction modifies the effective j_first at R4, potentially opening a T₃ = +1/2 slot for charm.
7. If a candidate works: apply, recompute full 24-entry scorecard, check charm status, update engine file.
8. If no candidate works: flag as unsolved, document what was tried, record which constraints failed.

---

*The mass ladder is the McKay graph. The correction is in the stairs. The stairs have different treads depending on which vacuum you're climbing in, and the landing at R8 is where the staircase forks.*

---

/ **[`main`](../../../)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
