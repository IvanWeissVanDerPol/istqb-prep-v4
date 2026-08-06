# Sample Exam C — ISTQB CTFL v4.0.1 (40 preguntas)

> Variación más práctica, con preguntas "K3 apply" emphasized.

---

## Cap 1 (5 preguntas)

**C1. (K2, 1.4.1) ¿En qué actividad NO se produciría un test log?**

A) Test execution.
B) Test completion.
C) Test design.
D) Test analysis.

<details><summary>✅</summary>C. Test design produce test cases y data, no test logs. Logs son de execution.</details>

**C2. (K2, 1.2.3) Un developer escribe mal la condición `i<3` en lugar de `i<=3`. Esto es un:**

A) Failure.
B) Error.
C) Defect.
D) Root cause.

<details><summary>✅</summary>C. Action wrong = defect en código. Error = mistake humano (no el acto de copiar mal en sí). Root cause = por qué se equivocó.</details>

**C3. (K1, 1.3.1) El "pesticide paradox" se supera con:**

A) Más test cases del mismo tipo.
B) Actualizar y diversificar tests regularmente.
C) Eliminar tests viejos.
D) No hacer testing.

<details><summary>✅</summary>B. Mismos tests = mismos bugs encontrados. Solución: actualizar tests, agregar nuevos.</details>

**C4. (K2, 1.5.3) ¿Cuál es el MÁXIMO nivel de independence de testing?**

A) Mismo developer testea su propio código.
B) Test lead testea.
C) Equipo interno de testing.
D) Equipo externo independiente.

<details><summary>✅</summary>D. Equipo externo = mayor independencia.</details>

**C5. (K2, 1.4.5) ¿Qué hace el "test designer"?**

A) Ejecuta todos los tests.
B) Diseña test cases y data.
C) Solo planning.
D) Reporta bugs.

<details><summary>✅</summary>B. Test designer role: diseñar test cases específicos.</details>

---

## Cap 2 (7 preguntas)

**C6. (K2, 2.2.1) ¿Cuál describe mejor "component testing"?**

A) Testear interfaces entre módulos.
B) Testear todo el sistema con un usuario real.
C) Testear una pieza aislada, típicamente con mocks.
D) Testear performance.

<details><summary>✅</summary>C. Component = individual isolated unit.</details>

**C7. (K2, 2.2.2) Tests de performance, stress y load son:**

A) Functional testing.
B) Non-functional testing.
C) Component testing.
D) Acceptance testing.

<details><summary>✅</summary>B. Son tipos non-funcionales.</details>

**C8. (K2, 2.1.5) Shift-left mejora:**

A) Solo el manual de usuario.
B) La detección temprana de defects.
C) Solo los nombres de variables.
D) Performance del servidor.

<details><summary>✅</summary>B. Shift-left = detección temprana.</details>

**C9. (K2, 2.1.4) El impacto principal de DevOps en testing es:**

A) Eliminar el rol de QA.
B) Feedback loop rápido, testing continuo.
C) Solo CI.
D) Solo CD.

<details><summary>✅</summary>B. DevOps = feedback loop rápido.</details>

**C10. (K1, 2.1.3) Test-first approaches incluyen:**

A) Waterfall y V-Model.
B) TDD, ATDD, BDD.
C) Solo TDD.
D) Solo mantenimiento.

<details><summary>✅</summary>B. TDD, ATDD, BDD son test-first.</details>

**C11. (K2, 2.2.3) Confirmation testing es precedida por:**

A) Un fix a un defect específico.
B) Una nueva versión.
C) Un sprint planning.
D) Una demo.

<details><summary>✅</summary>A. Confirmation = re-testear DESPUÉS del fix.</details>

**C12. (K2, 2.3.1) Maintenance testing típicamente NO tiene:**

A) Specs actualizados.
B) Bug fixes.
C) Regression test.
D) Ambiente nuevo.

<details><summary>✅</summary>A. Maintenance testing a menudo carece de specs actualizados (porque es post-deployment).</details>

---

## Cap 3 (3 preguntas)

**C13. (K2, 3.1.3) Static testing se diferencia de dynamic porque:**

A) Static es 10x más lento.
B) Static NO ejecuta el software bajo prueba.
C) Dynamic usa personas, static usa máquinas.
D) Static solo se aplica a COBOL.

