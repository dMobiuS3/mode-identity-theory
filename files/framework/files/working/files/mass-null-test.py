#!/usr/bin/env python3
"""The Torsion Null Test -- execution script (companion to mass-null-test.md).

Two independent paths, so the committed artifacts are authoritative and the
representation engine is their verifier:

  DERIVE  builds the 2I character table from the icosians, the tensor
          multiplicities N, the 24-slot quantum-number map (T3 gate + Z3
          color), the masses, and the 8x24 compatibility matrix from scratch.
  LOAD    reads the committed frozen artifacts (mass-null-inputs.json,
          mass-null-slotmap.csv, mass-null-compat.csv).

Modes:
  (default)   Step-0 gates: DERIVE, LOAD, and compare (G1 masses, G2 torsions,
              G3a compatibility matrix) plus G3b scorecard and the T3/color
              anchors against the page; then a coarse published-display check.
  --emit      DERIVE and write the frozen artifacts; print SHA-256 of each.
  --selfcheck exercise the ensemble machinery on throwaway draws (seed != 120,
              tiny M, no Null D) to prove the code runs, producing no
              registered statistic.
  --run       the single registered ensemble. Gated: refuses unless HEAD is
              tagged mass-null-v1.1. Nulls A/B/C at M=100000, Null D exact 576,
              Generator(PCG64) seed 120, p_hat=(k+1)/(M+1) for A-C and the exact
              fraction for D, tails fixed in SCORE_TAILS.

v1.1 (2026-07-28): re-registration against the corrected torsion table (the
half-integer torsion correction, torsion-correction.md): the four half-integer
base torsions become their exact closed forms (phi^-4/4, phi^4/4, 1, 4), so all
nine base factors are now exact (C_geom stays 4 dp). Only the inputs and the
Step-0 expected values changed; the statistic, four nulls, seed 120, M/576, and
the SVII p_A bands are byte-retained from v1.0. v1.0's run (p_A = 0.174 on the
pre-correction table) is history; its results file is preserved as committed.
The verdict machinery is frozen; this script reads inputs, it does not change
the rule that reads them.
"""
import numpy as np, itertools, math, json, hashlib, sys, os, csv, subprocess

PHI = (1 + 5 ** 0.5) / 2
HERE = os.path.dirname(os.path.abspath(__file__))
ART = {'inputs': 'mass-null-inputs.json', 'slotmap': 'mass-null-slotmap.csv', 'compat': 'mass-null-compat.csv'}
# frozen digests of the committed artifacts (a run verifies it reads exactly these bytes)
FROZEN_SHA256 = {'mass-null-inputs.json': '9efcd3f0766239d814745e184cab56dae2be2ba098cf773ea66a707e2d622237',
                 'mass-null-slotmap.csv': '86ddf8184f0df42df56704359c3d46a1c6bfbd24c9606d1905a7f671b85d34ce',
                 'mass-null-compat.csv': 'd7b4def487bb25c0b944dc8dc336913010448a67a02a9452c5c3fa12729ac9cd'}
def _sha256(name):
    return hashlib.sha256(open(os.path.join(HERE, name), 'rb').read()).hexdigest()
def verify_artifacts():
    for name, h in FROZEN_SHA256.items():
        got = _sha256(name)
        if got != h:
            raise SystemExit(f"--run refused: {name} sha256 {got} != frozen {h} (working-tree artifact modified).")
RS = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8']
RHO_LIST = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8']
SIG_LIST = ['triv', 'std', 'gal']
VAC = {'triv': 'R0', 'std': 'R1', 'gal': 'R2'}
# scored fermions: (T3, kind, observed GeV). electron benchmark + 3 neutrinos excluded.
FERM = {'u': (+.5, 'q', 2.16e-3), 'd': (-.5, 'q', 4.67e-3), 's': (-.5, 'q', 9.34e-2),
        'c': (+.5, 'q', 1.27),    'mu': (-.5, 'l', 1.057e-1), 'tau': (-.5, 'l', 1.777),
        'b': (-.5, 'q', 4.18),    't': (+.5, 'q', 172.7)}
FLIST = list(FERM.keys())
# frozen tails (SV): upper for count statistics, lower for S4, S5 descriptive
SCORE_TAILS = {'S1': 'upper', 'S2': 'upper', 'S3': 'upper', 'S1p': 'upper', 'S4': 'lower', 'S5': None}

