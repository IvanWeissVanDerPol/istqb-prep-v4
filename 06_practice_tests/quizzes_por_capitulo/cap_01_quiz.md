# Quiz Cap 1 — Fundamentals of Testing (v4.0.1)

> **20 preguntas** — meta: **≥80% (16/20)**
> Tiempo recomendado: 25 minutos
> K-levels cubiertos: K1 + K2 (Cap 1 tiene 1 K1, 13 K2)

---

## Pregunta 1
**LO 1.2.3 — ¿Cuál de las siguientes afirmaciones describe mejor la diferencia entre "error", "defect" y "failure"?**

A) Son sinónimos.
B) Un **error** es una acción humana que produce un **defect** (imperfección en el código), el cual puede causar un **failure** durante la ejecución.
C) Un defect es un failure que todavía no se descubrió.
D) Un error es siempre generado por un developer.

<details><summary>✅ Respuesta</summary>B

- **Error (o mistake):** acción humana que produce resultado incorrecto (causa)
- **Defect (o fault, bug):** imperfección en el componente (manifestación del error)
- **Failure:** desviación del componente de su comportamiento esperado (efecto visible)

Los tres NO son sinónimos. Un error puede no generar defects visibles. Un defect puede quedar latente y no causar failures hasta que el path correcto se ejecute.</details>

---

## Pregunta 2
**LO 1.3.1 — ¿Cuál de los siguientes NO es uno de los 7 Principios de Testing?**

A) Testing muestra la presencia de defects, no su ausencia.
B) Testing exhaustivo es posible.
C) El testing temprano ahorra tiempo y dinero.
D) Beware the pesticide paradox.

<details><summary>✅ Respuesta</summary>B

**Trampa clásica.** El principio real es "Testing exhaustivo es **imposible**" (no "es posible"). Este es uno de los siete principios oficiales.</details>

---

## Pregunta 3
**LO 1.4.1 — ¿Cuál de las siguientes actividades pertenece a la fase de "test implementation"?**

A) Evaluar los test items para identificar condiciones testeables.
B) Crear y priorizar test cases, crear test data.
C) Preparar y verificar la ejecución de test suites.
D) Reportar discrepancias como defects.

<details><summary>✅ Respuesta</summary>C

**Orden oficial:**
1. Test planning
2. Test monitoring & control (continuo)
3. Test analysis → identifica condiciones
4. Test design → test cases, data
5. **Test implementation → test procedures/suites** ← acá
6. Test execution → corre tests, registra resultados
7. Test completion → summary report</details>

---

## Pregunta 4
**LO 1.4.4 — ¿Cuál es el valor principal de mantener trazabilidad entre testware?**

A) Permite automatizar todos los tests.
B) Hace posible evaluar la cobertura y entender el impacto de cambios.
C) Reduce el número de defects.
D) Elimina la necesidad de un test plan.

<details><summary>✅ Respuesta</summary>B

**Trazabilidad** = relación entre los elementos de testing (requisitos ↔ test cases ↔ defects ↔ riesgos). Permite:
- Verificar **cobertura** (todos los requisitos testeados)
- **Impact analysis** cuando cambia algo
- Auditoría regulatoria

NO automatiza tests, NO reduce defects por sí mismo, NO reemplaza al test plan.</details>

---

## Pregunta 5
**LO 1.4.5 — ¿Cuál de las siguientes opciones describe mejor la relación entre test manager y test lead?**

A) Son el mismo rol.
B) El test manager gestiona un proyecto de testing; el test lead lidera un equipo específico dentro de él.
C) El test lead reporta al test engineer.
D) El test manager solo se ocupa de tareas técnicas.

<details><summary>✅ Respuesta</summary>B

**Roles oficiales v4.0.1:**
- **Test manager** — gestiona globalmente el proyecto de testing
- **Test lead** — lidera el equipo técnico de testing
- **Tester** — ejecuta tests
- **Test designer** — diseña tests específicos
- **Test automation engineer** — automatiza</details>

---

## Pregunta 6
**LO 1.5.1 — ¿Cuáles de las siguientes son habilidades genéricas requeridas para un buen tester?**

A) Solo habilidades técnicas de testing.
B) Habilidades analíticas, técnicas, conocimiento del dominio, comunicación y atención al detalle.
C) Conocimiento exclusivo del dominio de la aplicación.
D) Habilidades de project management.

<details><summary>✅ Respuesta</summary>B

**Un buen tester necesita múltiples skills:**
- **Analíticas** — pensar lógicamente
- **Técnicas** — herramientas, scripting
- **Dominio** — entender el producto
- **Comunicación** — escribir reports claros, dar feedback
- **Atención al detalle** — ver lo que otros no ven
- **Pensamiento crítico** — cuestionar cosas</details>

---

## Pregunta 7
**LO 1.5.3 — ¿Cuál es el principal beneficio de la independencia en testing?**

