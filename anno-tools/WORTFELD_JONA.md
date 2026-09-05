# Wortfeld Jona (Buch 32)

Vier Kapitel, 48 Verse, **1136 Einzelwort- und 64 Mehrwort-Eintraege**.
Ein Agent je Kapitel.

`selfcheck`, `konvention`, `levelcheck`, `sweeplemma`, `kongruenz 32`,
`artikel 32`, `qa`, `validate`, `hilfsverb` alle **0**; `glosskollision`
**0 inhaltliche Paare in allen vier Kapiteln**; `paketcheck` Abschnitt A
leer; die Wiederholungs-Gegenrechnung ueber das ganze Buch **ohne einen
einzigen Befund** — alle sieben kapitelübergreifenden Bindungen stehen
zeichengleich.

**Jona ist Erzaehlung, kein Prophetenspruch.** `spricht` steht im ganzen
Buch nicht; die Redeeinleitung ist durchgehend `sagen`.

## 0 · Die Verszaehlung — vier Ausgaben, vier Zaehlungen

```
                Kap 1   Kap 2   Kap 3   Kap 4   gesamt
    deutsch       16      11      10      11      48
    WEB           17      10      10      11      48
    RV1909mod     16      10      10      11      47
    LSG           16      11      10      11      48   ← deckungsgleich
    RIV           17      10      10      11      48
```

**WEB und RIV ziehen den Fisch-Vers ins erste Kapitel:** der deutsche
2,1 steht dort als **1,17**, danach laeuft Kapitel 2 um einen Vers
versetzt. **RIV markiert es im Text** — elf Verse beginnen mit `(2:1)`,
`(2:2)`; wer die RIV-Zeile abzaehlt, hat zwei Tokens Vorsprung.

**RV1909mod zieht die deutschen Verse 2,10 und 2,11 zusammen.** Nicht
ausgelassen — RV 2,10 traegt beide. Vollstaendig in
`BEFUND_JONA_VERSZAEHLUNG.md`, samt der Geschichte des Irrtums.

