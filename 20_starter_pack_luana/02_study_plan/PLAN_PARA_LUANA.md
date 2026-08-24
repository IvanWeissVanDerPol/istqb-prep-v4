# 📅 Plan de Estudio ISTQB CTFL v4.0.1 — Para Luana (8 semanas)

> **Hecho para:** Luana Benitez, Asunción. Intérprete + Community Manager + Psicología, trilingüe.
> **Tiempo semanal realista:** 6-8 horas (lun-sáb trabajo, domingo día fuerte)
> **Día de estudio fuerte:** Domingo (2-3 horas continuas) + 1 hora entre semana (lun, mié o vie)
> **Material:** este repo (`istqb-prep-v4`) + syllabus oficial v4.0.1 gratis en istqb.org
> **Meta:** pasar el examen con ≥70% en la primera intentona

---

## 🌟 Por qué este plan es distinto al plan genérico del repo

El plan genérico del repo (`01_plan_estudio/00_vision_general.md`) está hecho para el grupo de amigos Paraguay, que estudian en comunidad 5-6 horas por semana. **El tuyo está calibrado a tu vida real:**

1. **Sos la única que lo lee.** No hay presión de grupo, pero tampoco red de seguridad. Yo te la hago con checkpoints claros.
2. **Tus días laborales (lun-sáb) son limitados** por tu trabajo actual. No te voy a pedir 2 horas cada noche.
3. **Tenés skills transferibles brutales** (Cap 1, 3, 5) que te permiten avanzar más rápido. Por eso vamos a hacer Cap 4 (el más pesado) en dos semanas, no una.
4. **Tu inglés avanzado te permite leer el syllabus oficial** sin diccionario — eso es una ventaja enorme que pocos paraguayos tienen.

---

## 📋 Setup (antes de la semana 1)

Hacé esto en una tarde de domingo:

- [ ] **Fork + clone** este repo: https://github.com/IvanWeissVanDerPol/istqb-prep-v4
- [ ] **Descargá el syllabus oficial PDF** desde https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/ (es gratis)
- [ ] **Anki instalado** en tu celu o PC. Guía de import: `04_flashcards/anki_import_guide.md`
- [ ] **Importá las 85 flashcards** de `04_flashcards/flashcards_v4.0.1.csv`
- [ ] **Leyó `01_intro/LUANA_INTRO.md`** ← este pack
- [ ] **Leyó `03_skill_bridge/SKILLS_TRANSFER.md`** ← este pack
- [ ] **Anotó fecha tentativa del examen:** ASOLINFO Paraguay (Asociación Paraguaya de Informática) — buscar contacto actual en https://istqb.org/member-boards/. Examen ~USD 200, 60 min, 40 preguntas, 65% mínimo.
- [ ] **Creó archivo de progreso propio:** copiá `00_README/00_PROGRESS.md` y renombralo `LUANA_PROGRESS.md` (opcional, pero ayuda)

> 🎯 **Tip:** En Paraguay el examen oficial viene en español LATAM. Pero **leé el syllabus en inglés** porque las preguntas del examen usan los términos en inglés cuando hay ambigüedad. Tu nivel ya te lo permite.

---

## 📊 Distribución de horas (resumen)

| Sem | Cap | Horas | Porcentaje del examen | Tu facilidad | Focus |
|---|---|---|---|---|---|
| 1 | Cap 1 Fundamentals | 4 h | ~25% (14 LOs) | ⭐⭐⭐⭐⭐ | Lectura + quiz + principios |
| 2 | Cap 2 SDLC | 4 h | ~18% (10 LOs) | ⭐⭐⭐⭐ | Lo nuevo v4.0 (DevOps, shift-left) |
| 3 | Cap 3 Static Testing | 3 h | ~12% (8 LOs) | ⭐⭐⭐⭐⭐ | Reviews = tu vida diaria |
| 4-5 | Cap 4 Test Analysis & Design | 10 h | ~30% (14 LOs, 5 K3) | ⭐⭐⭐ | El más pesado: técnicas formales |
| 6 | Cap 5 Management + Cap 6 Tools | 5 h | ~18% (16+2 LOs) | ⭐⭐⭐⭐⭐ (Cap 5) | Riesgo, defect report |
| 7 | Simulacros | 6 h | 100% transversal | — | Sample exams A/B/C |
| 8 | Repaso final + EXAMEN | 4 h | — | — | Cheat sheets + flashcards |

