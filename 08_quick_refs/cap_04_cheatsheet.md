# Cap 4 — Quick Reference (1 página) 🔴 MÁS PESADO

```
TEST ANALYSIS AND DESIGN — 390 minutos oficiales (1/3 del syllabus)
──────────────────────────────────────────────────────────────────
14 LOs: 5 K3, 9 K2   ← único cap con K3 (apply)
```

## 3 (+1) FAMILIAS DE TÉCNICAS (4.1.1)

- **Black-box** (4.2) — basado en specs
- **White-box** (4.3) — basado en código
- **Experience-based** (4.4) — intuición
- 🆕 **Collaboration-based** (4.5) — user stories + ATDD

## EP — EQUIVALENCE PARTITIONING (4.2.1)

```
input range 1-100

├── 1-50 (válido) → 25
├── 51-100 (válido) → 75
└── <1, >100 (inválido) → 0, 150

Tests: 4 totales (EP recomienda 1 valor/partición)
```

## BVA — BOUNDARY VALUE ANALYSIS (4.2.2)

```
Para 1-100: testa 0, 1, 100, 101
4 valores, 2 dentro / 2 fuera
```

## DECISION TABLE (4.2.3)

| Condiciones / Reglas | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| User válido | T | T | F | F |
| Pass válido | T | F | T | F |
| Acción | OK | Retry | Retry | Retry |

Reglas = 2^n condiciones. **Invalidar** inválidas si no aplica.

## STATE TRANSITION (4.2.4)

```
         Login OK
[Idle] ───────────→ [Logged In]
   │                    │
   │ fail               │ logout
   ↓                    ↓
[Locked]              [Idle]

Testear: cada transición + transiciones inválidas
(antes: state transition diagram, ahora: state diagram)
```

## STATEMENT vs BRANCH COVERAGE (4.3)

| Coverage | Mide | Coverage % | Más fuerte |
|---|---|---|---|
| Statement | Líneas ejecutadas | 100% cuando todas las líneas corrieron | No |
| Branch | Decisiones evaluadas a true/false | 100% implica 100% statement | Sí |

## 3 EXPERIENCE-BASED (4.4)

- **Error guessing** — adivinas bugs por experiencia
- **Exploratory** — diseño + ejecución simultáneos (charter + timebox)
- **Checklist-based** — listas predefinidas

## 🆕 COLLABORATION-BASED (4.5)

- **User story:** "Como <rol>, quiero <acción>, para <beneficio>"
- **INVEST:** Independent, Negotiable, Valuable, Estimable, Small, Testable
- **Acceptance criteria:** Given-When-Then / Checklist / Scenario
- **ATDD:** equipo (3 amigos: dev+test+business) escribe acceptance tests ANTES del código
