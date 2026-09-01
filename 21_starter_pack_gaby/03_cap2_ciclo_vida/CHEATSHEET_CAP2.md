# 📋 Cheatsheet Cap 2 — Ciclo de Vida (1 página)

> *Imprimible. Para repaso rápido.*

---

## 🎯 ISTQB en 1 frase

> El testing ocurre **en todas las fases del desarrollo**, no solo al final. Hay distintos **niveles** (qué tan grande es la unidad testeada) y **tipos** (qué se testea).

---

## 📐 Modelos de ciclo de vida (LO 2.1.2) ⭐

```
WATERFALL          Requisitos → Diseño → Impl → Test → Deploy
                    (lineal, una vez)

MODELO EN V        Cada fase de dev tiene su fase de test对应的对应
                    (test cases se diseñan junto con requisitos)

ITERATIVO          Producto se construye en iteraciones cortas
                    (ortodoncia con alineadores: cada set = iteración)

INCREMENTAL        Entregas parciales funcionales
                    (rehabilitación por fases: perio → operatoria → prostodoncia)

AGILE              Iterativo + incremental + feedback continuo
                    (Scrum: sprints de 2 semanas)
```

**Cuándo usar V:** sistemas críticos (médico, aeronáutico).
**Cuándo usar ágil:** requisitos cambiantes, feedback temprano.

---

## 🏗️ 4 Niveles de testing (LO 2.2.1) ⭐⭐⭐

| Nivel | Qué se testea | Quién | Dental |
|---|---|---|---|
| **Component** | Unidad más pequeña (función, pantalla) | Developer | Probar el autoclave solo |
| **Integration** | Cómo trabajan juntas las unidades | Developer / Tester | Probar RVG + software juntos |
| **System** | El sistema completo end-to-end | Tester dedicado | Probar todo el journey del paciente |
| **Acceptance** | El usuario acepta | Cliente / vos | "OK, adopto el software" |

> 📌 **De menor a mayor alcance**: Component → Integration → System → Acceptance.

---

## 🔍 Tipos de testing (LO 2.2.2, 2.3.1, 2.4.1) ⭐

### Functional (LO 2.2.2)

**Qué:** ¿El sistema hace lo que tiene que hacer?

### Non-functional (LO 2.2.2)

**Qué:** ¿Cómo lo hace? (Performance, usability, security, etc.)

### Change-related (LO 2.2.3) ⭐

| Tipo | Qué verifica | Dental |
|---|---|---|
| **Confirmation** | El bug específico reportado se arregló | ¿Desapareció el dolor del paciente? |
| **Regression** | Lo que antes andaba, sigue andando | ¿El paciente sigue mordiendo bien después del cambio? |

> 📌 **Confirmation ≠ Regression.** Confirmation verifica el fix; Regression verifica el resto.

### Maintenance (LO 2.4.1)

**Qué:** testing después de cambios en el entorno (Windows update, navegador, etc.), no en el código.

---

## 🔥 Tipos adicionales que preguntan

| Tipo | Qué es | Cuándo |
|---|---|---|
| **Smoke** | ¿Arranca lo básico? | Primera ejecución después de build |
| **Sanity** | ¿La parte específica que cambió funciona razonablemente? | Después de un cambio pequeño |
| **Exploratory** | Sin docs previas, descubrir mientras testeás | Cuando hay poco tiempo o sistema nuevo |
| **Ad-hoc** | Sin documentación ni diseño, informal | Tester con experiencia, escenarios raros |

---

## 📊 Matriz niveles × tipos

```
                  ┌─────────────────────────────────────────────┐
                  │              Acceptance Testing             │
                  ├─────────────────────────────────────────────┤
                  │              System Testing                │
                  ├─────────────────────────────────────────────┤
                  │            Integration Testing              │
                  ├─────────────────────────────────────────────┤
                  │           Component Testing                 │
                  └─────────────────────────────────────────────┘
                  Cada nivel puede tener: Functional | Non-functional | Change-related
```

---

## ⬅️ Shift-left testing (LO 2.5.2)

**Idea:** testing temprano. No esperar al final.

**Dental:** no esperar a que el paciente vuelva con dolor. Hacer diagnóstico temprano.

**Beneficio:** defectos encontrados en requisitos cuestan 100x menos que en producción.

---

## 🔄 Maintenance testing (LO 2.4.1)

**Cuándo:** cambios en el entorno (no en el código):
- Sistema operativo se actualiza
- Navegador se actualiza
- Base de datos migra
- Integración con sistema externo cambia

**Dental:** cuando cambia el instrumental (nueva autoclave) o el software de la clínica, hay que revalidar todo.

---

## 🎯 Relación testing ↔ development (LO 2.5.1)

| Testing | Development |
|---|---|
| ¿Está bien hecho? | Construir lo que hay que construir |
| Encuentra defects | Corrige defects |
| Tester | Developer |

**Independencia:** los dos roles deben estar separados para evitar sesgo de confirmación.

---

*Cap 2 listo. Memorizá los 4 niveles en orden. Memorizá confirmation ≠ regression.*