**Total:** ~36 horas en 8 semanas (≈4.5 h/semana) — más realista para tu contexto.

---

## 📅 Semana 1 — Cap 1 Fundamentals of Testing (4 horas)

**Por qué arranca acá:** Cap 1 te da el vocabulario de TODO el examen. Es el capítulo más preguntable (25% del examen) y, para tu perfil, el más fácil.

### Domingo (3 h continuas — día de estudio fuerte)

**Bloque 1 (90 min) — Lectura + skill transfer**
- Abrí `05_summaries/cap_01_fundamentos_v4.md` y leelo UNA vez en voz alta (ayuda a fijar memoria)
- Mirá la sección "Tu experiencia" en `03_skill_bridge/SKILLS_TRANSFER.md` para Cap 1
- Escribí en tu cuaderno (o Notes del celu) los **7 principios** con tu propia versión de cada uno

**Bloque 2 (45 min) — Quiz Cap 1**
- `06_practice_tests/quizzes_por_capitulo/cap_01_quiz.md`
- Hacelo SIN mirar nada, 20 preguntas
- Score honesto. **Meta: ≥75% (15/20)**

**Bloque 3 (45 min) — Revisión + flashcards**
- Repasá las preguntas que fallaste
- Hacé 30 flashcards de Anki (las del bloque Cap 1)

### Entre semana (1 h — elegí tu día más libre)

- Repasá flashcards Cap 1 (Anki)
- Releé los 7 principios sin mirar. **Test mental:** podés decir los 7 sin trampas?

### ✅ Checkpoint fin de semana
- [ ] Quiz Cap 1: ≥15/20 (75%)
- [ ] 7 principios memorizados
- [ ] Distingo error/defect/failure con ejemplos propios
- [ ] Anki: 30 cards hechas

**Si llegás:** seguí a semana 2.
**Si NO llegás:** re-leé el summary y repetí el quiz antes de avanzar.

---

## 📅 Semana 2 — Cap 2 SDLC (4 horas)

**Foco:** Lo nuevo de v4.0.1 (shift-left, DevOps, retrospectives). El resto es vocabulario conocido.

### Domingo (2.5 h)

**Bloque 1 (60 min) — Lectura**
- `05_summaries/cap_02_ciclo_vida_v4.md`
- Mirá el skill transfer de Cap 2 en `03_skill_bridge/SKILLS_TRANSFER.md`
- Hacé una mini-tabla: **4 niveles** (component, integration, system, acceptance) con un ejemplo tuyo para cada uno
- Hacé otra mini-tabla: **functional vs non-functional** con ejemplo tuyo

**Bloque 2 (45 min) — Lo nuevo v4.0**
- **Shift-left:** ¿dónde aplicaba esto en tu vida? (interpretación médica =预防)
- **DevOps:** no te asuste el nombre. Es solo "desarrollo + operaciones juntos". Vos hacías "comunicación + salud + comunidad" juntos. Mismo concepto.
- **Retrospectives:** post-mortem de campaña CM
- **Confirmation vs Regression:** la distinción más importante de este cap (LO 2.2.3). Memorizala con tu ejemplo.

**Bloque 3 (45 min) — Quiz Cap 2 + flashcards**
- `06_practice_tests/quizzes_por_capitulo/cap_02_quiz.md`
- **Meta: ≥75%** (15 preguntas)
- Anki: 25 cards de Cap 2

### Entre semana (1 h)

- Relée el skill transfer Cap 2
- Flashcards Anki (15 min)
- **Ejercicio mental:** andá por tu casa o trabajo "viendo" SDLC. La clínica tenía su ciclo. La campaña tenía su ciclo. La interpretación tenía su ciclo. Mapeá cada uno a "qué test harías en cada fase".

### ✅ Checkpoint fin de semana
- [ ] Quiz Cap 2: ≥75%
- [ ] Confirmación vs Regression: puedo explicarlo en una frase
- [ ] Los 4 niveles + tipos funcionales/no funcionales memorizados

---

## 📅 Semana 3 — Cap 3 Static Testing (3 horas) ⭐⭐⭐⭐⭐

**Buena noticia:** Este es tu capítulo más fuerte. Lo hacés en 3 horas en vez de 5.

