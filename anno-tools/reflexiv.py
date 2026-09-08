#!/usr/bin/env python3
"""Wo traegt das Verbtoken sein reflexives Lemma — und wo fehlt es?

Die Regel steht in BINDUNGEN_FRA_NT.md unter „Wo das reflexive Lemma
sitzt": gibt es ein Mehrwort, traegt IT die reflexive Bedeutung und das
Verbtoken behaelt das schlichte Lemma; gibt es keines, traegt sie das
Verbtoken selbst.

Dieses Skript meldet die Verstoesse gegen die zweite Haelfte: ein Token
mit `se`/`s’` davor, KEIN Mehrwort darueber, und trotzdem das schlichte
Lemma. Der Koordinator hat die Probe von Hand einmal falsch gefahren —
ohne den Mehrwortfilter meldet sie genau die Stellen, die die Regel
ausdruecklich richtig nennt (Mt 17,14 · Marc 10,17). Deshalb steht sie
jetzt als Werkzeug da.

    python3 reflexiv.py <buchNr> [<buchNr> ...]
    python3 reflexiv.py <buchNr> --datei <abgabe.json> [--kapitel <KAP>]

Mit `--datei` wird die noch nicht eingesammelte Abgabe mitgeprueft: die
Bestandsbuecher liefern die Liste der vorhandenen `se <lemma>`, die
Abgabe wird dagegen gehalten. Der Agent fuer Actes 16 musste die Probe
sonst von Hand nachbauen, weil `reflexiv.py` nur den gebauten Bestand
las.
"""
import sys, json, collections
import common

REFL = {'se', 's’', "s'"}


def kapitel_pruefen(vv, nr, vorhanden, stellen, nur_sammeln=False):
    for kap, vvv in vv.items():
        for v, eintr in vvv.items():
            ein = sorted([e for e in eintr if 'pos_end' not in e
                          and 'parts' not in e], key=lambda e: e['pos'])
            bp = {e['pos']: e for e in ein}
            mwpos = set()
            for m in eintr:
                if 'pos_end' in m:
                    mwpos |= set(range(m['pos'], m['pos_end'] + 1))
                elif 'parts' in m:
                    mwpos |= set(m['parts'])
            for e in ein:
                lem = e.get('lemma') or ''
                if lem.startswith(('se ', 's\u2019')):
                    vorhanden.add(lem)
                    continue
                if nur_sammeln:
                    continue
                vor = bp.get(e['pos'] - 1)
                if not vor or vor['form'].lower() not in REFL:
                    continue
                if e['pos'] in mwpos:
                    continue
                stellen.append((nr, kap, v, e['pos'], e['form'], lem))


def lauf_datei(nummern, pfad, kapitel=None):
    """Die Abgabe gegen den Bestand halten."""
    import json
    vorhanden, stellen = set(), []
    for nr in nummern:
        try:
            d = common.load_anno(nr)
        except Exception:
            continue
        if d:
            kapitel_pruefen(d['chapters'], nr, vorhanden, [], nur_sammeln=True)
    with open(pfad, encoding='utf-8') as f:
        roh = json.load(f)
    ch = roh.get('chapters', roh)
    # Die Abgabedatei ist FLACH nach Versnummer: {"1": [...], "2": [...]}.
    # Ein `--kapitel 16` traf hier zuerst den VERS 16 und die Huelle blieb
    # aus. Die Form entscheidet, nicht die Nummer: sind die Werte Listen,
    # ist es ein einzelnes Kapitel.
    if ch and isinstance(next(iter(ch.values())), list):
        ch = {str(kapitel or '?'): ch}
    kapitel_pruefen(ch, nummern[0] if nummern else 0, vorhanden, stellen)
    return vorhanden, stellen


