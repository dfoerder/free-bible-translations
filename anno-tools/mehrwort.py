"""Einzelwörter, die die Glosse ihres Mehrwort-Eintrags übernommen haben.

    mehrwort.py <buchNr …> | alle [--nur=Form,Form] [--fix]

**`--fix` gehört immer mit `--nur`.** Ein pauschaler Lauf korrigiert auch, was
richtig ist: `Ufer` in Josua 3,15 ist im Deutschen wirklich Plural („trat über
seine Ufer"), und `das Rechte` in 1. Johannes 2,29 ist ein anderes Wort als die
`Rechte` im Sinne von Rechtsansprüchen. Erst den Bericht lesen, die Formen
prüfen, dann gezielt ziehen.

Ein Mehrwort-Eintrag überdeckt Positionen, an denen auch Einzelwort-Einträge
liegen. Die idiomatische Glosse der Wendung passt dort oft **nicht**: der
französische Ausdruck `livrer entre les mains` steht im Plural, das deutsche
`Hand` daneben im Singular. Wer die Wendung zuerst schreibt und dann die
Einzelwörter, greift beim Einzelwort in die fertige Wendung — und der Lesefluss
zeigt an einem Singularwort einen Plural.

Vier belegte Fälle: Esra 5,12 (`Hand`, fr), Nehemia 9,27 und 9,30 (`Hand`, fr),
Nehemia 9,29 (`Rücken`, it). Gefunden wurden sie alle drei Mal nur zufällig —
`ausreisser.py` schlägt an, wenn drei Sprachen sich einig sind und die vierte
abweicht, aber wenn **zwei** Sprachen die Wendung übernehmen, sieht es das
nicht. `selfcheck.py` und `qa.py` sehen es prinzipiell nicht: strukturell ist
beides korrekt.

Gesucht wird deshalb gezielt: ein **Inhaltswort** unter einem Mehrwort-Eintrag,
dessen Glosse wörtlich in der Glosse der Wendung vorkommt und zugleich eine
**Flexionsvariante** der Korpusmehrheit für diese Wortform ist — gleicher
Stamm, andere Endung. Das ist die Signatur des Griffs in die Wendung.

Ohne diese beiden Einschränkungen ist der Bericht unbrauchbar: die erste
Fassung meldete **18 335** Stellen, fast alles Artikel und Präpositionen, deren
Zielsprachenform legitim nach Genus und Kasus wechselt.

Jeder Treffer ist ein **Verdacht**. Es gibt legitime Fälle: wo die Wendung
selbst das Wort im richtigen Numerus enthält, ist die Übereinstimmung kein
Fehler, sondern das Erwartete.
"""
import collections
import re
import sys

import hints
import qa
import common as C

FUNK = hints.FUNKTION | qa.FUNKTIONSWOERTER
MIN_STAMM = 4


def mehrheit(idx):
    return idx.most_common(1)[0] if idx else (None, 0)


def enthaelt(wendung, wort):
    """Steht `wort` als **ganzes Wort** in `wendung`?

    Die erste Fassung prüfte auf Teilzeichenketten und verwarf dadurch genau
    die Fälle, für die das Skript gebaut ist: `main` ist eine Teilzeichenkette
    von `mains`, also galt die Mehrheitsform als in der Wendung enthalten und
    der Treffer fiel weg. Die Gegenprobe an drei künstlich wiederhergestellten
    Fehlern hat das aufgedeckt — das Skript meldete null.
    """
    return re.search(r'(?<!\w)' + re.escape(wort) + r'(?!\w)', wendung, re.I) is not None


def flexionsvariante(a, b):
    """Zwei Glossen desselben Wortes in verschiedener Form — `main`/`mains`,
    `schiena`/`spalle` nicht. Genau das ist die gesuchte Signatur: das
    Einzelwort steht im Numerus der Wendung statt im eigenen."""
    a, b = a.lower(), b.lower()
    if a == b or ' ' in a or ' ' in b:
        return False
    n = min(len(a), len(b))
    if n < MIN_STAMM:
        return False
    return a[:MIN_STAMM] == b[:MIN_STAMM] and abs(len(a) - len(b)) <= 3


fix = '--fix' in sys.argv
nur = None
datei = kapitel = None
argv = []
_it = iter(range(len(sys.argv[1:])))
for a in sys.argv[1:]:
    if a == '--fix':
        continue
    if a.startswith('--datei='):
        datei = a[8:]
        continue
    if a.startswith('--kapitel='):
        kapitel = a[10:]
        continue
    if a.startswith('--nur='):
        nur = {x.strip() for x in a[6:].split(',')}
        continue
    argv.append(a)
