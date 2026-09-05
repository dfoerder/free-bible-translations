# Wortfeld Hosea (Buch 28)

Waechst mit jedem Paket. **Alle** Abschnitte lesen, nicht nur die ersten.

Die buchweiten Entscheidungen — Verszaehlung, Namen, das Hurerei-Wortfeld —
stehen vollstaendig in **`PAKETE_HOSEA.txt`**. Diese Datei sammelt, was die
Kapitel danach zusaetzlich festlegen.

## 0 · Vor dem ersten Kapitel — die vier Faelle, die jeden angehen

**1. Die vier Ausgaben zaehlen untereinander verschieden.** In Kapitel 2 und
12 folgt **allein die franzoesische** der deutschen Zaehlung; en und it sind
um zwei bzw. einen Vers versetzt, es in Kapitel 2 ebenfalls und in Kapitel 12
gar nicht. In Kapitel 14 sind alle vier versetzt. Die Tabelle steht in
`PAKETE_HOSEA.txt`; `ausgaben.py` richtet Kapitel 2 und 12 nicht zuverlaessig
aus.

**2. RIV traegt in 11,12–12,14 eine zweite Verszaehlung im Text** — fuenfzehn
Verse beginnen mit `(12:1)`, `(12:2)` und so fort. Kein Defekt, sondern ein
Fliesstext-Artefakt der italienischen Ausgabe. Wer die RIV-Zeile Wort fuer
Wort abzaehlt, hat zwei Tokens Vorsprung.

**3. `Gomer` ist ein Doppeltraeger, und die haeufigere Lesart ist die
falsche.** Fuenf Bestandsbelege fuehren das Hohlmass (*omer*), vier den Namen.
In 1,3 ist es die Frau.

**4. `Hurerei` ist mit 46 Belegen einstimmig gebunden** —
*sexual immorality · fornicación · débauche · fornicazione*. Das Wort und
seine Familie tragen das ganze Buch (20 Vorkommen).

## 1 · Paket 1 — Kapitel 1 · 2 · 3

39 Verse, 1037 Eintraege. `paketcheck` Abschnitt **A leer**.

### Die Namen des Buches stehen

    Lo-Ruhama   A1  Lo-Ruhamah · Lo-ruhama · Lo-Ruchama · Lo-ruhama   (neu)
    Lo-Ammi     A1  Lo-Ammi · Lo-ammi · Lo-Ammi · Lo-ammi             (neu)
    Diblaim     A1  of Diblaim · de Diblaim · de Diblaïm · di Diblaim (neu)
    Gomer       A1  Gomer · Gomer · Gomer · Gomer      — der **Name**, nicht das Hohlmass
    Beeri       A1  of Beeri · de Beeri · de Beéri · di Beerì         (1. Mose 26,34)
    Jesreel     A1  Jezreel · Jezreel · Jizreel · Izreel
                    Genitiv: of Jezreel · de Jezreel · de Jizreel · d'Izreel
    Jehu        A1  Jehu · Jehú · Jéhu · **Jehu**      — nicht *Iehu*, s. u.
    Usia · Jotham · Ahas · Hiskia · Jerobeam · Joas — alle belegt

