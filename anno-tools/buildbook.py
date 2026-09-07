"""Baut die Anno-Datei eines Buches aus den Kapitelquellen.

    buildbook.py <buchNr> [--trocken]

Quellen: bibles-translations/anno-quellen/$ANNO_EDITION/<nr>/ch<N>.json
Ziel:    bible-reader/bibles/$ANNO_EDITION/anno/<nr><ANNO_SUFFIX>.json

Beide Pfade folgen `ANNO_EDITION` (Default `deu/l1912mod`); bis zum
franzoesischen NT standen sie hier fest ausgeschrieben.

Ein Kapitel wird nur aufgenommen, wenn es vollständig ist und der Validator
es durchwinkt; unvollständige Stände (laufender Agent) werden mit Hinweis
übersprungen. Danach: Satzzeichen-Einträge verwerfen, Level vereinheitlichen,
buchübergreifend angleichen, kompakt schreiben.

Der Level-Abgleich gehört in den Build und nicht dahinter — die Datei entsteht
bei jedem Build neu, eine nachträgliche Korrektur wäre sofort wieder weg.
"""
import collections
import glob
import json
import os
import re
import sys

import common as C
import validate as V


def _mehrheit(counter):
    """Häufigstes Level; bei Gleichstand das niedrigere."""
    if not counter:
        return None
    top = max(counter.values())
    kandidaten = [lv for lv, n in counter.items() if n == top]
    return min(kandidaten, key=C.LEVELS.index)


def level_abgleich(chapters, nr, verbose=True):
    """Vereinheitlicht die CEFR-Level. Das Level hängt laut Spezifikation am
    **Lemma**; verschiedene Agenten stufen dasselbe Wort aber unabhängig ein.

    Zwei Durchgänge:
      1. gleiche Bedeutung (Lemma + vier Glossen) → gleiches Level, im Buch
      2. gleiches Lemma → häufigstes Level im **gesamten** Bestand,
         bei Gleichstand das niedrigere

    Durchgang 2 ist endgültig und partitioniert alle Einträge, deshalb ist das
    Ergebnis ein Fixpunkt: ein zweiter Lauf ändert nichts mehr. Eine frühere
    Fassung hatte zusätzlich einen Wortform-Durchgang **nach** dem Lemma-Abgleich;
    der schaukelte sich mit ihm auf (Lauf 1 und Lauf 2 lieferten verschiedene
    Stände). Wortformen, deren Lemmata verschieden eingestuft sind, werden
    stattdessen nur **gemeldet** — das sind Homographen oder uneinheitliche
    Lemmatisierung, und beides gehört angesehen, nicht automatisch geglättet.
    """
    alle = [e for vs in chapters.values() for es in vs.values() for e in es]

    # 1. gleiche Bedeutung im Buch
    counter = collections.defaultdict(collections.Counter)
    for e in alle:
        counter[(e['lemma'],) + C.reihe(e)][e['level']] += 1
    ziel = {k: _mehrheit(c) for k, c in counter.items() if len(c) > 1}
    n = 0
    for e in alle:
        k = (e['lemma'],) + C.reihe(e)
        if k in ziel and e['level'] != ziel[k]:
            e['level'] = ziel[k]
            n += 1
    if verbose and n:
        print(f'  Level gleiche Bedeutung: {n} Einträge angeglichen')

    # 2. gleiches Lemma, buchübergreifend — **aus den Kapitelquellen**, nicht
    # aus den gebauten Dateien. Das war ein Konstruktionsfehler: die Mehrheit
    # kam aus dem Ergebnis des letzten Builds, und damit war eine korpusweite
    # Levelkorrektur über die Quellen prinzipiell unmöglich. Wer `vierzehnt`
    # in allen 22 Quellen von B1 auf A2 zog, bekam beim Bauen von Buch 6 die
    # 42 noch nicht gebauten Bücher als B1-Mehrheit entgegen und die Änderung
    # zurück — und zwar bei jedem Buch, in jeder Reihenfolge, beliebig oft
    # wiederholt. Ein stabiler Attraktor am falschen Ort.
    #
    # Die Quelle ist der bearbeitete Stand und damit die Autorität; die
    # gebaute Datei ist ihr Ergebnis. Wo eine Quelle fehlt, springt die
    # gebaute Datei ein.
    bestand = collections.defaultdict(collections.Counter)
    for other in C.anno_books():
        if other == int(nr):
            continue
        kapitel = C.quellen_kapitel(other)
        if kapitel:
            for kap in kapitel:
                for es in (C.load_quelle(other, kap) or {}).values():
                    for e in es:
                        if e.get('lemma') and e.get('level'):
                            bestand[e['lemma']][e['level']] += 1
        else:
            for _, _, _, e in C.iter_corpus([other]):
                bestand[e['lemma']][e['level']] += 1
    for e in alle:
        bestand[e['lemma']][e['level']] += 1

    n = 0
    for e in alle:
        z = _mehrheit(bestand[e['lemma']])
        if z and e['level'] != z:
            e['level'] = z
            n += 1
    if verbose and n:
        print(f'  Level gleiches Lemma (buchübergreifend): {n} Einträge angeglichen')

    # Bericht: gleiche Wortform, verschiedene Level (verschiedene Lemmata)
    formen = collections.defaultdict(set)
    for e in alle:
        formen[e['form']].add((e['lemma'], e['level']))
    gemischt = {f: s for f, s in formen.items() if len({lv for _, lv in s}) > 1}
    if verbose and gemischt:
        print(f'  Hinweis: {len(gemischt)} Wortformen mit verschiedenen Leveln '
              f'(verschiedene Lemmata) — ansehen:')
        for f, s in sorted(gemischt.items())[:10]:
            print('    ', f, sorted(s))


