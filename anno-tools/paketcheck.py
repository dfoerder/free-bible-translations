"""Mehrere gleichzeitig gebaute Kapitel gegeneinander — vor dem Einsammeln.

    paketcheck.py <buchNr> <kapitel> <kapitel> [<kapitel> …]
    paketcheck.py <datei.json> <datei.json> [<datei.json> …]

`crosscheck.py` prueft zwei Abschnitte **eines** Kapitels, `konsistenz.py` ein
fertig gebautes **Buch**. Dazwischen fehlte das Werkzeug fuer den Fall, der in
jeder Welle vorkommt: **zwei oder drei Agenten schreiben gleichzeitig, jeder
sieht nur sein Kapitel, und keiner sieht, was der andere gerade praegt.**

## Der Anlass

Jesaja Paket 15. `wackeln` steht in 40,20 und 41,7 im selben Sachfeld — der
Goetzenbauer, der sein Standbild befestigt, „damit es nicht wackelt". Die
beiden Agenten haben es verschieden gepraegt:

    40,20   wobbles · se tambalea · branle · vacilla     B1
    41,7    totter  · mueva       · branle · smuova      B2

`selfcheck.py`, `qa.py`, `konvention.py`, `sweeplemma.py`, `glosskollision.py`
und `levelcheck.py` laufen ueber **beide** Kapitel ohne Befund. Strukturell
fehlt nichts, und im Bestand gibt es keine Zeile, gegen die zu pruefen waere —
das Wort ist ja neu. Der Fall ist von Hand gefunden worden, durch einen
Vergleich aller Lemmata, die in mindestens zwei Kapiteln des Pakets vorkommen.
Dieses Skript ist dieser Vergleich.

## Die drei Abschnitte, nach Schaerfe geordnet

**A — neu gepraegte Lemmata in mehreren Kapiteln.** Das Lemma steht in keiner
fertigen Anno-Datei des Bestands, also hatte jeder Agent freie Hand, und keine
Bindung konnte ihn korrigieren. **Hier liegt der `wackeln`-Fall.** Jede Zeile
dieses Abschnitts ist anzusehen. Zu pruefen ist nicht, ob die Reihen
buchstabengleich sind — das Skript kennt keine Flexion, und zwei Verse mit
verschiedenem Tempus oder Numerus stehen hier zwangslaeufig — sondern ob
**dieselbe Wortfamilie** gewaehlt wurde. *totters/totter* ist in Ordnung,
*wobbles/totter* ist der Fall, um den es geht.

**B — belegte Lemmata ohne gemeinsame Reihe.** Das Lemma kommt in mehreren
Kapiteln vor, und **keine einzige Glossenreihe kommt in allen** vor. Das ist
meistens harmlos (Tempus, Numerus, Genus, Kontext) — deshalb steht dahinter,
in wie vielen Sprachen die Reihen sich unterscheiden. Ein Fall, der **in allen
vier Sprachen** auseinandergeht, ist der Verdaechtige; einer, der nur in einer
Sprache abweicht, ist meist eine Kongruenzvariante.

**C — Level-Divergenzen.** Dasselbe Lemma, zwei Level. `buildbook.py` zieht das
beim Bauen auf die Korpusmehrheit — aber wenn das Lemma neu ist, gibt es keine
Mehrheit, und dann entscheidet die Reihenfolge der Dateien. `levelcheck.py`
sieht es nicht, weil es je Kapitel gegen den **Bestand** prueft und nicht die
Kapitel des Pakets gegeneinander.

Wie jedes Pruefskript hier meldet es **Verdacht, keine Fehler**. Und die
Auflösung ist nicht automatisch dieselbe Reihe fuer beide Stellen: wo der
deutsche Text zwei verschiedene Woerter schreibt oder die Ausgaben an den
beiden Versen selbst verschieden lesen, darf die Divergenz stehen bleiben.
Entschieden wird am Vers, nicht an der Zaehlung.
"""
import collections
import json
import os
import sys

import common as C
import hints


def lade(args):
    """([(name, {vers: [eintraege]})], {(buchNr, kap)}) — Nummern oder Pfade.

    Die zweite Rueckgabe nennt die Kapitel, die aus dem Bestandsvergleich
    herausgehalten werden muessen: ein Kapitel, das schon einmal gebaut wurde,
    steht in der Anno-Datei und wuerde sein eigenes neues Lemma als "belegt"
    ausweisen — dann landet der `wackeln`-Fall in Abschnitt B statt A.
    """
    if args[0].isdigit() and all(a.isdigit() for a in args[1:]):
        nr = int(args[0])
        out, eigene = [], set()
        for kap in args[1:]:
            eigene.add((nr, str(int(kap))))
            data = C.load_quelle(nr, int(kap))
            if data is None:
                anno = C.load_anno(nr)['chapters']
                data = anno.get(str(int(kap)))
            if data is None:
                raise SystemExit(f'Kapitel {kap} nicht gefunden — '
                                 f'weder in anno-quellen noch in der Anno-Datei')
            out.append((f'{C.book_name(nr)} {int(kap)}', data))
        return out, eigene
    out = []
    for p in args:
        with open(p, encoding='utf-8') as f:
            data = json.load(f)
        if 'chapters' in data:
            raise SystemExit('Bitte Kapiteldateien angeben, keine Buchdatei')
        out.append((os.path.basename(p), data))
    return out, set()


