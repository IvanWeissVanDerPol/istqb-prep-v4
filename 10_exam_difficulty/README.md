# ⚠️ Common Exam Failures & How to Avoid Them

> **Por qué falla la gente el CTFL** (basado en trendig.com + istqb.guru, datos 2024-2026)
> **Y qué hacer concretamente para no ser parte del 25-30% que reprueba**

---

## 📊 Estadísticas oficiales

- **CTFL fail rate:** **25-30%** a nivel mundial (1ra vez)
- **CTAL fail rate:** hasta **40%** (más difícil)
- **Tiempo promedio de preparación:** **40-60 horas**
- **Costo del fail:** USD 250-500 (fee + materiales + tiempo perdido)

> **Para Paraguay:** USD 150-300 fee + materiales. Un fail es costoso.

---

## 🚨 Las 7 razones por las que la gente falla el CTFL (con fixes concretos)

### **Razón 1: Memorizar definiciones sin entender K-levels** ⭐⭐⭐

> "El error más común, especialmente entre candidatos que usan flashcards pesadas."

**Qué pasa:**
- El syllabus v4.0.1 asigna K-level a cada LO:
  - **K1:** recordar
  - **K2:** entender/explicar/distinguir
  - **K3:** aplicar/usar (Cap 4 y 5)
- **~60% de las preguntas son K2 o K3** — no K1.
- Memorizar "regression testing es testing para detectar modificaciones side effects" → no te sirve cuando la pregunta lo describe con un scenario diferente.

**Cómo evitarlo:**

1. Para cada concepto, después de leer la definición, escribí un **escenario real** donde aparezca.
2. Practicá con preguntas **basadas en scenarios**, no con definiciones copiadas.
3. Cuando falles un practice, preguntate: "¿No sabía el concepto, o no lo reconocí en este scenario?" — el segundo es más común de lo que pensás.

---

### **Razón 2: Skipear la aplicación práctica de Cap 4** ⭐⭐⭐

> "Cap 4 = 30% del examen. Si solo leíste sin practicar, fallás."

**Qué pasa:**
- Decision table testing con 3-4 conditions: building incorrecto, missing combinations
- BVA confundido entre 2-value y 3-value
- State transition con transitions inválidas missed
- Statement coverage calculando mal unreachable statements

**Cómo evitarlo:**

Sin notas, en menos de 10 minutos cada uno:

1. **Decision table** — Construí una desde un requisito con 3-4 conditions. Colapsá columnas redundantes.
2. **BVA** — Aplica 2-value a un rango. Luego 3-value al mismo rango. Explicá la diferencia en voz alta.
3. **State diagram** — Dibujá desde un sistema descrito (ATM lifecycle). Derivá tests para valid + invalid transitions.
4. **Coverage** — Calculá statement y branch para un fragment de código de 5-10 líneas con if-else.

**Hacelo al menos 3 veces con scenarios diferentes** antes de rendir.

---

### **Razón 3: Confundir términos similares** ⭐⭐⭐

> "ISTQB usa lenguaje preciso. El examen explota esa precisión."

**Los pares más confundidos:**

#### Error vs Defect vs Failure vs Mistake

- **Error / Mistake:** acción humana que produce resultado incorrecto
- **Defect (fault, bug):** imperfección en el código
- **Failure:** comportamiento incorrecto observable
- **Root cause:** razón fundamental que origina el error

#### Verification vs Validation

- **Verification:** "estamos construyendo el producto correctamente?" (cumple specs)
- **Validation:** "estamos construyendo el producto correcto?" (cumple necesidades)

#### Confirmation vs Regression testing

- **Confirmation (re-test):** ese bug específico está fixed
- **Regression:** cambios no rompieron otras cosas

#### Severity vs Priority

- **Severity:** impacto técnico (high/medium/low)
- **Priority:** urgencia para fixear (high/medium/low)

#### Project risk vs Product risk

