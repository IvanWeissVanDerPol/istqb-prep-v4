# Contributing to ISTQB CTFL Prep Hub v4.0.1

¡Gracias por tu interés en contribuir! 🎉

Este repo es un esfuerzo comunitario para ayudar a personas en Paraguay y LATAM a prepararse para el examen ISTQB CTFL v4.0.1.

---

## 📜 Code of Conduct

Al participar, esperás adherir a nuestro [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Por favor léelo antes de contribuir.

---

## 🐛 ¿Cómo reportar un bug?

1. **Verificá** que no exista ya en [Issues](https://github.com/IvanWeissVanDerPol/istqb-prep-v4/issues).
2. **Creá** un nuevo issue usando la plantilla `bug_report.md`.
3. **Incluí**:
   - URL o path del archivo afectado
   - Línea específica (si aplica)
   - Comportamiento esperado vs actual
   - Pasos para reproducir

---

## 💡 ¿Cómo sugerir una mejora?

1. **Verificá** que no exista en [Issues](https://github.com/IvanWeissVanDerPol/istqb-prep-v4/issues).
2. **Creá** un issue usando la plantilla `feature_request.md`.
3. **Describí**:
   - Qué quieres agregar
   - Por qué agrega valor
   - Cómo lo implementarías (opcional)

---

## 🔧 ¿Cómo hacer un Pull Request?

### 1. Fork el repo

Click "Fork" en GitHub.

### 2. Cloná tu fork

```bash
git clone https://github.com/TU_USUARIO/istqb-prep-v4.git
cd istqb-prep-v4
```

### 3. Creá un branch

```bash
git checkout -b feature/mi-mejora
```

Naming conventions:
- `feature/<nombre>` para nuevas features
- `fix/<nombre>` para bug fixes
- `docs/<nombre>` para cambios solo de docs
- `refactor/<nombre>` para refactors

### 4. Hacé tus cambios

**Style guide:**

- **Idioma:** Español (vos, Paraguay). Inglés solo cuando es ISTQB oficial
- **Markdown:** usar `-` para listas, no `*`
- **Headers:** español (`# Capítulo 1`), no inglés (`# Chapter 1`)
- **Emojis:** máximo 3 por archivo
- **Longitud:** mantener archivos <50KB cuando posible
- **Cross-references:** usar paths relativos (`../05_summaries/`)

### 5. Verificá localmente

Antes de push:

- [ ] El markdown se ve bien en preview
- [ ] No hay links rotos en tus cambios
- [ ] Si agregaste quiz, incluiste respuestas
- [ ] Si agregaste sample exam, incluiste answer key

### 6. Push y PR

```bash
git add .
git commit -m "Add: descripción del cambio"
git push origin feature/mi-mejora
```

Después abrí un Pull Request en GitHub usando la plantilla `pull_request_template.md`.

### 7. Espera review

Un maintainer va a revisar tu PR. Puede pedir cambios. Sé paciente — esto es hobby project.

---

## 🎯 Tipos de contribuciones bienvenidas

### P0 (más necesitadas)

- [ ] **Answer keys** para sample exams (Sample A ya tiene — B y C también)
- [ ] **Más preguntas** para quizzes (Cap 4 y Cap 5 son prioritarios)
- [ ] **Más flashcards** (target: 200+ cards)
- [ ] **Traducción a otros idiomas** (PT, EN, FR)

### P1 (útiles)

- [ ] **Fix typos / erratas** (abrí PR directo)
- [ ] **Mejorar summaries** (más ejemplos, más claridad)
- [ ] **Agregar ejercicios hands-on** (BVA, decision tables)
- [ ] **Salarios PY actualizados** (con fuentes)

### P2 (nice)

- [ ] **Diagramas visuales** (mermaid, SVG)
- [ ] **Templates adicionales** (test plan, defect report)
- [ ] **Recursos externos** nuevos

---

## 🚫 Lo que NO aceptamos

- **Material con copyright ISTQB** (extractos del syllabus oficial, glossary oficial). Solo enlaces.
- **Sample exams oficiales pirateados** ("dumps"). ISTQB vende los oficiales.
- **Spam / promotion** de herramientas comerciales no relacionadas.
- **Contenido discriminatorio, sexista, o no profesional.**
- **Cambios masivos sin discutir primero** (abrí un issue primero).

---

## 📋 Proceso de review

1. Maintainer revisa PR dentro de 1-2 semanas (esto es hobby)
2. Si hay cambios pedidos, el contributor los aplica
3. Una vez aprobado, se mergea
4. Aparece en CHANGELOG.md

---

## 💬 ¿Preguntas?

- Abrí un [Discussion](https://github.com/IvanWeissVanDerPol/istqb-prep-v4/discussions)
- O mandame DM por GitHub

---

## 🏷️ Maintainers

- **Ivan Weiss Van Der Pol** ([@IvanWeissVanDerPol](https://github.com/IvanWeissVanDerPol))

Si te interesa ser maintainer: contactame. Necesito ayuda con review, especialmente para contenido en español.

---

## 🙏 Reconocimientos

Gracias a todas las personas que contribuyen. Lista en [CONTRIBUTORS.md](CONTRIBUTORS.md) (TBD).
