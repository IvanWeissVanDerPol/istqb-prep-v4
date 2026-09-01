# 📋 Quiz Diagnóstico Inicial — Antes de empezar a estudiar

> **15 preguntas para saber tu baseline. Tomate 20 minutos, sin mirar nada.**
>
> Repetilo después de estudiar — debería haber mejorado al menos 5 puntos.

---

## Instrucciones

- Sin mirar apuntes
- 20 minutos máximo
- Anotá tu puntaje y comparalo con el del [`../00_antes_de_empezar/AUTODIAGNOSTICO.md`](../00_antes_de_empezar/AUTODIAGNOSTICO.md) (que es el mismo test pero en formato más narrativo)

---

## Preguntas

### Q1. (K1, LO 1.1.1) ¿Cuál es un objetivo típico del testing?

A) Eliminar todos los defectos
B) Detectar defectos y reducir riesgo
C) Reemplazar al desarrollador
D) Garantizar cero errores en producción

### Q2. (K1, LO 1.2.3) ¿Cuál es el orden correcto de la cadena causal?

A) Failure → defect → error
B) Error → defect → failure
C) Defect → error → failure
D) Error → failure → defect

### Q3. (K2, LO 1.3.1) ¿Cuál de los siguientes NO es uno de los 7 principios del testing?

A) Testing shows the presence of defects, not their absence
B) Exhaustive testing is impossible
C) Defects are evenly distributed across the system
D) Early testing saves time and money

### Q4. (K2, LO 1.4.2) La diferencia entre verification y validation es:

A) Verification es manual; validation es automático
B) Verification = ¿lo hicimos bien?; Validation = ¿es lo correcto para el usuario?
C) Verification = unit tests; Validation = integration tests
D) Son sinónimos

### Q5. (K2, LO 2.2.1) ¿Cuál de los siguientes NO es un nivel de testing?

A) Component testing
B) Integration testing
C) Functional testing
D) Acceptance testing

### Q6. (K2, LO 2.2.3) Regression testing verifica que:

A) El defecto reportado fue arreglado
B) Lo que antes andaba, sigue andando después de un cambio
C) El sistema cumple con los requisitos
D) El sistema es rápido

### Q7. (K2, LO 3.1.1) ¿Cuál es la diferencia principal entre static y dynamic testing?

A) Static es manual; dynamic es automático
B) Static testing no ejecuta el software; dynamic sí
C) Static es para devs; dynamic es para testers
D) No hay diferencia

### Q8. (K2, LO 3.3.2) Un ateneo clínico donde un residente presenta un caso es un ejemplo de:

A) Informal review
B) Walkthrough
C) Technical review
D) Inspection

### Q9. (K3, LO 4.2.1) Una regla dice "los mayores de 65 años reciben 20% de descuento". ¿Cuántas particiones de equivalencia?

A) 1
B) 2
C) 3
D) 5

### Q10. (K3, LO 4.2.2) Para esa misma regla, ¿qué valores testarías con BVA?

A) 25, 45, 65, 85
B) 64, 65, 66
C) 1, 50, 100
D) 65 solamente

### Q11. (K3, LO 4.3.3) Si una decisión depende de 3 condiciones booleanas, ¿cuántas combinaciones posibles hay?

A) 3
B) 6
C) 8
D) 9

### Q12. (K2, LO 5.3.1) Risk-based testing significa:

A) Testear todo por igual
B) Priorizar testing por probabilidad × impacto
C) Testear solo lo que parece peligroso
D) Testear después de que se cae el sistema

### Q13. (K2, LO 5.3.3) La diferencia entre severidad y prioridad de un defecto es:

A) Son sinónimos
B) Severidad = impacto técnico; Prioridad = urgencia de resolución
C) Severidad = para devs; Prioridad = para users
D) Severidad = bugs; Prioridad = fallas

### Q14. (K2, LO 6.1.1) ¿Cuántas categorías de herramientas reconoce ISTQB?

A) 3
B) 5
C) 8
D) 12

### Q15. (K2, LO 6.3.1) El primer paso para adoptar una herramienta es:

A) Comprarla
B) Assessment (evaluar si realmente la necesitás)
C) Capacitar al equipo
D) Hacer rollout

---

## 📊 Respuestas

<details>
<summary><b>Click para ver respuestas</b></summary>

| Q | Respuesta | LO | Por qué |
|---|---|---|---|
| 1 | **B)** | LO 1.1.1 | "Detectar defects y reducir riesgo" es uno de los objetivos típicos |
| 2 | **B)** | LO 1.2.3 | Error → defect → failure |
| 3 | **C)** | LO 1.3.1 | "Defects evenly distributed" es FALSO; ISTQB dice "Defects cluster together" |
| 4 | **B)** | LO 1.4.2 | V&V: construcción correcta vs producto correcto |
| 5 | **C)** | LO 2.2.1 | Functional testing es un TIPO, no un nivel |
| 6 | **B)** | LO 2.2.3 | Regression = "lo que andaba, sigue andando" |
| 7 | **B)** | LO 3.1.1 | Static NO ejecuta, Dynamic sí |
| 8 | **B)** | LO 3.3.2 | Walkthrough = autor presenta, grupo pregunta |
| 9 | **B)** | LO 4.2.1 | 2 particiones: <65, ≥65 |
| 10 | **B)** | LO 4.2.2 | BVA testea los bordes |
| 11 | **C)** | LO 4.3.3 | 2³ = 8 |
| 12 | **B)** | LO 5.3.1 | Riesgo = probabilidad × impacto |
| 13 | **B)** | LO 5.3.3 | Impacto técnico vs urgencia |
| 14 | **C)** | LO 6.1.1 | 8 categorías |
| 15 | **B)** | LO 6.3.1 | Assessment primero |

</details>

---

## 📊 Tu puntaje

**Puntaje: ____ / 15**

**Diagnóstico:**
- **13-15:** Ya sabés bastante ISTQB. Vas a estudiar rápido.
- **10-12:** Buena base. Te faltan los formalismos.
- **6-9:** Conceptos generales pero no específicos.
- **0-5:** Arrancás de cero pero con experiencia clínica a tu favor.

**Anotá acá:**
```
Diagnóstico inicial: ____ / 15
Fecha: ___________
Capítulo donde más me cuesta: _______________
```

Después de estudiar los 6 capítulos, repetí este test. Deberías haber mejorado al menos 5 puntos.