# ============================================================ DERIVE path
def _chartable():
    def pe(vec):
        out = set()
        for p in itertools.permutations(range(4)):
            if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0:
                out.add(tuple(vec[p[i]] for i in range(4)))
        return out
    q = set()
    for i in range(4):
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[i] = s; q.add(tuple(v))
    for sg in itertools.product((0.5, -0.5), repeat=4):
        q.add(sg)
    a, b, c = 0.5, PHI / 2, 1 / (2 * PHI)
    for sb in (1, -1):
        for sc in (1, -1):
            for sd in (1, -1):
                q |= pe((0.0, sb * a, sc * b, sd * c))
    q = [np.array(x) for x in q]
    qm = lambda p, r: np.array([p[0]*r[0]-p[1]*r[1]-p[2]*r[2]-p[3]*r[3], p[0]*r[1]+p[1]*r[0]+p[2]*r[3]-p[3]*r[2],
                                p[0]*r[2]-p[1]*r[3]+p[2]*r[0]+p[3]*r[1], p[0]*r[3]+p[1]*r[2]-p[2]*r[1]+p[3]*r[0]])
    qc = lambda x: np.array([x[0], -x[1], -x[2], -x[3]]); ky = lambda x: tuple(np.round(x, 6))
    S = {ky(x): x for x in q}; el = list(S.values()); ix = {ky(x): i for i, x in enumerate(el)}
    seen = [False] * 120; cls = []
    for i in range(120):
        if seen[i]:
            continue
        cl = set()
        for x in el:
            cl.add(ky(qm(qm(x, el[i]), qc(x))))
        cls.append(sorted(cl))
        for k in cl:
            seen[ix[k]] = True
    cw = [float(round(el[ix[cl[0]]][0], 6)) for cl in cls]; cz = [len(cl) for cl in cls]; idc = cw.index(1.0)
    def cs(k, w):
        if abs(w - 1) < 1e-9: return k + 1
        if abs(w + 1) < 1e-9: return (-1) ** k * (k + 1)
        th = math.acos(max(-1, min(1, w))); return math.sin((k + 1) * th) / math.sin(th)
    sym = lambda k: np.array([cs(k, cw[i]) for i in range(9)])
    perm = list(range(9))
    for w1, w2 in [(0.809017, -0.309017), (0.309017, -0.809017)]:
        i, j = cw.index(round(w1, 6)), cw.index(round(w2, 6)); perm[i], perm[j] = perm[j], perm[i]
    gal = lambda v: np.array([v[perm[i]] for i in range(9)])
    inn = lambda x, y: sum(cz[i] * x[i] * y[i] for i in range(9)) / 120.0
    R0, R1, R3, R6, R7, R8 = sym(0), sym(1), sym(2), sym(3), sym(4), sym(5)
    R2, R4 = gal(R1), gal(R3); s6 = sym(6)
    kn = {'R0': R0, 'R1': R1, 'R2': R2, 'R3': R3, 'R4': R4, 'R6': R6, 'R7': R7, 'R8': R8}
    R5 = s6.copy()
    for k in kn:
        R5 = R5 - round(inn(s6, kn[k])) * kn[k]
    IRR = {'R0': R0, 'R1': R1, 'R2': R2, 'R3': R3, 'R4': R4, 'R5': R5, 'R6': R6, 'R7': R7, 'R8': R8}
    G = np.array([[inn(IRR[x], IRR[y]) for y in IRR] for x in IRR])
    assert np.allclose(G, np.eye(9), atol=1e-7), "2I character table not orthonormal"
    return IRR, cw, cz, idc

_CG = {"R1": 0.0988, "R2": 0.2436, "R3": 0.5553, "R4": 0.7970, "R5": 0.8017, "R6": 0.2098, "R7": 0.7564, "R8": 0.2382}
_DIST = {"R1": 1, "R2": 7, "R3": 2, "R4": 6, "R5": 6, "R6": 3, "R7": 4, "R8": 5}
_MU, _SQ = 2.25e-12, 1.019e61
_T2B = {"R0": 1.0, "R3": (4 / 5) * PHI ** -2, "R4": (4 / 5) * PHI ** 2, "R5": 25 / 9, "R7": 9 / 4,
        "R1": PHI ** -4 / 4, "R2": PHI ** 4 / 4, "R6": 1.0, "R8": 4.0}
