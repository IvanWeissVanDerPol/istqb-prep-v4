# 🩺 Autodiagnóstico — ¿Cuánto sabés de QA antes de empezar?

> **15 preguntas para medir tu baseline antes de empezar a estudiar.**
>
> **No es un examen. No se califica. Es para que vos misma veas dónde ya estás y dónde tenés que poner más esfuerzo.**

---

## Instrucciones

1. Hacé las 15 preguntas sin mirar nada.
2. Marcá la respuesta que te parezca correcta.
3. Al final, las respuestas con explicación.
4. Si ya sabés mucho, vas a estudiar más rápido. Si sabés poco, está bien — esta guía está pensada para llevarte de 0 al 65% del examen.

---

## Preguntas

### Q1. Cuando un odontólogo revisa una radiografía antes de tocar la pieza, ¿qué está haciendo?

A) Diagnosticando
B) Testing estático
C) Testing dinámico
D) Cirugía

### Q2. Si un paciente tiene dolor a la percusión 7 días después de una endodoncia "perfecta", ¿qué tipo de "defecto" podría ser?

A) Error humano del odontólogo
B) Defect (algo mal en el trabajo)
C) Failure (lo que ve el paciente)
D) La caries volvió

### Q3. ¿Cuántos principios del testing enumera ISTQB?

A) 3
B) 5
C) 7
D) 10

### Q4. ¿Cuál es la diferencia entre Verification y Validation?

A) Verification = manual; Validation = automático
B) Verification = ¿hicimos bien?; Validation = ¿es lo que necesita el usuario?
C) No hay diferencia, son sinónimos
D) Verification es para programadores; Validation es para testers

### Q5. ¿Cuál de estos es un ejemplo de "regression testing" en odontología?

A) El paciente volvió y el dolor desapareció después del retratamiento
B) El paciente volvió y los síntomas originales (dolor, inflamación) volvieron después de un tratamiento que parecía exitoso
C) Se tomó una radiografía final para confirmar el tratamiento
D) Se firmó el consentimiento informado

### Q6. ¿Qué tipo de testing se hace ANTES de ejecutar el software?

A) Dynamic testing
B) Static testing
C) Acceptance testing
D) Performance testing

### Q7. Si una regla de software dice "los mayores de 65 años reciben 20% de descuento", ¿cuántos grupos (particiones) de pacientes hay?

A) 1 (todos los pacientes)
B) 2 (menor a 65, mayor o igual a 65)
C) 3 (jóvenes, adultos, mayores)
D) Imposible saber

### Q8. En la misma regla, ¿qué valores testarías para encontrar defectos en los bordes?

A) 25, 45, 65, 85
B) 64, 65, 66
C) 1, 50, 100
D) No se testea, es regla lógica

### Q9. Si una decisión depende de 3 condiciones booleanas (sí/no), ¿cuántas combinaciones posibles hay?

A) 3
B) 6
C) 8
D) 9

### Q10. ¿Qué tipo de revisión es un ateneo clínico donde un residente presenta un caso?

A) Informal review
B) Walkthrough
C) Technical review
D) Inspection

### Q11. ¿Qué es "risk-based testing"?

A) Testear todo con máxima prioridad
B) Priorizar testing por probabilidad × impacto
C) Testear solo lo que tiene bugs
D) Testear después de que se cae el sistema

### Q12. ¿Cuál es la diferencia entre "severidad" y "prioridad" de un defecto?

A) Severidad = impacto técnico; Prioridad = urgencia de resolución
B) Severidad = para devs; Prioridad = para users
C) Sinónimos
D) Severidad = bugs; Prioridad = fallas

### Q13. ¿Qué es una "false negative" en testing?

A) El test dice "hay bug" cuando no hay
B) El test dice "no hay bug" cuando sí hay
C) El test pasó
D) El test falló por timeout

### Q14. ¿Cuántas categorías de herramientas de testing reconoce ISTQB?

A) 3
B) 5
C) 8
D) 12

### Q15. ¿Por qué es importante la INDEPENDENCIA en testing?

A) Para que el tester no se aburra
B) Porque el desarrollador tiene sesgo de confirmación sobre su propio código
C) Para pagar menos
D) Para usar más herramientas

---

## 📊 Respuestas y diagnóstico

<details>
<summary><b>Click para ver respuestas</b></summary>

| Q | Respuesta | Explicación corta |
|---|---|---|
| 1 | **B)** Testing estático | Revisa documentos (radiografía) sin ejecutar nada (sin tocar la pieza) |
| 2 | **C)** Failure | Es el comportamiento **observable** del paciente |
| 3 | **C)** 7 | Los 7 principios (memorizarlos) |
| 4 | **B)** | Verification = ¿lo hicimos bien?; Validation = ¿es lo correcto? |
| 5 | **B)** | Si vuelven los síntomas originales después del tratamiento, hay regression |
| 6 | **B)** Static testing | Sin ejecutar |
| 7 | **B)** 2 | Particiones por comportamiento: <65 (no descuento), ≥65 (sí descuento) |
| 8 | **B)** 64, 65, 66 | BVA testea los bordes |
| 9 | **C)** 8 | 2³ = 8 combinaciones |
| 10 | **B)** Walkthrough | El autor (residente) presenta, el grupo pregunta |
| 11 | **B)** | Priorizar por riesgo |
| 12 | **A)** | Impacto técnico vs urgencia |
| 13 | **B)** | Falso negativo = no detectar bug que existe |
| 14 | **C)** 8 | 8 categorías de herramientas |
| 15 | **B)** | Independencia = menos sesgo de confirmación |

---

## 📊 Tu diagnóstico

**Contá cuántas acertaste (no te castigues si fueron pocas):**

| Puntaje | Diagnóstico | Plan |
|---|---|---|
| **13-15** | Ya sabés bastante ISTQB. Probablemente sos QA disfrazada. | Vas a estudiar rápido. Saltá el Cap 1 si querés. |
| **10-12** | Buena base. Te faltan los formalismos. | Estudio normal: 6-8 semanas. |
| **6-9** | Conceptos generales pero no específicos. | Estudio detallado: 8 semanas, sin saltear nada. |
| **0-5** | Arrancás de cero pero con toda la experiencia clínica a favor. | Estudio paso a paso, 10-12 semanas. No te apures. |

**Lo importante:** **no importa tu puntaje.** Esta guía está diseñada para llevarte al 65%+ del examen oficial, sin importar de dónde arranques. La experiencia clínica que ya tenés es tu ventaja.

---

## 📝 Anotá tu puntaje acá

```
Mi puntaje: ____ / 15
Fecha: ___________
Capítulo donde más me cuesta: ___________
```

Después de estudiar los 6 capítulos, repetí este test (o el [`../08_quizzes_dentales/QUIZ_DIAGNOSTICO_INICIAL.md`](../08_quizzes_dentales/QUIZ_DIAGNOSTICO_INICIAL.md) es similar). Deberías haber mejorado al menos 5 puntos.
