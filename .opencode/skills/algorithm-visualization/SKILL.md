---
name: algorithm-visualization
description: Use when visualizing algorithms or their steps. Thin pointer to the FLPQ_sharp_edu CLI (FLPQ_sharp_edu/docs/user/cli.md); insert generated TeX fragments as-is, keep the tool's notations/styles, and route figures through the book's figures/ structure.
---

# Algorithm Visualization (визуализация алгоритмов)

Для визуализации алгоритмов (в т.ч. отдельных шагов) — инструмент из `FLPQ_sharp_edu` (консольная утилé). Подробнее: `FLPQ_sharp_edu/docs/user/cli.md`.

## Правила
1. Всегда визуализация в tikz (включена по умолчанию).
2. Соблюдай общие правила работы с изображениями, грамматиками и т.д.
3. Используй цветовые и стилевые решения инструмента; не дублируй стили; следи за унификацией в книге.
4. Сгенерированные TeX-фрагменты вставляй как есть — не перевёрстывай и не переписывай вручную (никаких собственных матриц, грамматик, SPPF, автоматов, если их умеет генерировать CLI).
5. Обозначения и соглашения бери из вывода инструмента без изменений (имена нетерминалов `N_1`, точка расщепления `k`, `\cdot` для пустых клеток, `\cellcolor{...}`, node-стили graphdrawing). Если вывод расходится с книгой — подгоняй текст под инструмент, а не наоборот.
6. CLI выдаёт самодостаточные TeX-фрагменты (без преамбулы). Для CYK: `grammar_original.tex`, `grammar_cnf.tex`, `input.tex`, `step_N/table.tex`, `sppf.tikz.tex`. Не разбирай полный `--summary`; используй отдельные артефакты шагов.
   - Рисунки (`sppf.tikz.tex`, автоматы) — перенеси в `figures/<NN_Section>/` по правилам и включай через `\input` внутри `figure`. Не ссылайся напрямую на файлы инструмента.
   - Чисто TeX-овское (грамматики `alignat*`, строка входа, таблицы `pNiceMatrix`) — inline: таблицы и вход внутри `\[ ... \]`, грамматики как есть.
7. SPPF и автоматы строятся через `\graph [layered layout, ...]` (graphdrawing). В `tex/styles/tikz.tex` обязательны `\usetikzlibrary{graphs,graphdrawing}` и `\usegdlibrary{layered}` (движок — lualatex). Добавь, если не подключены.
