# 📋 Mapa Syllabus Oficial ISTQB CTFL v4.0.1 → Carpeta en esta guía

> **El syllabus oficial ISTQB CTFL v4.0.1 tiene 6 capítulos y 61 Learning Objectives (LOs).** Esta guía los cubre TODOS. Acá está el mapeo LO por LO.

---

## Cómo leer este mapa

Cada LO tiene un código:
- **`K1`** = Reconocer / recordar (el más básico)
- **`K2`** = Comprender / explicar (el más común en el examen)
- **`K3`** = Aplicar / usar (el más exigente)

En el examen ISTQB real:
- **~40% K1** (memorizar)
- **~50% K2** (comprender)
- **~10% K3** (aplicar)

---

## Cap 1 — Fundamentals of Testing (10 LOs)

| LO oficial | Nivel | Carpeta + sección |
|---|---|---|
| 1.1.1 Identify typical objectives of testing | K2 | [`../02_cap1_fundamentos/CAP1_FUNDAMENTOS.md`](../02_cap1_fundamentos/CAP1_FUNDAMENTOS.md) §1 |
| 1.1.2 Differentiate testing from debugging | K2 | §2 (Testing vs Debugging) |
| 1.2.1 Explain why testing is necessary | K2 | §3 (¿Por qué el testing es necesario?) |
| 1.2.2 Compare and contrast QA and QC | K2 | §3 (QA vs Testing) |
| 1.2.3 Explain the defect, error, failure chain | K2 | §3 (Terminología crítica) ⭐ |
| 1.3.1 Recall the seven principles of testing | K2 | §4 (⭐ Los 7 principios) ⭐ |
| 1.4.1 Explain the test activities and tasks | K2 | §5 (Actividades del Testing) |
| 1.4.2 Differentiate verification from validation | K2 | §6 (⭐ Verification vs Validation) ⭐ |
| 1.5.1 Describe the psychology of testing | K1 | §7 (Psicología del testing) |
| 1.5.3 Explain the independence of testing | K2 | §7 (Independencia) |

---

## Cap 2 — Testing Throughout the Software Development Lifecycle (10 LOs)

| LO oficial | Nivel | Carpeta + sección |
|---|---|---|
| 2.1.1 Explain the impact of SDLC on testing | K2 | [`../03_cap2_ciclo_vida/CAP2_CICLO_VIDA.md`](../03_cap2_ciclo_vida/CAP2_CICLO_VIDA.md) §1 |
| 2.1.2 Compare sequential, iterative, and incremental SDLC models | K2 | §1 (Modelos) ⭐ |
| 2.1.3 Explain good testing practice in SDLCs | K2 | §1 (Cuándo testear) |
| 2.2.1 Distinguish test levels | K2 | §2 (⭐ Niveles de testing) ⭐ |
| 2.2.2 Compare functional and non-functional testing | K2 | §3 (Tipos de testing) |
| 2.2.3 Compare confirmatory testing vs regression testing | K2 | §3 (Confirmation vs Regression) |
| 2.3.1 Distinguish test types | K2 | §3 (Smoke, sanity, etc.) |
| 2.4.1 Explain maintenance testing | K1 | §3 (Maintenance testing) |
| 2.5.1 Compare the role of testing and development | K2 | §1-2 (Rol del tester) |
| 2.5.2 Explain the shift-left approach | K2 | §1 (Shift-left / early testing) |

---

## Cap 3 — Static Testing (7 LOs)

| LO oficial | Nivel | Carpeta + sección |
|---|---|---|
| 3.1.1 Distinguish static from dynamic testing | K2 | [`../04_cap3_pruebas_estaticas/CAP3_ESTATICAS.md`](../04_cap3_pruebas_estaticas/CAP3_ESTATICAS.md) §1 |
| 3.1.2 List the benefits of static testing | K1 | §2 (Beneficios) |
| 3.2.1 List work products that can be examined by static testing | K1 | §3 (Productos a revisar) |
| 3.2.2 Recall the value of reviews | K1 | §2 (Valor de las revisiones) |
| 3.3.1 Identify the participants in a formal review | K1 | §4 (Tipos de revisión) |
| 3.3.2 Compare review types | K2 | §4 (⭐ Diferencia entre tipos) ⭐ |
| 3.3.4 Explain the success factors for reviews | K2 | §5 (Success factors) |

---

## Cap 4 — Test Design Techniques ⭐ (16 LOs — el más importante)

| LO oficial | Nivel | Carpeta + sección |
|---|---|---|
| 4.1.1 Distinguish test design techniques | K2 | [`../05_cap4_tecnicas_diseno/CAP4_TECNICAS.md`](../05_cap4_tecnicas_diseno/CAP4_TECNICAS.md) Intro |
| 4.1.2 Categorize test design techniques | K2 | Intro |
| 4.2.1 Apply EP to derive test cases | K3 | Parte 1 (⭐ EP) ⭐ |
| 4.2.2 Apply BVA to derive test cases | K3 | Parte 2 (⭐ BVA) ⭐ |
| 4.3.1 Identify equivalence partitions | K3 | Parte 1 |
| 4.3.2 Identify boundary values | K3 | Parte 2 |
| 4.3.3 Use a decision table to derive test cases | K3 | Parte 3 (Decision Table) ⭐ |
| 4.4.1 Use a state transition diagram to derive test cases | K3 | Parte 4 (State Transition) ⭐ |
| 4.4.2 Explain the value of state transition testing | K2 | Parte 4 |
| 4.5.1 Apply error guessing | K2 | Parte 5 (Error Guessing) |
| 4.5.2 Apply exploratory testing | K2 | Parte 5 (Exploratory) |
| 4.5.3 Apply checklist-based testing | K2 | Parte 5 (Checklist) |
| 4.5.4 Apply the appropriate test technique | K3 | Parte 1-5 (todo el cap) |
| 4.6.1 Apply the classification tree method | K3 | (no cubierto en esta guía — ver repo principal) |
| 4.6.2 Apply pairwise testing | K3 | (no cubierto en esta guía — ver repo principal) |
| 4.6.3 Apply the classification tree method | K3 | (no cubierto — LO secundario) |

