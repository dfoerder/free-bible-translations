#!/usr/bin/env python3
"""Stimmen die LEVEL und REIHEN, die eine Vorgabedatei nennt?

    vorgabecheck.py <datei.md|.txt> [<datei> ...]

## Der Anlass

`promptcheck.py` prueft, ob ein Wort im Quelltext **vorkommt**. Das ist
nur die eine Haelfte. Die andere kostete in Amos Paket 1 sieben Fehler:
`Feuer A2` (der Bestand hat 336× A1), `machen A2` (1435× A1),
`rueckgaengig machen C1` (der einzige Beleg steht auf B2) — dazu eine
Reihe, deren spanische Spalte den Artikel wegliess, den die franzoesische
und italienische mitnahmen.

Alle sieben haetten sich in einer Sekunde messen lassen. Sie standen in
der Vorgabe, weil ich sie aus dem Gedaechtnis geschrieben und nur das
Vorkommen geprueft hatte.

## Was gelesen wird

Zeilen der Form

    Wort        B2  glosse · glosse · glosse · glosse
    `Wort` B2 *glosse · glosse · glosse · glosse*
    Wort B2 glosse·glosse·glosse·glosse

Das Level wird gegen die Mehrheit des Lemmas im Bestand gehalten, die
Reihe gegen die belegten Lesarten. Gemeldet wird:

    LEVEL   das genannte Level ist im Bestand nicht die Mehrheit
    REIHE   die genannte Vierer-Reihe steht im Bestand nirgends
    LEER    das Lemma ist im Bestand unbelegt (dann ist beides frei)
    AUSGABE ein Zitat, das einer Ausgabe zugeschrieben wird, steht dort nicht

Fuer die AUSGABE-Probe muss die Buchnummer mitgegeben werden:

    vorgabecheck.py <datei> --buch <nr>

Sie liest Muster wie `WEB „…"`, `RV *…*`, `LSG "…"` und sucht das Zitat
im ganzen Buchtext der genannten Ausgabe. Der Anlass: in Amos Paket 2
stand im Prompt, was die vier Ausgaben in 5,26 lesen — **alle vier
Angaben waren erfunden**, und nur der Agent hat es gemerkt, weil er
nachgelesen hat. Derselbe Fehlertyp wie in Daniel Paket 2, nur eine
Ebene weiter: nicht mehr ueber den Quelltext, sondern ueber die Zeugen.

**Ein Treffer ist ein Verdacht, kein Fehler.** Eine Vorgabe darf vom
Bestand abweichen — aber dann absichtlich, mit Begruendung daneben.
Neu gepraegte Reihen melden sich als LEER und sind genau richtig so.
"""
import sys, re, collections, unicodedata
import common as C

LEVELS = ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')
# Wort [Backticks] Level Glossen mit · getrennt
ZEILE = re.compile(
    r'^\s*`?([A-Za-zÄÖÜäöüß][\wÄÖÜäöüß\- ]{1,30}?)`?\s+'
    r'\*?\*?(' + '|'.join(LEVELS) + r')\*?\*?\s+'
    r'\*?([^\n*]{3,200}?)\*?\s*$')


def norm(s):
    s = unicodedata.normalize('NFC', s.strip())
    s = s.replace('**', '').replace('`', '').strip()
    return s


def reihen_index():
    lv = collections.defaultdict(collections.Counter)
    reihen = collections.defaultdict(set)
    form2lem = collections.defaultdict(collections.Counter)
    for nr in range(1, 67):
        try:
            anno = C.load_anno(nr)['chapters']
        except Exception:
            continue
        for kap, vv in anno.items():
            for v, ent in vv.items():
                for e in ent:
                    if not isinstance(e, dict):
                        continue
                    lv[e['lemma']][e['level']] += 1
                    reihen[e['lemma']].add((e['en'], e['es'], e['fr'], e['it']))
                    form2lem[C.strip_punct(e['form']).lower()][e['lemma']] += 1
    return lv, reihen, form2lem


