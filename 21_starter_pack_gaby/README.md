# 🦷 ISTQB CTFL v4.0.1 — Versión Gaby (Guía Completa)

> **La guía completa del ISTQB Certified Tester Foundation Level v4.0.1, explicada en lenguaje odontológico.** Para la **Dra. Gabriella María González Pane** — odontóloga, 3 especialidades + doctorado, 20+ años de carrera.
>
> **Mantenedor:** Ivan Weiss Van Der Pol
> **Syllabus oficial:** ISTQB CTFL v4.0.1 (15-sep-2024, 78 páginas, 1135 minutos oficiales)
> **Material base:** [`IvanWeissVanDerPol/istqb-prep-v4`](https://github.com/IvanWeissVanDerPol/istqb-prep-v4)
> **Fecha:** septiembre 2026

---

## 🎯 Esta guía es **completa y autocontenida**

**No necesitás abrir el repo principal.** Todo lo que necesitás para el examen está acá, explicado en tu lenguaje. El repo principal tiene material adicional (cheat sheets imprimibles, Anki deck, simulacros extra, grupos de estudio ASOLINFO PY) — recomendado después de terminar esta guía.

---

## 📚 El syllabus oficial ISTQB CTFL v4.0.1 — qué cubre esta guía

ISTQB CTFL v4.0.1 tiene **6 capítulos** y **~40 Learning Objectives (LOs)**. Esta guía cubre **el 100%** de los LOs oficiales, traducidos a contexto odontológico:

| Cap oficial | LOs cubiertos | Carpeta en esta guía |
|---|---|---|
| **1. Fundamentals of Testing** | 1.1.1–1.5.3 (10 LOs) | `02_cap1_fundamentos/` |
| **2. Testing Throughout the Software Development Lifecycle** | 2.1.1–2.5.2 (10 LOs) | `03_cap2_ciclo_vida/` |
| **3. Static Testing** | 3.1.1–3.3.4 (7 LOs) | `04_cap3_pruebas_estaticas/` |
| **4. Test Design Techniques** ⭐ | 4.1.1–4.5.4 (16 LOs, **cap más importante**) | `05_cap4_tecnicas_diseno/` |
| **5. Managing the Test Activities** | 5.1.1–5.3.4 (10 LOs) | `06_cap5_gestion/` |
| **6. Tools Support for Testing** | 6.1.1–6.4.3 (8 LOs) | `07_cap6_herramientas/` |

**Total:** 61 LOs oficiales cubiertos. Mirá [`00_antes_de_empezar/MAPA_SYLLABUS_OFICIAL.md`](00_antes_de_empezar/MAPA_SYLLABUS_OFICIAL.md) para ver el desglose LO por LO.

---

## 🗺️ Estructura de esta guía (13 carpetas, 35 archivos)

```
21_starter_pack_gaby/
│
├── README.md                                      ← estás acá
│
├── 00_antes_de_empezar/                           ← antes de leer nada
│   ├── CARTA_PARA_GABY.md                          (la carta personal que ya leíste)
│   ├── AUTODIAGNOSTICO.md                          (15 preguntas — mida tu baseline)
│   └── MAPA_SYLLABUS_OFICIAL.md                    (LO por LO — qué cubre esta guía)
│
├── 01_introduccion/
│   ├── POR_QUE_ISTQB_PARA_GABY.md                  (motivación + ROI personal)
│   └── PLAN_8_SEMANAS.md                           (calendario realista)
│
├── 02_cap1_fundamentos/                            ← 1.1–1.5
│   ├── CAP1_FUNDAMENTOS.md                         (versión clínica completa)
│   └── CHEATSHEET_CAP1.md                          (1 página imprimible)
│
├── 03_cap2_ciclo_vida/                             ← 2.1–2.5
│   ├── CAP2_CICLO_VIDA.md
│   └── CHEATSHEET_CAP2.md
│
├── 04_cap3_pruebas_estaticas/                      ← 3.1–3.3
│   ├── CAP3_ESTATICAS.md
│   └── CHEATSHEET_CAP3.md
│
├── 05_cap4_tecnicas_diseno/                        ← 4.1–4.6 (cap largo)
│   ├── CAP4_TECNICAS.md
│   └── CHEATSHEET_CAP4.md
│
├── 06_cap5_gestion/                                ← 5.1–5.3
│   ├── CAP5_GESTION.md
│   └── CHEATSHEET_CAP5.md
│
├── 07_cap6_herramientas/                           ← 6.1–6.4
│   ├── CAP6_HERRAMIENTAS.md
│   └── CHEATSHEET_CAP6.md
│
├── 08_quizzes_dentales/
│   ├── QUIZ_DIAGNOSTICO_INICIAL.md                 (15 preguntas — antes de empezar)
│   ├── QUIZ_CAP1.md (10 preguntas)
│   ├── QUIZ_CAP2.md (10 preguntas)
│   ├── QUIZ_CAP3.md (8 preguntas)
│   ├── QUIZ_CAP4.md (12 preguntas — el más importante)
│   ├── QUIZ_CAP5.md (10 preguntas)
│   └── QUIZ_CAP6.md (8 preguntas)
│
├── 09_examenes_simulacro/
│   ├── SAMPLE_EXAM_A.md (40 preguntas, 60 min)
│   ├── SAMPLE_EXAM_A_ANSWERS.md (con explicaciones)
│   ├── SAMPLE_EXAM_B.md (40 preguntas)
│   ├── SAMPLE_EXAM_B_ANSWERS.md
│   └── SAMPLE_EXAM_C.md (40 preguntas — sin respuestas, para práctica real)
│
├── 10_glosario_oficial_istqb/
│   ├── GLOSARIO_DENTAL_QA.md                        (ES dental ↔ EN ISTQB ↔ PT)
│   └── GLOSARIO_OFICIAL_ISTQB.md                    (los 200+ términos oficiales v4.0.1)
│
├── 11_checklist_pre_examen/
│   └── CHECKLIST_FINAL.md                           (la semana antes del examen)
│
└── 12_post_examen/
    └── QUE_HACE_DESPUES.md                          (después de aprobar — qué sigue)
```

---

## 🚀 Quickstart (orden recomendado)

### Fase 1: Antes de empezar (1 día)

1. **Leé** [`00_antes_de_empezar/CARTA_PARA_GABY.md`](00_antes_de_empezar/CARTA_PARA_GABY.md) — la carta personal (5 min).
2. **Hacé** [`00_antes_de_empezar/AUTODIAGNOSTICO.md`](00_antes_de_empezar/AUTODIAGNOSTICO.md) — 15 preguntas para saber tu baseline (20 min).
3. **Mirá** [`00_antes_de_empezar/MAPA_SYLLABUS_OFICIAL.md`](00_antes_de_empezar/MAPA_SYLLABUS_OFICIAL.md) — qué vas a aprender LO por LO (10 min).
4. **Leé** [`01_introduccion/POR_QUE_ISTQB_PARA_GABY.md`](01_introduccion/POR_QUE_ISTQB_PARA_GABY.md) — por qué ISTQB te sirve específicamente a vos (10 min).

### Fase 2: Estudio por capítulos (8 semanas, 3-4 h/sem)

Seguí el [`01_introduccion/PLAN_8_SEMANAS.md`](01_introduccion/PLAN_8_SEMANAS.md). Cada semana:

1. Leé el capítulo completo (`02_cap1...`, `03_cap2...`, etc.).
2. Imprimí la [`CHEATSHEET_CAP?.md`](.../CHEATSHEET_CAP?.md) correspondiente y pegala en la pared.
3. Hacé el quiz del capítulo (`08_quizzes_dentales/QUIZ_CAP?.md`).
4. Si fallás más del 30%, releé el capítulo antes de avanzar.

### Fase 3: Simulación de examen (semana 8)

1. **Lunes:** `09_examenes_simulacro/SAMPLE_EXAM_A.md` cronometrado (60 min).
2. **Miércoles:** Revisá respuestas y entendé cada error con `SAMPLE_EXAM_A_ANSWERS.md`.
3. **Viernes:** `09_examenes_simulacro/SAMPLE_EXAM_B.md` cronometrado + revisar.
4. **Domingo:** `09_examenes_simulacro/SAMPLE_EXAM_C.md` (sin respuestas — práctica real).

### Fase 4: Semana del examen

Seguí el [`11_checklist_pre_examen/CHECKLIST_FINAL.md`](11_checklist_pre_examen/CHECKLIST_FINAL.md) día por día.

### Fase 5: Post-examen

[`12_post_examen/QUE_HACE_DESPUES.md`](12_post_examen/QUE_HACE_DESPUES.md) — después de aprobar, qué caminos se abren.

---

## 📊 Lo que ya sabés (mapeo rápido dental → QA)

| Concepto ISTQB | Lo que ya hacés en odontología |
|---|---|
| **Test case** | Protocolo clínico (lista de pasos) |
| **Test plan** | Plan de tratamiento |
| **Defect (bug)** | iatrogenia, fractura de instrumento, necrosis residual |
| **Failure** | Complicación post-operatoria observable |
| **Root cause analysis** | Diagnóstico diferencial |
| **Regression testing** | Control post-operatorio |
| **Acceptance criteria** | Criterios de éxito del tratamiento |
| **User story** | Motivo de consulta |
| **Test data** | Historia clínica + radiografías + modelos |
| **Bug report** | Epicrisis / nota de evolución |
| **Verification** | "¿Hicimos lo que dijimos?" |
| **Validation** | "¿Funciona para el paciente?" |
| **Risk-based testing** | Priorizar por urgencia clínica |
| **Static testing (revisión)** | Revisar la radiografía antes de tratarla |
| **Equivalence partitioning** | Agrupar pacientes por rango etario |
| **Decision table** | Antibiótico si: infección + no alergia + dentro de presupuesto |
| **State transition** | Historia clínica: Borrador → Firmada → Cerrada |
| **Smoke test** | ¿El sillón enciende? |
| **Sanity test** | ¿El nuevo composite polimeriza? |
| **Confirmation test** | El paciente volvió, ¿se resolvió? |
| **Defect density** | Complicaciones / procedimiento |
| **Test harness** | Tu set de instrumental estéril listo |
| **CI/CD** | Tu autoclave valida y no deja avanzar si no llega a temperatura |

---

## ⏱️ Tiempo total estimado

| Fase | Horas |
|---|---|
| Antes de empezar | 0.5 h |
| 6 capítulos (lectura) | ~4 h |
| 6 quizzes | ~3 h |
| Diagnóstico + sample exams | ~5 h |
| Repaso + cheatsheets | ~2 h |
| **Total activo de estudio** | **~15-20 h** |
| **Total incluyendo repaso relajado** | **~25-30 h** |

**A 3-4 horas por semana → 8 semanas. A 1 hora por día → 1 mes.**

---

## 🎯 Para quién es esta guía (específicamente)

**Gaby, esta guía es para vos si:**

- ✅ Sos profesional de la salud con años de experiencia clínica
- ✅ Usás software de gestión clínica a diario (fichas, presupuestos, agenda)
- ✅ Querés entender QA de software desde cero, pero explicándote a vos misma en tu lenguaje
- ✅ Te interesa la calidad, la trazabilidad, y la evidencia (lo aplicás en tu trabajo todos los días)
- ✅ Querés un documento ISTQB CTFL v4.0.1 explicado en español con ejemplos que ya conocés
- ✅ No querés tener que saltar entre 20 carpetas del repo principal — querés una sola guía coherente

**Esta guía NO es para:**

- ❌ Personas que quieren ser QA profesional (eso es un career switch, mirá los packs 19 y 20)
- ❌ Personas que necesitan el syllabus oficial palabra por palabra (eso está en ISTQB.org)
- ❌ Personas que ya saben QA y solo quieren un refresher (eso es la cheatsheet del repo principal)

---

## 📜 Licencia y atribución

- **Esta guía:** MIT (mismo que el repo principal)
- **Material ISTQB oficial:** © ISTQB — esta guía **no redistribuye** el syllabus oficial, solo lo comenta, traduce y explica pedagógicamente con fines educativos
- **Para el syllabus oficial:** [www.istqb.org](https://www.istqb.org)
- **Para rendir en Paraguay:** ASOLINFO (Asociación de Software Libre y Open Source del Paraguay) coordina fechas

---

## 🆘 Soporte

Si te trabás con algún concepto:

1. Releé la cheatsheet del capítulo (1 página)
2. Mirá el quiz — las preguntas往往 aclaran qué era importante
3. Buscá en el [`10_glosario_oficial_istqb/`](10_glosario_oficial_istqb/) el término ISTQB exacto
4. Escribime (Ivan) — pero primero intentá sola, muchas veces el desbloqueo está en la segunda lectura

---

*Hecho con cariño en Asunción. Para Gaby, que después de 20 años de carrera todavía quiere aprender cosas nuevas.*

*Ivan Weiss Van Der Pol — septiembre 2026*
