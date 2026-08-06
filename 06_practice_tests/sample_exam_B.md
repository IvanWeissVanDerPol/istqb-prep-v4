# Sample Exam B — ISTQB CTFL v4.0.1 (40 preguntas)

> Variación del Sample Exam A. Mismo syllabus, preguntas diferentes, misma dificultad.
> Tiempo: 60 min cronometrados. Mínimo 65% = 26/40.

---

## Cap 1 (5 preguntas)

**B1. (K2, 1.2.3) Un usuario reporta que el sistema borró todos sus datos después de una actualización fallida. En términos ISTQB, este evento es un:**

A) Error.
B) Defect.
C) Failure.
D) Root cause.

<details><summary>✅</summary>C. Failure = evento observable (usuario lo ve). Defect = imperfección en código. Error = mistake humano. Root cause = razón fundamental.</details>

**B2. (K2, 1.3.1) "Exhaustive testing is impossible" significa:**

A) Que solo se testean casos críticos.
B) Que se pueden testear todas las combinaciones posibles si se dedica tiempo.
C) Que el número de combinaciones es tan alto que es imposible testearlo todo.
D) Que ISTQB no recomienda testing completo.

<details><summary>✅</summary>C. Los defectos cluster, las combinaciones son infinitas.</details>

**B3. (K2, 1.4.1) ¿En qué actividad se construyen los test cases a partir de test conditions?**

A) Test implementation.
B) Test design.
C) Test analysis.
D) Test completion.

<details><summary>✅</summary>B. Test design convierte test conditions en test cases concretos.</details>

**B4. (K1, 1.5.2) El "whole team approach" significa que:**

A) Solo el equipo de QA es responsable.
B) El equipo entero (dev + QA + business) comparte la responsabilidad de calidad.
C) Cada uno testea lo suyo independientemente.
D) Solo developers y QA.

<details><summary>✅</summary>B. Whole team = TODOS son responsables.</details>

**B5. (K2, 1.4.4) El valor principal de mantener trazabilidad es:**

A) Permitir automatización.
B) Asegurar cobertura y entender impacto de cambios.
C) Reducir el número de tests.
D) Cumplir regulatoriamente nada más.

<details><summary>✅</summary>B. Trazabilidad sirve para impacto y cobertura.</details>

---

## Cap 2 (7 preguntas)

**B6. (K1, 2.1.3) ¿Cuál es un test-first approach?**

A) Waterfall.
B) TDD (Test-Driven Development).
C) Maintenance testing.
D) Regression testing.

<details><summary>✅</summary>B. TDD es test-first. ATDD, BDD también.</details>

**B7. (K2, 2.2.1) ¿Cuál describe mejor "system testing"?**

A) Testea una unidad aislada.
B) Testea interfaces entre componentes.
C) Testea el sistema integrado completo.
D) Lo hace el usuario final.

<details><summary>✅</summary>C. System = sistema integrado completo. Independent.</details>

**B8. (K2, 2.1.5) "Shift-left" se logra con:**

A) Más testing al final.
B) Testing temprano en el SDLC, idealmente antes del código.
C) Eliminar testing.
D) Tests separados por geografía.

<details><summary>✅</summary>B. Shift-left = testing temprano.</details>

**B9. (K2, 2.2.2) "Flexibility" (ISO 25010:2023) reemplazó a:**

A) Usability.
B) Compatibility.
C) Portability.
D) Maintainability.

<details><summary>✅</summary>C. Portability → Flexibility en ISO 25010:2023.</details>

**B10. (K2, 2.2.3) ¿Cuál es la diferencia entre confirmation y regression?**

A) Son iguales.
B) Confirmation: bug específico fixed. Regression: cambios no rompieron otras cosas.
C) Confirmation se hace antes, regression después.
D) Regression es opcional.

<details><summary>✅</summary>B. Re-testear = confirmation. Suite completa = regression.</details>

**B11. (K1, 2.1.6) Las "retrospectives" son:**

A) Una herramienta ISTQB.
B) Mecanismo para reflexionar y mejorar el proceso al final de cada iteración.
C) Solo en waterfall.
D) Igual a post-mortem.

<details><summary>✅</summary>B. Retros = mejora continua.</details>

**B12. (K2, 2.3.1) Maintenance testing es disparado por:**

A) Migration, retirement, nuevos environments.
B) Solo cuando hay bugs.
C) Solo anual.
D) Solo post-launch.

<details><summary>✅</summary>A. Migration, retirement, nuevos environments.</details>

---

