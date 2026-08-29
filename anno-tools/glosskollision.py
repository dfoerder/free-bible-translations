"""Zwei deutsche Wörter im selben Vers, die dieselbe Glosse tragen.

    glosskollision.py <buchNr …> | alle [--kapitel <kap>]
    glosskollision.py --datei <buchNr> <kapitel> <datei.json>

Das Gegenstück zu `hints.py` Abschnitt 2. **`hints.py` sucht im Quelltext**:
es nimmt zwei deutsche Wortformen, schlägt beide im Bestand nach und meldet,
wenn dort dieselbe Glosse steht. Das findet nur, was der Bestand schon kennt —
und es findet gar nichts, wenn eine der beiden Formen unbelegt ist oder wenn
die Kollision erst durch die Entscheidung des schreibenden Agenten entsteht.

**Dieses Werkzeug sucht im fertigen Kapitel**: es vergleicht die tatsächlich
gesetzten Glossen Vers für Vers und Sprache für Sprache. Damit sieht es die
Kollision, die `hints.py` prinzipiell nicht sehen kann.

Der Anlass waren fünf Fälle aus vier Psalter-Paketen, die `hints.py` alle
nicht gemeldet hat — für zwei der Kapitel meldete es sogar null Paare:

    Ps 81,2   `Jauchzt … zu` / `jubelt … zu`   (alle vier)
    Ps 84,9   `höre` / `vernimm`               (nur es: *oye*)
    Ps 84,10  `schau` / `blick`                (alle vier)
    Ps 88,18  `umgeben` / `umringen`           (alle vier)
    Ps 90,11  `er` / `es`                      (nur en: *it*)

Gefunden hat sie jedes Mal ein Agent von Hand.

## Die Rangfolge

Entscheidend ist, **in wie vielen Sprachen** die beiden zusammenfallen:

- **1 von 4** — der stärkste Verdacht. Drei Sprachen unterscheiden die Wörter,
  die vierte nicht: dann ist die Trennung möglich und fehlt nur hier.
  (`Freundlichkeit`/`Güte` sind romanisch sauber getrennt und englisch beide
  *kindness*; `er`/`es` sind es/fr/it getrennt und englisch beide *it*.)
- **2–3 von 4** — ansehen.
- **4 von 4** — meist harmlos: entweder sind die Wörter wirklich synonym, oder
  die Zielsprachen haben die Unterscheidung schlicht nicht.

Geschlossene Wortarten (Artikel, Präpositionen, Pronomen, Konjunktionen)
verschmelzen in den Zielsprachen dauernd, ohne dass etwas verloren geht —
`des`/`von` sind spanisch beide *de*, `an`/`zu` beide *a*. Sie stehen deshalb
in einem eigenen Abschnitt am Ende, den `--nurinhalt` unterdrückt. **Aber nicht
ausschließen:** `er`/`es` war genau so ein Paar und ein echter Fehler.

Wie jedes Prüfskript hier meldet es **Verdacht, keine Fehler**. Und wie überall
gilt die Regel aus Hiob: aufgelöst wird **nur im Kollisionsvers**.
"""
import argparse
import collections
import json
import sys

import common as C

