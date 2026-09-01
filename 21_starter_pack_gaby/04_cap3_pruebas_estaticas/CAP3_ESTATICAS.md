# Cap 3 — Pruebas Estáticas (versión clínica)

> **Versión ISTQB CTFL v4.0.1 — Sección 3.** Cubre LOs **3.1.1, 3.1.2, 3.2.1, 3.2.2, 3.3.1, 3.3.2, 3.3.4** (7 de 7 LOs del capítulo).
>
> Equivalente a [`../../05_summaries/cap_03_estaticas_v4.md`](../../05_summaries/cap_03_estaticas_v4.md) del repo principal.
>
> Tiempo de lectura: ~25 minutos.
>
> **Para repaso rápido:** [`CHEATSHEET_CAP3.md`](CHEATSHEET_CAP3.md) (1 página).

---

## 1. ¿Qué son las pruebas estáticas? (3.1)

ISTQB define dos grandes familias de testing:

- **Dynamic testing:** ejecutás el software y mirás si funciona.
- **Static testing:** NO ejecutás el software. **Revisás** los documentos (requisitos, código, diseños, manuales) para encontrar defectos.

### En la clínica

**Static testing = revisar antes de actuar.**

Ejemplos que ya hacés:

| Práctica clínica | Static testing equivalente |
|---|---|
| Revisar la radiografía antes de tratarla | Inspección visual de artefactos |
| Leer la historia clínica antes de la consulta | Walkthrough de documentos |
| Discutir un caso complejo en el ateneo | Technical review |
| Verificar que el consentimiento informado esté completo | Inspection formal |
| Revisar la receta antes de firmarla | Peer review |
| Checklist pre-quirúrgico (OMS) | Formal review con checklist |

**Idea clave:** podés encontrar **la mayoría de los defectos** sin necesidad de ejecutar el software. Una buena revisión de requisitos elimina defectos que serían carísimos de arreglar después.

### Beneficios de las pruebas estáticas (3.1.1)

ISTQB lista estos beneficios (todos aplican a tu práctica):

1. **Encontrar defectos temprano** — antes de que se hagan código, antes de que lleguen al paciente
2. **Detectar defectos que el testing dinámico no encuentra** — ej: requisitos faltantes, inconsistencias, ambigüedades
3. **Mejorar la comunicación** — al revisar, todos entienden lo mismo
4. **Reducir costos** — arreglar un requisito mal escrito cuesta muchísimo menos que arreglar un sistema ya construido
5. **Mejorar la calidad del producto final** — porque los documentos están mejor escritos

**En la clínica:**
> Cuando hacés un ateneo y revisás un caso antes de la cirugía, encontrás cosas que en el momento de la cirugía te habrían demorado 30 minutos o puesto en riesgo al paciente. Eso es testing estático.

---

## 2. Productos que se pueden revisar (3.2)

ISTQB dice que se puede revisar cualquier "work product". En software:

- **Requisitos** (qué tiene que hacer el sistema)
- **Diseño** (cómo va a estar armado)
- **Código** (la implementación en sí)
- **Test plans** (planes de prueba)
- **Test cases** (casos de prueba específicos)
- **Manuales de usuario**
- **Contratos**
- **Cualquier documento**

### En la clínica

Documentos que revisás:

| Documento dental | Work product ISTQB equivalente |
|---|---|
| Historia clínica | Documento de requisitos (estado actual del paciente) |
| Plan de tratamiento | Diseño (cómo voy a resolver) |
| Consentimiento informado | Contrato (qué acepta el paciente) |
| Epicrisis | Manual de uso (instrucciones post-operatorias) |
| Presupuesto | Especificación funcional (qué incluye y qué no) |
| Auditoría de historia clínica | Code review (revisión de pares) |

---

## 3. Tipos de revisión (3.3) ⭐ IMPORTANTE

ISTQB distingue 4 tipos de revisión, de menos formal a más formal.

### 1. Informal Review (Revisión informal)

**Qué:** pasarle el documento a un colega y pedirle opinión. Sin estructura, sin roles, sin proceso formal.

**En la clínica:**
> *"Che, ¿vos qué harías en este caso?"* Conversación de pasillo con un colega.

