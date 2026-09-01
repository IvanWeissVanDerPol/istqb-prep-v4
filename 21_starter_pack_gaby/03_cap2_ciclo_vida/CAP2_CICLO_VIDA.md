# Cap 2 — Testing en el Ciclo de Vida del Software (versión clínica)

> **Versión ISTQB CTFL v4.0.1 — Sección 2.** Cubre LOs **2.1.1, 2.1.2, 2.1.3, 2.2.1, 2.2.2, 2.2.3, 2.3.1, 2.4.1, 2.5.1, 2.5.2** (10 de 10 LOs del capítulo).
>
> Equivalente a [`../../05_summaries/cap_02_ciclo_vida_v4.md`](../../05_summaries/cap_02_ciclo_vida_v4.md) del repo principal.
>
> Tiempo de lectura: ~30 minutos.
>
> **Para repaso rápido:** [`CHEATSHEET_CAP2.md`](CHEATSHEET_CAP2.md) (1 página).

---

## 1. Modelos de ciclo de vida del software (2.1)

Un "modelo de ciclo de vida" es cómo se organiza el trabajo de construir software de principio a fin. En odontología ya conocés los modelos — solo que los llamás "flujos de atención" o "protocolos institucionales".

### Modelo en cascada (Waterfall)

```
Requisitos → Diseño → Implementación → Testing → Despliegue → Mantenimiento
   (1 vez)    (1 vez)    (1 vez)       (1 vez)    (1 vez)     (continuo)
```

**ISTQB dice:** secuencial, cada fase completa antes de la siguiente.

**En la clínica — la consulta tradicional paso a paso:**

```
1. Primera consulta: anamnesis + examen + radiografía + diagnóstico presuntivo
2. Plan de tratamiento (propuesta al paciente, presupuesto, aceptación)
3. Ejecución del tratamiento (sesiones)
4. Control y ajuste post-tratamiento
5. Alta + plan de mantenimiento (controles periódicos)
```

**Cuando usar waterfall:** cuando el paciente llega, vos sabés qué tiene, hacés un plan, lo ejecutás. No esperás sorpresas. Es el flujo "ideal" pero no el más común.

**Limitaciones:** si en el paso 3 descubrís algo no visto en el paso 1, tenés que volver al paso 1. Caro.

### Modelo en V (extension del cascada)

```
Requisitos ←←←←←←←←←←←←←← Acceptance Testing
Diseño       ←←←←←←←←←← System Testing
Diseño detallado ←←←←← Integration Testing
Implementación ←←← Unit Testing
```

**Idea:** cada fase de desarrollo tiene su fase de testing对应的对应. Los test cases se diseñan en la fase de requisitos (no después).

**En la clínica — el plan que se valida contra sus propios criterios:**

Cuando vos hacés un plan de tratamiento, también definís los **criterios de éxito**:
- "Endodoncia: conducto obturado a longitud de trabajo, asintomático, radiolucidez resuelta en 6 meses"
- "Implante: oseointegración a 3 meses, sin movilidad, sin pérdida ósea >1mm al año"

Esos criterios se escriben **junto con el plan**, no después. Eso es V.

**Cuando usar V:** sistemas críticos (médico, aeronáutico, nuclear). Cuando testear todo después es demasiado tarde.

### Modelos iterativos e incrementales

**Idea:** en vez de hacer todo de una vez, hacé varias rondas cortas. Cada ronda entrega una mejora funcional.

**En la clínica — el tratamiento por sesiones del periodoncista:**

```
Sesión 1: diagnóstico + raspaje supragingival
   ↓
Sesión 2: re-evaluación + raspaje subgingival sector 1
   ↓
Sesión 3: re-evaluación + raspaje subgingival sector 2
   ↓
Sesión 4: re-evaluación + mantenimiento + alta
```

Cada sesión es un "incremento". Entre cada sesión, evaluás (testing) si el plan está funcionando. Si no, lo cambiás.

### Modelo iterativo (general)

**ISTQB dice:** el producto se construye en iteraciones cortas. Cada iteración pasa por mini-diseño → mini-implementación → mini-testing → feedback.

