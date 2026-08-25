"""Parallelkapitel als gemessene Vorlage — Vers für Vers, mit Versatz.

    vorlage.py <nrA> <kapA> <nrB> <kapB> [minratio]

A ist das **neue** Kapitel, B das **fertig annotierte**. Für jeden Vers von A
wird der ähnlichste Vers von B gesucht und beides nebeneinandergestellt, dazu
die Einträge von B mit ihren Tokenpositionen.

Entstanden für Nehemia 7 ↔ Esra 2: 56 der 73 Verse sind zu über 75 Prozent
wortgleich, aber die Verszählung ist verschoben und einzelne Sippen stehen in
anderer Reihenfolge (Neh 7,22·23·24 ↔ Esra 2,19·17·18). Genau die Konstellation,
an der in 1. Chronik die Blockpositionen verrutscht sind.

Zwei Warnungen, die zur Ausgabe gehören:

- **Die Zahlen weichen ab.** Esra 2 und Nehemia 7 nennen für dieselbe Sippe
  vielfach verschiedene Summen. Der Wortlaut ist übertragbar, die Zahl nie.
- **Wortgleich ist nicht bedeutungsgleich.** Esra 5,14 und 6,5 teilen einen
  18-Token-Block `aus dem Tempel` und meinen zwei verschiedene Tempel.
"""
import difflib
import sys

import common as C


def norm(t):
    return [C.strip_punct(x) for x in t.split()]


nrA, kapA, nrB, kapB = sys.argv[1:5]
minr = float(sys.argv[5]) if len(sys.argv) > 5 else 0.4

srcA = C.load_source(nrA)['chapters'][kapA]
srcB = C.load_source(nrB)['chapters'][kapB]
annoB = C.load_anno(nrB)['chapters'][kapB]

print(f'# {C.book_name(nrA)} {kapA} ← Vorlage {C.book_name(nrB)} {kapB}\n')
print('Die Zahlen weichen zwischen den Fassungen ab — der Wortlaut ist')
print('übertragbar, die Zahl nie. Jede Zeile am eigenen Vers nachrechnen.\n')

treffer = 0
for v in sorted(srcA, key=int):
    a = norm(srcA[v])
    best = (0.0, None)
    for w in sorted(srcB, key=int):
        r = difflib.SequenceMatcher(None, a, norm(srcB[w])).ratio()
        if r > best[0]:
            best = (r, w)
    r, w = best
    if w is None or r < minr:
        print(f'## {kapA},{v}  — keine Vorlage (beste Ähnlichkeit {r:.2f})')
        print(f'   {srcA[v]}\n')
        continue
    treffer += 1
    b = norm(srcB[w])
    sm = difflib.SequenceMatcher(None, a, b)
    print(f'## {kapA},{v} ← {kapB},{w}   Ähnlichkeit {r:.2f}')
    print(f'   neu : {srcA[v]}')
    print(f'   alt : {srcB[w]}')
    for bl in sm.get_matching_blocks():
        if bl.size >= 2:
            print(f'   Block A-pos {bl.a} ← B-pos {bl.b}, Länge {bl.size}, '
                  f'Versatz {bl.b - bl.a:+d}: `{" ".join(a[bl.a:bl.a + bl.size])}`')
    for e in annoB.get(w, []):
        pos = e.get('parts') or ([e['pos'], e['pos_end']] if 'pos_end' in e else [e['pos']])
        print(f"   B-pos {str(pos):<10} {e['form']:<18} {e['lemma']:<18} {e['level']}  "
              f"{e['en']} · {e['es']} · {e['fr']} · {e['it']}")
    print()

print(f'{treffer} von {len(srcA)} Versen haben eine Vorlage ab Ähnlichkeit {minr}.')
