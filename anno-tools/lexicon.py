"""Gefilterter Lexikon-Extrakt für einen Versbereich.

    lexicon.py <buchNr> <kapitel> [<vonVers> <bisVers>] [-o datei]

Bestimmt erst die Wortformen des Abschnitts, sammelt dann **nur zu diesen**
die Einträge aus allen fertigen Anno-Dateien. Ein vollständiger Extrakt wäre
bei über 230 000 Einträgen rund 1 MB und bringt den Agentenlauf zum Stillstand.

Zwei Abschnitte:
  BELEGT      — die Form steht so im Bestand, mit allen Lesarten und Zählung
  VERWANDT    — die Form nicht, aber ein Wort mit gleichem Stamm; das ist ein
                Hinweis, keine Vorgabe. In Namenskapiteln liefert dieser
                Abschnitt mehr Rauschen als Signal (Gosen→gießen).

Und eine Warnung, die in jeden Prompt gehört: **die Liste der unbelegten
Formen ist formbasiert.** Das Lemma kann über eine andere Form längst im
Bestand stehen — deshalb steht der VERWANDT-Abschnitt überhaupt da.
"""
import argparse
import collections
import sys

import common as C

MIN_STAMM = 5
MAX_LESARTEN = 6          # sonst wird der Extrakt für Funktionswörter unlesbar
DECKUNG = 0.9             # so viele Belege sollen die gezeigten Lesarten abdecken


def _kuerzen(sortiert):
    """Die häufigsten Lesarten, bis 90 % der Belege abgedeckt sind, höchstens
    MAX_LESARTEN. Ohne das ist `soll` allein zwanzig Zeilen lang und der
    Extrakt eines Kapitels über 250 KB groß."""
    gesamt = sum(c for _, (c, _) in sortiert) or 1
    zeigen, summe = [], 0
    for eintrag in sortiert:
        zeigen.append(eintrag)
        summe += eintrag[1][0]
        if len(zeigen) >= MAX_LESARTEN or summe / gesamt >= DECKUNG:
            break
    return zeigen, len(sortiert) - len(zeigen)


def formen_des_abschnitts(nr, kap, von=None, bis=None):
    verses = C.load_source(nr)['chapters'][str(kap)]
    out = collections.Counter()
    for v, txt in verses.items():
        if von is not None and not (von <= int(v) <= bis):
            continue
        for t in C.tokens(txt):
            f = C.strip_punct(t)
            if f:
                out[f] += 1
    return out


def bestand_index(ausser=None):
    """form -> {(lemma, level, en, es, fr, it): [anzahl, erste_stelle]}"""
    idx = collections.defaultdict(dict)
    lemma_formen = collections.defaultdict(set)
    for nr in C.anno_books():
        if ausser and nr == int(ausser):
            continue
        name = C.load_source(nr)['name']
        for _, kap, vers, e in C.iter_corpus([nr]):
            if C.is_multi(e):
                continue
            key = (e['lemma'], e['level'], e['en'], e['es'], e['fr'], e['it'])
            rec = idx[e['form']].setdefault(key, [0, f'{name} {kap},{vers}'])
            rec[0] += 1
            lemma_formen[e['lemma']].add(e['form'])
    return idx, lemma_formen


def mehrwort_index(ausser=None):
    idx = collections.defaultdict(dict)
    for nr in C.anno_books():
        if ausser and nr == int(ausser):
            continue
        name = C.load_source(nr)['name']
        for _, kap, vers, e in C.iter_corpus([nr]):
            if not C.is_multi(e):
                continue
            key = (e['lemma'], e['level'], e['en'], e['es'], e['fr'], e['it'])
            art = 'parts' if 'parts' in e else 'span'
            rec = idx[e['form']].setdefault((art,) + key, [0, f'{name} {kap},{vers}'])
            rec[0] += 1
    return idx


