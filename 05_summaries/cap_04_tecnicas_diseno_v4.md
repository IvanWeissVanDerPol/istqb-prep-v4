# Resumen Cap 4 (v4.0.1) — Test Analysis and Design 🔴 EL MÁS PESADO

> **390 minutos oficiales** (~34% del syllabus). Estudia esto 2x más que cualquier otro capítulo.

---

## 1. Overview (4.1)

**3 familias de técnicas:**

| Familia | Punto de vista | Usado en |
|---|---|---|
| **Black-box** (4.2) | Especificaciones/requisitos | Cualquier nivel, especialmente system/acceptance |
| **White-box** (4.3) | Estructura interna del código | Component/integration |
| **Experience-based** (4.4) | Intuición + experiencia | Exploratory |
| **🆕 Collaboration-based (4.5)** | Trabajo en equipo | Acceptance/ATDD |

---

## 2. Black-box Techniques (4.2) ⭐⭐⭐

### 2.1 Equivalence Partitioning (EP) — K3 ⭐⭐⭐

**Concepto:**
- Dividir el dominio de entrada en **grupos** de valores que deben comportarse igual
- Testear **un valor por partición** es suficiente
- Reducís tests infinitos a unos pocos bien elegidos

**Particiones:**
- **Válidas** — inputs aceptados
- **Inválidas** — inputs rechazados

**Reglas:**
- Cada partición inválida se testea **en isolation** (v4.0.1 nueva aclaración, para evitar **defect masking**)

**Ejemplo:**
> Edad para votar: 18-65 válido, <18 inválido, >65 válido
> - Partición 1 (inválida): -5 → probar -5
> - Partición 2 (válida): 18-65 → probar 30
> - Partición 3 (válida): >65 → probar 70
> 
> Resultado: 3 tests

### 2.2 Boundary Value Analysis (BVA) — K3 ⭐⭐⭐

**Concepto:**
- Tests en los **bordes** de las particiones (límites)
- Los defectos cluster en los bordes (v3.1: "defects cluster together" — principio)

**Variantes:**
- **2-value:** min, max (los límites y uno antes/después)
- **3-value:** min-1, min, max, max+1 (los clásicos)

**Ejemplo edad 18-65:**
- 17 (justo abajo del límite inferior — inválido)
- 18 (límite inferior — válido)
- 65 (límite superior — válido)
- 66 (justo arriba del límite superior — inválido)
- 
> Resultado: 4 tests (vs 3 con EP solo)

**EP + BVA combinados** = cobertura sólida con pocos tests.

### 2.3 Decision Table Testing — K3 ⭐⭐

**Cuándo:**
- Lógica con combinaciones de inputs que llevan a distintas acciones
- Las combinaciones causan distinta salida

**Estructura:**
- **Condiciones** (entradas) en filas
- **Acciones** (salidas) en filas
- **Reglas:** combinaciones específicas de condiciones que llevan a acciones

**Ejemplo: Login**
| Regla | User válido | Password válido | → Acción |
|---|---|---|---|
| R1 | sí | sí | → login OK |
| R2 | sí | no | → retry |
| R3 | no | sí | → retry |
| R4 | no | no | → retry |

> 4 reglas = 4 tests

### 2.4 State Transition Testing — K3 ⭐⭐

**Cuándo:**
- Sistemas con **estados** discretos
- Transiciones disparadas por **eventos**
- Validar **estados ejercidos** (no "visitados" — cambio v4.0.1)

**Estados típicos:**
- Idle → Processing → Success / Failure

**Tests derivados:**
- Valid transitions (cada transición válida)
- Invalid transitions (disparar evento cuando no aplica)

**Cobertura:**
- **0-switch:** todas las transiciones
- **1-switch:** todas las parejas de transiciones seguidas
- (mejor cobertura = más tests)

---

## 3. White-box Techniques (4.3) ⭐

### 3.1 Statement Testing (4.3.1)

- ¿Qué porcentaje de **statements** (líneas) del código se ejecutan?
- 100% statement coverage ≠ sin bugs (no detecta ramas faltantes)

### 3.2 Branch Testing (4.3.2) ⭐ — MÁS USADO

- ¿Qué porcentaje de **branches** (decisiones) se ejecutaron **en ambos sentidos**?
- Branch coverage >= Statement coverage

**Ejemplo:**
```python
if edad > 18:   # branch 1
    print("Mayor")   # statement cubierto por True
# False branch nunca tocado
```

100% statement coverage (la línea del if) = 50% branch coverage.

### 3.3 Value (4.3.3)

White-box testing:
- Encuentra código muerto, código no testeado
- Útil en **componentes críticos** (security, payments)
- Encuentra bugs que black-box no encuentra

---

## 4. Experience-based Techniques (4.4)

### 4.1 Error Guessing (4.4.1)
- Tester **adivina** dónde podría haber bugs basándose en experiencia
- Úsalo combinado con técnicas formales

### 4.2 Exploratory Testing (4.4.2) ⭐
- **Learning, test design, execution** en paralelo
- **Session-based:** con **charter** (objetivo) + **timebox** (tiempo límite) + **session notes** (qué se hizo)
- Útil cuando no hay specs claras

### 4.3 Checklist-based Testing (4.4.3)
- Listas de verificación predefinidas
- Combina estructura con experiencia

---

## 5. 🆕 Collaboration-based Approaches (4.5) — NUEVO EN v4.0

### 5.1 User Stories (4.5.1) ⭐ NUEVO

**Formato típico:**
> "Como [rol], quiero [acción], para [beneficio]"

**3 C's de una user story:**
- **Card** — la historia escrita
- **Conversation** — discusiones con el equipo
- **Confirmation** — criterios de aceptación

### 5.2 Acceptance Criteria (4.5.2) ⭐ NUEVO

**Opciones para escribir:**
- **Formato Given-When-Then** (BDD-style):
  > Given [precondición]
  > When [acción]
  > Then [resultado esperado]
- **Formato checklist** — bullets
- **Formato Scenario-based**

### 5.3 ATDD (4.5.3) ⭐⭐ NUEVO

**Acceptance Test-Driven Development:**
1. Equipo (dev + tester + business) escribe acceptance tests **ANTES** del código
2. Tests fallan al inicio (sistema no existe)
3. Implementan código hasta que pasen
4. Igual que TDD pero a nivel de acceptance (no unitario)

**Diferencia TDD vs ATDD:**
| | TDD | ATDD |
|---|---|---|
| Quién lo escribe | Developer | Equipo (3 personas) |
| Granularidad | Unitario | Acceptance/E2E |
| Sirve para | Diseño interno | Validación requisitos |

---

## 🎯 Preguntas típicas del Cap 4

1. **BVA enfoca tests en...** → boundaries entre particiones
2. **EP es útil cuando...** → muchas combinaciones de inputs
3. **100% statement coverage garantiza...** → ? (no garantiza bugs-free)
4. **State diagram reemplaza a...** → state transition diagram
5. **Exploratory testing NO es...** → testing sin tiempo límite
6. **ATDD es test-first a nivel de...** → acceptance
7. **User story "Como... quiero... para..."** es formato [INVEST] con [3 C's]

---

## 📝 Mnemotécnicos

- **EP:** "una partición = un test"
- **BVA:** "los bugs viven en los bordes"
- **Decision Table:** "AND/OR"
- **State:** "estados + eventos + transiciones"
- **Statement vs Branch:** "líneas vs decisiones"
- **ATDD:** "acceptance level + TDD style"
