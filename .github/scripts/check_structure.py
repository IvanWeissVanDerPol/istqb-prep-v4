#!/usr/bin/env python3
"""
check_structure.py - Verify the repo's numbered-directory structure is sane.

Checks:
1. Top-level directories are numbered consistently (NN_name format)
2. No orphaned numbered gaps that aren't documented (current gap: 16 = consolidated into 08)
3. Required files exist: README.md, INDEX.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md
4. Each numbered directory has either a README.md or matches a documented exception

Exit code: 0 if clean, 1 otherwise.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

REQUIRED_FILES = {
    'README.md', 'INDEX.md', 'LICENSE', 'CHANGELOG.md',
    'CONTRIBUTING.md', 'CONTRIBUTORS.md', 'CODE_OF_CONDUCT.md',
}

# Documented gaps in numbering (number -> reason)
DOCUMENTED_GAPS = {
    16: 'Consolidated into 08_quick_refs/cheatsheets/15_printable_cheatsheets.md (Aug 2026)',
}

# Directories that don't require README.md because their contents are self-explanatory
# or because the parent INDEX.md describes them adequately
ALLOW_NO_README = {
    '01_plan_estudio',         # 1 file, named 00_vision_general.md (clear)
    '03_glosario',             # 1 file, named GLOSARIO_v4.0.1.md (clear)
    '05_summaries',            # 6 files, cap_NN_*.md (clear naming)
    '06_practice_tests',       # 12 files in subfolder, named clearly
    '07_resources',            # 4 files, named clearly
    '08_quick_refs',           # 7 files + subfolder, named clearly
    '13_v4_changes',           # 1 file, named clearly
    '18_audit',                # internal audit doc, not user-facing
}


def main() -> int:
    issues = []

    # Check required root files
    for required in REQUIRED_FILES:
        if not (ROOT / required).exists():
            issues.append(f"Missing required file: {required}")

    # Scan numbered directories
    numbered = []
    unnumbered_dirs = []
    for entry in sorted(ROOT.iterdir()):
        if entry.name.startswith('.'):
            continue
        if not entry.is_dir():
            continue
        if re.match(r'^\d{2}_', entry.name):
            num = int(entry.name.split('_')[0])
            numbered.append((num, entry.name))
        else:
            unnumbered_dirs.append(entry.name)

    if not numbered:
        issues.append("No numbered directories found at root")

    # Check for undocumented gaps
    if numbered:
        nums = sorted(n for n, _ in numbered)
        for n in range(min(nums), max(nums) + 1):
            if n not in nums:
                if n not in DOCUMENTED_GAPS:
                    issues.append(f"Undocumented numbering gap at {n:02d}")
                # Documented gaps are fine — they print as info

    # Check each numbered dir has either README.md or is in allow list
    for num, name in numbered:
        d = ROOT / name
        if not (d / 'README.md').exists():
            # Allow if it has another obvious index file
            has_index = any((d / f).exists() for f in ['00_PROGRESS.md', 'VERSION.md', 'README.md', 'INDEX.md'])
            if not has_index and name not in ALLOW_NO_README:
                issues.append(f"Directory {name}/ has no README.md or index file")

    # Report
    print(f"Found {len(numbered)} numbered directories, {len(unnumbered_dirs)} unnumbered top-level dirs.")
    for num, name in sorted(numbered):
        marker = "⚠" if name not in [n for _, n in numbered] else "✓"
        print(f"  {marker} {name}")

    if unnumbered_dirs:
        print(f"\nUnnumbered directories:")
        for d in unnumbered_dirs:
            print(f"  - {d}")

    if DOCUMENTED_GAPS:
        print(f"\nDocumented gaps:")
        for n, reason in sorted(DOCUMENTED_GAPS.items()):
            print(f"  - {n:02d}: {reason}")

    if issues:
        print(f"\n✗ {len(issues)} issues found:\n")
        for issue in issues:
            print(f"  {issue}")
        return 1

    print("\n✓ Repo structure is healthy.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
