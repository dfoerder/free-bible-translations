#!/usr/bin/env python3
"""Die Bindungstabelle eines Pakets — was es praegt und was es uebernimmt.

    paketvorb.py <buchNr> <kapitel> [<kapitel> ...] [-o datei]

## Der Anlass

`wiederholungen.py` gibt die Wortfolgen eines ganzen Buches — in
Matthaeus sind das **503**, 45 KB. Kein Kapitelagent braucht alle, und
keiner soll sie durchsuchen muessen; in Maleachi habe ich genau diese
Liste mit `tail -40` gelesen und die haeufigste Folge dabei verloren.

Dieses Werkzeug schneidet den Teil heraus, der ein Paket angeht, und
trennt ihn in die zwei Faelle, die verschieden zu behandeln sind:

    PRAEGT       der frueheste Ort der Folge liegt in DIESEM Paket.
                 Das Paket entscheidet die Reihe fuer alle spaeteren.
    UEBERNIMMT   der frueheste Ort liegt in einem Kapitel, das schon
                 annotiert ist. Dann steht die Reihe fest und wird
                 zeichengleich uebernommen — sie wird hier **gemessen**,
                 nicht aus dem Gedaechtnis geschrieben.

Fuer den zweiten Fall zaehlt es jede Variante mit ihrer Zahl aus
(`folgenreihe.stellen`). Wo der Bestand selbst schwankt, steht das da —
dann entscheidet der Vers, und die Vorgabe sagt es ausdruecklich.
"""
import argparse
import collections
import re
import sys

import common as C
import folgenreihe as F
import wiederholungen as W


def folgen(nr, minlen=4, ab=2):
    """[(folge, [(kap, vers), …])] aus wiederholungen.py, haeufigste zuerst."""
    d = C.load_source(nr)['chapters']
    quelle = []
    for k in sorted(d, key=int):
        for v in sorted(d[k], key=int):
            quelle.append((f'{k},{v}', W.TOKEN.findall(d[k][v])))
    out = []
    for _laenge, orte, phr in W.folgen(quelle, minlen):
        if len(orte) < ab:
            continue
        out.append((phr, [tuple(o.split(',')) for o in orte]))
    return out


def _reihe(phr):
    """Die gemessenen Glossenreihen einer Folge im fertigen Bestand."""
    # `*_` faengt ab, was `folgenreihe.stellen()` spaeter noch
    # zurueckgibt. Die Grossschreibungswarnung hat dort ein sechstes
    # Feld angehaengt, und dieser Aufruf ist mit einem ValueError
    # gestorben — die Bindungsdateien des laufenden Pakets enthielten
    # danach einen Traceback statt eines Berichts. Gefunden vom
    # Agenten fuer 1. Korinther 16, der sich mit einem Shim beholfen
    # hat, statt anno-tools anzufassen.
    _w, voll, orte, unvoll, mehrwort, *_ = F.stellen(phr)
    return voll, orte, unvoll, mehrwort


