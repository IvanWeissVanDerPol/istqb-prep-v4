# Sample Exam A — Answer Key

> **Score máximo:** 40/40 (100%)
> **Pass threshold:** 26/40 (65%)
> **Validar contra:** ISTQB CTFL Syllabus v4.0.1
> **Este es un gabarito NO oficial.** ISTQB vende sample exams oficiales a través de Member Boards (ASOLINFO Paraguay).

---

## 📊 Score interpretation

| Score | Resultado |
|---|---|
| **≥80% (32+)** | Excelente. Listo para examen real. |
| **65-79% (26-31)** | OK. Rendí. Repasá puntos débiles. |
| **50-64% (20-25)** | Necesita más estudio. Volvé a summaries. |
| **<50% (<20)** | Repasá el plan desde semana 1. |

---

## 📝 Answer Key — Detallado

| Q# | LO | Respuesta | K-level | Explicación |
|----|----|-----------|---------|-------------|
| **1** | 1.2.3 | **B** (Error → defect → failure) | K2 | Cadena causal oficial: humano hace Error → queda Defect en código → Defect ejecuta → Failure observable |
| **2** | 1.3.1 | **B** (Aplicar los mismos tests repetidamente encuentra cada vez menos nuevos defects) | K1 | Pesticide paradox — los bugs se "inmunizan" a tests repetidos; hay que refresh tests |
| **3** | 1.3.1 | **B** (Un sistema sin defects puede no satisfacer las necesidades del usuario) | K2 | Absence-of-errors fallacy: software puede ser 99% bug-free pero totalmente inútil. Ej: software correcto per spec pero nadie lo quiere |
| **4** | 1.4.1 | **D** (Test abandonment) | K2 | Las 5 actividades son: planning, analysis, design, implementation, execution, completion. "Abandonment" no es actividad |
| **5** | 1.5.3 | **C** (Testing realizado por un equipo independiente externo) | K2 | Independencia crece: same author → peer → separate team → external company. C es la MÁS independiente |
| **6** | 2.2.1 | **C** (Functional testing) | K2 | 4 niveles ISTQB: Component, Integration, System, Acceptance. Functional NO es nivel, es tipo |
| **7** | 2.2.2 | **B** (Verificar performance bajo carga) | K2 | Non-functional = calidad (perf, security, usability). Functional = qué hace. A,C,D son funcionales |
| **8** | 2.2.3 | **B** (Confirmation verifica bug específico fixed; regression verifica nada más se rompió) | K2 | Confirmation = re-test específico. Regression = broad sweep. NO son sinónimos |
| **9** | 2.1.5 | **B** (Mover testing hacia el inicio del SDLC) | K2 | Shift-left = testear antes, no después |
| **10** | 2.1.4 | **B** (Testing continuo integrado en CI/CD) | K2 | DevOps impact: continuous testing en pipeline |
| **11** | 2.1.3 | **D** (XYZ-testing) | K1 | TDD, ATDD, BDD son test-first approaches. "XYZ-testing" no existe en ISTQB |
| **12** | 2.1.6 | **B** (Mecanismo para identificar mejoras continuas al proceso de testing) | K2 | Retrospectives = process improvement. NO son para castigar |
| **13** | 3.1.3 | **B** (Static testing NO ejecuta el software; dynamic testing SÍ lo ejecuta) | K2 | Definición directa |
| **14** | 3.2.4 | **D** (Inspection) | K2 | Inspection es la MÁS formal (roles + métricas + entry/exit criteria) |
| **15** | 3.2.3 | **B** (Moderator) | K1 | Roles ISTQB: moderator, author, reader, scribe, reviewer. Hacker/Scrum Master/end-user no son roles de review |
| **16** | 4.2.1 | **C** (3) | K3 | EP para 18-65: <18 (inválida), 18-65 (válida), >65 (inválida). 3 particiones, 3 tests |
| **17** | 4.2.2 | **B** (0, 1, 31, 32) | K3 | BVA 2-value clásico para 1-31: b-1=0, b=1, a=31, a+1=32 |
| **18** | 4.2.3 | **D** (32) | K3 | 2^5 = 32 combinaciones posibles para 5 conditions binarias |
| **19** | 4.2.4 | **B** (Estados, eventos, transiciones y acciones) | K3 | State transition testing cubre los 4 elementos del modelo |
| **20** | 4.3.2 | **B** (Requiere que cada decisión se evalúe a true y false) | K2 | Branch coverage implica statement coverage (branch ≥ statement siempre) |
| **21** | 4.4.1 | **C** (Experience-based) | K2 | Error guessing es experience-based (vs specification, structure, collaboration) |
| **22** | 4.4.2 | **B** (Combina diseño, ejecución y aprendizaje en paralelo) | K2 | Exploratory testing = aprender+diseñar+ejecutar simultáneamente. NO es aleatorio |
| **23** | 4.4.3 | **B** (Usa listas de verificación predefinidas) | K2 | Checklist-based = pre-made lists. NO es ad-hoc |
| **24** | 4.5.1 | **B** ("Como <rol>, quiero <acción>, para <beneficio>") | K2 | User story format estándar |
| **25** | 4.5.2 | **D** (Compiled OOP class) | K2 | Acceptance criteria: Given-When-Then (Gherkin), checklist, scenarios. OOP class no es opción |
| **26** | 4.5.3 | **B** (Acceptance Test-Driven Development) | K3 | ATDD = team escribe acceptance tests ANTES del código |
| **27** | 4.3.3 | **B** (Encontrar código muerto y medir coverage) | K2 | White-box útil para coverage + código muerto. NO reemplaza black-box |
| **28** | 5.1.6 | **C** (Abajo — unit tests) | K1 | Test pyramid: 70% unit (base), 20% integration, 10% E2E |
| **29** | 5.2.1 | **B** (Multiplicando likelihood × impact) | K1 | Risk = likelihood × impact (producto, no suma) |
| **30** | 5.2.2 | **C** (Un riesgo que afecta el schedule/coste/calidad del proyecto de testing) | K2 | Project risk ≠ product risk. Project = schedule/coste. Product = calidad del producto |
| **31** | 5.1.3 | **B** (Entry ANTES de empezar; Exit ANTES de cerrar) | K2 | Entry/exit criteria NO son sinónimos (v4.0.1 explícito) |
| **32** | 5.5.1 | **B** (Severity y priority) | K3 | Defect report típico: ID, title, severity, priority, description, steps to reproduce, expected/actual |
| **33** | 5.3.1 | **C** (Cantidad de developers) | K2 | Métricas ISTQB: % ejecución, % pass, defects found/resolved. Cantidad de devs no es métrica de testing |
| **34** | 5.1.5 | **B** (Determinar el ORDEN en que se ejecutan tests según riesgo/cobertura) | K3 | Prioritization = orden de ejecución |
| **35** | 5.1.7 | **D** (Component testing) | K2 | Q1 (tech-facing, support team) = component + integration. Performance/Functional/Security son otros Q |
| **36** | 6.1.1 | **D** (Calendar tool) | K2 | ISTQB tool categories: management, execution, static analysis, performance, etc. Calendar no es ISTQB tool category |
| **37** | 6.2.1 | **B** (Repetibilidad y velocidad para tests repetitivos) | K1 | Automation benefit: repetibilidad + velocidad. NO elimina todos bugs ni reemplaza humanos |
| **38** | 6.2.1 | **B** (Mantenimiento alto y expectativa falsa de "100% coverage") | K1 | Automation risk: maintenance burden + unrealistic expectations |
| **39** | 6.1.1 | **B** (Indefinición de variables / potencial null) | K2 | Static analysis: detecta undefined variables, syntax errors, code smells. Runtime bugs requiere dynamic |
| **40** | 6.1.1 | **B** (Herramienta que ejecuta tests automáticamente, e.g., Selenium, Playwright) | K2 | Test execution tool = automated test runner |

