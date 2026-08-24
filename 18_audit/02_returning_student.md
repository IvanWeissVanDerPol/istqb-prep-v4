# 🔥 Role 2 — Returning Student (Week 3 of study)

**Quién es:** Ya leyó el README raíz, está en semana 3 del plan. Vuelve para repasar.

## 🎯 Lo que quiere

- Ver su progreso
- Hacer un quiz para autoevaluarse
- Tener un sample exam con respuestas para validar
- Encontrar flashcards rápido

## ❌ Findings con evidencia

### 🚨 P0: Sample Exams NO tienen answer keys

**`06_practice_tests/sample_exam_A.md` línea 13-353:**
Las 40 preguntas están pero **NO HAY respuestas marcadas**. Solo al final (línea 317-326) dice "calculá tu score" pero sin answer key.

**`06_practice_tests/sample_exam_B.md`** — verificar mismo problema.
**`06_practice_tests/sample_exam_C.md`** — verificar mismo problema.

**Esto hace que los sample exams sean INÚTILES para estudiar.** Son como dar examen sin gabarito.

### 🚨 P0: Quizzes tienen respuestas inconsistentes

**`06_practice_tests/quizzes_por_capitulo/cap_01_quiz.md`** — tiene respuestas en `<details>` blocks.
**`06_practice_tests/quizzes_por_capitulo/cap_02_quiz.md`** — verificar.
**`06_practice_tests/quizzes_por_capitulo/cap_04_quiz.md`** — verificar.

Si los quizzes tienen respuestas pero los sample exams no, la inconsistencia es problemática.

### 🚨 P0: No hay progress tracking personal

El plan de 8 semanas es narrativo (`01_plan_estudio/00_vision_general.md`) pero no tiene:
- Checkboxes
- Score history
- "What I did this week"
- "What's next"

Un estudiante en semana 3 no sabe qué hizo en semana 1-2.

### P1: 08_quick_refs/ y 16_cheat_sheets/ se solapan

- `08_quick_refs/` tiene cheatsheets 1-página por cap (Cap 1-6 + Global)
- `16_cheat_sheets/` tiene 15 cheat sheets printable (CS-01 a CS-15)

**Overlap del 60-70%:** Ambos hablan de principles, BVA, decision tables, etc.

Confuso: ¿cuál usar? ¿Por qué hay dos?

### P1: Flashcards insuficientes

**`04_flashcards/flashcards_v4.0.1.csv`** — 85 cards.

Pero:
- 64 LOs oficiales × ~3 cards/LO = debería ser ~200 cards
- Coverage gaps en Cap 4 (K3 aplicado) y Cap 5 (gestión)

### P1: No hay "after-cap" summary con score tracking

Después de cada cap no hay template como:
```
Cap X — [fecha] — score Y/N — tiempo Z
Dudas recurrentes: ...
Plan semana siguiente: ...
```

## 🔥 P0 Fixes (CRÍTICO)

### F2.1: Crear answer keys para Sample Exams

Crear:
- `06_practice_tests/sample_exam_A_ANSWERS.md`
- `06_practice_tests/sample_exam_B_ANSWERS.md`
- `06_practice_tests/sample_exam_C_ANSWERS.md`

**Formato:**
```markdown
# Sample Exam A — Answer Key

**Score máximo:** 40/40 (100%)
**Pass threshold:** 26/40 (65%)
**Idioma:** inglés (con explicación español)

| Q# | Respuesta | Explicación | LO |
|----|-----------|-------------|-----|
| 1  | B         | Error → defect → failure (cadena causal) | 1.2.3 |
| 2  | B         | Pesticide paradox: mismos tests = menos defects | 1.3.1 |
...
```

### F2.2: Crear `00_README/00_PROGRESS.md` personalizable

```markdown
# 📊 Mi progreso CTFL

## Setup
- [ ] Creé fork del repo
- [ ] Configuré Anki + importé flashcards
- [ ] Agendé examen con ASOLINFO para: ____

## Semana 1 (___ a ___): Cap 1
- [ ] Leí summary Cap 1
- [ ] Hice quiz Cap 1 — score: ___/20
- [ ] Repasé dudas con grupo

...
```

### F2.3: Consolidar quick_refs y cheat_sheets

**Decisión:** Mantener uno solo. Sugerencia: borrar `16_cheat_sheets/` y mover lo bueno a `08_quick_refs/`.

Razón: `08_quick_refs/` ya está nombrado "cheatsheet" — es el lugar canónico.

**O alternativamente:** consolidar en `08_quick_refs/` y dejar que `16_cheat_sheets/` desaparezca.

## 🔧 P1 Fixes

### F2.4: Expandir flashcards a 200+ cards

Generar más cards para Cap 4 (K3 aplicado) y Cap 5 (gestión).

### F2.5: Template post-cap

Crear `01_plan_estudio/templates/after_cap_review.md` con template a llenar.

## 🔧 P2 Fixes

- F2.6: Sistema de badges por cap completado
- F2.7: Dashboard script (Python) para parsear progress

## 📊 Metrics de éxito

Después de los fixes:
- 100% de sample exams tienen answer keys
- 80%+ de quizzes tienen respuestas consistentes
- Returning student puede ver "qué hice antes" sin buscar en Git log

## 🔗 Conecta con

- Theme 1 (Sin Answer Keys) — ESTE ROLE es el más afectado
- Theme 3 (Duplicación Masiva) — F2.3 fix
- Theme 5 (Falta Index) — F2.2 fix