<details><summary>✅</summary>B. Static = NO execution.</details>

**C14. (K2, 3.2.4) ¿Cuál es la review MÁS estructurada?**

A) Walkthrough.
B) Technical review.
C) Inspection.
D) Informal.

<details><summary>✅</summary>C. Inspection = la más formal.</details>

**C15. (K1, 3.2.3) ¿Quién en una inspection registra defects?**

A) Author.
B) Moderator.
C) Reviewer.
D) Scribe.

<details><summary>✅</summary>D. Scribe registra.</details>

---

## Cap 4 (12 preguntas)

**C16. (K3, 4.2.1) Para password con longitud 8-20 chars, ¿cuántas particiones válidas tiene?**

A) 1.
B) 2.
C) 3.
D) 5.

<details><summary>✅</summary>A. 1 partición válida (8-20). Inválidas: <8, >20. Total 3 particiones pero 1 sola válida.</details>

**C17. (K3, 4.2.2) Para edad válida 18-65, BVA 3-value incluye:**

A) 17, 18, 65, 66.
B) 18, 65.
C) 0, 18, 65, 100.
D) 18, 30, 65.

<details><summary>✅</summary>A. BVA 4-value: 17, 18, 65, 66.</details>

**C18. (K3, 4.2.3) Sistema con entrada: tipo cliente (regular/premium), modo pago (anual/mensual). ¿Máximo combinaciones?**

A) 2.
B) 4.
C) 8.
D) 16.

<details><summary>✅</summary>B. 2 × 2 = 4 reglas posibles.</details>

**C19. (K2, 4.3.2) Branch coverage requiere:**

A) Solo ejecutar el path principal.
B) Cada decisión evaluada a true Y false.
C) Un solo test completo.
D) Specs detalladas.

<details><summary>✅</summary>B. Cada decisión = ambos sentidos.</details>

**C20. (K3, 4.5.3) ATDD vs TDD — ¿cuál NO es correcto?**

A) TDD = developer escribe unit tests.
B) ATDD = equipo escribe acceptance tests.
C) ATDD típicamente va antes de TDD en el ciclo.
D) TDD puede no tener tests automatizados.

<details><summary>✅</summary>D. TDD típicamente SÍ tiene tests automatizados.</details>

**C21. (K2, 4.4.2) Exploratory testing genera charter con:**

A) Lista de tests.
B) Objetivo + timebox + alcance.
C) Test automation framework.
D) Diagrama UML.

<details><summary>✅</summary>B. Charter = objetivo + timebox + alcance.</details>

**C22. (K2, 4.5.1) ¿Cuál NO es critério INVEST?**

A) Independent.
B) Negotiable.
C) Working software.
D) Testable.

<details><summary>✅</summary>C. INVEST = Independent, Negotiable, Valuable, Estimable, Small, Testable.</details>

**C23. (K2, 4.5.2) Given-When-Then es:**

A) Lenguaje de programación.
B) Formato de acceptance criteria.
C) Requisito de hardware.
D) Herramienta ISTQB.

<details><summary>✅</summary>B. Formato para escribir acceptance criteria, base de BDD.</details>

**C24. (K2, 4.3.1) 100% statement coverage significa:**

A) Todos los statements ejecutaron.
B) Todos los bugs encontrados.
C) Sistema sin defectos.
D) Branch coverage completo.

<details><summary>✅</summary>A. Statement coverage = líneas ejecutadas.</details>

**C25. (K2, 4.4.1) Error guessing es valuable porque:**

A) Es formal.
B) El tester usa experiencia de bugs pasados.
C) Es matemáticamente perfecto.
D) Tiene métricas confiables.

<details><summary>✅</summary>B. Usa experiencia.</details>

**C26. (K2, 4.2.4) Un state diagram modela:**

A) Flujo de trabajo del proyecto.
B) Estados del sistema + transiciones + eventos.
C) Solo clases.
D) Solo eventos.

<details><summary>✅</summary>B. Estados + eventos + transiciones.</details>

**C27. (K2, 4.1.1) ¿Cuál describe mejor "epistemic techniques" vs "experience-based"?**

