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

## Die Abgabedatei

`$ANNO_OUT/<NR>/ch<KAP>.json` ist **flach nach Versnummer**, ohne Huelle:

    {"1": [ {…}, {…} ], "2": [ … ], … }

Kein `chapters`, kein `book`, kein `verses`. `selfcheck` sagt es nicht,
und der Agent fuer Actes 13 musste es aus einer Nachbardatei ablesen.

## Handwerkliches, das jeden Vorgaenger einen Durchgang gekostet hat

- **`pos` zaehlt ab NULL.** Das erste Token eines Verses ist `pos: 0`.
  Es stand bisher nirgends — weder hier noch im Kapitelprompt, und das
  Formatbeispiel verraet es nicht. Der Agent fuer 1. Korinther 8 hat es
  sich aus `load_anno(46)` abgelesen.
- **`load_anno(nr)` hat dieselbe Huelle wie `load_source(nr)`**:
  `{'name': …, 'chapters': {kap: {vers: [eintraege]}}}`. Der Griff auf
  einen annotierten Vers ist also `load_anno(nr)['chapters'][kap][vers]`,
  parallel zum Quelltext.
- **Ein eigenes Hilfsskript in `work/<kap>/` findet `common` nicht.**
  Setz oben `sys.path.insert(0, '<repo>/anno-tools')`; `PYTHONPATH`
  allein reicht nicht, weil das Arbeitsverzeichnis nach jedem
  Bash-Aufruf zurueckfaellt.
- **`form` traegt keine Satzzeichen** (`common.strip_punct`). Sonst meldet
  `selfcheck` dreihundert Scheinbefunde `Dieu, != Dieu`. Bei Mehrwoertern
  wird die Oberflaeche aus den **Einzeleintraegen** gebaut, nie aus dem
  Quelltext. `parts` nur bei getrennten Positionen, sonst `pos_end`.
- **Der Bestand fuehrt durchgehend das typographische `’`** — und ebenso die
  **Ligatur `œ`**: `belegt.py oeuvres` meldet „NICHT belegt" und schlaegt
  `odeur` vor, `belegt.py œuvres` findet alles. Dieselbe stille Falle, ein
  anderes Zeichen.
  `belegt.py "d'eux"` findet nichts, `belegt.py "d’eux"` alles.
  `belegt.py` normalisiert, `folgenreihe.py` nicht — dort liefert ein
  gerades Apostroph stumm 0.
- **Feste Woerterbuchformen mit Elision tragen die Elision im Lemma:**
  `d’abord` (27 Belege) ist das Lemma, nicht `abord`; ebenso `jusqu’à`.
  Die Regel „der Kopf ist das Inhaltswort" fuehrt dort in die Irre.
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
- **Und darunter liegt noch eine Schicht: `mehrwoerter.py`.** `sweep` meldet
  ab 75 Prozent Deckung, `sweeplemma` ab 60 — eine Wendung, die der Bestand
  in der HAELFTE der Faelle fasst und in der anderen nicht, sehen beide
  nicht. Das ist kein Rauschen, sondern ein Kriterium, das nirgends
  aufgeschrieben steht: `un autre` steht 22-mal als Mehrwort und 33-mal
  nicht, und die Grenze laeuft zwischen pronominalem Gebrauch (`épouse une
  autre`) und dem Nomen dahinter (`une autre loi`). Der Agent fuer Roemer 7
  hat sich dafuer ein eigenes Skript gebaut — er war der achte.
  `mehrwoerter.py <buch> <kapitel> <deinedatei.json>` druckt zu jeder
  geteilten Signatur BEIDE Seiten mit Stellen und Wendungslemma. Lauf es
  nach `sweeplemma`. **Ein Treffer ist eine Frage, keine Anweisung** — oft
  ist die Antwort „hier zu Recht nicht", und dann ist die Begruendung der
  Ertrag.
- **`folgenreihe` findet eine Wendung nur unter IHRER Spanne.** Der Agent
  fuer 1. Korinther 2 hat `auprès de` beinahe neu erfunden, weil
  `folgenreihe "auprès de vous"` 0 meldet: `vous` gehoert nicht zur
  Spanne des Mehrworts, und die laengere Zeichenkette trifft deshalb
  nichts. Frag im Zweifel die kurze Spanne allein ab — oder `sweeplemma`,
  das ueber das Lemma sucht.
- **Schneide keine Werkzeugausgabe ab.** Fuenf Agenten haben inzwischen
  einen „Werkzeugfehler" gemeldet, der ein `| head` war: `folgenreihe`
  dreimal (der Mehrwortabschnitt steht unten), `belegt.py` zuletzt (die
  Zeile „im Bestand NICHT belegt" steht VOR den stammverwandten
  Lemmata). Diese Ausgaben sind so gebaut, dass die Antwort unter der
  Zusammenfassung steht. Lies sie ganz, oder schreibe sie in eine Datei.
