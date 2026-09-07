"""Alle Lesarten eines Lemmas oder einer Wortform mit Belegstellen.

    fixgloss.py show <lemma> [<lemma> …]
    fixgloss.py showform <form> [<form> …]
    fixgloss.py verse <buchNr> <kapitel> <vers> [--datei <ch.json>]
    fixgloss.py mw [<teilwort> …]      alle Mehrwort-Lemmata

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


def mehrwoerter(woerter):
    """Alle MEHRWORT-Lemmata des Bestands, gefiltert nach Teilwort.

        fixgloss.py mw                 alle
        fixgloss.py mw avoir monde     alle, die `avoir` ODER `monde` enthalten

    Zwei Agenten hintereinander haben sich diese Liste selbst gebaut,
    weil `folgenreihe.py` die ZEICHENKETTE des Quelltextes sucht: `"n’y
    avait pas"` und `"mit au monde"` melden 0, obwohl `il y avoir` und
    `mettre au monde` im Bestand stehen — die Oberflaeche ist gebeugt,
    das Lemma nicht. Wer nur folgenreihe fragt, erfindet vorhandene
    Mehrwoerter neu.
    """
    idx = collections.defaultdict(collections.Counter)
    orte = collections.defaultdict(list)
    for nr, k, v, e in C.iter_corpus():
        if not C.is_multi(e):
            continue
        lem = e.get('lemma', '')
        key = (e.get('level', ''),) + C.reihe(e)
        idx[lem][key] += 1
        if len(orte[(lem, key)]) < 3:
            orte[(lem, key)].append(f'{C.book_name(nr)} {k},{v}')
    # Ein Argument mit Leerzeichen ist ein Mehrwortlemma, kein Filter:
    # `fixgloss.py mw se précipiter` fragt sonst `se` und `précipiter`
    # einzeln und schuettet hundert `se`-Zeilen aus. Gemeldet vom
    # Agenten fuer Luc 4.
    such = [w.lower().replace("'", '\u2019') for w in woerter]
    if len(such) > 1 and all(' ' not in w for w in woerter):
        print(f'(Hinweis: {len(woerter)} getrennte Teilwoerter, ODER-verknuepft. '
              f'Fuer EIN Mehrwortlemma in Anfuehrungszeichen setzen: '
              f'"{" ".join(woerter)}")')
    treffer = [l for l in idx
               if not such or any(w in l.lower() for w in such)]
    print(f'*{C.bestandsstand()}*')
    print(f'\n{len(treffer)} Mehrwort-Lemmata'
          + (f' mit {" oder ".join(woerter)}' if woerter else ' im Bestand')
          + f' (von {len(idx)})\n')
    for lem in sorted(treffer):
        ges = sum(idx[lem].values())
        print(f'## {lem}   {ges}×')
        for key, n in idx[lem].most_common(4):
            print(f'   {n:4}  [{key[0]}]  ' + ' · '.join(key[1:])
                  + '   ' + ', '.join(orte[(lem, key)]))
        if len(idx[lem]) > 4:
            print(f'   … und {len(idx[lem]) - 4} weitere Reihen')
        print()


if __name__ == '__main__':
    if len(sys.argv) < 2 or (len(sys.argv) < 3
                             and sys.argv[1] != 'mw'):
        print(__doc__)
        sys.exit(1)
    modus = sys.argv[1]
    if modus == 'show':
        show(sys.argv[2:])
    elif modus == 'showform':
        show(sys.argv[2:], per_form=True)
    elif modus == 'mw':
        mehrwoerter(sys.argv[2:])
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
