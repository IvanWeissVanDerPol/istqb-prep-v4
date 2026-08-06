# Resumen Cap 5 (v4.0.1) — Managing the Test Activities

> **335 minutos oficiales** (~28% del syllabus). Segundo más pesado.

---

## 1. Test Planning (5.1)

### 1.1 Test Plan (5.1.1) ⭐

Documento que describe:
- **Purpose** — por qué
- **Scope** — qué se testea y qué NO
- **Approach** — estrategia (manual/auto, levels, types, técnicas)
- **Resources** — personas, herramientas, tiempo
- **Schedule** — calendario
- **Entry criteria** — cuándo empezar
- **Exit criteria** — cuándo terminar
- **Risks** — y contingencias
- **Deliverables** — qué se produce

### 1.2 Entry criteria vs Exit criteria (5.1.3) ⭐⭐

**Entry criteria** — qué debe cumplirse ANTES de empezar:
- Requisitos listos
- Ambiente preparado
- Recursos disponibles

**Exit criteria** — qué debe cumplirse ANTES de terminar:
- % test cases ejecutados
- % cobertura alcanzada
- No defects críticos abiertos
- Plan firmado

> Trampa v4.0.1: NO son sinónimos. "**entry criteria OR exit criteria**" (no combined).

### 1.3 Test Case Prioritization (5.1.5) ⭐ K3

**Por qué priorizar:**
- No siempre se corre toda la suite
- Asignar esfuerzo a lo más importante
- Riesgo primero

**Técnicas de priorización:**
- **Risk-based** — tests de mayor riesgo primero
- **Coverage-based** — primero los que cubren más funcionalidades
- **Requirements-based** — por requisitos críticos
- **Historical defects** — áreas con más bugs previos

### 1.4 Test Estimation (5.1.4) ⭐ K3

**Técnicas:**
- **Expert judgment / analogy** — experto estima
- **Percentages** — X% del esfuerzo de development
- **Wideband Delphi** — expertos estiman en iteraciones anónimas hasta converger (3 rondas típicamente)
- **3-point estimation (PERT)** — optimista + pesimista + más probable → weighted average

### 1.5 🆕 Test Pyramid (5.1.6) ⭐ NUEVO

**Concepto:** cómo organizar tus tests en **3 capas**:

```
        ▲   E2E / UI tests         ← pocos
       ╱ ╲
      ╱───╲  Integration/API tests ← algunos
     ╱─────╲
    ╱───────╲  Unit tests           ← muchos
```

**Mnemotécnica:** "pirámide = mucho abajo, poco arriba"

**Razón:**
- Unit tests son rápidos + baratos → MUCHOS
- E2E son lentos + frágiles → POCOS
- Balance ideal: ~70% unit, ~20% integration, ~10% E2E

**Trampa v4.0.1:** "higher layer = LOWER test isolation" (correcto en v4.0.1; era mal dicho en v3.1).

### 1.6 🆕 Testing Quadrants (5.1.7) ⭐ NUEVO

**2x2 matriz** que relaciona niveles (técnico vs business) con tipos (funcionales vs no-funcionales):

| | Functional | Non-functional |
|---|---|---|
| **Business-facing** | Q1 (Functional) | Q3 (Performance, load) |
| **Technology-facing** | Q2 (Component, integration) | Q4 (Security, reliability) |

**Aplicación:**
- Q1: UAT, exploratory
- Q2: Component testing, integration testing
- Q3: Performance testing (JMeter)
- Q4: Security testing (penetration, security scans)

**Stacey matrix** dice dónde está cada quadrant en el modelo ágil.

---

## 2. Risk Management (5.2) ⭐⭐

### 2.1 Risk Level (5.2.1) ⭐

**Risk = likelihood × impact (risk level)**

**Risk matrix:**

| Likelihood \ Impact | Low | Medium | High |
|---|---|---|---|
| **Low** | Low | Low | Medium |
| **Medium** | Low | Medium | High |
| **High** | Medium | High | High |

### 2.2 Project Risks vs Product Risks (5.2.2) ⭐⭐

**Project risks** — afectan schedule/cost/quality del proyecto:
- Falta de personal
- Plazos ajustados
- Cambios de scope
- Problemas técnicos
- Skills gaps

**Product risks** — afectan calidad del producto:
- Software complejo
- Áreas con defectos históricos
- Arquitectura insegura
- Módulos críticos para el negocio

> **Mnemotécnica:** "Project = meta del proyecto (cómo se hace); Product = meta del producto (qué se hace)"

