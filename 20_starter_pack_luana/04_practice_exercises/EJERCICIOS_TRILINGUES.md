# 🌎 Ejercicios Trilingües para Cap 4 — ISTQB CTFL v4.0.1

> **Para:** Luana Benitez
> **Por qué este archivo existe:** Tenés inglés advanced + portugués advanced. Eso es un activo de aprendizaje que pocos paraguayos tienen. Estos ejercicios usan tus tres idiomas (ES/EN/PT) como **andamiaje cognitivo** — leés el problema en tu idioma, lo resolvés, después lo pensás en el otro idioma. Es la misma técnica que usás en interpretación, aplicada a testing.

---

## 🧠 Por qué los ejercicios trilingües funcionan mejor para vos

Hay investigación seria detrás de esto (y lo viviste en Language Line):

1. **Cuando pensás un problema en dos idiomas, los sesgos del primero se rompen en el segundo.** Si una técnica de testing no tiene sentido en español, probablemente la entendiste mal — no es problema del idioma.
2. **Tus switching costs son bajos** (advanced en los tres). Podés alternar sin perder el hilo.
3. **El mercado laboral QA que querés es global.** Estos ejercicios te dan práctica con la nomenclatura que vas a leer en Jira, TestRail y Stack Overflow en inglés — que es donde vive el 95% del contenido QA mundial.

**Cómo usar este archivo:**
- Semana 4 (después del plan de estudio): hacé los ejercicios de "EP y BVA"
- Semana 5 (antes del hard mode): hacé decision tables, state transitions, ATDD
- Si te sobra tiempo: los bonus de localization testing al final

---

## 📚 Bloque 1 — Equivalence Partitioning (EP) — LO 4.2.1

### Ejercicio 1.1 — Edad de jubilación (trilingüe)

**Requisito (ES):** Un sistema permite solicitar jubilación a personas entre 60 y 70 años (inclusive).

**Requisito (EN):** A system allows retirement applications for people between 60 and 70 years old (inclusive).

**Requisito (PT):** Um sistema permite solicitação de aposentadoria para pessoas entre 60 e 70 anos (inclusive).

**Tarea:**
1. Identificá las particiones válidas e inválidas
2. Escribí los tests mínimos (1 valor por partición)
3. Verificá tu respuesta en los 3 idiomas — ¿los 3 describen el mismo dominio?

**Tu respuesta (plantilla):**
```
Particiones:
- Válidas: [        ]
- Inválidas: [      ]

Tests:
1. [        ] → esperado [        ]
2. [        ] → esperado [        ]
...
```

---

### Ejercicio 1.2 — Password de aplicación bancaria

**Requisito (ES):** El password debe tener entre 8 y 20 caracteres, incluir al menos una mayúscula, una minúscula y un dígito.

**Requisito (EN):** Password must be 8-20 characters, include at least one uppercase, one lowercase, and one digit.

**Requisito (PT):** A senha deve ter entre 8 e 20 caracteres, incluir pelo menos uma maiúscula, uma minúscula e um dígito.

**Tarea:**
1. Listá **al menos 6 particiones inválidas** (este requisito tiene muchos casos)
2. Listá **1 partición válida**
3. Escribí 1 test por partición
4. 💡 **Pregunta trampa del ISTQB:** ¿qué pasa si meto una partición inválida junto con una inválida? (Pensá en *defect masking*)

---

### Ejercicio 1.3 — Cupón de descuento de Somosgay

**Contexto real tuyo:** como CM gestionabas cupones. Supongamos:

**Requisito (ES):** Cupón `VERANO2024` aplica 20% descuento en compras mayores a ₲100.000 y solo una vez por usuario.

**Tarea:**
1. Identificá las **combinaciones válidas e inválidas** de (monto_compra, ya_usó_cupón, código_correcto)
2. Esto es EP puro sobre un input compuesto. Cuántas particiones hay?

---

## 📏 Bloque 2 — Boundary Value Analysis (BVA) — LO 4.2.2

### Ejercicio 2.1 — Edad para votar (clásico)

