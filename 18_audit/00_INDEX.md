# 🔥 Adversarial Audit — ISTQB CTFL Prep Hub v4.0.1

> **Auditoría honesta y adversarial** — 30+ roles, ~150+ findings, evidencia concreta.
>
> **Para qué sirve:** roadmap de mejoras, identificación de gaps críticos, honestidad sobre lo que falta.
>
> **Fecha:** agosto 2025
> **Versión auditada:** `IvanWeissVanDerPol/istqb-prep-v4` @ `c88d0bc`
> **Stats del repo auditado:** 48 archivos, 516KB, 17 directorios

---

## 📋 Cómo leer este auditoría

- **Roles 1-5:** Usuarios finales (estudiantes ISTQB)
- **Roles 6-10:** Expertos del dominio (instructores, ISTQB officials)
- **Roles 11-15:** Especialistas técnicos (frontend devs, content writers, SEO)
- **Roles 16-20:** Edge cases (mobile, no-native speaker, accessibility)
- **Roles 21-30:** Adversariales (competencia, trolls, plagiaristas)

Cada role tiene **≥5 findings** con números de línea o paths concretos.
Cada role tiene **P0/P1/P2/P3 fixes** separados al final.

## 📑 Índice de roles

| # | Rol | Archivo |
|---|---|---|
| 1 | First-time Student | `01_first_time_student.md` |
| 2 | Returning Student (week 3) | `02_returning_student.md` |
| 3 | Junior QA buscando trabajo | `03_junior_qa_job_hunt.md` |
| 4 | Senior / Manager | `04_senior_qa_manager.md` |
| 5 | CTFL Instructor | `05_instructor.md` |
| 6 | ISTQB Official | `06_istqb_official.md` |
| 7 | QA Tool Vendor | `07_vendor.md` |
| 8 | Academic Researcher | `08_researcher.md` |
| 9 | Translator | `09_translator.md` |
| 10 | Recruiter / HR | `10_recruiter.md` |
| 11 | GitHub Power User | `11_github_power_user.md` |
| 12 | SEO Specialist | `12_seo.md` |
| 13 | Content Writer | `13_content_writer.md` |
| 14 | UX/UI Designer | `14_designer.md` |
| 15 | Backend Dev (static analysis) | `15_backend.md` |
| 16 | Mobile User | `16_mobile.md` |
| 17 | Screen Reader User | `17_screen_reader.md` |
| 18 | Non-native English Speaker | `18_non_native.md` |
| 19 | Power User / Returning | `19_power_user.md` |
| 20 | New Team Member | `20_new_member.md` |
| 21 | Competitor (other ISTQB repo) | `21_competitor.md` |
| 22 | Troll / Hater | `22_troll.md` |
| 23 | Plagiarist | `23_plagiarist.md` |
| 24 | Scraper (training data) | `24_scraper.md` |
| 25 | Spam Bot | `25_spam.md` |
| 26 | Hacker | `26_hacker.md` |
| 27 | Lawyer (ISTQB IP) | `27_lawyer.md` |
| 28 | Diplomat / International body | `28_diplomat.md` |
| 29 | Future Maintainer (6 months later) | `29_future_maintainer.md` |
| 30 | Aisatsu (random visitor) | `30_random_visitor.md` |

## 🔥 Top 10 P0 (CRITICAL — debe arreglarse ASAP)

1. **Sample exams A, B, C NO tienen answer keys.** Sin respuesta correcta marcada, son inútiles para estudiar. El README dice "calculá tu score" pero no podés. **CRITICAL.**
2. **Sample exams no especifican idioma** — la audiencia es Paraguay pero las preguntas están mezcladas en español. Algunos hablan de "K-levels" sin contexto.
3. **No hay progress tracking** — el plan de 8 semanas es narrativo, sin checkboxes.
4. **Repetición extrema** — el contenido está duplicado entre `08_quick_refs/`, `13_v4_changes/`, `16_cheat_sheets/`. Tres lugares para lo mismo.
5. **Sample exams respuestas no validadas** — escribí las preguntas sin verificar contra fuentes oficiales. Pueden tener errores.
6. **README raíz overwhelming** — 12KB de front-loaded content. No hay 60-second elevator pitch.
7. **Glossary inconsistente** — `03_glosario/GLOSARIO_v4.0.1.md` es 11KB. Debería ser 200+ términos pero solo tiene ~50.
8. **No hay index/table of contents navegable** — el repo no tiene un `INDEX.md` central que mapee todos los archivos.
9. **`04_flashcards/flashcards_v4.0.1.csv` tiene 85 cards pero la calidad es inconsistente** — algunas tienen definiciones, otras son K1 triviales.
10. **No hay `CONTRIBUTING.md`** — el README lo menciona pero el archivo no existe.

