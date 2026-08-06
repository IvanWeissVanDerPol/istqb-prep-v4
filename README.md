# 🎓 ISTQB CTFL Prep Hub v4.0.1

> **Material curado para preparar el examen ISTQB Certified Tester Foundation Level (CTFL) v4.0.1** — la credencial internacional más reconocida de QA.

📅 **Basado en:** Syllabus oficial ISTQB CTFL v4.0.1 (15-sep-2024, 78 pp, 1135 min oficiales de instrucción)
📅 **Idiomas:** examen rendido en español LATAM a través de ASOLINFO Paraguay
📅 **Licencia:** MIT (este material) + © ISTQB (syllabus oficial — enlazado, no redistribuido)
🌐 **Repo público:** https://github.com/IvanWeissVanDerPol/istqb-prep-v4

---

## 🚀 Quick start (10 min reading, 8 weeks studying)

1. 📋 Lee **[`00_README/README.md`](00_README/README.md)** — overview completo
2. 📅 Sigue **[`01_plan_estudio/00_vision_general.md`](01_plan_estudio/00_vision_general.md)** — plan semana a semana
3. 📘 Entiende la **estructura del syllabus** en [`02_syllabus_v4_0_1/`](02_syllabus_v4_0_1/)
4. 📝 Lee **el resumen de cada capítulo** en [`05_summaries/`](05_summaries/)
5. ✅ Haz **quizzes por capítulo** en [`06_practice_tests/quizzes_por_capitulo/`](06_practice_tests/quizzes_por_capitulo/)
6. 🎯 Rendí **3 sample exams** completos en [`06_practice_tests/`](06_practice_tests/) (cronometrados, 60 min)
7. 🎴 Importa **flashcards** a Anki → ver [`04_flashcards/anki_import_guide.md`](04_flashcards/anki_import_guide.md)
8. 🏆 Última semana: **repasá los [quick refs](08_quick_refs/)** (1 página por capítulo)
9. 📖 Leé **[`09_career_paths/`](09_career_paths/)** después del examen para planificar tu carrera
10. 🛡️ Leé **[`10_exam_difficulty/`](10_exam_difficulty/)** para entender por qué falla la gente y cómo evitarlo

---

## 🆕 What's New (Aug 2026 update)

- **9 career paths added:** junior QA → SDET → staff engineer con salaries PY/LATAM/US
- **10 exam failure analysis** + concrete checklist (avoid the 25-30% fail rate)
- **11 cert paths** — full ISTQB catalog + alternatives (CSTE, CSQA, AWS, security certs)
- **12 external resources** — top 5 GitHub repos para CTFL v4.0 + simulators
- **Hard Mode Quiz Cap 4 & 5** — 20 preguntas con escenarios reales (donde la gente más falla)

---

## 📚 Para qué sirve este repo

| Audencia | Beneficio |
|---|---|
| 🧑‍🎓 **Aspirantes a QA** | Plan de estudio de 8 semanas con todo lo necesario para el examen |
| 👥 **Grupo de estudio** | Material compartido, quizzes, deck Anki, sample exams |
| 📚 **Profesores / Instructores** | Syllabus estructurado v4.0.1, quizzes con explicaciones |
| 🧪 **QA Analysts** | Glosario actualizado v4.0.1 + vocabulario oficial ISTQB |
| 🇵🇾 **Paraguay específico** | Contacto ASOLINFO + costos approximate |
| 💼 **Career switchers** | `09_career_paths/` para entender roles y salarios |
| 📈 **Career growth** | `11_cert_paths/` para planear siguientes certs (CTAL-TA, CT-GenAI, etc.) |

---

## 🗂️ Estructura del repo

