---
name: tikz
description: Use when laying out or generating tikz figures. Helpers: tools/dot2tikz.py (draft layout from dot), UCFS (SPPF/GSS/RSM examples, see docs/ucfs.md), and the graphdrawing libraries in tex/styles/tikz.tex.
---

# Tikz (работа с tikz)

1. Для определения раскладки — скрипт `tools/dot2tikz.py`: помогает понять взаимное расположение узлов и сгенерировать черновой tikz по dot.
2. Для примеров SPPF, GSS, RSM — `UCFS/UCFS/cfpq-paths-app` (детали в readme этой папки). Можно модифицировать `UCFS/UCFS/cfpq-paths-app/src/main/kotlin/org/ucfs/paths/Main.kt`, чтобы подать нужные dot-файлы и RSM. Описание построения примеров SPPF — в `docs/ucfs.md`.

Общие правила размещения/именования рисунков — в скилле `file-structure`.

## Gotchas

- **Арифметика в макросах:** в `\newcommand` запись вида `2#3` TeX читает как **конкатенацию** цифры `2` и аргумента `#3` (напр. `#3=2` даёт `22`), а НЕ как умножение. Для умножения пиши явно `2*#3`. Симптом бага: вершины фигуры уезжают за пределы (напр. верхняя вершина `(7,26)` вместо `(7,8)`), фигура рендерится гигантской/«перекошенной». (Найдено в S6 задачи #58, рисунок `02_Valiant_layers.tex`.)
