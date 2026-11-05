#!/usr/bin/env python3
"""Count MSC regression suite methods x plans; print Stage5 remainder."""
import re
from pathlib import Path

api = Path(r"C:\Workspace\GitLab\api-test-automation")


def parse_suite(xml_path):
    text = Path(xml_path).read_text(encoding="utf-8")
    plans = len(re.findall(r"<test name=", text))
    classes = re.findall(r'<class name="([^"]+)"/>', text)
    seen = set()
    first = []
    for c in classes:
        if c in seen:
            break
        seen.add(c)
        first.append(c)
    return first, plans


def resolve_java(module_root, classname):
    simple = classname.split(".")[-1] + ".java"
    hits = list(Path(module_root).rglob(simple))
    return hits[0] if hits else None


def count_methods(java_path):
    text = java_path.read_text(encoding="utf-8", errors="ignore")
    return re.findall(
        r"@Test(?:\s*\([^)]*\))?\s*(?:\r?\n\s*)*(?:public|protected)\s+void\s+(\w+)",
        text,
    )


for label, xml, mod in [
    ("M1-reg", api / "mobile/mobile1/testsuites/mobile1-regression-testng.xml", api / "mobile/mobile1"),
    ("M2-reg", api / "mobile/mobile2/testsuites/mobile2-regression-testng.xml", api / "mobile/mobile2"),
    ("ENR-reg", api / "mobile/enrollment/testsuites/enrollment-regression-testng.xml", api / "mobile/enrollment"),
]:
    classes, plans = parse_suite(xml)
    total = 0
    print(f"=== {label}: {plans} plans, {len(classes)} classes ===")
    for c in classes:
        jp = resolve_java(mod, c)
        if not jp:
            print("  MISSING", c)
            continue
        meths = count_methods(jp)
        print(f"  {len(meths):2d}  {c}")
        total += len(meths)
    print(f"  PER PLAN: {total}  x{plans} = {total * plans}\n")

# all @Test inventory
for module in ["mobile1", "mobile2", "enrollment"]:
    total = 0
    for p in (api / "mobile" / module / "src" / "test").rglob("*Test*.java"):
        if "pojo" in str(p).lower():
            continue
        if p.name.endswith("BaseTest.java"):
            continue
        total += len(count_methods(p))
    print(f"ALL @Test in {module}: {total} (x3 plans = {total * 3})")