---

## 🎯 Análisis por capítulo

| Cap | Score | % | Status |
|---|---|---|---|
| 1 (Q1-5) | /5 | % | _____ |
| 2 (Q6-12) | /7 | % | _____ |
| 3 (Q13-15) | /3 | % | _____ |
| 4 (Q16-27) | /12 | % | _____ |
| 5 (Q28-35) | /8 | % | _____ |
| 6 (Q36-40) | /5 | % | _____ |
| **Total** | **/40** | **%** | _____ |

---

## 🔴 Diagnóstico (si fallaste ≥30% en algún cap)

| Si fallaste en | Acción |
|---|---|
| **Cap 1** | Volvé a `05_summaries/cap_01_fundamentos_v4.md`. Memorizar 7 principios |
| **Cap 2** | Repasá SDLC, niveles, test-first approaches, shift-left |
| **Cap 3** | Memorizar tipos de review + static vs dynamic |
| **Cap 4** | Práctica hands-on de BVA, EP, decision tables. Construir tablas a mano |
| **Cap 5** | Memorizar risk = likelihood × impact. Repasar test pyramid + quadrants |
| **Cap 6** | Categorías de tools. Automation benefits vs risks |

---

## ⚠️ Disclaimer sobre estas respuestas

**Importante:** estas respuestas son **mi mejor interpretación** del syllabus oficial v4.0.1, no garantizadas 100% correctas. Diferencias posibles:

- **K-level assignments** pueden variar entre versiones
- **LO numbers** (e.g., 4.2.1) son aproximados — ISTQB los publica con otro formato
- **Wording** de preguntas puede ser diferente al oficial

**Para validación oficial:** rendí un sample oficial ISTQB (vendido por ASOLINFO).

---

## 🚀 Próximos pasos después de Sample Exam A

| Score | Acción |
|---|---|
| ≥80% | Rendí Sample Exam B + C. Si pasás los 3 con ≥75% → rendí el real |
| 65-79% | Repasá puntos débiles. Rendí Sample B en 2-3 días |
| 50-64% | Volvé a summaries + flashcards. Reintentá en 1 semana |
| <50% | Empezá desde semana 1 del plan. Reintentá en 2 semanas |

---

**Suerte. 🍀**
