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

---

## 📚 Para qué sirve este repo

| Audencia | Beneficio |
|---|---|
| 🧑‍🎓 **Aspirantes a QA** | Plan de estudio de 8 semanas con todo lo necesario para el examen |
| 👥 **Grupo de estudio** | Material compartido, quizzes, deck Anki, sample exams |
| 📚 **Profesores / Instructores** | Syllabus estructurado v4.0.1, quizzes con explicaciones |
| 🧪 **QA Analysts** | Glosario actualizado v4.0.1 + vocabulario oficial ISTQB |
| 🇵🇾 **Paraguay específico** | Contacto ASOLINFO + costos aproximados |

---

## 🗂️ Estructura del repo

```
istqb-prep-v4/
├── README.md                                  ← estás acá
├── LICENSE                                    ← MIT + notice sobre ISTQB
├── DEPLOY_COMMANDS.md                         ← comandos git / mantenimiento
│
├── 00_README/                                 ← overview completo
│   └── README.md
│
├── 01_plan_estudio/                           ← plan 8 semanas + checkpoints
│   └── 00_vision_general.md
│
├── 02_syllabus_v4_0_1/                        ← estructura oficial
│   ├── README.md                              ← mapa de capítulos
│   └── MAPA_COMPLETO_OBJETIVOS.md             ← checklist de los 64 LOs
│
├── 03_glosario/                                ← 200+ términos
│   └── GLOSARIO_v4.0.1.md
│
├── 04_flashcards/                              ← deck para Anki/Quizlet
│   ├── README.md
│   ├── anki_import_guide.md
│   └── flashcards_v4.0.1.csv                  ← 85 cards importable
│
├── 05_summaries/                               ← resúmenes capítulo por capítulo
│   ├── cap_01_fundamentos_v4.md
│   ├── cap_02_ciclo_vida_v4.md                ← Shift-left, DevOps (NUEVO)
│   ├── cap_03_estaticas_v4.md
│   ├── cap_04_tecnicas_diseno_v4.md           ← EP, BVA + ATDD (NUEVO)
│   ├── cap_05_gestion_v4.md                   ← Test pyramid (NUEVO)
│   └── cap_06_herramientas_v4.md
│
├── 06_practice_tests/                          ← quizzes + simulacros
│   ├── quizzes_por_capitulo/
│   │   ├── cap_01_quiz.md                     ← 20 preguntas
│   │   ├── cap_02_quiz.md                     ← 15 preguntas
│   │   ├── cap_03_quiz.md                     ← 10 preguntas
│   │   ├── cap_04_quiz.md                     ← 30 preguntas (el pesado)
│   │   ├── cap_05_quiz.md                     ← 15 preguntas
│   │   └── cap_06_quiz.md                     ← 8 preguntas
│   ├── sample_exam_A.md                       ← 40 preguntas, 60 min
│   ├── sample_exam_B.md                       ← variación A
│   └── sample_exam_C.md                       ← variación con K3 emphasized
│
├── 07_resources/                               ← links + herramientas
│   ├── links_utiles.md                         ← ISTQB, libros, cursos, videos
│   ├── herramientas_para_practicar.md         ← OWASP Juice Shop, Playwright, etc.
│   └── asolinfo_paraguay_contact.md            ← cómo inscribirte en PY
│
├── 08_quick_refs/                              ← 1 página por capítulo
│   ├── cap_00_cheatsheet_global.md
│   ├── cap_01_cheatsheet.md
│   ├── cap_02_cheatsheet.md
│   ├── cap_03_cheatsheet.md
│   ├── cap_04_cheatsheet.md
│   ├── cap_05_cheatsheet.md
│   └── cap_06_cheatsheet.md
│
└── 09_v4_changes/                              ← cambios importantes v3.1 → v4.0.1
    └── CAMBIOS_v3.1_a_v4.0.1.md               ← ~20% del contenido cambió
```

---

## 📊 Stats

- **37 archivos**
- **215 KB** (~185 KB de contenido markdown)
- **64 Learning Objectives** cubiertos
- **6 capítulos** completos
- **98 preguntas** entre quizzes (98) y sample exams (120)
- **85 flashcards** Anki-importable

---

## 🎯 Distribución por capítulo (siguiendo el syllabus oficial)

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

Ver detalles en [`09_v4_changes/CAMBIOS_v3.1_a_v4.0.1.md`](09_v4_changes/CAMBIOS_v3.1_a_v4.0.1.md)

---

## 🇵🇾 Para Paraguay específicamente

**ASOLINFO** es la entidad oficial. Material completo: [`07_resources/asolinfo_paraguay_contact.md`](07_resources/asolinfo_paraguay_contact.md).

**Costo approximate:** USD 150-300 (confirmar con ASOLINFO).
**Modalidades:** online con proctor o presencial en Asunción.
**Idioma:** español LATAM disponible.

---

## ⚠️ Limitaciones honestas

1. **Sample exams NO son oficiales** — ISTQB vende sample exams oficiales a través de Member Boards. Los de este repo son aproximaciones curriculares.
2. **El syllabus PDF no se redistribuye** — copyright ISTQB. Solo está **enlazado**.
3. **JIDs `@201309445722357` y `@117111141752976`** no se identificaron en el corpus local (probablemente canales/grupos externos de ISTQB PY).

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

## ❓ FAQ

**P: ¿Puedo usar este material para ganar dinero?**
R: NO comercialmente. MIT + fair-use ISTQB solo permite compartir libremente sin venta.

**P: ¿Rinde el examen tras estudiar esto?**
R: Si completás el plan de 8 semanas + 3 sample exams con ≥65% consistente, deberías pasar. Pero el material es apoyo; el syllabus PDF oficial es la fuente autoritativa.

**P: ¿Puedo estudiar con la app de iOS/Android?**
R: No dedicado — usá Anki mobile + descargar el repo offline.

**P: ¿Necesito experiencia previa en QA?**
R: No obligatorio pero ayuda. Algunos conceptos (DevOps, ATDD) requieren familiaridad con desarrollo.

**P: ¿Qué pasa si paso en inglés en lugar de español?**
R: El contenido ISTQB CTFL se mantiene igual. Cuestiones cambian:
- Tests disponibles en ambos idiomas (ASOLINFO)
- Vocabulario a veces varía sutilmente (mejores: usar inglés del syllabus)

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
- **Siguiente nivel:** CTFL Advanced (CTAL)

---

## 🌟 Si te sirve, dale una estrella (GitHub)

Si este material te ayudó a pasar el CTFL, una ⭐ ayuda a que otros lo encuentren.

**Happy testing! 🐛🔍**
