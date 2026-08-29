"""Dasselbe Wort unter derselben Wendung, in einer Sprache anders gelesen.

    unterwendung.py <buchNr …> | alle [--min 3] [--wieoft 1]

## Wozu

`mehrwort.py` findet den **Griff in die Wendung**: ein Einzelwort, das die
Glosse seines Mehrwort-Eintrags uebernommen hat. Es verlangt dafuer, dass die
uebernommene Glosse eine **Flexionsvariante** der Korpusmehrheit ist —
`main`/`mains`. Ohne diese Einschraenkung meldete die erste Fassung 18 335
Stellen.

Damit sieht es einen Fall nicht: wenn die uebernommene Glosse ein **ganz
anderes Wort** ist. Der Agent der Psalmen 40-41 hat ihn gefunden. `Gepriesen`
steht im Bestand achtmal auf *Praised* und zweimal auf *Blessed*, beide
Ausreisser in 1. Chronika — und darueber liegt jedes Mal derselbe
Mehrwort-Eintrag `gepriesen sein` = *Blessed be*. Das Einzelwort hatte sich
das *Blessed* aus der Wendung gegriffen. 1. Chronika 16,36 ist mit Psalm 41,14
elf Tokens lang wortgleich: zwei identische deutsche Saetze, zwei verschiedene
englische Glossen.

## Wie hier gefiltert wird

Nicht ueber die Korpusmehrheit der Wortform, sondern ueber das **Paar aus
Wortform und Wendungslemma**. `Gepriesen` unter `gepriesen sein` ist ein
anderer Fall als `Gepriesen` irgendwo sonst, und innerhalb des Paares ist die
Streuung klein genug, dass ein Ausreisser auffaellt.

Zwei Schwellen halten den Bericht lesbar:

- Die Mehrheitslesart des Paares muss **mindestens dreimal** belegt sein
  (`--min`). Bei zwei gegen eins gibt es keine Mehrheit, nur zwei Meinungen.
- Es weicht **genau eine Sprache** ab. Das ist die Signatur des Griffs: der
  Agent hat drei Spalten aus dem Bestand genommen und eine aus der Wendung.
  Weichen zwei oder mehr ab, ist es meist eine legitime Kontextvariante
  (Person, Tempus, Numerus).

## Wieviel es meldet

Gemessen am Stand vom 29.08.2026 ueber alle 46 Buecher: **243 Faelle.** Die
Trefferquote ist ungefaehr die von `qa.py` — ein gutes Drittel sind echte
Ausreisser (`Hause` unter `nach Hause` liest *house* statt *home*, `bis` unter
`bis zu` liest *up* statt *up to*), der Rest ist berechtigte Kontextvariation
(`fuerchten` als *be afraid* statt *fear*, `Angst` als *dread* statt *fear*).

**Jeder Treffer ist ein Verdacht.** Die Frage lautet: liest das Einzelwort hier
sein eigenes Wort oder das der Wendung?
"""
import argparse
import collections

import common as C
import hints


def sammeln(buecher):
    """(wortform, wendungslemma) -> {lesart: [(buch, kap, vers)]}"""
    paar = collections.defaultdict(lambda: collections.defaultdict(list))
    for nr in buecher:
        d = C.load_anno(nr)
        name = C.book_name(nr)
        for kap, verse in d['chapters'].items():
            for v, ee in verse.items():
                multis = [e for e in ee if C.is_multi(e)]
                if not multis:
                    continue
                einzel = {e['pos']: e for e in ee if not C.is_multi(e)}
                for m in multis:
                    for p in C.covered(m):
                        e = einzel.get(p)
                        if e is None:
                            continue
                        lesart = tuple(e[l] for l in C.LANGS)
                        paar[(e['form'], m['lemma'])][lesart].append((name, kap, v))
    return paar


def pruefe(paar, min_belege, wieoft, funktionswoerter):
    treffer = []
    for (form, lemma), lesarten in paar.items():
        if len(lesarten) < 2:
            continue
        if not funktionswoerter and form.lower() in hints.FUNKTION:
            continue
        sortiert = sorted(lesarten.items(), key=lambda x: -len(x[1]))
        top, topstellen = sortiert[0]
        if len(topstellen) < min_belege:
            continue
        for lesart, stellen in sortiert[1:]:
            if len(stellen) > wieoft:
                continue
            abw = [i for i in range(len(C.LANGS)) if lesart[i] != top[i]]
            if len(abw) != 1:
                continue
            i = abw[0]
            treffer.append((form, lemma, C.LANGS[i], lesart[i], top[i],
                            len(topstellen), stellen))
    return treffer


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buecher', nargs='*')
    p.add_argument('--min', type=int, default=3,
                   help='so oft muss die Mehrheitslesart des Paares belegt sein (Vorgabe 3)')
    p.add_argument('--wieoft', type=int, default=1,
                   help='so oft darf die abweichende Lesart hoechstens stehen (Vorgabe 1)')
    p.add_argument('--funktionswoerter', action='store_true')
    args = p.parse_args()

    # Der Vergleich braucht **immer** den ganzen Bestand: die Mehrheit eines
    # Paares steht meist in anderen Buechern als der Ausreisser. Die
    # Buchangabe filtert nur die Ausgabe.
    paar = sammeln(C.anno_books())
    treffer = pruefe(paar, args.min, args.wieoft, args.funktionswoerter)

    nur = None
    if args.buecher and args.buecher != ['alle']:
        nur = {C.book_name(int(b)) for b in args.buecher}

    gezeigt = 0
    for form, lemma, lang, wort, top, n, stellen in sorted(treffer, key=lambda x: -x[5]):
        for buch, kap, v in stellen:
            if nur and buch not in nur:
                continue
            print(f'{buch} {kap},{v}  `{form}` unter `{lemma}`  '
                  f'{lang}: {wort!r} statt {top!r} ({n} Belege)')
            gezeigt += 1
    print(f'\n{gezeigt} Faelle: dieselbe Wortform unter derselben Wendung, genau eine')
    print('Sprache weicht ab. Jeder Treffer ist ein Verdacht — liest das Einzelwort')
    print('hier sein eigenes Wort oder das der Wendung?')


if __name__ == '__main__':
    main()
