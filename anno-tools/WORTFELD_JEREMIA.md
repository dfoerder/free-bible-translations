# Wortfeld Jeremia (Buch 24)

Ein Abschnitt je Paket, wie `WORTFELD_JESAJA.md`. Der Prompt des naechsten
Pakets bekommt daraus, was ueber die Kapitelgrenze laeuft.

## 1. Was das Buch von Jesaja unterscheidet

**261 buchinterne Dublettenpaare** (`dubletten.py`), gegen rund fuenf in
Jesaja. Der groesste Teil sind Botenformeln, und sie sind in Paket 1
entschieden. Deshalb steht am Anfang dieses Buches nicht ein Massstabskapitel,
sondern eine **Formelentscheidung**.

Dazu ein Werkzeug, das es fuer Jesaja noch nicht gab: `vorbereitung.py` baut
die Vorbereitungsdatei jedes Pakets maschinell und teilt die Dubletten in die
drei Richtungen auf, die etwas voellig Verschiedenes bedeuten — Vorlage steht
in einem fertigen Kapitel, beide Verse im selben Paket, oder der eigene Vers
ist die Vorlage fuer spaeter. **Die dritte Sorte sieht der Agent, der sie
erzeugt, ueberhaupt nicht.**

## 2. Paket 1 (Kap. 1 · 2 · 3) — die Botenformel des Buches

81 Verse, 2128 Eintraege. Versatz +0 in allen vier Ausgaben und allen drei
Kapiteln. `paketcheck.py` Abschnitt A und C leer, Artikel vor `HERR` null
Korrekturen.

### `Das Wort des HERRN erging an mich` — sieben Felder, siebzehn Kapitel

1,4 und 2,1 sind **woertlich gleich** und lagen in **einem Paket**, also im
toten Winkel: die beiden Agenten konnten einander nicht sehen. Beide haben
`fixgloss.py show ergehen` gefragt, beide dieselbe Vorlage gefunden (1Kön 16,1
und 1Sam 15,10) — und beide dieselbe Reihe gesetzt. **Sieben von sieben
Feldern identisch, ohne Absprache.**

| pos | Form | Lemma · Level | en · es · fr · it |
|---|---|---|---|
| 0 | Das | `der` A1 | The · La · La · La |
| 1 | Wort | `Wort` A1 | word · palabra · parole · parola |
| 2 | des | `der` A1 | of the · **del** · de l' · **del** |
| 3 | HERRN | `HERR` A1 | LORD · SEÑOR · ÉTERNEL · SIGNORE |
| 4 | erging | `ergehen` C1 | came · vino · vint · giunse |
| 5 | an | `an` A1 | to · a · à · a |
| 6 | mich | `ich` A1 | me · mí · moi · me |

Die Reihe gilt fuer **16,1** (woertlich gleich) und als Vorlage fuer 7,1 ·
13,3 · 13,8 · 18,1 · 18,5 · 24,4 · 29,30 · 32,6 · 32,26 · 33,19 · 33,23 ·
34,12 · 35,12 · 37,6 · 42,7 · 43,8.

**`ergehen an` ist kein Mehrwort** — `fixgloss.py show "ergehen an"` findet
nichts, und die Vorlagen glossieren Wort fuer Wort. Alle 20 Bestandsbelege der
Lesart *came · vino · vint · giunse* stammen aus derselben Formel.

### `spricht der HERR` — Vers fuer Vers nach LSG

