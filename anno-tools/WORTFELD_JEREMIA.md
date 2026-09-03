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
Die Formel kommt in 11,8 · 13,10 · 16,12 · 18,12 · 23,17 wieder.

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
