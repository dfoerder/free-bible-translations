#!/usr/bin/env python3
"""Stehen die wiederkehrenden Wortfolgen eines Buches zeichengleich?

    folgencheck.py <buchNr> [--min 4] [--kapitel 16,17] [--datei <ch.json> ...]

## Der Anlass

`wiederholungen.py` findet vor der Arbeit, welche Wortfolgen ein Buch
mehrfach traegt. Ob die Agenten sie dann wirklich gleich gesetzt haben,
habe ich seit Zefanja bei **jedem** Paket mit einem weggeworfenen Skript
geprueft — fuenfmal allein in Sacharja. Einmal hat es einen echten
Fehler gefunden (Zefanja 3,6 fehlte das Mehrwort `niemand mehr`, das
Kapitel 2 gesetzt und ausdruecklich angemahnt hatte), und mehrfach
Abweichungen, die **richtig** waren.

## Was eine Abweichung bedeutet

Nicht jede ist ein Fehler. Die haeufigen Gruende, alle in Sacharja und
Haggai belegt:

- **Satzposition** — `So` steht am Versanfang gross, satzintern klein.
- **Kasus** — `dem Engel` ist in Sacharja 1,11 Dativobjekt (*to the*),
  in 3,1 steht es nach `vor` (*the*).
- **Genus des Bezugsworts** — `die zwei` vor `olivos` ist es *los*,
  vor `ramas` *las*.
- **Numerus** — `darin` meint in Zefanja 2,5 die Kueste (f. Sg.), in
  3,6 die Staedte (f. Pl.).
- **Funktion** — `In` ist in Sacharja 8,4 lokal (*Dans*), in 8,23
  temporal (*En*).

Gemeldet wird deshalb **jede** Abweichung mit dem Token, an dem sie
haengt; die Entscheidung bleibt am Vers.
"""
import sys, json, collections
import common as C


def folgen(quelle, minlen=4, maxlen=14):
    """Alle Wortfolgen, die im Buch mehr als einmal stehen.

    Jeder Treffer traegt die **Originalpositionen** seiner Tokens, nicht
    einen Startindex: zwischen zwei Woertern kann ein alleinstehendes
    Satzzeichen liegen, das keinen Eintrag bekommt. Im Franzoesischen ist
    das die Regel — LSG setzt vor `?`, `;`, `!` und `:` ein Leerzeichen.
    """
    idx = collections.defaultdict(list)
    for ort, toks, pos in quelle:
        for n in range(maxlen, minlen - 1, -1):
            for i in range(len(toks) - n + 1):
                idx[tuple(toks[i:i + n])].append((ort, tuple(pos[i:i + n])))
    gemeldet, out = set(), []
    for g in sorted(idx, key=lambda x: (-len(x), x)):
        orte = idx[g]
        if len({o for o, _ in orte}) < 2:
            continue
        if any(tuple(g[a:a + m]) in gemeldet
               for m in range(len(g), minlen - 1, -1)
               for a in range(len(g) - m + 1)):
            continue
        gemeldet.add(g)
        out.append((g, orte))
    return out


def signatur(eintraege, pp):
    """Die Glossen an den Positionen `pp` — als vergleichbare Signatur.

    `pp` sind die Originalpositionen der Folge, nicht ein Bereich: ein
    alleinstehendes Satzzeichen dazwischen bekommt keinen Eintrag und
    verschiebt alles danach.
    """
    E = {e['pos']: e for e in eintraege
         if 'pos_end' not in e and 'parts' not in e}
    ein = tuple(((E[j]['lemma'],) + C.reihe(E[j])) if j in E else None
                for j in pp)
    von, bis = pp[0], pp[-1]
    # Die Mehrwort-Spanne wird ueber den INDEX innerhalb der Folge
    # ausgedrueckt, nicht ueber den Rohabstand: `toi;` ist ein Token,
    # `toi ;` sind zwei, und dann verschiebt sich jede Rohdistanz
    # dahinter. In Matthaeus 18,8 gegen 18,9 meldete das eine Abweichung,
    # obwohl die Glossen zeichengleich waren.
    stelle = {p: i for i, p in enumerate(pp)}
    mw = []
    for m in eintraege:
        sp = m.get('parts', list(range(m['pos'],
                                       m.get('pos_end', m['pos']) + 1)))
        if len(sp) > 1 and min(sp) >= von and max(sp) <= bis:
            idx = tuple(stelle.get(x, -1) for x in sp)
            mw.append((idx, m['lemma']) + C.reihe(m))
    return ein, tuple(sorted(mw))


