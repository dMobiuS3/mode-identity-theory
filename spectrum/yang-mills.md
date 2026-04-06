# Easy Money: Yang-Mills on the Poincaré Homology Sphere

The Millennium Prize asks whether pure Yang-Mills theory on $\mathbb{R}^4$ has a positive mass gap. On flat space, confinement must emerge dynamically. On the Poincaré Homology Sphere $M = S^3/2I$, the answer is forced by geometry. 

Positive Ricci curvature provides a universal floor. The finite fundamental group yields exactly three isolated vacua: trivial, standard, and Galois conjugate. The McKay correspondence for the extended $E_8$ diagram filters the spectrum at each vacuum, producing a ninefold enhancement at the Galois sector. 

The same curvature that enters the Λ conversion guarantees confinement.

| Property | Value |
|---|---|
| Curvature floor | $\lambda \geq 2/R^2$ (universal, Weitzenböck) |
| Vacua | 3 isolated (trivial, standard, Galois) |
| Gap (trivial, standard) | $\Delta^2 = 4/R^2$ |
| Gap (Galois) | $\Delta^2 = 36/R^2$ (9x enhancement) |
| Three vacua | Three particle generations |

## I. The Geometry

The Weitzenböck identity on $S^3$ decomposes the gauge-covariant Hodge Laplacian on bundle-valued 1-forms. In the Hamiltonian formulation of Yang-Mills on $M \times \mathbb{R}$, temporal gauge ($A_0 = 0$) with the Coulomb condition ($d_A^\ast a = 0$) reduces the linearized equation around a flat connection to $\partial_t^2 a + \Delta_{\mathrm{Hodge}} a = 0$. Solutions oscillate as $e^{i\omega t}$ with $\omega^2 = \lambda$, so the spectral gap is the lowest eigenvalue of $\Delta_{\mathrm{Hodge}}$ on the coexact subspace. For a flat connection ($F_A = 0$), the identity reduces to:

$$\Delta_{\mathrm{Hodge}} = \nabla_A^\ast \nabla_A + \mathrm{Ric}$$

On the round $S^3$ of radius $R$, the Ricci tensor is $R_{ij} = (2/R^2)\,g_{ij}$. Since $\nabla_A^\ast \nabla_A \geq 0$ and $\mathrm{Ric} = 2/R^2 > 0$, every coexact (divergence-free) gauge fluctuation around any flat connection satisfies:

$$\lambda_{\min} \geq \frac{2}{R^2}$$

This bound is universal: it holds for any quotient $S^3/\Gamma$ inheriting the round metric, independent of $\Gamma$ and the choice of flat connection. The existence of a positive spectral floor is topological: $S^3/2I$ has finite fundamental group and universal cover $S^3$, so it is a spherical space form and admits the round metric with $\mathrm{Ric} > 0$. On any metric with $\mathrm{Ric} \geq \kappa > 0$, the Weitzenböck bound gives $\lambda_{\min} \geq \kappa$; the existence of a gap is guaranteed by the topology, its numerical value by the metric. The specific value $2/R^2$ uses the round metric. The actual lowest eigenvalue exceeds this floor. The following sections compute it exactly.

## II. Three Vacua

Flat $\mathrm{SU}(2)$ connections on $M$ are classified by $\mathrm{Hom}(2I, \mathrm{SU}(2))/\mathrm{conj}$. A homomorphism $\rho: 2I \to \mathrm{SU}(2)$ is equivalently a 2-dimensional unitary representation with determinant 1. The character table of $2I$ has exactly nine irreducible representations, of which exactly two have dimension 2: $R_1$ and $R_7$. Both are faithful. The only remaining possibility is the trivial map ($\rho(g) = I$). This gives three conjugacy classes total.

