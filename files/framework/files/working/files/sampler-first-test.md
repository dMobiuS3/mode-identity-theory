/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The sampler's first test: does the readout resolve sixty labels?

**Status (2026-08-19):** Set up, not run. This worksheet turns the first test of the [sampler reading](postulate-bridge.md) into a computation with a definite pass and fail. Three things are settled here and are not the test: the pullback $`f^*E_\tau`$ is canonically trivial, so the $`\mathcal L`$-twist cannot come from section data; the transverse derivative along the one-sided realization supplies that twist canonically, giving a first candidate operator that needs no arbitrary choice; and the naive form of the intensity question is unfalsifiable, passing for every candidate including operators that sample nothing. The falsifiable content is the separation half, and it reduces to one geometric quantity, the setwise stabilizer $`S = \mathrm{Stab}_{2I}(i(M))`$, whose order determines the number of distinguishable lifts, with $`\lvert S\rvert = 2`$ the unique target giving sixty. The boundary-stabilizer step is now computed: for a subgroup great circle, $`\mathrm{Stab}_{2I}(\gamma)`$ is $`C_4`$, $`C_6`$, or $`C_{10}`$ on the thirty-one icosahedral axes and $`\{\pm 1\}`$ on every other axis, so a generic boundary excludes over-collapse a priori and the whole test reduces to a single existence question. The supporting group facts about $`2I`$ are verified exactly; the worksheet is [sampler-first-test.test.py](sampler-first-test.test.py). That existence question, whether an admissible band with $`S = \{\pm 1\}`$ exists, is open and is the computation to run.

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

The normal direction $`\nu`$ is defined only up to sign, and globally that sign cannot be fixed; the value is therefore not a function but a section of the twisted bundle, which is exactly the required target type. By contrast the plain restriction $`\mathcal O^{(0)}_M(\Psi) = \widetilde\Psi \circ i`$ lands in $`\Gamma(M, f^*E_\tau)`$ with no twist, so it does not have the right type. Combining that with §1:

```math
\boxed{\ \text{the natural Möbius sampler is transverse, not restrictive}\ }
```

The field cannot supply the twist and the restriction does not carry it, so the sampler reads how the field varies across the band rather than its value on it. This statement is independent of how the test below turns out.

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

Second, every element of order four in $`2I`$ squares to $`-1`$, so any $`\mathbb Z_4 \subset 2I`$ contains the centre.

What $`\lvert S\rvert`$ can be is constrained but not to three values. Any element preserving the band preserves its boundary, so $`S \subseteq H := \mathrm{Stab}_{2I}(\gamma)`$, and $`H`$ is cyclic (§6), hence $`S`$ is cyclic and $`\lvert S\rvert`$ divides $`\lvert H\rvert`$. Since the cyclic subgroup orders available in $`2I`$ are $`1, 2, 3, 4, 5, 6, 10`$, the a priori possibilities are:

| $`\lvert S\rvert`$ | lifts | reading |
|---|---|---|
| $`1`$ | $`120`$ | no geometric identification at all |
| $`2`$, so $`S = \{\pm 1\}`$ | $`60`$ | exactly the central halving: the target |
| $`3`$ or $`5`$ | $`40`$ or $`24`$ | collapse from a symmetry unrelated to the centre ($`-1 \notin S`$) |
| $`4`$, $`6`$, $`10`$ | $`30`$, $`20`$, $`12`$ | central halving plus extra symmetry: over-collapse |

The sharp statement is therefore not a three-way split but

```math
\boxed{\ \lvert S\rvert = 2 \iff \text{exactly sixty lifts}\ }
```

