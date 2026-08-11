"""Korpusweite Korrektur einer Glosse, numerus-erhaltend.

    remap.py <lemma> <feld> alt=neu [alt=neu …] [--form <form>] [--trocken]

Beispiel — `Ehre` kollidierte korpusweit mit `Herrlichkeit`:

    remap.py Ehre en glory=honor
    remap.py Ehre es gloria=honra

Ersetzt **feldweise nur exakte Werte**; Singular und Plural bleiben dadurch
getrennt (`glory` → `honor` lässt `glories` unangetastet, dafür gibt es einen
zweiten Aufruf). Mit `--form` nur an einer bestimmten Wortform.

Geschrieben wird in die **Kapitelquellen**; anschließend werden die betroffenen
Bücher neu gebaut. Beides zusammen — ohne den Neubau stünde die Korrektur nicht
in der ausgelieferten Datei, ohne die Quelle wäre sie beim nächsten Build
wieder weg. Das war früher Handarbeit und die häufigste Fehlerquelle.
"""
import argparse
import collections

import buildbook
import common as C


def remap(lemma, feld, paare, form=None, trocken=False):
    if feld not in C.LANGS + ['level', 'lemma']:
        raise SystemExit(f'Feld {feld!r} unbekannt')
    betroffen = collections.Counter()

    for nr in C.anno_books():
        for kap in C.quellen_kapitel(nr):
            data = C.load_quelle(nr, kap)
            geaendert = False
            for vers, entries in data.items():
                for e in entries:
                    if e['lemma'] != lemma:
                        continue
                    if form and e['form'] != form:
                        continue
                    if e.get(feld) in paare:
                        alt = e[feld]
                        if not trocken:
                            e[feld] = paare[alt]
                        betroffen[nr] += 1
                        geaendert = True
            if geaendert and not trocken:
                C.write_quelle(nr, kap, data)

    if not betroffen:
        print('Keine Treffer.')
        return
    for nr, n in sorted(betroffen.items()):
        print(f'{nr} {C.load_source(nr)["name"]}: {n} Einträge')
    print(f'Summe: {sum(betroffen.values())} Einträge in {len(betroffen)} Büchern')
    if trocken:
        print('(trocken — nichts geschrieben, nichts gebaut)')
        return
    for nr in sorted(betroffen):
        buildbook.build(nr)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('lemma')
    p.add_argument('feld')
    p.add_argument('paare', nargs='+')
    p.add_argument('--form')
    p.add_argument('--trocken', action='store_true')
    a = p.parse_args()
    paare = {}
    for s in a.paare:
        if '=' not in s:
            raise SystemExit(f'{s!r} ist kein alt=neu-Paar')
        alt, neu = s.split('=', 1)
        paare[alt] = neu
    remap(a.lemma, a.feld, paare, a.form, a.trocken)
