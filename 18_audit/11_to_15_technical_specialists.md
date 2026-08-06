# Roles 11-15 — Technical Specialists

> **Roles cubiertos:**
> - 11. GitHub Power User (devops-oriented)
> - 12. SEO Specialist
> - 13. Content Writer (technical)
> - 14. UX/UI Designer
> - 15. Backend Dev (static analysis)

## 🔥 Role 11 — GitHub Power User

**Quién es:** Dev senior que mira el repo técnicamente. Evalúa mantenimiento, CI/CD, governance.

### Findings

1. **No hay GitHub Actions / workflows** — `.github/workflows/` no existe. CI/CD = 0.
2. **No hay `CONTRIBUTING.md`** — README lo menciona pero el archivo no existe.
3. **No hay `CODE_OF_CONDUCT.md`** — required for friendly community.
4. **No hay `CHANGELOG.md`** — el repo evolucionó sin track.
5. **No hay release tags / GitHub Releases** — no hay manera de ver versiones.
6. **No hay `SECURITY.md`** — sin disclosure policy.
7. **No hay Dependabot config** — para update de actions.
8. **No hay CODEOWNERS** — sin asignación clara de reviewers.
9. **No hay link checker** — 88+ URLs externos sin validar.
10. **No hay `package.json` / build process** — todo es markdown manual.

### P0 Fixes
- F11.1: Crear `.github/workflows/markdown-lint.yml`
- F11.2: Crear `.github/workflows/link-checker.yml` (weekly)
- F11.3: Crear `CONTRIBUTING.md` raíz
- F11.4: Crear `CODE_OF_CONDUCT.md` raíz
- F11.5: Crear `SECURITY.md`
- F11.6: Crear `CHANGELOG.md` (con retroactivo)
- F11.7: Crear GitHub Releases v0.1, v0.2, v0.3, v1.0

### P1 Fixes
- F11.8: Configurar Dependabot
- F11.9: Crear CODEOWNERS
- F11.10: Habilitar GitHub Discussions

---

## 🔥 Role 12 — SEO Specialist

**Quién es:** Especialista que evalúa cómo se encuentra el repo en Google / GitHub search.

### Findings

1. **README raíz no tiene description optimizada** — no aparece en "ISTQB CTFL prep" search.
2. **No hay GitHub social preview image** — share links sin imagen.
3. **Repo name "istqb-prep-v4"** es OK pero "istqb-ctfl-foundation-v4" sería mejor.
4. **No hay topics tags** — `istqb`, `ctfl`, `qa`, `paraguay`, `study-material` faltan.
5. **No hay "About" section** — descripción del repo vacía.
6. **No hay keywords en el repo** — falta `description` en metadata.
7. **No hay issues pinned** — para mantener issues importantes visibles.
8. **No hay Discussions** — para Q&A (mejora SEO).
9. **Algunos archivos tienen nombres con guiones bajos vs guiones** — inconsistencia (`istqb_py_grupos_wa.md` vs `00_README/`).
10. **URLs de archivos son largas** — afecta shallow indexing.

### P0 Fixes
- F12.1: Agregar GitHub repo description: "ISTQB CTFL v4.0.1 prep hub — study plan, sample exams, flashcards, career guidance. Spanish LATAM (Paraguay)."
- F12.2: Agregar topics: `istqb`, `ctfl`, `qa`, `testing`, `paraguay`, `study-material`, `certification`, `spanish`
- F12.3: Crear social preview image (1280x640)
- F12.4: Renombrar repo a `istqb-ctfl-prep-v4` (más keyword-rich)

### P1 Fixes
- F12.5: Pin 3 issues importantes
- F12.6: Habilitar Discussions
- F12.7: Estandarizar naming (todos con guiones, no guiones bajos)

---

## 🔥 Role 13 — Content Writer / Editor

**Quién es:** Editor profesional que evalúa la calidad del contenido.

### Findings

1. **Tono inconsistente** — algunos archivos son súper formales, otros informales (ej: `06_practice_tests/sample_exam_A.md` vs `00_README/README.md`).
2. **Voice inconsistente** — a veces "tú", a veces "vos", a veces "usted". Mezcla con inglés.
3. **Errores tipográficos** — buscar `grep` para typos comunes (`a ver`, `haber`, etc).
4. **Estructura inconsistente** — algunos archivos tienen TOC, otros no.
5. **Longitud inconsistente** — algunos archivos son 1KB, otros 21KB.
6. **Repetición** — mismo concepto explicado en 3 lugares distintos.
7. **Markdown inconsistente** — algunas listas con `-`, otras con `*`.
8. **Sin "Edit history" / versiones** — sin clarity de cuándo se actualizó qué.
9. **Disclaimer placement inconsistente** — algunos al inicio, otros al final.
10. **Bilingual headers** — algunos archivos usan "Cap" (en español) otros "Chapter" (en inglés).

