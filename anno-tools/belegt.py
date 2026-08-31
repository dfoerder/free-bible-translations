#!/usr/bin/env python3
"""belegt.py — ist dieses Wort im Bestand belegt, und unter welchem Lemma?

Warum es dieses Werkzeug gibt
-----------------------------
Zweimal in zwei Buechern hat die Vorbereitung ein Wort als „im Bestand
unbelegt" gefuehrt, das laengst dastand:

  * `beschwoeren` (Hohelied) — 13 Belege, neun davon im AT. Gezaehlt worden
    war die Form `beschwoere`.
  * `Heerscharen` (Jesaja) — 34 Belege unter dem Lemma `Heerschar`. Der
    Bestand normalisiert auf den Singular; `fixgloss.py show Heerscharen`
    schweigt, weil `show` ein LEMMA erwartet, keine Wortform.

Beide Male war die Folge dieselbe: ein Kapitel wurde als „Massstab" vorgezogen,
um eine Festlegung zu treffen, die der Bestand schon getroffen hatte.

`fixgloss.py show` fragt nach dem **Lemma**. Dieses Werkzeug fragt nach der
**Wortform** — der Groesse, die im Quelltext steht und die man vor sich hat.
Es sucht direkt im gebauten Bestand und kann die Form deshalb nicht verfehlen.

  belegt.py Heerscharen        eine Form
  belegt.py Heerscharen Spross Braut     mehrere
  belegt.py -d 23              alle unbelegten Formen eines Buches auflisten

Beide Richtungen
----------------
Die erste Fassung suchte nur nach der **Form** und hatte damit die genaue
Umkehrung derselben Luecke: `forttreiben` (Jes 6,12) steht im Bestand nur als
`forttreibt` / `treibt fort` / `treibe fort`, die Infinitivform also nirgends —
das Werkzeug meldete „nicht belegt", waehrend `fixgloss.py show forttreiben`
drei Belege lieferte. Gefunden vom Agenten fuer Jesaja 6.

Seither wird **beides** indiziert: schlaegt die Formsuche fehl, wird geprueft,
ob das gesuchte Wort selbst ein Lemma des Bestands ist.
"""
import argparse, collections, glob, json, os, sys
import common as C

ANNO = os.path.join(C.REPO, 'bibles', 'deu', 'l1912mod', 'anno')


def bestand():
    """{wortform_klein: Counter{(lemma, level, en, es, fr, it): n}}, plus Belegstellen."""
    formen = collections.defaultdict(collections.Counter)
    lemmata = collections.defaultdict(collections.Counter)
    stellen = collections.defaultdict(list)
    lstellen = collections.defaultdict(list)
    for pfad in sorted(glob.glob(os.path.join(ANNO, '*_l1912mod_multi.json'))):
        d = json.load(open(pfad))
        name = d.get('name') or os.path.basename(pfad).split('_')[0]
        ch = d.get('chapters', d)
        for k in ch:
            for v in ch[k]:
                for e in ch[k][v]:
                    f = C.strip_punct(e['form']).lower()
                    if not f:
                        continue
                    schluessel = (C.strip_punct(e['form']), e['lemma'], e['level'],
                                  e['en'], e['es'], e['fr'], e['it'])
                    formen[f][schluessel] += 1
                    if len(stellen[f]) < 8:
                        stellen[f].append(f'{name} {k},{v}')
                    l = e['lemma'].lower()
                    lemmata[l][schluessel] += 1
                    if len(lstellen[l]) < 8:
                        lstellen[l].append(f'{name} {k},{v}')
    return formen, stellen, lemmata, lstellen


