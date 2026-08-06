# ⭐ Hard Mode Quiz — Cap 4 & 5 (los más pesados)

> **20 preguntas avanzadas con escenarios** — la gente falla acá más que en cualquier otro cap.
> Meta: **≥70% (14/20)** para considerar que estás listo para el examen real.
> Tiempo: 35 min cronometrados.

---

## Cap 4 — K3 aplicado (10 preguntas)

**Q1. (LO 4.2.1, K3) Aplicá EP al campo "Edad" que acepta rango válido 18-65 y rechaza mayores de 65 (tercera edad no es target).**

¿**Cuántas particiones equivalentes** hay?

A) 2 (válida, inválida).
B) 3 (menor de 18, 18-65, mayor de 65).
C) 4 (menor de 18, 18-65, mayor de 65, edad negativa).
D) 5 (negativa, 0-17, 18-65, 66-100, >100).

<details><summary>✅ Respuesta</summary>B. 3 particiones: inválida 1 (<18), válida (18-65), inválida 2 (>65). EP elige UN valor por partición = 3 tests.</details>

**Q2. (LO 4.2.2, K3) Para campo "Edad" válido 18-65, BVA 2-value:**

A) 17, 18.
B) 17, 18, 65, 66.
C) 18, 65.
D) 16, 17, 18, 65, 66, 67.

<details><summary>✅ Respuesta</summary>B. BVA 2-value clásico: b-1, b (límite inferior ± 1) + a, a+1 (límite superior ± 1). Para 18-65: 17, 18, 65, 66.</details>

**Q3. (LO 4.2.2, K3) ¿Cuál es la diferencia entre BVA 2-value y 3-value?**

A) 2-value testea dentro y fuera del límite; 3-value testea solo los límites.
B) 2-value: b-1, b, a, a+1; 3-value: b-1, b, b+1, a-1, a, a+1.
C) 2-value requiere más tests que 3-value.
D) No hay diferencia, son sinónimos.

<details><summary>✅ Respuesta</summary>B. 2-value es clásico (b-1, b / a, a+1). 3-value es extendido (incluye b+1 y a-1 para más cobertura). 3-value = más tests.</details>

**Q4. (LO 4.2.3, K3) Construí una decision table para: "Login exitoso SI usuario válido AND password válido AND 2FA OK". ¿Cuántas reglas mínimas?**

A) 3 reglas (todas OK).
B) 8 reglas (2^3).
C) 4 reglas (success + 3 fails).
D) 7 reglas (success + 6 fails, menos la all-fail).

<details><summary>✅ Respuesta</summary>C. Con 3 conditions binarias hay 8 combinaciones posibles, pero podemos colapsar: 1 success (all OK) + 3 fails (1 fail each) = 4 reglas mínimas. La regla "todo mal" no aporta porque cualquier fail individual cubre el caso.</details>

**Q5. (LO 4.2.4, K2) ¿Cuál es la diferencia entre "state transition diagram" v3.1 y "state diagram" v4.0?**

A) No hay diferencia.
B) Es solo cambio de nombre (semántico).
C) v4.0 incluye invalid transitions; v3.1 no.
D) v4.0 usa UML; v3.1 usa flowcharts.

<details><summary>✅ Respuesta</summary>B. v4.0 cambió "state transition diagram" → "state diagram" (nombre más usado en CS, consistente con model-based testing).</details>

**Q6. (LO 4.3.2, K2) Branch coverage de un código con 3 ifs sin else requiere:**

A) 1 test (cubre todo).
B) 2 tests (cubrir true y false de cada if).
C) 3 tests (uno por if).
D) 4 tests mínimo (3 ifs + default path).

<details><summary>✅ Respuesta</summary>D. Para 100% branch coverage con 3 ifs sin else, hay 4 paths posibles (cada if puede ser true o false). Mínimo 4 tests. Si hay else, los caminos cambian.</details>

**Q7. (LO 4.5.3, K3) ¿Cuál es la diferencia clave entre TDD y ATDD?**

A) TDD es para QA, ATDD para devs.
B) TDD = unit tests escritos por dev; ATDD = acceptance tests escritos por equipo (dev+test+business).
C) TDD es Java, ATDD es Python.
D) TDD no tiene tests automatizados.

<details><summary>✅ Respuesta</summary>B. TDD (Test-Driven Development) = unit tests ANTES del código, escritos por el developer. ATDD (Acceptance Test-Driven Development) = acceptance tests ANTES del código, escritos por el equipo (3 amigos).</details>

**Q8. (LO 4.5.1, K2) ¿Qué significa la "I" en INVEST?**

A) International.
B) Interactive.
C) Independent.
D) Iterative.

<details><summary>✅ Respuesta</summary>C. INVEST = Independent, Negotiable, Valuable, Estimable, Small, Testable. Criterios para buena user story.</details>

**Q9. (LO 4.2.4, K2) Para un ATM con estados {Idle, CardInserted, PINEntered, Authenticated, Transaction, End}, ¿cuál es el MÍNIMO de tests para 0-switch coverage si hay 7 transiciones?**

A) 3 tests.
B) 5 tests.
C) 7 tests (1 por transición).
D) 14 tests (todas las combinaciones).

<details><summary>✅ Respuesta</summary>C. 0-switch coverage = cada transición ejercitada al menos una vez. 7 transiciones = 7 tests mínimo.</details>

**Q10. (LO 4.2.1, K3) Si las particiones inválidas se testean JUNTAS con válidas, ¿qué riesgo aparece?**

A) Tests más lentos.
B) **Defect masking** — un failure oculta otro.
C) Mejor cobertura.
D) Sin riesgo.

