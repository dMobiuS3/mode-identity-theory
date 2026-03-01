# Easy Money: Yang-Mills on the Poincare Homology Sphere

The Millennium Prize asks whether pure Yang-Mills theory on $\mathbb{R}^4$ has a positive mass gap. On flat space, confinement must emerge dynamically. On the Poincare homology sphere $M = S^3/2I$, where $2I$ is the binary icosahedral group of order 120, the answer is forced by geometry. 

Positive Ricci curvature provides a universal floor. The finite fundamental group yields exactly three isolated vacua: trivial, standard, and Galois conjugate. The McKay correspondence for the extended $E_8$ diagram filters the spectrum at each vacuum, producing a ninefold enhancement at the Galois sector. 

The same curvature that enters the Λ conversion guarantees confinement.

**Mass gap on M = S^3/2I**

| Property | Value |
|---|---|
| Curvature floor | $\lambda \geq 2/R^2$ (universal, Weitzenböck) |
| Vacua | 3 isolated (trivial, standard, Galois) |
| Gap (trivial, standard) | $\Delta^2 = 4/R^2$ |
| Gap (Galois) | $\Delta^2 = 36/R^2$ (9x enhancement) |
| Three vacua | Three particle generations |

## I. The Geometry

The Weitzenböck identity on $S^3$ decomposes the gauge-covariant Hodge Laplacian on bundle-valued 1-forms. For a flat connection ($F_A = 0$), it reduces to:

$$\Delta_{\text{Hodge}} = \nabla_A^\ast \nabla_A + \text{Ric}$$

On the round $S^3$ of radius $R$, the Ricci tensor is $R_{ij} = (2/R^2)\,g_{ij}$. Since $\nabla_A^\ast \nabla_A \geq 0$ and $\text{Ric} = 2/R^2 > 0$, every gauge fluctuation around any flat connection satisfies:

$$\lambda_{\min} \geq \frac{2}{R^2}$$

This bound is universal: it holds for any quotient $S^3/\Gamma$ inheriting the round metric, independent of $\Gamma$ and the choice of flat connection. The gap exists before any computation specific to $2I$ begins. The actual lowest eigenvalue exceeds this floor. The following sections compute it exactly.

## II. Three Vacua

Flat $\text{SU}(2)$ connections on $M$ are classified by $\text{Hom}(2I, \text{SU}(2))/\text{conj}$. A homomorphism $\rho: 2I \to \text{SU}(2)$ is equivalently a 2-dimensional unitary representation with determinant 1. The normal subgroups of $2I$ are $\{1\}$, $\{\pm 1\}$, and $2I$ itself, yielding three possibilities: the trivial map, and two inequivalent faithful embeddings distinguished by their character values on elements of order 10.

| Generation | Vacuum | Adjoint rep | 2I irrep | $E_8$ position |
|---|---|---|---|---|
| 1st | $\rho_{\text{triv}}$ | trivial | $R_0$ | origin |
| 2nd | $\rho_{\text{std}}$ | 3a | $R_3$ | near origin |
| 3rd | $\rho_{\text{gal}}$ | 3b | $R_4$ | branch tip |

The standard and Galois embeddings are distinguished by the golden ratio: $\rho_{\text{std}}$ has trace $\varphi = (1+\sqrt{5})/2$ on order-10 elements, while $\rho_{\text{gal}}$ has trace $\bar\varphi = (1-\sqrt{5})/2$. Since $\text{SU}(2)$ conjugation preserves traces and $\varphi \neq \bar\varphi$, the two define distinct conjugacy classes. The kernel $\{\pm 1\}$ case (factoring through $A_5$) produces no additional class because $A_5$ has no faithful 2-dimensional representation.

### Vacuum isolation

Vanishing $H^1(M;\,\text{ad}\,\rho) = 0$ at each irreducible flat connection guarantees that no continuous moduli connect the families and no massless Goldstone modes bridge them. Each vacuum is isolated with positive-definite Hessian. The number three is the count of flat $\text{SU}(2)$ connections on $S^3/2I$. Three vacua, three families.

## III. The Spectral Filter

The McKay graph of $2I$ is the extended (affine) $E_8$ Dynkin diagram. Each node corresponds to an irreducible representation of $2I$; the edges encode tensor product with the fundamental 2-dimensional representation. The restriction of the spin-$j$ representation of $\text{SU}(2)$ to $2I$ follows the McKay recursion along this graph.

### Coexact spectrum on S^3

On the round $S^3$ of radius $R$, coexact (divergence-free) 1-forms organize into levels $k = 1, 2, 3, \ldots$ with eigenvalue:

$$\lambda_k = \frac{(k+1)^2}{R^2}$$

