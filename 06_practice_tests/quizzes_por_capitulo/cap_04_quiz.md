# Quiz Cap 4 — Test Analysis and Design (v4.0.1)

> **30 preguntas** — meta: **≥75% (23/30)** ⚠️ Cap más pesado del examen
> Tiempo recomendado: 40 minutos
> K-levels cubiertos: K2 + K3 (este es el único cap con K3)

---

## 🟢 Pregunta 1 — K2 Black-box overview
**LO 4.1.1 — ¿Cuál de las siguientes técnicas NO es black-box?**

A) Equivalence partitioning.
B) Boundary value analysis.
C) Statement testing.
D) Decision table testing.

<details><summary>✅ Respuesta</summary>C

Statement testing es **white-box** (basado en estructura del código).
EP, BVA y decision table son black-box (basados en specs/requisitos).</details>

---

## 🟡 Pregunta 2 — K3 ⭐⭐ EP apply
**LO 4.2.1 — Una página web acepta passwords de 8 a 20 caracteres. ¿Cuáles son las particiones inválidas?**

A) Solo length = 10.
B) length < 8, length > 20.
C) Solo length = 100.
D) length = 8, length = 20.

<details><summary>✅ Respuesta</summary>B

**Particiones:**
- Inválida 1: length < 8 (ej: 5)
- Válida: 8 ≤ length ≤ 20 (ej: 12)
- Inválida 2: length > 20 (ej: 25)

Cada partición inválida requiere **al menos un test**.</details>

---

## 🟡 Pregunta 3 — K3 ⭐⭐ BVA apply
**LO 4.2.2 — Para el mismo campo (password 8-20), ¿qué valores testearías con BVA?**

A) Solo los valores medios.
B) 7, 8, 20, 21.
C) Cualquier valor entre 8-20.
D) 8, 14, 20.

<details><summary>✅ Respuesta</summary>B

**BVA clásico de 4 valores:**
- 7 (b-1): justo abajo del límite inferior — inválido
- 8 (b): límite inferior — válido
- 20 (a): límite superior — válido
- 21 (a+1): justo arriba del límite superior — inválido

Por eso 7, 8, 20, 21.</details>

---

## 🟢 Pregunta 4
**LO 4.2.1 — Si las particiones inválidas se testean combinadas con válidas, ¿qué riesgo aparece?**

A) El test pasa más rápido.
B) **Defect masking** — un bug en una partición oculta otro.
C) Mejor cobertura.
D) No hay riesgo.

<details><summary>✅ Respuesta</summary>B

**Bug masking** = un failure en una partición oculta la causa de otro test. Por eso v4.0.1 recomienda testear **particiones inválidas en isolation** (cambio oficial reciente).</details>

---

## 🟡 Pregunta 5 — K3 Decision Table
**LO 4.2.3 — Un test tiene 4 condiciones (cada una true/false). ¿Cuántas reglas posibles hay?**

A) 4.
B) 8.
C) 16.
D) 256.

<details><summary>✅ Respuesta</summary>C

**2^n** combinaciones posibles donde n = número de condiciones.
- 4 condiciones → 2^4 = 16 reglas posibles.

En la práctica se eliminan reglas no-alcanzables o equivalentes (simplificación).</details>

---

## 🟢 Pregunta 6
**LO 4.2.4 — En state transition testing, ¿qué representa el "state diagram"?**

A) Solo los estados sin conexiones.
B) Estados + transiciones + eventos + acciones.
C) Una clase UML.
D) Una decisión binaria.

<details><summary>✅ Respuesta</summary>B

**State diagram (antes "state transition diagram"):**
- **Estados** — condiciones que puede tener el sistema
- **Transiciones** — paso de un estado a otro
- **Eventos** — disparan transiciones
- **Acciones** — qué hace el sistema en cada transición</details>

---

## 🟡 Pregunta 7
**LO 4.2.4 — ¿Cuál es la diferencia entre "0-switch" y "1-switch" coverage?**

A) 0-switch es más exhaustivo.
B) 0-switch cubre transiciones individuales; 1-switch cubre **pares consecutivos** de transiciones.
C) 1-switch es opcional.
D) Solo se usa 0-switch.

<details><summary>✅ Respuesta</summary>B

- **0-switch coverage:** cada transición individual cubierta
- **1-switch coverage:** cada par consecutivo de transiciones cubierto (más fuerte)

Cuanto más alto el número de switches, más cobertura pero más tests.</details>

---

## 🟢 Pregunta 8
**LO 4.3.1 — ¿Qué mide "statement coverage"?**

A) % de branches ejecutados en ambos sentidos.
B) % de statements ejecutados al menos una vez.
C) % de líneas en tests.
D) % de requisitos cubiertos.

<details><summary>✅ Respuesta</summary>B

