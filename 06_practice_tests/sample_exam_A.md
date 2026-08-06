# Sample Exam A — ISTQB CTFL v4.0.1 (40 preguntas)

> **Condiciones de examen real:**
> - Tiempo: **60 minutos** (cronometrar)
> - Total: **40 preguntas**, multiple choice (4 opciones típicamente)
> - Nota mínima: **26/40 = 65%**
> - Idioma oficial: tu Member Board lo ofrece (Latinoamérica: español)
>
> **⚠️ Disclaimer:** este es un sample NO oficial hecho a partir del syllabus v4.0.1 oficial. ISTQB no publica sample exams gratuitos oficiales. Para material oficial, consultar con ASOLINFO Paraguay o el Member Board.

---

## Preguntas — Cap 1 (5 preguntas, ~13%)

**Q1. (K2, LO 1.2.3) ¿Cuál de las siguientes es la cadena causal correcta?**

A) Failure → defect → error.
B) Error → defect → failure.
C) Error → failure → defect.
D) Defect → error → failure.

**Q2. (K1, LO 1.3.1) El "pesticide paradox" significa que:**

A) Los bugs se acumulan como pesticidas.
B) Aplicar los mismos tests repetidamente encuentra cada vez menos nuevos defects.
C) Los tests automatizados son tóxicos.
D) Solo se puede usar una herramienta de testing por proyecto.

**Q3. (K2, LO 1.3.1) El principio "Absence-of-errors is a fallacy" implica que:**

A) No se puede tener cero errors.
B) Un sistema sin defects puede no satisfacer las necesidades del usuario.
C) El testing es innecesario.
D) Los defectos siempre están.

**Q4. (K2, LO 1.4.1) ¿Cuál de las siguientes NO es una actividad típica del proceso de testing?**

A) Test analysis.
B) Test design.
C) Test implementation.
D) Test abandonment.

**Q5. (K2, LO 1.5.3) ¿Cuál es el nivel MÁS ALTO de independencia de testing?**

A) Testing realizado por el mismo developer que escribió el código.
B) Testing realizado por un colega del equipo de desarrollo.
C) Testing realizado por un equipo independiente externo a la organización.
D) Testing realizado por el test manager.

---

## Preguntas — Cap 2 (7 preguntas, ~17%)

**Q6. (K2, LO 2.2.1) ¿Cuál de los siguientes NO es un nivel de testing?**

A) Component testing.
B) Integration testing.
C) Functional testing.
D) Acceptance testing.

**Q7. (K2, LO 2.2.2) Según ISO 25010 (2023), ¿cuál de las siguientes es NON-functional?**

A) Confirmar que el login acepta passwords.
B) Verificar performance del sistema bajo carga.
C) Validar que el botón "Comprar" crea orden.
D) Probar que el formulario valida email.

**Q8. (K2, LO 2.2.3) ¿Cuál es la diferencia entre confirmation testing y regression testing?**

A) Son sinónimos.
B) Confirmation verifica que un bug específico está fixed; regression verifica que cambios no rompieron nada más.
C) Regression es antes; confirmation después.
D) Solo se hace una al mes.

**Q9. (K2, LO 2.1.5) "Shift-left" significa:**

A) Mover testing al final del proyecto.
B) Mover testing hacia el inicio del SDLC.
C) Eliminar testing.
D) Mover al hemisferio izquierdo.

**Q10. (K2, LO 2.1.4) ¿Cuál de los siguientes es impacto típico de DevOps en testing?**

A) Testing más lento.
B) Testing continuo integrado en el pipeline CI/CD.
C) Eliminación de tests automatizados.
D) Solo testing manual.

**Q11. (K1, LO 2.1.3) ¿Cuál NO es un test-first approach?**

A) TDD.
B) ATDD.
C) BDD.
D) XYZ-testing.

**Q12. (K2, LO 2.1.6) ¿Para qué sirven las "retrospectives" en testing?**

A) Castigar a los developers.
B) Mecanismo para identificar mejoras continuas al proceso de testing.
C) Eliminar la fase de planning.
D) Definir el presupuesto.

---

## Preguntas — Cap 3 (3 preguntas, ~8%)

