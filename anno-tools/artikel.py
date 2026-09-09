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


# Praepositionen und Konjunktionen, die eine Nominalphrase beenden —
# dieselbe Liste, die kongruenz.py fuehrt.
PHRASENENDE = {'en', 'à', 'au', 'aux', 'de', 'du', 'des', 'dans', 'pour',
               'par', 'sur', 'sous', 'avec', 'sans', 'que', 'qui', 'et',
               'ou', 'comme', 'chez', 'entre', 'vers', 'depuis', 'selon',
               'contre', 'jusqu’à', 'afin'}


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
        # Eine Praeposition beendet die Phrase. Das Fenster ist fuer
        # eingeschobene ADJEKTIVE da; laeuft es ueber eine Praeposition,
        # trifft es das Nomen der naechsten Phrase und vergleicht zwei
        # Woerter, die nichts miteinander zu tun haben. `le long du
        # chemin` pruefte so `le` gegen `chemin` und meldete sechsmal
        # ein falsches Genus, obwohl der Artikel des Nomens (`du` →
        # `della`) richtig dasteht; `Le lendemain une foule` sprang von
        # `Le` auf `foule`. Dieselbe Grenze fuehrt kongruenz.py.
        if (kand.get('form') or '').lower() in PHRASENENDE:
            return None
        # Ein zweiter Artikel beendet die Phrase ebenso sicher. Noetig,
        # wo die Grossschreibung nicht traegt: `Le lendemain une foule`
        # glossiert `lendemain` als „nächsten Tag" — klein, also
        # uebersprungen —, und der Lauf verglich `Le` mit `foule`,
        # obwohl `Al día siguiente` / `Il giorno seguente` richtig ist.
        if C.de_wort(kand).lower() in DE_ARTIKEL:
            return None
    return None


def artikelglosse(g, tab):
    """Ist die Glosse WIRKLICH nur ein Artikel?

    Zwei Woerter sind erlaubt, weil `de la`, `a los` und `di quelli`
    Artikel bleiben — aber nur, wenn auch das zweite Wort eines ist.
    Ohne diese Bedingung ging `ce` → `il fatto` / `el hecho` als
    Artikel `il`/`el` durch und wurde gegen das uebernaechste Nomen
    geprueft (Rm 1,8 und 2 Ko 7,9).
    """
    w = (g or '').split()
    if len(w) == 1:
        return True
    if len(w) == 2:
        return w[1].lower() in tab
    return False


def sammle():
    """Artikelverteilung je (Sprache, Nomenform) aus dem ganzen Bestand.

    Gibt neben den Zahlen die Belegstellen zurueck — der Block
    `gespalten()` zeigt beide Seiten, und ohne Orte kann sie niemand
    nachschlagen.
    """
    zaehl = collections.defaultdict(collections.Counter)
    orte = collections.defaultdict(lambda: collections.defaultdict(list))
    for pfad in sorted(glob.glob(os.path.join(ANNO, f'*{C.ANNO_SUFFIX}'))):
        nr = re.match(r'(\d+)', os.path.basename(pfad)).group(1)
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
                        if a in tab and artikelglosse(e.get(sp), tab):
                            n = erstes_wort(nx.get(sp))
                            if len(n) > 2:
                                zaehl[(sp, n)][tab[a]] += 1
                                orte[(sp, n)][tab[a]].append(
                                    f'{nr} {k},{v}')
    return zaehl, orte


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

# Die Vokalklasse muss die AKZENTE mitfuehren. Ohne sie las
# `s[^aeiouh]` das Wort `sì` als unreines s und verlangte `lo sì`
# statt `il sì` — gemeldet vom Agenten fuer 2. Korinther 1, wo `le oui`
# und `le non` als Nomen stehen („il sì e il no"). Dasselbe traefe
# jedes `sé`, `sù`, `già`.
VOK = 'aeiouàáâäãéèêëíìîïóòôöõúùûüh'
IT_KONS = re.compile(r"^s(?![" + VOK + r"])|^(?:z|gn|ps|pn|x|y)", re.I)
IT_VOKAL = re.compile(r"^[" + VOK[:-1] + r"]", re.I)


# `dio` bildet den Plural unregelmaessig und nimmt trotz schlichtem
# Anlaut `gli`: `gli dèi`, `degli dèi`. Die Anlautprobe meldete deshalb
# `Gli dèi` (Actes 14,11) als Fehler und wollte `I dèi` — gemeldet vom
# Agenten fuer Actes 14, bestaetigt durch riv1927 („Gli dèi") und durch
# den Bestand selbst (Actes 7,40 `degli dèi`). Andere Woerter dieser Art
# gehoeren hier dazu, sobald sie auftauchen.
IT_GLI_UNREGELMAESSIG = re.compile(r'(?i)^(d[eè]i)\b')


