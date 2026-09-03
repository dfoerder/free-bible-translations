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


## 12. Paket 11 (Kap. 31 · 32 · 33) — das Formel-Paket, und das groesste des Buches

110 Verse, 3116 Eintraege, Versatz +0 ueberall. **49 Dubletten hatten eine
fertige Vorlage** — mehr als in jedem anderen Paket. `paketcheck.py` Abschnitt
A und C leer, 65 Zeilen in B ohne Befund; `qa`, `konvention` und `levelcheck`
ueber alle drei Kapitel ohne Treffer, `sweep` drei Fehlalarme,
`glosskollision.py` ein einziges inhaltliches Paar im ganzen Paket.

### Fuenf Fassungen der Botenformel, alle maschinell nachgerechnet

| Vers | Wortlaut | Vorlage | Ergebnis |
|---|---|---|---|
| **32,6** | `Das Wort des HERRN erging an mich` | 1,4 = 2,1 = 16,1 | **7 von 7 identisch** |
| **32,26** | `Da erging das Wort des HERRN an Jeremia` | 29,30 | **8 von 8 identisch** |
| **33,19 = 33,23** | `Das Wort des HERRN erging an Jeremia` | 1,4 | **7 von 7 untereinander**, pos 0-5 gleich mit 1,4 |
| **33,1** | `… erging zum zweiten Mal an Jeremia` | 13,3 | acht Felder gleich, einschliesslich `zum zweiten Mal` A2 |
| **32,1** | `Dies ist das Wort … im zehnten Jahr` | 30,1 = 11,1 + 25,1 | pos 0-9 gleich, Datierung nach 25,1 |

Damit sind die neun offenen Formelstellen des Buches (34,12 · 35,12 · 37,6 ·
42,7 · 43,8 und die Datierungen 35,1 · 36,1 · 49,34) vollstaendig vorbereitet.

### `Sieh, es kommt die Zeit`: vier Stellen, zwei Agenten, null Abweichungen

Die Formel steht dreimal in Kapitel 31 (27 · 31 · 38) und einmal in 33,14 —
also bei **zwei verschiedenen Agenten**. Beide haben 23,5 als Vorlage genommen
(die einzige Bestandsstelle ohne `Darum` davor), und die zehn Positionen sind
**ueber alle vier Stellen Feld fuer Feld identisch**. LSG schreibt an allen vier
Stellen `dit`.

### `Wachhof` — der Fall, fuer den Abschnitt A gebaut ist

Das Wort ist im Bestand unbelegt und steht in **32,2 · 32,8 · 32,12 und 33,1**,
also bei zwei Agenten. Sie haben es verschieden gepraegt:

    Kapitel 32   court of the guard · patio de la guardia · cour de la garde · cortile della guardia
    Kapitel 33   court of the guard · patio de la guardia · cour de la prison · cortile della prigione

**Die Ausgaben stehen zwei zu zwei**: WEB und RV schreiben die Wache, **LSG und
RIV schreiben das Gefaengnis**. Entschieden hat das deutsche Kompositum
(`Wache` + `Hof`, beide im Bestand) — dieselbe Regel wie bei `Volkstor`
(Paket 6) und `Scherbentor` (Paket 7). 33,1 ist angeglichen. Gefunden beim
Vergleich der beiden Berichte; `paketcheck.py` haette es ebenso gemeldet.

### Die Form-gegen-Lemma-Falle luegt zum zweiten Mal

Nach `wachst` (29,26, unter `wachsen` statt `wachen`) liefert `belegt.py` in
**32,8 fuer `Erbrecht` das Lemma `erbrechen`** — *vomit*, aus Jer 25,27.
Beide Male ist die Auskunft **plausibel und falsch**, nicht bloss leer.

Die Quote der falschen „unbelegt"-Meldungen bleibt hoch: **zehn von fuenfzehn**
in Kapitel 31, fuenf von acht in Kapitel 32. Darunter `Messschnur` (7 Belege),
`Ecktor`, `Rosstor`, `Kidron`, `Gareb`, `Urkunde`, `Abschrift`, `Vetter`.

**Neu ist die Falle an einem Mehrwort**: `fixgloss.py show "Bund brechen"` und
`"einen Bund brechen"` schweigen beide — das Bestandslemma heisst **`den Bund
brechen`** (11 Belege). Gefunden hat es `sweeplemma.py`; ohne den Lauf waere
31,32 ohne den Eintrag geblieben.

### `Hananel`: mein Hinweis war falsch, und beide Agenten haben es gemerkt

Die Vorbereitung fuehrte den Namen als unbelegt. Der Bestand hat **`Hananeel`
A1 *Hananel · Hananeel · Hananeel · Hananeel*** (Neh 3,1 · 12,39) mit genau der
Reihe, die die vier Ausgaben hier schreiben. Der l1912mod schreibt `Hananel` —
zwei deutsche Formen, also ein eigenes Lemma mit uebernommener Reihe, wie
`Paschhur`/`Pashur` in Paket 7. Der Agent von Kapitel 32 hat ausserdem
festgestellt, dass **`Hananel` in Kapitel 32 gar nicht vorkommt** (dort heisst
der Vetter `Hanamel`) — auch das stand falsch im Auftrag.

### Drei Vorlagen ausserhalb des Buches, die die Werkzeuge nicht nannten

* **31,21 ist wortgleich mit Sprüche 23,19** (`richte dein Herz auf`) — das
  Bestands-Mehrwort `richten auf` B2 hat dort zehn Belege. `sweep.py` und
  `sweeplemma.py` haben es gemeldet, die Vorbereitung nicht.
* **31,15 hat die Parallele in Matthaeus 2,18**, nicht in dem von
  `parallelen.py` als laengstem Block genannten Ps 77,3 — mit dem fertigen
  Mehrwort `sich trösten lassen` B2.
* **31,31-34 hat in Hebraeer 8,8-11 eine fast woertliche Vorlage.**

**Fuenfte Bestaetigung, dass der Werkzeugbefund eine untere Schranke ist.**

### Ein Befund ueber den Bestand, den nur diese Dublette zeigt

**Hebraeer 8 und Jeremia glossieren `das Haus Israel` verschieden**: dort steht
der blosse Name (*Israel*), hier durchgehend der Genitiv (*of Israel · de
Israel · d'Israël · d'Israele*, im Buch 12 : 0). Genommen ist die Buchmehrheit;
korpusweiter Angleichungskandidat.

### 31,29-30 ist die Vorlage fuer Hesekiel 18,2

Das Sprichwort von den `sauren Trauben` und den `stumpfen Zähnen` steht
vollstaendig in `ch31.json`. `sauer` und `Traube` sind Feld fuer Feld aus
Jes 5,2; **`stumpf` B2 ist eine zweite Lesart** — der Bestand hat nur die
Klingen-Lesart *blunt · desafilado · émoussé · smussato* (Ps 89,44), hier steht
*set on edge · con dentera · agacées · allegati*.

### Die Eigenpruefung faengt jetzt Fehlerklassen, die kein Lauf kennt

Der Agent von Kapitel 32 hat **fuenfzehn** Uneinheitlichkeiten gefunden,
darunter drei echte Fehler:

* **`ich` stand in 32,40 spanisch als *je*** — ein **franzoesisches Wort in der
  spanischen Spalte**. `qa.py` sieht das nicht, `glosskollision.py` auch nicht.
* `der` vor `Gott` stand in 32,27 italienisch als *l'* („l' Dio") statt *il*.
* `ein` vor `Herz` stand in 32,39 italienisch als *uno* statt *un*.

Kapitel 31 und 33 haben je drei weitere gefunden. **Die Wortklasse „falsche
Zielsprache" ist neu** und von keinem der sieben Pflichtlaeufe abgedeckt.

### Befunde im Bestand

* **`Dankopfer` (33,11)**: der Bestand steht 79 : 5 auf *peace offerings*, aber
  das sind die Opferordnungen von 3. Mose. Hier ist es das Dankopfer, und alle
  vier Ausgaben schreiben die Danksagung — genommen ist die vorhandene zweite
  Lesart *thank offerings*.
* **`gefangen` (32,2)**: die AT-Mehrheit ist *captive* (Kriegsgefangene), hier
  ist es die Haft. Genommen ist die einzige *imprisoned*-Reihe des Bestands, und
  die stammt aus **drei NT-Belegen** — wieder ein Fall, in dem im AT die
  NT-Lesart die richtige ist.
* **`am` in „der Sand am Meer" (33,22) traegt im Bestand drei unvereinbare
  Reihen** — Angleichungskandidat.
* **`Herr` weicht in 31,32 auf *master · dueño · maître · padrone* aus**, weil
  `HERR` im selben Vers steht; die Mehrheitsreihe waere spanisch und
  italienisch mit `SEÑOR`/`SIGNORE` kollidiert.
* `Bestimmung` (32,11), `teuer` (31,20), `umherziehen` (31,24), `Rat` (32,19),
  `aufrechterhalten` (33,25), `gesund machen` (33,6) und `stumpf` (31,29) sind
  sieben weitere Kandidaten fuer zweite Bestandslesarten.
* **`Machseja` faellt spanisch mit `Maaseja` zusammen** — RV schreibt beide
  Namen *Maasías*, WEB, LSG und RIV trennen sie. Der Ausgabe gefolgt; im Kapitel
  steht `Maaseja` nicht, also keine Kollisionsstelle.

### Befunde in den Ausgaben

* **RV1909mod liest in 31,31 „la casa de Jacob"**, wo der deutsche Text, WEB,
  LSG und RIV `Haus Israel` haben — der auffaelligste Textbefund des Pakets.
* **32,24: vier Ausgaben, vier Bilder fuer `Belagerungswälle`** — WEB *mounds*,
  **RV *arietes* (Rammboecke)**, LSG *terrasses*, RIV *opere d'assedio*.
* **32,20: die beiden deutschen Verben lesen alle vier Ausgaben verschieden, und
  keine zwei gleich.**
* **33,7 · 33,11 · 33,26: alle vier Ausgaben lesen „die Gefangenen
  zurückbringen"**, der l1912mod schreibt `das Schicksal wenden` — dem Bestand
  gefolgt, die Reihe steht seit 29,14 fest.
* Neun RIV-Anlautfehler im Paket, darunter zweimal `Anatot`/`abilonia` im selben
  Kapitel; **RIV schreibt in 32,7 „ad natoth" und in 32,8 korrekt „ad Anatoth"**.
* **RV1909mod siezt in allen drei Kapiteln** — elfte Meldung.

### `spricht der HERR`: Stand nach 33 Kapiteln

**121 `dit` zu 96 `parle`**. Kapitel 33 steht 3 : 7, Kapitel 32 3 : 6,
Kapitel 31 hat die Formel elfmal.

### Neue Lemmata des Pakets (27)

`Wachhof` C1 · `Hanamel` A1 · `Nerija` A1 (**gilt fuer 36,4 · 43,3 · 45,1 ·
51,59**) · `Machseja` A1 · `Kaufurkunde` C1 *deed of purchase · contrato de
venta · contrat d'acquisition · atto di compra* · `Vorkaufsrecht` C1 ·
`Erbrecht` C1 · `Lösungsrecht` C1 · `unterschreiben` B2 · `dazunehmen` B2 ·
`zukehren` B2 · `Gründung` B2 · `einsperren lassen` B2 · `Hananel` A1 ·
`Goa` A1 · `Wegzeichen` C1 · `Markierung` C1 · `betend` B2 · `entlangleiten`
C1 · `ausmessen` C1 · `ungezähmt` C1 · `Lieblingskind` C1 *darling child · niño
querido · enfant de mes délices · figlio prediletto* · `Wohnstatt` C1 ·
`Reigen` C1 · `sich wehren` B2 · `aufrechterhalten` B2 · `erwachsen lassen` B2.

## 13. Paket 12 (Kap. 34 · 35 · 36) — das Paket, in dem `paketcheck.py` Abschnitt A leer blieb

**73 Verse, 2158 Einzelwort- und 72 Mehrwort-Eintraege.** Buchstand: 36 von 52
Kapiteln, 928 Verse, 25 248 Eintraege.

`paketcheck.py` meldete **0 + 39 + 0** — **Abschnitt A war zum ersten Mal in
diesem Buch vollstaendig leer**: jedes neu gepraegte Lemma des Pakets traegt in
allen drei Kapiteln dieselbe Reihe, ohne dass die Agenten voneinander wussten.
Die 39 Faelle aus Abschnitt B waren bis auf einen Numerus, Tempus oder Genus.

### Die Formelketten — alle maschinell nachgerechnet

Das Paket schliesst die Botenformel des Buches ab. Sieben Ketten, jede Feld
fuer Feld verglichen, **null Abweichungen**:

    34,12  = 35,12 = 29,30 = 32,26          8 von 8 Feldern
    34,1   pos 0-9   = 30,1 = 11,1
    35,1   pos 0-9   = 30,1 = 11,1
    35,1   pos 10-20 = 1,3 pos 2-12         die Datierung, woertlich
    36,1   pos 1-10  = 25,1 pos 14-23       die Datierung
    36,1   pos 11-17 = 27,1 pos 13-19       `erging dieses Wort vom HERRN an`
    35,1   pos 13-20 = 36,1 pos 3-10        die beiden Datierungen gegeneinander

`34,12` und `35,12` sind bei **zwei Agenten ohne Absprache** identisch
zurueckgekommen. Damit stehen die Vorlagen fuer **37,6 · 42,7 · 43,8** fest;
**36,27** traegt zusaetzlich dieselbe Reihe **ohne** einleitendes `Da`.

Ein Befund an der Datierung: die engste Vorlage fuer `in der Zeit Jojakims, des
Sohnes Josias, des Koenigs von Juda` ist **nicht 25,1 oder 32,1, sondern 1,3** —
dort steht sie woertlich. Die Vorbereitungstabelle nannte sie nicht;
`parallelen.py` meldet den Elf-Token-Block.

### `Buchrolle` gegen `Rolle` — die Kollision steht im selben Vers

