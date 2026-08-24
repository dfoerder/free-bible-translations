"""Vorab-Bindungstabelle aus dem Bestand — maschinell, nicht von Hand.

    vorab.py <buchNr> <kapitel …>

In Welle 1 waren acht von 54 handgetippten Levels falsch. Diese Tabelle
entsteht deshalb aus dem Bestand: für jede Wortform der genannten Kapitel,
die im Bestand belegt ist, die häufigste Lesart mit Lemma, Level und
Belegzahl. Zeigt nur Formen, die in **mehreren** Kapiteln der Welle stehen —
genau die, an denen parallele Agenten auseinanderlaufen.
"""
import sys, json, glob, os, collections
sys.path.insert(0,'/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import hints, qa, common as C

FUNK = hints.FUNKTION | qa.FUNKTIONSWOERTER
nr=int(sys.argv[1]); kaps=sys.argv[2:]
src=json.load(open(f'{C.SRC_DIR}/{nr}_l1912mod.json',encoding='utf-8'))['chapters']

vorkommen=collections.defaultdict(set)
for k in kaps:
    for v,t in src[k].items():
        for tok in t.split():
            f=C.strip_punct(tok)
            if f and f.lower() not in FUNK and len(f)>2:
                vorkommen[f].add(k)

bestand=collections.defaultdict(collections.Counter)
for p in sorted(glob.glob(os.path.join(C.ANNO_DIR,'*_multi.json'))):
    d=json.load(open(p,encoding='utf-8'))
    for kap,verse in d['chapters'].items():
        for v,ee in verse.items():
            for e in ee:
                if C.is_multi(e): continue
                if e['form'] in vorkommen:
                    bestand[e['form']][(e['lemma'],e['level'],e['en'],e['es'],e['fr'],e['it'])]+=1

print(f'| Form | Lemma | Level | en · es · fr · it | Belege | Kapitel |')
print(f'|---|---|---|---|---|---|')
n=0
for f in sorted(vorkommen):
    if len(vorkommen[f])<2 or f not in bestand: continue
    (lem,lv,en,es,fr,it),c = bestand[f].most_common(1)[0]
    gesamt=sum(bestand[f].values())
    anteil=f'{c}' if c==gesamt else f'{c}/{gesamt}'
    print(f'| {f} | {lem} | {lv} | {en} · {es} · {fr} · {it} | {anteil} | {",".join(sorted(vorkommen[f], key=int))} |')
    n+=1
print(f'\n{n} Formen, die in mehreren Kapiteln der Welle stehen und im Bestand belegt sind.')
