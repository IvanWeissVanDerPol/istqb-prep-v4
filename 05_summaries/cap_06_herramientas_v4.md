# Resumen Cap 6 (v4.0.1) — Test Tools

> Solo 20 minutos oficiales — el cap más corto del syllabus.

---

## 1. Tipos de Test Tools (6.1) ⭐

**ISTQB clasifica las herramientas en categorías:**

### Test Management tools
- **Función:** gestionar el proceso de testing
- **Ejemplos:** Jira + Xray/Zephyr, TestRail, qTest, Qase

### Test Design and Test Implementation tools
- **Función:** asistir en diseño de test cases
- **Ejemplos:** Tools para modelar state diagrams, decision tables

### Static Analysis tools
- **Función:** analizar código SIN ejecutar
- **Ejemplos:** Linters (ESLint, Pylint, RuboCop), SonarQube, Coverity

### Test Execution tools
- **Función:** ejecutar tests automáticamente
- **Ejemplos:** Selenium, Playwright, Cypress, Postman (API tests), JMeter (performance)
- **Sub-tipos:** UI testing, API testing, performance testing, load testing

### Test Data Preparation tools
- **Función:** generar, anonimizar o transformar datos de test
- **Ejemplos:** Faker (Python), generar scripts SQL, scripts de anonimización

### Test Support tools (6.1)
- Coverage tools
- Defect tracking
- Environment virtualization

### Test Monitoring tools
- Dashboards
- Métricas

---

## 2. Beneficios y Riesgos de Test Automation (6.2)

### Beneficios (6.2.1)

- **Velocidad** — corre más rápido que humanos
- **Repetibilidad** — sin cansancio humano
- **Reusabilidad** — los tests se pueden ejecutar en distintos envs
- **Consistencia** — sin variabilidad humana
- **Cobertura** — permite más tests
- **Confianza** — feedback rápido

### Riesgos

- **Expectativa falsa** de que 100% auto = no bugs
- **Mantenimiento alto** — scripts se rompen con cualquier cambio UI
- **Costos iniciales altos**
- **Necesita skills específicas** (scripting, herramientas)
- **Reemplaza al tester humano** solo para ciertas tareas

### Por qué NO automatizar todo

- **Bugs visuales/UX** requieren ojo humano
- **Tests exploratorios** requieren creatividad
- **Tests únicos** (1-shot) no valen el esfuerzo

---

## 🎯 Preguntas típicas

1. ¿Cuál es un ejemplo de static analysis tool?
2. ¿Cuál es un beneficio de automation?
3. ¿Cuál es un RIESGO de automation?
4. ¿Qué tool NO es de test management?

---

## 📝 Mnemotécnicos

- **Categorías de tools:** "Mngr, Design, Static, Execution, Data, Support, Monitoring"
- **Risk/benefit:** "BAJA 100% → 100% bugs"
- **Tooling scripture:** "Test insight ≠ test automation"
