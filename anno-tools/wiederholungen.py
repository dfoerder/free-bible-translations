#!/usr/bin/env python3
"""Welche Wortfolgen wiederholt der Quelltext eines Buches?

    wiederholungen.py <buchNr> [--min <tokens>] [--ab <vorkommen>]
    wiederholungen.py <buchNr> --kapitel <k> [<k> ...]

## Der Anlass

`dubletten.py` vergleicht **ganze Verse** und meldet erst ab 60 Prozent
gemeinsamer Formen. Damit findet es die Gerichtsformel in Amos 1-2, aber
**nicht** den Refrain „Doch ihr seid nicht zu mir umgekehrt, spricht der
HERR", der in Amos 4,6 · 4,8 · 4,9 · 4,10 · 4,11 fuenfmal am Versende
steht — die Verse ringsum sind zu verschieden.

Genau diese Teilvers-Wiederholungen sind aber das, was zwei Agenten
verschieden entscheiden, wenn niemand es ihnen vorher sagt. In Joel fiel
`einberufen` in 1,14 und 2,15 auseinander, obwohl die beiden Verse
woertlich gleich sind; gefunden wurde es erst beim Einsammeln.

Dieses Skript rechnet dieselbe Gegenrechnung **vor** der Arbeit, auf dem
Quelltext statt auf den fertigen Glossen. Das Ergebnis gehoert in die
Paketdatei: es sagt jedem Agenten, welche seiner Entscheidungen in einem
anderen Kapitel wiederkehren — auch ueber Paketgrenzen hinweg.

## Wie gelesen wird

Gemeldet wird die **laengste** Folge; kuerzere, die ganz in einer schon
gemeldeten stecken, werden unterdrueckt. Sortiert nach Haeufigkeit, dann
nach Laenge. Wo die Orte in verschiedenen Paketen liegen, ist die Folge
eine Bindung ueber die Paketgrenze — der frueheste Ort legt fest.

## Was die Gegenprobe am fertigen Bestand ergab

Dieselbe Rechnung, angewandt auf Daniel, Hosea und Joel und mit den
fertigen Glossen verglichen, meldet 13 Folgen mit abweichenden Reihen —
und **keine einzige davon ist ein Fehler**:

- **Joel** (2): beide waren beim Einsammeln schon geprueft. `ist` in
  1,15 gegen 2,11 ist es *está cerca* gegen *es grande*; `aus` in 4,18
  weicht aus, weil `von` im selben Vers *de · de* traegt.
- **Hosea** (1): 5,6 „**er** hat sich abgewandt" gegen 14,5 „**mein
  Zorn** hat sich abgewandt" — fr *détourné/détournée*, it
  *allontanato/allontanata*. Genuskongruenz mit dem Subjekt.
- **Daniel** (10): Kasus- und Personenwechsel. In 12,6 („fragte den
  Mann") steht fr *à l'*, in 12,7 („hoerte den Mann") *l'* — LSG liest
  an der ersten Stelle „dit **à** l'homme". Verbrektion, kein Fehler.

Das Werkzeug meldet also Verdachtsfaelle, keine Fehler — wie jedes andere
hier. Sein Wert liegt darin, sie **vor** der Arbeit zu zeigen statt nach
ihr: in Joel waeren beide Treffer ohne das Einsammeln stehen geblieben.
"""
import sys, re, collections
import common as C

TOKEN = re.compile(r'\b[\wÄÖÜäöüß-]+\b')


def folgen(quelle, minlen=4, maxlen=12):
    idx = collections.defaultdict(list)
    for ort, toks in quelle:
        for n in range(maxlen, minlen - 1, -1):
            for i in range(len(toks) - n + 1):
                idx[tuple(toks[i:i + n])].append(ort)
    gemeldet, out = set(), []
    for g in sorted(idx, key=lambda x: (-len(x), x)):
        orte = idx[g]
        if len(orte) < 2:
            continue
        if any(tuple(g[a:a + m]) in gemeldet
               for m in range(len(g), minlen - 1, -1)
               for a in range(len(g) - m + 1)):
            continue
        for a in range(len(g) - minlen + 1):
            for m in range(minlen, len(g) + 1):
                if a + m <= len(g):
                    gemeldet.add(tuple(g[a:a + m]))
        out.append((len(g), orte, ' '.join(g)))
    out.sort(key=lambda x: (-len(x[1]), -x[0]))
    return out


def main():
    args = [a for a in sys.argv[1:]]
    if not args or not args[0].isdigit():
        print(__doc__)
        return 2
    nr = int(args[0])
    minlen, ab, kapitel = 4, 2, None
    i = 1
    while i < len(args):
        if args[i] == '--min':
            minlen = int(args[i + 1]); i += 2
        elif args[i] == '--ab':
            ab = int(args[i + 1]); i += 2
        elif args[i] == '--kapitel':
            kapitel = set(args[i + 1:]); i = len(args)
        else:
            i += 1
    d = C.load_source(nr)['chapters']
    quelle = []
    for k in sorted(d, key=int):
        for v in sorted(d[k], key=int):
            quelle.append((f'{k},{v}', TOKEN.findall(d[k][v])))
    out = [x for x in folgen(quelle, minlen) if len(x[1]) >= ab]
    if kapitel:
        out = [x for x in out
               if any(o.split(',')[0] in kapitel for o in x[1])]
    print(f'# Wiederholte Wortfolgen: {C.book_name(nr)}')
    print(f'\nAb {minlen} Tokens, ab {ab} Vorkommen, ueber Versgrenzen hinweg.')
    print(f'**{len(out)} Folgen.** Der frueheste Ort legt die Reihe fest;'
          ' alle weiteren\nuebernehmen sie zeichengleich.\n')
    for L, orte, g in out:
        kaps = sorted({o.split(',')[0] for o in orte}, key=int)
        quer = '  ← ueber Kapitelgrenzen' if len(kaps) > 1 else ''
        print(f'  {len(orte)}× ({L} Tokens){quer}')
        print(f'      „{g}"')
        print(f'      {", ".join(orte)}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
