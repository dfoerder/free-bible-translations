# AUFTRAG_AT — der Ablauf für ein Kapitel des Alten Testaments

Gilt für die Bücher 1–39. Der Prompt eines Agenten enthält nur noch, was an
seinem Kapitel besonders ist; alles Wiederkehrende steht hier.

## Vorbereitung (in dieser Reihenfolge)

1. `SPEC.md` lesen — Datenformat und Verbote.
2. Den **Quelltext** des Kapitels lesen. Er liegt in
   `bible-reader/bibles/deu/l1912mod/<buchNr>_l1912mod.json` unter
   `chapters["<kapitel>"]`. Nicht aus der Bibelkenntnis arbeiten.
3. Den Lexikon-Extrakt lesen, den der Prompt nennt (`lexicon.py` hat ihn
   erzeugt). Er zeigt für jede Wortform des Kapitels, wie der fertige Bestand
   sie übersetzt.
4. Die Hinweise lesen, die der Prompt nennt (`hints.py`): unbelegte Formen,
   Kollisionen im Vers, mehrdeutige Formen.
5. `BINDUNGEN_AT.md` lesen, Abschnitt zum eigenen Buch und die allgemeinen
   Bindungen.

## Arbeit

Abschnitte von 8–10 Versen. **Nach jedem Abschnitt die Teildatei wegschreiben**
(`ch<N>.part<M>.json` im eigenen Arbeitsordner). Vier gleichzeitig laufende
Agenten sind schon an einem Nutzungslimit abgebrochen; gerettet wurde nur, was
weggeschrieben war.

Übersetzungen **direkt am Eintrags-Dict** zuweisen — nie eine Liste von
Glossen bauen und hinterher per Index zusammenführen.

Bei Listen (Stammeslisten, Maßangaben, Materiallisten, Opferordnungen) ein
**eigenes kleines Prüfskript** schreiben, das die Position jedes Listenglieds
aus dem Quelltext ableitet und den Eintrag dort dagegenhält. Aufzählungen
gleicher Bauart sind die wahrscheinlichste Stelle für eine um eine Position
verrutschte Zuordnung, und strukturell fällt das nicht auf.

## Prüfung vor der Abgabe

```
python3 selfcheck.py <buchNr> <kapitel> <deine_datei.json>
python3 qa.py --kapitel <buchNr> <kapitel> <deine_datei.json>
```

Beide müssen sauber durchlaufen. `selfcheck.py` prüft Vollständigkeit, Formen,
Spannen und Klammern; `qa.py` prüft Eigennamen, Wiederholungsläufe,
Funktionswörter mit langer Glosse und fremdsprachige Zeichen.

Ein `qa.py`-Treffer ist ein **Verdacht**, kein Fehler: erst die Stelle ansehen,
dann entscheiden, wer recht hat — das Skript kann selbst falsch liegen.

## Abgabe

Eine Datei `ch<N>.json` im eigenen Arbeitsordner, Inhalt `{"<vers>": [...]}`
über **alle** Verse des Kapitels.

Dazu ein kurzer Bericht mit:

- **Wortfeld-Liste der Schnittstelle**: die Begriffe, die über die
  Kapitelgrenze laufen, samt gewählter Glosse und Level. Der nächste Agent
  bekommt sie in den Prompt.
- **Abweichungen vom Prompt**: wo der Quelltext etwas anderes sagt als der
  Hinweis. Das ist der häufigste echte Befund — über dreißigmal in der
  Offenbarung, ein Dutzend Mal in den Briefen.
- **Befunde im Bestand**: wo der Lexikon-Extrakt in sich uneinheitlich ist
  oder eine Bindung falsch aussieht. Nicht selbst korpusweit korrigieren —
  melden.

## Die drei Fallen des Alten Testaments

**Die Lexikonfalle.** Der Extrakt zeigt die Korpusmehrheit. Wo eine Handvoll
NT-Belege gegen eine AT-Bindung steht, zieht die Mehrheit auf die falsche
Seite. Rund vierzig Wörter sind so korpusweit korrigiert worden — `HERR`,
`Land`, `Knecht`, `Magd`, `Hütte`, `Vieh`, `Not`, `Kummer`, `Grimm`. Eine
Bestandsmehrheit ist nur dann ein Argument, wenn die Belege aus **vergleichbaren
Kontexten** stammen.

**Die Dublette formuliert neu.** Wo der Text sich wiederholt (2Mo 25–31 ↔
35–40, die Opferordnungen in 3Mo 1–7, die Musterungen in 4Mo 1 ↔ 26), ist die
zweite Fassung fast nie wörtlich gleich: `Bronze`/`Erz`, `Vorhof`/`Hof`,
`Becken`/`Waschbecken`, Adjektiv gegen Substantiv. **Wer abschreibt, glossiert
falsch.** In 3Mo 3 fanden sich in einem Kapitel mit drei Fassungen 45
Abweichungsblöcke und genau ein wörtlich dreimal identischer Vers.

**Das Sachfeld verschiebt die Grundbedeutung.** Im Stiftshüttenblock ist `Fuß`
der Sockel und `Kopf` das Säulenkapitell — zwei A1-Körperteilwörter mit einer
Bauteillesart, und drei Verse weiter steht „pro Kopf" und meint wieder den
Kopf. Das Level bleibt trotzdem am Lemma (A1); eine Anhebung zöge alle
Körperteil-Einträge mit.

## Was nie passiert

- ins Repository `bible-reader` schreiben
- eigene Subagenten starten
- einen Namen deuten, den der Text nicht selbst deutet
- ein Kapitel als „fertig" melden, das `selfcheck.py` nicht sauber durchläuft
