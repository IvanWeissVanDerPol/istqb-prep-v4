# Cap 6 — Soporte de Herramientas (versión clínica)

> **Versión ISTQB CTFL v4.0.1 — Sección 6.** Cubre LOs **6.1.1, 6.1.2, 6.2.1, 6.2.2, 6.2.3, 6.2.4, 6.3.1, 6.4.1** (8 de 8 LOs del capítulo).
>
> Equivalente a [`../../05_summaries/cap_06_herramientas_v4.md`](../../05_summaries/cap_06_herramientas_v4.md) del repo principal.
>
> Tiempo de lectura: ~25 minutos.
>
> **Para repaso rápido:** [`CHEATSHEET_CAP6.md`](CHEATSHEET_CAP6.md) (1 página).

---

## 1. ¿Por qué herramientas? (6.1)

ISTQB agrupa las herramientas de testing en categorías. En la clínica ya conocés esto: las herramientas reemplazan trabajo manual repetitivo, dan consistencia, y permiten escalar.

### En la clínica

| Herramienta clínica | Reemplaza | Beneficio |
|---|---|---|
| Eyector de saliva | Hisopo manual | Consistencia, velocidad |
| Amalgamador | Mezcla manual | Uniformidad, tiempo exacto |
| Lámpara de polimerización | Espera natural | Control del tiempo |
| Software de historia clínica | Ficha en papel | Buscabilidad, backup, auditoría |
| Autoclave | Hervido en agua | Estandarización, registros |

Misma idea en software: las herramientas hacen lo mismo pero para testing.

---

## 2. Categorías de herramientas (6.2) ⭐ PREGUNTADO

ISTQB lista estas categorías:

### 1. Test Management Tools

**Qué:** gestionar el proceso de testing (planes, casos, ejecución, métricas).

**En la clínica:** tu agenda + sistema de gestión clínica.

**Ejemplos software:** TestRail, Zephyr, qTest, PractiTest.

### 2. Bug Tracking / Defect Management

**Qué:** registrar, asignar, seguir defectos hasta su resolución.

**En la clínica:** la epicrisis + sistema de seguimiento de complicaciones.

**Ejemplos software:** Jira, Bugzilla, Mantis, GitHub Issues, Linear.

### 3. Test Data Preparation

**Qué:** preparar los datos necesarios para los tests (datos de pacientes, historiales mock).

**En la clínica:** los modelos, radiografías de prueba, dientes extraídos.

**Importante:** NO usar datos reales de pacientes en testing (privacidad).

### 4. Test Execution / Automation

**Qué:** ejecutar tests automáticamente.

**En la clínica:** ¿qué automatizás? El autoclave. El autoclave ejecuta un ciclo de esterilización automáticamente. Test execution tool.

**Ejemplos software:** Selenium, Cypress, Playwright (para aplicaciones web).

### 5. Static Analysis

**Qué:** analizar código sin ejecutarlo, encontrar problemas potenciales.

**En la clínica:** la revisión de la radiografía antes de tratarla.

**Ejemplos software:** SonarQube, ESLint, Pylint.

### 6. Performance Testing

**Qué:** medir performance (velocidad, carga).

**En la clínica:** cuánto tarda en cargarse la historia clínica de un paciente con 12 años de fichas.

**Ejemplos software:** JMeter, Gatling, k6, LoadRunner.

### 7. Test Design

**Qué:** ayudar a diseñar tests (generar particiones, BVA, etc.).

**En la clínica:** las plantillas de protocolos.

**Ejemplos software:** herramientas de modelado, generación automática de casos.

### 8. DevOps / CI/CD

**Qué:** integración continua, entrega continua. Cada cambio al código se testea automáticamente.

**En la clínica:** la autoclave valida automáticamente que llegó a la temperatura correcta. Si no, no deja avanzar.

**Ejemplos software:** Jenkins, GitHub Actions, GitLab CI, CircleCI.

---

## 3. Criterios para adoptar una herramienta (6.3) ⭐ PREGUNTADO

ISTQB dice que antes de comprar/adoptar una herramienta, evaluá:

### Para vos (clínica):

1. **¿Realmente la necesitás?** No compres un escáner intraoral si atendés 3 pacientes por día.
2. **¿Tu equipo la puede usar?** La mejor herramienta es la que tu equipo efectivamente usa.
3. **¿Cuánto cuesta vs cuánto ahorra?** ROI real, no ROI teórico.
4. **¿Se integra con lo que ya tenés?** Un RVG que no se integra con tu software de historia es un dolor.
5. **¿El vendor tiene soporte local?** Si se rompe, ¿quién te lo arregla?
6. **¿Podés migrar después?** No te cases con un solo vendor.

### ISTQB dice lo mismo para herramientas de testing:

1. **Assessment:** ¿qué problemas resuelve?
2. **Proof of concept:** probala en un proyecto pequeño antes de comprometerte.
3. **Tool selection:** elegí entre las opciones.
4. **Pilot:** probá en real.
5. **Rollout:** expansión gradual.
6. **Review:** ¿estuvo a la altura? ¿seguimos o cambiamos?

> 📌 En el examen: preguntas sobre los criterios de adopción. Memorizar los 6 puntos.

---

## 4. Riesgos de las herramientas (6.4)

ISTQB advierte que las herramientas también tienen problemas:

### En la clínica

| Riesgo de la herramienta dental | Riesgo equivalente en herramienta de testing |
|---|---|
| Dependencia del vendor ("si se rompe el autoclave, ¿quién me lo arregla?") | Vendor lock-in |
| Falsa sensación de seguridad ("¡está polimerizado!" — pero ¿está bien polimerizado?) | Falsa sensación de cobertura |
| Curva de aprendizaje ("el nuevo asistente no sabe usar la lámpara") | Resistencia del equipo |
| Costo oculto (mantenimiento, repuestos, calibración) | Costo de licencias + mantenimiento |
| No reemplaza al profesional ("el autoclave no detecta si el instrumental está limpio") | No reemplaza al tester humano |

> 📌 **Regla de oro:** las herramientas asisten al tester, no lo reemplazan. Lo mismo en clínica: la herramienta asiste al profesional.

---

## 5. Resumen del Cap 6

✅ Hay 8 categorías de herramientas de testing.
✅ Antes de adoptar una herramienta: assessment → PoC → selección → pilot → rollout → review.
✅ Las herramientas asisten, no reemplazan.
✅ Siempre considerar: costo real, soporte local, capacidad del equipo, integración.
✅ Cuidado con la falsa sensación de cobertura: pasar tests ≠ software de calidad.

---

## Para chequear que entendiste

1. Nombrá las 8 categorías de herramientas de testing y un ejemplo de cada una (real o análogo dental).
2. ¿Por qué una herramienta puede dar falsa sensación de cobertura? Doy un ejemplo dental.
3. ¿Cuáles son los 6 pasos para adoptar una herramienta?

Hacé el [`QUIZ_CAP6.md`](../08_quizzes_dentales/QUIZ_CAP6.md).
