"""Ein Lemma, zwei Lesarten im selben Buch — und eine davon ist hausgemacht.

    zweigleisig.py <buchNr …> | alle [--min 5] [--wieoft 2]

## Wozu

In Hiob ist derselbe Mechanismus dreimal aufgetreten:

- **`würde`** bekam in 3,13 die Ausweichlesart *starei per*, weil `hätte` im
  selben Vers schon *avrei* trug. Kapitel 5 und 6 lasen sie als Bindung und
  reichten sie weiter — in Verse ohne jede Kollision.
- **`nur`** bekam in 1,15 die Ausweichlesart *Solamente · Soltanto* gegen
  `allein`. Sie stand danach in zwölf Einträgen des Buches, während `allein`
  im ganzen Buch nur in vier Versen daneben vorkommt.
- **`Grab`** stand in 5,26 auf *grave · sepultura · tombeau · tomba*, einer
  Lesart mit genau diesem einen Beleg im gesamten Bestand. Kapitel 10 hat sie
  übernommen.

Der Grund ist strukturell: `lexicon.py` zieht aus **allen** vorhandenen
Anno-Dateien, also auch aus den frisch gebauten Kapiteln des laufenden Buches.
Was ein Kapitel entscheidet, sieht das nächste als Bestand — ohne zu sehen, ob
es eine Kollisionsauflösung war, die nur für einen Vers gilt.

## Was gemeldet wird

Ein Lemma, das im Buch **zwei oder mehr** Lesarten trägt, von denen eine im
übrigen Bestand gut belegt ist und eine andere kaum oder gar nicht — **und die
schwache Lesart steht mindestens zweimal im Buch.**

Die Zweimal-Schwelle ist der eigentliche Kern der Prüfung, nicht ein Filter
gegen zuviel Ausgabe. Eine Kollisionsauflösung gilt für **einen** Vers und
bleibt dort: `Dunkel` = *gloom* steht nur in 3,5, `Mensch` = *mortal* nur in
4,17, `Angesicht` = *countenance* nur in 6,28. Eine hausgemachte Lesart wird
dagegen **weitergereicht** — `nur` stand in zwölf Einträgen, `Grab` in zweien,
`würde` in vieren. Genau das misst die Schwelle.

Ohne sie meldet die Prüfung außerdem jede Konjunktivform einzeln: seit die
Irrealis-Konvention gilt, trägt jedes `würde` den Konditional seines eigenen
Vollverbs, und keine dieser Formen steht im übrigen Bestand. Das sind Dutzende
richtiger Einträge und kein einziger Befund.

Funktionswörter bleiben draußen. Präpositionen und Artikel tragen legitim ein
Dutzend kontextabhängiger Lesarten; sie würden den Bericht füllen, ohne dass
etwas dran wäre. Mit `--wieoft 1` und `--funktionswoerter` lässt sich beides
abschalten.

Numerus- und Genusvarianten werden zusammengefasst, sonst besteht der Bericht
nur aus Singular/Plural-Paaren.

## Wieviel es meldet

Gemessen am Stand vom 28.08.2026: **Hiob 7** (elf Kapitel), **Esra 14**,
**Ester 15**, **Nehemia 38**, **1. Mose 127**, **Matthäus 106**. Der Rest sind
durchweg Tempus- und Personformen, die der Stammabgleich nicht zusammenzieht
(*comer* gegen *comían*) — die Prüfung ist deshalb für das **Buch in Arbeit**
gedacht, wie `konsistenz.py`, nicht für einen Durchlauf über den Gesamtbestand.

Bei den fünf echten Fällen, die sie gefunden hätte, lag sie richtig: `nur`,
`würde`, `Grab`, `sodass` (italienisch *sicché* gegen *così che*, 379 Belege)
und `doch` (*aun así · pure* gegen *sin embargo · eppure*, 80 Belege).

## Was ein Treffer bedeutet

Er ist ein **Verdacht**, kein Fehler — genau wie bei `qa.py`. Eine
Kollisionsauflösung sieht identisch aus und ist richtig: `Dunkel` trägt in
3,5 *gloom*, weil `Finsternis` im selben Vers steht, und in 3,23 wieder die
Bestandslesart. Die Frage am Treffer lautet deshalb immer:

    Steht in den Versen der seltenen Lesart ein Wort, das die häufige Lesart
    im Lesefluss ununterscheidbar machen würde?

Ja → richtig, die Ausweichlesart bleibt, aber **nur dort**.
Nein → hausgemacht, auf die Bestandslesart ziehen.
"""
import argparse
import collections

import common as C
import hints
import qa

FUNKTION = hints.FUNKTION | qa.FUNKTIONSWOERTER


STAMM = 5


