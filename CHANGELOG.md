# Changelog

Todos los cambios notables a este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Pendiente
- Agregar issue templates y PR template
- Traducción a inglés y portugués
- Agregar LICENSE educativa explícita
- Crear CITATION.cff
- Crear `21_for_managers/` directory
- Crear `22_for_instructors/` directory

---

## [1.1.0] - 2026-08-24

### 🔧 Repo hygiene + structural improvements

**Resultado de auditoría 2026-08-24 que identificó issues estructurales y los resolvió.**

### Changed
- **Renamed `19_starter_pack_amiga/` → `19_starter_pack_belen/`** — el pack ahora lleva el nombre real de la persona para quien fue creado (Belen, amiga del maintainer, perfil animal caretaker / iPhone-first).
- **Renamed `02_syllabus_v4_0_1/` → `02_syllabus/`** — la versión v4.0.1 ahora vive en `02_syllabus/VERSION.md` (no en el path). Prepara el repo para futuras versiones sin tener que renombrar directorios.
- **Moved `00_README/00_PROGRESS.md` → `00_README/00_PROGRESS.md`** — el tracker personal ahora vive con el overview del repo. Agregado link en `00_README/README.md` para descubrimiento.
- **Replaced 8 broken references** to `16_cheat_sheets/` (directorio eliminado en v1.0.0) → ahora apuntan a `08_quick_refs/cheatsheets/15_printable_cheatsheets.md`.
- **Replaced 7 broken references** to `09_v4_changes/` (número equivocado) → ahora apuntan a `13_v4_changes/`.

### Added
- **`20_starter_pack_luana/`** — Nuevo starter pack personalizado para Luana Benitez (perfil trilingüe + intérprete + CM + Psicología). 6 archivos: intro, plan 8 semanas, skill bridge LO-por-LO, ejercicios trilingües EN/ES/PT, carrera QA por nicho. ~1500 líneas / 116 KB.
- **`CONTRIBUTORS.md`** — placeholder con los 3 contribuidores actuales (Ivan, Belen, Luana).
- **`.github/workflows/repo-hygiene.yml`** — CI workflow con 3 jobs:
  - `link-check`: verifica que cada internal link resuelva (script: `check_links.py`)
  - `flashcard-validate`: valida CSV de flashcards (script: `validate_flashcards.py`)
  - `structure-check`: valida estructura numerada de directorios (script: `check_structure.py`)
- **`.github/scripts/`** — 3 scripts Python auto-contenidos:
  - `check_links.py` (convención root-relative + fallback file-relative)
  - `validate_flashcards.py` (tolerante a duplicados bilingües EN/ES)
  - `check_structure.py` (gaps documentados: 16 = consolidado en 08)
- **`02_syllabus/VERSION.md`** — documenta la versión actual del syllabus y la política de versionado.
- **Nota en `INDEX.md`** aclarando que los packs 19 y 20 son deliberadamente divergentes (cada uno cubre un perfil distinto).

### Fixed
- **313 broken internal links detected and resolved** — todas las referencias internas ahora resuelven (205 verificadas con script final).
- **Link `08_quick_refs/cheatsheets/15_printable_cheatsheets.md`** (no existía) → `08_quick_refs/cheatsheets/15_printable_cheatsheets.md`.
- **Link `CHANGELOG.md`** (forward-looking fantasma) → referencia al `CHANGELOG.md` real.
- **Link relativo en `19_starter_pack_belen/01_what_is_qa/WHAT_QA_DOES.md`** → `19_starter_pack_belen/02_study_plan/ISTQB_PLAN_FOR_YOU.md`.
- **2 flashcards duplicates** (EN/ES bilingüe) ahora se reconocen como intencionales y el validador lo reporta informational-only.

### Verified
- ✓ 205/205 internal references resolve
- ✓ 151 flashcards, well-formed, 2 bilingual pairs noted
- ✓ 20 numbered directories, 0 undocumented gaps
- ✓ All 3 CI scripts pass locally

---

## [1.0.0] - 2025-08-05

### 🎉 Lanzamiento inicial

**Repo público creado:** `IvanWeissVanDerPol/istqb-prep-v4`

### Added
- README raíz con overview completo + quick start
- LICENSE MIT + notice sobre ISTQB
- Plan de estudio de 8 semanas (`01_plan_estudio/`)
- Estructura oficial del syllabus v4.0.1 (`02_syllabus/`)
- Glosario con 50+ términos v4.0.1 (`03_glosario/`)
- 85 flashcards Anki-importable CSV (`04_flashcards/`)
- 6 resúmenes de capítulos (`05_summaries/`)
- 6 quizzes por capítulo + 1 Hard Mode Quiz (`06_practice_tests/`)
- 3 sample exams A/B/C (`06_practice_tests/`)
- Sample Exam A — answer key agregado post-audit
- Resources Paraguay-specific (ASOLINFO + ISTQB PY grupos WA) (`07_resources/`)
- Cheatsheets 1-página por capítulo (`08_quick_refs/`)
- Career paths con salaries PY/LATAM/US (`09_career_paths/`)
- Exam failure analysis (`10_exam_difficulty/`)
- Full ISTQB certification catalog (`11_cert_paths/`)
- External resources curated (`12_external_resources/`)
- Cambios v3.1 → v4.0.1 (`13_v4_changes/`)
- 18+ GitHub repos curados (`14_external_repos/`)
- 60 preguntas de interview prep + STAR framework (`15_interview_prep/`)
- 15 cheat sheets printable (`08_quick_refs/cheatsheets/`)
- Study groups facilitation guide (`17_study_groups/`)
- Auditoría adversarial con 30+ roles (`18_audit/`)
- Progress tracker personal (`00_README/00_PROGRESS.md`)
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md

### Stats finales v1.0.0
- 51+ archivos markdown
- ~530KB contenido
- 19 directorios temáticos
- 200+ preguntas entre quizzes y sample exams
- 85 flashcards
- 60+ interview questions
- 18+ repos externos curados
- 15 cheat sheets
- 30+ roles auditados

---

## Cómo contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Links

- [Repo](https://github.com/IvanWeissVanDerPol/istqb-prep-v4)
- [Issues](https://github.com/IvanWeissVanDerPol/istqb-prep-v4/issues)
- [Releases](https://github.com/IvanWeissVanDerPol/istqb-prep-v4/releases)
