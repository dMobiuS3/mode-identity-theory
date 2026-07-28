"""Torsion correction (2026-07-28): reproducible verification artifact.

Recomputes the Reidemeister torsion T^2(tau) of every 2I irrep on S^3/2I from the
spectral-zeta definition (twisted scalar + coexact one-form towers, Ray-Singer
combination  log T^2 = zeta'_coex(0) - 2 zeta'_scalar(0)), and certifies:

  1. ONE exact target, T^2(R7) = 9/4, fixes the overall sign convention; the
     remaining integer-spin closed forms (4/5)phi^-2, 25/9, (4/5)phi^2 then
     validate the pipeline as independent targets;
  2. the Galois ratios phi^-4 (R3/R4) and phi^-8 (R1/R2) and the sector products
     4 (integer) and 1/4 (half-integer), as consistency identities;
  3. the corrected half-integer closed forms  phi^-4/4, phi^4/4, 1, 4;
  4. THE DIAGNOSIS: the pre-correction page values (15.887, 0.473, 4.328, 0.257)
     equal exp(+zeta'_coex(0)), the coexact-only quantity (scalar term omitted;
     the scalar tower of a half-integer bundle is supported at odd n);
  5. the tensor multiplicities N_{rho sigma tau}, DERIVED from the reconstructed
     character table and gated against known decompositions and dimension sums;
  6. the 24-product propagation built from those derived N: the 12 revised
     ranked-table masses follow by the derived torsion ratios (page
     transcription), and the other 12 products are unchanged (ratio 1);
  7. the ladder splitting numbers quoted in mass-spectrum section V.

Scope: one implementation, validated as above; an independent-method
reproduction has not yet been performed and is queued on the OpenWave M8 track.

Meta-guard: every gate has a stable id; every mutation declares the gate id it
attacks; the suite FAILS unless (a) the set of mutation targets equals the set
of gate ids, so a gate without a mutation is itself a failure, and (b) every
mutation turns its gate red.

  python3 torsion-correction.test.py                   # verify (9+ gates)
  python3 torsion-correction.test.py --mutation-tests  # coverage + all defects red
  python3 torsion-correction.test.py --precise         # dps 50, jmax 80, sigma 1e-5
"""
import argparse
import math
import sys

import mpmath as mp
import numpy as np

labels = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
dims = [1, 2, 2, 3, 3, 4, 4, 5, 6]
idx = {l: i for i, l in enumerate(labels)}
edges = [("R0", "R1"), ("R1", "R3"), ("R3", "R6"), ("R6", "R7"),
         ("R7", "R8"), ("R8", "R5"), ("R5", "R2"), ("R8", "R4")]
classes = [(0.0, 1), (math.pi, 1), (math.pi / 2, 30), (math.pi / 3, 20),
           (2 * math.pi / 3, 20), (math.pi / 5, 12), (2 * math.pi / 5, 12),
           (3 * math.pi / 5, 12), (4 * math.pi / 5, 12)]
HALF = ["R1", "R2", "R6", "R8"]
INT_ = ["R3", "R4", "R5", "R7"]


def build(edge_list=edges, u_factor=True, co_shift=1):
    A = np.zeros((9, 9))
    for a, b in edge_list:
        A[idx[a], idx[b]] = A[idx[b], idx[a]] = 1
    thetas = np.array([c[0] for c in classes])
    sizes = np.array([c[1] for c in classes], float)

    def chiV(n, th):
        s = math.sin(th)
        if abs(s) < 1e-12:
            return (n + 1) * math.cos(n * th)
        return math.sin((n + 1) * th) / s

    m = [np.zeros(9) for _ in range(24)]
    m[0][idx["R0"]] = 1.0
    m[1][idx["R1"]] = 1.0
    for n in range(1, 23):
        m[n + 1] = A.dot(m[n]) - m[n - 1]
    Mmat = np.array([m[n] for n in range(9)])
    chi = np.zeros((9, 9))
    for c in range(9):
        rhs = np.array([chiV(n, thetas[c]) for n in range(9)])
        chi[:, c] = np.linalg.solve(Mmat, rhs)

    def mult(tau_i, n):
        if n < 0:
            return 0
        v = sum(sizes[c] * chiV(n, thetas[c]) * chi[tau_i][c] for c in range(9))
        return int(round(v / 120.0))

    def m0(tau_i):  # scalar tower, u = n+1; right-SU(2) degeneracy factor u
        return lambda u: (u if u_factor else 1) * mult(tau_i, u - 1)

    def mco(tau_i):  # coexact tower, u = l+1 >= 2
        return lambda u: (u + co_shift) * mult(tau_i, u - 2) + (u - co_shift) * mult(tau_i, u)

    return A, chi, sizes, m0, mco


