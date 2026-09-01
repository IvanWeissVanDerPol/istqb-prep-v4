# Respuestas Sample Exam A — Con explicaciones

> **Cómo usar este documento:**
> 1. Mirar tu puntaje en [`SAMPLE_EXAM_A.md`](SAMPLE_EXAM_A.md).
> 2. Para cada pregunta que fallaste, leer la explicación.
> 3. Si fallaste más del 30%, releer el capítulo correspondiente antes de seguir.

---

## SECCIÓN 1 — Fundamentos del Testing

### Q1. ✅ **C) Compilar el código**
Compilar es tarea del developer, no del tester. Los otros tres son objetivos típicos del testing (LO 1.1.1).

### Q2. ✅ **C) El conducto que quedó sin tratar (por ejemplo)**
El defect es la imperfección en el producto (LO 1.2.3). El dolor (failure) es lo que el paciente siente; el error es la acción humana. El conducto sin tratar es la imperfección.

### Q3. ✅ **B) Aplicar los mismos tests repetidamente encuentra cada vez menos nuevos defects**
Principio 5 del testing (LO 1.3.1). Los tests "envejecen" — hay que actualizarlos.

### Q4. ✅ **B) Un sistema sin defects puede no satisfacer las necesidades del usuario**
Principio 7 (LO 1.3.1). Absence-of-errors fallacy: sin defects ≠ útil.

### Q5. ✅ **B)** Verification = ¿lo hicimos bien?; Validation = ¿es lo correcto para el usuario?
LO 1.4.2. La trampa más común.

### Q6. ✅ **D) Test abandonment**
No existe. Las actividades son: planning, monitoring, analysis, design, implementation, execution, completion (LO 1.4.1).

### Q7. ✅ **C) Testing realizado por un equipo independiente externo a la organización**
LO 1.5.3. Mayor independencia = mejor testing. El developer mismo es la peor opción.

### Q8. ✅ **B) Error es una acción humana incorrecta; failure es un comportamiento observable**
LO 1.2.3. Distinción crítica para el examen.

---

## SECCIÓN 2 — Ciclo de Vida

### Q9. ✅ **D) Modelo de Fibonacci**
Fibonacci no es un modelo SDLC (LO 2.1.2). Los modelos son cascada, V, iterativo, incremental, ágil.

### Q10. ✅ **B) Component testing**
LO 2.2.1. Una pantalla sola = componente. Integration sería probar varias juntas.

### Q11. ✅ **B) Confirmation testing (re-testing)**
LO 2.2.3. Confirmation verifica el fix específico. Regression verifica el resto.

### Q12. ✅ **B) Después de un cambio en el entorno (navegador, OS, base de datos)**
LO 2.4.1. Maintenance testing es para cambios en el entorno, no en el código.

### Q13. ✅ **B) Functional verifica QUÉ hace; non-functional verifica CÓMO lo hace**
LO 2.2.2. Functional = funcionalidad. Non-functional = performance, usability, security.

### Q14. ✅ **B) Testear temprano en el ciclo de vida**
LO 2.5.2. Shift-left = mover testing a la izquierda del cronograma (más temprano).

---

## SECCIÓN 3 — Pruebas Estáticas

### Q15. ✅ **B) No requiere ejecutar el software**
LO 3.1.1. Static testing = revisar documentos sin ejecutar.

### Q16. ✅ **D) Inspection**
LO 3.3.2. Más formal = más roles, más proceso, más métricas.

### Q17. ✅ **C) Reader**
LO 3.3.1. Roles: Moderator (facilita), Author (escribió), Reader (lee en voz alta), Reviewer (busca defects), Recorder (anota).

### Q18. ✅ **C) Usar la herramienta más cara**
LO 3.3.4. Success factors son objetivos claros, revisores adecuados, checklists, registro, seguimiento. La herramienta cara no es un factor.

---

## SECCIÓN 4 — Técnicas de Diseño ⭐

### Q19. ✅ **B) Black-box testea sin ver el código; white-box testea mirando el código**
LO 4.1.1.

### Q20. ✅ **B) 2**
LO 4.2.1. <65 y ≥65 son las dos particiones.

### Q21. ✅ **B) 64, 65, 66**
LO 4.2.2. BVA testea los bordes. 64 (afuera), 65 (borde exacto), 66 (adentro).

