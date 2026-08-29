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
    off = on[-1] - dn[-1]
    dl = {int(v): len(t.split()) for v, t in dkap.items()}
    ol = {int(v): len(t.split()) for v, t in okap.items()}
    paare = [(dl[i], ol[i + off]) for i in dl if i + off in ol]
    fehlend = [i for i in sorted(dl) if i + off not in ol]
    if not paare:
        return (off, 1.0, fehlend)
    s = sum(abs(a - b) / max(a, b, 1) for a, b in paare) / len(paare)
    # Deckt der Versatz fast alle Verse ab, ist die Ausrichtung in Ordnung und
    # die Luecke eine echte Luecke der Ausgabe — nicht ein falscher Versatz.
    # Der italienische Psalter hat in 63 Psalmen keinen Vers 1; ohne diese
    # Unterscheidung stuende dort eine Versatzwarnung statt der Wahrheit.
    if len(paare) < 0.9 * min(len(dkap), len(okap)):
        s = max(s, SCHWACH + 0.01)
    return (off, s, fehlend)


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
        versaetze[kurz] = versatz(dkap, okap) if okap else None

    print(f'# {s["name"]} {kap}\n')
    kopf = []
    for kurz, _, edition in AUSGABEN:
        v = versaetze.get(kurz)
        if v is None:
            kopf.append(f'{kurz} ({edition}): fehlt')
        else:
            marke = '  UNSICHER' if v[1] > SCHWACH else ''
            luecke = [x for x in v[2] if x + v[0] >= 1]
            if luecke:
                marke += ('  — FEHLT in der Datei: de '
                          + ', '.join(str(x) for x in luecke[:6]))
            kopf.append(f'{kurz} ({edition}): Versatz {v[0]:+d}, Abstand {v[1]:.2f}{marke}')
    print('Ausrichtung ueber die Verslaengen — die Versnummer jeder Ausgabe steht')
    print('bei jeder Zeile. Wo sie nicht zum deutschen Vers passt, ist der Versatz')
    print('sichtbar und nachpruefbar.\n')
    for z in kopf:
        print('   ' + z)
    print()

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
                    print(f'   {kurz} {n0:>3}   — FEHLT in der Datei der Ausgabe '
                          f'(Datenfehler des Bestands, keine Vorlage)')
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
