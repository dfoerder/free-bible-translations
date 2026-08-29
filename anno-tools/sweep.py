"""Jede Mehrwort-Wendung des Bestands im Quelltext suchen — wo fehlt der Eintrag?

    sweep.py <buchNr …> | alle [--min 3] [--deckung 0.75] [--kapitel 3 4 5]

## Wozu

`konvention.py` prueft fuenf von Hand eingetragene Wendungen (`um zu`, `so wie`,
`genau wie`, `nicht mehr`, `wie wenn`). Der Bestand fuehrt aber **3835**
verschiedene Mehrwort-Lemmata. Ein fehlender Mehrwort-Eintrag ist strukturell
kein Fehler — `selfcheck.py` und `qa.py` koennen ihn prinzipiell nicht sehen,
weil jede Position ihren Einzeleintrag hat und alles zaehlt. Er faellt erst im
Lesefluss auf, wo `stand auf` als *stood* + *on* erscheint statt als *got up*.

In Hiob haben sich die Kapitel 39 und 41 dafuer eigene Skripte gebaut und
zusammen dreizehn echte Luecken gefunden. Das ist dieses Skript, dauerhaft.

## Wie die Fehlalarme klein bleiben

Der Trick ist der **Deckungsgrad**. Zu jeder Wendung wird ausgezaehlt, wie oft
ihre Wortfolge im annotierten Quelltext ueberhaupt vorkommt und wie oft dort
ein Mehrwort-Eintrag darauf liegt. `gab es` ist zu 96 % gedeckt — ein
ungedecktes Vorkommen ist dann eine Luecke. `die Hand` waere zu 4 % gedeckt und
faellt heraus: die Wortfolge steht meistens woertlich da und ist zu Recht
einzeln annotiert.

Ohne diese Schwelle meldet der Lauf ueber Hiob mehrere hundert Stellen, fast
alles woertliche Verwendungen. Mit `--deckung 0.75` bleiben die uebrig, bei
denen der Bestand selbst sagt: diese Wortfolge ist fast immer eine Wendung.

Gesucht wird die **Wortform**, nicht das Lemma. `stand auf`, `standen auf` und
`steh auf` sind drei Muster mit eigener Statistik. Das kostet Trefferquote —
eine Form, die der Bestand noch nie gesehen hat, kann nicht gefunden werden —
aber es macht jeden Treffer nachpruefbar.

Getrennte Verbzusaetze werden mit Abstand gesucht, hoechstens so weit
auseinander, wie der Bestand es fuer genau dieses Muster belegt.

## Was ein Treffer bedeutet

Ein **Verdacht**. Die Frage lautet: steht die Wortfolge hier als Wendung oder
woertlich? `Er stand auf dem Berg` ist kein `aufstehen`. Der Bericht druckt
deshalb den Vers mit, damit die Entscheidung ohne Nachschlagen faellt.
"""
import argparse
import collections
import json
import os
import sys

import common as C

MAXLEN = 5          # laengere Wendungen tragen nichts bei, kosten nur Zeit
MAXGAP = 14         # weiter auseinander steht kein Verbzusatz im Bestand


def _toks(text):
    """[(index_im_split, wort_klein_ohne_satzzeichen)] — Satzzeichen fallen raus,
    die Indizes bleiben die des ungefilterten `split()`, denn danach zaehlen
    die `pos`-Angaben der Eintraege."""
    out = []
    for i, t in enumerate(text.split()):
        w = C.strip_punct(t).lower()
        if w:
            out.append((i, w))
    return out


