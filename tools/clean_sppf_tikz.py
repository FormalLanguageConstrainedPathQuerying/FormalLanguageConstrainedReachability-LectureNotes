#!/usr/bin/env python3
"""
Post-process dot2tikz-generated SPPF figures:
- Classifies nodes by type (from UCFS label)
- Replaces [draw] with appropriate style
- Shortens labels using book's SPPF definition notation:
  Intermediate: I_{q,v}, Range: R^{q_from,v_from}_{q_to,v_to}
- Renames RSM state names S_X -> q_X to match book examples
"""

import re
import sys


_Q_REMAP = {'S_': 'q_'}


def _rename_rsm(name):
    for old, new in _Q_REMAP.items():
        name = name.replace(old, new)
    return name


def classify_and_clean(label):
    """Classify node type from UCFS label and return (style, clean_label)."""
    label = label.strip()

    if 'Nonterminal' in label:
        m = re.search(r'Nonterminal (\w+), input: \[(\d+), (\d+)\]', label)
        if m:
            name = m.group(1)
            return 'symbol_node', f'${name}_{{{m.group(2)},{m.group(3)}}}$'
        return 'symbol_node', label

    if 'Range' in label:
        # "1 Range , input: [0, 6], rsm: [S\_0, S\_4]" -> R^{q_0,0}_{q_4,6}
        m_inp = re.search(r'input: \[(\d+), (\d+)\]', label)
        m_rsm = re.search(r'rsm: \[(\w+)\\\_(\d+), (\w+)\\\_(\d+)\]', label)
        if m_inp and m_rsm:
            q_from = _rename_rsm(m_rsm.group(1) + '_' + m_rsm.group(2))
            q_to   = _rename_rsm(m_rsm.group(3) + '_' + m_rsm.group(4))
            v_from = m_inp.group(1)
            v_to   = m_inp.group(2)
            return 'prod_node', f'$R^{{{q_from},{v_from}}}_{{{q_to},{v_to}}}$'
        if m_inp:
            return 'prod_node', f'$[{m_inp.group(1)},{m_inp.group(2)}]$'
        return 'prod_node', ''

    if 'Intermediate' in label:
        # "2 Intermediate input: 2, rsm: S\_3, input: [0, 6]"
        # Use first "input:" (the split position), not the second (node range).
        m = re.search(r'^\d+\s+Intermediate input: (\d+), rsm: (\w+)\\\_(\d+)', label)
        if m:
            v = m.group(1)
            q = _rename_rsm(m.group(2) + '_' + m.group(3))
            return 'intermediate_node', f'$I_{{{q},{v}}}$'
        return 'intermediate_node', 'I'

    if 'Epsilon' in label:
        m = re.search(r'input: \[(\d+), (\d+)\]', label)
        if m:
            return 'symbol_node', f'$\\varepsilon_{{{m.group(1)}}}$'
        return 'symbol_node', '$\\varepsilon$'

    if 'Terminal' in label:
        m_term = re.search(r"Terminal '(\w+)'", label)
        m_range = re.search(r'input: \[(\d+), (\d+)\]', label)
        if m_term and m_range:
            return 'symbol_node', f'${m_term.group(1)}_{{{m_range.group(1)},{m_range.group(2)}}}$'
        return 'symbol_node', label

    return 'symbol_node', label


def process_tikz(content):
    """Process tikz content, replacing node styles and labels."""
    lines = content.split('\n')
    out = []

    for line in lines:
        m = re.match(r'(\s*)\\node\[draw\]\s*\((\w+)\)\s*(\[.*?\])?\s*\{(.+)\};', line)
        if m:
            indent = m.group(1)
            name = m.group(2)
            pos = m.group(3) or ''
            label = m.group(4)

            style, clean_label = classify_and_clean(label)

            if pos:
                out.append(f'{indent}\\node[{style}] ({name}) {pos} {{{clean_label}}};')
            else:
                out.append(f'{indent}\\node[{style}] ({name}) {{{clean_label}}};')
        else:
            out.append(line)

    return '\n'.join(out)


def main():
    if len(sys.argv) != 3:
        print('Usage: python3 clean_sppf_tikz.py input.tex output.tex')
        sys.exit(1)

    with open(sys.argv[1]) as f:
        content = f.read()

    result = process_tikz(content)

    with open(sys.argv[2], 'w') as f:
        f.write(result)

    print(f'Processed {sys.argv[1]} -> {sys.argv[2]}')


if __name__ == '__main__':
    main()
