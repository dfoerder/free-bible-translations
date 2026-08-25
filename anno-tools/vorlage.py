"""Parallelkapitel als gemessene Vorlage — Vers für Vers, mit Versatz.

    vorlage.py <nrA> <kapA> <nrB> <kapB> [minratio]

A ist das **neue** Kapitel, B das **fertig annotierte**. Ausgegeben werden für
jeden Vers von A der Wortlaut beider Fassungen, die gemeinsamen Blöcke mit
gemessenem Versatz, **jede einzelne Abweichung** und die Einträge von B mit
ihren Tokenpositionen.

Entstanden für Nehemia 7 ↔ Esra 2: 56 der 73 Verse sind zu über 75 Prozent
wortgleich, aber die Verszählung ist verschoben und einzelne Sippen stehen in
anderer Reihenfolge. Genau die Konstellation, an der in 1. Chronik die
Blockpositionen verrutscht sind.

## Warum zwei Zuordnungen ausgegeben werden

Die erste Fassung suchte je Vers von A unabhängig den ähnlichsten Vers von B.
Bei einer Liste gleichgebauter Zeilen (`die Nachkommen von X: Zahl;`) trägt
das nicht: der Agent von Nehemia 7,1–40 hat **drei Fehlzuordnungen** gefunden.
Neh 7,15 (Binnui/648) bekam Esra 2,4 (Sephatja/372) bei Ähnlichkeit 0,60,
weil Name und Zahl abweichen und der Rest der Zeile in **jeder** Listenzeile
gleich lautet; die Sachparallele ist Esra 2,10. Ebenso 7,26 und 7,28.

Deshalb rechnet das Skript jetzt zusätzlich eine **ordnungserhaltende
Gesamtzuordnung** (Needleman-Wunsch über die Ähnlichkeitsmatrix). Sie kann
eine Zeile nicht überspringen, um eine zufällig ähnlichere weiter hinten zu
greifen — und trifft in genau den Fällen richtig, in denen die reine
Ähnlichkeit versagt.

Wo beide Verfahren dasselbe sagen, ist die Zuordnung belastbar. **Wo sie
auseinandergehen, steht ein ausdrücklicher Warnhinweis** — dort ist entweder
eine Umstellung im Text (Neh 7,22·23·24 ↔ Esra 2,19·2,17·2,18) oder eine
Fehlzuordnung des Ähnlichkeitsmaßes. Beides muss ein Mensch entscheiden.

## Zwei Warnungen, die zur Ausgabe gehören

- **Die Zahlen weichen ab**, und sie stehen als **ausgeschriebene Zahlwörter**
  da, nicht als Ziffern: `zweitausendachthundertzwölf` gegen
  `zweitausendachthundertachtzehn`. Keine Ziffernprüfung fängt das. Auch die
  Namen weichen ab (`Parevs`/`Pareos`, `Bani`/`Binnui`). Der Wortlaut ist
  übertragbar, die Zahl nie.
- **Wortgleich ist nicht bedeutungsgleich.** Esra 5,14 und 6,5 teilen einen
  18-Token-Block `aus dem Tempel` und meinen zwei verschiedene Tempel.
"""
import difflib
import sys

import common as C


def norm(t):
    return [C.strip_punct(x) for x in t.split()]


def aehnlichkeitsmatrix(va, vb, sa, sb):
    m = {}
    for i, v in enumerate(va):
        a = norm(sa[v])
        for j, w in enumerate(vb):
            m[(i, j)] = difflib.SequenceMatcher(None, a, norm(sb[w])).ratio()
    return m


def ordnungstreu(va, vb, m):
    """Needleman-Wunsch ohne Lückenstrafe: maximiert die Summe der
    Ähnlichkeiten unter der Bedingung, dass die Reihenfolge erhalten bleibt."""
    n, k = len(va), len(vb)
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + m[(i - 1, j - 1)],
                           dp[i - 1][j], dp[i][j - 1])
    paare, i, j = {}, n, k
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + m[(i - 1, j - 1)]:
            paare[va[i - 1]] = (vb[j - 1], m[(i - 1, j - 1)])
            i, j = i - 1, j - 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return paare


nrA, kapA, nrB, kapB = sys.argv[1:5]
minr = float(sys.argv[5]) if len(sys.argv) > 5 else 0.4

