# Mode Identity Theory — Interactive Calculator

**Run MIT for yourself. One postulate. Zero free parameters.**

$$S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset$$

## What This Is

An interactive calculator implementing the complete MIT scaling law:

$$\frac{A}{A_P} \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}$$

Every output traces from a single topological postulate through a locked derivation chain. No hidden parameters. No fitting. The code is the math.

## Live Site

**[modeidentitytheory.github.io/calculator](https://modeidentitytheory.github.io/calculator)** (or your deployment URL)

## Features

| Tab | What it does |
|-----|-------------|
| **Scaling Law** | Input any well position Θ, manifold index n, and scale Ω. Get A/Aₚ. Presets for α, a₀, H₀, Λ. |
| **Spectrum** | The mass formula. Pick any irrep and vacuum, see Formula A compute the mass. Full 24-entry table with SM assignments. All locked data: 8 C_geom values, 27 vacuum torsion entries. |
| **Theory** | The postulate, five foundations, cosmic wave Ψ, 120 domain, manifold assignments. |
| **Scorecard** | Extended scorecard: cosmological constants through particle masses. Falsification criteria. |
| **Registry** | All 12 Zenodo DOIs. Links to every companion paper. |

## Deploy Your Own

This is a single `index.html` file. No build step. No dependencies. No server.

### GitHub Pages

1. Fork this repository
2. Go to Settings → Pages
3. Set source to `main` branch, root directory
4. Your site is live at `https://yourusername.github.io/mit-calculator`

### Local

```bash
git clone https://github.com/yourusername/mit-calculator.git
open mit-calculator/index.html
```

That's it.

## The Math

Four lines produce constants spanning 122 orders of magnitude:

```
C(Θ) = 2 sin²(πΘ)
A/Aₚ = C(Θ) · (√Ω)⁻ⁿ
Θ ∈ {13, 21, 34, 55, 60} / 120
n ∈ {1/30, 1, 3/2, 2, 3}
```

One formula produces 24 particle masses:

```
m(ρ,σ) = μ_Λ · C_geom(ρ) · (√Ω_Λ)^(dist/30) · T²(ρ ⊗ σ)
```

8 irreps × 3 vacua. 10 of 12 SM fermions within factor of 3. All 12 within factor of 10.

### Constants Used

| Constant | Value | Role |
|----------|-------|------|
| Ω_Λ | (R_Λ / ℓ_P)² ≈ 3.52 × 10¹²² | de Sitter scale (epoch-independent) |
| Ω_H | (R_H / ℓ_P)² ≈ 3.13 × 10¹²² | Hubble scale (epoch-dependent) |
| ℓ_P | 1.616 × 10⁻³⁵ m | Planck length |

### Scorecard

| Observable | Predicted | Observed | Agreement |
|-----------|-----------|----------|-----------|
| α | 0.00733 | 0.007297 | ~0.5% |
| a₀/(cH₀) | 0.184 | 0.183 | <1% |
| H₀ local shift | 8.4% | ~8.7% | <1% |
| Λ·ℓ_P² | 3.0 × 10⁻¹²² | 2.84 × 10⁻¹²² | ~5% |
| m_e | 5.21 × 10⁻⁴ GeV | 5.11 × 10⁻⁴ GeV | 2% |
| m_u | 2.03 × 10⁻³ GeV | 2.16 × 10⁻³ GeV | 6% |
| m_μ | 1.03 × 10⁻¹ GeV | 1.057 × 10⁻¹ GeV | 2% |
| 12 SM fermions | 24 entries | 12 targets | 10/12 ≤3× |

## Papers

All 12 papers are registered with DOIs on Zenodo:

- **Core:** [MITv6](https://doi.org/10.5281/zenodo.18064856)
- **Falsification:** [Team Cosine](https://doi.org/10.5281/zenodo.18189078)
- **Full registry:** [Zenodo Community](https://zenodo.org/communities/modeidentitytheory)

Falsification window: **Euclid Data Release 1 — October 21, 2026**

## Author

Blake Shatto, P.E. — [bshatto.pe@gmail.com](mailto:bshatto.pe@gmail.com)

[modeidentitytheory.com](https://modeidentitytheory.com)

## License

MIT License. The framework belongs to everyone who can run the numbers.
