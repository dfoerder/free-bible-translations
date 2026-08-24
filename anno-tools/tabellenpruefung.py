"""Prüft eine Vorab-Bindungstabelle Zeile für Zeile gegen den fertigen Bestand.

    tabellenpruefung.py <tabelle.md>

Die Level-Spalte ist bisher von Hand getippt worden und war in Welle 1 bei
acht von 54 Lemmata falsch. Das Level ist eine Lemma-Eigenschaft und im
Bestand je Lemma zu 100 % einheitlich — es lässt sich also mechanisch prüfen.
Dasselbe für die vier Glossen.
"""
import sys, json, glob, os, collections, re
sys.path.insert(0, '/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import common as C

lv = collections.defaultdict(collections.Counter)
gl = collections.defaultdict(collections.Counter)
for p in sorted(glob.glob(os.path.join(C.ANNO_DIR, '*_multi.json'))):
    d = json.load(open(p, encoding='utf-8'))
    for kap, verse in d['chapters'].items():
        for v, ee in verse.items():
            for e in ee:
                if e.get('lemma') and e.get('level'):
                    lv[e['lemma']][e['level']] += 1
                    gl[e['lemma']][(e['en'], e['es'], e['fr'], e['it'])] += 1

ROW = re.compile(r'^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(A1|A2|B1|B2|C1|C2)\s*\|\s*([^|]+?)\s*\|')
fehler = 0
for zeile in open(sys.argv[1], encoding='utf-8'):
    m = ROW.match(zeile)
    if not m:
        continue
    form, lemma, level, glossen = m.groups()
    if lemma not in lv:
        print(f'  [neu]   {lemma:<24} im Bestand unbelegt — nicht prüfbar')
        continue
    ist = lv[lemma].most_common()
    if ist[0][0] != level:
        fehler += 1
        print(f'  [LEVEL] {lemma:<24} Tabelle {level}  Bestand {dict(ist)}')
    teile = tuple(x.strip() for x in glossen.split('·'))
    if len(teile) == 4 and teile not in gl[lemma]:
        fehler += 1
        top = gl[lemma].most_common(1)[0]
        print(f'  [GLOSSE] {lemma:<23} Tabelle {" · ".join(teile)}')
        print(f'           {"":<23} Bestand {" · ".join(top[0])} ({top[1]}×)')
print(f'\n{fehler} Abweichungen')
sys.exit(1 if fehler else 0)