Beide Woerter stehen in **36,28 und 36,32 nebeneinander** („eine andere
Buchrolle … alle Worte der Rolle"), also musste getrennt werden:

    Buchrolle  C1  book scroll · rollo de libro · rouleau de livre · rotolo di libro
    Rolle      B1  scroll · rollo · rouleau · rotolo

Entschieden hat wieder das deutsche Kompositum — dieselbe Regel wie bei
`Volkstor` (Paket 6), `Scherbentor` (Paket 7) und `Wachhof` (Paket 11). WEB
schreibt in 36,2 und 36,4 selbst *a scroll of a book*, RIV *un rotolo da
scrivere*. `Buchrolle` steht elfmal, `Rolle` neunmal — die Auftragsangabe von
acht traf keines der beiden.

### `Hand` in `in die Hand geben` — eine buchweite Angleichung

`mehrwort.py` meldete nach dem Bau **13 Verdachtsfaelle**, zwoelf davon
`Hand` franzoesisch *mains*. Der Bestand ausserhalb Jeremias steht in genau
dieser Wendung **68 : 11 auf *main*** — das deutsche Wort ist Singular, nur die
franzoesische Wendung (*livrer entre les mains*) traegt den Plural. Das Buch war
darauf abgedriftet, weil die Vorgabe im Prompt seit Paket 7 *mains* verlangte.

Angeglichen sind **16 Eintraege** in acht Kapiteln — zwoelf innerhalb der
Wendungsspanne (20,4 · 20,5 · 29,21 · 32,3 · 32,25 · 32,28 · 32,36 · 32,43 ·
34,2 · 34,3 · 34,20 · 34,21) und vier deutsche Singulare ausserhalb jeder
Wendung (32,24 · 32,28 · 34,3 · 34,21). Die Wendung selbst behaelt *entre les
mains*. **`mehrwort.py` faellt damit von 13 auf 1**; der Rest (`Sicherheit` it
*sicuro* in *al sicuro*) ist richtig, das italienische Idiom enthaelt das Wort.

### Die Form-gegen-Lemma-Falle, dritter vorab gemeldeter Fall — bestaetigt

`Spalte` in 36,23 liefert bei `belegt.py` das Verb `spalten` B2 mit 13 Belegen
(*split · dividió · fendit · spaccò*) — plausibel und falsch, wie `wachst`
(29,26) und `Erbrecht` (32,8). Der Vers meint die Kolumnen der Schriftrolle; die
vier Ausgaben stehen 2 : 2 (RV *columnas*, RIV *colonne* gegen WEB *leaves*,
LSG *feuilles*), entschieden hat das deutsche Wort:

    Spalte  B2  columns · columnas · colonnes · colonne

**Kapitel 34 hat die Falle fuenfmal am Stueck ausgeloest**: alle vier
„unbelegten" Formen der Hinweisdatei waren falsch (`Bedingungen`→`Bedingung`,
`Kalbes`→`Kalb`, `beigetreten`→`beitreten`, `hindurchgegangen`→`hindurchgehen`),
dazu `Hofbeamter`. In Kapitel 35 waren **5 von 10** Meldungen falsch, in
Kapitel 36 **sechs von zwanzig** reine Formfallen. Zusammen der bisher
deutlichste Beleg, dass `hints.py` ohne `belegt.py` nicht zu gebrauchen ist.

### Was die Eigenpruefung fand, die kein Pflichtlauf sieht

Die Agenten haben ihre haeufigen Lemmata gegen sich selbst geprueft und vier
echte Uneinheitlichkeiten behoben, die alle sieben Laeufe passiert haetten:
`als` fr *lorsque*/*quand* (34,1 gegen 34,13) · `machen` es *hacer*/*convertir*
(34,17 gegen 34,22) · `zu` fr *à redevenir* mit doppeltem „re-" (34,11) ·
`seine` es *sus* vor einem Singular-Substantiv (36,31).

Beim Einsammeln kam **`Jahr` in 34,14** dazu, der einzige echte Fall aus
Abschnitt B: zwei Plurale **im selben Vers**, einer auf *ans*, einer auf
*années*. Das Buch trennt sauber nach Numerus — Singular *année* (14×), Plural
*ans* (6×) —, also ist *années* der Ausreisser. Korrigiert.

### Befunde im Bestand

* **`machen zu` B1 fehlt in 24,9 und 29,18**, steht aber in 25,9 und 25,18 bei
  identischer Bauform. Der belastbarste Nachtragskandidat des Pakets.
* **`der` vor `Gott Israels` traegt im Buch zwei italienische Reihen** — *il* an
  20 Stellen, ***l'*** an sieben (9,14 · 13,12 · 16,9 · 21,4 · 23,2 · 25,15 ·
  25,27). „l' Dio" ist falsches Italienisch; dieselbe Bauform wie der Fall 32,27
  aus Paket 11. **Angleichungskandidat fuer die sieben Stellen.**
* **`dem Land` steht 11 : 2** auf `the · el · le · il`; die zwei Ausreisser
  (24,10 · 25,5) haben spanisch *la* vor dem maskulinen *país*.
* **`Jaasanja`**: der Bestand fuehrt italienisch *Iaazania*, RIV schreibt an der
  Bestandsstelle (2Koen 25,23) selbst *Jaazania* — dasselbe *Ie-/Ia-*-Muster wie
  bei `Jechonja`/`Ieconia` aus Paket 8. Bestandsreihe genommen, Korrekturkandidat.
* **`Vorhof` C1 und `Hof` B1 tragen dieselbe Reihe** *courtyard · patio · cour ·
  cortile* und stehen in 36,10 und 36,20 — verschiedene Verse, nach der Regel
  also nicht aufgeloest, nur gemeldet.
* **`Fastentag` B2 (Jes 58,3) und `Fasttag`** sind zwei deutsche Woerter fuer
  dieselbe Sache. Zusammenfuehrungskandidat.
* **`ziehen` in `zur Rechenschaft ziehen` hat spanisch *traer*** gegen en
  *draw* / fr *tirer* / it *trarre* (29,32) — in sich schief.
  **Korrekturkandidat fuer 29,32**; in 36,31 kollidierte es und wich auf
  *tirar* aus.
* `weilen` C1, `Freilassung` B2 (ein einziger, neutestamentlicher Beleg),
  `zerschneiden` B2 (ein Beleg), `aehnlich` B1 (ein Beleg), `vorsetzen` B2 und
  `Raum` B1 sind sechs Kandidaten fuer zweite Bestandslesarten.
* **`Schreiber` B2 traegt en *scribe* neben romanisch *secretario · secrétaire ·
  segretario*.** Sieht uneinheitlich aus, ist gegen die Ausgaben aber richtig.
* **Level:** `neunt` ist A2 (nicht A1), `ganz` A2, `entzuenden` C1, `ab` als
  Verbpartikel A2 — alle vier von `levelcheck.py` gefunden.

### Befunde in den Ausgaben

* **RIV 36,1 hat einen echten Praepositionsfehler** — „questa parola fu rivolta
  **all'Eterno** a Geremia", richtig waere *dall'Eterno*. Anderer Bautyp als die
  bekannten Anlautfehler, und der erste seiner Art im Buch.
* **Kapitel 34 und 35 haben keinen einzigen RIV-Anlautfehler**, Kapitel 36
  gleich vier (`eremia` · `bdeel` · `oiakim` · `avide`). Damit sind acht der
  36 Kapitel anlautfehlerfrei.
* **RV 36,26 macht aus `dem Koenigssohn` einen Eigennamen** — „Jerameel hijo de
  **Hamelec**". Nach dem Deutschen glossiert.
* **RIV 36,26 schreibt „Sesaia" fuer `Seraja`**, wo die drei anderen Ausgaben
  den Namen richtig fuehren. RIV 34,22 hat „contro **i lei**" statt *di lei*.