## 🔥 Top 10 P1 (importante — debe arreglarse en próximas 2 semanas)

1. **No hay badges** (license, version, contributors, last-update).
2. **No hay GitHub Actions** — el repo no tiene CI/CD.
3. **No hay link checker** para URLs externos (88+ URLs en el repo, muchos se van a romper).
4. **No hay CHANGELOG.md** — el repo evolucionó sin track.
5. **No hay CITATION.cff** — no se puede citar académicamente.
6. **No hay CODE_OF_CONDUCT.md**.
7. **No hay LICENSE educational use** — un instructor no sabe si puede usar esto en su curso pago.
8. **No hay `translations/`** — para escalar a PT, EN, FR.
9. **`09_career_paths/` tiene salarios sin source verification** — números aproximados sin citas claras.
10. **No hay version pinning** — el repo dice "v4.0.1" pero si ISTQB publica errata 4.0.2, no hay manera de saber.

## 🔥 Top 10 P2 (nice-to-have — backlog)

1. **No hay GitHub Pages** (sitio web rendered del repo).
2. **No hay issue templates** específicos para bug/feature/question.
3. **No hay PR template**.
4. **No hay Discussions** activado.
5. **No hay wiki** activado.
6. **No hay project board** (Kanban para roadmap).
7. **No hay GitHub Sponsors** configurado.
8. **No hay "buy me a coffee"** link.
9. **No hay release notes** por commit importante.
10. **No hay `docs/` directory** para arquitectural decisions.

## 🔥 Top 10 P3 (cosmetic / nice)

1. **No hay theme** — todo default GitHub markdown.
2. **No hay diagramas** — solo ASCII art y tablas.
3. **No hay infografía** — todo texto.
4. **No hay podcasts / video** — solo lectura.
5. **No hay Discord/Slack** link.
6. **No hay Twitter/Mastodon** social.
7. **No hay "featured" section** en GitHub repo.
8. **No hay social preview image** (PNG/JPG).
9. **No hay favicon** (no aplica en GitHub).
10. **No hay "forked from"** si es fork (no es fork).

## 🔥 Cross-cutting themes (themes que cruzan todos los roles)

### Theme 1: Sin Answer Keys = El Material No Funciona

**Afecta:** Roles 1, 2, 3, 5.

El sample exam sin respuestas es como dar examen sin gabarito. Es lo más básico de cualquier plataforma de estudio.

**Fix propuesto:**
- Crear `06_practice_tests/sample_exam_A_answers.md`, `B_answers.md`, `C_answers.md`
- Formato: cada pregunta con respuesta correcta + explicación breve + LO reference

### Theme 2: Numeración Frágil y No Extensible

**Afecta:** Roles 1, 11, 29.

`09_career_paths/` se renombró a `09_career_paths/` y `09_v4_changes/` a `13_v4_changes/`. Esto rompe:
- Cualquier link interno que apunte a `09_v4_changes/`
- Cualquier PR que referencie el número
- La intuición del orden

**Fix propuesto:**
- Usar naming sin numbering (e.g. `career-paths/`, `v4-changes/`)
- O usar namespaces temáticos (`topic-career/`, `topic-v4-changes/`)

### Theme 3: Duplicación Masiva Entre Secciones

**Afecta:** Roles 1, 2, 13.

Múltiples lugares con la misma información:
- `08_quick_refs/` + `16_cheat_sheets/` (overlap 70%)
- `02_syllabus_v4_0_1/` + `05_summaries/` (overlap parcial)
- `10_exam_difficulty/` + `15_interview_prep/` (overlap conceptual)

**Fix propuesto:**
- Consolidar en uno solo
- O usar cross-references explícitos en lugar de duplicar

### Theme 4: No Hay Validación Independiente del Material

**Afecta:** Roles 6, 8.

Escribí preguntas, definiciones, y advice basado en research web. Pero:
- Ninguna pregunta fue validada contra ISTQB official
- Los números de LO son aproximados
- Salarios son aproximados

**Fix propuesto:**
- Cross-reference con iSQI/ISTQB official practice exams (si disponible)
- Disclaimer más prominente

### Theme 5: Falta Index/Navigation Central

**Afecta:** Roles 1, 11, 20.

17 directorios sin un index. Un recién llegado se pierde.

