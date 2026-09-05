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


def zeige(wort, formen, stellen, lemmata=None, lstellen=None,
          lemmata_alle=None):
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
        # Kein Treffer — aber vielleicht ueber den Stamm? Der starre
        # Praefixvergleich der ersten Fassung fand `sauer` zu `saure` nicht
        # (Vokalwechsel) und `hacken` zu `gehackt` nicht (ge-Praefix), beide
        # gemeldet vom Agenten fuer Jesaja 5. Deshalb zusaetzlich: Partizip- und
        # Endungsabbau, Umlautaufloesung, und ein Aehnlichkeitsmass.
        import difflib
        def stamm(w):
            w = (w.replace('ä', 'a').replace('ö', 'o')
                  .replace('ü', 'u').replace('ß', 'ss'))
            if w.startswith('ge') and len(w) > 5:
                w = w[2:]
            for e in ('esten', 'sten', 'ende', 'end', 'ten', 'ung',
                      'est', 'en', 'er', 'es', 'em', 'et', 'te', 'st',
                      'e', 't', 'n', 's'):
                if w.endswith(e) and len(w) - len(e) >= 3:
                    return w[:-len(e)]
            return w
        sf = stamm(f)
        kandidaten = set()
        for x in list(formen) + list(lemmata or ()):
            if len(x) < 4:
                continue
            sx = stamm(x)
            if sf == sx or sx.startswith(sf) or sf.startswith(sx) \
               or difflib.SequenceMatcher(None, sf, sx).ratio() >= 0.8:
                kandidaten.add(x)
        print('   im Bestand NICHT belegt.')
        if kandidaten:
            als_lemma = sorted(x for x in kandidaten if lemmata and x in lemmata)
            als_form = sorted(x for x in kandidaten if x not in set(als_lemma))
            if als_lemma:
                print('   Es gibt aber diese LEMMATA mit demselben Stamm — erst')
                print('   `fixgloss.py show <Lemma>` fragen, bevor etwas Neues')
                print('   erfunden wird: ' + ', '.join(f'`{x}`' for x in als_lemma[:10]))
            if als_form:
                print('   stammverwandte Formen: ' + ', '.join(als_form[:10]))
        print()
        return False
    ges = sum(c.values())
    lemma_index = lemmata            # {lemma_klein: Counter} — vor dem Ueberschreiben retten
    lemmata = {k[1] for k in c}
    schreibungen = {k[0] for k in c}
    if C.strip_punct(wort) not in schreibungen:
        print(f'   VORSICHT: im Bestand steht die Form nur als '
              + ', '.join(f'`{x}`' for x in sorted(schreibungen))
              + f' — nicht als `{C.strip_punct(wort)}`.')
        print('   Gross-/Kleinschreibung trennt hier womoeglich zwei Woerter')
        print('   (`Spross` das Substantiv gegen `spross` von `sprießen`).')
    # „belegt" ohne Zusatz ist dreimal missverstanden worden — in den
    # Vorbereitungen zu Daniel 7, Hosea 3 und Hosea 5 stand die Zahl der
    # FORM als Zahl des Lemmas im Prompt (`Klauen` 11 statt `Klaue` 13,
    # `Priestergewand` 10 statt 13, `Motte` 2 statt 8). Deshalb steht jetzt
    # dabei, was gezaehlt wurde.
    lsum = sum(sum(lemma_index.get(l.lower(), {}).values()) for l in lemmata) if lemma_index else 0
    zusatz = f' — das LEMMA hat {lsum}' if lsum > ges else ''
    print(f'   die FORM `{C.strip_punct(wort)}` ist **{ges}× belegt**{zusatz}, '
          'Lemma: ' + ', '.join(f'`{l}`' for l in sorted(lemmata)))
    if len(lemmata) == 1 and list(lemmata)[0].lower() != f:
        print(f'   ACHTUNG: das Lemma heisst `{list(lemmata)[0]}`, nicht `{wort}` —')
        print(f'   `fixgloss.py show {wort}` schweigt deshalb. Genau die Falle,')
        print('   fuer die dieses Werkzeug gebaut ist.')
    # Die Form kann unter einem fremden Lemma stehen UND das gesuchte Wort
    # zugleich selbst ein Lemma sein. `morden` ist der Fall, der das ans Licht
    # brachte (Hesekiel 26,15): die Form `Morden` steht unter dem Substantiv
    # `Mord`, das Verb-Lemma `morden` ist ueber die Form `mordet` belegt
    # (Jeremia 7,9) — und blieb hier unsichtbar, weil der Lemma-Hinweis bisher
    # nur im Zweig "gar nicht belegt" stand. Der Agent fand es nur, weil er
    # zusaetzlich `fixgloss.py show` fragte.
    # Case-SENSITIV vergleichen. Die erste Fassung dieser Pruefung verglich
    # kleingeschrieben und uebersah deshalb genau die haeufigste Bauform:
    # `flicken` (Verb, B2) neben `Flicken` (Substantiv, C1) — kleingeschrieben
    # sind beide gleich, also griff der Ausschluss und die Meldung fiel aus.
    # Gefunden vom Agenten fuer Hesekiel 27, ein Paket nachdem der Fall
    # `morden`/`Mord` die Pruefung ueberhaupt erst ausgeloest hatte.
    if lemmata_alle and wort in lemmata_alle and wort not in lemmata:
        print()
        print(f'   ABER: `{wort}` ist AUSSERDEM ein eigenes Lemma im Bestand,')
        print(f'   ueber andere Formen belegt. `fixgloss.py show {wort}`')
        print('   fragen — die Reihe dort ist womoeglich die gesuchte.')
    for (form, lemma, lvl, en, es, fr, it), n in c.most_common():
        print(f'   {n:4}× · {form} → `{lemma}` · {lvl} · '
              f'*{en}* · *{es}* · *{fr}* · *{it}*')
    print('   ' + ', '.join(stellen[f][:6]))
    # Das Lemma kann Lesarten fuehren, die diese FORM nicht hat. Gefunden am
    # Klauen/Klaue-Fall (Daniel 7,19): die Pluralform `Klauen` steht 11x und
    # ausnahmslos als *hooves* — der Singular `Klaue` aber zweimal, einmal als
    # *hoof* und einmal als *paw* (1. Samuel 17,37), und genau die zweite Lesart
    # war die gesuchte. Wer nur die Form abfragt, sieht sie nicht und haelt das
    # Lemma fuer einstimmig.
    if lemma_index:
        def _blosse_beugung(a, b):
            """Unterscheiden sich zwei Reihen nur in der Flexion?

            Ohne diese Sperre meldete der Lauf bei `Wort` die Reihe von
            `Worte` und bei `König` die von `Könige` als "weitere Lesart" —
            das ist derselbe Sinn im Plural und reines Rauschen. Gesucht sind
            Reihen wie *paw* neben *hooves*, die inhaltlich auseinandergehen.
            """
            for x, y in zip(a[3:], b[3:]):          # en · es · fr · it
                                                    # (0 Form, 1 Lemma, 2 Level)
                x, y = x.lower(), y.lower()
                if x == y:
                    continue                        # `re`/`re` — kurze Woerter
                k = min(len(x), len(y), 4)
                if k < 3 or x[:k] != y[:k]:
                    return False
            return True
        eigene = {k[1:] for k in c}
        andere = collections.Counter()
        for l in lemmata:
            for k, n in lemma_index.get(l.lower(), {}).items():
                if k[1:] in eigene:
                    continue
                if any(_blosse_beugung(k, e) for e in c):
                    continue
                andere[k] += n
        if andere:
            print()
            print(f'   Das LEMMA fuehrt {len(andere)} weitere Lesart(en), die diese')
            print('   Form nicht hat — am Vers pruefen, ob eine davon passt:')
            for (form, lemma, lvl, en, es, fr, it), n in andere.most_common(6):
                print(f'   {n:4}× · {form} → `{lemma}` · {lvl} · '
                      f'*{en}* · *{es}* · *{fr}* · *{it}*')
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
        if not zeige(w, formen, stellen, lemmata, lstellen,
                     set(lemmata or ())):
            fehlt += 1
    return 0 if fehlt == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
