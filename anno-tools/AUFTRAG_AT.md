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
   **Die Kollisionsliste ist nicht vollständig.** `hints.py` blendet
   Funktionswörter aus, sonst ersäuft der Bericht im Rauschen — darunter `aus`,
   `an`, `auf`, `zu`, `nach`, `vor`, `über`, `um`. Genau das sind aber die
   **Partikeln trennbarer Verben**, und die tragen eine eigene Bedeutung: in
   2Kön 6,7 standen `aus` (von *ausstrecken*) und `heraus` im selben Vers und
   trugen in allen vier Sprachen dieselbe Glosse. Der Fall wurde nicht gemeldet
   und war trotzdem echt. **Partikeln also selbst nachzählen.**
5. `BINDUNGEN_AT.md` lesen, Abschnitt zum eigenen Buch und die allgemeinen
   Bindungen.

## Arbeit

Abschnitte von 8–10 Versen. **Nach jedem Abschnitt die Teildatei wegschreiben**
(`ch<N>.part<M>.json` im eigenen Arbeitsordner). Vier gleichzeitig laufende
Agenten sind schon an einem Nutzungslimit abgebrochen; gerettet wurde nur, was
weggeschrieben war.

Übersetzungen **direkt am Eintrags-Dict** zuweisen — nie eine Liste von
Glossen bauen und hinterher per Index zusammenführen.

**Feste Wendungen, die der Bestand als Mehrwort führt, nicht vergessen.** Ein
fehlender Mehrwort-Eintrag ist für `selfcheck.py` und `qa.py` **prinzipiell
unsichtbar**: die Einzelwörter sind vollständig und richtig, strukturell fehlt
nichts. In Esra sind so zehn Stellen liegengeblieben, in Nehemia 4 und 5 noch
einmal vier. Die häufigsten: `um … zu` (287 Belege), `nicht mehr` (96),
`so wie` (95), `genau wie`, `wie wenn`. Nach dem Schreiben selbst prüfen:

```
export ANNO_OUT=<dein out-Ordner>
python3 konvention.py <buchNr> <kapitel>
```

Es produziert **richtigerweise Fehlalarme** — bei `den König um eine Eskorte zu
bitten` ist `um` die Rektion von `bitten`, bei `so wertvoll wie Gold` ist es die
Vergleichsklammer. Jeden Treffer am Vers ansehen, dann entscheiden.

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

*Zwei Dinge, an denen sich schon mehrere Agenten verrechnet haben:*

- **`lexicon.py` und `fixgloss.py` trennen nicht nach Testamenten.** Eine große
  Belegzahl kann fast ganz aus dem NT stammen. Bei `nämlich` sind von 49 Belegen
  für *in fact* **41 aus dem Neuen Testament** — im AT steht diese Lesart nur
  achtmal. Wer die Gesamtzahl gegen `BINDUNGEN_AT.md` hält, hält die Falle gegen
  die Warnung davor. Im Zweifel die genannten Belegstellen ansehen.
- **Die Bindungstabelle ist bedeutungsblind.** Sie nennt je Lemma die häufigste
  AT-Lesart, auch wo das Wort zwei Bedeutungen hat. `nämlich` steht im AT
  **14:14** zwischen der erklärenden Lesart (*namely*) und der kausalen
  (*in fact* / *for*) — da gibt es keine Bindung, sondern eine Entscheidung am
  Vers. Die Präambel der Tabelle sagt das selbst: eine Bindung gilt für dieselbe
  **Bedeutung**, nicht für dieselbe Buchstabenfolge. Wo beides auseinanderfällt,
  entscheidet die Bedeutung — und du meldest es.

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

## Die Glossen folgen den vier Referenzausgaben

**WEB** (en) · **RV1909mod** (es) · **LSG1910** (fr) · **RIV1927** (it). Eine
Sprache, die bei einem Namen oder einer Wendung altertümlich wirkt, ist **kein
Befund**, solange ihre Ausgabe es so schreibt. `Susa` trägt englisch *Shushan*
neben romanisch *Susa · Suse · Susa* — gemeldet als Inkonsistenz, geprüft, und
WEB schreibt tatsächlich „Shushan the palace" (Est 1,2). Nichts war zu
vereinheitlichen.

Vor jeder Meldung dieser Art die Ausgabe aufschlagen. Sie liegt in
`bible-reader/bibles/<sprache>/<edition>/<buchNr>_<edition>.json`:

```
bibles/eng/web/17_web.json
bibles/spa/rv1909mod/17_rv1909mod.json
bibles/fra/lsg1910/17_lsg1910.json
bibles/ita/riv1927/17_riv1927.json
```

Das gilt **nicht** für Fälle, in denen eine Sprache von sich selbst abweicht —
`Ohr` italienisch 42-mal *orecchi* und 8-mal *orecchie* ist ein echter Befund,
weil dieselbe Ausgabe nicht zwei Formen haben kann.

## Was nie passiert

- ins Repository `bible-reader` schreiben
- eigene Subagenten starten
- einen Namen deuten, den der Text nicht selbst deutet
- ein Kapitel als „fertig" melden, das `selfcheck.py` nicht sauber durchläuft