| Generation | Vacuum | Adjoint rep | 2I irrep | $E_8$ position |
|---|---|---|---|---|
| 1st | $\rho_{\mathrm{triv}}$ | trivial | $R_0^{\oplus 3}$ | origin |
| 2nd | $\rho_{\mathrm{std}}$ | 3a | $R_2$ | near origin |
| 3rd | $\rho_{\mathrm{gal}}$ | 3b | $R_8$ | branch tip |

The standard and Galois embeddings are distinguished by the golden ratio: $\rho_{\mathrm{std}}$ has trace $\varphi = (1+\sqrt{5})/2$ on order-10 elements, while $\rho_{\mathrm{gal}}$ has trace $\bar\varphi = (1-\sqrt{5})/2$. Since $\mathrm{SU}(2)$ conjugation preserves traces and $\varphi \neq \bar\varphi$, the two define distinct conjugacy classes. The kernel $\{\pm 1\}$ case (factoring through $A_5$) produces no additional class because $A_5$ has no faithful 2-dimensional representation.

### Vacuum isolation

Each vacuum is isolated: vanishing $H^1(M;\,\mathrm{ad}\,\rho) = 0$ at each flat connection guarantees that no continuous moduli connect the families and no massless modes bridge them. For any finite group $G$ and any $\mathbb{R}G$-module $V$, Maschke's theorem ($|G|$ invertible in $\mathbb{R}$) implies $H^n(G;\,V) = 0$ for all $n \geq 1$. Applied with $G = 2I$ and $V = \mathfrak{su}(2)$ under $\mathrm{Ad} \circ \rho$: $H^1(2I;\,\mathfrak{su}(2)_{\mathrm{Ad} \circ \rho}) = 0$ for every $\rho$, irreducible or trivial. For the trivial connection specifically, $H^1(M;\,\mathrm{ad}\,\rho_{\mathrm{triv}}) = H^1(M;\,\mathbb{R})^3$; since $\pi_1(M) = 2I$ is a perfect group ($2I$ equals its own commutator subgroup), $H_1(M;\,\mathbb{Z}) = 0$, so $H^1(M;\,\mathbb{R}) = 0$ by universal coefficients. Both routes give the same conclusion.

Each vacuum is stable on the physical fluctuation space. This is independent of the $H^1$ argument: the Weitzenböck bound from Section I applies to coexact (divergence-free) 1-forms, which are precisely the physical gauge fluctuations after Coulomb gauge-fixing. Since $\lambda \geq 2/R^2 > 0$ for every such mode, no physical fluctuation has zero or negative eigenvalue. Isolation (no directions to move) and stability (no soft modes) are established by separate mechanisms. The number three is the count of flat $\mathrm{SU}(2)$ connections on $S^3/2I$. The identification of three vacua with three particle generations is a structural observation within Mode Identity Theory; it is not a consequence of the Yang-Mills analysis presented here. The mathematical result is that exactly three isolated, stable vacua exist.

## III. The Spectral Filter

The McKay graph of $2I$ is the extended (affine) $E_8$ Dynkin diagram. Each node corresponds to an irreducible representation of $2I$; the edges encode tensor product with the fundamental 2-dimensional representation. The restriction of the spin-j representation of $\mathrm{SU}(2)$ to $2I$ follows the McKay recursion along this graph. Since each recursion step extends the reachable subgraph by at most one edge, an irrep at graph distance $d$ from $R_0$ requires at least $d$ steps to first appear: distance controls the filtration depth.

### Coexact spectrum on $S^3$

On the round $S^3$ of radius $R$, coexact (divergence-free) 1-forms organize into levels $k = 1, 2, 3, \ldots$ with eigenvalue:

$$\lambda_k = \frac{(k+1)^2}{R^2}$$

On $S^3 = \mathrm{SU}(2)$, the Hodge Laplacian commutes with the isometry group $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$, so its eigenvalue on an irreducible component $(j_L, j_R)$ takes the form $\lambda = a \cdot j_L(j_L+1) + b \cdot j_R(j_R+1) + c$. Hodge star symmetry ($*$ swaps $j_L \leftrightarrow j_R$) forces $a = b$. Agreement with the scalar Laplacian on exact 1-forms at $(j, j)$ fixes $a = 2/R^2$, $c = 0$. Coexact 1-forms appear at $(j_R \pm 1, j_R)$; both series yield eigenvalue $(k+1)^2/R^2$ with $k = 1, 2, 3, \ldots$

