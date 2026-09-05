#!/usr/bin/env python3
"""Ausrichtung ueber Kapitelgrenzen hinweg — was ausgaben.py nicht kann.

    kapitelgrenzen.py <buchNr> [<buchNr> …]

## Der Anlass

`ausgaben.py` sucht **je Kapitel** einen Versatz. Wo eine Ausgabe einen
ganzen Block ueber die Kapitelgrenze schiebt — Daniel 3,31 steht dort als
4,1, Joel 4,1 als 3,1, Maleachi 3,19 als 4,1 — findet es keinen und meldet
entweder `FEHLT` oder, schlimmer, einen falschen Versatz mit dem Zusatz
`UNSICHER`. In Daniel 3 und 5 war der automatisch gewaehlte Versatz falsch
und der Warnhinweis richtig; wer den Hinweis ueberliest, glossiert drei
Verse gegen die falsche Vorlage.

## Was dieses Skript macht

Es legt beide Buecher **flach** — eine Liste aller Verse in Kapitel- und
Versfolge — und sucht fuer jedes deutsche Kapitel den flachen Versatz, der
die Verslaengen am besten deckt. Ein Versatz, der ueber die Kapitelgrenze
zeigt, faellt damit genauso auf wie einer innerhalb des Kapitels.

Verglichen wird die **relative Verslaenge**, nicht der Inhalt: eine
Uebersetzung haelt die Laengenverhaeltnisse ihrer Vorlage ueber ein ganzes
Kapitel hinweg gut genug, um den Versatz eindeutig zu machen. Der Abstand
steht dabei; ueber 0.25 ist die Auskunft nicht zu trauen.
"""
import glob, os
import json
import sys


BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def flach(nr, dirname):
    """Die Verslaengen eines Buches, flach ueber alle Kapitel.

    Der Pfad wird vom Ort DIESER Datei aus gebildet, nicht vom
    Arbeitsverzeichnis. Vorher stand hier ein relativer glob — und weil
    jedes Werkzeug laut Prompt-Baustein **aus `anno-tools/` heraus**
    aufgerufen wird, fand er den Quelltext nie und das Skript meldete
    fuer jedes Buch „kein deutscher Quelltext". Aufgefallen an Sacharja,
    also am ersten Buch seit Daniel, das eine echte Kapitelgrenzen-
    verschiebung traegt.
    """
    treffer = glob.glob(os.path.join(BASIS, dirname, f'{nr}_*.json'))
    if not treffer:
        return None
    d = json.load(open(treffer[0], encoding='utf-8'))
    ch = d.get('chapters', d)
    aus = []
    for k in sorted(ch, key=int):
        for v in sorted(ch[k], key=int):
            aus.append((k, v, len(ch[k][v].split())))
    return aus


def abstand(de, fo, von, bis, d):
    """Mittlerer relativer Laengenunterschied fuer Versatz d."""
    s = n = 0
    for i in range(von, bis):
        j = i + d
        if not 0 <= j < len(fo):
            return 9.9
        a, b = de[i][2], fo[j][2]
        if a + b == 0:
            continue
        s += abs(a - b) / max(a, b)
        n += 1
    return s / n if n else 9.9


AUSGABEN = [('en', 'eng/web'), ('es', 'spa/rv1909mod'),
            ('fr', 'fra/lsg1910'), ('it', 'ita/riv1927')]


