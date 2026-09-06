"""Blocktabelle fuer den Prompt — maschinell, nicht von Hand.

    bloecke.py <buchNr> <kap> <vers> <buchNr> <kap> <vers> [minlen]

In Welle 1 ist mir beim Abschreiben ein Zwei-Token-Block verloren gegangen
(Esra 1,1 pos 27 'sodass er', Versatz +6). Der Agent hat ihn gefunden, ich
nicht. Seither entsteht die Tabelle hier.
"""
import sys, json, difflib
sys.path.insert(0,'/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools')
import common as C

def toks(nr,kap,v):
    return json.load(open(f'{C.SRC_DIR}/{nr}{C.TEXT_SUFFIX}',encoding='utf-8'))['chapters'][kap][v].split()

n1,k1,v1,n2,k2,v2 = sys.argv[1:7]
minlen = int(sys.argv[7]) if len(sys.argv)>7 else 2
a,b = toks(n1,k1,v1), toks(n2,k2,v2)
sm = difflib.SequenceMatcher(None,[C.strip_punct(x) for x in a],[C.strip_punct(x) for x in b])
print(f'| A-pos | B-pos | Länge | Versatz | Wortlaut |')
print(f'|---|---|---|---|---|')
for bl in sm.get_matching_blocks():
    if bl.size>=minlen:
        print(f'| {bl.a} | {bl.b} | {bl.size} | **{bl.b-bl.a:+d}** | `{" ".join(a[bl.a:bl.a+bl.size])}` |')
print(f'\nA = {k1},{v1} ({len(a)} Tokens) · B = {k2},{v2} ({len(b)} Tokens) · Ähnlichkeit {sm.ratio():.2f}')