def scratch_abgleich(nr):
    """Warnt, wenn $ANNO_OUT neuere Kapitel haelt als die Quellen.

    Der Koordinator arbeitet in `$ANNO_OUT/<nr>/chN.json` und kopiert von dort
    nach `anno-quellen/`. Wer nach dem Kopieren noch etwas korrigiert — und das
    passiert bei jedem Kreuzvergleich —, hat den Stand in zwei Dateien und baut
    aus der aelteren. In Daniel sind drei Korrekturen so verlorengegangen und
    erst dem Abschlusslauf von `konsistenz.py` aufgefallen (`Tier` in 4,13
    stand noch als *beast*, waehrend das ganze Buch *animal* fuehrt).
    """
    out = os.environ.get('ANNO_OUT')
    if not out:
        return
    verz = os.path.join(out, str(nr))
    if not os.path.isdir(verz):
        return
    abweichend = []
    for datei in sorted(glob.glob(os.path.join(verz, 'ch*.json'))):
        name = os.path.basename(datei)
        if not re.fullmatch(r'ch\d+\.json', name):
            continue                      # Teildateien (ch11.part2.json) ueberspringen
        kap = name[2:-5]
        try:
            a = json.load(open(datei, encoding='utf-8'))
            b = C.load_quelle(nr, kap)
        except Exception:
            continue
        if b is not None and a != b:
            abweichend.append(kap)
    if abweichend:
        print(f'  !! ACHTUNG: $ANNO_OUT weicht in Kapitel '
              f'{", ".join(abweichend)} von den Quellen ab.')
        print(f'     Gebaut wird aus anno-quellen. Erst kopieren, dann bauen.')


def build(nr, trocken=False):
    nr = int(nr)
    scratch_abgleich(nr)
    src = C.load_source(nr)
    kapitel = C.quellen_kapitel(nr)
    if not kapitel:
        print(f'Keine Kapitelquellen unter {C.quellen_dir(nr)}')
        return None

    chapters = {}
    uebersprungen = []
    for kap in kapitel:
        data = C.load_quelle(nr, kap)
        errs = V.validate_chapter(nr, kap, data)
        if errs:
            uebersprungen.append((kap, errs))
            continue
        # Satzzeichen-Einträge verwerfen (falls ein Agent doch welche liefert)
        rein = {}
        for v, entries in data.items():
            toks = C.tokens(src['chapters'][str(kap)][v])
            behalten = [e for e in entries
                        if C.is_multi(e) or not C.is_punct_only(toks[e['pos']])]
            # Kanonische Reihenfolge: nach Position, an gleicher Position der
            # Mehrwort-Eintrag zuerst — `getAnnotation` nimmt mit `find` den
            # ersten passenden und muss die Einheit vor dem Einzelwort sehen.
            rein[v] = sorted(behalten, key=lambda e: (e['pos'], 0 if C.is_multi(e) else 1))
        chapters[str(kap)] = {v: rein[v] for v in sorted(rein, key=int)}

    for kap, errs in uebersprungen:
        print(f'  Kapitel {kap} übersprungen ({len(errs)} Befunde): {errs[0]}')

    if not chapters:
        print('Nichts zu bauen.')
        return None

    level_abgleich(chapters, nr)

    fehlend = [k for k in src['chapters'] if k not in chapters]
    out = {'name': src['name'],
           'chapters': {k: chapters[k] for k in sorted(chapters, key=int)}}

    verse = sum(len(v) for v in chapters.values())
    eintraege = sum(len(e) for v in chapters.values() for e in v.values())
    print(f'{nr} {src["name"]}: {len(chapters)} Kapitel, {verse} Verse, {eintraege} Einträge')
    if fehlend:
        print(f'  noch offen: {len(fehlend)} Kapitel {sorted(fehlend, key=int)}')

    if trocken:
        print('  (trocken — nichts geschrieben)')
        return out

    C.write_compact(C.anno_path(nr), out)
    C._anno_cache.pop(nr, None)
    print(f'  geschrieben: {C.anno_path(nr)}')
    if not fehlend:
        tok, einzel, mehr, zeichen = V.gegenrechnung(nr)
        ok = 'stimmt' if tok - einzel == zeichen else 'STIMMT NICHT'
        print(f'  Gegenrechnung: {tok} − {einzel} = {tok-einzel}, '
              f'Satzzeichen {zeichen} — {ok}')
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    trocken = '--trocken' in sys.argv
    for a in sys.argv[1:]:
        if a.startswith('--'):
            continue
        build(int(a), trocken)
