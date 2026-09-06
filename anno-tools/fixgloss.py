"""Alle Lesarten eines Lemmas oder einer Wortform mit Belegstellen.

    fixgloss.py show <lemma> [<lemma> …]
    fixgloss.py showform <form> [<form> …]
    fixgloss.py verse <buchNr> <kapitel> <vers>

Grundlage für jede korpusweite Entscheidung: **vor jedem Zug die Belegverse
lesen.** Manche Spaltung sieht aus wie ein Fehler und ist richtig (`Herde` =
*herd* sind die Schweine von Gadara, `weiden` = *rule* ist die Hirtenmetapher
der Offenbarung).
"""
import collections
import sys

import common as C


def _zeig(idx, titel):
    if not idx:
        print(f'{titel}: nichts gefunden')
        return
    print(f'## {titel}')
    for key, stellen in sorted(idx.items(), key=lambda x: -len(x[1])):
        lemma, level, glossen = key[0], key[1], key[2:]
        print(f'{len(stellen):>4}× · lemma `{lemma}` · {level} · {C.zeige(glossen)}')
        print('       ' + ', '.join(stellen[:8]) + (' …' if len(stellen) > 8 else ''))
    print()


def show(lemmata, per_form=False):
    for ziel in lemmata:
        idx = collections.defaultdict(list)
        for nr in C.anno_books():
            name = C.load_source(nr)['name']
            for _, kap, vers, e in C.iter_corpus([nr]):
                treffer = (e['form'] == ziel) if per_form else (e['lemma'] == ziel)
                if treffer:
                    key = (e['lemma'], e['level']) + C.reihe(e)
                    idx[key].append(f'{name} {kap},{vers}')
        _zeig(idx, ('Form ' if per_form else 'Lemma ') + ziel)


def verse(nr, kap, vers):
    src = C.load_source(nr)['chapters'][str(kap)][str(vers)]
    print(src)
    for e in C.load_anno(nr)['chapters'][str(kap)][str(vers)]:
        span = (f'{e["pos"]}-{e["pos_end"]}' if 'pos_end' in e
                else (str(e['parts']) if 'parts' in e else str(e['pos'])))
        print(f'  {span:>8}  {e["form"]:<22} {e["lemma"]:<20} {e["level"]}  '
              f'en {e["en"]} · es {e["es"]} · fr {e["fr"]} · it {e["it"]}')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    modus = sys.argv[1]
    if modus == 'show':
        show(sys.argv[2:])
    elif modus == 'showform':
        show(sys.argv[2:], per_form=True)
    elif modus == 'verse':
        verse(*sys.argv[2:5])
    else:
        print(__doc__)
        sys.exit(1)
