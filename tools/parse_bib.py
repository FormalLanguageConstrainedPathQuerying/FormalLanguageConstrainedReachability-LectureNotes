#!/usr/bin/env python3
"""
Инструмент для сопоставления библиографических записей (`.bib`) с PDF-файлами в `papers_pdf/`.

Генерирует `papers.md` — сводный список источников со статусом скачивания.

## Использование

Запускать из корня проекта:

    python3 tools/parse_bib.py

## Что делает

1. Парсит `tex/FormalLanguageConstrainedReachabilityLectureNotes.bib`,
   извлекая ключ, название и авторов каждой записи.
2. Сопоставляет названия с PDF-файлами в `papers_pdf/` (через нормализацию:
   приведение к нижнему регистру, удаление пунктуации, LaTeX-команд и
   математической разметки).
3. Обнаруживает дубликаты в библиографии (одинаковые названия с разными
   ключами).
4. Записывает результат в `papers.md`:
   - Сводная таблица всех источников со столбцами:
     `Статус | Название | Авторы | Ключ`
   - Статус: ✓ — PDF скачан, ✗ — PDF отсутствует.
   - Дубликаты помечены символом ⚠.
   - Отдельные секции: PDF без bib-записи и группы дубликатов.

## Принцип сопоставления

Сопоставление трёхуровневое:
1. Точное совпадение нормализованных названий.
2. Одно название целиком содержится в другом.
3. Нечёткое совпадение (`SequenceMatcher.ratio > 0.80`).

## Зависимости

Только стандартная библиотека Python 3.
"""

import re
import os
from collections import defaultdict
from difflib import SequenceMatcher


def extract_field(body: str, field_name: str) -> str:
    """
    Извлекает значение поля из тела bib-записи.
    Корректно обрабатывает вложенные фигурные скобки и строки в кавычках.
    """
    pattern = re.compile(rf'(?<!\w){field_name}\s*=\s*([{{"])', re.IGNORECASE)
    m = pattern.search(body)
    if not m:
        return ''

    delimiter = m.group(1)
    start = m.end()

    if delimiter == '"':
        j = start
        prev = ''
        while j < len(body):
            if body[j] == '"' and prev != '\\':
                break
            prev = body[j]
            j += 1
        return body[start:j]
    else:
        brace_count = 1
        j = start
        while j < len(body) and brace_count > 0:
            if body[j] == '{':
                brace_count += 1
            elif body[j] == '}':
                brace_count -= 1
            j += 1
        return body[start:j - 1]


