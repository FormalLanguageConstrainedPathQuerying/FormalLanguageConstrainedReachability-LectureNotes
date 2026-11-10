---
name: project-navigation
description: Use before exploring or navigating the book. Navigate via docs/book-structure.md (the map), docs/glossary.md, docs/papers.md, docs/ucfs.md instead of scanning the whole tex/ tree; improve the map when navigation is slow or an area is undescribed.
---

# Project Navigation

Начинай навигацию по книге с документации, а не с обхода всего `tex/`.

## Процедура
1. Прочитай `docs/book-structure.md` — карта книги: структура по файлам, статусы разделов, краткое содержание.
2. Для терминов/сокращений — `docs/glossary.md`.
3. Для библиографии — `docs/papers.md`.
4. Для примеров SPPF/RSM через UCFS — `docs/ucfs.md`.
5. Открывай только нужный файл главы/раздела, который назвала карта; подтверждай точечными поисками (имя файла, метка `\label`), а не полным обходом дерева.

## Улучшай навигацию по ходу
Карта — часть продукта. Если `docs/book-structure.md` не отвечает на навигационный вопрос или ведёт не туда — поправь её в рамках задачи (обнови структуру/статус/краткое содержание при добавлении, удалении или изменении разделов).

## Правила
- Сначала карта, потом точечные чтения; «TeX-исходник — source of truth» не значит «сначала прочитать весь TeX».
- Держи этот скилл тонким указателем: не пересказывай содержимое `docs/` здесь.
