# Quiz Cap 1 — Fundamentos (versión dental)

> 10 preguntas tipo ISTQB con escenarios odontológicos. Marcar la respuesta correcta.

---

### Pregunta 1

Una odontóloga revisa la historia clínica antes de la primera consulta. Durante la revisión detecta que faltan alergias declaradas y que hay una contradicción entre la fecha de la última consulta y la fecha registrada en la radiografía.

¿Qué tipo de actividad de testing está haciendo?

A) Dynamic testing funcional
B) Static testing (revisión)
C) Regression testing
D) Maintenance testing

<details>
<summary>Respuesta</summary>

**B) Static testing (revisión).** Está revisando un documento (la historia clínica) sin ejecutar nada. No hay paciente presente, no se ejecuta ningún procedimiento.
</details>

---

### Pregunta 2

Un paciente vuelve 5 días después de una endodoncia con dolor a la percusión. La endodoncia fue hecha según el protocolo, pero el paciente ahora tiene dolor.

¿Cómo se llama esto en ISTQB?

A) Defect (fault)
B) Error (mistake)
C) Failure
D) Root cause

<details>
<summary>Respuesta</summary>

**C) Failure.** Es el comportamiento **observable** de un problema. El paciente siente dolor (observable). El defect (la necrosis residual, el conducto omitido, lo que sea) está adentro, no se ve. La failure es lo que el paciente reporta.
</details>

---

### Pregunta 3

En el caso anterior, ¿qué sería el "defect"?

A) El paciente sintió dolor
B) El profesional que hizo la endodoncia
C) El conducto que quedó sin tratar (por ejemplo)
D) El dolor a la percusión

<details>
<summary>Respuesta</summary>

**C) El conducto que quedó sin tratar.** Es la imperfección en el "producto" (el trabajo clínico). No es observable directamente; se manifiesta cuando algo lo activa (en este caso, la masticación post-operatoria).
</details>

---

### Pregunta 4

¿Cuál de los siguientes NO es uno de los 7 principios del testing según ISTQB?

A) Testing shows the presence of defects, not their absence
B) Exhaustive testing is impossible
C) Defects are evenly distributed across the system
D) Early testing saves time and money

<details>
<summary>Respuesta</summary>

**C) Defects are evenly distributed across the system.** Esto es FALSO. ISTQB dice exactamente lo contrario: "Defects cluster together" (Principio 4). Los defectos se concentran en pocas áreas, no están distribuidos parejo.
</details>

---

### Pregunta 5

Una odontóloga dice: "yo ya revisé todo el tratamiento, está perfecto, no puede haber ningún problema". ¿Qué principio del testing está violando con esa actitud?

A) Testing shows presence, not absence
B) Pesticide paradox
C) Exhaustive testing is impossible
D) Testing is context-dependent

<details>
<summary>Respuesta</summary>

**A) Testing shows the presence of defects, not their absence.** El testing puede encontrar problemas, pero NUNCA puede garantizar que no hay ninguno. Su confianza absoluta viola el Principio 1. Además, en el consentimiento informado esto es exactamente lo que se le aclara al paciente.
</details>

---

### Pregunta 6

Un consultorio usa un nuevo sistema de historia clínica electrónica. El sistema funciona perfectamente. Sin embargo, la recepcionista no puede usarlo bien porque la interfaz es muy complicada, y los pacientes se quejan de que el sistema es lento.

¿Qué tipo de testing habría detectado esto ANTES?

A) Functional testing
B) Non-functional testing (usability, performance)
C) Component testing
D) Regression testing

<details>
<summary>Respuesta</summary>

**B) Non-functional testing.** Funcionalmente está bien (hace lo que tiene que hacer). Lo que falla es cómo lo hace: es difícil de usar (usability) y es lento (performance). Eso son atributos non-functional.
</details>

---

### Pregunta 7

Una endodoncia se completó. Se tomó radiografía final, se confirmó que los conductos estaban obturados correctamente, y se verificó que el paciente no sentía dolor al alta. ¿Qué tipo de testing se hizo?

A) Validation
B) Verification
C) Ambos: verification Y validation
D) Solo testing dinámico

<details>
<summary>Respuesta</summary>

**B) Verification.** Se confirmó que se construyó correctamente (los conductos están bien obturados). Eso es "are we building the product right?". La validation sería: ¿el paciente puede masticar bien a las 2 semanas? ¿desapareció el síntoma original?
</details>

---

### Pregunta 8

Un sistema de software para consultorios dentales. ¿Cuál de las siguientes es una actividad de QA (Quality Assurance), no de testing (Quality Control)?

A) Definir el protocolo de validación de endodoncias
B) Ejecutar pruebas de vitalidad en cada paciente
C) Realizar el sondaje periodontal
D) Tomar la radiografía final

<details>
<summary>Respuesta</summary>

**A) Definir el protocolo de validación de endodoncias.** QA es sobre PROCESOS, no sobre el producto específico. Definir el protocolo es proactivo, sobre procesos. Las otras tres son testing del producto (cada paciente individual).
</details>

---

### Pregunta 9

El equipo de desarrollo de un software para consultorios odontológicos insiste en que ellos mismos van a probar el software porque "ya saben cómo funciona". ¿Qué problema de ISTQB les está pasando?

A) Pesticide paradox
B) Sesgo de confirmación / falta de independencia
C) Defects cluster together
D) Exhaustive testing

<details>
<summary>Respuesta</summary>

**B) Sesgo de confirmación / falta de independencia.** ISTQB recomienda independencia entre el desarrollador y el tester. Los mismos que programaron tienen sesgo de confirmación: quieren ver que funciona, no buscan problemas. La independencia es clave para encontrar defectos.
</details>

---

### Pregunta 10

¿Cuál de estos pares está en el orden correcto de la cadena?

A) Error → Failure → Defect
B) Defect → Error → Failure
C) Error → Defect → Failure
D) Failure → Defect → Error

<details>
<summary>Respuesta</summary>

**C) Error → Defect → Failure.**

- **Error (mistake):** la persona cometió un error (ej: el odontólogo no vio la caries en la radiografía).
- **Defect:** la imperfección está en el producto (ej: la caries progresó porque no se trató).
- **Failure:** el defecto se manifiesta como comportamiento observable (ej: el paciente vuelve con dolor).
</details>

---

## 📊 Puntuación

- **9-10 correctas:** Dominás el Cap 1. Pasá al Cap 2.
- **7-8 correctas:** Bien. Releé las secciones que fallaste.
- **5-6 correctas:** Necesitás repasar. Volvé a leer el cap.
- **< 5:** Releé completo, especialmente los 7 principios y la cadena Error/Defect/Failure.