# Zahlwoerter und Adjektive, die zwischen Artikel und Nomen stehen
# koennen — die deutsche Glosse ist dort klein, der italienische Artikel
# richtet sich aber nach ihnen.
IT_GLI_ZAHLADJ = re.compile(
    r'(due|tre|quattro|cinque|sei|sette|otto|nove|dieci|dodici|venti|'
    r'ventiquattro|cento|mille|santi|santo|altri|altro|stessi|stesso|'
    r'primi|primo|ultimi|ultimo|grandi|grande|veri|vero)$', re.I)


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
            # Die Nomenprobe („deutsche Glosse gross") haelt die
            # klitischen Pronomen fern, schliesst aber auch ZAHLWOERTER
            # und Adjektive aus: `gli sette` (Apk 8,2 · 8,6) und
            # `gli santi` sind dieser Probe entgangen, weil *sieben* und
            # *heiligen* klein stehen. Der Artikel richtet sich aber nach
            # dem unmittelbar folgenden Wort, nicht nach dem Nomen
            # dahinter. Die Verbprobe haelt `gli disse`/`lo vide`
            # genauso sicher fern und laesst Zahlwoerter durch.
            # Gemeldet vom Agenten fuer Offenbarung 11, der die Regel
            # von Hand nachgemessen hat.
            lem_nx = (nx.get('lemma') or '')
            ist_verb = (len(lem_nx) > 3 and not lem_nx[:1].isupper()
                        and lem_nx.endswith(('er', 'ir', 're', 'oir')))
            if ist_verb:
                continue
            if C.de_wort(nx)[:1].islower() and not IT_GLI_ZAHLADJ.match(w):
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


