# Sample Exam A — ISTQB CTFL v4.0.1 — Versión Dental (40 preguntas)

> **Condiciones de examen real:**
> - **Tiempo: 60 minutos** (cronometrar, no cheating)
> - **40 preguntas**, multiple choice (4 opciones típicamente)
> - **Nota mínima: 26/40 = 65%**
>
> **Distribución por capítulo (igual que ISTQB oficial):**
> - Cap 1 (Fundamentos): 8 preguntas (~20%)
> - Cap 2 (Ciclo de vida): 6 preguntas (~15%)
> - Cap 3 (Estáticas): 4 preguntas (~10%)
> - Cap 4 (Técnicas): 12 preguntas (~30%) — el más pesado
> - Cap 5 (Gestión): 6 preguntas (~15%)
> - Cap 6 (Herramientas): 4 preguntas (~10%)
>
> ⚠️ **Disclaimer:** este es un sample NO oficial hecho a partir del syllabus v4.0.1 oficial, en contexto odontológico. Para material oficial ISTQB, consultar [www.istqb.org](https://www.istqb.org).

---

## SECCIÓN 1 — Fundamentos del Testing (Q1-Q8)

### Q1. (K1, LO 1.1.1) ¿Cuál de los siguientes NO es un objetivo típico del testing?

A) Detectar defects
B) Reducir riesgo
C) Compilar el código
D) Validar necesidades del usuario

### Q2. (K2, LO 1.2.3) En el caso de la endodoncia con dolor post-operatorio, ¿cuál es el "defect"?

A) El paciente sintió dolor
B) El odontólogo hizo algo mal
C) El conducto que quedó sin tratar (por ejemplo)
D) El dolor a la percusión

### Q3. (K2, LO 1.3.1) El "pesticide paradox" significa que:

A) Los bugs se acumulan como pesticidas
B) Aplicar los mismos tests repetidamente encuentra cada vez menos nuevos defects
C) Solo se puede usar una herramienta de testing por proyecto
D) Los tests automatizados son tóxicos

### Q4. (K2, LO 1.3.1) El principio "Absence-of-errors is a fallacy" implica que:

A) No se puede tener cero errors
B) Un sistema sin defects puede no satisfacer las necesidades del usuario
C) El testing es innecesario
D) Los defects siempre están

### Q5. (K2, LO 1.4.2) ¿Cuál es la diferencia entre verification y validation?

A) Verification es manual; validation es automática
B) Verification = ¿hicimos el producto bien?; Validation = ¿es el producto correcto para el usuario?
C) Verification es unit tests; Validation es integration tests
D) No hay diferencia

### Q6. (K2, LO 1.4.1) ¿Cuál de las siguientes NO es una actividad típica del proceso de testing?

A) Test analysis
B) Test design
C) Test implementation
D) Test abandonment

### Q7. (K2, LO 1.5.3) ¿Cuál es el nivel MÁS ALTO de independencia de testing?

A) Testing realizado por el mismo developer que escribió el código
B) Testing realizado por un colega del equipo de desarrollo
C) Testing realizado por un equipo independiente externo a la organización
D) Testing realizado por el test manager

### Q8. (K2, LO 1.2.3) En la cadena causal, ¿cuál es la diferencia entre error y failure?

A) Error es en el producto; failure es en la persona
B) Error es una acción humana incorrecta; failure es un comportamiento observable
C) Error es detectable; failure no
D) Son sinónimos

---

## SECCIÓN 2 — Ciclo de Vida (Q9-Q14)

### Q9. (K2, LO 2.1.2) ¿Cuál de los siguientes NO es un modelo de ciclo de vida del software?

A) Cascada (Waterfall)
B) Modelo en V
C) Modelo iterativo
D) Modelo de Fibonacci

### Q10. (K2, LO 2.2.1) ¿En qué nivel de testing se prueba una pantalla individual del software sin conexión al resto?

A) Integration testing
B) Component testing
C) System testing
D) Acceptance testing

### Q11. (K2, LO 2.2.3) Un desarrollador arregló un bug donde el software no aceptaba la "ñ" en los nombres. ¿Qué tipo de testing verifica específicamente que el bug está arreglado?

