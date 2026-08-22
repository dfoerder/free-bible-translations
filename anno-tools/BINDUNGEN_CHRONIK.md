# BINDUNGEN_CHRONIK — die Formeln und Fallen von 1. und 2. Chronik

Von Hand gepflegt, wie `BINDUNGEN_KOENIGE.md`. **Nicht** von `bindungen.py`
erzeugt: die Formelwörter hier sind Allerweltswörter (`war`, `Söhne`, `Dies`),
deren Korpusmehrheit aus ganz anderen Kontexten stammt.

Diese Datei existiert, weil die Chronik **fast durchgehend Parallelen** zu
schon annotierten Büchern hat und weil ihre Kapitel 1–9 aus Namenslisten
bestehen. Beides erzeugt Fehler, die kein Prüfskript meldet.

## Die Genealogie-Kopula

> X **war** der Vater von Y.

| Fall | `war` fr/es/it |
|---|---|
| `war der Vater von` / `war Vater von` | **fue · fut · fu** |
| jede andere Verwendung | nach Kontext (*era*, *estaba*, *había* …) |

Die Perfektlesart ist die Mehrheit (64:18) und steht in den **direkten
Vorlagen** der Chronik-Genealogien: 1Mo 4,18 und Ruth 4,18–22. Der Ausreißer
war 1Mo 10, und weil 1Chr 1 sich daran orientiert hat, ist die falsche Lesart
über 1Chr 2 weitergewandert. 44 Einträge in fünf Büchern sind nachgezogen.

**Achtung, blinder Fleck:** `war` steht auf der Funktionswortliste und fällt
deshalb aus dem paarweisen Kapitelabgleich heraus. In einer Genealogie ist es
aber das Wort, das die ganze Textsorte trägt. **Beim Abgleich von
Genealogie-Kapiteln die Kopula ausdrücklich mitprüfen.**

## Die Listenmuster der Genealogien

| Muster | Behandlung |
|---|---|
| `Die Söhne X-s sind/waren:` | `Die`=The·Los·Les·I · `Söhne`=sons·hijos·fils·figli · `sind`=are·son·sont·sono · `waren`=were·fueron·furent·furono. Der Genitiv am Namen trägt die Präposition: `Judas` → *of Judah · de Judá · de Juda · di Giuda*; Lemma = Nominativ |
| `Die Söhne von X` | `von` = *of · de · de · di*, der Name steht bloß |
| `Die Söhne des <Eigenname>` | `des` = *of · de · de · di*, **nicht** *of the* |
| `X war der Vater der Y-iter` | `der` = *of the · de los · des · dei*, Völkername im **Plural** |
| `dem Y-iter` (Dativ Sg.) | Glosse **Singular** |
| `Das sind (alle/alles) Söhne X-s` | `Das` Lemma **`der`** = *These · Estos · **Ce** · Questi* |
| `Dies sind …` | `Dies` Lemma `dies`, fr **`Voici`** |
| `Dies ist …` | `Dies` Lemma `dies`, fr *Ceci* |
| `dessen Sohn war X` | `dessen` B1 = *his · su · son · il suo* |

Ordnungszahlen: attributiv `erster Sohn` → es **`primer`**; freistehend
(`der erste:`, `des zweiten`) → es **`primero`**, `segundo`, `tercero` …

## Gentilizia

Zwei Schemata, und die Wahl hängt an Numerus und Funktion:

| Fall | Schema | Beispiel |
|---|---|---|
| **Sippenname im Plural** (4Mo-26-Schema) | en *Xites* · es *xitas* (**klein**) · fr *Xites* (**groß**) · it *Xiti* (**groß**) | `Netofatiter`, `Zorathiter`, `Kiniter` |
| **Epitheton im Singular** (2Sam-23-Schema) | en *Xite* · es *xita* · fr *de X* / *d'X* · it *da X* | `der Ahohiter`, `der Mithniter` |

