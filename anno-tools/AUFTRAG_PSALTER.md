# Auftrag: ein Paket Psalmen annotieren (Buch 19, deu/l1912mod)

Alle Werkzeuge liegen in `/Users/dfoerd/Documents/projekte/bibel/bibles-translations/anno-tools`.
Dort arbeiten (`cd`), die Skripte mit `python3 <name>.py` aufrufen.

Dein Arbeitsordner steht in deinem Prompt:

```
export ANNO_OUT=<der Ordner aus deinem Prompt>
```

Die fertigen Kapitel schreibst du nach `$ANNO_OUT/19/ch<psalm>.json`.

## Vorbereitung — in dieser Reihenfolge

1. `anno-tools/SPEC.md` — Datenformat und Verbote.
2. `anno-tools/AUFTRAG_AT.md` — der allgemeine Ablauf für das Alte Testament.
   **Ganz lesen.** Besonders „Die drei Fallen des Alten Testaments" und
   „Die Glossen folgen den vier Referenzausgaben".
3. `anno-tools/WORTFELD_PSALTER.md` — was für den ganzen Psalter feststeht:
   die Überschriftenbegriffe, die nach Testamenten getrennt ausgezählten
   Bindungen, die Kollisionen des Buches.
4. `anno-tools/VERSZAEHLUNG_PSALMEN.md` — die Verszählung.
5. Den **Quelltext** deiner Psalmen lesen:
   `bible-reader/bibles/deu/l1912mod/19_l1912mod.json` → `chapters["<psalm>"]`.
   Nicht aus der Bibelkenntnis arbeiten.

## Die Werkzeuge, die du je Psalm laufen lässt

```
python3 ausgaben.py 19 <psalm>            # die vier Ausgaben, inhaltlich ausgerichtet
python3 lexicon.py 19 <psalm>             # wie der Bestand jede Wortform übersetzt
python3 hints.py 19 <psalm>               # unbelegte Formen, Kollisionen, Mehrdeutigkeit
python3 parallelen.py 19 <psalm>          # Parallelstellen im Bestand (oft leer im Psalter)
```

**`ausgaben.py` ist Pflicht und ersetzt das Aufschlagen der Ausgaben von Hand.**
In 63 der 150 Psalmen ist der deutsche Vers 12 nicht der englische Vers 12 —
die deutsche Zählung führt die Überschrift als Vers 1, WEB, RV1909 und RIV1927
tun es nicht. Wer eine Ausgabe über die deutsche Versnummer aufschlägt,
glossiert aus dem falschen Vers, und es liest sich plausibel.

Wo `ausgaben.py` `FEHLT in der Datei der Ausgabe` schreibt, hat diese Ausgabe
für den Vers **keine Vorlage**. Nicht die Nachbarzeile nehmen — sie gehört zum
nächsten deutschen Vers. Die Glosse folgt dort dem Bestand und den anderen
Ausgaben.

## Arbeit

Abschnitte von 8–10 Versen. **Nach jedem Abschnitt wegschreiben**
(`ch<psalm>.part<M>.json`), erst am Ende zu `ch<psalm>.json` zusammenfassen.
Agenten sind schon mitten im Lauf abgebrochen; gerettet wurde nur, was
weggeschrieben war.

Übersetzungen **direkt am Eintrags-Dict** zuweisen — nie eine Liste von Glossen
bauen und hinterher per Index zusammenführen.

Feste Wendungen, die der Bestand als Mehrwort führt, nicht vergessen. Ein
fehlender Mehrwort-Eintrag ist für `selfcheck.py` und `qa.py` **prinzipiell
unsichtbar**.

## Prüfung vor der Abgabe — alle vier müssen sauber sein

```
python3 selfcheck.py 19 <psalm> $ANNO_OUT/19/ch<psalm>.json
python3 qa.py --kapitel 19 <psalm> $ANNO_OUT/19/ch<psalm>.json
python3 konvention.py 19 <psalm>
python3 sweep.py 19 --kapitel <psalm>
python3 glosskollision.py --datei 19 <psalm> $ANNO_OUT/19/ch<psalm>.json --nurinhalt
```

`selfcheck.py` muss fehlerfrei durchlaufen — das ist die harte Bedingung.

**`glosskollision.py` ist der wichtigste der Verdachtsläufe.** Es vergleicht
die Glossen, die du tatsächlich gesetzt hast, Vers für Vers und Sprache für
Sprache, und meldet zwei deutsche Wörter, die dieselbe tragen. Das ist der
blinde Fleck von `hints.py`: das sucht im Quelltext gegen den Bestand und findet
deshalb nichts, wenn eine Form unbelegt ist oder die Kollision erst durch deine
eigene Entscheidung entsteht. In vier Paketen sind so fünf Kollisionen
durchgerutscht (Ps 81,2 · 84,9 · 84,10 · 88,18 · 90,11), für zwei der Kapitel
meldete `hints.py` sogar **null Paare**. Lies die Rangfolge im Kopf des Skripts:
**„1 von 4" ist der stärkste Verdacht**, nicht der schwächste.

`qa.py`, `konvention.py` und `sweep.py` melden **Verdacht, keine Fehler**:
jeden Treffer am Vers ansehen und entscheiden. `sweep.py` sucht die
Mehrwort-Wendungen des Bestands im Quelltext und fragt, ob ein Eintrag darauf
liegt; ein Treffer kann auch wörtlich gemeint sein (`Er stand auf dem Berg`
ist kein `aufstehen`).

## Ein Unterschied, der kein Befund ist

Die **Kapitelquelle** und das **gebaute Buch** können sich im `level`
unterscheiden. `buildbook.py` zieht beim Bauen zwei Angleichungen durch — je
Bedeutung und je Lemma über den ganzen Bestand — und schreibt das Ergebnis nur
in die gebaute Datei. Ps 31,10 trägt in der Quelle `angst sein` als B2 und im
Buch als A2; beides ist richtig, die Quelle hält die Entscheidung des Agenten,
das Buch die korpusweite Vereinheitlichung.

**Nicht als Befund melden.** Was zu melden ist: ein Level, das gegen die
Bestandsmehrheit steht — dafür ist `levelcheck.py` da.

## Abgabe

Je Psalm eine Datei `$ANNO_OUT/19/ch<psalm>.json`, Inhalt `{"<vers>": [...]}`
über **alle** Verse.

Dazu ein kurzer Bericht:

- **Wortfeld**: die Begriffe, die über deine Psalmen hinauslaufen, mit
  gewählter Glosse und Level. Sie kommen ins `WORTFELD_PSALTER.md`.
- **Abweichungen vom Auftrag**: wo der Quelltext etwas anderes sagt als ein
  Hinweis. Das ist der häufigste echte Befund.
- **Befunde im Bestand**: wo der Lexikon-Extrakt uneinheitlich ist oder eine
  Bindung falsch aussieht. Nicht selbst korpusweit korrigieren — melden.
- **Befunde in den Ausgaben**: fehlende Verse, Importartefakte (im
  italienischen Psalter stehen vereinzelt `}`-Zeichen mitten im Text).

## Was nie passiert

- ins Repository `bible-reader` schreiben (nur lesen)
- eigene Subagenten starten
- einen Namen deuten, den der Text nicht selbst deutet
- ein Kapitel als „fertig" melden, das `selfcheck.py` nicht sauber durchläuft
