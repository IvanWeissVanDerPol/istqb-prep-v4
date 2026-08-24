# 🔗 Skill Transfer Map — De Luana intérprete/CM a Luana QA

> **Para qué sirve este archivo:** Cada Learning Objective del ISTQB CTFL v4.0.1 está mapeado a una experiencia REAL tuya. Cuando estudies un LO, abrí este archivo y mirá la columna "Tu experiencia equivalente". Vas a ver que el ISTQB no te pide nada que no hagas ya.

---

## 📚 Cómo leer este archivo

Cada fila tiene:

| Columna | Qué contiene |
|---|---|
| **LO ISTQB** | El código oficial (ej: 1.2.3) y nombre del objetivo |
| **Concepto** | Lo que el examen te pide que sepas hacer |
| **Tu experiencia** | El momento de tu CV donde YA hacías esto |
| **Skill transfer** | Una frase que conecta los dos mundos |
| **Truco mnemónico** | Una pista para que te acuerdes en el examen |

---

## 📘 Capítulo 1 — Fundamentals of Testing (14 LOs)

| LO | Concepto | Tu experiencia | Skill transfer | Truco mnemónico |
|---|---|---|---|---|
| **1.1.1** | Identificar objetivos típicos del testing | Reportes semanales de Language Line (cumplimiento, métricas) | Ya reportabas objetivos cumplidos a tu supervisora | "El testing es reportar qué pasa, no arreglar" |
| **1.1.2** | Diferenciar testing de debugging | Cuando vos detectabas un error en una traducción, pero el fix lo hacía otra persona | Testing = vos detectás. Debugging = otro corrige | "Yo encuentro, otro arregla" |
| **1.2.1** | Ejemplificar por qué el testing es necesario | Atrapar errores médicos graves antes de que lleguen al paciente | **Vos literalmente prevenías daños médicos con tu oído** | "Testing salva vidas, igual que la interpretación médica" |
| **1.2.2** | Recordar relación testing vs QA (aseguramiento) | Como Community Manager, tu rol era **calidad** (estrategia); las ejecutoras eran otras | QA = estrategia. Testing = ejecución | "CM hace la estrategia; las personas del equipo ejecutan" |
| **1.2.3** ⭐ | Distinguir root cause / error / defect / failure | Cuando un doctor se equivocaba en una instrucción (root cause), vos interpretabas mal (error), salía defectuosa la comunicación (defect), y el paciente se confundía (failure) | La cadena completa: humano → transmisión → salida → impacto | "Médico-error-usted-comunicación-paciente" |
| **1.3.1** ⭐⭐ | Explicar los 7 principios del testing | Psicología + interpretación te dieron todo esto. Los siete principios son sentido común para vos. | Ver tabla expandida más abajo | "Siete principios = siete intuiciones" |
| **1.4.1** | Explicar actividades y tareas de testing | Planning → ejecución → reporte → cierre. Exactamente igual que organizar una campaña en redes. | Campaña CM = ciclo de testing | "Sprint = campaña; release = post publicado" |
| **1.4.2** | Impacto del contexto en el proceso | Médico ≠ bancario ≠ legal. Cada contexto cambia tu terminología y tu tono. | Domain-driven testing | "El contexto cambia el idioma, cambia el test" |
| **1.4.3** | Diferenciar testware (artefactos de testing) | Tenés: plan de contenido, calendario de posts, copies aprobados, métricas de engagement. Todos son **artefactos**. | CM produce artefactos todo el día | "Calendario editorial = test plan" |
| **1.4.4** ⭐ | Valor de la trazabilidad | Cuando agendabas una consulta → confirmación → recordatorio → consulta efectiva. Cada paso con su evidencia. | Trazabilidad = cadena de evidencia | "Cada paso留下 un registro" |
| **1.4.5** | Roles en testing (tester, dev, PM, etc.) | Trabajabas con: médicos, devs de comunidad, coordinadores, pacientes. Sabés cómo cada uno piensa distinto. | Multi-stakeholder navigation | "Stakeholder ≠ stakeholder ≠ stakeholder" |
| **1.5.1** | Generic skills del tester | Atención al detalle, comunicación, pensamiento crítico, trabajo en equipo, organización | Todo esto lo listaste en tu CV | "Skills blandos = superpoder QA" |
| **1.5.2** | Whole team approach | En Clínica Kunu'u, vos no eras solo secretaria: eras community manager + traductora + intérprete + atención al cliente. **Whole team en una persona.** | Sos el whole team embodied | "Yo era whole team antes de saber el nombre" |
| **1.5.3** ⭐ | Beneficios / drawbacks de independencia | Cuando eras la única intérprete, no había peer review. Riesgo alto. Cuando había equipo (Somosgay), había校对. | Independencia mejora el testing | "Más ojos = menos errores" |

