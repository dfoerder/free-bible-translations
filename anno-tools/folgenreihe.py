#!/usr/bin/env python3
"""Wie glossiert der Bestand eine WORTFOLGE? Vollstaendig, nie abgeschnitten.

    folgenreihe.py "So spricht der HERR" ["naechste Folge" ...]
    folgenreihe.py --buch <nr> "Folge"      nur die Buecher 1..nr-1 als Bestand

## Der Anlass

Fuer den Haggai-Prompt habe ich „So spricht der HERR" im Bestand gemessen,
mir die **zwei haeufigsten** von sechs Varianten ausgeben lassen und in den
Prompt geschrieben: „184 Vorkommen, alle mit `parle`". Der Agent hat
nachgemessen: **229 Vorkommen, vier davon mit `dit`**. Die Regel stimmte,
die Behauptung „alle" nicht.

Derselbe Fehler wie in Jona, wo ich ein Verszitat bei 95 Zeichen
abgeschnitten und aus dem Rest einen Befund abgeleitet hatte: **nie aus
einer abgeschnittenen Liste auf Vollstaendigkeit schliessen.**

Dieses Werkzeug schneidet nichts ab. Es zeigt jede Variante mit ihrer
Zahl und, wo es mehr als eine gibt, die Belegstellen der seltenen.

## Was es zaehlt

Jedes Vorkommen der Wortfolge im Quelltext eines Buches, das eine
Anno-Datei hat, mit den Glossen der **Einzeleintraege** an diesen
Positionen. Steht an einer Position kein Einzeleintrag (weil dort nur ein
Mehrwort liegt), faellt das Vorkommen als `(unvollstaendig)` heraus und
wird eigens gezaehlt — sonst waere die Gesamtzahl stillschweigend zu
klein, und genau daran ist die Haggai-Messung gescheitert.
"""
import sys, collections
import common as C


def stellen(phr, bis=None):
    # Der gerade Apostroph muss treffen wie der typografische: die
    # Vorbereitungsdateien und jede von Hand getippte Folge benutzen ihn.
    # Vorher fand `n'est pas` nichts und `n’est pas` alles — der Agent
    # fuer Matthaeus 18 hat einen Durchgang daran verloren.
    phr = phr.replace("'", '\u2019')
    w = [x.strip('.,;:!?„“"') for x in phr.split()]
    w = [x for x in w if x]
    # Eine Folge aus einer Bindungsdatei steht ohne Apostroph da
    # (`C est pourquoi`), der Quelltext hat ein Token (`C’est`). Ohne
    # diese Zeile meldet das Werkzeug „unbelegt", wo der Bestand
    # einstimmig ist.
    if not any('\u2019' in x for x in w):
        w = C.elision_zurueck(w)
    wk = [x.lower() for x in w]
    voll = collections.Counter()
    orte = collections.defaultdict(list)
    unvollstaendig = []
    mehrwort = collections.defaultdict(list)
    for nr in range(1, bis or 67):
        try:
            s = C.load_source(nr)
            anno = C.load_anno(nr)['chapters']
        except Exception:
            continue
        ch = s['chapters'] if 'chapters' in s else s
        for k, vv in ch.items():
            if k not in anno:
                continue
            for v, t in vv.items():
                if v not in anno[k] or wk[0] not in t.lower():
                    continue
                toks = [x.strip('.,;:!?„“"’') for x in t.split()]
                E = {e['pos']: e for e in anno[k][v]
                     if 'pos_end' not in e and 'parts' not in e}
                for i in range(len(toks) - len(w) + 1):
                    # Der Vergleich laeuft klein: `il y avait là` meldete
                    # 0, `Il y avait là` zwei einstimmige Vorkommen —
                    # dieselbe stille Null wie bei `garder/garda le
                    # silence`, nur ueber die Satzposition. Die Zeilen
                    # bleiben getrennt, wo die Glossen sich
                    # unterscheiden; die Zaehlung deckt jetzt beide
                    # Stellungen. Gemeldet vom Agenten fuer Marc 5.
                    if [x.lower() for x in toks[i:i + len(w)]] != wk:
                        continue
                    # Ein Mehrwort, das die Folge umspannt, wird
                    # IMMER erfasst — auch wenn alle Positionen
                    # zusaetzlich Einzeleintraege tragen, denn das
                    # Kopfwort behaelt seinen. Dessen Reihe ist oft die
                    # eigentliche Antwort: bei „Kehrt um" zerfaellt der
                    # Bestand als Einzelwort in sechs Varianten, als
                    # Mehrwort in genau drei — und die drei trennen sich
                    # nach Bedeutung (Richtung, Umkehrruf, Busse). Der
                    # Agent fuer Sacharja 1 musste das selbst
                    # herausfinden, weil hier frueher nur Einzelwoerter
                    # standen.
                    for m in anno[k][v]:
                        sp = m.get('parts', list(range(
                            m['pos'], m.get('pos_end', m['pos']) + 1)))
                        if len(sp) > 1 and min(sp) >= i \
                                and max(sp) < i + len(w):
                            mehrwort[(m['lemma'],) + C.reihe(m)].append(
                                f'{C.book_name(nr)} {k},{v}')
                    if not all(i + j in E for j in range(len(w))):
                        unvollstaendig.append(f'{C.book_name(nr)} {k},{v}')
                        continue
                    key = tuple(C.reihe(E[i + j])
                                for j in range(len(w)))
                    voll[key] += 1
                    orte[key].append(f'{C.book_name(nr)} {k},{v}')
    return w, voll, orte, unvollstaendig, mehrwort