**En la clínica — ortodoncia con alineadores:**

```
Set de alineadores 1-10 (8 semanas)
   ↓ evaluás
Set 11-20 (8 semanas)
   ↓ ajustás
Set 21-30 (8 semanas)
   ↓ etc.
```

Cada set es una iteración. Evaluás resultado, ajustás plan.

### Modelo incremental (entrega por módulos)

**ISTQB dice:** entregas parciales. Cada entrega es funcional por sí misma.

**En la clínica — rehabilitación por fases:**

```
Fase 1 (entregable 1): estabilización periodontal + urgencias
   ↓
Fase 2 (entregable 2): operatoria + endodoncias necesarias
   ↓
Fase 3 (entregable 3): prostodoncia fija
   ↓
Fase 4 (entregable 4): controles y mantenimiento
```

Cada fase es un "incremento" que el paciente puede usar y vos podés evaluar.

---

## 2. Niveles de testing (2.2) ⭐ IMPORTANTE

ISTQB distingue 4 niveles. Todos se aplican a software dental.

### 1. Component Testing (Unit Testing)

**Qué:** testear la **unidad más pequeña** (una función, un módulo, una pantalla).

**Quién:** el desarrollador (vos NO lo hacés).

**En la clínica:**
> Antes de instalar un software, el programador testea cada pantalla por separado. ¿La pantalla de "Cargar paciente nuevo" acepta el nombre? ¿Guarda? ¿Recupera? Eso es component testing.

**Analogía dental:** probar que el **lámpara del sillón funciona**, que el **rayos X saca la imagen esperada**, que el **autoclave llega a la temperatura correcta**, antes de operar. Test unitario de cada equipo.

### 2. Integration Testing

**Qué:** testear cómo **trabajan juntas** las unidades.

**Quién:** el desarrollador o un tester dedicado.

**En la clínica:**
> ¿La radiografía que toma el aparato se ve correctamente en el software? ¿El presupuesto del software se integra con el sistema de facturación? ¿La agenda online sincroniza con la del consultorio? Eso es integration testing.

**Analogía dental:** probar que la **imagen del RVG** se vea correctamente en el **software de historia clínica**, o que el **escáner intraoral** pase la imagen al **software de diseño de sonrisa**.

### 3. System Testing

**Qué:** testear el sistema **completo** como un todo, contra los requisitos.

**Quién:** equipo de testing dedicado.

**En la clínica:**
> Probar el flujo completo del paciente: llega → agenda → reception → espera → consultorio → tratamiento → pago → próxima cita. Todo el journey del paciente, end-to-end.

**Lo hacés vos?** A veces. "Voy a hacer una prueba piloto el lunes con un paciente real".

### 4. Acceptance Testing

**Qué:** el usuario final acepta que el sistema cumple sus necesidades.

**Quién:** el cliente (vos, en el caso del consultorio).

**En la clínica:**
> Después de un tiempo de prueba con el nuevo software, vos decís: "OK, esto sirve, lo adopto". Eso es acceptance testing.

A veces se divide en:
- **UAT (User Acceptance Testing):** el usuario acepta
- **OAT (Operational Acceptance Testing):** ops/admin acepta (backups, performance, seguridad)
- **Regulatory:** cumple normas regulatorias (ANMAT, FDA, MSP)

---

## 3. Tipos de testing (2.3)

ISTQB distingue los **niveles** (component, integration, system, acceptance) de los **tipos** (functional, non-functional, change-related).

### Functional Testing

**Qué:** testear **QUÉ** hace el sistema (las funciones).

**En la clínica:** "Si yo hago click en 'Guardar', ¿se guarda?" "¿Si pongo 28 piezas, las guarda?"

**Subtipos:**
- **Smoke testing:** ¿funciona lo básico? (análogo: ¿el sillón enciende?)
- **Sanity testing:** ¿funciona razonablemente lo que cambié? (análogo: ¿el nuevo composite polimeriza bien?)

### Non-functional Testing

