# Sample Exam B — ISTQB CTFL v4.0.1 — Versión Dental (40 preguntas)

> **Condiciones de examen real:**
> - **Tiempo: 60 minutos** (cronometrar)
> - **40 preguntas**, multiple choice
> - **Nota mínima: 26/40 = 65%**
>
> ⚠️ Sample NO oficial, basado en syllabus v4.0.1. Material oficial: [www.istqb.org](https://www.istqb.org)

---

## SECCIÓN 1 — Fundamentos del Testing (Q1-Q8)

### Q1. (K2, LO 1.2.1) ¿Por qué es necesario el testing de software?

A) Porque lo dice la ley
B) Porque el software está en sistemas críticos y los defects pueden causar daño
C) Porque el developer es vago
D) Porque el testing es divertido

### Q2. (K2, LO 1.2.2) La diferencia entre QA y Testing es:

A) QA es para juniors, Testing es para seniors
B) QA es sobre procesos (proactivo); Testing es sobre producto (reactivo)
C) Son sinónimos
D) QA es testing manual, Testing es automatizado

### Q3. (K2, LO 1.1.2) ¿Cuál es la diferencia entre testing y debugging?

A) Testing encuentra defects; debugging corrige defects
B) Testing es manual; debugging es automático
C) Testing es antes; debugging es después
D) No hay diferencia

### Q4. (K2, LO 1.3.1) ¿Cuál de estos es el Principio 4 del testing?

A) Testing shows the presence of defects
B) Defects cluster together
C) Early testing saves time and money
D) Testing is context-dependent

### Q5. (K2, LO 1.4.2) Una endodoncia técnicamente perfecta pero que el paciente no puede usar porque le molesta la oclusión. ¿Qué falló?

A) Verification (técnicamente bien)
B) Validation (no satisface al usuario)
C) Ambos
D) Ninguno

### Q6. (K2, LO 1.4.1) ¿Cuál es el orden correcto de las actividades de testing?

A) Design → Analysis → Implementation → Planning → Execution
B) Planning → Analysis → Design → Implementation → Execution
C) Implementation → Planning → Analysis → Design → Execution
D) No hay orden

### Q7. (K2, LO 1.5.1) El sesgo de confirmación en testing significa:

A) Que el tester confirma que el sistema funciona
B) Que el tester busca confirmar lo que cree (no lo que podría fallar)
C) Que el tester verifica las hipótesis
D) Que el tester es independiente

### Q8. (K2, LO 1.5.3) ¿Por qué es importante la independencia en testing?

A) Reduce costos
B) Reduce el sesgo de confirmación del developer
C) Aumenta la velocidad
D) Hace que los tests sean más largos

---

## SECCIÓN 2 — Ciclo de Vida (Q9-Q14)

### Q9. (K2, LO 2.1.2) El modelo en V se diferencia del cascada en que:

A) Es más rápido
B) Cada fase de desarrollo tiene su fase de testing对应的对应
C) Es para sistemas chicos
D) No tiene testing

### Q10. (K2, LO 2.1.2) Una rehabilitación por fases (periodoncia → operatoria → prostodoncia) es un ejemplo de:

A) Cascada
B) Modelo V
C) Incremental
D) Big Bang

### Q11. (K2, LO 2.2.1) ¿Cuál es el nivel MÁS ALTO de testing?

A) Component
B) Integration
C) System
D) Acceptance

### Q12. (K3, LO 2.2.3) Después de cambiar el software, se hace un test que verifica que los presupuestos que antes se creaban bien, **siguen** creándose bien. ¿Qué tipo es?

A) Confirmation
B) Regression
C) Smoke
D) Sanity

### Q13. (K2, LO 2.4.1) El navegador Chrome se actualizó y el software de turnos dejó de funcionar. ¿Qué tipo de testing se aplica?

A) Regression testing
B) Confirmation testing
C) Maintenance testing
D) Component testing

### Q14. (K2, LO 2.3.1) El "smoke testing" verifica:

A) Si hay humo en el sistema
B) Si las funciones básicas funcionan
C) Si el sistema es seguro
D) Si el sistema es rápido

---

## SECCIÓN 3 — Pruebas Estáticas (Q15-Q18)

### Q15. (K2, LO 3.1.1) ¿Cuál de las siguientes es static testing?

A) Ejecutar el software
B) Revisar el código sin ejecutarlo
C) Hacer performance testing
D) Hacer user acceptance testing

### Q16. (K2, LO 3.2.1) ¿Cuál de los siguientes work products NO se puede revisar con static testing?

A) Requisitos
B) Código fuente
C) Manuales de usuario
D) Datos en tiempo de ejecución

### Q17. (K2, LO 3.3.2) Una auditoría de historias clínicas con checklist, roles definidos y proceso formal es:

A) Informal review
B) Walkthrough
C) Technical review
D) Inspection

### Q18. (K2, LO 3.3.2) Un colega te pasa un documento y te pide opinión informal, sin proceso. ¿Qué tipo de revisión es?

A) Informal review
B) Walkthrough
C) Technical review
D) Inspection

---

## SECCIÓN 4 — Técnicas de Diseño ⭐ (Q19-Q30)

### Q19. (K2, LO 4.1.2) ¿Cuál de estas NO es una técnica black-box?

A) Equivalence Partitioning
B) Boundary Value Analysis
C) Statement Coverage
D) Decision Table

