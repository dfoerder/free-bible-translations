"""Level gegen den Bestand — je Lemma, vor dem Build.

    levelcheck.py <buchNr> <kapitel …> [--fix]

Das Level hängt am Lemma und ist im Bestand je Lemma fast immer zu 100 %
einheitlich. `buildbook.py` zieht abweichende Einträge beim Build ohnehin auf
die Korpusmehrheit — die Quelle soll dann nicht etwas anderes behaupten als das
Ergebnis, sonst wandert die Abweichung durch jeden Neubau mit.

Gemeldet wird nur, wo der Bestand **einheitlich** ist (eine einzige Lesart);
wo er selbst schwankt, entscheidet der Vers.
"""
import sys, json, glob, os, collections
sys.path.insert(0,'/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import common as C

OUT='/private/tmp/claude-502/-Users-dfoerd-Documents-projekte-bibel-bible-reader/3d1d1224-a30a-484b-869b-fa465569a632/scratchpad/esra/out/'
fix = '--fix' in sys.argv
argv = [a for a in sys.argv[1:] if a != '--fix']
nr, kaps = int(argv[0]), argv[1:]

lv=collections.defaultdict(collections.Counter)
for p in sorted(glob.glob(os.path.join(C.ANNO_DIR,'*_multi.json'))):
    d=json.load(open(p,encoding='utf-8'))
    for kap,verse in d['chapters'].items():
        for v,ee in verse.items():
            for e in ee:
                if e.get('lemma') and e.get('level'): lv[e['lemma']][e['level']]+=1

n=0
for kap in kaps:
    p=f'{OUT}{nr}/ch{kap}.json'
    d=json.load(open(p,encoding='utf-8'))
    for v in sorted(d, key=int):
        for e in d[v]:
            l=e.get('lemma')
            if l not in lv or len(lv[l])>1: continue      # Bestand nicht einheitlich
            soll=next(iter(lv[l]))
            if e['level']!=soll:
                n+=1
                print(f"  {nr} {kap},{v} {e['form']:<20} lemma={l:<18} {e['level']} "
                      f"{'->' if fix else 'gegen'} {soll}  ({sum(lv[l].values())} Belege)")
                if fix: e['level']=soll
    if fix: json.dump(d, open(p,'w',encoding='utf-8'), ensure_ascii=False)
print(f'\n{n} Abweichungen' + (' — korrigiert' if fix else ''))
