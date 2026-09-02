"""Mass ladder (2026-09-02): reproducible regression guard for the 24-entry table.

Recomputes every entry of mass-spectrum.md section III from the formula

    m(rho, sigma) = mu_Lambda * C_geom(rho) * (sqrt(Omega_Lambda))^(dist(rho)/30)
                    * T^2(rho tensor sigma)

and certifies:

  1. all 24 published masses, to a 0.5% tolerance (worst observed 0.45%, set by
     the 3-to-4 figure precision of the printed C_geom and T^2 inputs);
  2. THE ANCHOR COUPLING, which is the reason this file exists. The two printed
     inputs are not independent. Omega_Lambda = 3/(Lambda l_P^2) inverts
     sqrt(Omega_Lambda) = 1.019e61 into a definite Lambda, and pushing that same
     Lambda through mu_Lambda = rho_Lambda^(1/4) returns the printed 2.25 meV.
     Freshening either input alone breaks the identity, which is exactly what the
     page's calibration note says must not happen, stated here so it fails loudly.
     The same identity names the row: both printed figures encode Planck 2018
     +BAO (67.66, 0.6889), giving 1.019e61 and 2.25 meV, and neither encodes the
     framework's own named TT,TE,EE+lowE+lensing row, which would give 1.027e61
     and 2.24 meV. The rows differ by more than the printed precision, so this is
     decidable, and it is the check that fires if either figure is freshened
     toward the named row without rerunning the table;
  3. the anchor-shift exponent: an entry at McKay distance d moves as
     Lambda^((15-d)/60), so the electron at d = 4 moves as Lambda^(11/60). Checked
     numerically by perturbing Lambda and refitting the exponent, not asserted;
  4. the anchor-free class: a ratio of two entries at the same rho shares both
     C_geom and the distance, so it reduces to T^2/T^2 and carries no Lambda. The
     R1 neutrino ladder is the only such family in the table;
  5. the m_e <-> Lambda loop: the forward comparison closes to 2% in mass, which
     inverts through the 11/60 exponent to ~11% in Lambda;
  6. the exact torsion algebra the table rests on (Galois ratios phi^-4 and
     phi^-8, sector products 4 and 1/4, R7 Galois-blind at 4).

Checks 2 through 5 are the ones that cannot be satisfied by transcribing the
table: they constrain the anchor, not the entries.

Run: python3 mass-ladder.test.py

Note for anyone running all of the repo's .test.py files in one loop on macOS:
there is no `timeout` binary on a stock install, so a harness that wraps each
run in `timeout` reports every artifact as failing before python is ever
reached. Run them bare, or install coreutils and use `gtimeout`.
"""

import math

PHI = (1 + 5 ** 0.5) / 2
TOL = 0.005  # 0.5%, section III entries

# ---------------------------------------------------------------- the anchor
# Both values are printed on mass-spectrum.md (sections II.1 and II.3) and belong
# to ONE pinned calibration. See check 2: they are mutually derivable.
MU_LAMBDA_MEV = 2.25          # section II.1, rho_Lambda^(1/4)
SQRT_OMEGA_LAMBDA = 1.019e61  # section II.3

MU_LAMBDA_GEV = MU_LAMBDA_MEV * 1e-12

# CODATA / PDG constants, for the anchor-coupling check only.
L_PLANCK = 1.616255e-35       # m
C_LIGHT = 2.99792458e8        # m/s
G_NEWTON = 6.67430e-11        # m^3 kg^-1 s^-2
EV_JOULE = 1.602176634e-19    # J
HBAR_C = 1.973269804e-7       # eV m
MPC = 3.0856775814913673e22   # m

# The two Planck 2018 combinations at issue, as (H0 in km/s/Mpc, Omega_Lambda).
# They differ by more than the printed precision of the anchor, so check 2 can
# say which one the mass ladder actually sits on.
PLANCK_NAMED = (67.36, 0.6847)  # TT,TE,EE+lowE+lensing: the framework's named row
PLANCK_BAO = (67.66, 0.6889)    # +BAO: what this table's inputs actually encode

