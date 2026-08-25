"""Parallelstellen eines Kapitels im **ganzen** annotierten Bestand.

    parallelen.py <buchNr> <kapitel> [minblock] [--alle]

Für jeden Vers des Kapitels wird der Vers des Bestands gesucht, der den
**längsten gemeinsamen Wortblock** teilt — nicht den höchsten
Ähnlichkeitswert. Das ist der Unterschied, an dem die erste Fassung dieser
Suche gescheitert ist.

## Warum nicht nach Ähnlichkeit

Nehemia 11,7 hat gegen 1. Chronik 5,14 die Ähnlichkeit **0,57**, teilt mit ihr
aber nur `Dies sind die` — drei Allerweltswörter. Gegen 1. Chronik 9,7 liegt
die Ähnlichkeit bei **0,44**, der gemeinsame Block ist aber
`Benjamins: Sallu, der Sohn Mesullams, des Sohnes` — sieben Tokens, die es so
nur an dieser einen Stelle gibt. Die zweite ist die Parallele, die erste ist
Genealogie-Bauform.

Bei Listen und Genealogien besteht ein großer Teil jeder Zeile aus derselben
Bauform (`der Sohn X, des Sohnes Y`). Die Ähnlichkeit misst dann vor allem,
wie sehr zwei Zeilen **derselben Gattung** angehören; der lange Block misst,
ob sie **dieselbe Stelle** meinen. Dasselbe Problem hatte `vorlage.py`, dort
ist es durch eine ordnungserhaltende Zuordnung gelöst — die geht hier nicht,
weil über den ganzen Bestand gesucht wird und es keine Bezugsreihenfolge gibt.

Ausgegeben wird deshalb **beides**: der Treffer nach Blocklänge und, wo er
abweicht, der Treffer nach Ähnlichkeit. Entscheiden muss ein Mensch.
"""
import difflib
import sys

import common as C


def norm(t):
    return [C.strip_punct(x) for x in t.split()]


def bester_block(a, b):
    """Länge des längsten gemeinsamen zusammenhängenden Blocks."""
    return difflib.SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b)).size


nr, kap = int(sys.argv[1]), sys.argv[2]
minblock = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 4
alle = '--alle' in sys.argv

quelle = C.load_source(nr)['chapters'][kap]
buecher = [b for b in C.anno_books()]

print(f'# Parallelstellen zu {C.book_name(nr)} {kap} im annotierten Bestand\n')
print(f'Gesucht wird der **längste gemeinsame Wortblock** (ab {minblock} Tokens),')
print('nicht die höchste Ähnlichkeit. Wo beide Maße auseinandergehen, steht der')
print('Ähnlichkeitstreffer daneben — dann selbst entscheiden.\n')

gefunden = 0
for v in sorted(quelle, key=int):
    a = norm(quelle[v])
    if len(a) < minblock:
        continue
    top_block = (0, 0.0, None)
    top_ratio = (0.0, 0, None)
    for b in buecher:
        src = C.load_source(b)['chapters']
        for k in src:
            if b == nr and k == kap:
                continue
            for w, t in src[k].items():
                bb = norm(t)
                blk = bester_block(a, bb)
                if blk < minblock and not alle:
                    continue
                r = difflib.SequenceMatcher(None, a, bb).ratio()
                if (blk, r) > (top_block[0], top_block[1]):
                    top_block = (blk, r, (b, k, w))
                if (r, blk) > (top_ratio[0], top_ratio[1]):
                    top_ratio = (r, blk, (b, k, w))
    if top_block[2] is None:
        continue
    gefunden += 1
    blk, r, (b, k, w) = top_block
    print(f'## {kap},{v} ← {C.book_name(b)} {k},{w}   Block {blk}, Ähnlichkeit {r:.2f}')
    sm = difflib.SequenceMatcher(None, a, norm(C.load_source(b)['chapters'][k][w]))
    for bl in sm.get_matching_blocks():
        if bl.size >= minblock:
            print(f'   Block A-pos {bl.a} ← B-pos {bl.b}, Länge {bl.size}, '
                  f'Versatz {bl.b - bl.a:+d}: `{" ".join(a[bl.a:bl.a + bl.size])}`')
    if top_ratio[2] and top_ratio[2] != top_block[2]:
        r2, blk2, (b2, k2, w2) = top_ratio
        print(f'   **Die Ähnlichkeit zeigt woanders hin**: {C.book_name(b2)} {k2},{w2} '
              f'(Ähnlichkeit {r2:.2f}, längster Block aber nur {blk2}). '
              f'Der lange Block oben ist der belastbarere Treffer — trotzdem selbst ansehen.')
    print()

print(f'{gefunden} von {len(quelle)} Versen haben eine Parallelstelle mit '
      f'mindestens {minblock} gemeinsamen Tokens.')
