from fractions import Fraction as F

# Q(sqrt5): a + b*sqrt5
class S:
    def __init__(s,a,b=0): s.a=F(a); s.b=F(b)
    def __add__(s,o): o=S.c(o); return S(s.a+o.a, s.b+o.b)
    def __radd__(s,o): return s+o
    def __sub__(s,o): o=S.c(o); return S(s.a-o.a, s.b-o.b)
    def __mul__(s,o): o=S.c(o); return S(s.a*o.a+5*s.b*o.b, s.a*o.b+s.b*o.a)
    def __rmul__(s,o): return s*o
    def inv(s):
        d = s.a*s.a - 5*s.b*s.b
        return S(s.a/d, -s.b/d)
    @staticmethod
    def c(o): return o if isinstance(o,S) else S(o)
    def rat(s):
        assert s.b==0, f"not rational: {s.a}+{s.b}v5"
        return s.a
    def __repr__(s): return f"{s.a}" if s.b==0 else f"({s.a}+{s.b}v5)"

half=F(1,2)
# conjugacy classes (excluding identity): (size, chi_Q exact)
# chi_Q = 2cos(phi): pi:-2, pi/2:0, 2pi/3:-1, pi/3:1, pi/5:(1+v5)/2, 2pi/5:(v5-1)/2, 3pi/5:(1-v5)/2, 4pi/5:-(1+v5)/2
classes = [
 (1,  S(-2)),
 (30, S(0)),
 (20, S(-1)),
 (20, S(1)),
 (12, S(half,half)),
 (12, S(-half,half)),
 (12, S(half,-half)),
 (12, S(-half,-half)),
]
def galois(x): return S(x.a, -x.b)
def chi_sym2(chiQ, chiQ2):     # chi_Sym2(g) = (chi(g)^2 + chi(g^2))/2
    return S(half)*(chiQ*chiQ + chiQ2)
# chi_Q(g^2) = chi_Q^2 - 2  (since eigenvalues square: 2cos(2phi) = (2cos phi)^2 - 2)
reps = {}
reps['triv'] = [S(1) for _ in classes]
reps['Q']    = [c for _,c in classes]
reps['Qp']   = [galois(c) for _,c in classes]
reps['adQ']  = [chi_sym2(c, c*c - S(2)) for _,c in classes]
reps['adQp'] = [galois(x) for x in reps['adQ']]

def D(name):
    """KN sum: (1/120) sum_{g!=1} chi_W(g) / (2 - chi_Q(g)). This equals Int_X ch(R_W) Ahat by KN (A.2) with j=0."""
    tot = S(0)
    for (size, cq), chi in zip(classes, reps[name]):
        tot = tot + S(size) * chi * (S(2) - cq).inv()
    return (S(F(1,120)) * tot).rat()

print("=== KN boundary/Ahat sums D_W = (1/120) sum chi_W/(2-chi_Q)  [= Int ch(R_W) Ahat, KN (A.2) j=0] ===")
Dv = {}
for name in ['triv','Q','Qp','adQ','adQp']:
    Dv[name] = D(name)
    print(f"  D_{name:5s} = {Dv[name]}")
print()
print("=== item 3: untwisted APS consistency ==> eta_Dirac(+Sigma) = 2*D_triv (h=0, PSC) ===")
print(f"  eta_Dirac(Sigma(2,3,5), quotient orientation) = {2*Dv['triv']}   (denominator divides 720? {(2*Dv['triv']).denominator})")
print()
print("=== item 2: charges of the tautological bundles: k_i := rk_i * D_triv - D_{R_i}  (= Int(c2 - c1^2/2)) ===")
rk = {'Q':2, 'Qp':2, 'adQ':3, 'adQp':3}
cs = {'Q':F(-1,120), 'Qp':F(-49,120), 'adQ':4*F(-1,120), 'adQp':4*F(-49,120)}  # cs on +Sigma (Step 2); adjoint = 4x fund via Dynkin
for name in ['Q','Qp','adQ','adQp']:
    k = rk[name]*Dv['triv'] - Dv[name]
    csv = cs[name] % 1
    match = (k - (-cs[name])) % 1 == 0, (k - cs[name]) % 1 == 0
    print(f"  k({name:4s}) = {k}  = {float(k):+.6f};  k mod 1 = {k%1};  cs mod 1 = {csv};  k=-cs mod1: {match[0]}, k=+cs mod1: {match[1]}")