**Warnung zum Massenzug.** Ein Skript, das Gentilizia über die Endung `-iter`
filtert, trifft auch `weiter`, `Reiter`, `Arbeiter`, `Leiter`, `Begleiter`,
`Mitarbeiter` — beim Versuch, die italienische Großschreibung nachzuziehen,
waren so **1000 Einträge in allen Büchern** betroffen statt der sechs
gemeinten. Der Zug ist vollständig zurückgesetzt worden. **Jeder korpusweite
Zug wird erst gezählt und die Trefferliste angesehen, bevor geschrieben wird**
— die Zahl allein verrät den Fehler sofort.

Offen geblieben ist dabei `Kahathiter` = it **`kehatiti`** (9 Belege,
durchgehend klein). Es steht gegen das Schema, ist in sich aber konsistent;
eine Angleichung wäre ein eigener, gezählter Zug.

### Die levitischen Sippennamen sind im Italienischen klein — alle

`Kahathiter` ist **kein Einzelfall**, sondern die Spitze einer geschlossenen
Gruppe. Der Bestand schreibt die Leviten-Sippen im Italienischen durchgehend
klein, und zwar einheitlich:

| Sippe | it | Belege |
|---|---|---|
| `Gersoniter` | `ghersoniti` | 6, darunter ch23,7 |
| `Jizhariter` | `ishariti` | 2, darunter ch24,22 |
| `Kahathiter` | `kehatiti` | 9–10 |
| `Merariter` | `merariti` | |
| `Hebroniter` | `ebroniti` | |
| `Amramiter` | `amramiti` | |
| `Usieliter` | `uzzieliti` | |

**Die Ausnahme ist `Korahiter`**: dort steht der Bestand 3:1 auf **groß**, und
die direkte Torhüter-Vorlage 1Chr 9,19 hat `Coreiti`. Folge: in **26,19 steht
`Coreiti` neben `merariti`**, im selben Vers. Das ist bekannt und bleibt
stehen; eine Vereinheitlichung ist ein eigener, gezählter Zug über etwa
zwanzig Einträge — nicht über tausend, denn der `-iter`-Filter ist die Falle
von oben.

Die Belegbasis ist dünn: `Merariter`, `Hebroniter`, `Amramiter`, `Jizhariter`
und `Usieliter` stehen je nur ein- bis zweimal, fast alle aus 4Mo 3,27 und
26,57 f.

**Die Groß-/Kleinschreibung ist ausgezählt, nicht geraten:** im Bestand stehen
Gentilizia im **Spanischen zu 843:33 klein** und im **Italienischen zu 704:172
groß**. Die 172 italienischen Kleinschreibungen sind fast alle die
`da X`-Formen des Singular-Schemas, wo nur die Präposition kleingeschrieben
ist. 16 echte Ausreißer in 1Chr 2 und 5 sind nachgezogen worden.

Feminine Epitheta tragen echte Adjektive, nicht *de X*: `Jesreelitin` =
*Jezreelitess · jezreelita · Jizreélite · Izreelita*, ebenso `Karmelitin`.
Das weicht bewusst vom maskulinen `Karmeliter` (*de Carmel*) ab — „la de
Carmel" ist nach dem Artikel nicht lesbar.

## Schreibungsvarianten: die Regel und ihre Reichweite

> **Jede Stelle behält ihre eigene Schreibung als Lemma, beide teilen die
> Glosse.**

So ist der Bestand mit `Gräuel`/`Greuel` und `Hesbon`/`Heschbon` verfahren.
Allein 1Chr 1 hat **18 solche Paare** gegenüber 1. Mose, und in keinem Fall
war ein neuer Name zu prägen: `Zephi`/`Zepho`, `Homam`/`Heman`,
`Aljan`/`Alwan`, `Sephi`/`Sepho`, `Hamran`/`Hemdan`, `Saawan`/`Sawan`,
`Jaakan`/`Akan`, `Mizbar`/`Mibzar`, `Thogarma`/`Thorgama`,
`Tharsisa`/`Tharsis`, `Adbeel`/`Abdeel`, `Hadad`/`Hadar`, `Pagi`/`Pagu` u. a.