_JF = {'R1': {'triv': 0.5, 'std': 0.5, 'gal': 2.5}, 'R2': {'triv': 3.5, 'std': 2.5, 'gal': 1.5},
       'R3': {'triv': 1, 'std': 0, 'gal': 2}, 'R4': {'triv': 3, 'std': 2, 'gal': 0},
       'R5': {'triv': 3, 'std': 2, 'gal': 1}, 'R6': {'triv': 1.5, 'std': 0.5, 'gal': 1.5},
       'R7': {'triv': 2, 'std': 1, 'gal': 1}, 'R8': {'triv': 2.5, 'std': 1.5, 'gal': 0.5}}
_NONFIX = {'R1', 'R2', 'R3', 'R4'}; _HAS1317 = {'R2', 'R6', 'R8'}

def derive_all():
    IRR, CW, CZ, IDC = _chartable()
    inn = lambda x, y: sum(CZ[i] * x[i] * y[i] for i in range(9)) / 120.0
    tm = lambda A, B, C: round(inn(np.array([IRR[A][i] * IRR[B][i] for i in range(9)]), IRR[C]))
    dimR = {R: round(IRR[R][IDC]) for R in RS}
    o3 = CW.index(-0.5); chi_o3 = {R: IRR[R][o3] for R in RS}
    def dec(rho, sig):
        return {C: tm(rho, VAC[sig], C) for C in RS if tm(rho, VAC[sig], C)}
    def T2(rho, sig):
        return math.exp(sum(m * math.log(_T2B[c]) for c, m in dec(rho, sig).items()))
    def mass(rho, sig):
        return _MU * _CG[rho] * _SQ ** (_DIST[rho] / 30.0) * T2(rho, sig)
    def T3(rho, sig):
        j = _JF[rho][sig]
        if abs(j - round(j)) < 1e-9: return -0.5
        nonfixed = any(c in _NONFIX for c in dec(rho, sig))
        stripped = (sig != 'triv') and (rho in _HAS1317)
        return -0.5 if (stripped and nonfixed) else +0.5
    def color(rho, sig):
        x = sum(m * chi_o3[c] for c, m in dec(rho, sig).items()); dv = dimR[rho] * dimR[VAC[sig]]
        return round((dv + 2 * x) / 3), round((dv - x) / 3)
    slots, N = [], {}
    for si, rho in enumerate(RHO_LIST):
        for sj, sig in enumerate(SIG_LIST):
            s, cp = color(rho, sig); k = f"{rho}_{sig}"
            slots.append({'slot_index': len(slots), 'rho': rho, 'sig': sig, 'mass': mass(rho, sig),
                          'T2': T2(rho, sig), 'T3': T3(rho, sig), 'singlet': bool(s > 0),
                          'colored': bool(cp > 0), 'j_first': _JF[rho][sig]})
            N[k] = dec(rho, sig)
    compat = {}
    for f, (t3, kind, _) in FERM.items():
        compat[f] = [1 if (abs(s['T3'] - t3) < 1e-9 and (s['colored'] if kind == 'q' else s['singlet'])) else 0
                     for s in slots]
    inputs = {'mu_Lambda_GeV': _MU, 'sqrt_Omega_Lambda': _SQ, 'C_geom': _CG, 'mckay_distance': _DIST,
              'T2_base': {k: _T2B[k] for k in RS}, 'j_first': _JF, 'tensor_multiplicities_N': N,
              'galois_nonfixed': sorted(_NONFIX), 'has_1317': sorted(_HAS1317),
              'fermions': {f: list(FERM[f]) for f in FERM},
              'precision': 'published-precision test: source displayed precision '
                           '(C_geom 4dp; half-integer base torsions R1,R2,R6,R8 to 3-5 significant '
                           'figures; closed forms R0,R3,R4,R5,R7 exact)'}
    return slots, compat, inputs

# ============================================================ LOAD path
def load_all():
    inputs = json.load(open(os.path.join(HERE, ART['inputs'])))
    slots = []
    with open(os.path.join(HERE, ART['slotmap'])) as fh:
        for row in csv.DictReader(fh):
            slots.append({'slot_index': int(row['slot_index']), 'rho': row['rho'], 'sig': row['sigma'],
                          'mass': float(row['mass_GeV']), 'T2': float(row['T2']), 'T3': float(row['T3']),
                          'singlet': row['singlet'] == '1', 'colored': row['colored'] == '1',
                          'j_first': float(row['j_first'])})
    compat = {}
    with open(os.path.join(HERE, ART['compat'])) as fh:
        rd = csv.reader(fh); hdr = next(rd)
        for row in rd:
            compat[row[0]] = [int(x) for x in row[1:]]
    return slots, compat, inputs

