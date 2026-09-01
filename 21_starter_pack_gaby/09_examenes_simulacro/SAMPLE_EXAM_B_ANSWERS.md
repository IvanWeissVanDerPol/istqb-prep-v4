# Respuestas Sample Exam B

> Respuestas con referencia al LO + explicación corta.

---

## SECCIÓN 1 — Fundamentos del Testing

### Q1. ✅ **B)** LO 1.2.1 — El software está en sistemas críticos (médicos, financieros, de transporte). Los defects pueden causar daño real.

### Q2. ✅ **B)** LO 1.2.2 — QA = procesos (proactivo). Testing = producto (reactivo).

### Q3. ✅ **A)** LO 1.1.2 — Testing encuentra. Debugging corrige.

### Q4. ✅ **B)** LO 1.3.1 — "Defects cluster together" es el Principio 4.

### Q5. ✅ **B)** LO 1.4.2 — Validation falla cuando el producto no satisface al usuario. La oclusión molesta = no usable.

### Q6. ✅ **B)** LO 1.4.1 — Planning → Analysis → Design → Implementation → Execution → Completion.

### Q7. ✅ **B)** LO 1.5.1 — Sesgo de confirmación: buscar confirmar lo que ya crees, no buscar problemas.

### Q8. ✅ **B)** LO 1.5.3 — Independencia reduce el sesgo de confirmación.

---

## SECCIÓN 2 — Ciclo de Vida

### Q9. ✅ **B)** LO 2.1.2 — Modelo V = cada fase de dev tiene su fase de testing对应的对应.

### Q10. ✅ **C)** LO 2.1.2 — Incremental = entregas parciales funcionales (cada fase es un incremento).

### Q11. ✅ **D)** LO 2.2.1 — Component → Integration → System → Acceptance (de menor a mayor).

### Q12. ✅ **B)** LO 2.2.3 — Regression = "lo que andaba, sigue andando".

### Q13. ✅ **C)** LO 2.4.1 — Maintenance testing = cambios en el entorno (Chrome update).

### Q14. ✅ **B)** LO 2.3.1 — Smoke testing = ¿las funciones básicas funcionan?

---

## SECCIÓN 3 — Pruebas Estáticas

### Q15. ✅ **B)** LO 3.1.1 — Static testing = revisar sin ejecutar.

### Q16. ✅ **D)** LO 3.2.1 — Datos en tiempo de ejecución requieren ejecución (dynamic). Los otros tres son documentos que se pueden revisar estáticamente.

### Q17. ✅ **D)** LO 3.3.2 — Inspection = checklist + roles + proceso + métricas.

### Q18. ✅ **A)** LO 3.3.2 — Informal review = sin proceso formal.

---

## SECCIÓN 4 — Técnicas de Diseño ⭐

### Q19. ✅ **C)** LO 4.1.2 — Statement coverage es white-box (mirando código). Las otras son black-box.

### Q20. ✅ **B)** LO 4.2.1 — 3 particiones: baja, normal, alta. Las tres tienen comportamiento distinto respecto a la alerta.

### Q21. ✅ **A)** LO 4.2.2 — 17, 18, 19 (borde inferior), 64, 65, 66 (borde superior). BVA testea -1, 0, +1 alrededor de cada borde.

### Q22. ✅ **C)** LO 4.3.3 — 3 condiciones booleanas = 2³ = 8 combinaciones.

### Q23. ✅ **D)** LO 4.3.1 — 150 está fuera del rango 0-120, es una partición inválida.

### Q24. ✅ **C)** LO 4.4.1 — Cerrada → Firmada es una transición inversa inválida.

### Q25. ✅ **C)** LO 4.5.1 — Error guessing se basa en la experiencia del tester.

### Q26. ✅ **B)** LO 4.5.2 — Sin docs + poco tiempo = exploratory testing.

### Q27. ✅ **C)** LO 4.5.3 — Checklist pre-quirúrgico = checklist-based testing.

### Q28. ✅ **D)** LO 4.5.4 — Transiciones de workflow = State Transition Testing.

### Q29. ✅ **A)** LO 4.2.2 — 0 (sin intentos), 1 (intento 1), 2 (intento 2), 3 (borde exacto, debe permitir), 4 (debe bloquear), 5 (más allá).

### Q30. ✅ **B)** LO 4.3.3 — Mínimo 2 condiciones para que sea útil (1 sola condición es trivial).

---

## SECCIÓN 5 — Gestión de Testing

### Q31. ✅ **B)** LO 5.1.2 — Criterios de salida = cuándo dejar de testear.

### Q32. ✅ **B)** LO 5.3.1 — Alta probabilidad + bajo impacto = riesgo medio (5×1=5, matriz MA/A/M/M/B/MB según escala).

### Q33. ✅ **B)** LO 5.3.3 — Ciclo: Nuevo → Asignado → En progreso → Resuelto → Cerrado.

### Q34. ✅ **B)** LO 5.2.2 — Tiempo medio de resolución = métrica de proceso.

### Q35. ✅ **D)** LO 5.3.2 — Los usuarios no se versionan. Todo lo demás sí.

### Q36. ✅ **B)** LO 5.3.5 — El testing da información sobre calidad y riesgo, ayudando a tomar decisiones informadas.

---

## SECCIÓN 6 — Herramientas

### Q37. ✅ **B)** LO 6.1.1 — Jira es bug tracking. Selenium = automation, SonarQube = static analysis, Jenkins = CI/CD.

### Q38. ✅ **C)** LO 6.1.1 — Jenkins, GitHub Actions, GitLab CI = CI/CD / DevOps.

### Q39. ✅ **B)** LO 6.3.1 — Assessment → PoC → Selection → Pilot → Rollout → Review.

### Q40. ✅ **A)** LO 6.1.2 — Falsa sensación de cobertura es el riesgo principal de la automatización.

---

## 📊 Tu diagnóstico

| Puntaje | Significado | Acción |
|---|---|---|
| **32-40 (80%+)** | Excelente. | Listo para rendir. |
| **26-31 (65-79%)** | Bien. | Repasá errores puntuales. |
| **20-25 (50-64%)** | Cerca pero no. | Releé capítulos donde fallaste. |
| **< 20 (< 50%)** | Necesitás más estudio. | Volvé a los capítulos. |

**Comparación entre Examen A y B:**
- Si sacás similar puntaje en ambos → consistente
- Si sacás mucho mejor en uno → tema suerte, hacé un tercer examen (Sample C)
- Si sacás mucho peor en uno → estrés, practicá la técnica de examen cronometrado

---

## 🎯 Próximos pasos

1. Si sacás 65%+ en A y B → hacé el Sample C como práctica final.
2. Si sacás < 65% → releé los capítulos débiles y repetí los quizzes antes del Sample C.
3. Cuando estés lista para el examen real → mirá el [`../11_checklist_pre_examen/CHECKLIST_FINAL.md`](../11_checklist_pre_examen/CHECKLIST_FINAL.md).