# ------------------------------------------------------------------- inputs
# C_geom, section II.2 table.  dist, section II.3 McKay graph.
C_GEOM = {"R1": 0.0988, "R2": 0.2436, "R3": 0.5553, "R4": 0.7970,
          "R5": 0.8017, "R6": 0.2098, "R7": 0.7564, "R8": 0.2382}
DIST = {"R1": 1, "R2": 7, "R3": 2, "R4": 6,
        "R5": 6, "R6": 3, "R7": 4, "R8": 5}

# T^2(rho, sigma), section II.4 table, columns (triv, std, gal).
T2 = {"R1": (0.0365, 0.306, 2.778), "R2": (1.714, 2.778, 2.094),
      "R3": (0.306, 0.0365, 4.000), "R4": (2.094, 4.000, 1.714),
      "R5": (2.778, 6.854, 0.146), "R6": (1.000, 0.688, 4.712),
      "R7": (2.250, 4.000, 4.000), "R8": (4.000, 13.090, 1.910)}
SIGMA = {"triv": 0, "std": 1, "gal": 2}

# Section III, ranked table: (rank, rho, sigma, published mass in GeV).
PUBLISHED = [
    (1, "R1", "triv", 8.75e-13), (2, "R1", "std", 7.33e-12),
    (3, "R1", "gal", 6.67e-11), (4, "R3", "std", 5.30e-10),
    (5, "R3", "triv", 4.45e-9), (6, "R3", "gal", 5.83e-8),
    (7, "R6", "std", 4.09e-7), (8, "R6", "triv", 5.94e-7),
    (9, "R6", "gal", 2.80e-6), (10, "R7", "triv", 5.21e-4),
    (11, "R7", "std", 9.26e-4), (12, "R7", "gal", 9.26e-4),
    (13, "R8", "gal", 1.51e-2), (14, "R8", "triv", 3.16e-2),
    (15, "R8", "std", 1.03e-1), (16, "R5", "gal", 4.18e-1),
    (17, "R4", "gal", 4.89), (18, "R4", "triv", 5.97),
    (19, "R5", "triv", 7.96), (20, "R4", "std", 11.41),
    (21, "R5", "std", 19.64), (22, "R2", "triv", 161.3),
    (23, "R2", "gal", 197.0), (24, "R2", "std", 261.46),
]

M_ELECTRON = 5.11e-4  # GeV, PDG, the section III "Observed" cell for rank 10


def mass(rho, sigma, mu=MU_LAMBDA_GEV, sqrt_omega=SQRT_OMEGA_LAMBDA):
    """The section I formula, verbatim."""
    return (mu
            * C_GEOM[rho]
            * sqrt_omega ** (DIST[rho] / 30)
            * T2[rho][SIGMA[sigma]])


def check(label, condition, detail=""):
    if not condition:
        raise AssertionError(f"{label} FAILED  {detail}")
    print(f"  PASS  {label}" + (f"   {detail}" if detail else ""))


# =============================================================== 1. entries
print("\nCHECK 1  the 24 ranked entries reproduce section III within 0.5%")
worst, worst_rank = 0.0, None
for rank, rho, sigma, published in PUBLISHED:
    computed = mass(rho, sigma)
    dev = abs(computed / published - 1)
    if dev > worst:
        worst, worst_rank = dev, rank
    if dev > TOL:
        raise AssertionError(
            f"rank {rank} ({rho},{sigma}): formula {computed:.4g} "
            f"vs published {published:.4g}, {dev * 100:.2f}% > {TOL * 100}%")
check("all 24 entries within tolerance",
      True, f"worst {worst * 100:.2f}% at rank {worst_rank}")

# ========================================================= 2. anchor coupling
print("\nCHECK 2  the two printed inputs are one calibration, not two knobs")
def mu_from_lambda(lambda_lp2_value):
    """mu_Lambda = rho_Lambda^(1/4) in meV, from a dimensionless Lambda l_P^2."""
    lam_si = lambda_lp2_value / L_PLANCK ** 2                   # m^-2
    rho_si = lam_si * C_LIGHT ** 4 / (8 * math.pi * G_NEWTON)   # J m^-3
    rho_ev4 = (rho_si / EV_JOULE) * HBAR_C ** 3                 # eV^4
    return rho_ev4 ** 0.25 * 1e3                                # meV


