# 🔥 Role 1 — First-Time Student from Google

**Quién es:** Llega al repo desde búsqueda Google ("ISTQB CTFL prep"). Lee README raíz por 30 segundos.

## 🎯 Lo que quiere

- Entender QUÉ es este repo en 30 segundos
- Saber si vale la pena hacer fork/clone
- Encontrar el "Quick start" obvio
- Empezar a estudiar

## ❌ Findings con evidencia

1. **`README.md` línea 1-12** tiene 12KB y empieza con emoji-heavy title + 6 metadata lines. Es front-loaded. Un first-timer no sabe si esto es para él.

2. **`README.md` líneas 11-12** — el "Quick start" tiene 11 items. Demasiado para 30 segundos.

3. **`README.md` línea 3-4** — emojis + 6 metadata lines (📅, 📅, 📅, 🌐, ⭐). Looks like infomercial.

4. **`00_README/README.md`** — existe un sub-README. ¿Por qué? Si duplica el root, es ruido.

5. **No hay badges** — nada que indique "MIT licensed", "v4.0.1", "last updated".

6. **No hay "60-second elevator pitch"** al inicio. ¿Qué es esto? ¿Para quién? ¿Qué gano?

7. **No hay TOC / nav graph** — el primer vistazo ve "17 directorios" sin mapa.

8. **README línea 14** dice "Quick start (10 min reading, 8 weeks studying)" pero los 11 items no son 10 min.

9. **No hay live demo / preview image** — no podés "ver" qué hay adentro sin clonar.

10. **`DEPLOY_COMMANDS.md` en raíz** — un first-timer lo ve y piensa "¿es para mí?". No, es para mantener el repo.

11. **Línea 13** — "Quick start" mezcla setup, study plan, career advice. Tres cosas distintas en un solo listado.

12. **No hay "What this is NOT"** — un first-timer podría creer que pasar CTFL = job garantizado.

13. **El repo dice "v4.0.1" pero no hay GitHub release** — no podés confirmar que está al día.

14. **No hay CHANGELOG** — no sabés qué cambió desde la última versión.

## 🔥 P0 Fixes

### F1.1: Agregar "60-second elevator pitch"

Al inicio del README raíz, ANTES de emojis:

```markdown
## 🎯 En 60 segundos

ISTQB CTFL es la certificación internacional más reconocida para testers.
Pasar el examen te abre puertas a trabajos QA mejor pagos (USD 24-48K+ remoto LATAM).

Este repo te da todo lo necesario para pasar:
- 8 semanas de plan de estudio
- Sample exams cronometrados
- Flashcards Anki
- Quizzes por capítulo

Empezá por: [`01_plan_estudio/`](01_plan_estudio/) (el plan)
```

### F1.2: Quitar o diferenciar `00_README/`

Opción A: Borrar `00_README/README.md`. El README raíz es suficiente.
Opción B: Moverlo a `00_README/overview.md` y diferenciarlo como "Overview extendido".

**Recomendación:** Opción A. Es redundante.

### F1.3: Mover `DEPLOY_COMMANDS.md` a directorio interno

Crear `.devops/deploy.md`. El root público debería ser solo contenido de estudio.

### F1.4: Agregar badges al README raíz

```markdown
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ISTQB CTFL v4.0.1](https://img.shields.io/badge/ISTQB-CTFL%20v4.0.1-blue)](https://www.istqb.org)
[![Last commit](https://img.shields.io/github/last-commit/IvanWeissVanDerPol/istqb-prep-v4)](https://github.com/IvanWeissVanDerPol/istqb-prep-v4)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/IvanWeissVanDerPol/istqb-prep-v4)
```

### F1.5: Reducir emoji noise

Emojis solo cuando agregan valor:
- ✅ cuando es checklist
- ⚠️ cuando es warning
- ❌ cuando es anti-pattern

NO en cada heading.

## 🔧 P1 Fixes

### F1.6: Crear TOC visual al inicio del README

```markdown
## 🗺️ Mapa del repo

[Diagrama tree aquí]
```

### F1.7: Agregar "What this is NOT"

```markdown
## ⚠️ Lo que este repo NO es

- NO es material oficial ISTQB
- NO garantiza trabajo después del examen
- NO es sustituto del syllabus PDF oficial
- NO reemplaza práctica real con herramientas

Es APOYO al estudio, no la fuente autoritativa.
```

### F1.8: Crear `social-preview.png`

GitHub permite preview image 1280x640px. Generar uno con:
- Logo / title
- Tagline
- ISTQB CTFL v4.0.1
- 17 secciones preview

## 🔧 P2 Fixes

- F1.9: Crear GitHub Pages con navegación
- F1.10: Crear "tour" GIF animado
- F1.11: Mover 17 directorios a naming sin numbers (`topic-career/` en vez de `09_career_paths/`)

## 📊 Metrics de éxito

Después de los fixes:
- First-timer puede entender QUÉ es el repo en 60 segundos (medible: time-on-page)
- 50% reduction en "qué hago primero?" type questions (medible: GitHub issues)

## 🔗 Conecta con

- Role 2 (Returning Student) — necesita INDEX después del fix F1.6
- Role 11 (GitHub Power User) — necesita badges (F1.4) y releases
- Theme 5 (Falta Index/Navigation Central) — crítica