```
istqb-prep-v4/
├── README.md                                  ← estás acá
├── LICENSE                                    ← MIT + notice sobre ISTQB
├── DEPLOY_COMMANDS.md                         ← comandos git / mantenimiento
│
├── 00_README/                                 ← overview completo
├── 01_plan_estudio/                           ← plan 8 semanas + checkpoints
├── 02_syllabus_v4_0_1/                        ← estructura oficial
├── 03_glosario/                                ← 200+ términos
├── 04_flashcards/                              ← deck Anki (85 cards CSV)
├── 05_summaries/                               ← 6 resúmenes de capítulos
├── 06_practice_tests/                          ← quizzes + 3 sample exams + hard mode quiz
├── 07_resources/                               ← links + ASOLINFO PY + ISTQB PY grupos WA
├── 08_quick_refs/                              ← 1 página por capítulo (cheatsheets)
├── 09_career_paths/                            ← QA career roadmap + salaries PY/global
├── 10_exam_difficulty/                         ← common failures + prep checklist
├── 11_cert_paths/                              ← full ISTQB catalog + alternatives
├── 12_external_resources/                      ← top GitHub repos + simulators
└── 13_v4_changes/                              ← cambios importantes v3.1 → v4.0.1
```

---

## 📊 Stats

- **42+ archivos**
- **~340 KB** de contenido markdown
- **64 Learning Objectives** cubiertos
- **6 capítulos** completos + hard mode quiz
- **120+ preguntas** entre quizzes (Cap 1+4 detallados, hard mode) y sample exams (120)
- **85 flashcards** Anki-importable
- **9 career paths** documentados
- **24+ ISTQB certifications** mapeadas
- **5 external GitHub repos** curados

---

## 🎯 Distribución por capítulo

| Cap | Título | Min. oficiales | ~Preguntas | Importancia |
|---|---|---|---|---|
| 1 | Fundamentals of Testing | 180 min | 5 | Media (7 principios son gratis) |
| 2 | Testing Throughout the SDLC | 130 min | 7 | Alta (DevOps, shift-left nuevos) |
| 3 | Static Testing | 80 min | 3 | Media (revisiones) |
| 4 | **Test Analysis and Design** | **390 min** | **12** | **CRÍTICO** — el más pesado |
| 5 | Managing the Test | 335 min | 8 | Alta (test pyramid nuevo) |
| 6 | Test Tools | 20 min | 5 | Baja |
| **Total** | | 1135 min | 40 | 60 min |

---

## 📝 ¿Cambió el syllabus? SÍ — esto es v4.0.1 (2024)

Lo más importante si ya estudiaste v3.1 (2018):

1. **Cap 4.5 NUEVO** — Collaboration-based Test Approaches (user stories, ATDD)
2. **Cap 2.1.4-6 NUEVO** — DevOps, Shift-left, Retrospectives oficiales
3. **Cap 5.1.6-7 NUEVO** — Test Pyramid + Testing Quadrants
4. **Vocabulario unificado:** `documentation` → `work products`, `stage` → `phase`, `white box` → `white-box`
5. **ISO 25010 actualizado (2023):** `usability` → `interaction capability`, `portability` → `flexibility`, **+ `safety`** (nuevo)

Ver detalles en [`13_v4_changes/CAMBIOS_v3.1_a_v4.0.1.md`](13_v4_changes/CAMBIOS_v3.1_a_v4.0.1.md)

---

## 🇵🇾 Para Paraguay específicamente

**ASOLINFO** es la entidad oficial. Material completo: [`07_resources/asolinfo_paraguay_contact.md`](07_resources/asolinfo_paraguay_contact.md).

**Costo approximate:** USD 150-300 (confirmar con ASOLINFO).
**Modalidades:** online con proctor o presencial en Asunción.
**Idioma:** español LATAM disponible.

**Sobre los 2 JIDs `@201309445722357` y `@117111141752976`:** eran IDs internos del bridge de WhatsApp de Iván (no contactos). Lo encontrado, **el grupo ISTQB PY real es `120363175387159404@g.us` (Grupo: "ISTQB Brave and Courageous")**, y los 6 miembros del grupo son:
- **Natalia Cruz** (595982923913) — tier3
- **Daisy** (595981459382) — tier2 core
- **Alejandro Maciel (MentorMate)** (595974465910) — INSTRUCTOR del curso ISTQB
- **Jose S** (595971190089) — untiered
- ¿? (595983988909) — sin nombre en vCard
- **V BC** (595961831298) — vCard

Ver [`07_resources/istqb_py_grupos_wa.md`](07_resources/istqb_py_grupos_wa.md) para el detalle.

