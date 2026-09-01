# Cap 4 — Técnicas de Diseño de Tests (versión clínica)

> **Versión ISTQB CTFL v4.0.1 — Sección 4.** Cubre LOs **4.1.1, 4.1.2, 4.2.1, 4.2.2, 4.3.1, 4.3.2, 4.3.3, 4.4.1, 4.4.2, 4.5.1, 4.5.2, 4.5.3, 4.5.4** (13 LOs del capítulo; 4.6.x son técnicas avanzadas no cubiertas acá).
>
> Equivalente a [`../../05_summaries/cap_04_tecnicas_diseno_v4.md`](../../05_summaries/cap_04_tecnicas_diseno_v4.md) del repo principal.
>
> Tiempo de lectura: ~60 minutos (dividido en 4 sesiones). **Capítulo más importante del examen (~30%).**
>
> **Para repaso rápido:** [`CHEATSHEET_CAP4.md`](CHEATSHEET_CAP4.md) (1 página).
>
> **Por qué importa:** este capítulo cubre ~30% del examen. Sin dominar estas técnicas, no aprobás.

---

## Introducción — ¿Por qué necesitamos técnicas?

Si tuvieras que testear **todo** sobre un paciente, no terminarías nunca. Hay que elegir. ¿Qué testeás?

Las **técnicas de diseño de tests** son métodos sistemáticos para elegir **qué tests son más valiosos**. Hay dos grandes familias:

- **Black-box (caja negra):** testear sin saber cómo está hecho por dentro. Solo importa qué entra y qué sale.
- **White-box (caja blanca):** testear mirando el código por dentro.
- **Experience-based:** basado en la intuición y experiencia del tester.

---

## Parte 1 — Equivalence Partitioning (EP) ⭐ MUY PREGUNTADO

### Idea

Dividís los datos de entrada en **grupos (particiones) que se comportan igual**. Testeás **un valor de cada grupo**. Si funciona para uno, funciona para todos los del grupo.

### Ejemplo dental

Estás testeando un sistema de recordatorios de turnos para tu consultorio. La regla es:

> "Si el paciente tiene **60+ años**, recibe recordatorio por **llamada telefónica**."

**Sin EP, ¿cuántos casos testeás?**

- 60 años, 61, 62, 63, 64, 65, 70, 80, 90, 100... infinito. Imposible.

**Con EP:**

| Partición | Valores representativos | ¿Recibe llamada? |
|---|---|---|
| Pacientes < 60 años | 25, 35, 45, 59 | NO |
| Pacientes ≥ 60 años | 60, 61, 70, 80 | SÍ |

Solo testeás **2 valores** (uno de cada grupo). Cubriste toda la lógica.

### Reglas EP

1. **Ambos lados del límite pueden ser particiones separadas** si la regla cambia en el límite
2. **Valores inválidos también son particiones** (ej: edad negativa, edad 200)
3. **Una partición por característica**, no mezclada

### Ejemplo dental 2 — software de historia clínica

Regla: "El campo 'Edad' acepta valores entre 0 y 120".

**Particiones válidas:**
- 0-120 años (caso típico)
- Menores a 0 (inválido: -1, -10)
- Mayores a 120 (inválido: 121, 200)

**Casos de prueba:**
1. Edad = 35 (caso típico válido) → debe aceptar
2. Edad = -1 (inválido por debajo) → debe rechazar con mensaje de error
3. Edad = 200 (inválido por arriba) → debe rechazar con mensaje de error
4. Edad = 0 (borde inferior válido) → debe aceptar
5. Edad = 120 (borde superior válido) → debe aceptar

> 📌 En el examen: te van a dar una especificación y pedirte identificar las particiones. Memorizar: "EP = agrupar por comportamiento equivalente".

---

## Parte 2 — Boundary Value Analysis (BVA) ⭐ MUY PREGUNTADO

### Idea

Los defectos están **en los bordes** (límites) de las particiones, no en el medio. Testeás los valores en el límite exactamente, y los valores justo adentro/afuera.

**Si tu sistema acepta edad entre 0 y 120, testeás:** -1, 0, 1, 119, 120, 121.

### Por qué funciona así

Porque los programadores escriben cosas como:

```python
if edad < 0 or edad > 120:
    error("edad inválida")
```