On the quotient $M = S^3/2I$, physical modes at level $k$ must satisfy a twisted equivariance condition: the adjoint representation $\sigma$ of the vacuum must appear in the McKay decomposition of the spin content at that level. If $\sigma$ is absent, the level is filtered out entirely.

### Standard vacuum (3a)

The adjoint representation 3a is precisely $V_1 \lvert_{2I}$: it appears at the first spin level. The first allowed coexact mode sits at $k = 1$:

$$\Delta^2 = \frac{(1+1)^2}{R^2} = \frac{4}{R^2}$$

### Galois vacuum (3b)

The adjoint 3b does not appear until $j = 3$ in the McKay decomposition, reflecting its position at graph distance 6 from $R_0$ on the $E_8$ graph (through the branch at $R_8$). The icosahedral symmetry filters all fluctuation modes across the first four coexact levels. The first allowed mode sits at $k = 5$:

$$\Delta^2 = \frac{(5+1)^2}{R^2} = \frac{36}{R^2}$$

| Vacuum | Adjoint | First allowed k | Gap | Enhancement |
|---|---|---|---|---|
| $\rho_{\text{triv}}$ | trivial ($R_0$) | 1 | $4/R^2$ | 1x |
| $\rho_{\text{std}}$ | 3a ($R_3$) | 1 | $4/R^2$ | 1x |
| $\rho_{\text{gal}}$ | 3b ($R_4$) | 5 | $36/R^2$ | 9x |

The 9x enhancement is topological: it counts filtered levels, not metric parameters. The mass hierarchy between generations follows from this filter. Each vacuum accesses different levels of the McKay decomposition. The Galois vacuum sees the largest gap, consistent with the heaviest family.

## IV. Three Pillars

The mass gap result rests on three independent arguments, each verifiable with standard mathematical tools:

| Pillar | Method | What it establishes |
|---|---|---|
| Curvature floor | Riemannian geometry (Weitzenböck) | $\lambda \geq 2/R^2$ for all gauge fluctuations around any flat connection on any $S^3$ quotient. The gap exists. |
| Vacuum isolation | Algebraic topology (Floer theory) | Finiteness of $\pi_1 = 2I$ gives a finite moduli space. $H^1 = 0$ at each irreducible flat: no moduli, no Goldstone modes. |
| Spectral computation | Finite group theory (McKay) | Explicit gap values at each vacuum. Icosahedral filtering at the Galois sector produces the 9x enhancement. |

### What is topological vs metric-dependent

The existence of the gap, the discreteness of vacua, the vanishing $H^1$, the number of filtered levels, and the 9x enhancement are all topological. The numerical value of $\lambda_{\min}$ scales as $1/R^2$ and is metric-dependent.

### Connection to MIT

Within Mode Identity Theory, $R$ is fixed by cosmological parameters, making $\Delta^2 = 4/R^2$ a determinate physical constant. The same positive curvature $\text{Ric}(S^3) = 2/R^2$ that guarantees confinement here enters the Gauss-Codazzi conversion that produces Λ. One geometry, two consequences: the cosmological constant and the mass gap share a common origin in the curvature of $S^3$.

The $2I$ structure performs three roles: it partitions phase space into the 120-domain (the scaling law), it filters gauge fluctuations into three isolated vacua with computed mass gaps (this result), and it provides the spectral geometry whose McKay multiplicities are the $E_8$ root system.

## V. Falsification

Every prediction is checkable by finite computation.

| Prediction | Falsified if |
|---|---|
| 3 conjugacy classes in $\text{Hom}(2I, \text{SU}(2))/\text{conj}$ | Additional class constructed, or standard and Galois proved conjugate |
| $H^1(M;\,\text{ad}\,\rho) = 0$ at irreducible flats | Nonzero cohomology demonstrated |
| First 3b appearance at $j = 3$ in McKay table | Character sum yields different result |
| Galois gap at $k = 5$ | Coexact 1-form of 3b type found at lower $k$ |

### Physical predictions (conditional on compact topology)

| Prediction | Test |
|---|---|
| Mass gap scales as $1/R^2$ | Lattice Yang-Mills on $S^3/2I$ geometry |
| 9x enhancement at Galois vacuum | Lattice measurement of sector-resolved spectrum |
| Confinement scale set by cosmological $R$ | Comparison with observed $\Lambda_{\text{QCD}}$ |

---

SU(2) Yang-Mills on the Poincare homology sphere has a positive mass gap. Positive curvature forces it. Three isolated vacua produce three families: the McKay correspondence filters the Galois sector through four empty levels, yielding a ninefold enhancement at the branch tip of the $E_8$ graph. The existence of the gap is topological, its value is geometric. The computation reduces to finite group representation theory, standard gauge theory, and Riemannian geometry.

*On curved ground, confinement is easy money.*
