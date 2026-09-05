# Wortfeld Zephanja (36)

Drei Kapitel, 53 Verse, 1340 Tokens, 70 Mehrwoerter. Ein Paket, drei
Agenten. `paketcheck` Abschnitt A: **leer**.

## Die Reihen des Buches

```
HERR       A1  LORD · SEÑOR · ÉTERNEL · SIGNORE
Tag        A1  day · día · jour · giorno
Zorn       B2  wrath · ira · colère · ira
Rest       B1  remnant · remanente · reste · resto
Schmach    C1  reproach · oprobio · outrage · oltraggio
Eifer      C1  zeal · celo · zèle · zelo
verzehren  C1  consume · consumir · consumer · consumare
ausrotten  C1  cut off · eliminar · retrancher · eliminare
verwuesten C1  lay waste · asolar · dévaster · devastare
bruellend  B2  roaring · rugiente · rugissant · ruggente
Kusch      A1  Ethiopia · Etiopía · Éthiopie · Etiopia
```

`Volk` traegt drei Lesarten, und alle drei sind gewollt: `people`
(Israel), `peoples` (Menschengruppen — 2,11 die Inselvoelker, 3,9 die
reinen Lippen, 3,20 „unter allen Voelkern"), `nations` (politische
Groessen — 3,6 ausgerottet, 3,8 versammelt neben den Koenigreichen).
`denn` steht 12× als `for` und 2× als `Because` — der Unterschied ist
die Satzstellung, beide Male am Satzanfang von 3,8.

## Die sechs Wiederholungen

`wiederholungen.py` fand sechs Folgen, zwei davon ueber Kapitelgrenzen.
Fuenf sind Token fuer Token gleich gesetzt:

```
am Tag des Zorns des HERRN   1,18 · 2,3    ueber die Kapitelgrenze
Tag des HERRN ist nahe       1,7  · 1,14
den Namen des HERRN          3,9  · 3,12
des HERRN ueber euch         2,2  · 2,2    zweimal im selben Vers
ist mitten unter dir         3,15 · 3,17
niemand mehr darin wohnt     2,5  · 3,6    ueber die Kapitelgrenze
```

**Die erste ist der belastbarste Einzelbefund des Buches.** Die Agenten
fuer Kapitel 1 und 2 mussten sie unabhaengig setzen — die Datei des
anderen lag nicht vor —, beide gingen auf Hesekiel 7,19 zurueck, und
alle sechs Eintraege kamen zeichengleich heraus. Derselbe Vorgang wie
der 10-Token-Block in Nahum.

**Die sechste ging schief und wurde eingesammelt.** Kapitel 2 setzte in
2,5 das Mehrwort `niemand mehr` (24 Bestandsbelege, einstimmig) und
meldete ausdruecklich: „Kapitel 3 muss diesen Mehrwort-Eintrag
mitsetzen, sonst laufen die beiden Stellen auseinander." Kapitel 3 hat
es an **beiden** Stellen des Verses 3,6 nicht gesetzt. Nachgetragen.

Der Rest der Folge weicht zu Recht ab: `darin` heisst in 2,5 `in it ·
en ella` (die Meereskueste, f. Sg.), in 3,6 `in them · en ellas` (die
Staedte, f. Pl.). Der sechste Fall, in dem die n-Gramm-Gegenrechnung
eine Kongruenzgrenze nicht kennt.

## Zehn Bloecke gegen den Bestand

`parallelen.py` fand zehn Bloecke ab sechs Tokens. Acht sind
zeichengleich uebernommen, zwei weichen ab — beide begruendet:

- **1,15 gegen Joel 2,2**: fr `de` statt `d'`. Elision vor Vokal —
  Joel liest `d'obscurité`, Zephanja `de brume`.