**Requisito (multilingüe):** Voto obligatorio entre 18 y 65 años (inclusive), optativo de 16-17 y 66-75.

**Tarea con 2-value BVA:**
- Test en min (16 si optativo, 18 si obligatorio) y max (65 obligatorio, 75 optativo)
- Para cada límite: el valor límite y uno afuera

**Tarea con 3-value BVA:**
- min-1, min, max, max+1

**Tabla para completar (2-value):**

| Caso | Edad | Esperado |
|---|---|---|
| Min-1 (inválido) | 15 | "Muy joven para votar" |
| Min | 16 | "Voto optativo" |
| Max | 65 | "Voto obligatorio" |
| Max+1 | 66 | "Voto optativo" |
| Max+1 (fuera de optativo) | 76 | "Fuera de rango" |

**Tu tarea:** armá la versión 3-value y comparalas.

---

### Ejercicio 2.2 — Inscripción a curso ISTQB

**Requisito:** El curso acepta inscripciones de personas entre 18 y 65 años (sí, sí, es el mismo dominio que edad de jubilación, lo hacemos a propósito para que veas cómo cambia el test según el contexto).

**Tarea:**
1. ¿Cuántos tests con 2-value? ¿Y con 3-value?
2. ¿En qué se diferencia este ejercicio del Ejercicio 2.1?
3. 💡 **Esto demuestra LO 1.4.2:** el mismo input (edad) requiere tests distintos según el contexto.

---

### Ejercicio 2.3 — Cantidad máxima de acompañantes en consulta

**Requisito:** Cada consulta permite máximo 2 acompañantes por paciente.

**Tarea:**
1. EP: identificá particiones
2. BVA: diseñá tests con 2-value y 3-value
3. Escribí una **negative test** clara

---

## 📋 Bloque 3 — Decision Table Testing — LO 4.2.3

### Ejercicio 3.1 — Devolución de producto (clásico)

**Requisito:** "Se acepta devolución si: tiene recibo + días desde compra ≤30 + producto en buen estado. Si no tiene recibo, solo se acepta cambio por el mismo producto si está sin abrir."

**Tarea:**
1. Construí la decision table completa
2. ¿Cuántas reglas resultan?
3. Identificá la regla "imposible" (si existe)

**Plantilla:**
| Regla | Tiene recibo | Días ≤30 | Buen estado | → Acción |
|---|---|---|---|---|
| R1 | sí | sí | sí | ... |
| ... | | | | |

---

### Ejercicio 3.2 — Sistema de alerta médica (contexto tuyo)

**Contexto:** Como intérprete, recibías llamadas con prioridad. Adaptemos al contexto de triage:

**Requisito:** "Una consulta se marca como URGENTE si: paciente tiene dolor torácico OR (dificultad respiratoria + fiebre alta). Se marca como PRIORITARIA si: fiebre alta OR (tos + más de 65 años). Resto: NORMAL."

**Esto tiene una trampa:** hay ORs, lo que significa que **no es una decisión pura por combinaciones**. Para ISTQB esto es válido — no todas las decision tables son del estilo "todo AND".

**Tarea:**
1. Convertilo a una decision table asumiendo las combinaciones posibles
2. ¿Cuántas reglas?
3. ¿Hay reglas redundantes?

---

### Ejercicio 3.3 — Aprobación de crédito

**Requisito (clásico pero útil):** "Crédito aprobado si: ingresos ≥ ₲5M/mes Y (antigüedad laboral ≥ 1 año O tener un codeudor solvente). Se rechaza si: scoring < 600. Si scoring entre 600-700, requiere entrevista."

**Tarea:**
1. Construí decision table
2. ¿Cuántas reglas?
3. ¿Alguna regla es combinación imposible?

---

## 🔄 Bloque 4 — State Transition Testing — LO 4.2.4

### Ejercicio 4.1 — Sistema de login (clásico)

**Estados:** LOCKED, ACTIVE, DISABLED
**Eventos:** login_success, login_fail, admin_unlock, account_disable (3 fails), wait_timeout

