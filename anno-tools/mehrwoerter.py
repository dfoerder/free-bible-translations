"""Die Mehrwoerter, bei denen der Bestand selbst geteilter Meinung ist.

    mehrwoerter.py <buchNr> <kapitel> <datei.json> [--von 0.15] [--bis 0.6]

## Die Luecke zwischen `sweep.py` und `sweeplemma.py`

Beide arbeiten mit einer **Deckungsschwelle** — `sweep.py` mit 0,75,
`sweeplemma.py` mit 0,6 — und melden nur, was darueber liegt. Das ist
richtig so: eine Signatur wie (`der`, `Hand`) steht fast immer woertlich
da, und ohne Schwelle waere der Lauf unlesbar.

Aber genau darunter liegt das Interessante. Eine Signatur, die der
Bestand in der HAELFTE der Faelle als Wendung fasst und in der anderen
Haelfte nicht, ist kein Rauschen — sie ist eine Stelle, an der der
Bestand ein **Kriterium** kennt, das nirgends aufgeschrieben steht.

Der Agent fuer Roemer 7 hat das an `un autre` gezeigt: 18-mal als
Mehrwort, 17-mal nicht, Deckung 0,51 — also unter beiden Schwellen und
in keinem der beiden Laeufe sichtbar. Er hat sich dafuer ein eigenes
Skript gebaut, alle 1922 Mehrwort-Oberflaechen des Bestands gegen
seinen Kapiteltext gehalten und dabei das Kriterium gefunden: **der
Bestand setzt das Mehrwort nur beim pronominalen Gebrauch** (`à un
autre`, `épouse une autre`), nie vor folgendem Nomen. Er war der achte
Agent, der ein solches Skript gebraucht hat.

`--alle` in `sweeplemma.py` zeigt zwar auch die niedrig gedeckten
Signaturen, aber ohne die Gegenseite: man sieht, dass eine Signatur zu
51 Prozent gedeckt ist, und weiss danach genauso wenig, wo die Grenze
laeuft.

## Was dieses Werkzeug anders macht

Es meldet **nur das Mittelfeld** (0,15 bis 0,6) und druckt zu jeder
Signatur BEIDE Seiten mit Stellen und Reihen:

    `un autre`  18 als Wendung / 35 gesamt = 51%
       als Wendung:  Luc 9,59 · Luc 16,7 · Jean 5,7
       woertlich:    Mt 8,9 · Mt 12,45 · Marc 12,31

Damit ist die Frage am Vers zu entscheiden, ohne dass jemand sich ein
Skript baut. Was oberhalb von 0,6 liegt, holt `sweeplemma.py`; was
unterhalb von 0,15 liegt, ist Rauschen.

## Was ein Treffer bedeutet

Einen **Verdacht**, wie ueberall. Der Bestand kann an einer geteilten
Signatur auch schlicht uneinheitlich sein — dann ist der Treffer die
Aufforderung, die Uneinheitlichkeit zu melden, nicht sie fortzusetzen.
"""
import argparse
import collections
import json

import common as C

MAXLEN = 5
MAXGAP = 14


def _vorkommen(lem_nach_pos, s, abstand):
    """Alle Fundstellen der Signatur s in einem Vers: [(start, ende)]"""
    posn = sorted(lem_nach_pos)
    treffer = []
    for i, p in enumerate(posn):
        if lem_nach_pos[p] != s[0]:
            continue
        k, j, gef = 1, i + 1, [p]
        while k < len(s) and j < len(posn) and posn[j] - p <= abstand:
            if lem_nach_pos[posn[j]] == s[k]:
                gef.append(posn[j])
                k += 1
            j += 1
        if k == len(s):
            treffer.append(tuple(gef))
    eng = []
    for a in treffer:
        if not any(b != a and b[0] >= a[0] and b[-1] <= a[-1] for b in treffer):
            eng.append(a)
    return eng