### Q22. ✅ **C) 4**
LO 4.3.3. 2 condiciones, 2 valores cada una = 2² = 4 combinaciones.

### Q23. ✅ **D) Pagada → Confirmada**
LO 4.4.1. State Transition testing busca las transiciones inválidas.

### Q24. ✅ **B) -1, -10 (menor a 0)**
LO 4.2.1. Las particiones inválidas también son particiones. Edad negativa no es válida.

### Q25. ✅ **B) 3 (59, 60, 61)**
LO 4.3.2. BVA testea el valor adentro, el valor afuera, y el valor en el borde.

### Q26. ✅ **C) Decision Table**
LO 4.3.3. Tres condiciones booleanas combinadas = decision table clásico.

### Q27. ✅ **B) La intuición y experiencia del tester**
LO 4.5.1. Error guessing = adivinar dónde están los defects basado en experiencia.

### Q28. ✅ **B) Cuando hay poco tiempo y poca documentación**
LO 4.5.2. Exploratory testing es ideal cuando no hay docs y el tiempo es corto.

### Q29. ✅ **B) Testing usando una lista predefinida de cosas a verificar**
LO 4.5.3. Checklist-based testing = usar una lista.

### Q30. ✅ **C) Equivalence Partitioning + Boundary Value Analysis**
LO 4.5.4. Rangos numéricos → EP + BVA es la combinación estándar.

---

## SECCIÓN 5 — Gestión de Testing

### Q31. ✅ **C) El código fuente completo del sistema**
LO 5.1.2. Un test plan NO contiene el código fuente. Contiene el plan de cómo testear.

### Q32. ✅ **B) Test plan es para un proyecto específico; test strategy es para la organización**
LO 5.1.3. Plan = específico. Strategy = organizacional.

### Q33. ✅ **B) Riesgo = probabilidad × impacto**
LO 5.3.1. Fórmula clásica.

### Q34. ✅ **B) El defecto es crítico pero no urge arreglarlo**
LO 5.3.3. Ejemplo típico: defecto crítico en función que nadie usa.

### Q35. ✅ **B) Producto**
LO 5.2.2. Densidad de defectos = calidad del producto. Una métrica de proceso sería, por ejemplo, el tiempo medio de resolución.

### Q36. ✅ **C) Código, requisitos, tests, datos, herramientas**
LO 5.3.2. Configuration management es integral — todo bajo control.

---

## SECCIÓN 6 — Herramientas

### Q37. ✅ **C) SonarQube**
LO 6.1.1. JMeter = performance, Selenium = test execution, Jira = bug tracking.

### Q38. ✅ **C) Test execution / automation**
LO 6.1.1. Selenium automatiza tests de aplicaciones web.

### Q39. ✅ **B) Assessment (evaluar qué necesitás)**
LO 6.3.1. Assessment es el primer paso de los 6 formales.

### Q40. ✅ **A) Los tests pasan pero el software tiene defects graves**
LO 6.1.2. Falsa sensación de cobertura = tests verdes pero software roto.

---

## 📊 Tu diagnóstico

| Puntaje | Significado | Acción |
|---|---|---|
| **32-40 (80%+)** | Excelente. Dominás el material. | Listo para rendir. |
| **26-31 (65-79%)** | Bien. Aprobás el examen. | Repasá los errores puntuales. |
| **20-25 (50-64%)** | Cerca pero no. | Releé los capítulos donde fallaste. |
| **< 20 (< 50%)** | Necesitás más estudio. | Volvé al Cap 1, re-estudia, repetí el examen. |

**Si fallaste más del 30% en una sección específica, esa sección necesita más estudio:**
- Cap 1: releé [`../02_cap1_fundamentos/`](../02_cap1_fundamentos/)
- Cap 2: [`../03_cap2_ciclo_vida/`](../03_cap2_ciclo_vida/)
- Cap 3: [`../04_cap3_pruebas_estaticas/`](../04_cap3_pruebas_estaticas/)
- Cap 4: [`../05_cap4_tecnicas_diseno/`](../05_cap4_tecnicas_diseno/) ← **el más importante**
- Cap 5: [`../06_cap5_gestion/`](../06_cap5_gestion/)
- Cap 6: [`../07_cap6_herramientas/`](../07_cap6_herramientas/)
