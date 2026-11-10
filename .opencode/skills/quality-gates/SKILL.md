---
name: quality-gates
description: The pre-merge gate that must pass before a task is integrated: the book builds cleanly (build) and the changed text passes the checking checklist.
---

# Quality Gates

Гейт перед интеграцией задачи. Должен показать PASS.

## Гейты
1. **Сборка**: книга собирается чисто (см. `build`). Для задачи, тронувшей текст/стили/библиографию/фигуры — полная сборка.
2. **Checking**: изменённый текст проходит чек-лист (см. `checking` / `docs/checking.md`).

## Правила
- Если BLOCKED — не оценивай, «предсуществующие» ли падения; чини все и повторяй до PASS.
- Задача только по документации (без влияния на сборку) пропускает сборку, но проходит checking по затронутым docs.