def umlaut(w):
    """Alle Ruecknahmen der ASCII-Umschrift, nicht nur die volle.

    `laesst` wird zu `lässt` UND zu `läßt` — die Vorgabedateien sind in
    ASCII geschrieben, der Bestand nicht, und `ss` steht dort mal fuer
    `ss`, mal fuer `ß`.
    """
    out = {w}
    for a, b in (('ae', 'ä'), ('oe', 'ö'), ('ue', 'ü'), ('ss', 'ß')):
        out |= {x.replace(a, b) for x in out}
    return sorted(out, key=len)


AUSGABEN = {'WEB': 'eng/web', 'RV': 'spa/rv1909mod', 'RV1909': 'spa/rv1909mod',
            'RV1909mod': 'spa/rv1909mod', 'LSG': 'fra/lsg1910mod',
            'RIV': 'ita/riv1927', 'RIV1927': 'ita/riv1927'}
NENNUNG = re.compile(r'\b(WEB|RV1909mod|RV1909|RV|LSG|RIV1927|RIV)\b')
EINZITAT = re.compile(r'[„"\u201c]([^„"\u201c\u201d\n]{3,90})[""\u201d]')


def zitate(zeile):
    """Jedes Zitat den Ausgaben zuordnen, die unmittelbar davor stehen.

    `WEB „Sakkuth"/„Kaiwan"` nennt WEB einmal und zitiert zweimal — beide
    Zitate gehoeren zu WEB. Ein Muster, das nur bis zum ersten Zitat
    reicht, laesst die Haelfte durch.

    `WEB/RV „temple", LSG/RIV „palais"` nennt ZWEI Ausgaben vor einem
    Zitat, und das Zitat steht nur in einer davon. Deshalb wird gegen
    die ganze Gruppe geprueft und nur gemeldet, was in KEINER steht.
    """
    treffer = []
    marken = [(m.start(), m.end(), m.group(1)) for m in NENNUNG.finditer(zeile)]
    for m in EINZITAT.finditer(zeile):
        gruppe, ende = [], None
        for start, stop, kuerzel in marken:
            if start >= m.start():
                break
            # Eine neue Gruppe beginnt, wo zwischen zwei Nennungen mehr
            # steht als ein Trennzeichen.
            if ende is not None and zeile[ende:start].strip(' /,+&').replace('und', ''):
                gruppe = []
            gruppe.append(kuerzel)
            ende = stop
        if gruppe:
            treffer.append((tuple(gruppe), m.group(1)))
    return treffer


def ausgabentext(nr):
    """Der ganze Buchtext je Ausgabe, klein und ohne Sonderzeichen."""
    import glob, json, os
    basis = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = {}
    for kuerzel, pfad in list(AUSGABEN.items()) + [('__de__', 'deu/l1912mod')]:
        g = glob.glob(os.path.join(basis, pfad, f'{nr}_*.json'))
        if not g:
            continue
        x = json.load(open(g[0], encoding='utf-8'))
        x = x.get('chapters', x)
        roh = ' '.join(v for kap in x.values() for v in kap.values())
        out[kuerzel] = re.sub(r'[^a-z0-9äöüàâèéêëîïôûùç ]', ' ',
                              roh.lower().replace('\u2019', "'")
                              .replace("'", ' ')).replace('  ', ' ')
    return out


