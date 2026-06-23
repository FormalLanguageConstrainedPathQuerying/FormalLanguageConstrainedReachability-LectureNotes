#!/usr/bin/env python3
"""
Конвертирует dot-файл (Graphviz) в tikz-изображение с раскладкой по решётке.

## Использование

Запускать из корня проекта:

    python3 tools/dot2tikz.py input.dot output.tex

## Что делает

 1. Запускает `dot -Tplain input.dot` для получения координат узлов.
 2. Группирует узлы в строки (по y-координате) и сортирует их слева направо.
 3. Для каждого узла определяет позицию через ближайшего соседа сверху
    (`below=of`, `below left=of`, `below right=of`).
 4. Генерирует `.tex` файл с `tikzpicture`, включая все рёбра из dot-файла.

## Зависимости

- Python 3 (только стандартная библиотека)
- `dot` из Graphviz (доступен в PATH)
"""

import subprocess
import sys
import re
import os
from collections import OrderedDict


STYLE_KEYWORDS = {
    'solid', 'dashed', 'dotted', 'bold', 'invis',
    'filled', 'diagonals', 'rounded',
}


def run_dot_plain(dot_file: str) -> str:
    result = subprocess.run(
        ['dot', '-Tplain', dot_file],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def parse_plain(plain_output: str):
    """Разбирает вывод dot -Tplain.

    Возвращает (nodes, edges), где:
      nodes: OrderedDict name -> {x, y, w, h, label}
      edges: list of (tail, head)
    """
    nodes = OrderedDict()
    edges = []

    for line in plain_output.strip().split('\n'):
        if not line:
            continue
        parts = line.split()

        cmd = parts[0]

        if cmd == 'node':
            name = parts[1]
            x = float(parts[2])
            y = float(parts[3])
            w = float(parts[4])
            h = float(parts[5])

            # Находим позицию стиля (solid, dashed, …)
            style_idx = None
            for i in range(6, len(parts)):
                if parts[i] in STYLE_KEYWORDS:
                    style_idx = i
                    break

            if style_idx is None:
                label = ' '.join(parts[6:])
            else:
                label = ' '.join(parts[6:style_idx])

            label = _strip_quotes(label)
            nodes[name] = {'x': x, 'y': y, 'w': w, 'h': h, 'label': label}

        elif cmd == 'edge':
            tail = parts[1]
            head = parts[2]
            edges.append((tail, head))

    return nodes, edges


def cluster_rows(nodes, tolerance: float | None = None):
    """Группирует узлы в строки по y-координате.

    Если tolerance не задан, вычисляется как 0.4 * средняя высота узла.
    Возвращает список строк; каждая строка — список (name, node),
    отсортированный по x слева направо.
    """
    if not nodes:
        return []

    if tolerance is None:
        avg_h = sum(n['h'] for n in nodes.values()) / len(nodes)
        tolerance = avg_h * 0.4

    # Сортируем по убыванию y (в graphviz y=0 — низ, больше y — выше)
    sorted_items = sorted(nodes.items(), key=lambda kv: -kv[1]['y'])

    rows = []
    current_row = []
    current_y = None

    for name, nd in sorted_items:
        if current_y is None or abs(nd['y'] - current_y) <= tolerance:
            current_row.append((name, nd))
            if current_y is None:
                current_y = nd['y']
        else:
            current_row.sort(key=lambda kv: kv[1]['x'])
            rows.append(current_row)
            current_row = [(name, nd)]
            current_y = nd['y']

    if current_row:
        current_row.sort(key=lambda kv: kv[1]['x'])
        rows.append(current_row)

    return rows


def _strip_quotes(label: str) -> str:
    if len(label) >= 2 and label[0] == '"' and label[-1] == '"':
        return label[1:-1]
    return label


def sanitize_name(name: str) -> str:
    """Преобразует имя узла из dot в безопасное имя координаты TikZ."""
    name = name.replace('_', 'us')
    name = name.replace('-', 'h')
    name = name.replace('.', 'd')
    name = name.replace(':', 'c')
    name = re.sub(r'[^a-zA-Z0-9]', '', name)
    if not name or name[0].isdigit():
        name = 'n' + name
    return name


def escape_label(label: str) -> str:
    """Экранирует спецсимволы LaTeX в метке узла.

    Символ `_` экранируется только вне фрагментов $...$, чтобы не
    повредить математическую моду."""
    # Защищаем $...$-блоки
    math_blocks = []

    def _protect(m):
        math_blocks.append(m.group(0))
        return f'\x00MATH{len(math_blocks) - 1}\x00'

    label = re.sub(r'\$[^$]*\$', _protect, label)

    # Экранируем _ , # , % , & , { , } , ~
    for ch in ['\\', '#', '%', '&', '{', '}', '~']:
        label = label.replace(ch, '\\' + ch)
    label = re.sub(r'(?<!\\)_', r'\\_', label)

    # Восстанавливаем $...$-блоки
    def _restore(m):
        idx = int(m.group(1))
        return math_blocks[idx]

    label = re.sub(r'\x00MATH(\d+)\x00', _restore, label)

    return label


def generate_tikz(nodes, edges, rows):
    """Генерирует код tikzpicture."""
    lines = []
    lines.append('\\begin{tikzpicture}[shorten >=1pt,node distance=1.2cm]')

    name_map = {}       # orig -> safe
    safe_to_orig = {}   # safe -> orig
    row_of = {}         # orig -> row_index

    for name in nodes:
        name_map[name] = sanitize_name(name)
        safe_to_orig[name_map[name]] = name

    for ridx, row_nodes in enumerate(rows):
        for orig_name, _ in row_nodes:
            row_of[orig_name] = ridx

    # Строим отображение размещённых узлов для поиска соседей
    placing = OrderedDict()  # safe_name -> orig_name, в порядке размещения

    avg_w = sum(n['w'] for n in nodes.values()) / len(nodes) if nodes else 1.0
    x_tol = avg_w * 0.3

    for row_idx, row_nodes in enumerate(rows):
        for col_idx, (orig_name, nd) in enumerate(row_nodes):
            safe_name = name_map[orig_name]

            if row_idx == 0:
                if col_idx == 0:
                    pos = ''
                else:
                    left_safe = name_map[row_nodes[col_idx - 1][0]]
                    pos = f'right=of {left_safe}'
            elif col_idx > 0:
                # В пределах строки цепляем узлы горизонтально
                left_safe = name_map[row_nodes[col_idx - 1][0]]
                pos = f'right=of {left_safe}'
            else:
                # Первый узел строки: ищем ближайший по x узел из предыдущей строки
                prev_row_names = {name for name, _ in rows[row_idx - 1]}
                min_dist = float('inf')
                ref_safe = None
                for prev_safe, prev_orig in placing.items():
                    if prev_orig not in prev_row_names:
                        continue
                    prev_nd = nodes[prev_orig]
                    x_dist_candidate = abs(nd['x'] - prev_nd['x'])
                    if x_dist_candidate < min_dist:
                        min_dist = x_dist_candidate
                        ref_safe = prev_safe

                if ref_safe is None:
                    prev_row = rows[row_idx - 1]
                    ref_safe = name_map[prev_row[0][0]]
                    ref_nd = nodes[prev_row[0][0]]
                else:
                    ref_nd = nodes[safe_to_orig[ref_safe]]

                x_dist = nd['x'] - ref_nd['x']

                if abs(x_dist) <= x_tol:
                    pos = f'below=of {ref_safe}'
                elif x_dist < 0:
                    pos = f'below left=of {ref_safe}'
                else:
                    pos = f'below right=of {ref_safe}'

            label = nodes[orig_name]['label']
            escaped = escape_label(label)
            if pos:
                lines.append(
                    f'    \\node[draw] ({safe_name}) [{pos}] {{{escaped}}};'
                )
            else:
                lines.append(
                    f'    \\node[draw] ({safe_name}) {{{escaped}}};'
                )
            placing[safe_name] = orig_name

    # Рёбра
    if edges:
        lines.append('')
        lines.append('    \\path[->]')
        for tail, head in edges:
            t_safe = name_map.get(tail)
            h_safe = name_map.get(head)
            if t_safe is None or h_safe is None:
                continue

            if tail == head:
                lines.append(f'        ({t_safe}) edge [loop above] ()')
                continue

            t_row = row_of.get(tail)
            h_row = row_of.get(head)
            if t_row is not None and h_row is not None and abs(t_row - h_row) > 1:
                lines.append(f'        ({t_safe}) edge [bend right] ({h_safe})')
            else:
                lines.append(f'        ({t_safe}) edge ({h_safe})')

        lines.append('    ;')

    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines) + '\n'


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        sys.exit(1)

    dot_file = sys.argv[1]
    tex_file = sys.argv[2]

    if not os.path.exists(dot_file):
        print(f'Error: file not found: {dot_file}', file=sys.stderr)
        sys.exit(1)

    plain_output = run_dot_plain(dot_file)
    nodes, edges = parse_plain(plain_output)

    if not nodes:
        print('Error: no nodes found in the dot file', file=sys.stderr)
        sys.exit(1)

    rows = cluster_rows(nodes)
    tikz_code = generate_tikz(nodes, edges, rows)

    with open(tex_file, 'w') as f:
        f.write(tikz_code)

    print(
        f'Generated {tex_file}: '
        f'{len(nodes)} nodes, {len(edges)} edges, {len(rows)} rows'
    )


if __name__ == '__main__':
    main()
