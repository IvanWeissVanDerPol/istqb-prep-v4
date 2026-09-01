# Quiz Cap 4 — Técnicas de Diseño (versión dental)

> 12 preguntas tipo ISTQB. **Este es el quiz más importante — vale 30% del examen.**

---

### Pregunta 1

Una regla dice: "Los pacientes mayores de 65 años reciben 20% de descuento en su consulta". ¿Cuántas particiones de equivalencia hay?

A) 1 partición
B) 2 particiones (menor a 65, mayor o igual a 65)
C) 3 particiones (menor a 65, igual a 65, mayor a 65)
D) 4 particiones (incluyendo inválidas)

<details>
<summary>Respuesta</summary>

**B) 2 particiones.** Las particiones son grupos donde el comportamiento es el mismo. Hay dos comportamientos: "recibe descuento" (≥65) y "no recibe descuento" (<65). Edad 65 y 64 dan comportamientos distintos pero son parte de la misma partición cada uno, así que 2 particiones. **Pero ojo**: las edades inválidas (negativas, muy altas) son particiones separadas. Si el campo "edad" valida también, podría haber más. La pregunta es sobre la regla del descuento.
</details>

---

### Pregunta 2

Para la regla anterior, ¿qué valores testarías con BVA?

A) 1 y 100
B) 64, 65, 66
C) 30, 50, 70
D) 64 y 65 solamente

<details>
<summary>Respuesta</summary>

**B) 64, 65, 66.** BVA = los bordes. 65 es el borde exacto. 64 (un año menos) y 66 (un año más) son los valores inmediatamente adentro/afuera del borde.
</details>

---

### Pregunta 3

Una decisión clínica dice: "Se prescribe antibiótico si (a) hay infección activa Y (b) no hay alergia al antibiótico". ¿Cuántas combinaciones significativas tiene una decision table completa?

A) 2
B) 4 (2x2)
C) 8 (2x2x2)
D) Imposible saber sin más datos

<details>
<summary>Respuesta</summary>

**B) 4 combinaciones.** 2 condiciones, cada una con 2 valores posibles (SÍ/NO) = 2² = 4.

| Infección | Alergia | ¿Antibiótico? |
|---|---|---|
| NO | NO | NO |
| SÍ | NO | SÍ |
| NO | SÍ | NO |
| SÍ | SÍ | NO (alergia) |

Solo se prescribe cuando ambas son verdaderas. Los demás casos no.
</details>

---

### Pregunta 4

Un software tiene los siguientes estados para una cita: [Programada] → [Confirmada] → [Atendida] → [Pagada]. ¿Cuál de las siguientes es una transición INVÁLIDA?

A) Programada → Confirmada
B) Confirmada → Atendida
C) Atendida → Pagada
D) Pagada → Confirmada

<details>
<summary>Respuesta</summary>

**D) Pagada → Confirmada.** Una cita pagada no puede volver a estado "confirmada" — es una transición inversa inválida. State transition testing busca justamente estas: las transiciones que no deberían existir.
</details>

---

### Pregunta 5

¿Cuál es la diferencia principal entre EP y BVA?

A) EP es para functional testing; BVA es para non-functional testing
B) EP testea los bordes; BVA testea el medio
C) EP testea un valor representativo por partición; BVA testea los valores en los bordes
D) No hay diferencia, son sinónimos

<details>
<summary>Respuesta</summary>

**C) EP testea un valor representativo por partición; BVA testea los valores en los bordes.** EP mira el "qué" (las particiones); BVA mira el "dónde falla" (los bordes).
</details>

---

### Pregunta 6

Un sistema de recordatorios dice: "Si el turno es entre las 6 y las 9 AM, recordatorio el día anterior a las 8 PM". ¿Qué técnica es más apropiada para testear esto?

A) Equivalence partitioning
B) Boundary value analysis (los bordes son 6 AM, 9 AM)
C) Decision table
D) State transition

<details>
<summary>Respuesta</summary>

**B) Boundary value analysis.** Los bordes son críticos: ¿qué pasa a las 5:59 AM? ¿a las 6:00 AM exactos? ¿a las 8:59 AM? ¿a las 9:00 AM exactos? ¿a las 9:01 AM? Esos son los valores a testear.
</details>

---

### Pregunta 7

Estás diseñando tests para un sistema de gestión de obras sociales. El sistema aprueba una autorización si: (a) el paciente tiene obra social activa, Y (b) el tratamiento está cubierto, Y (c) no pasó el período de carencia. ¿Qué técnica es la más apropiada?

A) EP
B) BVA
C) Decision table
D) State transition

<details>
<summary>Respuesta</summary>

**C) Decision table.** Tres condiciones booleanas combinadas. Es el caso clásico de decision table testing.
</details>

---

### Pregunta 8

Una historia clínica digital tiene un campo "Fecha de última consulta". El sistema permite fechas entre 1900 y hoy. ¿Qué valores testarías con BVA?

A) 1900, 1901, hoy-1, hoy, hoy+1
B) 1899, 1900, hoy, hoy+1
C) 1899, 1900, 1950, hoy, hoy+1
D) 1900, hoy

<details>
<summary>Respuesta</summary>

**B) 1899, 1900, hoy, hoy+1.** Los bordes: 1899 (un año antes del mínimo, debe rechazar), 1900 (mínimo exacto, debe aceptar), hoy (máximo exacto, debe aceptar), hoy+1 (un día después, debe rechazar). 1950 no es borde.
</details>

---

### Pregunta 9

Estás testeando un sistema de alertas. La regla es: "Si la presión sistólica es < 90 o > 140, generar alerta". ¿Cuántas particiones de equivalencia?

A) 2 (normal y anormal)
B) 3 (baja, normal, alta)
C) 4 (baja, normal-baja, normal-alta, alta)
D) Imposible, depende del contexto

<details>
<summary>Respuesta</summary>

**B) 3 particiones.** Baja (< 90), Normal (90-140), Alta (> 140). Las tres tienen comportamiento distinto respecto a la alerta.
</details>

---

### Pregunta 10

Una técnica de testing basada en experiencia, donde el tester usa su intuición y experiencia previa para adivinar dónde están los defectos, se llama:

A) Error guessing
B) Exploratory testing
C) Checklist-based testing
D) Decision table

<details>
<summary>Respuesta</summary>

**A) Error guessing.** Es la técnica específica donde adivinás dónde están los defectos basándote en la experiencia.
</details>

---

### Pregunta 11

Estás testeando un nuevo software de gestión. No tenés documentación. Tenés poco tiempo. ¿Qué técnica es la más apropiada?

A) Decision table
B) State transition
C) Exploratory testing
D) BVA

<details>
<summary>Respuesta</summary>

**C) Exploratory testing.** Sin documentación y con poco tiempo, las técnicas formales no aplican. Exploratory es la indicada: diseñar y ejecutar tests simultáneamente, basándose en la intuición.
</details>

---

### Pregunta 12

¿Verdadero o Falso? BVA y EP son técnicas black-box.

A) Verdadero
B) Falso

<details>
<summary>Respuesta</summary>

**A) Verdadero.** Ambas son técnicas black-box: testeás sin mirar el código. Las white-box son las que requieren mirar el código por dentro (como coverage testing).
</details>

---

## 📊 Puntuación

- **11-12 correctas:** Excelente. Dominás las técnicas. Listo para el examen.
- **9-10 correctas:** Muy bien. Revisá los errores.
- **7-8 correctas:** Bien. Releé las secciones que fallaste.
- **< 7:** Necesitás repasar este capítulo en profundidad. Las técnicas de diseño son obligatorias para aprobar.