def muster_sammeln():
    """muster -> [abstand_max, anzahl_als_wendung]

    Muster ist die Wortfolge, wie sie im Quelltext steht, an den Positionen
    des Mehrwort-Eintrags abgelesen. Nicht die `form` des Eintrags: die ist
    gelegentlich normalisiert (`sich sammeln` fuer `sammle dich`), das Muster
    muss aber im Quelltext wiederfindbar sein.
    """
    muster = {}
    for nr in C.anno_books():
        src = C.load_source(nr)['chapters']
        d = C.load_anno(nr)
        for kap, verses in d['chapters'].items():
            for vers, entries in verses.items():
                roh = src[kap][vers].split()
                for e in entries:
                    if not C.is_multi(e):
                        continue
                    pos = C.covered(e)
                    if len(pos) > MAXLEN or max(pos) >= len(roh):
                        continue
                    woerter = tuple(C.strip_punct(roh[p]).lower() for p in pos)
                    if any(not w for w in woerter):
                        continue
                    spanne = max(pos) - min(pos)
                    if spanne > MAXGAP:
                        continue
                    rec = muster.setdefault(woerter, [0, 0])
                    rec[0] = max(rec[0], spanne)
                    rec[1] += 1
    return muster


def _finden(tf, muster_nach_erstwort):
    """Alle Musterfundstellen in einem Vers: [(startpos, endpos, muster)]"""
    treffer = []
    for i, (pos_i, w) in enumerate(tf):
        for woerter, abstand in muster_nach_erstwort.get(w, ()):
            j, k = i + 1, 1
            gefunden = [pos_i]
            while k < len(woerter) and j < len(tf) and tf[j][0] - pos_i <= abstand:
                if tf[j][1] == woerter[k]:
                    gefunden.append(tf[j][0])
                    k += 1
                j += 1
            if k == len(woerter):
                treffer.append((gefunden[0], gefunden[-1], woerter))
    # Von zwei Fundstellen desselben Musters die engere behalten. Hiob 40,32
    # hat gezeigt, warum: `an ... denken` fand das erste `an` in `Legst du
    # deine Hand einmal an es` und meldete eine Luecke, waehrend der richtige
    # Eintrag zwei Woerter spaeter auf `an diesen Kampf ... denken` liegt.
    eng = []
    for a in treffer:
        if not any(b is not a and b[2] == a[2] and b[0] >= a[0] and b[1] <= a[1]
                   and (b[1] - b[0]) < (a[1] - a[0]) for b in treffer):
            eng.append(a)
    return eng


def _gedeckt(entries, start, ende):
    """Liegt ein Mehrwort-Eintrag darueber?

    Zwei Faelle zaehlen als gedeckt. Der erste ist die Ueberspannung: eine
    Wortfolge innerhalb einer groesseren Wendung ist keine Luecke, sondern
    Teil davon.

    Der zweite ist das belegte Ankerwort. Ein Wort kann nicht zu zwei
    Wendungen gehoeren. Hiob 18,2 hat es gezeigt: dort steht `hört auf` als
    `aufhören` auf [1,4], und das Muster `hört zu` griff ueber diesen Eintrag
    hinweg nach dem `zu` des folgenden Infinitivs. Wo das erste Wort schon
    vergeben ist, ist die Stelle entschieden — richtig oder falsch, aber nicht
    uebersehen. Dasselbe in 18,5, 29,8 und 20,22.
    """
    for e in entries:
        if not C.is_multi(e):
            continue
        pos = C.covered(e)
        lo, hi = min(pos), max(pos)
        if (lo <= start and hi >= ende) or (lo <= start <= hi):
            return True
    return False


def deckungsgrad(muster, min_belege):
    """muster -> (gedeckt, gesamt) ueber den gesamten annotierten Bestand."""
    nach_erstwort = collections.defaultdict(list)
    for woerter, (abstand, n) in muster.items():
        if n >= min_belege:
            nach_erstwort[woerter[0]].append((woerter, abstand))
    zaehler = collections.defaultdict(lambda: [0, 0])
    for nr in C.anno_books():
        src = C.load_source(nr)['chapters']
        d = C.load_anno(nr)
        for kap, verses in d['chapters'].items():
            for vers, entries in verses.items():
                tf = _toks(src[kap][vers])
                for start, ende, w in _finden(tf, nach_erstwort):
                    z = zaehler[w]
                    z[1] += 1
                    if _gedeckt(entries, start, ende):
                        z[0] += 1
    return nach_erstwort, zaehler