A) Son iguales.
B) Técnicas formales (black/white) vs intuición.
C) Experience-based son superiores.
D) Black-box es más fuerte.

<details><summary>✅</summary>B. Formal techniques (EP, BVA) vs experience-based (intuición).</details>

---

## Cap 5 (8 preguntas)

**C28. (K1, 5.1.6) Test pyramid: integración abajo de UI?**

A) Sí, UI es lo más bajo.
B) No, UI es arriba (pocos), unit abajo (muchos).
C) Todos en una capa.
D) Sin layers.

<details><summary>✅</summary>B. UI = pocos (arriba), unit = muchos (abajo).</details>

**C29. (K1, 5.2.1) Likelihood x Impact ejemplo: Med likelihood + High impact = ?**

A) Low risk.
B) Medium risk.
C) High risk.
D) Critical (no existe).

<details><summary>✅</summary>C. 2x3 = 6 (alto en la matriz típica).</details>

**C30. (K2, 5.2.2) Un riesgo que afecta al PRODUCTO final, NO al proyecto, es:**

A) Project risk.
B) Product risk.
C) Failure risk.
D) Quality management risk.

<details><summary>✅</summary>B. Product risk.</details>

**C31. (K2, 5.1.3) ¿Exit criteria incluye típicamente?**

A) Cobertura alcanzada + defects cerrados.
B) Solo defects cerrados.
C) Solo el final del sprint.
D) Solo para managers.

<details><summary>✅</summary>A. Exit = coverage + defects closed.</details>

**C32. (K1, 5.3.1) ¿Métrica clave para test progress?**

A) Cantidad de developers.
B) % test cases ejecutados.
C) Velocidad de internet.
D) Versión de Python.

<details><summary>✅</summary>B. % ejecutados = principal.</details>

**C33. (K3, 5.5.1) Un componente falla con crash en producción = severity:**

A) Low.
B) Medium.
C) High.
D) None.

<details><summary>✅</summary>C. Crash = alta.</details>

**C34. (K2, 5.2.4) "Transfer" el riesgo es:**

A) Eliminarlo.
B) Pasarlo a otro (seguro, outsourcing).
C) Aceptarlo.
D) Negarlo.

<details><summary>✅</summary>B. Transfer = pasarlo a otra parte.</details>

**C35. (K2, 5.1.7) Testing quadrants: ¿qué es Q1?**

A) Security.
B) Performance.
C) Functional business-facing (UAT, exploratory).
D) Component testing.

<details><summary>✅</summary>C. Q1 = functional + business-facing.</details>

---

## Cap 6 (5 preguntas)

**C36. (K1, 6.2.1) ¿Cuál NO es beneficio de automation?**

A) Velocidad.
B) Repetibilidad.
C) Eliminar planning.
D) Coverage.

<details><summary>✅</summary>C. Planning no es eliminado.</details>

**C37. (K1, 6.2.1) ¿Riesgo #1 de automation?**

A) Velocidad excesiva.
B) Mantenimiento alto de scripts.
C) Coverage perfecto.
D) Sin errors humanos.

<details><summary>✅</summary>B. Mantenimiento = principal.</details>

**C38. (K2, 6.1.1) ¿Cómo se llama una herramienta de gestión de testing?**

A) Selenium.
B) TestRail.
C) JMeter.
D) ESLint.

<details><summary>✅</summary>B. TestRail = test management.</details>

**C39. (K2, 6.1.1) ¿Cuál es una herramienta de load testing?**

A) Selenium.
B) Postman.
C) JMeter / k6.
D) ESLint.

<details><summary>✅</summary>C. JMeter / k6 = load testing.</details>

**C40. (K2, 6.1.1) Selenium WebDriver es para:**

A) Static analysis.
B) UI test automation.
C) Management.
D) Performance del código.

<details><summary>✅</summary>B. UI test automation.</details>

---

## 📝 Scoring

| Score | Acción |
|---|---|
| ≥80% (32+) | Excelente |
| 65-79% (26-31) | Listo |
| 50-64% (20-25) | Reforzar |
| <50% | Retomar plan |

## ✏️ Para el grupo

Después de 3 sample exams + 6 quizzes, ya tenés una base sólida.
Si sacaste ≥65% consistente → rendí el examen oficial.