def bestandslemmata(ohne=()):
    """Alle Lemmata des fertigen Bestands, ohne die Kapitel des Pakets."""
    ohne = set(ohne)
    return {e['lemma'] for nr, kap, _, e in C.iter_corpus()
            if (nr, kap) not in ohne and (int(nr), kap) not in ohne}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    kapitel, eigene = lade(sys.argv[1:])
    if len(kapitel) < 2:
        raise SystemExit('Mindestens zwei Kapitel — sonst gibt es nichts zu vergleichen.')

    # lemma -> kapitelname -> {reihe: [verse]}
    reihen = collections.defaultdict(lambda: collections.defaultdict(
        lambda: collections.defaultdict(list)))
    level = collections.defaultdict(lambda: collections.defaultdict(set))
    for name, data in kapitel:
        for vers, entries in data.items():
            for e in entries:
                lemma = e['lemma']
                if lemma.lower() in hints.FUNKTION:
                    continue
                reihen[lemma][name][tuple(e[l] for l in C.LANGS)].append(vers)
                level[lemma][name].add(e.get('level'))

    gemeinsam = {lm: byk for lm, byk in reihen.items() if len(byk) > 1}
    bestand = bestandslemmata(eigene)

    def zeilen(byk):
        for name, gruppen in sorted(byk.items()):
            for reihe, verse in sorted(gruppen.items()):
                stellen = ', '.join(verse[:4]) + (' …' if len(verse) > 4 else '')
                print(f'    {name:<16} {" · ".join(reihe)}   — V. {stellen}')

    def ohne_gemeinsame_reihe(byk):
        mengen = [set(g) for g in byk.values()]
        return not set.intersection(*mengen)

    def sprachen_verschieden(byk):
        """In wie vielen der vier Sprachen gehen die Kapitel auseinander."""
        n = 0
        for i in range(len(C.LANGS)):
            mengen = [{r[i] for r in g} for g in byk.values()]
            if not set.intersection(*mengen):
                n += 1
        return n

    print(f'# Paketvergleich: {len(kapitel)} Kapitel '
          f'({", ".join(n for n, _ in kapitel)})')
    print(f'\n{len(reihen)} Inhaltslemmata insgesamt, '
          f'{len(gemeinsam)} davon in mehr als einem Kapitel.')

    neu = {lm: byk for lm, byk in gemeinsam.items()
           if lm not in bestand and ohne_gemeinsame_reihe(byk)}
    print('\n## A — neu gepraegte Lemmata, verschieden entschieden\n')
    if not neu:
        print('    keine — jedes neue Lemma des Pakets traegt in allen '
              'Kapiteln dieselbe Reihe.')
    for lemma, byk in sorted(neu.items()):
        print(f'`{lemma}`  (im Bestand unbelegt)')
        zeilen(byk)

    alt = [(sprachen_verschieden(byk), lm, byk) for lm, byk in gemeinsam.items()
           if lm in bestand and ohne_gemeinsame_reihe(byk)]
    print(f'\n## B — belegte Lemmata ohne gemeinsame Reihe ({len(alt)})\n')
    for n_spr, lemma, byk in sorted(alt, key=lambda x: (-x[0], x[1])):
        print(f'`{lemma}`  — {n_spr} von 4 Sprachen verschieden')
        zeilen(byk)

    print('\n## C — Level-Divergenzen\n')
    n_lvl = 0
    for lemma, byk in sorted(level.items()):
        if len(byk) < 2:
            continue
        alle = set().union(*byk.values())
        if len(alle) > 1:
            n_lvl += 1
            marke = '  ← neues Lemma' if lemma not in bestand else ''
            print(f'`{lemma}`  ' +
                  ' · '.join(f'{n}: {"/".join(sorted(v))}'
                             for n, v in sorted(byk.items())) + marke)
    if not n_lvl:
        print('    keine.')

    print(f'\n{len(neu)} + {len(alt)} + {n_lvl} Verdachtsfaelle. '
          'Abschnitt A zuerst — dort hatte kein Agent eine Bindung, '
          'die ihn haette korrigieren koennen.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
