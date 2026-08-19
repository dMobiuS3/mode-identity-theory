/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The sampler's first test: does the readout resolve sixty labels?

**Status (2026-08-19):** Set up, not run. This worksheet turns the first test of the [sampler reading](postulate-bridge.md) into a computation with a definite pass and fail. Three things are settled here and are not the test: the pullback $`f^*E_\tau`$ is canonically trivial, so the $`\mathcal L`$-twist cannot come from section data; the transverse derivative along the one-sided realization supplies that twist canonically, giving a first candidate operator that needs no arbitrary choice; and the naive form of the intensity question is unfalsifiable, passing for every candidate including operators that sample nothing. The falsifiable content is the separation half, and it reduces to one geometric quantity, the setwise stabilizer $`S = \mathrm{Stab}_{2I}(i(M))`$, whose three possible sizes give three distinguishable outcomes. The supporting group facts about $`2I`$ are verified exactly; the worksheet is [sampler-first-test.test.py](sampler-first-test.test.py). The geometric question, whether an admissible band with $`S = \{\pm 1\}`$ exists, is open and is the computation to run.

**Related:** [Postulate bridge](postulate-bridge.md), [First eigenvalue](../../bedrock/files/first-eigenvalue.md), [Galois pair](../../bedrock/files/galois-pair.md), [engine](../../../README.md).

---

**Goal.** The sampler reading asks whether an admissible sampling operator $`\mathcal O_M`$ intertwines the central $`-1 \in 2I`$ with the Möbius sign ambiguity, so that an intensity observable factors through $`2I/\{\pm 1\} \cong I`$. Stated that way the question is not yet a computation: no $`\mathcal O_M`$ is constructed, and the property as worded is satisfied trivially. This worksheet fixes both problems. It exhibits a canonical candidate operator, isolates the half of the question that can fail, and reduces that half to a single stabilizer computation on an already-specified admissible class.

**Conventions.** $`X = S^3/2I`$ with $`\pi : S^3 \to X`$ the quotient by the left action of $`2I \subset \mathrm{SU}(2) \cong S^3`$, so $`\pi_1(X) = 2I`$ and the deck group is $`2I`$. A flat bundle $`E_\tau = S^3 \times_{2I} V_\tau`$ is associated to a unitary representation $`\tau`$ of $`2I`$, and a section $`\Psi \in \Gamma(X, E_\tau)`$ is the same thing as an equivariant map $`\widetilde\Psi : S^3 \to V_\tau`$ with $`\widetilde\Psi(\gamma x) = \tau(\gamma)\widetilde\Psi(x)`$. $`M`$ is the Möbius band, $`i : M \to S^3`$ a smooth embedding from the admissible class $`\mathcal A_\gamma`$ of the [Tier 2 ground floor](postulate-bridge.md) (boundary held on a fixed round great circle $`\gamma \subset S^3(R)`$), $`f = \pi \circ i`$, and $`\mathcal L \to M`$ the orientation local system. Throughout, $`\lvert\cdot\rvert`$ on $`V_\tau`$ is a $`2I`$-invariant Hermitian metric.

---

## 1. The pullback carries no twist

The composite $`f = \pi \circ i`$ has a preferred lift to the universal cover, namely $`i`$ itself. Equivalently, $`f_* : \pi_1(M) \to \pi_1(X) = 2I`$ is the trivial homomorphism: the core loop of $`M`$ is a loop in the simply connected $`S^3`$ before it is pushed to $`X`$, so it dies there. Consequently

```math
f^*E_\tau \;=\; i^*\pi^*E_\tau \;=\; i^*(S^3 \times V_\tau) \;=\; M \times V_\tau ,
```

canonically trivialized as a flat bundle, and $`f^*\Psi`$ is the honest $`V_\tau`$-valued function $`\widetilde\Psi \circ i`$ on $`M`$.

