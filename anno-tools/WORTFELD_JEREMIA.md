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
