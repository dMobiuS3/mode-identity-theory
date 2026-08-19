# Group facts about 2I used by sampler-first-test.md, section 5.
#
# 2I is built by closing a generating pair of unit quaternions under multiplication.
# The build is self-verifying: the closure must be a group of order 120 with nine
# conjugacy classes before any fact below is asserted.
#
# Facts established (all asserted, so this file fails loudly if any is wrong):
#   1. exactly one conjugacy class is closed under g -> -g: the order-4 class, size 30
#   1b. the other eight classes are swapped in four pairs
#   2. 2I has exactly one element of order 2, the central -1
#      (with Cauchy: every even-order subgroup contains -1, so -1 in S iff |S| even)
#   3. element orders are 1,2,3,4,5,6,10; there is no element of order 15
#      (so the odd-order subgroups are only 1, Z3, Z5)
#   4. every order-4 element squares to -1, so every Z4 < 2I contains the centre
#
# Quaternions are stored as 4-tuples rounded to R decimals. Entry gaps in 2I are
# about 0.19, far above the rounding, so the keys are exact identifiers; powers snap
# to the canonical key at every step so float error cannot accumulate.

from math import sqrt

PHI = (1 + sqrt(5)) / 2
R = 7


def key(q):
    return tuple(round(x, R) + 0.0 for x in q)


def mul(a, b):
    a1, a2, a3, a4 = a
    b1, b2, b3, b4 = b
    return (
        a1*b1 - a2*b2 - a3*b3 - a4*b4,
        a1*b2 + a2*b1 + a3*b4 - a4*b3,
        a1*b3 - a2*b4 + a3*b1 + a4*b2,
        a1*b4 + a2*b3 - a3*b2 + a4*b1,
    )


def neg(q):
    return tuple(-x for x in q)


def inv(q):  # unit quaternion
    return (q[0], -q[1], -q[2], -q[3])


# ---- build 2I ----
raw_gens = [(0.0, 1.0, 0.0, 0.0),                        # i
            (PHI/2, 1.0/(2*PHI), 0.5, 0.0)]              # golden icosian
for g in raw_gens:
    assert abs(sum(x*x for x in g) - 1) < 1e-12, f"generator not a unit quaternion: {g}"
gens = [key(g) for g in raw_gens]

G = set(gens) | {key((1.0, 0.0, 0.0, 0.0))}
while True:
    new = {key(mul(a, b)) for a in G for b in gens}
    if new <= G:
        break
    G |= new
G = sorted(G)

assert len(G) == 120, f"closure is not order 120: {len(G)}"
Gset = set(G)
for a in G:
    for b in G:
        assert key(mul(a, b)) in Gset, "closure is not a group"

ONE = key((1.0, 0.0, 0.0, 0.0))
MINUS_ONE = key((-1.0, 0.0, 0.0, 0.0))
assert MINUS_ONE in Gset


def order(g):
    n, x = 1, key(g)
    while x != ONE:
        x = key(mul(x, g))   # snap to canonical key: no drift over long orbits
        n += 1
        assert n <= 120, f"order loop failed to close for {g}"
    return n


# ---- conjugacy classes ----
classes, unassigned = [], set(G)
while unassigned:
    g = next(iter(unassigned))
    orb = {key(mul(mul(h, g), inv(h))) for h in G}
    classes.append(orb)
    unassigned -= orb
classes.sort(key=lambda c: (len(c), order(next(iter(c)))))

assert len(classes) == 9, f"expected 9 conjugacy classes, got {len(classes)}"
assert sorted(len(c) for c in classes) == [1, 1, 12, 12, 12, 12, 20, 20, 30]

print("2I built and verified: order 120, 9 conjugacy classes")
print()
print(f"{'size':>5}  {'order':>5}  {'trace':>9}   negation-closed")
print("-" * 46)
for c in classes:
    rep = next(iter(c))
    print(f"{len(c):>5}  {order(rep):>5}  {2*rep[0]:>9.5f}   {key(neg(rep)) in c}")
print()

# ---- fact 1: unique negation-closed class ----
closed = [(len(c), order(next(iter(c)))) for c in classes if key(neg(next(iter(c)))) in c]
assert closed == [(30, 4)], f"expected only the size-30 order-4 class, got {closed}"
print(f"FACT 1  unique negation-closed class (size, order) = {closed[0]}")

# ---- fact 1b: the rest pair up ----
swapped = sum(1 for c in classes if key(neg(next(iter(c)))) not in c)
assert swapped == 8 and swapped // 2 == 4
print(f"FACT 1b {swapped} classes swapped in {swapped//2} pairs, plus 1 fixed = {swapped+1}")

# ---- fact 2: unique involution ----
involutions = [g for g in G if order(g) == 2]
assert involutions == [MINUS_ONE], f"expected only -1, got {involutions}"
print("FACT 2  exactly one element of order 2, and it is the central -1")

# ---- fact 3: element orders ----
orders = sorted({order(g) for g in G})
assert orders == [1, 2, 3, 4, 5, 6, 10], orders
assert 15 not in orders
odd = sorted(o for o in orders if o % 2 == 1)
assert odd == [1, 3, 5]
print(f"FACT 3  element orders {orders}; odd cyclic subgroup orders {odd}")

# ---- fact 4: order-4 elements square to the centre ----
assert all(key(mul(g, g)) == MINUS_ONE for g in G if order(g) == 4)
print("FACT 4  every order-4 element squares to -1, so every Z4 < 2I contains the centre")

# ---- fact 5: subgroup-circle stabilizers H = 2I cap C ----
# For a one-parameter-subgroup circle C = {exp(tZ)}, left translation gives
# gamma.C = C iff gamma in C, so H = 2I cap C. Each non-central element lies on
# the unique such circle through its rotation axis (taken up to sign).
from collections import defaultdict


def axis(q):
    v = q[1:]
    n = sum(x*x for x in v) ** 0.5
    u = tuple(x/n for x in v)
    if u < tuple(-x for x in u):       # canonical representative of +-u
        u = tuple(-x for x in u)
    return tuple(round(x, 6) + 0.0 for x in u)


by_axis = defaultdict(list)
for g in G:
    if g not in (ONE, MINUS_ONE):
        by_axis[axis(g)].append(g)

# circle through an occupied axis holds its elements plus +-1
h_orders = defaultdict(int)
for els in by_axis.values():
    h_orders[len(els) + 2] += 1

assert dict(h_orders) == {4: 15, 6: 10, 10: 6}, dict(h_orders)
assert sum(h_orders.values()) == 31
assert sum((k - 2) * v for k, v in h_orders.items()) + 2 == 120
print(f"FACT 5  occupied axes: C4 on {h_orders[4]}, C6 on {h_orders[6]}, "
      f"C10 on {h_orders[10]}; {sum(h_orders.values())} special axes total,")
print("        every other axis gives H = {+-1}, so a generic boundary excludes over-collapse")

print()
print("ALL CHECKS PASSED")
