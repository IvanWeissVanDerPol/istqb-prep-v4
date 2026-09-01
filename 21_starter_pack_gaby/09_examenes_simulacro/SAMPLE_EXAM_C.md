# Sample Exam C — ISTQB CTFL v4.0.1 — Versión Dental (40 preguntas)

> **Este examen NO tiene respuestas.** Es para práctica final antes del examen real.
>
> **Condiciones:**
> - Tiempo: **60 minutos** (cronometrar estricto)
> - 40 preguntas, multiple choice
> - Aprobar: **65%+ (26/40)**
>
> **Después de hacerlo:** buscá las respuestas correctas comparando con [`SAMPLE_EXAM_A_ANSWERS.md`](SAMPLE_EXAM_A_ANSWERS.md) y [`SAMPLE_EXAM_B_ANSWERS.md`](SAMPLE_EXAM_B_ANSWERS.md). Los LOs son los mismos.
>
> ⚠️ Sample NO oficial, basado en syllabus v4.0.1.

---

## SECCIÓN 1 — Fundamentos del Testing (Q1-Q8)

### Q1. (K2, LO 1.2.3) Una paciente tuvo una reacción alérgica a un anestésico que vos le diste. ¿Qué representa la alergia?

A) Defect
B) Failure
C) Error
D) Validation failure

### Q2. (K2, LO 1.3.1) El principio "Exhaustive testing is impossible" implica que:

A) No se puede testear software
B) Hay que elegir qué testear (no se puede cubrir todo)
C) Los tests son caros
D) Hay que contratar muchos testers

### Q3. (K2, LO 1.3.1) ¿Cuál es el principio que dice "los defects se concentran en pocas áreas"?

A) Pesticide paradox
B) Defects cluster together
C) Early testing saves time and money
D) Context-dependent

### Q4. (K2, LO 1.4.2) En un plan de tratamiento de ortodoncia, los criterios de éxito ("oclusión correcta, alineación, sonrisa funcional") son un ejemplo de:

A) Acceptance criteria (validation)
B) Test cases (verification)
C) Smoke testing
D) Maintenance testing

### Q5. (K2, LO 1.4.1) ¿Cuál de estas actividades ocurre DURANTE todo el ciclo de testing?

A) Test execution
B) Test monitoring and control
C) Test design
D) Test analysis

### Q6. (K2, LO 1.2.3) ¿Cuál es la cadena causal correcta?

A) Error → Defect → Failure
B) Failure → Defect → Error
C) Defect → Error → Failure
D) Error → Failure → Defect

### Q7. (K2, LO 1.5.1) ¿Qué es el sesgo de confirmación?

A) Confirmar el presupuesto con el paciente
B) Tendencia a buscar evidencia que confirme lo que uno ya cree
C) Confirmar que el software funciona
D) Confirmar la cita del paciente

### Q8. (K2, LO 1.1.1) ¿Cuál NO es un objetivo del testing?

A) Detectar defects
B) Compilar el código
C) Validar las necesidades del usuario
D) Construir confianza

---

## SECCIÓN 2 — Ciclo de Vida (Q9-Q14)

### Q9. (K2, LO 2.1.2) Scrum es un ejemplo de:

A) Cascada
B) Modelo V
C) Ágil / iterativo
D) Big Bang

### Q10. (K2, LO 2.2.1) ¿Cuál es el orden correcto de los niveles de testing (de menor a mayor alcance)?

A) Component → Integration → System → Acceptance
B) Acceptance → System → Integration → Component
C) Component → System → Integration → Acceptance
D) Integration → Component → System → Acceptance

### Q11. (K2, LO 2.2.3) ¿Cuál es la diferencia entre regression testing y confirmation testing?

A) Son sinónimos
B) Regression verifica el fix específico; confirmation verifica el resto
C) Regression verifica que lo que andaba, sigue andando; confirmation verifica el fix específico
D) Regression es manual; confirmation es automático