On the quotient $M = S^3/2I$, physical modes at level $k$ must satisfy a twisted equivariance condition: the adjoint representation $\mathrm{ad}(\sigma)$ of the vacuum must appear in the $2I$-decomposition of the 1-form representation at that level. By Frobenius reciprocity, the dimension of the $\mathrm{ad}(\sigma)$-isotypic equivariant subspace at level $k$ is $\langle \mathrm{ad}(\sigma),\, (V_{k-1} \oplus V_{k+1})|_{2I} \rangle_{2I}$. When this inner product vanishes, no equivariant section exists and the level is filtered out entirely.

### Representation content at each level

The left-$\mathrm{SU}(2)$ content of coexact 1-forms at eigenvalue $(k+1)^2/R^2$ is $V_{k-1} \oplus V_{k+1}$, combining the two coexact series identified above. Restricting to $2I$ via the McKay recursion $V_{l+1}|_{2I} = R_1 \otimes V_l|_{2I} - V_{l-1}|_{2I}$ gives:

$$V_0 = R_0, \quad V_1 = R_1, \quad V_2 = R_2, \quad V_3 = R_3, \quad V_4 = R_4, \quad V_5 = R_5, \quad V_6 = R_6 \oplus R_8$$

The $2I$ content of gauge-valued 1-forms at each coexact level is therefore $(V_{k-1} \oplus V_{k+1})|_{2I}$:

| $k$ | $\lambda_k$ | $V_{k-1}|_{2I}$ | $V_{k+1}|_{2I}$ | Combined $2I$ content | $R_0$? | $R_2$? | $R_8$? |
|---|---|---|---|---|---|---|---|
| 1 | $4/R^2$ | $R_0$ | $R_2$ | $R_0,\; R_2$ | ✓ | ✓ | — |
| 2 | $9/R^2$ | $R_1$ | $R_3$ | $R_1,\; R_3$ | — | — | — |
| 3 | $16/R^2$ | $R_2$ | $R_4$ | $R_2,\; R_4$ | — | ✓ | — |
| 4 | $25/R^2$ | $R_3$ | $R_5$ | $R_3,\; R_5$ | — | — | — |
| 5 | $36/R^2$ | $R_4$ | $R_6 \oplus R_8$ | $R_4,\; R_6,\; R_8$ | — | — | ✓ |

Each vacuum requires its adjoint representation to appear in the combined column. The trivial vacuum ($\mathrm{ad} = 3 \times R_0$: trivial $2I$-action on $\mathfrak{su}(2)$) requires $R_0$; the standard vacuum ($\mathrm{ad} = R_2$) requires $R_2$. Both pass at $k = 1$. The Galois vacuum ($\mathrm{ad} = R_8$) requires $R_8$, which is absent at $k = 1$ through $k = 4$ and first appears at $k = 5$. Four levels are filtered. The computation is finite and verifiable from the character table of $2I$.

### Gap values

Trivial and standard vacua: first allowed mode at $k = 1$:

$$\Delta^2 = \frac{(1+1)^2}{R^2} = \frac{4}{R^2}$$

Galois vacuum: first allowed mode at $k = 5$:

$$\Delta^2 = \frac{(5+1)^2}{R^2} = \frac{36}{R^2}$$

The $k = 5$ entry is read directly from the table above: $R_8$ is absent from the combined $2I$ content at every level below $k = 5$.