- **3,17 gegen 5. Mose 4,24**: es `está` statt `es`. Beide Verse
  beginnen „Denn der HERR, dein Gott, ist"; in 5. Mose folgt eine
  Eigenschaft („ein verzehrendes Feuer" → *ser*), in Zephanja ein Ort
  („mitten unter dir" → *estar*).

## Was am Quelltext widerlegt wurde

Vier Angaben meiner Vorgabe hielten dem Text nicht stand, drei davon
erfundene Zitate:

- **3,3** zitiert als „Ihre Fuersten sind bruellende Loewen … die bis
  zum Morgen nichts uebriglassen." Der Text liest „sind **in ihrer
  Mitte** bruellende Loewen" und „die nichts **fuer den Morgen**
  uebriglassen". Aus dem Einschub wird ein Mehrwort, das die Vorgabe
  nicht kannte.
- **3,17** zitiert als „Er wird sich ueber dich freuen mit Jubel". Der
  Text hat „und ueber dich **jubeln mit lautem Gesang**".
- **`Jubel`, `Freude`, `Jauchzen`** als Substantive: keines kommt vor.
  Das Kapitel hat nur Verben — `Juble`, `Jauchze`, `jubeln`.
- **`Kusch`** steht als `Kuschs`, **`ausgiessen`** als `auszugiessen`
  mit `um` — also ein `um zu`-Mehrwort mit verschmolzenem Infinitiv.

Daraus wurde `vorgabecheck.py --buch` um die **Quelltextprobe**
erweitert: jedes Verszitat ohne Ausgabennennung wird gegen den
deutschen Buchtext gehalten, an `…` in Segmente geteilt. Sie findet
alle drei Faelle. Dabei fiel ein Fehler auf, der schon laenger in der
Ausgabenprobe sass: die Normalisierung hatte `ß` durch ein Leerzeichen
ersetzt, `ließ` wurde zu `lie`. Behoben.

## Namen

`Kusch` (3,10) ist der einzige strittige. **WEB schreibt „Cush"**, der
Bestand bindet 16:1 auf `Ethiopia`, und RV/LSG/RIV lesen
Etiopía/Éthiopie/Etiopia. Der Bestand hat gewonnen; der einzige
`Cush`-Beleg im Korpus (Psalm 7,1) ist eine Person, kein Land.

Der Zefanja-2-Agent hat drei Namen meiner Vorgabe widerlegt:
`Kereter`/`Aschdod`/`Maktesch` — der Text liest `Kreter`, `Asdod`,
`Muehlenviertel`. Die Namenslisten der Prompts stehen als Fliesstext
mit `·` ohne Backticks und wurden bis dahin nie geprueft; seither liest
`promptcheck.namensliste()` sie mit.

## Gegen die Bestandsmehrheit entschieden

- `vergewaltigen` (3,4) — der Bestand kennt nur den Sexualsinn
  (2 Belege). „vergewaltigen das Gesetz" ist *violate · violan ·
  violent · violentano*.
- `Gabe` (3,10) — Bestand *gift · don · don · dono* (78). „mir als
  Gabe gebracht" ist *offering · ofrenda · offrande · offerta*, wie
  alle vier Ausgaben.
- `heimbringen` (3,20) — der einzige Beleg (1. Mose 42,19) betrifft
  Getreide und liest fr *rapporter à la maison*. Fuer Menschen
  **ramener**.
- `am Abend` (3,3) — der Bestand glossiert temporal; hier ist es
  attributiv („Woelfe am Abend" = Abendwoelfe): *of the evening · del
  atardecer · du soir · della sera*.
- `Nähe` (3,2) — „die Naehe ihres Gottes" ist nicht die Ortsnaehe:
  en *nearness*, romanische Reihe unveraendert.

## Aufgeloeste Kollisionen

- **3,8 `versammeln` ↔ `zusammenbringen`** — aufgeloest nach **Micha
  4,6**, wo derselbe Zusammenstoss schon entschieden war.
- **3,17 `laut` ↔ `stark`** — `stark` behaelt die starke Bindung (27),
  `laut` weicht auf *sonoro · retentissant · sonoro* aus. In 1,10 steht
  `laut` ohne Kollision und behaelt deshalb die Bestandsreihe
  *fuerte · forte*: aufgeloest wird nur im Kollisionsvers.
- **3,5 `lässt` ↔ `tut`** — `lässt` traegt die woertliche Kopfwortreihe
  *lets · deja · laisse · lascia*, die Kausativbedeutung steckt im
  Mehrwort `kommen lassen`. Die Kopfwortkonvention.

## Die `spricht`-Stellungsregel, dritter Fall

2,9 liest „spricht der HERR der Heerscharen, **der Gott Israels**" —
nachgestellt, aber mit Apposition, also fr `parle`. 1,2 · 1,3 · 1,10 ·
3,8 · 3,20 sind nachgestellt ohne Apposition und lesen `dit`. Das Buch
bestaetigt die Regel in beiden Richtungen.

## Ausgabenbefunde

- **RIV 1,18 `ivorato`** statt *divorato* — Anlautverlust hinter `sarà`
  (1× gegen 28×). In `RIV_ANLAUTFEHLER.md` nachgetragen.
- **RIV 3,6 „Io ha sterminato"** — 1.-Person-Pronomen mit
  3.-Person-Verb (muesste „ho"). Die dritte Fehlerklasse: ein falsches,
  aber echtes Wort. Keine Glosse betroffen.
- **RIV 3,10 „i miei figliuoli dispersi"** wo der deutsche Text „mein
  zerstreutes Volk" hat — echte Vorlagendifferenz, kein Setzfehler.
- **WEB 3,8 „until the day that I rise up to the prey"**, RV „para el
  despojo", LSG „pour le butin", RIV „per il bottino" — alle vier gegen
  den deutschen „um Zeugnis abzulegen". Der `BEFUND_TEXTGRUNDLAGE`-Fall:
  der deutsche Text entscheidet, `Zeugnis ablegen` gesetzt.
- **LSG 3,20** endet mit einem freistehenden `~`. Nicht glossiert,
  nicht gezaehlt.

## Bestandsbefund

**Jeremia 33,22** traegt fr `des` vor dem maskulinen Singular `ciel`
(Bestand: 106× `du`, 2× `des`). Der Kapitel-1-Agent wollte den Block
„das Heer des Himmels" von dort uebernehmen, sah den Fehler und setzte
in 1,5 `du`. Steht in `NACHLESE_BESTAND.md`.

## Fehlalarme, am Vers geprueft und stehen gelassen

- `kongruenz` meldet 2,10 `sich erheben` fr `ont` → `sont`. Der Vers
  liest „weil sie das Volk … **verhoehnt und** sich ueber sie erhoben
  haben" — das Hilfsverb traegt zugleich ein zweites, nicht reflexives
  Partizip. `ont`/`hanno` ist richtig. Genau der Fall, den die
  Werkzeugwarnung beschreibt.
- `sweeplemma` meldet 1,14 `nahe kommen`. Der Vers liest „ist nahe, er
  ist nahe und kommt sehr schnell" — praedikatives `nahe`, eigenes
  `kommt`, keine Wendung.
- 3,7 „**Fuerchte mich** doch" ist kein Reflexiv, sondern „fuerchte
  **mich** = fear me"; alle vier Ausgaben lesen so. Deshalb kein
  Mehrwort und es *Teme* statt *Temas*.
- 3,6 „so leer gemacht, dass" — `so` ist Gradadverb zu `leer`, nicht
  die konsekutive Klammer. Sonst traegen `so … dass` und `sodass` im
  selben Vers dieselbe Glosse.