def zeige(wort, formen, stellen, lemmata=None, lstellen=None):
    f = C.strip_punct(wort).lower()
    c = formen.get(f)
    print(f'## Wortform `{wort}`')
    if not c and lemmata and f in lemmata:
        # Die Umkehrung der Heerschar-Falle: das gesuchte Wort IST das Lemma,
        # steht im Bestand aber nur flektiert. Gefunden an `forttreiben`
        # (Jes 6,12): die Form fehlt, das Lemma hat drei Belege.
        c2 = lemmata[f]
        ges = sum(c2.values())
        print(f'   Die FORM steht nicht im Bestand — aber `{wort}` ist ein')
        print(f'   **LEMMA mit {ges} Belegen**, dort nur flektiert:')
        for (form, lemma, lvl, en, es, fr, it), n in c2.most_common():
            print(f'   {n:4}× · {form} → `{lemma}` · {lvl} · '
                  f'*{en}* · *{es}* · *{fr}* · *{it}*')
        print('   ' + ', '.join(lstellen[f][:6]))
        print('   Level und Lesart von dort uebernehmen, nichts Neues erfinden.')
        print()
        return True
    if not c:
        # Kein Treffer — aber vielleicht ueber den Stamm?
        nah = sorted(x for x in formen
                     if len(x) >= 4 and (x.startswith(f[:5]) or f.startswith(x[:5])))
        print('   im Bestand NICHT belegt.')
        if nah:
            print('   stammverwandte Formen, die es gibt: '
                  + ', '.join(nah[:12]))
            print('   -> `lexicon.py` und `fixgloss.py show <Lemma>` fragen,'
                  ' bevor etwas Neues erfunden wird.')
        print()
        return False
    ges = sum(c.values())
    lemmata = {k[1] for k in c}
    schreibungen = {k[0] for k in c}
    if C.strip_punct(wort) not in schreibungen:
        print(f'   VORSICHT: im Bestand steht die Form nur als '
              + ', '.join(f'`{x}`' for x in sorted(schreibungen))
              + f' — nicht als `{C.strip_punct(wort)}`.')
        print('   Gross-/Kleinschreibung trennt hier womoeglich zwei Woerter')
        print('   (`Spross` das Substantiv gegen `spross` von `sprießen`).')
    print(f'   **{ges}× belegt**, Lemma: ' + ', '.join(f'`{l}`' for l in sorted(lemmata)))
    if len(lemmata) == 1 and list(lemmata)[0].lower() != f:
        print(f'   ACHTUNG: das Lemma heisst `{list(lemmata)[0]}`, nicht `{wort}` —')
        print(f'   `fixgloss.py show {wort}` schweigt deshalb. Genau die Falle,')
        print('   fuer die dieses Werkzeug gebaut ist.')
    for (form, lemma, lvl, en, es, fr, it), n in c.most_common():
        print(f'   {n:4}× · {form} → `{lemma}` · {lvl} · '
              f'*{en}* · *{es}* · *{fr}* · *{it}*')
    print('   ' + ', '.join(stellen[f][:6]))
    print()
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument('woerter', nargs='*')
    p.add_argument('-d', '--durchsuchen', type=int, metavar='BUCHNR',
                   help='alle Wortformen dieses Buches gegen den Bestand halten')
    a = p.parse_args()
    formen, stellen, lemmata, lstellen = bestand()
    if a.durchsuchen:
        s = C.load_source(a.durchsuchen)
        zaehl = collections.Counter()
        for k in s['chapters']:
            for v in s['chapters'][k].values():
                for t in C.tokens(v):
                    w = C.strip_punct(t).lower()
                    if w and not w.isdigit():
                        zaehl[w] += 1
        unbelegt = [(w, n) for w, n in zaehl.items()
                    if w not in formen and w not in lemmata]
        print(f'# {s["name"]}: {len(zaehl)} Wortformen, '
              f'{len(unbelegt)} im Bestand unbelegt '
              f'({100*len(unbelegt)/len(zaehl):.0f} %)\n')
        for w, n in sorted(unbelegt, key=lambda x: (-x[1], x[0])):
            print(f'{n:4}× {w}')
        return 0
    if not a.woerter:
        p.error('Wortform angeben oder -d <buchnr>')
    fehlt = 0
    for w in a.woerter:
        if not zeige(w, formen, stellen, lemmata, lstellen):
            fehlt += 1
    return 0 if fehlt == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