def kapitel_eintraege(nr, kap, out):
    """Eintraege eines Kapitels — aus dem Arbeitsordner, sonst der Kapitelquelle,
    sonst der gebauten Anno-Datei."""
    if out:
        p = os.path.join(out, str(nr), f'ch{kap}.json')
        if os.path.exists(p):
            with open(p, encoding='utf-8') as f:
                return json.load(f)
    q = C.load_quelle(nr, kap)
    if q is not None:
        return q
    if C.has_anno(nr):
        return C.load_anno(nr)['chapters'].get(str(kap))
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buecher', nargs='+')
    p.add_argument('--min', type=int, default=3,
                   help='so oft muss der Bestand das Muster als Wendung fuehren (Vorgabe 3)')
    p.add_argument('--deckung', type=float, default=0.75,
                   help='ab diesem Anteil gedeckter Vorkommen gilt die Wortfolge '
                        'als Wendung und ein ungedecktes Vorkommen als Luecke (Vorgabe 0.75)')
    p.add_argument('--kapitel', nargs='*', help='nur diese Kapitel')
    args = p.parse_args()

    out = os.environ.get('ANNO_OUT')
    if out and not out.endswith('/'):
        out += '/'

    print('Muster sammeln …', file=sys.stderr)
    muster = muster_sammeln()
    print(f'{len(muster)} Muster, davon {sum(1 for v in muster.values() if v[1] >= args.min)} '
          f'ab {args.min} Belegen', file=sys.stderr)
    print('Deckungsgrad auszaehlen …', file=sys.stderr)
    nach_erstwort, zaehler = deckungsgrad(muster, args.min)

    fest = collections.defaultdict(list)
    for woerter, (ged, ges) in zaehler.items():
        if ges and ged / ges >= args.deckung:
            fest[woerter[0]].append((woerter, muster[woerter][0], ged, ges))
    n_fest = sum(len(v) for v in fest.values())
    print(f'{n_fest} Muster ueber der Deckungsschwelle\n', file=sys.stderr)

    nummern = C.anno_books() if args.buecher == ['alle'] else [int(b) for b in args.buecher]
    gesamt = 0
    for nr in nummern:
        s = C.load_source(nr)
        kaps = args.kapitel or sorted(s['chapters'], key=int)
        befunde = []
        for kap in kaps:
            kap = str(int(kap))
            entries_kap = kapitel_eintraege(nr, kap, out)
            if entries_kap is None:
                continue
            for vers, text in s['chapters'][kap].items():
                entries = entries_kap.get(vers)
                if entries is None:
                    continue
                tf = _toks(text)
                such = {w: [(m, ab) for m, ab, _, _ in v] for w, v in fest.items()}
                for start, ende, w in _finden(tf, such):
                    if _gedeckt(entries, start, ende):
                        continue
                    ged, ges = zaehler[w]
                    befunde.append((kap, vers, w, ende - start, ged, ges, text))
        if not befunde:
            continue
        print(f'\n## {s["name"]}\n')
        for kap, vers, w, abstand, ged, ges, text in befunde:
            weite = '' if abstand == len(w) - 1 else f' · Abstand {abstand}'
            print(f'{kap},{vers}  `{" ".join(w)}`  — Bestand {ged}/{ges} gedeckt{weite}')
            print(f'   {text}')
            gesamt += 1
    print(f'\n{gesamt} ungedeckte Vorkommen einer im Bestand gefuehrten Wendung.')
    print('Jeder Treffer ist ein Verdacht: steht die Wortfolge hier als Wendung')
    print('oder woertlich? `Er stand auf dem Berg` ist kein `aufstehen`.')


if __name__ == '__main__':
    main()