¿Ven el bug? Es `< 0` y `> 120`, pero ¿qué pasa con edad = 0 y edad = 120? **Eso es lo que BVA testea.** Es donde están los errores.

### Ejemplo dental — fechas

Regla: "El sistema permite cargar turnos para los próximos 60 días".

**BVA:**
- Día -1 desde hoy (ayer, no debería poder cargar) → debe rechazar
- Día 0 (hoy) → sí puede cargar
- Día 1 → sí
- Día 30 → sí (medio)
- Día 59 → sí (borde adentro)
- **Día 60 → sí (borde exacto, justo en el límite)**
- **Día 61 → no (borde afuera)**
- Día 90 → no

> 📌 En el examen: te van a preguntar cómo derivar BVA a partir de EP. Memorizar: "BVA = testar los bordes".

### Diferencia EP vs BVA

| EP | BVA |
|---|---|
| Testear un valor por partición | Testear los bordes de las particiones |
| Mira el "qué" | Mira el "dónde falla" |
| Sirve para cubrir toda la lógica | Sirve para encontrar errores en condiciones límites |

**En la clínica:**
- **EP** es "testeás pacientes adultos vs pediátricos" (cubriste la lógica)
- **BVA** es "testeás justo el paciente que tiene 18 años (justo en el límite de mayoría de edad)" (buscás el error)

**Regla práctica: usá ambas juntas.** EP para elegir grupos, BVA para elegir los valores específicos.

---

## Parte 3 — Decision Table Testing ⭐ MUY PREGUNTADO

### Idea

Cuando una decisión depende de **múltiples condiciones combinadas**, hacés una tabla con todas las combinaciones posibles y testeás cada una.

### Ejemplo dental — sistema de clasificación de urgencia

Estás testeando la lógica de tu software de turnos para asignar prioridad:

| Condición | Turno normal | Turno prioritario | Urgencia |
|---|---|---|---|
| ¿Es paciente con dolor agudo? | No | Sí | Sí |
| ¿Tiene infección activa (flemón, absceso)? | No | No | Sí |
| ¿Viene derivado de urgencia hospitalaria? | No | No | Sí |

**Tabla de decisión:**

| Condición | Caso 1 | Caso 2 | Caso 3 | Caso 4 | Caso 5 |
|---|---|---|---|---|---|
| Dolor agudo | No | Sí | No | Sí | Sí |
| Infección activa | No | No | Sí | Sí | No |
| Derivado hospital | No | No | No | Sí | Sí |
| **→ Prioridad** | **Normal** | **Normal** | **Urgencia** | **Urgencia** | **Urgencia** |

(Las últimas 3 filas son "cubiertas" porque ya tienen la respuesta.)

**Casos de prueba a ejecutar:**
- Caso 1 (sin dolor, sin infección, no derivado) → normal
- Caso 2 (dolor, sin infección, no derivado) → normal
- Caso 3 (sin dolor, con infección, no derivado) → urgencia

Reducimos 8 combinaciones posibles a 3 casos testeables, y aún cubrimos toda la lógica.

### Otro ejemplo dental — aprobación de tratamiento

Regla: "Un tratamiento se aprueba si (a) tiene consentimiento firmado Y (b) el paciente no es alérgico al anestésico Y (c) está dentro del presupuesto del plan".

**Tabla:**

| Condición | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Consentimiento firmado | N | S | N | S | N | S | N | S |
| No es alérgico | N | N | S | S | N | N | S | S |
| Está en presupuesto | N | N | N | N | S | S | S | S |
| **→ ¿Aprobado?** | **No** | **No** | **No** | **No** | **No** | **No** | **No** | **Sí** |

**Decisión:** solo el caso 8 aprueba. Los demás tienen alguna condición fallando. Testeás **1 caso** que aprueba (regla completa) y unos cuantos que rechazan (cada razón individual).

> 📌 En el examen: te van a dar reglas con AND/OR y pedirte la tabla de decisión. Memorizar: "Decision table = combinaciones de condiciones".

---

## Parte 4 — State Transition Testing ⭐ PREGUNTADO

### Idea

Algunos sistemas tienen **estados**. Testeas las **transiciones** entre estados.

### Ejemplo dental — software de historia clínica