**Tarea:**
1. Dibujá el diagrama de estados con flechas
2. Lista 5 transiciones válidas
3. Lista 3 transiciones inválidas
4. Escribí 1 test por cada transición válida

---

### Ejercicio 4.2 — Workflow de campaña en redes sociales (tu experiencia CM)

**Contexto real tuyo:** cada post pasaba por estados.

**Estados:** DRAFT, REVIEW, APPROVED, SCHEDULED, PUBLISHED, ARCHIVED

**Eventos:** submit_for_review, approve, request_changes, schedule, publish, archive, edit_after_published

**Tarea:**
1. Dibujá el diagrama
2. ¿Qué pasa si un post SCHEDULED recibe un `request_changes`? ¿Es válido o no?
3. ¿Cuántas transiciones válidas vs inválidas?
4. 💡 **Bonus:** Si tuvieras que automatizar este flujo en Jira, ¿qué campos tendría cada ticket? Esto es "traceability" (LO 1.4.4) en la práctica.

---

### Ejercicio 4.3 — Estados de una cita médica

**Estados:** REQUESTED, CONFIRMED, IN_PROGRESS, COMPLETED, CANCELLED, NO_SHOW

**Eventos:** confirm, start_visit, end_visit, cancel_before_24h, cancel_after_24h, no_show

**Tarea:**
1. Diagrama
2. ¿`cancel_after_24h` desde REQUESTED es válido? ¿Y desde CONFIRMED?
3. Tests críticos a cubrir

---

## 🧪 Bloque 5 — Statement + Branch Coverage — LO 4.3.1, 4.3.2

### Ejercicio 5.1 — Función canVote

```python
def canVote(age, registered):
    if age < 0:
        return "invalid age"
    if age >= 18 and registered:
        if age > 75:
            return "vote optional"
        else:
            return "must vote"
    else:
        if age >= 16:
            return "vote optional"
        else:
            return "too young"
```

**Tarea:**
1. **Statement coverage 100%:** ¿cuántos tests? Escribilos.
2. **Branch coverage 100%:** ¿cuántos tests? Escribilos.
3. ¿Cuántos tests en total para cubrir ambos?

**Pista:** cada `if` tiene 2 ramas (verdadera y falsa). 4 `if`s = 8 ramas. Pero algunas son inalcanzables en ciertos ordenamientos.

---

### Ejercicio 5.2 — Sistema de descuento

```python
def calculate_discount(total, has_coupon, is_member):
    discount = 0
    if total > 100000:
        discount = 0.10
    if has_coupon:
        discount = discount + 0.05
    if is_member:
        discount = discount + 0.05
    if discount > 0.20:
        discount = 0.20
    return total * (1 - discount)
```

**Tarea:**
1. Cuántas líneas ejecutables? → 100% statement coverage = ?
2. Cuántas branches? → 100% branch coverage = ?
3. Encontrá un input que cubra todo en 1 solo test (¿se puede?)

---

## 👥 Bloque 6 — User Stories + Acceptance Criteria + ATDD — LO 4.5.1-4.5.3

> **Este es el bloque NUEVO en v4.0.** Es donde más vas a brillar porque tu trabajo en CM era EXACTAMENTE escribir user stories y acceptance criteria (solo que no los llamabas así).

### Ejercicio 6.1 — App de delivery (3 user stories)

**Contexto:** sos PM/PO de una app de delivery estilo PedidosYa.

**Tarea:** Escribí 3 user stories siguiendo el formato:

```
Como [tipo de usuario]
Quiero [acción]
Para [beneficio]
```

Posibles usuarios:
- Cliente nuevo
- Cliente registrado
- Repartidor
- Restaurante

**Para cada user story, escribí 4-5 acceptance criteria** en formato:

```
DADO [contexto inicial]
CUANDO [acción del usuario]
ENTONCES [resultado esperado]
```

---

### Ejercicio 6.2 — Feature de intérprete (basada en tu experiencia)

**Contexto:** estás diseñando una feature para Language Line que detecta automáticamente si una llamada requiere intérprete médico o legal.

**Tarea:**
1. Escribí 1 user story desde la perspectiva del operador de la central
2. 3 acceptance criteria en formato Given/When/Then
3. 2 tests ATDD concretos