def normalize(text: str) -> str:
    """
    Нормализует строку для сравнения: нижний регистр, удаление LaTeX-команд
    и мат. разметки, удаление пунктуации, склейка пробелов.
    """
    s = text.lower()
    # Удаляем $ из математической моды, сохраняя содержимое
    s = s.replace('$', '')
    # Удаляем LaTeX-команды (\texttimes, \mathbb и т.д.)
    s = re.sub(r'\\[a-zA-Z]+\s*', '', s)
    # Удаляем фигурные скобки, сохраняя содержимое
    s = re.sub(r'\{([^}]*)\}', r'\1', s)
    # Заменяем знаки пунктуации на пробелы
    s = re.sub(r'[^\w\s]', ' ', s)
    # Схлопываем множественные пробелы
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def parse_bib(filepath: str) -> list[dict]:
    """
    Парсит .bib-файл.
    Возвращает список словарей с ключами: key, type, title, author.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    entries: list[dict] = []
    pos = 0

    while True:
        # Ищем начало записи: @type{key,
        m = re.search(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', content[pos:])
        if not m:
            break

        entry_type = m.group(1)
        entry_key = m.group(2)
        body_start = pos + m.end()

        # Ищем закрывающую фигурную скобку (с учётом вложенности и кавычек)
        brace_count = 1
        in_quotes = False
        prev_char = ''
        body_end = body_start
        for j in range(body_start, len(content)):
            c = content[j]
            if c == '"' and prev_char != '\\':
                in_quotes = not in_quotes
            if not in_quotes:
                if c == '{':
                    brace_count += 1
                elif c == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        body_end = j
                        break
            prev_char = c

        body = content[body_start:body_end]
        pos = body_end + 1

        title = re.sub(r'\s+', ' ', extract_field(body, 'title').strip())
        author = re.sub(r'\s+', ' ', extract_field(body, 'author').strip())
        author = re.sub(r'\s+and\s+', '; ', author)

        entries.append({
            'key': entry_key,
            'type': entry_type,
            'title': title,
            'author': author,
        })

    return entries


def main() -> None:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    bib_path = os.path.join(
        project_root, 'tex', 'FormalLanguageConstrainedReachabilityLectureNotes.bib'
    )
    pdf_dir = os.path.join(project_root, 'papers_pdf')
    output_path = os.path.join(project_root, 'papers.md')

    # Парсим библиографию
    entries = parse_bib(bib_path)
    assert all(e['title'] for e in entries), \
        f"Не удалось извлечь название у {sum(1 for e in entries if not e['title'])} записей"

    # Собираем PDF-файлы
    if not os.path.isdir(pdf_dir):
        print(f"Директория {pdf_dir} не найдена")
        pdf_files = []
    else:
        pdf_files = sorted([f for f in os.listdir(pdf_dir) if f.endswith('.pdf')])

    # Нормализуем имена PDF
    pdf_norm = {f: normalize(f[:-4]) for f in pdf_files}

    # --- Сопоставление ---
    matched_nts: set[str] = set()

    for e in entries:
        nt = normalize(e['title'])
        if not nt:
            continue
        for pdf in pdf_files:
            pn = pdf_norm[pdf]
            # Уровень 1: точное совпадение
            if nt == pn:
                matched_nts.add(nt)
                break
            # Уровень 2: одно содержится в другом
            if len(nt) > 15 and len(pn) > 15 and (nt in pn or pn in nt):
                matched_nts.add(nt)
                break
            # Уровень 3: нечёткое совпадение
            if len(nt) > 15 and SequenceMatcher(None, nt, pn).ratio() > 0.80:
                matched_nts.add(nt)
                break

    # Определяем, какие PDF сопоставлены
    matched_pdfs: set[str] = set()
    for e in entries:
        nt = normalize(e['title'])
        if nt not in matched_nts:
            continue
        for pdf in pdf_files:
            pn = pdf_norm[pdf]
            if (nt == pn or
                (len(nt) > 15 and len(pn) > 15 and (nt in pn or pn in nt)) or
                (len(nt) > 15 and SequenceMatcher(None, nt, pn).ratio() > 0.80)):
                matched_pdfs.add(pdf)
                break

    unmatched_pdfs = sorted(set(pdf_files) - matched_pdfs)

    # --- Дубликаты ---
    # В библиографии
    seen_nt: dict[str, list[str]] = defaultdict(list)
    for e in entries:
        nt = normalize(e['title'])
        if nt:
            seen_nt[nt].append(e['key'])

    dup_groups = {k: v for k, v in seen_nt.items() if len(v) > 1}
    dup_keys: set[str] = set()
    for keys in dup_groups.values():
        dup_keys.update(keys)

    # Среди PDF
    seen_pn: dict[str, str] = {}
    pdf_dup: dict[str, str] = {}
    for pdf in sorted(pdf_files):
        pn = pdf_norm[pdf]
        if pn in seen_pn:
            pdf_dup[pdf] = seen_pn[pn]
        else:
            seen_pn[pn] = pdf

    # Статус для каждой bib-записи
    entry_has_pdf = {e['key']: normalize(e['title']) in matched_nts for e in entries}

    # --- Генерация Markdown ---
    lines: list[str] = []
    lines.append('# Список источников')
    lines.append('')
    lines.append('| Показатель | Значение |')
    lines.append('|---|---|')
    lines.append(f'| Всего записей в библиографии | **{len(entries)}** |')
    lines.append(f'| Скачано PDF | **{len(pdf_files)}** |')
    lines.append(f'| ✓ скачано (есть PDF) | **{sum(entry_has_pdf.values())}** |')
    lines.append(f'| ✗ не скачано | **{len(entries) - sum(entry_has_pdf.values())}** |')
    lines.append(f'| Дубликатов в bib | **{len(dup_groups)}** групп |')
    lines.append(f'| PDF без bib-записи | **{len(unmatched_pdfs)}** |')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('| Статус | Название | Авторы | Ключ |')
    lines.append('|--------|----------|--------|------|')

    for e in entries:
        status = '✓' if entry_has_pdf[e['key']] else '✗'
        dup_mark = ' ⚠' if e['key'] in dup_keys else ''
        key_display = f'`{e["key"]}`{dup_mark}'
        title_esc = e['title'].replace('|', '\\|')
        author_esc = e['author'].replace('|', '\\|')
        lines.append(f'| {status} | {title_esc} | {author_esc} | {key_display} |')

    if unmatched_pdfs:
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('## PDF-файлы без bib-записи')
        lines.append('')
        for f in unmatched_pdfs:
            label = f' — дубликат `{pdf_dup[f]}`' if f in pdf_dup else ''
            lines.append(f'- {f}{label}')

    if dup_groups:
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('## Дубликаты в библиографии')
        lines.append('')
        for nt, keys in sorted(dup_groups.items()):
            e0 = next(x for x in entries if x['key'] == keys[0])
            has_pdf = '✓' if nt in matched_nts else '✗'
            lines.append(
                f'- {has_pdf} **{e0["title"]}**: '
                f'{", ".join(f"`{k}`" for k in keys)}'
            )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    downloaded = sum(entry_has_pdf.values())
    print(f'Скачано: {downloaded}/{len(entries)}')
    print(f'PDF без bib-записи: {len(unmatched_pdfs)}')
    print(f'Групп дубликатов: {len(dup_groups)}')
    print(f'Результат сохранён в {output_path}')


if __name__ == '__main__':
    main()
