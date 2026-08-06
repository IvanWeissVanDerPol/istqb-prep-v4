# 📖 Glosario CTFL v4.0.1 — Términos NUEVOS y CRÍTICOS

> Glosario complementario — **no reemplaza** el syllabus completo.
> Solo término CLAVES + cambios desde v3.1.

---

## 🆕 TÉRMINOS NUEVOS v4.0.1 (importantes para el examen)

### A

**Acceptance criteria (NUEVO énfasis):** condiciones que debe cumplir un componente para ser aceptado por el usuario. Formatos: Given-When-Then, checklist, scenario.

**Acceptance Test-Driven Development (ATDD):** metodología donde el equipo (developer+tester+business) escribe acceptance tests ANTES del código.

**Alpha testing:** testing en el sitio del developer (sin cliente).

**AST:** ver "Acceptance test-driven development"

### B

**Backward compatibility:** capacidad de coexistir con versiones previas.

**BDD (Behavior-Driven Development):** derivar tests de requisitos usando ejemplos en formato Given-When-Then. Test-first + colaboración.

**Beta testing:** testing en el sitio del cliente (no del developer).

**Bug mask / defect masking:** cuando un failure en una partición oculta la causa de otro test. Razón para testear inválidos en isolation (v4.0.1).

### C

**Charter (exploratory):** descripción breve de qué se va a explorar en una sesión de exploratory testing.

**Collaboration-based test approach (NUEVO v4.0):** testing que depende de la colaboración entre devs, testers y business (e.g., user stories + acceptance criteria + ATDD).

**Compatibility:** capacidad del producto de coexistir con otros productos en el mismo ambiente. ISO 25010:2023.

**Component integration testing (NUEVO énfasis):** testing de cómo un componente interactúa con infraestructura externa (DB, file system, etc.). Diferente de integration testing (entre componentes).

**Confirmation testing:** testing que confirma que un defect específico fue corregido.

**Configuration management:** disciplina de trackear y controlar cambios.

### D

**Data-driven testing:** testing donde los datos de prueba están en archivos externos, separados de los scripts.

**Defect report:** documento describiendo un defecto.

**DevOps (NUEVO v4.0):** combinación de desarrollo y operaciones que impacta testing (integración continua, despliegue continuo, feedback loop).

**Documentation → work products (CAMBIO DE VOCABULARIO):** "documentation" se reemplazó por "work products" en todo el syllabus v4.0.

### E

**Entry criteria:** condiciones que deben cumplirse antes de empezar una actividad de testing.

**Equivalence partition:** grupo de valores para los cuales se asume el mismo comportamiento.

**Exit criteria:** condiciones que deben cumplirse antes de declarar una actividad de testing como terminada. (NO es sinónimo de entry criteria — v4.0.1 lo aclara explícitamente)

**Exploratory testing:** testing simultáneo de aprendizaje, diseño y ejecución.

### F

**Failure:** evento en el que un componente/sistema no cumple sus funciones requeridas.

**Flexibility (CAMBIO v4.0 — antes "Portability"):** capacidad del producto de ser transferido de un ambiente a otro. ISO 25010:2023.

**Functional testing:** testing que verifica que las funciones del sistema operan correctamente.

### G

**Given-When-Then:** formato Given [precondición], When [acción], Then [resultado esperado]. Para acceptance criteria y BDD.

### H

**Hexagonal:** ver "user stories" (formato).

### I

**Independence of testing (CAMBIO DE VOCABULARIO):** antes "test independence" o "independence of testing". Separa el testing del desarrollo.

**Integration testing:** testing de interfaces entre componentes/sistemas.

**Interaction capability (CAMBIO v4.0 — antes "Usability"):** capacidad del producto de ser usado por usuarios específicos para alcanzar objetivos específicos. ISO 25010:2023.

**INVEST (NUEVO v4.0 — implícito):** criterios para buena user story: Independent, Negotiable, Valuable, Estimable, Small, Testable.

### J

**Jira-style issues:** no oficial, pero defectos típicamente registrados en herramientas tipo Jira.