def als_lemma(phr):
    """Steht die Folge als LEMMA eines Mehrworts im Bestand?

    `stellen()` sucht die Zeichenkette im Quelltext. Ein Mehrwort steht
    dort aber in seiner gebeugten Form: das Lemma `garder le silence`
    erscheint als `garda le silence` (Mt 26,63), und die Suche meldete
    dafuer 0 Vorkommen. Der Agent fuer Marc 3 hat es bemerkt — wer nur
    diese Null liest, erfindet ein vorhandenes Mehrwort neu.
    """
    phr = phr.replace("'", '\u2019').strip('.,;:!?„“"')
    treffer = collections.defaultdict(list)
    for nr, k, v, e in C.iter_corpus():
        if not C.is_multi(e) or e.get('lemma', '') != phr:
            continue
        treffer[(e.get('level', '?'),) + C.reihe(e)].append(
            f'{C.book_name(nr)} {k},{v}')
    return treffer


def main():
    args = list(sys.argv[1:])
    bis = None
    if '--buch' in args:
        i = args.index('--buch')
        bis = int(args[i + 1])
        del args[i:i + 2]
    if not args:
        print(__doc__)
        return 2
    print(f'*{C.bestandsstand()}*')
    for phr in args:
        w, voll, orte, unv, mehrwort = stellen(phr, bis)
        ges = sum(voll.values())
        print(f'\n# „{phr}"\n')
        print(f'{ges} vollstaendig glossierte Vorkommen, '
              f'{len(voll)} verschiedene Reihen'
              + (f', {len(unv)} mit Mehrwort an einer Position'
                 if unv else ''))
        if len(voll) == 1:
            print('**einstimmig**')
        print()
        for r, n in voll.most_common():
            anteil = f'{100 * n / ges:.0f}%' if ges else '—'
            print(f'  {n:5}  ({anteil})')
            for j, x in enumerate(r):
                print(f'      {w[j]:<24} ' + ' · '.join(x))
            if n <= 3:
                print(f'      → {", ".join(orte[r][:5])}')
            print()
        if mehrwort:
            ges_mw = sum(len(v) for v in mehrwort.values())
            print(f'  Als MEHRWORT gefasst: {ges_mw} Vorkommen, '
                  f'{len(mehrwort)} Reihen')
            print()
            for mkey, wo in sorted(
                    mehrwort.items(), key=lambda x: -len(x[1])):
                lemma, glossen = mkey[0], mkey[1:]
                print(f'  {len(wo):5}  [{lemma}]  ' + ' · '.join(glossen))
                print(f'      → {", ".join(wo[:6])}'
                      + (' …' if len(wo) > 6 else ''))
            print()
        elif unv:
            print(f'  Mehrwort an einer Position: {", ".join(unv[:8])}'
                  + (' …' if len(unv) > 8 else ''))
        if not ges and not mehrwort:
            lem = als_lemma(phr)
            if lem:
                n = sum(len(v) for v in lem.values())
                print(f'  **Als LEMMA eines Mehrworts im Bestand: '
                      f'{n} Vorkommen** — die Zeichenkette oben trifft '
                      f'nicht, weil das Mehrwort dort gebeugt steht.')
                print()
                for key, wo in sorted(lem.items(), key=lambda x: -len(x[1])):
                    print(f'  {len(wo):5}  [{phr}] {key[0]}  '
                          + ' · '.join(key[1:]))
                    print(f'      → {", ".join(wo[:6])}'
                          + (' …' if len(wo) > 6 else ''))
                print()
            else:
                print('  Auch nicht als Lemma eines Mehrworts im Bestand.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
