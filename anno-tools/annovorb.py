#!/usr/bin/env python3
"""Alles, was ein Paket einer Annotation braucht — ein Lauf.

    annovorb.py <buchNr> <kapitel> [<kapitel> ...] --scratch <verzeichnis>

Der gemeinsame Rumpf hinter `fravorb.py` und `itavorb.py`. Welche
Ausgabe gemeint ist, sagt `ANNO_EDITION`; der Baustein heisst
`PROMPT_BAUSTEIN_<KUERZEL>.md` und wird daraus abgeleitet.

Schreibt nach `<scratch>/vorb/`:

    rueckwaerts_<nr>_<kap>.md   je Kapitel — der Bestand zu jedem Wort
    ausgaben_<nr>_<kap>.md      je Kapitel — die vier Zeugen daneben
    parallelen_<nr>_<kap>.md    je Kapitel — derselbe Wortlaut, schon annotiert
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

# Der Bestandsname der Sprache, wie er im Prompttext vorkommt.
SPRACHE = {'de': 'deutschen', 'en': 'englischen', 'es': 'spanischen',
           'fr': 'franzoesischen', 'it': 'italienischen'}


def baustein_pfad(edition=None):
    kurz = C.AUSGABEN[edition or C.EDITION]['kurz']
    return os.path.join(HIER, f'PROMPT_BAUSTEIN_{kurz.upper()}.md')


def lauf(argv, ziel):
    """Ein Werkzeug laufen lassen und die Ausgabe wegschreiben."""
    r = subprocess.run([sys.executable] + argv, cwd=HIER,
                       capture_output=True, text=True, env=os.environ)
    open(ziel, 'w', encoding='utf-8').write(r.stdout + r.stderr)
    return len(r.stdout)


def baustein(nr, kap, buch, scratch, paket=()):
    s = open(baustein_pfad(), encoding='utf-8').read()
    s = s[s.index('Du annotierst'):]
    # `<PAKET>` sind ALLE Kapitel des Pakets. Vorher stand im Baustein
    # `paketcheck.py <NR> <KAP> <KAP> <KAP>` — nach der Ersetzung also
    # dreimal die eigene Nummer, und der Lauf verglich das Kapitel mit
    # sich selbst. Jeder Agent hielt den leeren Lauf fuer sauber.
    # Gemeldet vom Agenten fuer Matthaeus 27.
    # `<GEGEN>` sind alle schon annotierten Buecher ausser dem eigenen.
    # Fuer Markus ist das Matthaeus, fuer Lukas Matthaeus und Markus —
    # die Liste waechst von selbst mit dem Bestand.
    gegen = ' '.join(str(b) for b in sorted(C.anno_books()) if b != nr)
    for a, b in (('<NR>', str(nr)), ('<KAP>', str(kap)),
                 ('<GEGEN>', gegen),
                 ('<PAKET>', ' '.join(str(x) for x in paket)),
                 ('<BUCH>', buch), ('<SCRATCH>', scratch)):
        s = s.replace(a, b)
    return s


def main(edition=None):
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

    if edition and C.EDITION != edition:
        raise SystemExit(f'ANNO_EDITION steht auf {C.EDITION!r} — '
                         f'dieses Skript ist fuer {edition}.')
    if not os.path.exists(baustein_pfad()):
        raise SystemExit(f'Kein Baustein fuer {C.EDITION}: '
                         f'{baustein_pfad()} fehlt.')

    nr, kaps = a.buch, a.kapitel
    buch = C.book_name(nr)
    sprache = SPRACHE[C.LANG]
    vorb = os.path.join(a.scratch, 'vorb')
    os.makedirs(vorb, exist_ok=True)

    kg = os.path.join(vorb, f'kapitelgrenzen_{nr}.md')
    if not os.path.exists(kg):
        lauf(['kapitelgrenzen.py', str(nr)], kg)

    marke = '_'.join(kaps)
    bind = os.path.join(vorb, f'bindungen_{nr}_p{marke}.md')
    lauf(['paketvorb.py', str(nr)] + kaps, bind)

    for kap in kaps:
        # `parallelen.py` kam mit Markus dazu. In Matthaeus haette es
        # nichts gefunden — es war das erste franzoesische Buch. Von
        # Markus an steht der Synoptikerstoff annotiert daneben: Marc 1,3
        # teilt mit Matthieu 3,3 siebzehn Tokens am Stueck.
        for werkzeug, name in (('rueckwaerts.py', 'rueckwaerts'),
                               ('ausgaben.py', 'ausgaben'),
                               ('parallelen.py', 'parallelen'),
                               ('hints.py', 'hints')):
            lauf([werkzeug, str(nr), kap],
                 os.path.join(vorb, f'{name}_{nr}_{kap}.md'))

        prompt = baustein(nr, kap, buch, a.scratch, kaps)
        eigene = [h.split(':', 1)[1].strip() for h in a.hinweis
                  if h.split(':', 1)[0].strip() == str(kap)]
        prompt += f'''

---

## Deine Vorbereitung — alles gemessen, nichts behauptet

Die Dateien liegen in `{vorb}/`:

    rueckwaerts_{nr}_{kap}.md   was der Bestand zu jedem Wort deines
                            Kapitels fuehrt, vers fuer vers, vier Schichten
    ausgaben_{nr}_{kap}.md      die vier Zeugen neben deinem Vers
    parallelen_{nr}_{kap}.md    wo derselbe Wortlaut schon annotiert
                            im {sprache} Bestand steht
    hints_{nr}_{kap}.md         unbelegte Formen, Kollisionen im Vers
    bindungen_{nr}_p{marke}.md  die Wortfolgen dieses Pakets
    kapitelgrenzen_{nr}.md      die Verszaehlung aller Zeugen

**Lies `bindungen_{nr}_p{marke}.md` zuerst.** Es trennt, was dein Paket
**praegt** (der frueheste Ort der Folge liegt hier — was du setzt, gilt
fuer das ganze Buch) von dem, was es **uebernimmt** (die Reihe steht
schon, gemessen, nicht erinnert). Im Paket selbst wird zeichengleich
gesetzt: sprich dich ueber die Folgen ab, die in mehreren Kapiteln des
Pakets stehen — dein Bericht nennt sie ausdruecklich.

Danach `parallelen_{nr}_{kap}.md`: **das ist die staerkste Bindung, die
es gibt** — nicht ein Wort, sondern derselbe Wortlaut, schon annotiert.
Wo ein Block dort steht, wird er zeichengleich uebernommen; gemessen
wird er mit `folgenreihe.py "<der Block>"`, der die Glossen des Bestands
zu genau dieser Folge zeigt. Weicht dein Vers vom Parallelvers ab, gilt
**dein** Vers — die Parallele ist eine Vorlage, kein Gleichheitszeichen.

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
