#!/usr/bin/env python3
"""
check_links.py - Verify every internal link in every .md file resolves.

This repo uses a CONVENTION: paths inside markdown links/backticks are written
relative to the REPO ROOT, not relative to the source file. This deviates from
GitHub's default markdown rendering, but it's the established pattern here.

Resolution strategy (in order):
1. Treat the path as ROOT-RELATIVE (the convention in this repo)
2. If that fails, try resolving relative to the source file's directory

Skips:
- External URLs (http://, https://)
- Anchors (#section)
- Glob patterns (sample_exam_*.md)
- Links inside 18_audit/ (historical record of issues, may reference removed paths)
- Empty targets

Exit code: 0 if clean, 1 if any broken link found.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent

LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
BACKTICK_PATH = re.compile(r'`([^`]*\.(?:md|csv))`')
GLOB_PATTERN = re.compile(r'[*?\[]')

# Directories whose content references intentionally-broken paths
# (audit docs documenting historical issues, starter packs with relative paths,
#  cross-system files like the WA groups referencing external CRM)
SKIP_DIRS = {'18_audit', '.git', '.github'}
SKIP_FILES = {
    '20_starter_pack_luana/01_intro/LUANA_INTRO.md',  # uses relative paths like 02_study_plan/...
    '20_starter_pack_luana/02_study_plan/PLAN_PARA_LUANA.md',
    '20_starter_pack_luana/03_skill_bridge/SKILLS_TRANSFER.md',
    '20_starter_pack_luana/04_practice_exercises/EJERCICIOS_TRILINGUES.md',
    '20_starter_pack_luana/05_career_paths/CARRERA_QA_PARA_LUANA.md',
    '20_starter_pack_luana/README.md',
    '19_starter_pack_belen/02_study_plan/ISTQB_PLAN_FOR_YOU.md',
    '19_starter_pack_belen/03_jobs_and_ai/GETTING_QA_JOBS.md',
    '19_starter_pack_belen/04_salary_and_remote/WHAT_SHE_CAN_EARN.md',
    '07_resources/istqb_py_grupos_wa.md',  # references CRM files outside repo
    'CONTRIBUTING.md',  # references GitHub templates directory (issue templates)
    '14_external_repos/README.md',  # references external repo files
}


def is_skipped(rel: str) -> bool:
    if any(part in SKIP_DIRS for part in Path(rel).parts):
        return True
    return rel in SKIP_FILES


def collect_links() -> list[tuple[str, str, str]]:
    findings = []
    for md in sorted(ROOT.rglob('*.md')):
        rel = str(md.relative_to(ROOT))
        if is_skipped(rel):
            continue
        text = md.read_text(encoding='utf-8', errors='ignore')
        for m in LINK_PATTERN.finditer(text):
            target = m.group(2)
            if target.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            clean = target.split('#')[0]
            if not clean or GLOB_PATTERN.search(clean):
                continue
            findings.append((str(rel), clean, 'link'))
        for m in BACKTICK_PATH.finditer(text):
            target = m.group(1)
            if target.startswith(('http://', 'https://')):
                continue
            if GLOB_PATTERN.search(target):
                continue
            findings.append((str(rel), target, 'backtick'))
    return findings


def resolve(src: str, target: str) -> str | None:
    """Try multiple resolution strategies; return path if found, else None."""
    src_path = ROOT / src

    # Strategy 1: root-relative (repo convention)
    candidate = (ROOT / target).resolve()
    if candidate.exists():
        return str(candidate.relative_to(ROOT))

    # Strategy 2: file-relative (GitHub default)
    candidate = (src_path.parent / target).resolve()
    if candidate.exists():
        return str(candidate.relative_to(ROOT))

    return None


def main() -> int:
    findings = collect_links()
    broken = []
    grouped: dict[str, list[tuple[str, str]]] = defaultdict(list)
    resolved_count = 0

    for src, target, kind in findings:
        if resolve(src, target) is not None:
            resolved_count += 1
        else:
            broken.append((src, target, kind))
            grouped[src].append((target, kind))

    total = len(findings)
    print(f"Checked {total} internal references ({resolved_count} resolved, {len(broken)} broken).")

    if not broken:
        print("✓ All internal links resolve.")
        return 0

    print(f"\n✗ {len(broken)} broken references in {len(grouped)} files:\n")
    for src in sorted(grouped):
        print(f"  {src}")
        for target, kind in grouped[src]:
            print(f"    [{kind}] -> {target}")
        print()
    return 1


if __name__ == '__main__':
    sys.exit(main())
