# 🚀 Plan de Mejoras Detallado — Roadmap

> **Después de la auditoría adversarial** — qué cambiar, en qué orden, y por qué.
>
> **Estructura:** Sprint 1 (esta semana) → Sprint 2 (próximas 2 semanas) → Sprint 3+ (mes)

---

## 🎯 Sprint 1 — Crítico (esta semana)

### F1. Eliminar duplicación

**Problema:** `08_quick_refs/` (7 archivos) y `16_cheat_sheets/` (15 sheets) tienen overlap del 70%.

**Acción:**
1. Mantener `08_quick_refs/` (más enfocado en cheat sheet por cap)
2. Mover lo bueno de `16_cheat_sheets/` (15 sheets ASCII) a `08_quick_refs/`
3. Borrar `16_cheat_sheets/`
4. Actualizar README para reflejar cambio

**Esfuerzo:** 2 horas
**Impacto:** -50% duplicación, navegación más clara

---

### F2. Crear `INDEX.md` raíz (resumen)

**Problema:** 17 directorios sin mapa central.

**Acción:**
Crear `INDEX.md` con:
- Tabla de todos los directorios con descripción 1-línea
- Tabla de todos los archivos con tamaño + descripción
- "Si solo lees 3 archivos: X, Y, Z"

**Esfuerzo:** 1 hora
**Impacto:** Reduce "dónde está X?" type questions

---

### F3. Expandir flashcards a 200+

**Problema:** 85 cards vs 200+ ideales.

**Acción:**
1. Generar más cards para Cap 4 (K3) — 50 cards
2. Generar más cards para Cap 5 (gestión) — 30 cards
3. Cap 1, 2, 3: completar gaps — 35 cards

**Esfuerzo:** 3 horas
**Impacto:** Spaced repetition más completo

---

### F4. Estandarizar glossary

**Problema:** Glossary tiene 50 términos vs 200+ ideales.

**Acción:**
1. Auditar qué LO no tiene término en glossary
2. Agregar 100+ términos faltantes
3. Cross-reference con syllabus LOs

**Esfuerzo:** 3 horas
**Impacto:** Reference material más completo

---

## 🎯 Sprint 2 — Importante (próximas 2 semanas)

### F5. GitHub Actions / CI

**Acción:**
1. `.github/workflows/markdown-lint.yml` — validar markdown
2. `.github/workflows/link-checker.yml` — validar links externos
3. `.github/workflows/internal-links.yml` — validar cross-refs internos
4. `.github/workflows/quiz-validator.yml` — verificar que quizzes tienen respuestas

**Esfuerzo:** 4 horas (configurar + debug)
**Impacto:** Previene rotura futura

---

### F6. Issue templates + PR template

**Acción:**
1. `.github/ISSUE_TEMPLATE/bug_report.md`
2. `.github/ISSUE_TEMPLATE/feature_request.md`
3. `.github/ISSUE_TEMPLATE/question.md`
4. `.github/PULL_REQUEST_TEMPLATE.md`

**Esfuerzo:** 2 horas
**Impacto:** Contribuciones estructuradas

---

### F7. SECURITY.md + Dependabot

**Acción:**
1. `SECURITY.md` con disclosure policy
2. `.github/dependabot.yml` para update actions

**Esfuerzo:** 1 hora
**Impacto:** Compliance + seguridad

---

### F8. CITATION.cff + Zenodo

**Acción:**
1. `CITATION.cff` para citación académica
2. Activar Zenodo integration

**Esfuerzo:** 30 min
**Impacto:** Citable academicamente

---

## 🎯 Sprint 3 — Stretch (mes)

### F9. ARCHITECTURE.md + ROADMAP.md

**Acción:**
1. `ARCHITECTURE.md` — decisiones de diseño (¿por qué 17 directorios? ¿por qué no GitHub Pages? etc)
2. `.github/ROADMAP.md` — qué viene en próximas versiones