def planck_row(h0, f_lambda):
    """Lambda l_P^2 and sqrt(Omega_Lambda) for a Planck 2018 combination."""
    h_si = h0 * 1e3 / MPC
    llp = 3 * f_lambda * (h_si / C_LIGHT) ** 2 * L_PLANCK ** 2
    return llp, (3 / llp) ** 0.5


# Omega_Lambda = (R/l_P)^2 = 3/(Lambda l_P^2)  [the Lambda_ref = 3/R^2 typing]
lambda_lp2 = 3.0 / SQRT_OMEGA_LAMBDA ** 2
mu_derived_mev = mu_from_lambda(lambda_lp2)
spread = abs(mu_derived_mev / MU_LAMBDA_MEV - 1)
check("sqrt(Omega_Lambda) inverts to a definite Lambda",
      2.8e-122 < lambda_lp2 < 3.0e-122, f"Lambda l_P^2 = {lambda_lp2:.5g}")
check("that same Lambda regenerates the printed mu_Lambda",
      spread < TOL,
      f"derived {mu_derived_mev:.4g} meV vs printed {MU_LAMBDA_MEV} meV "
      f"({spread * 100:.2f}%)")

# Which Planck combination is this anchor? The two rows differ by more than the
# printed precision, so the question is decidable, and both printed figures
# answer it the same way. This is the check that fires if either is freshened
# toward the framework's own named row.
bao_llp, bao_sqrt = planck_row(*PLANCK_BAO)
named_llp, named_sqrt = planck_row(*PLANCK_NAMED)
check("sqrt(Omega_Lambda) matches the +BAO row to four figures",
      abs(bao_sqrt / SQRT_OMEGA_LAMBDA - 1) < 1e-3,
      f"+BAO gives {bao_sqrt:.6g}, printed {SQRT_OMEGA_LAMBDA:.4g}")
check("and does NOT match the named TT,TE,EE+lowE+lensing row",
      abs(named_sqrt / SQRT_OMEGA_LAMBDA - 1) > 5e-3,
      f"named row would give {named_sqrt / 1e61:.3f}e61, not "
      f"{SQRT_OMEGA_LAMBDA / 1e61:.3f}e61")
check("mu_Lambda agrees with that same +BAO row",
      abs(mu_from_lambda(bao_llp) - MU_LAMBDA_MEV) < 0.005,
      f"+BAO gives {mu_from_lambda(bao_llp):.4g} meV")
check("and disagrees with the named row, so both figures name one combination",
      abs(mu_from_lambda(named_llp) - MU_LAMBDA_MEV) > 0.005,
      f"named row would print {mu_from_lambda(named_llp):.3g} meV, "
      f"not {MU_LAMBDA_MEV}")

# ======================================================= 3. anchor exponent
print("\nCHECK 3  an entry at McKay distance d moves as Lambda^((15-d)/60)")
# mu ~ Lambda^(1/4) and sqrt(Omega) ~ Lambda^(-1/2), so perturb Lambda and refit.
BUMP = 1.10
for rho in sorted(DIST, key=lambda r: DIST[r]):
    base = mass(rho, "triv")
    bumped = mass(rho, "triv",
                  mu=MU_LAMBDA_GEV * BUMP ** 0.25,
                  sqrt_omega=SQRT_OMEGA_LAMBDA * BUMP ** -0.5)
    fitted = math.log(bumped / base) / math.log(BUMP)
    predicted = (15 - DIST[rho]) / 60
    if abs(fitted - predicted) > 1e-9:
        raise AssertionError(f"{rho}: fitted {fitted:.6f} vs {predicted:.6f}")