def main():
    args = list(sys.argv[1:])
    minlen = 4
    if '--min' in args:
        k = args.index('--min')
        minlen = int(args[k + 1])
        del args[k:k + 2]
    # Ein Agent will die Bloecke sehen, die SEIN Kapitel betreffen. Ohne
    # Filter sind es fuer Matthaeus 304 — der Agent fuer Kapitel 16 musste
    # sich die vierzehn eigenen mit einem Skript herausziehen, und wer
    # stattdessen `head -40` nimmt, sieht ausschliesslich fremde Kapitel.
    nurkap = None
    while '--kapitel' in args:
        k = args.index('--kapitel')
        nurkap = set((nurkap or set())) | {str(int(x)) for x in
                                           args[k + 1].split(',')}
        del args[k:k + 2]
    extra = {}
    while '--datei' in args:
        k = args.index('--datei')
        p = args[k + 1]
        del args[k:k + 2]
        kap = ''.join(c for c in p.split('/')[-1] if c.isdigit())
        extra[str(int(kap))] = json.load(open(p, encoding='utf-8'))
    if not args:
        print(__doc__)
        return 2
    nr = int(args[0])
    src = C.load_source(nr)
    ch = src['chapters'] if 'chapters' in src else src
    try:
        anno = C.load_anno(nr)['chapters']
    except Exception:
        anno = {}
    anno = dict(anno)
    anno.update(extra)

    quelle = []
    for k in sorted(ch, key=int):
        for v in sorted(ch[k], key=int):
            roh = ch[k][v].split()
            toks, pos = [], []
            for i, x in enumerate(roh):
                t = x.strip('.,;:!?„“"’')
                if t:
                    toks.append(t)
                    pos.append(i)          # die Originalposition merken
            quelle.append(((k, v), toks, pos))

    print(f'# Zeichengleichheit: {C.book_name(nr)}\n')
    gleich = abweichend = ohne = 0
    for g, orte in folgen(quelle, minlen):
        gruppen = {}
        for (k, v), pp in orte:
            if k not in anno or v not in anno[k]:
                continue
            gruppen.setdefault(signatur(anno[k][v], pp),
                               []).append(f'{k},{v}')
        if nurkap is not None and not any(
                w.split(',')[0] in nurkap
                for x in gruppen.values() for w in x):
            continue
        stellen = sum(len(x) for x in gruppen.values())
        if stellen < 2:
            ohne += 1
            continue
        if len(gruppen) == 1:
            gleich += 1
            continue
        abweichend += 1
        haupt = max(gruppen.items(), key=lambda x: len(x[1]))
        # `--kapitel` filtert bisher nur, OB ein Block gedruckt wird.
        # Gedruckt wurden dann alle seine Abweichungen, auch die fremder
        # Kapitel — in Matthaeus 26 waren das 796 Zeilen fuer ein
        # Dutzend eigene. Jetzt filtert es auch die Zeilen.
        # Gemeldet vom Agenten fuer Matthaeus 26.
        kopf = f'## „{" ".join(g)}"  ({len(g)} Tokens)\n'
        for sig, wo in gruppen.items():
            if sig is haupt[0]:
                continue
            if nurkap is not None and not any(
                    w.split(',')[0] in nurkap for w in wo) \
                    and not any(w.split(',')[0] in nurkap
                                for w in haupt[1]):
                continue
            if kopf:
                print(kopf)
                kopf = ''
            for idx, (a, b) in enumerate(zip(haupt[0][0], sig[0])):
                if a != b:
                    print(f'   {", ".join(wo)}  bei `{g[idx]}`:')
                    print(f'      hier  {b}')
                    print(f'      dort  {a}  ({", ".join(haupt[1])})')
            if haupt[0][1] != sig[1]:
                print(f'   {", ".join(wo)}  Mehrwoerter: {sig[1] or "keine"}')
                print(f'      dort  {haupt[0][1] or "keine"}')
        print()
    print(f'{gleich} Folgen zeichengleich, {abweichend} mit Abweichung'
          + (f', {ohne} noch nicht annotiert' if ohne else '') + '.')
    if abweichend:
        print('Jede Abweichung am Vers pruefen — Satzposition, Kasus, '
              'Genus,\nNumerus und Funktion sind haeufige und richtige '
              'Gruende.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
