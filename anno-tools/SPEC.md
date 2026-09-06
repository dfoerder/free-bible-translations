# SPEC — Wort-für-Wort-Annotation einer Bibelausgabe

Bis Maleachi galt diese Datei für genau eine Richtung: `deu/l1912mod` →
en/es/fr/it. Seit dem französischen NT entscheidet `ANNO_EDITION`, welche
Ausgabe der Quelltext ist und welche vier Sprachen die Glossen tragen
(`common.py` führt die Tabelle). Alles hier Beschriebene gilt für jede
Richtung; wo Beispiele deutsch sind, sind sie Beispiele und keine
Einschränkung.

Verbindliche Spezifikation für jeden Agentenlauf. Wer hiervon abweicht,
liefert Daten, die der Validator zurückweist.

## Was entsteht

Zu jedem Kapitel eine Datei `{"<vers>": [<einträge>]}`. Der annotierte Text ist
die Ausgabe aus `ANNO_EDITION`, die vier anderen Sprachen sind die Glossen:

    deu/l1912mod     Quelltext deutsch,      Glossen en · es · fr · it
    fra/lsg1910mod   Quelltext französisch,  Glossen de · en · es · it

## Einzelwort-Eintrag

```json
{"pos": 3, "form": "Vater", "lemma": "Vater", "level": "A1",
 "en": "father", "es": "padre", "fr": "père", "it": "padre"}
```

- `pos` — 0-basierter Index im Vers, gezählt über `text.split()`
- `form` — das Token **ohne** umschließende Satzzeichen (`"Davids,"` → `"Davids"`);
  Binnenzeichen bleiben (`Abel-Mizrajim`)
- `lemma` — Grundform. Artikel und Pronomen werden normalisiert
  (`das`/`dem`/`den` → `der`), Verben auf den Infinitiv, Substantive auf den
  Nominativ Singular
- `level` — CEFR **aus Sicht dessen, der die Sprache des Quelltextes lernt**,
  bezogen auf das **Lemma**, einer von `A1 A2 B1 B2 C1 C2`. Beim französischen
  Text also aus Sicht von Französischlernenden — das Level eines Zeugen ist
  **nicht** übertragbar, `mangera` steht im Französischen nicht dort, wo
  `will eat` im Englischen steht
- vier Glossen, **kontextuell** korrekt in Tempus, Numerus und Person

**Jede Tokenposition bekommt genau einen Einzelwort-Eintrag.** Einzige Ausnahme:
ein alleinstehendes Satzzeichen (ein eingeschobener Gedankenstrich) bleibt
unannotiert — eine Glosse „dash/tiret" wäre ein Übersetzungsetikett an einem
Satzzeichen. Die App stellt unannotierte Tokens als normalen Text dar.

Ziffern sind **kein** Satzzeichen: „46 Jahre" bekommt an der Ziffer einen
regulären Eintrag mit `"46"` in allen vier Sprachen.

## Mehrwort-Einträge

Zusätzlich zu den Einzelwörtern, **nicht statt ihrer**. Die Einzelwörter
behalten ihre wörtliche Bedeutung, der Mehrwort-Eintrag trägt die Bedeutung
der Einheit.

Zusammenhängend — `pos` + `pos_end`:

```json
{"pos": 4, "pos_end": 6, "form": "zur Welt bringen", "lemma": "zur Welt bringen",
 "level": "B1", "en": "give birth to", "es": "dar a luz", "fr": "…", "it": "…"}
```

Getrennte Satzklammer — `pos` + `parts`:

```json
{"pos": 1, "parts": [1, 3], "form": "stand auf", "lemma": "aufstehen",
 "level": "A2", "en": "got up", "es": "se levantó", "fr": "…", "it": "…"}
```

`parts[0] == pos`, aufsteigend, mindestens zwei Positionen, **nie
zusammenhängend** (dann `pos_end`). `form` sind die Tokens an genau diesen
Positionen — also „stand auf", nicht „stand Joseph auf". Wörter dazwischen
gehören nicht dazu und behalten ihre eigenen Glossen.

