---
name: documentation
description: Use when a book change requires updating the agent docs. Maps source changes to doc updates: docs/book-structure.md (structure/status), docs/glossary.md (new terms), docs/papers.md (bibliography status).
---

# Documentation (маппинг изменений → docs)

При изменении книги обнови соответствующие docs (source of truth):

| Изменение в книге | Обновить |
|---|---|
| Добавил/удалил/переименовал раздел, главу, часть | `docs/book-structure.md` (структура, статус, краткое содержание) |
| Ввёл новый термин/сокращение | `docs/glossary.md` |
| Добавил/изменил библиографию, скачал PDF | `docs/papers.md` |
| Изменил правила вёрстки/стилей | соответствующий скилл + `tex/styles/` |

## Правила
- Не дублируй: doc держит только то, что нельзя однозначно восстановить из TeX-исходников.
- Если навигация по `docs/book-structure.md` стала медленной или область не описана — поправь её (см. `project-navigation`).
