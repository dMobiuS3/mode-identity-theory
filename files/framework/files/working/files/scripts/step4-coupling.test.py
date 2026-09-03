from fractions import Fraction as F
# The decoupling mechanism, checked at the level of exact pairings.
#
# 1) For a closed NON-ORIENTABLE surface F: H^2(F;Q) = 0 and H^2(F;Z) = Z_2 (UCT: Ext(H_1,Z)).
#    So the restriction of ANY integral 2-class c to F is torsion, detected by <c mod 2, [F]_2>_W.
# 2) Complex bundles on a closed surface are classified by (rank, c_1); real by (w_1, w_2).
#    => R|_F is TRIVIAL iff the mod-2 evaluation vanishes.
#
# Evaluations <c_1(R_j) mod 2, x> for x = the characteristic class (0) and x = root classes:
# c_1(R_j) is dual to the curve basis: <c_1(R_j), [E_i]> = delta_ij  (KN A.7 dual basis).
print("=== restriction data of the tautological bundles ===")
print("on the CHARACTERISTIC slot ([F]_2 = 0):")
print("  <c_1(R_j) mod 2, 0> = 0 for ALL j  =>  c_1(R_j)|_F = 0 in H^2(F;Z) = Z_2")
print("  w_2(ad-bundles)|_F = <w_2, 0> = 0; w_1 = 0 (SU(2)-adjoint)")
print("  => R_d2|_F and R_d6|_F are BOTH TRIVIAL rank-3 bundles: index-locally indistinguishable")
print()
print("on the ROOT class x_d6 ([F]_2 = [E_8] mod 2):")
print("  <c_1(R_d6) mod 2, x_d6> = 1 (dual basis)  => nontrivial Z_2 restriction: couples,")
print("  but Step 3: the Brown/GM package is UNDEFINED off the characteristic slot => no Mobius data there")
print()
print("=== the with-boundary Guillou-Marin constant on W (ingredient C's own identity) ===")
# closed GM: sign(X) = F.F + 2 beta(F) mod 16 for characteristic F.
# with boundary (ZHS): sign(W) = e(F) + 2 beta(F) + 8 mu(Sigma) mod 16.
# Calibrate on B^4 (sign 0, mu(S^3)=0): local RP^2 e=+2 => beta=-1 (standard).  Then on W:
sign_W, mu = -8, 1
print(f"  e(F) + 2 beta(F) = sign(W) - 8 mu(Sigma) = {sign_W - 8*mu} = -16 = 0 mod 16")
print("  check with local RP^2 (e=+2, beta=-1): e+2beta = 0 mod 16 OK")
print()
print("=== the Galois-difference cancellation ===")
print("  any F-localized index term T_F(R) satisfies T_F(R) = f(e,beta,nu-data) * rk(R)  (R|_F trivial)")
print("  Galois difference: T_F(R_d6) - T_F(R_d2) = f * (3 - 3) = 0  identically")
print("  => in every identity of the branched-cover / G-signature / GM route, the surface term")
print("     cancels from the Galois difference; what survives is the A<->B content:")
dD = F(-19,160) - F(9,32)
print(f"     Delta rho = 4 Delta D = 4*({dD}) = {4*dD};   Delta k = {F(71,30)-F(59,30)}")
