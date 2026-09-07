"""Inhaltliche Qualitätssicherung (Ebene 2).

    qa.py <buchNr …> | alle
    qa.py --kapitel <buchNr> <kapitel> <datei.json>

Findet, was strukturell unauffällig ist: eine um eine Position verrutschte
Zuordnung ist strukturell perfekt und inhaltlich Unsinn. Die Heuristiken
melden Verdacht, keine Fehler — **bei einem Treffer erst die Stelle ansehen,
dann entscheiden, wer den Fehler hat.** Das Prüfskript kann selbst falsch
liegen (qa.py schlug bei Lukas 16,15 an, die Glosse war richtig).
"""
import argparse
import collections
import json
import re
import sys
import unicodedata

import common as C

# ---------------------------------------------------------------- Zeichenvorrat
ERLAUBT = {
    'de': set("abcdefghijklmnopqrstuvwxyz0123456789 '-.,…!?äöüß"),
    'en': set("abcdefghijklmnopqrstuvwxyz0123456789 '-.,…!?"),
    'es': set("abcdefghijklmnopqrstuvwxyz0123456789 '-.,…!?áéíóúüñ¿¡"),
    'fr': set("abcdefghijklmnopqrstuvwxyz0123456789 '-.,…!?àâçéèêëîïôùûüÿœæ"),
    'it': set("abcdefghijklmnopqrstuvwxyz0123456789 '-.,…!?àèéìíîòóùú"),
}
ZEICHEN_AUSNAHMEN = {'fiancée'}
# Der typografische Apostroph stand in keiner Zeichenliste — eine
# italienische Glosse `l’immoralità` waere als fremdes Zeichen
# gemeldet worden, die gerade Form `l'immoralità` nicht. Beide sind
# richtig geschrieben; die Pruefung soll die Rechtschreibung meinen,
# nicht die Anfuehrungszeichenwahl. Gemeldet vom Agenten des
# franzoesischen Pilotbuchs.
for _l in ERLAUBT:
    ERLAUBT[_l].add('\u2019')

# Die Funktionswoerter des QUELLTEXTES, nicht der Glossen. Welche Liste
# gilt, haengt daran, welche Ausgabe annotiert wird — die deutsche Liste
# trifft im franzoesischen Text nichts, und die Pruefung faellt dann
# lautlos aus statt zu melden, dass sie nichts geprueft hat.
FUNKTION_JE_SPRACHE = {
    'de': {
        'der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine', 'einen', 'einem',
        'eines', 'einer', 'und', 'oder', 'aber', 'von', 'zu', 'in', 'an', 'auf',
        'mit', 'bei', 'nach', 'aus', 'für', 'ist', 'sind', 'war', 'waren',
    },
    'fr': {
        'le', 'la', 'les', "l'", 'un', 'une', 'des', 'du', 'de', "d'",
        'et', 'ou', 'mais', 'donc', 'car', 'ni', 'à', 'au', 'aux', 'en',
        'dans', 'sur', 'sous', 'pour', 'par', 'avec', 'sans', 'ce', 'cet',
        'cette', 'ces', 'qui', 'que', "qu'", 'dont', 'où', 'ne', 'pas',
        'est', 'sont', 'était', 'étaient', 'se', 'y',
    },
    'en': {
        'the', 'a', 'an', 'and', 'or', 'but', 'of', 'to', 'in', 'on', 'at',
        'by', 'for', 'with', 'from', 'is', 'are', 'was', 'were', 'that',
        'which', 'who', 'not',
    },
    'es': {
        'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'de', 'del',
        'y', 'o', 'pero', 'a', 'al', 'en', 'con', 'sin', 'por', 'para',
        'que', 'quien', 'no', 'es', 'son', 'era', 'eran',
    },
    'it': {
        'il', 'lo', 'la', 'i', 'gli', 'le', "l'", 'un', 'uno', 'una',
        "un'", 'di', 'del', 'dello', 'della', 'dei', 'degli', 'delle',
        'a', 'al', 'allo', 'alla', 'ai', 'agli', 'alle', 'da', 'dal',
        'dalla', 'in', 'nel', 'nella', 'nei', 'nelle', 'con', 'su',
        'sul', 'sulla', 'per', 'tra', 'fra', 'e', 'ed', 'o', 'ma',
        'che', 'chi', 'non', 'si', 'ne', 'ci', 'vi',
        'è', 'sono', 'era', 'erano',
    },
}
FUNKTIONSWOERTER = FUNKTION_JE_SPRACHE.get(C.LANG, set())
# echte periphrastische Entsprechungen, die lang sein dürfen. Alle sechs sind
# im geprüften Bestand belegt und richtig — der Kanarienvogel soll auf Neues
# anschlagen, nicht auf diese.
LANG_ERLAUBT = (
    'de la part de', 'à la place', 'à la recherche', 'à partir de',
    'a lo largo de', 'ne … pas', "n'est pas",
)


def _norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def eigennamen(mindest=6):
    """Formen, deren Glossen im Bestand durchweg die Form selbst sind — der
    Kanarienvogel. Aus dem Bestand abgeleitet, nicht von Hand gepflegt."""
    treffer = collections.defaultdict(collections.Counter)
    for _, _, _, e in C.iter_corpus():
        if C.is_multi(e) or not e['form'][:1].isupper():
            continue
        treffer[e['form']]['n'] += 1
        gleich = all(_norm(e['form']).rstrip('s') in _norm(e[l]) for l in C.LANGS)
        if gleich:
            treffer[e['form']]['gleich'] += 1
    return {f: c['n'] for f, c in treffer.items()
            if c['n'] >= mindest and c['gleich'] / c['n'] >= 0.95}