def pruefe_zitate(pfad, nr):
    texte = ausgabentext(nr)
    # Der deutsche Text zaehlt mit: ein Zitat, das dort steht, ist ein
    # Zitat des Quelltextes, keine Behauptung ueber eine Ausgabe.
    deutsch = texte.pop('__de__', '')
    if not texte:
        print(f'  (keine Ausgabendateien fuer Buch {nr} gefunden)')
        return 0
    befunde = 0
    with open(pfad, encoding='utf-8') as f:
        for zeile in f:
            for gruppe, zitat in zitate(zeile):
                kandidaten = [texte[k] for k in gruppe if k in texte]
                if not kandidaten:
                    continue
                kuerzel = '/'.join(dict.fromkeys(gruppe))
                such = re.sub(r'[^a-z0-9äöüàâèéêëîïôûùç ]', ' ',
                              zitat.lower().replace('\u2019', "'")
                              .replace("'", ' ')).split()
                if not such:
                    continue
                # Das laengste Wort des Zitats muss vorkommen, und bei
                # mehreren Woertern auch die Folge.
                lang = max(such, key=len)
                def steht(txt):
                    if len(lang) >= 4 and lang not in txt.split():
                        return False
                    if len(such) > 1 and ' '.join(such) not in txt:
                        return False
                    return True
                if any(steht(x) for x in kandidaten) or steht(deutsch):
                    continue
                befunde += 1
                print(f'  AUSGABE {kuerzel} liest „{zitat}" — '
                      f'steht in keiner der genannten Ausgaben')
    return befunde


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    args = list(sys.argv[1:])
    buch = None
    if '--buch' in args:
        i = args.index('--buch')
        buch = int(args[i + 1])
        del args[i:i + 2]
    lv, reihen, form2lem = reihen_index()
    gesamt = befunde = 0
    for pfad in args:
        print(f'\n# {pfad}\n')
        n = 0
        with open(pfad, encoding='utf-8') as f:
            for zeile in f:
                m = ZEILE.match(zeile.rstrip())
                if not m:
                    continue
                wort, level, rest = norm(m.group(1)), m.group(2), norm(m.group(3))
                # Kommentar hinter der Reihe abschneiden: „(142×)", „  ← s. u."
                rest = re.split(r'\s{2,}|\s+\(|\s+←|\s+—', rest)[0].strip()
                teile = [t.strip() for t in rest.split('·')]
                if len(teile) != 4 or any(not t for t in teile):
                    continue
                n += 1
                gesamt += 1
                kand = []
                for v in umlaut(wort):
                    kand += [v, v.capitalize(), v.lower()]
                # Alle Lemmata sammeln, die auf das Wort passen — `So` und
                # `so` sind im Bestand ZWEI Lemmata mit verschiedenen
                # Lesarten, und die Vorgabe meint fast immer beide.
                treffer = [k for k in kand if k in lv]
                lem = next((k for k in treffer
                            if tuple(teile) in reihen[k]), None) or \
                      next((k for k in treffer if level in lv[k]), None) or \
                      (treffer[0] if treffer else None)
                if lem is None:   # ueber die Wortform aufs Lemma aufloesen
                    for k in kand:
                        if k.lower() in form2lem:
                            lem = form2lem[k.lower()].most_common(1)[0][0]
                            break
                if lem is None:
                    print(f'  LEER   `{wort}` — im Bestand unbelegt, Level und Reihe frei')
                    continue
                mehr, anz = lv[lem].most_common(1)[0]
                ges = sum(lv[lem].values())
                if level != mehr:
                    befunde += 1
                    print(f'  LEVEL  `{lem}` steht hier auf {level}, '
                          f'der Bestand auf {mehr} ({anz}/{ges})')
                if tuple(teile) not in reihen[lem]:
                    befunde += 1
                    nah = [r for r in reihen[lem] if sum(a == b for a, b in zip(r, teile)) >= 2]
                    print(f'  REIHE  `{lem}` — {" · ".join(teile)}')
                    for r in sorted(nah)[:2]:
                        print(f'             Bestand: {" · ".join(r)}')
                    if not nah:
                        print(f'             (keine aehnliche Bestandsreihe; '
                              f'{len(reihen[lem])} andere Lesarten)')
        if buch:
            befunde += pruefe_zitate(pfad, buch)
        print(f'  — {n} Vorgabezeilen gelesen')
    print(f'\n{befunde} Befunde aus {gesamt} Vorgabezeilen. Jeder ist eine '
          'Absicht oder ein Fehler —\nwo er Absicht ist, gehoert die Begruendung daneben.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
