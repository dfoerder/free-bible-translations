"""Die Vorbereitungsdatei eines Pakets, maschinell.

    vorbereitung.py <buchNr> <kapitel …> [-o datei]

## Wozu

Fuer jedes Paket eines Buches entsteht bisher von Hand eine `VORLAGEN.md`:
Versatz je Ausgabe, Parallelstellen im fertigen Bestand, buchinterne Dubletten,
und die Aufteilung der Dubletten in *schon annotiert* / *innerhalb des Pakets* /
*fuer spaetere Pakete einsammeln*. Fuer Jesaja waren das zehn Dateien; Jeremia
hat **52 Kapitel, 18 Pakete und 261 buchinterne Dublettenpaare** — das von Hand
zu sortieren ist die Sorte Arbeit, bei der Fehler entstehen.

Dieses Skript baut das Geruest. Was es **nicht** kann und was von Hand
dazukommt: die Vorgabetabelle der paketweiten Glossenreihen (die entsteht aus
`fixgloss.py show`) und die Hinweise zum einzelnen Kapitel. Und was immer
dazugehoert: **`promptcheck.py` ueber die fertige Datei laufen lassen**, bevor
sie an Agenten geht.

## Die drei Dublettenrichtungen

Sie sind der Grund fuer das Skript. Eine Dublette ist je nach Lage etwas
voellig anderes:

* **Vorlage steht in einem frueheren Kapitel** — dort nachschlagen und Position
  fuer Position uebernehmen, nach dem Grundsatz aus Paket 14 (die Einstufung
  sagt, wo nachzusehen ist, nicht wo kopiert werden darf).
* **Beide Verse liegen im selben Paket** — die Agenten laufen gleichzeitig und
  koennen einander nicht sehen; die Reihe gehoert in beide Berichte, und der
  Koordinator gleicht beim Einsammeln ab.
* **Vorlage ist dein Vers, die Wiederholung kommt spaeter** — die Reihe gehoert
  vollstaendig in den Bericht, damit das spaetere Paket sie bekommt.

Ein Werkzeug, das die drei nicht unterscheidet, ist wertlos: die dritte Sorte
sieht der Agent, der sie erzeugt, ueberhaupt nicht.
"""
import argparse
import collections
import io
import json
import os
import subprocess
import sys

import common as C

HIER = os.path.dirname(os.path.abspath(__file__))


def versatz(nr, kaps):
    """Zeile je Kapitel: was `ausgaben.py` ueber den Versatz sagt."""
    raus = []
    for kap in kaps:
        r = subprocess.run([sys.executable, 'ausgaben.py', str(nr), str(kap)],
                           capture_output=True, text=True, cwd=HIER)
        zeilen = [z.strip() for z in r.stdout.splitlines() if '): Versatz' in z]
        raus.append((kap, zeilen))
    return raus


def parallelen(nr, kaps, minblock=5):
    """{kapitel: [zeilen]} aus `parallelen.py`, auf Ueberschriften gekuerzt."""
    raus = {}
    for kap in kaps:
        r = subprocess.run([sys.executable, 'parallelen.py', str(nr), str(kap),
                            str(minblock)], capture_output=True, text=True, cwd=HIER)
        treffer = [z.rstrip() for z in r.stdout.splitlines() if z.startswith('## ')]
        raus[kap] = treffer
    return raus


