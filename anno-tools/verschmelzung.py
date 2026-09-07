#!/usr/bin/env python3
"""Traegt die verschmolzene Praeposition ihren Artikel?

    verschmelzung.py [<buchNr> ...]
    verschmelzung.py --datei <pfad> <buchNr> <kapitel>

## Der Anlass

`nella` ist EIN Token und traegt zwei Woerter: die Praeposition `in` und
den Artikel `la`. Faellt der Artikel in der Glosse weg, steht dort
dasselbe wie bei der blossen Form `in` — und der Leser sieht den
Unterschied nicht mehr, den der italienische Text macht.

`glosskollision.py` findet das nicht. Es gruppiert nach LEMMA, und
`su` und `sulla` stehen beide auf `su`; die beiden Eintraege fallen dort
in denselben Topf, statt gegeneinander gemessen zu werden. Der Agent fuer
Matteo 7 hat es an 7,25 gefunden und als Reihe 68.3 vermerkt: dieselbe
Pruefung von der anderen Seite.

## Zwei Abschnitte, verschieden scharf

**A — im selben Vers.** Verschmolzene und blosse Form desselben Lemmas
stehen im selben Vers und tragen in mindestens zwei Sprachen dieselbe
Glosse. Das ist der scharfe Befund: der Text unterscheidet, die Glosse
nicht.

Zwei Stellungen sind ausgenommen, weil dort keine Zielsprache den
Artikel setzen kann: vor dem **Possessiv** (Reihe 22, `dei suoi
fratelli`) und vor dem **Eigennamen** (`dalla Galilea`). Ohne diese
beiden Ausnahmen meldet der erste Lauf ueber Matteo 1-9 vierzehn
Stellen, und alle vierzehn sind richtig.

**B — Glosse ohne Artikel.** Eine verschmolzene Form, deren Glosse in
einer Sprache keinen Artikel enthaelt. Das ist eine VERDACHTSLISTE, kein
Befund: die Nullantwort ist oft richtig. `figliuoli dei re` heisst
deutsch „Soehne von Koenigen" ohne Artikel; vor dem Possessiv faellt er
nach Reihe 22 ohnehin weg; und im Englischen steht bei Stoffnamen und
Abstrakta kein Artikel. Erwartbar sind hier dreistellige Zahlen — der
Abschnitt lohnt nur, wenn man eine bestimmte Form nachsieht.

Als Artikel zaehlt auch die Verschmelzung der ZIELSPRACHE: `zur`, `im`,
`del`, `au`, `des` tragen ihn mit.
"""
import argparse
import collections
import json
import re
import sys

import common as C

# Die verschmolzenen Formen des Italienischen. Die apostrophierten
# (`dell'`, `nell'`, `all'`, `sull'`, `dall'`) stehen ohne Apostroph in
# der Liste und werden vor dem Vergleich abgeschnitten.
VERSCHMOLZEN = re.compile(
    r"^(al|allo|alla|all|ai|agli|alle"
    r"|del|dello|della|dell|dei|degli|delle"
    r"|dal|dallo|dalla|dall|dai|dagli|dalle"
    r"|nel|nello|nella|nell|nei|negli|nelle"
    r"|sul|sullo|sulla|sull|sui|sugli|sulle"
    r"|col|coi|pel|pei)$", re.I)

BLOSS = {'a', 'di', 'da', 'in', 'su', 'con', 'per'}

# Zwei Klassen, in denen die gleiche Glosse RICHTIG ist — beide beim
# ersten Lauf ueber Matteo 1-9 gefunden, wo sie alle 14 Treffer des
# Abschnitts A stellten und keiner davon ein Fehler war.
#
# **Vor dem Possessiv** faellt der Artikel in allen vier Zielsprachen
# weg (Reihe 22): `dei suoi fratelli` ist „von seinen Bruedern", nicht
# „von den seinen Bruedern". Die verschmolzene Form kann ihren Artikel
# gar nicht zeigen.
#
# **Vor dem Eigennamen** ebenso: `dalla Galilea` ist „aus Galilaea".
POSSESSIV = {'suo', 'sua', 'suoi', 'sue', 'mio', 'mia', 'miei', 'mie',
             'tuo', 'tua', 'tuoi', 'tue', 'nostro', 'nostra', 'nostri',
             'nostre', 'vostro', 'vostra', 'vostri', 'vostre', 'loro',
             'proprio', 'propria', 'propri', 'proprie'}

# `dalla quale`, `nel quale`, `ai quali` — das Relativpronomen traegt
# seinen Artikel selbst (`la quale` ist eine Einheit), und die
# Zielsprachen setzen `welcher`/`whom`/`laquelle` ohne zweiten.
RELATIV = {'quale', 'quali'}

ARTIKEL = {
    'de': re.compile(r"\b(der|die|das|dem|den|des"
                     r"|zum|zur|im|am|vom|beim|ins|ans|aufs|fuers|fürs"
                     r"|durchs|uebers|übers|unters|hinters|ums)\b", re.I),
    'en': re.compile(r"\bthe\b", re.I),
    'es': re.compile(r"\b(el|la|los|las|lo|del|al)\b", re.I),
    'fr': re.compile(r"\b(le|la|les|du|au|aux|des)\b|\bl['’]", re.I),
}