check("exponent (15-d)/60 recovered for all eight irreps", True)
check("the electron (R7, d=4) moves as Lambda^(11/60)",
      abs((15 - DIST["R7"]) / 60 - 11 / 60) < 1e-12)

# ====================================================== 4. anchor-free class
print("\nCHECK 4  same-rho ratios are Lambda-free; the R1 ladder is the only one")
r1_base = [mass("R1", s) for s in ("triv", "std", "gal")]
r1_bump = [mass("R1", s, mu=MU_LAMBDA_GEV * BUMP ** 0.25,
                sqrt_omega=SQRT_OMEGA_LAMBDA * BUMP ** -0.5)
           for s in ("triv", "std", "gal")]
ratios_base = [r1_base[1] / r1_base[0], r1_base[2] / r1_base[0]]
ratios_bump = [r1_bump[1] / r1_bump[0], r1_bump[2] / r1_bump[0]]
check("R1 ladder ratios invariant under a 10% Lambda shift",
      all(abs(a / b - 1) < 1e-12 for a, b in zip(ratios_base, ratios_bump)),
      f"ratios {ratios_base[0]:.4g}, {ratios_base[1]:.4g}")
check("those ratios are pure torsion ratios",
      abs(ratios_base[0] - T2["R1"][1] / T2["R1"][0]) < 1e-12)
# A cross-rho ratio must NOT be invariant, or check 4 would be vacuous. Its
# Lambda exponent is (d_a - d_b)/60, so assert that value rather than clearing
# some arbitrary threshold: the shift is only 0.5% for a 10% bump on this pair,
# and a threshold loose enough to catch it would not distinguish it from noise.
cross_base = mass("R7", "triv") / mass("R1", "triv")
cross_bump = (mass("R7", "triv", mu=MU_LAMBDA_GEV * BUMP ** 0.25,
                   sqrt_omega=SQRT_OMEGA_LAMBDA * BUMP ** -0.5)
              / r1_bump[0])
cross_exp = math.log(cross_bump / cross_base) / math.log(BUMP)
cross_pred = (DIST["R1"] - DIST["R7"]) / 60
check("a cross-rho ratio DOES move, at exactly the predicted exponent",
      abs(cross_exp - cross_pred) < 1e-9 and abs(cross_pred) > 1e-12,
      f"exponent {cross_exp:.5f} = (d_R1 - d_R7)/60")

# ==================================================== 5. m_e <-> Lambda loop
print("\nCHECK 5  the m_e <-> Lambda loop closes at 2% forward, ~11% inverted")
forward = abs(mass("R7", "triv") / M_ELECTRON - 1)
inverted = forward * 60 / 11
check("forward closure ~2% in mass", 0.015 < forward < 0.030,
      f"{forward * 100:.1f}%")
check("inverse closure ~11% in Lambda", 0.09 < inverted < 0.14,
      f"{inverted * 100:.1f}%")

# ==================================================== 6. exact torsion algebra
print("\nCHECK 6  the closed-form torsion identities the table rests on")
check("Galois pair T2(R3)/T2(R4) = phi^-4",
      abs(T2["R3"][0] / T2["R4"][0] / PHI ** -4 - 1) < 2e-3)
check("Galois pair T2(R1)/T2(R2) = phi^-8",
      abs(T2["R1"][0] / T2["R2"][0] / PHI ** -8 - 1) < 2e-3)
int_product = T2["R3"][0] * T2["R7"][0] * T2["R5"][0] * T2["R4"][0]
half_product = T2["R1"][0] * T2["R2"][0] * T2["R6"][0] * T2["R8"][0]
check("integer-spin sector product = 4", abs(int_product / 4 - 1) < 2e-3,
      f"{int_product:.4f}")
check("half-integer sector product = 1/4", abs(half_product * 4 - 1) < 2e-3,
      f"{half_product:.4f}")
check("the two sector products are exact inverses",
      abs(int_product * half_product - 1) < 4e-3)
check("R7 is Galois-blind at 4",
      T2["R7"][1] == T2["R7"][2] == 4.000)

print("\nALL CHECKS PASSED\n")