## Cap 3 (3 preguntas)

**B13. (K2, 3.1.3) ¿Cuál describe mejor static testing?**

A) Ejecuta el código y observa resultados.
B) NO ejecuta el código; usa reviews o análisis sintáctico.
C) Lo mismo que dynamic testing.
D) Solo aplica a scripts.

<details><summary>✅</summary>B. Static = NO execution.</details>

**B14. (K2, 3.2.4) ¿Qué tipo de review es dirigida por el autor?**

A) Inspection.
B) Walkthrough.
C) Technical review.
D) Peer review.

<details><summary>✅</summary>B. Walkthrough = lidera el autor. Inspection = lidera moderator.</details>

**B15. (K1, 3.2.3) ¿Cuál NO es rol en una review?**

A) Author.
B) Moderator.
C) Reviewer.
D) Procurador.

<details><summary>✅</summary>D. Roles: Author, Moderator, Reviewer, Scribe, Manager.</details>

---

## Cap 4 (12 preguntas)

**B16. (K3, 4.2.1) ¿Cuántas particiones equivalentes tiene un campo edad que acepta 0-150?**

A) 1.
B) 3.
C) 5.
D) Infinito.

<details><summary>✅</summary>B. 3 particiones: inválida (<0), válida (0-150), inválida (>150). Opcionalmente subdividir 0-150 en grupos.</details>

**B17. (K3, 4.2.2) Para campo entero 10-20, ¿qué valores son típicos BVA?**

A) 10, 15, 20.
B) 9, 10, 20, 21.
C) 5, 10, 20, 25.
D) Solo 10 y 20.

<details><summary>✅</summary>B. BVA clásico: 9 (b-1), 10 (b), 20 (a), 21 (a+1).</details>

**B18. (K3, 4.2.3) ¿Cuántas reglas posibles tienen 4 condiciones booleanas?**

A) 4.
B) 8.
C) 16.
D) 32.

<details><summary>✅</summary>C. 2^4 = 16 reglas posibles.</details>

**B19. (K2, 4.3.2) Branch coverage es más fuerte que statement porque:**

A) Mide líneas.
B) Cada decisión se evalúa en true Y false.
C) Es automatizada.
D) Es manual.

<details><summary>✅</summary>B. Branch = cada decisión evaluada en ambos sentidos.</details>

**B20. (K2, 4.4.2) Exploratory testing usa:**

A) Specs detalladas previas.
B) Charter + timebox + notas (descubrir mientras testeas).
C) Solo tests manuales.
D) Solo para bugs visuales.

<details><summary>✅</summary>B. Charter-guided, timeboxed, no full specs.</details>

**B21. (K3, 4.5.3) ATDD significa:**

A) Automatic Test-Driven Development.
B) Acceptance Test-Driven Development — equipo 3 amigos escribe acceptance tests ANTES del código.
C) Acceptance Trend Analysis.
D) Abstract Test Definition Document.

<details><summary>✅</summary>B. ATDD = 3 amigos (dev + tester + business) escribiendo acceptance tests ANTES del código.</details>

**B22. (K2, 4.5.1) Una buena user story en formato standard es:**

A) Un párrafo técnico detallado.
B) "Como <rol>, quiero <acción>, para <beneficio>".
C) Código UML.
D) Lista de bullet points.

<details><summary>✅</summary>B. Formato INVEST.</details>

**B23. (K2, 4.5.2) Acceptance criteria pueden ser escritos en:**

A) Solo Given-When-Then.
B) Given-When-Then, Checklist, o Scenario.
C) Solo binary.
D) Solo diagramas.

<details><summary>✅</summary>B. 3 opciones oficiales.</details>

**B24. (K2, 4.1.1) ¿Cuál NO es black-box?**

A) EP.
B) BVA.
C) Statement testing.
D) Decision table.

<details><summary>✅</summary>C. Statement testing es white-box.</details>

**B25. (K2, 4.4.1) Error guessing se basa en:**

A) Specs rigurosas.
B) Experiencia e intuición del tester.
C) Una fórmula matemática.
D) Automated tools.

<details><summary>✅</summary>B. Error guessing = experience-based, usa intuición.</details>

**B26. (K2, 4.2.4) En el state diagram, ¿qué es un evento?**

A) El estado del sistema.
B) Algo que dispara una transición.
C) La acción resultante.
D) La lista de defects.

<details><summary>✅</summary>B. Evento = disparador de una transición.</details>

**B27. (K2, 4.3.1) Statement coverage mide:**