Dazu aus den Erzählkapiteln: `Jabes`/`Jabesch`, `Malchisua`/`Malkischua`,
`Bath-Sua`/`Batseba`, `Jechonja`/`Jojachin`, `Chalubai`/`Kaleb`,
`Asahael`/`Asahel`, `Kiniter`/`Keniter`, `Nathanel`/`Nathanael`.

**Die Grenze:** zwei *verschiedene* deutsche Schreibungen im selben Buch sind
zwei Lemmata mit **eigenen** Glossen, wenn der Bestand sie schon trennt —
`Pelet` (1Chr 2,47) und `Peleth` (2,33) sind zwei Wörter, und eine Glosse aus
dem einen gehört nicht ans andere.

## Lemma-Fallen des Extrakts

Der Lexikon-Extrakt trennt nicht nach Testamenten und nicht nach Personen.
Wer ihm folgt, glossiert regelmäßig den falschen Mann:

| Form | Extrakt zeigt | in der Chronik ist es |
|---|---|---|
| `Berechja` | *Barachiah* (Mt 23,35, griechische Form) | **Berechiah** (1Chr 3,20) |
| `Johanan` | *Joanan* (Lk 3,27, Genealogie Jesu) | **Johanan** ben Kareach bzw. Josias Sohn |
| `Simri` | *Zimri* (Königsbücher) | **Shimri** (1Chr 11,45) |
| `Hezro` | steht im Bestand unter der Form `Hezrai` | dieselbe Person, Form `Hezro` (11,37) |
| `Elisa` | *Elisha* (82 Belege, der Prophet) | **Elishah**, Javans Sohn (1Chr 1,7) |
| `Gomer` | Person **und** das Hohlmaß Omer unter einem Lemma | die Person |
| `Moza` | *Mozah*, ein Ort (Jos 18,26) | eine Person (1Chr 2,46) |
| `Usia`, `Jesaja`, `Hiskia`, `Daniel`, `Seraja`, `Adrammelech` | der bekannte Träger | ein anderer Träger, **dieselbe** Glosse |

Die letzte Zeile ist die Gegenprobe: **zwei Träger mit demselben Namen
bekommen dieselbe Glosse.** Nur wo die Glosse selbst einer anderen Tradition
folgt (NT-Griechisch, ein anderer Name), wird sie ersetzt.

## 2. Chronik: die Parallelen sind noch schärfer

**Die gemessenen Versätze reichen von −355 bis +1062** — in 1. Chronik waren
es −49 bis +34. Das liegt daran, dass 2. Chronik ganze Erzählbögen der
Königsbücher aufgreift, sie aber anders einteilt, kürzt und erweitert. **Ein
übertragener Block landet in diesem Buch nicht drei Positionen daneben,
sondern dreihundert.**

Auch *innerhalb* eines Kapitelpaars streuen die Versätze weit: 2Chr 25 gegen
2Kön 14 von −332 bis +58, 2Chr 34 gegen 2Kön 22 von −237 bis 0. Ein am
Kapitelanfang gemessener Versatz gilt am Kapitelende nicht mehr. **Jeder Block
wird einzeln gemessen.**

### Die Parallelenkarte steht in einer eigenen Datei

**`PARALLELEN_2CHR.md`** listet für **jeden Vers** des Buches die beste
Entsprechung, die Zahl der gemeinsamen Tokens, den Versatz *innerhalb* des
Verspaars und beide Verslängen. Jeder Agentenauftrag verweist darauf.

**Die erste Fassung dieser Karte war grob falsch**, weil sie Kapitel gegen
Kapitel gemessen hat. Damit fällt jede Parallele durch, die über eine
Kapitelgrenze der Quelle läuft: 2Chr 5,1 galt als Sondergut, obwohl es mit 27
gemeinsamen Tokens die engste Parallele seines Kapitels zu **1Kön 7,51** ist —
gefunden hat es der Agent, weil er selbst nachgemessen hat. Ebenso stand
2Chr 12 mit 8 % in der Tabelle und hat in Wahrheit 26 %.

Versweise gemessen sieht das Buch so aus:

| Anteil | Kapitel |
|---|---|
| **über 40 %** | 18 (46) · 10 (45) · 5 (43) · 6 (43) |
| 20–40 % | 9 (38) · 12 (26) · 22 (24) · 33 (24) · 27 (23) · 21 (22) |
| 10–20 % | 25 (19) · 34 (19) · 7 (18) · 16 (18) · 36 (18) · 11 (16) |
| unter 10 % | 4 · 23 · 28 · 1 · 26 · 8 · 2 · 13 · 20 · 24 · 29 · 32 · 15 · 30 · 35 |
| **echtes Sondergut** (kein Vers mit Parallele) | **3 · 14 · 17 · 19 · 31** |

Es sind also **fünf** Sondergut-Kapitel, nicht fünfzehn.

**Achtung**: 2Chr 30, 35 und 36 haben Parallelen in **Esra**, 2Chr 29 in
1. Chronik. Esra, Nehemia und Jeremia sind **noch nicht annotiert** und stehen
als Vorlage nicht zur Verfügung — `PARALLELEN_2CHR.md` markiert das.

**Achtung bei 1, 2 und 3.** Sie *erzählen* dieselbe Sache wie 1Kön 3, 5 und 6
(Gibeon, der Vertrag mit dem König von Tyrus, der Tempelbau), aber der Chronist
formuliert neu — versweise gemessen bleiben 6 %, 4 % und 0 %. Das ist die
gefährlichste Sorte Parallele: inhaltsgleich, wortverschieden. **Wer abschreibt,
glossiert falsch.**

### Die Formeln der Königsbücher gelten weiter

