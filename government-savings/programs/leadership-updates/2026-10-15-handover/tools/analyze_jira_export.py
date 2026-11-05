#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

p = Path(r"C:\Users\swpatil\Downloads\Sprint 15, 16, 17 - JIRA.csv")
rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))
print("Total issues:", len(rows))

def sprint_label(r):
    for v in r.values():
        if not v:
            continue
        if "26.15" in v and "Sprint" in v:
            return "26.15"
        if "26.16" in v and "Sprint" in v:
            return "26.16"
        if "26.17" in v and ("Sprint" in v or "AMSQAD" in v):
            return "26.17"
    sv = r.get("Custom field (Sprint Velocity)", "") or ""
    if "26.15" in sv:
        return "26.15"
    if "26.16" in sv:
        return "26.16"
    if "26.17" in sv:
        return "26.17"
    return "?"

by_sprint = defaultdict(list)
by_assignee = defaultdict(lambda: {"done": 0, "active": 0, "sp": 0.0})
by_area = defaultdict(int)

for r in rows:
    sp = sprint_label(r)
    by_sprint[sp].append(r)
    a = r.get("Assignee", "Unassigned") or "Unassigned"
    st = r.get("Status", "")
    try:
        sp_pts = float(r.get("Custom field (Story Points)", "") or 0)
    except ValueError:
        sp_pts = 0
    if st in ("Done", "Closed", "Resolved"):
        by_assignee[a]["done"] += 1
        by_assignee[a]["sp"] += sp_pts
    else:
        by_assignee[a]["active"] += 1
    summ = (r.get("Summary") or "").upper()
    if "MSC" in summ or "MOBILE" in summ or "ENROLL" in summ:
        by_area["MSC/API"] += 1
    elif "PERF" in summ or "JMETER" in summ or "TAURUS" in summ:
        by_area["Perf"] += 1
    elif "[V2]" in summ or "V2 " in summ:
        by_area["V2"] += 1
    elif "[V3]" in summ or "V3 " in summ or "UNITE" in summ or "UNIVERSAL" in summ:
        by_area["V3/UE"] += 1
    else:
        by_area["Other/Platform"] += 1

print("\n=== By sprint ===")
for sp in ("26.15", "26.16", "26.17", "?"):
    if sp not in by_sprint:
        continue
    items = by_sprint[sp]
    done = sum(1 for i in items if i.get("Status") in ("Done", "Closed", "Resolved"))
    print(f"  Sprint {sp}: {len(items)} issues · {done} Done/Closed")

print("\n=== By assignee (team) ===")
for a in sorted(by_assignee, key=lambda x: -by_assignee[x]["done"]):
    d = by_assignee[a]
    if d["done"] + d["active"] < 1:
        continue
    print(f"  {a}: {d['done']} done, {d['active']} open · {d['sp']:.0f} SP (done items)")

print("\n=== Theme (rough) ===")
for k, v in sorted(by_area.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

print("\n=== Open / in progress ===")
for r in rows:
    if r.get("Status") not in ("Done", "Closed", "Resolved"):
        print(f"  {r.get('Status')} | {r.get('Issue key')} | {r.get('Assignee')} | {(r.get('Summary') or '')[:65]}")
