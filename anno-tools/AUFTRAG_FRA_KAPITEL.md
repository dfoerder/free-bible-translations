# Auftragsbaustein: ein Kapitel der franzoesischen Bibel annotieren

Dieser Text ist fuer jedes Kapitel gleich. Der Aufruf nennt dazu nur noch
Buch, Kapitel und was dieses Kapitel besonders macht.

## Umgebung — in JEDEM Bash-Aufruf neu setzen

Das Arbeitsverzeichnis faellt nach jedem Aufruf zurueck.

    export ANNO_EDITION=fra/lsg1910mod
    export ANNO_OUT=<der im Auftrag genannte Pfad>

## Fuenf Regeln, ohne Ausnahme

- Ins Repo `/Users/dfoerd/Documents/projekte/bibel/bible-reader` wird NUR
  GELESEN. Nie schreiben.
- Starte keine eigenen Subagenten.
- Nie ein Grammatik-Tag in Klammern als Glosse („(futuro)", „(plural)") —
  immer ein echtes Wort der Zielsprache.
- Keinen Namen deuten, den der Text nicht selbst deutet.
- Spanisch durchgehend **vosotros**, kein `ustedes`.

## Handwerkliches, das jeden Vorgaenger einen Durchgang gekostet hat

- **`form` traegt keine Satzzeichen** (`common.strip_punct`). Sonst meldet
  `selfcheck` dreihundert Scheinbefunde `Dieu, != Dieu`. Bei Mehrwoertern
  wird die Oberflaeche aus den **Einzeleintraegen** gebaut, nie aus dem
  Quelltext. `parts` nur bei getrennten Positionen, sonst `pos_end`.
- **Der Bestand fuehrt durchgehend das typographische `’`.**
  `belegt.py "d'eux"` findet nichts, `belegt.py "d’eux"` alles.
  `belegt.py` normalisiert, `folgenreihe.py` nicht — dort liefert ein
  gerades Apostroph stumm 0.
- **`hints_*.md` gibt Zeugen-Level, keine Bestands-Level.** Nur
  `belegt.py <wort>` traegt. `levelcheck` hat bei jedem der letzten
  Agenten Level korrigiert, die aus den Zeugen geerbt waren.
- **`folgenreihe.py` und `fixgloss.py mw` finden Mehrwoerter nur ueber die
  Zeichenkette, nicht ueber das Lemma.** Sieben Agenten haben deshalb
  Mehrwoerter neu erfunden oder gar nicht gesetzt, die es laengst gibt
  (`prendre la fuite`, `près de`, `rendre l’esprit`, `c’est toi`,
  `moi aussi`, `du milieu de` unter dem Lemmanamen `au milieu de`).
  **Der zweite und dritte Abschnitt von `sweeplemma` fangen das** — lauf
  sie vor der Abgabe, sie sind das eigentliche Mehrwort-Suchwerkzeug.
- `fixgloss.py verse` nimmt seine drei Argumente einzeln; in einer
  zsh-Schleife ueber eine Variable bricht es ab. Es sagt das sauber.

## Die Regeln dieser Arbeit — alle in `BINDUNGEN_FRA_NT.md`

**Lies die letzten zwoelf Abschnitte, bevor du glossierst.** Jede dieser
Regeln steht dort mit ihrer Messung; die meisten wurden **gegen die
Mehrheit im Bestand** entschieden, weil der Zeuge etwas anderes sagte.

1. `croire en` + Person als Glaubensobjekt: italienisch `credere **in**`,
   nicht `a`. Nur beim Glauben an eine Aussage steht `a`.
2. `etre` + Partizip eines Bewegungsverbs (`venir aller arriver entrer
   sortir monter descendre tomber revenir passer rester`) ist das
   **Perfekt**: deutsch und italienisch `bin`/`sono`, aber englisch
   `have/has` und spanisch `he/has/ha`, nie `am`/`soy`. Das Partizip zieht
   mit (`has fallen`, nicht `has fell`); nach `haber` ist es
   unveraenderlich (`ha llegado`, nicht `ha llegada`).
