# RIV1927: fehlende Anfangsbuchstaben — ein Befund, keine Reparatur

Gefunden beim Annotieren von **Jeremia 1**: der Agent meldete, RIV schreibe in
1,1 „nel paese di **eniamino**" und in 1,3 „re di **iuda**". Beides sind Woerter
ohne ihren ersten Buchstaben.

## Der Umfang

Gemessen ueber alle fuenf Ausgaben des Bestands. Gesucht wurde jede
kleingeschriebene Form, die hoechstens dreimal vorkommt und durch **einen
vorangestellten Buchstaben** zu einer mindestens zwanzigmal haeufigeren Form
des Korpus wird:

| Ausgabe | Wortformen | verdaechtige Vorkommen |
|---|---|---|
| WEB (en) | 13 332 | 32 |
| RV1909mod (es) | 26 727 | 22 |
| LSG1910 (fr) | 21 827 | 25 |
| l1912mod (de) | 25 042 | 30 |
| **RIV1927 (it)** | **31 834** | **440** |

Die rund dreissig Treffer der anderen vier Ausgaben sind Rauschen (echte
seltene Woerter, die zufaellig einem haeufigen Wort minus Anlaut gleichen).
**Der italienische Wert liegt vierzehnmal darueber** und ist damit kein
Rauschen, sondern ein Defekt der Datei.

## Die Belege

190 Stellen liegen in einer Stellung, in der ein Name zu erwarten ist (nach
`di`, `a`, `in`, `da`, `re di`, `figliuolo di` …), und **jede davon hat den
vollen Namen im selben Buch korrekt geschrieben**:

    Jer 1,1    nel paese di eniamino          → Beniamino
    Jer 1,3    re di iuda                     → Giuda
    2Sam 2,4   fu riferito a avide            → Davide
    2Re 25,28  con lui a abilonia             → Babilonia
    Neh 8,1    stabiliti da sraele            → Israele
    Ger 36,4   a dettatura di eremia          → Geremia

Betroffen sind 68 Namen (Giuda 25×, Davide 15×, Babilonia 12×, Cristo 10×,
Giacobbe und Faraone je 8× …). Der Defekt trifft aber **nicht nur Namen**:
`arte` → `parte`, `uoco` → `fuoco`, `ietra` → `pietra`, `ccidente` →
`occidente`, `utti` → `tutti`, `olui` → `colui`. Insgesamt 322 verschiedene
Formen.

## Warum hier nichts repariert wird

Die Reparatur waere mechanisch moeglich — die Regel „setze den Buchstaben
davor, der die Form zu einem im selben Buch belegten Wort macht" trifft in den
190 Namensfaellen eindeutig. Aber:

* Es sind **ueber vierhundert Aenderungen am Bibeltext selbst**, nicht an
  Annotationsdaten. Der Text ist das, was der Leser in der App sieht.
* Eine falsch geratene Ergaenzung ist im Ergebnis nicht mehr von einer
  richtigen zu unterscheiden — anders als bei einer Glosse, die jederzeit
  gegen den Quelltext nachpruefbar bleibt.
* Die verlaesslichste Korrektur kaeme aus der **Quelle** der RIV-Datei, nicht
  aus einer Heuristik ueber die Datei selbst.

Die Liste der 190 Namensfaelle liegt in `scratchpad/riv_anlaut.json`.

## Was das fuer die Annotation heisst

**Ein Name ohne Anfangsbuchstaben in RIV ist keine Schreibvariante der
Ausgabe.** Wo `NAMENSSCHREIBUNG_*.md` und `AUFTRAG_AT.md` sagen „erst die
Ausgabe aufschlagen", gilt fuer RIV zusaetzlich: sieht die Schreibung um genau
einen fehlenden Anlaut falsch aus, **dieselbe Stelle im selben Buch an einer
zweiten Belegstelle nachschlagen**.