This sharpens the second guardrail of the sampler reading. The obstruction is not only that $`\mathcal L`$ has no global nowhere-zero section: the pulled-back section data carries no twist at all, so the $`\mathcal L`$ in the target of $`\mathcal O_M`$ has to be supplied by the geometry of the realization rather than extracted from the field. Any construction that produces it by other means is inserting the twist by hand, and the insertion is the thing to scrutinize.

## 2. A canonical candidate: the twist is transverse

$`M`$ is non-orientable and $`S^3`$ is orientable, so $`M`$ is one-sided and its normal bundle $`\nu`$ is isomorphic, as a flat real line bundle with its induced normal connection, to the orientation local system $`\mathcal L`$ (Fact B of the Tier 2 ground floor). A real line bundle with $`\pm 1`$ transitions is self-dual, so $`\nu^* \cong \mathcal L`$ as well. Since $`\widetilde\Psi`$ is defined on all of $`S^3`$ and not merely on the image of $`i`$, its transverse derivative along the realization exists and is canonically $`\mathcal L`$-valued:

```math
\mathcal O^{(1)}_M(\Psi) \;:=\; \partial_\nu\bigl(\widetilde\Psi\bigr)\big\vert_{i(M)} \;\in\; \Gamma\bigl(M,\ f^*E_\tau \otimes \mathcal L\bigr).
```

The normal direction $`\nu`$ is defined only up to sign, and globally that sign cannot be fixed; the value is therefore not a function but a section of the twisted bundle, which is exactly the required target type. By contrast the plain restriction $`\mathcal O^{(0)}_M(\Psi) = \widetilde\Psi \circ i`$ lands in $`\Gamma(M, f^*E_\tau)`$ with no twist, so it does not have the right type. The twist enters through transversality, not through section content: the sampler reads how the field varies across the band, not merely its value on it.

$`\mathcal O^{(1)}_M`$ is *a* canonical candidate, not *the* operator. Higher normal jets, weighted combinations, and integral transforms along the transverse direction all produce the same target type, and nothing here selects among them. What $`\mathcal O^{(1)}_M`$ establishes is that the target type is attainable with no arbitrary choice, which was not previously on the record.

## 3. The trap: the naive test cannot fail

Take the question at face value: does an intensity observable factor through $`2I/\{\pm 1\}`$? For any $`\tau`$ and any $`2I`$-invariant metric,

```math
\bigl\lvert \widetilde\Psi(\gamma x)\bigr\rvert^2 \;=\; \bigl\lvert \tau(\gamma)\widetilde\Psi(x)\bigr\rvert^2 \;=\; \bigl\lvert \widetilde\Psi(x)\bigr\rvert^2 \qquad \text{for all } \gamma \in 2I,
```

and in particular at $`\gamma = -1`$, whatever the spin parity of $`\tau`$. Squaring an $`\mathcal L`$-valued section likewise kills the twist, since $`\mathcal L \otimes \mathcal L`$ is canonically trivial. So the intensity is sign-blind, and it is sign-blind for reasons that use nothing about $`M`$, about $`f`$, or about $`\mathcal O_M`$.

Mutation-testing the check confirms it is empty: replace $`M`$ by any other subset of $`S^3`$, or replace $`\mathcal O_M`$ by the zero operator, and the property still holds. A predicate that no candidate can fail is not evidence for any candidate. The "at most sixty" half of the claim is free, and it is not what the sampler reading has to earn.

The engine's own statement of the projection rests on this same sign-blindness and is untouched by anything below: the $`120`$ labels pass to the $`60`$ under $`\lvert\psi\rvert^2`$ because the anti-periodic sign is erased. That argument is sound and independent. The question here is the different one of whether the sampler *also* realizes the halving geometrically, which is what would make the reading produce structure rather than restate it.

## 4. The falsifiable core: the setwise stabilizer

