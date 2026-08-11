"""Hilfsverb, dessen Glosse das Vollverb des Nachbartokens verschluckt.

    hilfsverb.py <buchNr …> | alle

„ich **würde** **sterben**": an `würde` stand die volle Verbform
*moriría/mourrais/morirei*, und im Lesefluss stand an beiden Tokens dasselbe
Verb. `qa.py` sieht das nicht — strukturell ist der Eintrag perfekt, und die
Glossen sind nicht identisch, sondern nur **stammgleich**.

Gesucht wird: ein Hilfsverb (`werden`, `sollen`, `wollen`, `können`, `müssen`,
`dürfen`, `mögen`, `lassen`, `haben`, `sein`), dessen Glosse mit der Glosse
eines Vollverbs im selben Vers den Wortstamm teilt.

Der erste Lauf über den gesamten Bestand ergab vier Verdachtsfälle und zwei
echte Fehler (1Mo 19,19 · 1Kor 14,25), beide periphrastisch korrigiert
(*iba a / allais / stavo per* + Infinitiv).
"""
import argparse

import common as C

HILFSVERBEN = {'werden', 'sollen', 'wollen', 'können', 'müssen', 'dürfen',
               'mögen', 'lassen', 'haben', 'sein'}
MIN_STAMM = 5


def _stamm(g):
    w = g.lower().split()
    return w[-1][:MIN_STAMM] if w else ''


def pruefe(nrs):
    treffer = []
    for nr in nrs:
        name = C.load_source(nr)['name']
        d = C.load_anno(nr)['chapters']
        for kap, verses in d.items():
            for vers, entries in verses.items():
                einzel = [e for e in entries if not C.is_multi(e)]
                hilfs = [e for e in einzel if e['lemma'] in HILFSVERBEN]
                voll = [e for e in einzel if e['lemma'] not in HILFSVERBEN]
                for h in hilfs:
                    for v in voll:
                        if abs(h['pos'] - v['pos']) > 8:
                            continue
                        gleich = [l for l in C.LANGS
                                  if len(_stamm(h[l])) >= MIN_STAMM
                                  and _stamm(h[l]) == _stamm(v[l])]
                        if len(gleich) >= 2:
                            treffer.append((f'{name} {kap},{vers}', h, v, gleich))
    for wo, h, v, gleich in treffer:
        print(f'{wo}: {h["form"]!r} (pos {h["pos"]}) und {v["form"]!r} '
              f'(pos {v["pos"]}) stammgleich in {", ".join(gleich)}')
        for l in gleich:
            print(f'      {l}: {h[l]!r} / {v[l]!r}')
    print(f'\n{len(treffer)} Verdachtsfälle.')
    return treffer


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('args', nargs='+')
    a = p.parse_args()
    nrs = C.anno_books() if a.args[0] == 'alle' else [int(x) for x in a.args]
    pruefe(nrs)
