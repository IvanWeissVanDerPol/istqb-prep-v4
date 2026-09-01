# Cap 1 — Fundamentos del Testing (versión clínica)

> **Versión ISTQB CTFL v4.0.1 — Sección 1.** Cubre LOs **1.1.1, 1.1.2, 1.2.1, 1.2.2, 1.2.3, 1.3.1, 1.4.1, 1.4.2, 1.5.1, 1.5.3** (10 de 10 LOs del capítulo).
>
> Equivalente a [`../../05_summaries/cap_01_fundamentos_v4.md`](../../05_summaries/cap_01_fundamentos_v4.md) del repo principal, pero explicado en lenguaje odontológico.
>
> Tiempo de lectura: ~35 minutos.
>
> **Para repaso rápido:** [`CHEATSHEET_CAP1.md`](CHEATSHEET_CAP1.md) (1 página).

---

## 1. ¿Qué es testing? (1.1)

### Lo que dice ISTQB

> **Testing es el proceso que consiste en todas las actividades del ciclo de vida, estáticas y dinámicas, concernientes a la planificación, preparación y evaluación de productos software y productos de trabajo relacionados, para determinar que satisfacen los requisitos especificados, para mostrar que son aptos para el propósito y para detectar defectos.**

(Traducción: testing = verificar que el software hace lo que tiene que hacer, encontrar problemas, y dar confianza.)

### En la clínica

**Testing = control de calidad de la práctica clínica.**

Cada vez que vos:

- ❌ Hacé una **revisión pre-operatoria** (anamnesis, alergias, medicación) → estás testeando que el paciente está en condiciones para la intervención
- ❌ Tomá una **radiografía final** y la comparás con la inicial → estás verificando que el tratamiento logró el objetivo
- ❌ Le preguntás al paciente **"¿le duele algo?"** post-operatorio → estás testeando si hay failure
- ❌ Hacé **pruebas de vitalidad, percusión, sondaje** → estás testeando el estado de la pieza
- ❌ Mirá la **oclusión con papel de articular** después de una restauración → estás verificando funcionalidad

**Todo eso es testing.** ISTQB le pone nombre formal a lo que ya hacés.

### Objetivos típicos del testing (1.1.1)

| Objetivo ISTQB | En tu consultorio |
|---|---|
| Evaluar work products (requisitos, diseño, código) | Evaluar la historia clínica antes de operar |
| Detectar defects | Detectar caries incipiente, periodontitis temprana |
| Reducir riesgo | Reducir riesgo de complicación post-operatoria |
| Verificar cumplimiento de requisitos | ¿Hicimos lo que el paciente vino a buscar? |
| Mejorar calidad | Mejorar protocolos, materiales, técnicas |
| Cumplir regulaciones | Cumplir normas del MSP, Círculo de Odontólogos |
| Construir confianza | Que el paciente confíe en vos |
| Validar necesidades del usuario | ¿El paciente está conforme con el resultado? |

### Testing vs Debugging (1.1.2)

| Testing | Debugging |
|---|---|
| Encontrar el **defecto** | Encontrar la **causa raíz** y corregirlo |
| Lo hace el tester (vos con tu protocolo) | Lo hace el desarrollador (el programador) |
| Dice "esto falla" | Dice "esto falla PORQUE…" |

**En clínica:**
- **Testing:** detectás que el paciente tiene dolor a la percusión 7 días post-endodoncia.
- **Debugging:** investigás si es un conducto omitido, una sobreobturación, una fractura vertical, o un problema periodontal independiente.

El testing **no corrige**. El debugging **sí corrige**.

> 📌 **Regla de oro:** vos en tu consultorio hacés testing. El programador de tu software hace debugging. Si tu software falla, **pedile al programador que debuggee**, no que "arregle". La diferencia importa para que no se repita.

---

## 2. ¿Por qué el testing es necesario? (1.2)

### Lo que dice ISTQB (1.2.1)

Razones por las que el testing existe:

1. **El software está en todas partes** — incluyendo sistemas críticos (médicos, financieros, de transporte)
2. **Las personas cometen errores** — los desarrolladores también
3. **El costo de no testear es alto** — bugs en producción son 10-100x más caros que bugs encontrados temprano
4. **Las regulaciones lo exigen** — en industrias como salud, banca, aviación

### En la clínica

**Sí, el software médico es crítico.** No es un lujo:

- ❌ Un error en el software de prescripción puede matar a un paciente
- ❌ Un error en el software de facturación puede hacer que cobres de más o de menos
- ❌ Un error en el software de historia clínica puede hacer que pierdas información de 12 años
- ❌ Un error en el sistema de turnos puede hacer que un paciente con dolor agudo no sea atendido

**No testear software médico es como no hacer historia clínica antes de un procedimiento.** Es negligencia profesional, no un detalle técnico.

### QA vs Testing (1.2.2)

| QA (Quality Assurance) | Testing (Quality Control) |
|---|---|
| **Enfoque en procesos** | **Enfoque en producto** |
| Proactivo: "definamos bien cómo trabajar para tener calidad" | Reactivo: "verifiquemos que este producto cumple" |
| Ejemplo dental: escribir el protocolo de endodoncia | Ejemplo dental: ejecutar el protocolo paso por paso en un paciente |
| Es de management | Es del tester individual |

**En la clínica:** vos hacés QA cuando escribís tus protocolos. Hacés testing cuando los seguís paso a paso en cada paciente.

### Terminología crítica (1.2.3) ⭐ MUY PREGUNTADO EN EL EXAMEN

ISTQB distingue tres cosas que en español se mezclan:

```
ERROR (mistake)        ←  La acción humana incorrecta
   ↓ causa
DEFECT (fault, bug)    ←  La imperfección en el producto
   ↓ se manifiesta cuando se ejecuta
FAILURE                ←  El comportamiento observable incorrecto
```

**En la clínica:**

| Término ISTQB | Dental |
|---|---|
| **Error (mistake)** | La decisión equivocada del profesional. Ej: "vi la radiografía y decidí no hacer endodoncia" |
| **Defect (fault)** | La imperfección resultante. Ej: la necrosis pulpar progresó porque no se trató a tiempo |
| **Failure** | Lo que ve el paciente. Ej: "doctor, tengo un flemón" |

> 📌 **Analogía clave para el examen:** Un defect puede existir sin causar failure. Una necrosis puede estar ahí, sin dar síntomas todavía. Cuando el paciente llega con dolor, ahí hay failure.

**El testing busca defects (imperfecciones) antes de que se manifiesten como failures (problemas visibles para el usuario).**

---

## 3. ⭐ Los 7 Principios del Testing (1.3.1) — MUY PREGUNTADO

Estos 7 principios salen **siempre** en el examen. Memorizarlos.

### Principio 1: Testing shows the **presence** of defects, not their **absence**

**ISTQB:** El testing puede demostrar que hay defectos, pero **nunca puede probar que NO hay defectos**.

**En la clínica:**
> "Doctor, ¿está seguro de que el tratamiento va a funcionar?"
>
> "Ningún odontólogo honesto puede decir '100%, garantizado'. Lo que puedo decir es: hice todo el protocolo, encontré los problemas que pude encontrar, y los traté. Si hay algo que se me pasó, no lo sé hasta que aparezca."

**Reducir riesgo ≠ eliminar riesgo.** El testing reduce la probabilidad de defectos, pero no la lleva a cero.

### Principio 2: **Exhaustive testing is impossible**

**ISTQB:** No se puede testear todo. Hay que elegir.

**En la clínica:**
> Un paciente con 28 piezas, 4 conductos por molar, 3 planos de evaluación, etc. — ¿podés testear todos los estados posibles? No. Testeás los que tienen más probabilidad de tener problemas.

**Estrategia:** sampling, risk-based, time-boxed. Elegí los tests más importantes.

### Principio 3: **Early testing saves time and money**

**ISTQB:** Encontrar un defecto temprano (en requisitos) es 10-100x más barato que encontrarlo en producción.

**En la clínica:**

