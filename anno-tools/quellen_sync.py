"""Schreibt die Kapitelquellen aus den gebauten Anno-Dateien zurück.

    quellen_sync.py <buchNr …> | alle [--nur-fehlende]

Warum es das gibt: die gebaute Datei ist der **jüngere** Stand. Korpusweite
Korrekturen (`fixgloss.py`, `remap.py`) und der Level-Abgleich landen dort;
gingen Kapitelquellen verloren, war ein Buch bisher nicht mehr baubar
(Matthäus, Markus, 2. Mose 30–40). Aus der gebauten Datei lässt sich die
Quelle vollständig zurückgewinnen — verloren geht dabei nichts, was der Build
nicht ohnehin verwirft (Satzzeichen-Einträge) oder überschreibt (Level).

Mit `--nur-fehlende` werden vorhandene Quellen nicht angefasst.
"""
import sys

import common as C


def sync(nr, nur_fehlende=False):
    nr = int(nr)
    if not C.has_anno(nr):
        print(f'{nr}: keine Anno-Datei')
        return 0
    ann = C.load_anno(nr, cache=False)['chapters']
    vorhanden = set(C.quellen_kapitel(nr))
    n = 0
    for kap, verses in ann.items():
        if nur_fehlende and int(kap) in vorhanden:
            continue
        alt = C.load_quelle(nr, kap)
        neu = {v: verses[v] for v in sorted(verses, key=int)}
        if alt == neu:
            continue
        C.write_quelle(nr, kap, neu)
        n += 1
    print(f'{nr} {C.load_source(nr)["name"]}: {n} Kapitelquellen geschrieben '
          f'({len(ann)} Kapitel in der Anno-Datei)')
    return n


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    nur = '--nur-fehlende' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    nrs = C.anno_books() if args[0] == 'alle' else [int(a) for a in args]
    for nr in nrs:
        sync(nr, nur)