buecher = C.anno_books() if (not argv or argv[0] == 'alle') else [int(a) for a in argv]

# Korpusmehrheit je (Wortform, Feld) über den gesamten Bestand
korpus = collections.defaultdict(collections.Counter)
for nr, kap, v, e in C.iter_corpus():
    if C.is_multi(e):
        continue
    for f in C.LANGS:
        korpus[(e['form'], f)][e[f]] += 1

treffer = 0
if datei and (len(buecher) != 1 or not kapitel):
    raise SystemExit('mit --datei= sind genau eine Buchnummer und '
                     '--kapitel=<nr> noetig.')
for nr in buecher:
    d = (C.anno_wie_datei(nr, kapitel, datei) if datei
         else C.load_anno(nr, cache=False))
    geaendert = set()
    for kap, verse in d['chapters'].items():
        for v, ee in verse.items():
            multis = [e for e in ee if C.is_multi(e)]
            if not multis:
                continue
            einzel = {e['pos']: e for e in ee if not C.is_multi(e)}
            for m in multis:
                for p in C.covered(m):
                    e = einzel.get(p)
                    if not e:
                        continue
                    # Nur Substantive: bei Verben und Adjektiven ist die Form
                    # der Wendung meist die richtige (reflexive Verben, Numerus
                    # aus dem Kontext), und die echten Fälle ersaufen im Rauschen.
                    # Der Nomenanker ist die DEUTSCHE Seite: in
                    # deu/l1912mod die Form, sonst die de-Spalte.
                    if not C.de_wort(e)[:1].isupper():
                        continue
                    if nur is not None and e['form'] not in nur:
                        continue
                    if e['form'].lower() in FUNK or e['lemma'].lower() in FUNK:
                        continue
                    for f in C.LANGS:
                        wort, wendung = e[f], m[f]
                        if wort == wendung or not enthaelt(wendung, wort):
                            continue
                        top, n = mehrheit(korpus[(e['form'], f)])
                        gesamt = sum(korpus[(e['form'], f)].values())
                        if top is None or top == wort or n < 5:
                            continue
                        # Nur wo die Wortform im Bestand fast immer dieselbe
                        # Zielform trägt — sonst ist die deutsche Form selbst
                        # numerusmehrdeutig (`Propheten` ist Singular UND Plural)
                        # und die Mehrheit sagt nichts über diesen Vers.
                        if n / gesamt < 0.85:
                            continue
                        if not flexionsvariante(wort, top):
                            continue
                        # Nur melden, wenn die Mehrheit NICHT in der Wendung steckt:
                        # sonst hätte die Wendung das Wort ohnehin so gebraucht.
                        if enthaelt(wendung, top):
                            continue
                        treffer += 1
                        print(f'  {C.book_name(nr)} {kap},{v} pos {p}  {e["form"]!r} {f}: '
                              f'{wort!r} {"->" if fix else "steckt in"} der Wendung {m["form"]!r} '
                              f'({wendung!r}) — Bestandsmehrheit {top!r} ({n} Belege)')
                        if fix:
                            e[f] = top
                            geaendert.add(kap)

    # In **beides** schreiben: gebaute Datei und Kapitelquelle. Ohne die Quelle
    # ist jede Korrektur beim naechsten Build wieder weg.
    if fix and geaendert:
        C.write_compact(C.anno_path(nr), d)
        for kap in sorted(geaendert, key=int):
            q = C.load_quelle(nr, kap)
            if q is None:
                print(f'  ! {C.book_name(nr)} {kap}: keine Kapitelquelle — '
                      f'die Korrektur ist beim naechsten Build wieder weg')
                continue
            for v, ee in d['chapters'][kap].items():
                for e in ee:
                    if C.is_multi(e):
                        continue
                    for qe in q.get(v, []):
                        if qe.get('pos') == e['pos'] and not C.is_multi(qe):
                            for f in C.LANGS:
                                qe[f] = e[f]
            C.write_quelle(nr, kap, q)

print(f'\n{treffer} Verdachtsfälle' + (' — korrigiert, in Anno-Datei und Quelle.' if fix else
      '. Jeder ist am Vers zu prüfen: wo die Wendung das Wort im richtigen '
      'Numerus enthält, ist die Übereinstimmung richtig.'))
