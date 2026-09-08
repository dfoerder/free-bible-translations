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


# Der italienische Artikel richtet sich vor dem Nomen nach dem ANLAUT,
# nicht nach dem Genus: vor Vokal, s+Konsonant, z, gn, ps, pn und x
# stehen `gli`, `lo` und `uno` statt `i`, `il` und `un`. Das ist eine
# Regel, keine Statistik — sie traegt vom ersten Buch an, waehrend die
# Genusprobe oben erst ab 200 belegten Nomenformen etwas sagt.
#
# Ueber Judas, Matthaeus und Markus 1-11 gemessen: sieben Stellen mit
# `i` vor `gli`-Anlaut (`i afflitti`, `i operai`, `i scribi` dreimal,
# `i esattori` zweimal), und der italienische Zeuge liest an denselben
# Stellen selbst `gli scribi`. Anlass war ein Hinweis des Agenten fuer
# Marc 11, der `i` vor `anziani` in Mt 26,57 vermutet hatte — dort stand
# es richtig, beim `scribi` daneben aber nicht.
# Erste Fassung dieser Probe hat `un uomo` und `un angelo` angemahnt.
# Falsch: `uno` steht NUR vor s+Konsonant, z, gn, ps, pn und x — vor
# einem blossen Vokal ist `un` richtig. Und `il` wird vor Vokal nicht zu
# `lo`, sondern elidiert zu `l’`. Nur der Plural `i` wird in BEIDEN
# Faellen zu `gli`.
# `lo` und `gli` sind auch die klitischen Objektpronomen (`lo vide`,
# `gli disse`). Die Gegenrichtung der Anlautprobe unterscheidet sie am
# DEUTSCHEN Wort des Eintrags: ein Artikel glossiert zu `der`/`ein`,
# ein Klitikon zu `ihn`/`ihm`. Ohne diese Probe meldete die
# Gegenrichtung im ersten Lauf ueber tausend Pronomen.
DE_ARTIKEL = {'der', 'die', 'das', 'den', 'dem', 'des',
              'ein', 'eine', 'einen', 'einem', 'einer', 'eines',
              'am', 'im', 'zum', 'zur', 'vom', 'beim', 'ins', 'ans'}

IT_KONS = re.compile(r"^(?:s[^aeiouh]|z|gn|ps|pn|x|y)", re.I)
IT_VOKAL = re.compile(r"^[aeiou]", re.I)


# `dio` bildet den Plural unregelmaessig und nimmt trotz schlichtem
# Anlaut `gli`: `gli dèi`, `degli dèi`. Die Anlautprobe meldete deshalb
# `Gli dèi` (Actes 14,11) als Fehler und wollte `I dèi` — gemeldet vom
# Agenten fuer Actes 14, bestaetigt durch riv1927 („Gli dèi") und durch
# den Bestand selbst (Actes 7,40 `degli dèi`). Andere Woerter dieser Art
# gehoeren hier dazu, sobald sie auftauchen.
IT_GLI_UNREGELMAESSIG = re.compile(r'(?i)^(d[eè]i)\b')


