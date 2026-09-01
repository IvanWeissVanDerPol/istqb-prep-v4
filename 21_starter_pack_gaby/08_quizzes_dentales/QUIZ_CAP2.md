# Quiz Cap 2 — Ciclo de Vida (versión dental)

> 10 preguntas tipo ISTQB.

---

### Pregunta 1

Una clínica dental rehabilita a un paciente por fases: primero estabilización periodontal, luego operatoria, luego prostodoncia. ¿A qué modelo de ciclo de vida se parece más?

A) Cascada (Waterfall)
B) Modelo en V
C) Incremental
D) Big Bang

<details>
<summary>Respuesta</summary>

**C) Incremental.** Cada fase es un entregable funcional. El paciente va recibiendo valor incremental: primero puede comer sin dolor, después tiene las piezas tratadas, después tiene la sonrisa restaurada.
</details>

---

### Pregunta 2

Un software de historia clínica está siendo desarrollado. El equipo de testing prueba las pantallas individuales sin conexión al resto del sistema. ¿Qué nivel de testing es?

A) Integration testing
B) Component testing
C) System testing
D) Acceptance testing

<details>
<summary>Respuesta</summary>

**B) Component testing.** Se testea cada pantalla por separado (cada componente). El integration sería probar cómo se conectan entre sí.
</details>

---

### Pregunta 3

El mismo equipo ahora prueba que cuando guardás un paciente en una pantalla, la información aparece correctamente en la pantalla de turnos y en la de facturación. ¿Qué nivel de testing es?

A) Component testing
B) Integration testing
C) System testing
D) Acceptance testing

<details>
<summary>Respuesta</summary>

**B) Integration testing.** Estás probando cómo interactúan los componentes entre sí (paciente ↔ turnos ↔ facturación).
</details>

---

### Pregunta 4

Después de actualizar el software, se hace un test que verifica que los presupuestos que antes se creaban correctamente, **siguen** creándose correctamente. ¿Qué tipo de testing es?

A) Confirmation testing
B) Regression testing
C) Component testing
D) Maintenance testing

<details>
<summary>Respuesta</summary>

**B) Regression testing.** Estás verificando que lo que antes andaba, sigue andando después del cambio.
</details>

---

### Pregunta 5

Un desarrollador corrigió un bug donde el software no aceptaba el caracter "ñ" en los nombres de los pacientes. Después de la corrección, ¿qué test confirma que el bug está arreglado?

A) Regression testing
B) Confirmation testing (re-testing)
C) Smoke testing
D) Maintenance testing

<details>
<summary>Respuesta</summary>

**B) Confirmation testing (re-testing).** Es verificar específicamente que el bug reportado se arregló. Regression sería probar que las OTRA funciones siguen andando bien.
</details>

---

### Pregunta 6

¿Cuál es la diferencia principal entre system testing y acceptance testing?

A) System testing es manual, acceptance testing es automatizado
B) System testing lo hace el equipo de testing; acceptance testing lo hace el cliente/usuario
C) System testing prueba funciones; acceptance testing prueba performance
D) No hay diferencia, son sinónimos

<details>
<summary>Respuesta</summary>

**B)** System testing lo hace el equipo de testing de la organización. Acceptance testing lo hace el cliente o el usuario final (en este caso, vos, la odontóloga, diciendo "OK, lo adopto").
</details>

---

### Pregunta 7

El equipo de testing prueba que la página de login carga en menos de 2 segundos con 100 usuarios concurrentes. ¿Qué tipo de testing es?

A) Functional testing
B) Non-functional testing (performance/load)
C) Change-related testing
D) Component testing

<details>
<summary>Respuesta</summary>

**B) Non-functional testing (performance/load).** Funcionalmente, el login "funciona". Lo que se mide es CÓMO funciona (velocidad bajo carga).
</details>

---

### Pregunta 8

En el modelo en V, ¿qué tipo de testing se corresponde con la fase de "diseño detallado"?

A) Component testing
B) Integration testing
C) System testing
D) Acceptance testing

<details>
<summary>Respuesta</summary>

**B) Integration testing.** En el modelo en V, cada fase de desarrollo tiene su fase de testing对应的对应. Diseño detallado ↔ Integration testing.
</details>

---

### Pregunta 9

¿Qué tipo de testing es el más apropiado cuando se quiere probar el flujo completo: "paciente reserva turno online → confirma → llega al consultorio → firma consentimiento → paga → se retira"?

A) Component testing
B) Integration testing
C) System testing
D) Unit testing

<details>
<summary>Respuesta</summary>

**C) System testing.** Es un end-to-end test, prueba todo el sistema como un todo, no un componente aislado.
</details>

---

### Pregunta 10

Después de 3 años en producción, el navegador Chrome se actualiza y el software de turnos deja de funcionar. ¿Qué tipo de testing se aplica para verificar la nueva compatibilidad?

A) Regression testing
B) Confirmation testing
C) Maintenance testing
D) Component testing

<details>
<summary>Respuesta</summary>

**C) Maintenance testing.** El cambio fue en el ENTORNO (Chrome se actualizó), no en el sistema. Maintenance testing es para cambios en el ambiente, no en el código.
</details>

---

## 📊 Puntuación

- **9-10 correctas:** Dominás el Cap 2. Pasá al Cap 3.
- **7-8 correctas:** Bien. Releé los niveles y tipos.
- **5-6 correctas:** Necesitás repasar. Volvé a leer el cap.
- **< 5:** Releé completo, especialmente la diferencia entre regression y confirmation.