def lauf(nummern):
    vorhanden = set()
    stellen = []
    for nr in nummern:
        try:
            d = common.load_anno(nr)
        except Exception:
            continue
        if not d:
            continue
        for kap, vv in d['chapters'].items():
            for v, eintr in vv.items():
                ein = sorted([e for e in eintr if 'pos_end' not in e
                              and 'parts' not in e], key=lambda e: e['pos'])
                bp = {e['pos']: e for e in ein}
                mwpos = set()
                for m in eintr:
                    if 'pos_end' in m:
                        mwpos |= set(range(m['pos'], m['pos_end'] + 1))
                    elif 'parts' in m:
                        mwpos |= set(m['parts'])
                for e in ein:
                    lem = e.get('lemma') or ''
                    if lem.startswith(('se ', 's’')):
                        vorhanden.add(lem)
                        continue
                    vor = bp.get(e['pos'] - 1)
                    if not vor or vor['form'].lower() not in REFL:
                        continue
                    if e['pos'] in mwpos:
                        continue          # das Mehrwort traegt es — richtig
                    stellen.append((nr, kap, v, e['pos'], e['form'], lem))
    return vorhanden, stellen


def main():
    args = sys.argv[1:]
    datei = kapitel = None
    if '--datei' in args:
        i = args.index('--datei')
        datei = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
    if '--kapitel' in args:
        i = args.index('--kapitel')
        kapitel = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
    try:
        nummern = [int(x) for x in args]
    except ValueError:
        print(__doc__)
        return 2
    if not nummern:
        print(__doc__)
        return 2
    # Der Agent fuer Actes 8 rief `reflexiv.py 44 8` — die 8 wurde als
    # zweites Buch gelesen und das Skript starb mit einem Traceback.
    # Kapitelnummern nimmt es nicht; es prueft immer ganze Buecher.
    schlecht = [n for n in nummern if not 1 <= n <= 66]
    if schlecht:
        print(f'{schlecht} ist keine Buchnummer (1-66).')
        print('reflexiv.py nimmt BUCHnummern, keine Kapitel — es prueft '
              'immer ganze Buecher.')
        return 2
    def da(n):
        try:
            return bool(common.load_anno(n))
        except Exception:
            return False
    fehlt = [n for n in nummern if not da(n)]
    if fehlt:
        print(f'nicht gebaut oder leer: {fehlt}')
        if len(nummern) > len(fehlt):
            print('Sieht nach einer KAPITELnummer aus — reflexiv.py nimmt '
                  'nur Buchnummern und prueft immer ganze Buecher.')
        else:
            print('Erst `buildbook.py <nr>` laufen lassen.')
        return 2
    if datei:
        vorhanden, stellen = lauf_datei(nummern, datei, kapitel)
    else:
        vorhanden, stellen = lauf(nummern)
    nach_lemma = collections.defaultdict(list)
    for s in stellen:
        nach_lemma[s[5]].append(s)

    belegt = {l: v for l, v in nach_lemma.items() if f'se {l}' in vorhanden}
    unbelegt = {l: v for l, v in nach_lemma.items() if f'se {l}' not in vorhanden}

    print(common.bestandsstand())
    print()
    print(f'## Reflexives Lemma fehlt, obwohl der Bestand es fuehrt  '
          f'({sum(len(v) for v in belegt.values())})')
    print('   Hier ist die Spaltung sicher ein Fehler: dasselbe Verb steht')
    print('   anderswo unter `se <lemma>`.')
    for lem in sorted(belegt, key=lambda l: -len(belegt[l])):
        orte = ' · '.join(f'{a} {b},{c}' for a, b, c, _, _, _ in belegt[lem][:6])
        print(f'   {len(belegt[lem]):3}  {lem:16} → se {lem:14} {orte}')

    print()
    print(f'## `se <lemma>` gibt es im Bestand noch nicht  '
          f'({sum(len(v) for v in unbelegt.values())})')
    print('   Am Vers pruefen: echtes Pronominalverb, oder ist `se` das')
    print('   Objekt („ils se disaient" = sagten ZUEINANDER)? Nur im ersten')
    print('   Fall gehoert das Lemma gezogen.')
    for lem in sorted(unbelegt, key=lambda l: -len(unbelegt[l])):
        orte = ' · '.join(f'{a} {b},{c}' for a, b, c, _, _, _ in unbelegt[lem][:4])
        print(f'   {len(unbelegt[lem]):3}  {lem:16} {orte}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