<details><summary>✅ Respuesta</summary>B. Defect masking = cuando el primer failure impide detectar otros. Por eso v4.0 recomienda testear particiones inválidas **en isolation**.</details>

---

## Cap 5 — K2/K3 management (10 preguntas)

**Q11. (LO 5.2.1, K1) Risk level se calcula con:**

A) Sum (likelihood + impact).
B) Likelihood × impact.
C) Solo likelihood.
D) Solo impact.

<details><summary>✅ Respuesta</summary>B. Risk = likelihood × impact. Producto, no suma.</details>

**Q12. (LO 5.2.2, K2) Un código legacy sin tests automáticos es un ejemplo de:**

A) Project risk.
B) Product risk (calidad del producto).
C) Schedule risk.
D) Cost risk.

<details><summary>✅ Respuesta</summary>B. Product risk = afecta calidad del producto. El código legacy sin tests = riesgo de calidad = product risk.</details>

**Q13. (LO 5.5.1, K3) Bug cosmético en homepage de e-commerce con 10K visitas/día. ¿Severidad y prioridad típicas?**

A) High severity, low priority.
B) Low severity, high priority.
C) High severity, high priority.
D) Low severity, low priority.

<details><summary>✅ Respuesta</summary>B. Cosmético = low severity (no afecta funcionalidad core). Homepage con muchas visitas = high priority (impacta imagen y ventas). Caso clásico de separation.</details>

**Q14. (LO 5.1.3, K2) Entry y Exit criteria son:**

A) Sinónimos.
B) Entry ANTES de empezar testing; exit ANTES de cerrar.
C) Entry al final, exit al inicio.
D) Solo para agile.

<details><summary>✅ Respuesta</summary>B. Entry ≠ Exit. v4.0.1 aclara explícitamente que NO son sinónimos.</details>

**Q15. (LO 5.2.4, K2) Pasamos el riesgo de falla del servidor a un proveedor cloud. Esto es:**

A) Accept.
B) Mitigate.
C) Transfer.
D) Avoid.

<details><summary>✅ Respuesta</summary>C. Transfer = pasamos el riesgo a otro. Outsourcing/seguro = transfer.</details>

**Q16. (LO 5.1.6, K1) Test pyramid (NUEVO v4.0) tiene mayoría de tests en:**

A) UI/E2E.
B) Integration.
C) Unit.
D) Manual.

<details><summary>✅ Respuesta</summary>C. ~70% unit, ~20% integration, ~10% E2E.</details>

**Q17. (LO 5.1.7, K2) ¿Cuál describe mejor "testing quadrants"?**

A) Diagrama de 4 estados.
B) 2x2 matrix (business-facing/tech × functional/non-functional).
C) 4 fases de test.
D) Lista de skills.

<details><summary>✅ Respuesta</summary>B. Testing quadrants = 2x2 matrix (NUEVO en v4.0).</details>

**Q18. (LO 5.5.1, K3) ¿Cuál de estos NO es campo obligatorio de un defect report?**

A) ID, Title.
B) Severity, Priority.
C) Description, Steps to reproduce.
D) Costo estimado del fix.

<details><summary>✅ Respuesta</summary>D. Costo del fix NO es campo típico. ISTQB recomienda los otros (ID, title, severity, priority, etc.).</details>

**Q19. (LO 5.3.2, K2) ¿Cuál describe mejor "test progress report"?**

A) Reporte final al cerrar.
B) Reporte periódico durante testing.
C) Reporte solo para managers.
D) Reporte solo al final del sprint.

<details><summary>✅ Respuesta</summary>B. Progress report = ongoing status. Completion report = al cerrar (lessons learned).</details>

**Q20. (LO 5.1.5, K3) ¿Cuál describe mejor "test case prioritization"?**

A) Decoración de reports.
B) Determinar el ORDEN de ejecución según criterio (riesgo/cobertura).
C) Eliminar tests.
D) Asignar developers.

<details><summary>✅ Respuesta</summary>B. Prioritization = orden de ejecución. K3 apply.</details>

---

## 📊 Scoring

| Score | Acción |
|---|---|
| **18-20 (90%+)** | Excelente. Pasás el examen. |
| **16-17 (80%+)** | Muy bien. Listo. |
| **14-15 (70%+)** | OK. Rendí, pero repasá puntos débiles. |
| **12-13 (60-65%)** | Riesgo de fail. Estudiá más Cap 4 y 5. |
| **<12** | NO RENDIR. Volvé al plan de estudio. |

## 🎯 Si fallaste más de 3 en Cap 4 o 5:

| Si fallaste en | Repasá |
|---|---|
| 1-3 (EP) | Cap 4.2.1 + ejercitar con lápiz |
| 4 (decision table) | Cap 4.2.3 + construir 3-5 tablas a mano |
| 5-6 (BVA/coverage) | Cap 4.2.2 + 4.3.2 + ejercitar coverage manual |
| 7 (ATDD) | Cap 4.5.3 (NUEVO v4.0) |
| 8 (INVEST) | Cap 4.5.1 |
| 9 (state diagram) | Cap 4.2.4 |
| 10 (defect masking) | Cap 4.2.1 |
| 11-13 (risk basics) | Cap 5.2.1 + 5.2.2 |
| 14 (severity/priority) | Cap 5.5.1 |
| 15 (entry/exit) | Cap 5.1.3 |
| 16-17 (response, pyramid) | Cap 5.2.4 + 5.1.6 |
| 18 (defect report fields) | Cap 5.5.1 + preparar 3 reports |
| 19-20 (progress/completion) | Cap 5.3.2 |
