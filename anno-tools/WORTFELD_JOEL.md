# Wortfeld Joel (Buch 29)

Ein Paket, vier Kapitel, vier Agenten — das ganze Buch auf einmal.
73 Verse, 1662 Einzelwort- und 74 Mehrwort-Eintraege.

Die buchweiten Vorgaben stehen in **`PAKETE_JOEL.txt`**. Diese Datei haelt
fest, was die Kapitel entschieden haben und was beim Einsammeln dazukam.

## 0 · Die vier Faelle, die jeden angingen

**1. Keine Verszaehlungsabweichung — aber zwei Kapitelgrenzen.** Alle vier
Ausgaben lesen 1,1–20 und 2,1–27 auf Versatz +0. Die deutsche Zaehlung fuehrt
Kapitel 3 und 4 getrennt, wo en/es die Verse als 2,28–32 und Kapitel 3
zaehlen. `ausgaben.py` schaetzt fuer 2,1–27 faelschlich +5 und warnt selbst
davor; der Kapitel-2-Agent hat +0 am Text nachgelesen und behalten.

**2. Die vier Heuschreckenreihen aus 1,4 kehren in 2,25 wieder — und die
Ausgaben ordnen sie verschieden.** WEB und RV1909 behalten in 2,25 die
Reihenfolge von 1,4 bei, waehrend der deutsche Text (mit LSG und RIV) dem
Hebraeischen folgt und umstellt. **Dieselbe Tierbezeichnung steht in beiden
Versen also an verschiedenen hebraeischen Woertern** — eine positionsweise
Uebernahme aus WEB/RV waere in 2,25 verschoben. LSG transliteriert drei der
vier ueberhaupt nicht (*gazam*, *jelek*, *hasil*).

Die Reihen stehen in 1,4 und 2,25 **zeichengleich**, Level fuer Level:

```
Nagerheuschrecke  C1  gnawing locust · langosta roedora · sauterelle rongeante · locusta rodente
Wanderheuschrecke C1  migratory locust · langosta migratoria · sauterelle migratrice · locusta migratrice
Larve             B2  grub · oruga · larve · bruco
Fresser           C1  devourer · devorador · dévoreur · divoratore
```

`Larve` folgt der Bestandsreihe Ps 105,34; `Fresser` der **AT**-Lesart
Ri 14,14 (*devourer*) statt der NT-Mehrheit *glutton* (Mt 11,19 · Lk 7,34) —
eine Lexikonfalle. Die beiden unbelegten Komposita sind aus `Heuschrecke` C1
plus `nagend`/`wandernd` gepraegt.

**3. `fressen` und `verzehren` mussten auseinandergezogen werden.** Beide
tragen im Bestand *devour*-Reihen. In Joel ist der Unterschied
bedeutungstragend: Heuschrecken **fressen** (1,4 · 2,3 · 2,25), Feuer
**verzehrt** (1,19 · 1,20 · 2,5). Beim Einsammeln standen 1,19/1,20 noch auf
*devoured · devorado · dévoré · divorato* — **zeichengleich mit `fressen` in
2,25**. Beide Verse gingen deshalb auf die consumir-Reihe:

```
fressen    C1  devoured · devoró · dévora · divorò        (1,4)
verzehren  C1  consumed · consumido · consumé · consumato (1,19 · 1,20)
verzehren  C1  consumes · consume · consume · consuma     (2,5)
```

**4. `Wein` 6× stimmte nicht.** Der Prompt zaehlte `Weint` und `weint` (1,5)
mit — beides Formen von **weinen**. Das Substantiv `Wein` steht **1×** (1,10).
Gemeldet vom Kapitel-1-Agenten, am Quelltext bestaetigt.

## 1 · Was aus den Nachbartexten uebernommen wurde

`parallelen.py` traf in Kapitel 1 sieben Verse, in Kapitel 2 fuenfzehn von 27.

| Vers | Vorlage | uebernommen |
|---|---|---|
| 1,15 | **Jes 13,6** | vollstaendig, Token fuer Token (`der Tag des HERRN ist nahe, er kommt wie`) samt `Verwuestung` C1 |
| 1,1 | **Jer 46,1** | vollstaendig (`Dies ist das Wort des HERRN das an`) |
| 1,9 | 2Chr 33,15 | `aus dem Haus des HERRN` |
| 1,12 · 1,19 | Jes 55,12 | `alle Baeume des Feldes` |
| 1,13 | Neh 4,16 | `die Nacht ueber` als Mehrwort |
| 1,18 | Klgl 1,6 | `keine Weide finden und` |
| 1,19 · 1,20 | Ps 65,13 | `die Weiden der Steppe` — **mit einer Korrektur**, s. Abschnitt 3 |