`BINDUNGEN_KOENIGE.md` ist für dieses Buch **mitverbindlich**: die Quellen- und
Chronikformel, die Botenformel (`spricht` fr *parle* einleitend, *dit*
nachgestellt), `l'ÉTERNEL` statt `le`, die Nachfolgeformel `an seiner Stelle`
und die Todesformel-Familie. 2. Chronik hat eigene Fassungen der Quellenformel
(„in der Geschichte des Propheten …"), die **nicht** die der Königsbücher sind —
am Vers prüfen.

### Eine Kollisionsauflösung im Quellvers ist nicht übertragbar

Der Bestand enthält an vielen Stellen Lesarten, die **nur** dastehen, weil im
selben Vers ein zweites Wort dieselbe Glosse getragen hätte. Wer eine solche
Lesart in den Parallelvers übernimmt, ohne zu prüfen, ob der Grund dort
überhaupt vorliegt, schreibt eine Ausweichung fort, die nichts mehr ausweicht.

Der Musterfall: **1Kön 8,24** glossiert `zugesagt` als *pledged · asegurado ·
assuré · assicurato* statt der Korpusmehrheit *promised* (6:1). Der Grund steht
im selben Vers — „Mit deinem Mund hast du es **versprochen**". **2Chr 6,15
schreibt an dieser Stelle `gesagt`.** Die Kollision existiert dort nicht, und
die Ausweichung war zurückzunehmen.

**Also: bei jeder aus einer Parallele übernommenen Lesart prüfen, ob ihr Grund
im eigenen Vers vorliegt.** Umgekehrt gilt dasselbe — eine Auflösung bleibt
**lokal**: `bronzen` steht 36-mal auf *bronze* und nur in 1Chr 18,8 auf
*of bronze*, `beide` steht 104-mal auf *two* und weicht nur dort auf *both*
aus, wo `zwei` danebensteht.

### Offener Befund: `bis zum` doppelt die Präposition

Der Agent von 2Chr 19 hat gemeldet, dass 2Chr 7,8 und 1Kön 8,65 spanisch
„hasta al" und französisch „jusqu'à au" ergeben — die Präposition steht zweimal.
Nachgezählt über den ganzen Bestand: **245 Paare `bis` + `zum`/`zur`,
verteilt auf 34 verschiedene Kombinationen.**

| Muster | Anzahl | Bewertung |
|---|---|---|
| es «hasta el/la/las» | ~149 | richtig |
| **es «hasta al»** | **40** | Präposition doppelt |
| **es «hasta a la» / «hasta a»** | **28** | Präposition doppelt |
| **fr «jusqu'à au»** | **18** | Präposition doppelt |
| **fr «jusqu'à à la» / «jusqu'à à l'»** | **20** | Präposition doppelt |
| **fr «jusqu'au au»** | **3** | Präposition doppelt |

Die sauberen Aufteilungen sind: **es** `bis` = *hasta*, `zum` = *el* / `zur` =
*la* — die Präposition steckt bei `bis`, der Artikel bei `zum`. **fr** entweder
`bis` = *jusqu'* mit `zum` = *au*, oder `bis` = *jusqu'à* mit `zum` = *le/la*.

**Nicht angefasst.** Anders als bei der Elision vor `HERR` hängt die richtige
Fassung hier davon ab, **wie die App zwei benachbarte Glossen zusammensetzt** —
ob mit Leerzeichen, ob überhaupt. Das ist keine Frage, die sich aus dem Bestand
allein entscheiden lässt. Der Zug betrifft rund **96 Einträge** und wartet auf
eine Entscheidung.

### Namen, die in 2. Chronik leicht ineinanderrutschen

| Text schreibt | ist | nicht zu verwechseln mit |
|---|---|---|
| **`Joschafat`** (35 Belege, ab 2Chr 17,1) | der König von Juda, *Jehoshaphat · Josafat · Josaphat · Giosafat* | — **nicht** `Josaphat`; diese Schreibung gibt es im l1912mod nicht |
| **`Amasja`** (genau **1×**, 2Chr 17,16) | ein Heerführer Joschafats, *Amasiah · Amasías · Amasia · Amasia* | **`Amazja`** (18×, Kap. 24–25), der **König**, *Amaziah · Amasías · Amatsia · Amazia* |
| **`Michaja`** (2Chr 13,2 · 17,7) | Abias Mutter bzw. ein Fürst, *Micaiah · Micaías · Micaja · Micaia* | `Micha` in Kap. 18, der Prophet |
| **`Huram`** | der König von Tyrus **und** der Benjaminit aus 1Chr 8,5 — ein Lemma, eine Glosse *Huram ×4* | `Hiram`, das die Chronik nie schreibt |
| **`Asael`** (2Chr 17,8) | Schreibungsvariante, geteilte Glosse mit `Asahel` | `Asahael` (1Chr 2,16), wieder eine dritte Schreibung |
| **`Hethiter`** (8,7) und **`Hetiter`** (1,17) | dieselbe Glosse, zwei Lemmata | — |

`Amasja` und `Amazja` fallen im **Spanischen** beide auf *Amasías*. Sie stehen
nirgends im selben Vers; nach SPEC bleibt das unaufgelöst.

### Entscheidungen aus Welle 1 (2Chr 1–3)

**`bauen` ist formgebunden, nicht tempusgebunden.** Ausgezählt über den ganzen
Bestand:

| Form | es · it | Belege |
|---|---|---|
| `bauen` (Inf.) | **construir · costruire** | 45 : 6 |
| `baute` (3. Sg. Prät.) | **edificó · edificò** | 72 : 1 |
| `bauten` (3. Pl. Prät.) | **construyeron · costruirono** | 10 : 2 |
| `gebaut` (Part.) | **construido · costruito** | 43 : 0 |
| `baut`, `baue` | gespalten — am Vers entscheiden | |

Französisch hat durchgehend `bâtir`/`bâtit`, Englisch `build`/`built`. Also:
**nur die Form `baute` geht auf `edificar`/`edificare`**, alles andere auf
`construir`/`costruire`. Nicht auf eine Familie vereinheitlichen.

**`Huram` bleibt `Huram`.** Der König von Tyrus heißt in der Chronik `Huram`,
in 2Sam 5 und 1Kön 5 `Hiram` — und im ganzen Alten Testament steht `Hiram`
**nur** an diesen zwölf Stellen. Er bekommt trotzdem nicht die `Hiram`-Glosse:
`Huram` ist bereits ein Lemma des Bestands (1Chr 8,5, ein Benjaminit), und für
**zwei Träger unter einem Lemma** gilt „ein Name, eine Glosse". Die
Schreibungsvariantenregel greift nur *zwischen* zwei Lemmata. Verbindlich:
`Huram` A1 = *Huram · Huram · Huram · Huram*. Präzedenz ist `Ornan`, das in
1Chr 21 ebenfalls die Chronik-Schreibung behalten hat statt der Samuel-Form
`Arawna`.

Ebenso `Jafo` (2Chr 2,15) = *Joppa · Jope · Joppé · Ioppe* — hier greift die
Schreibungsvariantenregel, weil `Joppe` ein anderes Lemma ist.

**`zum` in `zum König machen`** steht im Bestand 14:3 auf
*as · como · comme · come*. Die drei Ausnahmen (1Kön 3,7 · 1Sam 11,15 ·
1Chr 28,4) sind sämtlich **lokale Kollisionsauflösungen**. Also: Mehrheit,
außer der Vers enthält `wie` oder `als`. Die Bedeutung trägt ohnehin der
Mehrwort-Eintrag `zum König machen` = *made king · proclamó rey · établit roi ·
costituì re*.

**`Herrschaft`** im Regierungs-Sinn: *reign · reinado · règne · **dominio***
(Bestand 12:4 gegen *regno*). Gilt für beide Chronikbücher.

## Die Parallelen sind der bestimmende Umstand

Fast jedes Kapitel hat eine Parallele in einem schon annotierten Buch. Die
Lexikon-Abdeckung reicht deshalb von 70 % (Genealogien mit eigenem Personal)
bis **97 %** (1Chr 10 gegen 1Sam 31, der höchste Wert des Projekts).

**Das ist keine Erleichterung, sondern die Hauptgefahr.** Gemessene Versätze:

| Stelle | Parallele | Versatz |
|---|---|---|
| 1Chr 10 | 1Sam 31 | 27 gemeinsame Blöcke, nur **8** auf ±0, sonst bis +14 |
| 1Chr 11,10–47 | 2Sam 23,8–39 | wandert monoton von **−1 auf −34** |
| 1Chr 11,1–9 | 2Sam 5,1–10 | zwischen **−1 und −49** |
| 1Chr 21,2 (2Kön) | — | zum Vergleich: −10 bei wortgleichem Block |

**Kein Block wird übertragen.** Jedes Kapitel mit Parallele bekommt ein
eigenes Prüfskript, das die Positionen aus **beiden** Quelltexten ableitet,
den Versatz ausgibt und alle sechs Felder gegeneinander hält.

Und der Chronist kürzt: 1Chr 10,9 nimmt nur den Kopf, wo 1Sam 31,9 ihn
abschlägt; 1Chr 1 lässt die Nimrod-Städte, die Grenzen Kanaans und alle
Altersangaben weg; 1Chr 11 hat 28 Namen mehr und 19 weniger als 2Sam 23.
**Die Parallelstelle liefert das Vokabular, nicht den Satz.**

## Zählangaben sind Prüfungen, keine Deko

Die Chronik zählt ihre eigenen Listen durch. Jede Angabe wird nachgerechnet;
**wo eine Probe nicht aufgeht, ist zuerst der Quelltext zu prüfen.**

Bisher: 1Chr 2 vier Proben, alle auf · 1Chr 3 sechs Proben, **fünf auf** ·
1Chr 12 einundzwanzig Zahlwörter, alle richtig (dort gibt es keine Summe,
12,38 sagt „Alle diese Kriegsleute" ohne Zahl).

**Die Ausnahme: 1Chr 3,22** nennt fünf Namen und sagt „die sechs". Die
Differenz steht schon im Luther 1912 und im masoretischen Text; klassisch
zählt man Semaja aus dem Halbvers davor mit. **Gemeldet, nicht korrigiert.**

## Die Satzzeichen-Tokens von 2. Chronik, richtig gezählt

**Ein Token kann aus mehreren Satzzeichen bestehen.** Neben dem blanken `–`
(U+2013) kommt **`–,`** vor — Gedankenstrich mit angeklebtem Komma, der
schließende Strich eines Klammerpaars vor einem Komma. Ein Zählskript, das nur
nach `–` sucht, übersieht ihn: in 2. Chronik sind das drei Tokens in den
Kapiteln 10, 12 und 22, und in 1. Chronik 26 dieselbe Bauart zweimal.

Richtig zählt man **Tokens, die nach dem Abstreifen aller Satzzeichen leer
bleiben** — genau das tut auch `selfcheck.py` in seiner Gegenrechnung.

Das Buch hat **44** solcher Tokens, nicht 41:

| Kap | Anzahl | Verse (Anzahl je Vers, wenn > 1) |
|---|---|---|
| **1** | 2 | 3(2) |
| **2** | 4 | 3 · 5 · 6 · 13 |
| **3** | 2 | 8(2) |
| **4** | 2 | 21(2) |
| **5** | 5 | 1(2) · 11 · 13(2) |
| **6** | 8 | 9 · 18 · 28(2) · 30(2) · 36(2) |
| **8** | 2 | 6 · 13 |
| **10** | 2 | 2(2) |
| **11** | 1 | 10 |
| **12** | 2 | 3(2) |
| **14** | 2 | 7 · 10 |
| **20** | 3 | 9(2) · 24 |
| **21** | 1 | 13 |
| **22** | 2 | 11(2) |
| **29** | 1 | 32 |
| **32** | 2 | 9(2) |
| **36** | 3 | 18 · 22(2) |

## Der Gedankenstrich

1. Chronik benutzt den **langen Strich** `–` (U+2013) als eigenes Token,
**71-mal** im Buch — deutlich mehr als jedes bisherige Buch (2. Könige: 16
Satzzeichen-Tokens insgesamt). Er bleibt nach SPEC unannotiert.

Verteilung: Kap. 1 (2) · 2 (3) · 3 (6) · 4 (2) · 5 (4) · 7 (6) · 8 (7) ·
9 (2) · 12 (1) · 21 (1) · 23 (5) · 24 (1) · **25 (24)** · 26 (5) · 28 (2).

## „Die Obersten über tausend und über hundert"

Die Wendung steht **fünfmal in 1. Chronik** (13,1 · 26,26 · 27,1 · 28,1 ·
29,6) und danach weiter in 2. Chronik (1,2 · 25,5). Zwei gleichzeitig
laufende Agenten haben sie in 26,26 und 27,1 verschieden geglost, obwohl sie
wörtlich dieselbe ist. Verbindlich:

| Wort | Level | en · es · fr · it |
|---|---|---|
| `Obersten` **bei Truppenkommando** | B2 | **chiefs** · jefes · chefs · capi |
| `Obersten` **der Versammlung** (`Obersten Israels`, `Obersten des Volkes`) | B2 | **leaders** · jefes · chefs · capi |
| `über` | A2 | over · sobre · sur · su |
| `tausend` | A1 | **a thousand** · mil · mille · mille |
| `hundert` | A1 | **a hundred** · cien · cent · cento |

Nur das Englische unterscheidet; Spanisch, Französisch und Italienisch tragen
in beiden Fällen dasselbe. Die Trennung ist ausgezählt: *leaders* hat 11
Belege, alle vom Typ „die Obersten Israels / des Volkes" (1Chr 21,2 · 22,17 ·
23,2 · 24,6), *chiefs* zwei, beide vom Kommandotyp — und **1Chr 15,25 ist die
nächste Parallele**: „die Obersten über Tausend". Die sechs Belege für den
Singular *chief* stehen sämtlich in 1Chr 15,5–8, wo je ein Mann pro Sippe
gemeint ist.

**Achtung in 28,1**: dort stehen **beide** Lesarten im selben Vers — „alle
Obersten Israels" und „die Obersten über tausend und über hundert".

`tausend`/`hundert` ist korpusweit uneinheitlich (*thousand* 6× gegen
*a thousand* 1×, *one hundred* 4× gegen *hundred* 2× gegen *a hundred* 1×),
und ohne Artikel ist „over thousand" im Englischen nicht grammatisch. In
1. Chronik gilt die buchinterne Lesart von 13,1. Der Rest des Bestands
(4Mo 31 viermal, 2Sam 18,1, 1Sam 22,7) wäre ein eigener, gezählter Zug.

## `Jüngerer` und `Älterer`

Der Satzteil `den Jüngeren wie den Älteren` steht in **25,8** und **26,13**
wörtlich gleich und ist von zwei Agenten verschieden geglost *und* verschieden
eingestuft worden. Verbindlich nach 25,8:

| Wort | Level | en · es · fr · it |
|---|---|---|
| `Jüngerer` | A2 | younger · menor · **cadet** · **minore** |
| `Älterer` | A2 | older · mayor · **aîné** · **maggiore** |

Nicht *plus jeune* / *plus âgé* und nicht *più giovane* / *più anziano*.

## Wörter, die in diesem Buch neu entstanden sind

| Wort | Level | en · es · fr · it |
|---|---|---|
| `streitbar` | C1 | battle-ready · aptos para la guerra · aptes à la guerre · atti alla guerra |
| `Geschlecht` (Genealogie) | C1 | lineage · linaje · lignée · stirpe |
| `Sippe` | C1 | clans · clanes · clans · clan |
| `Oberpriester` | C1 | chief priest · sacerdote principal · prêtre en chef · sacerdote capo |
| `Totenbeschwörerin` | C1 | medium · nigromante · nécromancienne · negromante |

`streitbar` ist von zwei Agenten gleichzeitig verschieden geprägt worden
(10,12 gegen 11,26). Die Fassung oben gewinnt, weil die Alternative
(*mighty · aguerridos · **vaillants** · agguerriti*) im Französischen genau
die Glosse von `tapfer` trug. Abzugrenzen bleiben: `tapfer` B2 = *valiant ·
valiente · vaillant · valoroso* und `kampffähig` C1 = *fit for battle ·
aptos para el combate · aptes au combat · atti al combattimento*.

## Namen und Titel, die schon festliegen

`David` A1 = *David · David · David · **Davide*** (508 Belege) ·
`Fürst` B2 = *prince · príncipe · prince · principe* (72 Belege; 2Sam 5,2 und
7,8 sind nachgezogen worden) · `Anführer` B2 = *leader · jefe · chef · capo* ·
**`Oberhaupt` B2 = *head · jefe · chef · capo*** (13 Belege; Plural *heads ·
jefes · chefs · capi*) · `Haupt` C1 = *head · cabeza · tête · capo*, Plural
*heads · cabezas · têtes · teste* · `Hauptmann` B2 = *captain · capitán ·
capitaine · capitano*.

**Die Ausnahme ist 1Chr 11,6**, wo `Oberhaupt`, `Anführer` und `Hauptmann` in
einem Vers stehen. Dort weicht `Oberhaupt` **lokal** auf *cabeza · tête ·
testa* aus. Das ist die einzige Stelle; überall sonst gilt die Mehrheitslesart.
Eine frühere Fassung dieser Tabelle hat den Ausreißer zitiert — gemeldet vom
Agenten von 1Chr 7.

**`Torhüter`** C1 = *gatekeepers · porteros · portiers · portinai* entsteht in
1Chr 15 neu und kommt ab dort 38-mal vor (16 · 23 · 26, 2Chr, Esra, Nehemia).
Es trägt dieselbe Glosse wie das einmalige `Torwächter` (2Kön 7,11); die
beiden stehen nirgends im selben Vers, deshalb bleibt es nach SPEC
unaufgelöst.

**`Posaune`** ist im Bestand *trumpets · trompetas · trompettes · trombe* wie
`Trompete`. Beide stehen im ganzen l1912mod **nur in 1Chr 15,28** zusammen;
dort — und nur dort — weicht `Posaune` auf *horns · bocinas · cors · corni*
aus (Schofar gegen Chatsotserah). Die 39 übrigen Belege bleiben unverändert.