def anlautprobe(ein, kap, vers, treffer):
    """Italienische Artikel gegen den Anlaut des folgenden Nomens.

    Eine Regel, keine Statistik — sie traegt vom ersten Buch an, waehrend
    die Genusprobe oben erst ab 200 belegten Nomenformen etwas sagt.

    Ueber Judas, Matthaeus und Markus 1-11 gemessen: sieben Stellen mit
    `i` vor `gli`-Anlaut (`i afflitti`, `i operai`, `i scribi` dreimal,
    `i esattori` zweimal), und der italienische Zeuge liest an denselben
    Stellen selbst `gli scribi`. Anlass war ein Hinweis des Agenten fuer
    Marc 11, der `i` vor `anziani` in Mt 26,57 vermutet hatte — dort
    stand es richtig, beim `scribi` daneben aber nicht.
    """
    for pos, e in ein.items():
        art = (e.get('it') or '').strip()
        kl = art.lower()
        if kl not in ('i', 'il', 'un', 'gli', 'lo', 'uno'):
            continue
        nx = ein.get(pos + 1)
        w = (nx.get('it') or '').strip() if nx else ''
        if not w:
            continue
        if kl in ('i', 'il', 'un'):
            if IT_KONS.match(w):
                soll = {'i': 'gli', 'il': 'lo', 'un': 'uno'}[kl]
            elif IT_VOKAL.match(w) and kl in ('i', 'il'):
                soll = 'gli' if kl == 'i' else 'l’'
            else:
                continue
        else:
            # Die Gegenrichtung. Die erste Fassung sah nur `i` vor
            # `gli`-Anlaut; ein `uno` vor schlichtem Konsonanten kam
            # durch. Der Agent fuer Luc 24 hat `uno fantasma` zweimal
            # von Hand gefunden, nachdem dieser Lauf 0 gemeldet hatte.
            #
            # `lo` und `gli` sind im Italienischen auch die klitischen
            # Objektpronomen — `lo vide`, `gli disse`. Ohne die
            # Nomenprobe meldete diese Richtung im ersten Lauf mehr als
            # tausend solcher Stellen und war damit unbrauchbar.
            # Zwei Proben, beide noetig. Ohne die erste meldete diese
            # Richtung ueber tausend klitische Pronomen (`lo vide`,
            # `gli disse`); ohne die zweite fuenfzig Mal das Zahlwort
            # `uno` in `uno di voi` — dort ist es kein Artikel, sondern
            # „einer von euch", und `uno` ist richtig.
            if erstes_wort(C.de_wort(e)) not in DE_ARTIKEL:
                continue
            if C.de_wort(nx)[:1].islower():
                continue
            if kl == 'uno' and not IT_KONS.match(w):
                soll = 'un'
            elif kl == 'gli' and not (IT_KONS.match(w)
                                      or IT_VOKAL.match(w)
                                      or IT_GLI_UNREGELMAESSIG.match(w)):
                soll = 'i'
            elif kl == 'lo' and not IT_KONS.match(w):
                soll = "l’" if IT_VOKAL.match(w) else 'il'
            else:
                continue
        if art[:1].isupper():
            soll = soll[0].upper() + soll[1:]
        treffer.append((int(kap), int(vers), e.get('form'), art,
                        nx.get('form'), w, soll))


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    buch, kaps = sys.argv[1], sys.argv[2:]
    out = os.environ.get('ANNO_OUT')
    if not out:
        raise SystemExit('ANNO_OUT ist nicht gesetzt.')
    zaehl = sammle()
    # Das Genus kommt aus der Artikelverteilung des BESTANDS. Ist der
    # klein, erreicht keine Nomenform die Meldeschwelle, und '0
    # Verdachtsfaelle' heisst dann nicht 'sauber', sondern 'nichts
    # gemessen'. Beim ersten Buch einer Ausgabe ist genau das der Fall.
    # Gemeldet vom Agenten fuer Matthaeus 1.
    tragfaehig = sum(1 for c in zaehl.values() if sum(c.values()) >= 5)
    treffer = []
    anlaut = []
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
            anlautprobe(ein, k, v, anlaut)
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
    if anlaut:
        print()
        print('  Italienischer Anlaut — der Artikel richtet sich nach dem\n  ANLAUT des Nomens, nicht nach seinem Genus:')
        for k, v, f1, a, f2, w, soll in sorted(set(anlaut)):
            print('  %s,%s,%-3s %-8s it %-6s | %-12s it %-14s  → %s'
                  % (buch, k, v, f1, a, f2, w, soll))
    print()
    if tragfaehig < 200:
        print(f'!! Der Bestand traegt erst {tragfaehig} Nomenformen mit '
              'mindestens 5 Belegen. Bei so wenig Referenz erreicht kaum '
              'etwas die Meldeschwelle — eine Null hier heisst NICHT '
              '"sauber", sondern "noch nichts gemessen".')
    print('%d Verdachtsfaelle%s. Das Genus ist aus der Artikelverteilung des'
          % (len(set(treffer)),
             f' und {len(set(anlaut))} Anlautfehler' if anlaut else ''))
    print('Bestands abgeleitet, nicht aus einem Woerterbuch — jeden Treffer')
    print('am Vers ansehen. Gemeldet wird nur ab 5 Belegen und 80 Prozent.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
