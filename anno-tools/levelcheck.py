"""Level gegen den Bestand — je Lemma, vor dem Build.

    levelcheck.py <buchNr> <kapitel …> [--fix]

Das Level hängt am Lemma und ist im Bestand je Lemma fast immer zu 100 %
einheitlich. `buildbook.py` zieht abweichende Einträge beim Build ohnehin auf
die Korpusmehrheit — die Quelle soll dann nicht etwas anderes behaupten als das
Ergebnis, sonst wandert die Abweichung durch jeden Neubau mit.

Gemeldet wird nur, wo der Bestand **einheitlich** ist (eine einzige Lesart);
wo er selbst schwankt, entscheidet der Vers.

`--fix` **behält die Schreibweise der Datei bei**. Die Kapitelquellen stehen im
Bestand in zwei Formaten nebeneinander — eingerückt (`indent=1`, so schreiben
die Agenten) und einzeilig (so schreibt `C.write_compact`). Eine frühere
Fassung dieses Skripts hat immer einzeilig geschrieben; ein Lauf über alle
Bücher hat dadurch 615 Dateien umformatiert und einen Diff von 2,7 Millionen
Zeilen erzeugt, obwohl nur 396 Level-Felder zu ändern waren.
"""
import sys, json, glob, os, collections
sys.path.insert(0,'/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import common as C

OUT=os.environ.get('ANNO_OUT')
if not OUT:
    sys.exit('ANNO_OUT nicht gesetzt — auf den out/-Ordner der laufenden '
             'Arbeit zeigen lassen: export ANNO_OUT=…/scratchpad/<buch>/out')
if not OUT.endswith('/'): OUT += '/'
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
    roh=open(p,encoding='utf-8').read()
    eingerueckt=roh.count('\n')>1
    d=json.loads(roh)
    geaendert=0
    for v in sorted(d, key=int):
        for e in d[v]:
            l=e.get('lemma')
            if l not in lv or len(lv[l])>1: continue      # Bestand nicht einheitlich
            soll=next(iter(lv[l]))
            if e['level']!=soll:
                n+=1
                print(f"  {nr} {kap},{v} {e['form']:<20} lemma={l:<18} {e['level']} "
                      f"{'->' if fix else 'gegen'} {soll}  ({sum(lv[l].values())} Belege)")
                if fix: e['level']=soll; geaendert+=1
    # nur schreiben, wo wirklich etwas zu aendern war — sonst formatiert der
    # Lauf Dateien um, die er gar nicht anfassen muss
    if fix and geaendert:
        with open(p,'w',encoding='utf-8') as f:
            if eingerueckt: json.dump(d, f, ensure_ascii=False, indent=1)
            else: json.dump(d, f, ensure_ascii=False, separators=(',',':'))
print(f'\n{n} Abweichungen' + (' — korrigiert' if fix else ''))
