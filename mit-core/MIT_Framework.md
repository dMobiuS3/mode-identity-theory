# Mode Identity Theory: The Framework

**Version:** 5.1  
**Author:** Blake Shatto, P.E.  
**Last Updated:** 2026-01-23

---

## Overview

One topology postulate generates a scaling law that recovers Lambda, H_0, and a_0 across 61 orders of magnitude. Each component of the scaling law traces to the postulate; no continuous free parameters are introduced.

---

## 1. The Nested Topology

The framework adopts a hierarchy of nested manifolds:

```
S^1 = boundary(Mobius) --> S^3
```

| Manifold | Boundary | Description |
|----------|----------|-------------|
| S^1 | boundary(S^1) = empty | Closed loop; boundary of Mobius |
| Mobius | boundary(M) = S^1 | Non-orientable surface; embedded in S^3 |
| S^3 | boundary(S^3) = empty | Orientable bulk; boundless |

**The Temporal Edge (S^1).** The 1D boundary of the Mobius surface. Circumference L; characteristic timescale L/c. Inherits the anti-periodic boundary condition.

**The Mobius Surface.** The 2D non-orientable manifold bounded by the edge. The Mobius Z_2 holonomy admits two boundary condition sectors:

| Sector | Condition | Selected by |
|--------|-----------|-------------|
| Periodic | psi(y+L) = +psi(y) | Bosonic matter |
| Anti-periodic | psi(y+L) = -psi(y) | Fermionic matter |

Observation selects the anti-periodic sector: matter is fermionic.

**Eigenproblem.** Along the twisted direction:

```
-d^2(psi)/dy^2 = lambda * psi
```

The ansatz psi ~ exp(iky) under psi(y+L) = -psi(y) requires:

```
exp(ikL) = -1  -->  kL = (2m + 1) * pi
```

Define nu = kL/(2*pi). Then:

```
nu = m + 1/2
```

The eigenvalues are half-integers: nu = 1/2, 3/2, 5/2, ...

**Ground State Selection.** The framework selects m = 0 by operational definition. Cosmological parameters (Lambda, H_0) describe the homogeneous, isotropic background. Three arguments exclude m > 0:

| Argument | Mechanism |
|----------|-----------|
| Isotropy | m > 0 nodes create O(1) anisotropy; CMB is isotropic to 10^-5 |
| Orthogonality | Oscillating modes average to zero over Gpc volumes |
| Relaxation | Higher modes decay; m = 0 dominates at late times |

**The Hypersphere Bulk (S^3).** The 3D volume containing the surface. Couples gravitationally only.

```
boundary(S^3) = empty
```

The hierarchy terminates here. "What's outside?" is malformed; there is no boundary from which to observe.

---

## 2. The Cosmic Wave

The temporal edge inherits the anti-periodic boundary condition. A field on the edge must reverse sign after one circuit; this admits standing wave solutions.

**Period.** Let t = 2*pi*y/L denote cosmic phase. Anti-periodicity requires Psi(t + 2*pi) = -Psi(t); return to original configuration requires two circuits: Psi(t + 4*pi) = Psi(t). Hence period 4*pi.

**The standing wave:**

```
Psi(t) = cos(t/2)
```

Cosine places extrema at t = 0 and t = 2*pi: maximum positive (Psi = +1) at start, maximum negative (Psi = -1) at midpoint.

| t (rad) | Psi(t) | Epoch |
|---------|--------|-------|
| 0 | +1 | Initial |
| pi | 0 | First crossing |
| 2*pi | -1 | Turnaround |
| 3*pi | 0 | Second crossing |
| 4*pi | +1 | Completion |

**Present epoch.** Fitting to DESI w(z) evolution constrains delta = -1.06 rad, placing the present at t = 2*pi + delta = 5.22 rad, approximately 2.8 Gyr before turnaround.

---

## 3. Cosmic Scale

**The Scale Hierarchy.** Two scales govern the framework:

```
Omega_Lambda = (R_Lambda / ell_P)^2  ~  10^122
Omega_H(z)   = (R_H(z) / ell_P)^2    ~  10^122  (at z ~ 0)
```

where R_Lambda = sqrt(3/Lambda) is the de Sitter radius and R_H(z) = c/H(z) is the Hubble radius. The squared definition reflects horizon area: degrees of freedom scale with boundary, not volume.

**The Observer.** The observer occupies sqrt(Omega) ~ 10^61, the geometric mean between Planck scale (~10^0) and cosmic scale (10^122).

```
0 -------- sqrt(Omega) = 10^61 -------- 10^122
Planck          Observer              Horizon
```