**Fix propuesto:**
- `INDEX.md` raíz con árbol completo + descripción de cada archivo
- O GitHub Pages con sitio navegable

### Theme 6: Contribuir es Ambigüo

**Afecta:** Roles 7, 9, 20.

README dice "abrí un issue o PR" pero no hay:
- CONTRIBUTING.md
- Issue templates
- PR template
- Code of conduct
- Style guide

**Fix propuesto:**
- Crear `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md`
- Crear `CONTRIBUTING.md` raíz
- Crear `CODE_OF_CONDUCT.md`

### Theme 7: Trademark / Branding Risk

**Afecta:** Roles 6, 27.

"ISTQB" es marca registrada. El repo la usa libremente.

**Fix propuesto:**
- Disclaimer prominent
- "Not affiliated" + "Not endorsed" prominent
- Si ISTQB pide cambio, remover branding

### Theme 8: Gaps de Mantenimiento Continuo

**Afecta:** Roles 19, 29.

El repo creció sin:
- CHANGELOG
- Release tagging
- Roadmap
- Issue triage process

**Fix propuesto:**
- CHANGELOG.md retroactivo + prospectivo
- GitHub Releases por versión
- Roadmap.md en `.github/`

### Theme 9: Faltan Roles Inesperados

**Afecta:** Roles 5, 10, 28.

El repo está orientado al estudiante. Faltan:
- Instructores
- Managers / decision makers
- Políticos / policy makers
- Recruiters

**Fix propuesto:**
- Sección "Para instructores" / "Para managers"
- Adaptar contenido

### Theme 10: Faltan Datos Paraguay-Específicos

**Afecta:** Roles 1, 3.

El grupo ISTQB PY es real (Daisy, Natalia, Jose S, V BC, Alejandro Maciel). Pero:
- No hay "Costo de vida PY 2025" comparativo
- No hay "Empresas que contratan QA en PY"
- No hay "Convenciones colectivas PY" si existen

**Fix propuesto:**
- Sección específica PY con datos locales
- Lista de empresas tech PY que contratan QA

## 📊 Resumen estadístico de findings

| Severidad | Cantidad aprox. |
|---|---|
| **P0 (crítico)** | ~25-30 |
| **P1 (importante)** | ~35-40 |
| **P2 (backlog)** | ~40-50 |
| **P3 (cosmético)** | ~30-40 |
| **Total** | ~150-200 |

## 🎯 Plan de acción inmediato (las 5 cosas más importantes)

Si tuviera que arreglar **5 cosas hoy**, serían:

1. **Crear answer keys para los 3 sample exams** — esto solo ya desbloquea el valor del material.
2. **Crear `INDEX.md` raíz** — un mapa de 1 página que muestre todo lo que hay.
3. **Consolidar `08_quick_refs/` y `16_cheat_sheets/`** — elegir uno y migrar.
4. **Crear `CONTRIBUTING.md`** — para que gente pueda contribuir sin ambigüedad.
5. **Agregar badges al README raíz** — signals de confianza.

Después de eso:
6. Crear GitHub Actions para validar markdown + check links
7. Crear CITATION.cff + Zenodo integration
8. Agregar `translations/` directory
9. Crear `19_for_managers/` + `20_for_instructors/`
10. Roadmap en `.github/ROADMAP.md`

---

## 📚 Cómo este documento se conecta con el resto del repo

- **Roles 1-5** → mejoras en contenido (`05_summaries/`, `06_practice_tests/`)
- **Roles 6-10** → mejoras legales / partnership (`LICENSE`, trademarks)
- **Roles 11-15** → mejoras técnicas (`.github/`, CI/CD)
- **Roles 16-20** → mejoras UX/accessibility
- **Roles 21-30** → riesgos y mitigaciones

---

## 🔗 Links a findings detallados

Cada rol tiene su propio archivo con ≥10 findings, evidencia línea por línea, y P-buckets separados.

Empezá por:
- [`01_first_time_student.md`](01_first_time_student.md) — el más importante
- [`02_returning_student.md`](02_returning_student.md) — el segundo más crítico

---

## ✍️ Sobre este audit

- **Autor:** Erebus (Erebus)
- **Fecha:** agosto 2025
- **Versión:** 1.0
- **Status:** living document — actualizable
- **Disclaimer:** Es honesto pero no exhaustivo. Un audit completo sería 100+ páginas.

**Si querés agregar findings nuevos:** abrí un PR con un archivo `NN_new_role.md` siguiendo el formato.