def pruefe_verse(nr, kap, vers, text, entries, namen, befunde):
    ort = f'{nr}: {kap},{vers}'
    toks = C.tokens(text)
    einzel = sorted(C.singles(entries), key=lambda e: e['pos'])

    for e in entries:
        # Eigennamen-Kanarienvogel
        if not C.is_multi(e) and e['form'] in namen:
            erwartet = _norm(e['form']).rstrip('s')
            fehl = [l for l in C.LANGS if erwartet not in _norm(e[l])]
            if fehl:
                befunde.append(f'{ort} Eigenname {e["form"]!r} (pos {e["pos"]}): '
                               f'{", ".join(l + "=" + e[l] for l in fehl)}')
        # Funktionswort mit langer Glosse: „der"/„und"/„von" dürfen kein
        # mehrwortiges Inhaltswort bekommen. Drei Wörter sind noch normal
        # („il y avait", „to the one"), ab vier wird es verdächtig.
        if not C.is_multi(e) and e['form'].lower() in FUNKTIONSWOERTER:
            for l in C.LANGS:
                if (len(e[l].split()) >= 4
                        and not any(e[l].lower().startswith(p) for p in LANG_ERLAUBT)):
                    befunde.append(f'{ort} Funktionswort {e["form"]!r} (pos {e["pos"]}) '
                                   f'{l}={e[l]!r}')
        # fremdsprachige Zeichen
        for l in C.LANGS:
            if e[l].lower() in ZEICHEN_AUSNAHMEN:
                continue
            fremd = {c for c in _norm_keep(e[l]) if c not in ERLAUBT[l]}
            if fremd:
                befunde.append(f'{ort} pos {e["pos"]} {l}={e[l]!r}: '
                               f'fremde Zeichen {"".join(sorted(fremd))}')
        # Die alte qa.py prüfte hier zusätzlich „Mehrwort-Lemma in finiter Form"
        # (`ließen gehen` statt `gehen lassen`). Jede Fassung dieser Prüfung, die
        # sich nachbauen lässt, meldet über hundert richtige Zitierformen mit
        # (`einen Bund schließen`, `Kinder bekommen`, `nicht mehr`, `um zu`) —
        # das Signal geht im Rauschen unter. Die Regel steht in SPEC.md und wird
        # von den Agenten eingehalten; automatisch geprüft wird sie nicht mehr.

    # Wiederholungsläufe: drei oder mehr Positionen in Folge gleich
    for l in C.LANGS:
        lauf = 1
        for i in range(1, len(einzel)):
            # Gleiche Glosse ist nur dann verdaechtig, wenn *verschiedene*
            # deutsche Woerter sie tragen. Wiederholt der Text dasselbe Wort
            # (1Sam 3,10 'Samuel, Samuel! Samuel antwortete'), muss die Glosse
            # sich wiederholen - das ist kein Befund, sondern der Quelltext.
            gleich = (einzel[i][l] == einzel[i - 1][l]
                      and einzel[i]['pos'] == einzel[i - 1]['pos'] + 1
                      and einzel[i].get('lemma') != einzel[i - 1].get('lemma'))
            lauf = lauf + 1 if gleich else 1
            if lauf == 3:
                p = einzel[i - 2]['pos']
                befunde.append(f'{ort} {l}: dreimal in Folge {einzel[i][l]!r} '
                               f'ab pos {p} ({" ".join(toks[p:p+3])})')


def _norm_keep(s):
    return _norm(s)


def pruefe_buch(nr, namen, befunde):
    d = C.load_anno(nr)
    src = C.load_source(nr)['chapters']
    for kap, verses in d['chapters'].items():
        for vers, entries in verses.items():
            pruefe_verse(nr, kap, vers, src[kap][vers], entries, namen, befunde)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('args', nargs='*')
    p.add_argument('--kapitel', action='store_true')
    a = p.parse_args()

    namen = eigennamen()
    befunde = []
    if a.kapitel:
        if len(a.args) != 3:
            p.error('--kapitel braucht <buchNr> <kapitel> <datei.json> '
                    'in dieser Reihenfolge')
        nr, kap, pfad = int(a.args[0]), int(a.args[1]), a.args[2]
        with open(pfad, encoding='utf-8') as f:
            data = json.load(f)
        if 'chapters' in data:
            data = data['chapters'][str(kap)]
        src = C.load_source(nr)['chapters'][str(kap)]
        geprueft = 0
        for vers, entries in data.items():
            if vers in src:
                pruefe_verse(nr, kap, vers, src[vers], entries, namen, befunde)
                geprueft += 1
        # Ohne diese Zeile war eine Datei, deren Versschluessel nicht zum
        # Kapitel passen, von einer sauberen Datei nicht zu unterscheiden:
        # beide meldeten '0 Verdachtsfaelle'. Gemeldet vom Agenten fuer
        # Matthaeus 4.
        if geprueft != len(src):
            print(f'!! {geprueft} von {len(src)} Versen des Kapitels geprueft '
                  '— die Datei deckt das Kapitel nicht ab.')
    else:
        nrs = C.anno_books() if (not a.args or a.args[0] == 'alle') \
            else [int(x) for x in a.args]
        for nr in nrs:
            pruefe_buch(nr, namen, befunde)

    for b in befunde:
        print(b)
    print(f'\n{len(befunde)} Verdachtsfälle · Kanarienvogel kennt {len(namen)} Eigennamen')
    if len(namen) < 50:
        print('!! Der Eigennamen-Kanarienvogel wird aus dem BESTAND abgeleitet '
              'und kennt bei so wenig Bestand fast nichts — diese Probe sagt '
              'hier noch nichts aus.')
    return 1 if befunde else 0


if __name__ == '__main__':
    sys.exit(main())
