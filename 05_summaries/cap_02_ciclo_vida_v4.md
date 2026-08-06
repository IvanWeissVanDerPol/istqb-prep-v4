# Resumen Cap 2 (v4.0.1) — Testing Throughout the SDLC

## 1. SDLC y su impacto en testing (2.1)

### 1.1 Modelos SDLC (2.1.1) ⭐

| Modelo | Característica | Impacto en testing |
|---|---|---|
| **Sequential (Waterfall)** | Phases one-by-one | Testing casi al final, riesgo alto |
| **Iterative** | Ciclos repetidos | Testing continuo + regression obligatorio |
| **Incremental** | Entrega por partes | Testing de cada incremento |
| **Agile (Scrum, XP)** | Sprints cortos | Testing integrado, automatización masiva |
| **DevOps** | CI/CD continuo | Testing dentro de pipeline |

**Conceptos nuevos oficiales en v4.0.1:**
- **Shift-left (2.1.5) ⭐** — testing se mueve lo más temprano posible en el ciclo. Tests definidos ANTES del código. Beneficios: detectar defectos temprano, reducir costo de fix.
- **Retrospectives (2.1.6) ⭐** — al final de cada iteración, el equipo reflexiona qué mejorar. Sirven como mecanismo de mejora continua del proceso de testing.
- **DevOps (2.1.4) ⭐** — combinación de desarrollo + operaciones. Impacto en testing: testing continuo, monitoreo en producción, feedback loop rápido.

### 1.2 Test-first approaches (2.1.3) ⭐ NUEVO en v4.0

- **TDD (Test-Driven Development)** — developer escribe test ANTES del código
- **ATDD (Acceptance Test-Driven Development)** — equipo (dev+test+business) escribe acceptance tests ANTES del código
- **BDD (Behavior-Driven Development)** — ejemplos en lenguaje natural (Given/When/Then) que se traducen a tests

---

## 2. Niveles de Testing (2.2.1) ⭐⭐

```
                    Acceptance (validación usuario)
                    ↑
                    System (todo el sistema)
                    ↑
                    Integration (interfaces entre componentes)
                    ↑
                    Component Integration (componente ↔ DB, FS, etc.)
                    ↑
                    Component (unitario aislado)
```

### ⭐ Diferencia Component vs Component Integration vs Integration

**Crítico para el examen — confunden mucho:**

- **Component testing** — testea UNA pieza aislada (con mocks/stubs). Owner: developer.
- **Component integration testing** — testea cómo un componente interactúa con infraestructura externa (DB, file system, servicios). Owner: developer.
- **Integration testing** — testea interfaces entre componentes. Múltiples componentes juntos. Owner: developer o tester.

### Acceptance testing (sub-tipos 2.2)

- **User Acceptance (UAT)** — usuarios prueban aceptación
- **Operational Acceptance (OAT)** — operaciones (backup, deployment, monitoring)
- **Contractual Acceptance** — cumplimiento de contrato
- **Regulatory Acceptance** — cumplimiento legal
- **Alpha** — en sitio del developer
- **Beta** — en sitio del cliente/usuarios

---

## 3. Tipos de Testing (2.2.2) ⭐⭐

### Functional vs Non-functional

| Functional | Non-functional |
|---|---|
| **Qué** hace el sistema | **Cómo de bien** lo hace |
| ¿Cumple requisitos funcionales? | ¿Performance, seguridad, usabilidad? |

### 🆕 Tipos según ISO 25010:2023 (actualizado v4.0.1)

**Functional:** ¿hace lo que debe?
**Performance Efficiency:** ¿rápido y eficiente?
**Compatibility:** ¿corre en distintos entornos?
**Interaction capability (antes: usability):** ¿fácil de usar?
**Reliability:** ¿estable, no falla?
**Security:** ¿protegido?
**Maintainability:** ¿fácil de mantener?
**Flexibility (antes: portability):** ¿se transfiere/adapta?
**+ Safety (NUEVO):** ¿es seguro para personas/datos?

> **Trampa:** "usability" sigue funcionando coloquialmente pero en el examen v4.0.1 = **"interaction capability"**.

### Structural testing
- Basado en **estructura interna** del código (white-box)
- Común en component testing

### Change-related (2.2.3) ⭐⭐

- **Confirmation testing (re-testing):** verificás que un defecto específico está fixed
  - Ejemplo: bug #123 era que el botón no respondía — testear específicamente ese botón después del fix
- **Regression testing:** verificás que cambios no rompieron features existentes
  - Ejemplo: ejecutar suite completa de tests después del fix

**Distinción clave:**
- Confirmation = ese bug específico está OK
- Regression = nada más se rompió

---

## 4. Maintenance Testing (2.3)

Modificaciones en producción.

**Triggers (cuándo se dispara):**
- Migration (datos o tecnología)
- Retirement (decommission)
- Nuevos environments
- Correcciones post-deployment

**Diferencia del development testing:** a menudo **no hay specs actualizados**, hay que investigar el sistema existente.

---

## 🎯 Preguntas típicas del cap

1. **¿Cuál NO es un nivel?** → Functional (es TIPO)
2. **Component testing es usualmente ejecutado por...** → Developer
3. **¿Shift-left significa?** → Testing se hace temprano en el ciclo
4. **Confirmation vs Regression:** cuáles son las diferencias (ya explicadas)
5. **¿Cuál es ISO 25010 nuevo?** → Safety
6. **Beta testing se hace en...** → sitio del cliente
7. **Retrospectives son para...** → mejora continua del proceso

---

## 📝 Mnemotécnicos

- **Niveles:** "C-CIS-A" (Component, Component Integration, Integration, System, Acceptance)
- **Tipos Functional/Non-func:** "QUIÉN vs CÓMO"
- **Confirmation vs Regression:** "ESE bug vs NINGÚN otro"
- **Shift-left:** "izquierda del cronograma = temprano"
- **ISO 25010 cambios:** "IFS replaced by FFS" (Interaction+Safety added; Portability→Flexibility; Usability→Interaction capability)