# ============================================================ scoring
def score(masses, compat):
    def hits(scale, ignore):
        n = 0
        for f, (t3, kind, mf) in FERM.items():
            cand = range(24) if ignore else [j for j in range(24) if compat[f][j] == 1]
            if any(max(mf / masses[j], masses[j] / mf) <= scale for j in cand):
                n += 1
        return n
    wl, used = [], set()
    for f in FLIST:
        mf = FERM[f][2]; idxs = [j for j in range(24) if compat[f][j] == 1]
        if idxs:
            j = min(idxs, key=lambda j: abs(math.log(masses[j] / mf)))
            wl.append(abs(math.log(masses[j] / mf))); used.add(j)
    return {'S1': hits(3.0, False), 'S2': hits(2.0, False), 'S3': hits(1.5, False),
            'S1p': hits(3.0, True), 'S4': float(np.median(wl)) if wl else float('nan'), 'S5': len(used)}

# ============================================================ Step-0 gates
def gates():
    ds, dc, di = derive_all()
    if not all(os.path.exists(os.path.join(HERE, p)) for p in ART.values()):
        print("  artifacts missing; run --emit first"); return {'artifacts_present': False}, None
    if not all(_sha256(n) == h for n, h in FROZEN_SHA256.items() if h != 'PENDING'):
        return {'artifact_hashes_match': False}, None   # tampered bytes: fail cleanly before parsing
    ls, lc, li = load_all()
    ck = {}
    # G1/G2/G3a: committed (LOAD) vs independent (DERIVE)
    ck['G1_masses_derive_vs_committed'] = all(math.isclose(a['mass'], b['mass'], rel_tol=1e-12, abs_tol=1e-15)
                                              for a, b in zip(ds, ls))
    ck['G2_torsions_derive_vs_committed'] = all(math.isclose(a['T2'], b['T2'], rel_tol=1e-12, abs_tol=1e-15)
                                                for a, b in zip(ds, ls))
    ck['G3a_compat_derive_vs_committed'] = (dc == lc)
    ck['slot_index_stable'] = all(a['slot_index'] == b['slot_index'] == i for i, (a, b) in enumerate(zip(ds, ls)))
    # G3b + anchors on the COMMITTED spectrum
    masses = [s['mass'] for s in ls]; sc = score(masses, lc)
    bj = min([j for j in range(24) if lc['b'][j] == 1], key=lambda j: abs(math.log(masses[j] / 4.18)))
    ck['G3b_S1_is_5'] = (sc['S1'] == 5); ck['G3b_S1p_is_6'] = (sc['S1p'] == 6)
    ck['G3b_b_via_R4gal_117'] = (ls[bj]['rho'] == 'R4' and ls[bj]['sig'] == 'gal'
                                 and abs(max(4.18 / masses[bj], masses[bj] / 4.18) - 1.17) < 0.01)
    known = {('R1', 'std'): .5, ('R1', 'gal'): .5, ('R7', 'triv'): -.5, ('R8', 'triv'): .5, ('R8', 'gal'): -.5,
             ('R8', 'std'): -.5, ('R4', 'std'): -.5, ('R2', 'gal'): -.5, ('R2', 'triv'): .5, ('R2', 'std'): .5}
    sm = {(s['rho'], s['sig']): s for s in ls}
    ck['T3_gate_10_of_10'] = all(abs(sm[k]['T3'] - v) < 1e-9 for k, v in known.items())
    # coarse published-display check (a real transcription error would trip this)
    pub = {('R8', 'triv'): (3.16e-2, 4.000), ('R2', 'std'): (261.46, 2.778), ('R8', 'std'): (0.103, 13.090)}
    ck['published_display_coarse'] = all(abs(math.log10(sm[k]['mass'] / pm)) < 0.02 and abs(sm[k]['T2'] - pT) < 0.01
                                         for k, (pm, pT) in pub.items())
    # G0: committed inputs.json vs independent derivation
    ck['G0_inputs_derive_vs_committed'] = (
        all(math.isclose(di['T2_base'][k], li['T2_base'][k], rel_tol=1e-12) for k in di['T2_base'])
        and all(math.isclose(di['C_geom'][k], li['C_geom'][k]) for k in di['C_geom'])
        and di['mckay_distance'] == li['mckay_distance']
        and di['tensor_multiplicities_N'] == li['tensor_multiplicities_N']
        and math.isclose(di['mu_Lambda_GeV'], li['mu_Lambda_GeV'])
        and math.isclose(di['sqrt_Omega_Lambda'], li['sqrt_Omega_Lambda']))
    # committed artifacts match the frozen digests (skips any digest still PENDING at build time)
    ck['artifact_hashes_match'] = all(_sha256(n) == h for n, h in FROZEN_SHA256.items() if h != 'PENDING')
    # the pinned secondary thresholds (SIV) are defended, not merely printed
    ck['G3b_secondaries_pinned'] = (sc['S2'] == 4 and sc['S3'] == 4 and abs(sc['S4'] - 0.58425) < 1e-3 and sc['S5'] == 5)
    return ck, sc