def _kapitel(nr, datei=None, kapitel=None):
    if datei:
        return C.anno_wie_datei(nr, kapitel, datei)['chapters']
    return C.load_anno(nr)['chapters']


def pruefe(buecher, datei=None, kapitel=None):
    imvers, ohnartikel = [], []
    for nr in buecher:
        try:
            d = _kapitel(nr, datei, kapitel)
        except Exception:
            continue
        for kap, vv in d.items():
            for v, ee in vv.items():
                einzel = [e for e in ee if not C.is_multi(e)]
                verschm = [e for e in einzel
                           if VERSCHMOLZEN.match((e.get('form') or '')
                                                 .rstrip("'’"))]
                blosse = [e for e in einzel
                          if (e.get('form') or '').lower() in BLOSS]
                nach = {e['pos']: e for e in einzel}
                ueberspannt = set()
                for m in ee:
                    if 'pos_end' in m:
                        ueberspannt.update(range(m['pos'], m['pos_end'] + 1))
                    elif 'parts' in m:
                        ueberspannt.update(m['parts'])
                for a in verschm:
                    folgt = nach.get(a['pos'] + 1)
                    ff = (folgt.get('form') or '') if folgt else ''
                    # Possessiv oder Eigenname: der Artikel kann in
                    # keiner Zielsprache stehen, die Gleichheit ist echt.
                    if (ff.lower() in POSSESSIV or ff.lower() in RELATIV
                            or ff[:1].isupper()):
                        continue
                    # Steht die Form unter einem Mehrwort, glossiert
                    # dieses den Ausdruck: `al di là` ist „jenseits",
                    # und das `an` des Einzeleintrags traegt dort gar
                    # keinen Artikel mehr. (Matteo 4,15)
                    if a['pos'] in ueberspannt:
                        continue
                    for b in blosse:
                        if a.get('lemma') != b.get('lemma'):
                            continue
                        gleich = [l for l in C.LANGS
                                  if a.get(l)
                                  and (a[l] or '').lower()
                                  == (b.get(l) or '').lower()]
                        if len(gleich) >= 2:
                            imvers.append((nr, kap, v, a, b, gleich))
                    fehlt = [l for l in C.LANGS
                             if not ARTIKEL.get(l, re.compile(r'$^'))
                             .search(a.get(l) or '')]
                    if fehlt:
                        ohnartikel.append((nr, kap, v, a, fehlt))
    return imvers, ohnartikel


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buecher', nargs='*', type=int)
    p.add_argument('--datei', help='eine Kapitel-Lieferdatei statt der '
                                   'gebauten Anno-Datei: '
                                   '--datei <pfad> <nr> <kap>')
    p.add_argument('--verdacht', action='store_true',
                   help='Abschnitt B ausschreiben statt nur zaehlen')
    a = p.parse_args()
    if a.datei:
        if len(a.buecher) != 2:
            p.error('mit --datei: <buchNr> <kapitel>')
        nr, kap = a.buecher
        buecher = [nr]
        imvers, ohne = pruefe(buecher, a.datei, kap)
        print(f'gelesen: {a.datei} — Buch {nr}, Kapitel {kap}\n')
    else:
        buecher = a.buecher or sorted(C.anno_books())
        imvers, ohne = pruefe(buecher)

    print('## A — verschmolzen und bloss im selben Vers, gleiche Glosse\n')
    for nr, kap, v, x, y, gleich in imvers:
        print(f'  {C.book_name(nr)} {kap},{v}  {x["form"]}/{y["form"]} '
              f'(Lemma {x.get("lemma")}) gleich in {"+".join(gleich)}: '
              + ' · '.join(f'{l} {x.get(l)}' for l in gleich))
    if not imvers:
        print('  keine.')

    zahl = collections.Counter()
    for nr, kap, v, x, fehlt in ohne:
        for l in fehlt:
            zahl[l] += 1
    print(f'\n## B — Verdacht: Glosse ohne Artikel  '
          + ' · '.join(f'{l} {zahl[l]}' for l in C.LANGS) + '\n')
    if a.verdacht:
        for nr, kap, v, x, fehlt in ohne:
            print(f'  {C.book_name(nr)} {kap},{v}  {x["form"]:10} '
                  + ' · '.join(f'{l} {x.get(l)!r}' for l in fehlt))
    else:
        print('  mit --verdacht ausschreiben. Die Nullantwort ist hier oft')
        print('  richtig — der Abschnitt lohnt nur fuer eine bestimmte Form.')

    print(f'\n{len(imvers)} Befunde in Abschnitt A. Jeder ist zu pruefen: '
          f'wo die Zielsprache\nden Artikel nicht setzen kann, sind die '
          f'beiden Glossen zu Recht gleich.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