**Pros:** rápido, barato.
**Contras:** inconsistente, no se documenta, depende de la buena voluntad.

### 2. Walkthrough (Recorrido guiado)

**Qué:** el **autor** del documento lo presenta a un grupo. El grupo hace preguntas y comenta. El autor guía.

**En la clínica:**
> El residente **presenta** el caso al ateneo. Los médicos asistentes preguntan, sugieren, cuestionan. El residente explica su razonamiento.

**Pros:** educativo, el autor recibe feedback directo.
**Contras:** lento, depende de la calidad del presentador.

### 3. Technical Review (Revisión técnica)

**Qué:** grupo de expertos técnicos revisa el documento. Discusión técnica. Identifica problemas técnicos.

**En la clínica:**
> Reunión del cuerpo médico para evaluar un protocolo institucional nuevo. Expertos en la materia debaten si el protocolo es técnicamente correcto.

**Pros:** riguroso, peer-reviewed.
**Contras:** requiere expertise, scheduling difícil.

### 4. Inspection (Inspección formal)

**Qué:** el más formal. Roles definidos, proceso paso a paso, métricas, checklists, log de defectos.

**Roles típicos:**
- **Author:** el que escribió el documento
- **Moderator:** facilita la reunión
- **Reader:** lee el documento en voz alta
- **Reviewer:** experto técnico que busca defectos
- **Recorder:** anota todos los defectos encontrados

**Proceso típico:**
1. Planning
2. Overview (introducción)
3. Individual preparation (cada uno lee solo)
4. Inspection meeting (reunión para discutir)
5. Rework (el autor corrige)
6. Follow-up (verificar que se corrigió)

**En la clínica:**
> Las **auditorías de historias clínicas** que hace el Círculo de Odontólogos o una aseguradora de calidad. Checklists, roles, proceso formal, métricas (% historias completas).

**Pros:** muy efectivo, encuentra muchos defectos.
**Contras:** caro, requiere tiempo, no escalable para todo.

---

## 4. Diferencia entre los 4 tipos

| Tipo | Formalidad | Roles definidos | Proceso documentado | Métricas |
|---|---|---|---|---|
| Informal review | Baja | No | No | No |
| Walkthrough | Media | A veces | A veces | No |
| Technical review | Alta | Sí | Sí | A veces |
| Inspection | Muy alta | Sí (5 roles) | Sí (6 pasos) | Sí |

**En el examen:** te pueden preguntar las diferencias. Memorizar esta tabla.

---

## 5. Success Factors for Reviews (3.4)

ISTQB dice que las revisiones funcionan mejor si:

1. **Hay objetivos claros** — saber qué se busca
2. **Los revisores son los adecuados** — expertise relevante
3. **Se usan checklists** — para no olvidarse de cosas
4. **Se registran los defectos encontrados** — para no perderlos
5. **Hay seguimiento** — verificar que se corrigieron

**En la clínica:**
> Misma lógica que un ateneo exitoso:
> - Objetivo: ¿estamos viendo un caso complejo o definiendo un protocolo?
> - Asistentes: ¿están los especialistas adecuados?
> - Checklist: ¿tenemos los puntos a cubrir?
> - Acta: ¿se documentó lo decidido?
> - Seguimiento: ¿se implementó lo acordado?

---

## Resumen del Cap 3

✅ Static testing = revisar sin ejecutar. Encontrás defectos en documentos.
✅ Se puede aplicar a cualquier work product (requisitos, código, historia clínica, presupuesto).
✅ 4 tipos de revisión: informal → walkthrough → technical → inspection (de menos a más formal).
✅ Más formal = más roles, más proceso, más métricas.
✅ Las revisiones tempranas son más baratas que testing dinámico.
✅ El ateneo clínico es un walkthrough. La auditoría es una inspection.

---

## Para chequear que entendiste

1. ¿Cuál es la diferencia entre walkthrough y technical review?
2. ¿Qué requiere una inspection formal que no requiere un walkthrough?
3. ¿Cuándo conviene más hacer static testing que dynamic testing? (Pista: pensá en una historia clínica de 12 años.)

Hacé el [`QUIZ_CAP3.md`](../08_quizzes_dentales/QUIZ_CAP3.md).
