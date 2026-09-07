#!/usr/bin/env python3
"""Alles, was ein Paket der franzoesischen Annotation braucht — ein Lauf.

    fravorb.py <buchNr> <kapitel> [<kapitel> ...] --scratch <verzeichnis>

Schreibt nach `<scratch>/vorb/`:

    rueckwaerts_<nr>_<kap>.md   je Kapitel — der Bestand zu jedem Wort
    ausgaben_<nr>_<kap>.md      je Kapitel — die vier Zeugen daneben
    hints_<nr>_<kap>.md         je Kapitel — unbelegte Formen, Kollisionen
    bindungen_<nr>_p<kaps>.md   fuer das Paket — was es praegt, was es erbt
    kapitelgrenzen_<nr>.md      einmal je Buch

und daraus je Kapitel einen fertigen Prompt nach `<scratch>/`:

    prompt_<nr>_<kap>.md        Baustein + Verweise auf die Vorbereitung

## Warum als Skript

In der deutschen Arbeit ist der Baustein einmal per `sed` aus dem Prompt
des Vorgaengerbuchs abgeleitet worden — und hat dessen Buchnummer
mitgeschleppt, sodass Obadja und Jona `kongruenz.py 30` verlangten, also
einen Lauf ueber Amos. Ein Generator kann diesen Fehler nicht machen.

Der erzeugte Prompt behauptet **nichts** ueber den Text: er verweist nur
auf gemessene Dateien. Was ich selbst hineinschreibe, ist der Teil, der
in Judas zweimal falsch war.
"""
import argparse
import os
import subprocess
import sys

import common as C

HIER = os.path.dirname(os.path.abspath(__file__))
BAUSTEIN = os.path.join(HIER, 'PROMPT_BAUSTEIN_FRA.md')


def lauf(argv, ziel):
    """Ein Werkzeug laufen lassen und die Ausgabe wegschreiben."""
    r = subprocess.run([sys.executable] + argv, cwd=HIER,
                       capture_output=True, text=True, env=os.environ)
    open(ziel, 'w', encoding='utf-8').write(r.stdout + r.stderr)
    return len(r.stdout)


def baustein(nr, kap, buch, scratch):
    s = open(BAUSTEIN, encoding='utf-8').read()
    s = s[s.index('Du annotierst'):]
    for a, b in (('<NR>', str(nr)), ('<KAP>', str(kap)),
                 ('<BUCH>', buch), ('<SCRATCH>', scratch)):
        s = s.replace(a, b)
    return s


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel', nargs='+')
    p.add_argument('--scratch', required=True)
    p.add_argument('--hinweis', action='append', default=[],
                   metavar='KAP:TEXT',
                   help='ein kapitelspezifischer Hinweis, der IN DIE '
                        'PROMPTDATEI geschrieben wird — nur dort sieht ihn '
                        'vorgabecheck.py')
    a = p.parse_args()

    if C.EDITION != 'fra/lsg1910mod':
        raise SystemExit(f'ANNO_EDITION steht auf {C.EDITION!r} — '
                         'dieses Skript ist fuer fra/lsg1910mod.')

    nr, kaps = a.buch, a.kapitel
    buch = C.book_name(nr)
    vorb = os.path.join(a.scratch, 'vorb')
    os.makedirs(vorb, exist_ok=True)

    kg = os.path.join(vorb, f'kapitelgrenzen_{nr}.md')
    if not os.path.exists(kg):
        lauf(['kapitelgrenzen.py', str(nr)], kg)

    marke = '_'.join(kaps)
    bind = os.path.join(vorb, f'bindungen_{nr}_p{marke}.md')
    lauf(['paketvorb.py', str(nr)] + kaps, bind)

    for kap in kaps:
        for werkzeug, name in (('rueckwaerts.py', 'rueckwaerts'),
                               ('ausgaben.py', 'ausgaben'),
                               ('hints.py', 'hints')):
            lauf([werkzeug, str(nr), kap],
                 os.path.join(vorb, f'{name}_{nr}_{kap}.md'))

        prompt = baustein(nr, kap, buch, a.scratch)
        eigene = [h.split(':', 1)[1].strip() for h in a.hinweis
                  if h.split(':', 1)[0].strip() == str(kap)]
        prompt += f'''

---

## Deine Vorbereitung — alles gemessen, nichts behauptet

Die Dateien liegen in `{vorb}/`:

    rueckwaerts_{nr}_{kap}.md   was der Bestand zu jedem Wort deines
                            Kapitels fuehrt, vers fuer vers, vier Schichten
    ausgaben_{nr}_{kap}.md      die vier Zeugen neben deinem Vers
    hints_{nr}_{kap}.md         unbelegte Formen, Kollisionen im Vers
    bindungen_{nr}_p{marke}.md  die Wortfolgen dieses Pakets
    kapitelgrenzen_{nr}.md      die Verszaehlung aller Zeugen

**Lies `bindungen_{nr}_p{marke}.md` zuerst.** Es trennt, was dein Paket
**praegt** (der frueheste Ort der Folge liegt hier — was du setzt, gilt
fuer das ganze Buch) von dem, was es **uebernimmt** (die Reihe steht
schon, gemessen, nicht erinnert). Im Paket selbst wird zeichengleich
gesetzt: sprich dich ueber die Folgen ab, die in mehreren Kapiteln des
Pakets stehen — dein Bericht nennt sie ausdruecklich.

Danach `rueckwaerts_{nr}_{kap}.md` und `ausgaben_{nr}_{kap}.md` ganz.

**Alles in diesem Prompt ist gemessen oder verweist auf eine Messung.**
Was in Judas zweimal falsch war, waren meine eigenen Verszitate aus dem
Gedaechtnis. Sollte hier dennoch eine Behauptung ueber den Text stehen
und der Quelltext etwas anderes sagen, **gilt der Quelltext** — und der
Widerspruch gehoert in deinen Bericht.
'''
        if eigene:
            prompt += '\n## Zu diesem Kapitel\n\n'
            prompt += '\n\n'.join(eigene) + '\n'
        ziel = os.path.join(a.scratch, f'prompt_{nr}_{kap}.md')
        open(ziel, 'w', encoding='utf-8').write(prompt)
        print(f'  {ziel}')
    print(f'Vorbereitung in {vorb}/')


if __name__ == '__main__':
    main()