Statement coverage = (statements ejecutados) / (total statements) × 100.

Coverage completo de statements no implica branches cubiertos (e.g. una línea `if` está ejecutada aunque el `if` siempre sea true).</details>

---

## 🟢 Pregunta 9
**LO 4.3.2 — ¿Por qué "branch coverage" es generalmente más fuerte que "statement coverage"?**

A) Porque considera líneas no ejecutadas.
B) Porque requiere que cada decisión se evalúe **a true y false**.
C) Porque es más rápida.
D) Porque es manual.

<details><summary>✅ Respuesta</summary>B

100% branch coverage implica 100% statement coverage. La inversa NO es cierta.
Para `if (x>5) y=10`:
- Statement coverage 100% si corre el path `x>5`
- Branch coverage 100% requiere correr ambos: `x>5` y `x≤5`</details>

---

## 🟢 Pregunta 10
**LO 4.4.1 — ¿Cuál describe mejor "error guessing"?**

A) Técnica basada en probar inputs aleatorios.
B) Técnica donde el tester adivina dónde podría haber defects basándose en experiencia.
C) Método de testing estructural.
D) Automatización.

<details><summary>✅ Respuesta</summary>B

**Error guessing** = el tester usa su experiencia de bugs pasados para **adivinar** dónde aparecerán nuevos bugs. Funciona muy bien combinada con técnicas formales (no como sustituto).

**Ejemplo típico:** "Si divido por cero", "Si meto comillas en input numérico", "Si año es bisiesto".</details>

---

## 🟢 Pregunta 11
**LO 4.4.2 — ¿Qué es "exploratory testing"?**

A) Testing sin documentación.
B) Testing que combina diseño, ejecución y aprendizaje en paralelo, sin specs detalladas.
C) Testing automatizado.
D) Probar aleatoriamente.

<details><summary>✅ Respuesta</summary>B

**Exploratory testing:**
- Diseño y ejecución **simultáneos**
- Aprendés del sistema mientras lo testeás
- Sesiones con **charter** (objetivo) + **timebox** (límite) + **notas**
- Útil cuando no hay specs claras o para descubrir bugs inesperados

**NO es** testing aleatorio: hay charter y método.</details>

---

## 🟢 Pregunta 12
**LO 4.4.3 — ¿Cuál describe mejor "checklist-based testing"?**

A) Testear items basados en checklists predefinidos.
B) Testing ad-hoc.
C) Testing automatizado.
D) Testing de UI.

<details><summary>✅ Respuesta</summary>A

Checklists = listas de verificación predefinidas. Garantiza coherencia entre testers, sin necesidad de reescribir test cases cada vez. Buena opción cuando hay variedad de items.</details>

---

## 🟡 Pregunta 13 — K2 User Stories ⭐ NUEVO
**LO 4.5.1 — ¿Cuál de los siguientes NO es típico de una user story bien escrita?**

A) "Como <rol>, quiero <acción>, para <beneficio>"
B) Long description técnica detallada.
C) Acceptance criteria.
D) Discusión con el equipo.

<details><summary>✅ Respuesta</summary>B

**User story bien escrita** = "INVEST":
- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

NO debe ser un documento técnico largo. Las user stories son **placeholders para conversaciones**.</details>

---

## 🟡 Pregunta 14 — K2 Acceptance Criteria ⭐ NUEVO
**LO 4.5.2 — ¿Cuál de las siguientes NO es una opción para escribir acceptance criteria?**

A) Given-When-Then format.
B) Checklist format.
C) Scenario format.
D) Compiled binary code.

<details><summary>✅ Respuesta</summary>D

**Opciones oficiales:**
- **Given-When-Then** (BDD-style)
- **Checklist**
- **Scenario-based**

NO se "compila" acceptance criteria (eso es testing automatizado).</details>

---

## 🟡 Pregunta 15 — K3 ⭐⭐ ATDD apply NUEVO
**LO 4.5.3 — ¿Cuál describe mejor ATDD?**

A) Acceptance tests escritos ANTES del código, colaborativamente.
B) Code review después de tests.
C) Integration testing automatizado.
D) Manual acceptance test post-delivery.

<details><summary>✅ Respuesta</summary>A

**ATDD = Acceptance Test-Driven Development**
- Equipo (dev + test + business) escribe acceptance tests **ANTES** del código
- Tests fallan al inicio (no hay código)
- Se implementa hasta que pasen
- Sinonimia: "Story Test-Driven Development" (SDD)</details>

---

## 🟢 Pregunta 16
**LO 4.5.3 — En ATDD, ¿cuál es la diferencia principal con TDD?**

A) ATDD no tiene tests.
B) ATDD usa business language para tests; TDD los escribe un developer solo.
C) TDD es para acceptance.
D) No hay diferencia.

<details><summary>✅ Respuesta</summary>B

