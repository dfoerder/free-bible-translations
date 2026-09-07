"""Alle Lesarten eines Lemmas oder einer Wortform mit Belegstellen.

    fixgloss.py show <lemma> [<lemma> …]
    fixgloss.py showform <form> [<form> …]
    fixgloss.py verse <buchNr> <kapitel> <vers> [--datei <ch.json>]

Grundlage für jede korpusweite Entscheidung: **vor jedem Zug die Belegverse
lesen.** Manche Spaltung sieht aus wie ein Fehler und ist richtig (`Herde` =
*herd* sind die Schweine von Gadara, `weiden` = *rule* ist die Hirtenmetapher
der Offenbarung).
"""
import collections
import json
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


def verse(nr, kap, vers, datei=None):
    """Ein annotierter Vers ganz — aus dem Bestand oder aus einer Datei.

    `--datei` kam mit Markus dazu. Drei Agenten hintereinander wollten
    einen Nachbarvers ihres eigenen Pakets lesen und bekamen
    `KeyError` — dieses Werkzeug liest den EINGESAMMELTEN Bestand, und
    das laufende Paket steht noch in `$ANNO_OUT`. Der Griff, den der
    Prompt als Standard nennt, funktionierte damit nur fuer fremde
    Buecher.
    """
    src = C.load_source(nr)['chapters'][str(kap)][str(vers)]
    print(src)
    if datei:
        d = json.load(open(datei, encoding='utf-8'))
        eintraege = d.get(str(vers)) or d.get('chapters', {}).get(
            str(kap), {}).get(str(vers))
        if eintraege is None:
            print(f'  Vers {vers} steht nicht in {datei}.')
            return
    else:
        try:
            anno = C.load_anno(nr)['chapters']
        except FileNotFoundError:
            anno = {}
        if str(kap) not in anno or str(vers) not in anno[str(kap)]:
            print(f'  {C.book_name(nr)} {kap},{vers} ist im Bestand noch '
                  f'nicht annotiert.\n  Liegt das Kapitel in $ANNO_OUT? '
                  f'Dann: fixgloss.py verse {nr} {kap} {vers} '
                  f'--datei $ANNO_OUT/{nr}/ch{kap}.json')
            return
        eintraege = anno[str(kap)][str(vers)]
    for e in eintraege:
        span = (f'{e["pos"]}-{e["pos_end"]}' if 'pos_end' in e
                else (str(e['parts']) if 'parts' in e else str(e['pos'])))
        print(f'  {span:>8}  {e["form"]:<22} {e["lemma"]:<20} {e["level"]}  '
              + ' · '.join(f'{l} {e[l]}' for l in C.LANGS))


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
        datei = None
        if '--datei' in sys.argv:
            i = sys.argv.index('--datei')
            datei = sys.argv[i + 1]
            del sys.argv[i:i + 2]
        if len(sys.argv) != 5:
            # Drei Agenten hintereinander sind darueber gestolpert: in
            # einer Shell-Schleife (`for a in "40 28 1"`) kommt alles als
            # EIN Argument an, und die blosse Aufrufhilfe sagt nicht,
            # dass das der Grund ist.
            if len(sys.argv) == 3 and len(sys.argv[2].split()) == 3:
                print(f'{sys.argv[2]!r} ist EIN Argument, nicht drei — in '
                      'einer Shell-Schleife zerlegt zsh die Variable nicht '
                      'am Leerzeichen.\nAufruf: fixgloss.py verse '
                      + ' '.join(sys.argv[2].split()))
            else:
                print('Aufruf: fixgloss.py verse <buchNr> <kapitel> <vers>  '
                      '— drei Argumente, einzeln')
            sys.exit(1)
        verse(*sys.argv[2:5], datei=datei)
    else:
        print(__doc__)
        sys.exit(1)
