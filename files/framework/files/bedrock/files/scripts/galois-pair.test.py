#!/usr/bin/env python3
"""
galois-pair.test.py  --  executable verification of every rational in
bedrock/files/galois-pair.md ("The Galois Pair on S^3/2I").

Independent third route: builds the 2I character data from first principles
(chi_Q(g) = 2 cos(phi_g); Q' = Galois conjugate sqrt5 -> -sqrt5;
Sym^2 chi = chi^2 - 1) and re-derives, with exact arithmetic (sympy):

  - the character sums D_alpha                              (Prop 3.3)
  - the conversion identity rho = dim + 4(D - dim*D_1)      (Thm 1.1)
  - the printed rho pair and the -8/5 golden gate           (Prop 4.1, Cor 4.2)
  - golden-class localization (-57/4 ; +48 and 0)           (Cor 4.2)
  - the tautological charges k = rk*D_1 - D and k = cs mod1  (Prop 5.2)
  - the exact echo eps(H) = -72, k(R_Q)-k(R_Q') = -3/5       (Prop 5.3)
  - eta_Dir = 2 D_1, eta_Sign, Ruberman-Saveliev = 1         (consistency web)
  - E_8 mod-4 refinement: 136 / 120 and Gauss sum 16         (Lemma 6.1)

Every assertion is checked against the value printed in the paper.
"""
import sympy as sp

s5 = sp.sqrt(5)
sigma = lambda x: sp.simplify(sp.expand(x).subs(s5, -s5))   # Galois automorphism

PASS = []
def check(name, got, want):
    got = sp.nsimplify(sp.simplify(got))
    want = sp.nsimplify(want)
    ok = sp.simplify(got - want) == 0
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:44s} got {str(got):>10s}  want {str(want):>10s}")
    return ok

# ---- 2I conjugacy classes: (defining-rep angle phi, class size) --------------
angles = [sp.Integer(0), sp.pi, sp.pi/2, 2*sp.pi/3, sp.pi/3,
          sp.pi/5, 2*sp.pi/5, 3*sp.pi/5, 4*sp.pi/5]
sizes  = [1, 1, 30, 20, 20, 12, 12, 12, 12]
golden = [i for i,a in enumerate(angles) if a in (sp.pi/5, 2*sp.pi/5, 3*sp.pi/5, 4*sp.pi/5)]
assert sum(sizes) == 120, "class sizes must total |2I| = 120"

# ---- characters from first principles ---------------------------------------
chi_Q   = [sp.simplify(2*sp.cos(a)) for a in angles]          # defining rep
chi_Qp  = [sigma(c) for c in chi_Q]                           # Galois conjugate Q'
chi_S2Q = [sp.simplify(c**2 - 1) for c in chi_Q]              # Sym^2 Q  (SU(2): chi^2-1)
chi_S2Qp= [sigma(c) for c in chi_S2Q]                         # Sym^2 Q'
chi_triv= [sp.Integer(1)]*9

# cross-check the printed character table (section 2.2)
tbl = {'chi_Q':(chi_Q,[2,-2,0,-1,1,(1+s5)/2,(s5-1)/2,(1-s5)/2,-(1+s5)/2]),
       'chi_Qp':(chi_Qp,[2,-2,0,-1,1,(1-s5)/2,-(1+s5)/2,(1+s5)/2,(s5-1)/2]),
       'chi_S2Q':(chi_S2Q,[3,3,-1,0,0,(1+s5)/2,(1-s5)/2,(1-s5)/2,(1+s5)/2])}
print("Character table (derived vs printed table, section 2.2):")
for nm,(got,want) in tbl.items():
    ok = all(sp.simplify(g-w)==0 for g,w in zip(got,want))
    PASS.append(ok); print(f"  [{'PASS' if ok else 'FAIL'}] {nm}")

# ---- character sums D_alpha  (2 - chi_Q = det(I2 - g)) -----------------------
def D(chi):
    tot = 0
    for i in range(1, 9):                      # skip identity (i=0)
        tot += sizes[i]*chi[i]/(2 - chi_Q[i])
    return sp.simplify(tot/120)

D1, DQ, DQp, DS2Q, DS2Qp = map(D, (chi_triv, chi_Q, chi_Qp, chi_S2Q, chi_S2Qp))
print("\nCharacter sums D_alpha (Prop 3.3):")
check("D_1",        D1,   sp.Rational(1079,1440))
check("D_Q",        DQ,   sp.Rational(73,144))
check("D_Q'",       DQp,  sp.Rational(-67,720))
check("D_Sym2Q",    DS2Q, sp.Rational(9,32))
check("D_Sym2Q'",   DS2Qp,sp.Rational(-19,160))

# ---- Theorem 1.1: rho = dim + 4(D - dim*D_1) --------------------------------
rho = lambda dim, Da: dim + 4*(Da - dim*D1)
print("\nConversion identity Thm 1.1 -> rho invariants (Prop 4.1):")
check("rho_Q      (= -59/30)",     rho(2, DQ),    sp.Rational(-59,30))
check("rho_Q'     (= -131/30)",    rho(2, DQp),   sp.Rational(-131,30))
check("rho_Sym2Q  (= -73/15)",     rho(3, DS2Q),  sp.Rational(-73,15))
check("rho_Sym2Q' (= -97/15)",     rho(3, DS2Qp), sp.Rational(-97,15))