### Q12. (K2, LO 2.4.1) El "maintenance testing" se aplica cuando:

A) El código cambia
B) El entorno cambia (navegador, OS)
C) Los usuarios cambian
D) La empresa cambia de nombre

### Q13. (K2, LO 2.5.1) ¿Quién es responsable de hacer el component testing?

A) El tester dedicado
B) El usuario final
C) El developer (típicamente)
D) El test manager

### Q14. (K2, LO 2.2.2) ¿Cuál es un ejemplo de non-functional testing?

A) Verificar que el botón "guardar" funciona
B) Verificar que la página carga en menos de 2 segundos
C) Verificar que el login valida usuario y contraseña
D) Verificar que el reporte PDF se genera

---

## SECCIÓN 3 — Pruebas Estáticas (Q15-Q18)

### Q15. (K2, LO 3.1.1) ¿Cuál de las siguientes es static testing?

A) Ejecutar el software
B) Revisar los requisitos del sistema
C) Hacer user acceptance testing
D) Hacer performance testing

### Q16. (K2, LO 3.3.2) Ordená los tipos de revisión de menos formal a más formal:

A) Inspection → Walkthrough → Technical → Informal
B) Informal → Walkthrough → Technical → Inspection
C) Technical → Informal → Inspection → Walkthrough
D) Walkthrough → Inspection → Informal → Technical

### Q17. (K2, LO 3.3.4) ¿Cuál NO es un success factor para revisiones?

A) Objetivos claros
B) Checklists
C) No documentar defectos
D) Seguimiento

### Q18. (K2, LO 3.1.2) ¿Cuál de las siguientes es ventaja del static testing?

A) Encuentra defectos temprano
B) Solo lo puede hacer el developer
C) No requiere leer documentos
D) Es más caro que el dynamic

---

## SECCIÓN 4 — Técnicas de Diseño ⭐ (Q19-Q30)

### Q19. (K3, LO 4.2.1) ¿Cuál es la definición de equivalence partitioning?

A) Testear los bordes
B) Dividir inputs en grupos con comportamiento equivalente y testear uno por grupo
C) Combinar todas las condiciones
D) Testear transiciones de estado

### Q20. (K3, LO 4.2.2) ¿Cuál es la diferencia entre EP y BVA?

A) No hay diferencia
B) EP testea un valor por partición; BVA testea los bordes
C) EP es para devs; BVA es para testers
D) EP es para functional; BVA es para non-functional

### Q21. (K3, LO 4.3.1) Una regla dice "Aceptar temperatura entre 36 y 42 grados". ¿Cuál es una partición INVÁLIDA?

A) 36.0
B) 37.5
C) 50
D) 42.0

### Q22. (K3, LO 4.2.2) Para la regla anterior, ¿qué valores testarías con BVA?

A) 35.9, 36.0, 36.1, 41.9, 42.0, 42.1
B) 37, 38
C) 36, 42
D) 1, 100

### Q23. (K3, LO 4.3.3) Una decisión dice: "Aprobar crédito si (ingresos > 1000) Y (no tiene deudas) Y (antigüedad > 6 meses)". ¿Cuántas combinaciones tiene la decision table?

A) 3
B) 6
C) 8
D) 9

### Q24. (K3, LO 4.4.1) Un sistema de pedidos tiene los estados: [Carrito] → [Pago] → [Enviado] → [Entregado]. ¿Cuál es una transición INVÁLIDA que vale la pena testear?

A) Carrito → Pago
B) Pago → Enviado
C) Enviado → Entregado
D) Entregado → Pago

### Q25. (K2, LO 4.5.1) ¿Cuándo se usa error guessing?

A) Cuando hay documentación completa
B) Cuando no hay documentación
C) Cuando el tester tiene experiencia y quiere complementar otras técnicas
D) Cuando se automatiza todo

### Q26. (K2, LO 4.5.2) ¿Cuál es una característica del exploratory testing?

