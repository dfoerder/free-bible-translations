"""Die Mehrwort-Luecken, die `sweep.py` prinzipiell nicht finden kann.

    sweeplemma.py <buchNr> <kapitel> <datei.json> [--deckung 0.6] [--alle]

## Wozu, und warum es nicht dasselbe ist wie sweep.py

`sweep.py` sagt es in seiner eigenen Dokumentation: „Gesucht wird die
**Wortform**, nicht das Lemma. Das kostet Trefferquote — eine Form, die der
Bestand noch nie gesehen hat, kann nicht gefunden werden."

Genau diese Luecke hat in den Paketen 9 und 10 von Jesaja **elf** Bestands-
Mehrwoerter durchgelassen, und drei Agenten hintereinander haben sich dafuer
ihr eigenes Skript gebaut:

  * `dahinschwinden`   (24,6)  — steht getrennt als „schwinden … dahin"
  * `hoffen auf`       (25,9 zweimal, 26,8) — 37 Belege
  * `machen zu`        (25,2)  — 36 Belege
  * `geboren werden`   (26,18) — 31 Belege
  * `in den Kampf ziehen` (27,4) — 20 Belege
  * `zu Boden werfen`  (25,12) — vom Nachbarkapitel gefunden, nicht vom Skript

Der Unterschied liegt in der **Flexion**. `sweep.py` kennt das Muster
(`hoffen`, `auf`) nur in den Wortformen, in denen es im Bestand schon steht.
„auf den wir **gehofft** haben" ist eine neue Form — also schweigt es. Dieses
Skript arbeitet stattdessen auf den **Lemmata, die der Agent selbst vergeben
hat**, und trifft deshalb jede Flexion.

## Der Preis dafuer

Es braucht die **fertige Kapiteldatei** als Eingabe, nicht nur den Quelltext.
Es ist also kein Vorbereitungswerkzeug, sondern ein Pruefwerkzeug fuer die
Abgabe — genau wie `selfcheck.py`.

## Wie die Fehlalarme klein bleiben

Wie bei `sweep.py` ueber den **Deckungsgrad**: zu jeder Lemma-Signatur wird
ausgezaehlt, wie oft sie im annotierten Bestand ueberhaupt vorkommt und wie oft
dort ein Mehrwort-Eintrag darauf liegt. Eine Signatur wie (`der`, `Hand`) steht
fast immer woertlich da und faellt heraus; (`hoffen`, `auf`) ist hoch gedeckt,
ein ungedecktes Vorkommen ist dann eine Luecke.

Die Schwelle ist mit 0,6 niedriger als bei `sweep.py` (0,75), weil die
Lemma-Signatur schaerfer trennt als die Wortform: sie unterscheidet `liegen an`
von `legen an`, wo die Form `lag an` beides sein kann.

## Was ein Treffer bedeutet

Einen **Verdacht**, nicht einen Fehler — dieselbe Regel wie ueberall. Der
Bericht druckt den Vers mit, damit die Entscheidung ohne Nachschlagen faellt.
`Er stand auf dem Berg` ist kein `aufstehen`, und `so wertvoll wie Gold` ist
keine Vergleichsklammer.
"""
import argparse
import collections
import json
import sys

import common as C

MAXLEN = 5      # laengere Signaturen tragen nichts bei
MAXGAP = 14     # weiter auseinander steht kein Verbzusatz im Bestand