---

## ⚠️ Limitaciones honestas

1. **Sample exams NO son oficiales** — ISTQB vende sample exams oficiales a través de Member Boards. Los de este repo son aproximaciones curriculares.
2. **El syllabus PDF no se redistribuye** — copyright ISTQB. Solo está **enlazado**.
3. **Salarios Paraguay** limitados a fuentes públicas (Glassdoor). Hay más variabilidad fuera de eso.
4. **Pass rates ISTQB no son oficiales** — son estimaciones de training providers (trendig, istqb.guru).
5. **Las cifras USD/₲ pueden cambiar** — verificar al momento de negociar.

---

## 🛠️ Stack técnico del repo

- **Markdown** (.md) — todos los archivos
- **CSV** — flashcards (Anki/Quizlet)
- **MIT License** — redistribution libre con atribución
- **Sin build process** — solo lectura

---

## 🤝 Contribuir

1. Fork el repo
2. Crea tu branch (`git checkout -b mejora/cap-5-quiz`)
3. Commit tus cambios (`git commit -m "Add Cap 5 preguntas K3 practice"`)
4. Push (`git push origin mejora/cap-5-quiz`)
5. Pull Request

---

## 🎯 Recommended Reading Order

### Antes del examen (8 semanas):
1. `01_plan_estudio/` — el plan
2. `02_syllabus_v4_0_1/` — la estructura
3. `05_summaries/` — los resúmenes
4. `06_practice_tests/quizzes_por_capitulo/` — quiz por cap
5. `06_practice_tests/sample_exam_A.md` → B → C
6. `06_practice_tests/quizzes_por_capitulo/cap_4_5_hard_mode.md` ⭐ (donde falla la gente)
7. `10_exam_difficulty/` — quédate sin fallar
8. `08_quick_refs/` — última milla
9. `04_flashcards/` — Anki mobile en commuting

### Después del examen (semana 9+):
10. `09_career_paths/` — qué carrera querés
11. `11_cert_paths/` — qué cert tomar después
12. `12_external_resources/` — otros recursos para seguir aprendiendo

---

## ❓ FAQ

**P: ¿Puedo usar este material para ganar dinero?**
R: NO comercialmente. MIT + fair-use ISTQB solo permite compartir libremente sin venta.

**P: ¿Rinde el examen tras estudiar esto?**
R: Si completás el plan de 8 semanas + 3 sample exams con ≥65% consistente, deberías pasar. Pero el material es apoyo; el syllabus PDF oficial es la fuente autoritativa.

**P: ¿Qué certificación tomar después?**
R: Depende de tu rol. Si te gusta automation → CTAL-TAE. Si vas a lead → CTAL-TM. Si te interesa AI → CT-GenAI. Ver `11_cert_paths/README.md`.

**P: ¿Es ISTQB suficiente para conseguir trabajo de QA?**
R: No. ISTQB es la **base**. Necesitás: ISTQB + automation skills (Playwright/Selenium) + inglés (B2+) + portfolio. Ver `09_career_paths/README.md`.

**P: ¿Cuál es el primer trabajo que puedo esperar?**
R: Junior QA local en PY: USD 1,300-3,300/año. Junior QA remoto para US: USD 24-48K. Ver `09_career_paths/README.md`.

---

## 📞 Soporte / comunidad

**Problemas con el material:** abrí un issue en este repo.
**Preguntas del examen:** ISTQB Member Board Paraguay (ASOLINFO).
**Preguntas ISTQB oficiales:** https://www.istqb.org

---

## 🏷️ Metadata

- **Versión ISTQB:** CTFL v4.0.1 (15-sep-2024)
- **Fecha del material:** agosto 2025
- **Maintainer:** Ivan Weiss Van Der Pol
- **Prerequisito ISTQB:** ninguno (Foundation es entrada)
- **Siguiente nivel:** CTFL Advanced (CTAL-TA/TM/TTA/TAE)

---

## 🌟 Si te sirve, dale una estrella (GitHub)

Si este material te ayudó a pasar el CTFL, una ⭐ ayuda a que otros lo encuentren.

**Happy testing! 🐛🔍**