- **`hints_*.md` und `rueckwaerts` beantworten VERSCHIEDENE Fragen.**
  `hints` fragt: steht diese Wortform im annotierten BESTAND?
  `rueckwaerts` fragt: gibt es fuer dieses Token irgendeine Zeile —
  aus dem Bestand ODER aus der `fr`-Spalte der Zeugen? Ein Wort kann
  bei `hints` unter „unbelegt" stehen und bei `rueckwaerts` eine Zeile
  haben, ohne dass eines von beiden falsch ist. Zwei Agenten haben das
  als Werkzeugfehler gemeldet. Maßgeblich fuer Lemma und Level ist der
  Bestand, also `belegt.py` — die Zeugenzeile ist ein Vorschlag, und
  `levelcheck` widerlegt sie regelmaessig.
- **Die Promptdateien sind Momentaufnahmen.** `hints_*.md`,
  `parallelen_*.md` und die uebrigen entstehen einmal bei der
  Vorbereitung; der Bestand und die Werkzeuge wandern waehrend deines
  Laufs weiter. Wo eine Promptdatei und ein Live-Aufruf sich
  widersprechen, hat der Live-Aufruf recht.
- **Die `form` eines Mehrworts ist die mit Leerzeichen verbundene Kette
  ALLER Einzelformen seiner Spanne** — nicht das erste Token. Der Agent
  fuer Roemer 10 hat sich daran 33 `selfcheck`-Befunde eingehandelt
  (`form 'rends' != Tokens 'rends le témoignage'`). Bei einem `parts`-
  Mehrwort sind es genau die Formen der genannten Positionen, ohne die
  uebersprungenen (`poussa cri` fuer `poussa de nouveau un grand cri`).
- `fixgloss.py verse` nimmt seine drei Argumente einzeln; in einer
  zsh-Schleife ueber eine Variable bricht es ab. Es sagt das sauber.
- **`folgenreihe.py` verschweigt ausserdem den Mehrwort-Abschnitt selbst
  dann, wenn die Zeichenkette trifft** — bei `c’est toi` (5 Belege) und
  `près de` (25) druckt es nur die Einzelreihen. Das ist ein zweiter,
  von der Zeichenkettensuche unabhaengiger Ausfall. Ohne `sweeplemma`
  haettest du beide neu erfunden.
- **`levelcheck` zaehlt Mehrworteintraege in die Lemma-Statistik mit.**
  Bei `se trouver` (6 Einzel-, 26 Mehrworteintraege) zeigt eine eigene
  Zaehlung ueber die Einzeleintraege deshalb in die falsche Richtung.
  Wenn `levelcheck` dir widerspricht, hat es meistens recht.
- **Den Quelltext holst du mit `common.load_source(nr)['chapters'][kap][vers]`**
  — eine `load_text` gibt es nicht.
- **`folgenreihe.py` vergleicht ohne Ruecksicht auf Gross-/Kleinschreibung**
  und sagt es in der Ausgabe nicht. `folgenreihe "Les choses"` meldet die
  Treffer von `les choses` mit. Wer daraus „einstimmig" liest, bindet an
  die falsche Zeile — sieh dir die Glossenzeilen an, nicht nur die Zahl.
- Die **Mehrwortliste steht am ENDE** der `folgenreihe`-Ausgabe. Drei
  Agenten haben sie mit `| head` abgeschnitten und dem Werkzeug
  vorgeworfen, es verschweige sie. Zeile fuenf sagt jetzt, ob es welche
  gibt — aber schneide die Ausgabe trotzdem nicht ab.
- **`reflexiv.py <buchNr> …`** meldet Verbtoken mit `se` davor, die ihr
  reflexives Lemma nicht tragen, obwohl kein Mehrwort es traegt. Der
  erste Abschnitt (reflexives Lemma existiert schon) ist sicher, der
  zweite am Vers zu pruefen — dort ist `se` oft Objekt, nicht Reflexiv.
  **Fuer deine eigene Abgabe:**

      python3 reflexiv.py 40 41 42 43 65 --datei $ANNO_OUT/<NR>/ch<KAP>.json --kapitel <KAP>

  Die Buchnummern liefern die vorhandenen `se <lemma>`, die Datei wird
  dagegen gehalten. Ohne `--datei` sieht das Werkzeug nur den gebauten
  Bestand und sagt ueber dein Kapitel nichts.

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

## Alleinstehende Satzzeichen zaehlen als Position mit

Ein Gedankenstrich, der als eigenes Wort im Vers steht, ist ein Token
und belegt eine Position — er bekommt nur keinen Eintrag. Die Abgabe
springt dort also (…5, 7, 8…), und `validate.py` besteht darauf.

`rueckwaerts_*.md` zaehlte diese Tokens frueher weg; wer die Nummern
von dort uebernahm, verschob alles dahinter. Der Fehler ist behoben
(gemeldet vom Agenten fuer Galates 2, dessen Vers 2,6 zwei
Gedankenstriche traegt) — aber **pruef die Position immer am eigenen
Vers nach**, nicht an einer Vorbereitungsdatei.
