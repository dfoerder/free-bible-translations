"""Vorab-Bindungstabelle aus dem Bestand — maschinell, nicht von Hand.

**Großgeschriebene Formen tragen einen Warnhinweis mit Belegstelle.** Die
Tabelle schlägt die Bestandslesart einer Wortform nach und weiß nicht, ob
derselbe Träger gemeint ist. In Ester 5 hat die Tabelle für `Seres` die Lesart
*Sheresh* aus 1Chr 7,16 angeboten — dort ist Seres der Bruder des Peres, in
Ester ist es Hamans Frau, die alle vier Ausgaben *Zeresh* schreiben. Der Agent
hat es an den Ausgaben geprüft und die Tabelle widerlegt. Seither steht bei
jeder großgeschriebenen Zeile die Belegstelle dabei, damit sie aufschlagbar
ist.

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
src=json.load(open(f'{C.SRC_DIR}/{nr}{C.TEXT_SUFFIX}',encoding='utf-8'))['chapters']

vorkommen=collections.defaultdict(set)
for k in kaps:
    for v,t in src[k].items():
        for tok in t.split():
            f=C.strip_punct(tok)
            if f and f.lower() not in FUNK and len(f)>2:
                vorkommen[f].add(k)

stellen=collections.defaultdict(list)
bestand=collections.defaultdict(collections.Counter)
for p in sorted(glob.glob(os.path.join(C.ANNO_DIR,'*_multi.json'))):
    d=json.load(open(p,encoding='utf-8'))
    for kap,verse in d['chapters'].items():
        for v,ee in verse.items():
            for e in ee:
                if C.is_multi(e): continue
                if e['form'] in vorkommen:
                    key=(e['lemma'],e['level'],e['en'],e['es'],e['fr'],e['it'])
                    bestand[e['form']][key]+=1
                    if len(stellen[(e['form'],key)])<3:
                        stellen[(e['form'],key)].append(f'{d["name"]} {kap},{v}')

print('**Warnung zu großgeschriebenen Formen.** Die Tabelle schlägt die')
print('Bestandslesart einer **Wortform** nach — sie weiß nicht, ob dieselbe')
print('Person oder derselbe Ort gemeint ist. Bei Eigennamen führt das aktiv in')
print('die Irre: `Seres` steht im Bestand einmal (1Chr 7,16, der Bruder des')
print('Peres, *Sheresh*), in Ester ist es Hamans Frau (*Zeresh*). Bei jeder')
print('großgeschriebenen Zeile deshalb **die Belegstelle aufschlagen** und')
print('prüfen, ob es derselbe Träger ist — sonst gilt die Referenzausgabe.\n')
print(f'| Form | Lemma | Level | en · es · fr · it | Belege | Kapitel |')
print(f'|---|---|---|---|---|---|')
n=0
for f in sorted(vorkommen):
    if len(vorkommen[f])<2 or f not in bestand: continue
    (lem,lv,en,es,fr,it),c = bestand[f].most_common(1)[0]
    gesamt=sum(bestand[f].values())
    anteil=f'{c}' if c==gesamt else f'{c}/{gesamt}'
    # Bei Eigennamen ist die blosse Zahl wertlos - die Belegstelle entscheidet.
    if f[:1].isupper():
        anteil += ' ⚠ ' + '; '.join(stellen[(f,(lem,lv,en,es,fr,it))])
    print(f'| {f} | {lem} | {lv} | {en} · {es} · {fr} · {it} | {anteil} | {",".join(sorted(vorkommen[f], key=int))} |')
    n+=1
print(f'\n{n} Formen, die in mehreren Kapiteln der Welle stehen und im Bestand belegt sind.')
