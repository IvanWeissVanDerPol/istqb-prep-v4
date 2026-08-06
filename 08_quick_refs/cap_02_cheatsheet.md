# Cap 2 — Quick Reference (1 página)

```
TESTING THROUGHOUT THE SDLC — 130 minutos oficiales
───────────────────────────────────────────────────
10 LOs: 2 K1, 8 K2
```

## 4 NIVELES DE TESTING

```
        Acceptance (validación usuario)
        ↑
        System (todo el sistema integrado)
        ↑
        Integration (interfaces entre componentes)
        ↑ (+ Component Integration: componente vs infra)
        Component / Unit (individual, aislado)
```

## TIPOS

- **Functional** — QUÉ hace el sistema
- **Non-functional** — CÓMO de bien (performance, security, etc.)
- **Structural / White-box** — estructura interna
- **Change-related** — confirmation + regression

## ISO 25010:2023 — 8 characteristics + safety

```
┌────────────────────────┬────────────────────────┐
│ Functional             │ Performance efficiency │
│ Compatibility          │ Interaction capability │ ← antes Usability
│ Reliability            │ Security               │
│ Maintainability        │ Flexibility            │ ← antes Portability
│ (Safety NEW)                                    │
└────────────────────────┴────────────────────────┘
```

## CONFIRMATION vs REGRESSION ⭐

- **Confirmation**: "ese bug específico está fixed"
- **Regression**: "ningún otro componente se rompió"

## SHIFT-LEFT (2.1.5) NUEVO v4.0

Testing se mueve lo más TEMPRANO posible en el SDLC.
Antes del código: tests + specs ya están listos.

## DEVOPS (2.1.4) NUEVO v4.0

Testing continuo en CI/CD pipeline. Monitoreo en producción.
Feedback loop rápido.

## RETROSPECTIVES (2.1.6) NUEVO v4.0

Mecanismo de mejora continua al final de cada iteración/sprint.

## TEST-FIRST (2.1.3) NUEVO énfasis

- **TDD** — developer escribe unit tests antes del código
- **ATDD** — equipo escribe acceptance tests antes del código
- **BDD** — given-when-then natural language

## CONFIRMATION / REGRESSION en cada nivel

Cualquier nivel puede tener cualquier tipo. Ej: **Functional testing en system level** es lo más común.

## MAINTENANCE TESTING (2.3)

Modificaciones post-deployment.
Triggers: migration, retirement, nuevos environments.