- **TDD:** developer escribe tests unitarios ANTES del código
- **ATDD:** equipo completo (3 amigos: dev+test+business) escribe acceptance tests en lenguaje de negocio

ATDD es a **nivel de acceptance** (E2E), TDD a nivel **unitario**.</details>

---

## 🟢 Pregunta 17
**LO 4.2.4 — Si una ATM tiene 4 estados posibles, ¿cuál es el máximo práctico de transiciones en un state diagram?**

A) 2.
B) 4.
C) 12.
D) 16.

<details><summary>✅ Respuesta</summary>C

**n*(n-1) = 4*3 = 12 transiciones posibles** como máximo (si cada estado puede transicionar a todos los demás).
Pero en la práctica son menos por restricciones del dominio.</details>

---

## 🟢 Pregunta 18
**LO 4.3.3 — ¿Cuál NO es valor del white-box testing?**

A) Encuentra código no testeado.
B) Útil en componentes críticos.
C) Reemplaza al black-box.
D) Encuentra código muerto.

<details><summary>✅ Respuesta</summary>C

White-box **complementa** al black-box, NO lo reemplaza. Ambos tienen valor:
- White-box: code coverage, código muerto, paths complejos
- Black-box: comportamiento, requisitos</details>

---

## 🟡 Pregunta 19 — K3 ⭐⭐ BVA apply
**LO 4.2.2 — Un campo acepta valores 10.00 a 99.99. ¿Cuál de los siguientes es el conjunto de BVA CORRECTO?**

A) 9.99, 10.00, 99.99, 100.00.
B) 10.00, 50.00, 99.99.
C) 9.99, 10.01, 99.99.
D) 0.00, 10.00, 100.00.

<details><summary>✅ Respuesta</summary>A

BVA clásico:
- Borde inferior - 0.01 → 9.99 (inválido)
- Borde inferior → 10.00 (válido)
- Borde superior → 99.99 (válido)
- Borde superior + 0.01 → 100.00 (inválido)

Ajustado a `+0.01` por la precisión decimal.</details>

---

## 🟡 Pregunta 20 — K3 EP apply
**LO 4.2.1 — Una función clasifica edad así: <13 niño, 13-18 adolescente, 18-65 adulto, >65 senior. ¿Cuántas particiones equivalentes hay?**

A) 2.
B) 4.
C) 8.
D) 10.

<details><summary>✅ Respuesta</summary>B

**4 particiones:**
1. <13 (niño) — inválida para "adolescente"
2. 13-18 (adolescente) — válida
3. 18-65 (adulto) — válida
4. >65 (senior) — válida

EP elegiría 1 valor por partición → 4 tests (vs. potencialmente 100+).</details>

---

## 🟢 Pregunta 21
**LO 4.2.1 — En EP, ¿se necesita testear múltiples valores en la misma partición?**

A) Sí, porque cada valor es único.
B) No, si los valores de la misma partición deben comportarse igual.
C) Solo si la partición es inválida.
D) Solo si tiene muchos elementos.

<details><summary>✅ Respuesta</summary>B

Por definición de EP, los valores dentro de una partición se comportan igual. Si uno falla, todos fallarían. Por eso un solo valor por partición es suficiente.</details>

---

## 🟢 Pregunta 22
**LO 4.4.1 — ¿Por qué "error guessing" se considera una técnica experience-based?**

A) Porque usa herramientas automatizadas.
B) Porque depende de la intuición y experiencia del tester.
C) Porque se basa en specs.
D) Porque requiere grafos.

<details><summary>✅ Respuesta</summary>B

Error guessing = técnica **experience-based**. NO usa herramientas ni specs formales — depende de la **intuición** y **experiencia pasada** del tester. Las listas comunes se vuelven checklists implícitas.</details>

---

## 🟢 Pregunta 23
**LO 4.2.3 — Decision table testing es más útil cuando:**

A) Hay inputs independientes.
B) Combinaciones de inputs producen distintas acciones (lógica compleja).
C) Hay pocos inputs.
D) Hay tests visuales.

<details><summary>✅ Respuesta</summary>B

Las decision tables brillan con **combinaciones de entradas** que generan **distintas acciones** según combinaciones específicas.
Si los inputs son independientes, EP/BVA son más simples.</details>

---

## 🟢 Pregunta 24
**LO 4.5.1 — Una buena user story sigue INVEST. ¿Qué significa la "I"?**

A) Interesante.
B) Independent (no depende de otras stories).
C) Internacional.
D) Internacionalizable.

<details><summary>✅ Respuesta</summary>B

**INVEST:**
- **I**ndependent — autosuficiente
- **N**egotiable — no es contrato rígido
- **V**aluable — entrega valor al usuario
- **E**stimable — se puede estimar esfuerzo
- **S**mall — cabe en un sprint
- **T**estable — se puede definir como pasa/falla</details>

