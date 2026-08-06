# Quiz Cap 2 (v4.0.1) — Testing Throughout SDLC

> **15 preguntas** — meta: **≥80% (12/15)**
> Tiempo: 18 min

---

**Q1. (LO 2.2.1) ¿Cuál NO es un nivel de testing?**

A) Component testing.
B) Integration testing.
C) Functional testing.
D) Acceptance testing.

<details><summary>✅</summary>C. Functional es un **tipo**, no nivel.</details>

**Q2. (LO 2.2.2) ¿Cuál NO es una característica de calidad ISO 25010:2023?**

A) Performance efficiency.
B) Maintainability.
C) Productivity.
D) Flexibility.

<details><summary>✅</summary>C. Las 8 (+safety) son: Functional, Performance efficiency, Compatibility, Interaction capability, Reliability, Security, Maintainability, Flexibility, Safety.</details>

**Q3. (LO 2.2.3) Confirmation testing verifica:**

A) Que el código cumple requisitos.
B) Que un defecto específico está fixed.
C) Que no se rompió nada.
D) Que el sistema corre rápido.

<details><summary>✅</summary>B. Confirmation = re-test de UN defecto. Regression = nada se rompió.</details>

**Q4. (LO 2.1.5) "Shift-left" significa:**

A) Mover testing a la izquierda del cronograma / más temprano en el SDLC.
B) Mover testing al final.
C) Mover al hemisferio.
D) Eliminar testing.

<details><summary>✅</summary>A. Shift-left = testing temprano. Tests definidos antes del código.</details>

**Q5. (LO 2.1.4) ¿Cuál es el impacto típico de DevOps en testing?**

A) Testing más lento.
B) Testing continuo integrado en CI/CD pipeline.
C) Eliminar tests.
D) Solo manual.

<details><summary>✅</summary>B. DevOps impacta testing en CI/CD continuo, monitoreo en producción, feedback loop rápido.</details>

**Q6. (LO 2.2.1) Integration testing es típicamente ejecutado por:**

A) Solo el usuario.
B) Solo el PO.
C) Developers o testers.
D) Solo QA manual.

<details><summary>✅</summary>C. Mientras component testing es developer, integration puede ser dev o tester.</details>

**Q7. (LO 2.2.2) ¿Cuál describe mejor "non-functional testing"?**

A) Tests que solo aplican al inicio.
B) Tests sobre cómo de bien el sistema hace las cosas (performance, security, etc).
C) Tests que son opcionales.
D) Tests no requeridos por ISTQB.

<details><summary>✅</summary>B. Non-func = cómo (performance, security, usability, compatibility, etc).</details>

**Q8. (LO 2.1.3) ¿Cuál NO es test-first approach?**

A) TDD.
B) ATDD.
C) BDD.
D) Maintenance testing.

<details><summary>✅</summary>D. Maintenance testing es post-deployment. TDD/ATDD/BDD son test-first.</details>

**Q9. (LO 2.1.6) ¿Para qué sirven las "retrospectives" en agile testing?**

A) Castigar devs.
B) Mecanismo para identificar mejoras continuas al proceso de testing.
C) Eliminar planning.
D) Definir presupuesto.

<details><summary>✅</summary>B. Retrospectives = mejora continua al final de iteraciones.</details>

**Q10. (LO 2.2.1) Maintenance testing se activa por:**

A) Migration, retirement, nuevos environments.
B) Lunch.
C) Final sprint.
D) Demo.

<details><summary>✅</summary>A. Maintenance triggers: migration, retirement, nuevos envs, post-deployment fixes.</details>

**Q11. (LO 2.2.2) "Interaction capability" (ISO 25010:2023) reemplazó a:**

A) Portability.
B) Usability.
C) Flexibility.
D) Compatibility.

<details><summary>✅</summary>B. Cambio v4.0: usability → interaction capability. (Mismo concepto, nuevo nombre oficial.)</details>

**Q12. (LO 2.2.3) Regression testing se ejecuta:**

A) Antes del fix.
B) Después del fix para verificar que todo sigue funcionando.
C) Solo en maintenance.
D) Solo cuando hay memory leak.

<details><summary>✅</summary>B. Regression = suite completa post-cambio para verificar nada se rompió.</details>

**Q13. (LO 2.2.1) Acceptance testing típicamente es ejecutado por:**

A) Solo developer.
B) Usuario / cliente / sponsor.
C) Solo PM.
D) Nadie.

<details><summary>✅</summary>B. Acceptance es validación del usuario/cliente final.</details>

**Q14. (LO 2.2.2) "Safety" como característica de calidad (NUEVO ISO 25010:2023) significa:**

A) Operar sin causar daño a personas/datos.
B) Login seguro.
C) Password complejo.
D) Backup frecuente.

<details><summary>✅</summary>A. Safety = ausencia de daño. ISO 25010:2023 renombró/expandió las 8 categorías.</details>

**Q15. (LO 2.1.5) ¿Cuáles son los BENEFICIOS de shift-left?**

A) Mismo esfuerzo, mismo costo.
B) Detectar defectos más temprano = menos costo de fix, mejor feedback, menos retrabajo.
C) Solo ahorra tiempo después.
D) Menos defectos al final es un mito.

<details><summary>✅</summary>B. Shift-left es uno de los principios: early testing saves money.</details>

---

## 📊 Scoring

- **13-15 correctas:** Dominás Cap 2
- **11-12 correctas:** Pasás, refrescá puntos débiles
- **<10:** Repasá el summary del cap
