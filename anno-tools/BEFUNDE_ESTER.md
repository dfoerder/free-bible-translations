# Bestandsbefunde aus Ester — gemeldet, nicht korrigiert

Was Agenten im **fertigen Bestand** oder in den **Referenzausgaben** gefunden
haben, während sie Ester annotierten.

## Aus den Kapiteln 1 bis 3

- **`herrschen` hat im Bestand keine saubere „regieren"-Lesart.** Die
  Kombination *reinaba · régnait · regnava* ist dort durchgehend an englisch
  ***prevailed*** gekoppelt (10 Belege, alle „Hungersnot herrschte"). Für
  Ester 1,1 („der über 127 Länder herrschte") wäre das eine Lexikonfalle
  gewesen; dort steht jetzt *reigned · reinaba · régnait · regnava* — eine neue
  Kombination. **Korpusweit zu prüfen.**
- **`Getränk`:** `BINDUNGEN_AT.md` nennt *beverage · bebida · boisson ·
  bevanda* (7/10), der einzige Beleg im Bestand (Jer 42,1.15) trägt aber
  *drinks · bebidas · boissons · bevande* auf A2.
- **`reichen` hat 20 Lesarten und keine für „darreichen".** Est 1,7
  (`gereicht` = *served*) ist die erste.
- **`Erlass` gab es im Bestand nicht.** In Ester dreifach auseinandergelaufen
  und an den Ausgaben entschieden: *decree · decreto · édit · editto*, B2.
  Kapitel 3 war auf *edict* ausgewichen, um `Anordnung` (*decree*, 7 Belege)
  Platz zu machen — aber **`Anordnung` kommt in Ester gar nicht vor**. Eine
  Auflösung ohne Kollisionsstelle macht den Bestand nur inkonsistent.
- **`Ohr` italienisch weiter uneinheitlich** (42 *orecchi* / 10 *orecchie*).
  Est 2,22 folgt der Mehrwortvorlage `zu Ohren kommen` (1Mo 35,22) mit
  *alle orecchie*. Der Bruch aus `BEFUNDE_NEHEMIA.md` bleibt offen.
- **`nur` und `allein` teilen sich in nur 6 Bestandsversen eine Glosse** — also
  **keine** korpusweite Praxis. In Est 3,6 stehen beide im selben Vers und sind
  verse-lokal getrennt worden.

## Befunde in den Referenzausgaben selbst

Diese betreffen nicht den Bestand, sondern die Quellen — und sie sind der
Grund, warum die Regel „folge der Ausgabe" eine Mehrheitsentscheidung braucht,
wenn die Ausgabe selbst schwankt.

- **WEB schreibt `Susa` innerhalb desselben Buches zweierlei:** *Shushan* in
  1,2 · 1,5 · 3,15 · 4,8 · 4,16 · 9,13–18, *Susa* in 2,3 · 2,5 · 2,8 ·
  8,14–15 · 9,6–12. Die Annotation folgt der Bestandsbindung *Shushan*
  (Neh 1,1) und schreibt sie durchgehend fort.
- **LSG1910 schreibt `Hegai` zweierlei:** *Hégué* in 2,3, *Hégaï* in 2,8 ·
  2,15. Mehrheitsform *Hégaï* genommen.
- **RIV1927 hat in Kapitel 2 zwei Setzfehler:** „figliuolo di **cimei**" (2,5,
  gemeint Simei) und „il **ettimo** anno" (2,16). Der Bestand (*di Simei*) und
  die korrekte Ordinalform (*settimo*) gehen vor.
- **WEB schreibt den Kämmerer in 1,10 „Carcass"** — im Lesefluss stünde an
  einem Personennamen das englische Wort für Kadaver. Die drei anderen
  Ausgaben schreiben *Carcas*, und die gilt. Die Ausnahme ist in
  `AUFTRAG_AT.md` festgehalten.
- **`Tharsis`:** die Ausgaben schreiben uneinheitlich, der Bestand hat aus zwei
  Belegen *Tarshish · Tarsis · Tarsis · Tarsis*. Bindung geht vor.
- **RIV1927 schreibt `Bigthan` im selben Buch zweierlei** — *Bightan* in 2,21,
  *Bigthan* in 6,2. Ein Buchstabendreher, und zwar in derselben RIV-Passage,
  in der schon `cimei` und `ettimo` stehen. Auf *Bigthan* vereinheitlicht
  (2,21 und 6,2), weil das Italienische keinen Grund hat zu variieren und die
  drei anderen Ausgaben es stützen.
- **WEB schreibt `Bigthan` in 2,21 und `Bigthana` in 6,2** — das ist **kein**
  Fehler, sondern folgt dem Hebräischen (בִּגְתָן / בִּגְתָנָא). Weil der
  deutsche Text an beiden Stellen `Bigthan` hat und es dieselbe Person ist,
  bleibt die englische Glosse einheitlich *Bigthan*: eine Namensvariante ohne
  Referenzunterschied gehört nicht in den Lesefluss.
- **`Seres` ist ein Homograph wie `Sethar`** — 1Chr 7,16 der Bruder des Peres
  (*Sheresh*), in Ester Hamans Frau (*Zeresh*). Beide Agenten haben es
  unabhängig an den Ausgaben geprüft; nachgerechnet an 5,10 · 5,14 · 6,13 in
  allen vier Ausgaben.

## Werkzeugbefunde

**`vorab.py` führte bei Eigennamen aktiv in die Irre.** Die Tabelle schlägt die
Bestandslesart einer **Wortform** nach und weiß nicht, ob derselbe Träger
gemeint ist. Für `Seres` bot sie *Sheresh · Seres · Schéresch · Seres* mit
einem Beleg an — der Beleg ist **1Chr 7,16**, wo Seres der Bruder des Peres
ist. Hamans Frau schreiben alle vier Ausgaben *Zeresh · Zeres · Zéresch ·
Zeresh*. Der Agent von Kapitel 5 hat die Tabelle an den Ausgaben widerlegt;
unabhängig nachgeprüft an 5,10 · 5,14 · 6,13 in allen vier Ausgaben.

Derselbe Fall wie `Sethar` in Ester 1,10/1,14 — nur dass der dort **nicht** im
Bestand stand und die Tabelle deshalb schwieg. Seither trägt jede
großgeschriebene Zeile in `vorab.py` einen Warnhinweis **mit Belegstelle**:
`Seres | … | 1 ⚠ 1. Chronika 7,16`. Die bloße Zahl ist bei einem Eigennamen
wertlos — erst die Stelle zeigt, dass sie aus einem anderen Zusammenhang kommt.

**`lexicon.py` und `hints.py` verlieren das Lemma `laden`.** `geladen`
(Est 5,12) steht im Extrakt nur unter VERWANDT bei `Geladener`/`gelangen`,
obwohl der Bestand 36 Belege für `laden` auf B1 hat, darunter genau die
Einladungs-Lesart. Aufgedeckt hat es wieder nur `levelcheck.py` — die
Präfixverb-Lücke, viertes Vorkommen in Ester.

**Der Bestand widerspricht sich bei `kleiden`:** das Simplex steht auf B2
(22 Belege), das Reflexivum `sich kleiden` auf B1 (2 Belege). Beide Lemmata
sind fortgeschrieben worden; die Stufung ist in sich unstimmig.

## Werkzeugbefund

**`hints.py` widerspricht sich bei `Pfahl` selbst:** es listet die Form als
unbelegt und nennt im selben Eintrag `Pfahl` als verwandten Stamm. Der Singular
ist tatsächlich unbelegt, der Plural `Pfähle` steht dreimal. Harmlos, aber es
zeigt, dass der VERWANDT-Abschnitt das Lemma nicht gegen die Formliste prüft.

## Ein Prozessfehler von mir, nicht von den Agenten

Für die Wellenbriefings habe ich die Wiederholungsblöcke mit `bloecke.py`
vermessen — aber die **Verspaare von Hand ausgewählt**, aus dem Gefühl heraus,
welche Verse zusammengehören könnten. Für Ester 8 nannte meine Tabelle fünf
Blöcke.

Der Agent hat `parallelen_ch8.md` gelesen und **siebzehn** gefunden, darunter
den mit Abstand längsten des Kapitels: **8,13 ← 3,14, Block der Länge 19,
Ähnlichkeit 0,74** — der ganze Anfang von 8,13 ist wörtlich. In meiner Tabelle
stand er nicht.

**Die Datei lag vor.** Ich hatte `parallelen.py` für die Kapitel 7, 8 und 10 im
Hintergrund laufen lassen, bevor ich das Briefing schrieb, und dann aus
Handauswahl geschrieben statt aus der Ausgabe. Der Fehler ist nicht die
Werkzeugkette, sondern ihre Nichtbenutzung.

**Regel für kommende Bücher:** Das Wellenbriefing wird aus `parallelen.py`
**abgeschrieben**, nicht aus geratenen Verspaaren zusammengestellt.
`bloecke.py` ist für die Nachmessung eines einzelnen, bereits bekannten Paares
da — nicht für die Suche.

## Zwei Bestandsdefekte, die Ester 9 und 10 aufgedeckt haben

**Die Ordinalzahlen waren uneinheitlich gestuft.** `vierzehnt` stand in allen
22 Belegen auf **B1**, während die ganze Zehnerklasse — `elft`, `zwölft`,
`dreizehnt`, `fünfzehnt`, `sechzehnt`, `siebzehnt`, `achtzehnt`, `neunzehnt`,
`zwanzigst` — durchgehend **A2** ist. Ein Einzelausreißer gegen seine gesamte
Klasse, uniform in sich und deshalb von `levelcheck.py` nicht zu finden (das
meldet nur, wo der Bestand einheitlich ist und ein *Kapitel* abweicht).
Gezogen, dazu `einundzwanzigst`.

**Der Versuch, es zu ziehen, hat einen Konstruktionsfehler in `buildbook.py`
freigelegt** — siehe unten. Die niedrigen Ordinalia sind weiter uneinheitlich
(`sechst` A2 gegen `siebt`/`acht` A1), aber dort mischen sich Kardinal- und
Ordinalhomographen; nicht angefasst.

**`begehen`, `ausfallen`, `zutragen` sind im Bestand bedeutungsverschoben.**
`begehen` kennt nur „eine Sünde begehen" (46 Belege), Est 9,22 meint „ein Fest
begehen"; `ausfallen` kennt nur den Haarausfall aus 3Mo 13,40, Est 9,28 meint
„nicht mehr gehalten werden"; `zutragen` kennt nur `sich zutragen` =
*happen*, Est 9,26 meint „berichtet werden". Alle drei mit eigener Glosse am
selben Lemma versehen.

**`bedrohen` ist rein neutestamentlich belegt** (4 Belege, alle *rebuked* —
Jesus bedroht Wind und Dämonen). Est 8,11 meint es im Wortsinn.

## Der Konstruktionsfehler in `buildbook.py`

Durchgang 2 des Level-Abgleichs bestimmte die Korpusmehrheit je Lemma aus den
**gebauten** Dateien der anderen Bücher. Damit war eine korpusweite
Levelkorrektur über die Quellen **prinzipiell unmöglich**: wer `vierzehnt` in
allen 22 Quellen von B1 auf A2 zieht, bekommt beim Bauen von Buch 6 die 42 noch
nicht gebauten Bücher als B1-Mehrheit entgegen — und die Änderung zurück. Bei
jedem Buch, in jeder Reihenfolge, beliebig oft wiederholt. Ein stabiler
Attraktor am falschen Ort.

Die Mehrheit kommt jetzt aus den **Kapitelquellen**; die gebaute Datei springt
nur ein, wo eine Quelle fehlt. Die Quelle ist der bearbeitete Stand und damit
die Autorität — die gebaute Datei ist ihr Ergebnis.

**Der Neubau hat dabei eine Regression ausgelöst, die zu diesem Fehler gehört:**
`Kidron` in Johannes 18,1 stand in der Quelle italienisch auf *Kidron*, in der
gebauten Datei auf *Cedron*. Eine Korrektur hatte also nur in der gebauten
Datei gelebt — genau das, wovor die Werkzeugdoku warnt. Beide Stände waren
falsch: RIV1927 schreibt an allen acht alttestamentlichen Stellen *Kidron* und
in Johannes 18,1 ***Chedron***, weil es dort dem griechischen Κεδρών folgt. Die
Ausgabe unterscheidet also selbst zwischen AT und NT; auf *Chedron* gesetzt, in
Quelle **und** Datei.