with every other order a distinct failure mode of the proposed geometric realization. The odd cases are worth separating from $`\lvert S\rvert = 1`$: they collapse the lift family without the centre doing the work, which would produce a label count the framework does not read and would not be a halving at all. Note also that antipodal invariance alone gives only $`\{\pm 1\} \subseteq S`$, not equality, so it is necessary and not sufficient. The predicate can fail in several distinguishable ways, which is what the naive form lacked.

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
| Subgroup-circle stabilizers $`2I \cap C`$ | $`C_4`$ on $`15`$ axes, $`C_6`$ on $`10`$, $`C_{10}`$ on $`6`$, $`\{\pm 1\}`$ otherwise |

The last row is the boundary computation of §6, done here because it is pure group theory. Every element of $`2I`$ other than $`\pm 1`$ lies on a unique subgroup circle, indexed by its rotation axis up to sign; grouping the $`118`$ non-central elements by axis gives $`31`$ occupied axes, carrying $`2`$, $`4`$, and $`8`$ non-central elements respectively, so the circle through each contains $`4`$, $`6`$, or $`10`$ elements of $`2I`$ once $`\pm 1`$ are counted. These are the icosahedral symmetry axes: $`15`$ two-fold (edge), $`10`$ three-fold (face), $`6`$ five-fold (vertex), and $`15 + 10 + 6 = 31`$. Every other axis carries no element of $`2I`$ beyond the centre, so its circle has $`2I \cap C = \{\pm 1\}`$.

The first two rows are recorded because they are easy to over-read. Negation acts on $`\mathrm{SU}(2)`$ conjugacy classes by $`\varphi \mapsto \pi - \varphi`$ on the rotation angle, so the order-four class ($`\varphi = \pi/2`$, trace $`0`$) is the unique fixed one. This says something about conjugacy, not about the stabilizer question of §4, and it does not by itself select $`\mathbb Z_4`$ as the band's stabilizer. It is listed because the framework separately names a $`\mathbb Z_4`$ edge stabilizer in the mass sector, and the coincidence of the symbol $`\mathbb Z_4`$ across two different questions is exactly the kind of thing that invites a false identification. The mass-sector $`\mathbb Z_4`$ is about representation content restricted to a cyclic subgroup; the $`S`$ of §4 is a setwise stabilizer of an embedded band. Whether they meet is a question, not a given.

## 6. The computation, in order

**Step 1, the stabilizer of the boundary: done, and it governs the rest.** For a one-parameter-subgroup circle $`C = \{\exp(tZ)\}`$, left translation gives $`\gamma C = C`$ exactly when $`\gamma \in C`$, because $`1 \in C`$ forces $`\gamma \in \gamma C`$. So $`H = \mathrm{Stab}_{2I}(C) = 2I \cap C`$, a finite subgroup of a circle group and therefore cyclic, which is what makes $`S`$ cyclic in §4. Every such circle contains $`-1`$, since $`\exp(\pi Z) = -1`$ for unit $`Z \in \mathfrak{su}(2)`$, so $`\lvert H\rvert`$ is always even. By §5, $`H`$ is $`C_4`$, $`C_6`$, or $`C_{10}`$ when the axis is one of the $`31`$ icosahedral axes and $`\{\pm 1\}`$ otherwise. The admissible possibilities for $`S`$ follow at once.

| $`H`$ | $`\lvert S\rvert`$ possible | over-collapse reachable |
|---|---|---|
| $`\{\pm 1\}`$ (generic axis) | $`1, 2`$ | no |
| $`C_4`$ (15 edge axes) | $`1, 2, 4`$ | yes |
| $`C_6`$ (10 face axes) | $`1, 2, 3, 6`$ | yes |
| $`C_{10}`$ (6 vertex axes) | $`1, 2, 5, 10`$ | yes |

A generic boundary circle is therefore the clean case: $`S \subseteq \{\pm 1\}`$ leaves only $`\lvert S\rvert \in \{1, 2\}`$, so over-collapse and the odd unrelated-symmetry cases are excluded before any geometry is attempted, and the test becomes binary. Which circle the postulate's boundary actually is remains a choice to record explicitly, not an assumption to make quietly; if it sits on one of the $`31`$ special axes, symmetry-breaking becomes part of the construction problem.