| Cuándo se detecta el defecto dental | Costo análogo |
|---|---|
| En el diagnóstico inicial (radiografía pre-tratamiento) | Bajo: plan cambia, costo marginal |
| Durante el tratamiento (al abrir, ves necrosis no diagnosticada) | Medio: cambiar procedimiento mid-flow |
| Post-operatorio (paciente vuelve con dolor) | Alto: retratamiento, pérdida de confianza, posible demanda |

**Igual en software:**

| Cuándo se detecta el bug | Costo real |
|---|---|
| En la escritura de requisitos | USD 100 (re-escribir 1 párrafo) |
| En desarrollo | USD 1,000 (re-codificar) |
| En testing | USD 10,000 (re-testear + fix) |
| En producción | USD 100,000+ (emergencia, daño a reputación, posible demanda) |

### Principio 4: **Defects cluster together**

**ISTQB:** La mayoría de los defectos están concentrados en pocas áreas. (Regla 80/20: 80% de los bugs están en 20% del código.)

**En la clínica:**
> El 80% de las caries están en los molares. El 80% de los fracasos de endodoncia están en los conductos MV de molares superiores. El 80% de las complicaciones periodontales están en los sectores posteriores.

**Por qué:** complejidad + dificultad de acceso + humedad + biofilm.

**Aplicado al software:** las pantallas con más campos, los flujos más complejos, las integraciones con sistemas externos son donde se concentran los bugs.

### Principio 5: **Beware the pesticide paradox**

**ISTQB:** Si ejecutás los mismos tests una y otra vez, eventualmente no encuentran nuevos defectos. Los tests "envejecen".

**En la clínica:**
> Si vos siempre revisás las mismas 6 caras de cada pieza con la misma técnica, eventualmente dejás de ver lo nuevo. Hay que cambiar la técnica, usar nuevos métodos (transiluminación, escáner intraoral, CBCT).

**Aplicado al software:** actualizar los tests, agregar nuevos, cambiar la perspectiva.

### Principio 6: **Testing is context-dependent**

**ISTQB:** No se testea igual un software médico que un juego. El testing depende del contexto.

**En la clínica:**
> No se trata igual una caries de un paciente con xerostomía que una caries de un paciente sano. El protocolo cambia.

**Aplicado al software:** testing de un e-commerce ≠ testing de un marcapasos. El riesgo y el rigor son diferentes.

### Principio 7: **Absence-of-errors is a fallacy**

**ISTQB:** Que el software no tenga defectos **NO significa** que sea útil. Un software puede pasar todos los tests y aun así no resolver el problema del usuario.

**En la clínica:**
> Una endodoncia técnicamente perfecta (conductos limpios, obturación hermética, radiografía normal) puede ser un **fracaso clínico** si al paciente le molesta la oclusión post-tratamiento, o si no resolvió el motivo de consulta original.

**Aplicado al software:** testing verifica "está bien hecho", no "es lo que el usuario necesita". Para eso está la **validación** (vs verification — ver sección 5).

---

## 4. Actividades del Testing (1.4.1)

ISTQB define un proceso en 5+1 etapas. En la clínica ya lo hacés.

### Proceso ISTQB

```
1. Test Planning              ← Planificar
   ↓
2. Test Monitoring & Control  ← Monitorear (continuo)
   ↓
3. Test Analysis              ← Analizar (qué testear)
   ↓
4. Test Design                ← Diseñar (cómo testear)
   ↓
5. Test Implementation        ← Implementar (preparar ejecución)
   ↓
6. Test Execution             ← Ejecutar
   ↓
7. Test Completion            ← Cerrar y reportar
```

### En la clínica

| Etapa ISTQB | Tu equivalente |
|---|---|
| Test Planning | Plan de tratamiento escrito, con presupuesto y plazos |
| Test Monitoring & Control | ¿Vamos en tiempo? ¿Apareció algo nuevo? (control post-operatorio) |
| Test Analysis | Análisis de la historia clínica: ¿qué testear (radiografía, vitalidad, sondaje)? |
| Test Design | Diseño del plan: qué estudios pedir, qué hacer si encuentro X |
| Test Implementation | Preparación: anestesia, dique, instrumental listo |
| Test Execution | El procedimiento en sí |
| Test Completion | Epicrisis, indicaciones, alta, control a 7 días |