**Pista:** ¿qué keywords activarían "modo médico"? ¿Cuáles "modo legal"? Esto es experience-based testing aplicado.

---

### Ejercicio 6.3 — Formulario de inscripción a curso ISTQB (humor)

**Contexto:** estás diseñando el formulario de inscripción a este curso ISTQB.

**Tarea:**
1. 2 user stories (una para el alumno, una para el admin)
2. 5 acceptance criteria total
3. 2 tests ATDD

---

## 🎁 Bloque BONUS — Localization Testing (no está en CTFL pero es tu futuro laburo)

> **Por qué este bloque existe:** Cuando consigas tu primer trabajo QA, una de las puertas más lógicas para tu perfil es **Localization QA (LQA)**. No es parte del CTFL, pero es donde tu trilingüismo se convierte en salario en USD.

### Ejercicio Bonus 1 — Detección de errores de localización

**Contexto:** Una app de e-commerce tiene estos strings en ES, EN, PT. Encontrá los errores:

| Key | ES | EN | PT |
|---|---|---|---|
| cart_empty | "Tu carrito está vacío" | "Your cart is empty" | "Seu carrinho está vazio" |
| checkout_button | "Finalizar compra" | "Finish purchase" | "Finalizar compra" |
| error_500 | "Algo salió mal" | "Something went wrong" | "Algo deu errado" |
| date_format | "31/12/2024" | "12/31/2024" | "31/12/2024" |
| currency | "₲150.000" | "Gs. 150,000" | "R$ 1.250" |

**Tareas:**
1. ¿Cuál tiene error de currency formatting en EN? (decimales con punto vs coma)
2. ¿Cuál tiene error de date format en US vs Paraguay?
3. ¿Cuál parece estar hardcodeado (no localizado)?

---

### Ejercicio Bonus 2 — Traducción que NO funciona

**Contexto:** Una empresa de juegos traduce así su botón de "Save":

- ES: "Salvar"
- PT: "Salvar"
- EN: "Save"

**Tarea:** ¿Por qué "Salvar" en ES es problemático? ¿Y en PT es aceptable?

**Pista:** pensá en el contexto gaming. En ES, "salvar" tiene connotación religiosa (salvar el alma). En PT, "salvar" = guardar archivo es normal. La misma palabra en dos idiomas requiere decisiones distintas.

---

### Ejercicio Bonus 3 — Caso real tuyo

**Contexto:** como Translation Officer adaptaste documentos. Pensá en 1 caso real donde la traducción literal no funcionaba y tuviste que **adaptar culturalmente**.

**Tarea:**
1. Describí el caso brevemente
2. ¿Cómo fue la decisión de adaptar vs traducir literal?
3. ¿Cómo informarías esto a un equipo de QA hoy?

---

## 📊 Cuándo hacer este archivo

| Semana del plan | Bloques a hacer | Tiempo estimado |
|---|---|---|
| Semana 1 | Ninguno — estás en Cap 1 | — |
| Semana 2 | Bloque 1 (EP) si te sentís cómoda | 1-2 h extra |
| Semana 3 | Ninguno — Cap 3 es rápido | — |
| Semana 4 | **Bloques 1, 2, 3, 4, 5** completos | 6-8 h |
| Semana 5 | **Bloque 6** + repaso de lo difícil | 4-5 h |
| Semana 6 | Bonus si te interesa LQA | 2-3 h |
| Semana 7 | Repaso focal de los que más te costaron | 1-2 h |

---

## 📂 Siguiente archivo

→ [`../05_career_paths/CARRERA_QA_PARA_LUANA.md`](../05_career_paths/CARRERA_QA_PARA_LUANA.md) — Roles específicos para tu perfil (LQA, Functional QA, Customer Success QA, etc.), salarios reales PY/LATAM/remoto en USD, empresas que contratan trilingües, dónde aplicar.

*Si un ejercicio te queda difícil, saltá al siguiente. Si los tres bloques principales (1, 2, 4) los hacés con fluidez, estás lista para Cap 4 del examen.*
