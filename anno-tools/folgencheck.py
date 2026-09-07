#!/usr/bin/env python3
"""Stehen die wiederkehrenden Wortfolgen eines Buches zeichengleich?

    folgencheck.py <buchNr> [--min 4] [--kapitel 16,17] [--datei <ch.json> ...]
    folgencheck.py <buchNr> --gegen 40 [40 ...]      auch gegen andere Buecher

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

## `--gegen`: die Bindung ueber die Buchgrenze

Bis Markus verglich dieses Werkzeug nur **innerhalb** eines Buches. Bei
den Synoptikern ist das die kleinere Haelfte der Arbeit: Marc 1,3 teilt
mit Matthieu 3,3 siebzehn Tokens am Stueck, und ob die beiden
zeichengleich stehen, hat kein Lauf geprueft — die Agenten fuer Marc 1
und Marc 2 haben es sich beide selbst gebaut, einer davon mit einem
Positionsversatz, der sechs Scheinabweichungen erzeugte.

`--gegen 40` nimmt die Verse von Matthaeus mit in den Vergleich. Beide
Buecher zusammen bilden EINEN Wortfolgenraum; gemeldet werden nur
Bloecke, an denen das eigene Buch beteiligt ist. Die Stellen tragen
ihren Buchnamen.
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
    # `--kapitel 13 14 15` hat bis hierher NUR auf 13 gefiltert: die
    # Trennung war das Komma, und die beiden uebrigen Zahlen fielen
    # hinten als Positionsargumente an, wo sie stillschweigend
    # weggeworfen wurden. Der Lauf sah aus wie ein Lauf ueber drei
    # Kapitel. Jetzt zaehlen Komma UND Leerzeichen.
    nurkap = None
    while '--kapitel' in args:
        k = args.index('--kapitel')
        j = k + 1
        werte = []
        while j < len(args) and not args[j].startswith('--'):
            werte += [x for x in args[j].replace(',', ' ').split() if x]
            j += 1
        if not werte:
            raise SystemExit('--kapitel ohne Kapitelnummer.')
        nurkap = set(nurkap or set()) | {str(int(x)) for x in werte}
        del args[k:j]
    # Ohne diesen Schalter meldet der Kapitelfilter auch die Zeilen, in
    # denen das eigene Kapitel die MEHRHEIT stellt und ein fremder Vers
    # abweicht. Das ist wertvoll — mehrere Altlasten in Matthaeus sind
    # nur so gefunden worden —, aber wer sein eigenes Kapitel abnehmen
    # will, ertrinkt darin. Gewuenscht von den Agenten fuer Luc 16 und
    # Luc 22.
    nur_eigene = '--nur-eigene' in args
    if nur_eigene:
        args.remove('--nur-eigene')
    gegen = []
    while '--gegen' in args:
        k = args.index('--gegen')
        j = k + 1
        while j < len(args) and args[j].isdigit() and int(args[j]) < 67:
            j += 1
        gegen += [int(x) for x in args[k + 1:j]]
        del args[k:j]
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
    if len(args) > 1:
        raise SystemExit(
            f'Zu viele Positionsargumente: {" ".join(args)}.\n'
            'Bis heute wurden die ueberzaehligen stillschweigend '
            'weggeworfen — ein Lauf mit `--kapitel 13 14 15` filterte '
            'in Wahrheit nur auf 13 und sah trotzdem sauber aus.')
    nr = int(args[0])
    # `--gegen 41` beim Lauf ueber 41 waere derselbe Selbstvergleich, an
    # dem in Matthaeus jeder `paketcheck`-Lauf leer durchlief.
    gegen = [b for b in gegen if b != nr]
    src = C.load_source(nr)
    ch = src['chapters'] if 'chapters' in src else src
    try:
        anno = C.load_anno(nr)['chapters']
    except Exception:
        anno = {}
    anno = dict(anno)
    anno.update(extra)

    annos = {nr: anno}
    quelle = []

    def einlesen(b, kapitel):
        for k in sorted(kapitel, key=int):
            for v in sorted(kapitel[k], key=int):
                roh = kapitel[k][v].split()
                toks, pos = [], []
                for i, x in enumerate(roh):
                    t = x.strip('.,;:!?„“"’')
                    if t:
                        toks.append(t)
                        pos.append(i)      # die Originalposition merken
                quelle.append(((b, k, v), toks, pos))

    einlesen(nr, ch)
    for b in gegen:
        s2 = C.load_source(b)
        try:
            annos[b] = C.load_anno(b)['chapters']
        except Exception:
            continue
        einlesen(b, s2['chapters'] if 'chapters' in s2 else s2)

    print(f'# Zeichengleichheit: {C.book_name(nr)}\n')
    gleich = abweichend = ohne = 0
    # Dieselbe Abweichung erscheint in jedem Fenster, das sie enthaelt.
    # Ueber die Buchgrenze sind das viele: der Agent fuer Marc 8 bekam
    # EINEN Befund (8,2 `cette`) elfmal gemeldet, und zwei echte unter
    # 22 Bloecken. Gezeigt wird jede Abweichung jetzt einmal — beim
    # laengsten Block, der sie traegt, denn `folgen()` liefert absteigend
    # nach Laenge.
    gesehen_abw = set()
    doppelt = 0
    for g, orte in folgen(quelle, minlen):
        gruppen = {}
        eigen = False
        for (b, k, v), pp in orte:
            a = annos.get(b, {})
            if k not in a or v not in a[k]:
                continue
            marke = f'{k},{v}' if b == nr else f'{C.book_name(b)} {k},{v}'
            if b == nr:
                eigen = True
            gruppen.setdefault(signatur(a[k][v], pp), []).append(marke)
        # Ein Block, an dem das eigene Buch gar nicht beteiligt ist, ist
        # eine Wiederholung INNERHALB des Vergleichsbuchs — nicht die
        # Frage, die hier gestellt wird.
        if gegen and not eigen:
            continue
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
            if nurkap is not None:
                eigen_wo = any(w.split(',')[0] in nurkap for w in wo)
                eigen_haupt = any(w.split(',')[0] in nurkap
                                  for w in haupt[1])
                if not eigen_wo and (nur_eigene or not eigen_haupt):
                    continue
            for idx, (a, b) in enumerate(zip(haupt[0][0], sig[0])):
                if a != b:
                    marke = (tuple(wo), tuple(haupt[1]), g[idx], a, b)
                    if marke in gesehen_abw:
                        doppelt += 1
                        continue
                    gesehen_abw.add(marke)
                    if kopf:
                        print(kopf)
                        kopf = ''
                    print(f'   {", ".join(wo)}  bei `{g[idx]}`:')
                    print(f'      hier  {b}')
                    print(f'      dort  {a}  ({", ".join(haupt[1])})')
            if haupt[0][1] != sig[1]:
                marke = (tuple(wo), tuple(haupt[1]), 'MW', haupt[0][1], sig[1])
                if marke in gesehen_abw:
                    doppelt += 1
                else:
                    gesehen_abw.add(marke)
                    if kopf:
                        print(kopf)
                        kopf = ''
                    print(f'   {", ".join(wo)}  Mehrwoerter: {sig[1] or "keine"}')
                    print(f'      dort  {haupt[0][1] or "keine"}')
        print()
    print(f'{gleich} Folgen zeichengleich, {abweichend} mit Abweichung'
          + (f', {ohne} noch nicht annotiert' if ohne else '') + '.')
    if doppelt:
        print(f'{doppelt} Wiederholungen derselben Abweichung in kuerzeren '
              'Fenstern sind weggelassen.')
    if abweichend:
        print('Jede Abweichung am Vers pruefen — Satzposition, Kasus, '
              'Genus,\nNumerus und Funktion sind haeufige und richtige '
              'Gruende.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