Mehrwort-Einträge **nur**, wenn sich die Bedeutung nicht aus den Teilen ergibt:

- trennbare Verben mit Bedeutungsverschiebung (`fing … an`)
- Funktionsverbgefüge (`hatte … Angst`, `steht geschrieben`)
- feste Wendungen (`auf die Probe stellen`)
- Reflexiva (`freuten … sich`)
- Kausativ (`ließ … töten`)

**Nicht** für reine Tempus- und Passivklammern (`hat … gesagt`, `wird …
genannt`) — die funktionieren Wort für Wort.

Das `lemma` eines verbalen Mehrwort-Eintrags steht in der **Zitierform**:
`gehen lassen`, nicht `ließen gehen`. Bei festen Wendungen ist die Zitierform
die übliche Nennform (`einen Bund schließen`, `Kinder bekommen`).

## Verboten

- leere Werte, `-`, `?`, `…` als ganze Glosse
- Grammatik-Tags in Klammern statt einer Übersetzung: `(futuro)`, `(plural)`.
  Wo ein deutsches Hilfsverb oder eine Partikel keine Entsprechung hat, gehört
  dorthin ein **echtes Wort** der Zielsprache oder die periphrastische
  Entsprechung — nie ein Etikett über die Grammatik.
- eine Glosse in der falschen Sprachspalte (ein französisches `à` im
  spanischen Feld)
- dieselbe Glosse an drei aufeinanderfolgenden Positionen
- ein mehrwortiges Inhaltswort an einem Funktionswort (`der`, `und`, `von`)

## Hilfsverben dürfen das Vollverb nicht verschlucken

„ich **würde** **sterben**": an `würde` gehört die Hilfsverb-Entsprechung, an
`sterben` das Vollverb. Steht an beiden Tokens dieselbe volle Verbform
(*moriría* / *moriría*), ist der Eintrag strukturell perfekt und im Lesefluss
falsch. Periphrastisch lösen: *iba a* / *allais* / *stavo per* + Infinitiv.

## Anschluss an den Bestand

Der Lexikon-Extrakt (`lexicon.py`) zeigt, wie ein Wort im fertigen Bestand
übersetzt ist. **Die Vorgabe gilt für dieselbe Bedeutung, nicht für dieselbe
Buchstabenfolge.** `Ofen` ist Backofen und Feuerofen, `Himmel` ist *heaven* und
*sky*, `weiß` ist eine Form von *wissen* und die Farbe. Bei anderer Bedeutung:
eigene Glosse **und eigenes Lemma**.

Umgekehrt gilt: wo der Bestand eine Lesart hat und die Bedeutung dieselbe ist,
wird sie **übernommen**, nicht neu erfunden. Sonst laufen zwei Kapitel
auseinander, die dasselbe sagen.

**Der Extrakt ist formbasiert.** Steht eine Form nicht drin, kann das Lemma
über eine andere Form längst im Bestand stehen — im VERWANDT-Abschnitt
nachsehen, bevor etwas Neues erfunden wird.

## Kollisionen

Zwei verschiedene deutsche Wörter mit derselben Glosse sind im Lesefluss nicht
zu unterscheiden. Wo zwei solche Wörter **im selben Vers** stehen, muss eines
ausweichen (`Ehre` ≠ `Herrlichkeit`, `Kelch` ≠ `Becher` ≠ `Schale`). Wo sie
nirgends zusammenstehen, wird **nicht** aufgelöst — eine buchlokale
Sonderlösung macht den Bestand nur inkonsistent.

## Namen

