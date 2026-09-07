#!/usr/bin/env python3
"""Eine Glosse in einer Kapitelquelle aendern — an EINER Position.

    setzen.py <buchNr> <kap> <vers> <pos> <erwarteteForm> feld=wert [feld=wert …]
    setzen.py … --grund "warum"

## Der Anlass

Beim Einsammeln von Matthaeus Paket 1 wollte ich in 1,22 das relative
`que` angleichen und habe **nach Wortform** ersetzt. Im Vers stehen zwei
`que` — die Konjunktion in `pour que` und das Relativum in `ce que`. Es
traf beide, und `folgencheck.py` hat es im naechsten Lauf gemeldet.

In Paket 2 derselbe Fehler noch einmal: `le` in „je vous le dis" traf
auch das `le` in „comme le font", `vous` in „Je vous le dis" auch das
Subjekt in „Lorsque vous priez".

Zweimal derselbe Griff. Deshalb dieses Werkzeug: es aendert **nur eine
Position**, und es verlangt die **erwartete Oberflaechenform** als
Argument — stimmt sie nicht, passiert nichts. Genau die Vorsichts-
massnahme, die `PROMPT_BAUSTEIN.md` den Agenten fuer Mehrwoerter
vorschreibt; sie gilt fuer den Koordinator genauso.

## Was es nicht tut

Es aendert Einzelwort-Eintraege. Mehrwoerter (mit `pos_end` oder
`parts`) laesst es stehen — die haben ihre eigene Kopfposition und
werden von Hand oder mit `remap.py` bearbeitet.
"""
import argparse
import json
import os
import sys

import common as C


def setze(nr, kap, vers, pos, form, felder, grund=None, trocken=False,
          aus_out=False):
    """`aus_out` schreibt in $ANNO_OUT statt in die Kapitelquellen.

    Ein Agent arbeitet in `$ANNO_OUT`, der Koordinator in
    `anno-quellen/`. Die erste Fassung kannte nur den zweiten Ort und
    meldete dem Agenten fuer Matthaeus 10 „gibt es nicht" — wer das fuer
    erledigt haelt, korrigiert nichts.
    """
    if aus_out:
        out = os.environ.get('ANNO_OUT')
        if not out:
            raise SystemExit('ANNO_OUT ist nicht gesetzt.')
        p = os.path.join(out, str(nr), f'ch{kap}.json')
    else:
        p = os.path.join(C.QUELLEN, str(nr), f'ch{kap}.json')
    if not os.path.exists(p):
        andere = (os.path.join(C.QUELLEN, str(nr), f'ch{kap}.json') if aus_out
                  else os.path.join(os.environ.get('ANNO_OUT', '?'),
                                    str(nr), f'ch{kap}.json'))
        hinweis = (f'\nSie liegt aber in {andere} — dann '
                   + ('ohne' if aus_out else 'mit') + ' --out arbeiten.'
                   ) if os.path.exists(andere) else ''
        raise SystemExit(f'{p} gibt es nicht.{hinweis}')
    d = json.load(open(p, encoding='utf-8'))
    if str(vers) not in d:
        raise SystemExit(f'Vers {vers} steht nicht in ch{kap}.json.')

    treffer = [e for e in d[str(vers)]
               if e['pos'] == pos and not C.is_multi(e)]
    if not treffer:
        raise SystemExit(f'{nr} {kap},{vers}: kein Einzelwort-Eintrag auf '
                         f'Position {pos}.')
    e = treffer[0]
    if C.strip_punct(e['form']) != C.strip_punct(form):
        raise SystemExit(f'{nr} {kap},{vers} pos {pos}: dort steht '
                         f'{e["form"]!r}, erwartet war {form!r}. '
                         'Nichts geaendert.')

    unbekannt = [f for f in felder
                 if f not in C.LANGS + ['lemma', 'level', 'form']]
    if unbekannt:
        raise SystemExit(f'Unbekannte Felder: {", ".join(unbekannt)}. '
                         f'Erlaubt: {", ".join(C.LANGS + ["lemma", "level"])}')

    alt = {f: e.get(f) for f in felder}
    if alt == felder:
        print(f'{nr} {kap},{vers} pos {pos} {e["form"]}: steht schon so.')
        return 0
    if not trocken:
        e.update(felder)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    marke = '(trocken) ' if trocken else ''
    print(f'{marke}{nr} {kap},{vers} pos {pos} {e["form"]}: '
          + ' · '.join(f'{f} {alt[f]!r} → {w!r}' for f, w in felder.items())
          + (f'   — {grund}' if grund else ''))
    return 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel')
    p.add_argument('vers')
    p.add_argument('pos', type=int)
    p.add_argument('form', help='die erwartete Oberflaechenform an dieser '
                                'Position — sie wird hart geprueft')
    p.add_argument('felder', nargs='+', help='feld=wert, z. B. en="to you"')
    p.add_argument('--grund')
    p.add_argument('--trocken', action='store_true')
    p.add_argument('--out', action='store_true',
                   help='in $ANNO_OUT arbeiten statt in den Kapitelquellen '
                        '— das ist der Ort, an dem ein Agent seine Abgabe hat')
    a = p.parse_args()

    felder = {}
    for x in a.felder:
        if '=' not in x:
            p.error(f'{x!r} ist kein feld=wert')
        f, w = x.split('=', 1)
        felder[f] = w
    ok = setze(a.buch, a.kapitel, a.vers, a.pos, a.form, felder,
               a.grund, a.trocken, a.out)
    # Die Aenderung steht in der KAPITELQUELLE. Jedes messende Werkzeug
    # liest die gebaute Anno-Datei — bis `buildbook.py` gelaufen ist,
    # misst es also den alten Stand. Ich bin heute selbst darauf
    # hereingefallen: nach vierzehn Lemma-Korrekturen meldete die
    # Gegenprobe alle vierzehn unveraendert.
    if ok >= 0 and not a.trocken and not a.out:
        print(f'   → noch nicht gebaut: python3 buildbook.py {a.buch}')
    sys.exit(0 if ok >= 0 else 1)


if __name__ == '__main__':
    main()