---

## 🟢 Pregunta 25
**LO 4.3.1 — Una función tiene 100 statements y un test los ejecuta todos. ¿Cuál es el statement coverage?**

A) 0%.
B) 50%.
C) 100%.
D) Depende del branch coverage.

<details><summary>✅ Respuesta</summary>C

Por definición, si todos los statements se ejecutaron, la cobertura es 100%.

**Pero atención:** 100% statement NO significa 0 bugs. Podés tener branches no testeados, condiciones lógicas nunca falsas, etc.</details>

---

## 🟡 Pregunta 26 — K3 Decision Table apply
**LO 4.2.3 — El sistema accede al sitio si username válido AND password válido. ¿Cuántas reglas mínimas tiene una decision table mínima?**

A) 1.
B) 2.
C) 3.
D) 4.

<details><summary>✅ Respuesta</summary>B

**Estructura:**
- Regla 1: User válido + password válido → acceso OK
- Regla 2: Cualquier combinación inválida → acceso denegado (puede simplificarse en una sola regla "any other")

Con colapso (simplificación) → 2 reglas.</details>

---

## 🟢 Pregunta 27
**LO 4.4.2 — En session-based exploratory testing, ¿qué contiene el charter?**

A) El ambiente de testing.
B) Un objetivo claro, duración y alcance.
C) Los casos de prueba detallados.
D) Las expectativas de stakeholders.

<details><summary>✅ Respuesta</summary>B

**Charter = misión de la sesión:** qué objetivo tiene, cuánto tiempo (timebox), qué se va a explorar (scope). NO incluye casos detallados — la ejecución los va descubriendo.</details>

---

## 🟢 Pregunta 28
**LO 4.2.4 — Para un sistema con 6 estados y 8 transiciones documentadas, ¿qué coverage mínimo esperás?**

A) 100% (todas cubren).
B) 75-80% típicamente con 0-switch.
C) 50%.
D) No se puede estimar.

<details><summary>✅ Respuesta</summary>B

La coverage real depende de cuántos tests se ejecutan. 0-switch = cada transición ejecutada. Lograr 100% es posible con suficientes tests. En la práctica 75-80% es común en early testing.</details>

---

## 🟢 Pregunta 29
**LO 4.5.3 — En ATDD, ¿quién participa en escribir los acceptance tests?**

A) Solo developers.
B) Solo testers.
C) Un equipo de 3 personas representando a developers, testers y business representatives.
D) Solo el PO.

<details><summary>✅ Respuesta</summary>C

ATDD es **trabajo en equipo**. Los "3 amigos":
- **Developer** — cómo se implementa
- **Tester** — qué podría fallar
- **Business representative** — qué necesita el negocio

Esto reduce malentendidos y captura requisitos reales.</details>

---

## 🟢 Pregunta 30
**LO 4.1.1 — ¿Cuál describe la diferencia principal entre black-box y white-box?**

A) Black-box se ejecuta más rápido.
B) Black-box testea desde la perspectiva de las specs/inputs; white-box testea desde la estructura interna.
C) Black-box es manual; white-box es automatizado.
D) No hay diferencia.

<details><summary>✅ Respuesta</summary>B

- **Black-box:** testea SIN conocimiento del código. Inputs + outputs según spec.
- **White-box:** testea CON conocimiento del código. Coverage de statements/branches/conditions.

Ambas son válidas y complementarias.</details>

---

## 📊 Scoring

- **27-30 correctas:** Dominás las técnicas
- **23-26 correctas:** Aprobado, estudiá los fallidos
- **18-22 correctas:** Necesitás más práctica manual con EP/BVA
- **<18:** Repasá los summaries, volvé a leer capítulo 4 del syllabus

## 🎯 Diagnóstico

| Si fallaste en Q | Repasá |
|---|---|
| 2, 3, 19, 20 | EP y BVA — practicá más con lápiz y papel |
| 5, 23, 26 | Decision Tables — dibujá matrices |
| 6, 7, 17, 28 | State Transition — diseñá diagramas |
| 8, 9, 18, 25, 30 | White-box — confundís coverage |
| 10, 11, 12, 22 | Experience-based — entender cuándo aplicar |
| 13, 14, 24, 29 | **NUEVO v4.0** — User stories y ATDD |
| 15, 16 | **K3 apply** — ATDD/TDD |

## 🛠️ Ejercicios prácticos recomendados

Después de este quiz, hacé estos ejercicios en papel:

1. **EP + BVA:** Dado un campo edad (18-99), derivá tests con ambas técnicas.
2. **Decision table:** Diseña una para "descuento VIP > $1000".
3. **State diagram:** Diseña para una máquina expendedora.
4. **Coverage:** Dado un programa con 3 `if`s, calculá el mínimo de tests para 100% branch.
