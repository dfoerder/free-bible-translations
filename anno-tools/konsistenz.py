"""Ein Lemma, zwei Lesarten — innerhalb eines Buches und gegen den Bestand.

    konsistenz.py <buchNr> [--min 3]

`crosscheck.py` prüft zwei Hälften **eines** Kapitels, `konsistenz.py` ein
ganzes Buch:

- **Abschnitt A** — Lemmata, die innerhalb des Buches zwei Lesarten tragen.
- **Abschnitt B** — Lemmata, deren Buchlesart von der Bestandsmehrheit
  abweicht. Beschränkt auf Substantive und auf Bestandslesarten mit
  mindestens `--min` Belegen: bei Verben und Adjektiven überwiegen Person-,
  Numerus- und Tempusvarianten so stark, dass die echten Fälle im Rauschen
  verschwinden.

Numerus, Genus und vorangestellte Kasuspräpositionen werden zusammengefasst,
sonst besteht der Bericht nur aus Singular/Plural-Paaren.

Es findet, was kein Agent sehen kann, weil es **zwischen** Kapiteln liegt.
"""
import argparse
import collections

import common as C

# Vorangestellte Artikel und Kasuspräpositionen aller vier Zielsprachen.
# Ohne sie besteht der Bericht aus Paaren wie `Abraham` / `de Abraham`.
VORWEG = ('of the ', 'to the ', 'in the ', 'from the ', 'with the ', 'of ', 'to ',
          'the ', 'a ', 'an ', 'in ', 'from ', 'with ', 'for ', 'and ',
          'de la ', 'de los ', 'de las ', 'del ', 'de ', 'al ', 'a la ', 'los ',
          'las ', 'el ', 'la ', 'un ', 'una ', 'en ', 'con ', 'para ', 'por ',
          'du ', 'des ', 'au ', 'aux ', 'le ', 'les ', 'une ', 'dans ', 'avec ',
          "d'", "l'", "dell'", "dei ", 'delle ', 'dello ', 'della ', 'degli ',
          'il ', 'lo ', 'gli ', 'nel ', 'nella ', 'sul ', 'con ')


def _kern(g):
    g = g.lower().strip()
    for p in VORWEG:
        if g.startswith(p):
            g = g[len(p):]
            break
    return g.rstrip('s').rstrip('e')


def _gruppe(e):
    """Lesart ohne Numerus- und Kasusvariation."""
    return tuple(_kern(e[l]) for l in C.LANGS)


LIMIT_A = 60


def bericht(nr, min_belege=3, alle=False):
    nr = int(nr)
    eigen = collections.defaultdict(lambda: collections.defaultdict(list))
    name = C.load_source(nr)['name']
    for _, kap, vers, e in C.iter_corpus([nr]):
        if C.is_multi(e):
            continue
        eigen[e['lemma']][_gruppe(e)].append((f'{kap},{vers}', e['en']))

    bestand = collections.defaultdict(collections.Counter)
    bestand_bsp = {}
    for other in C.anno_books():
        if other == nr:
            continue
        oname = C.load_source(other)['name']
        for _, kap, vers, e in C.iter_corpus([other]):
            if C.is_multi(e):
                continue
            g = _gruppe(e)
            bestand[e['lemma']][g] += 1
            bestand_bsp.setdefault((e['lemma'], g), (e['en'], f'{oname} {kap},{vers}'))

    print(f'# Konsistenz: {name}\n')

    print('## A — zwei Lesarten innerhalb des Buches\n')
    kandidaten = []
    einzelfaelle = 0
    for lemma, gruppen in eigen.items():
        if len({g[0] for g in gruppen}) < 2:   # nur echte Bedeutungsspaltungen
            continue
        groessen = sorted((len(s) for s in gruppen.values()), reverse=True)
        if groessen[1] < 2:                    # Einzelbeleg gegen den Rest
            einzelfaelle += 1
            continue
        kandidaten.append((groessen[1], lemma, gruppen))
    kandidaten.sort(key=lambda x: (-x[0], x[1]))
    for _, lemma, gruppen in kandidaten if alle else kandidaten[:LIMIT_A]:
        print(f'`{lemma}`')
        for g, stellen in sorted(gruppen.items(), key=lambda x: -len(x[1])):
            orte = ', '.join(s for s, _ in stellen[:5])
            print(f'   {len(stellen):>3}× *{stellen[0][1]}* — {orte}'
                  + (' …' if len(stellen) > 5 else ''))
    if len(kandidaten) > LIMIT_A and not alle:
        print(f'\n… {len(kandidaten) - LIMIT_A} weitere (Aufruf mit --alle)')
    print(f'\n{len(kandidaten)} Lemmata mit zwei belegten Lesarten, dazu '
          f'{einzelfaelle} mit einem einzelnen abweichenden Beleg.\n')

    print(f'## B — Buchlesart weicht von der Bestandsmehrheit ab '
          f'(Substantive, ab {min_belege} Belegen)\n')
    m = 0
    for lemma, gruppen in sorted(eigen.items()):
        if not lemma[:1].isupper():          # nur Substantive und Namen
            continue
        if lemma not in bestand:
            continue
        haupt, cnt = bestand[lemma].most_common(1)[0]
        if cnt < min_belege:
            continue
        eigene = max(gruppen.items(), key=lambda x: len(x[1]))[0]
        # Nur melden, wenn die **englische** Lesart abweicht. Weicht nur eine
        # der drei romanischen Sprachen ab, ist es fast immer eine legitime
        # Genus- oder Registervariante; dafür ist ausreisser.py da.
        if eigene[0] == haupt[0]:
            continue
        m += 1
        bsp_en, bsp_wo = bestand_bsp[(lemma, haupt)]
        stellen = gruppen[eigene]
        print(f'`{lemma}` — hier *{stellen[0][1]}* ({len(stellen)}×, '
              f'{", ".join(s for s, _ in stellen[:3])}) · '
              f'Bestand *{bsp_en}* ({cnt}×, {bsp_wo})')
    print(f'\n{m} Abweichungen von der Bestandsmehrheit.')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('--min', type=int, default=3)
    p.add_argument('--alle', action='store_true')
    a = p.parse_args()
    bericht(a.buch, a.min, a.alle)
