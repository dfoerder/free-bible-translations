# Wortfeld Amos (Buch 30)

Drei Pakete zu je drei Kapiteln, ein Agent je Kapitel.
9 Kapitel, 146 Verse, **3525 Einzelwort- und 138 Mehrwort-Eintraege**.

Die buchweiten Vorgaben stehen in **`PAKETE_AMOS.txt`** — in der
**berichtigten** Fassung: elf Angaben darin waren falsch, alle von den
Agenten am Bestand oder an den Ausgaben widerlegt (Abschnitt 5).

## 0 · Die zwei Formeln, die das Buch tragen

**Die Gerichtsformel, achtmal** (1,3 · 1,6 · 1,9 · 1,11 · 1,13 · 2,1 ·
2,4 · 2,6), maschinell auf Zeichengleichheit geprueft:

```
So          A1  Thus · Así · Ainsi · Così
spricht     A2  says · dice · parle · dice      (vorangestellt!)
Wegen       B1  Because of · A causa de · À cause de · A causa di
der         A1  the · los · des · dei           (der Artikel steht SEPARAT)
vielfachen  B2  repeated · repetidos · répétés · ripetuti
Verbrechen  B2  crimes · crímenes · crimes · crimini
Urteil      B1  judgment · juicio · jugement · giudizio
mache       A1  make · hago · fais · faccio
rückgängig  B2  reversed · revocado · révoqué · revocato
MW rückgängig machen  B2  revoke · revoco · révoque · revoco   (parts, FINIT)
```

