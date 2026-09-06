#!/usr/bin/env python3
"""Romanische Artikel gegen das Genus des folgenden Nomens — datengetrieben.

    artikel.py <buchNr> [<kapitel> ...]

Der ertragreichste Fehlertyp, den bis Paket 17 kein Lauf abdeckte:
`le limite` statt `la limite` (14 Stellen in Kapitel 48), `la límite`
statt `el límite` (11,10 · 11,11), `le cour` statt `la cour` (fuenf
Stellen), `dei operai` statt `degli operai`. Gefunden wurden sie nur
durch Handpruefung aller Attributketten — der Kapitel-48-Agent hat
92 Paare einzeln durchgesehen, der Kapitel-43-Agent 152.

Das Genus steht nirgends im Bestand. Es laesst sich aber ERMITTELN:
wo dieselbe fremdsprachliche Nomenform im ganzen Bestand ueberwiegend
mit `la` steht, ist sie feminin. Der Lauf sammelt also erst die
Artikelverteilung je Nomenform und meldet dann die Ausreisser.

Gemeldet wird nur, was klar ist: mindestens fuenf Belege und
mindestens 80 Prozent Mehrheit. Alles darunter schweigt.
"""
import collections, glob, json, os, re, sys
import common as C

# Die zweiwortigen Formen (`a la`, `de la`, `à la`) standen anfangs nicht
# in der Tabelle. Der Agent fuer Nahum 2 fand deshalb einen Fehler, den
# das Skript nicht gemeldet hatte: `zur Stadtmauer` trug es `alla` (das
# Skript sah es) UND es `a la` (das Skript sah es nicht), beide vor dem
# maskulinen `muro`. Wer nur eine Spalte prueft, findet nur die halbe
# Kongruenz.
ART = {
    'es': {'el': 'm', 'la': 'f', 'los': 'mp', 'las': 'fp',
           'del': 'm', 'al': 'm',
           'a la': 'f', 'de la': 'f', 'a los': 'mp', 'a las': 'fp',
           'de los': 'mp', 'de las': 'fp'},
    'fr': {'le': 'm', 'la': 'f', 'les': 'p', 'du': 'm', 'au': 'm',
           'à la': 'f', 'de la': 'f', 'aux': 'p', 'des': 'p'},
    'it': {'il': 'm', 'la': 'f', 'lo': 'm', 'i': 'mp', 'gli': 'mp',
           'le': 'fp', 'del': 'm', 'della': 'f', 'dei': 'mp',
           'degli': 'mp', 'delle': 'fp', 'al': 'm', 'alla': 'f',
           'ai': 'mp', 'alle': 'fp', 'agli': 'mp',
           'nel': 'm', 'nella': 'f', 'nei': 'mp', 'nelle': 'fp',
           'sul': 'm', 'sulla': 'f'},
}
# Nur diese deutschen Formen werden geprueft. Ohne den Filter las der Lauf
# jede Glosse, die mit einem Artikelwort beginnt, als Artikel — `entlang`
# = *le long de* etwa, und meldete dann das Genus des falschen Nomens.
# Die deutsche Seite ist die verlaessliche: was hier steht, IST ein Artikel.
DE_ARTIKEL = {
    'der', 'die', 'das', 'den', 'dem', 'des',
    'am', 'im', 'zum', 'zur', 'vom', 'beim', 'ins', 'ans',
    'ein', 'eine', 'einen', 'einem', 'einer', 'eines',
}

ANNO = C.ANNO_DIR


def erstes_wort(s):
    s = (s or '').strip().lower()
    m = re.match(r"[a-zàâäçéèêëîïôöùûüñ']+", s)
    return m.group(0) if m else ''


def nomen_danach(einzel, pos):
    """Das erste grossgeschriebene deutsche Folgewort — das ist das Nomen.

    Ohne diesen Schritt meldete der Lauf jedes Adjektiv zwischen Artikel
    und Nomen (`den inneren Vorhof`: geprueft wurde `interior`, nicht
    `patio`). Dieselbe Heuristik traegt schon kongruenz.py seit Paket 11:
    deutsche Nomen sind gross, Adjektive klein.
    """
    for d in (1, 2, 3):
        kand = einzel.get(pos + d)
        if kand is None:
            return None
        if C.de_wort(kand)[:1].isupper():
            return kand
    return None


def sammle():
    """Artikelverteilung je (Sprache, Nomenform) aus dem ganzen Bestand."""
    zaehl = collections.defaultdict(collections.Counter)
    for pfad in sorted(glob.glob(os.path.join(ANNO, f'*{C.ANNO_SUFFIX}'))):
        d = json.load(open(pfad))
        ch = d.get('chapters', d)
        for k, vv in ch.items():
            if not isinstance(vv, dict):
                continue
            for v, ents in vv.items():
                ein = {e['pos']: e for e in ents
                       if isinstance(e, dict) and 'pos_end' not in e
                       and 'parts' not in e}
                for pos, e in ein.items():
                    nx = nomen_danach(ein, pos)
                    if not nx:
                        continue
                    if C.de_wort(e).lower() not in DE_ARTIKEL:
                        continue
                    for sp, tab in ART.items():
                        a = erstes_wort(e.get(sp))
                        if a in tab and len((e.get(sp) or '').split()) <= 2:
                            n = erstes_wort(nx.get(sp))
                            if len(n) > 2:
                                zaehl[(sp, n)][tab[a]] += 1
    return zaehl


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    buch, kaps = sys.argv[1], sys.argv[2:]
    out = os.environ.get('ANNO_OUT')
    if not out:
        raise SystemExit('ANNO_OUT ist nicht gesetzt.')
    zaehl = sammle()
    treffer = []
    for f in sorted(glob.glob(os.path.join(out, buch, 'ch*.json'))):
        if '.part' in f:
            continue
        k = re.search(r'ch(\d+)\.json$', f).group(1)
        if kaps and k not in kaps:
            continue
        d = json.load(open(f))
        for v, ents in d.items():
            ein = {e['pos']: e for e in ents
                   if 'pos_end' not in e and 'parts' not in e}
            for pos, e in ein.items():
                nx = nomen_danach(ein, pos)
                if not nx:
                    continue
                if (e.get('form') or '').lower() not in DE_ARTIKEL:
                    continue
                for sp, tab in ART.items():
                    a = erstes_wort(e.get(sp))
                    if a not in tab or len((e.get(sp) or '').split()) > 2:
                        continue
                    n = erstes_wort(nx.get(sp))
                    c = zaehl.get((sp, n))
                    if not c:
                        continue
                    ges = sum(c.values())
                    haupt, anz = c.most_common(1)[0]
                    if ges >= 5 and anz / ges >= 0.8 and tab[a] != haupt:
                        treffer.append((int(k), int(v), sp, e['form'],
                                        e[sp], nx['form'], nx[sp],
                                        haupt, anz, ges))
    for k, v, sp, f1, g1, f2, g2, soll, anz, ges in sorted(set(treffer)):
        print('  %s,%s,%-3s %s  %-10s %-8s | %-14s %-14s  Bestand: %s (%d/%d)'
              % (buch, k, v, sp, f1, g1, f2, g2, soll, anz, ges))
    print()
    print('%d Verdachtsfaelle. Das Genus ist aus der Artikelverteilung des'
          % len(set(treffer)))
    print('Bestands abgeleitet, nicht aus einem Woerterbuch — jeden Treffer')
    print('am Vers ansehen. Gemeldet wird nur ab 5 Belegen und 80 Prozent.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
