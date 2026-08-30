# Wortfeld des Predigers — was vor dem ersten Kapitel feststeht

Buch 21, 12 Kapitel, 222 Verse, 4991 Tokens. Ein durchgehender Traktat mit
wiederkehrenden Refrains — was über die Kapitelgrenze läuft, ist hier nicht die
Handlung, sondern **eine Handvoll Leitwörter, die in fast jedem Kapitel
stehen**.

Alle Zahlen sind aus dem fertigen Bestand ausgezählt.

## 1. Die Verszählung wackelt in vier von zwölf Kapiteln

| Kapitel | de | en | es | fr | it |
|---|---|---|---|---|---|
| 4 | 17 | **16** | **16** | 17 | **16** |
| 5 | 19 | **20** | **20** | 19 | **20** |
| 11 | 10 | 10 | 10 | **8** | 10 |
| 12 | 14 | 14 | 14 | **16** | 14 |

**Es sind zwei verschobene Kapitelgrenzen, keine fehlenden Verse.** Vers für
Vers nachgemessen:

| | wo die Grenze anders liegt |
|---|---|
| **4 / 5** | de 4,1–16 = en/es/it 4,1–16, aber **de 4,17 = en/es/it 5,1**. Danach ist ganz Kapitel 5 um eins versetzt: **de 5,n = en/es/it 5,n+1**. **Das Französische folgt dem Deutschen** in beiden Kapiteln. |
| **11 / 12** | umgekehrt: **das Französische** zieht die Grenze zwei Verse früher. de 11,9 = fr 12,1, de 11,10 = fr 12,2, und danach **de 12,n = fr 12,n+2**. en, es und it folgen dem Deutschen. |

**`ausgaben.py` meldet für Kapitel 4 `Versatz -1 … UNSICHER`, und das ist
irreführend**: die ersten sechzehn Verse stehen auf +0, nur der siebzehnte
rutscht. Wer den gemeldeten Versatz global anwendet, glossiert sechzehn Verse
aus der falschen Zeile. In diesen vier Kapiteln ist **jede** Ausgabenzeile am
Inhalt zu prüfen, nicht an der Nummer.

Die übrigen acht Kapitel stimmen in allen fünf Ausgaben überein.

## 2. `vergänglich` — das Leitwort des Buches, und die Ausgaben helfen nicht

Es steht **25×** (dazu `Vergänglichkeit` 2×) und ist damit nach `Zeit`,
`Gott` und `Sonne` das häufigste Inhaltswort. Der Bestand kennt es siebenmal,
davon sechs im NT als *perishable* (verderbliche Speise, vergängliches Silber)
und **einmal im AT**: Psalmen 39,5, `vergänglich` = *transient · pasajero ·
éphémère · effimero* (B2) — genau der Qohelet-Sinn.