**Step 2, the single existence question.** With the boundary fixed, everything reduces to

```math
\exists\, i(M) \in \mathcal A_\gamma \ \ \text{with} \ \ \mathrm{Stab}_{2I}\bigl(i(M)\bigr) = \{\pm 1\}\ ?
```

This one equality carries both halves: $`-1 \in S`$ is antipodal invariance of the whole band, not merely of its boundary curve, and $`S \subseteq \{\pm 1\}`$ is the exclusion of extra symmetry. On a generic boundary the second half is automatic, so the question collapses further to whether an antipodally invariant admissible band exists at all. If one does, exhibit it; if the constraint is obstructed, the obstruction is the result.

**Step 3, only then, the operator.** With the geometry settled, evaluate whether $`\mathcal O^{(1)}_M`$ separates the sixty lifts, that is whether the sampled intensities on inequivalent lifts are actually distinct for some $`\Psi`$. Steps 1 and 2 are necessary conditions and are cheaper; a failure there stops the program without any analysis of the operator.

A caution carried from the corpus: if step 2 succeeds, the resulting band is antipodally symmetric in $`S^3`$ under the deck element $`-1 \in 2I`$. The first-eigenvalue pillar also has an antipodal quotient in its construction, the double lune on the covering $`S^2(R)`$ whose antipodal quotient is the band. These are antipodal maps on different spheres serving different purposes, and they must not be merged. The pillar's is intrinsic to the band's own covering geometry; the one here is the deck action on the ambient $`S^3`$. Any statement that slides between them is the failure mode already recorded on this program, a number computed on a valid object and narrated on an invalid one.

## 7. What each outcome would mean

A result at $`\lvert S\rvert = 2`$ would be the first structure the sampler reading produces rather than explains: the halving from $`120`$ to $`60`$ would hold geometrically, as a property of the sampler family, in addition to holding automatically at the level of intensities. That is the case in which the reading earns promotion from interpretation toward mechanism, and it is the point at which reconsidering the engine's master narrative becomes reasonable rather than premature.

A result at $`\lvert S\rvert = 1`$ for every admissible band closes this route. The halving would remain exactly what the engine already says it is, and the sampler reading would have produced no new structure here. Stated for a specified admissible class, that is a real negative and belongs on the record, in the same way the restriction-route negative of Steps 1 to 4 does.

A result at $`\lvert S\rvert > 2`$ would be the most interesting outcome and the least anticipated: a sampler resolving thirty, twenty, or twelve labels where the framework reads sixty. It would not refute the engine's projection, which stands on its own argument, but it would say the sampler and the label count come apart, and that discrepancy would need an account. The odd cases $`\lvert S\rvert = 3, 5`$ are stranger still and would be the clearest negative of all: the lift family collapses while the centre does nothing, so whatever the sampler is doing there is not the halving the reading was built to explain. All of these are reachable only from a special-axis boundary, which is why fixing the boundary circle is the first thing to settle.

## 8. Scope and non-claims

Nothing here asserts that $`\mathcal O^{(1)}_M`$ is the right operator, only that it is canonical and has the correct target type. Nothing here couples to the $`2I`$-decorated gauge sector: this is the sampling half of the postulate, and the Galois side is untouched, exactly as the Tier 2 ground floor is the surface half only. Nothing here is dynamical; which admissible band is realized is Tier 2's question, and this worksheet takes the band as given. The surface pillar is not in play: its twisted spectrum and its $`2/R^2`$ first positive level are an independent result about the band's own intrinsic geometry, and no eigenvalue of that problem enters any statement above. The bar of the [postulate bridge](postulate-bridge.md) is unchanged, and this worksheet does not meet it; it only makes the first test a thing that can be run and can fail.

---

*The operator has a canonical candidate and the question has a definite failure mode. What remains is one geometric existence problem.*

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