def tensor_N(chi, sizes):
    """N[a][b][c] = mult of irrep c in a (x) b, derived from the character table."""
    N = np.zeros((9, 9, 9), int)
    for a in range(9):
        for b in range(9):
            for c in range(9):
                v = np.sum(sizes * chi[a] * chi[b] * chi[c]) / 120.0
                N[a, b, c] = int(round(v))
    return N


def quasi_quad(mult_fn):
    coeffs = []
    for r in range(60):
        us = [r + 120, r + 180, r + 240]
        M = np.array([[u * u, u, 1] for u in us], float)
        abc = np.linalg.solve(M, np.array([mult_fn(u) for u in us], float))
        for u in (r + 300, r + 360):
            if abs(abc[0] * u * u + abc[1] * u + abc[2] - mult_fn(u)) > 1e-4:
                raise RuntimeError(f"fit fails r={r}")
        coeffs.append(abc)
    return coeffs


class Cache:
    def __init__(self):
        self.c = {}

    def val(self, s, p, j, r):
        k = (str(s), p, j, r)
        if k not in self.c:
            k0 = 0
            while 60 * k0 + r < 2:
                k0 += 1
            z = 2 * s + 2 * j - p
            self.c[k] = mp.power(60, -z) * mp.zeta(z, mp.mpf(k0) + mp.mpf(r) / 60)
        return self.c[k]


def zeta_prime0(coeffs, cache, jmax, exact_sq, sigma):
    def zf(s):
        tot = mp.mpf(0)
        if exact_sq:
            for r in range(60):
                for p, cf in ((2, coeffs[r][0]), (1, coeffs[r][1]), (0, coeffs[r][2])):
                    if abs(cf) > 1e-12:
                        tot += mp.mpf(cf) * cache.val(s, p, 0, r)
            return tot
        g = mp.mpf(1)
        for j in range(jmax):
            if j > 0:
                g *= (s + j - 1) / j
            inner = mp.mpf(0)
            for r in range(60):
                for p, cf in ((2, coeffs[r][0]), (1, coeffs[r][1]), (0, coeffs[r][2])):
                    if abs(cf) > 1e-12:
                        inner += mp.mpf(cf) * cache.val(s, p, j, r)
            tot += g * inner
        return tot
    ss = [sigma * k for k in (-2, -1, 1, 2)]
    vals = [zf(mp.mpf(s)) for s in ss]
    M = mp.matrix([[mp.mpf(s) ** i for i in range(4)] for s in ss])
    return mp.lu_solve(M, mp.matrix(vals))[1]


def torsion_X(jmax, sigma, u_factor=True, co_shift=1, only=None):
    """Return (X, Xco) per irrep: X = zeta'_co - 2 zeta'_0 (log T^2 up to sign), Xco = zeta'_co."""
    _, _, _, m0f, mcof = build(edges, u_factor, co_shift)
    c0, cco = Cache(), Cache()
    X, Xco = {}, {}
    for l in (only or labels[1:]):
        zp0 = zeta_prime0(quasi_quad(m0f(idx[l])), c0, jmax, False, sigma)
        zpc = zeta_prime0(quasi_quad(mcof(idx[l])), cco, 0, True, sigma)
        X[l] = zpc - 2 * zp0
        Xco[l] = zpc
    return X, Xco


