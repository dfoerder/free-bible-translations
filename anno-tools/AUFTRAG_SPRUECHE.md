# Auftrag: ein Kapitel der Sprüche annotieren (Buch 20, deu/l1912mod)

Alle Werkzeuge liegen in `/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools`.
Dort arbeiten (`cd`), die Skripte mit `python3 <name>.py` aufrufen.

Dein Arbeitsordner steht in deinem Prompt:

```
export ANNO_OUT=<der Ordner aus deinem Prompt>
```

Das fertige Kapitel schreibst du nach `$ANNO_OUT/20/ch<kapitel>.json`.

## Vorbereitung — in dieser Reihenfolge

1. `anno-tools/SPEC.md` — Datenformat und Verbote.
2. `anno-tools/AUFTRAG_AT.md` — der allgemeine Ablauf für das Alte Testament.
   **Ganz lesen.** Besonders „Die drei Fallen des Alten Testaments" und
   „Die Glossen folgen den vier Referenzausgaben".
3. `anno-tools/WORTFELD_SPRUECHE.md` — was für das ganze Buch feststeht:
   die Weisheits- und Torheitsbegriffe, die nach Testamenten getrennt
   ausgezählten Bindungen, die Homographen und Kollisionen des Buches.
4. `anno-tools/DUBLETTEN_SPRUECHE.md` — die 26 buchinternen Verspaare. Steht
   dein Kapitel dort, ist der Partner entweder schon fertig (dann übernimmst du
   seine Glossenreihe, wo der Text wörtlich gleich ist) oder er kommt noch
   (dann ist deine Reihe die Vorlage). **Wo der Text nicht wörtlich gleich ist,
   nicht abschreiben** — die Ähnlichkeitszahl steht bei jedem Paar.
5. `anno-tools/BINDUNGEN_AT.md`, Abschnitt zu Buch 20 und die allgemeinen
   Bindungen.
6. Den **Quelltext** deines Kapitels lesen:
   `bible-reader/bibles/deu/l1912mod/20_l1912mod.json` → `chapters["<kapitel>"]`.
   Nicht aus der Bibelkenntnis arbeiten.

## Die Werkzeuge, die du je Kapitel laufen lässt

```
python3 ausgaben.py 20 <kap>            # die vier Ausgaben, inhaltlich ausgerichtet
python3 lexicon.py 20 <kap>             # wie der Bestand jede Wortform übersetzt
python3 hints.py 20 <kap>               # unbelegte Formen, Kollisionen, Mehrdeutigkeit
python3 parallelen.py 20 <kap>          # Parallelstellen im Bestand
```

**`ausgaben.py` ist Pflicht.** Anders als im Psalter ist die Verszählung hier
unproblematisch: über alle 31 Kapitel stimmt die Verszahl der vier Ausgaben mit
der deutschen **exakt** überein (gemessen, 0 Abweichungen), und der von
`ausgaben.py` errechnete Versatz ist überall `+0`. Das entbindet nicht vom Lauf —
das Werkzeug zeigt die vier Vorlagen nebeneinander, und genau das brauchst du
bei Sprichwörtern, die im Deutschen mehrdeutig sind.

## Was dieses Buch besonders macht

**Jeder Vers steht für sich.** Ab Kapitel 10 sind es Einzelsprüche ohne
Zusammenhang. Es gibt keinen Erzählfaden, aus dem sich eine Lesart ergibt —
was einen Vers entscheidet, ist der **Parallelismus** in ihm selbst: die zweite
Vershälfte sagt dasselbe noch einmal oder das Gegenteil. Sie ist deine beste
Quelle für die Bedeutung eines mehrdeutigen Wortes, noch vor den Ausgaben.

**Das Buch lebt von Synonymreihen.** `Weisheit · Klugheit · Einsicht ·
Verstand · Erkenntnis · Erziehung · Zucht · Unterweisung · Lehre · Weisung`
stehen teils in **einem** Vers (1,2–1,7 hat sechs davon), ebenso
`Narr · Tor · Spötter · Einfältiger · Unverständiger`. Zwei deutsche Wörter im
selben Vers dürfen nicht dieselbe Glosse tragen. `WORTFELD_SPRUECHE.md` hält
fest, was dafür schon festgelegt ist; jede weitere Auflösung meldest du.

