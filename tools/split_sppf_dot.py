#!/usr/bin/env python3
"""
Разделяет комбинированный SPPF DOT-файл (от UCFS) на отдельные DOT-файлы —
по одному на каждый subgraph cluster. Также определяет <<полный>> кластер
(покрывающий всю входную цепочку).

Использование:
    python3 tools/split_sppf_dot.py input.dot output_prefix [--full-only]

    input.dot     — комбинированный SPPF DOT-файл
    output_prefix — префикс для выходных файлов (output_prefix_cluster_0.dot, …)

    --full-only   — выдать только полный кластер (для линейного входа)

Определение полного кластера: кластер, в котором нетерминальный узел
имеет наибольший диапазон [i, j] (максимальное значение j - i).
"""

import re
import sys
import os
from pathlib import Path


def parse_dot(content: str):
    """Разбирает DOT-файл: возвращает список кластеров.
    Каждый кластер — dict с ключами 'id' (int), 'nodes' (список строк),
    'edges' (список строк), 'span' (int — макс. длина диапазона)."""
    clusters = []

    pat_subgraph = re.compile(
        r'subgraph\s+cluster_(\d+)\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}',
        re.DOTALL
    )

    for m in pat_subgraph.finditer(content):
        cid = int(m.group(1))
        body = m.group(2)

        nodes = []
        edges = []
        max_span = 0

        for line in body.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            if '->' in line and 'label' not in line:
                edges.append(line)
            elif '[' in line and 'label' in line:
                nodes.append(line)
                # Определяем диапазон для поиска полного кластера
                span_m = re.search(r'input:\s*\[(\d+),\s*(\d+)\]', line)
                if span_m:
                    span = int(span_m.group(2)) - int(span_m.group(1))
                    if span > max_span:
                        max_span = span

        clusters.append({
            'id': cid,
            'nodes': nodes,
            'edges': edges,
            'span': max_span,
        })

    return clusters


def write_cluster(cluster: dict, filepath: str, label: str = ''):
    """Записывает один кластер как самостоятельный DOT-файл."""
    with open(filepath, 'w') as f:
        f.write('digraph g {\n')
        f.write('labelloc="t"\n')
        f.write(f'label="{label}"\n')
        for node in cluster['nodes']:
            f.write(node + '\n')
        for edge in cluster['edges']:
            f.write(edge + '\n')
        f.write('}\n')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]

    if len(args) < 2:
        print(__doc__.strip())
        sys.exit(1)

    input_file = args[0]
    output_prefix = args[1]
    full_only = '--full-only' in flags

    with open(input_file) as f:
        content = f.read()

    clusters = parse_dot(content)

    if not clusters:
        print(f'Error: no subgraph clusters found in {input_file}', file=sys.stderr)
        sys.exit(1)

    # Определяем полный кластер
    full_cluster = max(clusters, key=lambda c: c['span'])
    print(f'Clusters found: {len(clusters)}, full cluster: {full_cluster["id"]} (span={full_cluster["span"]})')

    out_dir = Path(output_prefix).parent
    base = Path(output_prefix).name

    if full_only:
        out_path = str(Path(out_dir) / f'{base}_cluster_{full_cluster["id"]}.dot')
        write_cluster(full_cluster, out_path, label=f'cluster_{full_cluster["id"]}')
        print(f'Wrote {out_path}')
    else:
        for c in clusters:
            out_path = str(Path(out_dir) / f'{base}_cluster_{c["id"]}.dot')
            write_cluster(c, out_path, label=f'cluster_{c["id"]}')
            print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