**Keine Namensdeutung ohne hörbare Ableitung im Text.** Der l1912mod deutet
nirgends; wo Luther transliterierte, übersetzt er selbst (`Machpela` →
`Doppelhöhle`, `Mizpa` → `Warte`). Ein Eigenname bekommt als Glosse den Namen
in der Schreibung der Zielsprache (`Mose` → *Moses/Moisés/Moïse/Mosè`),
vorangestellte Kasuspräpositionen inklusive (`Moses` → *of Moses*).

## Die Werkzeuge

**`WERKZEUGE.md`** ist das Register: welches Skript wozu, wann und wie
aufgerufen — nach Arbeitsschritt geordnet. Die Begruendung, an welchem
Fehler ein Werkzeug entstanden ist, steht im Docstring der Datei selbst.

Vier davon pruefen **vor der Abgabe** und sind Pflicht: `selfcheck.py`,
`glosskollision.py`, `levelcheck.py`, `qa.py`.

Zwei pruefen **den Prompt**, bevor er an einen Agenten geht, und sie
pruefen Verschiedenes: `vorgabecheck.py` haelt Level, Reihen und
Verszitate gegen Bestand und Quelltext, `promptcheck.py` prueft, ob die
genannten Woerter im Kapitel **ueberhaupt vorkommen**. Beide laufen zu
lassen ist nicht optional — in Sacharja Paket 4 lief nur das erste, und
zwei Reihen im Prompt gehoerten zu Woertern, die der Text gar nicht hat.

## Drei Arten, sich selbst zu taeuschen

Alle drei sind in einer einzigen Sitzung passiert, jede von einem
Agenten gefunden, und alle drei haben dieselbe Form: **aus einer
abgeschnittenen Ausgabe auf Vollstaendigkeit geschlossen.**

1. Ein Verszitat bei 95 Zeichen abgeschnitten und daraus einen
   Verszaehlungsbefund abgeleitet (Jona).
2. Mit `most_common(2)` zwei von **sechs** Glossenvarianten angesehen
   und „alle" geschrieben (Haggai).
3. Eine Werkzeugausgabe mit `tail -40` gelesen; die Gesamtzahl stand im
   **Kopf** der Ausgabe, und vier von vierzehn Wortfolgen fehlten
   (Maleachi).

Dagegen hilft kein Werkzeug, sondern eine Gewohnheit: **erst die
Gesamtzahl lesen, dann kuerzen.** `folgenreihe.py` schneidet aus
demselben Grund nichts ab.

## Arbeitsweise

1. Diese Datei und `AUFTRAG_AT.md` lesen
2. Den **Quelltext** des Kapitels lesen —
   `bible-reader/bibles/deu/l1912mod/<nr>_l1912mod.json`
3. Den Lexikon-Extrakt lesen, den der Auftrag nennt
4. In Abschnitten von 8–10 Versen arbeiten und **nach jedem Abschnitt die
   Teildatei wegschreiben**. Das ist der einzige Schutz gegen einen Abbruch
   mitten im Kapitel.
5. Übersetzungen **direkt am Eintrags-Dict** zuweisen. Nie eine separate Liste
   bauen und hinterher per Index zusammenführen — dabei verrutschen Zuordnungen
   unbemerkt um eine Position, und das fällt strukturell nicht auf.
6. `selfcheck.py` und `qa.py --kapitel` laufen lassen, bis beide sauber sind
7. Abgeben und melden, was aufgefallen ist

**Nie ins Repository `bible-reader` schreiben** — nur lesen. Geliefert wird in
den eigenen Arbeitsordner.

**Keine eigenen Subagenten starten.**

## Der Quelltext hat immer recht

Perikopen-Hinweise im Prompt sind **Hypothesen**, auch wenn ein Skript sie
erzeugt hat. Der modernisierte Text weicht oft von der Bibelkenntnis ab: kein
`Malzeichen`, sondern `Zeichen`; kein `Büchlein`, sondern `Schriftrolle`; keine
`Unzucht`, sondern `sexuelle Unmoral`. **Abweichungen melden, nicht dem Hinweis
folgen.**
