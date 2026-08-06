# 🔄 Cambios CTFL v3.1 (2018) → v4.0.1 (2024)

> Material viejo (v3.1) aún circula online. **Si estás preparando el examen 2025+, estudio con material v4.0.1.**

## 🚨 Resumen ejecutivo

**v4.0 (abril 2023) + v4.0.1 errata (sep 2024):** update MAYOR. **No es solo cambios menores.**

Esta versión:
- Reduce drásticamente el syllabus (de más largo a más conciso)
- **Fusiona contenidos del Agile Tester 2014** (un certificado ISTQB separado antes)
- Cambia vocabulario para alinearlo con el glosario oficial
- Introduce conceptos modernos (DevOps, Shift-left, Test Pyramid, ATDD)
- Actualiza ISO 25010 (2023)

---

## 📋 Cambios capítulo por capítulo

### **Cap 1 — Fundamentals of Testing**

**Lo que se mantuvo:**
- 7 principios de testing (sigue apareciendo 1.3.1)
- Conceptos error → defect → failure (1.2.3)
- Roles en testing (1.4.5)

**Lo que cambió:**
- 1.4.1 — antes "summarize test activities" → ahora "**explain**" (nivel K2 más alto)
- 1.4.4 — "value of maintaining traceability" — nuevo énfasis
- ISO 25010 actualizaciones aplican también a este capítulo

**Nuevo vocabulario obligatorio:**
- "work products" (en lugar de "documentation")
- "test process" (en lugar de "test project")

---

### **Cap 2 — Testing Throughout the SDLC**

**Lo que se mantuvo:**
- Niveles: Component, Integration, System, Acceptance
- Tipos: Functional, Non-functional, Structural, Change-related
- Confirmation testing vs Regression testing (2.2.3)

**NUEVO / Cambió:**
- **2.1.4 DevOps** — impacto en testing (NUEVO)
- **2.1.5 Shift left** — concepto oficial (NUEVO)
- **2.1.6 Retrospectives** — mejora de proceso (NUEVO)
- **2.1.3 Test-first approaches** — incluye BDD, ATDD, TDD (NUEVO énfasis)

**Vocabulario actualizado:**
- "iterative development models and incremental development models" (antes juntos)
- "stage" → "phase"

---

### **Cap 3 — Static Testing**

**Lo que se mantuvo:**
- 3.2.2 Review process activities
- 3.2.3 Roles principales en reviews
- 3.2.4 Tipos de review

**Lo que cambió:**
- 3.1.1 cambió a "work products that can be examined by static testing" (anterior: "different static test techniques")
- 3.1.3 — comparación explicit "static vs dynamic testing"
- 3.2.1 — énfasis en feedback temprano de stakeholders

**Importante:**
- "early and frequent stakeholder feedback" es ahora punto explícito

---

### **Cap 4 — Test Analysis and Design (el más cambiado)**

**Lo que se mantuvo (lo esencial):**
- 4.1.1 Distinguir black-box, white-box, experience-based
- **4.2.x Black-box:** EP, BVA, Decision Table, State Transition (todos K3 — apply)
- **4.3.x White-box:** Statement, Branch (K2 — explain)
- **4.4.x Experience-based:** Error guessing, Exploratory, Checklist-based

**NUEVO IMPORTANTE — Sección 4.5: Collaboration-based Test Approaches**
- **4.5.1 User stories** — escribir en colaboración con devs/business
- **4.5.2 Acceptance criteria** — opciones (Given/When/Then, etc.)
- **4.5.3 ATDD** (Acceptance Test-Driven Development) — derivar test cases ← K3 apply

**Cambios en redacción:**
- "test object" → "test item" (4.2.1)
- 4.2.1 — invalid EP deben testearse en **isolation** (para evitar defect masking)
- 4.2.4 "state transition diagram" → "state diagram" (nombre técnico correcto)
- "step" → "test step"

---

### **Cap 5 — Managing Test Activities**

**Lo que se mantuvo:**
- 5.1 Test Planning
- 5.2 Risk Management (product vs project)
- 5.5 Defect Management

**NUEVO importante:**
- **5.1.6 Test Pyramid** — concepto (K1)
- **5.1.7 Testing Quadrants** — relaciones entre levels y types (K2)
- **5.1.5 Test case prioritization** — K3 apply
- **5.3.1 Test metrics** — común confundido: "test progress reporting" vs "test completion reporting"