def _kern(reading):
    """Lesart auf Wortstaemme gekuerzt, damit Flexionsformen zusammenfallen.

    Ohne das meldet jedes Substantiv sein eigenes Singular/Plural-Paar. Eine
    erste Fassung strich feste Endungen (`es`, `s`, `i`, `e`) — das reichte
    fuers Englische und Franzoesische, versagte aber genau dort, wo Spanisch
    und Italienisch die Endung wechseln statt sie anzuhaengen: *province* gegen
    *provincia* blieb getrennt, und Ester meldete daraufhin seine halbe
    Substantivliste.

    Gekuerzt wird deshalb jedes Wort auf die ersten fuenf Zeichen. Das ist
    grob und zieht gelegentlich zwei verwandte Woerter zusammen (*sepulcro*
    und *sepultura*), aber es wird ueber **alle vier** Sprachen verglichen —
    dass alle vier gleichzeitig faelschlich zusammenfallen, kommt praktisch
    nicht vor. Bei `Grab` trennt das Englische (*tomb* gegen *grave*), was das
    Spanische verschmilzt.
    """
    return tuple(' '.join(w[:STAMM] for w in g.lower().split()) for g in reading)


def sammeln(nr):
    """lemma -> {kern -> [anzahl_im_buch, beispiel_lesart, [stellen]]}"""
    buch = collections.defaultdict(dict)
    name = C.load_source(nr)['name']
    for _, kap, vers, e in C.iter_corpus([nr]):
        if C.is_multi(e):
            continue
        lesart = tuple(e[l] for l in C.LANGS)
        rec = buch[e['lemma']].setdefault(_kern(lesart), [0, lesart, []])
        rec[0] += 1
        if len(rec[2]) < 6:
            rec[2].append(f'{kap},{vers}')
    return name, buch


def bestand_ausserhalb(nr):
    """lemma -> {kern -> anzahl} über alle Bücher AUSSER nr."""
    idx = collections.defaultdict(collections.Counter)
    for b in C.anno_books():
        if b == nr:
            continue
        for _, _, _, e in C.iter_corpus([b]):
            if C.is_multi(e):
                continue
            idx[e['lemma']][_kern(tuple(e[l] for l in C.LANGS))] += 1
    return idx


def pruefe(nr, min_belege, wieoft, funktionswoerter):
    name, buch = sammeln(nr)
    aussen = bestand_ausserhalb(nr)
    treffer = []
    for lemma, lesarten in buch.items():
        if len(lesarten) < 2:
            continue
        if not funktionswoerter and lemma.lower() in FUNKTION:
            continue
        bewertet = [(k, v[0], v[1], v[2], aussen[lemma].get(k, 0)) for k, v in lesarten.items()]
        stark = [b for b in bewertet if b[4] >= min_belege]
        schwach = [b for b in bewertet if b[4] < min_belege and b[1] >= wieoft]
        if not stark or not schwach:
            continue
        treffer.append((lemma, sorted(stark, key=lambda b: -b[4]), sorted(schwach, key=lambda b: b[4])))
    return name, treffer


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buecher', nargs='+')
    p.add_argument('--min', type=int, default=5,
                   help='ab so vielen Belegen ausserhalb des Buches gilt eine '
                        'Lesart als im Bestand verankert (Vorgabe 5)')
    p.add_argument('--wieoft', type=int, default=2,
                   help='so oft muss die schwache Lesart im Buch stehen, damit '
                        'sie als weitergereicht gilt (Vorgabe 2). Mit 1 werden '
                        'auch einmalige Kollisionsaufloesungen gemeldet.')
    p.add_argument('--funktionswoerter', action='store_true',
                   help='Praepositionen, Artikel und Pronomen mitpruefen')
    args = p.parse_args()

    nummern = C.anno_books() if args.buecher == ['alle'] else [int(b) for b in args.buecher]
    gesamt = 0
    for nr in nummern:
        name, treffer = pruefe(nr, args.min, args.wieoft, args.funktionswoerter)
        if not treffer:
            continue
        print(f'\n## {name}\n')
        for lemma, stark, schwach in sorted(treffer):
            print(f'`{lemma}`')
            for _, n, lesart, stellen, aussen in stark:
                print(f'   im Bestand: {aussen}× · im Buch {n}× · '
                      f'{" · ".join(lesart)}  ({", ".join(stellen)})')
            for _, n, lesart, stellen, aussen in schwach:
                print(f'   HAUSGEMACHT: {aussen}× im Bestand · im Buch {n}× · '
                      f'{" · ".join(lesart)}  ({", ".join(stellen)})')
            gesamt += 1
    print(f'\n{gesamt} Lemmata mit einer weitergereichten Zweitlesart.')
    print('Jeder Treffer ist ein Verdacht. Die Frage lautet: steht in den Versen')
    print('der seltenen Lesart ein Wort, das die haeufige ununterscheidbar machen')
    print('wuerde? Ja -> Kollisionsaufloesung, richtig. Nein -> hausgemacht.')


if __name__ == '__main__':
    main()
