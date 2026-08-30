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
| `beschwören` | 4× | **9 AT + 4 NT** | adjure · conjuro · adjure · scongiuro (C1) |

> **KORREKTUR (nach Kapitel 2).** Diese Zeile stand hier zuerst mit
> „0 (NT 3×)" und der Behauptung, `beschwören` sei im AT unbelegt. **Das war
> falsch**, und zwar formbasiert falsch: nur die *Form* `beschwöre` ist im AT
> unbelegt. Das *Lemma* hat 13 Belege, neun davon im AT. Die Vorbereitung hat
> die Form gezählt statt das Lemma — genau der Fehler, vor dem dieses Dokument
> die Kapitelagenten warnt. Der Agent für Kapitel 2 hat es nachgeprüft und
> gemeldet, statt die Angabe zu übernehmen.

**`beschwören` trägt den Refrain** (2,7 · 3,5 · 8,4, dazu `beschwörst` in 5,9)
und zerfällt im Bestand in **drei Bedeutungsgruppen**:

| Lesart | Belege | Glossen |
|---|---|---|
| **feierlich bitten** | 1Kön 22,16 · 2Chr 18,15 · 1Kön 2,42 · Mt 26,63 · Mk 5,7 · 1Thess 5,27 · Apg 19,13 | *adjure · conjuro · adjure · scongiuro* |
| Zauberei (Totenbeschwörung) | 1Sam 28,7 · 28,8 | *conjure up · invocar · évoquer · evocare* |
| Zauberei (Schlangenbeschwörung) | Ps 58,6 · Pred 10,11 | *charm · encantar · charmer · affascinare* |
| beim Namen schwören | Jos 23,7 | *swear by · jurar por · jurer par · giurare per* |