def bestand(nr, kapitel):
    """signatur -> (abstand, ja, gesamt, orte_ja, orte_nein)

    Das eigene Kapitel zaehlt nicht mit — sonst bestaetigt die Abgabe
    sich selbst.
    """
    sig = {}
    for b in C.anno_books():
        d = C.load_anno(b)
        for kap, verses in d['chapters'].items():
            if int(b) == int(nr) and str(kap) == str(kapitel):
                continue
            for vers, entries in verses.items():
                lem = {e['pos']: e['lemma']
                       for e in entries if not C.is_multi(e)}
                for e in entries:
                    if not C.is_multi(e):
                        continue
                    pos = C.covered(e)
                    if len(pos) > MAXLEN or not all(p in lem for p in pos):
                        continue
                    spanne = max(pos) - min(pos)
                    if spanne > MAXGAP:
                        continue
                    s = tuple(lem[p] for p in pos)
                    rec = sig.setdefault(s, [0, 0, 0, [], []])
                    rec[0] = max(rec[0], spanne)

    nach_erst = collections.defaultdict(list)
    for s, rec in sig.items():
        nach_erst[s[0]].append((s, rec[0]))

    for b in C.anno_books():
        d = C.load_anno(b)
        for kap, verses in d['chapters'].items():
            if int(b) == int(nr) and str(kap) == str(kapitel):
                continue
            for vers, entries in verses.items():
                lem = {e['pos']: e['lemma']
                       for e in entries if not C.is_multi(e)}
                gedeckt = {}
                spannen = {}
                for e in entries:
                    if C.is_multi(e):
                        pos = C.covered(e)
                        spannen[frozenset(pos)] = e.get('lemma', '?')
                        for p in pos:
                            gedeckt[p] = e.get('lemma', '?')
                kand = set()
                for p, l in lem.items():
                    for paar in nach_erst.get(l, ()):
                        kand.add(paar)
                for s, abstand in kand:
                    for gef in _vorkommen(lem, s, abstand):
                        rec = sig[s]
                        wo = f'{C.book_name(b)} {kap},{vers}'
                        genau = spannen.get(frozenset(gef))
                        if genau is not None:
                            rec[1] += 1
                            rec[2] += 1
                            # WELCHE Wendung dort liegt, ist die eigentliche
                            # Auskunft.
                            if len(rec[3]) < 4:
                                rec[3].append(f'{wo} (`{genau}`)')
                        elif any(p in gedeckt for p in gef):
                            # Eine ANDERE Wendung liegt darauf (`parce que`
                            # ueber der Signatur (`être`, `que`)). Diese
                            # Stelle stand nie zur Wahl und gehoert in
                            # keine der beiden Zahlen — sonst zaehlt jedes
                            # zufaellige Nebeneinander als Gegenbeleg und
                            # traegt eine Signatur ins Mittelfeld, die dort
                            # nichts zu suchen hat.
                            continue
                        else:
                            rec[2] += 1
                            if len(rec[4]) < 4:
                                rec[4].append(wo)
    return sig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('buch', type=int)
    ap.add_argument('kapitel')
    ap.add_argument('datei')
    ap.add_argument('--von', type=float, default=0.15)
    ap.add_argument('--bis', type=float, default=0.6)
    a = ap.parse_args()

    with open(a.datei, encoding='utf-8') as f:
        kap = json.load(f)
    if kap and isinstance(next(iter(kap.values())), dict):
        kap = kap.get(str(a.kapitel), kap)
    src = C.load_source(a.buch)['chapters'][str(a.kapitel)]

    sig = bestand(a.buch, a.kapitel)
    geteilt = {}
    for s, (abstand, ja, ges, orte_ja, orte_nein) in sig.items():
        if not ges:
            continue
        q = ja / ges
        if a.von <= q < a.bis:
            geteilt[s] = (abstand, ja, ges, q, orte_ja, orte_nein)

    nach_erst = collections.defaultdict(list)
    for s, rec in geteilt.items():
        nach_erst[s[0]].append(s)

    befunde = []
    for vers in sorted(kap, key=int):
        entries = kap[vers]
        lem = {e['pos']: e['lemma'] for e in entries if not C.is_multi(e)}
        gedeckt = set()
        for e in entries:
            if C.is_multi(e):
                gedeckt |= set(C.covered(e))
        kand = set()
        for p, l in lem.items():
            for s in nach_erst.get(l, ()):
                kand.add(s)
        for s in sorted(kand):
            abstand = geteilt[s][0]
            for gef in _vorkommen(lem, s, abstand):
                if any(p in gedeckt for p in gef):
                    continue
                befunde.append((vers, gef[0], gef[-1], s))

    print(f'# Geteilte Mehrwoerter: {C.book_name(a.buch)} {a.kapitel} '
          f'— {a.datei}')
    print(f'# Deckung zwischen {a.von:.0%} und {a.bis:.0%}: '
          f'{len(geteilt)} Signaturen im Bestand')
    print()
    if not befunde:
        print('0 geteilte Signaturen in diesem Kapitel ungedeckt.')
        print()
        print('Das heisst NICHT, dass keine Wendung fehlt — nur, dass keine '
              'aus dem\nMittelfeld hier ungedeckt steht. Oberhalb von '
              f'{a.bis:.0%} prueft `sweeplemma.py`.')
        return
    for vers, start, ende, s in befunde:
        _, ja, ges, q, orte_ja, orte_nein = geteilt[s]
        print(f'{a.kapitel},{vers} pos {start}–{ende}  `{" ".join(s)}`  '
              f'{ja} als Wendung / {ges} gesamt = {q:.0%}')
        print(f'    als Wendung:  {" · ".join(orte_ja) or "—"}')
        print(f'    woertlich:    {" · ".join(orte_nein) or "—"}')
        print(f'    {src[vers]}')
        print()
    print(f'{len(befunde)} Verdachtsfaelle. Der Bestand ist hier GETEILT — '
          'suche das\nKriterium an den beiden Seiten, statt der Mehrheit zu '
          'folgen. Wo es\nkeines gibt, ist die Uneinheitlichkeit selbst der '
          'Befund und gehoert\ngemeldet.')


if __name__ == '__main__':
    main()
