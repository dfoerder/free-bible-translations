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