3. **Italienische Klitikahaeufung:** `mi ti ci vi` werden vor
   `lo la li le ne` zu `me te ce ve` — `ve l’ho detto`. Das
   unpersoenliche `si` ist ausgenommen.
4. **`avoir` als Besitzverb ist spanisch `tener`, nicht `haber`.** `haber`
   ist nur Hilfsverb und das unpersoenliche `hay`. Unter `il y avoir`
   traegt der Einzeleintrag dasselbe Existenzverb wie das Mehrwort
   (`hay / había / hubo / habrá`), nie `tener`.
5. **Teilungsartikel:** `de` vor einem Artikel traegt italienisch nur
   `di`, der Artikel bleibt bei seinem Token; `de` vor blossem Nomen
   traegt den ganzen `del`/`della`. **`un po’ di` ist eine Altlast.** Der
   verneinte Teilungsartikel (`pas de péché`) heisst deutsch **`kein`**,
   nicht `irgendein`; spanisch `ningún`, italienisch `alcun`.
6. **Das zweite Token einer Konjunktion traegt die Konjunktion mit:**
   `afin` = *damit* + `qu’il` = ***dass er***. Gilt fuer `afin que`,
   `parce que`, `de peur que`, `pendant que`, `pour que`, `dès que`,
   `tandis que`. **Nicht** fuer `ce que`/`ce qui` (dort `ce` = *das* +
   `que`/`qui` = ***was***) und nicht fuer `ainsi que`, `ne que`,
   `tant que`. Die Einzelzeilen doppeln damit die Konjunktion — das ist
   gewollt, genau wie `ne` und `pas` beide *nicht* tragen.
7. **Italienisch verschmilzt die Praeposition nie in ein Possessiv:**
   `di` + `i suoi`, nie `di` + `dei suoi`. (Der Teilungsartikel nach einer
   Praeposition ist etwas anderes: `con delle` ist richtig.)
8. `pouvoir` als Nomen ist `authority`, ausser neben `autorité` im selben
   Vers.
9. `serviteur` = *Diener · servant · siervo · servo*; *Knecht ·
   bondservant · esclavo · schiavo* gehoert `esclave`. `maître` beim
   Knechtsherrn = *Herr · master · señor · padrone*, die Anrede an Jesus
   = *Meister · Teacher*.
10. Volksnamen italienisch als **Nomen** gross (`Giudei`, `Galilei`,
    `Israeliti`), als Adjektiv klein; spanisch immer klein.

## Was wirklich prueft

`folgencheck --min 3` (der Standardlauf meldet nur einen Bruchteil),
`folgencheck --gegen <die fertigen Buecher> --min 5`, der zweite und
dritte Abschnitt von `sweeplemma`, und `paketcheck`, sobald deine
Nachbarn abgegeben haben. Die acht Einzeleintrags-Pruefungen melden fast
immer Null; `levelcheck` und `artikel` sind die Ausnahmen und haben in
jedem der letzten Pakete etwas gefunden.

## Wie du melden sollst

Knapp: Gepraegtes, gemessen Uebernommenes, aufgeloeste und bewusst stehen
gelassene Kollisionen, und wo dir ein Werkzeug oder eine Vorgabe
widersprochen hat.

**Wenn du eine Bestandsstelle fuer falsch haeltst, sag es mit dem
Zeugenbeleg** — solche Meldungen haben in Johannes und Apostelgeschichte
siebzehn bestandsweite Fehler aufgedeckt. Acht weitere Meldungen waren
falsch, weil der Bestand einen Unterschied abbildete, den der Melder fuer
Zufall hielt: **pruefe erst, ob die Spaltung einen Grund hat** — Kasus,
Genus, Satzfunktion, oder eine andere Konstruktion mit demselben Wort.
Und **miss ueber alle Formen**, nicht nur ueber die, die in deinem Vers
steht: eine Stichprobe von drei Stellen hat zuletzt in die falsche
Richtung gezeigt.