def bericht(nr, kaps):
    kaps = {str(k) for k in kaps}
    fertig = set()
    for kap in C.quellen_kapitel(nr):
        fertig.add(str(kap))
    fertig -= kaps

    L = [f'# Bindungen fuer Buch {nr}, Kapitel {", ".join(sorted(kaps, key=int))}',
         '']
    eigen = C.book_name(nr)
    praegt, uebernimmt, fremd, spaeter = [], [], [], []
    for phr, stellen in folgen(nr):
        beruehrt = [s for s in stellen if s[0] in kaps]
        if not beruehrt:
            continue
        erst = min(stellen, key=lambda s: (int(s[0]), int(s[1])))
        if erst[0] in kaps:
            # Bis Markus hiess „der frueheste Ort liegt hier" auch, dass
            # die Folge noch nirgends steht. Das galt, solange Matthaeus
            # das einzige Buch war. Jetzt kann dieselbe Folge laengst in
            # einem ANDEREN Buch annotiert sein: `la tradition des
            # anciens` stand hier als „7,3 legt fest" und steht in
            # Mt 15,2. Gemeldet vom Agenten fuer Marc 7.
            voll, orte, unvoll, mw = _reihe(phr)
            auswaerts = sorted({x for xs in list(orte.values()) + list(mw.values())
                                for x in xs if not x.startswith(eigen + ' ')})
            if auswaerts:
                fremd.append((phr, stellen, erst, auswaerts))
            else:
                # Zweite Probe, bevor „PRAEGT" behauptet wird: steht ein
                # MEHRWORTLEMMA im Bestand, das die Inhaltswoerter der
                # Folge deckt? Die Suche oben laeuft ueber die
                # Zeichenkette und ist blind, sobald ein Wort
                # eingeschoben ist oder anders flektiert:
                # „rendre continuellement grâces à Dieu" stand hier als
                # PRAEGT und ist `rendre grâces` mit 43 Belegen,
                # „devons à votre sujet" ist `au sujet de` mit 9.
                # Dreimal gemeldet (Galater 1, 2. Thess. 1 und 2).
                # Nur warnen, wo ALLE Inhaltswoerter des Lemmas in der
                # Folge stecken. Sonst warnt die Vier-Zeichen-Heuristik
                # bei `j'ai obtenu miséricorde` vor `mise au tombeau`
                # (`mise` und `misé` teilen den Stamm) — Rauschen, das
                # die Warnung entwertet.
                nah = {l: o for l, o in F.nahe_lemmata(phr, wieviel=6).items()
                       if F.inhalt_stamm(l) <= F.inhalt_stamm(phr)}
                nah = dict(list(nah.items())[:2])
                if nah:
                    praegt.append((phr, stellen, erst, nah))
                else:
                    praegt.append((phr, stellen, erst, None))
        elif erst[0] in fertig:
            uebernimmt.append((phr, stellen, erst))
        else:
            spaeter.append((phr, stellen, erst))

    L.append(f'**{len(praegt)} praegt · {len(uebernimmt)} uebernimmt aus '
             f'diesem Buch · {len(fremd)} steht schon in einem anderen Buch · '
             f'{len(spaeter)} haengt an einem noch nicht annotierten Kapitel**')
    L.append('')

    if fremd:
        L.append('## STEHT SCHON IN EINEM ANDEREN BUCH')
        L.append('')
        L.append('Der frueheste Ort **in diesem Buch** liegt in deinem Paket — '
                 'aber die Folge ist anderswo im Bestand schon annotiert. Dann '
                 'praegst du nicht, sondern uebernimmst. Miss die Reihe mit '
                 '`folgenreihe.py "<die Folge>"` nach und setze zeichengleich, '
                 'wo dein Vers dasselbe sagt.')
        L.append('')
        for phr, stellen, erst, auswaerts in sorted(fremd,
                                                    key=lambda x: -len(x[1])):
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            L.append(f'### „{phr}"   (hier: {", ".join(hier)})')
            L.append(f'- steht schon: {", ".join(auswaerts[:6])}'
                     + (' …' if len(auswaerts) > 6 else ''))
            voll, _orte, unvoll, mw = _reihe(phr)
            for key, n in voll.most_common(3):
                L.append('- %d×  %s' % (n, ' | '.join(' '.join(t) for t in key)))
            for key, wo in sorted(mw.items(), key=lambda x: -len(x[1]))[:3]:
                L.append(f'- {len(wo)}× MEHRWORT [{key[0]}]  '
                         + ' · '.join(key[2:]))
            L.append('')

    if uebernimmt:
        L.append('## UEBERNIMMT — die Reihe steht schon fest')
        L.append('')
        L.append('Der frueheste Ort ist annotiert. Diese Reihen sind **gemessen**, '
                 'nicht erinnert. Wo mehrere Varianten stehen, schwankt der '
                 'Bestand selbst — dann entscheidet der Vers.')
        L.append('')
        for phr, stellen, erst in uebernimmt:
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            L.append(f'### „{phr}"   (zuerst {erst[0]},{erst[1]} — '
                     f'hier: {", ".join(hier)})')
            voll, orte, unvoll, mw = _reihe(phr)
            if not voll:
                L.append('- im Bestand noch nicht vollstaendig belegt')
            for key, n in voll.most_common():
                zeile = ' | '.join(' '.join(t) for t in key)
                L.append(f'- {n}×  {zeile}')
            # **Die Mehrwoerter gehoeren hierher, nicht nur in den
            # Auswaerts-Block.** Bis Matteo 22 stand hier allein die
            # Zeile „N Vorkommen unvollstaendig (dort liegt ein
            # Mehrwort)" — sie sagt, DASS eins da ist, aber nicht
            # welches. Der Agent fuer Matteo 22 hat nachgesehen: sechs
            # der zehn Folgen seines Kapitels tragen im Bestand einen
            # Mehrworteintrag (`simile a`, `di nuovo`, `meravigliarsi`,
            # `quello che`, `mettere alla prova`, `te stesso`), und wer
            # nur die Wort-fuer-Wort-Reihen liest, verliert sie alle.
            for key, wo in sorted(mw.items(), key=lambda x: -len(x[1])):
                L.append(f'- {len(wo)}× MEHRWORT [{key[0]}]  '
                         + ' · '.join(key[2:]))
            if unvoll:
                L.append(f'- {len(unvoll)} Vorkommen unvollstaendig '
                         '(dort liegt ein Mehrwort)')
            L.append('')

    if praegt:
        L.append('## PRAEGT — dieses Paket entscheidet')
        L.append('')
        L.append('Der frueheste Ort liegt hier, **und die Zeichenkette '
                 'steht in keinem anderen Buch des Bestands** — beides '
                 'gemessen. Was gesetzt wird, gilt fuer alle spaeteren '
                 'Vorkommen im ganzen Buch, **innerhalb des Pakets '
                 'zeichengleich**.')
        L.append('')
        L.append('Wo „**Achtung**" steht, deckt ein vorhandenes '
                 'Mehrwortlemma die Inhaltswoerter der Folge: dann ist sie '
                 'wahrscheinlich NICHT gepraegt, sondern gebunden, und die '
                 'Zeichenkette hat sie nur wegen eines eingeschobenen oder '
                 'anders flektierten Wortes verfehlt. Nachsehen, bevor du '
                 'praegst.')
        L.append('')
        for phr, stellen, erst, nah in sorted(praegt, key=lambda x: -len(x[1])):
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            spaet = len(stellen) - len(hier)
            L.append(f'- **„{phr}"** — {erst[0]},{erst[1]} legt fest · hier: '
                     f'{", ".join(hier)}'
                     + (f' · spaeter noch {spaet}×' if spaet else '')
                     + ('  \n  **Achtung**, im Bestand steht: '
                        + ' · '.join(f'`{l}` ({len(o)}×)'
                                     for l, o in nah.items()) if nah else ''))
        L.append('')

    if spaeter:
        L.append('## HAENGT AN EINEM SPAETEREN KAPITEL')
        L.append('')
        L.append('Der frueheste Ort ist noch nicht annotiert. **Nicht praegen** — '
                 'diese Folge entscheidet ein anderes Paket; hier nur den Vers '
                 'lesen und die naheliegende Reihe setzen.')
        L.append('')
        for phr, stellen, erst in spaeter:
            hier = [f'{k},{v}' for k, v in stellen if k in kaps]
            L.append(f'- „{phr}" — zuerst {erst[0]},{erst[1]} · hier: '
                     f'{", ".join(hier)}')
        L.append('')
    return '\n'.join(L)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel', nargs='+')
    p.add_argument('-o', '--out')
    a = p.parse_args()
    txt = bericht(a.buch, a.kapitel)
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(txt)
        print(f'{a.out} geschrieben ({len(txt)} Zeichen)')
    else:
        sys.stdout.write(txt)