A) % branches ejecutados.
B) % statements ejecutados al menos una vez.
C) % decisiones.
D) % requisitos cubiertos.

<details><summary>✅</summary>B. Statement coverage = líneas ejecutadas.</details>

---

## Cap 5 (8 preguntas)

**B28. (K1, 5.1.6) Test pyramid (NUEVO) tiene la mayoría de tests en:**

A) UI/E2E arriba.
B) API integration.
C) Unit tests abajo.
D) Manuales.

<details><summary>✅</summary>C. ~70% unit, ~20% integration, ~10% E2E.</details>

**B29. (K1, 5.2.1) Risk level = likelihood × impact. Para likelihood=High, impact=Medium, el level es:**

A) Low.
B) Medium.
C) High.
D) Critical.

<details><summary>✅</summary>C. Alto x medio = alto.</details>

**B30. (K2, 5.2.2) Un riesgo histórico en código legacy es un:**

A) Project risk.
B) Product risk.
C) Test risk.
D) Solo un bug.

<details><summary>✅</summary>B. Product risk = afecta calidad del producto.</details>

**B31. (K2, 5.1.3) Entry y Exit criteria son:**

A) Sinónimos.
B) Entry ANTES de empezar; exit ANTES de cerrar.
C) Solo aplican a agile.
D) Solo aplican a manual.

<details><summary>✅</summary>B. Entry ≠ Exit.</details>

**B32. (K1, 5.3.1) ¿Cuál NO es un métrica típica de testing?**

A) % test cases ejecutados.
B) % pass rate.
C) Cantidad de developers.
D) Defects found/resolved ratio.

<details><summary>✅</summary>C. No es métrica de testing.</details>

**B33. (K3, 5.5.1) Un bug que causa pérdida de datos tiene:**

A) Low severity.
B) Medium severity.
C) High severity.
D) Sin severity.

<details><summary>✅</summary>C. Pérdida de datos = high severity.</details>

**B34. (K2, 5.2.4) Mitigar un riesgo significa:**

A) Eliminarlo.
B) Acciones para reducir la probabilidad o impacto.
C) Aceptar la pérdida.
D) Ignorarlo.

<details><summary>✅</summary>B. Mitigate = acciones para reducir.</details>

**B35. (K2, 5.1.7) Testing quadrants (NUEVO v4.0) divide por:**

A) Levels vs types.
B) Business-facing vs technology-facing × functional vs non-functional.
C) Manual vs auto.
D) Static vs dynamic.

<details><summary>✅</summary>B. 2x2 matrix.</details>

---

## Cap 6 (5 preguntas)

**B36. (K1, 6.2.1) ¿Cuál es un beneficio de automation?**

A) Eliminar bugs.
B) Repetibilidad y velocidad.
C) Reemplazar todo.
D) Sin mantenimiento.

<details><summary>✅</summary>B. Velocidad + repetición.</details>

**B37. (K1, 6.2.1) ¿Cuál es un riesgo de automation?**

A) Tests más rápidos.
B) Mantenimiento alto y falsa sensación 100%.
C) Sin skills especiales.
D) Sin curva de aprendizaje.

<details><summary>✅</summary>B. Mantenimiento = #1 riesgo.</details>

**B38. (K2, 6.1.1) ¿Cuál NO es test tool?**

A) Selenium.
B) Postman.
C) SonarQube.
D) WhatsApp.

<details><summary>✅</summary>D. WhatsApp no es una test tool.</details>

**B39. (K2, 6.1.1) ¿Herramienta de static analysis?**

A) Selenium WebDriver.
B) SonarQube.
C) JMeter.
D) Postman.

<details><summary>✅</summary>B. SonarQube es static analysis.</details>

**B40. (K2, 6.1.1) ¿Test execution tool típica?**

A) Linter.
B) Selenium / Playwright.
C) TestRail.
D) JMeter.

<details><summary>✅</summary>B. Selenium/Playwright ejecutan tests automáticamente.</details>

---

## 📝 Scoring

| Score | Acción |
|---|---|
| ≥32 (80%) | Excelente, listo |
| 26-31 (65-79%) | Aprobado, repaso final |
| 20-25 (50-64%) | Repaso |
| <20 (<50%) | Retoma el plan de estudio |

## 🔍 Análisis

| Cap | Obtuviste / Total | Porcentaje |
|-----|-------------------|-----------|
| 1 | /5 | % |
| 2 | /7 | % |
| 3 | /3 | % |
| 4 | /12 | % |
| 5 | /8 | % |
| 6 | /5 | % |
