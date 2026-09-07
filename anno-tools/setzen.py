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

## Was es aendert

Einzelwort-Eintraege; mit `--mehrwort` die Reihe eines vorhandenen
Mehrworts; mit `--neu` legt es ein Mehrwort an, das noch fehlt:

    setzen.py 40 8 19 10 "partout où" --neu --bis 11 \\
        level=B1 de="überall wo" en=wherever es="dondequiera que" it=dovunque
    setzen.py 42 7 30 11 "se faire baptiser" --neu --teile 11,12,14 …

## Der Anlass fuer `--neu`

Beim Einsammeln von Lukas Paket 3 meldete der Agent fuer Kapitel 7,
dass Matthaeus 8,19 das Mehrwort `partout où` nicht traegt, das der
Bestand seit Marc 6,55 fuehrt. Zum Nachtragen gab es kein Werkzeug —
nur ein Wegwerfskript, und genau daran ist in Matthaeus schon zweimal
die falsche Stelle getroffen worden. `--neu` prueft darum jede
abgedeckte Position gegen den Quelltext, bevor es schreibt, und setzt
den Eintrag an die Stelle, an der der Bestand ihn erwartet: direkt
hinter das Einzelwort seiner Kopfposition.
"""
import argparse
import json
import os
import sys

import common as C


def pfad(nr, kap, aus_out):
    """`aus_out` waehlt $ANNO_OUT statt der Kapitelquellen."""
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
    return p


def setze(nr, kap, vers, pos, form, felder, grund=None, trocken=False,
          aus_out=False, mehrwort=False):
    """`aus_out` schreibt in $ANNO_OUT statt in die Kapitelquellen.

    Ein Agent arbeitet in `$ANNO_OUT`, der Koordinator in
    `anno-quellen/`. Die erste Fassung kannte nur den zweiten Ort und
    meldete dem Agenten fuer Matthaeus 10 „gibt es nicht" — wer das fuer
    erledigt haelt, korrigiert nichts.
    """
    p = pfad(nr, kap, aus_out)
    d = json.load(open(p, encoding='utf-8'))
    if str(vers) not in d:
        raise SystemExit(f'Vers {vers} steht nicht in ch{kap}.json.')

    # `--mehrwort` waehlt den MEHRWORT-Eintrag, der auf dieser Position
    # beginnt, und prueft statt der Oberflaechenform sein LEMMA. Ohne
    # das kam der Koordinator an eine Mehrwortreihe nur mit einem
    # Wegwerfskript heran — und genau dabei ist in Matthaeus zweimal die
    # falsche Stelle getroffen worden.
    if mehrwort:
        treffer = [e for e in d[str(vers)]
                   if C.is_multi(e) and e['pos'] == pos]
        if not treffer:
            raise SystemExit(f'{nr} {kap},{vers}: kein Mehrwort-Eintrag, der '
                             f'auf Position {pos} beginnt.')
        e = treffer[0]
        if e.get('lemma') != form:
            raise SystemExit(f'{nr} {kap},{vers} pos {pos}: dort steht das '
                             f'Mehrwort {e.get("lemma")!r}, erwartet war '
                             f'{form!r}. Nichts geaendert.')
    else:
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


def neues_mehrwort(nr, kap, vers, pos, lemma, felder, bis=None, teile=None,
                   grund=None, trocken=False, aus_out=False):
    """Ein Mehrwort anlegen, das es an dieser Stelle noch nicht gibt.

    Die Oberflaechenform wird nicht uebergeben, sondern aus dem
    Quelltext gebaut — so kann sie nicht von den Positionen abweichen,
    die der Eintrag beansprucht.
    """
    p = pfad(nr, kap, aus_out)
    d = json.load(open(p, encoding='utf-8'))
    if str(vers) not in d:
        raise SystemExit(f'Vers {vers} steht nicht in ch{kap}.json.')
    eintraege = d[str(vers)]

    if (bis is None) == (teile is None):
        raise SystemExit('--neu braucht genau eines von --bis und --teile.')
    stellen = list(range(pos, bis + 1)) if teile is None else list(teile)
    if stellen[0] != pos:
        raise SystemExit(f'Die erste Position in --teile ist {stellen[0]}, '
                         f'als Kopfposition steht aber {pos} da.')
    if len(stellen) < 2:
        raise SystemExit('Ein Mehrwort deckt mindestens zwei Positionen ab.')

    wort = C.tokens(C.load_source(nr)['chapters'][str(kap)][str(vers)])
    if stellen[-1] >= len(wort):
        raise SystemExit(f'Der Vers hat {len(wort)} Positionen (0–'
                         f'{len(wort) - 1}), verlangt ist bis {stellen[-1]}.')

    # Jede abgedeckte Position muss als Einzelwort dastehen — fehlt eine,
    # ist entweder die Spanne falsch oder der Vers nicht fertig annotiert.
    einzeln = {e['pos']: e for e in eintraege if not C.is_multi(e)}
    fehlt = [i for i in stellen if i not in einzeln]
    if fehlt:
        raise SystemExit(f'{nr} {kap},{vers}: kein Einzelwort-Eintrag auf '
                         f'Position(en) {", ".join(str(i) for i in fehlt)}.')

    schon = [e for e in eintraege
             if C.is_multi(e) and C.covered(e) == stellen]
    if schon:
        raise SystemExit(f'{nr} {kap},{vers}: ueber diese Spanne steht schon '
                         f'das Mehrwort {schon[0].get("lemma")!r}. Zum '
                         'Aendern --mehrwort statt --neu.')

    fehlend = [f for f in C.LANGS + ['level'] if f not in felder]
    if fehlend:
        raise SystemExit(f'Es fehlen: {", ".join(fehlend)}. Ein Mehrwort '
                         'ohne vollstaendige Reihe faellt jedem Pruefwerkzeug '
                         'auf.')

    # Die Oberflaeche kommt aus den EINZELEINTRAEGEN, nicht aus dem
    # Quelltext: der Bestand fuehrt sie ohne Satzzeichen. Die erste
    # Fassung baute sie aus `wort` und schrieb in Marc 12,3 ein
    # Mehrwort `les mains vides.` mit Punkt — die einzige Stelle, an
    # der die Spanne bis ans Versende reichte.
    e = {'pos': pos, 'form': ' '.join(einzeln[i]['form'] for i in stellen),
         'lemma': lemma, 'level': felder['level']}
    if teile is None:
        e['pos_end'] = bis
    else:
        e['parts'] = stellen
    for lang in C.LANGS:
        e[lang] = felder[lang]

    # Der Bestand setzt ein Mehrwort direkt hinter das Einzelwort seiner
    # Kopfposition (Marc 6,55: `se` · `se mit à` · `mit` · `à`).
    stelle = eintraege.index(einzeln[pos]) + 1
    while (stelle < len(eintraege) and C.is_multi(eintraege[stelle])
           and eintraege[stelle]['pos'] == pos
           and len(C.covered(eintraege[stelle])) > len(stellen)):
        stelle += 1
    if not trocken:
        eintraege.insert(stelle, e)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    marke = '(trocken) ' if trocken else ''
    spanne = f'{pos}-{bis}' if teile is None else str(stellen)
    print(f'{marke}{nr} {kap},{vers} {spanne} {e["form"]!r} NEU: {lemma} '
          f'{felder["level"]} · ' + ' · '.join(f'{l} {e[l]}' for l in C.LANGS)
          + (f'   — {grund}' if grund else ''))
    return 1


def loesche_mehrwort(nr, kap, vers, pos, lemma, grund=None, trocken=False,
                     aus_out=False):
    """Ein Mehrwort entfernen. Einzelwoerter bleiben unberuehrt.

    Das Gegenstueck zu `--neu`. Anlass: `tout ce que` stand an sechs
    Stellen als Dreier-Mehrwort und an dreissig als `tout` daneben
    plus `ce que`; die sechs mussten weg, und dafuer gab es nur den
    Weg ueber ein Skript.
    """
    p = pfad(nr, kap, aus_out)
    d = json.load(open(p, encoding='utf-8'))
    if str(vers) not in d:
        raise SystemExit(f'Vers {vers} steht nicht in ch{kap}.json.')
    treffer = [e for e in d[str(vers)] if C.is_multi(e) and e['pos'] == pos]
    if not treffer:
        raise SystemExit(f'{nr} {kap},{vers}: kein Mehrwort-Eintrag, der auf '
                         f'Position {pos} beginnt.')
    e = treffer[0]
    if e.get('lemma') != lemma:
        raise SystemExit(f'{nr} {kap},{vers} pos {pos}: dort steht das '
                         f'Mehrwort {e.get("lemma")!r}, erwartet war '
                         f'{lemma!r}. Nichts geloescht.')

    # Jede Position, die es abgedeckt hat, muss als Einzelwort dastehen
    # — sonst hinterlaesst das Loeschen eine Luecke, und `validate.py`
    # meldet sie erst nach dem Bauen.
    einzeln = {x['pos'] for x in d[str(vers)] if not C.is_multi(x)}
    fehlt = [i for i in C.covered(e) if i not in einzeln]
    if fehlt:
        raise SystemExit(f'{nr} {kap},{vers}: nach dem Loeschen stuenden die '
                         f'Positionen {", ".join(str(i) for i in fehlt)} ohne '
                         'Eintrag da. Erst die Einzelwoerter setzen.')
    if not trocken:
        d[str(vers)].remove(e)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    marke = '(trocken) ' if trocken else ''
    print(f'{marke}{nr} {kap},{vers} pos {pos} {e["form"]!r} GELOESCHT: '
          f'{lemma}' + (f'   — {grund}' if grund else ''))
    return 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel')
    p.add_argument('vers')
    p.add_argument('pos', type=int)
    p.add_argument('form', help='die erwartete Oberflaechenform an dieser '
                                'Position — sie wird hart geprueft; mit '
                                '--mehrwort stattdessen das Lemma')
    p.add_argument('felder', nargs='*', help='feld=wert, z. B. en="to you" '
                                           '— bei --loeschen keine')
    p.add_argument('--grund')
    p.add_argument('--trocken', action='store_true')
    p.add_argument('--mehrwort', action='store_true',
                   help='den MEHRWORT-Eintrag auf dieser Position aendern; '
                        '<form> ist dann sein LEMMA')
    p.add_argument('--neu', action='store_true',
                   help='ein Mehrwort ANLEGEN, das hier noch fehlt; <form> '
                        'ist sein LEMMA, die Spanne kommt aus --bis/--teile')
    p.add_argument('--bis', type=int, metavar='POS',
                   help='letzte Position eines zusammenhaengenden Mehrworts')
    p.add_argument('--teile', metavar='P,P,P',
                   help='die Positionen eines getrennten Mehrworts')
    p.add_argument('--loeschen', action='store_true',
                   help='das MEHRWORT auf dieser Position entfernen; <form> '
                        'ist sein LEMMA. Braucht keine Felder.')
    p.add_argument('--out', action='store_true',
                   help='in $ANNO_OUT arbeiten statt in den Kapitelquellen '
                        '— das ist der Ort, an dem ein Agent seine Abgabe hat')
    # `felder` steht als letztes Positional; sobald danach noch ein
    # Schalter mit Wert kommt (`--neu --bis 12 de=…`), reisst argparse
    # die Zuordnung auseinander und meldet nur „unrecognized
    # arguments". Deshalb werden die `feld=wert`-Angaben hier
    # eingesammelt, egal an welcher Stelle sie stehen.
    a, rest = p.parse_known_args()

    felder = {}
    for x in list(a.felder) + list(rest):
        if '=' not in x:
            p.error(f'{x!r} ist kein feld=wert')
        f, w = x.split('=', 1)
        felder[f] = w
    if a.loeschen:
        if a.neu or a.mehrwort:
            p.error('--loeschen schliesst --neu und --mehrwort aus.')
        if felder:
            p.error('--loeschen nimmt keine Felder.')
        ok = loesche_mehrwort(a.buch, a.kapitel, a.vers, a.pos, a.form,
                              a.grund, a.trocken, a.out)
    elif a.neu:
        if a.mehrwort:
            p.error('--neu und --mehrwort schliessen einander aus.')
        teile = ([int(x) for x in a.teile.replace(',', ' ').split()]
                 if a.teile else None)
        ok = neues_mehrwort(a.buch, a.kapitel, a.vers, a.pos, a.form, felder,
                            a.bis, teile, a.grund, a.trocken, a.out)
    else:
        if a.bis is not None or a.teile:
            p.error('--bis und --teile gelten nur mit --neu.')
        ok = setze(a.buch, a.kapitel, a.vers, a.pos, a.form, felder,
                   a.grund, a.trocken, a.out, a.mehrwort)
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