Das ist der zweite Defekt dieser Datei nach dem Rohbyte 0x85, das als
Auslassungszeichen fehldekodiert war (46 Stellen in 13 Buechern).

## Nachtrag: derselbe Defekt am Wortende — aber nur in einer Form

Gefunden beim Annotieren von **Daniel 10**: RIV schreibt in 10,3
`entraron` statt `entrarono`. Der Agent hielt es fuer eine spanische
Form im italienischen Text.

Nachgemessen ueber alle 66 Buecher: es sind **20 Vorkommen in elf
Formen**, alle nach demselben Muster — die 3. Person Plural des Perfekts
ohne ihr Schluss-`o`:

    4×  levaron       → levarono      (32× korrekt)   4Mo 16,2 · Ri 9,34 · Mt 15,37
    3×  entraron      → entrarono     (36×)           Jos 8,19 · Dan 10,3 · Mt 25,10
    3×  alzaron       → alzarono      (13×)           1Sam 30,4 · Joh 17,13 · Apg 4,24
    2×  cavaron       → cavarono                      Ri 16,21 · 2Kön 25,7
    2×  presentaron   → presentarono  (34×)           Mt 14,35 · Apg 1,10
    je 1×: odiaron · mostraron · montaron · invocaron · prepararon · prestaron

Jede dieser Formen hat im selben Korpus die richtige Fassung, meist
dutzendfach. Ob der Setzer ein `o` verloren oder aus einer spanischen
Vorlage abgeschrieben hat, ist von aussen nicht zu entscheiden — die
Zeichenfolgen sind dieselben.

**Ein allgemeiner Defekt am Wortende ist es nicht.** Dieselbe Heuristik
wie oben, nur umgedreht (seltene Form, die durch **einen angehaengten**
Buchstaben zu einer mindestens zwanzigmal haeufigeren Form wird):

| Ausgabe | Vorkommen | Formen |
|---|---|---|
| WEB (en) | 9 | 7 |
| RV1909mod (es) | 22 | 13 |
| LSG1910 (fr) | 39 | 22 |
| l1912mod (de) | 78 | 53 |
| **RIV1927 (it)** | **97** | **72** |

Der italienische Wert liegt nur knapp ueber dem deutschen, nicht
vierzehnfach darueber wie beim Anlaut. Die Treffer sind zum
allergroessten Teil echte Woerter (`territori` gegen `territorio`,
`simil` gegen `simile`). **Der Defekt sitzt am Wortanfang; am Wortende
gibt es nur diese eine, eng umrissene Gruppe.**

## Nachtrag 2: RIV traegt die alternative Verszaehlung im Text

Gefunden bei der Vorbereitung von **Hosea**: RIV beginnt dort fuenfzehn Verse
(11,12 bis 12,14) mit einer Klammerziffer — `(12:1)`, `(12:2)`, … Das ist die
**hebraeische Zaehlung**, die die Ausgabe als Fliesstext mitfuehrt, weil sie
selbst nach der griechischen zaehlt.

Ueber alle 66 Buecher und alle vier Ausgaben gemessen:

| Ausgabe | Verse mit Klammerziffer am Anfang |
|---|---|
| WEB (en) | 0 |
| RV1909mod (es) | 0 |
| LSG1910 (fr) | 0 |
| **RIV1927 (it)** | **222 Verse in 20 Buechern** |

Betroffen sind die Buecher 1 · 9 · 10 · 11 · 12 · 13 · 14 · 18 · 19 · 21 · 22 ·
23 · 24 · 26 · 28 · 30 · 32 · 33 · 47 · 66 — darunter **elf bereits fertige**.

**Es ist kein Defekt und kein Schaden im Bestand.** Annotiert wird der deutsche
Text; die Klammerziffern erzeugen keine Eintraege. Gegenprobe ueber alle
Glossen des Bestands: **null** enthalten eine Klammerziffer.