### Tabla expandida: Los 7 principios (LO 1.3.1) traducidos a tu vida

| # | Principio | Cómo lo viviste | Cómo lo escribís en el examen |
|---|---|---|---|
| 1 | Testing shows presence of defects, not their absence | Por más perfecta que sea tu interpretación, siempre puede haber un error que se te escapó | "Testing muestra presencia de defectos, no su ausencia" |
| 2 | Exhaustive testing is impossible | Nunca vas a traducir todas las frases que un médico puede decir | "El testing exhaustivo es imposible en la práctica" |
| 3 | Early testing saves time and money | Cuando preguntabas al médico ANTES de interpretar, ahorrabas tiempo | "Testear temprano (shift-left) ahorra tiempo y dinero" |
| 4 | Defects cluster together | Si un doctor tiene un acento difícil, sus errores se repiten; no están distribuidos | "Los defectos se agrupan (cluster)" |
| 5 | Beware of the pesticide paradox | Si usás siempre las mismas técnicas de interpretación, los defectos viejos se esconden y aparecen nuevos | "El testing repetitivo pierde efectividad" |
| 6 | Testing is context dependent | Una interpretación legal no se testea igual que una médica | "El testing depende del contexto" |
| 7 | Absence-of-defects is a fallacy | Una traducción perfecta técnicamente puede ser culturalmente ofensivo. Sin usability testing, el defecto está | "Ausencia de errores ≠ calidad" |

> 🎯 **Dato clave:** Los 7 principios vienen en al menos 1 pregunta del examen oficial. Memorizalos con tu historia personal, no como lista muerta.

---

## 📗 Capítulo 2 — Testing Throughout the SDLC (10 LOs)

| LO | Concepto | Tu experiencia | Skill transfer | Truco mnemónico |
|---|---|---|---|---|
| **2.1.1** | SDLC impact on testing | Clínica Kunu'u tenía su propio ciclo: captación → consulta → seguimiento. Cada fase requería testing distinto | Software tiene fases; cada fase necesita testing | "Fase ≠ fase" |
| **2.1.2** | Good testing practices for all SDLCs | Hacer reportes claros SIEMPRE, sin importar el cliente | Practices universales | "Reportes claros: regla de oro" |
| **2.1.3** ⭐ | Test-first approaches (BDD/TDD/ATDD) | Cuando preparabas un guion ANTES de la transmisión en vivo (test-first). El guion era tu "test" | "Test first" no es nuevo; vos lo hacías con guiones | "Guion = test" |
| **2.1.4** ⭐ | DevOps impact on testing | Live talks transmitidos sin pausa. Iteración rápida = necesitas testing continuo | **Live production = DevOps en esteroides** | "Live stream = CI/CD de contenido" |
| **2.1.5** ⭐⭐ | Shift left (testing temprano) | Vos detectabas ambigüedades ANTES de traducir. Esto es shift-left puro | Prevención >> corrección | "Preguntar ANTES = shift-left" |
| **2.1.6** ⭐ | Retrospectives | Al final de cada campaña, analizabas: qué funcionó, qué no, qué ajustar | **Vos hacías retrospectives en cada post-mortem de campaña** | "Post-campaña = retrospective" |
| **2.2.1** ⭐ | Test levels (unit/integration/system/acceptance) | Niveles de testing = niveles de revisión. Vos revisabas: copia → diseño → campaña → resultado final | Cuatro niveles = cuatro checkpoints | "C-I-S-A = Creación-InSpección-Salida-Approved" |
| **2.2.2** ⭐ | Test types (functional/non-functional/white-box/black-box) | Una cosa es que la traducción sea correcta (functional); otra es que suene natural (usability = non-functional) | Funcional vs no funcional | "Correcto vs bueno" |
| **2.2.3** ⭐⭐ | Confirmation vs regression | Confirmation = "el fix funcionó?". Regression = "el fix rompió otra cosa?". | Hiciste esto cada vez que el médico se autocorregía a media interpretación | "Confirmation = '¿arreglé?'; Regression = '¿rompí otra cosa?'" |
| **2.3.1** | Maintenance testing | Cuando cambiaba una policy de la clínica, vos actualizabas todos los materiales (testing de mantenimiento) | "Cambió la regla → cambiaron los materiales" | "Cambio = re-test obligatorio" |