**Den Ausgaben ist hier nicht zu folgen.** Alle vier schreiben ein
**Substantiv**: *vanity · vanidad · vanité · vanità* („Eitelkeit"), wo der
modernisierte deutsche Text ein **Adjektiv** hat. In 1,2 bauen sie den Vers
sogar völlig anders („Vanity of vanities" gegen „Alles ist vergänglich").
Wort-für-Wort-Glossen müssen dem deutschen Text folgen; der einzige AT-Beleg
ist die naheliegende Wahl. **Kapitel 1 entscheidet und trägt es hier ein.**

## 3. `Haschen nach Wind` — die zweite Formel, im Bestand unbelegt

`Haschen` steht **9×** und hat im ganzen Korpus **keinen Beleg**. Die vier
Ausgaben sind sich uneins: WEB *a chasing after wind*, LSG *poursuite du vent*,
RIV *un correr dietro al vento* — aber **RV schreibt etwas ganz anderes**:
*aflicción de espíritu* („Betrübnis des Geistes", die alte Vulgata-Lesart).

Das ist die Stelle, an der die spanische Ausgabe dem deutschen Text nicht
folgt. `Wind` ist gebunden (*wind · viento · vent · vento*, 26 Belege);
`Haschen` ist eine Entscheidung, keine Ablesung, und sie muss für alle neun
Stellen dieselbe sein.

## 4. `Prediger` — der Buchtitel, ebenfalls unbelegt

Steht 6× (dazu `Predigers` 1×). Die Ausgaben teilen sich:

| en (WEB) | es (RV) | fr (LSG) | it (RIV) |
|---|---|---|---|
| Preacher | Predicador | **Ecclésiaste** | **Ecclesiaste** |

Französisch und Italienisch nehmen den griechischen Buchtitel, Englisch und
Spanisch übersetzen. Beides ist die jeweilige Ausgabe — nach der Regel „die
Ausgabe liefert den Namen" ist ihnen zu folgen, auch wo sie auseinandergehen.

## 5. Die übrigen Leitwörter

Alle im Bestand gebunden und ohne Eingriff zu übernehmen:

| deutsch | in Pred | AT-Bestand | en · es · fr · it | Level |
|---|---|---|---|---|
| `Zeit` | 38× | 312× | time · tiempo · temps · tempo | A1 |
| `Sonne` | 34× | 55× | sun · sol · soleil · sole | A1 |
| `Weisheit` | 29× | 109× | wisdom · sabiduría · sagesse · sapienza | B2 |
| `Mühe` | 17× | 14× | toil · fatiga · peine · fatica | B2 |
| `Narr` | 23× | 57× | fool · necio · insensé · stolto | B2 |
| `Weiser` | 12× | 31× | wise · sabios · sages · saggi | B2 |
| `Torheit` | 9× | 28× | foolishness · necedad · folie · stoltezza | C1 |
| `Wind` | 12× | 26× | wind · viento · vent · vento | A2 |
| `geschehen` | 19× | 56× | happens · sucede · arrive · accade | B1 |
| `Werk` | 8× | 47× | work · obra · œuvre · opera | B1 |
| `Reichtum` | 6× | 43× | riches · riqueza · richesse · ricchezza | B2 |

`besser` ist 16× und im Bestand als `gut`-Komparativ geführt (41 Belege,
*better · mejor · mieux · meglio*) — dieselbe Form wie in den Sprüchen.

## 6. Kollisionen im selben Vers — was `hints.py` meldet

22 Paare. **Die Liste ist nicht vollständig**, und die Erfahrung aus Buch 20
sagt, dass ein Fünftel davon Fehlalarme sind (Partikeln trennbarer Verben,
Verbformen, die wie Adjektive aussehen) und dass `glosskollision.py` mehr echte
findet, als hier steht.

Die inhaltlich schwersten:

| Paar | Stellen |
|---|---|
| `ergehen` ↔ `geschehen` | 8,14 (alle vier Sprachen!) |
| `Torheit` ↔ `Unsinn` | 1,17 · 2,12 · 10,13 (es *necedad*) |
| `Mühe` ↔ `abmühen` | 1,3 · 2,22 |
| `Mühe` ↔ `mühen` | 4,8 |
| `Werk` ↔ `wirken` | 11,5 |
| `Netz` ↔ `Schlinge` | 9,12 |
| `Schaden` ↔ `Übel` | 5,12 |
| `Lebender` ↔ `lebendig` | 9,4 |
| `Böse` ↔ `böse` | 8,11 |

Dazu neun Paare aus Funktionswörtern und Adverbien (`neu`/`wieder`,
`dasselbe`/`derselbe`, `ebenso`/`genauso`, `solange`/`während`, `bis`/`solange`,
`denn`/`weil`, `dennoch`/`doch`, `desto`/`mehr`, `gut`/`ja`), die in Buch 20
fast durchweg als echte Verschmelzungen der Zielsprachen stehen geblieben sind.

**`Mühe` ↔ `abmühen` und `Werk` ↔ `wirken` sind Substantiv und Stammverb** —
in Buch 20 war das viermal ein Fehlalarm (`Schlaf`/`schlafen`,
`Lüge`/`lügen`, `satt`/`gesättigt`, `Armen`/`arm`). Erst am Vers entscheiden.

## 7. Vier buchinterne Dubletten

| Paar | Ähnlichkeit | Text |
|---|---|---|
| **1,2 ↔ 12,8** | 0,70 | „Alles ist vergänglich, sagte der Prediger" — Anfang und Ende des Buches |
| 1,3 ↔ 2,22 | 0,73 | „Was hat der Mensch für einen Gewinn von all seiner Mühe" |
| 1,14 ↔ 2,17 | 0,65 | „alles vergänglich und ein Haschen nach Wind" |
| 6,1 ↔ 10,5 | 0,59 | „Es gibt ein Übel, das ich unter der Sonne gesehen habe" |

Alle vier tragen die Leitwörter aus Abschnitt 2 und 3. `dubletten.py 21`
erzeugt die Karte neu.

## 8. Die 124 unbelegten Wortformen

`hints.py` meldet sie **formbasiert** — das Lemma kann über eine andere Form
längst im Bestand stehen. In Buch 20 sind mehrere Agenten darauf
hereingefallen und haben Wörter neu erfunden, die es gab (`Steinmauer`,
`guttun`, `freigebig`, `Wasserlauf`). **Immer zusätzlich `lexicon.py` fragen
und bei zusammengesetzten Wörtern das Grundwort suchen.**

## 9. Was Kapitel 1 festgelegt hat

Kapitel 1 ist gelaufen und validiert (18 Verse, 351 Einzelwort- und 21
Mehrwort-Einträge, alle sechs Prüfläufe ohne Befund).

### Die drei Leitwörter

| deutsch | en · es · fr · it | Level | gilt für |
|---|---|---|---|
| `vergänglich` | transient · pasajero · éphémère · effimero | B2 | alle 25 Stellen |
| `Haschen` | chasing · correr · courir · correre | C1 | alle 9 Stellen — **kein** Mehrwort |
| `nach` (bei `Haschen`) | after · tras · après · dietro | A1 | dieselbe Stelle |
| `Prediger` | Preacher · Predicador · Ecclésiaste · Ecclesiaste | B2 | alle 7 Stellen |

**`vergänglich` folgt dem einzigen AT-Beleg** (Ps 39,5), nicht der
NT-Mehrheit (6:1 *perishable*, aber dort an verderblicher Speise und
vergänglichem Silber — „dem Verderben unterworfen", nicht „flüchtig").

**Den Ausgaben ist aus einem grammatischen Grund nicht zu folgen**: alle vier
schreiben ein Substantiv, wo der Text ein prädikatives Adjektiv hat, und das
adjektivische Gegenstück (*vain · vano*) sagt „eitel/nichtig" — was der
Modernisierer gerade nicht geschrieben hat. Er hat Luthers „Es ist alles ganz
eitel" durch „Alles ist vergänglich" ersetzt und die Bedeutung damit von
*nichtig* auf *flüchtig* verschoben.

**`Haschen nach` ist bewusst kein Mehrwort-Eintrag.** `SPEC.md` erlaubt sie
nur, wo sich die Bedeutung nicht aus den Teilen ergibt. Der Schlüssel ist
`nach`: der Bestand führt für die Verfolgungsrichtung schon *after · tras ·
après · dietro* (99 Belege, 1Mo 31,23 „jagte ihm nach"), und damit komponiert
die Wendung in allen vier Sprachen sauber. **Das Spanische ist als einziges
nicht abgelesen, sondern gebildet** — RV schreibt an allen neun Stellen
*aflicción de espíritu*, die alte Vulgata-Lesart, und folgt dem deutschen Text
nicht.

### Die vier gemeldeten Kollisionen

| Vers | Paar | Befund |
|---|---|---|
| 1,3 | `Mühe` ↔ `abmühen` | **echt, und schärfer als gemeldet**: `hints.py` sah nur en *toil*, tatsächlich fielen auch es *fatiga* und fr *peine* zusammen. `abmühen` weicht auf zwei belegte Bestandslesarten aus (en *labors*, fr *fatigue*) und es *afana* nach RV im Vers. |
| 1,6 | `drehen` ↔ `kehren` | echt; `kehren` nimmt die zweite Bestandslesart *returns · vuelve · revient · torna* — passt ohnehin besser, weil es zur Klammer `zurückkehren` gehört. |
| 1,9 | `neu` ↔ `wieder` | **Fehlalarm**: `hints.py` rechnete mit der adverbialen `neu`-Lesart („aufs Neue"); hier steht „nichts **Neues**", das Adjektiv. |
| 1,17 | `Torheit` ↔ `Unsinn` | echt, nur es. `Unsinn` hat **einen** Bestandsbeleg und keine zweite Lesart; genommen ist RVs eigenes *locura*, das die Ausgabe an allen drei Unsinn-Versen neben *necedad* schreibt. **Gilt für 2,12 und 10,13.** |

### Zwei Formfallen, die für die Folgekapitel gelten

**`voller` ist zweierlei.** In 1,8 („so voller Mühsal") ist es die
Bestandswendung `voller` B1 = *full of · lleno de · plein de · pieno di* (78
Belege); in 1,7 („das Meer wird nicht voller") ist es der **Komparativ von
`voll`** — anderes Lemma, A2, *fuller · más lleno · plus plein · più pieno*.
Die Wortform ist identisch. Wer den Extrakt formbasiert liest, setzt die
falsche Wendung.

**`gerade` ist in 1,15 räumlich** (*straight · derecho · droit · diritto*, 8
Belege), nicht temporal — die Korpusmehrheit ist mit 31 Belegen die temporale
Lesart „just then".

### Weitere Festlegungen

| deutsch | en · es · fr · it | Level | Herkunft |
|---|---|---|---|
| `Unsinn` | nonsense · **locura** · sottise · sciocchezza | B2 | es aus RV, Rest Bestand |
| `abmühen` | labors · afana · fatigue · affatica | B2 | Auflösung 1,3 |
| `sich abmühen` (MW) | wears himself out · se afana · se fatigue · si affatica | B2 | Bestand (Ps 39,7) |
| `Mühsal` | hardship · penalidad · tribulation · tribolazione | C1 | Bestand — **gegen alle vier Ausgaben**; RVs *fatiga* wäre mit `Mühe` kollidiert |
| `Gewinn` | gain · ganancia · gain · guadagno | B1 | Bestand |
| `plagen` (sich p.) | toil · afanen · peinent · affatichino | B2 | **neue Lesart** — die Bestandsbindung ist *plague* (die Frösche von 2Mo 7,27) |
| `münden` | empty · desembocan · débouchent · sboccano | B2 | Bestand (Jos 15,4) — hält `fließen` im selben Vers frei |
| `Ausgangspunkt` | starting point · punto de partida · point de départ · punto di partenza | B2 | **neu** — keine der vier Ausgaben hilft, alle übersetzen die hebräische Kreisbewegung |
| `Späterer` | of after · de después · d'après · di poi | B2 | **neu**, symmetrisch zu `Früherer` (Hiob 18,20) |
| `Verständnis` / `Erkenntnis` / `Wissen` | understanding · … / knowledge · … / knowledge · … | B2/B2/B1 | ⚠ `Erkenntnis` und `Wissen` tragen dieselben vier Glossen — in 1,16/1,18 verschiedene Verse, deshalb nicht aufgelöst |
| `Kummer` / `Schmerz` | grief · pesar · chagrin · cordoglio / pain · dolor · douleur · dolore | B2/B1 | Bestand |
| `vollkommen` (Gradadverb) | completely · completamente · complètement · completamente | B2 | **neue Lesart**; **nicht** nach 12,8 übertragen, dort steht „ganz und gar" |

### Bestandsbefunde

- **`Ohr` ist im Spanischen uneinheitlich**: *oído* (24×) gegen *oreja* (21×)
  für dasselbe Lemma bei fast gleicher Belegzahl. Genommen ist *oído*.
- `abmühen`, `mühen` und `sich abmühen` liegen als drei Lemmata nebeneinander
  (Ps 39,7 hat zwei davon im selben Vers) — eine Bestandsaltlast.

### Befunde in den Ausgaben

- **RIV 1,2/1,3 verschiebt den Versschnitt**: „vanità delle vanità; tutto è
  vanità" steht am Anfang von 1,3. `ausgaben.py` richtet trotzdem korrekt aus.
- **RIV 1,13 hat ein Importartefakt**: „**ccupazione** penosa" — das `o` von
  *occupazione* fehlt.

## 10. Was die Kapitel 2, 3 und 4 festgelegt haben

### Die Ausrichtung von Kapitel 4 ist bestätigt

Der Agent hat sie Vers für Vers am Inhalt nachgemessen: **4,1–16 stehen in
allen vier Ausgaben auf +0**, nur 4,17 ist in WEB, RV und RIV der Vers 5,1;
LSG folgt dem Deutschen. Der von `ausgaben.py` gemeldete `Versatz -1 …
UNSICHER` ist falsch, aber das Skript **zeigt trotzdem die richtige Zeile an**
(die verschobenen sind mit `?` markiert). Für Kapitel 5 gilt durchgehend
de 5,n = en/es/it 5,n+1, fr = de.

### Das Zeitgedicht 3,1–8 — mit eigenem Listenskript geprüft

**Sieben Verse, vierzehn Paare, 28 Glieder**, positionsgenau gegen den
Quelltext geprüft. Das Skript leitet die Position jedes Gliedes selbst ab und
prüft zusätzlich, dass die vier Glieder eines Verses in **jeder** Sprache
verschiedene Glossen tragen. Der erste Lauf hat die eigene Ableitung des
Agenten widerlegt (das koordinierende `und` gehörte nicht zum Glied).

**Sechs der 28 Glieder standen schon als Substantiv-Lemma im Bestand**
(`Weinen`, `Lachen`, `Klagen`, `Schweigen`, `Reden`, `Sterben`) und wurden
übernommen; die übrigen sind formbasiert unbelegt, ihre Verbstämme aber
sämtlich belegt und maßgeblich. **Kein Wort neu erfunden, das es gab.**

Zwei Lexikonfallen darin:

- **`Sterben`** hat im Bestand zwei Lesarten — *dying · agonía · agonie ·
  agonia* (9×, der Todeskampf von 1Mo 35,18) und *dying · morir · mourir ·
  morire* (2×, Ps 49,18). Die Korpusmehrheit hätte hier „Agonie" gesetzt.
- **`Klagen`** (Substantiv) ist an *groaning · gemido · gémissement · gemito*
  gebunden (8×, das Seufzen Israels unter der Fron), während das Verb `klagen`
  *lament* trägt. Gegen `Tanzen` ist die Klage gemeint: *mourning · lamento ·
  lamentation · lamento*. RIVs *cordoglio* wurde gemieden, weil `Kummer` im
  Bestand darauf gebunden ist.

### Die gemeldeten Kollisionen

| Vers | Paar | Befund |
|---|---|---|
| 2,3 | `während` ↔ `solange` (es) | `solange` weicht auf es *en tanto que* aus — **gebildet**, weil alle 86 Bestandsbelege *mientras* tragen und keine Ausgabe hier eine Konjunktion setzt |
| 2,3 | `bis` ↔ `solange` (it) | `solange` weicht auf die **belegte** zweite Lesart *fintanto che* aus (Neh 7,3); `bis` behält *finché*, was RIV wörtlich schreibt |
| 2,12 | `Torheit` ↔ `Unsinn` | Kapitel-1-Lösung übernommen; RV schreibt in 2,12 beide Wörter selbst |
| 3,19 | `dasselbe` ↔ `derselbe` | echt — das Genus trennt sie **nur im Italienischen**. Gelöst mit zwei Bestandslesarten: *the same thing · lo mismo · la même chose · la stessa cosa* (1Sam 17,23) gegen *the same · el mismo · le même · lo stesso* (1Kön 19,15) |
| 4,8 | `Mühe` ↔ `mühen` | echt, aber **nur in zwei Sprachen** (en *toil*, fr *peine*) — es und it trennen von sich aus. `mühen` weicht aus auf *labor · afano · fatigue · affatico* |

Dazu **über zwanzig Kollisionen, die erst `glosskollision.py` gefunden hat**
und für die `hints.py` nichts gemeldet hatte — darunter 2,10
`verweigern`/`versagen` (alle vier Sprachen!), 2,15 `Da`/`dann` (alle vier) und
in Kapitel 4 fünf weitere.

### Weitere Festlegungen

| deutsch | en · es · fr · it | Level | Herkunft |
|---|---|---|---|
| `solange` | as long as · en tanto que · tant que · fintanto che | B1 | Auflösung 2,3 |
| `verweigern` / `versagen` | refused · negué · privai · rifiutai / denied · rehusé · refusai · negai | B2 | Auflösung 2,10 |
| `dann` (rhetorisch) | therefore · pues · donc · dunque | A1 | Auflösung 2,15 |
| `mühen` | labor · afano · fatigue · affatico | B2 | Auflösung 4,8 |
| `Vergänglichkeit` | transience · fugacidad · fugacité · caducità | C1 | **neu** — der einzige Bestandsbeleg (Röm 8,21) ist *decay*, also φθορά, nicht der Qohelet-Sinn |
| `Ruhe` (4,6) | rest · descanso · repos · riposo | A2 | Bestand 74:11 — im Prediger die Ruhe-Lesart, anders als 1,33 in den Sprüchen |
| `Lohn` | wages · salario · salaire · salario | B1 | vereinheitlicht, s. u. |
| `Besseres` | better · mejor · mieux · meglio | B1 | vereinheitlicht, s. u. |
| `Atem` | breath · aliento · souffle · respiro | B2 | Bestand (28×) — **gegen WEB und RV**, die in 3,21 *spirit*/*espíritu* schreiben |
| `jeder` | every · cada · chaque · ogni | A1 | Auflösung 3,1 gegen `alles` (Level A1, nicht A2 — vom Bestand und von `levelcheck.py` bestätigt) |
| `Stätte` | place · lugar · lieu · luogo | C1 | ⚠ identisch mit `Ort` (A2) — verschiedene Verse, nicht aufgelöst |
| `Park` | parks · parques · parcs · parchi | B1 | **neu**; LSG *vergers* und RV *jardines* wären mit `Gärten` kollidiert |
| `Streben` · `ereilen` · `aufwenden` · `Einzelner` · `trostlos` · `verschränken` | … | B2/C1/B2/B2/C1/B2 | **neu** |

### Was der Kreuzabgleich gefunden hat

63 gemeinsame Inhaltswortformen. Zwei echte Divergenzen, beide vereinheitlicht:

- **`Besseres`** trug in 2,24 *meilleur · migliore*, in 3,12 und 3,22
  *mieux · meglio* — bei identischer Konstruktion („es gibt nichts Besseres
  … als"). RIV schreibt an allen drei Stellen *nulla di meglio*.
- **`Lohn`** trug in 2,10 *reward · recompensa · récompense · ricompensa*, in
  4,9 *wages · salario · salaire · salario*. Der Bestand ist mit 32:29 fast
  geteilt; genommen ist die AT-Lesart, die auch die Sprüche führen und die LSG
  in 4,9 wörtlich schreibt.

### Prompt-Hinweise, die im Text nicht stehen

**Neun allein in Kapitel 3**: `Abbrechen`/`Bauen` heißen `Abreißen`/`Aufbauen`;
`Steinewerfen`/`Steinesammeln` sind zwei dreigliedrige Fügungen, keine
Komposita; `Meiden` gibt es nicht (der Text sagt „sich vom Umarmen
fernzuhalten", und `Umarmen` steht **zweimal** im Vers); `Behalten` heißt
`Aufbewahren`, `Nähen` heißt `Zusammennähen`; **3,9 ist nicht die Dublette zu
1,3** (das ist 2,22) und formuliert anders; 3,16–17 haben weder `Gericht` noch
`Gottloser`, sondern `Recht`/`Unrecht`/`Gerechtigkeit`/`Ungerechte`; **`Geist`
steht in 3,18–21 überhaupt nicht** — der Text hat dreimal `Atem`, der
angekündigte Zweideutigkeitsfall entsteht gar nicht; und der `Staub`-Refrain
greift 1Mo 3,19 im Deutschen **nicht** auf, weil der modernisierte Text dort
`Erde` sagt.

In Kapitel 2: `Knechte` und `Herden` stehen nicht da (der Text hat `Diener`,
`Dienerinnen`, `Gesinde`, `Rinder`, `Schafe`). In Kapitel 4: `Gewalt` steht
nirgends im Prediger (4,1 hat `Macht`), und 4,12 hat eine „dreifach
**geflochtene** Schnur", zwei Wörter.

### Bestandsbefunde

- **`Finsternis` (C1) und `Dunkel` (B1) tragen in allen vier Sprachen dieselben
  Glossen** und stehen in 2,13/2,14 in benachbarten Versen. Nicht aufgelöst,
  aber korpusweit fällig.
- **`hinzugeben` liegt doppelt**: eigenes Lemma C1 = *add* (3Mo 27,13) und Form
  von `hingeben` B2. In 2,3 ist `hingeben` richtig; formbasiert liest man
  „hinzufügen".
- `Erkenntnis`/`Wissen` — der Befund aus Kapitel 1 bestätigt sich.

### Vier Importartefakte in der italienischen Ausgabe

Nach 1,13 (`ccupazione`) noch: **2,10 `oiché`** (das *p* von *poiché* fehlt),
**2,12 `esaminate`** statt *esaminare*, **3,22 `ale`** (das *t* von *tale*
fehlt).

## 11. Was die Kapitel 5, 6 und 7 festgelegt haben

### Die Ausrichtung von Kapitel 5 ist bestätigt

Vers für Vers am Inhalt nachgemessen: **de 5,n = WEB/RV/RIV 5,n+1** durchgehend,
**LSG folgt dem Deutschen** (fr 5,n = de 5,n). Die vier Ausgaben laufen also
untereinander auseinander; für jeden Vers braucht man beide Nummern.
`ausgaben.py` meldet die Versätze korrekt (+1/+1/+0/+1).

### „ein schlimmes Übel" — die Wendung steht dreimal, und der Bestand hilft nicht

5,12 · 5,15 · 6,2. Kapitel 5 und 6 liefen **gleichzeitig** und hatten sie
verschieden gelöst (*terrible* gegen *severe · grave · grave · grave*). Der
Bestand führt für `schlimm` **keine passende Lesart** — alle 24 Belege sind
*worse* oder *bad*. Also entscheiden die Ausgaben, und die sind über alle drei
Verse konsistent:

| deutsch | en · es · fr · it | Level |
|---|---|---|
| `schlimm` (an `Übel`) | grievous · doloroso · grave · grave | B1 |

WEB schreibt zweimal *grievous*, RV zweimal *doloroso*, LSG und RIV dreimal
*grave*. Jede Sprache bekommt das Wort ihrer eigenen Ausgabe.

### Die gemeldeten Kollisionen — vier von fünf sind Fehlalarme oder anders

| Vers | Paar | Befund |
|---|---|---|
| 5,11 | `Schlaf` ↔ `schlafen` | **Fehlalarm** — Substantiv und Stammverb, nur en; **alle vier Ausgaben wiederholen das Wort selbst**. Dieselbe Konstellation wie Spr 4,16. |
| 5,12 | `Schaden` ↔ `Übel` | echt; `Schaden` weicht auf die belegte zweite Lesart aus (Esra 4,13), und **nur im Französischen**: *harm · daño · dommage · danno* |
| 5,19 | `denn` ↔ `weil` | echt (es); `denn` weicht auf die belegte Lesart *pues* aus. **RV verteilt es andersherum** — hier gewinnt der Bestand über die Ausgabe |
| 7,10 | `Frage` ↔ `fragen` | **bleibt stehen** — Imperativ `Frag` gegen Substantiv `Frage`, nur es, und dort nur bis auf die Groß-/Kleinschreibung. Das Deutsche unterscheidet die beiden selbst kaum |
| 7,11 | `gut` ↔ `ja` | **Fehlalarm, die Kollision entsteht gar nicht**: `hints.py` rechnete mit der adverbialen `gut`-Lesart, im Vers steht der Äquativ „so gut wie" mit prädikativem Adjektiv zu einem Femininum (*buena · bonne · buona*) |

Dazu **eine echte Kollision, die kein Werkzeug gemeldet hat**: 7,25 `Torheit` ↔
`Wahnsinn`, beide im Bestand fr *folie*, und sie stehen im selben Vers („die
Torheit des Wahnsinns"). `Wahnsinn` weicht **nur französisch** auf *démence*
aus. Damit sind `Torheit` (*folie*), `Unsinn` (*sottise*) und `Wahnsinn`
(*démence*) im Buch durchgehend getrennt.

### `Trauer` — eine bewusste Abweichung von allen vier Ausgaben

`Trauer` ist im Bestand **4:3 geteilt**: *mourning · luto · deuil · lutto* (AT)
gegen *sorrow · tristeza · tristesse · tristezza* — und **alle drei
sorrow-Belege sind neutestamentlich**. Genommen ist einheitlich die AT-Lesart
an allen drei Stellen (7,2 · 7,3 · 7,4), obwohl die vier Ausgaben in 7,3
einhellig das Traurigkeitswort schreiben.

Zwei Gründe: die Lexikonfalle, und dass der modernisierte Text in 7,2–7,4
dreimal dasselbe deutsche Wort setzt — der Leser bekäme sonst mitten in einer
Verskette zwei Glossen für ein Wort. Zusätzlich hält *deuil* die Bahn frei für
`Kummer`, das der Bestand an fr *chagrin* bindet (1,18).

### `besser` — der Regelfall und zwei begründete Ausnahmen

Regelfall *better · mejor · mieux · meglio* (B1, neun Belege in Kapitel 7).
**Zwei Stellen tragen die kongruierende Adjektivform**, weil dort kein
„valoir mieux"-Rahmen steht, sondern ein Prädikats- oder Objektprädikativ:

- **7,3b** „macht das Herz besser" → *better · mejor · meilleur · migliore*
  (RIV schreibt *il cuore diventa migliore*)
- **7,10** „waren die früheren Tage besser" → *better · mejores · meilleurs ·
  migliori* (LSG *meilleurs*, RIV *migliori*, RV *mejores*)

**Bestandsbefund:** Spr 16,32 („Geduld ist besser als Heldenkraft"), die
direkte Parallele zu 7,8b, trägt *meilleure · migliore*. Buch 20 und Buch 21
gehen bei derselben Sprichwortbauform auseinander — gemeldet, nicht angefasst.

### Weitere Festlegungen

| deutsch | en · es · fr · it | Level | Herkunft |
|---|---|---|---|
| `Trauer` | mourning · luto · deuil · lutto | B1 | AT-Lesart, gegen die Ausgaben |
| `Wahnsinn` | madness · locura · démence · pazzia | C1 | Auflösung 7,25 |
| `Schaden` | harm · daño · dommage · danno | B1 | Auflösung 5,12 |
| `Fremder` | stranger · extraño · étranger · estraneo | B1 | die NT-/Sprüche-Lesart — der Außenstehende, nicht der Fremdling im Land. **RIV schreibt *straniero*** und weicht ab |
| `feststehen` | is known · se sabe · est connu · è noto | B2 | **neue Lesart** — alle Bestandsbelege sind *stand firm* |
| `verbringen` | spends · vive · vit · trascorre | B1 | Auflösung 6,12 gegen `vergehen`, das in es/fr/it identisch wäre |
| `Möglichkeit` | opportunity · oportunidad · possibilité · possibilità | B1 | **Lexikonfalle in Gegenrichtung** — die AT-Lesart ist *way · manera*, gemeint ist die NT-Lesart |
| `zehren` / `davon zehren` (MW) | feed · consumen · mangent · mangiano / live off it · viven de ello · en vivent · ne vivono | C1/B2 | **neu** — die einzige Bestandslesart (*eats away · ronge*) passt nicht |
| `zeugen` (von) | testifies · muestra · témoigne · testimonia | B2 | **neue Lesart** neben *begets*; keine Ausgabe übersetzt das Wort |
| `aus der Hand lassen` (MW) | let go of · soltar · lâcher · lasciar andare | B2 | **neu** |
| `Feiern` · `Knistern` · `Ausflucht` · `Missgeschick` · `Lebenstage` | feasting · fiesta · festin · convito / crackling · crepitar · crépitement · scoppiettio / excuses · evasivas · faux-fuyants · sotterfugi / … | B1/C1/C1/C1 | **neu** |
| `Erpressung` / `Bestechung` | extortion · extorsión · extorsion · estorsione / bribe · soborno · pot-de-vin · tangente | C1/B2 | Bestand, gegen alle vier Ausgaben |
| `Netz` / `Falle` / `Fessel` | net · red · filet · rete / trap · trampa · piège · trappola / shackles · grillos · entraves · ceppi | B1/B2/C1 | in 7,26 **alle drei im selben Vers**, in allen vier Sprachen getrennt |
| `gerecht` (adjektivisch) | righteous · justo · juste · giusto | B2 | 7,16 · 7,20 — die Buch-20-Vereinheitlichung auf *justly* gilt nur adverbial |
| `solange` (ohne Kollision) | as long as · mientras · tant que · finché | B1 | **nicht** die 2,3-Auflösung — die gilt nur, wo `während` oder `bis` daneben steht |

### Für Kapitel 9 vorgemerkt

`Netz` ist in 7,26 auf *net · red · filet · rete* gesetzt, `Falle` und `Fessel`
sind dort ebenfalls vergeben. Die für 9,12 gemeldete Kollision `Netz`/`Schlinge`
muss also mit einer **anderen** Ausweichlesart für `Schlinge` gelöst werden.

### Bestandsbefunde

- **`nützen` und `dienen` tragen dieselben drei romanischen Glossen** (*sirve ·
  sert · serve*) und stehen in 6,7/6,8 in benachbarten Versen.
- **`gottlos` und `Gottloser`** tragen beide *impío · impie · empio*; nur das
  Englische trennt (*godless* / *ungodly*). 7,15 und 7,17, verschiedene Verse.
- **`Arbeiter` liegt doppelt**: `Arbeiter` A2 = *workers · obreros* neben
  `Arbeitender` B2 = *laborer · trabajador*. Altlast, korpusweit fällig.
- **Korrektur an diesem Dokument**: `jeder` ist **A1**, nicht A2 (Abschnitt 10)
  — vom Bestand (756 Belege) und von `levelcheck.py` bestätigt.

### Prompt-Hinweise, die im Text nicht stehen

Kapitel 5: `Unterdrückung` und `Beamte` (der Text hat das Verb `unterdrückt`
und die dreistufige Steigerung `Hoher`/`Höherer`), `Erbe` steht nirgends, und
es heißt `Geschenk Gottes`, nicht `Gabe`. Kapitel 6: `tausend Jahre` und
`zweimal` (der Text sagt **`zweitausend`**, ein Wort), `Verlangen` (es heißt
`Begierde`), `Streit` (es ist das Verb). Kapitel 7: **acht Stück** — `Name`,
`Salböl`, `Todestag`, `Geburtstag`, `Trauerhaus`, `Festhaus`, `Kummer`,
`Hochmut`, `Rechnung`, `Fallstrick` heißen im Text alle anders.

### Zwei weitere Importartefakte in RIV

**5,4 `dempi`** (das *a* von *adempi* fehlt) — nach 1,13, 2,10, 2,12 und 3,22
das fünfte. Dazu in 7,14 „l'uno come 'altro" und 7,18 „chi teme ddio", die aber
keine Glosse berühren.

## 12. Was die Kapitel 8, 9 und 10 festgelegt haben

### 8,14 — die einzige Vier-Sprachen-Kollision des Buches

`geschieht` und zweimal `ergeht` stehen im selben Vers, und beide Lemmata
tragen im Bestand *happens · sucede · arrive · accade*. **Drei der vier
Ausgaben schreiben genau die Kollisionswörter** (WEB *is done … it happens*,
RV *ocurre … les sucede*, LSG *a lieu … il arrive*); nur RIV weicht aus, und
zwar durch Umformulierung, nicht lexikalisch.

`geschehen` ist die Buchbindung und kann nicht ausweichen. Gelöst mit **zwei
belegten Lesarten**, nichts erfunden:

| | en · es · fr · it | Level | Beleg |
|---|---|---|---|
| `geschehen` | happens · sucede · arrive · accade | B1 | unverändert |
| `ergehen` (Einzelwort) | goes · va · va · va | C1 | Ps 49,14 — formgleich, dieselbe Person, dasselbe Tempus |
| `es ergehen` (Mehrwort) | it goes · les va · il en va · va loro | C1 | Hiob 8,13 · Ps 49,14 · Spr 1,19; it nach Ps 73,3 auf den Plural-Dativ angepasst |

**Der Mehrwort-Eintrag trägt hier die eigentliche Arbeit**: „denen ergeht es"
ist ein Funktionsverbgefüge, dessen Sinn sich aus den Teilen nicht ergibt.
Prediger 2,15 führt ihn bereits — dort stand kein `geschehen` daneben.

### 9,12 — `Netz` ↔ `Schlinge`, und alle naheliegenden Auswege waren vergeben

Kapitel 7 hatte in 7,26 drei Fangwörter in **einem** Vers gesetzt (`Netz`
*filet*, `Falle` *piège*, `Fessel` *entraves*). `Schlinge` brauchte also eine
vierte Lösung — und der Bestand führt sie: **drei** Lesarten, darunter
*snares · lazos · **lacets** · lacci* (Ps 140,6).

| deutsch | en · es · fr · it | Level |
|---|---|---|
| `Schlinge` | snare · lazo · lacet · laccio | B2 |

Nur das Französische weicht aus; *lacet* schreibt LSG selbst in Ps 140,6. Die
vier Fangwörter des Buches sind damit durchgehend getrennt.

Im selben Vers steckte eine **zweite, ungemeldete Kollision**: `fangen` (Fische)
↔ `verfangen` (Vögel), im Bestand beide *caught · atrapado · pris · preso*.

### 9,4 `Lebender` ↔ `lebendig` — bleibt bewusst stehen

`glosskollision.py` stuft es als stärksten Verdacht ein („1 von 4"), und es
bleibt trotzdem: die Bedeutung ist **identisch** (beide sagen „am Leben"),
drei Sprachen trennen von selbst, **alle vier Ausgaben wiederholen ihr eigenes
Wort**, und eine englische Ausweichform (*a live dog*) würde eine
Unterscheidung behaupten, die der Vers gerade nicht macht — die Wiederholung
ist die Pointe.

Das ist der Gegenfall zu Spr 8,13 (`Böse`/`böse`), wo Substantiv und Adjektiv
**verschiedene Dinge** meinen und deshalb aufgelöst wurde.

### Die weiteren gemeldeten Kollisionen

| Vers | Paar | Befund |
|---|---|---|
| 8,11 | `Böse` ↔ `böse` | echt, nur en — genau die Spr-8,13-Konstellation. Das Adjektiv weicht auf *wicked* aus (Est 7,6) |
| 8,12 | `dennoch` ↔ `doch` | echt, nur es. `dennoch` hat **nur eine** Lesart (10 Belege *sin embargo*), also weicht `doch` aus: *ciertamente* (1Mo 19,19) |
| 8,17 | `desto` ↔ `mehr` | echt und **schärfer als gemeldet**: `Je`, `mehr` und `desto` wären französisch **alle drei** *plus*. Gelöst nach 3Mo 25,16 mit vier verschiedenen Wörtern (*Plus · davantage · d'autant · moins*) |
| 10,13 | `Torheit` ↔ `Unsinn` | Kapitel-1-Lösung übernommen; `Wahnsinn` kommt in Kapitel 10 nicht vor, die befürchtete zweite Kollisionsstelle entsteht nicht |

**`Je mehr … desto weniger` ist keine Mehrwort-Wendung.** Der Bestand führt
`je mehr` und `desto mehr`, aber **`desto weniger` gibt es nicht**.

### Weitere Festlegungen

| deutsch | en · es · fr · it | Level | Herkunft |
|---|---|---|---|
| `Ehrfurcht haben` (MW) | revere · veneran · révèrent · riveriscono | C1 | Auflösung 8,12 — Kapitel 3 hatte es mit **denselben** Glossen wie `fürchten` gesetzt |
| `Fehler` | mistake · error · faute · errore | A2 | **Lexikonfalle in Gegenrichtung** — die AT-Bindung ist *defect* (das fehlerhafte Opfertier von 3Mo 22,19) |
| `Salböl` (10,1) | anointing oil · aceite perfumado · huile parfumée · olio profumato | C1 | zweite Bestandslesart (Spr 27,9) — das Öl des Salbenmischers, nicht das kultische |
| `Amt` | office · cargo · charge · carica | B2 | die weltliche der zwei Bestandslesarten |
| `Frau` (9,9) | wife · esposa · femme · moglie | A1 | **nicht** die 7,26/7,28-Lesart — hier ist die Ehefrau gemeint |
| `Schneller` · `Kundiger` · `Zufall` · `Planen` · `Belagerungswerk` · `Gehör finden` (MW) | … | B1/B2/B2/B2/C1/B2 | **neu** (9,10–9,14) |
| `Fliege` · `faulig` · `Gelassenheit` · `Fähiger` · `bösartig` · `geflügelt` | … | B1/B2/C1/B2/C1/B2 | **neu** (Kapitel 10) |
| `Härte` · `Entlassung` · `anstrengen` | hardness · dureza · dureté · durezza / discharge · licencia · congé · congedo / exerts · esfuerza · efforce · sforza | B2 | **neu** (Kapitel 8) — bei den ersten beiden **weicht LSG ab** und wurde nicht befolgt |
| `scheuen` · `gewinnen` (Rennen) · `ziehen` (marschieren) · `erleiden` | shuns · rehúye · redoute · rifugge / win · ganan · gagnent · vincono / marched · marchó · marcha · marciò / suffer · sufren · subissent · subiscono | C1/B1/A2/B2 | **neue Lesarten** |

**Drei Bindungen gegen die Ausgaben** in Kapitel 8: `Urteil` = *judgment*
(alle vier schreiben *sentence*), `Weg` = *way* (WEB *procedure*, LSG/RIV
*jugement*), `Atem` = *breath* (WEB *spirit*, RV *espíritu*, die Entscheidung
aus Kapitel 3). In 10,3 lesen **WEB, LSG und RIV „die Reichen"**, nur RV folgt
dem deutschen `Fähige`.

### Bestandsbefunde

- **`BINDUNGEN_AT.md` führte für `Netz` die falsche Lesart** — der Agent von
  Kapitel 9 hat es gemeldet. Kein Generatorfehler, sondern ein Wartungsfehler:
  die Tabelle stammte aus einem Bestand von 14 AT-Belegen, inzwischen sind es
  31, und die Mehrheit hat sich vom Fettnetz zum Fischernetz gedreht. Tabelle
  neu erzeugt; von 1127 gemeinsamen Lemmata haben **elf** eine andere Lesart,
  inhaltlich schwer sind `Netz` und `Mal` (*mark* → *time*).
- **`Kraft` (A2) und `Stärke` (B1)** tragen in en und fr dieselbe Glosse —
  9,10/9,16, verschiedene Verse.
- **Buch 21 führt `es geben` und `es gibt` als zwei Lemmata nebeneinander**
  (1,9 gegen 3,12). Durchgehend `es geben` gesetzt, die Zitierform mit 105+
  Belegen.
- `Voraus`/`voraus` und `Arbeiter`/`Arbeitender` liegen ebenfalls doppelt.

### Prompt-Hinweise, die im Text nicht stehen

Kapitel 8: `Herrscher` steht nirgends im Kapitel (im Prediger erst 10,5),
`Lebenstage` nicht in 8,15 (dort „alle Tage seines Lebens", drei Wörter),
`gottlos` als Adjektiv **gar nicht** — alle vier Stellen sind das
substantivierte `Gottloser`, die im Prompt genannte englische Trennung wird
nicht gebraucht. Kapitel 9: sechs Wörter heißen anders (`Neid` statt
`Eifersucht`, `Anerkennung` statt `Gunst`, `Klugen` statt `Verständige`,
`Kriegswaffen` statt `Kriegsgerät`), und **9,18 sagt nicht „besser als
Stärke"** — das steht nur in 9,16. Kapitel 10: `Brot` steht in 10,19 nicht,
`Edler` ist ein Adjektiv, 10,9 hat kein `Eisen`.

### Das sechste und siebte Importartefakt in RIV

**8,13 `erché`** (das *p* von *perché* fehlt) und **9,5 `oiché`** (dasselbe
Wort wie in 2,10). Damit sind es in diesem Buch sieben: 1,13 · 2,10 · 2,12 ·
3,22 · 5,4 · 8,13 · 9,5.