## Arbeit

Abschnitte von 8–10 Versen. **Nach jedem Abschnitt wegschreiben**
(`ch<kap>.part<M>.json`), erst am Ende zu `ch<kap>.json` zusammenfassen.
Agenten sind schon mitten im Lauf abgebrochen; gerettet wurde nur, was
weggeschrieben war.

Übersetzungen **direkt am Eintrags-Dict** zuweisen — nie eine Liste von Glossen
bauen und hinterher per Index zusammenführen.

Feste Wendungen, die der Bestand als Mehrwort führt, nicht vergessen. Ein
fehlender Mehrwort-Eintrag ist für `selfcheck.py` und `qa.py` **prinzipiell
unsichtbar**.

## Prüfung vor der Abgabe — alle fünf müssen gelaufen sein

```
python3 selfcheck.py 20 <kap> $ANNO_OUT/20/ch<kap>.json
python3 qa.py --kapitel 20 <kap> $ANNO_OUT/20/ch<kap>.json
python3 konvention.py 20 <kap>
python3 sweep.py 20 --kapitel <kap>
python3 glosskollision.py --datei 20 <kap> $ANNO_OUT/20/ch<kap>.json
```

`selfcheck.py` muss fehlerfrei durchlaufen — das ist die harte Bedingung.

**`glosskollision.py` ist bei diesem Buch der wichtigste Verdachtslauf.** Es
vergleicht die Glossen, die du tatsächlich gesetzt hast, Vers für Vers und
Sprache für Sprache, und meldet zwei deutsche Wörter, die dieselbe tragen. Das
ist der blinde Fleck von `hints.py`: das sucht im Quelltext gegen den Bestand
und findet nichts, wenn eine Form unbelegt ist oder die Kollision erst durch
deine eigene Entscheidung entsteht. Bei einem Buch aus Synonymreihen ist das
der Regelfall, nicht die Ausnahme. Lies die Rangfolge im Kopf des Skripts:
**„1 von 4" ist der stärkste Verdacht**, nicht der schwächste. Den Abschnitt
„geschlossene Wortarten" mitlesen und `--nurinhalt` **nicht** setzen.

`qa.py`, `konvention.py` und `sweep.py` melden **Verdacht, keine Fehler**:
jeden Treffer am Vers ansehen und entscheiden.

## Ein Unterschied, der kein Befund ist

Die **Kapitelquelle** und das **gebaute Buch** können sich im `level`
unterscheiden. `buildbook.py` zieht beim Bauen zwei Angleichungen durch — je
Bedeutung und je Lemma über den ganzen Bestand — und schreibt das Ergebnis nur
in die gebaute Datei. **Nicht als Befund melden.** Was zu melden ist: ein
Level, das gegen die Bestandsmehrheit steht.

## Abgabe

Eine Datei `$ANNO_OUT/20/ch<kap>.json`, Inhalt `{"<vers>": [...]}` über **alle**
Verse des Kapitels.

Dazu ein kurzer Bericht:

- **Wortfeld**: die Begriffe, die über dein Kapitel hinauslaufen, mit gewählter
  Glosse und Level. Sie kommen ins `WORTFELD_SPRUECHE.md`.
- **Abweichungen vom Auftrag**: wo der Quelltext etwas anderes sagt als ein
  Hinweis. Das ist der häufigste echte Befund.
- **Befunde im Bestand**: wo der Lexikon-Extrakt uneinheitlich ist oder eine
  Bindung falsch aussieht. Nicht selbst korpusweit korrigieren — melden.
- **Befunde in den Ausgaben**: fehlende Verse, Importartefakte.

## Was nie passiert

- ins Repository `bible-reader` schreiben (nur lesen)
- eigene Subagenten starten
- einen Namen deuten, den der Text nicht selbst deutet
- ein Kapitel als „fertig" melden, das `selfcheck.py` nicht sauber durchläuft