### K

**K-level:** nivel cognitivo de un LO en el syllabus:
- K1 = reconocer/recordar
- K2 = explicar/distinguir
- K3 = usar/aplicar en contexto

### L

**Learning objective (LO):** objetivo de aprendizaje del syllabus.

**Lifelong certification:** algunas certificaciones son lifetime (no expiran). Verificar con el Member Board.

### M

**Maintenance testing:** testing durante el mantenimiento (después del primer release).

### N

**Non-functional testing:** testing de atributos no funcionales (performance, security, etc.).

### P

**Performance efficiency (ISO 25010:2023):** capacidad del producto de cumplir requisitos de tiempo y eficiencia.

**Project risk:** riesgo que afecta el schedule/coste/calidad del proyecto (no del producto).

**Product risk:** riesgo que afecta la calidad del producto final.

**Prioritization (de test cases):** ordenar tests según criterio (riesgo, cobertura, etc.).

### Q

**Quality assurance (QA):** enfoque planificado y proactivo para asegurar que procesos → calidad.

**Quadrants (testing quadrants, NUEVO v4.0):** matriz 2x2 que cruza niveles (business-facing vs technology-facing) con tipos (functional vs non-functional).

### R

**Regression testing:** testing después del cambio para verificar que todo sigue funcionando.

**Risk level:** combinación de likelihood × impact.

**Risk-based testing:** testing dirigido por análisis de riesgos.

### S

**Safety (NUEVO ISO 25010:2023):** capacidad del producto de operar sin causar daño a personas, datos, etc.

**Session-based testing:** exploratory testing estructurado por charter + timebox + notas.

**Shift left (NUEVO v4.0):** mover testing lo más temprano posible en el SDLC.

**State diagram (CAMBIO v4.0 — antes "state transition diagram"):** modelo que muestra estados, transiciones, eventos y acciones.

**Static testing:** testing sin ejecutar el software (revisiones, análisis estático).

### T

**TDD (Test-Driven Development):** developer escribe tests unitarios ANTES del código.

**Test analysis:** actividad que identifica condiciones testeables desde test basis.

**Test case prioritization (NUEVO énfasis v4.0):** ordenar los tests según criterio.

**Test closure (test completion):** actividad que consolida testing, hace summary report.

**Test completion report:** reporte final al cerrar testing. SINÓNIMO de **test summary report** (pero diferente de **test progress report**).

**Test control:** acción correctiva para mantener/mejorar testing.

**Test completion reporting (NUEVA terminología v4.0):** reporte que documenta testing terminado.

**Test design:** actividad de derivar test cases desde test conditions.

**Test execution:** correr tests y registrar resultados.

**Test implementation:** preparar y verificar test suites (procedimientos, orden).

**Test item:** (CAMBIO v4.0 — antes "test object") pieza de software que se testea.

**Test monitoring:** actividad que verifica progreso vs plan. Distinto de "test control".

**Test objective:** razón o propósito del testing.

**Test plan:** documento describiendo scope, approach, resources, schedule.

**Test planning:** actividad de definir el test plan.

**Test policy:** objetivos de testing de alto nivel en una organización.

**Test progress report:** reporte periódico sobre avance del testing. Distinto de "test completion report".

**Test progress reporting (NUEVA terminología v4.0):** "reporting on test progress" → formalizado.

**Test pyramid (NUEVO v4.0):** representación piramidal de la proporción de tests en distintos niveles (muchos unit, menos E2E).

**Test reporting:** actividad de generar reports sobre testing.

**Test step (CAMBIO — antes "step"):** acción individual dentro de un test case.

**Test strategy:** descripción de alto nivel del testing a aplicar.

**Test techniques:** métodos para diseñar y seleccionar test cases.

### U

**Unit test framework:** herramienta para escribir/correr tests unitarios (pytest, JUnit, etc.).

**User story (NUEVO énfasis v4.0):** descripción breve de funcionalidad desde perspectiva del usuario, formato "Como... quiero... para...".

### V