A) Regression testing
B) Confirmation testing (re-testing)
C) Smoke testing
D) Maintenance testing

### Q12. (K2, LO 2.4.1) ¿Cuándo aplica el maintenance testing?

A) Después de un cambio en el código
B) Después de un cambio en el entorno (navegador, OS, base de datos)
C) Solo en producción
D) Solo al inicio del proyecto

### Q13. (K2, LO 2.2.2) ¿Cuál es la diferencia entre functional y non-functional testing?

A) Functional es manual; non-functional es automático
B) Functional verifica QUÉ hace; non-functional verifica CÓMO lo hace
C) Functional es para devs; non-functional es para testers
D) No hay diferencia

### Q14. (K2, LO 2.5.2) El "shift-left" en testing significa:

A) Mover el testing al final del proyecto
B) Testear temprano en el ciclo de vida
C) Testear solo en producción
D) Usar herramientas automatizadas

---

## SECCIÓN 3 — Pruebas Estáticas (Q15-Q18)

### Q15. (K2, LO 3.1.1) ¿Cuál de las siguientes es una característica del static testing?

A) Requiere ejecutar el software
B) No requiere ejecutar el software
C) Solo aplica a código fuente
D) Solo lo hace el developer

### Q16. (K2, LO 3.3.2) ¿Cuál de los siguientes tipos de revisión es el MÁS formal?

A) Informal review
B) Walkthrough
C) Technical review
D) Inspection

### Q17. (K2, LO 3.3.1) En una inspection formal, ¿qué rol lee el documento en voz alta durante la reunión?

A) Moderator
B) Author
C) Reader
D) Reviewer

### Q18. (K2, LO 3.3.4) ¿Cuál de las siguientes NO es un success factor para las revisiones?

A) Objetivos claros
B) Revisores adecuados
C) Usar la herramienta más cara
D) Registro de defects encontrados

---

## SECCIÓN 4 — Técnicas de Diseño ⭐ (Q19-Q30)

### Q19. (K2, LO 4.1.1) ¿Cuál es la diferencia entre black-box y white-box testing?

A) Black-box es manual; white-box es automático
B) Black-box testea sin ver el código; white-box testea mirando el código
C) Black-box es para users; white-box es para devs
D) No hay diferencia

### Q20. (K3, LO 4.2.1) Una regla dice: "Los pacientes mayores de 65 años reciben 20% de descuento". ¿Cuántas particiones de equivalencia?

A) 1
B) 2
C) 3
D) 4

### Q21. (K3, LO 4.2.2) Para esa misma regla, ¿qué valores testarías con BVA?

A) 25, 45, 65, 85
B) 64, 65, 66
C) 1, 50, 100
D) 65 solamente

### Q22. (K3, LO 4.3.3) Una decisión dice: "Se prescribe antibiótico si (a) hay infección activa Y (b) no hay alergia". ¿Cuántas combinaciones tiene la decision table?

A) 2
B) 3
C) 4
D) 8

### Q23. (K3, LO 4.4.1) Un sistema tiene los siguientes estados para una cita: [Programada] → [Confirmada] → [Atendida] → [Pagada]. ¿Cuál es una transición INVÁLIDA?

A) Programada → Confirmada
B) Confirmada → Atendida
C) Atendida → Pagada
D) Pagada → Confirmada

### Q24. (K3, LO 4.2.1) El campo "Edad" en un sistema acepta valores entre 0 y 120. ¿Cuál es una partición INVÁLIDA?

A) 0-120 (caso típico)
B) -1, -10 (menor a 0)
C) 30 (caso válido)
D) 60 (caso válido)

### Q25. (K3, LO 4.3.1) Para una regla "descuento del 15% para mayores de 60 años", ¿cuántos valores BVA necesitarías testear como mínimo?

A) 2 (un valor por partición)
B) 3 (59, 60, 61)
C) 4 (60, 61, 62, 63)
D) 10