### Domingo (2 h)

**Bloque 1 (45 min) — Lectura rápida**
- `05_summaries/cap_03_estaticas_v4.md`
- Vas a reconocer TODO. Tu trabajo como Translation Officer + Executive Secretary era static testing puro.

**Bloque 2 (45 min) — La tabla clave: tipos de review**

Hacé esta tabla en tu cuaderno. Te la van a preguntar:

| Tipo | Quién conduce | Formalidad | Cuándo lo hacías |
|---|---|---|---|
| **Walkthrough** | El autor | Informal | Cuando explicabas un documento nuevo a alguien |
| **Technical review** | Revisor técnico | Semiformal | Cuando校对 un documento técnico (manual, policy) |
| **Inspection** | Moderador entrenado | Formal | Casi nunca, salvo auditoría |

**Bloque 3 (30 min) — Quiz Cap 3 + flashcards**
- `06_practice_tests/quizzes_por_capitulo/cap_03_quiz.md`
- **Meta: ≥80%** (8/10) — es muy corto, podés
- Anki: 15 cards

### Entre semana (1 h)

- Anki: repaso flashcards (15 min)
- **Mini-ejercicio:** agarrá CUALQUIER documento que tengas a mano (recibo, email, contrato, paper) y hacé una review informal. Anotá 1 defecto. Es la mejor forma de fijar este capítulo.

### ✅ Checkpoint fin de semana
- [ ] Quiz Cap 3: ≥80%
- [ ] Distingo walkthrough/technical/inspection
- [ ] Sé los 5 roles de un review

---

## 📅📅 Semanas 4-5 — Cap 4 Test Analysis & Design (10 horas) 🔴🔴🔴

**Por qué lo separamos en 2 semanas:** Cap 4 vale 30% del examen y tiene las técnicas formales (EP, BVA, decision tables, state transitions, ATDD) que requieren práctica con lápiz y papel. **No es difícil, solo requiere repetición.**

### Semana 4 — Black-box + White-box (5 h)

#### Domingo 1 (2.5 h)

**Bloque 1 (45 min) — Overview + EP**
- `05_summaries/cap_04_tecnicas_diseno_v4.md` (lee solo las secciones 1 y 2.1 — equivalence partitioning)
- **Ejercicio EP (30 min en cuaderno):**
  - Edad para votar (18-65): escribí 3 tests
  - Password (8-20 chars): escribí 4 tests
  - Email format: escribí 3 tests
  - Mirá `04_practice_exercises/EJERCICIOS_TRILINGUES.md` (este pack) para más práctica

**Bloque 2 (45 min) — BVA**
- Misma sección: lee 2.2 (BVA)
- **Ejercicio BVA (30 min en cuaderno):**
  - Edad 18-65: tests con 2-value y 3-value
  - Password 8-20: tests con 2-value y 3-value
  - **Truco:** EP+BVA siempre juntos. 4 valores = 4 tests mínimo.

**Bloque 3 (60 min) — Decision Tables + State Transitions**
- Lee 2.3 y 2.4 del summary
- **Ejercicio Decision Table (30 min):**
  - "Can I return this product?" — reglas: tiene recibo (sí/no), días desde compra (≤30/>30), condición (nuevo/usado)
  - Dibujá 4 reglas en una tabla
- **Ejercicio State Transition (30 min):**
  - Login system: estados = LOCKED, ACTIVE, DISABLED. Eventos = login_success, login_fail_3x, etc.
  - Dibujá el diagrama con flechas
  - Lista 4 transiciones válidas y 2 inválidas

#### Domingo 2 (2.5 h)

**Bloque 4 (60 min) — White-box (statement, branch coverage)**
- Lee 4.3 del summary
- **Ejercicio (30 min):** dado este pseudocódigo:
  ```
  function canVote(age) {
    if (age >= 18) {
      if (age <= 65) {
        return "puede votar"
      } else {
        return "no obligatorio"
      }
    } else {
      return "muy joven"
    }
  }
  ```
  - ¿Cuántas líneas ejecutables hay? (statement coverage)
  - ¿Cuántas ramas if hay? (branch coverage)
  - Escribí los tests mínimos para 100% statement y 100% branch

