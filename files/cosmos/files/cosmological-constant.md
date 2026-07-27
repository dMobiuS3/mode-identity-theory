/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

<img src="https://pbs.twimg.com/media/HLlsyI3W8AAYqUP?format=jpg&name=4096x4096" width="100%" alt="Cosmological Constant">

This page reads the cosmological constant as geometry. Its coefficient is set by the first positive curvature level carried on a Möbius surface embedded in the closed spatial domain, which fixes the dimensionless relation $\Lambda R^2 = 3$. The value of $\Lambda$ additionally needs the curvature radius $R$, which remains open, so this is a coefficient, not a number.

## I. The relationship

In general relativity Λ sits on the geometric side of the field equations,

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

multiplying the metric: pure geometry. General relativity is local. It gives dynamics on a domain but fixes neither the domain nor the value of Λ; on a flat, simply connected, non-compact background the coefficient is unconstrained. Reversing the hierarchy, the present closed-domain construction supplies a distinguished spectral seed, $R_\Sigma = 2/R^2$, which converts through the standard Gauss and de Sitter relations to $\Lambda = 3/R^2$.

Moved to the matter side, $\rho_\Lambda = \Lambda c^4 / 8\pi G$ reads as a vacuum energy density, and the zero-point estimate overshoots observation by roughly 122 orders of magnitude, the cosmological-constant problem. This construction does not derive the observed Λ from that mode sum; it instead treats Λ as global geometric data and returns in §VI to the unresolved radiative-stability question.

Einstein's 1917 setting was a closed $S^3$ with Λ as geometry. This construction reclaims that setting, not his matter-Λ equilibrium: it does not use a matter-Λ force balance, and $R$ remains open, so the result is the coefficient $\Lambda R^2 = 3$, not the observed number.

## II. The geometry

The domain is the minimal closed one. $S^3$ is the unique simply connected closed 3-manifold (Poincaré). The postulate embeds a non-orientable carrier in it:

$$S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \qquad \partial S^3 = \emptyset.$$

The ambient space is closed and has no boundary. The Möbius band is an embedded spectral carrier, not a boundary of $S^3$; its own boundary is the circle $S^1$. It is built as the edge-identified quotient of a totally geodesic covering great-$`S^2`$ band in $S^3$, and inherits that band's constant-curvature metric. Among non-orientable surfaces with one boundary component (a disk removed from a connected sum of $k$ crosscaps) the framework adopts the minimal case, $k = 1$, the Möbius band. That minimality is an adopted, natural criterion, not a derived necessity.

The observable spatial quotient is $S^3/2I$, the hypersphere modulo the binary icosahedral group ($`\lvert 2I\rvert = 120`$), the largest exceptional finite subgroup of $\mathrm{SU}(2) \cong S^3$. The local curvature geometry of §§III-IV lives on the cover $S^3(R)$; the quotient enters later only as the large-scale harmonic selection rule.

## III. The spectral seed

The operator is the twisted Laplacian on sections of the orientation line bundle over the curved Möbius carrier. The Möbius holonomy imposes anti-equivariance. In the full curved conic problem the spectral bottom is extension-dependent, zero for the Friedrichs realization (a discontinuous constant-sector mode) and negative for the bridging family, and no self-adjoint extension has a strictly positive bottom. The robust datum is therefore not a ground state but the first positive level, and in the narrow-band class it is stable at

$$\lambda_+ = \frac{2}{R^2},$$

