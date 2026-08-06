# Resumen Cap 3 (v4.0.1) — Static Testing

## 1. Static Testing Basics (3.1)

### 1.1 Work products que se pueden testear (3.1.1) ⭐

**Cualquier artefacto producido durante el SDLC:**
- Especificación de requisitos
- Diseño (alto nivel, detallado)
- Código fuente
- Scripts de testing
- **Casos de prueba manuales**
- Documentación de usuario
- Contratos
- Modelos de datos

### 1.2 Valor del Static Testing (3.1.2)

**Beneficios:**
- Detecta defects **antes** que se ejecute el código (más temprano = más barato)
- Encuentra omisiones, ambigüedades, inconsistencias
- Mejora comunicación
- Reduce defectos en etapas tardías
- Permite **participación** de stakeholders

**Tipos de defectos encontrados:**
- Omisiones
- Errores tipográficos
- Ambigüedades
- Inconsistencias entre documentos
- Requisitos inalcanzables
- Errores de diseño

### 1.3 Static vs Dynamic (3.1.3) ⭐

| Static | Dynamic |
|---|---|
| NO ejecuta el software | SÍ ejecuta el software |
| Reviews + análisis estático | Test execution |
| Encuentra "defects en código" | Encuentra failures |
| Más temprano en el ciclo | Más tarde |

**Ambos son complementarios.** Static encuentra defectos que dynamic no encuentra (y viceversa).

---

## 2. Review Process (3.2)

### 2.1 Beneficios del feedback temprano (3.2.1)

> "Early and frequent stakeholder feedback"

- Detectar issues antes
- Alineamiento con el negocio
- Reduce re-trabajo
- Mejora satisfacción

### 2.2 Actividades del review process (3.2.2) ⭐

```
Planning → Kick-off → Individual preparation →
  Review meeting (defects logged) →
    Rework (author fixes) →
      Follow-up (verificar fixes)
```

### 2.3 Roles en reviews (3.2.3) ⭐

| Rol | Responsabilidad |
|---|---|
| **Author** | Crea el documento, arregla defectos |
| **Moderator** | Facilita, media, no juzga |
| **Reviewer** | Identifica defectos, sugiere mejoras |
| **Scribe** | Registra defectos en sesión |
| **Manager** | Asigna recursos, monitorea progreso |

### 2.4 Tipos de review (3.2.4) ⭐⭐

| Tipo | Formalidad | Líder |
|---|---|---|
| **Informal review** | Muy baja | No aplica |
| **Walkthrough** | Baja | Autor |
| **Technical review** | Media | No autor |
| **Inspection** | Alta | Moderator (no autor) |

**Walkthrough:**
- Liderado por el **autor**
- Sin roles formales
- Sin métricas
- Informal

**Inspection (la más formal):**
- Liderada por **moderator** (no autor)
- Roles formales: moderator, author, reviewer, scribe
- Proceso estructurado: planning, individual prep, meeting, rework, follow-up
- **Métricas reunidas:** # defects, effort, time
- Basada en reglas y checklists

**Technical review:** nivel medio. Sin scribe formal.

### 2.5 Factores de éxito de una review (3.2.5)

- **Charter claramente definido**
- **Reviewers correctos** (competentes)
- **Tiempo adecuado** para preparación
- **Material entregado a tiempo**
- **Checklist efectiva**
- **Aprendizaje organizacional** (métricas se preservan)
- **Cultura psicológica segura** (no blame)

---

## 🎯 Preguntas típicas

1. ¿Cuál es el tipo de review más formal?
2. ¿Quién lidera un walkthrough?
3. ¿Qué es el rol de moderator en una inspection?
4. ¿Cuál es la diferencia entre static y dynamic testing?
5. ¿Cuántas actividades tiene una inspection formal?
6. ¿Qué work products NO son típicamente testeados con static testing?

---

## 📝 Mnemotécnicos

- **6 activities de inspection:** "P-K-I-R-F" (Plan, Kick, Inspect (prep+meeting), Rework, Follow-up)
- **5 roles de review:** "MARS" + Manager (Moderator, Author, Reviewer, Scribe)
- **Static vs Dynamic:** "STATIC piensa antes de ejecutar; DYNAMIC ejecuta y observa"
- **Tipo de review por formalidad:** "Informal < Walkthrough < Technical < Inspection"