---

## 📙 Capítulo 3 — Static Testing (8 LOs)

> **Cap 3 es donde más brillás.** El static testing es revisar artefactos sin ejecutar el sistema. Vos hacías esto CADA DÍA como Translation Officer.

| LO | Concepto | Tu experiencia | Skill transfer | Truco mnemónico |
|---|---|---|---|---|
| **3.1.1** ⭐ | Work products que se pueden revisar | En Somosgay revisabas: PRDs, copies, contratos, propuestas. **Todos son work products revisables.** | Tu trabajo era 100% static testing | "Todo documento = work product" |
| **3.1.2** | Valor del static testing | Encontrabas errores de redacción ANTES de publicar (ahorrabas crisis de reputación) | Prevenir es más barato que apagar incendios | "Revisar antes = crisis prevented" |
| **3.1.3** ⭐ | Static vs dynamic testing | Static = revisar copy antes de publicar. Dynamic = probar el link de la campaña después de publicar | Static ANTES, dynamic DURANTE | "Static sin ejecutar, dynamic ejecutando" |
| **3.2.1** | Beneficios de feedback temprano | Cuando pedías feedback del copy a la coordinadora antes de publicar, evitabas retrabajo | Loop corto = calidad alta | "Feedback temprano = menos retrabajo" |
| **3.2.2** ⭐ | Proceso de review (planning → kickoff → individual prep → review meeting → rework → follow-up) | Tu flujo de revisión de documentos: brief → individual review → meeting → edición → aprobación | **Esto es EXACTAMENTE el proceso de review formal** | "Tu proceso editorial = proceso ISTQB" |
| **3.2.3** ⭐ | Roles en review (author/moderator/reviewer/scribe/manager) | Vos eras el **reviewer** principal. La coordinadora era el **manager**. El autor era quien escribió el copy | Mapeo 1:1 | "Vos = reviewer" |
| **3.2.4** ⭐ | Tipos de review (walkthrough/technical/inspection) | Walkthrough = explicar el documento al equipo. Technical review = revisar gramática/estilo. Inspection = buscar defectos formales. | Hiciste las tres, solo que no las llamabas así | "Tres nombres, tres profundidades" |
| **3.2.5** | Factores de éxito de un review | Checklist, foco, ambiente seguro, datos, capacitación | Tu checklist de revisión tenía todo esto implícito | "Buena review = checklist + tiempo + respeto" |

---

## 📕 Capítulo 4 — Test Analysis & Design (14 LOs) — EL MÁS PESADO

> **Este es el capítulo de 30% del examen.** Acá hay técnica pura. La buena noticia: muchas de estas técnicas son **lo que hacías intuitivamente como intérprete y CM**. Solo hay que ponerles nombre.

