"""Die vier Referenzausgaben neben dem deutschen Vers — inhaltlich ausgerichtet.

    ausgaben.py <buchNr> <kapitel> [<vonVers> [<bisVers>]]

## Wozu

Bis Hiob hat jeder Agent die vier Ausgaben von Hand aufgeschlagen und dabei
stillschweigend angenommen, dass Vers 12 in allen fuenf Ausgaben derselbe Vers
ist. In Hiob 38-41 stimmte das nicht, und der Fehler war unsichtbar: die
verschobene Zeile stammt aus derselben Tierreihe und liest sich plausibel.
`VERSZAEHLUNG_38_41.md` haelt die Messung fest.

Im Psalter ist das kein Sonderfall mehr, sondern der Normalfall. Die deutsche
Zaehlung fuehrt die Ueberschrift (`Ein Psalm Davids`) als Vers 1, WEB und
RV1909 zaehlen sie nicht mit, RIV1927 weicht noch einmal anders ab, und
LSG1910 folgt fast durchweg dem Deutschen. Von 150 Psalmen haben **104** eine
abweichende Verszahl in mindestens einer Ausgabe, verteilt auf fuenf
verschiedene Muster.

Dieses Werkzeug nimmt die Ausrichtung ab.

## Wie ausgerichtet wird

Ueber den **letzten Vers**, nicht ueber eine Aehnlichkeit. Wo eine Ausgabe die
Ueberschrift nicht mitzaehlt, fehlt sie vorn und der Schluss deckt sich: Ps 19
hat deutsch 15 Verse und englisch 14, und deutsch 15 ist englisch 14, Wort fuer
Wort dasselbe.

Eine erste Fassung hat den Versatz aus der Folge der Verslaengen geschaetzt.
Das war die falsche Groesse und lag in Ps 9, 15 und 19 daneben — jedes Mal
lautlos, denn die verschobene Zeile liest sich plausibel. Genau der Fehler,
gegen den dieses Werkzeug gebaut ist. Die Verslaengen sind seither nur noch
**Kontrolle**: passt die Folge beim errechneten Versatz nicht zusammen, steht
eine Warnung darueber.

Die **Versnummer jeder Ausgabe** steht bei jeder Zeile. Wo `de 4` neben `en 3`
steht, ist der Versatz sichtbar und nachpruefbar.

**Die Nummer der Ausgabe nie in einen Bericht schreiben, ohne sie hier
abgelesen zu haben.**

## Was dieses Werkzeug nicht kann

Es erkennt **fehlende** Verse, nicht **vertauschten Inhalt**. In Ps 60 traegt
die erste italienische Zeile nur die abgeschnittene Ueberschrift statt des
Verses; die Zeile ist vorhanden und lang, also richtet das Werkzeug sie
kommentarlos gegen den deutschen Vers 60,3 aus. Drei Versuche, das mechanisch
zu finden, sind gescheitert — ueber das Satzendezeichen (2000-3000 Fehlalarme
je Ausgabe), ueber die Verslaenge (findet den Fall gar nicht) und ueber
Ueberschriftenmerkmale (vier Treffer, drei davon zu Recht). Siehe
`VERSZAEHLUNG_PSALMEN.md`.

## Wo eine Ausgabe den Vers gar nicht hat

Der italienische Psalter hat in **63 Psalmen keinen Vers 1** — in Ps 23 fehlt
`Il Signore e il mio pastore`. Das ist ein Datenfehler des Bestands, kein
Versatz, und er steht schon im importierten Grundtext.

Dort druckt dieses Werkzeug ausdruecklich `dieser Vers fehlt in der Ausgabe`
und **bietet den Nachbarvers nicht an**. Genau so entstuende der Fehler: die
naechste italienische Zeile ist der Inhalt des deutschen Verses 2, und wer sie
nimmt, glossiert Vers 1 aus Vers 2. Fuer diese Verse hat das Italienische keine
Vorlage; die Glosse folgt dem Bestand und den drei anderen Ausgaben.
"""
import argparse
import json
import os

import common as C

AUSGABEN = [('en', 'eng', 'web'), ('es', 'spa', 'rv1909mod'),
            ('fr', 'fra', 'lsg1910'), ('it', 'ita', 'riv1927')]