def signaturen():
    """lemma-signatur -> [abstand_max, als_wendung, gesamt]

    Die Signatur ist die Folge der **Einzelwort-Lemmata** an den Positionen des
    Mehrwort-Eintrags — nicht das `lemma`-Feld des Eintrags selbst. Das Feld ist
    eine Zitierform (`sich sammeln` fuer `sammle dich`) und im Vers nicht
    wiederfindbar; die Lemmata der Einzeleintraege sind es.
    """
    sig = {}
    gesamt = collections.Counter()
    for nr in C.anno_books():
        d = C.load_anno(nr)
        for kap, verses in d['chapters'].items():
            for vers, entries in verses.items():
                lem = {e['pos']: e['lemma'] for e in entries if not C.is_multi(e)}
                # Vorkommen jeder bekannten Signatur zaehlen wir spaeter;
                # hier nur die tatsaechlich als Wendung markierten.
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
                    rec = sig.setdefault(s, [0, 0])
                    rec[0] = max(rec[0], spanne)
                    rec[1] += 1
    return sig


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
            treffer.append((gef[0], gef[-1]))
    # Von ueberlappenden Fundstellen die engere behalten (wie sweep.py)
    eng = []
    for a in treffer:
        if not any(b != a and b[0] >= a[0] and b[1] <= a[1] for b in treffer):
            eng.append(a)
    return eng


def deckung_zaehlen(sig):
    """Wie oft steht jede Signatur im Bestand ueberhaupt da (gedeckt oder nicht)?"""
    gesamt = collections.Counter()
    nach_erst = collections.defaultdict(list)
    for s, (abstand, _) in sig.items():
        nach_erst[s[0]].append((s, abstand))
    for nr in C.anno_books():
        d = C.load_anno(nr)
        for kap, verses in d['chapters'].items():
            for vers, entries in verses.items():
                lem = {e['pos']: e['lemma'] for e in entries if not C.is_multi(e)}
                kand = set()
                for p, l in lem.items():
                    for s, abstand in nach_erst.get(l, ()):
                        kand.add((s, abstand))
                for s, abstand in kand:
                    gesamt[s] += len(_vorkommen(lem, s, abstand))
    return gesamt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('buch', type=int)
    ap.add_argument('kapitel')
    ap.add_argument('datei')
    ap.add_argument('--deckung', type=float, default=0.6)
    ap.add_argument('--alle', action='store_true',
                    help='auch Signaturen unterhalb der Deckungsschwelle zeigen')
    a = ap.parse_args()

    with open(a.datei, encoding='utf-8') as f:
        kap = json.load(f)
    src = C.load_source(a.buch)['chapters'][str(a.kapitel)]

    sig = signaturen()
    gesamt = deckung_zaehlen(sig)
    nach_erst = collections.defaultdict(list)
    for s, (abstand, alswendung) in sig.items():
        g = gesamt.get(s, 0)
        quote = alswendung / g if g else 0.0
        if not a.alle and quote < a.deckung:
            continue
        nach_erst[s[0]].append((s, abstand, alswendung, quote))

    befunde = []
    for vers in sorted(kap, key=int):
        entries = kap[vers]
        lem = {e['pos']: e['lemma'] for e in entries if not C.is_multi(e)}
        belegt = set()
        for e in entries:
            if C.is_multi(e):
                belegt |= set(C.covered(e))
        kand = set()
        for p, l in lem.items():
            for rec in nach_erst.get(l, ()):
                kand.add(rec)
        for s, abstand, alswendung, quote in sorted(kand):
            for start, ende in _vorkommen(lem, s, abstand):
                spanne = set(range(start, ende + 1)) & set(lem)
                if spanne & belegt:
                    continue
                befunde.append((vers, start, ende, s, alswendung, quote))

    print(f'# Lemma-Sweep: {C.book_name(a.buch)} {a.kapitel} — {a.datei}')
    print(f'# {len(nach_erst)} Erstlemmata, Deckungsschwelle {a.deckung}')
    print()
    if not befunde:
        print('0 ungedeckte Lemma-Signaturen.')
        return
    for vers, start, ende, s, n, quote in befunde:
        print(f'{a.kapitel},{vers} pos {start}–{ende}  '
              f'`{" ".join(s)}`  {n} Belege, {quote:.0%} gedeckt')
        print(f'    {src[vers]}')
        print()
    print(f'{len(befunde)} Verdachtsfälle. Jeder ist am Vers zu prüfen: steht die '
          'Wortfolge hier als Wendung oder wörtlich?')


if __name__ == '__main__':
    main()
