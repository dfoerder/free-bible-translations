"""Feste Wendungen, die der Bestand als Mehrwort-Eintrag führt — fehlen sie?

    konvention.py <buchNr> <kapitel …>

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
        for a,b,maxd in WENDUNGEN:
            for i,t in enumerate(toks):
                if t.lower()!=a: continue
                for j in range(i+1, min(i+maxd+1, len(toks))):
                    if toks[j].lower()==b:
                        lem=f'{a} {b}'
                        if (i,j) not in belegt:
                            offen+=1
                            print(f'  {nr} {kap},{v} pos {i}–{j}  «{lem}»  kein Mehrwort-Eintrag '
                                  f'(Bestand: {bestand[lem]}×)  | {" ".join(toks[i:j+1])[:60]}')
                        break
print(f'\n{offen} Stellen ohne Eintrag')
