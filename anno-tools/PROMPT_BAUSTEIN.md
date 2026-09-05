# Der gemeinsame Prompt-Baustein

**Platzhalter: `<NR>` = Buchnummer, `<KAP>` = Kapitelnummer, `<BUCH>` =
Buchname, `<SCRATCH>` = Scratchpad-Verzeichnis des Buches.**

Alles darunter wird woertlich in den Kapitelprompt kopiert, die
Platzhalter ersetzt, und dann der buchspezifische Teil angehaengt.

## Warum diese Datei existiert

Bis Jona (32) wurde der Baustein per `sed` aus dem Prompt des
**Vorgaengerbuchs** abgeleitet. Damit wanderten Buchnummern mit, die
niemand mehr sah: Obadjas und Jonas Prompts verlangten `kongruenz.py 30`
und `artikel.py 30` — also einen Lauf ueber **Amos**. Der Agent fuer
Jona 2 hat es gemerkt und beide zusaetzlich auf 32 laufen lassen; dort
schlugen sie **zweimal zu Recht** an. Ohne seinen Zusatzlauf waeren beide
Fehler durchgegangen.

Ein Baustein mit Platzhaltern kann diesen Fehler nicht tragen.

**Der zweite Anlass** kam aus Micha Paket 2: das Scratchpad ist nicht pro
Agent getrennt, und zwei Agenten haben einander Hilfsskripte
ueberschrieben. Deshalb steht jetzt oben ein eigenes Arbeitsverzeichnis
je Kapitel.

---

Du annotierst **<BUCH> (Buch <NR>), Kapitel <KAP>** des modernisierten
Luther-1912-Textes `l1912mod` mit Wort-fuer-Wort-Glossen in Englisch,
Spanisch, Franzoesisch und Italienisch plus CEFR-Level.

## Wo alles liegt

Arbeitsverzeichnis: `/Users/dfoerd/Documents/projekte/bibel/bibles-translations`

    export ANNO_OUT=<SCRATCH>/out

Das ist Pflicht — ohne die Variable laeuft kein Werkzeug. Alle Werkzeuge
werden **aus `anno-tools/` heraus** aufgerufen.

Deine Abgabe: `$ANNO_OUT/<NR>/ch<KAP>.json`

**Dein Arbeitsverzeichnis fuer alles andere:** `$ANNO_OUT/../work/<KAP>/`
— lege es an und schreibe **jede** Zwischendatei und **jedes** Hilfsskript
dorthin. Mehrere Agenten arbeiten gleichzeitig im selben Scratchpad; in
Micha Paket 2 haben zwei Agenten einander `build1.py` und `build2.py`
ueberschrieben, und einer hat versehentlich das Skript des anderen
ausgefuehrt. Es ging gut aus, weil beide es gemerkt haben — verlass dich
nicht darauf. Auch Teildateien (`ch<KAP>.partN.json`) gehoeren in dein
Arbeitsverzeichnis, nicht neben die Abgabe.

## Eintragsformat

    {"pos": 3, "form": "Feuer", "lemma": "Feuer", "level": "A1",
     "en": "fire", "es": "fuego", "fr": "feu", "it": "fuoco"}

Mehrwoerter tragen zusaetzlich `pos_end` (zusammenhaengend) **oder**
`parts` (getrennte Positionen, z. B. `"parts": [5, 8]`). Das Kopfwort
eines Mehrworts behaelt daneben seinen eigenen Eintrag — in der Regel mit
**seiner woertlichen Glosse**, nicht der Glosse der Wendung (so macht es
der Bestand in 5. Mose 32,1 und Nehemia 5,7). Wo das Kopfwort allein
keine eigene Bedeutung hat, traegt es dieselbe Reihe wie die Wendung
(Amos 4,5 `kuendigen`/`ankuendigen`).

## Wie du arbeitest

- **`belegt.py <Wort>`** vor jeder Entscheidung. Es sagt dir, wie oft die
  **Form** belegt ist und wie oft das **Lemma** — die beiden Zahlen gehen
  auseinander, und die Lemma-Zahl ist die richtige.
- **`lexicon.py`** fuer unbelegte Woerter. Die haeufigste Lesart eines
  Lemmas ist oft nicht die passende — das ist die Lexikonfalle.
- **`hints.py <NR> <KAP>`** listet unbelegte Formen, Kollisionen im
  selben Vers und mehrdeutige Formen. **Die Liste der unbelegten Formen
  ist formbasiert**: das Lemma steht oft laengst im Bestand.
- **`parallelen.py <NR> <KAP>`** findet die laengsten gemeinsamen
  Wortbloecke mit dem fertigen Bestand. Wo ein Block passt, wird er
  **Token fuer Token** uebernommen — aber erst am Vers pruefen, ob er
  inhaltlich passt. **Ein Block kann ueber eine Satzgrenze laufen** und
  zwei verschiedene Konstruktionen verbinden (Obadja 1,8).
- **`ausgaben.py <NR> <KAP>`** zeigt die vier Ausgaben nebeneinander und
  **warnt von selbst**, wenn der berechnete Versatz unsicher ist. Frag es,
  bevor du selbst zaehlst.
- **Aufgeloest wird nur im Kollisionsvers.** Zwei Woerter mit derselben
  Glosse sind nur dann ein Fehler, wenn sie im selben Vers stehen.

## Vor der Abgabe — jeder Lauf, jedesmal, mit DEINER Buchnummer

    cd anno-tools
    python3 selfcheck.py <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 konvention.py <NR> <KAP>
    python3 levelcheck.py <NR> <KAP>
    python3 sweeplemma.py <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 glosskollision.py --datei <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 kongruenz.py <NR>
    python3 artikel.py <NR>

**Erklaere kein Kapitel fuer fertig, das `selfcheck.py` nicht sauber
durchlaeuft.** Jeder Rest aus `glosskollision` und `sweeplemma` wird am
Vers geprueft und im Bericht begruendet — aufgeloest oder verworfen.

## Feste Regeln

- **Ins Repo `/Users/dfoerd/Documents/projekte/bibel/bible-reader` wird NUR
  GELESEN. Nie schreiben.**
- **Starte keine eigenen Subagenten.**
- **Nie ein Grammatik-Tag in Klammern als Glosse („(futuro)", „(plural)")
  — immer ein echtes Wort der Zielsprache.**
- **Keinen Namen deuten, den der Text nicht selbst deutet.**
- Spanisch durchgehend **vosotros**, kein `ustedes` — auch wo RV1909mod
  siezt (es tut es oft).
- Glossen duerfen umgangssprachlich sein; nur Gassensprache vermeiden.

## Dein Bericht

Am Ende: was du entschieden hast und warum, welche Prompt-Angaben du am
Quelltext **widerlegt** hast (das ist der wertvollste Teil — die Zahlen in
jedem Prompt sind maschinell geprueft, aber nicht unfehlbar), welche
Kollisionen du aufgeloest und welche du bewusst stehen gelassen hast,
welche Ausgabenbefunde dir aufgefallen sind, und welche Reihen die
Nachbarkapitel uebernehmen sollen.
