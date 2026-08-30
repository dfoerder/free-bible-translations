# Wortfeld des Hoheliedes — was vor dem ersten Kapitel feststeht

Buch 22, 8 Kapitel, 117 Verse, 2352 Tokens. Das kürzeste Buch der Reihe und
zugleich das dichteste: ein Wechselgesang zweier Liebender mit **sieben
buchinternen Dubletten**, drei davon wörtlich gleich.

Alle Zahlen sind aus dem fertigen Bestand ausgezählt.

## 1. Eine verschobene Kapitelgrenze zwischen 6 und 7

| Kapitel | de | en | es | fr | it |
|---|---|---|---|---|---|
| 6 | 12 | **13** | **13** | 12 | **13** |
| 7 | 14 | **13** | **13** | 14 | **13** |

Vers für Vers nachgemessen:

- **de 7,1 = WEB/RV/RIV 6,13** („Kehr zurück, kehr zurück, Sulamith!")
- danach **de 7,n = WEB/RV/RIV 7,n−1** durchgehend
- **LSG folgt dem Deutschen** (fr 7,n = de 7,n)

Das ist das Spiegelbild von Prediger 4/5, wo das deutsche Kapitel eine Zeile
später endete. Die übrigen sechs Kapitel stimmen in allen fünf Ausgaben überein.

**Achtung bei `ausgaben.py`:** bei einer verschobenen Kapitelgrenze ist der
global geschätzte Versatz am Kapitelanfang 0 und kippt erst später. Wenn das
Werkzeug `UNSICHER` meldet, kann auch die **Anzeige** falsch sein (so geschehen
in Prediger 11) — dann die Kapiteldatei der Ausgabe direkt aufschlagen.

## 2. `Geliebter` und `Geliebte` — dasselbe Lemma, entgegengesetztes Genus

Das Leitwort des Buches. **39 Vorkommen** (`Geliebter` 22×, `Geliebten` 9×,
`Geliebte` 8×) — und der Bestand kennt es neunmal, davon nur drei im AT.

Die beiden Liebenden nennen einander mit demselben deutschen Wort:

- **maskulin** = der Mann, von der Frau gesprochen (1,13 · 1,16 · 2,16 · 5,16 …)
- **feminin** = die Frau, vom Mann gesprochen (1,15 · 2,10 · 4,1 …)

**In 2,10 stehen beide im selben Vers**: „Mein **Geliebter** hebt an … Steh
auf, meine **Geliebte**". `hints.py` meldet das als Kollision, und es ist eine —
aber **nur im Englischen**. Spanisch, Französisch und Italienisch trennen über
das Genus.

Die vier Ausgaben trennen alle vier, jede anders:

| | maskulin (der Mann) | feminin (die Frau) |
|---|---|---|
| WEB | beloved | **my love** |
| RV1909mod | amado | amada |
| LSG1910 | bien-aimé | **amie** |
| RIV1927 | **amico** | **amica** |

Der Bestand bindet `Geliebter` an *beloved · amado · bien-aimé · amato* (9
Belege, u. a. 5Mo 33,12 und Ps 45,10). **Kapitel 1 entscheidet**, ob die
maskuline Form dabei bleibt und welche Glosse die feminine bekommt; RIVs
*amico/amica* („Freund/Freundin") ist die Wahl **einer** Ausgabe gegen eine
Bestandsbindung.

Zusätzlich stehen im Buch `Freund` (1×), `Freundin` (1×) und `Freunde` (2×) —
in 5,16 sogar **`Geliebter` und `Freund` im selben Vers**. Die Glosse für
`Freund` muss sich also von beiden Geliebten-Formen unterscheiden.

## 3. Sieben buchinterne Dubletten — die Refrains des Buches

| Paar | Ähnlichkeit | Text |
|---|---|---|
| **2,6 ↔ 8,3** | wörtlich gleich | „Seine Linke ist unter meinem Haupt" |
| **2,7 ↔ 3,5** | wörtlich gleich | „Ich beschwöre euch, ihr Töchter Jerusalems" |
| **2,16 ↔ 6,3** | wörtlich gleich | „Mein Geliebter ist mein, und ich bin sein" |
| 4,2 ↔ 6,6 | 0,91 | „Deine Zähne sind wie eine Herde …" |
| 2,7 ↔ 8,4 | 0,83 | der Beschwörungsrefrain, dritte Fassung |
| 3,5 ↔ 8,4 | 0,83 | dieselbe |
| 4,5 ↔ 7,4 | 0,77 | „Deine beiden Brüste sind wie zwei Kitze" |

Die Paketreihenfolge ist danach gebaut: **jede Vorlage ist fertig, bevor der
abhängige Vers läuft.**

## 4. Kollisionen im selben Vers — was `hints.py` meldet

Nur acht Paare, deutlich weniger als in den Sprüchen (30) oder im Prediger (22).
**Die Liste ist nicht vollständig**, und die Erfahrung der beiden Vorgängerbücher
sagt, dass `glosskollision.py` mehr echte findet.

| Paar | Stellen | Sprachen |
|---|---|---|
| `beide` ↔ `zwei` | 4,5 (+4 weitere) | **alle vier** |
| `Gasse` ↔ `Straße` | 3,2 | alle vier |
| `blicken` ↔ `sehen` | 2,9 | es/fr/it |
| `voll` ↔ `voller` | 5,2 | en/it |
| `Liebe` ↔ `lieben` | 1,4 | en |
| `schauen` ↔ `sehen` | 2,9 | en |
| `Geliebte` ↔ `Geliebter` | 2,10 | en — s. Abschnitt 2 |
| `loben` ↔ `preisen` | 6,9 | en |

**`beide` ↔ `zwei` in 4,5 ist die einzige Vier-Sprachen-Kollision** und steht
zugleich in einer Dublette (4,5 ↔ 7,4) — was dort entschieden wird, gilt für
beide Verse.

**`Liebe` ↔ `lieben` und `voll` ↔ `voller`** sind Substantiv-plus-Stammverb
bzw. Stammvarianten — in Buch 20 und 21 war das siebenmal ein Fall, der
bewusst stehen blieb. Erst am Vers entscheiden, und dabei prüfen, ob die
Ausgaben das Wort selbst wiederholen.

## 5. Das Sachvokabular ist dünn belegt

Das Buch lebt von Bildern, die im Bestand kaum vorkommen. Die häufigsten
Inhaltswörter mit ihrer AT-Belegzahl:

| deutsch | in Hld | AT-Bestand | Bindung |
|---|---|---|---|
| `Geliebter` | 39× | 3× (+6 NT) | s. Abschnitt 2 |
| `Liebe` | 17× | 18× | love · amor · amour · amore (A2) |
| `schön` | 12× | 17× | beautiful · hermosa · belle · bella (A1) |
| `Duft` | 7× | 26× | fragrance · aroma · parfum · profumo (B2) |
| `Myrrhe` | 7× | 5× | myrrh · mirra · myrrhe · mirra (C1) |
| `Lilie` | 6× | 4× | lilies · lirios · lis · gigli (B2) |
| `Braut` | 6× | **1×** | bride · novia · épouse · sposa (B1) |
| `Brust` | 6× | **1×** | breasts · pechos · mamelles · mammelle (A2) |
| `lieblich` | 5× | **2×** | lovely · amables · aimables · amabili (B2) |
| `Gazelle` | 5× | **2×** | gazelle · gacela · gazelle · gazzella (B2) |
| `Schleier` | 4× | **1×** | veil · velo · voile · velo (B2) |
| `Zwilling` | 4× | **2×** | twins · gemelos · jumeaux · gemelli (B1) |
| `beschwören` | 4× | **0 (NT 3×)** | adjure · conjuro · adjure · scongiuro (C1) |

**`beschwören` ist im AT unbelegt** und trägt den Beschwörungsrefrain, der
dreimal im Buch steht (2,7 · 3,5 · 8,4) — eine der folgenreichsten
Festlegungen, und Kapitel 2 trifft sie.

126 Wortformen meldet `hints.py` als unbelegt. **Formbasiert** — in Buch 20
und 21 waren zusammen achtzehn davon längst im Bestand. Immer zusätzlich
`lexicon.py` fragen und bei Komposita das Grundwort suchen.

## 6. Die Eigennamen

`Salomo` (4×), `Jerusalem` (7×), `Libanon` (7×), `Sulamith` (2×), dazu
`Kedar`, `En-Gedi`, `Scharon`, `Hermon`, `Amana`, `Senir`, `Tirza`, `Karmel`,
`Damaskus`, `Baal-Hamon`, `Heschbon`, `Bat-Rabbim`. Die meisten sind im
Bestand belegt; **`Sulamith` ist es nicht** und steht in 7,1 — dem Vers, der
zugleich in der verschobenen Kapitelgrenze liegt.

Nach der Regel `AUFTRAG_AT.md` liefert **die Ausgabe den Namen**. `qa.py`
prüft Eigennamen und kennt 160.