**Bloque 5 (45 min) — Experience-based**
- Lee 4.4 del summary
- **Reflexión:** ¿en qué momentos del día estás haciendo error guessing? (Interpretación: "este doctor seguro va a decir X mal")

**Bloque 6 (45 min) — Quiz Cap 4**
- `06_practice_tests/quizzes_por_capitulo/cap_04_quiz.md`
- **Meta: ≥75%** (23/30). **No te frustres si no llegás — Cap 4 es el más largo.**

### Semana 5 — Finish Cap 4 + Hard Mode (5 h)

#### Domingo (3 h continuas)

**Bloque 1 (90 min) — Lo nuevo v4.0: User Stories + ATDD (LO 4.5.1-4.5.3)**
- Lee las secciones 4.5.1, 4.5.2, 4.5.3 del summary
- **Ejercicio (60 min):** Escribí 3 user stories en formato "Como [user], quiero [acción], para [beneficio]"
  - Una para un paciente de clínica
  - Una para un seguidor de una red social
  - Una para un estudiante del curso ISTQB
- Para cada user story, escribí **acceptance criteria** en formato bullet
- Para una de ellas, escribí **test cases ATDD** (Given/When/Then)

**Bloque 2 (45 min) — Repaso de Cap 4**
- Volvé a leer TODO el summary de Cap 4
- Anki: 40 cards (es el capítulo más grande)

**Bloque 3 (45 min) — Hard Mode Quiz**
- `06_practice_tests/quizzes_por_capitulo/cap_4_5_hard_mode.md`
- **Meta: ≥70%** (14/20). Si llegás, vas muy bien para el examen.

### ✅ Checkpoint fin de semana
- [ ] Quiz Cap 4: ≥75%
- [ ] Hard mode: ≥70%
- [ ] Puedo aplicar EP, BVA, decision table, state diagram sin mirar apuntes
- [ ] Sé qué son user stories + acceptance criteria + ATDD

**Si llegás:** seguí a semana 6 con confianza.
**Si NO llegás en Cap 4:** dedicá 3 días más solo a Cap 4 antes de seguir. Es el capítulo que más cae.

---

## 📅 Semana 6 — Cap 5 (Management) + Cap 6 (Tools) (5 horas)

### Domingo (3.5 h)

**Bloque 1 (60 min) — Cap 5 conceptos clave**
- `05_summaries/cap_05_gestion_v4.md`
- **Las 4 tablas críticas para vos:**
  - Test pyramid (70-20-10)
  - Testing quadrants (Q1-Q4)
  - Project risk vs Product risk
  - Severity vs Priority (LO 5.5.1 — K3, va a caer)
- Hacé las 4 tablas en tu cuaderno

**Bloque 2 (60 min) — Defect report + Risk = L × I**
- **Ejercicio defect report (45 min):** Tomá una situación real tuya donde reportaste un problema (interpretación, CM, secretariado) y completá un defect report formal con todos los campos:
  - ID, title, severity, priority, steps, expected, actual, environment, attachments
- **Ejercicio Risk (15 min):** calculá L × I para 3 riesgos del proyecto ISTQB:
  - "No tener Anki" (L=alta, I=baja) → nivel medio
  - "No entender EP" (L=media, I=alta) → nivel alto
  - "Rendir el examen sin práctica" (L=baja si estudiaste, I=alta) → nivel bajo si estudiaste

**Bloque 3 (45 min) — Cap 6 (herramientas)**
- `05_summaries/cap_06_herramientas_v4.md`
- Solo vocabulario. Capítulo más corto. **Meta:** saber decir qué hace Jira, TestRail, Selenium, JMeter en una frase cada uno.

**Bloque 4 (45 min) — Quizzes + flashcards**
- `06_practice_tests/quizzes_por_capitulo/cap_05_quiz.md` — **meta ≥75%**
- `06_practice_tests/quizzes_por_capitulo/cap_06_quiz.md` — **meta ≥75%**
- Anki: 25 cards (Cap 5+6)

### ✅ Checkpoint fin de semana
- [ ] Quiz Cap 5: ≥75%
- [ ] Quiz Cap 6: ≥75%
- [ ] Severity vs Priority: distingo con ejemplos
- [ ] Risk: sé calcular L × I

---

## 📅 Semana 7 — Simulacros (6 horas) 🔴

**Esta semana es donde se confirma si estás lista.** Tres sample exams cronometrados.