srcA = C.load_source(nrA)['chapters'][kapA]
srcB = C.load_source(nrB)['chapters'][kapB]
annoB = C.load_anno(nrB)['chapters'][kapB]

va = sorted(srcA, key=int)
vb = sorted(srcB, key=int)
m = aehnlichkeitsmatrix(va, vb, srcA, srcB)
ordnung = ordnungstreu(va, vb, m)

print(f'# {C.book_name(nrA)} {kapA} ← Vorlage {C.book_name(nrB)} {kapB}\n')
print('Die Zahlen weichen zwischen den Fassungen ab und stehen als')
print('ausgeschriebene Zahlwörter da — der Wortlaut ist übertragbar, die Zahl')
print('nie. Jede Zeile am eigenen Vers nachrechnen.\n')
print('Jede Zuordnung ist doppelt gerechnet: über die reine Ähnlichkeit und')
print('über eine ordnungserhaltende Gesamtzuordnung. **Wo beide auseinander-')
print('gehen, steht ein WARNUNG-Hinweis** — dort ist entweder der Text')
print('umgestellt oder das Ähnlichkeitsmaß irrt.\n')

treffer = strittig = 0
for idx, v in enumerate(va):
    a = norm(srcA[v])
    j_best = max(range(len(vb)), key=lambda j: m[(idx, j)])
    w_best, r_best = vb[j_best], m[(idx, j_best)]
    w_ord, r_ord = ordnung.get(v, (None, 0.0))

    # Die ordnungstreue Zuordnung hat Vorrang, sobald sie überhaupt greift.
    w, r = (w_ord, r_ord) if w_ord else (w_best, r_best)

    if w is None or r < minr:
        print(f'## {kapA},{v}  — keine Vorlage (beste Ähnlichkeit {r_best:.2f})')
        print(f'   {srcA[v]}\n')
        continue
    treffer += 1
    print(f'## {kapA},{v} ← {kapB},{w}   Ähnlichkeit {r:.2f}')
    if w_ord and w_best != w_ord:
        strittig += 1
        print(f'   **WARNUNG** — die reine Ähnlichkeit zeigt auf {kapB},{w_best} '
              f'({r_best:.2f}), die ordnungserhaltende Zuordnung auf {kapB},{w_ord} '
              f'({r_ord:.2f}). Entweder ist der Text hier umgestellt oder das')
        print(f'   Ähnlichkeitsmaß irrt. **Selbst entscheiden, bevor du etwas '
              f'überträgst.** Wortlaut von {kapB},{w_best}: {srcB[w_best]}')
        print(f'   Einträge der Gegenkandidatin {kapB},{w_best}:')
        for e in annoB.get(w_best, []):
            pos = e.get('parts') or ([e['pos'], e['pos_end']] if 'pos_end' in e else [e['pos']])
            print(f"      B-pos {str(pos):<10} {e['form']:<18} {e['lemma']:<18} "
                  f"{e['level']}  {e['en']} · {e['es']} · {e['fr']} · {e['it']}")
    b = norm(srcB[w])
    sm = difflib.SequenceMatcher(None, a, b)
    print(f'   neu : {srcA[v]}')
    print(f'   alt : {srcB[w]}')
    for bl in sm.get_matching_blocks():
        if bl.size >= 2:
            print(f'   Block A-pos {bl.a} ← B-pos {bl.b}, Länge {bl.size}, '
                  f'Versatz {bl.b - bl.a:+d}: `{" ".join(a[bl.a:bl.a + bl.size])}`')
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        links = ' '.join(a[i1:i2]) or '—'
        rechts = ' '.join(b[j1:j2]) or '—'
        print(f'   ABWEICHUNG A-pos {i1}: `{links}`   statt B-pos {j1}: `{rechts}`')
    for e in annoB.get(w, []):
        pos = e.get('parts') or ([e['pos'], e['pos_end']] if 'pos_end' in e else [e['pos']])
        print(f"   B-pos {str(pos):<10} {e['form']:<18} {e['lemma']:<18} {e['level']}  "
              f"{e['en']} · {e['es']} · {e['fr']} · {e['it']}")
    print()

print(f'{treffer} von {len(va)} Versen haben eine Vorlage ab Ähnlichkeit {minr}.')
print(f'{strittig} Zuordnungen sind strittig und mit WARNUNG markiert.')