**Qué:** testear **CÓMO** se comporta (no qué hace, sino cómo).

**Categorías:**
- **Performance:** ¿es rápido? — ¿cuánto tarda en cargar la historia clínica?
- **Load:** ¿aguanta con muchos usuarios? — 5 odontólogos usando el sistema a la vez
- **Security:** ¿es seguro? — ¿se puede acceder a la historia clínica de otro paciente?
- **Usability:** ¿es fácil de usar? — ¿la recepcionista aprende en 1 día?
- **Compatibility:** ¿funciona en distintos navegadores/dispositivos?
- **Reliability:** ¿se cae seguido?
- **Maintainability:** ¿es fácil de arreglar/modificar?

**En la clínica:**
> **Equivalente:** la silla dental — ¿es rápida para ajustar? (performance), ¿aguanta 8 horas de uso? (load), ¿es segura? (security — no se cae), ¿es fácil de limpiar? (maintainability).

### Change-related Testing

**Qué:** después de un cambio, verificar que (a) el cambio funciona, (b) no rompió nada de lo que ya andaba.

**Dos subtipos:**

#### a) Regression Testing

**Qué:** verificar que **lo que antes andaba, sigue andando** después del cambio.

**En la clínica:**
> Cambiás el software de historia clínica. El odontólogo tenía 12 años de fichas. ¿Las puede seguir viendo? ¿Las puede buscar por fecha? ¿Las puede imprimir? Si algo que funcionaba dejó de funcionar, hay regression.

**Analogía dental directa:** después de cambiar un composite, ¿el paciente sigue mordiendo bien? ¿Volvió la sensibilidad? Eso es regression testing.

#### b) Confirmation Testing (Re-testing)

**Qué:** verificar que **el defecto específico que se reportó**, ya está arreglado.

**En la clínica:**
> El software perdía los presupuestos al guardar. Lo arreglaron. Confirmation: ¿ahora guarda correctamente? Si sí, OK. Si no, el bug no se arregló.

**Analogía:** el paciente vino con dolor a la percusión post-endodoncia. Re-trataste el conducto. Confirmation: ¿desapareció el dolor? Si sí, arreglado.

### Maintenance Testing

**Qué:** testing después de que el sistema está en producción, por cambios en el entorno, upgrades, o correcciones.

**En la clínica:**
> Windows se actualizó. ¿Tu software sigue funcionando? El navegador se actualizó. ¿La web de turnos sigue mostrando bien? Eso es maintenance testing.

---

## 4. Resumen visual — Los 4 niveles × tipos

```
                   ┌─────────────────────────────────────────────┐
                   │              Acceptance Testing             │ ← funcional + no funcional + change-related
                   ├─────────────────────────────────────────────┤
                   │              System Testing                │
                   ├─────────────────────────────────────────────┤
                   │            Integration Testing              │
                   ├─────────────────────────────────────────────┤
                   │           Component Testing                 │
                   └─────────────────────────────────────────────┘
                                    ↓
              Cada nivel puede tener: Functional | Non-Functional | Change-related
```

---

## Resumen del Cap 2

✅ Hay distintos modelos de ciclo de vida (cascada, V, iterativo, incremental). No hay "uno mejor".
✅ 4 niveles: component → integration → system → acceptance (de menor a mayor alcance).
✅ 3 tipos de testing: functional (qué hace), non-functional (cómo lo hace), change-related (qué cambia después de un cambio).
✅ Regression = "lo que andaba, sigue andando".
✅ Confirmation = "el bug que reporté, ya está arreglado".
✅ Cada nivel y tipo se puede aplicar al software de tu consultorio, de tu clínica anterior, o al software de cualquier sistema médico.

---

## Para chequear que entendiste

1. ¿En qué se diferencia system testing de acceptance testing?
2. ¿Qué es regression testing y por qué importa cuando actualizás un software?
3. ¿Cuál es la diferencia entre functional y non-functional testing? Doy un ejemplo dental.

Hacé el [`QUIZ_CAP2.md`](../08_quizzes_dentales/QUIZ_CAP2.md).
