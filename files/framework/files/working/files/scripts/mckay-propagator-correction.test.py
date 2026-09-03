#!/usr/bin/env python3
"""Reproducible test for mckay-propagator-correction.md.

Runs the test protocol (SS6, SS11) against the actual mass-formula data
(mass-spectrum.md SS II). No fitted physics: it recomputes the published
masses, the SIGNED residuals, and checks whether any parameter-free,
path-based correction tracks them. Result: none do (see the note's Result
section). Run: python3 mckay-propagator-correction.test.py

NOTE (2026-07-11): reflects the pre-July-2026 published table. The T^2(R_0)
correction (mass-spectrum SS4) set T^2(R_0)=1, recomputing the two diagonal
entries: (R2,gal)=b -> ~197 GeV (now uncounted, tally 5-of-8) and
(R1,std)=nu1 -> 7.3e-12. The T2 table and pub dict below are kept as the
2026-06 diagnostic record; they intentionally still reproduce the old values.
"""
import math

# ---- formula constants (mass-spectrum.md SS II) ----
mu = 2.25e-12          # GeV  (mu_Lambda)
sqrtOmega = 1.019e61   # (sqrt Omega_Lambda)

Cgeom = {"R1":0.0988,"R2":0.2436,"R3":0.5553,"R4":0.7970,
         "R5":0.8017,"R6":0.2098,"R7":0.7564,"R8":0.2382}
dist  = {"R0":0,"R1":1,"R3":2,"R6":3,"R7":4,"R8":5,"R5":6,"R4":6,"R2":7}

# T^2(rho (x) sigma) table (SS II.4, the 24 values)
T2 = {
 "R1":{"triv":15.887,"std":0.00827,"gal":2.778},
 "R2":{"triv":0.473, "std":2.778, "gal":0.0567},
 "R3":{"triv":0.306, "std":68.765,"gal":0.257},
 "R4":{"triv":2.094, "std":0.257, "gal":2.048},
 "R5":{"triv":2.778, "std":0.122, "gal":4.089},
 "R6":{"triv":4.328, "std":0.688, "gal":4.712},
 "R7":{"triv":2.250, "std":1.114, "gal":1.114},
 "R8":{"triv":0.257, "std":13.090,"gal":1.910},
}

# unique shortest-path intermediate nodes (SS2.5)
intermediates = {
 "R1":[], "R3":["R1"], "R6":["R1","R3"], "R7":["R1","R3","R6"],
 "R8":["R1","R3","R6","R7"],
 "R5":["R1","R3","R6","R7","R8"], "R4":["R1","R3","R6","R7","R8"],
 "R2":["R1","R3","R6","R7","R8","R5"],
}

def mass(rho, sig):
    return mu * Cgeom[rho] * sqrtOmega**(dist[rho]/30.0) * T2[rho][sig]

def PiT(rho, sig):   # product of intermediate torsion (SS4.5, primary candidate)
    p = 1.0
    for i in intermediates[rho]: p *= T2[i][sig]
    return p

def PiC(rho):        # product of intermediate C_geom (SS4.1, vacuum-independent)
    p = 1.0
    for i in intermediates[rho]: p *= Cgeom[i]
    return p

# ---- assigned SM entries: (name, rho, sigma, observed GeV, clean?) ----
entries = [
 ("e",  "R7","triv",5.11e-4, True),
 ("u",  "R8","triv",2.16e-3, True),
 ("d",  "R8","gal", 4.67e-3, True),
 ("mu", "R8","std", 1.057e-1,True),
 ("s",  "R8","std", 9.34e-2, True),
 ("tau","R4","std", 1.777,   True),
 ("b",  "R2","gal", 4.18,    True),
 ("t",  "R2","std", 172.7,   True),
 ("nu1","R1","std", 1e-13,   False),  # observed inferred, soft
 ("nu3","R1","gal", 5.06e-11,False),  # proxy sqrt(dm2_31)
]

print("=== sanity: recomputed vs published predicted mass ===")
pub = {"e":5.21e-4,"u":2.03e-3,"d":1.51e-2,"mu":1.03e-1,"s":1.03e-1,
       "tau":7.34e-1,"b":5.33,"t":261.46,"nu1":1.98e-13,"nu3":6.67e-11}
for n,rho,sig,obs,clean in entries:
    m = mass(rho,sig)
    print(f"  {n:4s} {rho} {sig:4s}  recompute={m:.3e}  published={pub[n]:.3e}  ok={abs(math.log10(m/pub[n]))<0.02}")

print("\n=== signed residuals and candidate corrections ===")
print(f"{'f':4s} {'(rho,sig)':10s} {'dist':>4s} {'pred':>10s} {'obs':>10s} {'r=log(p/o)':>10s} {'|fold|':>7s} {'log PiT':>8s} {'log PiC':>8s}")
rows=[]
for n,rho,sig,obs,clean in entries:
    m=mass(rho,sig); r=math.log10(m/obs); fold=10**abs(r)
    lpt=math.log10(PiT(rho,sig)); lpc=math.log10(PiC(rho))
    rows.append((n,rho,sig,dist[rho],m,obs,r,lpt,lpc,clean))
    print(f"{n:4s} ({rho},{sig:4s}) {dist[rho]:>4d} {m:>10.3e} {obs:>10.3e} {r:>+10.3f} {fold:>7.2f} {lpt:>8.3f} {lpc:>8.3f}")

# ---- correlation of SIGNED residual with each candidate (clean set) ----
def pearson(xs,ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    sxy=sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    sxx=sum((x-mx)**2 for x in xs); syy=sum((y-my)**2 for y in ys)
    return sxy/math.sqrt(sxx*syy) if sxx>0 and syy>0 else float('nan')

clean=[row for row in rows if row[9] and row[0]!="s"]  # drop soft nu and the s/mu duplicate
r_vals=[row[6] for row in clean]
print("\n=== does any candidate track the SIGNED residual? (clean charged set, n=%d) ==="%len(clean))
for label,idx in [("log PiT (SS4.5)",7),("log PiC (SS4.1)",8),("dist (baseline)",3)]:
    x=[row[idx] for row in clean]
    rho_p=pearson(x,r_vals)
    mx=sum(x)/len(x); my=sum(r_vals)/len(r_vals)
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,r_vals)); den=sum((xi-mx)**2 for xi in x)
    p = num/den if den else float('nan'); b=my-p*mx
    resid=[yi-(p*xi+b) for xi,yi in zip(x,r_vals)]
    rms0=math.sqrt(sum(yi**2 for yi in r_vals)/len(r_vals))
    rms1=math.sqrt(sum(e**2 for e in resid)/len(resid))
    print(f"  {label:18s}  Pearson={rho_p:+.3f}  best p={p:+.3f}  RMS resid {rms0:.3f} -> {rms1:.3f}")

print("\n=== critical check: largest |residual| assigned fermions ===")
for row in sorted(clean,key=lambda r:abs(r[6]),reverse=True)[:3]:
    print(f"  {row[0]:4s} ({row[1]},{row[2]}): r={row[6]:+.3f} -> {'OVERshoot' if row[6]>0 else 'UNDERshoot'} by {10**abs(row[6]):.2f}x")
