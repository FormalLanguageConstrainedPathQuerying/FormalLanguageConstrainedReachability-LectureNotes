---
name: file-structure
description: Use when creating or moving files/directories in the book. File and directory naming and organization: part_NN_Name/, chapter_NN_Name/, NN_Name.tex, figures/, styles/, frontmatter/, and \tikzsetfigurename.
---

# File Structure (структура и именование файлов)

Все исходники — в `tex/`.

## Терминология
- часть — `\addpart`; глава — `\chapter`; раздел — `\section`; подраздел — `\subsection`.
- Структурная единица — часть, глава, раздел, подраздел.
- Вводная часть главы — то, что до первого раздела; вводная часть раздела — то, что до первого подраздела.

## Правила
1. Имена файлов и директорий — только латиница.
2. **Часть** — `part_NN_Name/`: `main.tex` (`\addpart` + вводная часть + `\input` глав) и поддиректории глав.
3. **Глава** — `chapter_NN_Name/` внутри части: `main.tex` (`\chapter` + вводная часть + `\input` разделов) и файлы разделов. Если глава не разбита на разделы, `main.tex` содержит всё.
4. **Раздел** — `NN_Name.tex` рядом с `main.tex` главы: `\section{...}` и всё наполнение, включая `\subsection`.
5. Подразделы в отдельные файлы не выносятся.
6. Каждая структурная единица имеет `\label` с содержательным именем.
7. В каждом файле структурной единицы — `\tikzsetfigurename` (после «начала» единицы). Префикс меток секций — по главе (`sec:RP0...`); у всех секций одной главы одинаковый префикс. Подразделы: `sec:<префикс главы>_<префикс раздела>_`.
8. **Изображения** — в `figures/` внутри директории главы; при многих рисунках — поддиректории по номеру раздела (`figures/03_TensorProduct/`). Если используются в >1 главе — `figures/` на уровне части; в >1 части — верхний уровень. Не забыть поправить пути. Все tikz-рисунки — в отдельный `.tex` в `figures/`.
9. `figures/externalized/` — техническая директория для tikz externalization.
10. `styles/` — настройки пакетов и вспомогательные функции.

## Frontmatter
`Introduction.tex` и `List_of_contributors.tex` — в `frontmatter/`.