### Domingo (4 h)

**Bloque 1 — Sample Exam A (3 h cronometradas)**
- `06_practice_tests/sample_exam_A.md`
- **Timer de 60 min en el celu.** Sin pausas. Sin mirar apuntes. Sin traductor. Solo vos y el examen.
- Cuando termine el tiempo, pará.
- Score honesto. Anotá: score total + tiempo + qué capítulos fallaste más.
- **Ahora sí:** leé `sample_exam_A_ANSWERS.md` con cada respuesta que fallaste

**Bloque 2 — Sample Exam B (60 min cronometrados)**
- `06_practice_tests/sample_exam_B.md`
- 60 min, sin parar.
- Score + análisis

### Entre semana — Sample Exam C + análisis (2 h)

- Sample Exam C — **cronometrado**
- Análisis de los 3 exámenes: ¿qué capítulo tiene el score más bajo?

### Domingo 2 (opcional, 2 h)
- Si tu peor capítulo fue Cap 4: re-leé el summary y hacé 5 ejercicios nuevos
- Si fue Cap 5: re-leé el skill transfer de Cap 5
- Si fueron varios: re-leé el cheatsheet global `08_quick_refs/cap_00_cheatsheet_global.md`

### ✅ Checkpoint fin de semana
- [ ] Sample Exam A: ≥65%
- [ ] Sample Exam B: ≥65%
- [ ] Sample Exam C: ≥65%
- [ ] Identifiqué mi peor capítulo

**Meta:** promediar ≥70% en los 3. Si llegás, **estás lista para el examen.**

---

## 📅 Semana 8 — Repaso final + EXAMEN (4 h)

### Lunes-Martes (2 h repartidas)

- Repasá cheat sheets: `08_quick_refs/cap_00_cheatsheet_global.md`
- Anki marathon: todas las cards
- Releé `10_exam_difficulty/README.md` (errores comunes)

### Miércoles (2 h)
- Re-tomá Sample Exam A cronometrado. **Meta: ≥75%** esta vez.
- Si llegás, estás ready.

### Jueves-Viernes (descanso activo)
- No estudies más de 30 min/día
- Glosario `03_glosario/GLOSARIO_v4.0.1.md` (skim rápido)
- Confirmá logística del examen: ASOLINFO, fecha, hora, documento de identidad, conectividad (si es online)

### Sábado (NO ESTUDIAR)
- Actividad relajada. Paseo. Familia.
- Dormí temprano.

### Domingo / fecha agendada — **¡RINDÍ!** 🎯

- Llegá 15 min antes
- 60 min, 40 preguntas
- Si no sabés una: marcá, seguí, volvé después
- 65% mínimo = 26 correctas

---

## 🎯 Resumen de metas semanales

| Sem | Cap | Horas | Meta score |
|---|---|---|---|
| 1 | 1 Fundamentals | 4 | Quiz ≥75% |
| 2 | 2 SDLC | 4 | Quiz ≥75% |
| 3 | 3 Static Testing | 3 | Quiz ≥80% |
| 4-5 | 4 Test Analysis & Design | 10 | Quiz ≥75%, Hard ≥70% |
| 6 | 5 Mgmt + 6 Tools | 5 | Quiz ≥75% |
| 7 | Sample exams | 6 | Promedio ≥70% |
| 8 | Repaso final + EXAMEN | 4 | ≥65% en el examen |

---

## 📞 Soporte durante las 8 semanas

Si en cualquier momento tenés:
- **Una duda sobre un concepto:** preguntame directo
- **Un quiz que te fue mal:** pegame tu score + las preguntas que fallaste y te ayudo a entender el patrón
- **Una semana que no pudiste cumplir:** decímelo y ajustamos el plan (podemos extender a 9-10 semanas sin drama)
- **Una pregunta del examen real que no entiendas:** la guardás y la discutimos después

---

## 📂 Siguiente archivo

→ [`../04_practice_exercises/EJERCICIOS_TRILINGUES.md`](../04_practice_exercises/EJERCICIOS_TRILINGUES.md) — Ejercicios extra (EN/ES/PT) para Cap 4, tu capítulo más pesado. Practicá con estos entre semana 4 y 5.

*Te voy a ir acompañando semana a semana. La idea es que en 8 semanas estés certificada.*