---

## 5. ⭐ Verification vs Validation (1.4.2) — MUY PREGUNTADO

Dos palabras que suenan parecido y significan cosas distintas.

### Verification

**ISTQB:** "¿Estamos construyendo el producto **correctamente**?" (Are we building the product right?)

**En la clínica:** "¿Hicimos lo que dijimos que íbamos a hacer?"
> El plan decía: endodoncia de conducto MV, ML, DB en 36. ¿Se hicieron los 3 conductos? ¿La obturación llega a longitud de trabajo? ¿Hay gutapercha suficiente? Eso es verification.

### Validation

**ISTQB:** "¿Estamos construyendo el **producto correcto**?" (Are we building the right product?)

**En la clínica:** "¿Funciona para el paciente?"
> El paciente llegó con dolor. ¿Se le fue el dolor? ¿Puede masticar? ¿Está conforme? Eso es validation.

### Diferencia clave

| Verification | Validation |
|---|---|
| Confirma el cumplimiento de requisitos | Confirma que el producto satisface las necesidades del usuario |
| "¿Lo hicimos bien?" | "¿Es lo que el paciente necesitaba?" |
| Se puede hacer con documentos | Requiere usuario real |
| Pre-requisito de la validation | Es la última prueba |

**Analogía de una restauración clase II:**
- **Verification:** ¿La restauración está bien adaptada, sin desbordes, con contactos, con anatomía?
- **Validation:** ¿El paciente puede comer sin que se le fracture, sin dolor, sin que se le acumule comida?

> 📌 **Trampa común en el examen:** confundir las dos. Memorizar la fórmula: V&V.

---

## 6. La psicología del testing (1.4.3) — Bonus

ISTQB dedica una sección a esto porque es sorprendentemente importante. testing **involucra personas**, y las personas tienen sesgos.

### Sesgos típicos

| Sesgo | En la clínica | En software |
|---|---|---|
| Confirmación (querer ver que sí funciona) | "Seguro la obturación está bien, no necesito radiografía final" | "El código se ve bien, no lo voy a probar más" |
| Apego al autor | "Yo diseñé este plan, no puede estar mal" | "Yo escribí este código, no puede tener bugs" |
| Sesgo de supervivencia | "Los últimos 50 pacientes salieron bien" | "Los últimos 50 tests pasaron" |
| Ceguera de atención | Después de 8 horas, ves menos | Después de horas mirando código, ves menos |

### Por qué importa

- ❌ Un tester demasiado cercano al desarrollador **no va a encontrar sus propios bugs**
- ❌ Un desarrollador que se testea a sí mismo tiene sesgo de confirmación
- ❌ El ego del profesional afecta el rigor

### Buenas prácticas

1. **Independencia:** cuanto más independiente es el tester, mejor testea
2. **Doble revisión:** que otro profesional mire lo que vos hiciste
3. **Documentar todo:** lo que se hizo y lo que NO se hizo

---

## Resumen del Cap 1 — Para repaso rápido

✅ Testing = verificar que algo cumple lo que tiene que cumplir
✅ Error → Defect → Failure (memorizar la cadena)
✅ 7 principios (memorizar)
✅ Verification vs Validation
✅ QA (procesos) ≠ Testing (producto)
✅ El testing es necesario porque el software está en sistemas críticos (médicos incluidos)

---

## Para chequear que entendiste

Antes de pasar al Cap 2, intentá responder estas preguntas mentalmente (o por escrito):

1. ¿Cuál es la diferencia entre un defect y un failure? Doy un ejemplo dental.
2. ¿Por qué "testing muestra presencia, no ausencia" importa al firmar un consentimiento informado?
3. Si tu programador te dice "ya lo probé todo", ¿qué le respondés basándote en los principios?

Las respuestas están en [`../08_quizzes_dentales/QUIZ_CAP1.md`](../08_quizzes_dentales/QUIZ_CAP1.md) mezcladas con preguntas de formato ISTQB. Hacé ese quiz ahora.