Die zweite Buchformel, ueber zweihundert Stellen. Franzoesisch wechselt
zwischen *dit* und *parle*, und Jesaja hat das Vers fuer Vers nach der Ausgabe
entschieden (25 : 23). Jeremia macht es genauso: Kapitel 2 hat **parle** in
2,2 und 2,5 („Ainsi parle"), **dit** in den sechs uebrigen; Kapitel 1 und 3
haben durchgehend *dit*, weil LSG dort nichts anderes schreibt.

### Das Untreue-Wortfeld (Kap. 3) gilt fuer den ganzen ersten Buchteil

`Abtruenniger` C1 *renegade* (Substantiv) gegen `abtruennig` C1 *rebellious*
(Adjektiv) · `treulos` B2 · `untreu` B2 · `Untreue` C1 · `Hurerei` C1 ·
`Hure` C1 · `Ehebruch` C1 · `Scheidebrief` C1 (= Jes 50,1) · `entweihen` C1 ·
`zurueckkehren` B1.

**`abtruennig` und `treulos` stehen in 3,8 und 3,11 nebeneinander** und bleiben
in allen vier Sprachen getrennt. `treulos` und `untreu` tragen dieselbe Reihe,
stehen aber nirgends im selben Vers — nach der Kollisionsregel **nicht**
aufgeloest. **Die vier Ausgaben vertauschen die Zuordnung** (WEB
*backsliding*/*treacherous*, LSG *infidèle*/*perfide*); genommen ist der
Bestand.

### Der Quelltext hat einen mutmasslichen Setzfehler

**1,7 schreibt `aufträgt`** (3. Person) mit dem Subjekt `ich` — „und verkünden,
was ich dir aufträgt." 1,17 schreibt an derselben Stelle korrekt `auftrage`,
und alle vier Ausgaben haben die 1. Person. Kontextuell in der 1. Person
glossiert und als Befund am l1912mod gemeldet.

### Was `sweeplemma.py` in einem einzigen Kapitel fand

Sechs Bestands-Mehrwoerter fehlten in Kapitel 2: `nicht einmal` · `was nuetzt
es` (zweimal) · `auch wenn` · `zur rechten Zeit` · `Tag fuer Tag`. Alle sechs
sind mit 20 bis 39 Belegen im Bestand, und **keines haette `selfcheck`, `qa`
oder `konvention` gesehen.** Achte Bestaetigung seiner Pflichtstellung.

### Bestandsbefunde

* **`dich` traegt in Josua 10,8 das Lemma `sich`** — korpusweit steht `du`
  1527-mal, `sich` 15-mal, `dich` einmal. Die 15 Stellen sind ein Kandidat
  fuer eine korpusweite Angleichung.
* **`rings um` fehlt als Mehrwort in Josua 6,3 und 3Mo 16,18**, obwohl der
  Bestand die Wendung 18-mal fuehrt.
* **`Urteil sprechen` steht unter zwei Lemmata** — `Urteil sprechen` (AT) und
  `das Urteil sprechen` (NT, 3 Belege). Eine der beiden gehoert
  zusammengefuehrt.
* **`besser` laeuft unter zwei Lemmata** (53 Belege unter `gut`, 27 unter
  `besser`) bei gleicher Bedeutung.
* **`erschauern` und `erbeben` fallen korpusweit in es und fr zusammen.** In
  2,12 stehen beide in einem Vers; dort weicht `erbeben` aus. Keine
  korpusweite Aenderung.

### Und der Befund, der das ganze Buch betrifft

**RIV1927 hat rund 440 Woerter ohne Anfangsbuchstaben** — „nel paese di
eniamino", „re di iuda", „dice il ignore". Gemessen gegen die vier anderen
Ausgaben (32 · 22 · 25 · 30 Rauschtreffer) ist das vierzehnfach ueber dem
Grundrauschen. Einzelheiten und Stellenliste in `RIV_ANLAUTFEHLER.md`.
**Nicht repariert** — es waeren ueber vierhundert Aenderungen am Bibeltext
selbst. Fuer die Annotation gilt: sieht eine RIV-Schreibung um genau einen
fehlenden Anlaut falsch aus, an einer zweiten Belegstelle nachschlagen.

## 3. Paket 2 (Kap. 4 · 5 · 6) — der Feind aus dem Norden

92 Verse, 2242 Eintraege. Versatz +0 in allen vier Ausgaben und allen drei
Kapiteln. `paketcheck.py` Abschnitt A und C leer; von den 75 Zeilen in
Abschnitt B ist keine ein Befund — es sind Numerus, Tempus und echte
Bedeutungsunterschiede desselben Lemmas.

### `Sollte ich das nicht ahnden` — die zweite Buchdublette, fertig entschieden

5,9 und 5,29 sind **woertlich gleich** und lagen bei **einem** Agenten, anders
als 1,4 / 2,1 in Paket 1. Beide Verse tragen Feld fuer Feld dieselbe Reihe
(18 Eintraege, maschinell verglichen). Sie gilt unveraendert fuer **9,8** —
das ist Paket 3.

| pos | Form | Lemma · Level | en · es · fr · it |
|---|---|---|---|
| 0 | Sollte | `sollen` A2 | Should · Debería · Devrais-je · Dovrei |
| 4 | ahnden | `ahnden` C1 | punish · castigar · punir · punire |
| 10 | mich rächen | `sich rächen` B2 | take revenge · vengarme · me venger · vendicarmi |
| 13 | solchen | `solch` B2 | such · tal · tel · tale |
| 16 | rächen | `rächen` B2 | avenge · vengar · venger · vendicare |

**6,15 ist die Vorlage fuer 8,12** (ebenfalls Paket 3) und steht vollstaendig
in `anno-quellen/deu/l1912mod/24/ch6.json`. Die tragenden Felder:
`sich schämen` B2 *be ashamed · avergonzarse · avoir honte · vergognarsi* ·
`Gräueltat` C1 *atrocities · atrocidades · atrocités · atrocità* ·
`Scham` B2 *shame · vergüenza · honte · vergogna* ·
`erröten` C1 *blushing · ruborizarse · rougir · arrossire* ·
`Fallender` B2 *who fall · que caen · qui tombent · che cadono* ·
`heimsuchen` C1 *punish · castigue · punirai · punirò* ·
`stürzen` B2 *be cast down · ser derribados · être renversés · essere rovesciati*.

### `spricht der HERR` — LSG bleibt der Massstab, und sie schwankt

19 Stellen in den drei Kapiteln, **13 `dit` zu 6 `parle`**, jede einzeln nach
LSG entschieden — Kapitel 4: `parle` in 4,3 und 4,27; Kapitel 5: `parle` nur in
5,14; Kapitel 6: `parle` in 6,6 · 6,9 · 6,16 · 6,21 · 6,22, also die Mehrheit.
en/es/it stehen an allen 19 Stellen auf *says · dice · dice*. Damit setzt sich
fort, was Jesaja mit 25 : 23 gezeigt hat: **die Verteilung ist kein Merkmal des
Buches, sondern der Ausgabe** — Kapitel 6 kippt sie um.

### Das Kriegs-Wortfeld laeuft durch das ganze Buch

`Kriegsbanner` C1 *war banner · bandera de guerra · bannière de guerre ·
bandiera di guerra* · `Feldhüter` C1 *field watchmen · guardianes de un campo ·
gardiens d'un champ · guardie d'un campo* · `der Mut sinken` B2 *lose courage ·
perder el ánimo · perdre courage · perdere il coraggio* · `heranwehen` B2 ·
`belauern` C1 · `zerfleischen` C1 · `niedermachen` C1 *make an end · acabéis ·
détruisez · finite* · `Abendschatten` B2 · `fallen an` B2 *pass to* (6,12, die
Haeuser, die an andere fallen).

Das Hurerei-Feld aus Kapitel 3 waechst weiter: `Dirnenhaus` C1 · `brünstig` C1
*in heat · en celo · en chaleur · in calore* · `Hengst` B2 · `Liebhaber` B2 ·
`sich behängen` C1 · `Goldschmuck` C1 · `Schminke` C1 (alle 4,30 und 5,7-8) und
`die Treue brechen` B2 *broken faith · quebrantado la fidelidad · rompu la
fidélité · rotto la fedeltà* (5,11).

Das Schmelzofenbild aus 6,27-30 steht zum ersten Mal: `Prüfer` B2 *tester* und
`Prober` C1 *assayer* im **selben Vers** — beide bleiben getrennt, weil die vier
Ausgaben sie trennen; dazu `Blasebalg` C1.

36 Lemmata des Pakets sind im Bestand neu, und **keines steht in zwei Kapiteln
zugleich** — deshalb ist Abschnitt A von `paketcheck.py` leer, nicht weil nichts
zu vergleichen war.

### Zwei Glossenkollisionen, beide bewusst stehen gelassen

* **4,22 `töricht` / `unverständige`** — beide *foolish*, aber **nur en**.
  WEB selbst schreibt „my people are foolish … They are foolish children";
  es, fr und it trennen (*necio/ignorantes* · *fou/insensés* ·
  *stolto/insensati*), und die Annotation trennt dort mit.
* **5,19 `Fremden` / `fremden`** — beide *étrangers*, und **nur fr**. LSG
  wiederholt das Wort selbst („des dieux étrangers … des étrangers"), genau wie
  der deutsche Text.

### `Ranke` steht zweimal und traegt zwei verschiedene Reihen — richtig so

5,10 hat *boughs · ramas · rameaux · tralci*, 6,9 *shoots · brotes · rameaux ·
rami*. Beide Reihen fuehrt der Bestand unter demselben Lemma `Ranke` C1 (drei
Belege fuer die zweite, einer — Ps 80,11 — fuer die erste), und beide Agenten
haben die genommen, die **ihre** Ausgaben stuetzen: in 5,10 schreibt RV *ramas*
und RIV *tralci*, in 6,9 RV *sarmientos*. Der Fall sieht in `paketcheck.py`
Abschnitt B wie eine Abweichung aus und ist keine.

### Drei Fehlalarme der Mehrwort-Sucher, alle derselben Bauart

`sweep.py` meldet 6,25 `geht auf` („geht nicht auf die Straße"),
`sweeplemma.py` 4,6 `bringen her` („Unheil von Norden her") und zweimal
`setzen ein` (5,22 „eine Grenze … gesetzt habe", 6,1 „setzt ein Zeichen"). In
allen vier Faellen gehoert das vermeintliche Partikel zum Nachbarn: `auf die
Straße`, `von Norden her`, `eine Grenze`, `ein Zeichen`. **Der Verdacht faellt
immer dort an, wo ein Artikel oder eine Praeposition wie ein Verbzusatz
aussieht.**

### Ein Homograph, den der Build meldet

`rechten` traegt zwei Lemmata: `rechten` C1 *reason · razonar* (2,9 und 2,29,
das Verb) und `recht` B1 *right · debido* (5,24 „zur rechten Zeit"). Der
Build-Hinweis „1 Wortform mit verschiedenen Leveln" ist genau das und kein
Befund — dieselbe Bauform wie `Spross`/`spross`.


## 4. Paket 3 (Kap. 7 · 8 · 9) — die Verszaehlung und die zweite Botenformel

82 Verse, 2141 Eintraege. Das Paket mit der **einzigen Verszaehlungsfalle des
Buches** und mit vier fertigen Dubletten aus Paket 2.

### Die Verszaehlung: `ausgaben.py` irrt, und es sagt das selbst

Fuer Kapitel 8 meldet das Werkzeug **Versatz −1** und schreibt daneben, dass
+0 besser liegt (Abstand 0.14 gegen 0.32 in allen vier Ausgaben). Die Warnung
hat recht:

    de 8,1-22  = Ausgaben 8,1-22       (+0)
    de 8,23    = Ausgaben 9,1          (in Kapitel 8 gibt es dort nichts)
    de 9,n     = Ausgaben 9,n+1        (+1, alle vier)

Die Rohausgabe des Werkzeugs ist **um einen Vers verschoben und liest sich
plausibel** — genau der Fehler, gegen den `ausgaben.py` gebaut wurde, hier vom
Werkzeug selbst erzeugt. Fuer Kapitel 8 ist die Datei deshalb **von Hand
gebaut** worden (1-22 aus Kapitel 8 der Ausgabe, 23 aus deren 9,1) und die
Rohfassung im Prompt ausdruecklich verboten worden. Beide Agenten haben die
Ausrichtung am Vers bestaetigt.

### `Starrsinn` — der zweite `wackeln`-Fall, und `paketcheck.py` hat ihn gefunden

7,24 und 9,13 tragen dieselbe Buchformel (`dem Starrsinn ihres Herzens
folgten`), das Lemma ist im Bestand **unbelegt**, und die beiden Agenten haben
es verschieden gepraegt:

    7,24   stubbornness · obstinación · obstination · ostinazione
    9,13   stubbornness · terquedad   · obstination · caparbietà

`selfcheck`, `qa`, `konvention`, `sweep`, `sweeplemma`, `glosskollision` und
`levelcheck` laufen ueber beide Kapitel ohne Befund — es gibt keine Zeile im
Bestand, gegen die zu pruefen waere. **Abschnitt A von `paketcheck.py` hat das
Paar gemeldet.** Entschieden ist es nicht ueber die Ausgaben (die schwanken:
*dureza*/*terquedad*, *penchants*/*caparbietà*), sondern ueber den Bestand:
`Halsstarrigkeit` C1 steht in 5Mo 31,27 mit **genau der Reihe von 7,24**
(*stubbornness · obstinación · obstination · ostinazione*), und `starrsinnig`
C1 traegt *stubborn · obstinado · obstiné · ostinato*. 9,13 ist angeglichen.
Die Formel kommt in 11,8 · 13,10 · 16,12 · 23,17 wieder — **und nicht in
18,12**, wie hier zunaechst stand: der Quelltext schreibt dort `was ihm sein
böses Herz eingibt`, obwohl alle vier Ausgaben *stubbornness · terquedad ·
penchants · caparbietà* lesen. Der Agent von Kapitel 18 hat es am Vers
widerlegt. **17,23 traegt das Adjektiv `starrsinnig` C1, nicht das
Substantiv** — zwei Lemmata.

### `Geschlecht` in 8,3 — die Lexikonfalle mit umgekehrtem Vorzeichen

Der Bestand fuehrt 198 Belege *lineage · linaje · lignée · stirpe* und nur
**sieben** *generation · generación · génération · generazione*. Die 198 sind
die Sippenlisten von 4. Mose; die sieben sind „dieses Geschlecht" — darunter
**Jeremia 2,31**, also dieses Buch. 8,3 (`dieses boesen Geschlechts`) gehoert
zur zweiten Gruppe, und RV schreibt dort selbst *generación*. Der Agent hatte
die Korpusmehrheit genommen; angeglichen an 7,29, das alle vier Ausgaben
einstimmig als *generation* haben. **Die Bindung gilt fuer dieselbe Bedeutung,
nicht fuer dieselbe Buchstabenfolge.**

### Die vier fertigen Dubletten — maschinell nachgerechnet

| Vers | Vorlage | Ergebnis |
|---|---|---|
| 8,12 | 6,15 | alle 38 Eintraege identisch |
| 8,11 | 6,14 | pos 0-3 identisch, pos 4-5 neu (`der Tochter`), ab pos 6 identisch mit Versatz +2 |
| 8,10 | 6,13 | erster Satz neu, ab pos 11 identisch mit Versatz +11 |
| 9,8 | 5,9 = 5,29 | alle 18 Eintraege identisch, einschliesslich `sich rächen` `parts` |

### `Das ist das Wort, das vom HERRN an Jeremia erging` (7,1)

Die zweite Buchformel, Vorlage fuer **siebzehn** spaetere Stellen (11,1 · 13,8
· 16,1 · 18,1 · 18,5 · 24,4 · 29,30 · 30,1 · 32,6 · 32,26 · 33,19 · 33,23 ·
34,12 · 35,12 · 37,6 · 42,7 · 43,8; 18,1 woertlich gleich).

| pos | Form | Lemma · Level | en · es · fr · it |
|---|---|---|---|
| 0 | Das | `der` A1 | This · Esta · Ceci · Questa |
| 1 | ist | `sein` A1 | is · es · est · è |
| 2 | das | `der` A1 | the · la · la · la |
| 3 | Wort | `Wort` A1 | word · palabra · parole · parola |
| 4 | das | `der` A1 | that · que · qui · che |
| 5 | vom | `vom` A1 | from the · del · de l' · dal |
| 6 | HERRN | `HERR` A1 | LORD · SEÑOR · ÉTERNEL · SIGNORE |
| 7 | an | `an` A1 | to · a · à · a |
| 8 | Jeremia | `Jeremia` A1 | Jeremiah · Jeremías · Jérémie · Geremia |
| 9 | erging | `ergehen` C1 | came · vino · vint · giunse |

`vom` ist die Bestandsmehrheit vor `HERRN` (45 von 56). Die vier Kernfelder
sind dieselben wie in 1,4 / 2,1 — die beiden Formeln des Buches beruehren
einander an `Wort`, `HERR`, `an` und `ergehen`.

**`das nach meinem Namen genannt ist`** steht viermal in Kapitel 7 (7,10 ·
7,11 · 7,14 · 7,30) und ist Vorlage fuer 32,34 und 34,15: `nach` A1 *by · por ·
par · **con*** · `Name` A1 · `nennen` A2 *called · llamado · appelé ·
chiamato*. Das italienische *con* statt *per* ist eine Kollisionsaufloesung —
mit *per* fiel `nach` in 7,10 mit `um` und in 7,11 mit `für` zusammen; die drei
Ausgaben ausser WEB formulieren die Wendung ohnehin passiv um und liefern gar
keine Praeposition.

### `spricht der HERR`: die LSG-Verteilung schwankt weiter

Kapitel 7 steht 5 : 3 fuer *dit*, Kapitel 8 5 : 1, Kapitel 9 **5 : 5**. Ueber
die sechs Kapitel der Pakete 2 und 3 sind es 28 *dit* zu 15 *parle*. en, es und
it stehen an allen 43 Stellen auf *says · dice · dice*.

### Vier Befunde im Bestand, einer davon eine Korrektur wert

* **`Griffel` C1 traegt eine Meissel-Reihe, die an einer ihrer zwei
  Belegstellen falsch ist.** Der Bestand hat *stylus · cincel · burin ·
  scalpello* aus Hiob 19,24, wo sie richtig ist (WEB „iron pen", RIV
  „scalpello di ferro"). **Ps 45,2 ist aber der Schreibgriffel**, und dort
  schreiben alle vier Ausgaben *pen · pluma · plume · penna*; die Meisselreihe
  ist trotzdem mituebernommen worden. In 8,8 (`der lügnerische Griffel der
  Schriftgelehrten`) schreiben die Ausgaben ebenfalls *pen*, und *cincel* waere
  am Vers falsch. Genommen ist *pen · pluma · plume · penna*; **Ps 45,2 ist ein
  Kandidat fuer eine korpusweite Korrektur.**
* **`Salbe` und `Balsam` tragen jetzt dieselbe Reihe.** Der Bestand fuehrt
  `Salbe` C1 viermal als *ointments · ungüentos · onguents · unguenti*, alle
  vier Koerperoel (Hohelied, Lukas) — 8,22 meint den Wundbalsam, alle vier
  Ausgaben schreiben ihn, genommen ist *balm · bálsamo · baume · balsamo*. Der
  Bestand hat dafuer aber **ein eigenes Lemma `Balsam` C1 mit genau dieser
  Reihe**. Beide stehen nirgends im selben Vers, also nicht aufgeloest.
* **`Lid` ist die dritte Bestaetigung der Form-gegen-Lemma-Falle.** `Lider`
  (9,17) stand als unbelegt im Extrakt; `belegt.py` zeigt das Lemma `Lid` C1
  mit zwei Belegen (Ps 132,4 · Spr 6,4), dort nur als `Lidern` flektiert.
* **`herbeiholen` und `herholen`** sind zwei Lemmata fuer dieselbe Sache (je
  ein Beleg) — Kandidat fuer eine Zusammenfuehrung. Ebenso fallen `Entsetzen`
  C1 und `Schrecken` B2 in en und es zusammen, `Einwohner` und `Bewohner` in
  allen vier; alle drei Paare stehen nie im selben Vers, also nur gemeldet.

### `hören auf` fehlte viermal, und zwei davon hat kein Werkzeug gefunden

`sweep.py` meldete 7,23 und 7,28. Der Agent hat am Vers nachgezaehlt und das
Bestands-Mehrwort (185 Belege, B1) auch in **7,26 und 7,27** ergaenzt, die
kein Lauf gemeldet hatte. Die x-te Bestaetigung, dass die Mehrwort-Sucher
Pflicht sind **und** nicht ausreichen.

`sweeplemma.py` meldet dafuer drei Fehlalarme derselben Bauart wie in Paket 2:
7,1 `vom an` (zwei getrennte Praepositionen), 7,30 `stellen nach` (das `nach`
gehoert zu `nach meinem Namen`), 9,9 `Klagelied anstimmen`. Der letzte ist der
interessante: der Bestand fuehrt die Wendung nur im **Plural**
(`Klagelieder anstimmen`, Mt 11,17 · Lk 7,32, *sung dirges*) als Kinderreim,
waehrend 7,29 und 9,9 den Singular haben und Wort fuer Wort glossiert bleiben —
in beiden Kapiteln gleich.

### Befunde in den Ausgaben

* **Vier RIV-Anlautfehler in einem Paket**: 7,23 „amminate" (camminate), 7,32
  „di innom" (Hinnom), 8,9 „he sapienza" (Che), 8,16 „oiché vengono" (Poiché).
  Das Muster aus `RIV_ANLAUTFEHLER.md`, nicht repariert.
* **RIV setzt die Satzgrenze zwischen 7,10 und 7,11 anders.** Der
  Raeuberhoehlen-Satz steht dort am Ende von 7,10, und 7,11 beginnt mitten im
  Satz. Kein Versatz, eine Klauselverschiebung — wer fuer 7,11 die italienische
  Vorlage sucht, muss 7,10 mitlesen.
* **RV vertauscht in 8,7 Kranich und Schwalbe**; RIV laesst in 8,11 `der
  Tochter` aus und hat in 8,13 einen anderen Schluss als die drei anderen. In
  allen Faellen ist nach dem deutschen Text glossiert.

### Neue Lemmata des Pakets (14)

`Himmelskönigin` C1 *queen of the sky · reina del cielo · reine du ciel ·
regina del cielo* (WEB schreibt *sky*, nicht *heaven*) · `Würgetal` C1 *Valley
of Slaughter · Valle de la Matanza · vallée du carnage · valle del massacro* ·
`Starrsinn` C1 · `morden` B2 · `verstummen lassen` C1 · `verbissen` C1
*doggedly · con obstinación · avec acharnement · con accanimento* ·
`Tränenbrunnen` C1 *spring of tears · fuente de lágrimas · source de larmes ·
fonte di lacrime* · `Wiehern` C1 (Substantiv neben dem vorhandenen Verb, nach
dem Muster `Schnauben`) · `wohin immer` B1 (Mehrwort) · `Klageweib` C1
*mourning women · plañideras · pleureuses · piagnone* · `Trauerlied` C1 ·
`Giftwasser` B2 · `trainieren` B1 · `stutzen` B2.


## 5. Paket 4 (Kap. 10 · 11 · 12) — der Goetzenbauer und der grosse Vorlagenblock

65 Verse, 1711 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer; von 45 Zeilen in Abschnitt B ist keine ein Befund. `glosskollision.py`
meldet in **allen drei Kapiteln null inhaltliche Paare** — das erste Paket des
Buches, in dem das gelingt.

### 10,12-16 → 51,15-19: der groesste Vorlagenblock des Buches

Vier Verse sind woertlich gleich (10,13-16 = 51,16-19), der fuenfte fast:
**51,15 ist 10,12 ohne das `aber`** — pos 0 gleich, pos 1 entfaellt, ab pos 2
identisch mit Versatz −1. Die Reihen stehen vollstaendig in
`anno-quellen/deu/l1912mod/24/ch10.json`. Paket 17 schlaegt dort nach und
entscheidet die Schoepfungshymne nicht noch einmal.

Zwei Entscheidungen tragen den Block: `Kraft` A2 traegt die **AT-Bindung**
*strength · fuerza · force · forza* und nicht die Ausgabenlesart *power* —
sonst fiele es mit `Macht` B1 (10,6 · 10,23) zusammen. Und `Abrechnung` B2
(10,15) traegt die einzige Bestandsreihe *accounting · cuentas · comptes ·
conti*, obwohl die Ausgaben dort *visitation · castigo · châtiment · castigo*
schreiben. **Wenn der Bestand hier je angeglichen wird, muessen 10,15 und
51,18 zusammen wandern.**

### Was `parallelen.py` nicht gemeldet hat

Die zweite Haelfte von **10,13 steht fertig in Psalmen 135,7** („Er lässt
Wolken aufsteigen vom Ende der Erde, macht Blitze zum Regen, lässt den Wind aus
seinen Vorratskammern hervorkommen"). Der Agent hat sie selbst gefunden und pos
8-29 Feld fuer Feld uebernommen, einschliesslich der beiden Kausativ-Mehrwoerter
`aufsteigen lassen` B2 und `hervorkommen lassen` B2. Abgewichen ist der
Quelltext nur in `für den Regen` (Ps: `zum Regen`) und `Kammern` (Ps:
`Vorratskammern`, ein eigenes Lemma). **Der Werkzeugbefund ist eine untere
Schranke, keine Liste.**

### Der Goetzenbauer stand schon in Jesaja

10,3-5 · 10,9 · 10,14 sind dieselbe Szene wie Jes 40,19-20 · 41,7 · 46,6-7, und
der Bestand war dort fertig. `wackeln` B1 — das Wort, an dem in Jesaja zwei
Agenten auseinandergelaufen sind und das `paketcheck.py` ueberhaupt erst
hervorgebracht hat — steht in 10,4 mit der inzwischen festen Reihe; genommen
ist die Form von Jes 41,7 (Zwecksatz), nicht die von 40,20 (Indikativ). Ebenso
`Goldschmied` B2 *goldsmith · platero · orfèvre · orefice* (drei der sechs
Belege sind genau diese Szene, und RV schreibt hier gegen die Bindung
*fundidor*) und `Gurkenfeld` C1 aus Jes 1,8.

**Die `Vogelscheuche` in 10,5 hat nur der deutsche Text.** WEB liest *a palm
tree, of turned work*, RV *un poste de palmera*, LSG *une colonne massive*, RIV
*pali*; das Gurkenfeld hat allein RIV. `Vogelscheuche` C1 *scarecrow ·
espantapájaros · épouvantail · spaventapasseri* ist deshalb frei gepraegt —
der seltene Fall, in dem keine Ausgabe hilft.

### `Volk` im Plural: buchweit vereinheitlicht

Der Bestand des Buches stand **16 : 2** auf *peoples · pueblos · peuples ·
popoli*, obwohl die vier Ausgaben an vielen dieser Stellen einstimmig
*nations* schreiben (1,5 · 4,7 · 6,18 · 10,2 · 10,7 · 10,10 · 10,25). Die
beiden Ausreisser standen in **9,15 und 9,25**; sie sind auf die Buchreihe
angeglichen. Kapitel 10 hat `Völker` siebenmal und ist durchgehend auf
*peoples* gesetzt — gestuetzt von den beiden Parallelversen Ps 96,5 (→ 10,3)
und Ps 79,6 (→ 10,25), die beide *peoples* tragen.

### Zwei Homographen, die der Build meldet, und beide sind richtig

12,1 hat **`rechten` C1 (Verb) und `Recht` B1 (Substantiv) im selben Vers**,
dazu `recht behalten` B2 — drei Glieder derselben Familie, alle drei getrennt
gefuehrt. 11,15 hat **`meinen` B1** („und meinen, das heilige Fleisch nehme
ihnen die Schuld ab") gegen das Possessivum `mein` A1. Der Build-Hinweis
„Wortformen mit verschiedenen Leveln (verschiedene Lemmata)" nennt beide; das
ist kein Befund, sondern die Bauform, die schon `Spross`/`spross` hatte.

**Ein Prompt-Hinweis dieser Vorbereitung war falsch:** die Vorgabetabelle nannte
`rechten` italienisch *ragionare*. Der Bestand hat an allen vier Belegstellen
(Hiob 23,7 · Ps 103,9 · Jer 2,9 · Jer 2,29) ***discutere***. Der Agent hat es am
Bestand widerlegt — die uebliche Quote, die uebliche Ursache.

### Die Form-gegen-Lemma-Falle, viertes und fuenftes Mal

* **`Nichtse` (10,8)** stand als unbelegt im Extrakt. Der Bestand fuehrt das
  Lemma **`Nichts` B2** (*nothingness · nada · néant · nulla*, 3 Belege) —
  vergeben ist dessen Plural, kein neues Lemma.
* **`Hämmern` (10,4) ist kein Verb.** Der Extrakt verweist auf `hämmern` B2
  (Jes 44,12); im Vers steht der Dativ Plural von `Hammer`, und alle vier
  Ausgaben schreiben das Substantiv. Vergeben ist `Hammer` B2 *hammers ·
  martillos · marteaux · martelli* — die Reihe von Jes 41,7, derselben Szene.
* In Kapitel 12 fuehrte `hints.py` fuenf weitere Formen als unbelegt
  (`antasten`, `vertrocknen`, `Sterblicher`, `Reiße`, `Nah`), die saemtlich als
  **Lemma** im Bestand stehen.

### `Treuloser` ist nicht `treulos`

12,1 hat das substantivierte `alle Treulosen`. Der Bestand fuehrt dafuer
`Treuloser` C1 *faithless · desleales · déloyaux · sleali* (7 Belege); das
Adjektiv `treulos` B2 aus Kapitel 3 ist ein anderes Lemma. Dieselbe Bauform wie
`Abtrünniger`/`abtrünnig` im selben Wortfeld.

### Befunde im Bestand

* **`Beil`: die einzige Belegstelle traegt die falsche Groesse.** Der Bestand
  hat *hatchet · hachuela · hachette · accetta* aus Ps 74,6. In 10,3 wird damit
  im Wald ein Baum gefaellt, und alle vier Ausgaben schreiben *ax · hacha ·
  hache · ascia*. **Ein Beleg ist keine Bindung** (`BINDUNGEN_AT` setzt die
  Schwelle bei acht); genommen ist die Ausgabenreihe. Ps 74,6 bleibt sachlich
  richtig — es sind zwei Werkzeuge.
* **`ausgießen` C1 traegt italienisch zwei Reihen bei gleicher Bedeutung**:
  *Effondi* (Jer 6,11) gegen *Spandi* (Ps 79,6). 10,25 ist die Ps-79,6-Dublette
  und nimmt *Spandi*. Kandidat fuer eine korpusweite Angleichung.
* **`zerreißen` B2 hat nur die Kleider-Lesart** (34 Belege *rasgar · déchirer ·
  stracciare*). In 10,20 reissen **Zeltstricke**, und alle vier Ausgaben
  schreiben *broken · rotas · rompus · rotti*. So vergeben, Lemma unveraendert.
* **`Vergeltung` C1 hat drei Reihen** (*retribution · venganza · vengeance ·
  vendetta* 10× und zwei Varianten zu je zwei Belegen), **`Schlachtung` C1 und
  `Schlachten` B2** sind dieselbe Sache mit identischer Reihe und
  verschiedenem Level, **`herausreißen` B2 und `ausreißen` B2** ebenso. Drei
  Kandidaten fuer eine Zusammenfuehrung, keiner angefasst.

### Befunde in den Ausgaben

* **Sechs RIV-Anlautfehler in einem Paket** — 10,16 „e sraele" · 10,20 „non
  ono" · 10,25 „oiché" · 12,6 „on li credere" · 12,8 „erciò". Dazu ein
  **neuer Bautyp in 11,19: „ffinché" statt *affinché***, also ein *doppelter*
  statt eines fehlenden Anlauts.
* **LSG 12,9 hat ein Tier mehr** als alle anderen („un oiseau de proie, **une
  hyène**"), LSG und RIV paraphrasieren 12,5b (`Dickicht am Jordan`), und
  **alle vier lesen 12,4a als „trauern"**, wo der l1912mod `vertrocknen`
  schreibt. Jedes Mal ist nach dem deutschen Text glossiert.
* **RV1909mod siezt in Kapitel 10 durchgehend** (*ustedes*: „Oigan", „No
  aprendan"), waehrend der Bestand im ganzen Buch *vosotros* fuehrt. Gefolgt
  ist dem Bestand.

### `spricht der HERR`: die Zwischenbilanz nach zwoelf Kapiteln

**44 `dit` zu 27 `parle`**, jede Stelle einzeln nach LSG. Die Verteilung
schwankt kapitelweise vollstaendig durch: Kapitel 3 hat achtmal *dit* und kein
*parle*, **Kapitel 11 viermal *parle* und kein *dit***, Kapitel 9 steht 5 : 6.
Dazu ein Beleg, der keine Botenformel ist: **10,1** („das der HERR zu euch
spricht") traegt *speaks · habla · **adresse** · rivolge*.

### Neue Lemmata des Pakets (14)

`Vogelscheuche` C1 · `Kunsthandwerker` C1 *skilled craftsmen · artesanos
expertos · habiles artisans · abili artefici* · `aufspannen` B2 · `gehämmert`
B2 · `Ufas` A1 *Uphaz · Ufaz · Uphaz · Ufaz* · `Schandaltar` C1 *shameful
altars · altares vergonzosos · autels de honte · altari dell'infamia* ·
`verhungern` B2 · `zu suchen haben` B2 (Mehrwort) · `so sei es` B1 (Mehrwort,
alle vier Ausgaben schreiben *Amen*) · `Fußgänger` B2 · `mithalten` B2 ·
`anbrüllen` B2 · `gesprenkelt` C1 · `Zornglut` C1 *fierce anger · ardiente ira ·
colère ardente · ardente ira* — **die `Zornglut`-Formel kehrt in 25,37 wieder.**


## 6. Paket 5 (Kap. 13 · 14 · 15) — die Schwert-Hunger-Pest-Formel

70 Verse, 1894 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer, 52 Zeilen in B ohne Befund.

### Die Formel, die das halbe Buch traegt

Kapitel 14 hat sie fuenfmal (14,12 · 14,13 · 14,15 zweimal · 14,16 · 14,18),
maschinell nachgerechnet **Feld fuer Feld identisch**:

| Wort | Level | en · es · fr · it |
|---|---|---|
| `Schwert` | B1 | sword · espada · épée · spada |
| `Hunger` | A2 | hunger · hambre · faim · fame |
| `Pest` | B2 | pestilence · pestilencia · peste · pestilenza |

Dazu einheitlich `durch` A2 *by · por · par · per* · `umkommen` B2 *perish ·
perecer · périr · perire* · `vernichten` B2 *destroy · destruir · détruire ·
distruggere*. **15,2 hat die erweiterte Fassung** mit `Tod` A2 *death · muerte ·
mort · morte* und `Gefangenschaft` **C1** *captivity · cautividad · captivité ·
cattività* (der Auftrag hatte B2 behauptet, der Bestand hat 33 Belege unter C1).
Der Rahmen: `wer` A1 *whoever · el que · celui qui · chi* · `bestimmen` B2
*destined · destinado · destiné · destinato* — `bestimmt ist` ist eine
Passivklammer, **kein Mehrwort**. Gilt fuer 21,7 · 21,9 · 24,10 · 27,8 ·
29,17 · 32,24 · 43,11.

### Die Botenformel in dritter Wortstellung

Das Buch hat jetzt drei Fassungen mit denselben Feldern:

| Stelle | Wortlaut |
|---|---|
| 1,4 = 2,1 | `Das Wort des HERRN erging an mich` |
| 7,1 = 11,1 | `Das/Dies ist das Wort, das vom HERRN an Jeremia erging` |
| **13,8** | `Da erging das Wort des HERRN an mich` |

13,8 ist **woertlich gleich mit 18,5 und 24,4**; 13,3 ist dieselbe Reihe plus
`zum zweiten Mal` A2 *for the second time · por segunda vez · pour la deuxième
fois · per la seconda volta* (aus Jer 1,13) und Vorlage fuer neun weitere
Stellen. Beide stehen vollstaendig in `ch13.json`; pos 0-5 sind maschinell als
identisch nachgerechnet. `Da` traegt *Then · Entonces · Alors · Allora*.

**14,1 ist trotz gleichem Anfang keine `ergehen`-Formel** — dort steht `sagte`.
Der Agent hat das am Quelltext bestaetigt und die 7,1-Reihe nicht angewandt.

### Zwei Dubletten, die maschinell nachgerechnet sind

* **14,19 gegen 8,15**: alle **14 gemeinsamen Felder identisch** (8,15 pos 0-7 →
  14,19 pos 19-26, 8,15 pos 12-17 → 14,19 pos 30-35). Die Mitte ist **nicht**
  abgeschrieben: 14,19 hat `wir hofften auf Heilung` statt `auf eine Zeit der
  Heilung`, und traegt damit den `hoffen auf`-Mehrworteintrag **zweimal**.
* **15,20 gegen 1,19**: **18 von 20 gemeinsamen Positionen identisch**, genau
  die zwei erwarteten Abweichungen — pos 11 `sie` (satzinitial gegen
  satzintern, nur Grossschreibung) und pos 19 **`überwältigen` C1 *overpower ·
  vencer · vaincre · vincere*** statt `besiegen` B2. Die Bestandsreihe von
  `überwältigen` (1Mo 32,26) deckt sich Wort fuer Wort mit RV/LSG/RIV.

### 15,13-14 → 17,3-4: die naechste Vorlage steht bereit

Beide Verse vollstaendig in `ch15.json`. Tragend: `preisgeben` C1 *give over ·
entrego · livre · consegno* (Mehrwort mit `parts`, Einzel-`preis` C1 *over · a
merced · en proie · in preda*) · `Reichtum` B2 · `Schatz` B1 · `Bezahlung` B1 ·
`Gebiet` B1 *region · región · région · regione* (101 Belege, gegen die
Ausgaben durchgehalten) · `ausliefern` C1 · `entfachen` B2.

### Ein Fehler, den kein Pflichtlauf sehen kann: dasselbe Wort zweimal im Kapitel

**`Gürtel` stand in 13,1 spanisch als *cinto*, in den sieben uebrigen
Vorkommen derselben Szene als *cinturón*.** `glosskollision.py` sieht nur
innerhalb eines Verses, `paketcheck.py` nur zwischen Kapiteln — eine
Uneinheitlichkeit **innerhalb** eines Kapitels faellt durch beide Netze und ist
beim Einsammeln von Hand gefunden worden. Vereinheitlicht auf *cinturón*: das
schreiben alle vier Ausgaben, und die 24 *cinto*-Belege des Bestands sind der
gewebte Priestergürtel aus 2. Mose 28, ein anderes Sachfeld. **Beim Einsammeln
jedes Pakets kuenftig ein Lemma, das im Kapitel oft vorkommt, gegen sich selbst
pruefen.**

### Die Form-gegen-Lemma-Falle: sechs weitere Faelle in einem Paket

Von den als „unbelegt" gemeldeten Formen waren **die meisten laengst als Lemma
da**: `Felsspalte` C1 (6 Belege, nur im Plural flektiert — 13,4 hat den
Singular und bekommt *rock crevice · hendidura de la roca · fente d'un rocher ·
fenditura d'una roccia*), `Königinmutter` B2 (1Kön 15,13; der Quelltext
schreibt den Bindestrich, der Bestand nicht), `Junges` B2 (24 Belege),
`wertvoll` B1, `wahrlich` B2, `unterscheiden` B2, dazu in Kapitel 14 acht von
elf gemeldeten Formen. **Wirklich neu waren nur fuenf Woerter im ganzen
Paket.**

### Vier Woerter, bei denen der Vers gegen die Korpusmehrheit entschieden hat

* **`Retter` (14,8)**: `BINDUNGEN_AT` bindet auf *deliverer · libertador ·
  libérateur · liberatore* — das sind die Richter-Belege, der menschliche
  Befreier. 14,8 meint Gott, alle vier Ausgaben schreiben *Savior*, und der
  Bestand hat diese Reihe 17-mal (Jes 49,26). **Die Bindung gilt fuer dieselbe
  Bedeutung, nicht fuer dieselbe Buchstabenfolge.**
* **`heißen` (13,6)** heisst hier „befehlen"; der Bestand hat 96× *was called*
  und keine Befehls-Lesart, alle vier Ausgaben schreiben *commanded*.
* **`sitzen` (13,11)** ist das Sitzen eines Kleidungsstuecks → *fits · se
  ajusta · s'ajuste · aderisce*; drei Verse spaeter (13,13, Thron) traegt
  dasselbe Lemma die gewoehnliche Lesart.
* **`Verlangen` (13,27)**: alle vier Ausgaben lesen dort *neighing*, der
  l1912mod schreibt `Verlangen`. Nach dem deutschen Text glossiert — das in
  Paket 3 gepraegte `Wiehern` C1 kommt hier **nicht** vor.

### Befunde im Bestand

* **`Gürtel` B1 hat zwei spanische Reihen** (*cinto* 24 gegen *cinturón* 4) bei
  gleicher Bedeutung — s. o., Kandidat fuer eine korpusweite Angleichung.
* **`ach` traegt im Buch zwei Reihen**: 1,6 *Oh · Ay · Ah · Ah* (Korpusmehrheit,
  25 Belege) gegen 4,10 *Ah · Ay · Ah · Ahi*. 14,7 und 14,13 folgen 4,10, weil
  14,13 dessen woertlicher Zwilling ist. Kandidat fuer eine Angleichung.
* **`Verfolger` C1 steht 14 : 2 auf *pursuers***, die zwei *persecutor*-Belege
  sind NT. In 15,15 schreiben **alle vier Ausgaben** die Verfolgungs-Lesart;
  genommen ist die AT-Bindung, weil Ps 7,2 / 31,16 / 35,3 dieselbe Sache
  meinen. Zur Pruefung gemeldet.
* **`Gefallen haben` und `Gefallen haben an`** sind zwei Lemmata fuer dieselbe
  Wendung, **`kein mehr` laeuft unter vier Lemmaschreibungen**, und
  **`Bewohner`/`Einwohner`**, **`Erbarmen`/`Mitleid`**, **`Scham`/`Schande`**,
  **`hadern`/`streiten`** fallen paarweise zusammen. Die vier letzten stehen je
  in **einem** Vers zusammen (13,13 · 13,14 · 15,9 · 15,10) und sind dort ueber
  eine zweite Bestandslesart aufgeloest — nie korpusweit.

### Befunde in den Ausgaben

* Vier RIV-Anlautfehler (13,9 · 15,2 · 15,4 und in 14,4 ein fehlender Akzent
  „e" statt „è"). **Kapitel 14 ist das erste Kapitel des Buches ohne einen
  echten Anlautfehler.**
* **RIV traegt in 15,21 den Versmarker „(15:20)"** — es zaehlt 21 als
  Fortsetzung von 20. Der Text ist vollstaendig und am richtigen Platz, **kein
  Versatz**, nur ein Zaehlartefakt des Imports.
* **RV1909mod siezt auch in 13,15-17** (*Escuchen*, *ustedes esperarán*),
  waehrend der Bestand im ganzen Buch *vosotros* fuehrt — dieselbe Beobachtung
  wie fuer Kapitel 10. Gefolgt ist dem Bestand.
* LSG liest in 14,2 `Tore` als *villes*, in 14,6 `Schakale` als *serpents*, und
  steht in 13,20 im Singular, wo alle anderen den Plural haben.

### `spricht der HERR`: Stand nach 15 Kapiteln

**54 `dit` zu 37 `parle`**. Kapitel 13 steht 3 : 4, Kapitel 15 4 : 2, Kapitel 14
1 : 1 — die Schwankung der Ausgabe setzt sich fort.

### Neue Lemmata des Pakets (11)

`verrottet` C1 *rotted · podrido · pourrie · marcita* (keine Ausgabe trifft das
deutsche Wort ausser RV) · `Wüstenwind` C1 · `hochheben` B1 · `Kuschit` B2
(Reihe vom Bestandslemma `Kuschiter`) · `umherschweifen` C1 *to wander · andar
errantes · courir çà et là · andar vagando* (bewusst gegen `umherirren` C1
abgesetzt) · `umherliegen` C1 · `Geschwächter` B2 · `fürs` A1 (nach dem Muster
`zum`/`vom`/`im`/`zur`/`am`) · dazu die Mehrwoerter `zum zweiten Mal` A2 und
`hereinbrechen lassen` B2.


## 7. Paket 6 (Kap. 16 · 17 · 18) — das Botenformel-Paket

71 Verse, 1903 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer, 44 Zeilen in B ohne Befund. `sweep`, `sweeplemma`, `konvention`,
`levelcheck` und `qa` melden ueber alle drei Kapitel **nichts** ausser zwei
Fehlalarmen; `glosskollision.py` findet ein einziges inhaltliches Paar
(16,10 `Sünde`/`gesündigt` — Verb und Stammsubstantiv, die benannte Ausnahme).

### Drei woertliche Uebernahmen, alle drei maschinell nachgerechnet

| Vers | Vorlage | Ergebnis |
|---|---|---|
| 16,1 | 1,4 = 2,1 | **7 von 7 Feldern identisch** |
| 18,1 | 7,1 | **10 von 10 Feldern identisch** |
| 18,5 | 13,8 | **8 von 8 Feldern identisch** |

Damit sind rund vierzig spaetere Stellen des Buches abgedeckt. **18,7 und 18,9**
sind ausserdem untereinander in **allen elf gemeinsamen Positionen** gleich und
tragen die Berufungsformel aus 1,10 (`ausreißen` · `niederreißen` ·
`vernichten` · `aufbauen` · `pflanzen`), hier im **Singular** von `Volk` und
`Königreich`. Die `um zu`-Eintraege enden vor dem freien `zu` — der Quelltext
hat `auszureißen`/`aufzubauen` mit **inkorporiertem `zu`**, die in
`konvention.py` dokumentierte Fehlalarmklasse.

### Was wie eine Dublette aussah und keine ist

* **7,34 hat `das Jubeln`, 16,9 hat `des Jubels`** — substantivierter Infinitiv
  gegen Substantiv, **zwei Lemmata**. `Jubel` C1 *jubilation · júbilo ·
  allégresse · giubilo* (36 Belege, Ps 27,6) gegen `Jubeln` C1 *cheering*.
  Ausserdem steht die Klammer in 7,34 zusammen (`verstummen lassen`), in 16,9
  getrennt (`ich lasse … verstummen`, `parts` [11,30]).
* **`Starrsinn` steht nicht in 18,12**, obwohl dieses Wortfeld es behauptet
  hatte und **alle vier Ausgaben** dort *stubbornness · terquedad · penchants ·
  caparbietà* lesen. Der l1912mod schreibt `was ihm sein böses Herz eingibt` —
  `eingeben` C1 *prompts · inspira · inspire · ispira*. Die Formelliste ist
  korrigiert.
* **17,23 traegt das Adjektiv `starrsinnig` C1** (*stubborn · obstinados ·
  obstinés · ostinati*, Plural nach Neh 9,16), nicht das Substantiv. pos 0-9
  sind Feld fuer Feld aus 7,24 = 11,8.
* **17,3-4 gegen 15,13-14**: nur `preisgeben`, `Schatz`, `Gebiet`, `entfachen`,
  `brennen`, `Feind`, `Land` und die Futurperiphrase sind gleich. 17,3 hat
  `Vermögen` B2 und `als Beute` statt `Reichtum` und `ohne Bezahlung`; 17,4 hat
  das neu gepraegte Kausativ **`dienen lassen` B2** statt `ausliefern`.

### `Griffel` traegt im Buch zwei Reihen — und das ist richtig

| Stelle | Reihe | Grund |
|---|---|---|
| **8,8** | pen · pluma · plume · penna | der luegnerische Griffel der **Schriftgelehrten**; alle vier Ausgaben schreiben die Feder |
| **17,1** | stylus · cincel · burin · scalpello | hier wird **eingeritzt und gegraben**, mit `diamantener Spitze`; RV *cincel*, LSG *burin*, RIV *stilo* — drei von vier auf dem Gravierwerkzeug |

Nur WEB schreibt an beiden Stellen *pen* — und WEB schreibt auch in Hiob 19,24
„iron pen", wo der Bestand *stylus* gesetzt hat. `eisern` B2 hat seinen
einzigen Bestandsbeleg ebenfalls in Hiob 19,24: **derselbe Vers, dasselbe
Werkzeug.** Der in Paket 3 gemeldete Befund zu **Ps 45,2** (dort ist es der
Schreibgriffel und traegt faelschlich die Meisselreihe) bleibt bestehen.

### `konsistenz.py` gehoert ab jetzt in die Einsammelkette

Nach der `Gürtel`-Lehre aus Paket 5 laeuft `konsistenz.py 24` seit diesem Paket
nach jedem Build mit. Es hat sofort etwas gefunden, das zwischen allen anderen
Netzen liegt:

**`Angst` stand in 6,24 als *fear · miedo · peur · paura*, in 4,31 · 13,21 ·
15,8 als *anguish · angustia · angoisse · angoscia*** — und zwar in derselben
Bedeutung: alle vier Verse vergleichen die Angst mit den Wehen einer
Gebaerenden. In 6,24 schreiben **alle vier Ausgaben** *anguish · angustia ·
angoisse · angoscia*. Angeglichen; 6,24 war der Ausreisser, drei gegen einen.

`paketcheck.py` konnte es nicht sehen (die Kapitel lagen in verschiedenen
Paketen), `glosskollision.py` auch nicht (verschiedene Verse), und im Bestand
gibt es keine Bindung dagegen (`Angst` steht dort 97-mal auf *fear*).
**Abschnitt B von `konsistenz.py` ist das einzige Netz fuer diesen Fall.**

### Zwei Entscheidungen, die spaetere Pakete binden

* **`Schefela` (17,26) ist Name geblieben**: A1 *Shephelah · Sefela ·
  Schéphéla · Scefela*. **Keine der vier Ausgaben transliteriert** (WEB
  *lowland*, RV *llanura*, LSG *vallée*, RIV *piano*), und der Bestand
  uebersetzt dieselbe Landschaft anderswo als `Hügelland` C1 / `Niederung` C1.
  Entschieden hat der deutsche Text: eine Lautfolge ohne deutsche Bedeutung
  bleibt Name. **`Schefela` steht noch in 32,44 und 33,13** — dort dieselbe
  Reihe, oder die Entscheidung wird zentral umgedreht.
* **`Volkstor` (17,19)** C1 *gate of the people · puerta del pueblo · porte du
  peuple · porta del popolo* — deutsches Kompositum, alle vier Ausgaben
  umschreiben, also uebersetzt statt transliteriert. Die Gegenprobe zur
  `Schefela`-Regel im selben Kapitel.

### Befunde im Bestand

* **`preisgeben` und `ausliefern` sind im ganzen Bestand nicht unterscheidbar**
  (es/fr/it fallen vollstaendig zusammen) und stehen in **18,21 im selben
  Vers**. Dort ist `ausliefern` auf *hand over · abandona · abandonne ·
  abbandona* ausgewichen (RIV schreibt genau das). Korpusweit nicht angefasst.
* **`Verfolger` C1**: zum zweiten Mal in diesem Buch (15,15 und 17,18) schreiben
  **alle vier Ausgaben** die Verfolgungslesart, waehrend die AT-Bindung 14 : 2
  auf *pursuers* steht. Zwei Kapitel stuetzen jetzt eine Korrektur.
* **`Land` traegt in 17,3 die Feldlesart** *country · campo · champ ·
  campagna* („im offenen Land"), in 17,4 · 17,6 · 17,26 die Bindung *land ·
  país · pays · paese*. Der Vers entscheidet.
* `reichen` (16,7, den Becher **reichen**) und `treiben` (16,12, es schlimmer
  **treiben**) haben im Bestand keine passende Lesart; beide sind nach den
  Ausgaben vergeben und als Kandidaten fuer eine zweite Bestandslesart
  gemeldet. `ritzen` C1 traegt eine Gravur-Reihe, die an allen drei Belegen
  (3Mo 21,5 · 5Mo 14,1 · hier 16,6) gleich schief aussieht.

### Befunde in den Ausgaben

* Vier RIV-Anlautfehler (16,5 „ompiangerli" · 17,8 „essa" statt *cessa* ·
  17,18 „enir" · 18,22 „oiché").
* **WEB, RV, LSG und RIV setzen die Satzgrenze zwischen 18,14 und 18,15
  anders** als der l1912mod („Aber mein Volk hat mich vergessen" steht deutsch
  am Ende von 18,14, dort am Anfang von 18,15). Kein Versatz, eine
  Klauselverschiebung — dieselbe Bauform wie RIV in 7,10/7,11 und 17,19/17,20.
* **RV1909mod siezt auch in den Kapiteln 13, 16 und 17** (*ustedes*), waehrend
  der Bestand im ganzen Buch *vosotros* fuehrt. Dritte Meldung derselben Sache;
  gefolgt ist jedes Mal dem Bestand.
* **LSG 17,6 hat kein Gewaechs**: „Il est comme **un misérable** dans le
  désert", wo WEB *heath*, RV *retama* und RIV *tamerice* stehen — vier
  Ausgaben, drei Pflanzen und ein Mensch. `Wacholderstrauch` C1 ist nach dem
  deutschen Wort gepraegt.

### Neue Lemmata des Pakets (16)

`Trauerhaus` C1 · `Trostbecher` C1 *cup of consolation · copa de consuelo ·
coupe de consolation · coppa della consolazione* · `unbeklagt` C1 ·
`unbegraben` C1 · `anfüllen` B2 · `Wacholderstrauch` C1 · `diamanten` C1 ·
`Volkstor` C1 · `Unglückstag` C1 · `Schefela` A1 · `sich drücken` C1 ·
`dienen lassen` B2 · `Töpferscheibe` C1 *potter's wheel · rueda de alfarero ·
tour de potier · ruota da vasaio* · `Bergwasser` B2 · `misslingen` B2 ·
`zudenken` C1 · `erwürgen` C1 · `straucheln lassen` C1.


## 8. Paket 7 (Kap. 19 · 20 · 21) — das sauberste Paket des Buches

47 Verse, 1433 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer, und **`glosskollision.py` meldet in allen drei Kapiteln null inhaltliche
Paare** — zum ersten Mal im Buch. `qa`, `konvention`, `sweeplemma` und
`levelcheck` laufen ueber alle drei Kapitel ohne einen Treffer; `sweep` hat
einen Fehlalarm.

### Zwei Vorlagen, die die Vorbereitung nicht kannte

* **19,3 ist fast woertlich 2. Koenige 21,12** („dass jedem, der davon hört, die
  Ohren gellen werden"). 16 von 16 gemeinsamen Feldern uebernommen; abgewichen
  ist nur das Genus (`Unglück` fem. dort, `Unheil` mask. hier — **zwei
  Lemmata**, und der l1912mod waehlt in Jeremia durchgehend `Unheil`).
* **19,6 hat in 16,14 einen laengeren Block als in 7,32** — zwoelf Tokens bei
  Versatz +0, gefunden von `parallelen.py` im Agentenlauf. pos 0-11 stammen von
  dort, nicht aus 7,32.

Zweite Bestaetigung derselben Lehre wie in Paket 4 (Ps 135,7 zu 10,13): **der
Befund der Vorbereitung ist eine untere Schranke.**

### Der Name, den der Text selbst uebersetzt — der zweite Fall des Bestands

**20,3 nennt Paschhurs neuen Namen `Grauen-ringsum`**, ein deutsches
Kompositum. Alle vier Ausgaben transliterieren (*Magor-Missabib*), aber nach
der Regel aus `AUFTRAG_BUCH.md` entscheidet der deutsche Text — wie bei
`Doppelhöhle` (Machpela), `Warte` (Mizpa) und `Schnell-Raub-Eilige-Beute`
(Jes 8,1). Gebaut in der Bindestrichform des Jesaja-Vorbilds:

    Grauen-ringsum  C1  Horror-all-around · Horror-alrededor ·
                        Effroi-tout-autour · Orrore-tutt'intorno

**20,10 hat dieselben zwei Woerter als freie Wendung** (`Grauen ringsum!`) und
traegt sie einzeln: `Grauen` C1 *horror · horror · effroi · orrore* +
`ringsum` B2. Der Name ist Bestandteil fuer Bestandteil die Summe der Wendung.

### `starrköpfig` — das vierte Wort eines Feldes, das jetzt viergliedrig ist

19,15 bringt ein drittes deutsches Wort fuer dieselbe Sache, und es ist im
Bestand unbelegt. Gepraegt als `starrköpfig` C1 ***headstrong · tercos · têtus ·
caparbi*** — und zwar bewusst mit den spanischen und italienischen Lesarten,
die in **Paket 3 fuer `Starrsinn` verworfen** worden sind. Damit steht das Feld
in allen vier Sprachen kollisionsfrei:

| Wort | Level | en · es · fr · it |
|---|---|---|
| `Starrsinn` | C1 | stubbornness · obstinación · obstination · ostinazione |
| `starrsinnig` | C1 | stubborn · obstinado · obstiné · ostinato |
| `starrköpfig` | C1 | headstrong · tercos · têtus · caparbi |
| `halsstarrig` | C1 | stiff-necked · de dura cerviz · au cou raide · di collo duro |

**Alle vier Ausgaben schreiben in 19,15 das Nackenbild** („made their neck
stiff", „endurecido su cerviz") — das waere `halsstarrig` gewesen. Der deutsche
Text sagt `starrköpfig`, und nach ihm ist gepraegt.

### `Scherbentor` (19,2) — die Gegenprobe zur `Schefela`-Regel

Deutsches Kompositum mit deutscher Bedeutung, also **uebersetzt**:
`Scherbentor` C1 *Potsherd Gate · Puerta de los Tiestos · porte des Tessons ·
porta dei Cocci*, gebaut auf `Scherbe` C1. Die Ausgaben helfen nicht und
widersprechen einander in drei Richtungen: **WEB transliteriert** (*the gate
Harsith*), **RV liest eine Himmelsrichtung** (*la puerta oriental*), LSG und
RIV die Toepferei. Zusammen mit `Volkstor` (Paket 6) und `Schefela` (Paket 6)
ist die Regel jetzt dreimal angewandt.

### `Verfolger`: drei Kapitel, zwoelf Ausgabenbelege gegen null

15,15 · 17,18 · 20,11 — an **allen drei Stellen** schreiben **alle vier
Ausgaben** die Verfolgungslesart (*persecutors · perseguidores · persécuteurs ·
persecutori*), waehrend die AT-Bindung 16 : 2 auf *pursuers · perseguidores ·
poursuivants · inseguitori* steht (die zwei Ausnahmen sind NT). Jedes Mal ist
der Bindung gefolgt worden. **Das ist der best belegte Korrekturkandidat des
Buches** — zwoelf Ausgabenbelege gegen keinen einzigen dagegen.

### Zwei Namen, die der Bestand anders schreibt

* **`Paschhur`** (20,1 · 21,1) steht im Bestand als Lemma **`Pashur`** A1
  (6 Belege) — dort schreibt der l1912mod `Pashur`, in Jeremia `Paschhur`. Zwei
  deutsche Formen, deshalb ein eigenes Lemma; die Reihe *Pashhur · Pashur ·
  Paschhur · Pashur* folgt den Ausgaben **an dieser Stelle**. Nebenbefund:
  **RV1909mod schreibt in Esra 2,38 *Pasur*, in Jeremia *Pashur*** — dieselbe
  Ausgabe, zwei Schreibungen. Kandidat fuer eine korpusweite Vereinheitlichung.
  Beide Agenten haben unabhaengig dieselbe Reihe gesetzt; `paketcheck.py`
  Abschnitt A bestaetigt es.
* **`Malkija`** (21,1) fuehrt der Bestand als **`Malchia`** A1 mit 13 Belegen —
  `belegt.py` schweigt zur Form, `fixgloss.py show` findet es. **Sechste
  Bestaetigung der Form-gegen-Lemma-Falle.**
* **`Immers`** (20,1) ist der Vatersname, kein Adverb: `Immer` A1 *of Immer ·
  de Imer · d'Immer · di Immer* (4 Belege) gegen `immer` A1 mit 418 Belegen.

### Ein widerlegter Hinweis und ein angeglichener Ausreisser

**Der Hinweis „21,8 hat eine Vorlage in 5. Mose 30,15" ist falsch.** Dort steht
`das Leben und das Gute … den Tod und das Böse` — **kein `Weg`**, keine
Wegformel. Gemeinsam ist allein das Mehrwort `vorlegen` B2. `den Weg zum Leben
und den Weg zum Tod` ist neu entschieden, mit `zum` = *of · de la · de la ·
della*, weil alle vier Ausgaben „way of life / camino de vida" lesen.

**`der Gott Israels` stand in 13,12 italienisch als *Iddio*, an allen 27
uebrigen Stellen des Buches als *Dio*.** RIV schreibt zwar an allen sechs
Formelstellen *Iddio*, der Bestand aber steht mit ueber 750 Belegen auf *Dio*.
13,12 ist angeglichen — der zweite Fund von `konsistenz.py` in zwei Paketen.

### Die `Gürtel`-Lehre wirkt jetzt im Agentenlauf

Der Agent von Kapitel 20 hat seine haeufigen Lemmata am Ende **selbst gegen
sich geprueft** und dabei zwei Uneinheitlichkeiten gefunden und bereinigt, die
durch alle sieben Netze gefallen waeren: `ganz` stand in 20,5 als
*toda/toute/tutta* gegen 20,8 *entero/entier/intero*, und `kommen` in 20,18 als
*salido/sorti/uscito* gegen 20,6 *venir/venir/venire*. **Die Auflage im Prompt
hat gehalten.**

### Befunde im Bestand

* **`Stock` hat keine Block-Lesart, `Block` hat sie.** Der Bestand fuehrt
  `Stock` B1 sechsmal als Stab/Knueppel/Rohr; fuer die Fussfessel gibt es das
  eigene Lemma `Block` C1 *stocks · cepo · ceps · ceppo* (Hi 13,27 · 33,11 ·
  Apg 16,24). In 20,2 · 20,3 schreibt der l1912mod `Stock` und meint dasselbe.
  Genommen ist die **Block-Reihe am Lemma `Stock`**; **LSG paraphrasiert als
  einzige mit *prison***, deshalb ist fr aus dem Bestand (*ceps*, das LSG in
  Hi 13,27 selbst schreibt).
* **`Tat` laeuft mit zwei Reihen bei gleicher Bedeutung**: *deeds · hechos ·
  actes · atti* (131 Belege, u. a. 17,10) gegen *deeds · obras · actions ·
  azioni* (4,4). Beide Verse von Kapitel 21 enthalten `Taten`; nach der
  `Gürtel`-Regel ist im Kapitel **eine** Reihe genommen (die von 4,4, die die
  Ausgaben an beiden Stellen stuetzen). Kandidat fuer eine Angleichung.
* **`höhnen` C1 (1 Beleg) faellt spanisch mit `Spott` B2 (24 Belege) zusammen**
  und beide stehen in **19,8 im selben Vers**; ausgewichen ist das schwaechere
  auf *mofarse*. Nebenbefund: **alle vier Ausgaben lesen `höhnen` dort als
  *hiss/silbar/siffler/fischiare*** (Zischen), der deutsche Text sagt „höhnen".
* **`Bedrängnis`** weicht in 19,9 auf seine NT-Mehrheit *tribulation* aus, weil
  `Not` im selben Vers die AT-Lesart *distress* traegt — hier ist die
  NT-Lesart die kollisionsaufloesende, nicht die falsche.
* `rauben` (3 Belege, „Menschen berauben"), `anzeigen` (1 Beleg, *indicates*),
  `anstellen` (3 Belege) und `irden` (zwei unvereinbare Reihen) liegen alle
  unter der Bindungsschwelle und sind nach den Ausgaben vergeben — vier
  Kandidaten fuer zweite Bestandslesarten.

### Befunde in den Ausgaben

* Vier RIV-Anlautfehler (20,2 „eniamino" · 21,7 zweimal „ano"/„on" · 21,14
  „erusalemme"). **Kapitel 19 ist nach Kapitel 14 das zweite des Buches ohne
  einen einzigen.**
* **RIV verschiebt die Satzgrenze zwischen 19,10 und 19,11** („e dirai loro"
  steht dort am Ende von 19,10) — dieselbe Bauform wie in 7,10/7,11 und
  18,14/18,15. Kein Versatz.
* **RV1909mod siezt in 19,3, 20,10 und 21,12** (*ustedes*, „Oigan",
  „Denúncienlo", „Hagan justicia") — **fuenfte Meldung derselben Sache**. Der
  Bestand fuehrt im ganzen Buch *vosotros*, und ihm ist jedes Mal gefolgt.
* **RIV 21,14 hat ein Wort mehr als alle anderen** („questa selva **di
  Gerusalemme**"), und **LSG liest dort `votre forêt`** (2. Person) gegen den
  Possessivbezug der drei anderen — vier Ausgaben, drei Bezuege.

### `spricht der HERR`: Stand nach 21 Kapiteln

**64 `dit` zu 49 `parle`**, dazu ein *adresse* (10,1, keine Botenformel). Die
Schwankung der Ausgabe bleibt kapitelweise: Kapitel 19 steht 2 : 4, Kapitel 20
hat die Formel nur einmal (*parle*), Kapitel 21 steht 4 : 3.

### Neue Lemmata des Pakets (12)

`starrköpfig` C1 · `Scherbentor` C1 · `höhnen`-Ausweichung (kein neues Lemma) ·
`Paschhur` A1 · `Malkija` A1 · `Grauen-ringsum` C1 · `Oberaufseher` C1 *chief
officer · jefe supervisor · inspecteur en chef · capo-soprintendente* ·
`Erwerb` B2 · `sich überlisten lassen` C1 · `Beraubter` C1 · `davontragen` B2
(**keine der vier Ausgaben** uebersetzt das Verb — alle formulieren um) ·
`Urteil üben` B2 (Mehrwort, nach `Vergeltung üben` in Ps 149,7) ·
`Kriegslärm` C1.


## 9. Paket 8 (Kap. 22 · 23 · 24) — drei Agenten sterben, ein Abschnitt ueberlebt

80 Verse, 2169 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer, 43 Zeilen in B ohne Befund; `qa`, `konvention`, `levelcheck` und
`sweep` ueber alle drei Kapitel ohne Treffer, `glosskollision.py` ein einziges
inhaltliches Paar in einer Sprache.

### Der Abbruch, und was das Wegschreiben gerettet hat

**Alle drei Agenten sind gleichzeitig an einem Serverfehler (HTTP 529)
gestorben**, kurz nach dem Einlesen der Unterlagen. Kapitel 22 und 24 hatten
nichts geschrieben; von Kapitel 23 lagen **die Verse 1-8 als Teildatei** da und
liefen ueber `selfcheck.py 24 23 <datei> 1 8` sauber durch — einschliesslich
der Dublette 23,7/23,8, der schwierigsten Stelle des Kapitels.

Der Nachfolger hat das Fragment als Vorlage gelesen, die Verse 9-40 ergaenzt und
**ueber das ganze Kapitel** geprueft. Dabei hat er im uebernommenen Teil genau
einen echten Fehler gefunden: **`König` stand in 23,5 auf A1, der Bestand fuehrt
es mit 614 Belegen einstimmig auf A2.** Sonst war nichts zu korrigieren.

**Zweite Bestaetigung der Lehre aus dem Nutzungslimit-Abbruch:** das
abschnittsweise Wegschreiben ist der einzige Schutz, und die Selbstpruefung des
Nachfolgers ueber das **ganze** Kapitel ist die zweite Haelfte davon.

### Die woertlichen Uebernahmen, maschinell nachgerechnet

| Vers | Vorlage | Ergebnis |
|---|---|---|
| 23,7 | 16,14 | **31 von 31 Eintraegen identisch** (29 Einzelwoerter + `nicht mehr` + `so wahr`) |
| 24,4 | 13,8 = 18,5 | **8 von 8 Feldern identisch** |
| 23,8 | 16,15 | Block bei Versatz +2 gleich mit **genau einer** Abweichung (pos 26 `ich` gegen `er`) |
| 23,35 | 23,37 | alle 13 gemeinsamen Felder identisch |

### Das `Last`-Wortspiel steht

`Last` steht in 23,33-38 **siebenmal** (nicht achtmal, wie die Vorbereitung
behauptet hatte — das achte entsteht nur, wenn man den Mehrwort-Eintrag
mitzaehlt) und traegt **ausnahmslos** `Last` B1 *burden · carga · charge ·
peso*, dieselbe Reihe wie viermal in 17,21-27. Damit bleibt das Wortspiel in
allen vier Sprachen erhalten — **LSG liest den Vers als *menace*, RIV als
*oracolo***, und wer ihnen folgte, haette es schon im ersten Vers zerlegt.
Dazu in 23,36 zusaetzlich das Bestands-Mehrwort `zur Last werden` B2 ueber den
Einzelwoertern.

### `Konja` gegen `Jechonja` — und ein Befund ueber den Bestand

Der l1912mod schreibt beide Formen desselben Namens im selben Buch: `Konja`
(22,24 · 22,28) und `Jechonja` (24,1). Zwei deutsche Formen, **zwei Lemmata**:

    Konja      A1   Coniah · Conías · Jeconia · Conia
    Jechonja   A1   Jechoniah · Jeconías · Jéchonias · Ieconia   (Bestand)

**Die Ausgaben trennen die beiden Formen nur zu dritt** — LSG schreibt an allen
drei Stellen *Jeconia*. Und der Bestandseintrag fuer `Jechonja` passt an seinen
**eigenen** AT-Belegstellen nicht zur Ausgabe: in 1Chr 3,16 und Est 2,6
schreiben WEB *Jeconiah*, LSG *Jeconia* und RIV *Jeconia*, waehrend die
Bestandsreihe *Jechoniah · Jéchonias · Ieconia* fuehrt — sie stammt aus den
Matthaeus-Belegen. **Korrekturkandidat fuer die AT-Stellen**; genommen ist
vorerst die Bestandsreihe, weil der Name dort bereits belegt ist.

### Drei Level-Angaben der Vorbereitung waren falsch

`Thron` ist **B2**, nicht B1. `Tor` ist **B1**, nicht A2. `denn` ist **A2**,
nicht A1. Alle drei von Agenten am Bestand widerlegt und von `levelcheck.py`
bestaetigt. Dazu die Fragment-Korrektur `König` A2. **Vier Level-Befunde in
einem Paket** — die Vorgabetabellen dieser Vorbereitung waren an dieser Stelle
schlechter als der Bestand.

### `Rat` traegt im Buch zwei englische Lesarten, und beide sind richtig

    18,18   advice · consejo · conseil · consiglio    (der Rat, den der Weise gibt)
    23,18   council · consejo · conseil · consiglio   (der Gottesrat als Versammlung)
    23,22   council · consejo · conseil · consiglio

Nur Englisch kann die beiden Bedeutungen trennen, und es tut es; es, fr und it
decken beide mit einem Wort. **Kein Ausreisser** — `konsistenz.py` wird das Paar
melden, es ist keiner.

### Zwei Kollisionen, die im selben Vers auseinandergehalten werden mussten

* **22,23 `Wehen` und `Geburtsschmerzen` stehen nebeneinander.** `Wehen` C1
  *birth pains · dolores de parto · douleurs de l'enfantement · doglie* aus
  13,21; `Geburtsschmerzen` C1 ist abgesetzt auf *labor · parto · travail ·
  parto* — genau das, was die vier Ausgaben dort schreiben.
* **24,1 `Schmiede` und `Schlosser` stehen nebeneinander.** `Schmied` B2 traegt
  die Bestandsreihe *smiths · herreros · forgerons · fabbri*; das neu gepraegte
  `Schlosser` B2 weicht italienisch auf ***magnani*** aus statt auf das
  naheliegende *fabbri*. Entschieden ueber LSG (*serruriers*, die einzige
  Ausgabe, die das deutsche Wort trifft). **29,2 ist die einzige weitere Stelle
  im Bestand und muss dieselbe Reihe bekommen.** Nebenbefund: drei der vier
  Ausgaben haben an erster Stelle den **Zimmermann**, der l1912mod den Schmied.

### „Im Bestand unbelegt": von sechs Meldungen war eine richtig

In Kapitel 23 hat `belegt.py` fuenf von sechs widerlegt (`abwerfen`,
`nachlassen`, `Entweihung`/`entweihen`, `Grauenhaftes`/`Grauen`,
`künftig`) — **nur `ruchlos` ist wirklich unbelegt**. In Kapitel 22 dasselbe
Bild: `stöhnen` (3 Belege, Ps 55) und `Trümmerstätte` (2Chr 34,6) standen
laengst da, `einschreiben` ebenfalls. **Siebte und achte Bestaetigung der
Form-gegen-Lemma-Falle.**

### Die Eigenpruefung der Agenten faengt jetzt mehr als die Pflichtlaeufe

Der Agent von Kapitel 22 hat beim maschinellen Abgleich seiner haeufigen
Lemmata **vier** Uneinheitlichkeiten gefunden, die durch alle sieben Netze
gefallen waeren: `hören` stand in 22,2 spanisch als *Oye*, in 22,29 als
*escucha* — **dieselbe Formel `Hör das Wort des HERRN`**; dazu `mit`, `nur` und
das Paar `geben`/`Hand` in 22,25. Der Agent von Kapitel 24 hat sechs Lemmata
gegengeprueft und keines beanstandet.

### Befunde im Bestand

* **`Ungerechtigkeit` und `Unrecht` fallen in es/fr/it vollstaendig zusammen**
  und stehen in 22,13 im selben Vers; ausgewichen ist das schwaechere
  (18 gegen 99 Belege) auf *iniquidad · iniquité · iniquità*, was LSG dort
  selbst schreibt.
* **`Schmach` und `Schande` fallen in en/es zusammen** und stehen in 23,40 im
  selben Vers; `Schmach` weicht auf *reproach · oprobio · outrage · oltraggio*.
* **`vernehmen` und `hören` fallen in allen vier Sprachen zusammen** und stehen
  in 23,18 im selben Vers; `vernehmen` weicht auf *perceived · percibido ·
  perçu · colto* (Hi 26,14).
* **`Hohn` traegt franzoesisch zwei Reihen** (*dérision* in den Psalmen,
  *opprobre* in Jes 51,7 und Jer 20,8) — Angleichungskandidat.
* **`weihen` gegen alle vier Ausgaben durchgehalten**: 22,7 schreiben sie
  einstimmig *prepare*, das deutsche Wort ist `weihen`, und die Bestandsreihe
  hat 86 Belege.
* `heißen` (22,16, „Heißt das nicht"), `halten` (22,21, „so hast du es
  gehalten"), `zurückziehen` (22,27), `wegschicken` (24,5, in die Verbannung),
  `wahrhaftig` (23,28), `künftig` (23,20), `glatt` (23,12) und `enthalten`
  (24,2) haben im Bestand **keine passende Lesart** und sind nach den Ausgaben
  vergeben — acht Kandidaten fuer zweite Bestandslesarten in einem Paket.

### Befunde in den Ausgaben

* Drei RIV-Anlautfehler, alle in Kapitel 22 (22,2 „opolo" · 22,11 „iosia" ·
  22,25 „ebucadnetsar"). **Kapitel 23 und 24 sind ohne einen** — damit sind es
  vier solche Kapitel im Buch (14 · 19 · 23 · 24).
* **RIV verschiebt die Satzgrenze in 22,1/22,2 und in 23,26/23,27** — dieselbe
  Bauform wie in 7,10/7,11, 19,10/19,11 und 24,5/24,6. Kein Versatz.
* **WEB 22,27 hat einen Setzfehler**: „to the land **t** which their soul
  longs".
* **RV1909mod siezt in allen drei Kapiteln** (22,3 · 22,30 · 23,2 · 23,16 ·
  23,17 · 23,39) — **siebte Meldung derselben Sache**; jedes Mal ist dem
  Bestand (*vosotros*) gefolgt.
* **`wirbelnder Sturm` (23,19) hat nur WEB** — RV *una tempestad ya preparada*,
  LSG *L'orage se précipite*, RIV *la tempesta scroscia*: vier Ausgaben, drei
  Bilder. `wirbelnd` C1 ist nach dem deutschen Wort gepraegt.

### `spricht der HERR`: Stand nach 24 Kapiteln

**86 `dit` zu 60 `parle`**. Kapitel 23 allein hat die Formel **22-mal**
(18 : 4), Kapitel 22 neunmal (3 : 6). **In 23,31 hat LSG keine Entsprechung**
(sie formuliert um) — dort ist der Vorgabewert *dit* gesetzt.

### Neue Lemmata des Pakets (16)

`Konja` A1 · `erpressen` C1 · `bemalen` B2 · `fortschleifen` C1 ·
`Geburtsschmerzen` C1 · `einbauen` B2 + `einbauen lassen` B2 · `übermannen` C1
· `ruchlos` C1 *profane · impíos · corrompus · empi* · `Grauenhaftes` C1 ·
`Entweihung` C1 *profanation · profanación · profanation · profanazione* ·
`wirbelnd` C1 · `niederfahren` B2 · `Leichtsinn` B2 · `gar nichts` A2
(Mehrwort) · `Schlosser` B2 *locksmiths · cerrajeros · serruriers · magnani* ·
`Verschleppter` C1 *deportees · deportados · déportés · deportati*.


## 10. Paket 9 (Kap. 25 · 26 · 27) — die Datierungsformel und der Voelkerbecher

84 Verse, 2312 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer, 44 Zeilen in B ohne Befund; `qa`, `konvention`, `levelcheck` und
`sweep` ueber alle drei Kapitel ohne Treffer. `glosskollision.py` meldet in 25
und 27 **null** inhaltliche Paare, in 26 zwei — beide `alles`/`ganz`, die
benannte Verschmelzung der Zielsprachen (*todo · tout · tutto* deckt beide
deutschen Woerter), wie schon 7,15 in Paket 3.

### Die Datierungsformel — drei Fassungen, und zwei mussten von Hand zusammen

Das Buch beginnt hier, Sprueche zu datieren. **26,1 und 27,1 sind bis auf den
Koenigsnamen derselbe Satz** und lagen bei **verschiedenen Agenten**; sie sind
verschieden gebaut zurueckgekommen und beim Einsammeln angeglichen worden:

* **`am Anfang`** ist ein Bestands-Mehrwort (3 Belege, Spr 20,21 · Pred 10,13 ·
  2Petr 2,20). 27,1 hatte es gesetzt, 26,1 nicht — **kein Pflichtlauf meldet
  das**, weil beide Verse fuer sich strukturell vollstaendig sind. Nachgetragen.
* **Die Genitiv-Apposition `des Sohnes … des Königs`**: 25,1 und 27,1 hatten
  *of the · del · du · del*, 26,1 *the · el · le · il*. Entschieden ueber den
  Bestand — die Wortfolge `des Sohnes` steht dort **288-mal** mit *of the* und
  55-mal mit *the*. 26,1 ist angeglichen.

Danach sind **26,1 und 27,1 in allen dreizehn gemeinsamen Feldern identisch**,
die einzige Abweichung ist der Koenigsname. Beide sind Vorlage fuer 35,1 und
36,1, 27,1 zusaetzlich fuer 49,34.

**25,1 ist die dritte Fassung** (`im vierten Jahr Jojakims`), Vorlage fuer
32,1 · 35,1 · 36,1. Der Anfang ist Feld fuer Feld 11,1 = 21,1; **`vom HERRN`
fehlt dort**, an seiner Stelle steht `über das ganze Volk Juda` mit `über`
*concerning · acerca de · sur · riguardo a*.

### Der Voelkerbecher: die dichteste Namensliste des Buches

25,18-26 nennt neunzehn Voelker und Staedte, und **alle bis auf einen stehen im
Bestand** — `Uz` · `Askalon` · `Gaza` · `Ekron` · `Aschdod` · `Dedan` · `Tema` ·
`Bus` · `Elam` · `Medien` · `Tyrus` · `Sidon` · `Edom` · `Moab` · `Ammoniter` ·
`Philister` · `Pharao` · `Ägypten` · `Arabien`, jeder einzeln mit `belegt.py`
geprueft. Zwei Sonderfaelle:

* **`Simri` (25,25) hat zwei Bestandslesarten** — *Zimri* (12 Belege) und
  *Shimri* (2). Hier ist der Voelkername gemeint, und alle vier Ausgaben
  schreiben *Zimri*.
* **`Scheschach` (25,26) ist wirklich unbelegt** und nach den Ausgaben gepraegt:
  A1 *Sheshach · Sesac · Schéschac · Sceshac*.

### `sich gereuen lassen` in drei Konstruktionen

Kapitel 26 hat das Verb dreimal, und nur eine der drei ist die Konstruktion aus
18,8:

    26,3    dann lasse ich mich das Unheil gereuen     → Mehrwort, Feld fuer Feld aus 18,8
    26,13   dann wird der HERR das Unheil gereuen      → kein `sich`, also kein Mehrwort
    26,19   sodass der HERR das Unheil gereute         → Praeteritum, dieselbe Reihe

`gereuen` C2 traegt an allen drei Stellen dieselbe Reihe, nur konjugiert.
**Eine Futurklammer (`wird … gereuen`) ist nach SPEC kein Mehrwort** — die
Unterscheidung haette kein Lauf erzwungen.

### Die vier Wahrsage-Berufe in einem Vers

27,9 stellt `Wahrsager`, `Traumdeuter`, `Zeichendeuter` und `Zauberer`
nebeneinander. `Zauberer` C1 traegt *sorcerers · hechiceros · **magiciens ·
maghi***, und `Wahrsager` hat im Bestand eine Reihe, die Wort fuer Wort
dieselbe waere. Genommen ist dessen 10-Beleg-Mehrheit *soothsayers · adivinos ·
devins · indovini*; danach ist der Vers in allen vier Sprachen kollisionsfrei.
**Der Auftrag hatte die kollidierende Reihe mit zwei Belegen angegeben — sie hat
einen.**

### Was `parallelen.py` wieder nicht gemeldet hat

* **25,33 deckt sich enger mit 8,2 als mit dem gemeldeten 9,21** — dort stehen
  `einsammeln`, `begraben`, `Dung` und `liegen` bereits nebeneinander.
  Uebernommen ist 8,2. **Dritte Bestaetigung**, dass der Werkzeugbefund eine
  untere Schranke ist (nach Ps 135,7 in Paket 4 und 2Kön 21,12 in Paket 7).
* **26,18 ist die Vorlage fuer Micha 3,12**, aber `parallelen.py` konnte das
  nicht sehen, weil Buch 33 im Bestand fehlt. Der Agent hat es am Quelltext
  gefunden: `Tempelberg`, `bewaldet` und `umpflügen` gelten dort unveraendert,
  **`Steinhaufen` ≠ `Trümmerhaufen`** — zwei Lemmata.

### Elf fehlende Bestands-Mehrwoerter in einem Kapitel

`sweep.py` und `sweeplemma.py` haben in Kapitel 25 elf Wendungen
hervorgeholt, darunter `bis zum heutigen Tag` B1, `für immer und ewig` B2,
`zu trinken geben` B1 und dreimal `machen zu` B1. **Gemeldet war nur ein Teil
davon** — der Agent hat die uebrigen an derselben Konstruktion selbst gefunden,
wie in Paket 3 bei `hören auf`.

### `Micha` ist im Bestand belegt, aber es ist ein anderer Mensch

Der Bestand fuehrt `Micha` A1 *Micah · **Micaías · Mica · Mica*** (Ri 17 ·
1Kön 22 · 2Sam 9). 26,18 ist Micha von Moreschet, und alle vier Ausgaben
schreiben ihn anders: *Micah · Miqueas · Michée · Michea*. Genommen ist die
zweite Lesart am selben Lemma — dieselbe Bauform wie `Griffel` in Paket 6.

### `Reichtum`: ein Ausreisser, den `konsistenz.py` gefunden hat

Das Wort steht viermal im Buch und trug **zwei englische Lesarten bei gleicher
Bedeutung**: *riches* in 9,22 und 20,5, *wealth* in 15,13 und 17,11. Der
Bestand steht 62 : 15 auf *riches*, und **WEB schreibt in 9,22, 17,11 und 20,5
selbst *riches***. 15,13 und 17,11 sind angeglichen — der dritte Fund von
`konsistenz.py` seit Paket 6.

### Befunde im Bestand

* **`ewig` weicht in 25,9 und 25,12 franzoesisch aus**, weil `HERR` dort
  *ÉTERNEL* traegt und `ewig` *éternel* getragen haette — genommen ist die
  vorhandene zweite Bestandsreihe *perpétuel*.
* **`Klang` und `Geräusch` tragen beide *sound*** und stehen in 25,10 im selben
  Vers; `Geräusch` weicht auf *noise* aus und faellt damit mit `Lärm`
  zusammen — die beiden stehen nirgends im selben Vers. Kandidat fuer eine
  korpusweite Trennung.
* **`Ende` hat zwei romanische Reihen bei gleicher Bedeutung** (*fin* aus
  Spr 17,24 gegen *extremo/extrémité/estremità* aus Jes 48,20). Im Kapitel ist
  nach der `Gürtel`-Regel **eine** genommen.
* **`Höhe` hat fuer die Gelaendebedeutung nur eine Pluralreihe** — 26,18
  braucht den Singular und bekommt *height · altura · hauteur · altura*, nicht
  die Maß-Reihe *altezza*.
* `dringen` (25,30 · 25,31), `erwirken` (27,18), `laden` (26,15), `holen`
  (26,23), `weglassen` (26,2) haben im Bestand keine passende Lesart und sind
  nach den Ausgaben vergeben — fuenf weitere Kandidaten fuer zweite
  Bestandslesarten.
* **`Hals` A2 und `Nacken` C1 tragen dieselbe Reihe** und stehen in Kapitel 27
  in verschiedenen Versen — nach der Regel **nicht** aufgeloest.

### Befunde in den Ausgaben

* **RIV laesst Medien in 25,25 aus und holt es in 25,26 nach** — eine
  Klauselverschiebung ueber die Versgrenze, kein Versatz. **RIV 25,20 schreibt
  „del paese di Ur" statt *Uz***, ein Buchstabenfehler derselben Bauart wie die
  Anlautfehler.
* **In 27,1 lesen alle vier Ausgaben „Jojakim", der deutsche Text sagt
  `Zedekias`.** Nach dem Deutschen glossiert — der auffaelligste Textbefund des
  Pakets.
* **RV 25,23 liest die Schläfen-Wendung ganz anders** („los confines del
  mundo"); genommen ist die fertige Reihe aus 9,25.
* **LSG 25,20 schreibt „toute l'Arabie" statt der Fremdvoelker** und 25,24 „les
  Arabes", wo im Deutschen `Arabiens` **und** `Fremdvölker` nebeneinanderstehen.
* **Kapitel 25 hat keinen einzigen RIV-Anlautfehler**, Kapitel 26 einen, Kapitel
  27 zwei. Damit sind es fuenf anlautfehlerfreie Kapitel im Buch (14 · 19 · 23 ·
  24 · 25).
* **RV1909mod siezt in allen drei Kapiteln** — neunte Meldung derselben Sache.

### Die Eigenpruefung: sieben Befunde in einem Kapitel

Der Agent von Kapitel 26 hat beim maschinellen Abgleich seiner haeufigen
Lemmata **sieben** Uneinheitlichkeiten gefunden und bereinigt, darunter `Wort`
einmal franzoesisch als *mot* statt *parole* und **`töten` franzoesisch als
*mourir* („sterben") statt *tuer***. Der Agent von Kapitel 25 hat eine gefunden:
`alle` stand in **einem Vers zweimal vor demselben Substantiv**, einmal
maskulin und einmal feminin. Alle acht waeren durch alle sieben Netze gefallen.

### `spricht der HERR`: Stand nach 27 Kapiteln

**91 `dit` zu 64 `parle`** (ohne Kapitel 26 und 27 gezaehlt: die drei Kapitel
bringen 9 : 4, 0 : 3 und 4 : 4). In **23,31 und 26,x** hat LSG teils keine
Entsprechung; dort ist der Vorgabewert *dit* gesetzt.

### Neue Lemmata des Pakets (13)

`Scheschach` A1 · `Zornwein` C1 *wine of wrath · vino de ira · vin de colère ·
vino d'ira* · `Fremdvolk` C1 · `Kelterer` C1 *grape treaders · pisadores de uva
· fouleurs au pressoir · pigiatori d'uva* · `Heulen` C1 (Substantiv neben dem
Verb, nach dem Muster `Jubel`/`Jubeln`) · `Volksversammlung` C1 · `Tempelberg`
C1 · `Moreschet` A1 · `Schemaja` A1 (Reihe vom Bestandslemma `Semaja`) ·
`Friedhof` B1 · `Jochstange` C1 *yoke bars · barras de yugo · barres de joug ·
stanghe di giogo* · `erwirken` C1 · `zurückbringen lassen` B2.


## 11. Paket 10 (Kap. 28 · 29 · 30) — das Paket mit den meisten fertigen Vorlagen

73 Verse, 1969 Eintraege, Versatz +0 ueberall. `paketcheck.py` Abschnitt A und
C leer, 42 Zeilen in B ohne Befund; `qa`, `konvention`, `levelcheck` und
`sweep` ueber alle drei Kapitel ohne Treffer. `glosskollision.py` meldet in 29
und 30 **null** inhaltliche Paare, in 28 eines in einer Sprache.

**Achtzehn Dubletten hatten eine fertige Vorlage** — so viele wie in keinem
Paket zuvor. Alle sind maschinell nachgerechnet:

| Vers | Vorlage | Ergebnis |
|---|---|---|
| **30,1** | 11,1 | **10 von 10 Feldern identisch** |
| **29,30** | 13,8 = 18,5 = 24,4 | **7 von 8 identisch**, die eine Abweichung ist `an Jeremia` statt `an mich` |
| **30,23** | 23,19 | Position fuer Position gleich, **nur pos 10 weicht ab** (`wütender` statt `wirbelnder`) |
| **30,24** | 23,20 | ab pos 2 gleich bei Versatz −1; `glühende` ist neu, `klar` entfaellt |
| **29,9** | 27,15 | alle 13 gemeinsamen Felder identisch |
| **29,18** | 24,9 | 22 von 24 gemeinsamen Feldern |
| **29,19** | 26,5 | einschliesslich der invertierten `hören auf`-Klammer |
| **30,22** | 11,4 | Bundesformel, pos 2-10 feldgleich |
| **28,1** | 27,1 | alle gemeinsamen Positionen; die vierte Fassung der Datierungsformel laesst die Apposition `des Sohnes X` weg |

Damit sind **29,30 und 30,1 zusammen Vorlage fuer achtzehn spaetere Stellen**
(32,6 · 32,26 · 33,19 · 33,23 · 34,12 · 35,12 · 37,6 · 42,7 · 43,8, je in
beiden Fassungen). Die beiden Agenten haben ohne Absprache dieselben Werte
gesetzt — kein Eingriff noetig.

### Die Kollision, die Paket 3 vorhergesagt hat

**29,18 stellt `Schrecken` und `Entsetzen` zum ersten Mal im Buch in einen
Vers.** Paket 3 hatte das Paar gemeldet und mit „stehen nie im selben Vers"
nicht aufgeloest — hier ist die Kollisionsstelle. Ausgewichen ist das
schwaechere `Entsetzen` (8 Belege gegen 46), und nur in den zwei betroffenen
Sprachen:

    Schrecken  B2  terror · espanto · terreur · terrore        (unveraendert)
    Entsetzen  C1  astonishment · asombro · effroi · spavento   (nur en/es)

WEB schreibt dort *astonishment*, RIV *stupore* — die Ausweichung ist gestuetzt.
**Die Auflösung gilt nur an der Kollisionsstelle**; an den uebrigen Stellen des
Buches behaelt `Entsetzen` seine Reihe.

### Die Form-gegen-Lemma-Falle mit gefaehrlicherem Vorzeichen

**`wachst` (29,26) fuehrt `belegt.py` ausschliesslich unter `wachsen` A2
(„grow").** Im Vers ist es aber das **Wachehalten** des Aufsehers, und alle
vier Ausgaben schreiben es so. Bisher hat die Falle immer **geschwiegen** (ein
Lemma nicht gefunden); hier hat sie eine **plausible falsche Auskunft**
geliefert. Vergeben ist `wachen` B1 *keep watch · veles · veilles · vegli*.

In Kapitel 29 waren ausserdem **sechs von zehn** „unbelegt"-Meldungen falsch, in
Kapitel 28 drei von vier, in Kapitel 30 eine von drei — die Quote bleibt bei
etwa zwei Dritteln.

### Zwei Ausreisser im schon gebauten Bestand

Beide von Agenten gemeldet, beide beim Einsammeln behoben:

* **`Priester` stand in 27,16 franzoesisch als *sacrificateurs***, an den 22
  uebrigen Stellen des Buches und 640 im Gesamtbestand als *prêtres*. Genau ein
  Ausreisser, und genau in der Formulierung, die LSG an dieser Stelle waehlt.
* **`zur` trug in 16,3 die Reihe *a la · à la · alla*, obwohl `Welt` dort
  maskulin glossiert ist** (*mundo · monde · mondo*) — grammatisch falsch in
  drei Sprachen. 20,14 und 29,6 haben korrekt *al · au · al*.

### `Land`: der vierte Fund von `konsistenz.py`

Das Wort steht 98-mal im Buch mit der Glosse *land* und trug **zwei spanische
Reihen**: *país* (87 Belege) und *tierra* (11). Die elf verteilen sich auf
4,16 · 5,19 · 13,13 und acht Stellen in Kapitel 25 — sie folgen RV, das
durchgehend *tierra* schreibt. **Der Bestand und das Buch stehen auf *país***,
und `Erde` traegt *tierra*; die Doppelung war eine latente Kollision fuer jeden
Vers, in dem beide Woerter stehen. Alle elf sind angeglichen, dazu ein
franzoesisches *terre* in 4,16.

### Ein Homograph, den der Build meldet, und er ist richtig

**`hört auf` traegt zwei Lemmata**: `aufhören` A2 *ceases · cesa · cesse ·
cessa* (15,18 · 17,8) und `hören auf` B1 *listen to · escuchad · écoutez ·
ascoltate* (18,10 · 26,13 · 27,9 · 29,8). Dieselbe Bauform wie `rechten`/`recht`
und `meinen`/`mein` — kein Befund.

### Die Eigenpruefung: fuenf Befunde, und einmal null

Der Agent von Kapitel 29 hat **vier** Uneinheitlichkeiten gefunden, darunter
**`allen` vor `Völkern` in 29,14 und 29,18 mit zwei verschiedenen und in beiden
Faellen falschen Genera**; der von Kapitel 28 eine (`vor` spanisch einmal *ante*,
einmal *delante de*, in derselben Wendung `in Gegenwart von`). **Der Agent von
Kapitel 30 hat 63 mehrfach vorkommende Lemmata geprueft und nichts gefunden** —
das erste Mal seit Paket 4, dass die Eigenpruefung leer ausgeht.

### Befunde im Bestand

* **`nahekommen` und `nähern` fallen in allen vier Sprachen zusammen** und
  stehen in **30,21 dreimal im selben Vers**. Der Bestand hat fuer `nahekommen`
  **keine zweite Lesart**; die Ausweichung (*draw near · aproximarse ·
  s'avancer · accostarsi*) ist gepraegt, nicht entlehnt. Kandidat fuer eine
  korpusweite Trennung.
* **`zerbrechen` und `zerreißen` fallen franzoesisch zusammen** (*briser*) und
  stehen in 30,8 im selben Vers; `zerreißen` weicht auf *burst · romper ·
  rompre · rompere* aus. **Zweiter Fall nach 10,20**, in dem die Kleider-Lesart
  von `zerreißen` nicht passt (dort Zeltstricke, hier Fesseln).
* **`Wohl` (29,7) hat keine brauchbare zweite Bestandslesart** — die vorhandene
  ist *Blessed*. Neu gepraegt als *welfare · bienestar · bien-être · benessere*,
  weil `Wohl` und `gut` im selben Vers stehen.
* **`Abfall` (28,16) traegt die Jer-2,19-Lesart *apostasy***, obwohl **alle vier
  Ausgaben** die Rebellions-Lesart schreiben.
* **`seit alters her` ist ein eigenes Lemma neben `von alters her`** (7 Belege)
  — der Quelltext schreibt `seit`. Zusammenfuehrungskandidat, dieselbe Bauform
  wie `herbeiholen`/`herholen`.
* `führen` („eine Sache führen", 30,13), `pressen` (30,6), `berauben` (30,16),
  `voll` (29,10), `auftreten` (29,27), `legen` (29,26) und `schaffen` (28,13)
  haben im Bestand keine passende Lesart und sind nach den Ausgaben vergeben.

### Befunde in den Ausgaben

* **WEB liest `Joch` in 28,10 · 28,12 · 28,13 als *bar(s)*, in 28,2 · 28,4 ·
  28,11 · 28,14 als *yoke*** — dieselbe Ausgabe, zwei Woerter fuer dasselbe
  deutsche Wort. Durchgehend *yoke*, sonst zerfaellt das Zeichen aus Kapitel 27.
* **In 30,8 stehen die Possessiva der Ausgaben quer** („his yoke from off your
  neck"), der l1912mod hat durchgehend die 2. Person.
* **30,18 lesen die vier Ausgaben den zweiten Halbvers in vier Richtungen** —
  Numerus, Sachbegriff und Adverbial gehen auseinander; `angestammt` C1 ist
  deshalb frei gepraegt.
* **`Nehelam`**: alle vier Ausgaben schreiben das Gentiliz (*Nehelamite*), der
  deutsche Text macht daraus einen Ortsnamen („Schemaja **aus** Nehelam").
  Nach dem Deutschen als Ortsname gepraegt.
* **RIV schreibt `Hananja` durchgehend *Anania***, der Bestand *Hanania*
  (1Chr 3,19) — dem Bestand gefolgt.
* Sechs RIV-Anlautfehler im Paket (28,4 · 28,11 · 28,14 · 29,3 · 29,20 ·
  29,28), dazu zwei in Kapitel 30 mitten im Vers („per iacobbe", „egli ultimi
  giorni"). **Kapitel 30 ist nach dem strengen Muster fehlerfrei** — das sechste
  solche Kapitel.
* **RV1909mod siezt in 29 und 30, aber nicht in 28** — das erste Kapitel seit
  langem ohne die inzwischen zehnmal gemeldete *ustedes*-Beobachtung.

### `spricht der HERR`: Stand nach 30 Kapiteln

**105 `dit` zu 80 `parle`**. Kapitel 28 steht 1 : 5, Kapitel 29 10 : 7,
Kapitel 30 7 : 4.

### Neue Lemmata des Pakets (13)

`Asur` A1 · `seit alters her` C1 · `Elasa` A1 · `Gemarja` A1 · `Nehelam` A1 ·
`Halseisen` C1 *neck iron · argolla · carcan · collare di ferro* (vier Ausgaben,
drei Sachen) · `sich finden lassen` B2 · `braten lassen` B2 · `Wohl` B1
(zweite Lesart) · `kreidebleich` C1 *pale as chalk · pálidos como la tiza ·
pâles comme la craie · pallidi come il gesso* · `angestammt` C1 ·
`nahekommen lassen` B2 · `wütend` B2 (feminine Form nach `Sturm`).
