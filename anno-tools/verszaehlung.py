"""Verszaehlung eines Buches gegen die vier Ausgaben — die Ausrichtungskarte.

    verszaehlung.py <buchNr> | alle

## Wozu

Bis Hiob hat jeder Agent stillschweigend angenommen, dass Vers 12 in allen
fuenf Ausgaben derselbe Vers ist. In Hiob 38-41 stimmte das nicht, im Psalter
war es der Normalfall (104 von 150 Psalmen), und in den Spruechen stimmte es
ueberall. Man kann es also nicht raten — man muss es messen, **bevor** das
erste Kapitel laeuft.

`ausgaben.py` richtet einen einzelnen Vers aus. Dieses Werkzeug gibt die Karte
fuer ein ganzes Buch: welche Kapitel wackeln, um wie viel, und in welcher
Ausgabe. Was es meldet, gehoert in das WORTFELD des Buches und in die Prompts
der betroffenen Kapitel.

## Wie zu lesen

`de 21 · en 21 · es 21 · fr 20 · it 21` heisst: das Franzoesische hat einen
Vers weniger. Ob er vorn, hinten oder in der Mitte fehlt, sagt erst
`ausgaben.py <nr> <kap>` — dieses Werkzeug zaehlt nur.

**Ein fehlendes Kapitel ist der schwerere Fall.** Joel und Maleachi teilen im
Deutschen anders als die Ausgaben; dort verschiebt sich nicht ein Vers, sondern
ein ganzer Block ueber die Kapitelgrenze.
"""
import sys

import common as C

AUSGABEN = [('en', 'eng/web', 'web'), ('es', 'spa/rv1909mod', 'rv1909mod'),
            ('fr', 'fra/lsg1910', 'lsg1910'), ('it', 'ita/riv1927', 'riv1927')]


def _lade(lang_pfad, kuerzel, nr):
    import json
    import os
    p = os.path.join(C.REPO, 'bibles', lang_pfad, f'{nr}_{kuerzel}.json')
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f)['chapters']


def karte(nr):
    de = C.load_source(nr)['chapters']
    ausg = {}
    for lang, pfad, kuerzel in AUSGABEN:
        ausg[lang] = _lade(pfad, kuerzel, nr)
    zeilen = []
    fehlende_kapitel = []
    for lang, ch in ausg.items():
        if ch is None:
            fehlende_kapitel.append(f'{lang}: Datei fehlt')
        elif len(ch) != len(de):
            fehlende_kapitel.append(f'{lang}: {len(ch)} Kapitel statt {len(de)}')
    for k in sorted(de, key=int):
        n = len(de[k])
        row = {}
        for lang, ch in ausg.items():
            row[lang] = None if ch is None else len(ch.get(k, {}))
        if any(v != n for v in row.values()):
            zeilen.append((k, n, row))
    return de, zeilen, fehlende_kapitel


def main():
    ziel = sys.argv[1]
    nrs = C.anno_books() if ziel == 'alle' else [int(ziel)]
    for nr in nrs:
        name = C.load_source(nr)['name']
        de, zeilen, fk = karte(nr)
        print(f'# {name} ({nr}) — {len(de)} Kapitel')
        if fk:
            print('\n**Abweichende Kapitelzahl:** ' + ' · '.join(fk))
            print('Dort verschiebt sich ein ganzer Block ueber die '
                  'Kapitelgrenze, nicht nur ein Vers.')
        if not zeilen:
            print('\nAlle Kapitel stimmen in der Verszahl mit allen vier '
                  'Ausgaben ueberein — keine Ausrichtungsfalle.\n')
            continue
        print(f'\n{len(zeilen)} von {len(de)} Kapiteln weichen ab:\n')
        print('| Kapitel | de | en | es | fr | it |')
        print('|---|---|---|---|---|---|')
        for k, n, row in zeilen:
            zellen = []
            for lang in ('en', 'es', 'fr', 'it'):
                v = row[lang]
                zellen.append('—' if v is None else
                              (f'**{v}**' if v != n else str(v)))
            print(f'| {k} | {n} | ' + ' | '.join(zellen) + ' |')
        print('\n`ausgaben.py <nr> <kap>` sagt, **wo** der Vers fehlt.\n')


if __name__ == '__main__':
    main()