**`ausgaben.py` stellt Kapitel 1 falsch dar:** es rechnet Versatz +1,
weil es die 17 gegen 16 Verse aus dem *letzten* Vers hochrechnet — der
Zusatzvers haengt aber **hinten**. Fuer Kapitel 1 ist +0 richtig. Das
Werkzeug warnt selbst („Versatz +0 liegt BESSER"); **die Warnung ist zu
lesen, nicht die Zahl.**

## 1 · Kapitel 2 ist ein Psalm — und der Psalter ist fertig

Jeder Vers des Gebets hat eine Vorlage im annotierten Bestand:

```
2,1 ← Matthäus 12,40   2,2 ← 2. Chronika 33,12   2,3 ← Psalmen 120,1
2,4 ← Psalmen 42,8     2,5 ← Psalmen 31,23       2,6 ← Psalmen 69,2
2,7 ← Psalmen 86,13    2,8 ← Psalmen 131,2
```

Sieben davon Token fuer Token uebernommen. **Zwei Einschraenkungen:**

- **2,1 ← Mt 12,40** traegt acht Tokens („drei Tage und drei Naechte im
  Bauch des"), aber **nicht das letzte**: dort steht `des Wals` (fem.),
  hier `des Fisches` (mask.) — `des` muss zu *del · du · del* werden.
- **2,5 ← Ps 31,23** liefert den Imperfekt, und das ist gegen RV („Yo
  pensé") bewusst so belassen: LSG „Je disais" und RIV „E io dicevo"
  lesen ebenfalls Imperfekt.

**Die schwerste Kollision des Buches steht in 2,4** — `Woge` und `Welle`
im selben Vers, in **allen vier** Sprachen. Nichts musste neu gepraegt
werden: **Ps 42,8 hat exakt dieselbe deutsche Wendung** („alle deine
Wogen und Wellen") und trennt bereits:

    Woge  B2  billows · ondas · flots · flutti
    Welle B1  waves · olas · vagues · onde

Und die Ps-42,8-Lesart erzeugt eine **zweite** Kollision, die `hints.py`
nicht melden kann, weil sie erst durch die richtige Wahl entsteht:
`Woge` faellt fr/it mit `Flut` zusammen. `Flut` weicht auf
*currents · corrientes · courants · correnti* — und das ist genau, was
**alle vier** Ausgaben lesen.

## 2 · Zwei Lexikonfallen, die die Bestandsmehrheit stellt

**`aufziehen` (4,7).** Der Bestand hat acht Belege, **alle** lesen
*raised · crió · éleva · allevò* — ein Kind aufziehen. In Jona 4,7 zieht
die **Morgenroete** auf. Neu: B2 *came up · despuntó · se leva · spuntò*.

**`groß` (3,3) traegt zwei Lesarten im selben Vers.** Einmal attributiv
(„eine gewaltig **große** Stadt", *great*), einmal als Mass („drei
Tagereisen **groß**", *in size · de tamaño · de taille · di grandezza*,
nach 1Kön 7,10). Wer der Mehrheitslesart folgt, glossiert die zweite
falsch.

Dazu: **`Hütte` (4,5)** nicht *tent* (22 Belege, alle Stiftshuette),
sondern die Minderheitszeile *shelter · enramada · hutte · capanna* —
was die Ausgaben lesen. **`verging` (4,10)** nicht *passed* (Zeitablauf),
sondern *perished*. **`traf` (1,7)** nicht *struck*, sondern
*fell on · cayó sobre · tomba sur · cadde su* — „das Los **traf** Jona".

## 3 · `leidtun` hat zwei Bedeutungszweige, und Jona braucht beide

```
Reue      3,10 · 4,2   regrets · se arrepiente · regrette · si pente   (1Mo 6,6 / Am 7,3)
Mitleid   4,10 · 4,11  feel sorry for · dar lástima · faire pitié · far pena   (2Mo 2,6 / Mk 8,2)
```

Der Prompt hatte behauptet, die Amos-Reihe binde alle drei Stellen. Der
Kapitel-4-Agent hat es am gelieferten `ch3.json` geprueft und widerlegt:
**4,10 und 4,11 heissen nicht „bereuen", sondern „Mitleid haben".** Nach
SPEC richtig so — eigene Bedeutung, eigene Glosse.

Auch das Kopfwort folgt: `leid` traegt in 3,10 die Reue-Zeile
(*pena · peine · dispiacere*), in 4,10 die Mitleid-Zeile
(*lástima · peine · pena*). Beide stehen so im Bestand.

## 4 · Aufgeloeste Kollisionen (Auswahl)

| Vers | Paar | Auflösung |
|---|---|---|
| 1,10 | `warum` ↔ `weil` (it *perché*) | `weil` auf *poiché* (Bestand, 9× lowercase). **RIV loest dieselbe Stelle mit „giacché" — das Wort steht im ganzen Bestand kein einziges Mal**, deshalb nicht uebernommen |
| 1,10 | `die` ↔ `ihn` (it *gli*) | `gli` ist im Italienischen zugleich Pluralartikel und Dativklitikon. „**gli** uomini" ist zwingend, also weicht `ihn` auf *lui* |
| 1,11 | — | **hier steht kein `gli`**, also gilt die Bestandsreihe *him · le · lui · gli* (= RIVs eigene Lesart). Die Regel „nur im Kollisionsvers" schlaegt die Zeichengleichheit der Wendung „fragten ihn" |
| 2,6 | `umgeben` ↔ `umschließen` ↔ `umschlingen` | **drei** um-Verben im selben Vers. `umschließen` auf *enclosed · envolvió · enveloppa · avvolse* (alle vier Ausgaben); `umschlingen` war im Bestand schon getrennt |
| 3,8 | `zu` ↔ `an` (4 von 4) | `zu Gott rufen` auf *toward · hacia · vers · verso*; `an` bleibt, weil **Hiob 16,17 woertlich denselben Satz traegt** |
| 4,9 | `Recht` ↔ `recht` | die Amos-Trennung passt **nicht**: `recht` ist hier *right · bien · bien · bene* (1Mo 4,7, so lesen alle vier Ausgaben). `Recht` weicht auf *reason · razón · raison · ragione* |
| 4,5 | `ab` ↔ `hinaus` | `ab` (in `abwarten`) auf Rut 3,18: *to the end · hasta el final · jusqu'au bout · fino alla fine* |

**Bewusst stehen gelassen:** 1,5 `hatte`/`war` (4 von 4) — zwei deutsche
Plusquamperfekt-Hilfsverben, die keine Zielsprache nachbildet · 1,3
`an`/`nach` (Apg 21,2 traegt dieselbe Konstellation im selben Vers) ·
1,8 `Was`/`welchem` (nur fr *Quel*) · 3,7 `Weder`/`noch` (sechs
Bestandsverse gegengelesen, **alle** setzen ni/ni/né) · 3,10
`ihrem`/`ihnen` (fr *leur*) · 4,2 `an`/`indem` (`an` ist durch den
Joel-2,13-Block gebunden).

## 5 · Eine Abwaegung, die dokumentiert gehoert

„Mach dich auf, geh **in** die grosse Stadt Ninive und" steht in **1,2 und
3,2** — zehn Tokens, die laengste Bindung des Buches. **Alle vier
Ausgaben lesen dort die Richtungspraeposition** („va **a** Ninive"), und
der Bestand fuehrt nach Bewegungsverben *into · **a** · dans · in* mit 60
gegen 41 Belegen.

Trotzdem steht in beiden Versen *into · **en** · dans · in*. Der Grund:
**in 1,2 steht „bis zu mir" mit spanisch `a`** — dort waere `a` eine
Kollision. In 3,2 nicht. Hier stehen zwei Projektregeln gegeneinander,
und die Zeichengleichheit eines Zehn-Token-Blocks wiegt schwerer als die
Auflösung eines Funktionsworts in nur einem der beiden Verse.

**Wer die Reihe aendert, muss 1,2 und 3,2 gemeinsam aendern** — und dann
die Kollision in 1,2 anders loesen.

## 6 · Befunde in den Ausgaben

**Drei RIV-Anlautfehler** (`iona` statt `Giona` in 4,6 und 4,8 — 4,6
traegt beide Formen im selben Vers), dazu **ein Untertyp**: in 1,1 faellt
nicht der Anlaut des Namens, sondern die **Praeposition davor** aus
(„fu rivolta ∅ Giona"). Die Gegenprobe fuehrte zu **Matthäus 16,4**, einem
fertigen Buch, mit demselben `di iona`. Alles in `RIV_ANLAUTFEHLER.md`.

**Wo der deutsche Text allein steht** (ueberall dem Deutschen gefolgt):
1,5 `unter Deck` · 1,6 „denkt Gott an uns" · 1,7 `Schuld` · 2,5 (der
einzige Vers, den der deutsche Text als **Frage** baut — nur RIV auch) ·
3,3 „vor Gott" (nur RIV hat es) · 3,8 die Klebe-Metapher · 4,2 „einer,
dem das Unheil leidtut" (alle vier reden Gott direkt an).

**RV1909mod zieht 3,7 zusammen** („ni se les dé de comer ni de beber") —
fuer `weiden` gibt es keine spanische Vorlage.

**RV siezt auch hier** (1,7 · 1,12 · 3,x); alle spanischen Glossen stehen
auf **vosotros**.

## 7 · Fuer die Nachbarbuecher

```
Jona A1 Jonah·Jonás·Jonas·Giona  ·  Ninive A1 Nineveh·Nínive·Ninive·Ninive
Tarsis A1 · Amittai A1 of Amittai·de Amitai·d'Amitthaï·di Amittai
Jafo A1 Joppa·Jope·Joppé·Ioppe   — NICHT die `Japho`-Reihe (Esra 3,7),
   die fr/it anders liest. Der Bestand fuehrt beide Schreibungen getrennt.
Fisch A1 fish·pez·poisson·pesce · Bauch B1 belly·vientre·ventre·ventre
verschlingen C1 swallowed up·devoró·engloutit·inghiottì  ≠ fressen (devor-Reihe)
speien C1 spewed·arrojó·vomit·vomitò   (EIN Bestandsbeleg, Offb 12,15)
Totenreich C1 realm of the dead·reino de los muertos·séjour des morts·regno dei morti
Woge B2 billows·ondas·flots·flutti  ≠  Welle B1 waves·olas·vagues·onde   (Ps 42,8)
Flut B2 floods·torrentes·flots·flutti — in 2,4 auf currents·corrientes·courants·correnti
Tiefe B1 deep·abismo·abîme·abisso · Kehle B2 throat·garganta·gorge·gola
Alge B2 seaweed·algas·algues·alghe · einriegeln C1 barred in·encerrado·enfermé·rinchiuso
Sacktuch C1 sackcloth·tela de cilicio·sac de deuil·sacco  (= Joels `Trauersack`)
Fasten B2 fast·ayuno·jeûne·digiuno · Asche B2 · Purpurgewand C1
Tagereise C1 day's journey·jornada de camino·journée de marche·giornata di cammino
Gewalttat B2 violence·violencia·violence·violenza
leidtun B1 zwei Zweige — s. Abschnitt 3
recht (Adj) B1 right·bien·bien·bene   ·  Recht B1 reason·razón·raison·ragione (4,9)
Rizinusstaude C1 castor-oil plant·ricino·ricin·ricino · Staude B2 plant·planta·plante·pianta
verdrießen C1 displeased·disgustó·déplut·dispiacque  ·  emporwachsen C1 grew up·se elevó·s'éleva·si elevò
aufziehen (Morgenröte) B2 came up·despuntó·se leva·spuntò — NICHT die raised-Reihe
Hütte B1 shelter·enramada·hutte·capanna — NICHT tent/tienda/tente/tenda
Fährgeld B2 fare·pasaje·prix du passage·prezzo del passaggio
Seemann B2 sailors·marineros·marins·marinai · rudern B2 · Los B2 · losen B2
Tier B1 animals·animales·animaux·animali (Pl.)  ·  animal·animal·animal·animale (Sg.)
Land A1 land·país·pays·paese (Gebiet)  ·  land·tierra·terre·terra (Festland gegen Meer)
```