print()
print("=== item 1: the two boundary invariants side by side (odd-signature rho vs Dirac-type sum) ===")
# odd-signature rho on +Sigma (Step 2): -73/15, -97/15; on X_{+1}: +. Dirac-type: from D-sums.
# Degeratu convention: eta_chi(Dirac, flat chi) = -2 * (1/|G|) sum chi/(2-chi_Q)?? -> record as dictionary, values:
print(f"  odd-signature rho_ad(Q)  on +Sigma = -73/15;  rho_ad(Q') = -97/15;  diff = -8/5")
dQ  = Dv['adQ']  - 3*Dv['triv']   # 'reduced' Dirac-type rho-analogue: subtract dim*trivial
dQp = Dv['adQp'] - 3*Dv['triv']
print(f"  Dirac-type rho-analogue: D_adQ - 3 D_triv = {dQ};  D_adQ' - 3 D_triv = {dQp};  diff = {dQp - dQ}")
print(f"  fundamental: D_Q - 2 D_triv = {Dv['Q']-2*Dv['triv']};  D_Q' - 2 D_triv = {Dv['Qp']-2*Dv['triv']};  diff = {Dv['Qp']-Dv['Q']}")
print(f"  adjoint Dirac diff D_adQ' - D_adQ = {Dv['adQp']-Dv['adQ']}   vs odd-signature diff -8/5: DIFFERENT invariants, both golden-supported")

print()
print("=== item 4: Ruberman-Saveliev Thm 1.1 check on +Sigma: (1/2) eta_Dir + (1/8) eta_Sign = -mubar ===")
# eta_Dir(+Sigma) = 2*D_triv ; eta_Sign(+Sigma) = +(1/120) sum cot^2(phi/2)
cot2 = [S(0), S(1), S(F(1,3)), S(3), S(5,2), S(1,F(2,5)), S(5,-2), S(1,F(-2,5))]
etaSign = (S(F(1,120)) * sum((S(sz)*c2 for (sz,_),c2 in zip(classes,cot2)), S(0))).rat()
etaDir = 2*Dv['triv']
print(f"  eta_Sign(+Sigma) = (1/120) sum cot^2 = {etaSign}")
print(f"  eta_Dir(+Sigma)  = 2 D_triv = {etaDir}")
val = F(1,2)*etaDir + F(1,8)*etaSign
print(f"  (1/2)eta_Dir + (1/8)eta_Sign = {val}  ==> mubar = {-val}   (Neumann: (sigma - w^2)/8 = (-8-0)/8 = -1)")
print("  sign-sharpness: the four sign combinations give:",
      [F(1,2)*s1*etaDir + F(1,8)*s2*etaSign for s1 in (1,-1) for s2 in (1,-1)])
print()
print("=== bonus exact identities ===")
print(f"  k(Q')-k(Q)   = {F(191,120)-F(119,120)} = 72/120  (the affine-E8 augmentation eps(H) = -72 reappears as the exact charge difference)")
print(f"  k(adQ')-k(adQ) = {F(71,30)-F(59,30)} = 2/5 (the adjoint CS-difference representative of Step 1 App. A)")
print(f"  conversion identity on +Sigma: rho_sign = dim + 4(D - dim*D_triv):")
for name, dim, expect in [('Q',2,F(-59,30)), ('Qp',2,F(-131,30)), ('adQ',3,F(-73,15)), ('adQp',3,F(-97,15))]:
    got = dim + 4*(Dv[name] - dim*Dv['triv'])
    print(f"    {name:4s}: {got}  (expected {expect}: {'OK' if got==expect else 'MISMATCH'})")

print()
print("=== round-1 verifications ===")
# F2 structural note: golden-class contributions to the D-sums for adQ and adQ'
for name in ['adQ','adQp']:
    gold = S(0); rat = S(0)
    for idx, ((size, cq), chi) in enumerate(zip(classes, reps[name])):
        term = S(size) * chi * (S(2) - cq).inv()
        if idx >= 4: gold = gold + term
        else: rat = rat + term
    print(f"  {name}: golden-class total = {gold},  rational-class total = {rat}  (times 1/120)")
# F2 optional: signature-theorem route: Int Ahat = -(1/8)(sign + eta_Sign)
lhs = Dv['triv']
rhs = -F(1,8)*(F(-8) + etaSign)
print(f"  signature route: -(1/8)(sign + eta_Sign) = {rhs}  vs D_triv = {lhs}  match: {lhs == rhs}")
# F2 flag 2 oriented echo: k(Q) - k(Q') = D_Q' - D_Q = eps(H)/|Gamma|
print(f"  oriented echo: k(Q)-k(Q') = {(2*Dv['triv']-Dv['Q']) - (2*Dv['triv']-Dv['Qp'])} = eps(H)/120 = -72/120 = {F(-72,120)}")
# F2 flag 1 counterexample: alpha = Q + trivial (dim 3, one trivial constituent)
alphaD = Dv['Q'] + Dv['triv']
rhs_bad = 3 + 4*(alphaD - 3*Dv['triv'])
print(f"  hypothesis check: alpha = Q+triv: RHS = {rhs_bad} vs rho_Q = -59/30 = {F(-59,30)}  (offset = {rhs_bad - F(-59,30)}, the trivial multiplicity)")
