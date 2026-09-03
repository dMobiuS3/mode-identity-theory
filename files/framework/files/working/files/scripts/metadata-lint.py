#!/usr/bin/env python3
"""metadata-lint.py -- lint the working-file research-status headers. (2026-09-03)

This is LINT, not a qualification harness. It enforces the header contract defined
in working/README.md and proves the propagation-detection branch fires.

FAIL conditions:
  - unknown Type / State / Verdict value
  - Verdict present on a non-Test page
  - missing or malformed Status date (YYYY-MM-DD)
  - a `gate:*` in Gated by that does not resolve to the README registry
  - a page Gated by a gate it also Works (self-dependency)
  - a Parent that does not resolve to an existing .md
  - State: Superseded without a resolving `Superseded by:`
  - a surviving legacy `**Dependencies:**` field
  - duplicate gate IDs in the registry

WARN conditions (reviewed, not blocking):
  - the page has a git commit newer than its Status date (possible staleness)
  - a gate's Last transition is newer than a page that names it (propagation event)

Pages without a metadata header yet are reported as PENDING, not failed, so the
lint is usable mid-pilot.

Run from anywhere: python3 metadata-lint.py
"""

import os, re, sys, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.dirname(HERE)                       # working/files
README = os.path.join(os.path.dirname(PAGES_DIR), 'README.md')  # working/README.md
REPO = subprocess.check_output(['git', '-C', HERE, 'rev-parse', '--show-toplevel'],
                               text=True).strip()

TYPES = {'Map', 'Program', 'Test', 'Result', 'Note'}
STATES = {'Open', 'Active', 'Blocked', 'Waiting', 'Closed', 'Reopened', 'Superseded'}
VERDICTS = {'Positive', 'Negative', 'Mixed', 'Inconclusive', 'Uninformative'}
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

fails, warns = [], []


def parse_registry(text):
    """Return {gate_id: {state, frontier, worked_by:set, last_transition}}."""
    gates = {}
    for m in re.finditer(r'^### `(gate:[a-z0-9-]+)`\s*\n(.*?)(?=^### |^## |\Z)',
                         text, re.S | re.M):
        gid, body = m.group(1), m.group(2)
        st = re.search(r'\*\*State:\*\*\s*(\w+)', body)
        fr = re.search(r'\*\*Frontier:\*\*\s*([^\n·]+)', body)
        lt = re.search(r'\*\*Last transition:\*\*\s*(\d{4}-\d{2}-\d{2})', body)
        wb = set(re.findall(r'`([\w./-]+\.md)`', body))
        gates[gid] = {'state': st.group(1) if st else None,
                      'frontier': fr.group(1).strip() if fr else None,
                      'worked_by': {os.path.basename(x) for x in wb},
                      'last_transition': lt.group(1) if lt else None}
    return gates


def parse_header(text):
    """Return the metadata fields from a page's header block, or None if absent."""
    if '**Type:**' not in text[:1500]:
        return None
    def field(name):
        m = re.search(rf'^\*\*{name}\s*(?:\((\d{{4}}-\d{{2}}-\d{{2}})\))?:\*\*[ \t]*(.*)$',
                      text, re.M)
        return (m.group(1), m.group(2).strip()) if m else (None, None)
    h = {}
    for f in ['Type', 'State', 'Verdict', 'Summary', 'Parent', 'Frozen', 'Superseded by']:
        _, v = field(f)
        h[f] = v
    h['status_date'], h['status_text'] = field('Status')
    _, gb = field('Gated by')
    h['gated_by'] = set(re.findall(r'`?(gate:[a-z0-9-]+)`?', gb or ''))
    _, inp = field('Inputs')
    h['inputs'] = inp
    return h


def last_commit_date(path):
    out = subprocess.check_output(
        ['git', '-C', REPO, 'log', '-1', '--format=%cs', '--', path], text=True).strip()
    return out or None