# Wo der Versatz aus dem letzten Vers falsch ist, weil die Ausgabe nicht vorn
# etwas weglaesst, sondern hinten zwei Verse zusammenzieht. Nur eintragen, was
# **am Inhalt** geprueft ist — die Verslaengen koennen es nicht entscheiden.
#
# Ps 13 fr: LSG zaehlt die Ueberschrift mit wie in allen anderen 149 Psalmen
# (fr 1 = `Au chef des chantres. Psaume de David.` = deutsch 13,1) und zieht am
# Ende de 6 und de 7 in fr 6 zusammen. Der Versatz aus dem letzten Vers sagt
# -1, richtig ist 0. Gefunden vom Agenten der Psalmen 10-13, der LSG direkt
# aus der Datei gelesen hat, statt der Tabelle zu glauben.
#
# Eine Fassung, die stattdessen den Versatz 0 als Kandidaten mitrechnen liess
# und nach Verslaengen entschied, hat Ps 13 richtig bekommen und dafuer Ps 21
# (it), Ps 58 (es), Ps 76 (en) und Ps 142 (it) falsch. Die Laengen taugen
# dafuer nicht.
AUSNAHMEN = {(19, '13', 'fr'): 0}

SCHWACH = 0.30      # ab hier gilt die Ausrichtung als unsicher


def _pfad(sprache, edition, nr):
    return os.path.join(C.REPO, 'bibles', sprache, edition, f'{int(nr)}_{edition}.json')


def lade(nr):
    """kuerzel -> {kap: {vers: text}}, fehlende Ausgaben fehlen im Ergebnis."""
    out = {}
    for kurz, sprache, edition in AUSGABEN:
        p = _pfad(sprache, edition, nr)
        if os.path.exists(p):
            with open(p, encoding='utf-8') as f:
                out[kurz] = json.load(f)['chapters']
    return out


def _laengen(kap):
    return {int(v): len(t.split()) for v, t in kap.items()}