the $\ell = 1$ zonal mode $\sin(y/R)$, common to the Friedrichs and bridging extensions for $\delta_0 > 2R/e$. The framework takes the narrow band $W \le \pi R/2$ as a physical input on the carrier, not a derived fact. The holonomy selects the twisted sector in which the first positive level is identified; the curvature of the covering great-$`S^2`$ band, of which the carrier is the edge-identified quotient, fixes its value. (On a flat strip the same anti-periodic mode returns only $1/R^2$; the band's curvature supplies an equal $1/R^2$, doubling it to the scalar-curvature value.) The [first-eigenvalue paper](../../framework/files/bedrock/files/first-eigenvalue.md) carries the proof.

The same coefficient appears independently as the ambient Ricci term in the Weitzenböck bound on coexact $1$-forms, $\lambda \ge 2/R^2$ from $\mathrm{Ric} = (2/R^2)g$; the operators and spectral statements are distinct, and that bound is a curvature floor rather than an attained eigenvalue. See the [coexact-gap paper](../../framework/files/bedrock/files/coexact-gap.md).

## IV. The conversion

The surface seed carries no Λ; the standard general-relativistic chain converts it, in two stages with distinct totally-geodesic conditions.

Stage 1, surface to spatial. For the totally geodesic covering great-$`S^2`$ band $\Sigma^2 \subset S^3$ (second fundamental form $A_{ij} = 0$), of which the Möbius carrier is the edge-identified quotient, in an isotropic space, the Gauss equation gives

$$R_\Sigma = \frac{2}{R^2} \Longrightarrow {}^{(3)}R = 3R_\Sigma = \frac{6}{R^2}.$$

Stage 2, spatial to Λ. On the round time-symmetric $S^3$ slice of four-dimensional de Sitter ($`S^3 \subset \mathrm{dS}_4`$, extrinsic curvature $`K_{ij} = 0`$, vacuum $`T_{\mu\nu} = 0`$), the vacuum Hamiltonian constraint gives

$${}^{(3)}R = 2\Lambda \Longrightarrow \Lambda = \frac{3}{R^2}.$$

The 3 is the isotropic spatial Ricci trace under $A_{ij} = 0$ on the great-$`S^2`$ band (derived); the 2 is the de Sitter / vacuum-constraint normalization on the time-symmetric slice (imported from general relativity); their ratio $3/2$ is the Gauss-equation interface. The coefficient $\Lambda R^2 = 3$ is the standard de Sitter value once a round time-symmetric $S^3(R)$ vacuum is assumed; the content here is the spectral origin of the upstream seed, not the coefficient.

| Step | Status |
|---|---|
| Möbius first positive level $2/R^2$ | Companion spectral result |
| Surface-to-spatial factor 3 | Standard Gauss geometry (isotropic covering great-$`S^2`$ band, $`A_{ij} = 0`$) |
| Time-symmetric vacuum relation ${}^{(3)}R = 2\Lambda$ | Standard GR input ($`K_{ij} = 0`$, vacuum) |
| $\Lambda R^2 = 3$ | Standard de Sitter coefficient, with a proposed spectral seed |
| Scale $R$ | Open |

## V. The open radius

$\Lambda = 3/R^2$ yields a number only with an independent $R$. Reading $R$ off $\Lambda$ through $R = \sqrt{3/\Lambda}$ is circular. Two live routes provide candidate independent estimates of $R$, without using $\Lambda$, the CMB, or the de Sitter relation: the coupling ($`\alpha`$) route, better conditioned, returns $\Lambda = 3/R^2$ to within about 24%; the particle mass spectrum gives $R \approx 20$ Gpc as an order-of-magnitude cross-check. Neither yet closes the prediction. Details in [The R Problem](../../framework/files/working/files/r-problem.md) and [R from the mass spectrum](../../framework/files/working/files/r-from-mass-spectrum.md).

Read back from the observed value, the consistency radius is $R = \sqrt{3/\Lambda_\text{obs}} \approx 5.3$ Gpc and $\Lambda_\text{obs}\ell_P^2 \approx 2.9 \times 10^{-122}$; this is a calibration read-back, not an independent determination. The $S^3/2I$ quotient also produces a low-shell Molien gap relevant to CMB power, but that structure does not independently determine $R$; it is treated in [The R Problem](../../framework/files/working/files/r-problem.md) and the CMB notes.

## VI. Test and scope

Einstein's field equations are unchanged; Λ stays on the geometric side. The direct test of the relation is

$$\Lambda_\text{obs}R_\text{ind}^2 = 3$$

with $R_\text{ind}$ obtained without the Λ-radius relation, stated in advance of the European Space Agency's Euclid Data Release 1. The cosmology-relevant tests read against the spectroscopic BAO and weak-lensing analyses that arrive with the full DR1 in mid 2027; the DR1-Foundation release of November 2026 carries data but no cosmology-derived products, and ESA notes its release dates are tentative. A departure from 3 at $> 5\sigma$, with $R$ obtained independently, would falsify the coefficient relation. Robust evidence that the dark-energy density evolves with redshift would instead falsify the broader identification of the observed component with a true cosmological constant.

This construction treats Λ as global geometric data rather than deriving it from a zero-point mode sum. That reframes the role assigned to Λ, but it does not by itself establish radiative stability: quantum vacuum stress still contributes to the effective gravitational equations, and whether it can renormalize or disturb the proposed spectral relation remains open. The compulsoriness of the Möbius carrier and the dynamical stability of the cosmology are likewise open.

---

The twisted Möbius problem realizes the round curvature scale $2/R^2$ as a stable first positive level despite an extension-dependent spectral bottom. Under the standard time-symmetric de Sitter conversion, that seed corresponds to $\Lambda R^2 = 3$; determining $R$ independently remains open. Einstein's instinct to treat Λ geometrically remains the useful one here.

---

/ **[`main`](/README.md)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
