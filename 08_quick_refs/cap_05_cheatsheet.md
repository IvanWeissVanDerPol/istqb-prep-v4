# Cap 5 — Quick Reference (1 página)

```
MANAGING THE TEST ACTIVITIES — 335 minutos oficiales
────────────────────────────────────────────────────
16 LOs: 4 K1, 11 K2, 1 K3
```

## TEST PLAN (5.1.1)

Documento que describe: Purpose, Scope, **Approach**, Resources, Schedule, **Entry/Exit criteria**, Risks, Deliverables.

## ENTRY vs EXIT criteria (5.1.3) ⭐

| Entry | Exit |
|---|---|
| ANTES de empezar | ANTES de cerrar |
| Requisitos listos | Cobertura alcanzada |
| Ambiente preparado | No defects críticos abiertos |

**NO son sinónimos** (v4.0.1 lo aclara).

## TEST CASE PRIORITIZATION (5.1.5)

Por riesgo / cobertura / históricos. K3 — usa este criterio.

## ESTIMATION TECHNIQUES (5.1.4)

- Expert judgment / analogy
- Wideband Delphi (rondas anónimas)
- 3-point PERT (Opt + Pes + 4*ML) / 6
- Percentages (% del esfuerzo de dev)

## 🆕 TEST PYRAMID (5.1.6)

```
        ▲  UI / E2E                ← POCOS (~10%)
       ╱ ╲
      ╱───╲  API / Integration    ← ALGUNOS (~20%)
     ╱─────╲
    ╱───────╲  Unit                ← MUCHOS (~70%)
```

## 🆕 TESTING QUADRANTS (5.1.7)

| | Functional | Non-functional |
|---|---|---|
| **Business-facing** | Q1 (UAT, exploratory) | Q3 (perf, load) |
| **Technology-facing** | Q2 (component, integration) | Q4 (security) |

## RISK MANAGEMENT (5.2)

**Risk level = likelihood × impact**

| | Low Impact | Med | High Impact |
|---|---|---|---|
| **Low Like** | Low | Low | Med |
| **Med Like** | Low | Med | High |
| **High Like** | Med | High | High |

**Project risks (5.2.2)** → schedule, coste, calidad del proyecto
**Product risks (5.2.2)** → calidad del producto final

**Risk responses (5.2.4):** Accept, Mitigate, Transfer, Avoid

## TEST METRICS (5.3.1)

- % test cases ejecutados
- % pass rate
- Defects found/resolved
- Coverage achieved
- Schedule variance

**Reports (5.3.2):**
- **Progress report** — ongoing status
- **Completion report** — al cerrar (lessons learned)

## CONFIG MANAGEMENT (5.4)

Traceability, versionado, baseline, repositorio único.

## DEFECT REPORT (5.5.1) — K3 ⭐⭐

Campos obligatorios:
- **ID + Title**
- **Description**
- **Steps to reproduce**
- **Expected vs Actual**
- **Severity + Priority**
- **Status** (New → Assigned → InProgress → Resolved → Verified → Closed)
- **Reporter + Asignee**
- **Environment**
- **Attachments**

## SEVERITY vs PRIORITY ⭐⭐

| Severity = IMPACTO técnico | Priority = URGENCIA fix |
|---|---|
| High = crash, data loss | High = fix immediate |
| Med = feature rota | Med = fix soon |
| Low = cosmético | Low = fix cuando se pueda |

**Caso especial:** cosmético en página popular = low severity + high priority.