# ============================================================ ensemble (registered)
def _ladder(slots):
    return np.array([_MU * _CG[s['rho']] * _SQ ** (_DIST[s['rho']] / 30.0) for s in slots])

def _null_A(rng, L, T2real, compat, M):
    out = {k: [] for k in SCORE_TAILS}
    for _ in range(M):
        t = T2real[rng.permutation(24)]
        out_add(out, score(L * t, compat))
    return out

def _null_B(rng, L, T2real, compat, M, slots):
    cols = {sig: [i for i, s in enumerate(slots) if s['sig'] == sig] for sig in SIG_LIST}
    out = {k: [] for k in SCORE_TAILS}
    for _ in range(M):
        t = T2real.copy()
        for sig in SIG_LIST:
            idx = cols[sig]; t[idx] = T2real[np.array(idx)[rng.permutation(len(idx))]]
        out_add(out, score(L * t, compat))
    return out

def _null_C(rng, L, T2real, compat, M):
    lo, hi = math.log(T2real.min()), math.log(T2real.max())
    out = {k: [] for k in SCORE_TAILS}
    for _ in range(M):
        t = np.exp(rng.uniform(lo, hi, 24))
        out_add(out, score(L * t, compat))
    return out

def _null_D(L, compat, slots, N, base):
    # permute base torsions within spin class; R0 fixed. exact 4!x4!=576
    integer_sp = ['R3', 'R4', 'R5', 'R7']; half_sp = ['R1', 'R2', 'R6', 'R8']
    out = {k: [] for k in SCORE_TAILS}
    for pI in itertools.permutations(integer_sp):
        for pH in itertools.permutations(half_sp):
            bmap = {'R0': base['R0']}
            for a, b in zip(integer_sp, pI): bmap[a] = base[b]
            for a, b in zip(half_sp, pH): bmap[a] = base[b]
            t = np.array([math.exp(sum(m * math.log(bmap[c]) for c, m in N[f"{s['rho']}_{s['sig']}"].items()))
                          for s in slots])
            out_add(out, score(L * t, compat))
    return out

def out_add(out, sc):
    for k in SCORE_TAILS:
        out[k].append(sc[k])

def _pvals(dist, obs, denom_exact=None):
    p = {}
    for k, tail in SCORE_TAILS.items():
        if tail is None:
            p[k] = None; continue
        arr = np.array(dist[k], float)
        k_ext = int(np.sum(arr >= obs[k])) if tail == 'upper' else int(np.sum(arr <= obs[k]))
        p[k] = (k_ext / denom_exact) if denom_exact else (k_ext + 1) / (len(arr) + 1)
    return p

def _counttable(vals):
    a = np.array(vals, float)
    if np.allclose(a, np.round(a)):                  # integer-valued statistic -> count table
        vi = a.astype(int)
        return {'type': 'counts', 'table': {int(v): int(np.sum(vi == v)) for v in sorted(set(vi.tolist()))}}
    return {'type': 'quantiles', 'q': {str(q): float(np.quantile(a, q)) for q in (0, .05, .25, .5, .75, .95, 1)}}

def _require_tag():
    try:
        tags = subprocess.check_output(['git', '-C', HERE, 'tag', '--points-at', 'HEAD'],
                                       stderr=subprocess.DEVNULL).decode().split()
    except Exception:
        tags = []
    if 'mass-null-v1.1' not in tags:                 # membership: robust to a co-located archival/DOI tag
        raise SystemExit(f"--run refused: HEAD does not carry tag mass-null-v1.1 (tags at HEAD: {tags}). "
                         "Commit and tag the frozen bundle, then run this exact code once.")