| Vacuum | Adjoint | First allowed k | Gap | Enhancement |
|---|---|---|---|---|
| $\rho_{\mathrm{triv}}$ | trivial ($R_0^{\oplus 3}$) | 1 | $4/R^2$ | 1x |
| $\rho_{\mathrm{std}}$ | 3a ($R_2$) | 1 | $4/R^2$ | 1x |
| $\rho_{\mathrm{gal}}$ | 3b ($R_8$) | 5 | $36/R^2$ | 9x |

The level index gap is topological: the Galois vacuum is filtered through four empty levels because $R_8$ sits at graph distance 6 from the trivial node. The ratio $9 = (5+1)^2/(1+1)^2$ uses the round-metric eigenvalue formula and is metric-dependent. The mass hierarchy between generations follows from this filter. Each vacuum accesses different levels of the McKay decomposition. The Galois vacuum sees the largest gap. Vacuum-to-generation assignment is open; no universal mass hierarchy holds across irreps.

## IV. Three Pillars

The spectral gap result rests on three independent arguments, each verifiable with standard mathematical tools:

| Pillar | Method | What it establishes |
|---|---|---|
| Curvature floor | Riemannian geometry (Weitzenböck) | $\lambda \geq 2/R^2$ for all coexact gauge fluctuations around any flat connection on any $S^3$ quotient. The gap exists. |
| Vacuum isolation | Algebraic topology | Finiteness of $\pi_1 = 2I$ gives a finite moduli space. $H^1 = 0$ at each flat connection: no moduli, no massless modes. |
| Spectral computation | Finite group theory (McKay) | Explicit gap values at each vacuum. Icosahedral filtering at the Galois sector produces the 9x enhancement. |

### What is topological vs metric-dependent

The existence of the gap, the discreteness of vacua, the vanishing $H^1$, and the number of filtered levels are all topological. The 9x enhancement ratio and the numerical value of $\lambda_{\min}$ are metric-dependent, following from the round-metric eigenvalue formula $\lambda_k = (k+1)^2/R^2$.

### Connection to MIT

Within Mode Identity Theory, $R$ is fixed by cosmological parameters, making $\Delta^2 = 4/R^2$ a determinate physical constant. The same positive curvature $\mathrm{Ric}(S^3) = 2/R^2$ that guarantees confinement here enters the Gauss-Codazzi conversion that produces Λ. One geometry, two consequences: the cosmological constant and the spectral gap share a common origin in the curvature of $S^3$.

The $2I$ structure performs three roles: it partitions phase space into the 120-domain (the scaling law), it filters gauge fluctuations into three isolated vacua with computed spectral gaps (this result), and it provides the spectral geometry whose McKay multiplicities are the $E_8$ root system.

## V. Falsification

Every prediction is checkable by finite computation.

| Prediction | Falsified if |
|---|---|
| 3 conjugacy classes in $\mathrm{Hom}(2I, \mathrm{SU}(2))/\mathrm{conj}$ | Additional class constructed, or standard and Galois proved conjugate |
| $H^1(M;\,\mathrm{ad}\,\rho) = 0$ at irreducible flats | Nonzero cohomology demonstrated |
| First 3b appearance at $k = 5$ ($R_8$ first in $V_6|_{2I}$) | Character sum yields $R_8$ at lower $k$ |
| Galois gap at $k = 5$ | Coexact 1-form of 3b type found at lower $k$ |

### Physical predictions (conditional on compact topology)

| Prediction | Test |
|---|---|
| Spectral gap scales as $1/R^2$ | Lattice Yang-Mills on $S^3/2I$ geometry |
| 9x enhancement at Galois vacuum | Lattice measurement of sector-resolved spectrum |

---

SU(2) Yang-Mills on the Poincaré Homology Sphere has a positive spectral gap. Positive curvature forces it. Three isolated vacua produce three families. The McKay correspondence filters the Galois sector through four empty levels, yielding a ninefold enhancement at the branch tip of the $E_8$ graph. The level gap is topological; the eigenvalues are geometric. The computation reduces to finite group representation theory, standard gauge theory, and Riemannian geometry.

*On curved ground, confinement is easy money.*
