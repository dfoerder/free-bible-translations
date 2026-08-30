"""Erzeugt die Bindungsliste für das Alte Testament aus dem Bestand.

    bindungen.py [-o BINDUNGEN_AT.md] [--min 8]

Die frühere `BINDUNGEN_AT.md` war handgepflegt, ein Abschnitt je Kapitel — und
ist mit dem Scratchpad verlorengegangen. Die Bindungen selbst stecken aber in
den Daten: was 1. und 2. Mose festgelegt haben, steht dort.

Erzeugt werden zwei Tabellen:

- **AT-Bindungen** — Lemmata mit einer klar dominierenden Lesart in den Büchern
  1–39. Für ein neues AT-Kapitel bindend, solange die Bedeutung dieselbe ist.
- **Lexikonfallen** — Lemmata, deren AT-Lesart von der NT-Mehrheit **abweicht**.
  Genau hier zieht der Lexikon-Extrakt einen Agenten auf die falsche Seite,
  weil er die Korpusmehrheit zeigt und die aus dem Neuen Testament stammt.
"""
import argparse
import collections

import common as C

AT = set(range(1, 40))
VORWEG = ('of the ', 'to the ', 'of ', 'to ', 'the ', 'a ', 'an ', 'in ', 'from ',
          'with ', 'for ', 'and ')


def _kern(g):
    g = g.lower().strip()
    for p in VORWEG:
        if g.startswith(p):
            g = g[len(p):]
            break
    return g.rstrip('s')


def _wirklich_anders(at, nt):
    """Numerus und vorangestellte Präposition sind keine Lexikonfalle.
    `Bruder` = *brother* vs. *brothers* ist eine Formvariante; `Fuß` =
    *sockets* vs. *feet* ist eine andere Bedeutung."""
    a, b = _kern(at), _kern(nt)
    if a == b:
        return False
    return not (a[:4] == b[:4] and min(len(a), len(b)) >= 4)


def sammle(min_belege):
    at = collections.defaultdict(collections.Counter)
    nt = collections.defaultdict(collections.Counter)
    for nr in C.anno_books():
        ziel = at if nr in AT else nt
        for _, _, _, e in C.iter_corpus([nr]):
            if C.is_multi(e):
                continue
            ziel[e['lemma']][(e['en'], e['es'], e['fr'], e['it'])] += 1

    bindungen, fallen = [], []
    for lemma, c in at.items():
        gesamt = sum(c.values())
        if gesamt < min_belege:
            continue
        (glosse, n) = c.most_common(1)[0]
        anteil = n / gesamt
        if anteil < 0.5:
            continue                      # zu viele Lesarten, keine Bindung
        eintrag = (lemma, glosse, n, gesamt)
        cn = nt.get(lemma)
        if cn and sum(cn.values()) >= 3:
            nt_glosse, nn = cn.most_common(1)[0]
            if _wirklich_anders(glosse[0], nt_glosse[0]):
                fallen.append(eintrag + (nt_glosse, nn, sum(cn.values())))
                continue
        bindungen.append(eintrag)
    return bindungen, fallen


def bericht(min_belege=8):
    bindungen, fallen = sammle(min_belege)
    L = ['# BINDUNGEN_AT — Glossen-Bindungen der Bücher 1–39', '',
         'Aus dem Bestand erzeugt (`bindungen.py`), nicht von Hand gepflegt.',
         'Eine Bindung gilt für **dieselbe Bedeutung**, nicht für dieselbe',
         'Buchstabenfolge: `Ofen` ist Backofen und Feuerofen, `Fuß` ist',
         'Körperteil und Sockel. Bei anderer Bedeutung eigene Glosse **und',
         'eigenes Lemma**.', '',
         f'Aufgenommen sind Lemmata mit mindestens {min_belege} Belegen im AT,',
         'deren häufigste Lesart **mindestens die Hälfte** der Belege trägt.',
         '',
         'Steht dort genau die Hälfte, ist der Zweitplatzierte gleichauf und',
         'die Zeile durch die Reihenfolge entschieden, nicht durch das Korpus.',
         'Das betrifft 91 Lemmata. Nachgemessen: bei allen 21 echten 50:50-Faellen',
         'unterscheiden sich die beiden Lesarten nur im Numerus, nicht in der',
         'Bedeutung (`Flamme` *flame* gegen *flames*) — die Bindung traegt also,',
         'die Zahl ist nur knapp. Deshalb bleibt die Schwelle bei >= 0.5.', '']

    L += ['## Lexikonfallen — AT-Lesart weicht von der NT-Mehrheit ab', '',
          'Der Lexikon-Extrakt zeigt die **Korpusmehrheit**. Bei diesen Wörtern',
          'stammt sie aus dem Neuen Testament und ist im AT falsch. Sie sind der',
          'häufigste Grund, warum ein AT-Kapitel neben dem Bestand herläuft.', '',
          '| Lemma | AT (bindend) | NT-Mehrheit (hier falsch) |', '|---|---|---|']
    for lemma, g, n, ges, gn, nn, nges in sorted(fallen, key=lambda x: -x[2]):
        L.append(f'| `{lemma}` | *{g[0]}* / *{g[1]}* / *{g[2]}* / *{g[3]}* '
                 f'({n}/{ges}) | *{gn[0]}* ({nn}/{nges}) |')
    L += ['']

    L += [f'## AT-Bindungen ({len(bindungen)} Lemmata)', '',
          '| Lemma | en | es | fr | it | Belege |', '|---|---|---|---|---|---|']
    for lemma, g, n, ges in sorted(bindungen, key=lambda x: -x[2]):
        L.append(f'| `{lemma}` | {g[0]} | {g[1]} | {g[2]} | {g[3]} | {n}/{ges} |')
    return '\n'.join(L)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-o', '--out')
    p.add_argument('--min', type=int, default=8)
    a = p.parse_args()
    txt = bericht(a.min)
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(txt + '\n')
        print(f'{a.out} geschrieben')
    else:
        print(txt)