### Q20. (K3, LO 4.2.1) Una regla dice: "Si la presión sistólica es < 90 o > 140, generar alerta". ¿Cuántas particiones de equivalencia?

A) 2 (normal y anormal)
B) 3 (baja, normal, alta)
C) 4 (baja, normal-baja, normal-alta, alta)
D) 5

### Q21. (K3, LO 4.2.2) Una regla dice: "Aceptar edad entre 18 y 65 años". ¿Qué valores testarías con BVA?

A) 17, 18, 19, 64, 65, 66
B) 18, 65
C) 25, 45
D) 1, 100

### Q22. (K3, LO 4.3.3) Una decisión dice: "Aprobar si (es dentista) Y (tiene CIPA) Y (no tiene sanciones)". ¿Cuántas combinaciones?

A) 3
B) 6
C) 8
D) 9

### Q23. (K3, LO 4.3.1) ¿Cuál de los siguientes valores pertenece a una partición INVÁLIDA para "edad entre 0-120"?

A) 0
B) 50
C) 120
D) 150

### Q24. (K3, LO 4.4.1) Una historia clínica digital tiene los estados: [Borrador] → [Firmada] → [Cerrada]. ¿Cuál transición es inválida?

A) Borrador → Firmada
B) Firmada → Cerrada
C) Cerrada → Firmada
D) Borrador → Cerrada

### Q25. (K2, LO 4.5.1) Error guessing se basa en:

A) Documentación
B) Standards ISO
C) La experiencia del tester
D) Generación automática

### Q26. (K2, LO 4.5.2) Exploratory testing es útil cuando:

A) Hay documentación completa
B) Hay poco tiempo y poca documentación
C) El sistema es pequeño
D) Hay muchos testers

### Q27. (K2, LO 4.5.3) El checklist pre-quirúrgico de la OMS es un ejemplo de:

A) Error guessing
B) Exploratory testing
C) Checklist-based testing
D) Decision table testing

### Q28. (K3, LO 4.5.4) Si tenés que testear las transiciones de un workflow, ¿qué técnica es la MÁS apropiada?

A) EP
B) BVA
C) Decision Table
D) State Transition

### Q29. (K3, LO 4.2.2) Una regla dice "máximo 3 intentos de login". ¿Qué valores testarías con BVA?

A) 0, 1, 2, 3, 4, 5
B) 1, 2, 3
C) 3
D) 0, 1, 3

### Q30. (K3, LO 4.3.3) ¿Cuántas condiciones tiene como mínimo una decision table útil?

A) 1
B) 2
C) 3
D) No hay mínimo

---

## SECCIÓN 5 — Gestión de Testing (Q31-Q36)

### Q31. (K2, LO 5.1.2) Los "criterios de salida" en un test plan definen:

A) Cuándo empezar a testear
B) Cuándo dejar de testear
C) Quién va a testear
D) Qué se va a testear

### Q32. (K2, LO 5.3.1) Si un defecto tiene alta probabilidad pero bajo impacto, su riesgo es:

A) Alto
B) Medio
C) Bajo
D) No se puede saber

### Q33. (K2, LO 5.3.3) En el ciclo de vida de un defecto, ¿cuál es el orden correcto?

A) Abierto → Cerrado → Asignado → Resuelto
B) Nuevo → Asignado → En progreso → Resuelto → Cerrado
C) Cerrado → Resuelto → En progreso
D) No hay orden

### Q34. (K3, LO 5.2.2) El "tiempo medio de resolución de defectos" es una métrica de:

A) Producto
B) Proceso
C) Proyecto
D) Equipo

### Q35. (K2, LO 5.3.2) Configuration management NO incluye:

A) Control de versiones del código
B) Control de versiones de los tests
C) Control de versiones de los datos de prueba
D) Control de versiones del usuario

### Q36. (K2, LO 5.3.5) ¿Cómo contribuye el testing al éxito del proyecto?

A) Eliminando todos los defects
B) Dando información sobre la calidad y el riesgo, ayudando a tomar decisiones
C) Garantizando que el proyecto termine a tiempo
D) Reemplazando al developer

---

## SECCIÓN 6 — Herramientas (Q37-Q40)

### Q37. (K2, LO 6.1.1) ¿Cuál es una herramienta de bug tracking?

A) Selenium
B) Jira
C) SonarQube
D) Jenkins

### Q38. (K2, LO 6.1.1) Jenkins, GitHub Actions y GitLab CI son ejemplos de:

A) Bug tracking
B) Test execution
C) CI/CD / DevOps
D) Static analysis

### Q39. (K2, LO 6.3.1) Los 6 pasos para adoptar una herramienta son:

A) Comprar → instalar → usar
B) Assessment → PoC → Selection → Pilot → Rollout → Review
C) Pilot → Rollout
D) Assessment → Rollout

### Q40. (K2, LO 6.1.2) ¿Cuál es el riesgo principal de la automatización de tests?

A) Falsa sensación de cobertura
B) Mayor costo
C) Mayor tiempo
D) Necesidad de más testers

---

## ⏰ STOP — Tu tiempo se acabó

Anotá tu puntaje (sin mirar las respuestas):
**Correctas: ____ / 40**

Ahora mirá [`SAMPLE_EXAM_B_ANSWERS.md`](SAMPLE_EXAM_B_ANSWERS.md) para corregir.
