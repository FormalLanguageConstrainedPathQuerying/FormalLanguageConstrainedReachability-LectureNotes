---
name: git-workflow
description: Use for branching, committing, rebasing, and merging. Feature branch per task from the integration branch, one commit per subtask, rebase+merge integration, and the commit message format.
---

# Git Workflow

## Ветвление
- **Integration branch**: `INTEGRATION=$(git config --get book.integrationBranch || echo dev)`. По умолчанию `dev`.
- На каждую задачу — своя feature-ветка, созданная от integration branch.
- Никогда не коммить напрямую в integration branch.

## Коммиты
- Один сабтаск = один коммит.
- Формат сообщения: `<S-id>(#<issue>): <что и почему>`. Пример: `S2(#47): добавить пример CYK с SPPF, т.к. ...`.
- Сообщение достаточно подробное, чтобы понять причину изменения.
- Последний коммит задачи несёт `Closes #<N>` отдельной строкой.

## Интеграция
- Пуш feature-ветки, PR в integration branch.
- Мерж — rebase + merge (fast-forward), чтобы сохранить линейность и коммиты сабтасков.
- После мержа — удалить feature-ветку.

## Обновление
- На границе задачи (перед созданием feature-ветки) — rebase integration branch на `origin/<integration>`.