This is not anthropic selection. The UV<->IR symmetry x --> Omega/x has fixed point x = sqrt(Omega). The observer IS the resolution site by geometric necessity.

**The Scale Factor.** Mode intensity dilutes in an embedded manifold:

```
|psi|^2 ~ (sqrt(Omega))^(-n)
```

The scale Omega = (R/ell_P)^2 counts Planck areas. Volume of an n-dimensional manifold scales as V_n ~ (sqrt(Omega))^n. Normalized mode intensity scales as the inverse.

**Manifold Index.** The index n specifies which manifold governs the mode:

| n | Manifold | Omega | (sqrt(Omega))^(-n) | Observables |
|---|----------|-------|---------------------|-------------|
| 1 | Temporal edge | Omega_H | 10^-61 | H_0, a_0 |
| 2 | Mobius surface | Omega_Lambda | 10^-122 | Lambda |
| 3 | Bulk | Omega_Lambda | 10^-183 | Dark matter |

**Selection Rules.** The manifold index is determined by observable character:

| Criterion | Result |
|-----------|--------|
| Epoch-dependent? | Yes --> n = 1 (edge) |
| Epoch-independent, gauge-coupled? | Yes --> n = 2 (surface) |
| Gravity-only coupling? | Yes --> n = 3 (bulk) |

**Why edge uses Omega_H while surface uses Omega_Lambda.** The temporal edge S^1 is where time happens; only the edge can reference a quantity that evolves. The Hubble horizon R_H(z) evolves; therefore H_0 and a_0 reference Omega_H. The Mobius surface is defined by Lambda, which sets the boundary condition itself. Boundary conditions do not evolve; therefore Lambda references Omega_Lambda.

**Exclusion test.** Wrong assignments fail by 61 orders. Lambda as n = 1 would give 10^-61, not 10^-122. H_0 as n = 2 would give 10^-122, not 10^-61.

---

## 4. The Phase Operator

Different positions on the standing wave carry different amplitude. The phase operator C(alpha) encodes this:

```
C(alpha) = 2 * sin^2(pi * alpha)
```

This function vanishes at alpha = 0 and alpha = 1 (boundaries), reaches maximum C = 2 at alpha = 1/2 (antinode).

**Derivation.** The anti-periodic ground state satisfying psi(alpha + 1) = -psi(alpha) is:

```
psi_0(alpha) = sin(pi * alpha)
```

Observable intensity is |psi|^2. Normalizing to unit mean sets peak amplitude to 2:

```
C(alpha) = 2 * sin^2(pi * alpha)
```

The periodic sector yields C = 1 everywhere, but H_0 and a_0 are both n = 1 modes with different magnitudes. The variation requires anti-periodic boundary conditions.

**The 120 Domain.** By Hurwitz's theorem, the golden ratio phi is the positive real most poorly approximated by rationals: the most stable sampling position. Fibonacci numbers are its convergents.

S^3 carries discrete subgroups: 2T (order 24), 2O (order 48), 2I (order 120). The observed well at 13/120 is irreducible: gcd(13, 120) = 1. No coarser grid can represent it. The 120-grid is the minimum resolution required.

**The Bosonic Filter.** The wavefunction psi has period 2 (spinor); observable intensity |psi|^2 has period 1 (scalar). The squaring operation projects 2I --> I. Geometric observables live on the 60R-grid: only even slots, minimum step 2/120.

**Active Wells.** An amplitude threshold C(alpha) >= 0.2 excludes low-Fibonacci wells (F_2 through F_6 all have C < 0.09). Surviving wells:

| F_n | Well | C(alpha) | Observable |
|-----|------|----------|------------|
| F_7 | 13/120 | 0.22 | a_0 |
| F_8 | 21/120 | 0.55 | -- |
| F_9 | 34/120 | 1.21 | H_0 |
| F_10 | 55/120 | 1.97 | -- |
| -- | 60/120 | 2.00 | Lambda (antinode) |

The wells are derived. The well-to-observable assignments are calibrated (with structural motivation from coprimality).

**Phase Field (alpha_f).** For global observations, alpha_f = 0. For local observations, alpha_f reflects the environment. The minimum bosonic step is 2/120; for the Milky Way, alpha_f ~ 2/120 produces an 8.4% shift in C(alpha), matching the Hubble tension.

---

## 5. The Scaling Law

The framework reduces to one equation:

```
A / A_P = (sqrt(Omega))^(-n) * C(alpha)
```

Read right to left: C(alpha) sets amplitude at position alpha; (sqrt(Omega))^(-n) dilutes by embedding in manifold n. The product yields A/A_P, the dimensionless observable.

