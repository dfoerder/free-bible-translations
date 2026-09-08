"""Drei Sprachen sind sich einig, die vierte weicht ab.

    ausreisser.py <buchNr …> | alle [--min 4]

Für jede Wortform wird die häufigste Lesart des Bestands bestimmt. Gemeldet
werden Einträge, die in **drei** Sprachen mit ihr übereinstimmen und in der
vierten nicht. Das findet Positionsverschiebungen und mechanisch angewandte
Grammatikregeln, die `konsistenz.py` prinzipiell nicht sehen kann: dort wird
je Lemma verglichen, hier je Sprache.

Der erste Lauf der alten Fassung ergab 862 Verdachtsfälle und 44 echte Fehler
— das Verhältnis gehört zur Natur der Prüfung. Sie ist für den **Abschluss
eines Buches** gedacht, nicht für jedes Kapitel.
"""
import argparse
import collections

import common as C
import hints


def bestand_lesarten(min_belege):
    """form -> (mehrheitliche Lesart als 4-Tupel, Anzahl)"""
    idx = collections.defaultdict(collections.Counter)
    for _, _, _, e in C.iter_corpus():
        if C.is_multi(e):
            continue
        idx[e['form']][tuple(e[l] for l in C.LANGS)] += 1
    haupt = {}
    for form, c in idx.items():
        lesart, n = c.most_common(1)[0]
        if n >= min_belege:
            haupt[form] = (lesart, n, sum(c.values()))
    return haupt


def pruefe(nrs, min_belege=4):
    haupt = bestand_lesarten(min_belege)
    treffer = []
    for nr in nrs:
        name = C.load_source(nr)['name']
        for _, kap, vers, e in C.iter_corpus([nr]):
            if C.is_multi(e) or e['form'] not in haupt:
                continue
            # Artikel, Pronomen und Präpositionen weichen legitim ständig ab
            # (Genus der Zielsprache, syntaktische Rolle) und würden die
            # echten Fälle zudecken — dieselbe Ausblendung wie in crosscheck.
            if e['form'].lower() in hints.FUNKTION or e['lemma'].lower() in hints.FUNKTION:
                continue
            lesart, n, ges = haupt[e['form']]
            eigene = tuple(e[l] for l in C.LANGS)
            abweichend = [i for i in range(4) if eigene[i] != lesart[i]]
            if len(abweichend) == 1:
                i = abweichend[0]
                treffer.append((f'{name} {kap},{vers}', e['form'], C.LANGS[i],
                                eigene[i], lesart[i], n, ges))
    for wo, form, lang, ist, soll, n, ges in treffer:
        print(f'{wo:<28} {form:<20} {lang}: *{ist}* — Bestand *{soll}* '
              f'({n}/{ges} Belege)')
    print(f'\n{len(treffer)} Verdachtsfälle. Drei Sprachen einig, die vierte '
          f'weicht ab — das ist oft eine legitime Genus- oder Registervariante. '
          f'Jeden Treffer am Vers ansehen.')
    return treffer


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('args', nargs='+')
    p.add_argument('--min', type=int, default=4)
    a = p.parse_args()
    if a.args[0] == 'alle':
        nrs = C.anno_books()
    else:
        nrs = [int(x) for x in a.args]
        # `ausreisser.py 45 10` sah aus wie zwei Buecher und starb mit
        # einem FileNotFoundError auf `10_…json`. Gemeldet vom Agenten
        # fuer Roemer 10 — dieselbe Falle wie bei `reflexiv.py 44 8`
        # und `lexicon.py tribun`: eine KAPITELnummer an der Stelle
        # einer Buchnummer. Dieses Skript prueft immer ganze Buecher.
        da = set(C.anno_books())
        fehlt = [n for n in nrs if n not in da]
        if fehlt:
            print('Kein Bestand fuer Buch ' +
                  ', '.join(str(n) for n in fehlt) + '.')
            if len(nrs) > len(fehlt):
                print('Sieht nach einer KAPITELnummer aus — '
                      'ausreisser.py nimmt nur Buchnummern und '
                      'prueft immer ganze Buecher. Fuer ein '
                      'einzelnes Kapitel gibt es `folgencheck --kapitel`.')
            raise SystemExit(1)
    pruefe(nrs, a.min)
