---
name: tikz
description: Use when laying out or generating tikz figures. Helpers: tools/dot2tikz.py (draft layout from dot), UCFS (SPPF/GSS/RSM examples, see docs/ucfs.md), and the graphdrawing libraries in tex/styles/tikz.tex.
---

# Tikz (работа с tikz)

1. Для определения раскладки — скрипт `tools/dot2tikz.py`: помогает понять взаимное расположение узлов и сгенерировать черновой tikz по dot.
2. Для примеров SPPF, GSS, RSM — `UCFS/UCFS/cfpq-paths-app` (детали в readme этой папки). Можно модифицировать `UCFS/UCFS/cfpq-paths-app/src/main/kotlin/org/ucfs/paths/Main.kt`, чтобы подать нужные dot-файлы и RSM. Описание построения примеров SPPF — в `docs/ucfs.md`.

Общие правила размещения/именования рисунков — в скилле `file-structure`.
