"""Abschnittsgrenzen: welche Inhaltswörter weichen links und rechts ab.

    crosscheck.py <datei.json> <grenze> [<grenze> …]
    crosscheck.py <buchNr> <kapitel> <grenze> [<grenze> …]

Für Kapitel, die zwei Agenten in Hälften bearbeitet haben. `grenze` ist die
Versnummer, ab der der nächste Abschnitt beginnt.

Es findet **keine Fehler, sondern Divergenzen**, die man ansehen muss: In Lukas
waren es zwischen 2 und 32 Inhaltswörter je Kapitel, durchweg berechtigte
Kontextvarianten (`hören` als *hear* vs. *listen*, `redete` punktuell vs.
durativ) — kein einziger Fall war eine verrutschte Zuordnung.

Funktionswörter bleiben ausgeblendet: Artikel, Pronomen und Präpositionen
weichen legitim ständig ab und würden die echten Fälle zudecken.
"""
import collections
import json
import sys

import common as C
import hints


def lade(args):
    if args[0].isdigit() and args[1].isdigit() and len(args) > 2:
        nr, kap = int(args[0]), int(args[1])
        data = C.load_quelle(nr, kap)
        if data is None:
            data = C.load_anno(nr)['chapters'][str(kap)]
        return data, [int(g) for g in args[2:]]
    with open(args[0], encoding='utf-8') as f:
        data = json.load(f)
    if 'chapters' in data:
        raise SystemExit('Bitte eine Kapiteldatei angeben, keine Buchdatei')
    return data, [int(g) for g in args[1:]]


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    data, grenzen = lade(sys.argv[1:])

    def abschnitt(v):
        i = 0
        for g in grenzen:
            if int(v) >= g:
                i += 1
        return i

    lesarten = collections.defaultdict(lambda: collections.defaultdict(list))
    for vers, entries in data.items():
        for e in entries:
            if C.is_multi(e) or e['lemma'].lower() in hints.FUNKTION:
                continue
            key = tuple(e[l] for l in C.LANGS)
            lesarten[e['lemma']][key].append((abschnitt(vers), vers))

    n = 0
    for lemma, gruppen in sorted(lesarten.items()):
        abschnitte = {a for stellen in gruppen.values() for a, _ in stellen}
        if len(gruppen) < 2 or len(abschnitte) < 2:
            continue
        # nur melden, wenn die Lesarten sich auf die Abschnitte verteilen
        pro_gruppe = [{a for a, _ in stellen} for stellen in gruppen.values()]
        if all(len(s) > 1 for s in pro_gruppe):
            continue
        n += 1
        print(f'`{lemma}`')
        for key, stellen in sorted(gruppen.items(), key=lambda x: -len(x[1])):
            orte = ', '.join(f'A{a+1}:{v}' for a, v in stellen[:6])
            print(f'   en *{key[0]}* · es *{key[1]}* · fr *{key[2]}* · it *{key[3]}*'
                  f'   — {orte}')
    print(f'\n{n} Inhaltswörter laufen über die Abschnittsgrenze auseinander.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