def products_from_N(N, singles):
    """T^2(rho x sigma) for sigma in {triv, std=R1, gal=R2}, propagated via derived N."""
    out = {}
    for l in labels[1:]:
        row = {"triv": singles[l]}
        for vname, vi in (("std", idx["R1"]), ("gal", idx["R2"])):
            lg = mp.mpf(0)
            for t in range(9):
                n = N[idx[l], vi, t]
                if n:
                    lg += n * mp.log(singles[labels[t]])
            row[vname] = mp.e ** lg
        out[l] = row
    return out


GATES, MUTS = [], []


def gate(gid, name, ok):
    GATES.append((gid, name, bool(ok)))
    print(f"  {'PASS' if ok else 'FAIL'}  [{gid}] {name}")


def mutation(target_gid, name, went_red):
    MUTS.append((target_gid, name, bool(went_red)))
    print(f"  {'RED (ok)' if went_red else 'STILL PASSING (BAD)'}  [{target_gid}] {name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutation-tests", action="store_true")
    ap.add_argument("--precise", action="store_true")
    args = ap.parse_args()
    mp.mp.dps = 50 if args.precise else 30
    jmax = 80 if args.precise else 55
    sigma = mp.mpf("1e-5") if args.precise else mp.mpf("1e-4")

    A, chi, sizes, _, _ = build()
    N = tensor_N(chi, sizes)
    phi = (1 + mp.sqrt(5)) / 2
    print("=" * 68)
    print("TORSION CORRECTION VERIFICATION (2026-07-28)")
    print("=" * 68)

    X, Xco = torsion_X(jmax, sigma)
    sign = 1 if abs(mp.e ** X["R7"] - mp.mpf(9) / 4) < abs(mp.e ** -X["R7"] - mp.mpf(9) / 4) else -1
    T2 = {l: mp.e ** (sign * X[l]) for l in labels[1:]}
    T2["R0"] = mp.mpf(1)
    Tco = {l: mp.e ** Xco[l] for l in labels[1:]}

    Gm = np.array([[np.sum(sizes * chi[i] * chi[j]) / 120.0 for j in range(9)] for i in range(9)])
    gate("char_orthonormality", "character table orthonormal",
         np.max(np.abs(Gm - np.eye(9))) < 1e-9)
    gate("e8_marks", "dims are affine E8 marks (A.dims = 2 dims)",
         np.allclose(A.dot(np.array(dims, float)), 2.0 * np.array(dims, float)))
    gate("r7_sign_calibration", "T^2(R7) = 9/4 (fixes the sign convention; magnitude a target)",
         abs(T2["R7"] / (mp.mpf(9) / 4) - 1) < 1e-8)
    tgt_int = {"R3": mp.mpf(4) / 5 * phi ** -2, "R5": mp.mpf(25) / 9, "R4": mp.mpf(4) / 5 * phi ** 2}
    gate("int_closed_forms", "independent integer-spin closed forms R3, R5, R4 (1e-8)",
         all(abs(T2[l] / t - 1) < 1e-8 for l, t in tgt_int.items()))
    tgt_half = {"R1": phi ** -4 / 4, "R2": phi ** 4 / 4, "R6": mp.mpf(1), "R8": mp.mpf(4)}
    gate("half_closed_forms", "corrected half-integer closed forms (4/4, 1e-8)",
         all(abs(T2[l] / t - 1) < 1e-8 for l, t in tgt_half.items()))
    gate("galois_ratios", "phi^-4 (R3/R4) and phi^-8 (R1/R2), 1e-10",
         abs(T2["R3"] / T2["R4"] / phi ** -4 - 1) < 1e-10
         and abs(T2["R1"] / T2["R2"] / phi ** -8 - 1) < 1e-10)
    gate("sector_products", "integer product = 4, half-integer product = 1/4",
         abs(T2["R3"] * T2["R7"] * T2["R5"] * T2["R4"] - 4) < 1e-8
         and abs(T2["R1"] * T2["R2"] * T2["R6"] * T2["R8"] - mp.mpf(1) / 4) < 1e-8)
    known = [("R1", "R1", {"R0": 1, "R3": 1}), ("R2", "R2", {"R0": 1, "R4": 1}),
             ("R7", "R1", {"R6": 1, "R8": 1}), ("R8", "R1", {"R7": 1, "R5": 1, "R4": 1}),
             ("R4", "R2", {"R2": 1, "R6": 1})]
    ok_n = all(all(N[idx[a], idx[b], idx[c]] == v for c, v in dec.items())
               and sum(N[idx[a], idx[b], t] * dims[t] for t in range(9)) == dims[idx[a]] * dims[idx[b]]
               for a, b, dec in known)
    ok_n &= all(sum(N[a, b, t] * dims[t] for t in range(9)) == dims[a] * dims[b]
                for a in range(9) for b in range(9))
    gate("tensor_N", "derived N: known decompositions + dimension sums (81 pairs)", ok_n)
    old_page = {"R1": 15.887, "R2": 0.473, "R6": 4.328, "R8": 0.257}
    gate("diagnosis_coexact_only", "pre-correction values = coexact-only (4/4)",
         all(abs(float(Tco[l]) - v) / v < 2e-3 for l, v in old_page.items()))
    # 24-product propagation from derived N, old (coexact-only halves) vs new
    singles_old = {l: (Tco[l] if l in HALF else T2[l]) for l in labels[1:]}
    singles_old["R0"] = mp.mpf(1)
    prod_old = products_from_N(N, singles_old)
    prod_new = products_from_N(N, T2)
    page_rev = {("R1", "triv"): (3.81e-10, 8.75e-13), ("R2", "triv"): (44.54, 161.3),
                ("R6", "triv"): (2.57e-6, 5.94e-7), ("R8", "triv"): (2.03e-3, 3.16e-2),
                ("R3", "std"): (1.00e-6, 5.30e-10), ("R3", "gal"): (3.75e-9, 5.83e-8),
                ("R4", "std"): (7.34e-1, 11.41), ("R4", "gal"): (5.84, 4.89),
                ("R5", "std"): (3.49e-1, 19.64), ("R5", "gal"): (11.72, 4.18e-1),
                ("R7", "std"): (2.58e-4, 9.26e-4), ("R7", "gal"): (2.58e-4, 9.26e-4)}
    ok_t = all(abs(float(old_m * prod_new[l][v] / prod_old[l][v]) - new_m) / new_m < 6e-3
               for (l, v), (old_m, new_m) in page_rev.items())
    gate("transcription_masses", "12 revised masses via derived product ratios", ok_t)
    unchanged = [(l, v) for l in labels[1:] for v in ("triv", "std", "gal")
                 if (l, v) not in page_rev]
    gate("unchanged_products", "the other 12 products have ratio exactly 1",
         len(unchanged) == 12 and all(
             abs(prod_new[l][v] / prod_old[l][v] - 1) < 1e-8 for l, v in unchanged))
    m1, m2, m3 = 0.875e-3, 7.33e-3, 66.7e-3
    gate("splittings", "section V numbers (5.3e-5, 4.5e-3 eV^2)",
         abs((m2 ** 2 - m1 ** 2) / 5.3e-5 - 1) < 0.02
         and abs((m3 ** 2 - m1 ** 2) / 4.45e-3 - 1) < 0.02)

    n_fail = sum(1 for _, _, ok in GATES if not ok)
    print(f"GATES: {len(GATES) - n_fail}/{len(GATES)} pass")

    if args.mutation_tests:
        print("=" * 68)
        print("MUTATION TESTS (registry: every gate id must be attacked and go red)")
        print("=" * 68)
        chi_bad = chi.copy()
        chi_bad[3] *= 1.05
        Gb = np.array([[np.sum(sizes * chi_bad[i] * chi_bad[j]) / 120.0 for j in range(9)]
                       for i in range(9)])
        mutation("char_orthonormality", "character row scaled 1.05",
                 np.max(np.abs(Gb - np.eye(9))) >= 1e-9)
        bad_edges = [e for e in edges if e != ("R8", "R4")] + [("R7", "R4")]
        Ab = np.zeros((9, 9))
        for a, b in bad_edges:
            Ab[idx[a], idx[b]] = Ab[idx[b], idx[a]] = 1
        mutation("e8_marks", "R8-R4 edge moved to R7-R4",
                 not np.allclose(Ab.dot(np.array(dims, float)), 2.0 * np.array(dims, float)))
        mutation("r7_sign_calibration", "X(R7) perturbed by +0.01: both sign branches miss 9/4",
                 min(abs(mp.e ** (X["R7"] + mp.mpf("0.01")) - mp.mpf(9) / 4),
                     abs(mp.e ** -(X["R7"] + mp.mpf("0.01")) - mp.mpf(9) / 4)) >= 1e-8)
        Xm, _ = torsion_X(jmax, sigma, u_factor=False, only=["R3"])
        mutation("int_closed_forms", "scalar tower without the u-degeneracy factor breaks R3",
                 abs(mp.e ** (sign * Xm["R3"]) / tgt_int["R3"] - 1) >= 1e-8)
        Xm, _ = torsion_X(jmax, sigma, co_shift=2, only=["R3"])
        mutation("int_closed_forms", "coexact multiplicity shift breaks R3",
                 abs(mp.e ** (sign * Xm["R3"]) / tgt_int["R3"] - 1) >= 1e-8)
        mutation("half_closed_forms", "coexact-only (the pre-correction method) breaks R1 = phi^-4/4",
                 abs(Tco["R1"] / (phi ** -4 / 4) - 1) >= 1e-8)
        mutation("galois_ratios", "T^2(R1) perturbed 1%: phi^-8 ratio fails",
                 abs((T2["R1"] * mp.mpf("1.01")) / T2["R2"] / phi ** -8 - 1) >= 1e-10)
        mutation("sector_products", "T^2(R8) perturbed 1%: half-integer product misses 1/4",
                 abs(T2["R1"] * T2["R2"] * T2["R6"] * (T2["R8"] * mp.mpf("1.01")) - mp.mpf(1) / 4) >= 1e-8)
        chi_swap = chi.copy()
        chi_swap[[idx["R3"], idx["R4"]]] = chi_swap[[idx["R4"], idx["R3"]]]
        Nb = tensor_N(chi_swap, sizes)
        mutation("tensor_N", "R3/R4 character rows swapped: known decompositions break",
                 not all(all(Nb[idx[a], idx[b], idx[c]] == v for c, v in dec.items())
                         for a, b, dec in known))
        mutation("diagnosis_coexact_only", "perturbed transcribed target (15.887 -> 15.0)",
                 not abs(float(Tco["R1"]) - 15.0) / 15.0 < 2e-3)
        mutation("transcription_masses", "perturbed revised mass (161.3 -> 150)",
                 not abs(float(44.54 * prod_new["R2"]["triv"] / prod_old["R2"]["triv"]) - 150.0) / 150.0 < 6e-3)
        mutation("unchanged_products", "an unchanged product perturbed 1%: ratio leaves 1",
                 abs((prod_new["R6"]["std"] * mp.mpf("1.01")) / prod_old["R6"]["std"] - 1) >= 1e-8)
        mutation("splittings", "m2 perturbed (7.33 -> 8.0 meV): solar splitting fails",
                 not abs((8.0e-3 ** 2 - m1 ** 2) / 5.3e-5 - 1) < 0.02)

        gate_ids = {g for g, _, _ in GATES}
        target_ids = {t for t, _, _ in MUTS}
        cover_ok = gate_ids == target_ids
        red_ok = all(r for _, _, r in MUTS)
        print(f"COVERAGE: gate ids == mutation targets: {cover_ok}"
              + ("" if cover_ok else f"  (uncovered: {sorted(gate_ids - target_ids)};"
                                     f" unknown targets: {sorted(target_ids - gate_ids)})"))
        print(f"ALL RED: {red_ok}")
        if not (cover_ok and red_ok):
            print("META-GUARD FAILED. Exiting nonzero.")
            sys.exit(2)
        print(f"MUTATIONS: {len(MUTS)} declared, every gate attacked, every defect red.")

    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