**Nicht uebernommen: 2,2 ← Hiob 10,21.** Joel hat `Finsternis` und `Dunkel`
im selben Vers; die Vorlage haette beide gleich geglosst. `Finsternis` bleibt
*darkness*, `Dunkel` weicht auf *gloom · penumbra · obscurité · caligine*.

**Joel 3,1–5 ist in Apg 2,17–21 zitiert** — der Abgleich lief Token fuer
Token. Er bestaetigt `Himmel` 3,3 (*heaven*), `anrufen` 3,5 und die
Konjunktivform `kommt` 3,4 (*venga · vienne · venga* nach „bevor"). Er
**widerlegt** nichts, deckt aber zwei Bestandsfehler auf (Abschnitt 3).

## 2 · Aufgeloeste Kollisionen (nur im Kollisionsvers)

| Vers | Paar | Auflösung |
|---|---|---|
| 1,2 | `hoeren` ↔ `zuhoeren` | beide standen fr auf *Écoutez*. `zuhoeren` weicht auf **LSGs eigene Lesart** *Prêtez l'oreille*; das Kopfwort `Hoert` (pos 4) traegt jetzt seine woertliche Reihe *Hear · Oíd · Écoutez · Udite* wie pos 0 — die Bestandskonvention (5Mo 32,1, Neh 5,7) |
| 1,10 | `Feld` ↔ `Acker` | `Acker` auf die zweite Bestandslesart *ground · suelo · sol · suolo* (1Mo 3,17) — deckt sich mit allen vier Ausgaben |
| 1,10 | `verdorren` ↔ `versiegen` | `versiegen` es *se agota* |
| 1,7 | `ab` ↔ `weg` | `weg` fr *au loin* · it *lontano* |
| 1,13 | `Trauergewand` ↔ `Trauersack` | `Trauersack` auf die cilicio-Reihe *haircloth · telas de cilicio · cilices · cilici*; in **1,8** (keine Kollisionsstelle) bleibt die Bestandsreihe |
| 1,17 | `Kornspeicher` ↔ `Scheune` | `Kornspeicher` (1 Beleg) weicht: *granaries · depósitos de grano · dépôts de grain · depositi di grano* |
| 1,17 | `liegen` ↔ `sind` | `liegen` auf *lie · yacen · gisent · giacciono* (Hiob 39,30) |
| 1,14 | `rufen` ↔ `berufen` | `berufen` *summon · convocad · convoquez · convocate* |
| 2,2 | `Finsternis` ↔ `Dunkel` | s. o. — die Vorlage Hiob 10,21 bewusst nicht uebernommen |
| 4,18 | `aus` ↔ `von` | `aus` weicht auf *out of · desde · depuis · da*. Deshalb steht 4,18 **anders als 1,9**, obwohl die Wortfolge „aus dem Haus des HERRN" dieselbe ist — 1,9 hat kein `von` im Vers |
| 4,19 | `Oede` ↔ `wuest` | Substantiv *desolation*, Adjektiv *desolate* — verschiedene Wortarten, keine Verschmelzung |

**Bewusst stehen gelassen:** 1,7 `Es`/`sie` beide en *it* (Subjekt vs. Objekt —
eine echte Verschmelzung des Englischen). 1,4 `fraß`/`Fresser` — figura
etymologica, der deutsche Text wiederholt den Stamm selbst. 3,1
`Menschen`/`Maenner` es/fr/it verschieden gehalten (*seres humanos* gegen
*hombres*), s. Abschnitt 3.

## 3 · Befunde im Bestand (nicht angefasst, zur Nachlese)

**1. Ps 65,13 traegt einen Artikel im falschen Genus.** Dort steht `der` in
„die Weiden **der** Steppe" als *of the · del · du · del* (maskulin),
waehrend derselbe Vers `Steppe` als *estepa · steppe · steppa* fuehrt — alle
drei feminin. Joel 1,19 · 1,20 · 2,22 haben *de la · de la · della*.
`artikel.py` meldet die Stelle. Gefunden vom Kapitel-1-Agenten.

**2. Apg 2,17 verschmilzt `Menschen` und `Maenner` in drei Sprachen.**
Beide tragen dort *hombres · hommes · uomini*, **im selben Vers**. Joel 3,1
hat denselben Satzbau und loest auf: `Menschen` *human beings · seres humanos
· êtres humains · esseri umani*, `Maenner` *hombres · hommes · uomini*.
Beim Einsammeln war Joel 3,1 zunaechst an Apg 2,17 angeglichen worden — die
Ruecknahme kam von `glosskollision.py`, das den Neubau sofort meldete.

**3. Apg 2,21 traegt ein franzoesisches Wort in der spanischen Spalte:**
`anruft` = *calls on · **invoque** · invoque · invoca*. Spanisch ist
*invoca*, wie Joel 3,5 es hat; der Bestand fuehrt die richtige Reihe 5×.
Eine Korpusmessung ueber alle 676 107 Eintraege auf spanische Glossen mit
franzoesischen Sonderzeichen (à â è ê ë î ï ô û ù ç œ) ergab **0 Treffer** —
der Fall ist ein Einzelstueck, kein Muster.

**4. `Kornspeicher` und `Scheune` tragen im Bestand dieselben es/fr/it-Glossen**
(*graneros · greniers · granai*); sie kollidieren ueberall, wo sie
zusammenstehen. Ebenso `Trauergewand` und `Trauersack` in en (*sackcloth*).

## 4 · Befunde in den Ausgaben

**RIV, drei neue Defekte — alle drei einmalig im ganzen Korpus:**

| Stelle | steht | muss | Gegenprobe |
|---|---|---|---|
| Joel 1,12 | „son **ecchi**" | *secchi* | `ecchi` korpusweit 2×: hier und Jos 9,4 („de' **ecchi** otri" → *vecchi*) |
| Joel 2,20 | „**alirà**" | *salirà* | `salirà` 18× gegen `alirà` 1× |
| Joel 2,16 | „**Radunare**" (Infinitiv) | *Radunate* | der einzige Vers im RIV-Korpus, der so beginnt — derselbe Vers hat die richtige Form zweimal |

