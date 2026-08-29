# Wortfeld des Psalters — was vor dem ersten Psalm feststeht

Der Psalter ist kein fortlaufender Text, sondern 150 einzelne Gedichte. Was
über die Kapitelgrenze läuft, ist deshalb nicht die Handlung, sondern das
**Vokabular**: `HERR`, `Zuflucht`, `Frevler`, `Gerechter`, `loben`, `Seele`,
`Güte` stehen in Dutzenden Psalmen, und jeder Psalm wird von einem anderen
Agenten geschrieben. Ohne eine vorab festgelegte Bindung liest derselbe Begriff
im selben Buch vier verschiedene Glossen.

Dieses Dokument hält fest, was **vor** dem ersten Kapitel gemessen wurde. Es
ist nicht vollständig und soll wachsen: was ein Kapitel entscheidet und was
über seine Grenze läuft, kommt hinzu.

## 1. Die Überschriften — 123 Zeilen ohne englische und spanische Vorlage

`WEB` und `RV1909mod` enthalten in diesem Bestand **keine einzige
Psalmüberschrift**. Gezählt: 0 Treffer für *chief musician* / *músico
principal* in beiden Dateien, gegen 55 Treffer für *chef des chantres* im
Französischen und 31 für *Capo de' musici* im Italienischen.

Für rund 123 Überschriftenzeilen gibt es also nur **eine oder zwei** Ausgaben
als Vorlage. Die englische und die spanische Glosse sind hier eine
**Entscheidung**, keine Ablesung — und sie muss für alle 150 Psalmen dieselbe
sein. Deshalb steht sie hier.

| deutsch | Vorkommen | en | es | fr (LSG) | it (RIV) |
|---|---|---|---|---|---|
| `Vorsänger` | 54× | chief musician | músico principal | chef des chantres | capo dei musici |
| `Wallfahrtslied` | 15× | song of ascents | cántico gradual | cantique des degrés | canto dei pellegrinaggi |
| `Unterweisung` | 13× | instruction | instrucción | instruction | istruzione |
| `Kleinod` | 6× | hymn | himno | hymne | inno |
| `Saitenspiel` | 5× | stringed instruments | instrumentos de cuerda | instruments à cordes | strumenti a corda |
| `Klagelied` | 1× | lament | lamento | complainte | lamento |
| `Brautlied` | 1× | wedding song | canto nupcial | chant d'amour | inno nuziale |
| `Flötenspiel` | 1× | flutes | flautas | flûtes | flauti |

**`Unterweisung` folgt nicht dem Französischen.** LSG schreibt dafür
`Cantique` — dasselbe Wort wie für `Lied`. In Ps 88,1 stehen beide im selben
Vers (`Ein Lied, ein Psalm … Eine Unterweisung Hemans`), und zwei deutsche
Wörter dürfen dort nicht dieselbe Glosse tragen. `Lied` behält die
Bestandslesart *song · cántico · cantique · cantico*, `Unterweisung` bekommt
die wörtliche.

Die Eigennamen und Melodieangaben (`Gittith`, `Jeduthun`, `Alamot`,
`Machalat`, `Esrahiten`, `Hirschkuh der Morgenröte`, `Zerstöre nicht`) folgen
der Ausgabe, die sie führt — `ausgaben.py` zeigt sie. Wo nur das Französische
sie hat, gilt seine Schreibung, ins Englische und Spanische übertragen.

`Weise` in `nach der Weise …` ist die Melodieangabe und **nicht** die
Bestandsbindung *way · manera · manière · modo*: *tune · melodía · air ·
melodia*, B2. In `auf wunderbare Weise` (Ps 4,4) gilt weiter die Bindung.

