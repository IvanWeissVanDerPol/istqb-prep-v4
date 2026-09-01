# 📋 Cheatsheet Cap 4 — Técnicas de Diseño ⭐ (1 página)

> *Imprimible. **El cap más importante del examen** (~30% del peso). Pegar en un lugar visible.*

---

## 🎯 ISTQB en 1 frase

> Las técnicas de diseño de tests son **métodos sistemáticos** para elegir qué tests son más valiosos. Hay técnicas **black-box** (sin ver código), **white-box** (viendo código), y **basadas en experiencia**.

---

## 🗂️ Las 6 técnicas principales ⭐⭐

```
BLACK-BOX (sin ver código):
├─ 1. Equivalence Partitioning (EP) ⭐
├─ 2. Boundary Value Analysis (BVA) ⭐
├─ 3. Decision Table Testing ⭐
├─ 4. State Transition Testing ⭐

EXPERIENCE-BASED:
├─ 5. Error Guessing
├─ 6. Exploratory Testing
└─ 7. Checklist-based Testing

WHITE-BOX (viendo código — poco en CTFL):
└─ Coverage testing (statement, branch)
```

---

## 1️⃣ EQUIVALENCE PARTITIONING (EP) ⭐⭐ (LO 4.2.1, 4.3.1)

**Idea:** agrupar inputs en **particiones** con comportamiento equivalente. Testear **un valor por partición**.

**Regla:** "mayores de 65 reciben descuento" → 2 particiones:
- < 65 años (sin descuento)
- ≥ 65 años (con descuento)

**Dental:** agrupar pacientes por rango etario (niños / adultos / mayores).

**Inválidos también:** edades negativas, edad 200 → particiones inválidas separadas.

---

## 2️⃣ BOUNDARY VALUE ANALYSIS (BVA) ⭐⭐ (LO 4.2.2, 4.3.2)

**Idea:** los defectos están **en los bordes**. Testear los valores límite: adentro, afuera, y justo en el borde.

**Regla:** "acepta edad entre 0 y 120" → testar:
- **-1** (afuera, debe rechazar)
- **0** (borde exacto, debe aceptar)
- **1** (adentro, debe aceptar)
- **119** (adentro, debe aceptar)
- **120** (borde exacto, debe aceptar)
- **121** (afuera, debe rechazar)

**Dental:** testear el paciente de **65 años exacto** (borde), no los de 25 y 80.

> 📌 **EP y BVA se usan juntos.** EP elige las particiones, BVA elige los valores específicos.

---

## 3️⃣ DECISION TABLE ⭐⭐ (LO 4.3.3)

**Idea:** cuando hay **múltiples condiciones combinadas**, hacer una tabla con todas las combinaciones.

**Ejemplo dental:** antibiótico si (infección + no alergia + en presupuesto):

| Infección | Alergia | Presupuesto | Antibiótico |
|---|---|---|---|
| NO | NO | NO | NO |
| SÍ | NO | NO | NO |
| NO | SÍ | NO | NO |
| SÍ | SÍ | NO | NO |
| NO | NO | SÍ | NO |
| SÍ | NO | SÍ | **SÍ** |
| NO | SÍ | SÍ | NO |
| SÍ | SÍ | SÍ | NO |

Solo el caso "todo SÍ" da antibiótico. Testear los casos representativos (no siempre los 8).

---

## 4️⃣ STATE TRANSITION ⭐⭐ (LO 4.4.1, 4.4.2)

**Idea:** sistema tiene **estados**. Testear las **transiciones** entre estados.

**Ejemplo dental:** historia clínica del presupuesto:
```
[Borrador] → [Enviado] → [Aprobado] → [Activo] → [Cerrado]
```

**Testear:**
- Transiciones válidas (Borrador → Enviado ✓)
- **Transiciones inválidas** (Aprobado → Borrador ✗) ← defectos potenciales

---

## 5️⃣ ERROR GUESSING (LO 4.5.1)

**Idea:** el tester **adivina** dónde están los defectos, basado en experiencia.

**Dental:** "los pacientes siempre mienten sobre el cepillado" → testear inconsistencias.

---

## 6️⃣ EXPLORATORY TESTING (LO 4.5.2)

**Idea:** diseñar y ejecutar tests **al mismo tiempo**, sin documentación previa.

**Cuándo:** poco tiempo, sistema nuevo, tester con experiencia.

---

## 7️⃣ CHECKLIST-BASED (LO 4.5.3)

**Idea:** una lista de cosas para verificar.

**Dental:** checklist pre-quirúrgico de la OMS.

---

## 📊 Cuándo usar cada técnica (LO 4.5.4)

| Situación | Técnica |
|---|---|
| Rangos numéricos | EP + BVA |
| Combinaciones de condiciones | Decision table |
| Estados del sistema | State transition |
| Sin documentación, poco tiempo | Exploratory |
| Tester con experiencia | Error guessing |
| Industria regulada | Checklist-based |

---

## 🎯 Resumen ultra-rápido (para repaso 1 min)

- **EP** = grupos equivalentes (testear 1 por grupo)
- **BVA** = bordes (-1, 0, 1, ..., n-1, n, n+1)
- **Decision Table** = combinaciones de condiciones
- **State Transition** = cambio de estados, válidas e inválidas
- **Error Guessing** = intuición del tester
- **Exploratory** = aprender mientras testeás
- **Checklist** = lista predefinida

---

*Cap 4 listo. Si no dominás EP, BVA, Decision Table y State Transition, NO rindas el examen.*
