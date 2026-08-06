# 🚀 Deploy Pack — ISTQB CTFL v4.0.1 Prep Hub

> Run these commands in order. Tested against current state in `/tmp/istqb-prep/`.

---

## ⚡ One-shot deployment

```bash
# 1. Set up working directory
WORKDIR="/tmp/istqb-deploy"
rm -rf "$WORKDIR" && mkdir -p "$WORKDIR" && cd "$WORKDIR"

# 2. Copy source from agent output
cp -r /tmp/istqb-prep/. "$WORKDIR/"

# 3. Initialize git
cd "$WORKDIR"
git init
git config user.name "Ivan Weiss"
git config user.email "weissvanderpol.ivan@gmail.com"

# 4. Create .gitignore (keep working dir clean)
cat > .gitignore <<'EOF'
.DS_Store
*.swp
*.tmp
.idea/
.vscode/
EOF

# 5. Create LICENSE (MIT)
cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2025 Ivan Weiss / Ai-Whisperers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

NOTE: The ISTQB syllabus is © ISTQB GmbH. This repo only summarizes and curates
non-commercial study material. Do not redistribute the official PDF — download
it from https://istqb.org instead.
EOF

# 6. Add all files
git add .

# 7. Initial commit
git commit -m "Initial: ISTQB CTFL v4.0.1 prep hub (11 files, ~100KB)

- 6 capítulos del syllabus v4.0.1 (oficial, sep-2024)
- 64 Learning Objectives en checklist
- 30+ quizzes (Cap 1 + Cap 4 los más detallados)
- Sample exam A (40 preguntas, simulacro real, 60 min)
- Glosario con términos NUEVOS v4.0.1 + cambios de vocabulario
- Resumen de cambios v3.1 → v4.0.1
- Top 30 preguntas más probables

Ver también: README.md y 09_v4_changes/."

# 8. Create repo on GitHub (creates remote)
REPO="ivanweiss/istqb-prep-v4"
gh repo create "$REPO" --public --source=. --remote=origin --description "ISTQB CTFL v4.0.1 prep hub — sample exam, quizzes, glossary for QA certification" --push
```

If `gh` is not authenticated yet, the command will fail at step 8. Run separately:

```bash
gh auth login --with-token < /path/to/github.token
```

---

## 🔗 The link

Once pushed, your repo lives at:

```
https://github.com/ivanweiss/istqb-prep-v4
```

Specific deep links (after first push):

| File | URL |
|---|---|
| README | https://github.com/ivanweiss/istqb-prep-v4/blob/main/00_README/README.md |
| Syllabus structure | https://github.com/ivanweiss/istqb-prep-v4/tree/main/02_syllabus_v4_0_1 |
| Full LO checklist | https://github.com/ivanweiss/istqb-prep-v4/blob/main/02_syllabus_v4_0_1/MAPA_COMPLETO_OBJETIVOS.md |
| Glossary v4.0.1 | https://github.com/ivanweiss/istqb-prep-v4/blob/main/03_glosario/GLOSARIO_v4.0.1.md |
| Sample exam A | https://github.com/ivanweiss/istqb-prep-v4/blob/main/06_practice_tests/sample_exam_A.md |
| Cap 4 quiz | https://github.com/ivanweiss/istqb-prep-v4/blob/main/06_practice_tests/quizzes_por_capitulo/cap_04_quiz.md |
| Changes v3.1→v4.0.1 | https://github.com/ivanweiss/istqb-prep-v4/blob/main/09_v4_changes/CAMBIOS_v3.1_a_v4.0.1.md |

---

## 🔄 Sync commands (after first push)

### Daily workflow

```bash
cd /tmp/istqb-deploy

# Status
git status

# Edit something
# Then:
git add .
git commit -m "Description of change"

# Pull + push
git pull --rebase origin main
git push origin main
```

### Add a remote (if you started without `gh repo create`)

```bash
git remote add origin git@github.com:ivanweiss/istqb-prep-v4.git
git branch -M main
git push -u origin main
```

---

## 🛡️ Safety rails

- **Public repo** (--public flag) — anyone can read. Switch to `--private` if you want only your friends to see it.
- **No secrets** in the working directory
- **No ISTQB PDF** redistributed — syllabus is summarized, not copied
- **MIT license** allows free redistribution with attribution

## ⚠️ Known limitations of this repo

1. **Sample exam is NOT official** — it's a curriculum-derived approximation. ISTQB sells official sample exams through Member Boards (e.g., USD 30-60 per exam).
2. **11 files in 5 of 9 planned folders** — `01_plan_estudio/`, `04_flashcards/`, `07_resources/`, `08_quick_refs/` are empty placeholders. Material is in `02_`, `03_`, `05_`, `06_`, `09_`. Expand over time.
3. **The two WhatsApp JIDs** (`201309445722357` and `117111141752976`) weren't resolved against Ivan's corpus — could be ISTQB PY community channels/groups not in personal archive. Re-check before linking in repo.

## Next obvious additions

If your friends need more:

- [ ] Sample exam B + C (variations)
- [ ] Quiz Cap 2, 3, 5 (only Cap 1 and 4 done)
- [ ] Flashcards (Anki `.apkg` or CSV)
- [ ] Summary of Cap 1 + Cap 3 + Cap 6 (the missing ones)
- [ ] "How to register" guide for ASOLINFO PY