**In 2,25 setzt der deutsche Text die Deutung selbst daneben** („Lo-Ruhama,
**die Unbegnadigte**", „Lo-Ammi, **der nicht mein Volk war**"). Die Deutung
ist deutscher Text und wird uebersetzt, der Name bleibt Name — auch dort,
wo **WEB gar keinen Namen mehr setzt** („her who had not obtained mercy").

`Unbegnadigte` C1 *unpardoned one · no indultada · non graciée · non
graziata* ist neu und haengt an `begnadigen` C1 (2,3).

### `Jehu` — der erste Fall, in dem ein Agent den Korpusbefund anwendet

Der Bestand glossiert `Jehu` italienisch 58× als *Iehu*. **RIV schreibt
73× `Jehu` und kein einziges Mal `Iehu`** — das ist Fall 1 aus
`BEFUNDE_RIV_ANLAUT_J.md`, dort mit 65 Vorkommen gelistet. Der Agent fuer
Kapitel 1 hat das nachgemessen und nach dem Daniel-Praezedenzfall die
RIV-Form gesetzt, ohne dass der Prompt ihn darauf hinwies.

### `Jesreel` — gegen die Ausgabe des Verses entschieden

**RIV schreibt `Jizreel` ausschliesslich in Hosea** (5×) und sonst 31×
`Izreel`, dazu 3× `Jzreel` und 2× `Iizreel` — beides Setzfehler. Bei einer
Ausgabe, die denselben Namen auf vier Arten schreibt, traegt die
Bestandsbindung (40 von 42) mehr als die Zeile im Vers. Dieselbe
Entscheidung ist in Daniel 11 bei `Griechenland` gefallen. **Beide Agenten
haben sie unabhaengig so getroffen.**

### Das Hurerei-Wortfeld

    Hurerei          C1  sexual immorality · fornicación · débauche · fornicazione
    Hurerei treiben  C1  (Mehrwort, 24 Bestandsbelege)
    Hure             C1  prostitute · prostituta · prostituée · prostituta
    Ehebruch         C1  adultery · adulterio · adultère · adulterio
    Ehebruch treiben C1  **neu** — commits adultery · comete adulterio ·
                         commet l'adultère · commette adulterio
    Liebhaber        B2  lovers · amantes · amants · amanti   (Sg. lover · amante · amant · amante)
    nachlaufen       B1  run after · correr tras · courir après · correre dietro

**`Ehebruch treiben` fehlte im Bestand**, obwohl `Hurerei treiben` 24
Belege hat und `Ehebruch` 17. Ein Funktionsverbgefuege derselben Bauart,
in Analogie angelegt.

### Der Landwirtschafts- und Festwortschatz aus Kapitel 2

Er kehrt in Kapitel 9 wieder:

    Getreide B1 grain · trigo · blé · grano   ·   Most B2 new wine · mosto · moût · mosto
    Öl A2 · Wolle B1 · Flachs B2 flax · lino · lin · lino
    Weinstock B2 · Feigenbaum B1 · Weinberg B1
    Fest A2 · Neumond B2 · Sabbat B1 · Feiertag B1

### `Baal` — Name, auch wo zwei Ausgaben uebersetzen

    Baal Sg.  A1  Baal · Baal · Baal · Baal          2,10 · 2,18
    Baal Pl.  A1  Baals · baales · Baals · Baal      2,15 (`Baalen`) · 2,19 (`Baale`)

In **2,18** („du wirst mich `mein Mann` nennen und nicht mehr `mein
Baal`") uebersetzen **WEB** (*my master*) und **LSG** (*Mon maître*),
waehrend RV (*Baali*) und RIV (*Mio Baal*) transliterieren. Der deutsche
Text deutet nicht — also bleibt es der Name.

### Zwei Faelle, in denen der l1912mod ein Fachwort meidet

**3,4** ist der klarste: der Vers zaehlt sechs Dinge auf, und **zwei
deutsche Woerter stehen an fremden Plaetzen.**

| Position | deutsch | alle vier Ausgaben |
|---|---|---|
| 4 | `Altar` | *sacred stone · piedra sagrada · statue · statua* (Mazzebe) |
| 6 | `Heiligtum` | *idols · ídolos domésticos · théraphim · idoli domestici* (Terafim) |

Glossiert wird der deutsche Text mit seiner Bestandsbindung. `Priestergewand`
dagegen traegt die Reihe der Ausgaben selbst: C1 *ephod · efod · éphod ·
efod* (13 Lemmabelege).

**`Fürsten` in 3,4 ist Akkusativ Singular**, nicht Plural — `Fürst` ist ein
n-Deklinationswort, und alle vier Ausgaben setzen den Singular. Die
Bindungstabelle allein haette in den Plural gefuehrt (229 gegen 34).

### Was `sweeplemma.py` allein gefunden hat

In Kapitel 2 hat es **drei** Mehrwortluecken gemeldet, die `sweep.py` und
`konvention.py` beide nicht sahen: `es geht jemandem gut` (2,9) und
zweimal `zu jener Zeit` (2,20 · 2,23). Der Lauf gehoert damit fest in die
Kapitelpruefung, obwohl `AUFTRAG_BUCH.md` ihn nicht unter den sechs
Pflichtlaeufen fuehrt.

### Neue Lesarten unter vorhandenen Lemmata (8)

    zusammenschließen  Bestand: feindliche Buendnisse — hier *gather together* (2,2)
    ausziehen          keine Lesart fuer „nackt ausziehen" — *strip · despojo* (2,5)
    ziehen             „eine Mauer davor ziehen" — *put up · levanto* (2,8)
    verloben           Bestand nur *engaged* — hier *betroth · desposo* (2,21)
    Jesreel            Genitiv — *of Jezreel · d'Izreel* (1,5)
    am / über          bei `ahnden` und `sich erbarmen` (1,4 · 1,6 · 1,7)
    anderthalb         Bestand nur maskulin — hier feminin nach `Scheffel` (3,2)
    gehören            Bestand nur 1. Person — hier verneinter Imperativ (3,3)

### Die Ausgaben

**RIV: zwei Anlautfehler, beide in 1,1 und 1,6** — und beide in denselben
zwei Versen des Kapitels:

    1,1  `di zechia`  → d'Ezechia   (134× `Ezechia` im Korpus, 3× `zechia`)
    1,1  `Acaz`       → Achaz       (39× `Achaz`, 1× `Acaz` — nur hier)
    1,6  `erché`      → perché      (2853× `perché`, 17× `erché`)

`zechia` steht ausserdem in **Jesaja 39,1 und Micha 1,1** —
vorgemerkt in `VORMERKUNGEN_29_39.md`.

**In Kapitel 2 und 3 kein einziger Anlautfehler**, in keiner der vier
Ausgaben. Beide Agenten haben ihren Detektor an 1,6 verifiziert.

**RV1909mod siezt** in 1,10 · 2,1 · 2,3 — auf `vosotros` umgestellt, wie
seit dem Hohelied festgelegt.

## 2 · Paket 2 — Kapitel 4 · 5 · 6 · 7

61 Verse. Zusammen: **100 von 197 Versen, 2444 Eintraege**, `validate.py`
ohne Befund. `paketcheck` Abschnitt **A leer**.

### Zwei Bindungen, vor denen die Tabelle in die Irre fuehrt

**`Netz`** steht in `BINDUNGEN_AT.md` als Warnbeispiel und hat in 5,1 und
7,12 wieder zugeschlagen: der Bestand fuehrt 33× das **Fischernetz** und
11× das *caul*, das Fettnetz des Opfertiers. Beide Agenten haben das
Fangnetz genommen — B1 *net · red · filet · rete*.

**`Ofen`** ist im Korpus zweierlei: **18× Schmelzofen** (*furnace ·
fournaise · fornace*) gegen **5× Backofen**. In Hosea 7,4 · 7,6 · 7,7 ist
es dreimal der Backofen, und alle vier Ausgaben bestaetigen es —
B1 *oven · horno · four · forno*. Die Mehrheit haette in den Schmelzofen
gefuehrt.

### Wo der l1912mod von allen vier Ausgaben zugleich abweicht

Das ist selten und deshalb festzuhalten. Zweimal in Kapitel 7:

| Stelle | deutsch | alle vier Ausgaben |
|---|---|---|
| 7,6 | „ihr **Zorn**" | *their baker sleeps · su panadero · leur boulanger · il loro fornaio* |
| 7,14 | „Sie **ritzen** sich" | *they assemble · se reúnen · se rassemblent · si radunano* |

Dazu **5,15**, wo der deutsche Vers offen mit „und sagen:" endet und
**keine** der vier Ausgaben eine Entsprechung hat. Glossiert wird jedes
Mal der deutsche Text.

### Zwei Verse, die `dubletten.py` nicht sieht

`dubletten.py` findet in Hosea null Paare — es misst ab 60 % gemeinsamer
Wortformen und 5 Tokens. Zwei Ueberschneidungen liegen darunter und sind
trotzdem wichtig:

    5,3 ↔ 6,10   „treibt Ephraim Hurerei, und Israel hat sich verunreinigt"
    6,4 ↔ 13,3   „wie die Morgenwolke, wie der Tau, der frueh vergeht"

**Die erste ist beim Einsammeln angeglichen worden.** 6,10 trug fuer das
Hilfsverb von „hat sich verunreinigt" franzoesisch *a* und italienisch
*ha*; das reflexive Perfekt nimmt in beiden Sprachen *être*/*essere*, wie
5,3 es richtig hat. Dazu *itself* → *himself*, nach der Bestandsmehrheit
(*defile himself*, 7 von 18).

**Die zweite ist eine Vorlage fuer Paket 4**: `Morgenwolke` B2 *morning
cloud · nube matutina · nuée du matin · nuvola mattutina* (neu),
`Tau` B2, `frueh am Morgen` A2.

### Was `sweeplemma.py` allein gefunden hat — jetzt in drei von vier Kapiteln

    Kap. 2  `es geht jemandem gut` · `zu jener Zeit` (2×)
    Kap. 4  `Schande bringen`      (durch „zu" getrennt)
    Kap. 5  `daran hindern`        (`parts:[2,4]`)

`sweep.py` und `konvention.py` haben **keinen** dieser fuenf gesehen. Der
Lauf gehoert fest in die Kapitelpruefung, auch wenn `AUFTRAG_BUCH.md` ihn
nicht unter den sechs Pflichtlaeufen fuehrt.

### Neu gepraegt

    Tücke              C1  treachery · perfidia · perfidie · perfidia   (im Bestand null Belege)
    Bluttat            C1  bloodshed · derramamiento de sangre · effusion de sang · spargimento di sangue
    Tempeldirne        C1  shrine prostitutes · prostitutas del templo · prostituées du temple · prostitute del tempio
    störrisch          C1  stubborn · terco · rétif · restio
    Morgenwolke        B2  morning cloud · nube matutina · nuée du matin · nuvola mattutina
    dreinschlagen      C1  struck down · golpeado · frappé · colpito
    Alarm schreien     B2  Mehrwort, in Analogie zu `Alarm blasen` (4. Mose 10,5)
    Auskunft geben     B2  ·  sich zuschanden machen C1  ·  es geht jemandem schlecht B1
    Lügen · Morden · Stehlen · Ehebrechen — substantivierte Infinitive aus 4,2

**`Hure` und `Dirne` tragen im Bestand dieselbe Reihe.** In **4,14**
stehen `Huren` und `Tempeldirnen` im selben Vers — deshalb hat
`Tempeldirne` eine eigene, unterscheidbare Reihe bekommen.

**In 4,2 fuehrt der Bestand die fuenf substantivierten Infinitive
uneinheitlich**: `Fluchen` hat ein eigenes Substantivlemma, `Morden` und
`Lügen` laufen unter `Mord`/`Lüge`, `Stehlen` und `Ehebrechen` nur als
Verben. Im Kapitel sind alle fuenf einheitlich als substantivierte
Infinitive gefuehrt.

### Was die Agenten am Auftrag widerlegt haben

| Vorgabe | tatsaechlich |
|---|---|
| `Terebinthen` unbelegt | **Lemma `Terebinthe` belegt** (Jesaja 6,13) — nur die Pluralform fehlt |
| `huren` 2× in Kap. 4 | **0×**; die zwei Treffer sind `Huren`, der Plural des Substantivs |
| `Hurerei treiben` an sechs Stellen | an **vier** (4,10 · 4,12 · 4,14 · 4,15) |
| `stürzen` 2× | **3×** — das Lemma, nicht die Form |
| `Treue` in 6,4 · 6,6 | **6,4 · 6,7** |
| „Kommt, wir wollen zum HERRN **umkehren**" | der Quelltext sagt **`zurückkehren`** |
| `Morgenrot` | **`Morgenröte`** |
| `Tau` in 6,1–3 | in **6,4** |
| `Großkönig` 1× belegt | **2×** — die Form einmal, das Lemma zweimal |
| `Motte` 2× belegt | **8×** — die Singularlesart zweimal |
| `parallelen.py` sollte Mt 9,13/12,7 melden | tut es **zu Recht nicht**: die Zitate lesen „Barmherzigkeit will ich und nicht Opfer" — kein `Liebe`, kein `lieber`, kein `Erkenntnis`, kein `Brandopfer` |

**Zwei Werkzeuge sind daraus verbessert worden.** `promptcheck.py` liest
jetzt auch deutsche Anfuehrungszeichen — `umkehren` und `Morgenrot`
standen in einem Zitat und nicht in Backticks und rutschten deshalb
durch. Und `belegt.py` sagt jetzt ausdruecklich, dass es die **Form**
zaehlt: „die FORM `Motte` ist 2× belegt — das LEMMA hat 8".

### Die Ausgaben

**RIV1927 — sechs Anlautfehler in vier Kapiteln.** Jeder Agent hat seinen
Detektor an Hosea 1,6 verifiziert, bevor er ihn laufen liess:

    4,14  `h'è`       → ch'è        (korpusweit genau 4 Stellen, s. u.)
    5,5   `iuda`      → Giuda       (30× gegen 841×)
    5,8   `eniamino`  → Beniamino   (5× gegen 157×)
    5,15  `uando`     → Quando      (8× gegen 1354×)
    7,1   `oiché`     → poiché      (21× gegen 977×)
    7,2   `sse`       → esse        (3× gegen 179×)

`iuda`, `eniamino` und `uando` streuen ueber zwanzig weitere Buecher —
buchuebergreifend, nicht Hosea-lokal. `h'è` steht korpusweit an genau
vier Stellen: 2. Mose 10,5 · 5. Mose 28,45 · 2. Koenige 17,27 · Hosea
4,14.

Dazu **RIV 7,9 `dei capelli bianche`** — `capelli` ist maskulin, RIV
schreibt sonst nie `capelli bianche`. Ein Kongruenzfehler, kein
Anlautverlust.

**WEB 4,3 ist gestoert**: „…will waste away. all living things in her…"
— Kleinschreibung nach Punkt, eingeschobener Satzteil ohne Anschluss.

**RV1909mod siezt in 4,1 · 4,13 · 4,14 · 4,15 · 5,1 · 6,1 · 6,4** und
**vertauscht in 5,8 die Instrumente** (deutsch `Horn` in Gibea und
`Trompete` in Rama, RV umgekehrt). Beides nach dem deutschen Text
entschieden.

### Ein Bestandsfehler ausserhalb Hoseas

**Jeremia 25,31**: `Rechtsstreit` ist dort italienisch *contenzioso*
(maskulin), der Artikel `einen` aber *una*. Gefunden vom Agenten fuer
Hosea 4 an der Parallelstelle zu 4,1.

## 3 · Paket 3 — Kapitel 8 · 9 · 10 · 11

57 Verse. Zusammen: **157 von 197 Versen, 3801 Eintraege**, `validate.py`
ohne Befund. `paketcheck` Abschnitt **A leer**, `kongruenz.py` **0**.

### Ein Werkzeug ist aus diesem Paket entstanden

Der Agent fuer Kapitel 8 meldete, dass **Hosea 7,13** das falsche
Hilfsverb traegt: „sie **haben** sich gegen mich aufgelehnt" stand
franzoesisch mit *ont* und italienisch mit *hanno*, waehrend das
reflexive Perfekt in beiden Sprachen *être* und *essere* nimmt — und im
Mehrwort-Eintrag desselben Verses stand die richtige Form. Das war die
**zweite** Stelle; die erste hatte Paket 2 in 6,10 gefunden.

`kongruenz.py` prueft es jetzt: Mehrwoerter mit Lemma `sich …`, deren
romanische Glosse mit *être*/*essere* gebildet ist, und davor ein
Einzelwort `haben`. **Der Lauf fand sofort eine dritte Stelle** — 1,2
„das Land hat sich vom HERRN abgewandt" —, die kein Agent gemeldet hatte.

Derselbe Lauf fand zwei Genusfehler: **2,8 „ihren Pfad"** stand in allen
drei romanischen Sprachen im Plural, obwohl der deutsche Singular ist;
**11,9 „in deiner Mitte"** trug *ta* und *la tua* vor den maskulinen
`milieu` und `mezzo`. Dazu **9,15 „ihrer Taten"** *le loro* vor `atti` —
die hat der Agent fuer Kapitel 9 selbst gefunden und behoben.

### Namen — der dritte Fall der `Iehu`-Familie

**`Zeboim` italienisch ist `Tseboim`, nicht `Seboim`.** Die haeufigere
Bestandslesart (4 von 6) fuehrt *Seboim*; **RIV schreibt korpusweit 7×
`Tseboim` und kein einziges `Seboim`.** Die zweite Bestandslesart
(1. Samuel 13,18 · Nehemia 11,34) hat es bereits richtig.

**`Moph` (9,6) ist ein eigenes Lemma.** Der Bestand fuehrt dieselbe Stadt
als `Memphis` mit fr *Noph* und it *Nof*; in Hosea schreibt der deutsche
Text `Moph`, LSG „Moph" und RIV „Memfi". Damit laeuft Memphis im Bestand
unter drei franzoesisch-italienischen Schreibungen — melden, nicht
vereinheitlichen.

**`Awen` (10,8) ist neu und nicht `Beth-Aven`.** Beide stehen im selben
Kapitel (10,5 und 10,8), und **LSG schreibt an beiden Stellen
`Beth-Aven`** — dort ist die Namensform `Aven` genommen, die LSG sonst
fuehrt (Amos 1,5), sonst waeren zwei Orte nicht unterscheidbar.

Weiter neu: `Schalman` A1 · `Beth-Arbel` A1 (beide 10,14) ·
`Adama` A1 *Admah · Adma · Adma · Adma* (die Lesart aus 1. Mose 10,19).

### Zwei Woerter, die der Bestand unter fremdem Lemma fuehrt

**`Dreschplatz`** (9,1 · 9,2) sieht unbelegt aus. Die **Sache** steht
aber 26× im Bestand — unter **`Tenne`** C2 *threshing floor · era · aire
· aia*. Das neue Lemma hat genau diese Reihe bekommen.

**`Distel`**: der Prompt fuehrte es als „nur flektiert belegt". Die Form
im Kapitel ist `Disteln`, und die ist **19× direkt belegt**.

### `Festtag` gegen `Feiertag` — eine im Bestand angelegte Kollision

Beide tragen dort *feast day · día de fiesta · jour de fête · giorno di
festa*, und `Feiertag` hat dafuer **einen einzigen Beleg** (Johannes
19,31), `Festtag` zehn. In **9,5** stehen sie im selben Vers. `Feiertag`
behaelt die Reihe (sie steht schon in 2,13), `Festtag` weicht auf die
Lesart aus, die **alle vier Ausgaben** dort setzen: B2 *solemn feast ·
solemnidad · jour solennel · solennità*.

### `Vergeltung` — eine Bestandsreihe, die in sich uneinheitlich ist

Die Mehrheitslesart (15 von 19) lautet *retribution · **venganza** ·
**vengeance** · **vendetta*** — englisch „Vergeltung", romanisch „Rache".
In 9,7 schreiben alle vier Ausgaben die Zweitlesart (*retribution ·
retribución · rétribution · retribuzione*, Jesaja 40,10), und die ist
genommen. Der Bruch in der Mehrheitsreihe ist ein Bestandsbefund.

### Neu gepraegt

    Awen A1 · Schalman A1 · Beth-Arbel A1 · Moph A1
    Dreschplatz  C1  threshing floor · era · aire · aia
    Geistesmann  C1  inspired man · hombre de espíritu · homme inspiré · uomo ispirato
    Schwangerschaft B1 · Neuland C1 · Giftkraft B2 · fortlaufen B1 · zurückmüssen B1
    Hass fassen  B2  Mehrwort, `parts:[7,9]`

### Was die Agenten am Auftrag widerlegt haben

| Vorgabe | tatsaechlich |
|---|---|
| `Kalb` 8,5 zweimal · 8,6 | umgekehrt: **8,5 einmal, 8,6 zweimal** |
| `Kalb` „zweimal (10,5)" | je einmal in **10,5 und 10,6** |
| 10,1 hat dreimal Je-desto | **zweimal** |
| `Distel` nur flektiert belegt | die Form `Disteln` ist **19× belegt** |
| `Dreschplatz` unbelegt | die **Sache** steht 26× unter `Tenne` |
| `Baal` steht in Kapitel 9 | nur als Teil von **`Baal-Peor`** — ein Praefixtreffer von `wortzahl.py` |
| „vier parallele Fragen `Wie könnte ich`" (11,8) | **drei**; die vierte ist elliptisch |
| „In Hosea 1–7 acht RIV-Anlautfehler" | **neun** — 6,9 `ichem` war in der Zaehlung nicht mit |
| Der Klammerziffern-Hinweis fuer Kapitel 11 | stand als Kopierrest in **allen vier** Prompts; zwei Agenten haben es unabhaengig gemeldet |

### Was `ausgaben.py` in Kapitel 11 falsch macht

Es waehlt fuer en und it **Versatz +1** und warnt selbst, dass +0 besser
liegt. **+0 ist richtig.** Der Grund liegt hinter dem Kapitel: en und it
haben zwoelf Verse, ihr 11,12 ist der deutsche 12,1.

### Die Ausgaben

**RIV — vier Anlautfehler und zwei Setzfehler in diesem Paket:**

    8,6   `amaria`   → Samaria    (21× gegen 117×)
    8,7   `aranno`   → faranno    (6×; in 14,7 steht dieselbe Form fuer `saranno`
                                   — der Detektor allein entscheidet den Buchstaben nicht)
    11,6  `de' oro`  → de' loro   (2× gegen 51×) — **findet der Detektor nicht**
    9,7   `i giorno` → i giorni   (1× gegen 105×), Numeruskongruenz
    7,9   `capelli bianche` → bianchi                (aus Paket 2)

**`de' oro` ist der methodisch wichtigste Fund des Buches.** Der
Frequenzdetektor sucht seltene Formen; `oro` ist selbst ein haeufiges
Wort (Gold). **Die in `RIV_ANLAUTFEHLER.md` gemessenen 440 verdaechtigen
Vorkommen sind damit eine Untergrenze, keine Zahl.** Betroffen ist jeder
Fall, in dem das verstuemmelte Wort zufaellig ein echtes Wort ergibt.

**RV1909mod** siezt in 9,5 · 9,10 · 10,12 · 10,13 · 10,15 und weicht in
9,6 (Pflanzen und Zelte), 8,14 (`Paläste` → *templos paganos*) und 11,2
(ergaenztes Subjekt) inhaltlich ab. **WEB** baut 9,7 um. Jedes Mal ist
der deutsche Text glossiert worden.

### Ein Bestandsfehler ausserhalb Hoseas

**Jeremia 14,10**: `kein` steht dort spanisch als *ningún*, waehrend
`Gefallen` *complacencia* (feminin) ist. Gefunden vom Agenten fuer
Hosea 8, der die Stelle als Vorlage haette uebernehmen sollen.
