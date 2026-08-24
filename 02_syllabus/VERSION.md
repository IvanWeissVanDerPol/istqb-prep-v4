# 📌 Syllabus Version

> **Current version:** **ISTQB CTFL v4.0.1**
> **Release date:** 15 September 2024
> **Official PDF:** https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/
> **Pages:** 78

---

## Why this file exists

This directory used to be named `02_syllabus_v4_0_1/` — version baked into the folder name. That was a bad pattern because:

1. **Renames create churn.** Every syllabus version bump would require a directory rename + every internal link rewrite.
2. **The version is content, not structure.** It belongs in a file, not a folder name.

So in Aug 2026 we renamed the directory to `02_syllabus/` and put the version here. When ISTQB publishes v4.1 or v5.0, we add a `CHANGELOG.md` in this folder with the diff. No directory rename required.

---

## 📚 Files in this folder

| File | Purpose |
|------|---------|
| `README.md` | Structure of the official syllabus (6 chapters, ~1135 min) |
| `MAPA_COMPLETO_OBJETIVOS.md` | Checklist of all 64 Learning Objectives with K-levels |

---

## 🔄 Versioning policy

- **Patch versions (v4.0.1 → v4.0.2):** Generally just typo corrections in official syllabus. No action needed unless they touch a LO we cover.
- **Minor versions (v4.0 → v4.1):** Updated syllabus. Update `VERSION.md`, `README.md`, add a changelog note in the repo root `CHANGELOG.md`, and re-validate all 64 LO mappings.
- **Major versions (v4.x → v5.0):** Structural changes (chapter renames, new chapters, LO changes). Likely requires re-validating the entire repo.

---

*Last reviewed: August 2026 — coincides with directory rename from `02_syllabus_v4_0_1/` to `02_syllabus/`.*
