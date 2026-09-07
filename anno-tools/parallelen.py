"""Parallelstellen eines Kapitels im **ganzen** annotierten Bestand.

    parallelen.py <buchNr> <kapitel> [minblock] [--alle]

Für jeden Vers des Kapitels wird der Vers des Bestands gesucht, der den
**längsten gemeinsamen Wortblock** teilt — nicht den höchsten
Ähnlichkeitswert. Das ist der Unterschied, an dem die erste Fassung dieser
Suche gescheitert ist.

## Was ein Treffer wert ist

Gesucht wird im **Quelltext** aller Buecher mit Anno-Datei — auch in Kapiteln,
die noch gar nicht annotiert sind. Ein Buch kann eine Anno-Datei haben und
trotzdem erst zur Haelfte gefuellt sein; der Psalter hatte 77 von 150 Kapiteln,
als das auffiel. Treffer in einem solchen Kapitel tragen **keine Glossen**, und
wer sie uebernimmt, uebernimmt nichts. Sie sind seither mit
`NOCH NICHT ANNOTIERT` markiert. Gezaehlt werden sowohl die Kapitel des
gebauten Buches als auch die Kapitelquellen unter `anno-quellen/` — waehrend
einer laufenden Welle ist ein Kapitel oft geschrieben, aber noch nicht gebaut.

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


if len(sys.argv) < 3:
    raise SystemExit('Aufruf: parallelen.py <buchNr> <kapitel> '
                     '[minblock] [--alle]\n'
                     'Ohne Kapitelnummer brach der Lauf mit einem '
                     'IndexError ab statt dies zu sagen.')
nr, kap = int(sys.argv[1]), sys.argv[2]
minblock = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 4
alle = '--alle' in sys.argv

quelle = C.load_source(nr)['chapters'][kap]
buecher = [b for b in C.anno_books()]

# Welche Kapitel tragen wirklich Glossen? Ein Buch kann eine Anno-Datei haben
# und trotzdem erst zur Haelfte annotiert sein — der Psalter hatte 77 von 150
# Kapiteln, als das hier gebraucht wurde. Gesucht wird aber im **Quelltext**
# aller Buecher mit Anno-Datei, also auch in Kapiteln ohne einen einzigen
# Eintrag. Wer so einen Treffer "uebernimmt", uebernimmt nichts.
# Dazu die **Kapitelquellen**: waehrend einer laufenden Welle sind Kapitel
# fertig geschrieben, aber noch nicht gebaut. Ohne sie meldet das Skript
# `NOCH NICHT ANNOTIERT` fuer eine Vorlage, die es laengst gibt — so geschehen
# bei Ps 128,5, das dem Agenten fuer Ps 134,3 als fehlend angezeigt wurde,
# obwohl ch128.json daneben lag.
annotiert = {}
for b in buecher:
    aus_buch = set(C.load_anno(b)['chapters'])
    aus_quelle = {str(k) for k in C.quellen_kapitel(b)}
    annotiert[b] = aus_buch | aus_quelle

print(f'# Parallelstellen zu {C.book_name(nr)} {kap} im annotierten Bestand\n')
print(f'Gesucht wird der **längste gemeinsame Wortblock** (ab {minblock} Tokens),')
print('nicht die höchste Ähnlichkeit. Wo beide Maße auseinandergehen, steht der')
print('Ähnlichkeitstreffer daneben — dann selbst entscheiden.\n')

gefunden = 0
traegt = 0    # davon die, deren Vorlage wirklich Glossen hat
for v in sorted(quelle, key=int):
    a = norm(quelle[v])
    if len(a) < minblock:
        continue
    top_block = (0, False, 0.0, None)
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
                # Bei gleicher Blocklaenge gewinnt der Vers, der
                # **Glossen traegt**. Vorher entschied allein die
                # Aehnlichkeit, und in Sacharja 4 fuehrte das dreimal
                # auf einen noch leeren Vers desselben Buches: 4,1 zeigte
                # auf 5,5 statt auf das fertige 1,14, 4,9 auf 6,15 statt
                # auf 2,13. Der Agent hat es gemerkt, weil die richtigen
                # Vorlagen im Prompt standen — ohne den Prompt haette er
                # drei leere Vorlagen bekommen. Je weiter ein Buch
                # gefuellt ist, desto haeufiger tritt der Fall auf.
                hat_glossen = k in annotiert.get(b, ())
                if (blk, hat_glossen, r) > (top_block[0], top_block[1],
                                            top_block[2]):
                    top_block = (blk, hat_glossen, r, (b, k, w))
                if (r, blk) > (top_ratio[0], top_ratio[1]):
                    top_ratio = (r, blk, (b, k, w))
    if top_block[3] is None:
        continue
    gefunden += 1
    blk, _hat, r, (b, k, w) = top_block
    if k in annotiert.get(b, ()):
        leer = ''
        traegt += 1
    else:
        leer = '   ⚠ NOCH NICHT ANNOTIERT — dort stehen keine Glossen'
    print(f'## {kap},{v} ← {C.book_name(b)} {k},{w}   Block {blk}, Ähnlichkeit {r:.2f}{leer}')
    sm = difflib.SequenceMatcher(None, a, norm(C.load_source(b)['chapters'][k][w]))
    for bl in sm.get_matching_blocks():
        if bl.size >= minblock:
            print(f'   Block A-pos {bl.a} ← B-pos {bl.b}, Länge {bl.size}, '
                  f'Versatz {bl.b - bl.a:+d}: `{" ".join(a[bl.a:bl.a + bl.size])}`')
    # `top_block` ist (blk, hat, ratio, ort) — `top_block[2]` ist die
    # ZAHL, nicht der Ort. Der Vergleich gegen `top_ratio[2]` (ein
    # Ort) war damit immer ungleich, und der Hinweis stand unter
    # JEDEM Treffer — auch wo beide Masse denselben Vers meinen
    # (Marc 1,3 ← Matthieu 3,3, Aehnlichkeitstreffer Matthieu 3,3).
    # Gefunden beim ersten Lauf ueber Markus.
    # Der Parallelvers GANZ, mit Lemma, Level und allen vier Glossen —
    # dieselbe Ausgabe wie `fixgloss.py verse`. Bis Markus 12 stand hier
    # nur die Fundstelle, und jeder Agent hat sie einzeln nachgeschlagen;
    # der Agent fuer Marc 12 hat vorgerechnet, dass 30 seiner 44 Verse
    # damit direkt lesbar gewesen waeren. Die Mehrwortspannen sind der
    # eigentliche Gewinn: sie stehen in keiner Blockzeile.
    # Nur bei einem TRAGENDEN Treffer. Marc 13,2 findet in Mt 22,37 vier
    # gemeinsame Tokens (`Jésus lui répondit Tu`) bei Aehnlichkeit 0.25 —
    # eine Formel, keine Parallele. Den ganzen Vers dazu auszuschreiben
    # waere genau das Rauschen, das den Rest unlesbar macht.
    if k in annotiert.get(b, ()) and (blk >= 6 or r >= 0.40):
        for e in C.load_anno(b)['chapters'][k][w]:
            span = (f'{e["pos"]}-{e["pos_end"]}' if 'pos_end' in e
                    else (str(e['parts']) if 'parts' in e else str(e['pos'])))
            print(f'     {span:>9}  {e["form"]:<20} {e.get("lemma",""):<18} '
                  f'{e.get("level","")}  '
                  + ' · '.join(f'{l} {e.get(l,"")}' for l in C.LANGS))
    if top_ratio[2] and top_ratio[2] != top_block[3]:
        r2, blk2, (b2, k2, w2) = top_ratio
        print(f'   **Die Ähnlichkeit zeigt woanders hin**: {C.book_name(b2)} {k2},{w2} '
              f'(Ähnlichkeit {r2:.2f}, längster Block aber nur {blk2}). '
              f'Der lange Block oben ist der belastbarere Treffer — trotzdem selbst ansehen.')
    print()

# Beide Zahlen, nicht nur die erste. Beim Vorwaertsarbeiten durch ein Buch
# zeigen die meisten Treffer auf spaetere Kapitel, die noch leer sind: in
# Matteo 9 waren 16 der 19 Treffer ohne Glossen, und der Koordinator hatte
# dem Agenten aus der einen Zahl `19 von 38` eine tragende Bindung
# versprochen, die es nicht gab. Der Agent hat es nachgemessen und gemeldet.
print(f'{gefunden} von {len(quelle)} Versen haben eine Parallelstelle mit '
      f'mindestens {minblock} gemeinsamen Tokens — davon {traegt} mit '
      f'Glossen in der Vorlage, {gefunden - traegt} noch ohne.')
if gefunden and traegt * 2 < gefunden:
    print(f'ACHTUNG: die Mehrheit der Treffer zeigt auf noch nicht '
          f'annotierte Verse. Tragend sind {traegt}, nicht {gefunden}.')