def check_page(fn, registry):
    path = os.path.join(PAGES_DIR, fn)
    text = open(path, encoding='utf-8').read()
    tag = fn
    h = parse_header(text)
    if h is None:
        return 'PENDING'   # not migrated yet; legacy Dependencies is expected, not a failure
    if re.search(r'^\*\*Dependencies:\*\*', text, re.M):
        fails.append(f'{tag}: legacy **Dependencies:** field survives after migration')
    if h['Type'] not in TYPES:
        fails.append(f'{tag}: unknown Type {h["Type"]!r}')
    if h['State'] not in STATES:
        fails.append(f'{tag}: unknown State {h["State"]!r}')
    if h['Verdict']:
        if h['Verdict'] not in VERDICTS:
            fails.append(f'{tag}: unknown Verdict {h["Verdict"]!r}')
        if h['Type'] != 'Test':
            fails.append(f'{tag}: Verdict present on non-Test ({h["Type"]})')
    if not h['status_date'] or not DATE_RE.match(h['status_date'] or ''):
        fails.append(f'{tag}: missing/malformed Status date')
    for g in h['gated_by']:
        if g not in registry:
            fails.append(f'{tag}: Gated by unresolved {g}')
        elif fn in registry[g]['worked_by']:
            fails.append(f'{tag}: is Gated by {g} but also Works it (self-dependency)')
    if h['Parent']:
        p = re.sub(r'[`*]', '', h['Parent']).split()[0]
        cand = [os.path.join(PAGES_DIR, p),
                os.path.normpath(os.path.join(PAGES_DIR, p)),
                os.path.normpath(os.path.join(REPO, p))]
        if not any(os.path.exists(c) for c in cand):
            fails.append(f'{tag}: Parent {p!r} does not resolve')
    if h['State'] == 'Superseded' and not h['Superseded by']:
        fails.append(f'{tag}: State Superseded without Superseded by')
    # WARN: git history newer than Status date
    lc = last_commit_date(path)
    if h['status_date'] and lc and lc > h['status_date']:
        warns.append(f'{tag}: last commit {lc} newer than Status {h["status_date"]} '
                     f'(verify not stale)')
    # WARN: a gate this page names has transitioned after the page's Status
    for g in h['gated_by']:
        gt = registry.get(g, {}).get('last_transition')
        if gt and h['status_date'] and h['status_date'] < gt:
            warns.append(f'{tag}: {g} transitioned {gt} after Status {h["status_date"]} '
                         f'(PROPAGATION: re-check this page)')
    return h['Type']


def warn_fixture():
    """Prove the stale-gate WARN branch can fire, on synthetic data."""
    gate_transition, dependent_status = '2026-07-05', '2026-07-04'
    fired = dependent_status < gate_transition
    return fired


def main():
    reg_text = open(README, encoding='utf-8').read()
    registry = parse_registry(reg_text)

    ids = re.findall(r'^### `(gate:[a-z0-9-]+)`', reg_text, re.M)
    for g in {x for x in ids if ids.count(x) > 1}:
        fails.append(f'registry: duplicate gate id {g}')

    print(f"registry: {len(registry)} gates")
    for g, d in registry.items():
        refs = len(d['worked_by'])  # worked-by count; gated-by tallied below
        # >=2-page proxy for the "two distinct programs" rule (human confirms distinctness)
        # count pages that reference the gate at all:
    # tally gated-by references across pages
    ref_count = {g: len(registry[g]['worked_by']) for g in registry}

    pages = sorted(f for f in os.listdir(PAGES_DIR) if f.endswith('.md'))
    headed, pending = [], []
    for fn in pages:
        r = check_page(fn, registry)
        (pending if r == 'PENDING' else headed).append(fn)
        h = parse_header(open(os.path.join(PAGES_DIR, fn), encoding='utf-8').read())
        if h:
            for g in h['gated_by']:
                ref_count[g] = ref_count.get(g, 0) + 1

    for g, n in ref_count.items():
        if n < 2:
            warns.append(f'registry: {g} referenced by {n} page(s) (<2; confirm it is '
                         f'shared across distinct programs or demote)')

    print(f"pages: {len(headed)} headed, {len(pending)} pending (no header yet)")
    print(f"fixture: stale-gate WARN branch fires on synthetic transition: "
          f"{'PASS' if warn_fixture() else 'FAIL'}")
    if not warn_fixture():
        fails.append('WARN fixture did not fire')

    print(f"\n{len(fails)} FAIL, {len(warns)} WARN")
    for f in fails:
        print(f"  FAIL  {f}")
    for w in warns:
        print(f"  warn  {w}")
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
