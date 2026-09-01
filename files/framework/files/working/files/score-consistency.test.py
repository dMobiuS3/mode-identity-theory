#!/usr/bin/env python3
"""
score-consistency.test.py -- regression test for the public Score tables. (2026-09-01)

The root README's Score is an aggregate of the two section landings: every row on
cosmos/README or spectrum/README also appears on the root. That duplication is
deliberate (the front door needs its number column, the landings need theirs), so
this test does not remove it; it makes a disagreement fail loudly instead of waiting
to be noticed.

What this buys, stated honestly: a cell like the KATRIN limit still lives twice, in
spectrum and in root. What changes is that a divergence becomes a failing assertion
rather than a discovery. On 2026-09-01 three cells had drifted between a landing and
the root (the alpha-route Lambda, the color-channel wording, and a superseded KATRIN
limit) and sat wrong until someone thought to compare by eye. If this test starts
failing often, that is the evidence that generating the root Score from the two
section tables has become worth the build step.

Scope: internal propagation only. It does NOT check whether a value is scientifically
current -- that is a data-maintenance question and mixing it in would turn a
deterministic repo test into a monitor.

Convention: run after any edit to the root, cosmos, or spectrum Score tables.
Run:  python3 score-consistency.test.py     (stdlib only; exit 1 on drift)
"""
import os, re, sys

# The Euclid card is a deposited pre-registration with its own header
# ("| Prediction | Value | Euclid DR1 channel | Falsified if |"). It is excluded by
# construction here rather than by luck: it must never be asserted against a landing.
SCORE_HEADER = "| Observable | Output | Observed | Agreement |"

LANDINGS = {"cosmos": "files/cosmos/README.md", "spectrum": "files/spectrum/README.md"}
ROOT = "README.md"


def repo_root():
    """Walk upward from this file until all three Score-bearing pages exist."""
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if all(os.path.exists(os.path.join(d, p)) for p in [ROOT, *LANDINGS.values()]):
            return d
        d = os.path.dirname(d)
    sys.exit("could not locate the repository root from this file's position")


def canonical(target, page):
    """Resolve a link target to a repo-relative path so root's '/files/x/y.md' and a
    landing's 'files/y.md' or '../spectrum/z.md' compare equal."""
    path, _, anchor = target.partition("#")
    path = path.lstrip("/") if target.startswith("/") else os.path.join(os.path.dirname(page), path)
    return os.path.normpath(path) + ("#" + anchor if anchor else "")


def score_rows(root, page):
    """Return {identity: (label, [data cells])} for the page's Score table only."""
    rows, inside = {}, False
    for line in open(os.path.join(root, page), encoding="utf-8").read().split("\n"):
        if line.strip() == SCORE_HEADER:
            inside = True
            continue
        if inside:
            if not line.startswith("|"):
                break
            # Separator detection must be structural: a line whose cells are ALL
            # dashes. A substring test for "---" would silently drop the w_eff row,
            # whose anchor slugifies "> -1" into a literal "---", and a row the parser
            # never sees is a row the test never checks.
            if set(line.strip()) <= set("|-: "):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            m = re.search(r"\[↗\]\(([^)]+)\)", cells[0])
            label = re.sub(r"\[↗\]\([^)]*\)", "", cells[0]).strip()
            # Identity is the link target PLUS the visible label. Target alone is not
            # unique: several rows share one anchor (#iii-the-24-entries carries four),
            # and keying on it silently collapses them, so rows would drop out of the
            # comparison and the test would pass by ignoring them. A label rename then
            # breaks identity, which surfaces as a presence WARNING for a human to
            # adjudicate rather than a false drift failure.
            ident = (canonical(m.group(1), page) if m else "", label)
            # Embedded link targets are resolved the same way row identity is: root
            # writes them absolute and the landings relative, which is notation rather
            # than drift. Everything else in the cell is compared literally.
            data = [re.sub(r"\]\(([^)]+)\)", lambda m: "](" + canonical(m.group(1), page) + ")", c)
                    for c in cells[1:]]
            rows[ident] = (label, data)
    return rows


def main():
    root = repo_root()
    r = score_rows(root, ROOT)
    locals_ = {k: score_rows(root, p) for k, p in LANDINGS.items()}
    c, s = locals_["cosmos"], locals_["spectrum"]
    hard, warn = [], []

    # 1. the landings partition: no row may be owned by two sections at once
    both = set(c) & set(s)
    if both:
        hard += [f"owned by BOTH landings: {b}" for b in sorted(both)]

    # 2. presence. Unmatched rows are a HARD failure by default, so that "every root
    #    row has an owner" is genuinely asserted and a deletion cannot slip through.
    #    The single exception is a demonstrable rename: exactly one unmatched row on
    #    each side sharing the same normalised link target, with only the visible label
    #    changed. That is downgraded to a warning, because renaming is legitimate
    #    maintenance and a checker that fails on it gets muted within a week. If the
    #    pairing is ambiguous, fail rather than guess.
    union = set(c) | set(s)
    only_local, only_root = sorted(union - set(r)), sorted(set(r) - union)
    for lk in list(only_local):
        cands = [rk for rk in only_root if rk[0] == lk[0]]
        peers = [x for x in only_local if x[0] == lk[0]]
        if len(cands) == 1 and len(peers) == 1:
            warn.append(f"probable rename on {lk[0]}: landing {lk[1]!r} vs root {cands[0][1]!r}")
            only_local.remove(lk); only_root.remove(cands[0])
    hard += [f"on a landing, absent from root (deletion or unpairable rename): {k}" for k in only_local]
    hard += [f"on root, no landing owns it (addition or unpairable rename):    {k}" for k in only_root]

    # 3. cell equality on every shared row. This is unambiguous drift, so it is hard.
    #    Nothing is normalised except surrounding whitespace: math wrappers, signs,
    #    units, status words and numeric formatting are exactly what we want to catch.
    for owner, rows in locals_.items():
        for ident, (label, cells) in rows.items():
            if ident not in r:
                continue
            rl, rc = r[ident]
            for i, (a, b) in enumerate(zip(rc, cells)):
                if a != b:
                    col = ["Output", "Observed", "Agreement"][i] if i < 3 else f"col{i}"
                    hard.append(f"{owner}: {label or rl}\n      [{col}]  root: {a}\n      "
                                f"{' ' * len(col)}   {owner}: {b}")

    for w in warn:
        print(f"  WARN  {w}")
    for h in hard:
        print(f"  FAIL  {h}")
    if hard:
        print(f"\nFAIL: {len(hard)} scorecard disagreement(s)")
        return 1
    print(f"PASS: root {len(r)} = cosmos {len(c)} + spectrum {len(s)}; "
          f"{len(set(r) & union)} shared rows match"
          + (f"; {len(warn)} warning(s) needing human adjudication" if warn else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
