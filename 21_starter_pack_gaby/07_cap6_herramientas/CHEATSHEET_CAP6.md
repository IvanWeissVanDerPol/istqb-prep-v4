# 📋 Cheatsheet Cap 6 — Herramientas (1 página)

> *Imprimible. Para repaso rápido.*

---

## 🎯 ISTQB en 1 frase

> Las herramientas de testing **asisten** al tester (no lo reemplazan). Hay 8 categorías. Antes de adoptar una herramienta, evaluá con los 6 pasos formales.

---

## 🛠️ Las 8 Categorías de herramientas (LO 6.1.1, 6.4.1) ⭐⭐

| # | Categoría | Qué hace | Dental analog | Ejemplo real |
|---|---|---|---|---|
| 1 | **Test Management** | Gestionar planes, casos, ejecución, métricas | Tu agenda + sistema de gestión | TestRail, Zephyr, qTest |
| 2 | **Bug Tracking / Defect Management** | Registrar, asignar, seguir defects | Epicrisis + seguimiento de complicaciones | Jira, GitHub Issues, Linear |
| 3 | **Test Data Preparation** | Preparar datos para tests | Modelos, radiografías de prueba | Generadores de datos sintéticos |
| 4 | **Test Execution / Automation** | Ejecutar tests automáticamente | El autoclave (ciclo automático) | Selenium, Cypress, Playwright |
| 5 | **Static Analysis** | Analizar código sin ejecutar | Revisar la radiografía antes | SonarQube, ESLint, Pylint |
| 6 | **Performance Testing** | Medir velocidad y carga | ¿Cuánto tarda la historia clínica? | JMeter, Gatling, k6 |
| 7 | **Test Design** | Ayudar a diseñar tests | Plantillas de protocolos | Modeladores |
| 8 | **DevOps / CI/CD** | Testear automáticamente cada cambio | Autoclave valida temperatura, no avanza si falla | Jenkins, GitHub Actions, GitLab CI |

> 📌 **Las 8 categorías** salen en el examen. Memorizar.

---

## 📋 6 Pasos para adoptar una herramienta (LO 6.3.1) ⭐

```
1. ASSESSMENT          ¿Qué problemas resuelve? ¿Realmente la necesitás?
2. PROOF OF CONCEPT    Probala en un proyecto pequeño
3. TOOL SELECTION      Elegí entre las opciones
4. PILOT               Probá en real, en pequeño
5. ROLLOUT             Expansión gradual
6. REVIEW              ¿Estuvo a la altura? ¿Seguimos?
```

**Dental:** antes de comprar un escáner intraoral:
1. ¿Lo necesitás? (¿cuántos pacientes/día?)
2. Probalo en una jornada
3. Elegí marca/modelo
4. Usalo 1 semana
5. Expandí su uso
6. Revisá si sirvió

---

## ⚠️ Riesgos de las herramientas (LO 6.1.2) ⭐

| Riesgo | Dental analog |
|---|---|
| **Vendor lock-in** (dependencia) | "Si se rompe el autoclave, ¿quién me lo arregla?" |
| **Falsa sensación de seguridad** | "¡Está polimerizado!" — pero ¿está bien polimerizado? |
| **Resistencia del equipo** | El nuevo asistente no sabe usar la lámpara |
| **Costo oculto** | Mantenimiento, repuestos, calibración |
| **No reemplaza al profesional** | El autoclave no detecta si el instrumental está limpio |

> 📌 **Las herramientas asisten, no reemplazan.** Sale en el examen.

---

## 🎯 Criterios para adoptar (LO 6.3.1)

1. **¿Realmente la necesitás?** No compres un escáner intraoral si atendés 3 pacientes por día.
2. **¿Tu equipo la puede usar?** La mejor herramienta es la que se usa.
3. **¿Costo vs ahorro?** ROI real.
4. **¿Se integra con lo que ya tenés?**
5. **¿Soporte local?**
6. **¿Podés migrar después?**

---

## 🧪 Test Automation — Riesgos y beneficios (LO 6.1.2)

### Beneficios

- Más tests en menos tiempo (escala)
- Consistencia (se ejecuta igual siempre)
- Ahorro de tiempo a largo plazo
- Feedback rápido

### Riesgos

- **Falsa sensación de cobertura** (tests pasan ≠ software bueno)
- Costo inicial alto (escribir los tests)
- Mantenimiento de los tests (cambian con el código)
- No encuentra bugs que requieren juicio humano
- Expectativas infladas ("100% automatizado" es mentira)

---

## 🤝 DevOps / CI/CD

**CI/CD = Continuous Integration / Continuous Delivery**

**Idea:** cada vez que alguien cambia el código, se ejecutan tests automáticamente. Si fallan, no se publica.

**Dental:** tu autoclave valida que llegó a temperatura antes de seguir. Si no, no avanza. Mismo principio.

---

## 📊 Métricas de herramientas (LO 6.4.1)

- Cobertura de código cubierta por automation
- Falsos positivos / falsos negativos de las herramientas
- Tiempo ahorrado vs tiempo invertido en automatización

---

## 🎯 Resumen ultra-rápido

- 8 categorías de herramientas (memorizar)
- 6 pasos para adopción (Assessment → PoC → Selection → Pilot → Rollout → Review)
- Las herramientas **asisten, no reemplazan**
- Falsa sensación de cobertura = riesgo #1

---

*Cap 6 listo. Memorizá las 8 categorías.*
