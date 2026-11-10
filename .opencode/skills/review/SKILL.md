---
name: review
description: Use before merging a task. Whole-repo review of the task's diff against the checking checklist; iteratively detect and fix problems until zero findings.
---

# Review (ревью перед мержем)

После всех сабтасков задачи — ревью всего затронутого (и связанных мест) до интеграции.

## Процедура
1. Посмотри полный дифф задачи: `git diff --stat "$INTEGRATION"...HEAD` и по файлам.
2. Прогони чек-лист из `docs/checking.md` (см. `checking`) на изменённый текст и на места, которые изменение затрагивает (обозначения, определения, ссылки, библиография, термины).
3. Итеративно находи и чини проблемы до **нуля замечаний**.
4. Проверь, что docs обновлены (см. `documentation`).

## Правила
- Не мержи с известными замечаниями.
- Найденные проблемы фиксируй в issue задачи (база знаний).