- **Project risk:** afecta schedule/coste/calidad del PROYECTO
- **Product risk:** afecta calidad del PRODUCTO final

#### Walkthrough vs Technical review vs Inspection

- **Walkthrough:** dirigida por AUTOR, informal
- **Technical review:** media formalidad, no autor
- **Inspection:** la más formal, moderator (no autor) + roles + métricas

#### Static vs Dynamic testing

- **Static:** NO ejecuta el código (revisiones, análisis)
- **Dynamic:** SÍ ejecuta

#### Test monitoring vs Test control

- **Monitoring:** medir progreso
- **Control:** acción correctiva

#### Statement coverage vs Branch coverage

- **Statement:** % líneas ejecutadas
- **Branch:** % decisiones evaluadas a true Y false

**Cómo evitarlo:**
- Tabla mental "vs" para cada par.
- Aplicar el principio "Si A, no B" — entender POR QUÉ son distintos.

---

### **Razón 4: Estudiar con material viejo (v3.1)** ⭐⭐⭐

> "Si tu material dice 'usability' en lugar de 'interaction capability', estás con v3.1."

**Cómo evitarlo:**
- Verificar versión en cada material: **v4.0.1 (sep 2024)**.
- Material v3.1 dice:
  - "documentation" → debe ser **"work products"**
  - "usability" → debe ser **"interaction capability"**
  - "portability" → debe ser **"flexibility"**
  - "white box" → debe ser **"white-box"**
  - "stage" → debe ser **"phase"**
  - "test object" → debe ser **"test item"**
- Este repo (IvanWeissVanDerPol/istqb-prep-v4) está alineado a v4.0.1.

---

### **Razón 5: Subestimar Cap 5 (Managing)** ⭐⭐

> "Cap 5 = ~18% del examen. Muchos lo skipean porque parece 'administrativo'."

**Cómo evitarlo:**
- **Memorizar:** test pyramid, testing quadrants, AMTA (Accept, Mitigate, Transfer, Avoid), risk = likelihood × impact
- **Saber hacer:** defect report (K3)
- **Diferenciar:** severity vs priority, monitoring vs control, project vs product risk

---

### **Razón 6: Patrones de pregunta ISTQB** ⭐

> "El examen tiene patrones que se repiten. Si no los conocés, los perdés."

**Patrones comunes:**

| Patrón | Cómo se ve | Cómo responder |
|---|---|---|
| **EXCEPT** | "Which of the following EXCEPT..." | Buscá la opción que NO aplica |
| **NOT** | "...is NOT a..." | La opción que NO es verdadero |
| **BEST** | "...the BEST way..." | La opción MÁS correcta |
| **MOST** | "...MOST appropriate..." | Lo MÁS correcto |
| **WHICH** | "Which of the following..." | A veces todas parecen correctas; elegí la más específica |
| **Always/Never** | "...is always..." | Casi siempre es FALSO (absolutos) |
| **Should/May** | "...should be done..." | Diferencia entre obligatorio vs opcional |

**Tips:**
- **Cuidado con absolutos:** "always / never / exactly" casi siempre son FALSO.
- **Cuando dudás entre 2 opciones:** ISTQB suele preferir la MÁS específica/técnica.
- **Si "testing is context-dependent"** está como opción, suele ser válida para preguntas de "what's the BEST practice".
- **Si la pregunta dice "depending on context"** — está apuntando al principio #6 (Testing is context-dependent).

---

### **Razón 7: Mala gestión del tiempo** ⭐

> "60 min / 40 preguntas = 1.5 min por pregunta. Si te atascás 5 min en una, perdés 3-4 preguntas siguientes."

**Estrategia:**

1. **Primera pasada (35 min):** contestá todas las fáciles. Marcá las difíciles.
2. **Bookmark 12-15 preguntas** difíciles.
3. **Volvé** (20 min) a las marcadas.
4. **Última pasada (5 min):** revisá que no dejaste nada en blanco (no hay penalidad).