| LO | Concepto | Tu experiencia | Skill transfer | Truco mnemónico |
|---|---|---|---|---|
| **4.1.1** | Black-box / white-box / experience-based | Black-box = traducir sin saber por qué el médico dice eso. White-box = entender el sistema. Experience-based = saber que el doctor X suele equivocarse en estos términos. | **Hiciste las tres en cada llamada** | "Tres sombreros" |
| **4.2.1** ⭐⭐⭐ | **Equivalence Partitioning (EP) K3** | Agrupar inputs que se comportan igual. Edad para votar: 18-65 = un grupo válido; -5 inválido; 100 inválido. Cada grupo → un test. | En interpretación, agrupabas terminología por dominio: cardiológica vs neurológica vs administrativa | "Cada grupo = 1 test" |
| **4.2.2** ⭐⭐⭐ | **Boundary Value Analysis (BVA) K3** | Los defectos ocurren en los BORDES. Edad 17 / 18 / 65 / 66. | Cuando un doctor pasaba de una sección a otra del formulario, vos **revisabas los bordes** (datos límites: 0, 999, etc.) | "Bordes, bordes, bordes" |
| **4.2.3** ⭐⭐ | **Decision Table Testing K3** | Tabla de combinaciones: UserOK + PasswordOK → Login. UserOK + PassFail → Reintentar. Etc. | **Tablas de decisión para decidir si una consulta requería intérprete o no (idioma, urgencia, complejidad)** | "Combinaciones → acciones" |
| **4.2.4** ⭐⭐ | **State Transition Testing K3** | Diagramas de estados: PENDIENTE → EN_REVISIÓN → APROBADO → PUBLICADO. Cada flecha es una transición. | Tus posts pasaban por: draft → revisión → aprobado → publicado → archivado. **Cada flecha = un test** | "Estados + flechas" |
| **4.3.1** | Statement testing (cobertura) | Cobertura = % de líneas de código ejecutadas por tests | No es exactamente lo que hacías, pero conceptualmente es "qué porcentaje del documento fue revisado" | "Cuánto cubriste?" |
| **4.3.2** | Branch testing (cobertura de ramas) | Cobertura de "ifs" del código. Si tuvieras "si es urgente, llamar ahora; si no, agendar", ambas ramas deben testearse. | Para cada decisión, testeás cada rama | "Cada IF = una rama testeada" |
| **4.3.3** | Valor de white-box testing | Testear desde dentro del código (el dev lo hace). Saber cómo funciona el sistema por dentro | Cuando entendías el sistema médico (no solo las palabras) | "Conocer el sistema = mejor testing" |
| **4.4.1** | Error guessing | Intuir dónde están los bugs sin técnica formal. "Si meto -5, seguro rompe" | **Vos intuías términos problemáticos** sin tener una lista formal | "Intuición de errores" |
| **4.4.2** | Exploratory testing | Probar libremente, sin script | Cuando entrabas a un nuevo cliente sin brief completo y explorabas qué necesitaba | "Exploración sin mapa" |
| **4.4.3** | Checklist-based testing | Lista de cosas a verificar | Tu checklist de revisión de documentos | "Lista en mano" |
| **4.5.1** ⭐ | User stories (NUEVO v4.0) | "Como [usuario], quiero [acción], para [beneficio]" | **Lo hacías como CM:** "Como paciente nueva, quiero agendar online, para no llamar" | "Usuario + acción + valor" |
| **4.5.2** ⭐ | Acceptance criteria (NUEVO v4.0) | Given/When/Then o lista de bullets | **Briefs que escribías para clientes o coordinadores** | "Criterios claros = criterios aceptables" |
| **4.5.3** ⭐⭐ | **ATDD K3 (NUEVO v4.0)** | Acceptance Test-Driven Development: tests se escriben ANTES del código, basados en acceptance criteria | Brief → criterios → tests → desarrollo. **Tu flujo editorial de campaña** | "Criterios antes de código" |

---

## 📒 Capítulo 5 — Managing Test Activities (16 LOs)

> **Acá también brillás.** Gestión pura. Project management + reporting + comunicación = tu vida diaria como Executive Secretary + CM.

| LO | Concepto | Tu experiencia | Skill transfer | Truco mnemónico |
|---|---|---|---|---|
| **5.1.1** | Test plan content | Plan = alcance, enfoque, recursos, cronograma, riesgos | **Tu plan de campaña CM tenía todo esto** | "Plan = plan, en cualquier idioma" |
| **5.1.2** | Tester value in planning | El tester informa si los criterios son testables | Vos advertías si un brief era ambiguo o vago | "Tester = detector de ambigüedad" |
| **5.1.3** ⭐ | Entry vs exit criteria | Entry = "empezamos porque X está listo". Exit = "terminamos porque Y está completo" | Cuando abrías una campaña (entry) y la cerrabas con métricas (exit) | "Entrada vs salida" |
| **5.1.4** ⭐ | Estimation techniques K3 | Estimar esfuerzo: expert opinion, analogy, planning poker | Tus estimaciones de tiempo de interpretación por minutos | "Estimar es adivinar con método" |
| **5.1.5** ⭐ | Test case prioritization K3 | Qué testear primero cuando no hay tiempo para todo | Cuando priorizabas: primero urgencias, después consultas regulares, después seguimientos | "Primero lo crítico" |
| **5.1.6** ⭐ | **Test pyramid (NUEVO)** | Unit (70%) / Integration (20%) / E2E (10%) | En tu trabajo: muchos mensajes cortos (unit), algunas conversaciones (integration), pocas sesiones largas (E2E) | "70-20-10" |
| **5.1.7** ⭐ | **Testing quadrants (NUEVO)** | 2x2: Q1 funcional vs Q2 no-funcional / Q3 business vs Q4 tech-facing | **No lo hacías directamente, pero es el marco para categorizar tests** | "Q1-Q4" |
| **5.2.1** ⭐ | Risk = Likelihood × Impact | Multiplicación simple. Alto × Alto = crítico | "Riesgo = probabilidad × daño" | "L × I" |
| **5.2.2** ⭐⭐ | Project risks vs product risks | Project = retrasos, presupuesto. Product = funcionalidad, calidad. | "Project = logística; Product = el producto mismo" | "Proyecto ≠ producto" |
| **5.2.3** | Risk analysis influence | Lo que testeás más depende del riesgo | Más riesgo = más tests | "Riesgo dirige esfuerzo" |
| **5.2.4** | Medidas para product risks | Mitigar, transferir, aceptar, evitar | Lo mismo que cualquier plan de contingencia | "M-T-A-E" |
| **5.3.1** | Métricas de testing | % ejecutado, % pasado, defectos encontrados | Engagement, alcance, conversión en tus métricas CM | "Números cuentan historias" |
| **5.3.2** | Test reports purposes/audiences | Por qué y para quién | Tus reportes tenían destinatarios distintos (coordinadora, cliente, equipo) | "Reporte ≠ reporte" |
| **5.3.3** | Communicating testing status | Cómo comunicar avance, blockers, riesgo | Tus status updates semanales | "Status = claridad" |
| **5.4.1** | Configuration management support | Versionar documentos, code, tests | Cuando versionabas copies en Google Drive | "Versionar todo" |
| **5.5.1** ⭐⭐ | **Defect report K3** | Estructura: ID, título, severity, priority, steps, expected, actual, environment | **Lo hacías como intérprete al reportar a tu supervisora** | "Reporte claro = fix rápido" |