# Geschlossene Wortarten. Bewusst knapp gehalten — je länger die Liste, desto
# mehr echte Fälle verschwinden im unterdrückten Abschnitt.
FUNKTION = {
    'der', 'ein', 'dieser', 'jener', 'welcher', 'all', 'kein',
    'ich', 'du', 'er', 'sie', 'es', 'wir', 'ihr', 'man', 'sich', 'wer', 'was',
    'mein', 'dein', 'sein', 'unser', 'euer', 'ihrer',
    'in', 'an', 'auf', 'zu', 'von', 'mit', 'bei', 'nach', 'aus', 'über',
    'unter', 'vor', 'für', 'um', 'durch', 'gegen', 'ohne', 'seit', 'bis',
    # Verschmelzungen aus Praeposition und Artikel. Sie tragen kein eigenes
    # Wort, sondern Praeposition + Artikel, und fallen in den Zielsprachen
    # staendig zusammen (`am`/`im` sind spanisch beide *en el*). Ohne sie in
    # der Liste bestand der Bericht fast nur aus ihnen.
    'am', 'im', 'ins', 'zum', 'zur', 'vom', 'beim', 'ans', 'aufs', 'fürs',
    'durchs', 'ums', 'vors', 'übers', 'unterm',
    'und', 'oder', 'aber', 'denn', 'dass', 'wenn', 'weil', 'als', 'wie',
    'da', 'so', 'auch', 'nicht', 'nur', 'noch', 'schon', 'ja', 'nein',
    'doch', 'weder', 'sondern', 'zwar', 'etwa', 'sehr', 'dort', 'hier',
    'sein_verb', 'haben', 'werden', 'wollen', 'sollen', 'müssen', 'können',
    # `lassen` steht in den Zielsprachen staendig fuer das blosse Hilfsverb
    # einer Umschreibung und faellt dann mit `haben`/`sein` zusammen
    # (`hat`/`laesst` sind englisch beide *has*).
    'lassen', 'selbst',
    # Richtungspartikeln trennbarer Verben. Sie tragen die Richtung, die die
    # Zielsprache schon im Verb hat, und fallen deshalb mit der blossen
    # Praeposition zusammen (`auf`/`hinauf` sind italienisch beide *su*).
    'hinein', 'hinauf', 'hinab', 'hinaus', 'hinunter', 'hinüber', 'hin',
    'herein', 'herauf', 'herab', 'heraus', 'herunter', 'herüber', 'her',
    'empor', 'dahin', 'davon', 'daran', 'darauf', 'darin', 'dazu', 'dagegen',
    'weg', 'fort', 'zurück', 'vorbei', 'nieder', 'umher',
}

SPRACHEN = ('en', 'es', 'fr', 'it')


def _norm(g):
    """Vergleichsschlüssel einer Glosse: klein, ohne Rand-Satzzeichen.

    **Akzente bleiben stehen.** `common.norm_key` entfernt sie, und damit fielen
    italienisch `e` (und) und `è` (ist) zusammen — vier erfundene Kollisionen
    im ersten Lauf. In den Zielsprachen trägt der Akzent Bedeutung.
    """
    if not g:
        return None
    k = g.strip().lower().strip('.,;:!?¡¿"\'’“”()[]…-–—')
    return k or None


def kollisionen_im_vers(entries):
    """Alle Paare (lemmaA, lemmaB) mit gemeinsamer Glosse, je Sprache.

    Nur Einzelworteinträge: bei Mehrwortwendungen ist eine geteilte Glosse
    keine Kollision, sondern die Wendung selbst.
    """
    treffer = collections.defaultdict(set)   # (lemA, lemB) -> {sprachen}
    nurschreibung = collections.defaultdict(set)  # nur Gross-/Kleinschreibung
    formen = {}                              # lemma -> gesehene Form
    glossen = collections.defaultdict(dict)  # (lemma, sprache) -> glosse
    for sprache in SPRACHEN:
        nach_gloss = collections.defaultdict(set)
        for e in C.singles(entries):
            lem = e.get('lemma')
            if not lem:
                continue
            k = _norm(e.get(sprache))
            if not k:
                continue
            nach_gloss[k].add(lem)
            formen.setdefault(lem, e.get('form') or lem)
            glossen[(lem, sprache)] = e.get(sprache)
        for k, lemmas in nach_gloss.items():
            if len(lemmas) < 2:
                continue
            ls = sorted(lemmas)
            for i in range(len(ls)):
                for j in range(i + 1, len(ls)):
                    a, b = ls[i], ls[j]
                    ga, gb = glossen.get((a, sprache)), glossen.get((b, sprache))
                    # Unterscheiden sich die Glossen NUR in der Schreibung, ist
                    # das im Psalter die gewollte Konvention: `HERR` -> LORD,
                    # `Herr` -> Lord. Der Leser sieht den Unterschied.
                    if ga != gb:
                        nurschreibung[(a, b)].add(sprache)
                    else:
                        treffer[(a, b)].add(sprache)
    return treffer, nurschreibung, formen, glossen


def _ist_funktionspaar(a, b):
    return a.lower() in FUNKTION and b.lower() in FUNKTION