---

## 🎯 Plan de preparación CONCRETO anti-fail

### Checklist antes de rendir (de istqb.guru):

- [ ] Saqué **≥75% en 3 simulacros cronometrados completos**
- [ ] Puedo **construir decision table + BVA 2/3-value + coverage** sin notas
- [ ] Puedo **explicar defect/failure/error/mistake** con ejemplos reales
- [ ] Puedo **explicar monitoring vs control, severity vs priority, product vs project risk**
- [ ] Puedo **identificar el tipo de review** desde un scenario
- [ ] Estoy usando **solo material v4.0.1**
- [ ] Practiqué leer stems buscando **EXCEPT, NOT, BEST, MOST**
- [ ] Pasé **al menos 8 horas en Cap 5**
- [ ] Si español no es nativa, **apliqué para extensión de tiempo** (+25%)

### Si algún ítem está sin tildar: **delay el examen.** Una semana más es más barata que un re-attempt.

---

## 📉 Cosas que NO ayudan

❌ **"Dumps"** — preguntas memorizadas cambian. ISTQB las rota. Tampoco aprendés.
❌ **Videos viejos** — muchos enseñan v3.1 aún. Verificar fecha y versión.
❌ **Skipear Cap 4** — el 30% más pesado.
❌ **Solo memorizar definiciones** — 60% del examen es K2/K3.
❌ **Rendir sin simulacro cronometrado** — el tiempo es un factor real.

---

## 💡 Tips adicionales (recopilados)

### Del trendig article (2026):
- **Mínimo 40 horas de estudio** distribuido en 6-8 semanas.
- **No subestimar el syllabus.** Es comprehensivo.
- **Practicar aplicación práctica**, no solo teoría.
- **Sample exams cronometrados** bajo condiciones reales.

### Del iSQI:
- **Para Foundation Level:** alcanzar comprensión conceptual, no memorizar.
- **Repetir simulacros** hasta consistency.
- **Read the official syllabus PDF** (no third-party glossaries).

### Del iQB Guatemala community:
- **Estudio en grupo** (vos ya lo tenés — el grupo de WhatsApp).
- **Tutor/mentor** (Alejandro Maciel es instructor en Paraguay).
- **Apply conceptos** en proyectos reales aunque sean personales.

---

## 🚨 Síntomas de "no estoy listo para rendir"

Si te pasa alguna de estas, **delay el examen:**

- ⏰ Sacás <65% en simulacros cronometrados
- ❌ No podés construir decision tables sin mirar el material
- ❌ Confundís severity vs priority en al menos 1-2 preguntas de cada quiz
- ❌ No podés describir los 7 principios de memoria
- ❌ Estudiás con material v3.1 sin saberlo
- ❌ El examen es en 2 semanas y no empezaste

**Si sacás ≥75% consistente en 3 simulacros → estás listo.** Adelante.

---

## 📊 Análisis de tu propio progreso

Llevá un tracking de:
- Score de cada simulacro (A, B, C)
- Tiempo tomado
- Preguntas marcadas para revisar
- Capítulos con más errores
- Errores recurrentes (que se repiten)

**Patrón típico de progreso:**
| Semana | Score sim A | Score sim B | Score sim C |
|---|---|---|---|
| 1 (inicio) | 40-50% | 45-55% | 50-60% |
| 3 (medio) | 55-65% | 60-70% | 65-70% |
| 5 (cerca) | 65-75% | 70-78% | 73-80% |
| 7 (listo) | ≥75% | ≥75% | ≥75% |

**Si llegás a 75% en 3 simulacros, rendí.**

---

## 🔗 Links a estudios de los que este archivo compila info

- trendig.com — Reducing the ISTQB Failure Rate (2026)
- istqb.guru — 7 Reasons Candidates Fail (2026 update)
- astqb.org — ISTQB official position
- iSQI — official exam provider observations