**Gefaehrlich ist es nur beim Abzaehlen.** Wer eine RIV-Zeile Wort fuer Wort
gegen den deutschen Vers haelt, hat zwei Tokens Vorsprung — dieselbe Falle wie
die Sprecherangaben, die WEB im Hohelied als Fliesstext fuehrt. Jede
Buchvorbereitung eines betroffenen Buches nennt die Stellen.

## Nachtrag 3: die Frequenzheuristik hat eine blinde Stelle

Gefunden beim Annotieren von **Hosea 11**: RIV schreibt in 11,6
`de' oro disegni` statt `de' loro disegni`. Korpusweit steht `de' oro` an
genau **zwei** Stellen — 4. Mose 26,2 und Hosea 11,6 — gegen **51×**
`de' loro`.

**Der uebliche Detektor findet das nicht.** Er sucht seltene Formen, die
durch einen vorangestellten Buchstaben zu einer viel haeufigeren werden.
`oro` ist aber selbst ein haeufiges italienisches Wort (Gold, 118
Vorkommen) — also faellt es durch kein Sieb.

Betroffen ist jeder Fall, in dem das verstuemmelte Wort **zufaellig ein
echtes Wort** ergibt:

    loro  → oro     (Gold)
    lira  → ira     (Zorn)
    corte → orte
    cera  → era
    palo  → alo

### Und eine zweite Untergrenze: die Haeufigkeitsschwelle

Gefunden beim Annotieren von **Hosea 12**: RIV schreibt in 12,12
`si fe' uardiano di greggi` statt `guardiano`. Der Lauf sucht Formen,
die durch einen vorangestellten Buchstaben zu einer **mindestens
zwanzigmal haeufigeren** werden — `guardiano` hat aber nur **15**
Belege. Der Fall faellt durch, obwohl er eindeutig ist.

Dieselbe Schwelle traf `aranno` → `faranno` (Hosea 8,7, 6 Belege) nur
knapp nicht. Wer sie senkt, bekommt mehr Fehlalarme; wer sie laesst,
verliert die seltenen Woerter.

**Beides zusammen — die Wortblindstelle und die Haeufigkeitsschwelle —
macht die oben gemessenen 440 verdaechtigen Vorkommen zu einer
Untergrenze, keiner Zahl.** Wie weit darueber, ist von aussen nur mit
Kontextmodellen zu bestimmen — ein eigener Arbeitsgang.

Dazu kommt eine dritte Sorte, die gar kein Anlautfall ist:
**`hai profeti` statt `ai profeti`** (Hosea 12,10). Hier ist ein
Buchstabe **zuviel**, und `hai` ist selbst ein sehr haeufiges Wort.

**Fuer die Kapitelarbeit heisst das:** der Frequenzlauf bleibt der erste
Schritt, aber er ersetzt das Lesen nicht. Zwei der bisher gefundenen
RIV-Defekte in Daniel und Hosea waren nur durch Lesen zu finden.

## Nachtrag 4: eine dritte Untergrenze — und eine belastbare Zahl

Gefunden beim Annotieren von **Joel 3**: RIV schreibt in 2,32 „sul monte
Sion ed in **erusalemme**". Der Detektor findet das **nicht** — nicht
wegen der Wortblindstelle und nicht wegen der Haeufigkeitsschwelle,
sondern weil er **seltene** Formen sucht: `erusalemme` steht korpusweit
**61×**. Eine oft genug wiederholte Verstuemmelung faellt aus dem Sieb.

Damit sind drei Untergrenzen bekannt:

1. das verstuemmelte Wort ist zufaellig ein echtes Wort (`loro` → `oro`)
2. das richtige Wort ist selbst selten (`guardiano`, 15 Belege)
3. **die Verstuemmelung ist haeufig** (`erusalemme`, 61 Belege)

### Die Namensverstuemmelungen, ohne Seltenheitsdeckel gezaehlt