### Q26. (K3, LO 4.3.3) Una regla compleja dice: "Se aprueba un plan si (consentimiento firmado) Y (no es alérgico) Y (está en presupuesto)". ¿Cuál técnica es MÁS apropiada?

A) EP
B) BVA
C) Decision Table
D) State Transition

### Q27. (K2, LO 4.5.1) "Error guessing" es una técnica basada en:

A) Documentación formal
B) La intuición y experiencia del tester
C) Generación automática
D) Standards ISO

### Q28. (K2, LO 4.5.2) ¿Cuándo conviene usar exploratory testing?

A) Cuando hay abundante documentación
B) Cuando hay poco tiempo y poca documentación
C) Solo en producción
D) Solo cuando hay un equipo grande

### Q29. (K2, LO 4.5.3) ¿Qué es checklist-based testing?

A) Testing sin documentación
B) Testing usando una lista predefinida de cosas a verificar
C) Testing solo al final
D) Testing automatizado

### Q30. (K3, LO 4.5.4) Si tenés que testear un sistema con rangos numéricos claros (ej: edad, peso, dosis), ¿qué técnica es la MÁS apropiada?

A) Decision Table
B) State Transition
C) Equivalence Partitioning + Boundary Value Analysis
D) Error Guessing

---

## SECCIÓN 5 — Gestión de Testing (Q31-Q36)

### Q31. (K2, LO 5.1.2) ¿Cuál de los siguientes NO es típicamente parte de un test plan?

A) Cronograma de testing
B) Recursos necesarios
C) El código fuente completo del sistema
D) Criterios de entrada y salida

### Q32. (K2, LO 5.1.3) ¿Cuál es la diferencia entre test plan y test strategy?

A) Son sinónimos
B) Test plan es para un proyecto específico; test strategy es para la organización
C) Test plan es para devs; test strategy es para managers
D) Test plan es técnico; test strategy es financiero

### Q33. (K2, LO 5.3.1) ¿Cuál es la fórmula de riesgo en testing?

A) Riesgo = probabilidad + impacto
B) Riesgo = probabilidad × impacto
C) Riesgo = probabilidad ÷ impacto
D) Riesgo = impacto ÷ probabilidad

### Q34. (K2, LO 5.3.3) Un defecto es "severidad alta" pero "prioridad baja". Esto significa:

A) El defecto es crítico y urge arreglarlo
B) El defecto es crítico pero no urge arreglarlo
C) El defecto es cosmético
D) El defecto no es importante

### Q35. (K3, LO 5.2.2) La densidad de defectos (defects/KLOC) es una métrica de:

A) Proceso
B) Producto
C) Proyecto
D) Personal

### Q36. (K2, LO 5.3.2) En configuration management, ¿cuáles elementos deben estar bajo control de versiones?

A) Solo el código
B) Solo los documentos de requisitos
C) Código, requisitos, tests, datos, herramientas
D) Solo los tests

---

## SECCIÓN 6 — Herramientas (Q37-Q40)

### Q37. (K2, LO 6.1.1) ¿Cuál de las siguientes es una herramienta de static analysis?

A) JMeter
B) Selenium
C) SonarQube
D) Jira

### Q38. (K2, LO 6.1.1) Selenium es una herramienta de:

A) Test management
B) Bug tracking
C) Test execution / automation
D) Static analysis

### Q39. (K2, LO 6.3.1) ¿Cuál es el PRIMER paso para adoptar una herramienta?

A) Comprar la herramienta
B) Assessment (evaluar qué necesitás)
C) Capacitar al equipo
D) Hacer rollout

### Q40. (K2, LO 6.1.2) La "falsa sensación de cobertura" ocurre cuando:

A) Los tests pasan pero el software tiene defects graves
B) Los tests fallan mucho
C) Los tests son lentos
D) Hay muchos tests automatizados

---

## ⏰ STOP — Tu tiempo se acabó

Anotá tu puntaje (sin mirar las respuestas):
**Correctas: ____ / 40**

Ahora mirá [`SAMPLE_EXAM_A_ANSWERS.md`](SAMPLE_EXAM_A_ANSWERS.md) para corregir.