Alle drei sind Anlaut- bzw. Endungsverluste desselben Typs wie in
`RIV_ANLAUTFEHLER.md`. Dazu: 1Chr 27,20 hat RIV `Ioel` — gehoert in die
I/J-Liste von `BEFUNDE_RIV_ANLAUT_J.md`.

**Widerspruch der vier Ausgaben, 1,6 `Backenzaehne`:** WEB *fangs* · RV
*colmillos* · LSG *mâchoires* · RIV *mascellari*. Im Bestand unbelegt, daher
woertlich geglosst (*molars · muelas · molaires · molari*), damit die vier
Sprachen untereinander stimmen.

**1,10:** alle vier Ausgaben setzen fuer deutsches `Wein` dasselbe Wort wie
fuer `Most` in 1,5. Gefolgt wurde dem Bestand (`Wein` A2 *wine · vino · vin ·
vino*), sonst waeren `Wein` und `Most` im selben Kapitel ununterscheidbar.

**1,11 ist Indikativ, kein Imperativ** („Die Bauern **sind** bestuerzt") —
alle vier Ausgaben haben dort Imperative. Glossiert wurde nach dem deutschen
Text.

**4,20 `bewohnt`:** die Ausgaben gehen im Genus auseinander — RV *habitada*
(f), LSG *habité* (m), RIV *abitata* (f). Die Glossen folgen jeder ihrer
eigenen Ausgabe; das ist kein Kongruenzfehler.

## 5 · Was beim Einsammeln zusaetzlich angeglichen wurde

Die n-Gramm-Gegenrechnung (4- bis 9-Gramme gegen den Bestand und
buchintern) und die Reihen-Gegenrechnung (welche Vier-Sprachen-Reihe traegt
im Buch zwei verschiedene Inhaltslemmata?) fanden sieben Stellen:

```
1,2   zuhören  fr  Écoutez -> Prêtez l'oreille   (Kollision mit hören, LSG-gestützt)
1,2   hören    pos 4: Mehrwortglosse -> wörtliche Reihe (Bestandskonvention)
1,14  einberufen  en convene -> summon  (einzige Bestandslesart; macht 1,14 = 2,15)
1,14  eures    your -> of your · de vuestro · de votre · del vostro  (= 2,26; RIV liest beidemal „del vostro")
1,19  verzehren -> consumed · consumido · consumé · consumato  (Trennung von fressen)
1,20  verzehren -> dieselbe Reihe
2,10  Himmel   sky -> heaven   (Bestand: „Himmel und Erde" 53× heaven gegen 3× sky)
2,15  eine     en a -> an      („an assembly")
2,22  Weinstock  fr vigne -> cep  (Bestand 26:11; vigne ist in 1,7 schon „Weinberg")
4,16  Himmel   heavens -> heaven  (= 2,10 und 3,3)
4,17  auf      fr sur · it su -> en · in  (= 2,1; WEB/RV/RIV lesen beidemal „in Sion")
```

**Eine Angleichung wurde zurueckgenommen:** 3,1 `Menschen` an Apg 2,17
(*people · hombres · hommes · uomini*) — `glosskollision.py` meldete
augenblicklich die neue Kollision mit `Maenner` im selben Vers. Die Vorlage
traegt den Defekt, nicht Joel. Derselbe Fehlertyp wie in Daniel 3,18.

**Eine Luecke im eigenen Verfahren:** die n-Gramm-Gegenrechnung indizierte nur
Einzelwoerter. Die Mehrwoerter (`einberufen` 1,14 gegen 2,15) fielen erst der
Reihen-Gegenrechnung auf. Beide Laeufe gehoeren kuenftig zusammen.

## 6 · Wortfeld fuer die Nachbarbuecher (Amos folgt)

```
Tag des HERRN (Formel, 1,15 ← Jes 13,6, wiederholt 2,1 · 2,11 · 3,4 · 4,14):
  Tag A1 day·día·jour·giorno · HERR A1 LORD·SEÑOR·ÉTERNEL·SIGNORE
  nahe A2 near·cerca·proche·vicino
  Verwüstung C1 desolation·desolación·désolation·desolazione
  Allmächtiger B2 Almighty·Todopoderoso·Tout-Puissant·Onnipotente
  wehe B2 Woe·Ay·Malheur·Guai
  „ist nahe" es está cerca — „ist groß" es es grande (2,11)

Landwirtschaft (aus Hosea bestätigt, unverändert):
  Most B2 new wine·mosto·moût·mosto · Getreide B1 grain·trigo·blé·grano
  Öl A2 · Wein A2 wine·vino·vin·vino · Weinstock B2 vine·vid·cep·vite
  Weinberg B1 vineyard·viña·vigne·vigna   (fr vigne ist der BERG, nicht der Stock)
  Feigenbaum B1 · Weizen B1 · Gerste B1 · Ernte B1 · Saat B2
  Feld A2 field·campo·champ·campo · Acker B1 ground·suelo·sol·suolo (2. Lesart)
  Kelter C1 winepress·lagar·pressoir·torchio · Tenne B2 · Sichel B2

Kult und Klage:
  Priester B1 · Ältester B2 elders·ancianos·anciens·anziani · Altar B1
  Speisopfer C1 · Trankopfer C1 · Fasten B2 fast·ayuno·jeûne·digiuno
  Versammlung B1 assembly·asamblea·assemblée·assemblea
  einberufen C1 summon·convocad·convoquez·convocate (Mehrwort)
  Trauergewand C1 sackcloth·telas de saco·sacs de deuil·sacchi
  Trauersack C1 sackcloth·tela de cilicio·sac de deuil·sacco

Himmel und Gestirne:
  Himmel A2 heaven·cielo·ciel·cielo   — durchgehend, auch neben „Erde" und „erbeben"
  Sonne A1 · Mond A1 · Stern A1
  verdunkeln C1 / verfinstern C1 — beide darken·oscurecen·obscurcissent·oscurano

Dürre und Feuer:
  Steppe B2 wilderness·estepa·steppe·steppa  (Artikel: de la · de la · della)
  Weide B1 pasture(s)·pasto(s)·pâturage(s)·pascolo/i
  verdorren C1 · verwelken C1 · vertrocknen B2 · austrocknen B2 · versiegen C1
  verzehren C1 consum-Reihe · fressen C1 devor-Reihe — nie vermischen

Neu geprägt in Joel:
  Nagerheuschrecke · Wanderheuschrecke (s. Abschnitt 0)
  Weintrinker B2 wine drinkers·bebedores de vino·buveurs de vin·bevitori di vino
  Backenzahn B2 molars·muelas·molaires·molari
  Rinde B2 bark·corteza·écorce·corteccia
  Kornspeicher C1 granaries·depósitos de grano·dépôts de grain·depositi di grano
  Pethuel A1 · Joel A1 Joel·Joel·Joël·Gioele   (it Gioele — Bestand Apg 2,16 + RIV)
  Schar B2 Multitudes·Multitudes·Multitudes·Moltitudini (4,14 — zufällige Kognaten)
  Entscheidung B1 decision·decisión·décision·decisione
  Winzermesser C1 pruning knives·podaderas·serpes·roncole
```

Spanisch durchgehend **vosotros**, kein `ustedes`. Keine Grammatik-Tags in
Klammern (maschinell gegengeprueft: 0 Treffer).
