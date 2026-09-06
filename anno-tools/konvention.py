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
# Feste Wendungen je Quelltextsprache. Die deutsche Liste traf im
# franzoesischen Text nichts, und der Lauf meldete „0 Stellen ohne
# Eintrag" — ein Leerlauf, der wie ein sauberer Lauf aussieht. Genau der
# Fehlertyp, gegen den der Abbruch bei fehlenden Kapitelnummern unten
# gebaut ist, nur eine Ebene tiefer. Gemeldet vom Agenten des
# franzoesischen Pilotbuchs.
WENDUNGEN_JE_SPRACHE = {
    'de': [('um','zu',18),('so','wie',1),('genau','wie',1),
           ('nicht','mehr',1),('wie','wenn',1)],
    'fr': [('afin','de',1),('au','contraire',1),('contre','nature',1),
           ('depuis','longtemps',1),('à','cause',1),
           ('ne','pas',6),('une','fois',1),('au','sujet',1),
           ('c','est',1),('parce','que',1),
           # `il y` allein ist keine Wendung: `Il y resta` heisst „er blieb
           # dort", das `y` ist das Ortsadverb. Existenziell wird es erst
           # mit einer Form von `avoir` dahinter. Gemeldet vom Agenten fuer
           # Matthaeus 2, nachdem die Regel dort zweimal falsch anschlug.
           ('il','y',1,{'a','avait','aura','ait','eut','aurait','aient'})],
}
WENDUNGEN=WENDUNGEN_JE_SPRACHE.get(C.LANG, [])
if not WENDUNGEN:
    raise SystemExit(f'Fuer die Quelltextsprache {C.LANG!r} sind keine '
                     'Wendungen hinterlegt — dieser Lauf wuerde NICHTS '
                     'pruefen und trotzdem "0" melden.')

bestand=collections.Counter()
for p in sorted(glob.glob(os.path.join(C.ANNO_DIR,f'*{C.ANNO_SUFFIX}'))):
    d=json.load(open(p,encoding='utf-8'))
    for kap,verse in d['chapters'].items():
        for v,ee in verse.items():
            for e in ee:
                if C.is_multi(e): bestand[e.get('lemma')]+=1

nr=int(sys.argv[1]); kaps=sys.argv[2:]

# Ohne Kapitelnummern lief die Schleife ueber eine leere Liste und meldete
# "0" — ein Leerlauf, der wie ein sauberer Lauf aussieht. In Jeremia hat das
# `levelcheck.py` paketlang verdeckt (23 echte Levelfehler in Paket 17), in
# Hesekiel `konvention.py` vier Pakete lang. Deshalb: lieber laut abbrechen.
if not kaps:
    raise SystemExit(
        'Kapitelnummern fehlen — ohne sie prueft dieses Skript NICHTS.\n'
        'Aufruf: %s <buchNr> <kapitel> [<kapitel> ...]' % sys.argv[0])
src=json.load(open(f'{C.SRC_DIR}/{nr}{C.TEXT_SUFFIX}',encoding='utf-8'))['chapters']
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
        # Welcher Mehrwort-Eintrag deckt eine Position sonst ab? Bei den
        # berechtigten Fehlalarmen (`um Gnade zu bitten`) liegt dort ein
        # anderes Lemma, das das Einleitwort selbst enthaelt. Das mitzudrucken
        # spart das Nachschlagen: Esra 8,22 und Est 4,8 haben es zweimal
        # gekostet.
        deckung={}
        for e in d[v]:
            if not C.is_multi(e): continue
            for pp in C.covered(e):
                deckung.setdefault(pp, e.get('lemma'))
        roh=src[kap][v].split()
        for regel in WENDUNGEN:
            a, b, maxd = regel[0], regel[1], regel[2]
            # Optional: welches Token unmittelbar hinter `b` stehen muss,
            # damit die Wendung ueberhaupt vorliegt.
            danach = regel[3] if len(regel) > 3 else None
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
                        if danach is not None and (
                                j + 1 >= len(toks)
                                or toks[j + 1].lower() not in danach):
                            break
                        lem=f'{a} {b}'
                        # Eine Bestandswendung wird auch von ihrer LAENGEREN
                        # Form gedeckt: in `au sujet du` steckt das kontrahierte
                        # `de`, der Eintrag traegt deshalb das Lemma
                        # `au sujet de` und begann fuer die Probe mit dem
                        # falschen Namen. Im Franzoesischen trifft das jede
                        # Wendung, die auf `de` oder `à` endet — gemeldet vom
                        # Agenten fuer Matthaeus 6.
                        laenger = any(p == i and (lm or '').split()[:2] == [a, b]
                                      for p, lm in beginnt)
                        if (i,j) not in belegt and (i,lem) not in beginnt \
                                and not laenger:
                            offen+=1
                            hinweis = ''
                            anderes = deckung.get(i)
                            if anderes and a in anderes.split():
                                hinweis = (f'  ← an pos {i} liegt «{anderes}»; '
                                           f'das Einleitwort gehoert vermutlich dorthin')
                            print(f'  {nr} {kap},{v} pos {i}–{j}  «{lem}»  kein Mehrwort-Eintrag '
                                  f'(Bestand: {bestand[lem]}×)  | {" ".join(toks[i:j+1])[:60]}'
                                  f'{hinweis}')
                        break
print(f'\n{offen} Stellen ohne Eintrag')