**Gesetzt ist die erste Gruppe**, und zwar die Form aus **Mt 26,63** („Ich
beschwöre dich bei dem lebendigen Gott") — dieselbe Konstruktion, dieselbe
Person, dasselbe „bei X". Die **Lexikonfalle** wäre hier die Zauberei-Lesart
gewesen: sie hat mit `Beschwörer` (*exorcist*) und `Beschwörung`
(*incantation*) das dichtere Wortumfeld.

**RV1909mod ist die einzige Ausgabe, die nicht mitgeht**: sie schreibt in allen
drei Refrainversen *les ruego* („ich bitte euch"), nicht *conjuro*. Nach der
Regel „die Ausgabe liefert den Namen, der Bestand die Bedeutung" ist der
Bestand genommen. WEB (*adjure*) und RIV (*scongiuro*) sind deckungsgleich,
LSG schreibt *conjure*, hat aber in Mt 26,63 selbst *adjure*.

**Für 5,9** (`beschwörst`, 2. Sg.): *adjure · conjuras · adjures · scongiuri*.
Kapitel 5 lief parallel zu Kapitel 2 und hat dieselbe Reihe gesetzt — geprüft.

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

## 7. `Geliebter` / `Geliebte` — die Festlegung (aus Hld 1, gilt fuer alle 39 Stellen)

**maskulin `Geliebter`** (31x, der Mann) — Bestandsbindung, unveraendert:
`beloved · amado · bien-aimé · amato` (B2)

**feminin `Geliebte`** (8x, die Frau) — eigenes Lemma, wie im Bestand:
`love · amada · bien-aimée · amata` (B2)

### Begruendung

Der Bestand fuehrt beide bereits als **zwei Lemmata**. `Geliebter` hat 9 Belege,
darunter 3 im AT (5Mo 33,12 · Ps 45,10 · Ps 60,7), alle mit demselben Kern.
`Geliebte` hat 2 Belege (Roem 9,25), en/es/fr/it = *beloved · amada · bien-aimée · amata*.

Drei der vier Ausgaben schreiben maskulin genau die Bestandslesart
(WEB *beloved*, RV *amado*, LSG *bien-aimé*); nur RIV weicht mit *amico* ab.
**RIV zu folgen waere ein Fehler:** in 5,16 steht `Geliebter` neben `Freund`
(89 Belege, gebunden an *friend · amigo · ami · **amico***), in 5,2 neben
`Freundin` (*amiga · amie · **amica***). Mit *amato* ist beides kollisionsfrei.

Feminin wird nur **im Englischen** vom Bestand abgewichen, weil Englisch kein
Genus hat und in **2,10** beide Formen im selben Vers stehen. Genommen ist WEBs
eigenes Wort: WEB schreibt fuer die Frau durchgehend „my love" (1,9 · 1,15 ·
2,10 · 2,13 · 4,1 · 4,7 · 6,4), fuer den Mann „beloved". Die Glosse steht am
Nomen (*love*), das Possessivum traegt `meine`. es/fr/it bleiben beim Bestand
(*amada · bien-aimée · amata*) und trennen ueber das Genus — dort besteht
ueberhaupt keine Kollision, und *amie*/*amica* bleiben fuer `Freundin` frei.

### Nachgemessen am ganzen Quelltext

- `Geliebte` (fem) und `Liebe` stehen **nirgends** im selben Vers. Der einzige
  Vers mit beidem ist **5,8** („findet ihr meinen **Geliebten** … krank vor
  **Liebe**") — dort ist die Form **maskulin**, also *beloved* gegen *love*.
  Die englische Doppelbelegung von *love* erzeugt im ganzen Buch keine Kollision.
- `Geliebte` (fem) und `lieben`/`liebt` treffen nie zusammen.
- **5,9** hat `Geliebter` (Sg.) und `Geliebten` (Pl., „anderen Geliebten") im
  selben Vers: Numerusform bilden (*beloveds · amados · bien-aimés · amati*),
  Lemma bleibt `Geliebter`.
- **6,4** hat `Geliebte` (*love*) neben `lieblich` (*lovely*) — verschiedene
  Zeichenketten, kein Konflikt, nur optisch nah.

### Fuer Kapitel 5 vorgemerkt

`Freund` behaelt *friend · amigo · ami · amico* (89 Belege),
`Freundin` *friends/friend · amiga · amie · amica*. Beide sind mit dieser
Festlegung in 5,2 und 5,16 kollisionsfrei.

## 8. Kapitel 1 — was der Maszstab ergeben hat

**Die Prompt-Hinweise waren wieder der unzuverlaessigste Teil.** Sieben von
ihnen standen so nicht im Quelltext: `Salboel` (es steht `Salbe` + `Parfuem`,
`Salboel` kommt im ganzen Buch nicht vor), `Kuesse` (es ist `Kuessen` Dat.Pl.
plus das Verb `kuesse`), `lagern` (es ist `ruhen lassen`), „Wagen des Pharao"
(es ist `Pharaos Wagen`), `Ketten`/`Gold`/`Silber` (es sind `Ohrgehaenge`,
`Perlenkette`, `goldene`, `Silberpunkten`), `Nardenoel` (es ist `Narde` allein —
das Bestandslemma ist das Kompositum, hier neues Lemma).

**`hints.py` meldet fuer Kap. 1 zwanzig unbelegte Formen — siebzehn davon stehen
ueber den Stamm laengst im Bestand.** Wirklich unbelegt sind drei
(`Ohrgehaenge(n)`, `Stute`). Die 126 formbasiert unbelegten Formen des Buches
sind entsprechend zu lesen: erst `lexicon.py` ueber den Stamm, dann entscheiden.

### Vier Kollisionen, alle bewusst stehengelassen

- **1,4 `Liebe` / `lieben` (nur en, *love*)** — Substantiv + Stammverb, der
  dokumentierte Regelfall. WEB wiederholt das Wort selbst („praise your **love**
  … right to **love** you"), LSG die Wurzel (*amour* … *aime*). Beide Woerter
  tragen die staerksten Bindungen des Buches (`Liebe` 131x, `lieben` 47+31x).
- **1,2 `Kuessen` / `kuesse` (nur it, *baci*)** — dieselbe Klasse, von
  `hints.py` nicht gesehen (weil `Kuessen` formbasiert unbelegt ist), von
  `glosskollision.py` gefunden. RIV wiederholt das Wort selbst: „Mi **baci**
  egli de' **baci**". en/es/fr trennen ohnehin.
- **1,12 `ihren` / `seiner` (es *su*)** und **1,14 `aus` / `von` (es *de*)** —
  echte Verschmelzungen des Spanischen, ausdruecklich Nicht-Fehler.

Fuenf Funktionswort-Kollisionen wurden **aufgeloest**, alle in 1,4, wo vier
Praepositionen zusammenstehen: `mit` = *with·con·avec·con*, `in` =
*into·en·dans·in*, `an` = *in·por·en·per*, `Zu` = *To·A·À·A*.

### Befunde im Bestand, die ueber das Kapitel hinausreichen

- **`Vorhang` ist an die Stiftshuette gebunden** — alle 46 Belege sind der
  Heiligtumsvorhang (*curtain · velo · voile · velo*, also es/it „Schleier").
  In 1,5 sind es die **Zelttuecher** Salomos, parallel zu den Zelten Kedars:
  *curtains · cortinas · pavillons · padiglioni* (B2). Nicht korpusweit angefasst.
- **`Spur`** — die haeufigste Lesart (*footsteps · pasos · traces · orme*) stammt
  aus drei rein **menschlichen** Belegen. 1,8 sind Tierspuren: en/es auf die
  Lesart der Ausgaben (*tracks · huellas*), fr/it beim Bestand.
- **`Traube`** — 12 Belege, alle Weintraube. 1,14 „eine Traube Hennablueten" ist
  eine **Rispe**: zweite Lesart *cluster · racimo · grappe · grappolo*, worin
  alle vier Ausgaben uebereinstimmen. Level B1 bleibt.
- **`Schoenster`** hat genau einen Beleg (Ps 45,3) und ist maskulin. 1,8 ist
  feminin: eigenes Lemma **`Schoenste`** (B1) — nach demselben Vorbild, nach dem
  der Bestand `Geliebter` und `Geliebte` trennt. Steht auch in 5,9 und 6,1.
- **`am`** ist im Bestand mit 1184:10 eigenes Lemma, nicht `an`. Ein Mehrwort
  `am Mittag` gibt es **nicht** (anders als `am Morgen`/`am Abend`).

### Befunde in den Ausgaben — fuer das ganze Buch

- **WEB hat die Sprecherangaben als Fliesztext im Vers**: „Beloved" am Ende von
  1,1 · 1,4 · 1,11 · 1,15, „Lover" am Ende von 1,7 · 1,14 · 1,16, in 1,4 sogar
  mitten im Vers („…into his rooms. **Friends** We will be glad…"). Klares
  Importartefakt. Fuer die Ausrichtung harmlos, aber wer WEB Wort fuer Wort
  abzaehlt, verrutscht. **Betrifft alle acht Kapitel.**
- **RIV 1,5: „come i padiglioni di *alomone*"** — fehlendes S.
- **1,7 `Verschleierte`: nur WEB stuetzt den deutschen Text** („one who is
  veiled"); RV *una vagabunda*, LSG *une égarée*, RIV *una donna sperduta*
  folgen der Lesart „umherirrend". Der l1912mod sagt „Verschleierte", also
  *veiled woman · velada · voilée · velata*. Zusatzargument: im selben Vers
  steht `umherirren` — die romanische Lesart haette dort eine
  Vier-Sprachen-Kollision erzeugt.
- **1,2/1,4 `Liebe`: RV *caricias*, RIV *carezze*** („Liebkosungen"). Bestand
  gehalten — gewoehnliches Wort, feste Bindung.
- **1,10/1,11 `Ohrgehaenge`: LSG *colliers*, RIV *collane*** (Halsketten).
  Das deutsche Wort sind Ohrringe: *earrings · pendientes · boucles d'oreilles ·
  orecchini*. LSG/RIV zu folgen haette in 1,10 mit `Perlenkette` kollidiert.

### Neu festgelegtes Vokabular (Kap. 1, laeuft weiter)

| deutsch | Lemma | Lvl | en · es · fr · it | wo noch |
|---|---|---|---|---|
| Hohelied | `Hohelied` | C1 | Song of Songs · Cantar de los Cantares · Cantique des Cantiques · Cantico dei Cantici | 1,1 |
| Parfuem | `Parfüm` | B2 | perfume · perfume · essence · essenza | 1,3 |
| Verschleierte | `Verschleierte` | C1 | veiled woman · velada · voilée · velata | 1,7 |
| Schoenste | `Schönste` | B1 | most beautiful · más hermosa · plus belle · più bella | **5,9 · 6,1** |
| Stute | `Stute` | B2 | mare · yegua · jument · cavalla | 1,9 |
| Ohrgehaenge | `Ohrgehänge` | B2 | earrings · pendientes · boucles d'oreilles · orecchini | 1,10 · 1,11 |
| Perlenkette | `Perlenkette` | B2 | pearl necklace · collar de perlas · collier de perles · collana di perle | 1,10 |
| Silberpunkt | `Silberpunkt` | C1 | studs of silver · incrustaciones de plata · points d'argent · punti d'argento | 1,11 |
| verstroemen | `verströmen` | C1 | gives off · exhala · exhale · esala | 1,12 · **2,13** |
| Narde | `Narde` | C1 | nard · nardo · nard · nardo | 1,12 |
| Hennabluete | `Hennablüte` | C1 | henna blossoms · flores de alheña · fleurs de troëne · fiori di cipro | 1,14 |
| liebreizend | `liebreizend` | B2 | charming · encantador · charmant · incantevole | 1,16 |
| Traube (Rispe) | `Traube` | B1 | cluster · racimo · grappe · grappolo | 1,14 |
| Vorhang (Zelttuch) | `Vorhang` | B2 | curtains · cortinas · pavillons · padiglioni | 1,5 |
| Spur (Tierfaehrte) | `Spur` | B2 | tracks · huellas · traces · orme | 1,8 |

Aus dem Bestand bestaetigt und damit fuer das Buch gesetzt:
`Liebe` A2 *love·amor·amour·amore* · `lieben` A1 · `schoen` A1 · `lieblich` B2
*lovely·amables·aimables·amabili* · `Duft` B2 *fragrance·aroma·parfum·profumo* ·
`Myrrhe` C1 · `Brust` A2 *breasts·pechos·mamelles·mammelle* · `Weinberg` B1 ·
`Herde` B1 *flock(s)·rebaño(s)·troupeau(x)·gregge/greggi* · `weiden` C1 ·
`Zelt` B1 · `Lager` B1 (Liebeslager) *couch·lecho·couche·giaciglio* ·
`Taube` B1 · `Gefaehrte` B2 *companions·compañeros·compagnons·compagni* ·
`Salbe` C1 *ointments·ungüentos·onguents·unguenti* (auch 4,10) ·
`Toechter Jerusalems` = *daughters·hijas·filles·figlie* + *of Jerusalem·
de Jerusalén·de Jérusalem·di Gerusalemme* (Refrain 2,7 · 3,5 · 5,8 · 5,16 · 8,4).

Mehrwort-Eintraege, die wiederkehren duerften: `lass uns` A2 · `sich freuen` A2 ·
`mehr als` A2 · `zu Recht` B2 · `ansehen` B1 · `machen zu` B1 · `ruhen lassen` B1 ·
`machen wollen` A2.

## 9. Geschlichtet: `aus` / `von` — 1,14 bleibt stehen, 4,2 wird aufgeloest

Kapitel 4 hat die Kollision `aus`/`von` in **4,2** aufgeloest (`aus` =
*out of · **desde** · **depuis** · da*), waehrend Kapitel 1 sie in **1,14**
hat stehenlassen. Der Agent hat die Abweichung selbst gemeldet. Nachgeprueft:

**Kapitel 1 hatte in der Begruendung unrecht, im Ergebnis recht.**
Die Begruendung lautete, jede Ausweichloesung mit *desde* braeche „eine Bindung
mit fast tausend Belegen". Das stimmt nicht: der Bestand fuehrt `aus` in
**elf Lesarten**, darunter *from · **desde** · **depuis** · da* mit 14 Belegen
(2Mo 25,22 · 3Mo 1,1 · Ri 1,16 …). Ein Ausweichen bricht also gar nichts.

**Der Unterschied ist die Bewegung, und den entscheiden die Ausgaben.**

- **4,2** „die **aus** der Schwemme kommen" — RV *que suben **del** lavadero*,
  LSG *qui remontent **de** l'abreuvoir*. Es ist eine Bewegung mit Ausgangspunkt;
  *desde* / *depuis* sind dort idiomatisch. **Aufloesung richtig.**
- **1,14** „eine Traube Hennablueten **aus** den Weinbergen **von** En-Gedi" —
  RV schreibt *Racimo de flores de alheña **en** las viñas de Engadi*. Keine
  Bewegung, nur Herkunft. *desde las viñas* waere schlechtes Spanisch.
  **Stehenlassen richtig.**

**Regel:** `aus` weicht bei Kollision mit `von` auf *desde · depuis* aus —
**aber nur, wo eine Bewegung mit Ausgangspunkt vorliegt.** Bei blosser Herkunft
bleibt die Verschmelzung stehen; sie ist dort eine echte des Spanischen.

Fuer **6,6** gilt die Aufloesung weiter: der Vers ist gekuerzt, aber `aus der
Schwemme` und das erste `von ihnen` stehen beide noch da.

## 10. Paket 2 (Kap. 2 · 4 · 5) — was die Welle ergeben hat

### Die drei Dublettenverse, fertig zum Abschreiben

**2,6 → 8,3** (wörtlich): kein Mehrwort. `liegt` steht **indikativisch**
(*lies · está · est · sta*), obwohl LSG und RIV konjunktivisch formulieren —
der l1912mod sagt „liegt". `Kopf` it bleibt Bestand *testa* (RIV: *capo*).

**2,7 → 3,5** (wörtlich) **und → 8,4** (gekürzt, ohne „bei den Gazellen …
auf dem Feld"; für 8,4 die Positionen 6–13 streichen und neu zählen).
Kein Mehrwort `aufwecken` für „Weckt … auf": SPEC lässt Mehrwort nur zu, wo
sich die Bedeutung nicht aus den Teilen ergibt, und `aufwecken` verschiebt
gegenüber `wecken` nichts. Der Bestand führt alle drei `aufwecken`-Belege als
**ein** Token; für eine getrennte Klammer gibt es keinen Präzedenzfall.
`stört` bleibt am Bestand (*disturb · molestar · déranger · disturbare`),
obwohl **alle vier Ausgaben** dort ein zweites Weck-Verb setzen — das wäre eine
Vier-Sprachen-Kollision mit `Weckt` gewesen.

**2,16 → 6,3** (wörtlich): `zwischen` steht auf der **zweiten** Bestandslesart
*among · entre · parmi · tra* (1Sam 2,8), nicht auf der Mehrheitslesart
*between* — es sind mehr als zwei Lilien, und alle vier Ausgaben schreiben
among/entre/parmi/fra. `weidet` ist intransitiv (Spr 15,14, *grazes · pace ·
paît · pascola*); RV/LSG/RIV ergänzen ein Objekt, WEB nicht.

**4,2 → 6,6** und **4,5 → 7,4**: vollständig im Bericht des Kapitel-4-Agenten.
Für 6,6 gilt die `aus`/`von`-Auflösung weiter (§9).

### `beide` ↔ `zwei` in 4,5 — die einzige Vier-Sprachen-Kollision

**`beide` weicht aus** auf *both · ambos · les deux · entrambe* (A2),
**`zwei` bleibt** *two · dos · deux · due* (A1). Nur an dieser Stelle.

`zwei` hat 407 Belege in **genau einer** Lesart und kann nirgendwohin. `beide`
hat für die kollidierende Lesart 107 Belege, für *both · ambos · les deux ·
entrambi* aber **155** — die „both"-Lesart ist im Bestand sogar die Mehrheit.
Zusatzargument: **RV wiederholt das Zahlwort nicht** („Tus pechos, como dos
cervatillos"), das Kriterium „alle vier wiederholen das Wort selbst" greift
also nicht. **Gilt auch für 7,4.**

### Neu: zweite Lesarten bestehender Lemmata, bindend fürs ganze Buch

| Wort | Lemma | Lvl | en · es · fr · it | Anlass |
|---|---|---|---|---|
| Sieh (deiktisch) | `sehen` | A1 | Behold · He aquí · Voici · Ecco | 2,8 · 2,9 · 2,11 |
| blickt (durchs Gitter) | `blicken` | B1 | glances · observa · observe · osserva | 2,9 |
| hebt an (zu reden) | `anheben` | B2 | speaks up · habla · parle · parla | 2,10 |
| Anblick (Aussehen) | `Anblick` | B2 | appearance · semblante · figure · aspetto | 2,14 |
| Gitter (Fenstergitter) | `Gitter` | C1 | lattice · celosía · treillis · inferriata | 2,9 |
| zwischen (unter mehreren) | `zwischen` | A2 | among · entre · parmi · tra | 2,16 → **6,3** |
| hüpfend | `hüpfen` | B2 | skipping · brincando · bondissant · balzando | 2,8 |
| vorbei (Regen) | `vorbei` | A2 | over · cesado · cessé · finito | 2,11 |
| Fassung (Steinfassung) | `Fassung` | C1 | setting · engaste · chaton · castone | 5,12 — **nicht** *composure* |
| Erscheinung (Aussehen) | `Erscheinung` | B2 | appearance · aspecto · aspect · aspetto | 5,15 |
| fort (prädikativ) | `fort` | A2 | gone · ido · parti · andato | 5,6 (als Partikel 5,7: *away · lejos · loin · via*) |
| aus (bei Bewegung) | `aus` | A1 | out of · desde · depuis · da | 4,2 → **6,6**, siehe §9 |

### Neues Vokabular

| deutsch | Lemma | Lvl | en · es · fr · it | wo noch |
|---|---|---|---|---|
| Schöne | `Schöne` | B1 | beautiful one · hermosa · belle · bella | 2,10 · 2,13 |
| Apfelbaum | `Apfelbaum` | B1 | apple tree · manzano · pommier · melo | 2,3 · **8,5** |
| Weinsaal | `Weinsaal` | C1 | banquet hall · sala del banquete · maison du vin · casa del convito | 2,4 |
| Traubenkuchen | `Traubenkuchen` | C1 | raisin cakes · tortas de pasas · gâteaux de raisins · schiacciate d'uva | 2,5 |
| zerklüftet | `zerklüftet` | C1 | rugged · escarpados · escarpées · scoscesi | 2,17 |
| Scharon | `Scharon` | A1 | Sharon · Sarón · Saron · Saron | 2,1 |
| in Blüte stehen | `in Blüte stehen` | B2 | are in blossom · están en flor · sont en fleur · sono in fiore | 2,13 · 2,15 · **6,11 · 7,13** |
| Schwemme | `Schwemme` | B2 | washing place · lavadero · abreuvoir · lavatoio | 4,2 → **6,6** |
| Rehkitz | `Rehkitz` | B2 | fawns · cervatillos · faons · cerbiatti | 4,5 → **7,4** |
| Scheibe (Granatapfel) | `Scheibe` | B1 | slice · rodaja · tranche · fetta | 4,3 (**6,7** prüfen) |
| Schicht | `Schicht` | B2 | layers · capas · couches · strati | 4,4 |
| Myrrhenberg | `Myrrhenberg` | C1 | mountain of myrrh · monte de la mirra · montagne de la myrrhe · monte della mirra | 4,6 |
| Weihrauchhügel | `Weihrauchhügel` | C1 | hill of frankincense · colina del incienso · colline de l'encens · colle dell'incenso | 4,6 |
| Weihrauchbaum | `Weihrauchbaum` | C1 | frankincense trees · árboles de incienso · arbres à encens · alberi d'incenso | 4,14 |
| Safran | `Safran` | C1 | saffron · azafrán · safran · zafferano | 4,14 |
| Quell | `Quell` | B2 | fountain · fuente · fontaine · fonte | 4,12 |
| Gartenquell | `Gartenquell` | C1 | garden fountain · fuente de jardín · fontaine des jardins · fontana di giardino | 4,15 |
| herabströmen | `herabströmen` | B2 | flows down · corre · coule · scorre giù | 4,15 |
| Band (Faden) | `Band` | B2 | thread · hilo · fil · filo | 4,3 |
| Türspalte | `Türspalte` | C1 | door opening · abertura de la puerta · ouverture de la porte · apertura della porta | 5,4 |
| Feuchte | `Feuchte` | B2 | dampness · humedad · humidité · umidità | 5,2 |
| flüssig | `flüssig` | B2 | liquid · líquida · liquide · liquida | 5,5 · 5,13 |
| gewellt | `gewellt` | B2 | wavy · onduladas · ondulées · ondulate | 5,11 |
| herausragend | `herausragend` | C1 | outstanding · distinguido · distingué · distinto | 5,10 |
| rosig | `rosig` | B2 | ruddy · sonrosado · vermeil · vermiglio | 5,10 |
| Balsamkraut | `Balsamkraut` | C1 | balsam herbs · hierbas balsámicas · herbes balsamiques · erbe balsamiche | 5,13 |
| Makellose | `Makellose` | C1 | spotless one · inmaculada · immaculée · immacolata | 5,2 |

Substantivierte Adjektive bekommen ein **eigenes Lemma** (`Schöne`,
`Makellose`, dazu `Schönste` und `Verschleierte` aus Kapitel 1) — nach dem
Vorbild, nach dem der Bestand `Geliebter`/`Geliebte` und
`Schönster`/`Schönste` trennt.

### Zwei Homographen, die den Lauf gekostet hätten

- **`Weh` (4,16) ist nicht `Weh`.** Der Bestand führt `Weh` C1 mit 17 Belegen
  als Klageruf. In „**Weh** durch meinen Garten" ist es der **Imperativ von
  `wehen`** (B2, *Blow · Sopla · Souffle · Soffia*). Ein Abgleich über die
  Wortform hätte „Woe" gesetzt.
- **`erlesen` (5,15)** ist das Adjektiv (C1, Spr 8,19 · 10,20, *choice ·
  escogida · de choix · eletto*), nicht das Partizip von „lesen". `lexicon.py`
  zeigte es formbasiert nur unter VERWANDT neben `erleben`/`erledigen`.

### Vom Koordinator angeglichen (zwei Wellen-Divergenzen)

- **`sich abkühlen`**: der Halbvers „Bis der Tag sich abkühlt und die Schatten
  fliehen" steht **wörtlich gleich in 2,17 und 4,6** — eine Dublette, die
  `dubletten.py` nicht meldet, weil die Verse im Rest auseinandergehen. Die
  beiden Kapitel liefen gleichzeitig und setzten fr/it verschieden
  (*refroidisse/raffreddi* gegen *rafraîchisse/rinfreschi*). Die Bestandsbindung
  (1Mo 27,45: *refroidie · raffreddata*) entscheidet: **4,6 auf 2,17
  angeglichen.** Dasselbe Muster wie Prediger 5/6.
- **`Horch`** (2,8 und 5,2): en *Hark* gegen *Listen*. **Auf *Listen*
  angeglichen** — es passt zu den drei romanischen Glossen (*Escucha ·
  Écoute · Ascolta* = zuhören, nicht „horch") und entspricht der
  Register-Regel: nicht ins Altertümliche greifen. Keine der vier Ausgaben
  übersetzt das Wort überhaupt als Interjektion.

### Von den Agenten selbst gefunden, von keinem Skript gemeldet

`glosskollision.py` hat in dieser Welle **fünf** Kollisionen nicht gesehen, die
die Agenten durch eigenes Nachzählen fanden — vier davon **Vier-Sprachen**-Fälle:

- **5,6 `doch` ↔ `aber`** — beide *but · pero · mais · ma*. `doch` weicht auf
  *yet · sin embargo · pourtant · eppure* (138 Belege).
- **2,8 `springend` ↔ `hüpfend`** — beide *leaping · saltando*. Alle vier
  Ausgaben trennen; `hüpfend` → *skipping · brincando · bondissant · balzando*.
- **2,11 `vorüber` ↔ `vorbei`** — identischer Lesartensatz. `vorbei` (Regen) →
  *over · cesado · cessé · finito*.
- **2,9 `Sieh` ↔ `schaut` ↔ `blickt`** — drei Wörter des Sehens in einem Vers,
  alle drei im Bestand auf *look · mira · regarde · guarda*. `hints.py` meldete
  zwei der drei Paare.
- **5,1 `an` ↔ `mit`** (en beide *with*) und **5,12 `an` ↔ `in`**.

Dazu **2,10 `an` ↔ `auf`**, zwei **Verbpartikeln** im selben Vers — die Klasse,
vor der `AUFTRAG_AT.md` mit 2Kön 6,7 warnt, und die `hints.py` nicht meldete.

### Befunde in den Ausgaben

- **WEB-Sprecherangaben, für alle drei Kapitel bestätigt**: „Lover" am Ende von
  2,1 · 2,13, „Beloved" am Ende von 2,2 · 2,15 · 4,15 · 5,9, „Friends" am Ende
  von 5,8 und **mitten in 5,1**. Für 8,4 vorgemerkt: dort hängt „Friends" an.
- **RV1909mod benutzt im Hohelied durchgehend *ustedes*** (2,5 · 2,7 · 2,15 ·
  5,8), der Bestand die *vosotros*-Konvention. Bestand genommen — sonst liefe
  das Buch gegen die übrigen 65.
- **Zwei weitere RIV-Setzfehler** derselben Klasse wie „alomone" in 1,5:
  **5,6 „’ho cercato"** (fehlendes `l`) und **5,9 „l'amico uo"** (fehlendes `t`).
- **5,14** liest in **allen vier** Ausgaben anders als der l1912mod: „hands"
  statt `Arme`, „rings" statt `Stäbe`, „beryl" statt `Türkis`. Deutsch + Bestand.
- **2,17 „zerklüfteten Bergen"**: WEB transliteriert („mountains of Bether"),
  die drei anderen übersetzen. Der deutsche Text hat ein Adjektiv, keinen
  Namen — **nicht** als Eigenname geglossiert.
- **LSG 2,9** ist die einzige Ausgabe, die `schaut` und `blickt` nicht trennt
  (zweimal *Il regarde*).
- **`Hirschkuh` en:** Bestand hat *does*, gesetzt ist **WEBs *hinds***. `does`
  ist im Englischen ein Homograph mit der Verbform — die Ausnahmeklasse
  „Carcass"/„Carcas" aus `AUFTRAG_AT.md`, eine echte Kollision im Lesefluss.

### Hinweis für Paket 4

**2,17 ↔ 8,14, Ähnlichkeit 0,63** — von `dubletten.py` **nicht** geführt (die
Schwelle ist nur einseitig erfüllt), von `parallelen.py` gefunden. Gemeinsamer
Block von 12 Tokens: „mein Geliebter sei wie eine Gazelle oder ein junger Hirsch
auf den". 8,14 beginnt mit „Eile" und endet auf „Bergen voller Gewürze".

## 11. Paket 3 (Kap. 3 · 6 · 7) — was die Welle ergeben hat

### Werkzeugfehler: `ausgaben.py` hat für Kapitel 6 lautlos falsch ausgerichtet

Der Agent für Kapitel 6 hat gemeldet, dass `ausgaben.py` fuer Hld 6 **Versatz +1**
fuer en/es/it anzeigt — ohne `UNSICHER`-Marke — und damit **jede** deutsche Zeile
mit der falschen fremdsprachigen paart. Nachgemessen: Versatz **0** bewertet
0,09–0,14, der angezeigte +1 bewertet 0,24–0,29.

Die Ursache ist strukturell. Der Versatz kommt aus dem letzten Vers. Hat eine
Ausgabe **einen Vers mehr**, weil ihre Kapitelgrenze weiter hinten liegt, schiebt
diese Rechnung den Ueberhang nach **vorn**. Die vorhandene Kontrolle
(`len(de) + versatz == len(ausgabe)`) stimmt in **beiden** Faellen und greift nie.

`ausgaben.py` bewertet jetzt die Nachbarversaetze mit und meldet, wenn einer
deutlich besser liegt (Commit `e1604ba`). Der angewandte Versatz wird **nicht**
stillschweigend ausgetauscht — genau das lag in Ps 9, 15 und 19 daneben. Die
Schwelle ist an fuenf Kapiteln geeicht; ueber alle 939 fertigen Kapitel melden
4,9 % etwas, **17 Ausgabenzeilen davon waeren vorher voellig stumm geblieben**,
darunter **Prediger 4**, das denselben Fehler traegt.

**Gemessene Verszaehlung des Hoheliedes** (nicht geschaetzt, abgezaehlt):

| | de | en | es | fr | it |
|---|---|---|---|---|---|
| Kap. 6 | 12 | 13 | 13 | 12 | 13 |
| Kap. 7 | 14 | 13 | 13 | 14 | 13 |

- **Kap. 6**: 6,1–6,12 stehen in allen fuenf Texten 1:1. Versatz **0**, nicht +1.
  Der 13. Vers von en/es/it ist de 7,1.
- **Kap. 7**: de 7,1 = deren **6,13**; danach de 7,n = deren 7,n−1. **LSG folgt
  dem Deutschen.** RIV traegt die deutsche Zaehlung selbst im Text mit
  („(7:1) Torna, torna, o Sulamita" steht unter 6,13).

### Vom Koordinator angeglichen (drei Wellen-Divergenzen)

- **„zwischen den Lilien weiden"** steht wortgleich in **2,16 · 4,5 · 6,3**.
  Kapitel 2 setzte `zwischen` = *among · entre · **parmi** · tra* (zweite
  Bestandslesart, 1Sam 2,8 — es sind mehr als zwei Lilien), Kapitel 4 nahm die
  Mehrheitslesart *between · entre · **entre** · tra*. Die Ausgaben entscheiden:
  WEB *among the lilies*, LSG *au milieu des lis*, RIV *fra i gigli*.
  **4,5 auf 2,16 angeglichen.**
- **`Weinstock` fr** in **6,11** gegen **7,13**: *vigne* gegen *cep*. Bestand
  19:6 fuer *cep/ceps*, und Hld 2,13 steht bereits auf *ceps*. Dazu: in 7,13
  steht `Weinberg` (*vignes*) im selben Vers — mit *vigne* eine franzoesische
  Kollision. **6,11 auf *cep* angeglichen.**
- **`ausschlagen`** in denselben beiden Versen: *sprouts · brota · bourgeonne ·
  germoglia* gegen *is budding · brota · pousse · sboccia*. WEB schreibt
  „has budded", LSG in **beiden** Versen „la vigne pousse"; *bourgeonne* und
  *germoglia* stehen in keiner Ausgabe. **6,11 auf die Reihe aus 7,13
  angeglichen.**

Der gemeinsame Block „sehen, ob der Weinstock ausschlaegt, ob die Granatbaeume
bluehen" (6,11 ↔ 7,13) wird von `dubletten.py` **nicht** gefuehrt, nur von
`parallelen.py`. Das ist nach `sich abkuehlen` (2,17 ↔ 4,6) der **zweite** Fall
im Buch, in dem gleichzeitig laufende Kapitel an einem Teilvers kollidieren,
den kein Dublettenwerkzeug meldet.

### Entscheidungen, die ueber ihr Kapitel hinausreichen

- **`Gasse` / `Straße` (3,2)** — die einzige Stelle im Buch. `Straße` hat 45
  Belege, `Gasse` 2. **`Gasse` weicht** auf seine eigene Bestandslesart
  (Lk 14,21): *alleys · callejones · ruelles · vicoli* (B2).
  Befund: **die vier Ausgaben verteilen genau umgekehrt** — sie geben
  *streets/calles/rues/strade* an `Gassen` und *squares/plazas/places/piazze* an
  `Straßen`. Ihnen zu folgen haette fuer das mit 45 Belegen gebundene `Straße`
  eine „Platz"-Lesart erfinden muessen, die das deutsche Wort nicht hat.
- **`loben` / `preisen` (6,9)** — `loben` hat ~110 Belege **ausnahmslos** in der
  *praise*-Familie und kann nicht weichen. **`preisen` weicht** auf seine
  zweite Bestandslesart: *extolled · glorificaron · glorifièrent · glorificarono*
  (Mt 15,31 · 1Chr 16,4). Nur en musste bewegt werden.
- **`Sulamith` (7,1, 2×)** — im Bestand unbelegt, nicht gedeutet. Schreibung der
  Ausgaben: *Shulammite · sulamita · Sulamithe · Sulamita* (A1). Spanisch
  **klein**, weil RV es als Gentiliknomen setzt.
- **`zurückkehren`, nicht `umkehren` (7,1)** — der Text sagt viermal „Kehr
  zurueck", die Partikel ist `zurück`. Bestand hat `zurückkehren` mit ueber 130
  Belegen: *Return · Vuelve · Reviens · Torna*, in allen vier Ausgaben woertlich.
  Bauweise wie 2,17: Mehrwort plus eigenstaendige Einzeleintraege.

### Eine feste Wendung, die drei Skripte uebersehen haben

**6,9 „priesen sie glücklich"** ist `glücklich preisen` — **im Bestand gefuehrt**
(C1, Hiob 29,11 · Ps 72,17 · Spr 31,28), und Spr 31,28 hat sogar exakt dieselbe
Konstellation (3. Pl., femininer Objektbezug): *call blessed · llaman dichosa ·
disent heureuse · proclamano beata*. Weder `sweep.py` noch `konvention.py` noch
`hints.py` haben sie gemeldet. Als `parts`-Eintrag gesetzt.

### Befunde im Bestand

- **`Rauchsäule` ist ein volles Bestandslemma** (C1, Ri 20,38 · 20,40), ebenso
  `Lehne`, `heraufsteigen` (8 Belege) und `vorübergehen` (15) — `hints.py`
  meldete fuer Kapitel 3 sechs „unbelegte" Formen, **wirklich neu waren zwei**.
- **`purpurn` und `Königsgewand`** (7,2) zeigte der Lexikon-Auszug **nicht**,
  auch nicht unter VERWANDT — nur `fixgloss.py show` fand sie. Von 18
  „unbelegten" Formen in Kapitel 7 waren 6 laengst im Bestand.
- **`ausschlagen` hatte im ganzen Bestand nur *knocks out*** (2Mo 21,27, einen
  Zahn ausschlagen) — ein glatter Homograph zu „austreiben". Zweite Lesart neu.
- **`Schale` (7,3)**: `BINDUNGEN_AT.md` fuehrt *basin · vasija · bassin · bacino*
  und markiert *bowl* als NT-Falle. Hier ist es ein **Trinkgefaess**; die
  *bowl*-Lesart hat 10 Belege, darunter Ri 5,25 im AT. **Die Tabelle ist an
  dieser Stelle bedeutungsblind.**
- **`kaum` (3,4)**: `BINDUNGEN_AT.md` nennt it *a malapena* (8/14), die
  **grossgeschriebene** Form hat aber 10 Belege mit *Appena*. **Die Tabelle ist
  positionsblind.**
- **`Garten` Plural** ist im Bestand an *jardines* gebunden (2 Belege), der
  Singular an *huerto* (25). In **6,2 stehen beide im selben Vers**; Plural auf
  *huertos* gesetzt, damit der Vers nicht in sich den Stamm wechselt. Abweichung
  von einem Zwei-Beleg-Lemma, gemeldet, nicht korpusweit angefasst.
- **`Teich` (7,5)** ist gespalten (11× *pool/piscine*, 3× *étang/stagno*,
  2× Plural *ponds/étangs*). Lemmamehrheit im Plural genommen; **LSG schreibt
  hier *étangs* und weicht damit von sich selbst ab** (anderswo „piscine").
- **`Ehe` (6,12)** ist der Homograph: nicht `Ehe` B1 *marriage* (24 Belege),
  sondern die Konjunktion `ehe` A2 (Hiob 15,32).
- **`versehen` passt in 6,12 in keiner seiner 14 Lesarten** — „Ehe ich mich
  versah" ist das Reflexivum; `sich versehen` war unbelegt, neu als Mehrwort.

### Befunde in den Ausgaben

- **WEB hat in Kapitel 3 als einzigem Kapitel *keine* Sprecherangaben** (alle
  11 Verse durchsucht). Sonst bestaetigt: „Beloved" 6,1 · 7,8, „Friends" 6,12,
  „Lover" mitten in ihrem 6,13 (= de 7,1).
- **Drei neue RIV-Setzfehler**, jetzt sechs insgesamt: **3,11** „il *iorno*"
  (fehlendes g), **7,2** und **7,4** je „*e*" statt „è". Dazu die bekannten
  „alomone" (1,5), „’ho cercato" (5,6), „l'amico uo" (5,9).
- **Alle vier Ausgaben ziehen `Helden` und `Krieger` in 3,7 zu einem Wort
  zusammen** („mighty men … mighty men"). Der Bestand trennt (*heroes* /
  *warriors*) — Bestand gehalten, sonst eine Vier-Sprachen-Kollision.
- **7,6 zweite Vershaelfte liest in allen vier Ausgaben anders** als der
  l1912mod: dort ist ein Koenig in den Locken gefangen, im Deutschen ist das
  Haar „in Locken gebunden". Deutsch + Bestand.
- **7,1 `Lager`**: WEB transliteriert („the dance of Mahanaim"), die drei
  anderen uebersetzen. Der deutsche Text hat kein Eigennamen-Signal
  („zweier Lager") — wie 2,17 „zerklueftete Berge" **nicht** als Name geglossiert.
- **6,12 `meines edlen Volkes`**: RIV liest „ai carri d'**Amminadab**" — ein
  Eigenname, wo die anderen drei und der l1912mod ein Attribut haben.
- **6,8 `Jungfrauen`**: nur WEB hat *virgins*, die drei romanischen lesen „junge
  Frauen". Bestand (27 Belege) genommen.

### Neues Vokabular

| deutsch | Lemma | Lvl | en · es · fr · it | Stelle |
|---|---|---|---|---|
| Sänfte | `Sänfte` | C1 | carriage · litera · litière · lettiga | 3,7 · 3,9 |
| umduften | `umduften` | C1 | perfumed · perfumada · parfumée · profumata | 3,6 |
| Lehne | `Lehne` | B2 | backrest · respaldo · dossier · spalliera | 3,10 (2. Lesart) |
| Blumenbeet | `Blumenbeet` | B2 | flower beds · canteros de flores · parterres de fleurs · aiuole di fiori | 6,2 |
| Nussgarten | `Nussgarten` | C1 | nut orchard · huerto de nogales · jardin des noyers · giardino dei noci | 6,11 |
| Granatbaum | `Granatbaum` | B2 | pomegranate trees · granados · grenadiers · melograni | 6,11 · 7,13 |
| einzigartig | `einzigartig` | B2 | unique · única · unique · unica | 6,9 |
| Einzige | `Einzige` | B1 | only one · única · seule · unica | 6,9 |
| Auserwählte | `Auserwählte` | C1 | chosen one · elegida · élue · eletta | 6,9 |
| Gebärerin | `Gebärerin` | C1 | birth mother · progenitora · génitrice · genitrice | 6,9 |
| sich versehen | `sich versehen` | C1 | realized it · me diera cuenta · m'en aperçoive · me ne accorgessi | 6,12 |
| Sulamith | `Sulamith` | A1 | Shulammite · sulamita · Sulamithe · Sulamita | 7,1 |
| Fürstentochter | `Fürstentochter` | B2 | prince's daughter · hija de príncipe · fille de prince · figlia di principe | 7,2 |
| Rundung | `Rundung` | B2 | curve · curva · contour · contorno | 7,2 |
| Meisterhand | `Meisterhand` | C1 | a master's hand · mano de maestro · main de maître · mano di maestro | 7,2 |
| Nabel | `Nabel` | B2 | navel · ombligo · nombril · ombelico | 7,3 |
| Würzwein | `Würzwein` | C1 | spiced wine · vino especiado · vin épicé · vino speziato | 7,3 |
| Weizenhaufen | `Weizenhaufen` | B2 | heap of wheat · montón de trigo · tas de blé · mucchio di grano | 7,3 |
| Bat-Rabbim | `Bat-Rabbim` | A1 | Bathrabbim · Bat-rabim · Bath-Rabbim · Bath-Rabbim | 7,5 |
| Wuchs | `Wuchs` | B2 | stature · talle · taille · statura | 7,8 |
| erklimmen | `erklimmen` | C1 | climb up · subir · monter · salire | 7,9 |
| Schlafender | `Schlafender` | B2 | sleeping ones · dormidos · endormis · dormienti | 7,10 |

**Zweite Lesarten**: `Schale` B1 *bowl · copa · coupe · coppa* · `aus` A1
*made of · hecha de · faite de · fatta di* (Material — die §9-Bewegungsregel
greift dort **nicht**) · `am` A1 *by the · junto a la · près de la · presso la* ·
`gelten` B2 *is directed toward · se dirige a · se porte vers · si rivolge a* ·
`ausschlagen` C1 *is budding · brota · pousse · sboccia* · `blühen` B2
*bloom · florecen · fleurissent · fioriscono* (**nicht** *flourish*) · `edel` B2
*noble* (Pred 10,17) · `rund` B2 adjektivisch *redonda · ronde · rotonda* ·
`du` A1 vokativisch *O · oh · ô · o*.

### Zwei Auftragsangaben, die am Quelltext scheiterten

- **`in Blüte stehen` steht weder in 6,11 noch in 7,13.** Beide Verse haben das
  Vollverb `blühen`; 7,13 dazu das Substantiv `Blüten` und `sich öffnen`. Die
  Zeile in §10 gilt nur fuer 2,13 und 2,15.
- **`Wein` ist A2, nicht A1** (Bestand und `BINDUNGEN_AT.md`, 92/93 Belege).

### Hinweise fuer Kapitel 8

- **3,6 teilt mit 8,5 einen 8-Token-Block ab Position 0** („Wer ist die, die aus
  der Wueste heraufsteigt"), Versatz 0 — einschliesslich der §9-Aufloesung an
  `aus` (*out of · desde · depuis · da*, Bewegung mit Ausgangspunkt).
- **3,4 teilt mit 8,2** den Block „ins Haus meiner Mutter".
- **2,17 ↔ 8,14**, Aehnlichkeit 0,63, gemeinsamer Block von 12 Tokens: „mein
  Geliebter sei wie eine Gazelle oder ein junger Hirsch auf den".
- **8,3 ← 2,6** und **8,4 ← 2,7/3,5**, beide woertlich (siehe §10).
- **`Apfelbaum` B1** *apple tree · manzano · pommier · melo* steht in **8,5**.

## 12. Kapitel 8 — das Buch ist fertig

**117 Verse, 2351 Einzelwort- und 56 Mehrwort-Eintraege in 8 Kapiteln.**

Unabhaengige Vollstaendigkeitspruefung gegen den Quelltext (jede Tokenposition
genau ein Eintrag, jede `form` deckungsgleich, kein Mehrwort ausserhalb seines
Verses, kein Feld leer, kein ungueltiges Level, kein Grammatik-Tag):
**0 Befunde.**

### Die fuenf Uebernahmen in Kapitel 8

Der Agent hat sie nicht geglaubt, sondern zweimal nachgemessen — erst den
Quelltext zeichenweise, dann die Eintraege Feld fuer Feld. Ergebnis:

| Uebernahme | Befund |
|---|---|
| 8,3 ← 2,6 | **zeichengleich**, unveraendert |
| 8,4 ← 2,7 (= 3,5) | **nicht** zeichengleich: 2,7 hat `Jerusalems,`, 8,4 `Jerusalems:` — auf `form`-Ebene gleich. Pos 6–13 gestrichen, 14–27 auf 6–19 umgezaehlt |
| 8,5 ← 3,6 | der „8-Token-Block" ist zeichenweise nur **7** Tokens: `heraufsteigt` gegen `heraufsteigt,` |
| 8,2 ← 3,4 | zeichengleich (3,4 Pos 26–29 = 8,2 Pos 5–8) |
| 8,14 ← 2,17 | zeichengleich, 12 Tokens (2,17 Pos 11–22 = 8,14 Pos 1–12) |

**Fuer kuenftige Buecher:** Dublettenangaben gelten auf **`form`-Ebene**, nicht
zeichenweise. Ein `diff`-basiertes Pruefskript meldet an der Satzzeichenstelle
einen Unterschied, wo keiner ist.

### Entscheidungen

- **`man` / `einer` (8,7)** — beide en *one*. `man` weicht auf seine zweite
  Bestandslesart *they · se · on · si* (150 Belege), **nur in 8,7**; in 8,8
  bleibt es auf *one*.
- **`führen` / `bringen` (8,2)** — von keinem Skript gemeldet. Beide tragen
  spanisch *llevar* (29× / 58×) und waeren im selben Vers zusammengefallen.
  `bringen` weicht auf *bring · **traer** · amener · portare* (22 Belege).
- **`Unter` / `unter` (8,5)** — zwei Vorkommen desselben Wortes in
  verschiedener Funktion, dazu `auf`. Ohne die dritte Bestandslesart
  *amid · entre · parmi · tra* waeren zwei davon in **allen vier** Sprachen
  zusammengefallen.
- **`Glut` (8,6) bleibt beim Bestand** (*embers · brasas · braises · braci*),
  obwohl **alle vier** Ausgaben „ardours/llamas/ardeurs/ardori" lesen: die
  Ausweichlesart haette in allen vier Sprachen denselben Stamm wie
  `loderndes` getragen.
- **`Wächter` (8,11) — bewusst NICHT die AT-Bindung.** `BINDUNGEN_AT.md`
  bindet an *watchman · centinela · sentinelle · sentinella* und markiert
  *guards* als NT-Falle. Das ist hier die **falsche Bedeutung**: 3,3 und 5,7
  sind Stadtwaechter, 8,11 sind Weinbergspaechter. Genommen ist
  *guards · guardias · gardes · guardie* (5 Belege, 2 davon AT). Die
  naheliegende Alternative *keeper · guardián · gardien · custode* ist die
  feste Bindung von **`Hüter`** — das im **Folgevers 8,12** steht.
- **`Brust` (8,1) Singular** = *breast · pecho · poitrine · petto*, nicht die
  Buch-Reihe. `parallelen.py` fand **Ps 22,10** mit dem zeichengleichen
  Halbvers „an der Brust meiner Mutter"; von dort woertlich uebernommen.

### Wieder: „unbelegt" war meist belegt

`hints.py` meldete 10 unbelegte Formen, **wirklich neu waren drei**. Und wieder
zeigte der Lexikon-Auszug zwei Lemmata **auch unter VERWANDT nicht** — nur
`fixgloss.py show` fand sie: **`verstärken`** (4 Belege) und **`bieten`**
(5 Belege, `Böte` stand sogar unter UNBELEGT).

Bilanz ueber das Buch: Kap. 1 — 17 von 20 belegt · Kap. 3 — 4 von 6 ·
Kap. 5 — 19 von 26 · Kap. 7 — 6 von 18 · Kap. 8 — 7 von 10.

### Ausgabenbefunde

- **WEB-Sprecherangaben in Kapitel 8: sechs** („Friends" 8,4 · 8,7,
  „Beloved" 8,9 · 8,13, „Lover" 8,12) — vier mehr, als der Auftrag nannte.
- **Neu, andere Klasse: LSG 8,14 endet mit einer freistehenden Tilde** —
  „Sur les montagnes des aromates! **~**". In Kap. 1–7 nicht aufgetreten.
- **RIV: keine neuen Setzfehler in Kapitel 8.** Es bleibt bei den sechs
  bekannten (1,5 · 3,11 · 5,6 · 5,9 · 7,2 · 7,4).
- **RV1909mod 8,6 laesst den Gottesnamen weg** („una llama ardiente"), wo
  WEB *flame of Yahweh*, LSG *flamme de l'Éternel*, RIV *fiamma dell'Eterno*
  und der l1912mod „eine Flamme des HERRN" haben.
- **8,5 `empfangen`**: RV und RIV lesen **gebaeren**, wo der deutsche Text
  `empfangen` und getrennt `unter Wehen geboren` sagt.

### Nach dem Buch: `BINDUNGEN_AT.md` neu erzeugt

1899 → **1909 Lemmata**, 20 neu (darunter `Geliebte`, `Geliebter`, `Gazelle`,
`Myrrhe`, `Siegel`, `Palme`, `lieblich`, `ehrfurchtgebietend`).

**Genau eine Bindung ist gekippt:** `Flamme` von *flames* auf *flame* — durch
Hld 8,6. Es ist ein 7:7-Gleichstand, bei dem die Reihenfolge entscheidet.

Das hat einen Randfall der Tabelle sichtbar gemacht: ihr Kopftext sagte
„haeufigste Lesart **ueber** die Haelfte", die Bedingung im Code laesst aber
**genau** die Haelfte durch (`anteil < 0.5: continue`). Betroffen sind
**91 Lemmata**. Nachgemessen, bevor etwas geaendert wurde: von den 21 echten
50:50-Gleichstaenden unterscheidet sich **keiner** in der Bedeutung — alle sind
Numerusvarianten derselben Lesart. Eine Verschaerfung haette 91 brauchbare
Zeilen fuer nichts gekostet. **Die Schwelle bleibt; der Kopftext ist berichtigt
und benennt den Randfall jetzt** (Commit an `bindungen.py`).