**Bei Versatz −1 lohnt der Blick in die italienische Zeile des deutschen
Verses 2.** RIV zieht die Überschrift dort in seinen Vers 1 hinein, und
`ausgaben.py` schreibt für den deutschen Vers 1 zu Recht „zählt die Ausgabe
nicht mit" — die italienischen Überschriftenwörter stehen aber da, eine Zeile
weiter. Für Ps 4 liest man dort `Al Capo de' musici. Per strumenti a corda.` und
hat damit die Quelle für zwei Festlegungen dieser Tabelle.

### `Sela` — der Bestand hilft hier nicht

Eine erste Fassung dieses Dokuments schrieb, `Sela` sei im Bestand belegt und
folge ihm. **Das ist falsch, und zwei Agenten haben es unabhängig voneinander
widerlegt.** Der Bestand kennt `Sela` nur als **Eigennamen**: den Sohn Judas
(1. Mose 38,5, *Shelah · Sela · Schéla · Sela*) und den edomitischen Felsen
(2. Könige 14,7). Das liturgische `Sela` des Psalters ist eine andere
Bedeutung — nach `SPEC.md` gilt eine Bindung für dieselbe Bedeutung, nicht für
dieselbe Buchstabenfolge.

Es gilt deshalb, was die vier Ausgaben schreiben, und die haben hier alle einen
Text:

| | en (WEB) | es (RV) | fr (LSG) | it (RIV) |
|---|---|---|---|---|
| `Sela` A1 | Selah | Selah | Pause | Sela |

Das betrifft **72 Verse**. Dass Französisch als einziges übersetzt statt zu
transkribieren, ist kein Befund — LSG druckt dort tatsächlich `— Pause`.

`Halleluja` (22 Verse) ist im Bestand belegt und folgt ihm.

### `Psalm` klein, nicht groß

In der Kopfzeile steht `Psalm` mitten im Satz (`Ein Psalm Davids`), also
*psalm · salmo · psaume · salmo*. Der Bestand hat beides je einmal (Apg 13,33
groß, 1. Kor 14,26 klein) und entscheidet nichts; die Satzstellung schon.
Level B2.

## 2. Die Lexikonfalle im Psalter — gemessen

`lexicon.py` zeigt die Korpusmehrheit über **alle 66 Bücher**. Wo eine Handvoll
NT-Belege gegen eine AT-Bindung steht, zieht die Mehrheit auf die falsche
Seite. Für die Wörter, die der Psalter am häufigsten braucht, ist der Bestand
hier nach Testamenten getrennt ausgezählt:

| Wort | im Psalter | AT-Bindung | NT-Mehrheit | **gilt** |
|---|---|---|---|---|
| `Kraft` | 28× | *strength* 62 : *power* 15 | *power* 82 : *strength* 10 | **AT** — *strength · fuerza · force · forza* |
| `Wunder` | 29× | *wonders* 21 | *miracles* 17 : *wonders* 9 | **AT** — *wonders · prodigios · prodiges · prodigi* |
| `Retter` | 11× | *deliverer* 4 | *Savior* 14 | **AT** — *deliverer · libertador · libérateur · liberatore* |
| `gnädig` | 31× | *gracious* 21 : *merciful* 5 | *merciful* 3 | **AT** — *gracious · clemente · clément · clemente* |
| `Bosheit` | 10× | *wickedness* 9 : *malice* 1 | *malice* 8 : *wickedness* 9 | **AT** — *wickedness · maldad · méchanceté · malvagità* |
| `Gewalt` | 10× | *violence* 15 : *force* 5 | *force* 8 | **AT** — *violence · violencia · violence · violenza* |
| `Völker` | 71× | *peoples* 103 : *nations* 26 | *nations* 24 : *peoples* 20 | **AT** — *peoples · pueblos · peuples · popoli* |
| `Recht` | 37× | *justice* 53 : *right* 15 | *right* 23 : *justice* 6 | **AT** — am Vers, aber romanisch fest: *derecho · droit · diritto* |
| `Rat` | — | *advice* 30 : *council* 4 | *council* 23 | **AT** — *advice · consejo · conseil · consiglio* |