### P0 Fixes
- F13.1: Crear `STYLE_GUIDE.md` con:
  - Voice: español Paraguay "vos" consistente
  - Tono: profesional pero accesible
  - Markdown: usar `-` para listas
  - Headers: español consistente
- F13.2: Spell-check + grammar-check todo el repo
- F13.3: Estandarizar estructura de cada archivo

### P1 Fixes
- F13.4: Editor humano (no IA) para QA final
- F13.5: Glossary de términos (decidir ISTQB vs inglés)

---

## 🔥 Role 14 — UX/UI Designer

**Quién es:** Diseñador que evalúa cómo se "ve" el repo y la experiencia de navegación.

### Findings

1. **README es solo texto** — sin imágenes, diagramas, ni visual hierarchy claro.
2. **17 directorios sin nav graph visual** — un mapa mental sería útil.
3. **Emoticons como jerarquía** — los emojis definen visual hierarchy, no headers estructurados.
4. **Sin callouts / cards** — todo es prosa plana.
5. **ASCII art en cheat sheets** — funciona pero no es scalable a mobile/print.
6. **Sin dark mode** — el repo se ve igual en light/dark.
7. **GitHub Pages no activado** — sin sitio navegable.
8. **Sin iconografía consistente** — cada autor usa emojis diferentes.
9. **Sin visual flowchart** del proceso de estudio.
10. **Sin progress bar / completion indicator** — feedback visual de avance.

### P0 Fixes
- F14.1: Crear visual nav graph (diagrama) en `00_README/`
- F14.2: Estandarizar emojis (≤3 emojis por archivo)
- F14.3: Crear ASCII flowchart del proceso de estudio

### P1 Fixes
- F14.4: Activar GitHub Pages con sitio navegable
- F14.5: Generar SVG icons custom (no emoji)
- F14.6: Diseñar progress bar interactivo

---

## 🔥 Role 15 — Backend Dev (static analysis)

**Quién es:** Dev que mira la "infra" del repo (markdown linting, file structure, etc).

### Findings

1. **No hay `.markdownlint.json`** — para validar estilo consistente.
2. **No hay `pre-commit` config** — sin validación antes de commit.
3. **No hay `mkdocs.yml` ni similar** — no se puede generar docs automáticamente.
4. **No hay `_config.yml` para Jekyll** — no hay GitHub Pages integrado.
5. **`.gitignore` minimalista** — solo `.DS_Store`, `*.swp`, etc. Falta `.venv/`, `node_modules/` etc (aunque repo no tiene código).
6. **No hay schema validation** — para archivos CSV (flashcards).
7. **No hay tests automatizados** — para verificar que los quizzes tienen respuestas.
8. **No hay tooling para validar que links internos funcionan** — riesgo de links rotos en reorganización.
9. **No hay `Makefile` o `justfile`** — comandos para rebuild no existen.
10. **No hay `Dockerfile`** — para correr el repo en container (no aplica pero igual).

### P0 Fixes
- F15.1: Crear `.markdownlint.json` con rules
- F15.2: Crear GitHub Action que corre markdownlint
- F15.3: Crear Python script que valida que todos los sample exams tienen answer keys
- F15.4: Crear GitHub Action que valida links internos

### P1 Fixes
- F15.5: Configurar mkdocs.yml (o docusaurus)
- F15.6: Crear pre-commit config
- F15.7: Schema JSON para flashcards CSV

---

## 📊 Resumen Roles 11-15

| Rol | # P0 fixes | # P1 fixes |
|---|---|---|
| 11 (GitHub Power User) | 7 | 3 |
| 12 (SEO) | 4 | 3 |
| 13 (Content Writer) | 3 | 2 |
| 14 (UX/UI Designer) | 3 | 3 |
| 15 (Backend Dev) | 4 | 3 |
| **Total** | **21** | **14** |

## 🔗 Conecta con

- Theme 6 (Contribuir es Ambigüo) — F11.3, F11.4
- Theme 5 (Falta Index) — F14.1
- Theme 8 (Falta Mantenimiento Continuo) — F11.6, F11.7