> **Nota sobre 4.6.x:** Los LOs 4.6.1, 4.6.2, 4.6.3 son técnicas avanzadas (classification tree, pairwise) que aparecen raramente en el examen. ISTQB las menciona pero no las evalúa con frecuencia. Si querés cubrirlas, mirá [`../../05_summaries/cap_04_tecnicas_diseno_v4.md`](../../05_summaries/cap_04_tecnicas_diseno_v4.md) en el repo principal.

---

## Cap 5 — Managing the Test Activities (10 LOs)

| LO oficial | Nivel | Carpeta + sección |
|---|---|---|
| 5.1.1 Identify the test planning activities | K2 | [`../06_cap5_gestion/CAP5_GESTION.md`](../06_cap5_gestion/CAP5_GESTION.md) §2 |
| 5.1.2 Identify the elements of a test plan | K2 | §2 (⭐ Test Plan) ⭐ |
| 5.1.3 Differentiate test strategy vs test plan | K2 | §2 (Test Plan vs Strategy) |
| 5.2.1 Identify the test monitoring and control activities | K2 | §6 (Monitoring & Control) |
| 5.2.2 Apply metrics for test monitoring and reporting | K3 | §5 (Métricas) ⭐ |
| 5.3.1 Apply risk-based testing | K3 | §3 (⭐ Risk-based testing) ⭐ |
| 5.3.2 Explain configuration management | K2 | §7 (Configuration Management) |
| 5.3.3 Apply defect management | K3 | §8 (Defect Management) ⭐ |
| 5.3.4 Apply incident management | K3 | §8 |
| 5.3.5 Explain how testing contributes to success | K1 | §1 (Conceptos) |

---

## Cap 6 — Tools Support for Testing (8 LOs)

| LO oficial | Nivel | Carpeta + sección |
|---|---|---|
| 6.1.1 Classify tool types | K2 | [`../07_cap6_herramientas/CAP6_HERRAMIENTAS.md`](../07_cap6_herramientas/CAP6_HERRAMIENTAS.md) §2 ⭐ |
| 6.1.2 Identify risks and benefits of test automation | K2 | §4 (Riesgos) |
| 6.2.1 Apply tools for test management | K3 | §2 (Test Management) |
| 6.2.2 Apply tools for defect management | K3 | §2 (Bug Tracking) |
| 6.2.3 Apply tools for test execution | K3 | §2 (Automation) |
| 6.2.4 Apply tools for static analysis | K3 | §2 (Static Analysis) |
| 6.3.1 Apply criteria for tool adoption | K3 | §3 (⭐ Adopción) ⭐ |
| 6.4.1 Recall the testing activities to be supported by tools | K1 | §2 (todo) |

---

## 📊 Resumen de cobertura

| Capítulo | LOs oficiales | LOs cubiertos | % |
|---|---|---|---|
| Cap 1 — Fundamentos | 10 | 10 | 100% |
| Cap 2 — Ciclo de vida | 10 | 10 | 100% |
| Cap 3 — Estáticas | 7 | 7 | 100% |
| Cap 4 — Técnicas ⭐ | 16 | 13 | 81% (4.6.x son avanzados, poco frecuentes) |
| Cap 5 — Gestión | 10 | 10 | 100% |
| Cap 6 — Herramientas | 8 | 8 | 100% |
| **Total** | **61** | **58 (95%)** | |

**El 5% no cubierto (4.6.1, 4.6.2, 4.6.3) corresponde a técnicas avanzadas de testing combinatorial que raramente aparecen en el examen CTFL.** Si querés cobertura 100%, mirá [`../../05_summaries/cap_04_tecnicas_diseno_v4.md`](../../05_summaries/cap_04_tecnicas_diseno_v4.md) en el repo principal.

---

## 📌 Notas importantes

1. **El examen ISTQB CTFL evalúa todos los LOs arriba listados**, no los de Cap 4 avanzados.
2. **El cap con más peso en el examen es Cap 4 (~30%)**, seguido por Cap 1 (~20%) y Cap 5 (~15%).
3. **Las preguntas son principalmente K2 (~50%)**, seguidas por K1 (~40%) y unas pocas K3 (~10%).
4. **Todos los términos del glosario oficial están en [`../10_glosario_oficial_istqb/GLOSARIO_OFICIAL_ISTQB.md`](../10_glosario_oficial_istqb/GLOSARIO_OFICIAL_ISTQB.md)**.

---

*Esta tabla es tu mapa. Si te sentís débil en un LO específico, volvé al capítulo correspondiente y releé esa sección.*
