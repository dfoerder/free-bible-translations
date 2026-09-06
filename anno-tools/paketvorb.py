#!/usr/bin/env python3
"""Die Bindungstabelle eines Pakets — was es praegt und was es uebernimmt.

    paketvorb.py <buchNr> <kapitel> [<kapitel> ...] [-o datei]

## Der Anlass

`wiederholungen.py` gibt die Wortfolgen eines ganzen Buches — in
Matthaeus sind das **503**, 45 KB. Kein Kapitelagent braucht alle, und
keiner soll sie durchsuchen muessen; in Maleachi habe ich genau diese
Liste mit `tail -40` gelesen und die haeufigste Folge dabei verloren.

Dieses Werkzeug schneidet den Teil heraus, der ein Paket angeht, und
trennt ihn in die zwei Faelle, die verschieden zu behandeln sind:

    PRAEGT       der frueheste Ort der Folge liegt in DIESEM Paket.
                 Das Paket entscheidet die Reihe fuer alle spaeteren.
    UEBERNIMMT   der frueheste Ort liegt in einem Kapitel, das schon
                 annotiert ist. Dann steht die Reihe fest und wird
                 zeichengleich uebernommen — sie wird hier **gemessen**,
                 nicht aus dem Gedaechtnis geschrieben.

Fuer den zweiten Fall zaehlt es jede Variante mit ihrer Zahl aus
(`folgenreihe.stellen`). Wo der Bestand selbst schwankt, steht das da —
dann entscheidet der Vers, und die Vorgabe sagt es ausdruecklich.
"""
import argparse
import collections
import re
import sys

import common as C
import folgenreihe as F
import wiederholungen as W


def folgen(nr, minlen=4, ab=2):
    """[(folge, [(kap, vers), …])] aus wiederholungen.py, haeufigste zuerst."""
    d = C.load_source(nr)['chapters']
    quelle = []
    for k in sorted(d, key=int):
        for v in sorted(d[k], key=int):
            quelle.append((f'{k},{v}', W.TOKEN.findall(d[k][v])))
    out = []
    for _laenge, orte, phr in W.folgen(quelle, minlen):
        if len(orte) < ab:
            continue
        out.append((phr, [tuple(o.split(',')) for o in orte]))
    return out


def _reihe(phr):
    """Die gemessenen Glossenreihen einer Folge im fertigen Bestand."""
    _w, voll, orte, unvoll, mehrwort = F.stellen(phr)
    return voll, orte, unvoll, mehrwort


def bericht(nr, kaps):
    kaps = {str(k) for k in kaps}
    fertig = set()
    for kap in C.quellen_kapitel(nr):
        fertig.add(str(kap))
    fertig -= kaps

    L = [f'# Bindungen fuer Buch {nr}, Kapitel {", ".join(sorted(kaps, key=int))}',
         '']
    praegt, uebernimmt, spaeter = [], [], []
    for phr, stellen in folgen(nr):
        beruehrt = [s for s in stellen if s[0] in kaps]
        if not beruehrt:
            continue
        erst = min(stellen, key=lambda s: (int(s[0]), int(s[1])))
        if erst[0] in kaps:
            praegt.append((phr, stellen, erst))
        elif erst[0] in fertig:
            uebernimmt.append((phr, stellen, erst))
        else:
            spaeter.append((phr, stellen, erst))

    L.append(f'**{len(praegt)} praegt · {len(uebernimmt)} uebernimmt · '
             f'{len(spaeter)} haengt an einem noch nicht annotierten Kapitel**')
    L.append('')

    if uebernimmt:
        L.append('## UEBERNIMMT — die Reihe steht schon fest')
        L.append('')
        L.append('Der frueheste Ort ist annotiert. Diese Reihen sind **gemessen**, '
                 'nicht erinnert. Wo mehrere Varianten stehen, schwankt der '
                 'Bestand selbst — dann entscheidet der Vers.')
        L.append('')
        for phr, stellen, erst in uebernimmt:
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            L.append(f'### „{phr}"   (zuerst {erst[0]},{erst[1]} — '
                     f'hier: {", ".join(hier)})')
            voll, orte, unvoll, _ = _reihe(phr)
            if not voll:
                L.append('- im Bestand noch nicht vollstaendig belegt')
            for key, n in voll.most_common():
                zeile = ' | '.join(' '.join(t) for t in key)
                L.append(f'- {n}×  {zeile}')
            if unvoll:
                L.append(f'- {len(unvoll)} Vorkommen unvollstaendig '
                         '(dort liegt ein Mehrwort)')
            L.append('')

    if praegt:
        L.append('## PRAEGT — dieses Paket entscheidet')
        L.append('')
        L.append('Der frueheste Ort liegt hier. Was gesetzt wird, gilt fuer alle '
                 'spaeteren Vorkommen im ganzen Buch — **innerhalb des Pakets '
                 'zeichengleich**.')
        L.append('')
        for phr, stellen, erst in sorted(praegt, key=lambda x: -len(x[1])):
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            spaet = len(stellen) - len(hier)
            L.append(f'- **„{phr}"** — {erst[0]},{erst[1]} legt fest · hier: '
                     f'{", ".join(hier)}'
                     + (f' · spaeter noch {spaet}×' if spaet else ''))
        L.append('')

    if spaeter:
        L.append('## HAENGT AN EINEM SPAETEREN KAPITEL')
        L.append('')
        L.append('Der frueheste Ort ist noch nicht annotiert. **Nicht praegen** — '
                 'diese Folge entscheidet ein anderes Paket; hier nur den Vers '
                 'lesen und die naheliegende Reihe setzen.')
        L.append('')
        for phr, stellen, erst in spaeter:
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            L.append(f'- „{phr}" — zuerst {erst[0]},{erst[1]} · hier: '
                     f'{", ".join(hier)}')
        L.append('')
    return '\n'.join(L)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel', nargs='+')
    p.add_argument('-o', '--out')
    a = p.parse_args()
    txt = bericht(a.buch, a.kapitel)
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(txt)
        print(f'{a.out} geschrieben ({len(txt)} Zeichen)')
    else:
        sys.stdout.write(txt)