* **34,3 lesen alle vier Ausgaben ganz anders als der l1912mod** („von Mund zu
  Mund reden" gegen `von Angesicht zu Angesicht gegenueberstehen`), **34,5**
  brennen sie Raeucherwerk, wo der deutsche Text nur `ein Feuer` hat, und
  **34,17** lesen sie den Schluss in vier verschiedene Richtungen.
* **RIV 36,8 laesst den Schlussteil aus** („nella casa dell'Eterno").
* **LSG 36,7 dreht das Subjekt um** — „l'Éternel écoutera-t-il leurs
  supplications", waehrend die drei anderen das Volk sein Flehen bringen lassen.
* **RV1909mod siezt in Kapitel 34 und 35** (zwoelfte Meldung), **in Kapitel 36
  erstmals seit langem nicht** — dort durchgehend *tú*.

### `spricht der HERR`: Stand nach 36 Kapiteln

Maschinell nachgezaehlt ueber alle 36 Kapitel: **137 `dit` zu 118 `parle`**.
Die bisher handgefuehrte Summe (121 : 96 nach 33 Kapiteln) war abgedriftet —
die Zaehlweise stimmt (Kap. 32 und 33 kommen exakt auf die notierten 3 : 6 und
3 : 7), nur die Fortschreibung hatte `parle` untergezaehlt. Kapitel 34 steht
3 : 5, Kapitel 35 1 : 4, Kapitel 36 0 : 2.

### Neue Lemmata des Pakets (18)

`Buchrolle` C1 · `Rolle` B1 · `Spalte` B2 · `Diktat` B2 *dictation · dictado ·
dictée · dettatura* · `diktieren` B2 · `Schreibermesser` C1 *penknife ·
cortaplumas · canif · temperino* · `Kohlenbecken` C1 *brazier · brasero ·
brasier · braciere* · `Winterhaus` C1 · `Fasttag` B2 · `eingeschraenkt` C1 ·
`Rechabiter` B2 *Rechabites · recabitas · Récabites · Recabiti* (nach der
Gentiliz-Bauform `Ammoniter`/`Moabiter`/`Chaldaeer`) · `Gottesmann` B2 *man of
God · hombre de Dios · homme de Dieu · uomo di Dio* · `Jehudi` A1 · `Kuschi` A1
· `Jirmeja` A1 (zweite deutsche Form neben `Jeremia`) · `Habazzinja` A1 ·
`Jigdalja` A1 · `Schelemja` A1 und `Jerachmeel` A1 (Reihen von `Selemja` bzw.
`Jerahmeel` uebernommen, wie `Paschhur`/`Pashur` und `Hananel`/`Hananeel`).

**Kapitel 34 hat kein einziges neues Lemma gebraucht** — jedes Wort hatte eine
Bestandsvorlage.

### Trennungen, die im Kapitel gehalten werden mussten

`Freiheit` B1 gegen `Freilassung` B2 (34,8 gegen 34,15/17) · `Sklave` gegen
`Sklavin`, das franzoesisch auf *servante* ausweicht (LSG schreibt es selbst so)
· `Becher` gegen `Schale` in **35,5 im selben Vers**, in allen vier Sprachen
getrennt, waehrend LSG die Zuordnung vertauscht · `sagen` it *parla* in 34,2
gegen `von` *di* · `damit` auf *in order that* gegen `sodass` in 34,9.

## 14. Paket 13 (Kap. 37 · 38 · 39) — das Paket, in dem die Vorbereitung widerlegt wurde

**67 Verse, 1721 Einzelwort- und 76 Mehrwort-Eintraege.** Buchstand: 39 von 52
Kapiteln, 995 Verse, 27 045 Eintraege.

`paketcheck.py` meldete **2 + 48 + 0**. Beide Faelle aus Abschnitt A liessen
sich an den Ausgaben entscheiden (s. u.), aus Abschnitt B war einer echt.

### Der Befund des Pakets: 2. Koenige 25 ist die Vorlage von Jeremia 39

**Die Vorbereitung hat das Gegenteil behauptet, und sie war falsch.** Ich hatte
in `prep13.md` geschrieben, 2Koen 25 sei „keine brauchbare Vorlage" — gestuetzt
auf **eine einzige** Aehnlichkeitszahl (0.35 fuer 39,5). Der Agent hat das
Kapitel trotzdem aufgeschlagen und **fuenf Verse woertlich** vorgefunden. Alle
fuenf sind nachgeprueft, jede Reihe steht dort:

    2Koen 25,6  → 39,5    `Urteil sprechen` B2  passed sentence · dictó sentencia ·
                          prononça la sentence · pronunciò la sentenza
                          dazu `Urteil` B1 es *sentencia* (nicht *juicio*)
    2Koen 25,7  → 39,6/7  `blenden` B2 · `Kette` B1 · die ganze Kausativklammer
    2Koen 25,11 → 39,9    `Rest` B1 · `Überläufer` C1 · `übrig` B1, und das
                          Vorbild `in die Verbannung führen` C1
    2Koen 25,12 → 39,10   `arm` A2 *poorest* · `zurücklassen` B2
    2Koen 25,21 → 39,6    `hinrichten lassen` B2 · `Hamat` A1

**Fuer Paket 18 (Kap. 52) heisst das: 2Koen 25 zuerst aufschlagen.** Kap. 52 hat
seine Dubletten in Jer 39 *und* in 2Koen 25; beide sind jetzt entschieden.

Die Lehre fuer die Vorbereitung: eine einzelne Aehnlichkeitszahl aus
`parallelen.py` traegt keine Negativaussage. Wo `PAKETE_JEREMIA.txt` eine
fremde Parallele nennt, gehoert sie in den Prompt, auch wenn das Werkzeug
schweigt.

### Abschnitt A — zwei Neupraegungen, beide an den Ausgaben entschieden

* **`Juchal`** — ch37 praegte *Jehucal · Jucal · Jucal · Jehucal*, ch38
  *Jucal* viermal. Die Ausgaben widersprechen **sich selbst**: WEB und RIV
  schreiben in 37,3 *Jehucal*, in 38,1 *Jucal*; RV und LSG beide Male *Jucal*.
  Das deutsche Wort ist an beiden Stellen `Juchal`, also **eine Reihe**.
  Genommen ist die an sechs der acht Ausgabenstellen belegte:
  `Juchal` A1 *Jucal · Jucal · Jucal · Jucal*.
* **`Benjamintor`** — ch37 *Benjamin Gate · Puerta de Benjamín*, ch38
  *gate of Benjamin · puerta de Benjamín*. **WEB schreibt an beiden Stellen
  „the gate of Benjamin"**, und die Bauform ist die von `Volkstor` C1
  (*gate of the people · puerta del pueblo*), nicht die von `Ecktor`/`Rosstor`
  (*Corner Gate*/*Horse Gate*). Genommen:
  `Benjamintor` C1 *gate of Benjamin · puerta de Benjamín · porte de Benjamin ·
  porta di Beniamino*.

### Abschnitt B — die aufgesogene Glosse in 39,8

Das Buch ist bei `in Brand setzen` an allen vier bisherigen Stellen (21,10 ·
32,29 · 34,2 · 34,22) **doppelt einheitlich**: die Wendung traegt
*prender fuego a · mettre le feu à · dare fuoco a*, und das Einzelwort `setzen`
traegt daneben *set · poner · mettre · mettere*. In **39,8** hatte das
Einzelwort die Glosse der Wendung aufgesogen (*prendieron · diedero*) — es
und it standen damit fuer sich genommen auf „nahmen"/„gaben". Auf die
Buchbindung angeglichen: *set · pusieron · mirent · misero*.

Dieselbe Fehlerklasse wie die `Hand`/*mains*-Angleichung aus Paket 12, nur
andersherum: dort sog das Einzelwort den **Numerus** der Wendung auf, hier ihr
**Lexem**.

**Die erste Passivfassung der Wendung** steht in 38,17 und 38,23 (`in Brand
gesetzt`) und weicht bewusst auf ein anderes Lexem aus — *set on fire ·
incendiada · brûlée · incendiata* —, weil das Passiv von *mettre le feu à*
im Franzoesischen und Spanischen unbrauchbar ist. Beide Stellen tragen
dieselbe Reihe; das Einzelwort `setzen` bleibt daneben *puesta · mise · messa*
und damit beim Buchlexem.

### Vier deutsche Woerter fuer die Haft, eines davon im selben Vers

Kapitel 37 stellt vier Woerter desselben Sachfelds nebeneinander, und zwei
davon **in 37,15 im selben Vers**:

    Gefängnis      B1  prison · cárcel · prison · prigione      37,4 · 37,15 · 37,18
    Kerker         C1  dungeon · calabozo · cachot · segreta    37,15
    Kellerverlies  C1  basement cell · celda del sótano ·
                       cellule souterraine · cella sotterranea  37,16
    Wachhof        C1  court of the guard · patio de la guardia ·
                       cour de la garde · cortile della guardia 37,21 (2×)

Die Kollision `Gefängnis` ↔ `Kerker` ist ueber die **vorhandene zweite
Bestandslesart** (Jes 42,7, *dungeon*) aufgeloest, nicht ueber eine
Neupraegung — der sauberste Fall dieser Art im Buch. `Kellerverlies` musste
dagegen gepraegt werden, weil **alle vier Ausgaben in 37,16 zwei Orte nennen**
(„the dungeon house, and into the cells"), wo der l1912mod ein Wort setzt.

### 38,18 und 38,23 — die paketinterne Dublette

Feld fuer Feld identisch zurueckgekommen, ohne Abgleich:
`du` · `selbst` B1 · `wirst` · `ihrer` (fr *leur*) · `Hand` (fr **Singular
*main***, nach der Paket-12-Regel) · `nicht` · `entkommen` B2 (= 34,3).

### Die Form-gegen-Lemma-Falle — drei von drei vorab gemeldet, alle bestaetigt

* **`Vertrauten` (38,22)** — `belegt.py` fuehrt an erster Stelle das Verb
  `vertrauen` (5× + 4× *trusted*); richtig ist das Substantiv `Vertrauter` C1
  (5 Belege, Ps 55/88, Jes 42,19, **Jer 13,21**).
* **`Aufstellung` (39,3)** — der einzige Beleg ist 2Mo 38,21 mit *inventory ·
  inventario · inventaire · inventario*, die Bestandsliste. Gemeint ist das
  Sich-Aufstellen; gepraegt als **zweite Lesart am selben Lemma**,
  `Aufstellung` B2 *position · posición · position · posizione*, dazu das
  Mehrwort `Aufstellung nehmen` B2.
* **`Stich` (38,22)** — nicht das Stechen. Der Bestand fuehrt das Wort nur als
  Teil dieser Redewendung, franzoesisch aber **in zwei Lesarten, die mit dem
  Verb korrelieren**: *plan* zu `im Stich lassen` = *abandonner* (3 Belege),
  *embarras* zu *laisser tomber* (2). Genommen ist die Mehrheitsseite.

**Die Trefferquote von `hints.py` ist weiter zu schlecht, um ihr zu glauben:**
Kapitel 37 **1 von 8** falsch, Kapitel 38 **9 von 16**, Kapitel 39 **3 von 12**.

### Zwei Namen, die einander aehneln — die Trennung hat gehalten

Der Bestand fuehrt **drei** Lemmata mit demselben Stamm: `Kuschi` A1
*of Cushi · de Cusi · de Cuschi · di Cusci* (der Personenname aus 36,14),
`Kuschit` **B2** *Cushite · cusita · Éthiopien · etiope* (die
Volkszugehoerigkeit, **in Jer 13,23 im selben Buch belegt**) und `Kuschiter`
B2 mit identischer Reihe (7 Belege, 2Sam 18). Beide Agenten haben unabhaengig
`Kuschit` genommen, Feld fuer Feld gleich mit 13,23. `Gedalja` steht in 38,1
und 39,14 fuer **zwei verschiedene Personen** und traegt in beiden Kapiteln
dieselbe Bestandsreihe.

### Befunde im Bestand

* **Der Artikel innerhalb von `in die Hand geben` ist korpusweit gespalten.**
  Nach der Paket-12-Angleichung steht in Jeremia 14× *les* + *main* („les
  main") und 1× *la* + *main* (21,7). Der uebrige Bestand steht **18× „les
  main", 10× „la main", 1× „les mains"** — die Paarung, die fuer sich genommen
  falsch aussieht, ist die Mehrheitsform des Korpus, und Jeremia stimmt in
  beiden Feldern mit ihr ueberein. **Der Widerspruch ist aelter und
  korpusweit, nicht von Paket 12 erzeugt**; ihn ueber 29 Stellen in vielen
  Buechern aufzuloesen ist eine eigene Entscheidung. Hier nur festgehalten.
* **`ergehen` hat im Bestand keine Perfektreihe** fuer die Botenformel. Fuer
  „war … ergangen" (39,15) ist sie stammtreu gebildet: `ergangen` C1
  *come · venido · venue · giunta*. **Vorlage fuer Kap. 52 und jede weitere
  Perfektfassung.**
* **`niederreissen` hat zwei italienische Reihen** — *demolirono* (2Chr 31,1,
  Jes 23,13) gegen *abbatterono* (2Chr 36,19). Angleichungskandidat.
* **`befehlen` hat zwei italienische Lexeme** — *ordinò* (79 Belege) gegen
  *comandato* (105); beide stehen jetzt im selben Kapitel (38,10 gegen 38,27),
  beide von RIV gestuetzt. Angleichungskandidat.
* **`durchs Schwert fallen` (Jes 3,25, einziger Beleg) traegt fr *sous le
  glaive***, waehrend `Schwert` im ganzen Bestand *épée* ist.
  **Korrekturkandidat fuer Jes 3,25.**
* **`So spricht …` am Versanfang steht im Buch 44× auf *Thus* und 4× auf *So*
  ** — 19,15 gehoert zu den vier Ausreissern. Angleichungskandidat.
* **`es geht jemandem gut` und `gut gehen` sind zwei Lemmata fuer dieselbe
  Sache** (Jer 5,28 gegen Jer 7,23 / 2Koen 25,24). Zusammenfuehrungskandidat,
  ebenso `Fastentag`/`Fasttag` aus Paket 12.
* **`Vornehmer` hat 12 Belege, nicht 2** — die Bindung ist viel fester, als die
  Vorbereitung angab. Ebenso `Zisterne` (6 Singular- + 4 Pluralbelege, nicht
  „einmal als Plural"), `Strick` (13 statt 2), `Kerker` (4 statt 3),
  `ueberlaufen` (6 statt 2).
* `festhalten`, `ausrichten`, `heraufziehen` und `bei` sind vier weitere
  Kandidaten fuer zweite Bestandslesarten.

### Befunde in den Ausgaben

* **RIV-Anlautfehler: neun im Paket** (37,11 `araone` · 37,14 `rrestò` ·
  37,20 `on` · 38,10 `eremia` · 38,25 `on` · 38,26 `ionathan` · 39,3 zweimal
  `amgar-nebu`/`abilonia` · 39,7 `abilonia`), dazu in 39,3 der Binnenfehler
  `capo de' agi` statt *magi* und in 39,16 `ed n quel giorno`.
* **WEB, LSG und RIV setzen 39,1 einen Satzteil voran** („When Jerusalem was
  taken"), den der deutsche Text und RV nicht haben — drei Ausgaben klammern
  39,1–2 dadurch als Einschub. Kein Versatz.
* **39,3 · 39,13: WEB und RV transliterieren die beiden Aemter als Eigennamen**
  („Rabsaris", „Rabmag"), LSG und RIV uebersetzen. Der deutsche Text hat zwei
  Komposita — nach ihm entschieden.
* **RV 38,28 hat einen Satzteil doppelt**, den keine andere Ausgabe und nicht
  der deutsche Text hat.
* **RIV 38,8 fehlt nichts, aber RV1909mod schreibt in 38,1 „Pasur"**, wo
  dieselbe Ausgabe in 20,1 · 20,3 · 20,6 · 21,1 „Pashur" hat — der Befund aus
  Paket 7, jetzt auch **buchintern**.
* **38,22: alle vier Ausgaben lesen „deine Fuesse sind im Schlamm versunken"**,
  der l1912mod schreibt `sie haben dich in den Schlamm geführt`; **LSG liest
  als einzige „par ceux qui t'annonçaient la paix"** statt `Deine engsten
  Vertrauten`.
* **37,12 stehen die Ausgaben 2 : 2 zum Sinn** — WEB und RIV lesen den
  Erbanteil, **RV und LSG die Flucht**; LSG laesst `Erbanteil` ganz weg.
* **RV1909mod siezt in Kapitel 37 viermal** (dreizehnte Meldung), in Kapitel 38
  genau **einmal** (38,5), in Kapitel 39 **gar nicht**.

### `spricht der HERR`: Stand nach 39 Kapiteln

Maschinell nachgezaehlt: **139 `dit` zu 124 `parle`**. Kapitel 37 steht 0 : 2,
Kapitel 38 0 : 3, Kapitel 39 2 : 1.

### Neue Lemmata des Pakets (26)

`Juchal` A1 · `Jirija` A1 · `Ebed-Melech` A1 · `Nergal-Sarezer` A1 ·
`Samgar-Nebo` A1 · `Sarsechim` A1 · `Nebuschasban` A1 · `Benjamintor` C1 ·
`Mitteltor` C1 *Middle Gate · puerta del Medio · porte du Milieu · porta di
Mezzo* · `Königsgarten` C1 *king's garden · huerto del rey · jardin du roi ·
giardino del re* · `Bäckergasse` C1 *bakers' street · calle de los panaderos ·
rue des boulangers · via dei panettieri* · `Kellerverlies` C1 · `Wachhabender`
C1 *captain of the guard · capitán de la guardia · commandant de la garde ·
capitano della guardia* · `Erbanteil` C1 (eigenes Lemma neben `Erbteil` C1,
Modell `Buchrolle`/`Rolle`) · `Oberkämmerer` C1 *chief chamberlain · jefe de
los chambelanes · chef des chambellans · capo dei ciambellani* · `Achsel` B2
*armpits · axilas · aisselles · ascelle* · `Gespräch` B1 · `Kampfeswille` C1
*will to fight · voluntad de combate · volonté de combattre · volontà di
combattere* · `mitspielen` B2 · `zuleide` B2 · `ergangen` C1 · Mehrwoerter:
`übel mitspielen` C1 · `Aufstellung nehmen` B2 · `zuleide tun` B2 ·
`blenden lassen` B2 · `in die Gefangenschaft führen` C1 · `in die Hand fallen`
B2.

Dazu **zwei zweite Bestandslesarten**: `Aufstellung` B2 (Position statt
Inventar) und `einbrechen` B2 (Mauerdurchbruch statt Einbruchsdiebstahl).

`Kampfeswille` ist der reinste Fall der Kompositum-Regel im Buch: **keine der
vier Ausgaben uebersetzt das Wort**, alle vier umschreiben es verschieden
(„weakens the hands of the men of war" · *desalienta a los soldados* · *il
décourage les hommes de guerre*). Entschieden hat allein das Deutsche.

### Ungenannte Vorlagen, die die Agenten selbst gefunden haben

**38,28 ist woertlich Josua 6,10 pos 17–22** (`bis zu dem Tag, an dem …`) und
**38,16 pos 29–34 woertlich Jeremia 11,21 pos 9–14** (`die dir nach dem Leben
trachten`) — beide von `vorbereitung.py` nicht gemeldet, beide Feld fuer Feld
uebernommen. Umgekehrt traegt **1Mo 37,24 fuer 38,6 nichts bei**: dort steht
`Grube`, nicht `Zisterne`, und `leer und ohne Wasser` statt `kein Wasser, nur
Schlamm`. Der Vorbereitungseintrag `39,3 ← 38,17` (Aehnlichkeit 0.19) ist ein
Rauschtreffer.

## 15. Paket 14 (Kap. 40 · 41 · 42) — die Gedalja-Erzaehlung, und wie oft die Vorbereitung irrt

**56 Verse, 1725 Einzelwort- und 60 Mehrwort-Eintraege.** Buchstand: 42 von 52
Kapiteln, 1051 Verse, 28 830 Eintraege.

`paketcheck.py` meldete nach vier Angleichungen **0 + 34 + 0**. Abschnitt A war
zum zweiten Mal im Buch von vornherein leer; Abschnitt C hatte zum ersten Mal
im Buch einen Treffer.

### 2. Koenige 25 hat diesmal von Anfang an im Prompt gestanden

Die Lehre aus Paket 13 ist umgesetzt worden, und sie hat getragen:
**2Koen 25,22–26 deckt die ganze Gedalja-Erzaehlung ab.** `vorbereitung.py`
meldet die Quelle von selbst (40,9 mit Aehnlichkeit **0.75**) — der Fehler in
Paket 13 lag nicht am Werkzeug, sondern an meiner Negativaussage aus einer
Einzelzahl.

Aus **2Koen 25,23** kommt die vollstaendige Namenreihe der Erzaehlung
(`Truppenführer` B2 *troop commanders · jefes de las tropas · chefs des troupes
· capi delle truppe`, `Mizpa`, `Jischmael`, `Netanja`, `Johanan`, `Kareach`,
`Seraja`, `Tanhumet`, `Netofa`, `Maachatiter`), aus **25,24** `gut gehen` A2,
aus **25,26** `sich fuerchten vor` B1. 2Koen 25,23 ist auch die Stelle, an der
`Truppenführer` zum ersten Mal steht — das Wortfeld dieser Erzaehlung haengt
an diesem einen Vers. (Die Angabe „je ein einziger Beleg" aus dem
Agentenbericht ist falsch: `Truppenführer` hat 8, `Elischama` 4. Siehe den
Nachtrag zur Belegzaehlung am Ende dieser Datei.)

Ein Agent hat den Umfang noch erweitert: **25,22 liefert 41,2 woertlich**, und
**25,25 deckt 41,1 + 41,2 + 41,3 zusammen ab**.

### Was die Agenten an meiner Vorbereitung berichtigt haben

Das Paket hat den bisher hoechsten Stand an widerlegten Prompt-Angaben, und
zwei davon waren echte Sachfehler:

* **`geritzt` (41,5) ist nicht neu.** Ich hatte es unter „wirklich neu"
  gefuehrt. Das Lemma heisst **`ritzen` C1** und steht **in Jer 16,6, im selben
  Buch**, fuer genau denselben Trauerritus. Wirklich neu war nur `abrasieren`.
* **Bei `Königstöchter` (41,10) habe ich auf die falsche Bestandsreihe
  gezeigt.** `belegt.py` fuehrt an erster Stelle Ps 45,10 *Kings' daughters ·
  Hijas de reyes* — das heisst „Toechter von Koenigen", nicht „die Toechter des
  Koenigs". Richtig ist die zweite Lesart (2Chr 22,11): `Königstochter` B2
  *king's daughters · hijas del rey · filles du roi · figlie del re*; alle vier
  Ausgaben bestaetigen sie.
* **Die Vorgabetabelle nannte fuer `Rest` die Minderheitslesart** (s. u.).
* **`Hand` fr Singular gilt nicht in 40,4** — dort steht der deutsche **Plural**
  `Händen`. Die Paket-12-Regel greift beim Singular in einer Wendung.
* **2Koen 25,24 ist nur in der Schlussklammer Vorlage von 40,9**; das
  Vorderstueck ist ein anderer Satz (`Habt keine Angst … untertan zu sein`
  gegen `Fürchtet euch nicht … zu dienen`).
* **`als` (zeitlich) kommt in Kap. 42 gar nicht vor** — die drei `als` dort sind
  das Rollen-`als` von `als Fremde`.
* **`Grimm` ist C2, nicht C1.** **`entschließen` (2 Belege), `ergießen`
  (3 + 5, darunter Jer 7,20 im selben Buch) und `bange sein` C1 sind belegt**,
  wo `hints.py` „unbelegt" meldete. Vier Zaehlangaben von mir waren zu niedrig:
  `restlich` 9 statt 4, `Erschlagener` 20 statt 13, `Vorrat` 26 statt 10,
  `Wunde` 34 statt 16.

Umgekehrt hat ein Agent **sieben Vorlagen benutzt, die `vorbereitung.py` nicht
meldet** (Jer 16,6 · 2Sam 19,1 · 1Mo 13,14 · 1Mo 19,1 · 1Mo 45,24 · 2Chr 16,14
· 2Koen 4,8), waehrend vier der gemeldeten reines Rauschen waren (41,6 ← Lk
22,40 · 41,7 ← 1Mo 24,54 · 41,13 ← 1Koen 18,39 · 41,14 ← Lk 18,43).

### `Rest` — eine Bedeutung, dreizehn Stellen, jetzt eine Reihe

Alle dreizehn `Rest`-Stellen des Buches meinen dasselbe: den ueberlebenden
Ueberrest eines Volkes. `Rest des Volkes` (39,9 · 41,10 · 41,16) ist derselbe
Gegenstand wie `dieser ganze Rest` (42,2) und `Rest aus Juda` (42,15 · 42,19).
Das Buch stand 10 : 3 auf *remnant · remanente · reste · resto*; die drei
Ausreisser trugen *rest · resto*, weil 39,9 der Reihe von **2Koen 25,11** folgt
und meine Vorgabetabelle diese dann fuer das ganze Paket wiederholt hat.

Angeglichen sind **39,9 · 41,10 · 41,16** auf die Buchreihe. Der Korpus fuehrt
beide Lesarten (31 *remnant* : 23 *rest*), sie sind also nicht falsch — aber
innerhalb eines Buches traegt eine Bedeutung eine Reihe. **2Koen 25,11 ist der
Angleichungskandidat.**

### Drei weitere Angleichungen beim Einsammeln

* **`wo` stand in ch42 auf B1**, im Korpus an allen **400** Stellen auf A1 —
  der erste Treffer in `paketcheck.py` Abschnitt C in diesem Buch. Korrigiert.
* **`samt`**: 42,1 trug fr *avec*, 41,7 *ainsi que*. Der Korpus steht 33 : 15
  fuer *ainsi que*. Angeglichen.
* **`zurück`**: 41,14 trug es *de vuelta*, 40,5 und 40,12 *atrás*. Der Korpus
  steht 316 : 53 fuer *atrás*. Angeglichen.

### Die Zwillingsstellen — vier Paare ueber die Kapitelgrenze

40,6 ↔ 41,1 · 40,11 ↔ 41,2 · 40,13 ↔ 41,11 · 40,16 ↔ 41,14, dazu 41,13 ↔ 42,8.
Drei Paare kamen Feld fuer Feld identisch zurueck. Zwei Punkte waren offen:

* **`einsetzen`** — 2Koen 25,22/23 fuehrt *designó · incaricò*, Jeremia selbst
  in 20,1 und 23,4 *puesto · posto*, franzoesisch beide *établi*. Die
  Buchbindung gewinnt; beide Agenten sind unabhaengig darauf gekommen.
  **Der Korpus fuehrt drei konkurrierende Reihen fuer denselben Satztyp** —
  Zusammenfuehrungskandidat.
* **`zu` vor dem Personennamen** — in 40,6 standen `zu` und `nach` **beide** auf
  fr *à*, eine unaufgeloeste Kollision im selben Vers. Der Agent fuer 41,1
  hatte sie gesehen und mit *auprès de* behoben. Die Ausgaben schreiben an den
  beiden Stellen verschieden (LSG *vers* in 40,6, *auprès de* in 41,1), aber
  der deutsche Satz ist identisch — 40,6 traegt jetzt die Reihe des Zwillings.

### Die Formelketten

**42,7** traegt die Botenformel **ohne** einleitendes `Da` und ist gegen
**36,27 pos 17–23** maschinell geprueft: **7 von 7 Feldern identisch**. Damit
ist auch **43,8** vorbereitet. **42,17 und 42,22** sind untereinander und gegen
**21,9 = 38,2** Feld fuer Feld gleich (`durch Schwert, Hunger und Pest
sterben`), ebenso `als Fremde wohnen` an drei Stellen. **40,1 pos 0–9** ist die
Reihe aus 30,1 = 11,1 = 35,1, zum vierten Mal unveraendert.

**42,18 zeigt, warum nach dem Deutschen entschieden wird**: der l1912mod hat
`Fluch · Entsetzen · Schwur · Schmach`, und **alle vier Ausgaben ordnen die
Glieder anders** — das erste Ausgabenglied (*execration*) entspricht dem
deutschen dritten, das dritte (*curse*) dem deutschen ersten. Die Bauform kommt
aus 24,9, die Glieder aus ihren eigenen Bestandsreihen.

### Kollisionen, die ohne Neupraegung aufgeloest wurden

* **40,12 `sehr` ↔ `viel`** (it *molto*): statt einer Erfindung hat der Agent
  **4Mo 32,1** aufgeschlagen, wo „sehr viel" woertlich steht, und beide
  Bestandsreihen uebernommen.
* **41,9 `Erschlagener` ↔ `erschlagen` im selben Vers**: das Verb ist mit ~135
  Belegen weit fester gebunden als das Substantiv (20), also weicht das
  Substantiv auf seine **vorhandene zweite Bestandslesart** aus (*slain
  persons*, 5Mo 21,1 ff.). Zusaetzlich steht `Leiche` B2 im selben Vers —
  drei Woerter desselben Feldes, drei Reihen.
* **41,10 `restlichen Rest` … `geblieben`**: drei Woerter derselben Familie in
  einem Vers, in allen vier Sprachen getrennt.
* **41,2 `bei` ↔ `mit`**: `bei` weicht auf **genau die Reihe aus, die 2Koen
  25,25 — die Vorlage dieses Verses — schon fuehrt**.
* **42,18 `werden` ↔ `ziehen`** (nur fr *allez*): `ziehen` weicht **in nur der
  einen Sprache** auf *partez* aus.

### Befunde im Bestand

* **`auch` hat im ganzen Bestand keine Modalpartikel-Lesart**, obwohl die
  Konstruktion „Weisst du auch …?" vorkommt (40,14). Kandidat fuer eine
  korpusweite zweite Lesart.
* **`Böse` hat im Buch zwoelf verschiedene Glossenreihen bei 25 Belegen**, B1
  und B2 gemischt. Aufraeumkandidat.
* **Jer 7,23 gibt dem Dummy-`es` italienisch *ci***, dasselbe Wort wie dem
  Dativ `euch`; in 42,6 waere daraus `es` = `uns` geworden. Dort steht deshalb
  die 1050-fach belegte Dummy-Reihe *it · ello · il · esso*. **7,23 ist der
  Angleichungskandidat.**
* **`einkehren` hat genau einen Beleg** (2Koen 4,8), **`nämlich` ist im Buch
  unbelegt** (korpusweit 61 : 45 zwischen *in fact* und *namely*),
  **`Erbarmen erweisen` gibt es nicht** als Mehrwort (`Gnade erweisen` B2 waere
  das Modell, aber fr *faire grâce* passt hier nicht).
* **`bringen` traegt in Kap. 42 zwei fr-Lexeme** — *apporter* (Korpusmehrheit,
  93 Belege) gegen *amener* (Jer 32,42, die einzige Buchstelle mit `über`).
  Verschiedene Verse, also nicht aufgeloest; Angleichungskandidat.
* **`Hoschaja` weicht franzoesisch vom Bestand ab**: `Hosaja` A1 fuehrt fr
  *Hoschaeja* (Neh 12,32), **LSG schreibt in Jer 42,1 und 43,2 beide Male
  „d'Hosée"**. Eigenes Lemma nach dem `Betlehem`-Modell; **gilt auch fuer
  43,2** im naechsten Paket.

### Befunde in den Ausgaben

* **RIV1927 hat in Kapitel 42 keinen einzigen Anlautfehler** — das erste
  Kapitel des Buches ohne einen, nachdem Paket 13 neun hatte. In Kap. 40 steht
  einer (`hedalia`), in Kap. 41 drei plus ein Binnenfehler (**`Shafam` statt
  `Shafan`** in 41,2).
* **RV1909mod siezt in Kapitel 42 in zwoelf von 22 Versen** — mit Abstand der
  hoechste Stand des Buches (Kap. 37 viermal, Kap. 38 einmal, Kap. 39 gar
  nicht, Kap. 40 dreimal, Kap. 41 einmal). Die tú-Anreden an Jeremia selbst
  sind korrekt Singular. Fuenfzehnte Meldung dieser Art.
* **WEB 41,9 ist verstuemmelt**: „(the same was who which Asa the king had
  made …)" — zwei Relativpronomen hintereinander.
* **LSG 42,13 verschiebt einen Hauptsatz ueber die Versgrenze**, RIV 42,8 und
  42,13 verschieben Redeeinleitungen in die Gegenrichtung. Kein Versatz.
* **RV1909mod 40,10 liest „el pan"** statt der Sommerfruechte, **41,12 „el gran
  estanque"** (Teich) statt der Wasser, **41,9 „a causa de Gedalías"** statt
  „zusammen mit".
* **41,17 stehen die Ausgaben 3 : 1** — WEB, RV und RIV transliterieren
  „Geruth Chimham" als Ortsnamen, **LSG uebersetzt „l'hôtellerie de Kimham"**,
  und der l1912mod schreibt `in der Herberge Kimhams`. Nach dem Deutschen
  entschieden.

### `spricht der HERR`: Stand nach 42 Kapiteln

**140 `dit` zu 127 `parle`**. **Kapitel 40 und 41 enthalten die Formel
ueberhaupt nicht** — die einzigen zwei Kapitel des Buches ohne sie. Kapitel 42
steht 1 : 3.

### Neue Lemmata des Pakets (10)

`Baalis` A1 · `Efai` A1 *of Ephai · de Efai · d'Éphaï · di Efai* · `Jesanja` A1
*Jezaniah · Jezanías · Jezania · Jezania* · `Hoschaja` A1 *of Hoshaiah · de
Osaías · d'Hosée · di Hosaia* · `Bascha` A1 *Baasha · Baasa · Baescha · Baasa*
· `Betlehem` A1 (eigenes Lemma neben `Bethlehem` A1, Reihe unveraendert —
Modell `Paschhur`/`Pashur`) · `abrasieren` B2 *shaved off · afeitado · rasé ·
raso* · `Posaunenklang` C1 *sound of the trumpet · sonido de trompeta · son de
la trompette · suono di tromba* · Mehrwoerter `hingehen lassen` B1 ·
`fortführen` B2.

Dazu **sieben zweite Lesarten an vorhandenen Lemmata**: `richtig` A2 *fitting*
· `auch` A1 *indeed* (Modalpartikel) · `ziehen` A2 *depart* · `liegen` A2
*lies* · `Erschlagener` B2 *slain persons* · `zurückholen` B2 *recovered* ·
`Schmach` C1 *reproach · oprobio* (die Minderheitslesart, weil der einzige
Jeremia-Beleg 23,40 sie traegt).

### Nachtrag zur `dit`/`parle`-Zaehlung

Der Agent fuer Kap. 45 hat eine Differenz von eins zu meinem Zaehler gemeldet
und damit einen Fehler im **Kriterium** aufgedeckt, nicht in den Daten. Ich
hatte alle Eintraege mit Lemma `sprechen` und fr *dit*/*parle* gezaehlt; das
fasst **34,6** mit ein, wo `sprach` steht — das schlichte Verb („und sprach
alle diese Worte zu Zedekia"), nicht die Botenformel.

Das richtige Kriterium ist die **Form `spricht`**. Damit lauten die Staende:
**133 : 107** nach 33 Kapiteln · **137 : 118** nach 36 · **139 : 124** nach 39
· **140 : 127** nach 42. Kapitel 34 steht 3 : 5, nicht 4 : 5. Die Abschnitte
13 bis 15 sind entsprechend korrigiert; die Zahlen bis Kapitel 33 waren nicht
betroffen, weil `sprach` erst in 34,6 vorkommt.

### Nachtrag: `belegt.py` zaehlt die Wortform, nicht das Lemma

Der Agent fuer Kap. 43 hat gemeldet, `Steinsäule` habe **6** Belege und nicht
den einen, den meine Vorgabetabelle nannte. Er hat recht, und der Fehler ist
systematisch: **`belegt.py <Wort>` zaehlt die uebergebene Wortform.**
`Steinsäule` (Singular) steht einmal, `Steinsäulen` fuenfmal — zusammen sechs.
Ich habe die Formzahl als Lemmazahl in die Vorgabetabellen geschrieben, seit
mehreren Paketen.

Nachgezaehlt, welche „duenn gebunden"-Angaben davon betroffen waren:

    Steinsäule       1 → 6      (Plural `Steinsäulen` 5×)
    Flüchtling       1 → 5      (Plural `Flüchtlinge` 4×)
    Truppenführer    1 → 8      (aus einem Agentenbericht uebernommen)
    Elischama        1 → 4      (ebenso)

Wirklich an einem einzigen Beleg haengen von den genannten nur
**`Tachpanhes`** (Jer 2,16), **`Himmelskönigin`** (Jer 7,18), **`Noph`**,
**`Patros`** und **`Lehmboden`** (2Chr 4,17) — bei diesen fuenf ist die
Formzahl zufaellig auch die Lemmazahl.

**Fuer die restlichen Pakete:** in der Vorgabetabelle nur Zahlen nennen, die
ueber alle Flexionsformen geprueft sind, oder gar keine. Eine zu niedrige
Belegzahl im Prompt laedt den Agenten dazu ein, eine feste Bindung fuer
verhandelbar zu halten.

## 16. Paket 15 (Kap. 43 · 44 · 45) — das Paket, das die Vorbereitung gepruefte

**48 Verse, 1474 Einzelwort- und 59 Mehrwort-Eintraege.** Buchstand: 45 von 52
Kapiteln, 1099 Verse, 30 363 Eintraege.

`paketcheck.py` meldete **0 + 18 + 0** — Abschnitt A und C beide leer, und
Abschnitt B war mit 18 der kleinste des Buches. Das lag an der Lage des
Pakets: `vorbereitung.py` fand **19 fertige Vorlagen und keine einzige
paketinterne Dublette**, Kapitel 44 allein vierzehn Vorlagen aus Jeremia
selbst. Es wurde weniger gepraegt als nachgeschlagen.

### 43,8 schliesst die Botenformel des Buches ab

Vorlage ist **33,19** (Aehnlichkeit 0.88), die Fassung mit **Subjekt voran** —
nicht die Verb-Zweit-Fassung von 42,7. pos 0–6 Feld fuer Feld identisch;
43,8 haengt `in Tachpanhes` an. Damit sind alle Fassungen der Formel im Buch
entschieden: mit `Da` (29,30 = 32,26 = 34,12 = 35,12 = 37,6), ohne `Da` und
verb-zweit (36,27 = 42,7), und mit Subjekt voran (33,19 = 43,8).

### Zwei Fehler in der Vorbereitung, die Lemmata und Level gekostet haetten

* **„45,4 ← 1,10 = 24,6 = 42,10" stimmt fuer den Sinn, nicht fuer zwei der
  vier Woerter.** Der l1912mod schreibt `gebaut` und `gepflanzt` — die drei
  genannten Vorlagen fuehren dort `aufbauen` B1 und `einpflanzen` B2. Richtig
  ist **31,28** (`bauen` A2, `pflanzen` B1), fuer die 1.-Sg.-Formen
  **Jes 5,5**. Waere die Angabe befolgt worden, staenden dort **zwei falsche
  Lemmata und zwei falsche Level**.
* **`Seufzen` (45,3) war im Prompt nur als Formfalle angekuendigt.**
  Tatsaechlich ist **Ps 6,7 die woertliche Vorlage des halben Verses** — fuenf
  von fuenf Positionen uebernommen. `vorbereitung.py` hatte die Stelle
  gemeldet; ich hatte sie im Prompt zur blossen Lemma-Warnung verkleinert.

Dazu die ueblichen Zahlkorrekturen: `Tachpanhes` steht **drei**mal, nicht vier;
`ergießen` ist belegt (5, darunter **Jer 7,20 und 42,18 im selben Buch**);
`überheblich` hat 20 Belege, und sein einziger franzoesischer Ausreisser ist
**Jes 10,12** (*orgueilleux* gegen 19× *arrogant*); `als` (zeitlich) kommt in
Kap. 44 **gar nicht** vor; die fuenf Verben aus 43,3, die ich als moeglicherweise
neu gefuehrt hatte, sind alle belegt.

### `dì` gegen `di'` — die Ausgabe widerspricht der Bestandsreihe

Der Agent fuer 43,10 loeste die Kollision `sag` ↔ `von` (it *di*) ueber die
vorhandene Bestandslesart **`dì`** aus Jer 25,28 auf. Beim Einsammeln zeigte
sich, dass diese Lesart selbst der Fehler ist:

* Das Buch steht **23 : 2** auf `di'`; die zwei Ausreisser sind 25,27 und 25,28.
* **`dì` heisst im Italienischen „Tag"**; der Imperativ von *dire* ist `di'`.
* **RIV1927 schreibt an beiden Stellen selbst `di'`** — in 43,10 („E di’ loro")
  und in 25,28 („di’ loro"). Die Ausgabe widerspricht der Reihe an ihrem
  eigenen Ort.
* Die Kollision, die vermieden werden sollte, toleriert das Buch ohnehin
  zweimal (14,17 · 22,2), und `di'` und `di` sind verschiedene Zeichenfolgen.

Korrigiert sind **43,10 und die beiden Altstellen 25,27 · 25,28**.

### `belegt.py` zaehlt die Wortform — der Fehler war meiner

Der Agent fuer Kap. 43 meldete, `Steinsäule` habe **6** Belege statt des einen
aus meiner Vorgabetabelle. Der Agent fuer Kap. 44 meldete dasselbe fuer
`Flüchtling` (**5** statt 1). Beide haben recht, und die Ursache ist
systematisch — sie steht im **Nachtrag zur Belegzaehlung** am Ende dieser
Datei. Kurz: `belegt.py <Wort>` zaehlt die uebergebene **Form**, nicht das
Lemma, und ich habe die Formzahl als Lemmazahl in die Prompts geschrieben.
Betroffen waren `Steinsäule` (1→6), `Flüchtling` (1→5), `Truppenführer` (1→8)
und `Elischama` (1→4).

### Zwei Vorlagen, die kein Werkzeug nannte

**Jer 6,13** liefert `vom Kleinsten bis zum Größten` fuer 44,12 einschliesslich
des Bestands-Mehrworts `bis zu` A2 — ohne sie waere der Eintrag liegengeblieben.
**Ps 6,7** siehe oben. Umgekehrt hat `sweep.py` in 44,22 das Bestands-Mehrwort
**`werden zu` A2** gefunden, das der Prompt nicht kannte; der Agent hat es auch
auf 44,6 angewandt. Folge: das `zur` dieser beiden Stellen traegt **nicht** die
Fluchreihe *as*, sondern *into · en · en · in* (Reihe aus 4,26) — die
Fluchglieder in 44,22 bleiben davon unberuehrt.

### Die Fluchglieder halten ueber vier Stellen

42,18 (Paket 14) · 44,8 · 44,12 · 44,22, maschinell gegeneinander geprueft,
jedes wiederkehrende Glied mit **einer** Reihe. `Schmach` C1 traegt weiter die
**Minderheitslesart** des Bestands (*reproach · oprobio*, 8 gegen 22), weil der
einzige Jeremia-Beleg (23,40) sie fuehrt.

Ebenso gehalten: die **zwei `in die Hand geben` in 44,30** (Hophra und Zedekia
im selben Vers), beide mit `Hand` fr **Singular *main*** nach der
Paket-12-Regel und den Reihen aus 22,25.

### `gut gehen` — die Regel hat sich bewaehrt

In Paket 14 galt `gut gehen` A2 fuer 40,9 und 42,6, weil beides **Nebensaetze**
sind. Fuer **44,17**, einen **Hauptsatz**, war `es geht jemandem gut` B1
vorgegeben — der Agent hat es bestaetigt und mit der Bauform von Jer 5,28
umgesetzt (`parts` Verb + Dummy-`es` + `gut`, Dativpronomen aussen). Die
Dreiteilung des Bestands bleibt Zusammenfuehrungskandidat, aber die
Verteilungsregel steht.

### Befunde im Bestand

* **`Einwohner` (18 Belege) und `Bewohner` (12) tragen im Buch die identische
  Reihe** *inhabitants · habitantes · habitants · abitanti*. In Kap. 44 stehen
  sie in verschiedenen Versen. Trennungs- oder Zusammenfuehrungskandidat.
* **`Feuer` A1 und `Brand` C1 tragen dieselbe Reihe** *fire · fuego · feu ·
  fuoco* (43,12 gegen 43,13). Im Jeremia-Text stehen die beiden staendig
  nebeneinander — buchweiter Aufraeumkandidat.
* **`Ödnis` C1 (neu) deckt sich mit `Verwüstung` C1.** Die beiden stehen
  nirgends zusammen; Zusammenfuehrungskandidat. `Öde` C1 schied aus, weil
  seine Reihe im selben Vers mit `Wüste` kollidiert.
* **`in` (in den Städten) ↔ `auf` (auf den Straßen) kollidiert 4 von 4 in
  44,17 und 44,21** — aber **die Vorlage Jer 7,17 traegt dieselbe Doppelung**.
  Eine Aufloesung haette drei Verse von ihrer Vorlage getrennt. Buchweiter
  Angleichungskandidat.
* **`Jojakim` traegt it *di Ioiakim*, waehrend RIV1927 in allen 35 Belegen
  „Joiakim" schreibt.** Betrifft 14 Stellen. Angleichungskandidat.
* **`alles Fleisch` hat im Bestand zwei Lemmata bei identischen Glossen** —
  `alles` (u. a. Jer 25,31) gegen `all` (Jes 49,26 u. a.). Aufraeumkandidat.
* **Die `niederreißen`-Reihe von Jes 5,5 ist in sich zeitinkonsistent**:
  en *tear down* (Praesens) gegen es/fr/it Futur.
* `herbeiholen` B2 (zwei Reihen), `Entsetzen` (6:1, Ausreisser 29,18) und
  `Ordnung` (zwei Reihen im Buch) sind drei weitere Kandidaten.

### Befunde in den Ausgaben

* **RIV1927 hat in Kap. 42, 43 und 45 keinen einzigen Anlautfehler** — drei
  von vier Kapiteln in Folge sauber, nachdem Paket 13 neun hatte. Kap. 44 hat
  zwei (`erusalemme`, `iuda`).
* **RV1909mod siezt in Kap. 44 in 12 von 30 Versen** — gleichauf mit dem
  Hoechststand aus Kap. 42 —, in **Kap. 43 dagegen in genau einem von 13** und
  in **Kap. 45 in keinem einzigen**. Sechzehnte bis achtzehnte Meldung.
* **RIV 43,13 uebersetzt `Bet-Schemesch`** als „le statue del tempio del sole",
  3 : 1 gegen die drei anderen. Derselbe Fall wie „Geruth Chimham" in 41,17,
  nur mit umgekehrten Rollen — dort uebersetzte LSG allein.
* **WEB 44,19 weicht inhaltlich ab** („to worship her" statt „die ihr Bild
  darstellen"); **nur RIV stuetzt den deutschen Text** („focacce a sua
  immagine"). Danach entschieden → `darstellen` B2 *depict*, eine zweite
  Lesart, weil der einzige Bestandsbeleg (Mk 4,30) *describe* ist.
* **LSG weicht dreimal ab**: 43,9/43,10 ersetzt es die Adressaten durch „les
  Juifs", 44,25/44,26 verschiebt es die Satzgrenze, und in **45,4 schreibt es
  „son tapis"** (Teppich) fuer `Prunkzelt`, wo die drei anderen das Zelt haben.
* **RV 45,4 laesst `Sieh` aus** und ersetzt beide finiten Verben durch
  *voy a* + Infinitiv.

### `spricht der HERR`: Stand nach 45 Kapiteln

**143 `dit` zu 135 `parle`** (Kriterium: Form `spricht`, siehe den Nachtrag zur
Zaehlung). Kapitel 43 steht 0 : 1, Kapitel 44 2 : 5, Kapitel 45 1 : 2.
Nachgerechnet wurde ausserdem: **„So spricht" steht im Buch 75-mal auf
*Thus · Así · Ainsi · Così* gegen 8-mal *So*.**

### Neue Lemmata des Pakets (7)

`Prunkzelt` C1 *royal pavilion · pabellón real · pavillon royal · padiglione
reale* · `Hophra` A1 *Hophra · Hofra · Hophra · Hofra* · `Ödnis` C1
*desolation · desolación · désolation · desolazione* · `Opfern` B2
(nominalisierter Infinitiv, Modell `Tun`/`Handeln`/`Wissen`) · `erstreben` C1
*seek · buscar · rechercher · cercare* · Mehrwoerter `sich überziehen` C1 und
`aufhetzen` C1.

Dazu **drei zweite Lesarten**: `überziehen` C1 *wrap in* (dritte Lesart neben
*overlay* und *overran*) · `darstellen` B2 *depict* · `vollbringen` *done*.

`erstreben` steht in 45,5 zweimal, einmal als verneinter Imperativ. Das Muster
es-Subjunktiv / it-Infinitiv dafuer ist nicht erfunden, sondern das des
Bestands (**Spr 30,6** fuehrt `hinzufügen` genau so).

### Nachtrag: `levelcheck.py 24` ohne Kapitelnummer prueft nichts

Der Agent fuer Kap. 46 hat es gemeldet, und der Quelltext bestaetigt es:

    nr, kaps = int(argv[0]), argv[1:]
    ...
    for kap in kaps:

**`levelcheck.py 24` setzt `kaps = []`** — die Schleife laeuft null Mal und das
Skript meldet unweigerlich „0 Abweichungen". Genau so stand der Aufruf in
meiner Sammelkette und in mehreren Agentenprompts.

Nachgeprueft: der Lauf ueber **alle 47 Kapitel** (`levelcheck.py 24 1 2 … 47`)
meldet ebenfalls **0 Abweichungen** — es ist also **kein Schaden entstanden**.
Die Agenten haben das Skript in ihren eigenen Laeufen ueberwiegend mit
Kapitelnummer aufgerufen und die Faelle dort gefunden; in Kap. 46 war
`levelcheck.py 24 46` sogar der einzige Lauf, der den `türmen`-Fehler sah.

**Fuer die restlichen Pakete:** in der Sammelkette und in jedem Prompt
`levelcheck.py 24 <kapitel>` schreiben. Ein Pflichtlauf, der bei falschem
Aufruf still „sauber" meldet, ist schlimmer als keiner.

## 17. Paket 16 (Kap. 46 · 47 · 48) — die Voelkersprueche, und ein Pflichtlauf, der nichts prueft

**82 Verse, 1831 Einzelwort- und 97 Mehrwort-Eintraege.** Buchstand: 48 von 52
Kapiteln, 1181 Verse, 32 291 Eintraege.

`paketcheck.py` meldete nach zwei Angleichungen **1 + 36 + 0**. Der eine Fall
in Abschnitt A ist kein Fehler, sondern die Kollisionsregel (s. u.).

### Der Werkzeugbefund: `levelcheck.py 24` prueft nichts

Der Agent fuer Kap. 46 hat es gefunden, der Quelltext bestaetigt es —
Einzelheiten im **Nachtrag zu `levelcheck.py`** am Ende dieser Datei. Kurz:
ohne Kapitelnummer laeuft die Schleife null Mal und das Skript meldet
unweigerlich „0 Abweichungen". Genau so stand der Aufruf in meiner
Sammelkette.

Der Lauf ueber **alle 48 Kapitel** meldet ebenfalls 0 — **es ist kein Schaden
entstanden**. Aber der erste richtige Aufruf im Einsammeln dieses Pakets fand
sofort einen echten Fall: **48,44 `gefangen` stand als `fangen` B2, waehrend
der Korpus `fangen` mit 61 Belegen auf A2 fuehrt.** Korrigiert.

### Jeremia 48 arbeitet Jesaja 15–16 um — die Vorbereitung hatte recht

Der Nachweis, den ich vor dem Prompt gefuehrt hatte, traegt: die seltensten
Ortsnamen des Kapitels haben je **einen** Bestandsbeleg, und er steht in
Jesaja (`Luhit` · `Horonajim` · `Eglat-Schelischija` → Jes 15,5, `Nimrim` →
15,6, `Kir-Heres` → 16,11). Der Agent hat **Jes 15,4–7 · 16,6 · 16,8 · 16,10 ·
16,11 · 24,17 · 24,18 · 47,1** und **4Mo 21,28** benutzt und Feld fuer Feld
uebernommen.

Vier meiner Zuordnungen trugen aber weniger weit, als ich geschrieben hatte:

* **„48,31 · 36 ← Jes 16,7 · 16,11" gilt nur fuer den Namen.** Jes 16,7 hat
  `jammern` und `Rosinenkuchen`, Jer 48,31 `wehklagen`/`aufschreien`/`seufzen`;
  Jes 16,11 hat `Innerstes`+`Harfe`, Jer 48,36 `Herz`+`Flöte`.
* **„48,18 ← Jes 47,1" traegt nur pos 0–1 und 8–12** — `Einwohnerin` steht in
  Jes 47,1 gar nicht (dort `Jungfrau`, `Tochter`).
* **„48,37 ← Jes 15,2–3" traegt nur `Bart` und `Trauergewand`.** Die naehere
  Vorlage fuer `stutzen` ist **Jer 9,25, im selben Buch**.
* **Eine Vorlage fehlte: 4Mo 21,29 ist die Vorlage von 48,46.** Wichtig fuer
  spaeter — **dort fuehrt der l1912mod das Lemma `Kamos`, in Jeremia
  `Kemosch`**. Zwei deutsche Formen, zwei Lemmata.

### Sechs Stolz-Woerter in einem Vers — geloest

48,29/30 haeuft `Stolz` · `stolz` · `Hochmut` · `Überheblichkeit` ·
`Anmaßung` · `Arroganz` · `Übermut` · `Prahlen`, und die Bestandsreihen
ueberschnitten einander bereits untereinander. Ergebnis: **acht Woerter, acht
Reihen in allen vier Sprachen**, und nur **zwei** Bestandsreihen mussten
bewegt werden — beide nur im Kollisionsvers:

    Stolz            B1  pride · orgullo · orgueil · orgoglio          (Bestand)
    stolz            B1  proud · orgulloso · fier · orgoglioso         (Bestand)
    Hochmut          C1  arrogance · soberbia · **hauteur** · superbia
    Überheblichkeit  C1  **haughtiness** · arrogancia · arrogance · arroganza
    Anmaßung         C1  presumption · altivez · présomption · presunzione   (neu)
    Arroganz         C1  conceit · altanería · suffisance · alterigia        (neu)
    Übermut          C1  insolence · insolencia · insolence · insolenza (Bestand)
    Prahlen          C1  boasting · jactancia · vantardise · vanteria   (Bestand)

`Hochmut` fr weicht auf **LSGs eigenes Wort an dieser Zeile** aus („Sa
hauteur") — nicht auf die Bestandsvariante *arrogance*, die mit
`Überheblichkeit` kollidiert haette. `Überheblichkeit` en weicht auf seine
**zweite Bestandslesart** aus (*haughtiness*, Jes 9,8). Die beiden
Neupraegungen nehmen, was die Ausgaben an dieser Stelle liefern (RV
*altivez*/*altanería*, RIV *alterigia*) und fuellen den Rest in die Luecken.

### Die `Grauen`-Falle, und wie ich mir selbst widersprochen habe

Fuer 48,43/44 hatte ich sauber getrennt: **Jes 24,17 schreibt `Schrecken`,
Jer 48,43 aber `Grauen`** — die Reihe darf nicht uebertragen werden. Der Agent
hat es eingehalten (`Grauen` C1 *horror · horror · effroi · orrore* aus
Jer 20,4; `Grube` und `Falle` woertlich aus Jesaja).

**Im selben Prompt habe ich dann fuer 46,5 behauptet, `Schrecken ringsum`
stehe im Buch schon in 6,25 · 20,3 · 20,10** — und an zwei der drei Stellen
steht **`Grauen`** (20,3 `Grauen-ringsum`, 20,10 `Grauen ringsum`), also genau
das Wort, das ich zwei Absaetze weiter oben davon getrennt hatte. Der Agent
fuer Kap. 46 hat es gemeldet und `Schrecken` B2 aus 6,25 mit `ringsum` B2 aus
20,10 zusammengesetzt.

### 50,1 haengt an 46,13, nicht an 46,1

Meine Handnotiz sagte „46,1 ist die Vorlage fuer 50,1". Beide Agenten haben
den Quelltext aufgeschlagen und widersprochen; `vorbereitung.py` hatte es
selbst richtig gemeldet (prep16: „46,13 ← Jeremia 50,1"):

    46,1   Dies ist das Wort **des HERRN, das an** den Propheten Jeremia … **erging**
    46,13  Dies ist das Wort, **das der HERR zum** Propheten Jeremia … **sprach**
    50,1   Dies ist das Wort, **das der HERR durch** den Propheten Jeremia … **sprach**

Mit 46,1 teilt 50,1 nur die vier Anfangswoerter. Die vollstaendige
46,13-Reihe liegt in `scratchpad/jeremia/NOTIZ_PAKET17.md`.

**49,34 dagegen traegt die 46,1-Bauform** und ist bis pos 12 woertlich gleich
mit **47,1** — vom Agenten fuer Kap. 47 am Quelltext geprueft.

### `Einwohnerin` — Abschnitt A meldet die Regel, nicht ihren Bruch

Das neue Lemma traegt in 48,18/19 *inhabitant · habitante · habitante ·
abitante* und in **46,19** *resident · residente · résidente · residente*.
Das ist kein Widerspruch: **46,19 traegt `Einwohnerin` und `Bewohner` im
selben Vers**, 48,18/19 nicht. Die Abweichung ist die kollisionslokale
Aufloesung. Angeglichen wurde nur das Level (C1 → **B2**, wie `Einwohner` und
`Bewohner`).

Damit ist der Befund aus Paket 15 zu einem **Dreierfeld** gewachsen:
`Bewohner` (98 Belege), `Einwohner` (44) und jetzt `Einwohnerin` tragen
dieselbe Reihe. In Kap. 47,2 hat `Einwohner` seinerseits auf *residents*
ausweichen muessen. Der Aufraeumbedarf ist damit dringlicher als vorher.

### Zwei Zweitschreibungen, die neu gepraegt werden mussten

**`Kaftor` und `Anakiter` sind im Bestand unbelegt** — meine Vorgabetabelle
fuehrte beide als „alle im Bestand". Der Bestand schreibt `Kaphthor`
(5Mo 2,23) und `Enakiter` (8 Belege); der l1912mod schreibt in Jeremia und
Amos anders als in den aelteren Buechern. Neue Lemmata mit der jeweiligen
Bestandsreihe — Modell `Paschhur`/`Pashur`, `Betlehem`/`Bethlehem`.
Angleichungskandidaten.

### Die Form-gegen-Lemma-Falle: acht Faelle in einem Kapitel

In Kap. 48 hatten **acht der 28 „unbelegten" Formen aus `hints48.txt` ein
belegtes Lemma** (`Schlucht` C1 · `stutzen` B2 (Jer 9,25) · `hereinbrechen`
B2 (vier Jeremia-Belege) · `leeren` B2 · `kahlscheren` C1 · `lärmend` C1 ·
`schütteln` B1 · `hinabsinken` B2). In Kap. 47 kam `kahlscheren` dazu, in
Kap. 46 der schwerste Fall:

**`türmen` (46,7/46,8) ist belegt, aber `belegt.py türmen` findet es nicht** —
es meldet `Türmen` → Lemma `Turm`. Das **Verb** `türmen` B2 hat einen Beleg,
**2Mo 15,8**, in genau demselben Bild („durch deinen Atem tuermten sich die
Wasser auf"). Der Agent hatte zuerst nach den Ausgaben gepraegt; **nur
`levelcheck.py 24 46` hat den Fehler gesehen** — der Lauf, den mein
Standardaufruf entwertet hatte.

### Befunde im Bestand

* **`zerschlagen` C1 und `zerschmettern` C1 tragen die identische Reihe**
  *shattered · destrozado · brisé · frantumato*; ebenso **`Gericht` B2 und
  `Urteil` B1** (*judgment · juicio · jugement · giudizio*) und **`Grauen` C1
  und `Entsetzen` C1** franzoesisch beide *effroi*. Drei Trennungskandidaten.
* **`Aufstieg` (neu, B2) deckt sich vollstaendig mit `Steige` C1** (Jes 15,5)
  — zwei deutsche Woerter, dieselbe Sache, **und ein Level-Widerspruch**.
* **`des Königs von Babel` laeuft im Buch 50 : 3 auseinander** — drei Stellen
  (22,25 · 26,18 · 44,30) glossieren das `des` als *the · el · le · il* statt
  *of the · del · du · del*. Angleichungskandidat.
* **`Kir-Heres`, `Kirjatajim`, `Bozra`, `Jaser` und `Eglat-Schelischija`
  weichen in der Bestandsreihe von der Schreibung der Ausgaben ab** — fuenf
  Angleichungskandidaten derselben Bauform wie `Jechonja`.
* **`Winzer` B2**: der einzige Bestandsbeleg (Jer 6,9) ist der Traubenleser,
  in 48,12 lesen alle vier Ausgaben „Umschuetter". Dem Bestand gefolgt, weil
  das deutsche Wort dasselbe ist.
* **`in seiner Mitte` (46,21) fand nur `sweeplemma.py`** — `konvention.py` und
  `sweep.py` suchen die Wortform, und die steht im Bestand nur einmal
  (Jes 29,23). Neunter Beleg fuer die Pflichtstellung dieses Laufs.

### Befunde in den Ausgaben

* **RIV1927: ein Anlautfehler in Kap. 46, einer in Kap. 47, vier in Kap. 48.**
  Dazu zwei fehlende Satzgrenzen (46,19 · 47,7) und in 48,44 `ai laccio`.
* **RV1909mod siezt in Kap. 48 in 10 von 47 Versen — und zwar in jedem
  einzelnen Imperativvers.** In Kap. 46 vier von 28, in Kap. 47 einer von
  sieben. Neunzehnte Meldung.
* **46,20 `Bremse` — nur RIV stuetzt den deutschen Text** („viene un tafano");
  die drei anderen lesen den Zerstoerer. **46,22 `Zischen` — keine Ausgabe
  hat es**, alle vier schreiben „Stimme". **48,1 `die Festung` — alle vier
  transliterieren „Misgab"**, der l1912mod uebersetzt. Jedes Mal nach dem
  deutschen Text glossiert.
* **RV 48,41 laesst `Kerijot` aus**, **LSG 48,29 hat fuer `Arroganz` kein
  Substantiv** („et son cœur altier"), **WEB 48,30 liest `Übermut` als
  „his wrath"** — alle drei allein gegen die uebrigen.
* **47,5 ist 3 : 1 gespalten**: WEB, RV und LSG lesen *Tal*, nur **RIV** hat
  den Volksnamen — und der l1912mod folgt RIV. Der deutsche Text hat also nur
  eine Ausgabe hinter sich.
* **47,7 wechseln LSG und RIV in die 3. Person**, wo Deutsch, WEB und RV das
  Schwert durchgehend anreden.

### `spricht der HERR`: Stand nach 48 Kapiteln

**158 `dit` zu 138 `parle`**. Die Voelkersprueche kehren das Muster um:
**Kapitel 46 steht 6 : 0** — das erste Kapitel des Buches, in dem LSG
ausschliesslich `dit` schreibt — und Kapitel 48 steht 9 : 2. Kapitel 47 hat
die Formel einmal, auf `parle`.

### Neue Lemmata des Pakets (44)

**Kap. 46 (21):** `Tartsche` C1 *buckler · broquel · **targe** · targa* ·
`Schneller` B1 · `kopflos` C1 · `Heilmittel` B2 · `Wehr` C1 · `entscheidend`
B2 · `Einwohnerin` **B2** · `Bremse` C1 *gadfly · tábano · taon · tafano* ·
`Söldner` B2 · `Zischen` C1 · `fliehend` B1 · `undurchdringlich` C1 · `Puter`
B2 · `Theben` A1 · Mehrwoerter `anschirren` C1 · `sich türmen` B2 · `sich satt
fressen` C1 · `sich voll trinken` C1 · `sich zur Wehr stellen` C1 ·
`stolpern lassen` B2.

Bei **`Tartsche`** liefern drei Ausgaben ein eigenes Lexem, LSG paraphrasiert.
Weil `Schild` fest an *bouclier* gebunden ist, ist fuer Franzoesisch **`targe`**
genommen — das echte Wort fuer diesen Schildtyp und der Kognat zu it *targa*.
**Die einzige Stelle des Pakets, an der gegen keine Ausgabe, sondern in eine
Luecke hinein entschieden wurde.**

**Kap. 47 (5):** `Rasseln` C1 *rattling · estrépito · cliquetis · strepito* ·
`Dröhnen` C1 *rumbling · fragor · grondement · fragore* · `Kaftor` A1 ·
`Anakiter` B2 · Mehrwort `zurückfahren` B2. — Die drei Geraeuschwoerter in
47,3 (`Getöse` · `Rasseln` · `Dröhnen`) sind in allen vier Sprachen getrennt,
**obwohl RIV und LSG dieselben Woerter in umgekehrter Zuordnung verwenden**;
der Agent ist der Bestandsbindung von `Getöse` gefolgt und hat das als
bewussten Zug gemeldet.

**Kap. 48 (25):** `Anmaßung` C1 · `Arroganz` C1 · `Aufstieg` B2 · `bekunden`
C1 · `Fliehender` B2 · `Entkommene` C1 · `Flüchtender` B2 · `erstürmen` C1 ·
`umschütten` C1 · `zerritzen` C1 · `wehklagen` C1 · `Obsternte` B2 ·
`Madmen` A1 · `Mefaat` A1 · `Kerijot` A1 · `Bet-Diblatajim` A1 · `Bet-Gamul`
A1 · `Bet-Meon` A1 · Mehrwoerter `Mitleid bekunden` C1 · `heraneilen` C1 ·
`heranschweben` C1 · `versiegen lassen` C1 · `über … hinaus` B2 · `so weit` B2.

Zu **`Madmen`**: alle vier Ausgaben schreiben den Namen, die
„Carcass"-Ausnahme greift nicht — genommen ist *Madmen · Madmén · Madmen ·
Madmen*, **obwohl die englische Schreibung mit dem Gemeinwort
„madmen" zusammenfaellt.** Zur Kenntnis fuer eine spaetere Durchsicht.

### Nachtrag: zwei weitere Aufrufe, die nicht so heissen, wie ich sie schreibe

Nach `levelcheck.py` hat der Agent fuer Kap. 50 einen zweiten gefunden:

    glosskollision.py --datei <buchNr> <kapitel> <datei.json>

**`--datei` verlangt die Datei zwingend als dritten Positionsparameter.** In
meiner Prompt-Kette stand `glosskollision.py --datei 24 50` ohne Datei. Der
Unterschied zu `levelcheck.py` ist wichtig: dieser Aufruf **stuerzt laut ab**
(`IndexError: list index out of range`) und kann deshalb nichts verstecken —
`levelcheck.py 24` dagegen meldete still „0 Abweichungen".

**Und die `Hand`-Regel war zu kurz formuliert.** Ich habe seit Paket 12
geschrieben: „`Hand` traegt franzoesisch Singular *main*". Richtig ist:

> **Das deutsche Singular `Hand` traegt fr *main*, auch innerhalb einer
> Wendung, deren franzoesische Fassung den Plural fuehrt.
> Der deutsche Plural `Hände`/`Händen` traegt *mains*** — im Korpus an
> **allen 322 Stellen**, ohne eine einzige Ausnahme.

Zwei Agenten haben die Verkuerzung unabhaengig gemeldet (Kap. 40 in Paket 14,
Kap. 50 in Paket 17). In den Daten ist dadurch nichts falsch geworden; beide
haben richtig entschieden und die Regel berichtigt statt sie zu befolgen.

## 18. Paket 17 (Kap. 49 · 50 · 51) — das dublettendichteste Paket, und was die Kapitelnummer wert ist

**149 Verse, 3673 Einzelwort- und 155 Mehrwort-Eintraege.** Buchstand: 51 von
52 Kapiteln, 1330 Verse, 36 120 Eintraege. Nur Kapitel 52 fehlt noch.

`paketcheck.py` meldete **0 + 111 + 0** — **Abschnitt A und C beide leer**, bei
149 Versen und sieben paketinternen Paaren. Abschnitt B ist mit 111 der
groesste des Buches, was bei drei langen Kapiteln zu erwarten war.

### Was der richtige `levelcheck`-Aufruf sofort einbrachte

Nach dem Befund aus Paket 16 trug jeder Prompt die Kapitelnummer. Das Ergebnis
ist der beste Beleg dafuer, wie teuer der stille Fehlaufruf war:

    Kap. 49   0 Levelfehler
    Kap. 50   6 Levelfehler   (`fangen` A2 · `darum` B1 · `stark` A1 · `fest` A2 …)
    Kap. 51  17 Levelfehler   (`ganz` A2 · `fallen` A1 · `sondern` B1 · `winden` C1 ·
                               `erfüllen` B2 · `denken` A1 …)

**Dreiundzwanzig echte Fehler in einem Paket**, alle von einem Lauf gefunden,
der vorher immer „0 Abweichungen" gemeldet hatte. Der nachgeholte Lauf ueber
alle 51 Kapitel meldet weiterhin null — die frueheren Pakete sind sauber, weil
die Agenten den Aufruf ueberwiegend selbst richtig geschrieben haben.

### Der groesste woertliche Block des Buches: 51,15–19 ← 10,12–16

Maschinell Position fuer Position nachgerechnet: **10,13 = 51,16 (32
Eintraege) · 10,14 = 51,17 (27) · 10,15 = 51,18 (17) · 10,16 = 51,19 (29)**,
alle vier `identisch = True`. **51,15 ← 10,12** ist bis auf das eine Wort
`aber` gleich (21 Eintraege, ab pos 1 Versatz −1). Kapitel 10 ist seit Paket 4
fertig; nichts davon wurde neu entschieden.

`51,52 ← 48,12` reicht **bis pos 11**, nicht nur bis pos 10 wie im Prompt
angegeben — 48,12 pos 11 ist ebenfalls `ich`.

### Die sieben paketinternen Paare — alle feldgleich

Der Agent fuer Kap. 49 hat die Nachbardatei selbst gelesen und drei Felder
angeglichen; vier Fragen blieben offen und sind beim Einsammeln am Bestand
entschieden worden:

    49,19 pos 4  `der` en   → *who*        (Korpus 1562 : 305 : 71)
    49,19 pos 24 `den` es   → *a aquel*    (Korpus `aquel` 68 : `al` 23)
    49,19 pos 28 `darüber`  → *dessus* / *sopra di essa*  (16 bzw. 7 gegen je 3)
    49,20/30 `fassen`       → *taken · tomado · prise · preso*  (Korpus 15 : 0 fuer *formed*)
    50,45 `über`            → die Kollisionsaufloesung aus 49,20

Danach im Schlussteil von 49,20/50,45 noch fuenf Felder, alle an den
Bestandszahlen entschieden (`wahrhaftig` es *ciertamente*, `selbst` es
*incluso* 41:15, `klein` en *least* 6:1) — bis auf eines, das umgekehrt lief:
**`über` nach `entsetzen` traegt fr *de* und it *di*** (Korpus 2:1), und
*s'épouvanter **sur*** waere ohnehin kein Franzoesisch.

**Ergebnis: 49,19 = 50,44 null Abweichungen ueber alle 45 Eintraege**,
49,20/50,45 null im gemeinsamen Teil, 49,26 ↔ 50,30 feldgleich,
49,18 ↔ 50,40 feldgleich.

Der letzte Zwilling, **50,23 ↔ 51,41**, hatte vier Abweichungen und einen
strukturellen Unterschied. Zwei der vier waren echte Fehler in 51,41:
**`den Völkern` stand spanisch als *las* und italienisch als *le***, obwohl
*pueblos* und *popoli* maskulin sind. Und **das Einzelwort `geworden` hatte die
Glosse seiner Wendung aufgesogen** (*convertido* statt *vuelto*, Korpus 136) —
derselbe Fall wie `setzen` in 39,8 aus Paket 13. Der strukturelle Unterschied:
51,41 fuehrte das Bestands-Mehrwort **`werden zu`** (33 Korpusverse), 50,23
nicht; es ist mit `parts` [11,13,15] nachgetragen.

### Die Kollisionsregel, zweimal richtig angewandt und einmal begruendet ausgesetzt

Der Agent fuer Kap. 49 hat **`fern` in 49,39 bewusst auf *lontano*
zurueckgesetzt**, obwohl 48,47 dort *remoto* traegt — weil das *remoto* eine
**kollisionslokale** Ausweichung gegen `weit` im selben Vers war und 49,39
kein `weit` enthaelt. Dieselbe Regel auf `Hochmut` (49,16, zurueck auf
*orgueil* statt des 48,29-*hauteur*) und auf `ewig` (49,33) angewandt.

Bei **`höhnen` in 49,17 hat er sie ausdruecklich nicht angewandt** und
begruendet, warum: der Bestand steht dort **1 : 1** (Ps 73,8 gegen Jer 19,8),
und **alle vier Ausgaben lesen an beiden Stellen etwas Drittes** („zischen"),
helfen also nicht. **Bei einem Patt entscheidet der buchinterne Zwilling.**
Das ist die praeziseste Formulierung der Regel, die das Buch bisher hat.

### Zwei weitere Zweitschreibungen — die Reihe wird laenger

* **`Teman` ist unbelegt**, der Bestand fuehrt `Theman` A1 (11 Belege).
* **`Ben-Hadad` (49,27) ist unbelegt**, der Bestand fuehrt `Benhadad` A1
  (27 Belege) — **vom Prompt nicht genannt, vom Agenten gefunden.**
* **`Aschkenas` (51,27) ist keine Neupraegung**: der Bestand fuehrt
  **`Askenas` A1** (1Mo 10,3 · 1Chr 1,6). Auch das gegen den Prompt.

Damit steht die Reihe bei sieben: `Paschhur`/`Pashur` · `Betlehem`/`Bethlehem`
· `Hananel`/`Hananeel` · `Kaftor`/`Kaphthor` · `Anakiter`/`Enakiter` ·
`Teman`/`Theman` · `Ben-Hadad`/`Benhadad` · `Aschkenas`/`Askenas`. **Der
l1912mod modernisiert Eigennamen in Jeremia systematisch anders als in den
aelteren Buechern** — das ist kein Einzelfall mehr, sondern eine Eigenschaft
der Ausgabe.

### Die Form-gegen-Lemma-Falle erreicht ihren Hoechststand

    Kap. 49   11 von 17 „unbelegten" Formen hatten ein belegtes Lemma
    Kap. 50   12 von 27
    Kap. 51   23 von 40   ← ueber die Haelfte

In Kapitel 51 waren von vierzig Meldungen **dreiundzwanzig** falsch, darunter
`Chaldäa`, `Heiligtum`, `Getöse`, `verschonen`, `schärfen`, `vorlesen`.
`hints.py` ist in diesem Register nicht mehr als ein Anfangsverdacht.

Ein Fund, den **kein** Werkzeug meldet: **`wie von Sinnen` C1 ist ein
Bestands-Mehrwort** (2Koen 9,20) samt der Zerlegung `von` = *out of* und
`Sinn` B1 = *his senses*. Der Agent hat es nur gefunden, weil er die
Belegstelle von `Sinn` aufgeschlagen hat.

### Befunde im Bestand

* **`Rache` B2 und `Vergeltung` C1 fallen in es/fr/it vollstaendig zusammen**
  (*venganza · vengeance · vendetta*) — von zwei Agenten unabhaengig gemeldet.
  Vierter Fall der Bauart aus Paket 16.
* **`wüst` B2 und `öde` C1 tragen dieselbe Reihe**, zusammen mit
  `Ödnis`/`Verwüstung` aus Paket 15 ein **Viererfeld mit Level-Widerspruch**.
* **`Kornspeicher` (neu) und `Kornhaus` C1**, **`fortschleppen` (neu) und
  `fortschleifen` C1**, **`herunterstürzen` (neu) und `hinunterstürzen` B2**,
  **`Übergang` (neu) und `Furt` C1** — vier neue Wortpaare derselben Art.
  Sie stehen nirgends im selben Vers, sind also nicht aufzuloesen, aber die
  Liste der Zusammenfuehrungskandidaten waechst mit jedem Paket.
* **`Über` als Spruchueberschrift laeuft auseinander**: 46,2 *Concerning ·
  Acerca de · Sur*, 48,1 *About · Sobre · Au sujet de*. Kap. 49 hat die
  Ueberschrift viermal und folgt 48,1. **Angleichungskandidat fuer 46,2.**
* **46,13 pos 4 `das` traegt fr *qui* in einem Objektrelativsatz**, wo LSG
  selbst *que* schreibt. Korrekturkandidat; 37,2 und 50,1 machen es richtig.
* **46,10 glossiert `Herrn` klein**, waehrend die Korpusmehrheit (646 Belege)
  gross fuehrt. Angleichungskandidat innerhalb des Buches.
* **`Trinkgelage` ist nur scheinbar belegt**: ein einziger Beleg (Gal 5,21) in
  der NT-Lasterlisten-Lesart. Ein Beleg ist keine Bindung — der Agent hat eine
  zweite Lesart gepraegt statt die Lasterliste zu uebernehmen.

### Befunde in den Ausgaben

* **RIV1927 hat in Kapitel 51 sieben Fehler**, darunter einen neuen Bautyp:
  **51,7 „han bevuto ***el*** suo vino" — ein spanischer Artikel im
  italienischen Text.** `RIV_ANLAUTFEHLER.md` fuehrt diese Klasse noch nicht.
  In Kap. 49 genau einer, in Kap. 50 keiner.
* **RV1909mod siezt in allen drei Kapiteln durchgehend in den Imperativversen**
  — Kap. 49 sieben Verse, Kap. 50 alle, Kap. 51 mindestens dreizehn.
  Zwanzigste Meldung; gefolgt ist ueberall dem Bestand.
* **51,1 `Leb-Kamai`: nur WEB transliteriert**, LSG liest „la Chaldée", RV und
  RIV paraphrasieren. Nach dem deutschen Text als Name gepraegt.
* **51,2 `Worfler` steht 2 : 2** — RV *aventadores* und LSG *vanneurs* gegen
  WEB *strangers* und RIV *stranieri*.
* **49,19/50,44 `wer fordert mich heraus`: vier Ausgaben, vier Bilder**, keine
  liest „herausfordern". Entschieden hat die Bestandsbindung.
* **49,25 kehrt LSG die Aussage um** („Elle **n'est pas** abandonnée").
* **50,21 uebersetzt LSG beide Eigennamen** („le pays doublement rebelle"),
  die drei anderen transliterieren — franzoesisch musste fuer `Meratajim` und
  `Pekod` in eine Luecke hinein gepraegt werden.

### `spricht der HERR`: Stand nach 51 Kapiteln

**188 `dit` zu 149 `parle`.** Kapitel 49 ist das erste des Buches, in dem die
Verteilung **rein syntaktisch** ist: alle fuenf `parle` stehen an
`So spricht`-Stellen, alle vierzehn `dit` an der eingeschobenen Formel. Kapitel
50 (8 : 2) und 51 (8 : 4) folgen demselben Muster.

### Neue Lemmata des Pakets (35)

**Kap. 49 (5):** `Tochterstadt` C1 · `Nachlesen` C1 · `herunterstürzen` B2 ·
`Nachbarstadt` C1 · `fortschleppen` C1. Dazu die Zweitschreibungen `Teman` und
`Ben-Hadad` und zwei zweite Lesarten (`besetzen` *occupy*, `was` *Why*).

**Kap. 50 (10):** `Merodach` A1 · `Leitbock` C1 *he-goats · machos cabríos ·
boucs · capri* (**alle vier Ausgaben glossieren nur „Bock"** — das „Leit-" hat
keine) · `herumspringen` B2 · `dreschend` C1 · `aufscheuchen` C1 ·
`Meratajim` A1 · `Pekod` A1 · `Kornspeicher` C1 · `Nachbarstadt` C1 ·
`fortschleppen` C1.

**Kap. 51 (20):** `Leb-Kamai` A1 · `Minni` A1 · `Aschkenas` A1 ·
`zerstörerisch` C1 · `Worfler` C2 · `Durchbohrter` C1 · `verwitwet` C1 ·
`Siegeslied` C1 · `Fahrer` B2 · `Zugtier` B2 · `Übergang` B2 · `Schreck` B2 ·
`festtreten` B2 · `Köstlichkeit` B2 · `Löwenjunges` B2 · `zottig` C1 ·
`Reisemarschall` C1 *quartermaster · jefe de intendencia · chambellan ·
ciambellano* · Mehrwoerter `herabwälzen` B2 · `heranziehen lassen` B2 ·
`sich auf die Lauer legen` C1. Dazu **neun zweite Lesarten**.

`Schreck` B2 ist bewusst gegen `Schrecken`, `Entsetzen` und `Grauen` abgesetzt
— vier deutsche Woerter desselben Feldes, vier Reihen.

## 19. Paket 18 (Kap. 52) — der geschichtliche Anhang, und das Buch ist fertig

**34 Verse, 817 Einzelwort- und 35 Mehrwort-Eintraege.**

**Jeremia ist vollstaendig: 52 Kapitel, 1364 Verse, 36 972 Eintraege,
3123 verschiedene Lemmata, 1452 Mehrwoerter.** `validate.py` rechnet die
35 638 Tokens der Paketplanung Zeichen fuer Zeichen nach: 35 520 Einzeleintraege
plus 118 alleinstehende Satzzeichen, **0 Befunde**.

### Die Warnung, die diesmal in die andere Richtung ging

`vorbereitung.py` meldet fuer Kap. 52 Aehnlichkeiten bis **0.96** (52,1 ←
2Koen 24,18) und **0.95** (52,32 ← 2Koen 25,28). Ich habe **alle fuenfzehn
Paare vor dem Prompt Zeichen fuer Zeichen verglichen: kein einziges ist
identisch.** Der l1912mod hat Jeremia und 2. Koenige unabhaengig voneinander
modernisiert — `Streitmacht` gegen `Heer`, `Tempel` gegen `Haus des HERRN`,
`fahrbare Kesselwagen` gegen `Gestelle`, `Befehlshaber` gegen `der Oberste der
Leibwache`. **52,7 weicht sogar im Inhalt ab**: dort fliehen die Soldaten „in
Richtung der Araba", in 2Koen 25,4 flieht der Koenig „in Richtung der Ebene".

Nach zwei Paketen, in denen die Vorbereitung fremde Vorlagen zu Unrecht
**ausgeschlossen** hatte (Paket 13) oder zu weit gefasst hatte (Paket 15/16),
war das der umgekehrte Fehler, den es zu vermeiden galt. Der Agent hat
bestaetigt: die *wortgleichen Spannen* sind Feld fuer Feld identisch, die
Verse als ganze nicht.

**Jeremia 39 gewinnt gegen 2. Koenige 25**, wo beide auseinandergehen —
94 verglichene Felder gegen Kap. 39, **null Abweichungen**. `der Oberste der
Leibwache` steht achtmal und ist maschinell auf Feldgleichheit geprueft.

### Die neunte Zweitschreibung

**`Ewil-Merodach` ist keine Neupraegung.** Der Bestand fuehrt
**`Evil-Merodach` A1** (2Koen 25,27) — derselbe Koenig, nur mit `v` statt `w`.
Mein Prompt hatte `Merodach-Baladan` und das in Paket 17 gepraegte `Merodach`
als Modell genannt und den eigentlichen Vorlaeufer uebersehen.

Damit steht die Reihe bei **neun**: `Paschhur`/`Pashur` · `Betlehem`/`Bethlehem`
· `Hananel`/`Hananeel` · `Kaftor`/`Kaphthor` · `Anakiter`/`Enakiter` ·
`Teman`/`Theman` · `Ben-Hadad`/`Benhadad` · `Aschkenas`/`Askenas` ·
`Ewil-Merodach`/`Evil-Merodach`. **Der l1912mod modernisiert Eigennamen in
Jeremia systematisch anders als in den aelteren Buechern.** Das gehoert in die
Vorbereitung jedes weiteren Buches.

### Die zwoelf Geraetenamen

52,18 und 52,19 haeufen `Kessel` · `Schaufel` · `Messer` · `Sprengschale` ·
`Pfanne` · `Becher` · `Feuerpfanne` · `Leuchter` · `Schale` · `Opferschale`,
dazu `Gestell` und `Meer`. **Alle zwoelf tragen paarweise verschiedene Reihen
in allen vier Sprachen**; `glosskollision.py` meldet null inhaltliche Paare.
Neu waren nur `Feuerpfanne` C1 (nach `Kohlenpfanne`, 2Mo 27,3) und
`Opferschale` C1.

### Der Abschluss-Durchgang ueber das fertige Buch

Nach dem letzten Bau sind alle Laeufe ueber alle 52 Kapitel wiederholt worden:

    validate        0 Befunde, Gegenrechnung stimmt
    qa              0 Verdachtsfaelle
    hilfsverb       0 Treffer
    levelcheck      0 Abweichungen  (mit Kapitelnummern 1…52)
    mehrwort        1 Verdachtsfall — der dokumentierte `al sicuro` in 32,37
    sweep           9 Verdachtsfaelle, alle in ihren Kapiteln als Fehlalarm geprueft
    glosskollision  16 inhaltliche Paare

Die 16 Kollisionspaare sind einzeln am Vers angesehen worden. **Fuenfzehn sind
echte Verschmelzungen der Zielsprachen und nicht aufloesbar:**

* **romanisch deckt `tun` und `machen` mit einem Verb ab** (32,20 — *hecho ·
  fait · fatto*), und **`Sünde`/`gesündigt` fallen in allen drei romanischen
  Sprachen zusammen**, weil das Partizip mit dem Substantiv homograph ist
  (16,10 — *pecado · péché · peccato*);
* `all`/`ganz` in drei Sprachen (7,15 · 26,8 · 26,12);
* franzoesisch *été* fuer `Sommer` und `worden` (8,20), *Va* fuer `Geh` und
  das Futurhilfsverb (34,2), *étrangers* fuer Substantiv und Adjektiv (5,19);
* englisch *rain* fuer `Regen` und `regnen` (14,22);
* italienisch `di'` neben `di` an vier Stellen (14,17 · 22,2 · 25,28 · 43,10)
  — nach der Korrektur aus Paket 15 buchweit einheitlich und vom Bestand
  toleriert.

**Einer war aufloesbar und ist aufgeloest:** **4,22** trug `töricht` und
`unverständige` englisch beide auf *foolish*. `unverständig` ist mit 7 Belegen
das schwaecher gebundene Wort (`töricht` 18) und **fuehrt *senseless* bereits
als zweite Bestandslesart** — genau, was die Regel verlangt. Geaendert nur an
der Kollisionsstelle, nur im Englischen. Der Vers stammt aus Paket 2 und hat
alle sechzehn folgenden Einsammlungen ueberstanden.

### `spricht der HERR`: der Endstand

**188 `dit` zu 149 `parle`** ueber das ganze Buch. Kapitel 52 enthaelt die Form
`spricht` kein einziges Mal — der Stand nach 51 Kapiteln ist der Endstand.

Das Muster, das Kapitel 49 zuerst rein gezeigt hat, traegt durch: **`parle`
steht dort, wo LSG „Ainsi parle l'Éternel" schreibt** (die einleitende
Botenformel), **`dit` bei der nachgestellten Formel „dit l'Éternel"**. Die
Voelkersprueche kehren das Mengenverhaeltnis um — Kapitel 46 steht 6 : 0 fuer
`dit`, das einzige Kapitel des Buches, in dem LSG ausschliesslich `dit`
schreibt.

### Die Levelverteilung des fertigen Buches

    A1  24 713      B1   3 380      C1   1 582
    A2   3 936      B2   3 319      C2      42

### Neue Lemmata des letzten Pakets (9)

`Ewil-Merodach` A1 · `Feuerpfanne` C1 · `Opferschale` C1 · `Handwerkervolk` C1
*artisan people · pueblo de artesanos · peuple d'artisans · popolo di
artigiani* (**keine der vier Ausgaben uebersetzt „Handwerker-"** — alle vier
schreiben nur „Rest der Menge"; entschieden hat allein das Deutsche) ·
`Verschleppung` C1 (vom Prompt nicht genannt; sauber getrennt von
`Gefangenschaft` C1 *captivity* und `Verbannung` C1 *exile*, die beide im
selben Kapitel stehen) · drei Zahlwoerter · Mehrwort `in Flammen aufgehen
lassen` C1.

### Was zum Schluss offen bleibt

`konsistenz.py 24` meldet **53 Abweichungen von der Bestandsmehrheit** — das
sind durchweg Numerus- und Tempusunterschiede gegenueber anderen Buechern, die
in diesem Buch richtig sind. Die eigentliche Nacharbeit steht in den
Kandidatenlisten der Abschnitte 13 bis 18: die Wortpaare mit identischen
Reihen (`Bewohner`/`Einwohner`/`Einwohnerin`, `Rache`/`Vergeltung`,
`Gericht`/`Urteil`, `zerschlagen`/`zerschmettern`, `wüst`/`öde`,
`Ödnis`/`Verwüstung`, `Kornspeicher`/`Kornhaus`, `fortschleppen`/`fortschleifen`,
`Weingärtner`/`Weinbauer`, `Ackerbauer`/`Ackermann`), die neun
Zweitschreibungen, und die korpusweite Artikelfrage in `in die Hand geben`.