def pruefe(kapitel_daten, nr, kap):
    """kapitel_daten: {vers: [eintraege]} -> Liste von Befunden."""
    out = []
    for vers in sorted(kapitel_daten, key=lambda v: int(v) if v.isdigit() else 0):
        treffer, nurschr, formen, glossen = kollisionen_im_vers(kapitel_daten[vers])
        for (a, b), sprachen in list(treffer.items()) + [
                (k, v) for k, v in nurschr.items() if k not in treffer]:
            nur_schreibung = (a, b) not in treffer
            out.append({
                'nr': nr, 'kap': str(kap), 'vers': vers,
                'a': a, 'b': b,
                'forma': formen.get(a, a), 'formb': formen.get(b, b),
                'sprachen': sorted(sprachen, key=SPRACHEN.index),
                'glossen': {s: glossen.get((a, s)) for s in sorted(sprachen, key=SPRACHEN.index)},
                'funktion': _ist_funktionspaar(a, b),
                'nur_schreibung': nur_schreibung,
            })
    return out


def _zeile(f):
    sp = '/'.join(f['sprachen'])
    g = ' · '.join(f'{s}: {f["glossen"][s]!r}' for s in f['sprachen'])
    return (f'  {C.book_name(f["nr"])} {f["kap"]},{f["vers"]}: '
            f'`{f["forma"]}` / `{f["formb"]}` — {len(f["sprachen"])} von 4 ({sp})  {g}')


def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument('args', nargs='+')
    p.add_argument('--kapitel', default=None)
    p.add_argument('--datei', action='store_true',
                   help='<buchNr> <kapitel> <datei.json> — Kapitelquelle statt gebautem Buch')
    p.add_argument('--nurinhalt', action='store_true',
                   help='Paare aus geschlossenen Wortarten ganz weglassen')
    a = p.parse_args()

    befunde = []
    if a.datei:
        nr, kap, pfad = int(a.args[0]), int(a.args[1]), a.args[2]
        with open(pfad, encoding='utf-8') as fh:
            befunde = pruefe(json.load(fh), nr, kap)
    else:
        buecher = C.anno_books() if a.args[0] == 'alle' else [int(x) for x in a.args]
        for nr in buecher:
            d = C.load_anno(nr)
            for kap, verses in d['chapters'].items():
                if a.kapitel is not None and str(kap) != str(a.kapitel):
                    continue
                befunde += pruefe(verses, nr, kap)

    schreibung = [f for f in befunde if f['nur_schreibung']]
    rest = [f for f in befunde if not f['nur_schreibung']]
    inhalt = [f for f in rest if not f['funktion']]
    funktion = [f for f in rest if f['funktion']]

    for stufe in (1, 2, 3, 4):
        teil = [f for f in inhalt if len(f['sprachen']) == stufe]
        if not teil:
            continue
        kopf = {1: 'nur EINE Sprache faellt zusammen — staerkster Verdacht',
                2: 'zwei Sprachen', 3: 'drei Sprachen',
                4: 'alle vier — meist wirklich synonym'}[stufe]
        print(f'\n## {stufe} von 4 — {kopf}  ({len(teil)})')
        for f in sorted(teil, key=lambda f: (f['nr'], int(f['kap']), int(f['vers']))):
            print(_zeile(f))

    if funktion and not a.nurinhalt:
        print(f'\n## geschlossene Wortarten — meist unvermeidlich  ({len(funktion)})')
        for f in sorted(funktion, key=lambda f: (len(f['sprachen']), f['nr']))[:40]:
            print(_zeile(f))
        if len(funktion) > 40:
            print(f'  … {len(funktion) - 40} weitere (--nurinhalt blendet den Abschnitt aus)')

    if schreibung:
        print(f'\n## nur Gross-/Kleinschreibung — im Psalter die Konvention  '
              f'({len(schreibung)}, nicht mitgezaehlt)')
        for f in sorted(schreibung, key=lambda f: (f['nr'], int(f['kap'])))[:10]:
            print(_zeile(f))
        if len(schreibung) > 10:
            print(f'  … {len(schreibung) - 10} weitere')

    n1 = len([f for f in inhalt if len(f['sprachen']) == 1])
    print(f'\n{len(inhalt)} inhaltliche Paare, davon {n1} in nur einer Sprache · '
          f'{len(funktion)} aus geschlossenen Wortarten.')
    print('Verdacht, kein Fehler: jeden Treffer am Vers ansehen. Aufgeloest wird '
          'nur im Kollisionsvers.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
