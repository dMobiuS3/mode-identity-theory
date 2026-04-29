/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /

---

# Ground Eigenvalue of the Twisted Laplacian on a Constant-Curvature Möbius Band in the Reduced Anti-Periodic Sector

[![Ground mode eigenvalue](https://img.youtube.com/vi/1AZfOvcrIdk/mqdefault.jpg)](https://www.youtube.com/watch?v=1AZfOvcrIdk)

We study the ground eigenvalue of the twisted Laplace-Beltrami operator in the $w$-constant anti-periodic sector (Sector $\mathcal{A}$) on the Möbius band constructed as the quotient of a spherical band on the great $S^2 \subset S^3$ by an orientation-reversing isometry. The quotient inherits the metric $ds^2 = dy^2 + \cos^2(y/R)\,dw^2$, which carries constant Gaussian curvature $K = 1/R^2$, with the metric degenerating at the interior cone point $y = \pi R/2$. The Möbius band inherits constant curvature $K = 1/R^2$ from the covering $S^2$; the spectral problem reduces to a regular-branch Sturm-Liouville eigenvalue problem on two smooth half-intervals joined at the interior cone point.

Two independent paths establish that the Sector $\mathcal{A}$ ground eigenvalue equals the surface scalar curvature exactly: $\lambda_0 = R_\Sigma = 2/R^2$. The upper bound follows from a direct eigenfunction computation with explicit Rayleigh quotient. The lower bound follows from the Bochner identity, with boundary flux vanishing because the boundary curves $w = \pm W$ are geodesics of the surface. Both bounds are established via cone point excision: near $y = \pi R/2$ the regular-branch eigenfunction satisfies $u' = O(\delta)$, so the excision boundary contributions vanish as $O(\epsilon^2)$.

The flat strip gives $\lambda_0 = 1/R^2 = R_\Sigma/2$. The constant positive curvature $K = 1/R^2$ inherited from $S^2$ supplies the missing factor of 2.

---

## 1. Introduction

The spectral geometry of non-orientable surfaces has been studied extensively in the closed case. The Lichnerowicz bound $\lambda_1 \geq R_\Sigma$ for the first nonzero eigenvalue of the Laplace-Beltrami operator on closed Riemannian manifolds with positive Ricci curvature is classical, and the Obata theorem characterizes the equality case. For the closed non-orientable surface $\mathbb{RP}^2 = S^2/\{\pm 1\}$, the twisted Laplacian acting on functions satisfying anti-periodic boundary conditions under the deck transformation has ground eigenvalue $\lambda_0 = 2/R^2 = R_\Sigma$, recoverable from the odd spherical harmonics at $\ell = 1$ (Chavel 1984, Ch. 3).

The open case has not received the same treatment. The Möbius band is the canonical non-orientable surface with boundary. Its twisted Laplacian on the flat strip is well understood, with ground eigenvalue $\lambda_0 = \pi^2/L^2$ in the anti-periodic sector. Curved Möbius band spectral theory has been studied by Kalvoda, Krejčiřík, and Zahradová (2020) for strips embedded in $\mathbb{R}^3$ with non-constant curvature in the thin-strip limit. The present model differs: the Möbius band is constructed as the quotient of a spherical band on $S^2 \subset S^3$ by an orientation-reversing isometry, inheriting a locally totally geodesic metric with constant curvature $K = 1/R^2$, and the computation yields an exact ground eigenvalue in the reduced anti-periodic sector rather than an asymptotic.

The problem is posed as a regular-branch Sturm-Liouville eigenvalue problem on two smooth half-intervals with continuity at the cone point, where the metric degenerates. Reilly (1977) extends the Lichnerowicz bound to compact manifolds with convex boundary via a Hessian operator argument; Escobar (1990) establishes sharp Neumann eigenvalue bounds on manifolds with boundary under Ricci and boundary curvature conditions. The totally geodesic boundary case, where the second fundamental form vanishes, is the cleanest instance of that framework. The present paper follows Reilly's method; integrating the Bochner formula and controlling the boundary term; adapted to this singular model via cone point excision.

We prove that, in Sector $\mathcal{A}$, the lowest eigenvalue satisfies:

$$\lambda_0 = R_\Sigma = \frac{2}{R^2}$$

The flat strip yields $\lambda_0 = 1/R^2 = R_\Sigma/2$. The constant positive curvature $K = 1/R^2$ inherited from $S^2$ supplies the missing factor of 2. Two independent paths establish this identity. Section 5 provides direct computation via the ground eigenfunction $\sin(y/R)$ with explicit Rayleigh quotient upper bound. Section 6 provides a Bochner identity argument yielding the lower bound independently. The two bounds meet at equality in Section 7.

---

## 2. Setup

Let $C \subset S^2_R$ be a reference great circle. For each $w \in [-W, W]$, let $\gamma_w$ denote the meridional geodesic orthogonal to $C$ at the point of $C$ with arclength parameter $w$. The strip

$$\widetilde{M} = \{(y, w) : 0 \leq y \leq \pi R,\; -W \leq w \leq W\}$$

carries the metric $ds^2 = dy^2 + \cos^2(y/R)\,dw^2$ (derived in Section 4 from the $S^2$ quotient construction), where $y$ is arclength along each meridian and $w$ labels meridians by arclength along $C$. Its boundary components are the curves $w = \pm W$. The Möbius band $M$ is obtained by the twisted identification

$$(0, w) \sim (\pi R, -w)$$

This identification pairs each point on the $y = 0$ edge with a reflected point on the $y = \pi R$ edge. Traversing the meridional direction once returns a field to the opposite transverse edge; a second traversal returns to the start. The boundary $\partial M = S^1$ is a single closed loop traversing the band twice. The boundary loop is embedded as a great circle of $S^3$ of radius $R$ and therefore has circumference $2\pi R$; since the loop traverses the band twice, the meridional period satisfies $L = \pi R$.

**The problem studied in this paper.** We study one specific eigenvalue problem: the twisted Laplace-Beltrami operator on this surface in Sector $\mathcal{A}$, with the metric inherited from the $S^2$ quotient construction derived in Section 4. The problem is stated as a regular-branch Sturm-Liouville problem on two half-intervals with an interior transmission condition at the cone point $y = \pi R/2$.

A function $u$ is *admissible* if:

- $u$ is $C^2$ on each of $(0, \pi R/2)$ and $(\pi R/2, \pi R)$
- $u$ is continuous at $y = \pi R/2$
- $u(\pi R) = -u(0)$ and $u'(\pi R) = -u'(0)$ &emsp; (anti-periodic condition)

The eigenvalue problem is: find $\lambda > 0$ and admissible $u \not\equiv 0$ satisfying

$$-\Delta_g\, u = \lambda\, u \qquad \text{on each smooth piece}$$

where $\Delta_g u = u'' - R^{-1}\tan(y/R)\,u'$ is the Laplace-Beltrami operator for the metric $ds^2 = dy^2 + \cos^2(y/R)\,dw^2$. We refer to this as **Sector $\mathcal{A}$**: the reduced $w$-constant admissible regular-branch anti-periodic sector.

**The cone point: cover vs. quotient.** At $y = \pi R/2$ the metric coefficient $\cos(y/R)$ vanishes. On the covering spherical band $\widetilde{M}$, this point is the north pole of a smooth $S^2$: the apparent coordinate singularity is removable in polar coordinates, and no special analysis is needed. On the quotient Möbius band $M$, the situation differs. The transverse interval $[-W, W]$ is metrically collapsed to a single point at $y = \pi R/2$, producing a cone point with cone angle $2W/R$. 

When $W = \pi R$ the cone angle is $2\pi$ and the singularity is removable (the quotient is $\mathbb{RP}^2$). When $W < \pi R$ the cone angle is less than $2\pi$, producing a genuine angular deficit and a metric singularity that is absent from the cover. The Sturm-Liouville analysis of Sections 5 and 6 addresses this quotient singularity. In Sector $\mathcal{A}$ (the $w$-constant sector), the reduction to an ODE in $y$ alone means the cone angle does not enter the reduced eigenequation directly; the singularity manifests as the vanishing of the coefficient $|\cos(y/R)|$ in the Sturm-Liouville weight, producing a singular endpoint at $y = \pi R/2$ regardless of $W$. The Gaussian curvature $K = 1/R^2$ extends continuously to the cone point on the smooth locus. The ground eigenfunction $u_0 = \sin(y/R)$ takes its maximum value 1 there with $u_0' = 0$.

**Boundary conditions.** The Möbius identification imposes the longitudinal condition directly and the transverse edges are taken as free:

- *Longitudinal (anti-periodic):* $\psi(\pi R, -w) = -\psi(0, w)$, imposed by the Möbius identification.
- *Transverse (Neumann):* $\partial_w \psi\big|_{w = \pm W} = 0$, free boundary at the transverse edges.

**Scope.** This paper establishes the ground eigenvalue in Sector $\mathcal{A}$. Section 5 exhibits the explicit ground eigenfunction. Section 6 establishes the lower bound. Section 7 combines them.

**Self-adjoint extension at the cone point.** The singular endpoint $y = \pi R/2$ is of limit-circle type in the Sturm-Liouville classification: both the regular branch $u \sim 1$ (with $u' = O(\delta)$) and the logarithmic branch $u \sim \log|\delta|$ (with $u' \sim 1/\delta$) are square-integrable with respect to the weight $|\cos(y/R)|\,dy \sim |\delta|/R\,d\delta$ near the cone point. At a limit-circle endpoint, square-integrability alone does not determine a unique self-adjoint operator; a boundary condition must be specified. We impose the Friedrichs extension (Friedrichs 1934), which is characterized by the requirement that functions in the operator domain have finite Dirichlet integral:

$$\int |\nabla u|^2\,dA = \int (u')^2\,|\cos(y/R)|\,dy\,dw < \infty$$

The logarithmic branch fails this condition: $(u')^2 \sim 1/\delta^2$ and $|\cos(y/R)| \sim |\delta|/R$, giving $\int (u')^2|\cos|\,d\delta \sim \int \delta^{-1}\,d\delta = \infty$. The Friedrichs extension therefore coincides with the regular-branch condition (continuity and boundedness at $y = \pi R/2$). Derivative matching at the cone point then follows: the Friedrichs extension selects the regular branch, whose Frobenius expansion (Section 5) gives $u = a_0 + a_2\delta^2 + O(\delta^4)$ with $u' = 2a_2\delta + O(\delta^3) = O(\delta) \to 0$ as $\delta \to 0$, so $u'(\pi R/2) = 0$ from each side. This is not separately imposed; it is a consequence of the finite Dirichlet integral condition selecting the regular branch, combined with the leading-order balance in the eigenequation.

The Friedrichs extension is the self-adjoint extension associated with the closed Dirichlet form, so the Rayleigh quotient characterizes the eigenvalues for the operator considered here. The upper bound of Section 5 (via the Rayleigh quotient of a trial function in the Friedrichs domain) and the lower bound of Section 6 (via the Bochner identity on the excised manifold, with excision boundary terms vanishing because $u' = O(\delta)$ in the Friedrichs domain) are therefore valid for this operator and yield the same eigenvalue.

**Correspondence between 2D and 1D domains.** For $w$-constant functions, the 2D Dirichlet integral factors: $\int_M |\nabla u|^2\,dA = 2W \int_0^{\pi R} (u')^2\,|\cos(y/R)|\,dy$. The finiteness condition defining the Friedrichs domain is therefore equivalent in the 2D and 1D settings: the 2D Friedrichs domain restricted to Sector $\mathcal{A}$ coincides with the 1D Friedrichs domain defined by the regular-branch condition. The Bochner bound (which operates on the 2D manifold) and the Rayleigh quotient (which operates on the reduced 1D problem) therefore act on the same operator domain, which is why the two bounds can meet at equality.

---

## 3. The Flat Strip Baseline

On the flat strip, the metric is Euclidean: $ds^2 = dy^2 + dw^2$. The Laplace-Beltrami operator reduces to the standard Laplacian $\Delta = \partial_y^2 + \partial_w^2$. In the anti-periodic sector with $\psi$ constant in $w$, the eigenproblem reduces to:

$$-\frac{d^2 u}{dy^2} = \lambda\, u, \qquad u(y + L) = -u(y)$$

The general solution is $u \propto e^{iky}$. The anti-periodic condition requires $e^{ikL} = -1$, satisfied when $kL = (2m+1)\pi$ for integer $m$. The ground mode is $m = 0$, giving $k = \pi/L$ and:

$$\lambda_0^{\text{flat}} = \frac{\pi^2}{L^2}$$

**Fixing $L$ from the boundary.** The boundary $\partial M = S^1$ is embedded as a great circle of $S^3$ of radius $R$. Its circumference is $2\pi R$. The Möbius identification $(y + L, w) \sim (y, -w)$ means a path traversing the meridional direction once arrives at the opposite transverse edge, not the starting point; a second traversal is required to return to the start, so the boundary loop has length $2L$:

$$2L = 2\pi R \qquad \Rightarrow \qquad L = \pi R$$

Substituting:

$$\lambda_0^{\text{flat}} = \frac{\pi^2}{(\pi R)^2} = \frac{1}{R^2}$$

The scalar curvature of a constant-curvature surface with $K = 1/R^2$ is $R_\Sigma = 2K = 2/R^2$. The flat strip therefore yields:

$$\lambda_0^{\text{flat}} = \frac{1}{R^2} = \frac{R_\Sigma}{2}$$

The constant positive curvature inherited from $S^2$ supplies the missing factor of 2 as developed in Section 4.

---

## 4. The Quotient Construction and Inherited Metric

The Möbius band $M$ is constructed as the quotient of a spherical band on the great $S^2 \subset S^3$ by an orientation-reversing isometry. The great $S^2$ is a totally geodesic submanifold of $S^3$; the Möbius band itself is not a totally geodesic submanifold of $S^3$. The Möbius band inherits a locally totally geodesic metric from the covering spherical band: the intrinsic geometry at every smooth point is identical to that of $S^2$, carrying constant Gaussian curvature $K = 1/R^2$. The spectral problem is well-posed on this abstract Riemannian manifold. Throughout this section, $K_{ij}$ denotes the extrinsic curvature (second fundamental form) of $S^2$ in $S^3$, while $K$ denotes the intrinsic Gaussian curvature of the surface.

**The covering space.** Realize $S^3$ as the simply connected closed 3-manifold of constant sectional curvature $1/R^2$. The great $S^2 \subset S^3$ is a totally geodesic 2-sphere: every geodesic of $S^2$ is a great circle of $S^3$, so the second fundamental form vanishes ($K_{ij} = 0$). The spherical band $\widetilde{M}$ defined in Section 2 is an open subset of this $S^2$. The orientation-reversing isometry

$$(x_1, x_2, x_3, x_4) \mapsto (-x_1, -x_2, -x_3, x_4)$$

is an isometry of $S^3$ that restricts to the antipodal map on the equatorial $S^2$, sending each point of the spherical band to its antipode. The Möbius band $M$ is the quotient of $\widetilde{M}$ by this identification, equivalently by imposing the twisted identification $(0, w) \sim (\pi R, -w)$ from Section 2. The quotient is an abstract Riemannian manifold that is locally isometric to $S^2$ but globally non-orientable. Away from the cone point $y = \pi R/2$, the Möbius band is locally modeled on $S^2$ and carries the same locally totally geodesic metric. Its boundary consists of the two curves $w = \pm W$, which together form a single closed loop $\partial M = S^1$ traversing the band twice.

**The induced metric.** Because the covering $S^2 \subset S^3$ is totally geodesic, its intrinsic metric equals the restriction of the ambient metric and intrinsic geodesics coincide with ambient geodesics. The Möbius band inherits this metric through the quotient. The following calculation is intrinsic to $S^2(R)$. In Fermi coordinates on the totally geodesic $S^2 \subset S^3$, let $w$ denote arclength along a reference great circle and let $y$ denote arc-length parameter along a meridional geodesic of $S^2$, with $y = 0$ at the reference great circle. The normal Jacobi field satisfies

$$J'' + \frac{1}{R^2}J = 0, \qquad J(0) = 1, \quad J'(0) = 0$$

so $J(y) = \cos(y/R)$. Hence the induced metric is $ds^2 = dy^2 + \cos^2(y/R)\,dw^2$, with $\cos(y/R)$ vanishing at $y = \pi R/2$. The associated Riemannian density is therefore $|\cos(y/R)|\,dy\,dw$. The parameter $y$ runs from $0$ to $\pi R$, passing through the pole at $y = \pi R/2$ and reaching the antipodal great circle at $y = \pi R$.

**The cone singularity.** At $y = \pi R/2$ the metric coefficient $\cos^2(y/R)$ vanishes. Setting $\delta = y - \pi R/2$ and $\rho = |\delta|$, the metric near $\rho = 0$ takes the form $ds^2 \approx d\rho^2 + (\rho/R)^2\,dw^2$, with total angular range $2W/R < 2\pi$ for $W < \pi R$: a genuine cone with deficit angle $2\pi - 2W/R$. On the covering $S^2$, $w$ ranges over $2\pi R$ and the deficit vanishes; the quotient identification restricts the range and creates the singularity. The Gaussian curvature $K = 1/R^2$ extends continuously to the cone point on the smooth locus. The Friedrichs extension and excision argument are detailed in Sections 2 and 6.

**The width parameter.** The band has transverse half-width $W \in (0, \pi R)$. At $W = \pi R$ the boundary vanishes and the band closes to $\mathbb{RP}^2$. The eigenvalue $\lambda_0 = 2/R^2$ is independent of $W$: it appears in neither the Rayleigh quotient ratio nor the Bochner bound, both of which involve $W$ only through overall factors that cancel. The cone angle at $y = \pi R/2$ is $2W/R$, which equals $2\pi$ only when $W = \pi R$; for smaller $W$ the cone point carries a genuine angular deficit, but the excision argument of Section 6 is valid for any cone angle.

**Curvature.** For a metric of the form $ds^2 = dy^2 + f(y)^2\,dw^2$, the Gaussian curvature is $K = -f''/f$. With $f(y) = \cos(y/R)$:

$$f'' = -\frac{1}{R^2}\cos(y/R) \qquad \Rightarrow \qquad K = -\frac{f''}{f} = \frac{1}{R^2}$$

The intrinsic scalar curvature is:

$$R_\Sigma = 2K = \frac{2}{R^2}$$

The $S^2$ quotient construction supplies it through the inherited constant curvature. The Laplace-Beltrami operator on this metric is the object of Sections 5 and 6.

---

## 5. Direct Computation and Upper Bound

For the metric $ds^2 = dy^2 + \cos^2(y/R)\,dw^2$ with $f(y) = \cos(y/R)$, the Laplace-Beltrami operator acting on $y$-dependent functions in the anti-periodic sector is:

$$\Delta u = u'' + \frac{f'}{f}\,u' = u'' - \frac{1}{R}\tan(y/R)\cdot u'$$

**The ground eigenfunction.** We test $u_0 = \sin(y/R)$. Computing the derivatives:

$$u_0' = \frac{1}{R}\cos(y/R), \qquad u_0'' = -\frac{1}{R^2}\sin(y/R)$$

Substituting into the operator:

$$\Delta u_0 = -\frac{1}{R^2}\sin(y/R) - \frac{1}{R}\tan(y/R)\cdot\frac{1}{R}\cos(y/R)$$

$$= -\frac{1}{R^2}\sin(y/R) - \frac{1}{R^2}\sin(y/R)$$

$$-\Delta u_0 = \frac{2}{R^2}\sin(y/R) = \frac{2}{R^2}\,u_0$$

The eigenvalue for this eigenfunction is $2/R^2$.

**Anti-periodic boundary condition.** Verifying directly:

$$u_0(y + \pi R) = \sin\!\left(\frac{y + \pi R}{R}\right) = \sin\!\left(\frac{y}{R} + \pi\right) = -\sin\!\left(\frac{y}{R}\right) = -u_0(y) \quad \checkmark$$

**Rayleigh quotient upper bound.** The area element is $dA = |\cos(y/R)|\,dy\,dw$, using the unsigned expression since $\cos(y/R) < 0$ for $y \in (\pi R/2, \pi R)$. With $\nabla u_0 = (1/R)\cos(y/R)\,\partial_y$ and $g_{yy} = 1$:

$$|\nabla u_0|^2 = \frac{\cos^2(y/R)}{R^2}$$

Substituting $t = y/R$:

$$\int_M |\nabla u_0|^2\,dA = \frac{2W}{R^2}\int_0^{\pi R}|\cos(y/R)|^3\,dy = \frac{2W}{R^2}\cdot 2R\int_0^{\pi/2}\cos^3 t\,dt = \frac{2W}{R^2}\cdot\frac{4R}{3} = \frac{8W}{3R}$$

$$\int_M u_0^2\,dA = 2W\int_0^{\pi R}\sin^2(y/R)|\cos(y/R)|\,dy = 2W\cdot 2R\int_0^{\pi/2}\sin^2 t\cos t\,dt = 2W\cdot\frac{2R}{3} = \frac{4WR}{3}$$

The Rayleigh quotient gives:

$$\lambda_0 \leq \frac{\int_M |\nabla u_0|^2\,dA}{\int_M u_0^2\,dA} = \frac{8W/3R}{4WR/3} = \frac{2}{R^2}$$

The lower bound is established in Section 6.

---

## 6. Bochner Lower Bound

Section 5 established $\lambda_0 \leq 2/R^2$ via direct computation. This section establishes the lower bound independently, without reference to any test function.

**Non-orientability.** The Möbius band is non-orientable, but the divergence theorem is applied here via the Riemannian density $|\cos(y/R)|\,dy\,dw$, which is a positive measure well-defined on any Riemannian manifold without requiring an orientation. The orientability obstruction to integrating differential forms does not apply to integration against a positive density.

We apply this identity to an eigenfunction $u$ in Sector $\mathcal{A}$.

Let $u$ be any admissible eigenfunction in Sector $\mathcal{A}$ with $-\Delta_g u = \lambda u$ and Neumann boundary condition $\partial_\nu u\big|_{\partial M} = 0$. Apply the Bochner formula in dimension 2:

$$\frac{1}{2}\Delta|\nabla u|^2 = |\nabla^2 u|^2 + \text{Ric}(\nabla u, \nabla u) + \langle \nabla u, \nabla \Delta u \rangle$$

On a 2-dimensional surface with $\text{Ric} = Kg$ where $K = 1/R^2$, substituting $\nabla \Delta u = -\lambda \nabla u$:

$$\frac{1}{2}\Delta|\nabla u|^2 = |\nabla^2 u|^2 + K|\nabla u|^2 - \lambda|\nabla u|^2$$

**Sturm-Liouville form and sign conventions.** On each half-interval, the Laplace-Beltrami operator $\Delta_g u = u'' + (f'/f)\,u'$ with $f(y) = \cos(y/R)$ can be written in Sturm-Liouville divergence form as $(f \cdot u')'/f$, equivalently $-\Delta_g u = \lambda u$ becomes

$$-(f \cdot u')' = \lambda f \cdot u$$

On $(0, \pi R/2)$, $f = \cos(y/R) > 0$; on $(\pi R/2, \pi R)$, $f = \cos(y/R) < 0$. Multiplying through by $\text{sgn}(f)$ on each half-interval converts to the standard Sturm-Liouville form with positive weight:

$$-(|f| \cdot u')' = \lambda |f| \cdot u$$

where $|f| = |\cos(y/R)|$. The Riemannian density $dA = |f|\,dy\,dw$ uses the same absolute value. The two forms are equivalent on each smooth half-interval; the absolute value is the natural choice for the Sturm-Liouville weight because it is the Riemannian density factor, positive on both sides of the pole.

**Cone point excision.** The Bochner formula is applied on the smooth manifold $M_\epsilon = M \setminus \{|y - \pi R/2| < \epsilon\}$. This introduces two additional boundary curves $y = \pi R/2 \pm \epsilon$. The excision boundary terms must vanish in the limit $\epsilon \to 0$; this requires explicit asymptotics at the singular point.

**Frobenius analysis at the cone point.** Writing $\delta = y - \pi R/2$, the weight function satisfies $|\cos(y/R)| = |\sin(\delta/R)| \sim |\delta|/R$ near $\delta = 0$. The reduced eigenequation in Sturm-Liouville form is

$$(|\delta|/R \cdot u')' + \lambda\,|\delta|/R \cdot u = 0$$

to leading order. On a single side ($\delta > 0$), substituting $p(\delta) = \delta/R$ and seeking a Frobenius solution $u = \delta^s \sum_{k=0}^\infty a_k \delta^k$:

Substituting $u = \delta^s$ and matching the leading $\delta^{s-1}$ terms gives $s^2 = 0$ (double root at $s = 0$). The two independent local solutions are:

$$u_1 = a_0 + a_2 \delta^2 + O(\delta^4), \qquad u_2 = \log|\delta| + b_2 \delta^2 + O(\delta^4)$$

where $a_2 = -\lambda a_0/4$ from the $O(\delta)$ balance in the eigenequation. The regular branch $u_1$ satisfies $u_1' = 2a_2\delta + O(\delta^3) = O(\delta)$ and $u_1'' = 2a_2 + O(\delta^2) = O(1)$. The logarithmic branch $u_2$ satisfies $u_2' = 1/\delta + O(\delta)$, giving $(u_2')^2\,|\cos| \sim \delta^{-1}$, which is non-integrable. Both solutions are square-integrable with respect to $|\cos|\,dy \sim |\delta|\,d\delta$ (limit-circle), but only $u_1$ has finite Dirichlet integral. The Friedrichs extension (Section 2) selects $u_1$.

**Excision boundary estimates.** For any eigenfunction $u$ in the Friedrichs domain, the Frobenius expansion gives:

- $u = a_0 + O(\delta^2)$, so $u = O(1)$
- $u' = O(\delta)$
- $u'' = O(1)$ (from the eigenequation: $u'' = -\lambda u + R^{-1}\tan(y/R)\cdot u'$, where $R^{-1}\tan(y/R) \sim R^{-1} \cdot R/\delta = 1/\delta$ but $u' = O(\delta)$, so the product is $O(1)$)

In the $w$-constant sector, $|\nabla u|^2 = (u')^2$ and $\nu = \pm\partial_y$ on the excision curves, so

$$\partial_\nu|\nabla u|^2 = 2u'u'' = O(\epsilon)$$

The arclength element along $y = \pi R/2 \pm \epsilon$ is $ds = |\cos(y/R)|\,dw \sim (\epsilon/R)\,dw$, so each excision curve has length $2W\epsilon/R = O(\epsilon)$. Therefore

$$\left|\int_{\{y = \pi R/2 \pm \epsilon\}} \partial_\nu|\nabla u|^2\,ds\right| \leq C\epsilon \cdot 2W\epsilon/R = O(\epsilon^2) \to 0$$

The divergence theorem on $M_\epsilon$ passes to the limit $\epsilon \to 0$ with no contribution from the excision boundaries.

$$\frac{1}{2}\int_M \Delta|\nabla u|^2\,dA = \frac{1}{2}\int_{\partial M} \partial_\nu|\nabla u|^2\,ds$$

**Boundary flux vanishing.** The Neumann condition $\partial_\nu u = 0$ makes $\nabla u$ tangential on $\partial M$, so the flux reduces to $2\nabla^2 u(\nu, T)\cdot \partial_T u$ where $T$ is the unit tangent to $\partial M$. Specifically, $T(\nu u) = 0$ since $\nu u = 0$ holds everywhere on $\partial M$ by Neumann, and $\nabla_T \nu = -\kappa_g T$ by the Frenet formula, giving $\nabla^2 u(\nu, T) = \kappa_g\,\partial_T u$ where $\kappa_g$ is the geodesic curvature of $\partial M$ within the surface. The boundary curves $w = \pm W$ are parametrized by $y$ at unit speed (since $g_{yy} = 1$), so $T = \partial_y$ is already the unit tangent and no normalization is required:

$$\nabla_{\partial_y}\partial_y = \Gamma^w_{yy}\partial_w = 0$$

since $g_{yy} = 1$ is constant and $g_{yw} = 0$. Therefore $\kappa_g = 0$ and the boundary flux is identically zero.

**Green's identity at the cone point.** The identity $\int_M|\nabla u|^2\,dA = \lambda\int_M u^2\,dA$ follows from Green's identity with Neumann BC. The same cone-point excision applies: by the Frobenius expansion, $u = O(1)$ and $u' = O(\delta)$ in the Friedrichs domain, so the boundary contribution is $|u\,\partial_\nu u|\cdot\text{arc-length} = O(1)\cdot O(\epsilon)\cdot O(\epsilon) = O(\epsilon^2) \to 0$.

**The integrated identity.** With the boundary term zero, integrating the right side over the Möbius band and rearranging yields:

$$\int_M |\nabla^2 u|^2\,dA = (\lambda - K)\int_M |\nabla u|^2\,dA$$

**Trace inequality on the Hessian.** The Hessian $\nabla^2 u$ is a symmetric $2\times 2$ tensor with components $u_{ij}$. The trace inequality gives:

$$|\nabla^2 u|^2 = \sum_{i,j} u_{ij}^2 \geq \frac{1}{2}\left(\sum_i u_{ii}\right)^2 = \frac{(\text{tr}\,\nabla^2 u)^2}{2} = \frac{(\Delta u)^2}{2}$$

The factor of $1/2$ arises because the trace squares two diagonal terms and the inequality distributes over the off-diagonal terms. Substituting $\Delta u = -\lambda u$:

$$|\nabla^2 u|^2 \geq \frac{\lambda^2 u^2}{2}$$

Integrating over the Möbius band and applying Green's identity with Neumann BC, $\int_M |\nabla u|^2\,dA = \lambda \int_M u^2\,dA$:

$$(\lambda - K)\lambda\int_M u^2\,dA \geq \frac{\lambda^2}{2}\int_M u^2\,dA$$

**The bound.** The anti-periodic sector excludes constants, so $u \not\equiv 0$ and $\lambda > 0$. Dividing by $\lambda \int_M u^2\,dA > 0$:

$$\lambda - K \geq \frac{\lambda}{2} \qquad \Rightarrow \qquad \lambda \geq 2K = R_\Sigma = \frac{2}{R^2}$$

This follows Reilly's strategy of integrating the Bochner formula and controlling the boundary term. The cone point is handled by excision: the excision boundary terms vanish in the limit as shown above, and the boundary terms from $\partial M$ vanish because $\kappa_g = 0$. The lower bound holds for any eigenfunction in Sector $\mathcal{A}$, independently of Section 5.

---

## 7. The Identity

Section 5 established the upper bound via direct computation:

$$\lambda_0 \leq \frac{2}{R^2}$$

Section 6 established the lower bound independently via the Bochner identity:

$$\lambda \geq \frac{2}{R^2}$$

for any admissible eigenfunction in Sector $\mathcal{A}$. In particular this bound applies to the ground eigenfunction, so it applies to $\lambda_0$. Together they force:

$$\boxed{\lambda_0 = R_\Sigma = \frac{2}{R^2}}$$

**Equality condition.** Equality in the trace inequality $|\nabla^2 u|^2 \geq (\text{tr}\,\nabla^2 u)^2/n$ in dimension $n = 2$ holds exactly when $\nabla^2 u = (\Delta u/2)\,g$. We verify that $u_0 = \sin(y/R)$ satisfies this on the smooth locus of $ds^2 = dy^2 + \cos^2(y/R)\,dw^2$. With $\Delta u_0 = -2\sin(y/R)/R^2$, the target is $\nabla^2 u_0 = -(\sin(y/R)/R^2)\,g$. The Christoffel symbols for $f = \cos(y/R)$, $f' = -\sin(y/R)/R$ are $\Gamma^y_{yy} = 0$, $\Gamma^y_{ww} = \sin(y/R)\cos(y/R)/R$, $\Gamma^w_{yw} = -\tan(y/R)/R$. The three Hessian components:

$$(\nabla^2 u_0)_{yy} = u_0'' - \Gamma^y_{yy}u_0' = -\frac{\sin(y/R)}{R^2} = \frac{\Delta u_0}{2}\cdot g_{yy} \quad\checkmark$$

$$(\nabla^2 u_0)_{yw} = 0 = \frac{\Delta u_0}{2}\cdot g_{yw} \quad\checkmark$$

$$(\nabla^2 u_0)_{ww} = -\Gamma^y_{ww}u_0' = -\frac{\sin(y/R)\cos^2(y/R)}{R^2} = \frac{\Delta u_0}{2}\cdot g_{ww} \quad\checkmark$$

where the $\partial_w\partial_w u_0$ and $\Gamma^w_{ww}\partial_w u_0$ terms vanish since $u_0$ depends only on $y$ and $\Gamma^w_{ww} = 0$. The bound is sharp and the equality is structural. This is the same Hessian condition that appears in the equality case of the classical Lichnerowicz-Obata/Reilly argument, here verified directly on the smooth locus.

**Simplicity.** In Sector $\mathcal{A}$, the ground eigenvalue is simple: by Sturm-Liouville theory for a limit-circle singular problem with the regular-branch condition at the cone point, the ground state has no interior zeros and is unique up to scaling (Zettl 2005, Ch. 4). The eigenfunction $\sin(y/R)$ is strictly positive on $(0, \pi R)$ and is the unique ground eigenfunction in Sector $\mathcal{A}$.

**Summary.** The flat strip carries $\lambda_0^{\text{flat}} = 1/R^2 = R_\Sigma/2$. The metric inherited from the covering $S^2 \subset S^3$ through the quotient construction contributes the additional curvature term $K = 1/R^2$, yielding the exact identity

$$\lambda_0 = \frac{2}{R^2} = R_\Sigma$$

for Sector $\mathcal{A}$.

---

## 8. Discussion

**Two independent paths.** The identity $\lambda_0 = R_\Sigma = 2/R^2$ is established by two arguments that operate independently. Section 5 constructs the ground eigenfunction explicitly and reads off the eigenvalue directly. Section 6 derives a lower bound from the Bochner identity without reference to any test function. That both paths land at the same value confirms the identity is a geometric property of the inherited curvature, not a coincidence of the computation.

**Relation to the closed case.** For the closed non-orientable surface $\mathbb{RP}^2 = S^2/\{\pm 1\}$, the ground eigenvalue of the twisted Laplacian is also $2/R^2 = R_\Sigma$, recoverable from the odd spherical harmonics at $\ell = 1$. The present result is the open analog: the Möbius band with geodesic boundary, carrying the metric inherited from $S^2 \subset S^3$, reproduces the same eigenvalue through a different geometric mechanism. On $\mathbb{RP}^2$ the result follows from global spherical harmonic theory on a smooth closed manifold. Here it follows from the $S^2$ quotient construction supplying constant curvature to an otherwise flat surface, with the cone point handled by excision and the boundary flux killed by $\kappa_g = 0$.

**The role of the inherited curvature.** The flat strip yields $\lambda_0 = 1/R^2 = R_\Sigma/2$. The missing factor of 2 enters through the metric coefficient $f(y) = \cos(y/R)$, which encodes the constant curvature of the covering $S^2$. A different choice of covering surface would generally induce a different intrinsic metric and curvature profile, so the spectrum would change through the induced geometry rather than through a separate explicit extrinsic term. The constant-curvature quotient construction isolates the curvature effect cleanly: the induced metric carries constant $K = 1/R^2$ and nothing else.

**The boundary flux vanishing.** The Bochner argument depends on the boundary integral vanishing. The Neumann condition reduces the flux to a term involving the geodesic curvature $\kappa_g$ of $\partial M$ within the surface. Two conditions are operative here and it is worth distinguishing them clearly. The totally geodesic embedding of the covering $S^2$ in $S^3$ (meaning $S^2$ has zero extrinsic curvature in the ambient space, $K_{ij} = 0$) establishes the inherited metric and curvature $K = 1/R^2$ on the Möbius quotient. The geodesic boundary condition (meaning the boundary curves $w = \pm W$ are geodesics within the surface, $\kappa_g = 0$) is what kills the flux. These are logically independent conditions that both hold here. For the metric $ds^2 = dy^2 + f(y)^2\,dw^2$, the $y$-curves satisfy $\Gamma^y_{yy} = \Gamma^w_{yy} = 0$, hence $\kappa_g = 0$ and the boundary flux is identically zero.

**The cone point.** The metric degenerates at $y = \pi R/2$. On the covering $S^2$ this is a smooth pole; on the quotient Möbius band it is a genuine cone singularity with angular deficit (Section 2). The Friedrichs extension (Section 2) specifies the self-adjoint operator at this limit-circle endpoint, selecting the regular branch via the finite Dirichlet integral condition. The ground eigenfunction $u_0 = \sin(y/R)$ takes its maximum value 1 at the cone point with $u_0' = 0$ and lies in the Friedrichs domain. The excision argument in Section 6 shows that the excision boundary terms vanish in the limit, so the Bochner and Green identities remain valid for eigenfunctions in the Friedrichs domain despite the metric degeneration.

**Gap in the literature.** Lichnerowicz-type bounds via the Bochner identity have been developed for manifolds with geodesic boundary (Reilly 1977). Kalvoda, Krejčiřík, and Zahradová (2020) study curved Möbius strips in $\mathbb{R}^3$ with non-constant curvature in the thin-strip limit. The present result is narrower: an explicit computation of the ground eigenvalue in Sector $\mathcal{A}$ for a positively curved band with interior cone singularity and geodesic boundary. We are not aware of a prior treatment of this specific model.

---

## 9. Conclusion

We have established that, in Sector $\mathcal{A}$, the lowest eigenvalue of the twisted Laplace-Beltrami problem on the induced Möbius-band model equals the surface scalar curvature exactly:

$$\lambda_0 = R_\Sigma = \frac{2}{R^2}$$

Two independent paths establish this identity. The upper bound follows from the explicit eigenfunction $u_0 = \sin(y/R)$ with Rayleigh quotient $2/R^2$. The lower bound follows from the Bochner identity, with boundary flux vanishing because the boundary curves are geodesics of the surface ($\kappa_g = 0$) and the cone point handled by excision. The upper and lower bounds coincide: the Hessian of $u_0$ is proportional to the metric at every smooth point, satisfying the equality condition of the trace inequality.

The flat strip carries $\lambda_0^{\text{flat}} = 1/R^2 = R_\Sigma/2$. The metric inherited from the covering $S^2 \subset S^3$ through the quotient construction supplies the missing factor of 2 through the constant curvature $K = 1/R^2$. The result is the open analog of the known closed case: the twisted Laplacian on $\mathbb{RP}^2$ also has ground eigenvalue $R_\Sigma$, but through global spherical harmonic theory on a smooth closed manifold. Here the same eigenvalue arises through curvature inheritance and a geodesic boundary condition.

The interior cone point at $y = \pi R/2$, corresponding to the pole of the covering $S^2$, carries constant curvature $K = 1/R^2$ on the smooth locus. The explicit eigenfunction extends regularly across this point in the Friedrichs domain, and the excision-based estimates of Section 6 show that the cone contributes no residual boundary term to the spectral argument.

---

## References

- Friedrichs, K. (1934). Spektraltheorie halbbeschränkter Operatoren und Anwendung auf die Spektralzerlegung von Differentialoperatoren. *Mathematische Annalen* 109, 465--487.
- Lichnerowicz, A. (1958). *Géométrie des groupes de transformations*. Dunod, Paris.
- Obata, M. (1962). Certain conditions for a Riemannian manifold to be isometric with a sphere. *Journal of the Mathematical Society of Japan* 14, 333--340.
- Reilly, R.C. (1977). Applications of the Hessian operator in a Riemannian manifold. *Indiana University Mathematics Journal* 26, 459--472.
- Chavel, I. (1984). *Eigenvalues in Riemannian Geometry*. Academic Press. Ch. 3 (twisted Laplacian on non-orientable surfaces); Ch. 4 (Bochner formula).
- Escobar, J.F. (1990). Uniqueness theorems on conformal deformation of metrics, Sobolev inequalities, and an eigenvalue estimate. *Communications on Pure and Applied Mathematics* 43, 857--883.
- Zettl, A. (2005). *Sturm-Liouville Theory*. American Mathematical Society. Ch. 4 (limit-circle singular endpoints and Frobenius expansions).
- Kalvoda, T., Krejčiřík, D., and Zahradová, K. (2020). Effective quantum dynamics on the Möbius strip. *Journal of Physics A* 53, 375201.

---

/ **[`main`](../../../README.md)** / **[`framework`](../../framework/)** / **[`cosmos`](../../cosmos/)** / **[`spectrum`](../../spectrum/)** /