def dubletten(nr, anteil=0.6, minlen=5):
    """[(kapA, versA, kapB, versB, woertlich)] ueber den Quelltext des Buches."""
    src = C.load_source(nr)['chapters']
    verse = []
    for kap in sorted(src, key=int):
        for v in sorted(src[kap], key=int):
            toks = [C.norm_key(t) for t in C.tokens(src[kap][v])]
            toks = [t for t in toks if t]
            if len(toks) >= minlen:
                verse.append((kap, v, set(toks), tuple(toks)))
    paare = []
    for i in range(len(verse)):
        ka, va, sa, ta = verse[i]
        for j in range(i + 1, len(verse)):
            kb, vb, sb, tb = verse[j]
            gem = len(sa & sb)
            if gem / len(sa) >= anteil and gem / len(sb) >= anteil:
                paare.append((ka, va, kb, vb, ta == tb))
    return paare


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('buch', type=int)
    p.add_argument('kapitel', nargs='+')
    p.add_argument('-o', '--out')
    p.add_argument('--minblock', type=int, default=5)
    a = p.parse_args()

    nr = a.buch
    kaps = [str(int(k)) for k in a.kapitel]
    name = C.book_name(nr)
    imPaket = set(kaps)
    frueher = {k for k in C.load_source(nr)['chapters'] if int(k) < min(int(x) for x in kaps)}

    aus = io.StringIO()
    w = aus.write
    w(f'# {name} — Vorbereitung fuer Kap. {" · ".join(kaps)}\n\n')
    w('Maschinell erzeugt von `vorbereitung.py`. Was von Hand dazukommt: die\n'
      'Vorgabetabelle der paketweiten Glossenreihen und die Hinweise zum\n'
      'einzelnen Kapitel. **Vor dem Abschicken `promptcheck.py` ueber diese\n'
      'Datei laufen lassen.**\n\n')

    w('## Versatz der vier Ausgaben\n\n')
    for kap, zeilen in versatz(nr, kaps):
        w(f'**Kap. {kap}**\n\n')
        for z in zeilen:
            w(f'    {z}\n')
        w('\n')

    w('## Parallelstellen im fertigen Bestand\n\n')
    par = parallelen(nr, kaps, a.minblock)
    for kap in kaps:
        w(f'**Kap. {kap}**\n\n')
        if not par[kap]:
            w(f'    keine ab {a.minblock} gemeinsamen Tokens\n\n')
            continue
        for z in par[kap]:
            w(f'    {z[3:]}\n')
        w('\n')

    w('## Buchinterne Dubletten\n\n')
    paare = dubletten(nr)
    vorlage, imselben, fuerspaeter = [], [], []
    for ka, va, kb, vb, woertlich in paare:
        marke = ' **woertlich gleich**' if woertlich else ''
        a_im, b_im = ka in imPaket, kb in imPaket
        if a_im and b_im:
            imselben.append(f'* {ka},{va} ↔ {kb},{vb}{marke}')
        elif b_im and ka in frueher:
            vorlage.append(f'* {kb},{vb} ← **{ka},{va}** (fertig){marke}')
        elif a_im and kb in frueher:
            vorlage.append(f'* {ka},{va} ← **{kb},{vb}** (fertig){marke}')
        elif a_im and not b_im:
            fuerspaeter.append(f'* {ka},{va} → **{kb},{vb}** (spaeteres Paket){marke}')
        elif b_im and not a_im:
            fuerspaeter.append(f'* {kb},{vb} → **{ka},{va}** (spaeteres Paket){marke}')

    for titel, liste, erklaerung in [
        ('Vorlage steht in einem fertigen Kapitel — nachschlagen', vorlage,
         'Position fuer Position pruefen. Die Einstufung sagt, wo nachzusehen\n'
         'ist, nicht wo kopiert werden darf.'),
        ('Beide Verse im selben Paket — die Agenten sehen einander nicht', imselben,
         'Jeder entscheidet seinen Vers aus dem Bestand und den Ausgaben und\n'
         'schreibt die Reihe in den Bericht; der Koordinator gleicht ab.'),
        ('Dein Vers ist die Vorlage — Reihe fuer spaeter einsammeln', fuerspaeter,
         'Vollstaendig in den Bericht, sonst muss ein spaeteres Paket dieselbe\n'
         'Entscheidung noch einmal treffen.'),
    ]:
        w(f'### {titel}\n\n{erklaerung}\n\n')
        if liste:
            w('\n'.join(sorted(set(liste))) + '\n\n')
        else:
            w('    keine\n\n')

    text = aus.getvalue()
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'geschrieben: {a.out}')
        print(f'{len(vorlage)} Vorlagen · {len(imselben)} paketintern · '
              f'{len(fuerspaeter)} fuer spaeter')
    else:
        print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