**Q13. (K2, LO 3.1.3) ¿Cuál describe mejor la diferencia entre static y dynamic testing?**

A) Static usa herramientas, dynamic no.
B) Static testing NO ejecuta el software; dynamic testing SÍ lo ejecuta.
C) Static es manual, dynamic es automatizado.
D) No hay diferencia.

**Q14. (K2, LO 3.2.4) ¿Cuál es el tipo de review MÁS formal?**

A) Informal review.
B) Walkthrough.
C) Technical review.
D) Inspection.

**Q15. (K1, LO 3.2.3) En una review, ¿cuál de estos es un rol estándar?**

A) Hacker.
B) Moderator.
C) Scrum Master.
D) End-user.

---

## Preguntas — Cap 4 (12 preguntas, ~30%) — MÁS PESADO

**Q16. (K3, LO 4.2.1) EP para un campo edad que acepta 18-65, ¿cuántas particiones hay?**

A) 1.
B) 2.
C) 3.
D) 4.

**Q17. (K3, LO 4.2.2) BVA clásico para campo 1-31, ¿cuál es el conjunto correcto?**

A) 1, 31.
B) 0, 1, 31, 32.
C) 1, 16, 31.
D) Solo los límites.

**Q18. (K3, LO 4.2.3) Si hay 5 condiciones binarias, ¿cuántas reglas posibles?**

A) 5.
B) 10.
C) 25.
D) 32.

**Q19. (K3, LO 4.2.4) State transition testing cubre:**

A) Solo inputs.
B) Estados, eventos, transiciones y acciones.
C) Solo outputs.
D) Solo branches del código.

**Q20. (K2, LO 4.3.2) Branch coverage es más fuerte que statement coverage porque:**

A) Mide líneas.
B) Requiere que cada decisión se evalúe a true y false.
C) Es más rápida.
D) Es manual.

**Q21. (K2, LO 4.4.1) Error guessing es una técnica:**

A) Estática.
B) Black-box formal.
C) Experience-based.
D) Automática.

**Q22. (K2, LO 4.4.2) Exploratory testing:**

A) Es testing aleatorio sin sentido.
B) Combina diseño, ejecución y aprendizaje en paralelo.
C) Solo funciona con automatizados.
D) Es lo mismo que stress testing.

**Q23. (K2, LO 4.4.3) Checklist-based testing:**

A) NO requiere documentación.
B) Usa listas de verificación predefinidas.
C) Es ad-hoc.
D) Solo aplica a UI.

**Q24. (K2, LO 4.5.1 — NUEVO v4.0) ¿Cuál es el formato típico de una user story?**

A) Diagrama UML.
B) "Como <rol>, quiero <acción>, para <beneficio>".
C) Diagrama de flujo.
D) Pseudocódigo.

**Q25. (K2, LO 4.5.2 — NUEVO v4.0) ¿Cuál NO es opción para escribir acceptance criteria?**

A) Given-When-Then.
B) Checklist.
C) Scenario-based.
D) Compiled OOP class.

**Q26. (K3, LO 4.5.3 — NUEVO v4.0) ATDD significa:**

A) Tests automáticos.
B) Acceptance Test-Driven Development — team escribe acceptance tests ANTES del código.
C) Author-Tested Development.
D) Automation Testing Definition Document.

**Q27. (K2, LO 4.3.3) White-box testing es útil para:**

A) Reemplazar black-box.
B) Encontrar código muerto y medir coverage.
C) Solo testing manual.
D) Solo al final del proyecto.

---

## Preguntas — Cap 5 (8 preguntas, ~20%)

**Q28. (K1, LO 5.1.6 — NUEVO v4.0) En el test pyramid, ¿dónde está el grueso de tus tests?**

A) Arriba (UI/E2E).
B) En el medio (integration).
C) Abajo (unit tests).
D) Solo en una capa.

**Q29. (K1, LO 5.2.1) ¿Cómo se calcula "risk level"?**

A) Sumando likelihood + impact.
B) Multiplicando likelihood × impact.
C) Restando.
D) Es opcional.

**Q30. (K2, LO 5.2.2) ¿Cuál describe mejor "project risk"?**