A) Requiere documentación previa
B) Es diseñar y ejecutar simultáneamente
C) Es lento
D) Es solo para developers

### Q27. (K2, LO 4.5.3) El checklist-based testing es útil cuando:

A) Hay que cubrir requisitos específicos y repetibles
B) Hay que improvisar
C) Hay que automatizar
D) Hay que testear performance

### Q28. (K3, LO 4.5.4) Si tenés que testear "Aprobar paciente si (cobertura OK) Y (consentimiento firmado) Y (no es alérgico)", ¿qué técnica?

A) EP
B) BVA
C) Decision Table
D) State Transition

### Q29. (K3, LO 4.3.2) Una regla dice "Descuento del 10% si compra > 100 USD". ¿Qué valores testarías con BVA?

A) 50, 100, 150
B) 99, 100, 101
C) 100
D) 1, 1000

### Q30. (K3, LO 4.2.1) Una regla dice "Edad válida entre 0 y 150". ¿Cuántas particiones?

A) 1
B) 2 (válida e inválida)
C) 3 (válida, inválida baja, inválida alta)
D) 4

---

## SECCIÓN 5 — Gestión de Testing (Q31-Q36)

### Q31. (K2, LO 5.1.2) ¿Cuál es la diferencia entre criterios de entrada y criterios de salida?

A) Son sinónimos
B) Entrada = cuándo empezar; Salida = cuándo terminar
C) Entrada = para devs; Salida = para testers
D) Entrada = antes; Salida = después

### Q32. (K2, LO 5.3.1) Si un defecto tiene alta probabilidad y alto impacto, su riesgo es:

A) Bajo
B) Medio
C) Alto
D) Muy alto

### Q33. (K2, LO 5.3.3) ¿Qué campo de un bug report es el MÁS importante?

A) El nombre del tester
B) La fecha
C) Los pasos para reproducir
D) La versión del software

### Q34. (K2, LO 5.3.3) Severidad alta + Prioridad baja significa:

A) Crítico y urge arreglar
B) Crítico pero no urge
C) Cosmético y urge
D) Cosmético y no urge

### Q35. (K3, LO 5.2.2) ¿Cuál es una métrica de PRODUCTO (no de proceso)?

A) % tests ejecutados a tiempo
B) Densidad de defectos
C) Tiempo medio de resolución
D) Esfuerzo dedicado a testing

### Q36. (K2, LO 5.3.2) Configuration management es importante porque:

A) Reduce costos
B) Asegura que todos los elementos del proyecto están bajo control
C) Hace que el software sea más rápido
D) Reemplaza al developer

---

## SECCIÓN 6 — Herramientas (Q37-Q40)

### Q37. (K2, LO 6.1.1) Selenium y Cypress son ejemplos de:

A) Test management tools
B) Test execution / automation tools
C) Static analysis
D) Bug tracking

### Q38. (K2, LO 6.1.1) JMeter es una herramienta de:

A) Bug tracking
B) Performance testing
C) Static analysis
D) Test management

### Q39. (K2, LO 6.3.1) El primer paso para adoptar una herramienta es:

A) Evaluación (Assessment)
B) PoC
C) Selección
D) Rollout

### Q40. (K2, LO 6.1.2) ¿Cuál es el principal riesgo de la automatización de tests?

A) Costo inicial alto
B) Falsa sensación de cobertura
C) Dificultad de mantenimiento
D) Necesidad de personal técnico

---

## ⏰ STOP — Tu tiempo se acabó

Anotá tu puntaje (sin mirar las respuestas — usá los LOs y la lógica):
**Correctas: ____ / 40**

**Calculá:**
- % del examen: ____%
- Aprobás (>= 65%): SÍ / NO

Si NO aprobás → no te preocupes. Volvé a los capítulos donde fallaste, repetí los quizzes, y agendá el examen real para 2 semanas después.

Si SÍ aprobás → agendá el examen real con confianza.