Fest und unstrittig, in beiden Testamenten gleich: `Herz` (*heart*),
`Seele` (*soul*), `Güte` (*kindness · bondad · bonté · bontà*),
`Treue` (*faithfulness*), `Zuflucht` (*refuge*), `Volk` (*people*, 947:2).

**`Menschensohn` ist im Bestand ein reiner NT-Titel.** 88 Belege, **alle** aus
dem Neuen Testament (Mt, Mk, Lk, Joh, Apg, Hebr, Offb), null aus dem Alten —
`lexicon.py` zeigt deshalb ausschließlich den christologischen Titel *Son of Man*
und schreibt ihn groß. Im Psalter (80,18) ist es die alttestamentliche
Gattungsbezeichnung, und alle vier Ausgaben schreiben klein: *son of man ·
hijo del hombre · fils de l'homme · figlio dell'uomo*. Die reinste Lexikonfalle
des Buches, weil der Extrakt hier nicht mehrheitlich, sondern **einstimmig**
in die falsche Richtung zeigt.

**`Höchster` ist dieselbe Falle wie `Menschensohn`.** Im Bestand ist es
ausschließlich der Gottestitel *Most High · Altísimo · Très-Haut · Altissimo*.
In Ps 89,28 ist es aber der schlichte Superlativ unter Königen („der Höchste
unter den Königen der Erde"): *highest · más excelso · plus élevé · più
eccelso*. Wie bei `Menschensohn` zeigt der Extrakt einstimmig auf den Titel.

**`Eber` ist ein Homograph.** 12 Belege als Patriarch (A1), in Ps 80,14 aber
das Wildschwein: *boar · jabalí · sanglier · cinghiale*, B2. `qa.py` meldet die
Stelle erwartungsgemäß als Eigennamen — das ist kein Fehler, sondern der Fall.

**`Herrn` klein geschrieben ist im AT der *master*, nicht der *Lord*.**
81 : 66 im AT, 286 : 12 andersherum im NT. Im Psalter ist fast immer Gott
gemeint — dort steht dann `HERR`/`HERRN` groß, und das ist *LORD · SEÑOR ·
ÉTERNEL · SIGNORE*. Vor jedem klein geschriebenen `Herrn` den Vers ansehen.

## 3. Die Kollisionen des Buches

`hints.py 19` zählt sie über den ganzen Quelltext aus — **71 Paare**. Die
wichtigsten, weil sie sich durch das ganze Buch ziehen:

- `loben` ↔ `preisen` (49,19 und 5 weitere)
- `Kraft` ↔ `Macht` (21,14 · 33,16 und 6 weitere)
- `Werk` ↔ `Wirken` (28,5 und 8 weitere)
- `schauen` ↔ `sehen` (80,15 und 4 weitere)
- `Pforte` ↔ `Tor` (24,7 und 4 weitere)
- `Schande` ↔ `Schmach` · `Einöde` ↔ `Wüste` · `Herrlichkeit` ↔ `Ruhm`
- `Dunkelheit` ↔ `Finsternis` (107,10 · 107,14)
- `bewahren` ↔ `halten` (119,34 · 119,106)
- `HERR` ↔ `Herr` (16,2 · 30,9 und 32 weitere)

**`hints.py` findet nicht alle.** Es meldet Kollisionen über die deutschen
Wortformen; wo zwei verschiedene deutsche Wörter erst über die **Glosse einer
einzelnen Sprache** zusammenfallen, sieht es nichts. In Psalm 84 lagen gleich
zwei solche Fälle in benachbarten Versen:

- 84,9 `höre` und `vernimm` — im Bestand beide spanisch *oye* (Ps 54,4 · Ps 5,3)
- 84,10 `schau` und `blick` — im Bestand beide *look · mira · regarde · guarda*
- 81,2 `Jauchzt … zu` und `jubelt … zu` — beide hätten `zujauchzen` getragen;
  `hints.py` meldet für Ps 81 **null** Paare
- 88,18 `umgeben` und `umringen` — im Bestand beide *surround · rodean ·
  entourent · circondano*; `hints.py` meldet für Ps 88 **null** Paare
- 89,7 `gleich` und `wie` — englisch beide *like*
- 90,11 `er` und `es` — englisch beide *it*
- 92,7 `törichter`/`Narr` · 94,4 `prahlen`/`sich rühmen` · 94,11 `kennt`/`weiß`

**Dafür gibt es jetzt `glosskollision.py`.** Es vergleicht die tatsächlich
gesetzten Glossen statt des Quelltexts gegen den Bestand und findet damit
genau diese Klasse. Pflichtlauf vor der Abgabe, siehe `AUFTRAG_PSALTER.md`.

Alle sind nur aufgefallen, weil die Agenten den Lexikon-Extrakt Wort für
Wort gelesen haben — in drei unabhängigen Paketen. **Bei Synonympaaren im selben
Vers nicht auf `hints.py` verlassen**, sondern die vier Glossen der Nachbarwörter
selbst vergleichen.

### Zwei Paare, deren Auflösung schon feststeht

**`Weg` ↔ `Tun`** kollidiert nur im Englischen — der Bestand glossiert `Tun`
als *ways*, genau wie `Weg`. In Ps 103,7 ist entschieden worden: `Weg` behält
*ways · caminos · chemins · vie*, `Tun` weicht **nur englisch** aus auf
*deeds*, romanisch bleibt es bei *proceder · conduite · condotta*. Die beiden
stehen in **Ps 119,3 und Ps 145,17 wieder zusammen** — dort dieselbe Auflösung
nehmen, nicht neu entscheiden.

**`fern` ↔ `weit`** tragen im Bestand in allen vier Sprachen dieselbe Glosse
(*far · lejos · loin · lontano*, 29 bzw. 49 Belege). In Ps 103,12 aufgelöst:
`weit` behält die Bindung, `fern` nimmt *distant · distante · éloigné ·
distante* — die Lesart steht im Bestand schon am Adjektiv `entfernt`. In
Ps 107–150 stehen die beiden nirgends mehr im selben Vers.

Gemessen über den Gesamtbestand: **keines der beiden Paare steht sonst
irgendwo unaufgelöst zusammen** (`glosskollision.py alle`).

**Die Regel bleibt die aus Hiob:** aufgelöst wird **nur im Kollisionsvers**.
Eine Ausweichlesart, die in einem Vers nötig war, gilt nicht im nächsten —
`lexicon.py` zieht auch aus den frisch gebauten Kapiteln des laufenden Buches,
und was ein Kapitel entscheidet, sieht das nächste als Bestand. In Hiob sind
so sechs Lesarten weitergereicht worden, die keine Bindung waren.
`zweigleisig.py <buchNr>` findet sie.

## 4. Der italienische Artikel vor `HERR`

`HERR` ist italienisch **`SIGNORE`**, und davor steht **`il`/`Il`** — nie
`l'/L'`. Über den gesamten Bestand: 1955 Einträge mit `il`, 39 mit `l'`, und
**alle 39 standen im Psalter** (Ps 12 · 24 · 25 · 27 · 28 · 29 · 31 · 32 · 33 ·
34 · 37 · 84 · 85), am 29.08.2026 korrigiert.

Die Ursache ist absehbar und wird wiederkommen: RIV schreibt `L'Eterno`, und wer
die Ausgabe abliest statt der Bindung zu folgen, übernimmt den Apostroph. Im
Lesefluss stand dann „L' SIGNORE".

## 5. Die Verszählung

Steht in `VERSZAEHLUNG_PSALMEN.md`. Kurz: in 63 der 150 Psalmen ist der
deutsche Vers nicht der englische Vers, und der italienische Psalter hat in 63
Psalmen seinen ersten Vers gar nicht. **Keine Ausgabe über die deutsche
Versnummer aufschlagen** — `ausgaben.py <buchNr> <kapitel>` richtet sie aus.