# Zweite Achse: dasselbe Zielnomen mit BEIDEN Artikeln.
#
# Die Probe oben braucht eine Mehrheit — sie fragt „welcher Artikel ist
# hier der richtige?" und muss das aus dem Bestand erraten. Diese hier
# fragt etwas anderes, das keine Mehrheit braucht: `conocimiento` hat
# genau EIN Genus, also ist jede Spaltung ein Befund, auch bei 12:7.
# Genau daran ist die erste vorbeigelaufen (63 % — unter beiden
# Schwellen), waehrend sechs falsche `la conocimiento` dastanden;
# gefunden vom Agenten fuer 2. Korinther 10, gemessen beim Einsammeln
# des Pakets.
#
# Der Block URTEILT NICHT. Er zeigt beide Seiten mit Orten, denn welche
# die falsche ist, sagt keine Zahl — bei `consuelo` stand die Mehrheit
# (5:1) falsch. Und drei Arten von Spaltung sind RICHTIG:
#   * Nomen gemeinsamen Geschlechts — `el joven` / `la joven`,
#     `il giovane` / `la giovane`, `guida`, `guardia` (die Person
#     ist maskulin, die Truppe feminin);
#   * die spanische a-tonica-Regel — feminine Nomen mit betontem
#     a-Anlaut nehmen im Singular `el`: `el arpa`, `el agua`;
#   * Adjektive und Adverbien, die als Nomen durchgehen (`gran`,
#     `mas`, `piu`, `ultimo`) — die richten sich nach ihrem Bezugswort.
def gespalten(zaehl, orte, buchnomen):
    """Nomen des geprueften Buches, die im Bestand beide Artikel tragen."""
    raus = []
    for (sp, n), c in zaehl.items():
        if (sp, n) not in buchnomen:
            continue
        # Nur die SINGULAR-Genera. `len(c) < 2` reichte nicht: eine
        # Zaehlung {'mp': 3, 'f': 1} hat zwei Schluessel und ist doch
        # keine Spaltung — Plural und Singular schliessen einander
        # nicht aus.
        m, f = c.get('m', 0), c.get('f', 0)
        if not (m and f):
            continue
        klein = 'm' if m <= f else 'f'
        raus.append((sp, n, m, f, klein,
                     orte[(sp, n)][klein], orte[(sp, n)]['f' if klein == 'm'
                                                         else 'm']))
    return sorted(raus)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    buch, kaps = sys.argv[1], sys.argv[2:]
    out = os.environ.get('ANNO_OUT')
    if not out:
        raise SystemExit('ANNO_OUT ist nicht gesetzt.')
    zaehl, orte = sammle()
    # Das Genus kommt aus der Artikelverteilung des BESTANDS. Ist der
    # klein, erreicht keine Nomenform die Meldeschwelle, und '0
    # Verdachtsfaelle' heisst dann nicht 'sauber', sondern 'nichts
    # gemessen'. Beim ersten Buch einer Ausgabe ist genau das der Fall.
    # Gemeldet vom Agenten fuer Matthaeus 1.
    tragfaehig = sum(1 for c in zaehl.values() if sum(c.values()) >= 5)
    treffer = []
    anlaut = []
    buchnomen = set()
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
                # `C.de_wort`, nicht `form`: in der franzoesischen und
                # englischen Richtung steht das Deutsche in `de`, und
                # `form` traegt dort `la`/`le`/`du`. Gegen eine Liste
                # DEUTSCHER Artikel geprueft passte davon nur, was in
                # beiden Sprachen gleich aussieht (`des`) — in 2 Kor
                # 38 von 451 Artikeln, also 8 %. Die Genusprobe lief
                # damit fuer fra/lsg1910mod jahrelang fast leer, und
                # ihre Nullen hiessen nicht „sauber", sondern „nichts
                # angesehen": 110 falsche Artikel standen unbemerkt im
                # Bestand. `sammle()` machte es an derselben Stelle
                # schon richtig — derselbe Fall, den der Docstring von
                # `common.de_wort` beschreibt, eine Zeile weiter unten
                # uebersehen.
                if C.de_wort(e).lower() not in DE_ARTIKEL:
                    continue
                for sp, tab in ART.items():
                    a = erstes_wort(e.get(sp))
                    if a not in tab or not artikelglosse(e.get(sp), tab):
                        continue
                    n = erstes_wort(nx.get(sp))
                    buchnomen.add((sp, n))
                    c = zaehl.get((sp, n))
                    if not c:
                        continue
                    ges = sum(c.values())
                    haupt, anz = c.most_common(1)[0]
                    # Zwei Schwellen. Die prozentuale (>=5 Belege, >=80 %)
                    # ist die alte. Die absolute kam dazu, weil `alimento`
                    # sie um EINEN Prozentpunkt verfehlt hat: 11 richtige
                    # `el` gegen 3 falsche `la` sind 79 %, und die drei
                    # Fehler standen jahrelang da (Actes 9,19 · 27,33 ·
                    # 27,34, gefunden vom Agenten fuer 1. Korinther 3).
                    #
                    # Eine grosse Stichprobe mit einer HANDVOLL Ausreisser
                    # ist der typische Fehlerfall; eine kleine Stichprobe
                    # mit vielen ist echte Uneinigkeit. Die zweite Schwelle
                    # trennt genau danach. Ueber den ganzen Bestand gemessen
                    # bringt sie null zusaetzliche Meldungen — sie faengt
                    # den naechsten Fall, nicht heutiges Rauschen.
                    stark = ges >= 5 and anz / ges >= 0.8
                    knapp = ges >= 10 and ges - anz <= 3
                    # Nur bei GLEICHEM Numerus. `du temps` heisst
                    # italienisch `ai tempi` — Plural, voellig richtig,
                    # und ueber das Genus sagt der Vergleich mit einem
                    # Bestand im Singular nichts. Ohne diese Zeile war
                    # rund die Haelfte der Meldungen aus der ersten
                    # fra-Messung genau das (`ai tempi` 5x, `los
                    # espiritus` 6x, `el discipulo` gegen `los
                    # discipulos`).
                    if (tab[a][-1:] == 'p') != (haupt[-1:] == 'p'):
                        continue
                    if (stark or knapp) and tab[a] != haupt:
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
    gesp = gespalten(zaehl, orte, buchnomen)
    if gesp:
        print()
        print('  Gespaltenes Genus — dasselbe Zielnomen traegt im Bestand\n'
              '  BEIDE Artikel. Kein Urteil, eine Frage: welche Seite ist\n'
              '  falsch? (Richtig gespalten sind Nomen gemeinsamen\n'
              '  Geschlechts, `el arpa` und Adjektive.)')
        for sp, n, m, f, klein, wenig, viel in gesp:
            print('  %-3s %-16s m=%-3d f=%-3d   %s: %s%s'
                  % (sp, n, m, f, klein, ', '.join(wenig[:5]),
                     ' …' if len(wenig) > 5 else ''))
            print('  %-3s %-16s              %s: %s%s'
                  % ('', '', 'f' if klein == 'm' else 'm',
                     ', '.join(viel[:5]), ' …' if len(viel) > 5 else ''))
    print()
    if tragfaehig < 200:
        print(f'!! Der Bestand traegt erst {tragfaehig} Nomenformen mit '
              'mindestens 5 Belegen. Bei so wenig Referenz erreicht kaum '
              'etwas die Meldeschwelle — eine Null hier heisst NICHT '
              '"sauber", sondern "noch nichts gemessen".')
    print('%d Verdachtsfaelle%s%s. Das Genus ist aus der Artikelverteilung des'
          % (len(set(treffer)),
             f' und {len(set(anlaut))} Anlautfehler' if anlaut else '',
             f' und {len(gesp)} gespaltene Nomen' if gesp else ''))
    print('Bestands abgeleitet, nicht aus einem Woerterbuch — jeden Treffer')
    print('am Vers ansehen. Gemeldet wird nur ab 5 Belegen und 80 Prozent.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