def buch(nr):
    de = flach(nr, 'deu/l1912mod')
    if de is None:
        print(f'Buch {nr}: kein deutscher Quelltext.')
        return
    kapitel = sorted({k for k, _, _ in de}, key=int)
    print(f'\n## Buch {nr} — {len(kapitel)} Kapitel, {len(de)} Verse\n')
    for spr, dirname in AUSGABEN:
        fo = flach(nr, dirname)
        if fo is None:
            print(f'   {spr}: keine Datei')
            continue
        zeilen = []
        if len(fo) != len(de):
            zeilen.append(f'   {spr}  GESAMTZAHL: {len(fo)} Verse gegen {len(de)} '
                          'deutsche — die Ausgabe zaehlt insgesamt anders')
        for k in kapitel:
            von = next(i for i, e in enumerate(de) if e[0] == k)
            bis = von + sum(1 for e in de if e[0] == k)
            # Bezugspunkt ist NICHT der flache Versatz 0, sondern die
            # kanonische Ausrichtung: derselbe Kapitel- und Versname in
            # der Ausgabe. Wo eine Ausgabe frueher einen Vers auslaesst,
            # sind flacher Versatz 0 und gleiche Versnummer zweierlei —
            # daran ist die erste Fassung dieses Skripts gescheitert.
            kanon = next((i - von for i, e in enumerate(fo)
                          if e[0] == k and e[1] == de[von][1]), None)
            gleich = sum(1 for e in fo if e[0] == k) == bis - von
            kand = sorted(range(-40, 41),
                          key=lambda d: abstand(de, fo, von, bis, d))
            best = kand[0]
            a = abstand(de, fo, von, bis, best)
            ruhe = abstand(de, fo, von, bis, kanon) if kanon is not None else 9.9
            # Ein abweichender Versatz zaehlt nur, wenn er DEUTLICH besser
            # liegt als die kanonische Ausrichtung — und nie, wenn das
            # gleichnamige Kapitel der Ausgabe schon gleich viele Verse hat.
            if kanon is not None and best != kanon and (
                    gleich or not (a < ruhe - 0.05 and a < 0.25)):
                best, a = kanon, ruhe
            ziel_von = fo[von + best] if 0 <= von + best < len(fo) else None
            ziel_bis = fo[bis - 1 + best] if 0 <= bis - 1 + best < len(fo) else None
            if ziel_von is None or ziel_bis is None:
                zeilen.append(f'   {spr}  K{k}: AUSSERHALB')
                continue
            quelle = f'{k},{de[von][1]}-{de[bis-1][1]}'
            ziel = (f'{ziel_von[0]},{ziel_von[1]}-{ziel_bis[1]}'
                    if ziel_von[0] == ziel_bis[0]
                    else f'{ziel_von[0]},{ziel_von[1]} - {ziel_bis[0]},{ziel_bis[1]}')
            marke = ''
            if best == kanon and ziel_von[0] == k and ziel_bis[0] != k:
                # Kanonischer Anfang, aber das deutsche Kapitel ist laenger:
                # die Ausgabe zieht Verse zusammen oder laesst einen aus.
                # Das ist KEIN Versatz — der naechste Kapitelanfang stimmt.
                schluss = ('stehen dort im NAECHSTEN Kapitel'
                           if len(fo) == len(de)
                           else 'haben dort KEINE Vorlage — die Ausgabe zaehlt '
                                'insgesamt weniger Verse')
                marke = (f'  << die Ausgabe hat nur '
                         f'{sum(1 for e in fo if e[0] == k)} Verse gegen {bis - von}'
                         f' — die letzten deutschen Verse {schluss}')
            elif ziel_von[0] != ziel_bis[0]:
                marke = '  << LAEUFT UEBER DIE KAPITELGRENZE'
            elif ziel_von[0] != k:
                marke = '  << ANDERES KAPITEL'
            elif ziel_von[1] != de[von][1]:
                marke = '  << Versatz'
            elif not gleich:
                marke = ('  << gleiche Versnummern, aber die Ausgabe hat '
                         f'{sum(1 for e in fo if e[0] == k)} Verse gegen {bis - von}'
                         ' — ein Vers FEHLT oder ist zusammengezogen')
            if marke:
                marke += f'   (Abstand {a:.2f}, kanonisch {ruhe:.2f})'
            zeilen.append(f'   {spr}  {quelle:>12}  ->  {ziel:<16}{marke}')
        auffaellig = [z for z in zeilen if '<<' in z or 'GESAMTZAHL' in z]
        if auffaellig:
            print('\n'.join(auffaellig))
    print('   (nur Kapitel mit Abweichung; alles Uebrige steht auf Versatz +0)')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for nr in sys.argv[1:]:
        buch(int(nr))