What can fail is the separation half: does the sampler resolve sixty labels, rather than fewer? Make it precise through the lifts. All $`120`$ translates $`\gamma \cdot i(M)`$ have the same image in $`X`$, so they are the lifts of one sampling locus, and the number of distinct lifts is

```math
\#\{\gamma \cdot i(M) : \gamma \in 2I\} \;=\; \frac{120}{\lvert S\rvert}, \qquad S \;=\; \mathrm{Stab}_{2I}\bigl(i(M)\bigr) \ \ \text{(setwise)} .
```

Two verified facts about $`2I`$ convert this into a sharp trichotomy. First, $`2I`$ has exactly one element of order two, namely the central $`-1`$; by Cauchy's theorem every subgroup of even order therefore contains $`-1`$, and the subgroups of odd order are only the trivial group, $`\mathbb Z_3`$, and $`\mathbb Z_5`$. Hence

```math
-1 \in S \iff \lvert S\rvert \ \text{is even} .
```

Second, every element of order four in $`2I`$ squares to $`-1`$, so any $`\mathbb Z_4 \subset 2I`$ contains the centre. The outcomes:

| $`\lvert S\rvert`$ | distinct lifts | reading |
|---|---|---|
| $`1`$ (generic band) | $`120`$ | $`-1 \notin S`$: the lift family is $`2I`$-labelled, no geometric halving |
| $`2`$, so $`S = \{\pm 1\}`$ | $`60`$ | lifts in bijection with $`I = 2I/\{\pm 1\}`$: the target outcome |
| $`4`$, e.g. $`S = \mathbb Z_4`$ | $`30`$ | over-collapse, fewer labels than the framework reads |

Only the middle row realizes the halving geometrically, and a generic band lands in the first. The predicate can fail, which is what the naive form lacked.

## 5. Group facts, verified

Computed exactly in [sampler-first-test.test.py](sampler-first-test.test.py), which builds $`2I`$ by closing a generating pair of unit quaternions and checks the closure is a group of order $`120`$ with nine conjugacy classes before asserting anything else.

| Fact | Value |
|---|---|
| Conjugacy classes of $`2I`$ | $`9`$, of sizes $`1, 1, 12, 12, 12, 12, 20, 20, 30`$ |
| Classes closed under $`g \mapsto -g`$ | exactly one, the order-four class of size $`30`$ |
| Behaviour of the rest | the other eight classes are swapped in four pairs |
| Elements of order two | exactly one, the central $`-1`$ |
| Element orders present | $`1, 2, 3, 4, 5, 6, 10`$ (no element of order $`15`$) |
| Squares of order-four elements | all equal $`-1`$ |
| Odd cyclic subgroup orders | $`1, 3, 5`$ |

The first two rows are recorded because they are easy to over-read. Negation acts on $`\mathrm{SU}(2)`$ conjugacy classes by $`\varphi \mapsto \pi - \varphi`$ on the rotation angle, so the order-four class ($`\varphi = \pi/2`$, trace $`0`$) is the unique fixed one. This says something about conjugacy, not about the stabilizer question of §4, and it does not by itself select $`\mathbb Z_4`$ as the band's stabilizer. It is listed because the framework separately names a $`\mathbb Z_4`$ edge stabilizer in the mass sector, and the coincidence of the symbol $`\mathbb Z_4`$ across two different questions is exactly the kind of thing that invites a false identification. The mass-sector $`\mathbb Z_4`$ is about representation content restricted to a cyclic subgroup; the $`S`$ of §4 is a setwise stabilizer of an embedded band. Whether they meet is a question, not a given.

## 6. The computation, in order

