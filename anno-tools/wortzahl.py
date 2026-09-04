#!/usr/bin/env python3
"""Wortvorkommen eines Kapitels zaehlen — mit Stammpraefix, nicht exakt.

    wortzahl.py <buchNr> <kapitel> <wort> [<wort> ...]

Zweimal hat eine exakte Suche in einer Paketvorbereitung falsch gezaehlt:
`Elle` fand die 33 `Ellen` nicht (Paket 15, gemeldet vom Kapitel-40-Agenten),
`Vorhof` die `Vorhoefe` nicht (Paket 16, gemeldet vom Kapitel-42-Agenten).
Beide Male stand die Zahl dann falsch im Prompt. Deshalb: Praefixsuche mit
Wortgrenze am Anfang, offen am Ende, plus Umlautvarianten.
"""
import json, re, sys, os

def varianten(w):
    """Umlautvarianten — JEDE Position einzeln, nicht alle zugleich.

    Die erste Fassung ersetzte alle Vorkommen und machte aus `Vorhof`
    den Unsinn `Voerhoef`; die Pluralform `Vorhoefe` in 42,6 blieb
    deshalb ungezaehlt — genau der Fehler, den das Werkzeug verhindern
    soll, nur eine Ebene tiefer.
    """
    v = {w}
    for a, b in (('au', 'äu'), ('a', 'ä'), ('o', 'ö'), ('u', 'ü')):
        for i in range(len(w) - len(a) + 1):
            if w[i:i + len(a)].lower() == a:
                v.add(w[:i] + (b.upper() if w[i].isupper() else b)
                      + w[i + len(a):])
    return v

def main():
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    nr, kap = sys.argv[1], sys.argv[2]
    woerter = sys.argv[3:]
    import glob
    tref = glob.glob('deu/l1912mod/%s_l1912mod.json' % nr)
    if not tref:
        raise SystemExit('Quelltext fuer Buch %s nicht gefunden.' % nr)
    d = json.load(open(tref[0]))
    ch = d.get('chapters', d)[kap]
    text = ' '.join(ch[v] for v in sorted(ch, key=int))
    print('%s,%s — %d Verse, %d Woerter'
          % (nr, kap, len(ch), len(re.findall(r"[\w'aeoeueaeoeuess-]+", text))))
    for w in woerter:
        treffer = []
        for var in varianten(w):
            treffer += re.findall(r'\b' + re.escape(var) + r'\w*', text)
        if treffer:
            from collections import Counter
            c = Counter(treffer)
            print('   %-16s %3d   %s' % (w, len(treffer),
                  ' · '.join('%s:%d' % (f, n) for f, n in c.most_common(6))))
        else:
            print('   %-16s   0   — kommt nicht vor' % w)
    return 0

if __name__ == '__main__':
    sys.exit(main())
