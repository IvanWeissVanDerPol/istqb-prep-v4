# Cap 5 — Gestión de Testing (versión clínica)

> **Versión ISTQB CTFL v4.0.1 — Sección 5.** Cubre LOs **5.1.1, 5.1.2, 5.1.3, 5.2.1, 5.2.2, 5.3.1, 5.3.2, 5.3.3, 5.3.4, 5.3.5** (10 de 10 LOs del capítulo).
>
> Equivalente a [`../../05_summaries/cap_05_gestion_v4.md`](../../05_summaries/cap_05_gestion_v4.md) del repo principal.
>
> Tiempo de lectura: ~35 minutos.
>
> **Para repaso rápido:** [`CHEATSHEET_CAP5.md`](CHEATSHEET_CAP5.md) (1 página).

---

## 1. Conceptos generales (5.1)

ISTQB dice que la gestión de testing tiene:

- **Test Planning** (planificar)
- **Test Monitoring & Control** (monitorear y controlar)
- **Test Completion** (cerrar y reportar)

### En la clínica

Vos ya administrás una clínica (o varias). La gestión de testing es idéntica a la gestión clínica:

| ISTQB | Clínica |
|---|---|
| Test plan | Plan de tratamiento + presupuesto |
| Test schedule | Agenda del consultorio |
| Test monitoring | Control de progreso del tratamiento |
| Test completion report | Epicrisis al alta |
| Risk-based testing | Priorizar pacientes por urgencia |
| Effort estimation | Estimar tiempo de cada procedimiento |
| Defect management | Gestión de complicaciones |
| Test team | Equipo (tú, asistente, recepcionista, técnico dental) |

---

## 2. Test Planning (5.2) ⭐ IMPORTANTE

ISTQB dice que un test plan debe incluir:

1. **Contexto** (qué sistema, qué stakeholders)
2. **Actividades** (qué se va a hacer)
3. **Recursos** (humanos, técnicos, infraestructura)
4. **Cronograma** (cuándo)
5. **Criterios de entrada y salida** (cuándo empieza y termina cada fase)
6. **Riesgos**
7. **Estrategia** (qué niveles, qué tipos de testing)
8. **Métricas**

### En la clínica — el plan de tratamiento escrito

Tu plan de tratamiento tiene exactamente esos componentes:

1. **Contexto:** paciente X, motivo de consulta Y
2. **Actividades:** diagnóstico, plan, ejecución, controles
3. **Recursos:** tiempo del doctor, materiales, equipos, instrumental
4. **Cronograma:** sesiones 1, 2, 3... en fechas X, Y, Z
5. **Criterios de entrada y salida:** "se inicia el tratamiento cuando el paciente firma el consentimiento; se da alta cuando se cumplen los criterios de éxito"
6. **Riesgos:** "paciente fumador, riesgo de recidiva"
7. **Estrategia:** "tratamiento conservador primero, quirúrgico si no responde"
8. **Métricas:** "control radiográfico a 3 y 6 meses"

**Misma estructura.** Diferente vocabulario.

### Test Plan vs Test Strategy

| Test Plan | Test Strategy |
|---|---|
| Para **un proyecto específico** | Para **toda la organización** |
| Detallado, con cronograma | General, con principios |
| Es como el plan de tratamiento de un paciente específico | Es como el protocolo institucional del consultorio |

---

## 3. Risk-based Testing (5.3) ⭐ IMPORTANTE

### Idea

No podés testear todo. Entonces priorizás lo que tiene **más riesgo**.

**Riesgo = probabilidad × impacto.**

### En la clínica — la priorización de la cola de espera

Cuando tenés una cola de pacientes esperando turno:

```
1. Dolor agudo + absceso → URGENTE (alto riesgo si no se trata)
2. Dolor agudo sin absceso → PRIORITARIO
3. Fractura coronal → PRIORITARIO
4. Caries asintomática → NORMAL
5. Control de rutina → BAJA PRIORIDAD
```

Eso es **risk-based prioritization**: priorizás por probabilidad de complicación × impacto si no se trata.

### Aplicado al software

Cuando tenés que decidir qué testear primero en un sistema nuevo:

- ¿Qué funciones son críticas? (registro de paciente, historia clínica) → TESTEAR PRIMERO
- ¿Qué funciones tienen más probabilidad de fallar? (integraciones externas) → TESTEAR PRIMERO
- ¿Qué funciones tienen más impacto si fallan? (facturación) → TESTEAR PRIMERO

**Riesgo alto = testear primero. Riesgo bajo = testear después o no testear.**

### Risk matrix

```
              IMPACTO
              Bajo    Medio    Alto
PROB  Alta  |  M  |  A  |  MA |
      Media |  B  |  M  |  A  |
      Baja  |  MB |  B  |  M  |
```

