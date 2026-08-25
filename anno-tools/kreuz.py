"""Kreuzabgleich der gleichzeitig gelaufenen Kapitel einer Welle.

    kreuz.py <buchNr> <kapitel> <kapitel> [...]

Hält die gemeinsamen Inhaltswortformen der Kapitel gegeneinander. Funktionswörter
und Mehrwort-Einträge bleiben ausgeblendet — sie weichen legitim ständig ab.

Findet keine Fehler, sondern Divergenzen. In 2. Chronik hat dieses Verfahren über
vierzig echte Abweichungen gefunden, und kein Prüfskript hatte eine davon gemeldet.
"""
import sys, os, json, collections
sys.path.insert(0,'/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import hints, qa, common as C

OUT=os.environ.get('ANNO_OUT')
if not OUT:
    sys.exit('ANNO_OUT nicht gesetzt — auf den out/-Ordner der laufenden '
             'Arbeit zeigen lassen: export ANNO_OUT=…/scratchpad/<buch>/out')
if not OUT.endswith('/'): OUT += '/'
FUNK = hints.FUNKTION | qa.FUNKTIONSWOERTER

nr=int(sys.argv[1]); kaps=[int(x) for x in sys.argv[2:]]
lesarten=collections.defaultdict(lambda: collections.defaultdict(list))
for k in kaps:
    d=json.load(open(f'{OUT}{nr}/ch{k}.json',encoding='utf-8'))
    for v,ee in d.items():
        for e in ee:
            if 'pos_end' in e or 'parts' in e: continue
            f=e['form']
            if f.lower() in FUNK or e['lemma'].lower() in FUNK or len(f)<3: continue
            lesarten[f][(e['level'],e['en'],e['es'],e['fr'],e['it'])].append(f'{k},{v}')

gemeinsam=0; divergent=0
for f in sorted(lesarten):
    kap={s.split(',')[0] for lst in lesarten[f].values() for s in lst}
    if len(kap)<2: continue
    gemeinsam+=1
    if len(lesarten[f])>1:
        divergent+=1
        print(f'\n## {f}')
        for k,stellen in sorted(lesarten[f].items(), key=lambda kv:-len(kv[1])):
            print(f'   {len(stellen):3d}× [{k[0]}] {k[1]} · {k[2]} · {k[3]} · {k[4]}')
            print(f'        {", ".join(stellen[:8])}{" …" if len(stellen)>8 else ""}')
print(f'\n{gemeinsam} gemeinsame Inhaltswortformen, {divergent} mit abweichenden Lesarten')