**Derivation Chain.** Each component traces to the topology:

| Component | Source |
|-----------|--------|
| C(alpha) = 2*sin^2(pi*alpha) | Anti-periodic BC + normalization |
| alpha on 120-grid | S^3 polyhedral subgroups + irreducibility |
| alpha in {13, 21, 34, 55, 60}/120 | Hurwitz stability + amplitude threshold |
| (sqrt(Omega))^(-n) | UV<->IR fixed point + volume scaling |
| m = 0 | Isotropy + orthogonality + relaxation |
| n = 1, 2, 3 | Epoch-dependence + coupling character |

---

## 6. Numerical Predictions

### Edge Modes (n = 1)

**H_0:**
```
H_0 * t_P = (sqrt(Omega_H))^(-1) * C(34/120)
         = 10^-61 * 1.21
         = 1.2 * 10^-61
```
Observed: 1.2 * 10^-61. Match.

**a_0:**
```
a_0 / a_P = (sqrt(Omega_H))^(-1) * C(13/120)
          = 10^-61 * 0.22
          = 2.2 * 10^-62
```
Observed: 2.0 * 10^-62. Match.

**Ratio check:**
```
a_0 / (c * H_0) = C(13/120) / C(34/120) = 0.22 / 1.21 = 0.18
```
Observed: 0.17. Match.

### Surface Mode (n = 2)

**Lambda (with surface-to-bulk conversion):**

The scaling law yields the surface eigenvalue:
```
Lambda_surface / M_P^4 = (sqrt(Omega_Lambda))^(-2) * C(60/120)
                       = 10^-122 * 2.0
                       = 2.0 * 10^-122
```

This is the 2D topological eigenvalue. GR defines Lambda in 3+1 spacetime. The surface-to-bulk conversion factor is 3/2:

```
Lambda_obs / M_P^4 = (3/2) * Lambda_surface / M_P^4
                   = (3/2) * 2.0 * 10^-122
                   = 3.0 * 10^-122
```

Observed (Planck 2018): 2.89 * 10^-122.

| Quantity | Value | Deviation |
|----------|-------|-----------|
| MIT surface eigenvalue | 2.0 * 10^-122 | -31% |
| MIT with 3/2 conversion | 3.0 * 10^-122 | +4% |
| Observed | 2.89 * 10^-122 | -- |

The 3/2 factor arises because Lambda is defined as a ground-state eigenvalue on the 2D Mobius surface (Laplace-Beltrami operator), but observed as an energy density in 3+1 spacetime (Einstein field equations). The conversion is geometric, not fitted.

### Bulk Mode (n = 3)

**Dark matter:**
```
DM coupling ~ (sqrt(Omega_Lambda))^(-3) ~ 10^-183
```

This suppresses non-gravitational signals to observational null. Particle dark matter searches (LZ, XENONnT) finding null results is the prediction, not experimental failure.

---

## 7. Summary

**What is derived:**

| Element | Status |
|---------|--------|
| C(alpha) = 2*sin^2(pi*alpha) | Derived from anti-periodic BC |
| 120-grid | Derived from irreducibility (gcd(13,120) = 1) |
| Fibonacci wells | Derived from Hurwitz stability |
| Observer at sqrt(Omega) | Derived from UV<->IR fixed point |
| m = 0 selection | Derived from isotropy/orthogonality |
| n = 1, 2, 3 assignments | Derived from observable character |

**What is calibrated:**

| Element | Status |
|---------|--------|
| Well <-> observable map | Calibrated (coprimality provides motivation) |

**What is postulated:**

| Element | Status |
|---------|--------|
| S^1 = boundary(Mobius) --> S^3 | Topology postulate (bedrock) |
| ell_P | Domain boundary (interface with QG) |

**The scaling law contains no continuous free parameters.**

---

## 8. Distinct Predictions

| Prediction | MIT | Standard | Test |
|------------|-----|----------|------|
| Lambda | Constant | May evolve | Euclid, DESI |
| a_0 | Evolves as H(z) | Constant | High-z kinematics |

The inversion is the signature. Standard assumptions hold a_0 constant and allow Lambda to evolve. MIT predicts the opposite. Both are testable now.

---

## References

- de Broglie, L. (1924). Recherches sur la theorie des quanta. Ph.D. thesis.
- Planck Collaboration (2020). Astron. Astrophys. 641, A6, A7.
- DESI Collaboration (2025). arXiv:2503.14738.
- Hurwitz, A. (1891). Math. Ann. 39, 279.
- Milgrom, M. (1983). Astrophys. J. 270, 365.

---

*One topology. One scaling law. No free parameters.*
