# Quiz Cap 5 — Gestión de Testing (versión dental)

> 10 preguntas tipo ISTQB.

---

### Pregunta 1

Un software de turnos tiene 50 funcionalidades. Tenés tiempo para testear solo 20. ¿Qué criterio de selección aplicás?

A) Risk-based testing: priorizá las 20 de mayor riesgo
B) Testear las más fáciles primero
C) Testear las 20 primeras del manual de usuario
D) Testear al azar

<details>
<summary>Respuesta</summary>

**A) Risk-based testing.** Priorizá por riesgo = probabilidad × impacto. Las funciones críticas (registro de pacientes, historia clínica, facturación) van primero.
</details>

---

### Pregunta 2

¿Cuál de los siguientes NO es típicamente parte de un test plan?

A) Cronograma de testing
B) Recursos necesarios
C) El código fuente completo del sistema
D) Criterios de entrada y salida

<details>
<summary>Respuesta</summary>

**C) El código fuente completo del sistema.** Un test plan NO contiene el código fuente. Contiene el plan de cómo se va a testear. El código va en otros documentos.
</details>

---

### Pregunta 3

La densidad de defectos (defects/KLOC) es una métrica de:

A) Proceso
B) Producto
C) Proyecto
D) Personal

<details>
<summary>Respuesta</summary>

**B) Producto.** Mide la calidad del PRODUCTO (cuántos defectos tiene por unidad de tamaño). Una métrica de proceso sería, por ejemplo, el tiempo medio de resolución de defectos.
</details>

---

### Pregunta 4

¿Cuál es la diferencia entre severidad y prioridad de un defecto?

A) Severidad es para el desarrollador; prioridad es para el tester
B) Severidad es el impacto técnico; prioridad es el orden de resolución
C) Son sinónimos
D) Severidad es para defects; prioridad es para failures

<details>
<summary>Respuesta</summary>

**B) Severidad = impacto técnico (cuán grave es); Prioridad = cuándo se resuelve.** Un defecto puede tener severidad alta pero prioridad baja (crítico pero no urge arreglarlo ahora), o severidad baja pero prioridad alta (cosmético pero urge para una demo).
</details>

---

### Pregunta 5

Un defecto es "severidad alta" pero "prioridad baja". ¿Cuándo aplica?

A) Defecto crítico en una función que nunca se usa
B) Defecto cosmético en la pantalla principal
C) Defecto crítico en el login que nadie puede usar
D) Defecto en el manual de usuario

<details>
<summary>Respuesta</summary>

**A) Defecto crítico en una función que nunca se usa.** Severidad alta porque si se manifestara, rompería algo. Prioridad baja porque esa función no se usa, así que no urge arreglar.
</details>

---

### Pregunta 6

¿Cuál de las siguientes actividades es parte del Test Monitoring & Control?

A) Recolectar métricas de progreso
B) Definir el alcance del testing
C) Identificar los criterios de entrada
D) Contratar al equipo de testing

<details>
<summary>Respuesta</summary>

**A) Recolectar métricas de progreso.** Monitoring = recoger datos, ver cómo va. Control = tomar acciones. Las otras opciones son de Test Planning.
</details>

---

### Pregunta 7

En configuration management, ¿cuál de los siguientes elementos debe estar bajo control de versiones?

A) El código fuente
B) Los documentos de requisitos
C) Los casos de prueba
D) Todos los anteriores

<details>
<summary>Respuesta</summary>

**D) Todos los anteriores.** Todo lo que se usa en el proyecto debe estar versionado: código, requisitos, tests, datos, herramientas, incluso los documentos. Configuration management es integral.
</details>

---

### Pregunta 8

Estás reportando un defecto en el software de gestión. ¿Cuál es el campo MÁS importante?

A) El nombre del tester
B) Pasos para reproducir
C) La fecha de creación
D) La versión del software

<details>
<summary>Respuesta</summary>

**B) Pasos para reproducir.** Si el desarrollador no puede reproducir el bug, no puede arreglarlo. Los pasos para reproducir son lo más crítico. Las otras opciones son útiles pero secundarias.
</details>

---

### Pregunta 9

Una aseguradora de salud te pide que registres el lote y la fecha de vencimiento de cada material que usás en una restauración. Eso es:

A) Risk management
B) Configuration management
C) Test management
D) Incident management

<details>
<summary>Respuesta</summary>

**B) Configuration management.** Estás controlando la configuración (versión/lote) de cada material que usás. Lo mismo que en software: controlar la versión de cada elemento.
</details>

---

### Pregunta 10

Un test plan tiene "criterios de salida". ¿Qué significa?

A) Cuándo empezar a testear
B) Cuándo dejar de testear
C) Quién va a testear
D) Qué se va a testear

<details>
<summary>Respuesta</summary>

**B) Cuándo dejar de testear.** Los criterios de salida definen cuándo se considera que el testing está completo y se puede cerrar la fase. Ej: "se da por completado el testing cuando se ejecutaron todos los tests planeados y no hay defectos críticos abiertos".
</details>

---

## 📊 Puntuación

- **9-10 correctas:** Dominás el Cap 5. Pasá al Cap 6.
- **7-8 correctas:** Bien.
- **5-6 correctas:** Necesitás repasar.
- **< 5:** Releé completo.
