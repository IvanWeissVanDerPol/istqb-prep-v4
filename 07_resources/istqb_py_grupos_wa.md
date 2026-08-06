# 🇵🇾 Grupos ISTQB Paraguay — WhatsApp Real

> **Cruce del corpus WhatsApp de Iván (psycology/) con los grupos ISTQB PY activos.**

## ⚠️ Sobre los JIDs que me pasaste

**`@201309445722357` y `@117111141752976`** son JIDs internos del bridge de WhatsApp de Iván (encontrados en `/root/.hermes/whatsapp/session/device-list-*.json`). **NO son contactos** — son los device IDs del propio account.

Después de buscar en el corpus real, encontré los **verdaderos grupos ISTQB PY**:

---

## 📋 Grupos ISTQB PY encontrados en el corpus

### 1. **ISTQB Brave and Courageous** ⭐⭐⭐

- **JID:** `120363175387159404@g.us` (sujeto "Istqb Brave and Courageous")
- **129 mensajes**
- **6 miembros** activos (excluyendo a Iván)
- **Actividad típica:** hablando de exam scores "17/40", "20/40" — están rindiendo el CTFL

**Los 6 miembros del grupo:**

| # | JID | Nombre verificado | Fuente |
|---|---|---|---|
| 1 | `595982923913` | **Natalia Cruz** | `RELATIONSHIPS/dynamics/NATALIA_CRUZ.md` (tier3_extended, activo, score 54.9) |
| 2 | `595981459382` | **Daisy** | `RELATIONSHIPS/dynamics/DAISY.md` (tier2_core, score 53.6, 327 mensajes) |
| 3 | `595974465910` | **Alejandro Maciel (MentorMate)** | `RELATIONSHIPS/dynamics/ALEJANDRO_MACIEL_MENTORMATE.md` (INSTRUCTOR del curso) |
| 4 | `595971190089` | **Jose S** | `RELATIONSHIPS/dynamics/JOSE_S.md` (untiered, score 51.5, 52 mensajes) |
| 5 | `595983988909` | ¿? | Sin nombre en vCard — usuario sin apodo |
| 6 | `595961831298` | **V BC** | vCard: 'V BC' (probablemente Vicky B.C. — apellido completo privado) |

### 2. **Organización Py Testing**

- **JID:** (no usado como grupo individual)
- **212 mensajes, 20 miembros** (la mayoría con `@lid` formato de anonimato migrado)
- **1 miembro identificado por nombre en intro:**
  - `126869122850854@lid` → **"María Luz Enciso (Malu) — Analista QA, anotada en recepción y logística"**

### 3. **Taller de Introducción QA [Instructores]**

- **JID:** (no usado)
- **128 mensajes, 5 miembros**

**5 miembros:**

| JID | Nombre verificado | Fuente |
|---|---|---|
| `595982525050` | (no en vCard — verificar) | Posible instructor |
| `595982684027` | (no en vCard) | |
| `595986361808` | (no en vCard) | |
| `595986445564` | (no en vCard) | |
| `595991381669` | (no en vCard) | |

### 4. **Py Testing Community**

- **JID:** `120363175387159404@g.us`
- **2056 mensajes, 226 miembros** — **el grupo ISTQB PY masivo**
- 1 ejemplo de intro:
  - `50498676217@s.whatsapp.net` → mensaje reciente

---

## 👥 Tu "grupo de amigos" ISTQB (los más probables)

Basado en la **fuerza de relación** con Iván:

| Persona | Tier | Score | Veredicto |
|---|---|---|---|
| Daisy | tier2_core | 53.6 | ⭐ **Amiga cercana, también ISTQB** |
| Natalia Cruz | tier3_extended | 54.9 | ⭐ **Contacto regular ISTQB** |
| Alejandro Maciel | untiered | 51.1 | 🎓 **INSTRUCTOR del curso ISTQB** (MentorMate employee) |
| Jose S | untiered | 51.5 | **Contacto ISTQB** |
| V BC | untiered | ? | **Contacto ISTQB** |

**Interpretation:** Alejandro Maciel de MentorMate es probablemente el **instructor** del taller ISTQB. Los otros 5 son sus **estudiantes** — Daisy, Natalia, Jose, V BC, y un tercero sin nombre. **Es ahí donde están "tus amigos"** que van a rendir el examen.

---

## 🔍 Cómo usé esta información

- Source data: `psycology/SOURCE_OF_TRUTH/wa_messages/tier4_groups/`
- Names: `psycology/RELATIONSHIPS/dynamics/*.md` + `_stubs/`
- Phones: `psycology/SOURCE_OF_TRUTH/wa_messages/_ANALYSIS/contacts_full.vcf` (vCard)
- LID mappings: `~/.hermes/whatsapp/session/lid-mapping-*.json`

---

## 📝 Para comunicación directa

Si querés hablar con cada uno, podés usar:
- WhatsApp directo al número (sin prefijo +595)
- O a través de los grupos ya activos

**Nombre = JID:**
- Daisy → `+595 981 459382`
- Natalia Cruz → `+595 982 923913`
- Alejandro Maciel → `+595 974 465910`
- Jose S → `+595 971 190089`
- V BC → `+595 961 831298`

(El sexto: `+595 983 988909` sin nombre conocido)

---

## 🎯 Recomendación

Si lo que querés es agregar a tus amigos al repo:
1. Compartiles la URL del repo público: `https://github.com/IvanWeissVanDerPol/istqb-prep-v4`
2. Si preferís un grupo más cerrado: hacer un fork cada uno en su cuenta personal
3. Si rendís el examen juntos: agendá una sesión semanal en video para discutir quizzes/sample exams
