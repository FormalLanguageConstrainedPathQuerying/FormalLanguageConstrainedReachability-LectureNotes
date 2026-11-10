---
name: typography
description: Use when writing or editing any TeX text in the book. Typesetting conventions: sidenote/sidecite, non-breaking spaces, «ёлочки» quotes, escaping, display math, \label prefixes, \rng, \Bbbone/\Bbbzero, w instead of omega, and the commands in tex/styles/math.tex.
---

# Typography (вёрстка)

- `sidenote` вместо `footnote`.
- `sidecite` вместо `cite` почти всегда. `cite` — только во вводных частях глав (чтобы не конфликтовало с `margintoc`) и внутри `sidenote`.
- Неразрывные пробелы: перед тире `текст~--- текст`; перед ссылками `текст~\cite{...}`, `текст~\sidecite{...}`.
- Кавычки — «ёлочки»: `<<текст>>`.
- Экранируй TeX-специальные символы в тексте: `#` → `\#`, `_` → `\_` и т.п.
- Выделенные (на отдельной строке) формулы — `\[ ... \]`.
- У `\label` всегда префикс типа: `\label{fig:...}`, `\label{sec:...}`, `\label{chpt:...}`.
- Диапазоны — `\rng`: `$[0 \rng n-1]$` (не `$[0 \ldots n-1]$`).
- `$\Bbbone$` — нейтральный по умножению; `$\Bbbzero$` — нейтральный по сложению.
- Для строк не используем $\omega$ — заменяем на `w`. Остальные греческие ($\alpha$, $\beta$) можно.
- Команды из `tex/styles/math.tex` — используй согласно описанию в комментариях к ним.

Source of truth: `tex/styles/math.tex`, `tex/styles/todonotes.tex`.
