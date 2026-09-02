<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Variational Score-to-Sample Program

**Status (2026-09-02):** WORKING / MOTIVATED. Ledger effect: none. Engine effect: none. Nothing on this page is derived: no functional is written down, and no lapse equation is solved. The page fixes the corpus conventions any candidate must respect, states the two-level action architecture, names the one bounded computation, and pre-registers its PASS and FAIL conditions before it is run. This is the working program behind the variational reading recorded on the [postulate bridge](postulate-bridge.md).

**Primary promotion gate:** derive the observer lapse $`N = S^{1/2}`$ from the native global functional, without inserting the exponent by hand.

**Dependencies:** [Postulate Bridge](postulate-bridge.md) (the variational reading this page expands, and the Tier 2 / Tier 3 arms it lies over), [Temporal Budget](temporal-budget.md) (the budget identity $`\Psi^2 + S^2 = 1`$ and the clock's home), [Friedmann as Output](friedmann-as-output.md) (the $`3/2`$ fence and the R-STAB hazard gate), [The Stress-Tensor Bridge](stress-tensor-bridge.md) (the descent target and the coefficient gate), [engine](../../../README.md) (the chronon $`\pi/30`$, the $`4\pi`$ anti-periodic period, and the Hubble clock).

**Related:** [The Waltz](../../../../spectrum/files/the-waltz.md) (the eight-functional well sweep, the recorded null this program must not repeat), [Sampler first test](sampler-first-test.md), [The Tick Lemma](tick-lemma.md), [The Level Exchange](half-power-involution.md).

---

## 1. Purpose

MIT already carries a global wave/history structure. The open problem is to select and descend the relation among the global wave, the embedding, the sampler, the connections, and the observer chart.

The program target is a native global functional coupling:

- the wave / budget fields;
- the embedding $`i`$;
- the sampler $`\mathcal O_M`$;
- the relevant flat and matter connections;
- and, at Tier 3, the metric response.

The observer-chart action is downstream:

```math
\mathcal{S}_{\text{MIT}}
\longrightarrow
\text{sampled local state}
\longrightarrow
\mathcal{S}_{\text{eff}}[g,\text{sampled fields}]
\longrightarrow
\text{Einstein field equations}.
```

$`\mathcal{S}_{\text{eff}}`$ descends from $`\mathcal{S}_{\text{MIT}}`$.

## 2. Fixed corpus conventions

Use the corpus symbols:

```math
\Psi=\cos(t/2), \qquad S=\sin(t/2)
```

for the existing on-shell budget solution.

$`t`$ is the native phase parameter.

The observer Hubble-clock variable is $`\tau_H`$, with general lapse

```math
d\tau_H=N(t)\,dt.
```

The currently used clock is

```math
N(t)=S(t)^{1/2}.
```

The descriptive chain is

```math
t \longrightarrow \tau_H(t) \longrightarrow q(\tau_H).
```

Time is phase advance; motion is change of resolved state under it.

## 3. Phase domain and Möbius sign

The one-lap phase interval has length $`2\pi`$ and carries the sign flip

```math
\Psi(t+2\pi)=-\Psi(t).
```

The closed edge traverses two laps, has phase length $`4\pi`$, and returns the field to itself:

```math
\Psi(t+4\pi)=\Psi(t).
```

Quadratic quantities satisfy

```math
\lvert\Psi(t+2\pi)\rvert^2=\lvert\Psi(t)\rvert^2,
```

so a quadratic functional on the closed $`4\pi`$ edge descends to the single $`2\pi`$ lap.

This descent forgets the Möbius orientation sign.

That $`\mathbb{Z}_2`$ is distinct from the central $`-I`$ of $`2I`$, which governs the separate $`120 \to 60`$ projection in the matter-side representation structure. Squaring is the same algebraic operation; the two $`\mathbb{Z}_2`$ structures are different objects.

A term that must retain Möbius orientation information must therefore retain data erased by $`\Psi \to -\Psi`$.

## 4. Existing variational foothold

The anti-periodic temporal sector already contains a variational statement.

On the one-lap problem with anti-periodic boundary condition,

```math
\Psi(t+2\pi)=-\Psi(t),
```

the functions

```math
\cos(t/2), \qquad \sin(t/2)
```

span the Rayleigh-quotient ground space of the quadratic form

```math
Q[\Psi]=\int \lvert\Psi'(t)\rvert^2\,dt.
```

The phase condition

```math
\Psi(0)=+1
```

selects the physical phase convention.

The program therefore extends an existing quadratic variational structure rather than beginning from zero.

## 5. Two-level action architecture

The intended architecture is

```math
\mathcal{S}_{\text{MIT}}
\;\longrightarrow\;
\mathcal{S}_{\text{eff}}.
```

The global functional carries the topology, phase, sampler, embedding, and connection data.

The effective observer-chart action carries the sampled matter and metric degrees of freedom.

This is the existing Tier-3 descent reading: sampled / twisted degrees of freedom are integrated out or descended into $`\mathcal{S}_{\text{eff}}`$.

The global and effective actions are therefore two levels of one program, rather than two independent postulates.

## 6. Candidate global functional

Keep the first functional schematic:

```math
\mathcal{S}_{\text{MIT}}
=
\mathcal{S}_{\text{MIT}}[\Psi,S,N,\lambda;\,i,\mathcal O_M,A,g,\ldots],
```

where:

- $`\Psi`$ is the complementary wave share;
- $`S`$ is the realized-mode share;
- $`N`$ is the observer lapse defined by $`d\tau_H = N\,dt`$;
- $`\lambda`$ is an optional multiplier enforcing a native budget constraint;
- $`i`$ is the embedding;
- $`\mathcal O_M`$ is the sampler / readout map;
- $`A`$ denotes the relevant flat and matter connections;
- $`g`$ enters when the Tier-3 metric-response arm is activated.

The minimal clock arm should contain only the structure required to test the lapse equation. Couplings to $`i`$, $`\mathcal O_M`$, $`A`$, and $`g`$ remain frozen during that first computation.

## 7. Jacobi precedent and the clock slot

The useful precedent is Jacobi's principle.

Jacobi replaces an externally driven time evolution with a geometric variational problem whose constraint supplies the physical clock along the extremal.

MIT already has a preferred phase parameter fixed by topology:

- one lap: $`2\pi`$;
- closed edge: $`4\pi`$;
- chronon: $`\pi/30`$.

The role of the global functional is therefore to convert the preferred phase parameter into the observer clock, rather than erase the preferred parameter.

Write

```math
d\tau_H=N(t)\,dt.
```

The promotion question is whether the lapse equation

```math
\frac{\delta \mathcal{S}_{\text{MIT}}}{\delta N}=0
```

forces

```math
N=S^{1/2}.
```

The identity

```math
\Psi^2+S^2=1
```

may appear as an on-shell constraint equation only. $`S`$ must remain a varied realized-mode share during the derivation, rather than being replaced at the start by $`\sin(t/2)`$.

### PASS

A preregistered native functional and its constraint structure determine

```math
N=S^{1/2}
```

without inserting the exponent as an input.

### PASS by stabilizer route

If the exponent is obtained through one of the currently unmerged numerical $`3/2`$ structures, the result promotes only together with the operator-level bridge that identifies the relevant structures.

This applies in particular to any route using a stabilizer ratio to reach the clock exponent.

### PASS by non-stabilizer route

A derivation of $`N=S^{1/2}`$ from a route independent of the unmerged $`3/2`$ structures stands on its own.

### FAIL

The minimal functional leaves $`N`$ underdetermined, returns another clock, or requires $`S^{1/2}`$ to be inserted into the action or constraint by construction.

## 8. Relation to the unmerged 3/2 triple

The corpus currently keeps three numerically equal $`3/2`$ appearances separate:

- the face / edge stabilizer ratio;
- the vacuum lift;
- the tick exponent $`S^{3/2}`$.

The Hubble-clock exponent $`1/2`$ is presently related to the tick exponent only after the existing import through

```math
a_\text{eff}=a_0 S.
```

Numerical equality is therefore insufficient for identification.

Any derivation that uses one of these $`3/2`$ structures as the source of the clock must supply the operator-level bridge that the current framework leaves open. The fence and its hazard gate are kept on [Friedmann as Output](friedmann-as-output.md).

## 9. Relation to the stress-tensor bridge

The existing stress-tensor result remains unchanged.

With

```math
a_\text{eff}=a_0 S
```

and

```math
d\tau_H=S^{1/2}\,dt,
```

the current bridge gives

```math
H^2=\frac{\Psi^2}{4S^3},
```

with the constant term excluded.

The variational program relocates the open question to the descent

```math
\mathcal{S}_{\text{MIT}}\longrightarrow \mathcal{S}_{\text{eff}}.
```

A successful global functional must explain why the observer-chart descent carries the required clock and stress-energy structure.

## 10. Tier relation and metric response

This program lies over the existing tiers.

Tier 2 remains the embedding-selection problem:

```math
\delta\mathcal{S}/\delta i.
```

Tier 3 remains the metric-response problem:

```math
\delta\mathcal{S}/\delta g.
```

For a diffeomorphism-invariant $`\mathcal{S}_{\text{eff}}`$ with sampled fields on shell, stress-energy conservation follows from the symmetry structure.

The load-bearing Tier-3 gate is the Einstein equation with the required coefficient structure:

```math
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
8\pi G\,T_{\mu\nu}.
```

The specific $`\Lambda`$ coefficient remains part of the coefficient gate.

## 11. First bounded computation

The first computation tests only the observer clock.

### Varied

Vary:

- $`N(t)`$, the observer lapse;
- $`S(t)`$, the realized-mode share;
- $`\Psi(t)`$, when required by the chosen minimal functional;
- $`\lambda(t)`$, when a multiplier is used to impose the native budget constraint.

### Held fixed

Hold fixed:

- the Möbius topology;
- the one-lap $`2\pi`$ anti-periodic boundary condition;
- the closed-edge $`4\pi`$ periodicity;
- the phase convention $`\Psi(0)=+1`$;
- the chronon $`\pi/30`$;
- the embedding $`i`$;
- the sampler $`\mathcal O_M`$;
- the flat and matter connections $`A`$;
- the metric $`g`$.

The first arm therefore asks only whether the native phase/budget variational structure determines the lapse.

### Constraint handling

If the functional uses

```math
\Psi^2+S^2=1,
```

treat it as a constraint equation arising from variation or multiplier enforcement.

The on-shell substitutions

```math
\Psi=\cos(t/2),
\qquad
S=\sin(t/2)
```

belong after the constraint equations are obtained.

### Primary observable

Read off the lapse law returned by the $`N`$ equation.

Promotion requires

```math
N(t)=S(t)^{1/2}
```

with the exponent fixed by the native functional.

## 12. Existing negative evidence

The eight-functional well-selection sweep remains a caution against low-complexity extremization narratives.

That sweep addressed a different search space: selection among discrete wells.

The present program concerns a functional over phase, lapse, and eventually embedding / sampler / connection data.

The candidate functional should still be preregistered before its observable consequences are inspected.

## 13. Expansion order after the clock gate

If the clock gate passes, arm the open objects in this order:

1. Couple the embedding $`i`$.
2. Couple the sampler $`\mathcal O_M`$.
3. Couple the relevant flat / matter connections.
4. Derive the sampled local state.
5. Activate metric variation and the Tier-3 descent.
6. Compare the resulting $`\mathcal{S}_{\text{eff}}`$ against the stress-tensor and coefficient gates.

Each arm should retain an independent stop condition and a predeclared observable.

## 14. Stop conditions

Stop and retain MOTIVATED status if:

- the lapse exponent is inserted rather than derived;
- the lapse equation leaves $`N`$ freely specifiable;
- the result depends on an arbitrary normalization that changes the exponent;
- the preferred topological phase parameter is erased;
- a stabilizer-based derivation merges the unbridged $`3/2`$ structures without the required operator map;
- the on-shell trigonometric forms are substituted before the constraint variation and thereby make the clock gate tautological;
- the desired clock appears only after observable-dependent tuning.

A failed clock arm may motivate a new preregistered functional, but it does not repair the failed arm.

## 15. Promotion rule

This program remains MOTIVATED until the bounded lapse computation passes.

Promotion occurs only when a native variational constraint fixes

```math
N=S^{1/2}
```

without importing the exponent, with any stabilizer-based route carrying its operator-level bridge.

At that point the score-to-sample reframing becomes a derivational result rather than program architecture.

---

*The clock in use is not the clock derived. Until the lapse equation returns its own exponent, this page is architecture.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