Tu historia clínica digital tiene 3 estados para un presupuesto:

```
[Borrador] → [Enviado al paciente] → [Aprobado/Rechazado]
   ↓              ↓                       ↓
editar         ver paciente            activar tratamiento
   ↓              ↓                       ↓
borrar         editar                   cobrar
```

**Diagrama de estados:**

```
                ┌────────────┐
                │ Borrador   │
                └─────┬──────┘
                      │ enviar
                      ▼
            ┌──────────────────┐
            │ Enviado paciente │
            └─┬──────────────┬─┘
              │ aprobar      │ rechazar
              ▼              ▼
        ┌──────────┐    ┌──────────┐
        │ Aprobado │    │Rechazado │
        └─────┬────┘    └──────────┘
              │ activar
              ▼
        ┌──────────────┐
        │ En tratamiento│
        └──────────────┘
```

**Casos de prueba:**
1. Borrador → enviar → Enviado (transición válida)
2. Enviado → aprobar → Aprobado (transición válida)
3. Enviado → rechazar → Rechazado (transición válida)
4. Aprobado → activar → En tratamiento (transición válida)
5. **Aprobado → editar → ??? (transición inválida, debería rechazar)** ← **defecto potencial**
6. Borrador → aprobar → ??? (no se puede aprobar lo que no se envió) ← **defecto potencial**

> 📌 En el examen: te dan un diagrama y te preguntan qué transiciones testear. Memorizar: "STT = estados + transiciones válidas + inválidas".

---

## Parte 5 — Técnicas basadas en experiencia

Cuando no tenés specs formales, o querés complementar las técnicas formales:

### Error Guessing

**Qué:** el tester **adivina** dónde es probable que haya defectos, basado en experiencia.

**En la clínica:**
> Sabés que los pacientes siempre mienten sobre si se cepillan los dientes. Si el sistema pregunta "¿se cepilla los dientes?" y vos querés testearlo, el test más interesante es: paciente dice que sí, pero su historia dice que no. ¿El sistema detecta la inconsistencia?

**Cómo usarlo:**
- Listas de defectos comunes por tipo de sistema
- Tu propia experiencia de bugs pasados

### Exploratory Testing

**Qué:** diseñar y ejecutar tests **simultáneamente**, en tiempo real, sin documentación previa.

**En la clínica:**
> Cuando atendés a un paciente nuevo que tiene algo raro, vos no seguís un protocolo rígido. Explorás. Mirás. Probás. Decidís sobre la marcha.

**Pros:** encuentra defectos que los tests formales no encuentran.
**Contras:** no reproducible, depende del tester.

**Cuándo usarlo:** cuando hay poco tiempo, o cuando el sistema es muy nuevo y no hay specs.

### Checklist-based Testing

**Qué:** una lista de cosas para verificar.

**En la clínica:**
> El checklist pre-quirúrgico de la OMS: "¿Identidad del paciente confirmada? ¿Sitio marcado? ¿Alergias revisadas? ¿Profilaxis antibiótica?". Es un checklist-based test.

**Cuándo usarlo:** para no olvidarse de cosas básicas. Standard en industrias reguladas.

---

## Resumen del Cap 4

✅ Hay 4 técnicas formales: EP, BVA, Decision Table, State Transition.
✅ Hay 3 basadas en experiencia: Error Guessing, Exploratory, Checklist.
✅ **EP** = agrupar por comportamiento. Testear uno por grupo.
✅ **BVA** = testear los bordes de las particiones.
✅ **Decision Table** = combinaciones de condiciones.
✅ **State Transition** = cambios de estado. Testear transiciones válidas e inválidas.
✅ **Este capítulo es 30% del examen.** Dominá las 4 técnicas formales.

---

## Para chequear que entendiste

1. Si una regla es "descuento del 10% para mayores de 65 años", ¿cuántas particiones hay? ¿Qué valores testarías con BVA?
2. ¿Cuál es la diferencia entre EP y BVA? ¿Cuándo usarías cada una?
3. ¿Cuándo conviene Decision Table sobre BVA?
4. ¿Qué es una transición inválida en State Transition? Doy un ejemplo.

Hacé el [`QUIZ_CAP4.md`](../08_quizzes_dentales/QUIZ_CAP4.md) — es el quiz más importante.
