#!/usr/bin/env python3
"""Elidiert die franzoesische Glossenspalte, wo sie es muss?

    elision.py [<buchNr> ...] [--setzen]

## Der Anlass

Beim Einsammeln von Matteo Paket 1 stand `perché si adempisse` dreimal
zeichengleich im Text und trug zweimal fr *s'accomplisse*, einmal
*se accomplisse*. `folgencheck.py` hat genau diese eine Stelle gemeldet,
weil sie in einer wiederholten Folge lag — die uebrigen 44 Stellen
derselben Art sah kein Werkzeug, weil sie in keiner Wiederholung stehen.

Die Gegenprobe an den fertigen Ausgaben zeigte, dass es dort nie
entschieden worden war: `deu/l1912mod` steht im NT 1754 zu 1313 und
`eng/web` 1992 zu 1344 — beide etwa 57 zu 43 gespalten. Fuer den
italienischen Durchgang ist entschieden worden, **durchgehend zu
elidieren**; dieses Werkzeug haelt das nach.

## Was geprueft wird

Zwei benachbarte EINZELWORT-Eintraege. Traegt der erste eine der zehn
elidierbaren Formen und beginnt die Glosse des zweiten mit einem Vokal,
gehoert die elidierte Form hin. Mehrwoerter bleiben aussen vor: ihre
Glosse ist ein ganzer Ausdruck und schreibt die Elision schon aus.

**Die Nachbarschaft der Eintraege ist nicht die Wortstellung des
Franzoesischen.** Wo die Zielsprache umstellt, steht die gemeldete
Glosse im fertigen Satz gar nicht nebeneinander — dann ist der Treffer
falsch. Er ist ein Verdacht wie ueberall sonst.

## Das aspirierte h

`la hache` ist richtig, `l'homme` auch. Welches `h` aspiriert ist, wird
**am franzoesischen Quelltext gemessen**, nicht geraten: wo LSG selbst
`le`/`la`/`de` voll davorstellt, ist es aspiriert; wo sie elidiert,
stumm. Das ergibt 156 aspirierte Formen mit 641 Belegen. Vier Namen
stehen in beiden Listen — LSG ist dort mit sich selbst uneins; sie
gelten als aspiriert, damit das Werkzeug lieber schweigt als falsch
meldet.
"""
import argparse
import collections
import json
import os
import re
import sys

import common as C

ELIDIERT = {'se': "s'", 'me': "m'", 'te': "t'", 'ne': "n'", 'le': "l'",
            'la': "l'", 'de': "d'", 'que': "qu'", 'ce': "c'", 'je': "j'"}
VOKAL = set('aeiouáàâäéèêëíìîïóòôöúùûü')

_h = None


def h_aspiriert():
    """{form} — die h-Woerter, vor denen LSG NICHT elidiert."""
    global _h
    if _h is not None:
        return _h
    asp, muet = collections.Counter(), collections.Counter()
    for nr in range(1, 67):
        p = C.text_pfad('fra/lsg1910mod', nr)
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding='utf-8'))
        for kap, vv in d['chapters'].items():
            for v, t in vv.items():
                for m in re.finditer(
                        r"\b(?:le|la|de|que|ne|se|me|te|ce|je)\s+(h\w+)", t, re.I):
                    asp[m.group(1).lower()] += 1
                for m in re.finditer(r"\b[ldqnsmtcj]['’](h\w+)", t, re.I):
                    muet[m.group(1).lower()] += 1
    # Uneinigkeit gilt als aspiriert — lieber schweigen als falsch melden.
    _h = set(asp)
    return _h


def vokalisch(w):
    w = (w or '').lstrip('«»"\'’ ').lower()
    if not w:
        return False
    if w[0] in VOKAL:
        return True
    if w[0] == 'h':
        wort = re.match(r"h[\w'’-]*", w)
        return bool(wort) and wort.group(0) not in h_aspiriert()
    return False


def pruefe(buecher):
    treffer = []
    for nr in buecher:
        try:
            d = C.load_anno(nr)['chapters']
        except Exception:
            continue
        for kap, vv in d.items():
            for v, ee in vv.items():
                einzel = {e['pos']: e for e in ee if not C.is_multi(e)}
                for pos, e in sorted(einzel.items()):
                    fr = (e.get('fr') or '').strip()
                    if fr.lower() not in ELIDIERT:
                        continue
                    nx = einzel.get(pos + 1)
                    if not nx or not vokalisch(nx.get('fr')):
                        continue
                    soll = ELIDIERT[fr.lower()]
                    if fr[:1].isupper():
                        soll = soll[:1].upper() + soll[1:]
                    treffer.append((nr, kap, v, pos, e.get('form'), fr, soll,
                                    nx.get('fr')))
    return treffer


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buecher', nargs='*', type=int)
    p.add_argument('--setzen', action='store_true',
                   help='die Aufrufe fuer setzen.py ausgeben')
    a = p.parse_args()
    buecher = a.buecher or sorted(C.anno_books())
    treffer = pruefe(buecher)
    if a.setzen:
        for nr, kap, v, pos, form, fr, soll, nach in treffer:
            print(f'python3 setzen.py {nr} {kap} {v} {pos} "{form}" '
                  f'fr="{soll}" --grund "franzoesische Elision vor {nach}"')
    else:
        for nr, kap, v, pos, form, fr, soll, nach in treffer:
            print(f'  {nr},{kap},{v:>3} pos{pos:<3} {form:14} '
                  f'fr {fr!r:6} -> {soll!r:6}   vor {nach!r}')
    print()
    print(f'{len(treffer)} nicht elidierte Stellen in '
          f'{len(buecher)} Buch/Buechern. Jede ist ein Verdacht: wo die '
          f'Zielsprache\numstellt, stehen die beiden Glossen im fertigen '
          f'Satz nicht nebeneinander.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