(MB=muy bajo, B=bajo, M=medio, A=alto, MA=muy alto)

Testeás primero los MA, después los A, etc.

---

## 4. Esfuerzo de testing y estimación (5.4)

ISTQB dice que la estimación se puede hacer con:

- **Expert judgment** (juicio experto)
- **Métricas de proyectos anteriores**
- **Estimación basada en tests** (cuántos tests identificados)
- **Puntos de función / casos de uso**

### En la clínica

Vos estimás tiempo de cada procedimiento con:
- Tu **experiencia previa**
- **Estadísticas** de cuánto tardan ciertos tratamientos
- **Complejidad del caso**

**Igual en testing.**

---

## 5. Métricas de testing (5.5) ⭐ PREGUNTADO

ISTQB distingue entre:

- **Métricas de producto:** calidad del producto (ej: % casos pasados, densidad de defectos)
- **Métricas de proceso:** calidad del proceso (ej: % tests ejecutados a tiempo)

### Métricas comunes

| Métrica | Qué mide | Dental analog |
|---|---|---|
| % casos de prueba pasados | Calidad del software | % tratamientos exitosos |
| Densidad de defectos (bugs / KLOC) | Complejidad | Complicaciones / procedimiento |
| Cobertura de testing | Cuánto del código se testea | % de piezas tratadas vs diagnosticadas |
| Tiempo medio de detección | Eficiencia del testing | Tiempo entre síntoma y diagnóstico |
| Tiempo medio de reparación | Eficiencia del fix | Tiempo entre diagnóstico y retratamiento |

> 📌 En el examen: preguntan métricas. Memorizar: "métricas de producto ≠ métricas de proceso".

---

## 6. Test Monitoring & Control (5.6)

ISTQB dice que monitoreás vs controlás:

- **Monitoring:** recoger datos, ver cómo va
- **Control:** tomar acciones correctivas cuando algo se desvía

### En la clínica

- **Monitoring:** "¿el paciente está evolucionando? ¿los valores están dentro de lo esperado?"
- **Control:** "el paciente está peor, cambio el plan, agrego antibiótico, llamo al especialista"

**Misma idea.** Si los tests no van bien, ajustás el plan.

---

## 7. Configuration Management (5.7)

ISTQB dice que todo lo que se usa en testing debe estar bajo control de configuración: requisitos, código, tests, datos, herramientas, resultados.

### En la clínica

La configuración de tu consultorio:
- **Versión de la historia clínica** (si tenés varias versiones)
- **Versión del protocolo** (cuando actualizás el protocolo)
- **Lotes de materiales** (anotá lote, fecha de vencimiento)
- **Calibración de equipos** (cuándo fue la última calibración del autoclave)
- **Capacitación del equipo** (quién está certificado para qué)

> 📌 Si te demandan, necesitás demostrar que tu autoclave estaba calibrado, que el material no estaba vencido, que el protocolo era el vigente. Eso es configuration management.

---

## 8. Defect Management (5.8) ⭐ IMPORTANTE

ISTQB dice que un defecto (bug report) debe incluir:

| Campo | Ejemplo dental |
|---|---|
| ID | BUG-001 |
| Título | "El software de turnos pierde citas los domingos" |
| Descripción | Detalle del problema |
| Pasos para reproducir | Cómo se llega al bug |
| Resultado esperado | Lo que debería pasar |
| Resultado actual | Lo que pasa |
| Severidad | Crítica / Alta / Media / Baja |
| Prioridad | Urgente / Alta / Media / Baja |
| Estado | Abierto / En progreso / Resuelto / Cerrado |
| Asignado a | Quién lo arregla |

### Ciclo de vida de un defecto

```
Nuevo → Asignado → En progreso → Resuelto → Cerrado
                ↑                          ↓
                └──── Rechazado ←── No reproducido
```

(Si se cierra mal, se reabre.)

### En la clínica

**Una epicrisis** tiene la misma estructura:
- ID de la complicación
- Cuándo ocurrió
- Qué pasó exactamente
- Qué se hizo
- Cómo se resolvió
- Estado actual

---

## 9. Resumen del Cap 5

✅ Test plan = plan de tratamiento (misma estructura).
✅ Risk-based testing = priorizar por urgencia (igual que la cola de espera).
✅ Métricas miden producto vs proceso.
✅ Defect management = misma estructura que una epicrisis de complicación.
✅ Configuration management = control de versiones de todo (protocolos, calibraciones, lotes).

---

## Para chequear que entendiste

1. ¿Qué tiene un test plan que un test strategy no?
2. ¿Cuál es la diferencia entre severidad y prioridad de un defecto? Doy un ejemplo dental.
3. ¿Por qué el risk-based testing es importante en sistemas médicos?

Hacé el [`QUIZ_CAP5.md`](../08_quizzes_dentales/QUIZ_CAP5.md).
