---
name: subtask-loop
description: Use when executing one atomic subtask from tasks/detailed_plan.md. Bounded uncommitted work, one commit per subtask, mirror plan progress to the issue, and verify task completeness.
---

# Subtask Loop

Цикл выполнения одного атомарного сабтаска из `tasks/detailed_plan.md`.

## Цикл
1. Возьми следующий незавершённый сабтаск (S1, S2, ...).
2. Реализуй его полностью — собираемый, проверяемый прирост.
3. Проверь прирост (сборка по `build`; для текстовых правок — по `checking`).
4. Закоммить как один коммит с идентификатором сабтаска в сообщении (см. `git-workflow`).
5. Отметь сабтаск выполненным в `tasks/detailed_plan.md` и обнови зеркало в issue-комментарии (первая строка `<!-- detailed-plan -->`).
6. Вернись к п.1 для следующего сабтаска.

## Правила
- Незакоммиченная работа — не более одного сабтаска.
- Не пропускай сабтаск молча: если не смог выполнить — отметь `[blocked]`/`[deferred]` и сообщи.
- Если сабтаск был начат, но откатился — он НЕ выполнен.

## Task Completeness Verification
Задача завершена, когда:
- все сабтаски закоммичены на feature-ветке;
- ни один сабтаск не `[blocked]`/`[deferred]`;
- последний коммит несёт `Closes #<N>` (номер задачи) отдельной строкой.
