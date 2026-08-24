#!/usr/bin/env python3
"""
validate_flashcards.py - Verify the Anki flashcards CSV is well-formed.

Expected format (from anki_import_guide.md):
- 4 columns separated by tab (or comma in raw CSV)
- Header row: question<TAB>answer<TAB>tag<TAB>extra
- Each subsequent row: 4 fields, no embedded tabs in fields

Tolerates bilingual duplicates (e.g., same question in EN and ES — common in
multilingual study decks like this one for PY/Spanish-speaking learners).
A "duplicate" only counts as an issue if both rows have the same question
AND the same answer AND the same LO tag.

Exit code: 0 if clean, 1 otherwise.
"""

from __future__ import annotations
import csv
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CSV_PATH = ROOT / '04_flashcards' / 'flashcards_v4.0.1.csv'

EXPECTED_FIELDS = 4
EXPECTED_MIN_CARDS = 50  # Per deck README, should have 85


def normalize(s: str) -> str:
    """Strip accents + lowercase for comparison."""
    nfkd = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower().strip()


def main() -> int:
    if not CSV_PATH.exists():
        print(f"✗ Flashcard CSV not found: {CSV_PATH}")
        return 1

    with open(CSV_PATH, encoding='utf-8', errors='ignore') as f:
        sample = f.read(2048)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters='\t,')
        except csv.Error:
            print(f"✗ Could not detect delimiter in {CSV_PATH.name}")
            return 1
        reader = csv.reader(f, dialect=dialect)
        rows = list(reader)

    issues = []
    if not rows:
        print(f"✗ Empty CSV: {CSV_PATH}")
        return 1

    header = rows[0]
    body = rows[1:]

    if len(header) != EXPECTED_FIELDS:
        issues.append(f"Header has {len(header)} fields, expected {EXPECTED_FIELDS}: {header}")

    if len(body) < EXPECTED_MIN_CARDS:
        issues.append(f"Only {len(body)} card rows; expected at least {EXPECTED_MIN_CARDS}")

    malformed = []
    for i, row in enumerate(body, start=2):
        if len(row) != EXPECTED_FIELDS:
            malformed.append((i, len(row), row))

    if malformed:
        issues.append(f"{len(malformed)} rows have wrong field count (expected {EXPECTED_FIELDS}):")
        for i, n, row in malformed[:10]:
            issues.append(f"  row {i}: {n} fields — {row[:80]}...")
        if len(malformed) > 10:
            issues.append(f"  ... and {len(malformed) - 10} more")

    empty_q = sum(1 for r in body if not (r[0] or '').strip())
    if empty_q:
        issues.append(f"{empty_q} cards have empty 'question' field")

    empty_a = sum(1 for r in body if not (r[1] or '').strip())
    if empty_a:
        issues.append(f"{empty_a} cards have empty 'answer' field")

    # True duplicates: same normalized question AND same normalized answer AND same tag
    triples = {}
    for r in body:
        q = normalize(r[0] if len(r) > 0 else '')
        a = normalize(r[1] if len(r) > 1 else '')
        t = (r[3] if len(r) > 3 else '').strip()
        key = (q, a, t)
        triples.setdefault(key, []).append(r)

    true_dups = {k: v for k, v in triples.items() if len(v) > 1}
    if true_dups:
        issues.append(f"{len(true_dups)} exact duplicate card(s) (same question + answer + tag):")
        for (q, a, t), rows in list(true_dups.items())[:5]:
            issues.append(f"  ({len(rows)}x) Q: {q[:60]}... / Tag: {t}")

    # Bilingual duplicates (informational): same normalized question, different answer language
    by_q = {}
    for r in body:
        q = normalize(r[0] if len(r) > 0 else '')
        by_q.setdefault(q, []).append(r)

    bilingual = [(q, rows) for q, rows in by_q.items() if len(rows) > 1 and (q, normalize(rows[0][1]), rows[0][3] if len(rows[0]) > 3 else '') not in true_dups]
    bilingual_note = ""
    if bilingual:
        bilingual_note = f"  ({len(bilingual)} bilingual pair(s) — same question in EN/ES, treated as intentional)"

    print(f"Validated {len(body)} cards in {CSV_PATH.name} ({len(header)} header fields, delimiter={repr(dialect.delimiter)})")
    if bilingual_note:
        print(bilingual_note)

    if issues:
        print("\n✗ Issues found:\n")
        for issue in issues:
            print(f"  {issue}")
        return 1

    print("✓ Flashcards CSV is well-formed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