**Vocabulario:**
- "entry/exit criteria" → "entry criteria OR exit criteria" (no usar como sinonimo)
- "test strategy" (NUEVO keyword)
- "contractual and regulatory acceptance testing" → "contractual acceptance testing AND regulatory acceptance testing"

---

### **Cap 6 — Test Tools**

**Lo que cambió:**
- **Drásticamente reducido** — de varios subtopics a apenas 3 K-level LOs
- **6.1.1** "Different types of test tools support testing" (K2)
- **6.2.1** "Benefits and risks of test automation" (K1)
- Antes tenía gestión de herramientas, tipos por categoría, etc.

**Vocabulario:**
- 6.2 — "defect rate" → "failure rate"
- "Test design and implementation tools" → "Test design and test implementation tools"

---

## 🔑 Cambios de vocabulario críticos para el examen

| Antiguo (v3.1) | Nuevo (v4.0.1) |
|---|---|
| documentation | work products |
| stage | phase |
| white box / white-box testing | white-box testing |
| defect rate | failure rate |
| entry/exit criteria | entry criteria OR exit criteria |
| test object | test item |
| step | test step |
| stage of testing | test activity |
| test project objectives | test objectives |
| usability | interaction capability (ISO 25010:2023) |
| portability | flexibility (ISO 25010:2023) |
| safety | (NEW in ISO 25010:2023) |
| organizational test policy | test policy |
| reporting on test progress | test progress reporting |
| shift-left / shift-left approach / shift-left strategy | shift left |
| white box | white-box |

---

## 🚨 Trampas si estudias con material viejo

1. **"Usability testing"** cambió a "interaction capability testing" — si te aparece la palabra "usability" en un examen v4.0.1, sabé que **NO es la nueva terminología**, y eso es trampa.
2. **"Portability testing"** → "flexibility testing" en v4.0.1.
3. **"White box testing"** → "**white-box testing**" (con guión).
4. **"Stage"** → "**phase**" en cualquier contexto.
5. **"Documentation"** → "**work products**".
6. **"test pyramid"** es ahora material oficial. Si no lo conocés, perdés 1-2 preguntas seguras.
7. **"Shift-left"** aparece en Cap 2. Si nunca lo estudiaste, perdés 1-2 preguntas.

---

## 📊 Cambios en la estructura del examen

**Diferencia importante:**
- El examen sigue siendo **40 preguntas, 60 min, 65% mínimo** — eso no cambió.
- Lo que cambió es la **distribución de pesos por capítulo** y el **énfasis**:

| Cap | v3.1 peso aprox. | v4.0.1 peso aprox. | Notas |
|---|---|---|---|
| 1 — Fundamentals | ~17.5% (7) | ~12.5% (5) | Menos énfasis |
| 2 — SDLC | ~12.5% (5) | ~17.5% (7) | MÁS énfasis (DevOps, shift-left) |
| 3 — Static | ~7.5% (3) | ~5% (2) | Menos |
| 4 — Test Analysis | ~25% (10) | ~30% (12) | MÁS — incluyendo ATDD |
| 5 — Managing | ~12.5% (5) | ~17.5% (7) | MÁS énfasis (test pyramid, prioritization) |
| 6 — Tools | ~7.5% (3) | ~5% (2) | Menos |
| Mix / cross-chapter | ~17.5% (7) | ~12.5% (5) | Menos |

**📢 Lo más importante:**
- **Cap 4 sigue siendo el más pesado** (~30%)
- **Cap 5 ganó mucho peso** (test pyramid, prioritization, retro)
- **Cap 2 ganó peso** (DevOps, shift-left, retros)

---

## ✅ Lo que tenés que hacer diferente si ya estudiaste v3.1

1. **Volvé a leer** las secciones nuevas (4.5, 5.1.6-7, 2.1.4-6)
2. **Memorizá el vocabulario actualizado** — esta es la mayor trampa
3. **Practica ATDD** (un concepto que no existía en v3.1)
4. **Desechá preguntas de examen v3.1** que hablen de "usability" o "portability" en sentido antiguo

---

## 📅 Línea de tiempo oficial

| Versión | Fecha | Status |
|---|---|---|
| v1.0 | 2005 | Histórico |
| v3.1.1 | jul 2021 | Copyright update |
| v4.0 | abr 2023 | Release general — mayor cambio |
| **v4.0.1** | **15-sep-2024** | **Errata actual** ← La que se examina hoy |
| vNext | TBA | Probable en 2026-2027 |

**Estudiá con v4.0.1.** Material v3.1 es 5+ años viejo.
