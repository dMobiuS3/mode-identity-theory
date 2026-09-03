import itertools
from fractions import Fraction

# Finite E8 in the McKay/curve basis, nodes 1..8 (index 0..7 here):
# chain 1-2-3-4-5-6-7, branch 5-8. Node1=Q(d1), Node2=Sym2Q(d2), Node5=trivalent(d5),
# Node6=(d6, mark4), Node7=Q'(d7), Node8=Sym2Q'(d6, mark3, short arm).
edges = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8)]
n = 8
A = [[0]*n for _ in range(n)]
for i,j in edges:
    A[i-1][j-1] = A[j-1][i-1] = 1
C = [[(2 if i==j else -A[i][j]) for j in range(n)] for i in range(n)]  # E8 Cartan
# intersection form of W = -C

# det(C) = 1?
def det_int(M):
    M = [row[:] for row in M]; N = len(M); d = Fraction(1)
    for c in range(N):
        p = next((r for r in range(c,N) if M[r][c]!=0), None)
        if p is None: return 0
        if p!=c: M[c],M[p]=M[p],M[c]; d=-d
        d *= M[c][c]
        for r in range(c+1,N):
            f = Fraction(M[r][c],M[c][c])
            M[r] = [Fraction(M[r][k])-f*M[c][k] for k in range(N)]
    return d
print("det(Cartan E8) =", det_int(C), " (unimodular; so -C too)")

# mod 2: intersection form = A (adjacency). alternating: diag 0. nonsingular?
def det_mod2(M):
    M=[[x%2 for x in row] for row in M]; N=len(M)
    for c in range(N):
        p = next((r for r in range(c,N) if M[r][c]), None)
        if p is None: return 0
        M[c],M[p]=M[p],M[c]
        for r in range(N):
            if r!=c and M[r][c]:
                M[r]=[(M[r][k]+M[c][k])%2 for k in range(N)]
    return 1
print("mod-2 form (= E8 adjacency): alternating (diag 0), nonsingular =", bool(det_mod2(A)))

# Pontryagin square P(x) = xi.xi mod 4 for any integer lift xi (well-defined: even form).
# In the curve basis the form is -C; P(x) = -(x^T C x) mod 4 using the 0/1 lift.
def P(x):
    s = 0
    for i in range(n):
        for j in range(n):
            s += x[i]*C[i][j]*x[j]
    return (-s) % 4
vals = {}
for x in itertools.product((0,1), repeat=n):
    vals.setdefault(P(x), []).append(x)
N0, N2 = len(vals.get(0,[])), len(vals.get(2,[]))
print(f"P values: N0(P=0) = {N0} (incl. zero class), N2(P=2) = {N2}; other:", {k:len(v) for k,v in vals.items() if k not in (0,2)})
print("Gauss sum N0 - N2 =", N0 - N2, " (theory: 16*exp(2pi i sigma/8), sigma=-8 -> +16)")
print("plus-type isotropic count check: (2^3+1)(2^4-1) =", (2**3+1)*(2**4-1), "= nonzero P=0 classes:", N0-1)

# E8 roots via reflection closure in simple-root coordinates: s_i(x) = x - (sum_j C[i][j] x_j) e_i
def reflect(x, i):
    coef = sum(C[i][j]*x[j] for j in range(n))
    y = list(x); y[i] -= coef; return tuple(y)
roots = set()
frontier = set()
for i in range(n):
    e = tuple(1 if k==i else 0 for k in range(n)); roots.add(e); frontier.add(e)
while frontier:
    new = set()
    for x in frontier:
        for i in range(n):
            y = reflect(x, i)
            if y not in roots and tuple(-c for c in y) not in () :
                pass
            if y not in roots:
                new.add(y)
    roots |= new; frontier = new
print("root count (closure incl. negatives) =", len(roots), " (E8: 240)")
rc = {tuple(c%2 for c in r) for r in roots}
print("distinct root classes mod 2 =", len(rc), "; all have P=2:", all(P(x)==2 for x in rc))
print("root classes == all P=2 classes:", rc == set(map(tuple, vals[2])))

# Galois node e8 (index 7): pairings mod 2, hyperbolic pair with trivalent node e5 (index 4)
e8 = tuple(1 if k==7 else 0 for k in range(n))
e5 = tuple(1 if k==4 else 0 for k in range(n))
def dot2(x,y): return sum(x[i]*A[i][j]*y[j] for i in range(n) for j in range(n)) % 2
print("Galois class e8: P =", P(e8), "; e8.e8 =", dot2(e8,e8), "; e8.e5(trivalent) =", dot2(e8,e5), "-> hyperbolic pair")
print("e8 pairs nontrivially only with:", [k+1 for k in range(n) if dot2(e8, tuple(1 if j==k else 0 for j in range(n)))])

# arm structure sanity: T(2,3,5) arms from trivalent node 5: {8}, {6,7}, {4,3,2,1}
deg = [sum(A[i]) for i in range(n)]
print("degrees:", {i+1: deg[i] for i in range(n)}, " (node 5 trivalent)")