A) Elimina la necesidad de comunicación.
B) Detecta defects que el autor podría pasar por alto.
C) Automatiza todos los tests.
D) Reduce el costo de testing.

<details><summary>✅ Respuesta</summary>B

**Independencia** = separación de quien escribió el código de quien lo testea. **A mayor independencia → más efectiva la detección de defects.**

Niveles de independencia (de menor a mayor):
1. Testing por el mismo author
2. Testing por un peer
3. Testing por un test lead
4. Testing por un equipo independiente
5. Testing por un equipo externo

**Drawback:** puede haber barreras de comunicación.</details>

---

## Pregunta 8
**LO 1.1.2 — ¿Cuál es la principal diferencia entre testing y debugging?**

A) Son lo mismo, solo cambia el nombre.
B) Testing es encontrar defects; debugging es localizar y corregir las causas raíz de los defects.
C) Testing lo hace el usuario; debugging el developer.
D) Debugging se hace después del deployment.

<details><summary>✅ Respuesta</summary>B

- **Testing:** actividad técnica que opera un sistema bajo condiciones específicas y observa los resultados
- **Debugging:** actividad de development (NO testing) que localiza la causa raíz de un defect y corrige el código

El testing puede encontrar un failure. El debugging es el proceso de entender POR QUÉ pasó y arreglarlo.</details>

---

## Pregunta 9
**LO 1.2.1 — ¿Por qué el testing es necesario?**

A) Para reducir el tiempo de desarrollo.
B) Para añadir nuevas features.
C) Para detectar defects, reducir riesgos, mejorar la calidad y ayudar a tomar decisiones.
D) Para eliminar la necesidad de tests automatizados.

<details><summary>✅ Respuesta</summary>C

**Objetivos típicos de testing:**
- Evaluar **work products** (requisitos, diseños, código, etc.)
- **Detectar defects** (encuentre errores)
- **Reducir el riesgo** de failures en producción
- **Verificar cumplimiento** de requisitos
- **Mejorar la calidad** global
- **Proveer información** para decisiones
- **Cumplir regulaciones** o contratos
- **Construir confianza** en el producto
- **Validar** que el producto cumple las necesidades del usuario</details>

---

## Pregunta 10
**LO 1.3.1 — El principio "Defects cluster together" significa que:**

A) Los defects se distribuyen uniformemente en el sistema.
B) La mayoría de los defects se encuentran en una pequeña parte del sistema.
C) Los defects solo ocurren en módulos nuevos.
D) Los defects se descubren juntos si se testea con un equipo.

<details><summary>✅ Respuesta</summary>B

Esto es el **Principio de Pareto** aplicado a defects: **80% de defects están en 20% del código**.
Implicación: los módulos con bugs históricos son los que más se deberían testear (riesgo).</details>

---

## Pregunta 11
**LO 1.4.2 — El "contexto" del proyecto impacta el proceso de testing en aspectos como:**

A) La cantidad de bugs solamente.
B) El nivel de rigor, profundidad de documentación, nivel de automatización y elección de técnicas.
C) El lenguaje de programación del producto.
D) La cantidad de developers.

<details><summary>✅ Respuesta</summary>B

**"Testing is context-dependent"** (Principio 6). El contexto (industria, madurez, regulación, riesgos) define:
- **Rigor:** medical software ≠ website
- **Documentación:** regulated vs ágil
- **Automatización:** proyectos cortos vs largos
- **Técnicas:** algunas no aplican a todos los contextos</details>

---

## Pregunta 12
**LO 1.4.3 — ¿Cuál de los siguientes NO se considera "testware"?**

A) Test plan.
B) Test cases y test data.
C) Manual scripts y automated scripts.
D) Production code ejecutándose en producción.

<details><summary>✅ Respuesta</summary>D

**Testware** son los **artefactos producidos durante testing**, NO el producto mismo. Incluye:
- Test plans, test cases, test procedures
- Test data, test scripts (manual y automatizados)
- Defect reports, test logs, test reports
- Traceability matrices

El código de producción ejecutándose NO es testware.</details>

---

## Pregunta 13
**LO 1.5.2 — El "whole team approach" significa que:**

A) Solo un equipo grande se encarga de testing.
B) El quality es responsabilidad de todo el equipo, no solo de los testers.
C) El equipo entero ejecuta tests manuales.
D) El equipo solo automatiza.

<details><summary>✅ Respuesta</summary>B

**Whole team approach** (Approach #5):
- Quality = **responsabilidad de TODO el equipo**
- Testers son coaches/coordinadores
- Developers, business, ops todos participan
- Ejemplo: en agile, el scrum master y developers escriben acceptance tests juntos

Ventaja: menos defectos pasan entre fases, mejor comunicación.</details>

---

## Pregunta 14
**LO 1.3.1 — El "pesticide paradox" significa que:**

A) Los mismos tests aplicados repetidamente dejan de encontrar nuevos defects.
B) Los bugs se acumulan como pesticidas.
C) Los tests automatizados son como químicos.
D) El testing es venenoso para el equipo.

