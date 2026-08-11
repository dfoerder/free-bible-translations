"""Selbstprüfung für Agenten: Kapiteldatei gegen den Quelltext.

    selfcheck.py <buchNr> <kapitel> <datei.json> [<vonVers> <bisVers>]

Ohne Versbereich wird Vollständigkeit über das ganze Kapitel verlangt.
Mit Versbereich nur über diesen Abschnitt (Teillieferung).

Rückgabewert 0 = sauber. Jeder Agent ruft das vor der Abgabe auf.
"""
import json
import sys

import common as C
import validate as V


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    nr, kap, pfad = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    von = int(sys.argv[4]) if len(sys.argv) > 4 else None
    bis = int(sys.argv[5]) if len(sys.argv) > 5 else None

    with open(pfad, encoding='utf-8') as f:
        data = json.load(f)
    if 'chapters' in data:                      # ganze Buchdatei geliefert
        data = data['chapters'][str(kap)]

    errs = V.validate_chapter(nr, kap, data, partial=False, von=von, bis=bis)
    src = C.load_source(nr)['chapters'][str(kap)]
    soll = [v for v in src if von is None or von <= int(v) <= bis]
    tok = sum(len(C.tokens(src[v])) for v in soll)
    zeichen = sum(1 for v in soll for t in C.tokens(src[v]) if C.is_punct_only(t))
    einzel = sum(len(C.singles(data[v])) for v in data if v in src)
    mehr = sum(len(C.multis(data[v])) for v in data if v in src)

    name = C.load_source(nr)['name']
    bereich = f'{kap}' + (f',{von}–{bis}' if von is not None else '')
    print(f'{name} {bereich}: {len(data)}/{len(soll)} Verse · {einzel} Einzelwort- '
          f'· {mehr} Mehrwort-Einträge')
    print(f'Gegenrechnung: {tok} Tokens − {einzel} Einzeleinträge = {tok - einzel} '
          f'(alleinstehende Satzzeichen: {zeichen}) — '
          + ('stimmt' if tok - einzel == zeichen else 'STIMMT NICHT'))
    if errs:
        print(f'\n{len(errs)} Befunde:')
        for e in errs:
            print(' ', e)
        return 1
    print('Struktur sauber.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
