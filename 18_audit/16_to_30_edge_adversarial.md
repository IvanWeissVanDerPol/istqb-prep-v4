# Roles 16-30 — Edge Cases + Adversariales

> Compactly formatted findings para roles 16-30.

---

## 🔥 Role 16 — Mobile User

1. **No mobile-optimized rendering** — el README raíz (12KB+) es overwhelming en mobile.
2. **Tablas anchas** (Careers sample) requieren scroll horizontal.
3. **Emojis grandes** no son friendly en mobile.
4. **Sin app / PWA** — todo es web.
5. **Pin to home screen** no es trivial.

**P0:** Responsive testing — validar mobile rendering.

---

## 🔥 Role 17 — Screen Reader User (Accessibility)

1. **Emojis sin alt text** — screen readers leen literalmente.
2. **Imágenes / diagramas sin alt** — si los hubiera.
3. **Tables without proper `<thead>` / `<th>`** — afecta navegación.
4. **Color coding** sin texto alternativo (no aplica porque todo es texto).
5. **Long lines without paragraph breaks** — hard to follow.

**P0:** Revisar accesibilidad básica. No emoji-only headings.

---

## 🔥 Role 18 — Non-Native English Speaker

1. **Sample exams en español, plan en español, README en español.** ✓
2. **Pero**: research links mostly in English.
3. **Glosario mezcla español + inglés** — términos ISTQB oficiales en inglés.
4. **Sin traducción formal al inglés del contenido.**
5. **Jerga ISTQB oficial en inglés** — útil pero confuso.

**P0:** Documentar decisión: español primary, inglés solo cuando es ISTQB oficial.

---

## 🔥 Role 19 — Power User (Week 8, ya casi rindiendo)

1. **Querría ver: total preguntas rendidas, scores históricos, comparación.**
2. **Querría ver: weakest LOs across all practice.**
3. **Querría: random quiz generator** (sample each time).
4. **Querría: timed mode with audio alert.**
5. **Querría: import progress from CSV.**

**P0:** Generador de quiz aleatorio (Python script).

---

## 🔥 Role 20 — New Team Member (contributor)

1. **CONTRIBUTING.md ✓ (lo agregamos).**
2. **Pero**: sin "good first issue" labels.
3. **Sin "help wanted" issues.**
4. **Sin "good first PR" examples.**
5. **Sin onboarding doc** — how to add a new quiz, summary, etc.

**P0:** Crear onboarding doc + issue labels.

---

## 🔥 Role 21 — Competitor (other ISTQB repo)

1. **Otros repos compiten por tráfico / stars.**
2. **bloomikko/ISTQB-CTFL-V4.0** (16 stars) — competing directly.
3. **lucas-alexandrino/ISTQB-CTFL** — en portugués.
4. **No hay diferenciación clara** vs ellos.
5. **No hay partnerships**.

**P1:** Identificar diferenciación (LATAM focus, comprehensive, Spanish).

---

## 🔥 Role 22 — Troll / Hater

1. **Trolls podrían crear issues SPAM.**
2. **Trolls podrían plagiar contenido.**
3. **Trolls podrían demandar DMCA falso.**
4. **CODE_OF_CONDUCT ✓** da base legal para ban.
5. **Pero**: sin moderation policy explícita.

**P0:** Política de moderación (en CONTRIBUTING).

---

## 🔥 Role 23 — Plagiarist

1. **Contenido es MIT licensed** — plagiar es legal si da attribution.
2. **Pero**: muchos copian sin attribution.
3. **ISTQB podría demandar si extractos del syllabus.**
4. **Disclaimer ✓ reduce riesgo.**
5. **Pero**: sin monitoring de plagio.

**P1:** Monitoring de plagio (manual).

---

## 🔥 Role 24 — Scraper (training data)

1. **El repo es público — scraping legal.**
2. **IA training data scrape es legal en mayoría de jurisdicciones.**
3. **No hay opt-out** (`robots.txt` no aplica en GitHub).
4. **No hay LICENSE custom que restrinja AI training.**
5. **No hay "do not use for AI" notice.**

**P3:** Decisión personal — ¿importa? Probablemente no.

---

## 🔥 Role 25 — Spam Bot

1. **GitHub issues son vectores de spam.**
2. **Templates de issue ayudan a filtrar.**
3. **Sin templates → spam entra.**
4. **GitHub tiene filtros built-in.**
5. **Pero**: sin CODEOWNERS, no hay triage automático.

**P0:** Crear issue templates.

---

## 🔥 Role 26 — Hacker

1. **Repo público sin secretos** — bueno.
2. **GitHub Actions futuras podrían tener secrets.**
3. **No hay SECURITY.md** — disclosure policy.
4. **No hay Dependabot** — para update actions.
5. **No hay signed commits**.

**P0:** SECURITY.md.

---

## 🔥 Role 27 — Lawyer (ISTQB IP)

1. **"ISTQB" es marca registrada.**
2. **"CTFL" es trademark.**
3. **El repo los usa extensamente.**
4. **Disclaimer "not affiliated" ✓ reduce riesgo.**
5. **Pero**: si ISTQB pide cambio, ¿qué pasa?

**P0:** Trademark policy explícito.

---

## 🔥 Role 28 — Diplomat / International Body

1. **El repo es LATAM-focused pero global accessible.**
2. **No hay version i18n formal.**
3. **ASOLINFO PY mención, pero no Brasil, no Argentina.**
4. **Podría expandirse a global.**
5. **Pero**: scope creep.

**P2:** Roadmap expansion to other LATAM countries.

---

## 🔥 Role 29 — Future Maintainer (6 months later)

1. **CHANGELOG.md ✓ (lo agregamos).**
2. **Pero**: sin ARCHITECTURE.md — decisiones de diseño no documentadas.
3. **Sin "intent of repo" doc** — ¿cuál es la misión?
4. **Sin "future direction"** — ¿qué sigue?
5. **Sin transfer plan** — si Ivan deja de mantener.

**P0:** ARCHITECTURE.md + ROADMAP.md.

---

## 🔥 Role 30 — Random Visitor (Google Search)

1. **Si buscan "ISTQB CTFL Paraguay"** → encuentran el repo.
2. **Si buscan "ISTQB prep español"** → probablemente encuentran primero bloomikko (16 stars) por SEO.
3. **Si buscan "QA jobs Paraguay"** → no encuentran.
4. **El repo es descubrible pero no prominente.**
5. **Sin backlinks**, sin presencia en redes, sin SEO agresivo.

**P1:** SEO improvement + social presence.

---

## 📊 Resumen Roles 16-30

| Rol | Severidad principal |
|---|---|
| 16 Mobile | P2 |
| 17 Accessibility | P1 |
| 18 Non-native | P0 (jargon mix) |
| 19 Power User | P1 |
| 20 New Member | P0 (issues setup) |
| 21 Competitor | P1 |
| 22 Troll | P0 (moderation) |
| 23 Plagiarist | P1 |
| 24 Scraper | P3 |
| 25 Spam | P0 |
| 26 Hacker | P0 |
| 27 Lawyer | P0 |
| 28 Diplomat | P2 |
| 29 Future Maintainer | P0 |
| 30 Random Visitor | P1 |