Der oben beschriebene Lauf hatte einen Deckel („hoechstens dreimal").
Ohne ihn, und beschraenkt auf den **eindeutigen** Fall — eine
kleingeschriebene Form, die durch **einen vorangestellten Grossbuchstaben**
zu einer mindestens zehnmal haeufigeren Form wird, und die selbst
nirgends grossgeschrieben vorkommt:

| Ausgabe | Vorkommen | Formen |
|---|---|---|
| LSG1910 (fr) | 3 | 3 |
| RV1909mod (es) | 13 | 6 |
| WEB (en) | 19 | 3 |
| l1912mod (de) | 20 | 8 |
| **RIV1927 (it)** | **672** | **201** |

**Vierunddreissigmal so viel wie die naechsthoehere Ausgabe.** Eine
Stichprobe ueber die 25 seltensten Treffer enthaelt **keinen einzigen
Fehlalarm** — jeder ist ein verstuemmelter Name oder ein
satzeroeffnendes Wort.

Die haeufigsten:

     61× erusalemme  → Gerusalemme      33× ignore   → Signore
     30× iuda        → Giuda            24× risto    → Cristo
     21× oiché       → Poiché           21× avide    → Davide
     19× sraele      → Israele          17× erché    → Perché
     14× abilonia    → Babilonia        12× iacobbe  → Giacobbe
      9× adre        → Padre             9× pirito   → Spirito
      8× araone      → Faraone           8× iuseppe  → Giuseppe
      8× uando       → Quando            8× ddio     → Iddio

**Das ist die belastbarste Zahl, die dieser Defekt bisher hat** — und
sie ist immer noch eine Untergrenze, weil sie nur den Namensfall zaehlt.
Die 440 aus dem ersten Lauf sind damit ueberholt.

**Fuer die Kapitelarbeit aendert sich nichts**: der Bestand ist
unbeschaedigt, weil der deutsche Text glossiert wird. Gefaehrlich ist der
Defekt nur, wenn eine RIV-Zeile als Vorlage abgezaehlt wird.

---

## Nachtrag Joel (Buch 29): drei Treffer, jeder korpusweit einmalig

Der systematische Lauf ueber Joel — jede im RIV-Korpus seltene Form gegen
jeden moeglichen vorangestellten Buchstaben — liefert genau drei Stellen.
Alle drei sind, jede fuer sich, im ganzen Korpus einmalig:

| Stelle | steht | muss | Gegenprobe im Korpus |
|---|---|---|---|
| Joel 1,12 | „tutti gli alberi della campagna son **ecchi**" | *secchi* | `ecchi` 2×: hier und **Jos 9,4** („de' **ecchi** otri" → *vecchi*) |
| Joel 2,20 | „**alirà**" | *salirà* | `salirà` 18× · `alirà` 1× |
| Joel 2,16 | „**Radunare** il popolo" | *Radunate* | der **einzige** Vers im RIV-Korpus, der mit dieser Form beginnt — und derselbe Vers traegt die richtige Form zweimal |

Joel 2,16 ist ein neuer Untertyp: kein verlorener Anlaut, sondern ein
Imperativ, der zum Infinitiv verlesen wurde (`Radunate` → `Radunare`).
Er faellt demselben Test auf — die Form ist an dieser Stelle einmalig,
waehrend die richtige Form ringsum steht.

**Jos 9,4 war bis hierher unbemerkt.** Der Joel-Lauf hat ihn als
Gegenprobe mitgefunden: wer eine seltene Form pruefen will, muss sie
korpusweit zaehlen, nicht nur im eigenen Buch.

### Ein Vers mit zwei Defekten

**1. Chronika 27,20** traegt beide Typen nebeneinander:

> „Della mezza tribù di Manasse: **Ioel**, figliuolo di **edaia**."

`Ioel` gehoert in die I/J-Liste (`BEFUNDE_RIV_ANLAUT_J.md`), `edaia`
(→ *Pedaia*) in diese hier. Der Vers zeigt, dass die beiden Defekte
dieselbe Ursache haben duerften.