# ---- Corollary 4.2: golden gate and its support -----------------------------
print("\nGolden gate and localization (Cor 4.2):")
check("rho_Sym2Q' - rho_Sym2Q",    rho(3,DS2Qp)-rho(3,DS2Q), sp.Rational(-8,5))
check("4*(D_Sym2Q' - D_Sym2Q)",    4*(DS2Qp-DS2Q),           sp.Rational(-8,5))
# split D*120 into non-golden and golden contributions
def split(chi):
    ng = sum(sizes[i]*chi[i]/(2-chi_Q[i]) for i in range(1,9) if i not in golden)
    gd = sum(sizes[i]*chi[i]/(2-chi_Q[i]) for i in golden)
    return sp.simplify(ng), sp.simplify(gd)
ngS2Q, gdS2Q   = split(chi_S2Q)
ngS2Qp, gdS2Qp = split(chi_S2Qp)
check("non-golden sum (Sym2Q)",  ngS2Q,  sp.Rational(-57,4))
check("non-golden sum (Sym2Q')", ngS2Qp, sp.Rational(-57,4))
check("golden sum (Sym2Q)  = 48", gdS2Q,  48)
check("golden sum (Sym2Q') = 0",  gdS2Qp, 0)

# ---- Section 5: tautological charges k = rk*D_1 - D --------------------------
k = lambda rk, Da: sp.simplify(rk*D1 - Da)
kQ, kQp, kS2Q, kS2Qp = k(2,DQ), k(2,DQp), k(3,DS2Q), k(3,DS2Qp)
print("\nTautological charges k = rk*D_1 - D  (Prop 5.2):")
check("k(R_Q)",       kQ,   sp.Rational(119,120))
check("k(R_Q')",      kQp,  sp.Rational(191,120))
check("k(R_Sym2Q)",   kS2Q, sp.Rational(59,30))
check("k(R_Sym2Q')",  kS2Qp,sp.Rational(71,30))
frac = lambda x: x - sp.floor(x)
print("  k = cs mod 1 in all four sectors:")
check("k(R_Q)   mod1 = cs(Q)   mod1",  frac(kQ),   frac(sp.Rational(-1,120)))
check("k(R_Q')  mod1 = cs(Q')  mod1",  frac(kQp),  frac(sp.Rational(-49,120)))
check("k(R_S2Q) mod1 = 4cs(Q)  mod1",  frac(kS2Q), frac(4*sp.Rational(-1,120)))
check("k(R_S2Q')mod1 = 4cs(Q') mod1",  frac(kS2Qp),frac(4*sp.Rational(-49,120)))

# ---- Prop 5.3: exact echo eps(H) = -72 --------------------------------------
print("\nExact echo (Prop 5.3):")
epsH = sp.simplify(120*(DQp - DQ))
check("eps(H) = 120*(D_Q' - D_Q)",  epsH, -72)
check("k(R_Q) - k(R_Q') = eps(H)/120", kQ - kQp, sp.Rational(-3,5))
check("k(R_S2Q') - k(R_S2Q) = +2/5",   kS2Qp - kS2Q, sp.Rational(2,5))

# ---- Consistency web: eta_Dir, eta_Sign, Ruberman-Saveliev ------------------
print("\nConsistency web (section 4):")
eta_Dir  = sp.simplify(2*D1)
cot2 = lambda phi: sp.simplify(sp.cot(phi/2)**2)
eta_Sign = sp.simplify(sum(sizes[i]*cot2(angles[i]) for i in range(1,9))/120)
check("eta_Dir  = 2 D_1 = 1079/720", eta_Dir,  sp.Rational(1079,720))
check("eta_Sign = 361/180",          eta_Sign, sp.Rational(361,180))
check("1/2 eta_Dir + 1/8 eta_Sign = 1 = -mu_bar",
      sp.Rational(1,2)*eta_Dir + sp.Rational(1,8)*eta_Sign, 1)

# ---- Lemma 6.1: E_8 mod-4 quadratic refinement ------------------------------
# E_8 Cartan (Gram) matrix, Bourbaki: chain 1-3-4-5-6-7-8, node 2 on node 4.
edges = [(1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4)]
G = sp.zeros(8,8)
for i in range(8): G[i,i] = 2
for a,b in edges: G[a-1,b-1] = G[b-1,a-1] = -1
print("\nE_8 mod-4 refinement (Lemma 6.1):")
check("det(E8 Cartan) = 1", G.det(), 1)
cnt = {0:0, 2:0}
roots = 0
for m in range(256):                              # {0,1}^8 lifts of F_2^8 classes
    xi = sp.Matrix([(m>>j)&1 for j in range(8)])
    q = int((xi.T*G*xi)[0,0]) % 4                 # P(x) = xi.xi mod 4
    cnt[q] = cnt.get(q,0)+1
gauss = cnt[0] - cnt[2]                            # sum of i^{P(x)}
check("# classes with P=0 (incl. 0) = 136", cnt[0], 136)
check("# classes with P=2         = 120", cnt[2], 120)
check("Gauss sum 136-120 = 16 = 2^(8/2)",  gauss, 16)

print("\n" + "="*66)
print(f"  galois-pair.md verification: {sum(PASS)}/{len(PASS)} checks PASS"
      + ("" if all(PASS) else "   *** FAILURES PRESENT ***"))
print("="*66)
import sys; sys.exit(0 if all(PASS) else 1)