### 2.3 Risk Analysis Influence (5.2.3)

Cómo el análisis de riesgos afecta:
- **Thoroughness** (qué tan exhaustivo)
- **Test scope** (qué se incluye/excluye)

### 2.4 Response (5.2.4)

- **Accept** — riesgo aceptable
- **Mitigate** — tomar acciones para reducirlo
- **Transfer** — pasarlo a otro (seguro)
- **Avoid** — eliminar la causa del riesgo

---

## 3. Test Monitoring, Control, Completion (5.3)

### 3.1 Metrics (5.3.1) ⭐

**Métricas típicas:**
- % test cases ejecutados
- % pass rate
- Defects encontrados vs resueltos
- Schedule variance
- Coverage achieved

> Trampa v4.0.1: **"test progress reporting"** vs **"test completion reporting"** son DIFERENTES (no sinonimo):
> - Progress = ongoing test execution status
> - Completion = al cerrar el proyecto, lessons learned

### 3.2 Test Reports (5.3.2)

**Tipos:**
- **Test progress report** — durante testing (status)
- **Test completion report** — al cerrar proyecto (resumen + lecciones)

**Audiencias:**
- Stakeholders: resumen ejecutivo
- Project team: detalle técnico

### 3.3 Communication (5.3.3)

- Status updates frecuentes
- Riesgos visibles
- Issues escalados

---

## 4. Configuration Management (5.4)

**Soporte que da CM al testing:**
- Traceability (requisito → test → defect)
- Versionado de testware
- Repositorio único para testware
- Control de cambios
- Baseline management

---

## 5. Defect Management (5.5) ⭐⭐⭐

### 5.1 Defect Report — K3 ⭐⭐

**Campos obligatorios (recomendado ISTQB):**
- **ID** — único
- **Title** — resumen corto
- **Description** — qué pasó
- **Steps to reproduce** — cómo reproducirlo
- **Expected vs actual** — qué esperabas / qué pasó
- **Severity** — impacto técnico (high/medium/low)
- **Priority** — urgencia fix (high/medium/low)
- **Status** — actual (open, assigned, resolved, verified, closed, reopened, rejected, deferred)
- **Reporter** — quién lo reportó
- **Assigned to** — quién lo arregla
- **Environment** — dónde pasó
- **Attachment** — screenshots, logs

### 5.2 Severity vs Priority ⭐⭐

**Severity** = IMPACTO en el sistema:
- High: crash, pérdida de datos
- Medium: feature rota pero hay workaround
- Low: cosmético, pequeña molestia

**Priority** = URGENCIA de fixear:
- High: fix immediately
- Medium: fix soon
- Low: fix cuando se pueda

> **NO siempre coinciden:** un bug cosmético en la página de login (baja severity) puede tener ALTA priority (afecta todas las visitas).

### 5.3 Defect Lifecycle

```
New → Assigned → In Progress → Resolved → Verified → Closed
  ↓        ↓                                       ↑
  Rejected  Deferred                              Reopened
```

---

## 🎯 Preguntas típicas del Cap 5

1. **Test plan es para:**
   - Planear testing (a) ✔
2. **Project risks afectan:**
   - Schedule/cost del proyecto (a) ✔ (no la calidad del producto)
3. **Severity vs priority son:**
   - Distintos conceptos (a) ✔
4. **Test pyramid bottom =:**
   - Unit tests (a) ✔ (muchos)
5. **Test quadrants — Q1 es para:**
   - Functional business-facing (a) ✔
6. **Wideband Delphi usa:**
   - Iteraciones de expertos (a) ✔
7. **Risk level se calcula con:**
   - Likelihood × impact (a) ✔
8. **High priority + low severity puede pasar cuando:**
   - Bug cosmético en página popular (a) ✔

---

## 📝 Mnemotécnicos

- **Entry vs Exit:** "ENTRAR fácil, SALIR probando"
- **Project vs Product risks:** "PROJECT = personas/coste, PRODUCT = producto"
- **Severity vs Priority:** "SEVERIDAD = Daño, PRIORIDAD = Rapidez"
- **Test Pyramid:** "mucho abajo, poco arriba"
- **Quadrants:** "Q1=Q2 funcional; Q3=Q4 no-funcional"
- **Estimación:** "PERT = (opt + pes + 4*ml) / 6"
- **Risk response:** "AMTA — Aceptar, Mitigar, Transferir, Avoid"
