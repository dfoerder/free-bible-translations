"""Feste Wendungen, die der Bestand als Mehrwort-Eintrag führt — fehlen sie?

    konvention.py <buchNr> <kapitel …>

Zwei Fehlalarmklassen sind behoben, beide von Agenten gemeldet: zwei Vorkommen
desselben Einleitworts (Neh 6,10) und das in den Infinitiv **inkorporierte
`zu`** (Est 6,4 `um … vorzuschlagen`), wo der Eintrag frueher endet als das
naechste freie `zu`.

Kapitel 4 hat gemeldet, dass Esra 1–3 `um zu` und `so wie` nicht als
Mehrwort-Einträge führt, obwohl der Bestand sie 267- bzw. 91-mal kennt. Kein
Prüfskript meldet das: strukturell ist ein fehlender Mehrwort-Eintrag kein
Fehler. Dieses Skript sucht die Wortfolge im Quelltext und fragt, ob ein
Eintrag darauf liegt.
"""
import sys, json, glob, os, collections
sys.path.insert(0,'/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import common as C

OUT=os.environ.get('ANNO_OUT')
if not OUT:
    sys.exit('ANNO_OUT nicht gesetzt — auf den out/-Ordner der laufenden '
             'Arbeit zeigen lassen: export ANNO_OUT=…/scratchpad/<buch>/out')
if not OUT.endswith('/'): OUT += '/'

# Wendungen aus zwei Tokens, die im Bestand oft genug als Mehrwort geführt sind,
# dass ein Fehlen erklärungsbedürftig ist. Erstes Token, letztes Token, Höchstabstand.
WENDUNGEN=[('um','zu',18),('so','wie',1),('genau','wie',1),('nicht','mehr',1),('wie','wenn',1)]

bestand=collections.Counter()
for p in sorted(glob.glob(os.path.join(C.ANNO_DIR,'*_multi.json'))):
    d=json.load(open(p,encoding='utf-8'))
    for kap,verse in d['chapters'].items():
        for v,ee in verse.items():
            for e in ee:
                if C.is_multi(e): bestand[e.get('lemma')]+=1

nr=int(sys.argv[1]); kaps=sys.argv[2:]
src=json.load(open(f'{C.SRC_DIR}/{nr}_l1912mod.json',encoding='utf-8'))['chapters']
offen=0
for kap in kaps:
    d=json.load(open(f'{OUT}{nr}/ch{kap}.json',encoding='utf-8'))
    for v in sorted(d, key=int):
        toks=[C.strip_punct(t) for t in src[kap][v].split()]
        belegt={(e['pos'], (e.get('parts') or [e['pos'],e.get('pos_end')])[-1])
                for e in d[v] if C.is_multi(e)}
        # Ein Mehrwort-Eintrag, der an derselben Position beginnt und dasselbe
        # Lemma traegt, deckt die Wendung auch dann ab, wenn er frueher endet:
        # bei `um ... vorzuschlagen` ist das `zu` in den Infinitiv inkorporiert,
        # der Eintrag steht auf [20,23], das freie `zu` des Objektsatzes erst
        # auf 28. Der Bestand fuehrt diese Bauform 14-mal (2Koen 3,10
        # `um auszuliefern`, 2Chr 26,16 `um darzubringen`). Ohne diese Zeile
        # meldet das Skript dort eine Luecke, die es nicht gibt.
        beginnt={(e['pos'], e.get('lemma')) for e in d[v] if C.is_multi(e)}
        roh=src[kap][v].split()
        for a,b,maxd in WENDUNGEN:
            for i,t in enumerate(toks):
                if t.lower()!=a: continue
                for j in range(i+1, min(i+maxd+1, len(toks))):
                    # Ein zweites `a` oder ein alleinstehender Gedankenstrich
                    # beendet die Suche: in Neh 6,10 stehen zwei `um`, das
                    # erste ohne eigenes `zu` (`um dich umzubringen`). Ohne
                    # den Abbruch paart das Skript `um` (37) mit dem `zu`
                    # (47) des zweiten Teilsatzes und meldet eine Luecke,
                    # die es nicht gibt.
                    if toks[j].lower()==a or C.is_punct_only(roh[j]):
                        break
                    if toks[j].lower()==b:
                        lem=f'{a} {b}'
                        if (i,j) not in belegt and (i,lem) not in beginnt:
                            offen+=1
                            print(f'  {nr} {kap},{v} pos {i}–{j}  «{lem}»  kein Mehrwort-Eintrag '
                                  f'(Bestand: {bestand[lem]}×)  | {" ".join(toks[i:j+1])[:60]}')
                        break
print(f'\n{offen} Stellen ohne Eintrag')
