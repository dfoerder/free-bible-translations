# Franzoesisches NT annotieren — was vorliegt und was zu tun ist

**Auftrag:** die Buecher 40-66 des `lsg1910mod` mit Wort-fuer-Wort-Glossen
in **Englisch, Deutsch, Italienisch und Spanisch**. Die Gegenrichtung zur
bisherigen Arbeit: dort war Deutsch der annotierte Text und Franzoesisch
eine Glossenspalte.

**Stand: noch nicht begonnen.** Dies ist die Bestandsaufnahme.

## Was da ist

```
bibles-translations/fra/lsg1910mod/     66 Quelltextdateien
bible-reader/bibles/fra/lsg1910mod/     dieselben, App-Kopie
bible-reader/bibles/fra/lsg1910mod/anno/   existiert nicht
anno-quellen/fra/                       existiert nicht
```

Die Registry in `index.html` fuehrt `fra-lsg1910mod` mit
`hasAnno: false`, `annoDir: null`, `annoSuffix: null`. Nach dem ersten
gebauten Buch sind diese drei zu setzen — Vorbild ist der Eintrag
`deu-l1912mod`.

## Die Zeugen

Fuer die deutsche Arbeit waren es WEB, RV1909mod, LSG1910mod, RIV1927.
Fuer die franzoesische ist **LSG der Quelltext**, also treten an ihre
Stelle die vier Zielsprachen:

```
en   eng/web
de   deu/l1912mod        ← jetzt Zeuge statt Quelle
it   ita/riv1927
es   spa/rv1909mod
```

`deu/l1912mod` ist als Zeuge besonders wertvoll: es ist **vollstaendig
annotiert**, und seine Glossen enthalten bereits eine franzoesische
Spalte. Fuer jedes franzoesische Wort laesst sich damit nachschlagen,
welches deutsche Wort ihm im Bestand gegenuebersteht — eine Bruecke, die
es bei der deutschen Arbeit nicht gab.

## Was an der Werkzeugkette zu tun ist

`common.py` ist an sechs Stellen fest verdrahtet:

```
SRC_DIR   bibles/deu/l1912mod
QUELLEN   anno-quellen/deu/l1912mod
Dateinamen  <nr>_l1912mod.json  und  <nr>_l1912mod_multi.json  (3 Stellen)
LANGS     ['en','es','fr','it']
```

Vorschlag: eine Umgebungsvariable **`ANNO_EDITION`** (Default
`deu/l1912mod`), aus der sich Verzeichnis, Dateisuffix und Sprachliste
ableiten. Dann laufen alle 43 Werkzeuge ohne weitere Aenderung mit —
`WERKZEUGE.md` listet sie.

**Eigene Pfade ausserhalb von `common.py`** haben mindestens
`vorgabecheck.ausgabentext()` und `kapitelgrenzen.flach()`; beide bauen
ihre Ausgabenliste selbst und muessen mitgezogen werden.

Die **Level** bedeuten dann CEFR aus Sicht von *Franzoesisch*lernenden,
nicht von Deutschlernenden — `SPEC.md` sagt das an einer Stelle
ausdruecklich und muss dort verallgemeinert werden.

## Vorgeschlagene Reihenfolge

1. `common.py` parametrisieren, die zwei Werkzeuge mit eigenen Pfaden
   nachziehen.
2. **Ein kurzes Buch als Pilot** — Judas (25 Verse, ein Kapitel) oder
   Philemon (25). Die Kette einmal ganz durchlaufen lassen: hints,
   lexicon, ausgaben, selfcheck, glosskollision, buildbook, validate.
   Erst dann steht fest, was noch klemmt.
3. Danach **Matthaeus** — das erste grosse Buch legt die Bindungen fuer
   das ganze NT fest, so wie 1. Mose es fuer das AT getan hat.

## Was aus der deutschen Arbeit uebertragbar ist

Alles Verfahrensmaessige: ein Agent je Kapitel, Pakete zu drei Kapiteln,
`wiederholungen.py` vor der Arbeit, `folgencheck.py` beim Einsammeln,
beide Promptpruefungen vor dem Start. **Nicht uebertragbar** sind die
inhaltlichen Bindungen: `BINDUNGEN_AT.md`, die Wortfelder und die
`spricht`-Stellungsregel gelten fuer den deutschen Text.