**Keine der vier Ausgaben taugt hier als Vorlage.** Alle lesen die
hebraeische Zahlenformel woertlich („For three transgressions … and for
four"), der deutsche Text fasst sie zu „die vielfachen Verbrechen"
zusammen. Es gibt in keiner Ausgabe ein Wort, das `vielfachen` entspraeche;
`vielfach` hat im Bestand einen einzigen, unpassenden Beleg (Lk 18,30).
Die Reihe ist neu gepraegt.

**Die Feuerformel, siebenmal** (1,4 · 1,7 · 1,10 · 1,12 · 1,14 · 2,2 · 2,5):

```
sende      B1  send · envío · envoie · mando
Feuer      A1  fire · fuego · feu · fuoco
Paläste    B2  palaces · palacios · palais · palazzi
verzehren  C1  consume · consumir · consumer · consumare
Mauern     B1  walls · muros · murailles · mura
```

## 1 · `verzehren` gegen `fressen` — und der Vers, der beides traegt

Joel (29) hat die Trennung festgelegt, Amos hat sie zum ersten Mal in
**einem einzigen Vers** zu leisten:

> **7,4** „Er rief das Feuer zur Strafe herbei, das die grosse Flut
> **verzehrte** und das Ackerland zu **fressen** begann."

```
verzehren  C1  consum-Reihe   9× (1,4 · 1,7 · 1,10 · 1,12 · 1,14 · 2,2 · 2,5 · 5,6 · 7,4)
fressen    B2  devor-Reihe    3× (4,9 · 7,2 · 7,4)
```

**Der Bestand haette hier den Fehler gebaut.** Die einzige belegte Lesart
der Form `verzehrte` (2Mo 15,7, 15 Belege) lautet
*consumed · consumió · **dévora** · **divorò*** — franzoesisch und
italienisch auf der devor-Reihe, also in 7,4 in zwei Sprachen
ununterscheidbar von `fressen`. Der Agent hat die Lexikonlesart verworfen
und *consumed · consumió · consuma · consumò* gesetzt.

## 2 · Die Falle `spricht` — die STELLUNG entscheidet

Gemessen ueber den ganzen Bestand:

```
vorangestellt  „So/Darum spricht der HERR …"       fr parle   220 : 4
nachgestellt   „…, spricht der HERR"               fr dit     252 : 95
mit „Gott, der HERR", beide Stellungen             fr parle   210, einstimmig
```

LSG bestaetigt die ersten beiden Vers fuer Vers („Ainsi **parle**
l'Éternel" in allen acht Gerichtsformeln, „**dit** l'Éternel" in 3,10).

**Eine dritte Lesart** steht dort, wo `spricht` kein Redeeinleiter ist,
sondern ein Vollverb: 3,1 „das der HERR **ueber euch** spricht" und 5,10
„der im Tor **Recht** spricht" folgen Jesaja 37,22 —
*speaks · habla · **prononce** · **pronunzia***.

**Zwei Stellen, an denen wir bewusst von LSG abweichen:**

- **8,3 · 8,9 · 8,11** — LSG liest dreimal „**dit** le Seigneur,
  l'Éternel", der Bestand glossiert die Wendung 100× als *parle*. Wir
  folgen dem Bestand; der Befund steht in `NACHLESE_BESTAND.md` E.
- **7,17** — LSG baut den Satz anders („voici ce que **dit** l'Éternel"
  statt „ainsi parle"), RIV liest „**parla**". Wir folgen der
  Stellungsregel und halten 7,17 zeichengleich mit 5,16.

## 3 · Die Wiederholungen, die `dubletten.py` nicht findet

`dubletten.py` vergleicht ganze Verse ab 60 Prozent. Damit findet es die
sechzehn Formelpaare in Kapitel 1-2 — aber **nicht** den Refrain, der die
laengste woertliche Wiederholung des Buches ist:

> **„Doch ihr seid nicht zu mir umgekehrt, spricht der HERR."**
> 4,6 · 4,8 · 4,9 · 4,10 · 4,11 — zehn Tokens, fuenfmal

Gefunden hat ihn `wiederholungen.py`, das eigens dafuer gebaut wurde. Die
Reihe: `Doch` A2 *Yet · Sin embargo · Pourtant · Eppure* · `seid` A1
*have · habéis · êtes · siete* · `umgekehrt` B1 *returned · vuelto ·
revenus · tornati* (nach 1Petr 2,25) · `spricht` nachgestellt → *dit*.

`Doch` weicht hier bewusst von 2,12 (*But · Pero · Mais · Ma*) ab — der
Refrain ist konzessiv, WEB liest „yet", LSG fuenfmal „Malgré cela".

Weitere Wiederholungen, alle zeichengleich gesetzt:

```
7,1 · 7,4 · 8,1   „Gott, der HERR, liess mich Folgendes sehen"  (8 Tokens)
                  7,7 ist die verkuerzte Fassung („Er liess mich …")
7,2 · 7,5         „Wie soll Jakob das ueberstehen? Er ist so klein." (9)
7,3 · 7,6         „tat … dem HERRN leid" · „wird nicht geschehen"
7,8 · 8,2         „Was siehst du, Amos? Ich antwortete" · „Da sagte der HERR"
7,11 · 7,17       „sterben, und Israel wird aus seinem Land"  (7)
8,8 · 9,5         „wie der Nil und" · „wie der Fluss Aegyptens"
8,11 · 9,13       „Siehe, es kommen Tage, spricht …"  (5)
5,8 · 9,6         „dem Wasser des Meeres" · „es ueber die Erde" · „HERR ist sein Name"
5,16 · 6,8 · 6,14 „spricht der HERR, der Gott der Heerscharen"  (7)
```

**Zwei binden nur teilweise:** „An jenem Tag werden **die**" (8,3 · 8,13)
bindet nur vier Tokens — 8,3 steht vor `Lieder` (m), 8,13 vor `Frauen`
(f). Und „…, spricht Gott, der HERR" gegen „…, spricht der HERR": das
`spricht` unterscheidet sich, die Apposition nicht.

## 4 · Aufgeloeste Kollisionen (nur im Kollisionsvers)

| Vers | Paar | Auflösung |
|---|---|---|
| 1,5 · 1,8 | `aus` ↔ `von` | `aus` weicht auf *out of · desde · depuis · da* (Joel-4,18-Praezedenz) |
| 1,10 | `Feld` ↔ `Acker` | `Acker` auf *ground · suelo · sol · suolo* |
| 2,9 | `Dabei` ↔ `doch` (4 von 4) | `doch` auf die Partikellesart *after all · después de todo · après tout · dopotutto* |
| 2,11 | `Sohn` ↔ `Kind` | `Kinder` auf *children · descendientes · enfants · discendenti* — **eine Aufloesung, KEINE Buchregel**: in 3,1 · 3,12 · 4,5 · 6,14 (kein `Sohn` im Vers) gilt die Bestandsreihe *hijos · figli* |
| 3,6 | `das` ↔ `dass` | `das` auf *which · la cual · lequel · la quale* (Bezug `Unglück`) |
| 3,12 | `Liegen` ↔ `Prunkbetten` | `Liege` fr *divans* statt *lits* |
| 4,4 | `alle` ↔ `jeden` | `jeden` von *every* auf *each* |
| 4,7 | `Regen` ↔ `regnen` | `regnen` en *to rain* (WEBs eigener Wortlaut) |
| 4,13 | `machen` ↔ `schaffen` ↔ `formen` | drei deutsche Verben, drei Reihen: *forms* · *creates* · MW *machen zu* |
| 5,15 | `hassen` ↔ `verabscheuen` | `hassen` = odiar-Reihe, `verabscheuen` = aborrecer-Reihe — buchweit getrennt |
| 5,16 | `Gasse` ↔ `Straße` | `Gasse` auf die Hld-3,2-Lesart *alleys · callejones · ruelles · vicoli* |
| 5,20 | `finster` ↔ `dunkel` | `dunkel` auf *gloomy · sombrío · sombre · buio* |
| 6,2 | `Zieht` ↔ `geht` | `Zieht` auf *Pass over · Pasad · Passez · Passate* |
| 6,10 | `der` ↔ `er` | `der` auf *the other · el otro · l'autre · l'altro* (LSG „cet homme", RIV „L'altro") |
| 7,7 | `war` ↔ `stand` | `war` es *había sido* |
| 8,5 · 8,6 | `Getreide` ↔ `Korn` | `Korn` auf die Ri-15,5-Lesart *corn · grano · grain · frumento* — die einzige, die in allen vier Sprachen auseinandergeht |
| 9,3 | `verstecken` ↔ `verbergen` | `verbergen` auf *conceal · ocultarse · se dérober · occultarsi* — genau das, was alle vier Ausgaben lesen |
| 9,5 | `all` ↔ `ganz` | `ganz` auf *wholly · entera · tout entière · tutta quanta* |
| 9,11 | `wieder` ↔ `neu` | `neu` auf *anew · a nuevo · à neuf · a nuovo* |

**Bewusst stehen gelassen:** 4,4 `Sünde`/`sündigt` (figura etymologica,
alle vier Ausgaben ebenso) · 7,2 · 7,5 `Herr`/`HERR` (19 Verse im Korpus
haben „Herr, HERR", **alle 19** einstimmig *Lord* gegen *LORD*) ·
die romanischen Artikel-gegen-Klitikon-Paare (`die`/`sie`, `das`/`es`).

## 5 · Elf Vorgabefehler — was die Agenten widerlegt haben

Die Paketvorgabe war der schwaechste Teil dieses Buches. Alle elf Fehler
kamen von mir, alle wurden am Bestand oder an den Ausgaben widerlegt:

```
Feuer A2 → A1                    (336 Belege einstimmig)
machen A2 → A1                   (1435)
rückgängig machen C1 → B2        (der einzige Bestandsbeleg)
Wegen: fr/it trugen den Artikel, den der Text als eigenes Token führt
die Mehrwortglosse stand im Infinitiv statt in der 1. Person
Dreschschlitten: Singularreihe zitiert, der Vers hat Plural
Usias: Nominativreihe zitiert, der Vers hat Genitiv
`spricht`: die Regel unterschied nach „Gott" statt nach der STELLUNG
   — alle acht Gerichtsformeln standen deshalb auf `dit`
„mit Gott, der HERR → parle" gilt für die Apposition GOTT, DER HERR,
   nicht für „der Gott der Heerscharen" (LSG liest dort „a dit")
Kalne: die Zwillingsregel führte in die Irre — `Kalno` (Jes 10,9) ist
   die Schreibung eines ANDEREN hebräischen Wortes
„Kinder Israel (2,11) → 4,5" hätte eine Kollisionsauflösung ohne
   Kollisionsstelle propagiert
```

Dazu zwei Fehler in Prompts: die vier Ausgabenlesarten zu 5,26
(`Sikkuth`/`Chiun`) waren **erfunden** — nur RV transliteriert ueberhaupt
(„Quiún") — und die vorgeschlagene `Verbuergen`-Glosse haette in 9,3 mit
`Versteckten` im selben Vers kollidiert.

Daraus ist **`vorgabecheck.py`** entstanden: es haelt Level und Reihen
einer Vorgabedatei gegen den Bestand und jedes Ausgabenzitat gegen deren
Buchtext. Fuer Paket 3 lief es vorab — 0 Befunde.

## 6 · Befunde in den Ausgaben

**Der RIV-Anlautdefekt hat jetzt einen Mechanismus.** Aus einem Einzelfall
(6,6 „la ruina di **iuseppe**") wurde die Messung: **145 Vorkommen** mit
verlorenem G-Anlaut ueber zwoelf Namen, und sie stehen fast alle
unmittelbar hinter einem kurzen Wort — 49× nach `di`, 30× nach `a`, 13×
nach `in`, 7× nach `e`. **8,3 ist der sauberste Beleg:** „grande sarà il
**umero** dei cadaveri" — `umero` 1× im Korpus, `numero` 209×, und es
steht hinter dem kurzen `il`. Vollstaendig in `RIV_ANLAUTFEHLER.md`.

**RIV traegt in 3,14 und 3,15 eine eigene Verszahl im Text** — `(3:13)`
bzw. `(3:14)`. Die RIV-Zaehlung laeuft ab 3,14 um eins zurueck, waehrend
die Dateizaehlung +0 bleibt. Nur diese zwei Verse.

**RIV 4,10 „Io *ha* mandato"** (3. statt 1. Person, derselbe Vers hat
danach zweimal richtig „ho") · **RIV 4,2 „sarete tratte *fiori*"** (→
*fuori*) · **RIV 4,3 bricht ab** (der Halbsatz „spricht der HERR" fehlt).

**RV1909mod siezt durchgehend** (`ustedes`), in Kapitel 2 · 3 · 4 · 5 · 6
· 9 nachgewiesen. Alle spanischen Glossen stehen auf **vosotros**.

**Wo der deutsche Text allein steht:** 2,7 (WEB/LSG/RIV lesen das
hebraeische Verb als „begehren", der deutsche Text als „treten") · 6,2
(dreht die Vergleichsrichtung gegen alle vier) · 6,12 (hat ein Objekt,
das keine Ausgabe hat) · 4,13 (RV kehrt die Richtung um) · 8,3
(WEB/RV „temple", LSG/RIV „palais" — deutsch `Palast`). Ueberall wurde
dem deutschen Text gefolgt.

## 7 · Befunde im Bestand und im Quelltext

- **Amos 9,3 hat einen Fehler im deutschen Text:** `Verbuergen` statt
  `Verbaergen` (Konjunktiv II von `verbergen`). Alle vier Ausgaben lesen
  „verbergen/verstecken", die Form steht korpusweit nur hier. **Nicht
  geaendert** — eine Textkorrektur ist eine andere Entscheidung als eine
  Glossenkorrektur. `NACHLESE_BESTAND.md` D.
- **Ps 78,9 traegt einen Artikel im falschen Genus** (`der` vor
  `Schlacht` als fr *du*, waehrend derselbe Vers *bataille* fuehrt) —
  derselbe Typ wie Ps 65,13 aus der Joel-Arbeit.
- **Apg 23,20 und Dan 2,9** glossieren `haben` bei `sich absprechen` als
  fr *ont* / it *hanno*, waehrend ihr eigener Mehrwort-Eintrag
  *se sont concertés* / *si sono messi d'accordo* liest.
- **`uebrig bleiben` (86×) und `uebrigbleiben` (30×)** stehen als zwei
  Lemmata nebeneinander — eine Spaltung derselben Wendung.
- **`Liegen` loest der Formindex nur aufs Verb auf**, obwohl
  `fixgloss.py show Liege` das Substantiv sofort liefert (Est 1,6 · 7,8).
  Wer nur der Formsuche folgt, glossiert 3,12 falsch.

## 8 · Wortfeld fuer die Nachbarbuecher

```
Gericht und Recht:
  Recht B1 justice·derecho·droit·diritto
  Gerechtigkeit B2 righteousness·justicia·justice·giustizia
     — die zweite `Recht`-Lesart (justicia·justice·giustizia) faellt in
       5,24 und 6,12 in drei Sprachen mit `Gerechtigkeit` zusammen
  recht (Adj) B1 right·recto·droit·retto
  Wermut C1 wormwood·ajenjo·absinthe·assenzio (5,7 · 6,12)
  Urteil B1 · Verbrechen B2 · ausrotten C1 cut off·eliminar·retrancher·eliminare
  Verbannung C1 exile·exilio·exil·esilio
  ausliefern C1 hand over·entregar·livrer·consegnare
  hassen B1 odiar-Reihe  ≠  verabscheuen C1 aborrecer-Reihe

Gottesnamen und Formeln:
  HERR A1 LORD·SEÑOR·ÉTERNEL·SIGNORE  ·  Herr B1 Lord·Señor·Seigneur·Signore
     — im selben Vers nur durch die Grossschreibung getrennt (19 Verse im Korpus)
  Heerschar C1 hosts·ejércitos·armées·eserciti
     „der Gott der Heerscharen": der (davor) of the·de los·des·degli
  Gott A1 God·Dios·Dieu·Dio

Kult:
  Bethel A1 Bethel·Betel·Béthel·Bethel · Gilgal A1 · Beerscheba A1
  Altar B1 · Heiligtum C1 · Kulthöhe C1 · Nasiräer C1 Nazirite·nazareo·naziréen·nazireo
  Brandopfer C1 · Speisopfer C1 · Dankopfer C1 · Schlachtopfer C1
  Fest A2 · Festversammlung C1 · Fasten B2

Landwirtschaft (aus Joel bestaetigt):
  Getreide B1 grain·trigo·blé·grano  ·  Korn B2 corn·grano·grain·frumento
  Wein A2 · Weinberg B1 vineyard·viña·vigne·vigna · Weinstock B2 vine·vid·cep·vite
  Ernte B1 · Saat B2 · Kelter C1 · Tenne B2 · Sichel B2
  Feld A2 field·campo·champ·campo · Acker B1 ground·suelo·sol·suolo (2. Lesart)
  Heuschrecke C1 · Getreidebrand C1 · Mehltau C1

Neu gepraegt in Amos:
  vielfach B2 repeated·repetidos·répétés·ripetuti     (die Gerichtsformel)
  Gefangenengruppe B2 groups of captives·grupos de cautivos·groupes de captifs·gruppi di prigionieri
  Bet-Eden A1 (nach dem Bet-Awen-Muster) · Kalne A1 Calneh·Calne·Calné·Calne
  Harmon A1 (transliteriert — keine zwei Ausgaben lesen gleich)
  Sikkuth A1 · Chiun A1 (dito; nur RV transliteriert ueberhaupt)
  Spätsaat-Wuchs C1 latter growth·heno tardío·regain·guaime
  Maulbeerfeige C1 sycamore figs·higos de sicómoro·figues de sycomore·fichi di sicomoro
  Reichstempel C1 temple of the kingdom·templo del reino·temple du royaume·tempio del regno
  Kapitellknauf C1 · Gewölbe C1 vault·bóveda·voûte·volta
  Traubentreter C1 grape treader·pisador de uvas·fouleur de raisin·pigiatore d'uva
  Klagefrau C1 mourning women·plañideras·pleureuses·piagnone
  Führender B2 leaders·dirigentes·dirigeants·dirigenti
  Lügengötze C1 · Gebüßter C1 · Schnellläufer B2 · Beherzteste C1
  Köder B2 bait·cebo·appât·esca · Beinknochen B2 · Ohrzipfel C1 · Prunkbett C1
  Sommerhaus C1 (Paar zu Winterhaus C1)

Homonyme, die im Bestand die falsche Mehrheit haben:
  Lot A1 plumb line·nivel·niveau·piombino   — NICHT *shekels* (59×)
  Höhle B1 den·guarida·tanière·tana         — NICHT *cave* (33×)
  Beute B2 prey·presa·proie·preda           — NICHT *spoils* (79×)
  Falle B2 trap·trampa·piège·trappola       — gegen das Verb `fallen`
  Angel B1 fishhooks·anzuelos·hameçons·ami da pesca — NICHT die Tuerangel
  Bahn B2 path·senda·sentier·sentiero       — NICHT die Zeltbahn
```

Spanisch durchgehend **vosotros** (in 4,1–4,3 femininem **vosotras**, weil
dort die „Kuehe von Baschan" angeredet sind). Keine Grammatik-Tags in
Klammern (maschinell gegengeprueft: 0 Treffer).