<details><summary>✅ Respuesta</summary>A

**Principio 5:** Si ejecutás los mismos tests una y otra vez, dejarán de encontrar nuevos defects (los defectos "mutan"). Solución: **actualizar/crear nuevos tests** constantemente.</details>

---

## Pregunta 15
**LO 1.2.2 — ¿Cuál es la relación correcta entre QA (Quality Assurance) y testing?**

A) Son sinónimos.
B) QA es un enfoque planificado y proactivo para asegurar calidad; testing es una actividad de QC que verifica la calidad.
C) Testing es la disciplina, QA es la herramienta.
D) QA reemplaza al testing.

<details><summary>✅ Respuesta</summary>B

- **QA (Quality Assurance):** enfoque planificado y preventivo para asegurar procesos → calidad
- **QC (Quality Control):** actividades reactivas para verificar y monitorear la calidad del producto (testing es parte de QC)

QA no reemplaza testing, son cosas distintas (proceso vs verificación).</details>

---

## Pregunta 16
**LO 1.3.1 — "Absence-of-errors is a fallacy" significa que:**

A) No se puede tener cero errors.
B) Un sistema sin defects no es necesariamente útil.
C) El software debe tener errores.
D) Los testers deben aceptar todos los errores.

<details><summary>✅ Respuesta</summary>B

**Principio 7:** Software sin defects (zero defects) ≠ software que satisface necesidades del usuario. Un producto puede estar perfecto técnicamente pero no servir.

Por eso testing debe:
1. Encontrar defects
2. **Verificar requisitos y necesidades**</details>

---

## Pregunta 17
**LO 1.1.1 — ¿Cuál es un objetivo típico de testing?**

A) Demostrar que el sistema no tiene defects.
B) Validar que el sistema cumple requisitos y encontrar defects.
C) Complicar el sistema.
D) Generar bugs intencionalmente.

<details><summary>✅ Respuesta</summary>B

Testear NO es demostrar que el sistema está bien (eso sería tonto, porque siempre quedan defects no encontrados). Testear es:
- **Encontrar defects** (objetivo central)
- **Validar** contra requisitos
- **Reducir riesgo**
- Dar **información** para decisiones</details>

---

## Pregunta 18
**LO 1.2.3 — ¿Cuál de estas secuencias describe mejor la cadena causal?**

A) Defect → error → failure.
B) Error → defect → failure.
C) Failure → defect → error.
D) Son independientes.

<details><summary>✅ Respuesta</summary>B

**Cadena:**
1. **Error (mistake):** persona hace algo mal (humano)
2. → causa un **Defect (fault, bug):** imperfección en el software
3. → si se ejecuta el path con el defect, **Failure:** comportamiento observable

**Ejemplo:** un developer (error humano) escribe una condición incorrecta (defect en el código) que, cuando un usuario hace click, la página falla (failure).</details>

---

## Pregunta 19
**LO 1.4.1 — ¿Cuál de las siguientes tareas es parte del "test completion" activity?**

A) Escribir test cases.
B) Ejecutar tests en paralelo.
C) Compilar el test summary report con lessons learned.
D) Diseñar nuevos test procedures.

<details><summary>✅ Respuesta</summary>C

**Test completion activities:**
- Comprobar que todos los reports estén entregados
- Verificar entry/exit criteria cumplidos
- Documentar **lessons learned**
- Compilar **test summary report**
- Archivar testware para uso futuro

NO incluye escribir nuevos test cases o ejecutarlos.</details>

---

## Pregunta 20
**LO 1.1.2 — ¿Por qué debugging NO se considera testing?**

A) Porque no usa herramientas.
B) Porque es realizado por developers, no testers, y su objetivo es reparar, no detectar.
C) Porque solo se aplica a errores de compilación.
D) Porque debugging es solo análisis estático.

<details><summary>✅ Respuesta</summary>B

**Diferencia clave:**
- **Testing:** detecta symptoms/failures, evalúa el comportamiento del sistema
- **Debugging:** localiza la **causa raíz** del problema y lo corrige (developer)

Aunque están relacionadas, son actividades distintas que pueden ser realizadas por personas diferentes.</details>

---

## 📊 Scoring

- **18-20 correctas:** Excelente, dominás Cap 1
- **15-17 correctas:** Aprobado, repasá puntos débiles
- **10-14 correctas:** Necesitás más estudio
- **<10:** Repasá el summary y reintentá

## 🎯 Si fallaste más de 3, repasá específicamente:

| Pregunta | LO a repasar |
|---|---|
| 1, 18 | 1.2.3 terminología |
| 2, 10, 14, 16 | 1.3.1 7 principios |
| 3, 12, 19 | 1.4.1 actividades |
| 4 | 1.4.4 trazabilidad |
| 5 | 1.4.5 roles |
| 7 | 1.5.3 independencia |
| 8, 20 | 1.1.2 testing vs debugging |
| 11 | 1.4.2 contexto |