1. **Stabilizer of the boundary.** The admissible class $`\mathcal A_\gamma`$ fixes $`\partial M = \gamma`$, and any element preserving the band preserves its boundary, so $`S \subseteq \mathrm{Stab}_{2I}(\gamma)`$. Compute $`\mathrm{Stab}_{2I}(\gamma)`$ for the round great circles of $`S^3`$ under left translation. For a one-parameter-subgroup circle $`C = \{\exp(tZ)\}`$ the left translates satisfy $`\gamma C = C`$ exactly when $`\gamma \in C`$, so $`\mathrm{Stab}_{2I}(C) = 2I \cap C`$, a cyclic subgroup. Note that every such circle passes through $`-1`$, since $`\exp(\pi Z) = -1`$ for unit $`Z \in \mathfrak{su}(2)`$, so this class of boundary curves already carries the centre. Whether the postulate's boundary is of this type is itself a choice to record, not an assumption to make quietly.
2. **Stabilizer of the band.** The real question, and strictly stronger: is there an $`M \in \mathcal A_\gamma`$ with $`-1 \cdot i(M) = i(M)`$ setwise? Antipodal invariance of the whole band, not merely of its boundary curve, is what §4 needs. If such a band exists, exhibit one; if the constraint is obstructed, the obstruction is the result.
3. **Exclude over-collapse.** Given a band from step 2, verify $`\lvert S\rvert = 2`$ rather than $`4`$ or more, so the count is sixty and not thirty.
4. **Only then, the operator.** With the geometry settled, evaluate whether $`\mathcal O^{(1)}_M`$ separates the sixty lifts, that is whether the sampled intensities on inequivalent lifts are actually distinct for some $`\Psi`$. Steps 1 to 3 are necessary conditions and are cheaper; a failure there stops the program without any analysis of the operator.

A caution carried from the corpus: if step 2 succeeds, the resulting band is antipodally symmetric in $`S^3`$ under the deck element $`-1 \in 2I`$. The first-eigenvalue pillar also has an antipodal quotient in its construction, the double lune on the covering $`S^2(R)`$ whose antipodal quotient is the band. These are antipodal maps on different spheres serving different purposes, and they must not be merged. The pillar's is intrinsic to the band's own covering geometry; the one here is the deck action on the ambient $`S^3`$. Any statement that slides between them is the failure mode already recorded on this program, a number computed on a valid object and narrated on an invalid one.

## 7. What each outcome would mean

A result at $`\lvert S\rvert = 2`$ would be the first structure the sampler reading produces rather than explains: the halving from $`120`$ to $`60`$ would hold geometrically, as a property of the sampler family, in addition to holding automatically at the level of intensities. That is the case in which the reading earns promotion from interpretation toward mechanism, and it is the point at which reconsidering the engine's master narrative becomes reasonable rather than premature.

A result at $`\lvert S\rvert = 1`$ for every admissible band closes this route. The halving would remain exactly what the engine already says it is, and the sampler reading would have produced no new structure here. Stated for a specified admissible class, that is a real negative and belongs on the record, in the same way the restriction-route negative of Steps 1 to 4 does.

A result at $`\lvert S\rvert = 4`$ would be the most interesting outcome and the least anticipated: a sampler resolving thirty labels where the framework reads sixty. It would not refute the engine's projection, which stands on its own argument, but it would say the sampler and the label count come apart, and that discrepancy would need an account.

## 8. Scope and non-claims

Nothing here asserts that $`\mathcal O^{(1)}_M`$ is the right operator, only that it is canonical and has the correct target type. Nothing here couples to the $`2I`$-decorated gauge sector: this is the sampling half of the postulate, and the Galois side is untouched, exactly as the Tier 2 ground floor is the surface half only. Nothing here is dynamical; which admissible band is realized is Tier 2's question, and this worksheet takes the band as given. The surface pillar is not in play: its twisted spectrum and its $`2/R^2`$ first positive level are an independent result about the band's own intrinsic geometry, and no eigenvalue of that problem enters any statement above. The bar of the [postulate bridge](postulate-bridge.md) is unchanged, and this worksheet does not meet it; it only makes the first test a thing that can be run and can fail.

---

*The operator has a canonical candidate and the question has a definite failure mode. What remains is one geometric existence problem.*

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
