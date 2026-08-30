"""Buchinterne Dubletten: Verspaare mit hoher Wortueberlappung.

    dubletten.py <buchNr> [--anteil 0.6] [--min 5]

## Wozu

`parallelen.py` sucht Parallelstellen im **ganzen Bestand** — also in schon
annotierten Buechern. Was es prinzipiell nicht findet, ist die Dublette
**innerhalb** des Buches, das gerade entsteht: dort ist noch nichts annotiert,
wenn der erste Agent laeuft.

Die Sprueche haben 26 solcher Paare, sechs davon woertlich gleich (14,12 =
16,25, 18,8 = 26,22, 21,9 = 25,24 und weitere). Sie liegen bis zu zwoelf
Kapitel auseinander und werden von verschiedenen Agenten geschrieben. Ohne
Vorwarnung bekommt derselbe Satz zwei verschiedene Glossenreihen.

## Wie zu lesen

Der Agent des **spaeteren** Verses bekommt den frueheren in den Prompt. Wo der
Text woertlich gleich ist, wird die Glossenreihe uebernommen. Wo er es nicht
ist, gilt die Warnung aus AUFTRAG_AT.md: **die zweite Fassung formuliert fast
nie woertlich gleich, und wer abschreibt, glossiert falsch.** Die
Aehnlichkeitszahl steht deshalb bei jedem Paar.
"""
import difflib
import itertools
import sys

import common as C


def paare(nr, anteil=0.6, mintok=5):
    src = C.load_source(nr)['chapters']
    verses = []
    for k in sorted(src, key=int):
        for v in sorted(src[k], key=int):
            toks = [t for t in (C.strip_punct(x).lower() for x in C.tokens(src[k][v])) if t]
            verses.append((int(k), int(v), src[k][v], toks))
    out = []
    for (k1, v1, t1, a), (k2, v2, t2, b) in itertools.combinations(verses, 2):
        if len(a) < mintok or len(b) < mintok:
            continue
        gem = len(set(a) & set(b))
        if gem / len(set(a)) >= anteil and gem / len(set(b)) >= anteil:
            out.append((difflib.SequenceMatcher(None, a, b).ratio(),
                        k1, v1, t1, k2, v2, t2))
    out.sort(key=lambda x: -x[0])
    return out


def main():
    nr = int(sys.argv[1])
    anteil, mintok = 0.6, 5
    args = sys.argv[2:]
    if '--anteil' in args:
        anteil = float(args[args.index('--anteil') + 1])
    if '--min' in args:
        mintok = int(args[args.index('--min') + 1])
    name = C.load_source(nr)['name']
    ps = paare(nr, anteil, mintok)
    print(f'# Buchinterne Dubletten: {name}\n')
    print(f'Verspaare mit mindestens {anteil:.0%} gemeinsamen Wortformen (beide '
          f'Richtungen)\nund mindestens {mintok} Tokens. Gemessen über den '
          'Quelltext.\n')
    print(f'**{len(ps)} Paare.**\n')
    for r, k1, v1, t1, k2, v2, t2 in ps:
        kennz = 'wörtlich gleich' if t1 == t2 else f'Ähnlichkeit {r:.2f}'
        print(f'## {k1},{v1} ↔ {k2},{v2} — {kennz}\n')
        print(f'- **{k1},{v1}**  {t1}')
        print(f'- **{k2},{v2}**  {t2}\n')


if __name__ == '__main__':
    main()