def extract(nr, kap, von=None, bis=None):
    formen = formen_des_abschnitts(nr, kap, von, bis)
    idx, lemma_formen = bestand_index()
    mw = mehrwort_index()

    stamm = collections.defaultdict(set)
    for lemma, fs in lemma_formen.items():
        if len(lemma) >= MIN_STAMM:
            stamm[lemma[:MIN_STAMM].lower()].add(lemma)

    belegt, verwandt, offen = [], [], []
    for f, n in sorted(formen.items(), key=lambda x: (-x[1], x[0])):
        if f in idx:
            belegt.append((f, n, idx[f]))
        else:
            kand = stamm.get(f[:MIN_STAMM].lower(), set()) if len(f) >= MIN_STAMM else set()
            if kand:
                verwandt.append((f, n, sorted(kand)))
            else:
                offen.append((f, n))

    L = []
    name = C.load_source(nr)['name']
    bereich = f'{kap}' + (f',{von}–{bis}' if von is not None else '')
    L.append(f'# Lexikon-Extrakt: {name} {bereich}')
    L.append('')
    ges = len(formen)
    L.append(f'{ges} verschiedene Wortformen · {len(belegt)} im Bestand belegt '
             f'({100*len(belegt)//max(ges,1)} %) · {len(verwandt)} nur über den Stamm · '
             f'{len(offen)} unbelegt')
    L.append('')
    L.append('**Belegte Lesarten sind bindend, solange die Bedeutung dieselbe ist.** '
             'Bei anderer Bedeutung eigene Glosse und eigenes Lemma — '
             'die App glossiert das deutsche Wort, nicht die Perikope.')
    L.append('')

    L.append('## BELEGT')
    L.append('')
    for f, n, lesarten in belegt:
        L.append(f'### {f}  ({n}× im Abschnitt)')
        sortiert = sorted(lesarten.items(), key=lambda x: -x[1][0])
        zeigen, rest = _kuerzen(sortiert)
        for (lemma, level, en, es, fr, it), (cnt, wo) in zeigen:
            L.append(f'- {cnt}× · lemma `{lemma}` · {level} · '
                     f'en *{en}* · es *{es}* · fr *{fr}* · it *{it}*   ({wo})')
        if rest:
            L.append(f'- (+ {rest} seltenere Lesarten — Tempus-, Person- und '
                     f'Numerusvarianten; im Zweifel nach dem Kontext bilden)')
        L.append('')

    if verwandt:
        L.append('## VERWANDT (Stamm belegt, Form nicht — Hinweis, keine Vorgabe)')
        L.append('')
        for f, n, kand in verwandt:
            zeilen = []
            for lemma in kand[:4]:
                bsp = None
                for form in sorted(lemma_formen[lemma]):
                    for (lm, lv, en, es, fr, it), (cnt, wo) in idx[form].items():
                        if lm == lemma:
                            bsp = f'`{lemma}` ({form}) {lv} · en *{en}* · es *{es}* · fr *{fr}* · it *{it}*'
                            break
                    if bsp:
                        break
                if bsp:
                    zeilen.append(bsp)
            L.append(f'- **{f}** ({n}×): ' + ' — '.join(zeilen))
        L.append('')

    if offen:
        L.append('## UNBELEGT (im ganzen Bestand keine Form dieses Wortes)')
        L.append('')
        L.append(', '.join(f'{f} ({n}×)' if n > 1 else f for f, n in offen))
        L.append('')

    # Mehrwort-Einträge, deren Bestandteile alle im Abschnitt vorkommen
    treffer = []
    fs = set(formen)
    for form, lesarten in mw.items():
        teile = form.split()
        if len(teile) >= 2 and all(t in fs for t in teile):
            treffer.append((form, lesarten))
    if treffer:
        L.append('## MEHRWORT-EINTRÄGE aus dem Bestand, deren Teile hier vorkommen')
        L.append('')
        for form, lesarten in sorted(treffer):
            for (art, lemma, level, en, es, fr, it), (cnt, wo) in sorted(
                    lesarten.items(), key=lambda x: -x[1][0]):
                L.append(f'- **{form}** [{art}] {cnt}× · lemma `{lemma}` · {level} · '
                         f'en *{en}* · es *{es}* · fr *{fr}* · it *{it}*   ({wo})')
        L.append('')

    return '\n'.join(L)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int)
    p.add_argument('kapitel', type=int)
    p.add_argument('von', type=int, nargs='?')
    p.add_argument('bis', type=int, nargs='?')
    p.add_argument('-o', '--out')
    a = p.parse_args()
    txt = extract(a.buch, a.kapitel, a.von, a.bis)
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(txt)
        print(f'{a.out} geschrieben ({len(txt)} Zeichen)')
    else:
        sys.stdout.write(txt)
