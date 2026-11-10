---
name: build
description: Use when compiling the book (latexmk/lualatex). Thin pointer to docs/build.md, tex/Makefile, and .github/workflows/main.yml; covers full vs incremental builds and the headless background watch mode (-pvc -view=none).
---

# Build

Что такое сборка и где точные команды — в `docs/build.md`, `tex/Makefile` и `.github/workflows/main.yml`. Читай `docs/build.md` перед сборкой.

## Ключевое
- **Полная сборка долгая** (вся книга, lualatex + biber + несколько проходов). **Инкрементальная быстрая** (latexmk + tikz-кэш `tex/figures/externalized/`).
- **Фоновый watch** (из `tex/`): `latexmk -lualatex -pvc -view=none -interaction=nonstopmode -shell-escape FormalLanguageConstrainedReachabilityLectureNotes.tex` — в фоне, автопересборка при изменении, без GUI-вьюера.
- **Политика**: во время работы — инкрементальная / `-pvc`; **одна полная сборка в конце большой задачи**.

## Не делай
- Не гоняй полные clean-сборки посреди задачи.
- Не собирай «на всякий случай» без необходимости.