### Componente estrella: Defect Report (LO 5.5.1) — cómo Luana lo hacía sin saberlo

Tu reporte cuando algo no funcionaba en una llamada era:

| Campo ISTQB | Tu reporte real (en Language Line) |
|---|---|
| **ID** | ID de ticket interno |
| **Title** | "Conflicto de terminología con paciente cardiológico en llamada 4521" |
| **Severity** | (no existía, pero si lo hubiera sido) Alta — afectó comunicación clínica |
| **Priority** | Alta — llamada en vivo, no esperaba |
| **Steps to reproduce** | 1. Llamada entra 2. Paciente describe dolor torácico 3. Doctor usa término "angina" 4. Glosario no tenía equivalente 5. Confusión |
| **Expected** | Glosario incluía "angina" |
| **Actual** | Glosario desactualizado |
| **Environment** | Sistema LLS v3.2.1, navegador Chrome, internet estable |

**Eso es un ISTQB-compliant defect report. Literal. Solo te faltaba el título "QA" encima.**

---

## 📓 Capítulo 6 — Test Tools (2 LOs)

| LO | Concepto | Tu experiencia | Skill transfer | Truco mnemónico |
|---|---|---|---|---|
| **6.1.1** | Tipos de herramientas de testing | Test management (TestRail), defect tracking (Jira), automation (Selenium), performance (JMeter) | En CM usabas: Meta Business Suite (gestión), Canva (diseño), Google Drive (versión), Trello/Asana (planning) | "Tus herramientas = QA tools" |
| **6.2.1** | Beneficios y riesgos de automation | Automation = rápido, repetible, sin fatiga. Riesgos = inversión inicial, falsos positivos, mantenimiento. | Manual vs automático en redes: post manual vs scheduling automático | "Rápido pero caro al inicio" |

---

## 🎯 Resumen ejecutivo del skill transfer

| Tu superpoder | LOs que tenés cubiertos casi sin estudiar |
|---|---|
| Intérprete médica | 1.2.3, 2.2.3, 5.5.1, 4.4.1 |
| Community Manager | 1.4.3, 2.1.6, 2.2.2, 5.3.2, 5.3.3, 6.1.1 |
| Translation Officer | 3.1.1, 3.1.2, 3.1.3, 3.2.2, 3.2.4 |
| Executive Secretary | 5.1.3, 5.1.5, 5.4.1, 5.5.1 |
| Psicología (5 semestres) | 1.3.1, 1.4.5, 1.5.1 |
| Trilingüe | Acceso a mercados EN, ES, PT (US, LATAM, Brasil) |

**Lectura honesta:** Estudiar este examen para vos es, en el 70% del syllabus, **aprender el nombre técnico de algo que ya hacés**. El 30% restante (Cap 4, técnicas formales) requiere práctica con lápiz y papel. El plan de 8 semanas lo refleja.

---

## 📂 Siguiente archivo

→ [`../02_study_plan/PLAN_PARA_LUANA.md`](../02_study_plan/PLAN_PARA_LUANA.md) — el plan de 8 semanas ajustado a tu disponibilidad real y priorizando los LOs donde tenés que practicar más.

*Si encontrás un LO donde no te sentís identificada, anotalo y me lo decís. Hay una chance de que mi mapeo esté incompleto — vos conocés tu experiencia mejor que yo.*