**Verification:** confirmar que el producto cumple las especificaciones (vs validation).

**Validation:** confirmar que el producto cumple las necesidades del usuario.

**Velocity (no oficial ISTQB):** concepto ágil, velocidad de entrega por sprint.

### W

**Walkthrough:** tipo de review informal, dirigida por el autor.

**White-box testing (CAMBIO — antes "white box testing"):** testing basado en estructura interna.

**Whole team approach (K1, antes en Cap 1):** calidad es responsabilidad de todo el equipo, no solo testers.

**Wideband Delphi (NUEVO mención v4.0):** técnica de estimación iterativa con expertos anónimos.

**Work products (CAMBIO mayor — antes "documentation" o "test documentation"):** cualquier artefacto producido durante el SDLC que puede ser revisado.

---

## 🔥 LAS 30 PREGUNTAS MÁS PROBABLES (TOP)

Si solo pudieras memorizar 30 cosas para el examen:

1. ¿Cuáles son los **7 principios de testing**? (Cap 1)
2. ¿Diferencia **error / defect / failure**? (Cap 1)
3. ¿Cuáles son los **4 niveles** de testing? (Cap 2)
4. ¿Cuáles son los **tipos** de testing (functional / non-functional)? (Cap 2)
5. ¿Cuáles son las **técnicas black-box**? (Cap 4)
6. ¿Cómo se aplica **EP**? Pasos (Cap 4)
7. ¿Cómo se aplica **BVA**? (Cap 4)
8. ¿Qué es **branch coverage**? (Cap 4)
9. ¿**Confirmation vs Regression** testing? (Cap 2)
10. ¿Qué son los **7 tipos de defects**? (resumidos)
11. ¿**Walkthrough vs Inspection**? (Cap 3)
12. ¿Cuál es el **test pyramid**? (Cap 5)
13. ¿**Project risk vs Product risk**? (Cap 5)
14. ¿**Severity vs Priority**? (Cap 5)
15. ¿**Entry vs Exit criteria**? (Cap 5)
16. ¿Qué es **shift-left**? (Cap 2)
17. ¿Qué es **DevOps impact** en testing? (Cap 2)
18. ¿Qué es **ATDD**? (Cap 4)
19. ¿Qué es **user story**? (Cap 4)
20. ¿Qué son **acceptance criteria**? (Cap 4)
21. ¿**QA vs QC vs Testing**? (Cap 1)
22. ¿Qué es **risk level** = likelihood × impact? (Cap 5)
23. ¿Qué son las **testing quadrants**? (Cap 5)
24. ¿Cuál es la **diferencia entre validation vs verification**? (Cap 1)
25. ¿Qué es **exploratory testing** con charter? (Cap 4)
26. ¿Qué es **whole team approach**? (Cap 1)
27. ¿Qué ISO 25010:2023 cambió? (interacción capability / flexibility / safety)
28. ¿Cuáles son los **3 K levels** (K1, K2, K3)? (Cap 0)
29. ¿Qué es **Wideband Delphi**? (Cap 5)
30. ¿Qué cambia en v4.0.1 desde v3.1? (por si te dan una pregunta de vocabulario)

---

## 📌 Mnemotécnicos rápidos

- **7 Principios:** "**S**how, **E**xhaustive, **E**arly, **C**luster, **P**esticide, **C**ontext, **A**bsence"
- **Niveles:** "**CISA**: Component, Integration, System, Acceptance"
- **Tipos F/NF:** "Functional = QUÉ; Non-Functional = CÓMO"
- **EP:** "una partición = un test"
- **BVA:** "los bugs viven en los **bordes**"
- **Decision Table:** "combinaciones = reglas"
- **State diagram:** "estados + eventos + acciones"
- **Branch coverage:** "100% branch ≥ 100% statement"
- **Test pyramid:** "mucho abajo, poco arriba"
- **Risk level:** "likely × impact"
- **Project vs Product risks:** "Project = cómo se hace; Product = qué se hace"
- **Severity vs Priority:** "Severity = Daño técnico; Priority = Urgencia"