---

## Der Mechanismus: Anlautverlust **nach einem kurzen Vorwort**

Bis hierher war der Defekt als Menge vermessen (672 Vorkommen in 201
Formen). Der Agent fuer **Amos 6** hat aus einem Einzelfall — RIV 6,6
liest „la ruina di **iuseppe**" — die Frage gemacht, *wo* im Satz der
Anlaut verlorengeht. Die Messung ueber zwoelf haeufige G-Namen:

**145 Vorkommen mit verlorenem `G`**, gegen zehntausende korrekte:

```
    61× Gerusalemme  → erusalemme   (korrekt 762×)
    30× Giuda        → iuda         (korrekt 842×)
    16× Gesù         → esù          (korrekt 1043×)
    12× Giacobbe     → iacobbe      (korrekt 378×)
     8× Giuseppe     → iuseppe      (korrekt 249×)
     7× Giordano     → iordano      (korrekt 196×)
     3× Gerico · 3× Giona · …
```

**Und sie stehen fast alle an derselben Stelle** — unmittelbar hinter
einem kurzen Wort:

```
    49× nach `di`        30× nach `a`         13× nach `in`
     7× nach `e`          5× nach `cristo`     3× nach `contro`
```

> 1. Mose 31,24 „…a **iacobbe**…" · 45,4 „son **iuseppe**" ·
> 49,7 „in **iacobbe**" · Amos 6,6 „la ruina di **iuseppe**"

Das ist kein Zufallsmuster, sondern eine Regel: **der erste Buchstabe
eines Wortes faellt weg, wenn ein kurzes Wort davorsteht.** Vermutlich
ein Zeilen- oder Trennungsartefakt des Imports.

Der Defekt trifft nicht nur `G`: 1. Samuel 17,23 hat „quel Filisteo di
**ath**" (→ *Gath*), und dieselbe Messung ueber andere Anlaute findet
`ontro` fuer *contro*, `ecchi` fuer *secchi* (Joel 1,12 · Josua 9,4),
`alirà` fuer *salirà* (Joel 2,20).

**Amos 8,3 ist der bisher sauberste Beleg fuer die Regel:** „grande sarà
il **umero** dei cadaveri" — `umero` steht **1×** im ganzen RIV-Korpus,
`numero` **209×**. Und es steht, wie die Regel es verlangt, unmittelbar
hinter dem kurzen `il`. Gefunden vom Agenten fuer Amos 8.

**Was daraus folgt:** wer eine RIV-Zeile abzaehlt, muss besonders auf
das Wort **nach `di`, `a`, `in`, `e`** achten. Dort steht der Defekt.
Und ein verstuemmeltes Wort, das zufaellig ein echtes ergibt (`oro`
statt `loro`, Hosea 11,6), faellt keiner maschinellen Probe auf.


---

## Nachtrag Obadja (31): drei Treffer in einem Kapitel von 21 Versen

Alle drei folgen der Regel — Anlautverlust hinter einem kurzen Wort —
und alle drei sind korpusweit gezaehlt:

| Stelle | steht | muss | Gegenprobe |
|---|---|---|---|
| Obadja 1,12 | „de' **igliuoli** di Giuda" | *figliuoli* | `igliuoli` **7×** · `figliuoli` **2574×** — hinter `de'` |
| Obadja 1,16 | „del continuo; **erranno**, inghiottiranno" | *berranno* | `erranno` **2 Stellen** · `berranno` **12×** — derselbe Vers hat „berranno" einen Halbsatz vorher richtig |
| Obadja 1,19 | „**ossederanno** i campi d'Efraim" | *possederanno* | `ossederanno` **1×** (nur hier) · `possederanno` **15×** — derselbe Vers hat „possederanno" und „possederà" richtig |

Zwei der drei stehen **im selben Vers wie die richtige Form** — das ist
der sauberste Beweis, dass es ein Satzfehler ist und keine Variante.

### `erranno` ist an beiden Stellen des Korpus ein Defekt — aus zwei verschiedenen Woertern

Die Gegenprobe fuehrt zu einem noch **offenen** Buch:

> **Micha 7,17** „…usciranno spaventate dai loro ripari; **erranno**
> tremanti all'Eterno" → *verranno* („sie werden zitternd kommen")

`erranno` steht im ganzen RIV-Korpus an genau zwei Stellen, Obadja 1,16
und Micha 7,17 — und **keine** davon ist eine echte Form von *errare*.
In Obadja fehlt das `b` von *berranno*, in Micha das `v` von *verranno*
(79×). Wer den Micha-Prompt schreibt, sollte es wissen.


---

## Nachtrag Jona (32): `iona` — und der dritte Fall steht im Neuen Testament

| Stelle | steht | muss | Gegenprobe |
|---|---|---|---|
| Jona 4,6 | „montò su di sopra **a iona**" | *Giona* | `iona` **3×** im ganzen Korpus · `Giona` **26×** |
| Jona 4,8 | „il sole picchiò sul capo **di iona**" | *Giona* | derselbe Vers hat „Giona" nicht, der Nachbarvers 4,6 schon |
| **Matthäus 16,4** | „segno non le sarà dato se non quello **di iona**" | *Giona* | ein **fertiges** Buch |

Alle drei stehen unmittelbar hinter einem kurzen Wort (`a`, `di`, `di`) —
die Regel aus dem Amos-Nachtrag. **Jona 4,6 traegt beide Formen im selben
Vers:** „a iona, per fargli ombra al capo; e **Giona** provò…".

### Ein Untertyp: das kurze Wort selbst faellt aus

**RIV Jona 1,1** liest „La parola dell'Eterno fu rivolta ∅ Giona" — hier
fehlt nicht der Anlaut des Namens, sondern die **Praeposition davor**
(*rivolta **a** Giona*). Derselbe Ort im Satz, die entgegengesetzte
Richtung des Verlusts. Gefunden vom Agenten fuer Jona 1.


---

## Nachtrag Micha (33), Kapitel 1: drei Anlautfehler in sechzehn Versen

| Stelle | steht | muss | korpusweit |
|---|---|---|---|
| Mi 1,1 | „ai giorni di Jotham, di Achaz e **di zechia**" | *Ezechia* | `zechia` **3×** — und **alle drei hinter `di`** |
| Mi 1,9 | „giunge fino alla porta del mio popolo, **fino a erusalemme**" | *Gerusalemme* | `erusalemme` **61×** |
| Mi 1,13 | „il principio del peccato per la **figliuola di ion**" | *Sion* | `ion` **2×** — beide hinter `di` |

**`zechia` steht in zwei fertigen Buechern:** Jesaja 39,1 und Hosea 1,1.
**`ion` ebenso:** Klagelieder 2,7. Beide Male dieselbe Stellung.

Damit sind es fuenf Namen, deren Anlaut ausschliesslich hinter einem
kurzen Wort verlorengeht — die Regel aus dem Amos-Nachtrag haelt an jedem
neuen Buch.

### Ein anderer Fehlertyp im selben Kapitel: die falsche Stadt

**RIV Mi 1,10** liest „Non l'annunziate **in Gad**!" — der deutsche Text
(und WEB, RV, LSG) haben **Gat**, die Philisterstadt. RIV schreibt sie
sonst `Gath` (45×), waehrend `Gad` korpusweit 80× der **Stammesname**
ist. Das ist kein Anlautverlust, sondern eine Verwechslung zweier
existierender Namen — und deshalb gefaehrlicher: keine Haeufigkeitsprobe
schlaegt an, das Wort ist ja echt. Nur der Vergleich mit den drei anderen
Ausgaben findet es.

Gefunden vom Agenten fuer Micha 1.
