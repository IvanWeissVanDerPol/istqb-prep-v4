# 📋 Cheatsheet Cap 5 — Gestión de Testing (1 página)

> *Imprimible. Para repaso rápido.*

---

## 🎯 ISTQB en 1 frase

> Gestionar testing = **planificar** qué se va a testear, **monitorear** cómo va, **controlar** desvíos, y **manejar defectos** cuando aparecen. Igual que gestionar una clínica.

---

## 🏗️ Componentes del Test Plan (LO 5.1.2) ⭐

```
Test Plan:
├─ 1. Contexto (qué sistema, stakeholders)
├─ 2. Actividades (qué se va a hacer)
├─ 3. Recursos (humanos, técnicos, infraestructura)
├─ 4. Cronograma
├─ 5. Criterios de entrada y salida ⭐
├─ 6. Riesgos
├─ 7. Estrategia (qué niveles/tipos)
└─ 8. Métricas
```

**Dental:** tu plan de tratamiento tiene los mismos componentes.

---

## 🆚 Test Plan vs Test Strategy (LO 5.1.3)

| Test Plan | Test Strategy |
|---|---|
| Para **un proyecto específico** | Para **toda la organización** |
| Detallado, con cronograma | General, con principios |
| Plan de tratamiento del paciente X | Protocolo institucional del consultorio |

---

## 📊 Risk-based testing (LO 5.3.1) ⭐⭐

**Idea:** no podés testear todo. Priorizá lo que tiene **más riesgo**.

**Riesgo = Probabilidad × Impacto**

```
              IMPACTO
              Bajo    Medio    Alto
PROB  Alta  |  M  |  A  |  MA |
      Media |  B  |  M  |  A  |
      Baja  |  MB |  B  |  M  |
```

Testear primero los **MA** (Muy Alto), después los A, etc.

**Dental:** priorización de la cola de espera:
- Dolor agudo + absceso → MA (urgente)
- Dolor sin absceso → A
- Caries asintomática → M
- Control de rutina → B

---

## 📈 Métricas (LO 5.2.2) ⭐

| Métrica | Qué mide | Tipo |
|---|---|---|
| % casos de prueba pasados | Calidad del producto | Producto |
| Densidad de defectos (bugs/KLOC) | Complejidad | Producto |
| Cobertura de testing | Cuánto se cubrió | Producto |
| % tests ejecutados a tiempo | Eficiencia del proceso | Proceso |
| Tiempo medio de detección | Eficiencia del testing | Proceso |
| Tiempo medio de resolución | Eficiencia del fix | Proceso |

> 📌 **Producto ≠ Proceso.** Memorizar la diferencia.

---

## 🔄 Monitoring vs Control (LO 5.1.1, 5.2.1)

| Monitoring | Control |
|---|---|
| **Recolectar datos** sobre cómo va | **Tomar acciones correctivas** |
| "El testing va al 60% del plan" | "Hay que agregar más testers" |
| **Pasivo** | **Activo** |

**Dental:**
- Monitoring: ¿el paciente está evolucionando?
- Control: "está empeorando, cambio el plan"

---

## ⚙️ Configuration Management (LO 5.3.2)

**Qué:** todo lo que se usa en testing bajo control de versiones:
- Requisitos
- Código
- Tests
- Datos
- Herramientas
- Documentos

**Dental:** control de versiones de protocolos, calibración de equipos, lotes de materiales.

---

## 🐛 Defect Management (LO 5.3.3, 5.3.4) ⭐⭐

### Campos de un bug report:

| Campo | Ejemplo dental |
|---|---|
| ID | BUG-001 |
| Título | "Software pierde citas los domingos" |
| Severidad | Crítica / Alta / Media / Baja |
| Prioridad | Urgente / Alta / Media / Baja |
| Pasos para reproducir | Cómo se llega al bug |
| Resultado esperado vs actual | Lo que debería / lo que pasa |
| Estado | Abierto / En progreso / Resuelto / Cerrado |
| Asignado a | Quién lo arregla |

### Severidad vs Prioridad (LO 5.3.3)

| Severidad | Prioridad | Ejemplo |
|---|---|---|
| Alta | Alta | Login roto, nadie puede entrar |
| **Alta** | **Baja** | Defecto crítico en función que **nadie usa** |
| Baja | Alta | Cosmético, pero urge para demo de mañana |
| Baja | Baja | Cosmético, no urge |

> 📌 **Severidad = impacto técnico. Prioridad = cuándo se arregla.**

### Ciclo de vida del defecto:

```
Nuevo → Asignado → En progreso → Resuelto → Cerrado
  ↑                                      ↓
  └──── Reabierto ←── No reproducido ←───┘
```

---

## 🎯 Criterios de entrada y salida (LO 5.1.2)

**Criterios de entrada:** cuándo empezar a testear
- Ej: "se empieza a testear cuando los requisitos están firmados"

**Criterios de salida:** cuándo dejar de testear
- Ej: "se cierra cuando se ejecutaron todos los tests planeados + no hay defectos críticos abiertos"

---

*Cap 5 listo. Memorizá el ciclo de vida del defecto y los componentes del test plan.*
