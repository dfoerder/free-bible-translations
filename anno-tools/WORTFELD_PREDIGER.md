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

Das Deutsche folgt in 4/5 dem Französischen (die Kapitelgrenze liegt anders),
in 11/12 dem Rest. **`ausgaben.py` ist in diesen vier Kapiteln zwingend**, und
wo es `FEHLT in der Datei der Ausgabe` schreibt, gibt es dort keine Vorlage.
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
