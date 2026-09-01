# 📋 Cheatsheet Cap 3 — Pruebas Estáticas (1 página)

> *Imprimible. Para repaso rápido.*

---

## 🎯 ISTQB en 1 frase

> **Static testing** = revisar documentos sin ejecutar el software. **Encuentra defectos temprano** y **barato**.

---

## 🔄 Static vs Dynamic testing (LO 3.1.1) ⭐

| Static | Dynamic |
|---|---|
| **No ejecuta** el software | **Ejecuta** el software |
| Revisa documentos (requisitos, código, historia clínica) | Prueba el sistema funcionando |
| Encuentra defectos en artefacts | Encuentra defects en ejecución |
| **Más barato** encontrar defectos | Más caro encontrar defectos |

---

## 📚 Work products que se pueden revisar (LO 3.2.1)

- Requisitos (qué tiene que hacer)
- Diseño (cómo se va a armar)
- Código fuente
- Test plans, test cases
- Manuales de usuario
- Contratos, presupuestos
- **Cualquier documento**

**Dental:** historia clínica, plan de tratamiento, consentimiento informado, presupuesto, epicrisis, manual de la autoclave.

---

## 🎯 Beneficios de static testing (LO 3.1.2, 3.2.2)

1. Encuentra defectos **temprano** (antes que dynamic)
2. Encuentra defectos que dynamic **NO encuentra** (ambigüedades, requisitos faltantes)
3. Mejora la comunicación
4. Reduce costos
5. Mejora la calidad del producto final

---

## 🏆 4 Tipos de revisión (LO 3.3.1, 3.3.2) ⭐⭐

De MENOS formal a MÁS formal:

```
┌─────────────────────────────────────────────────┐
│ 1. INFORMAL REVIEW                              │
│    Pasar el doc a un colega. Sin estructura.    │
│    "Che, ¿vos qué harías?"                      │
├─────────────────────────────────────────────────┤
│ 2. WALKTHROUGH                                  │
│    Autor PRESENTA. Grupo pregunta.               │
│    📌 El residente presenta el caso al ateneo.  │
├─────────────────────────────────────────────────┤
│ 3. TECHNICAL REVIEW                             │
│    Expertos evalúan técnicamente. Decisión.      │
│    Reunión del cuerpo médico para protocolo.     │
├─────────────────────────────────────────────────┤
│ 4. INSPECTION                                   │
│    Formal: roles, checklist, métricas, 6 pasos.  │
│    📌 Auditoría del Círculo de Odontólogos.      │
└─────────────────────────────────────────────────┘
```

**Característica por característica:**

| Característica | Informal | Walkthrough | Technical | Inspection |
|---|---|---|---|---|
| Roles definidos | No | A veces | Sí | Sí (5) |
| Proceso documentado | No | A veces | Sí | Sí (6 pasos) |
| Métricas | No | No | A veces | Sí |
| Checklists | No | No | A veces | Sí |

---

## 👥 Roles en una Inspection formal (LO 3.3.1)

| Rol | Función |
|---|---|
| **Author** | Escribió el documento |
| **Moderator** | Facilita la reunión |
| **Reader** | Lee el documento en voz alta |
| **Reviewer** | Experto técnico, busca defects |
| **Recorder** | Anota los defects encontrados |

---

## 🔄 Proceso de Inspection (6 pasos)

1. **Planning** — qué se revisa, quién, cuándo
2. **Overview** — introducción (opcional)
3. **Individual preparation** — cada uno lee solo
4. **Inspection meeting** — reunión para discutir
5. **Rework** — el autor corrige
6. **Follow-up** — verificar que se corrigió

---

## ✅ Success factors (LO 3.3.4)

1. Objetivos claros
2. Revisores adecuados (expertise)
3. Checklists para no olvidar
4. Registro de defects
5. Seguimiento (verificar que se corrigió)

**Dental:** Misma lógica que un ateneo exitoso.

---

## 🎯 Cuándo static testing > dynamic testing

- ✅ Cuando hay documentos que revisar (siempre hay)
- ✅ Cuando querés encontrar defectos temprano
- ✅ Para requisitos ambiguos o incompletos
- ✅ Para validar diseño antes de codificar

---

*Cap 3 listo. Memorizá los 4 tipos de revisión en orden de formalidad.*