A) Un bug en el producto.
B) Un riesgo que afecta la calidad del producto.
C) Un riesgo que afecta el schedule/coste/calidad del proyecto de testing.
D) Una técnica de testing.

**Q31. (K2, LO 5.1.3) ¿Cuál es la diferencia entre entry criteria y exit criteria?**

A) Son sinónimos.
B) Entry = condiciones ANTES de empezar; Exit = condiciones ANTES de cerrar.
C) Solo existen en agile.
D) Solo aplican al final.

**Q32. (K3, LO 5.5.1) En un defect report, ¿cuál de los siguientes campos es OBLIGATORIO?**

A) Nombre del developer.
B) Severity y priority.
C) Código del producto.
D) Cantidad de líneas afectadas.

**Q33. (K2, LO 5.3.1) ¿Cuál de estos NO es una métrica común de testing?**

A) % test cases ejecutados.
B) % pass rate.
C) Cantidad de developers.
D) Defects encontrados vs resueltos.

**Q34. (K3, LO 5.1.5) Test case prioritization se usa para:**

A) Decorar reportes.
B) Determinar el ORDEN en que se ejecutan tests según riesgo/cobertura.
C) Eliminar tests.
D) Esconder bugs.

**Q35. (K2, LO 5.1.7 — NUEVO v4.0) ¿Cuál es el cuadrante Q1 en testing quadrants?**

A) Performance.
B) Functional business-facing.
C) Security.
D) Component testing.

---

## Preguntas — Cap 6 (5 preguntas, ~12%)

**Q36. (K2, LO 6.1.1) ¿Cuál NO es un tipo de test tool?**

A) Test management tools.
B) Test execution tools.
C) Static analysis tools.
D) Calendar tool.

**Q37. (K1, LO 6.2.1) ¿Cuál es un beneficio típico de test automation?**

A) Eliminar todos los bugs.
B) Repetibilidad y velocidad para tests repetitivos.
C) Reemplazar al tester humano.
D) Eliminar la necesidad de specs.

**Q38. (K1, LO 6.2.1) ¿Cuál es un RIESGO típico de test automation?**

A) Tests automatizados son más rápidos.
B) Mantenimiento alto y expectativa falsa de "100% coverage".
C) Menos bugs en producción.
D) Documentación automática.

**Q39. (K2, LO 6.1.1) ¿Una herramienta de static analysis puede detectar?**

A) Bugs solo en runtime.
B) Indefinición de variables (potencial null).
C) Bugs visuales solo.
D) No detecta nada.

**Q40. (K2, LO 6.1.1) ¿Cuál describe mejor la palabra "test execution tool"?**

A) Herramienta para generar tests.
B) Herramienta que ejecuta tests automáticamente (e.g., Selenium, Playwright).
C) Herramienta para escribir reportes.
D) Herramienta de gestión de proyectos.

---

## 📝 Para completar el examen

Calculá tu score: **(correctas / 40) × 100**

| Score | Resultado |
|-------|-----------|
| **≥80% (32+)** | Excelente, listo para examen |
| **65-79% (26-31)** | Listo con repaso final |
| **50-64% (20-25)** | Necesita más estudio |
| **<50% (<20)** | Repasá summaries, retoma plan |

---

## 🔍 Análisis por capítulo (cuando termines)

| Cap | Obtuviste / Total | Porcentaje |
|-----|-------------------|-----------|
| 1 | /5 | % |
| 2 | /7 | % |
| 3 | /3 | % |
| 4 | /12 | % |
| 5 | /8 | % |
| 6 | /5 | % |

**Si fallaste más de la mitad en un capítulo → volver a leer el summary + hacer ejercicios.**

---

## 💡 Tips para el examen real

1. **60 min / 40 preguntas** = ~1.5 min por pregunta (sin dramas)
2. **Lee cada pregunta dos veces** — las preguntas ISTQB son densas
3. **Cuidado con "always / never / exactly"** — respuestas absolutas son casi siempre falsas
4. **Bookmark** las preguntas difíciles y volvé al final
5. **Primera opción que parece obvia** usualmente es correcta (no busques trampa)
6. **Si dudás entre 2 opciones**, la respuesta ISTQB es la más específica/técnica
7. **NO** dejes respuestas en blanco — no hay penalidad por mal