def versatz(dkap, okap):
    """(versatz, abstand) — um wieviel die Ausgabe gegen das Deutsche verschoben ist.

    Der Versatz kommt aus dem **letzten Vers**, nicht aus einer Aehnlichkeit:
    wo eine Ausgabe die Ueberschrift nicht mitzaehlt, fehlt sie vorn und der
    Schluss deckt sich. Ps 19 hat deutsch 15 Verse und englisch 14, und
    deutsch 15 ist englisch 14 — Wort fuer Wort dasselbe.

    Eine erste Fassung hat den Versatz ueber die Folge der Verslaengen
    geschaetzt. Das war die falsche Groesse und hat in Ps 9, 15 und 19
    danebengelegen, jedes Mal lautlos: die verschobene Zeile las sich
    plausibel. Genau der Fehler, gegen den dieses Werkzeug gebaut ist.

    Die Verslaengen bleiben als **Kontrolle**: passt die Folge beim errechneten
    Versatz nicht zusammen, hat die Ausgabe nicht nur vorn etwas weggelassen,
    sondern mittendrin zusammengezogen. Dann gilt kein fester Versatz und die
    Zeile traegt eine Warnung.
    """
    if not dkap or not okap:
        return None
    dn = sorted(int(v) for v in dkap)
    on = sorted(int(v) for v in okap)
    dl = {int(v): len(t.split()) for v, t in dkap.items()}
    ol = {int(v): len(t.split()) for v, t in okap.items()}

    def bewerten(off):
        paare = [(dl[i], ol[i + off]) for i in dl if i + off in ol]
        if not paare:
            return 1.0, len(dl)
        s = sum(abs(a - b) / max(a, b, 1) for a, b in paare) / len(paare)
        return s, len(dl) - len(paare)

    off = on[-1] - dn[-1]
    s, _ = bewerten(off)
    fehlend = [i for i in sorted(dl) if i + off not in ol]
    if len(dkap) + off != len(okap):
        s = max(s, SCHWACH + 0.01)

    # Der blinde Fleck des Versatzes-aus-dem-letzten-Vers: hat die Ausgabe EINEN
    # Vers MEHR als das Deutsche, weil ihr Kapitel einen Vers weiter reicht (die
    # naechste Kapitelgrenze liegt anders), dann sieht das an den blossen Zahlen
    # genauso aus wie ein durchgehender Versatz +1 — `len(dkap) + off ==
    # len(okap)` stimmt in BEIDEN Faellen, die Warnung oben greift also nicht.
    # Gemessen an Hld 6: en/es/it haben 13 Verse, de und fr 12, und ihr 13. Vers
    # ist de 7,1. Der richtige Versatz ist 0, das Werkzeug nahm +1 und paarte
    # jede Zeile mit der falschen — lautlos, mit Abstand 0.24-0.29, also unter
    # der Schwelle. Versatz 0 bewertet an derselben Stelle 0.09-0.14.
    #
    # Der Versatz wird deshalb NICHT stillschweigend ausgetauscht (genau das hat
    # in Ps 9, 15 und 19 danebengelegen, siehe oben). Stattdessen werden die
    # Nachbarversaetze mitbewertet, und wenn einer DEUTLICH besser liegt, traegt
    # die Zeile eine Warnung samt Alternative — sichtbar und nachpruefbar.
    rivale = []
    for kandidat in (0, off - 1, off + 1):
        if kandidat == off:
            continue
        ks, _ = bewerten(kandidat)
        rivale.append((ks, kandidat))
    rivale.sort()
    # Die Schwelle ist an fuenf bekannten Kapiteln geeicht. Sie muss eng sein:
    # eine Warnung, die staendig grundlos feuert, bringt jeder Agent sich ab.
    #   FEUERT RICHTIG — verschobene Kapitelgrenze, Rest haengt hinten:
    #     Hld 6  (0.14/0.29 · 0.09/0.24 · 0.14/0.27)
    #     Pred 4 (0.13/0.34 · 0.12/0.32 · 0.17/0.36)
    #   DARF NICHT FEUERN — deutsch zaehlt die Ueberschrift mit, die Ausgabe
    #   nicht; der Versatz aus dem letzten Vers ist dort gerade der richtige:
    #     Ps 19 it (0.19/0.31 = 0.61)  ·  Ps 15 en (0.13/0.22 = 0.59)
    # Verhaeltnis unter 0.55 trennt beides bis auf Ps 9 it (0.52), das als
    # bekannter Fehlalarm stehenbleibt — lieber einer zuviel als die Klasse
    # ganz unentdeckt.
    besser = None
    if rivale:
        ks, kandidat = rivale[0]
        if ks < s - 0.08 and ks < 0.55 * s:
            besser = (ks, kandidat)
    return (off, s, fehlend, besser)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel')
    p.add_argument('von', nargs='?', type=int)
    p.add_argument('bis', nargs='?', type=int)
    p.add_argument('--umgebung', type=int, default=0,
                   help='so viele Nachbarverse der Ausgaben mitdrucken')
    args = p.parse_args()

    s = C.load_source(args.buch)
    kap = str(int(args.kapitel))
    dkap = s['chapters'][kap]
    andere = lade(args.buch)

    versaetze = {}
    for kurz in andere:
        okap = andere[kurz].get(kap, {})
        v = versatz(dkap, okap) if okap else None
        fest = AUSNAHMEN.get((args.buch, kap, kurz))
        if v and fest is not None:
            v = (fest, v[1], [i for i in sorted(int(x) for x in dkap)
                              if str(i + fest) not in okap], None)
        versaetze[kurz] = v

    print(f'# {s["name"]} {kap}\n')
    kopf = []
    for kurz, _, edition in AUSGABEN:
        v = versaetze.get(kurz)
        if v is None:
            kopf.append(f'{kurz} ({edition}): fehlt')
        else:
            marke = '  UNSICHER' if v[1] > SCHWACH else ''
            if len(v) > 3 and v[3]:
                marke += (f'  !! Versatz {v[3][1]:+d} liegt BESSER '
                          f'(Abstand {v[3][0]:.2f} gegen {v[1]:.2f})')
            luecke = [x for x in v[2] if x + v[0] >= 1]
            if luecke:
                marke += ('  — ohne Gegenstueck: de '
                          + ', '.join(str(x) for x in luecke[:6]))
            kopf.append(f'{kurz} ({edition}): Versatz {v[0]:+d}, Abstand {v[1]:.2f}{marke}')
    print('Ausrichtung ueber die Verslaengen — die Versnummer jeder Ausgabe steht')
    print('bei jeder Zeile. Wo sie nicht zum deutschen Vers passt, ist der Versatz')
    print('sichtbar und nachpruefbar.\n')
    for z in kopf:
        print('   ' + z)
    print()
    strittig = {k: v for k, v in versaetze.items()
                if v and len(v) > 3 and v[3]}
    if strittig:
        print('!! ACHTUNG: fuer mindestens eine Ausgabe liegt ein ANDERER Versatz')
        print('!! besser als der angewandte. Die Zeilen unten stehen dann falsch')
        print('!! da — nicht nur die Zahl. Betroffen:')
        for k, v in strittig.items():
            print(f'!!   {k}: angewandt {v[0]:+d} (Abstand {v[1]:.2f}), '
                  f'besser waere {v[3][1]:+d} (Abstand {v[3][0]:.2f})')
        print('!!')
        print('!! Der haeufigste Grund: die Ausgabe zieht die KAPITELGRENZE anders,')
        print('!! der ueberzaehlige Vers haengt also HINTEN. Der Versatz kommt aber')
        print('!! aus dem letzten Vers und schiebt ihn nach VORN — dann steht jede')
        print('!! Zeile eine Nummer daneben. An den blossen Verszahlen sind die')
        print('!! beiden Faelle nicht zu unterscheiden.')
        print('!! Gemessen an Hld 6: en/es/it haben 13 Verse, de und fr 12, und ihr')
        print('!! 13. Vers ist de 7,1 — richtig ist Versatz 0, das Werkzeug nahm +1')
        print('!! und paarte jede Zeile mit der falschen. Ebenso Prediger 4.')
        print('!!')
        print('!! Es ist ein VERDACHT, keine Feststellung. Er kann auch dort feuern,')
        print('!! wo der angewandte Versatz stimmt — naemlich wenn das Deutsche die')
        print('!! Ueberschrift als Vers 1 mitzaehlt und die Ausgabe nicht (Ps 9, 15,')
        print('!! 19). Dann fehlt der Vers VORN und der Versatz ist richtig negativ.')
        print('!!')
        print('!! So oder so: NACHMESSEN. Die Kapiteldateien unter bibles/<sprache>/')
        print('!! <edition>/ direkt aufschlagen und Vers fuer Vers vergleichen.')
        print('!! Der Zahl hier nicht glauben — auch der Alternative nicht.\n')
    if any(v and v[1] > SCHWACH for v in versaetze.values()):
        print('!! ACHTUNG: mindestens ein Versatz ist UNSICHER. Der geschaetzte')
        print('!! Versatz wird global angewandt — wenn er falsch ist, stehen die')
        print('!! Zeilen dieser Ausgabe unten AUCH FALSCH da, nicht nur die Zahl.')
        print('!! Das passiert regelmaessig, wenn eine Ausgabe die KAPITELGRENZE')
        print('!! anders zieht: dann ist der Versatz am Kapitelanfang 0 und kippt')
        print('!! erst spaeter. Beispiele: Prediger 4 (dort war die Anzeige noch')
        print('!! richtig) und Prediger 11 (dort war sie es nicht).')
        print('!! Fuer die betroffene Ausgabe die Kapiteldatei direkt aufschlagen:')
        print('!! bible-reader/bibles/<sprache>/<edition>/<nr>_<edition>.json\n')

    verse = sorted(dkap, key=int)
    if args.von:
        bis = args.bis or args.von
        verse = [v for v in verse if args.von <= int(v) <= bis]

    for v in verse:
        print(f'## {kap},{v}')
        print(f'   de {v:>3}  {dkap[v]}')
        for kurz, _, _ in AUSGABEN:
            vs = versaetze.get(kurz)
            if vs is None:
                continue
            okap = andere[kurz].get(kap, {})
            n0 = int(v) + vs[0]
            if str(n0) not in okap:
                # Nicht den Nachbarvers anbieten. Genau so entsteht der Fehler,
                # gegen den dieses Werkzeug gebaut ist: der italienische Psalter
                # hat in Ps 23 keinen Vers 1, und die naechste Zeile ist der
                # deutsche Vers 2. Wer sie nimmt, glossiert Vers 1 aus Vers 2.
                if n0 < 1:
                    print(f'   {kurz}   -   — diesen Vers zaehlt die Ausgabe nicht mit '
                          f'(Ueberschrift)')
                else:
                    print(f'   {kurz} {n0:>3}   — kein Gegenstueck in dieser Ausgabe '
                          f'(Vers fehlt oder ist mit dem Nachbarn zusammengezogen)')
                continue
            unsicher = vs[1] > SCHWACH
            spanne = args.umgebung or (1 if unsicher else 0)
            for d in range(-spanne, spanne + 1):
                n = n0 + d
                t = okap.get(str(n))
                if t:
                    marke = ' ?' if d else '  '
                    print(f'   {kurz} {n:>3}{marke}{t}')
        print()


if __name__ == '__main__':
    main()