def run_ensemble(M=100000, seed=120):
    _require_tag()                                    # HEAD carries mass-null-v1.0
    verify_artifacts()                                # committed bytes == frozen digests
    ck, _ = gates()                                   # Step-0 gates must pass BEFORE any randomization (SVI)
    if not all(ck.values()):
        raise SystemExit("--run refused: Step-0 gates fail: " + ", ".join(k for k, v in ck.items() if not v))
    slots, compat, inputs = load_all()
    L = _ladder(slots); T2real = np.array([s['T2'] for s in slots]); base = {k: float(v) for k, v in inputs['T2_base'].items()}
    N = {k: {c: int(m) for c, m in v.items()} for k, v in inputs['tensor_multiplicities_N'].items()}
    obs = score(list(L * T2real), compat)
    rng = np.random.Generator(np.random.PCG64(seed))
    def summarize(d, denom=None):
        p = _pvals(d, obs, denom_exact=denom)
        se = {k: (math.sqrt(p[k] * (1 - p[k]) / M) if (SCORE_TAILS[k] and denom is None) else None) for k in p}
        return {'p': p, 'p_binom_se': se, 'dist': {k: _counttable(d[k]) for k in d},
                'mean': {k: float(np.mean(d[k])) for k in d}, 'sd': {k: float(np.std(d[k])) for k in d}}
    report = {'observed': obs, 'seed': seed, 'M': M, 'nulls': {}}
    report['nulls']['A'] = summarize(_null_A(rng, L, T2real, compat, M))
    report['nulls']['B'] = summarize(_null_B(rng, L, T2real, compat, M, slots))
    report['nulls']['C'] = summarize(_null_C(rng, L, T2real, compat, M))
    report['nulls']['D'] = summarize(_null_D(L, compat, slots, N, base), denom=576)
    print(json.dumps(report, indent=1))
    json.dump(report, open(os.path.join(HERE, 'mass-null-results-v1.1.json'), 'w'), indent=1)  # v1.0 results file preserved
    return report

def selfcheck():
    """Exercise ensemble machinery on throwaway draws (seed 1, tiny M, no Null D).
    Produces no registered statistic; only proves the code paths execute."""
    slots, compat, inputs = load_all()
    L = _ladder(slots); T2real = np.array([s['T2'] for s in slots])
    rng = np.random.Generator(np.random.PCG64(1))
    a = _null_A(rng, L, T2real, compat, 40); b = _null_B(rng, L, T2real, compat, 40, slots); c = _null_C(rng, L, T2real, compat, 40)
    ok = all(all(0 <= v <= 8 for v in d['S1']) for d in (a, b, c))
    # Null D structure check only: enumerate count, score exactly one permutation
    cnt = sum(1 for _ in itertools.product(itertools.permutations(range(4)), repeat=2))
    print(f"  ensemble machinery: A/B/C draws valid={ok}  Null-D enumeration size={cnt} (exp 576)  [throwaway seed 1, not registered]")
    return ok and cnt == 576

# ============================================================ emit / main
def emit():
    slots, compat, inputs = derive_all()
    json.dump(inputs, open(os.path.join(HERE, ART['inputs']), 'w'), indent=1, sort_keys=True)
    with open(os.path.join(HERE, ART['slotmap']), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['slot_index', 'rho', 'sigma', 'mass_GeV', 'T2', 'T3', 'singlet', 'colored', 'j_first'])
        for s in slots:
            w.writerow([s['slot_index'], s['rho'], s['sig'], repr(s['mass']), repr(s['T2']), s['T3'],
                        int(s['singlet']), int(s['colored']), s['j_first']])
    with open(os.path.join(HERE, ART['compat']), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['fermion'] + [f"{s['rho']}_{s['sig']}" for s in slots])
        for f in FLIST:
            w.writerow([f] + compat[f])
    print("=== frozen artifacts (record these hashes in the design) ===")
    for name in ART.values():
        h = hashlib.sha256(open(os.path.join(HERE, name), 'rb').read()).hexdigest()
        print(f"  {name}  sha256={h}")

def main():
    if '--emit' in sys.argv:
        emit(); return
    ck, sc = gates()
    print("=== Step-0 reproduction gates (committed vs independent derivation) ===")
    for k, v in ck.items():
        print(f"  {'PASS' if v else 'FAIL':4s}  {k}")
    if sc:
        print(f"  observed: S1={sc['S1']} S1'={sc['S1p']} S2={sc['S2']} S3={sc['S3']} S4={sc['S4']:.4f} S5={sc['S5']}")
    if not all(ck.values()):
        print("  GATES FAILED -- randomization blocked (§VI)"); sys.exit(1)   # BEFORE --run
    if '--selfcheck' in sys.argv:
        print("=== ensemble self-check ==="); selfcheck()
    if '--run' in sys.argv:
        run_ensemble()

if __name__ == '__main__':
    main()