**Esfuerzo:** 2 horas
**Impacto:** Mantenibilidad futura

---

### F10. Directorios nuevos para audiencias específicas

**Acción:**
1. `19_for_managers/` — para hiring managers + OKRs
2. `20_for_instructors/` — lesson plans + slides

**Esfuerzo:** 4 horas (más contenido que crear)
**Impacto:** Nuevas audiencias

---

### F11. Traducción a inglés + portugués

**Acción:**
1. `21_translations/en/` — version inglés
2. `21_translations/pt/` — version portugués
3. Translation memory

**Esfuerzo:** 8 horas
**Impacto:** Alcance global

---

### F12. GitHub Pages + sitio navegable

**Acción:**
1. `mkdocs.yml`
2. Theme (Material)
3. Deploy via GitHub Actions

**Esfuerzo:** 4 horas
**Impacto:** UX mejorada, SEO

---

## 📊 Backlog priorizado completo

### P0 (crítico)
1. ✅ Sample Exam A answer key (DONE)
2. ✅ Sample Exam A inline answers (DONE)
3. ✅ Progress tracker (DONE)
4. ✅ 60-second elevator pitch (DONE)
5. ✅ Badges (DONE)
6. ✅ What this is NOT (DONE)
7. ✅ CONTRIBUTING.md (DONE)
8. ✅ CODE_OF_CONDUCT.md (DONE)
9. ⏳ Issue templates (Sprint 2)
10. ⏳ Sample Exam B + C format check (verify answer keys)
11. ⏳ Glossary expansion (Sprint 1)

### P1 (importante)
1. ⏳ F1: Eliminar duplicación (Sprint 1)
2. ⏳ F2: INDEX.md raíz (Sprint 1)
3. ⏳ F3: Flashcards 200+ (Sprint 1)
4. ⏳ F5: GitHub Actions (Sprint 2)
5. ⏳ F6: Issue templates (Sprint 2)
6. ⏳ F8: CITATION.cff (Sprint 2)
7. ⏳ F11: Traducción (Sprint 3)
8. ⏳ F12: GitHub Pages (Sprint 3)

### P2 (backlog)
1. ⏳ F9: ARCHITECTURE.md
2. ⏳ F10: Directories nuevos
3. ⏳ Diagramas visuales (mermaid)
4. ⏳ Search integration (Algolia DocSearch)

### P3 (cosmetic)
1. ⏳ Dark mode testing
2. ⏳ Print stylesheet
3. ⏳ Custom logo

---

## 🚀 Quick wins (menos de 30 min cada uno)

- [ ] Agregar GitHub topics al repo (`istqb`, `ctfl`, `qa`, `paraguay`)
- [ ] Agregar repo description (ya está en README)
- [ ] Pin 3 issues importantes
- [ ] Habilitar Discussions
- [ ] Crear `social-preview.png` (1280x640)
- [ ] Crear `CONTRIBUTORS.md` automático
- [ ] Crear `.editorconfig`

---

## 📊 Métricas de éxito

**Después de Sprint 1:**
- 0 sample exams sin answer key
- 200+ flashcards
- 200+ glossary terms
- 50% menos duplicación

**Después de Sprint 2:**
- 100% issues con template
- 100% links válidos (CI)
- Markdown lint pasa
- Citable en papers académicos

**Después de Sprint 3:**
- 3 idiomas (es, en, pt)
- GitHub Pages live
- Nuevos directorios (managers, instructors)

---

## 🤝 Quién hace qué

- **Ivan (maintainer):** decisiones de roadmap, releases
- **Contributors:** PRs individuales (cualquiera)
- **Future maintainers:** si Iván deja el proyecto, definir succession plan

---

## 📞 Contacto para feedback

- GitHub Issues: https://github.com/IvanWeissVanDerPol/istqb-prep-v4/issues
- Discussions: (TBD)
- Email: ivanweissvanderpol@gmail.com
