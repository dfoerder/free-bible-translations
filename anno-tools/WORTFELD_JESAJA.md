# Wortfeld Jesaja (Buch 23)

**66 Kapitel, 1291 Verse, 31 193 Tokens.** Das groesste noch offene Buch —
mehr als Sprueche, Prediger und Hohelied zusammen (2,3-mal Sprueche).

## 1. Verszaehlung — drei Abweichungen, alle nachgemessen

`verszaehlung.py 23` meldet **3 von 66 Kapiteln**. Vers fuer Vers nachgezaehlt:

| Kapitel | de | en | es | fr | it |
|---|---|---|---|---|---|
| 8 | 23 | 22 | 22 | 23 | 22 |
| 9 | 20 | 21 | 21 | 20 | 21 |
| 64 | 11 | 12 | 12 | 11 | 12 |

### Kapitel 8 — `ausgaben.py` liegt hier FALSCH

**Das Werkzeug meldet Versatz −1 fuer en/es/it. Richtig ist 0.**
Es meldet das inzwischen selbst („!! Versatz +0 liegt BESSER", Abstand 0,12
gegen 0,32) — die Warnung ist genau fuer diesen Fall gebaut worden. Gemessen:

- **de 8,1–8,22 = en/es/it 8,1–8,22** — Versatz **0**
- **de 8,23 = en/es/it 9,1** („Doch es bleibt nicht dunkel fuer das Land")
- **fr folgt dem Deutschen** (23 Verse, Versatz 0)

### Kapitel 9 — Versatz +1, das Werkzeug hat recht

- **de 9,n = en/es/it 9,n+1**, weil deren Kapitel 9 mit de 8,23 beginnt
- **fr folgt dem Deutschen** (Versatz 0)

### Kapitel 64 — subtiler, als das Werkzeug meldet

Das Werkzeug meldet Versatz +1 fuer en/es/it und 0 fuer fr, ohne Warnung.
Beides stimmt **ab Vers 2**. Der erste Vers ist ein Sonderfall:

- **de 64,1 verschmilzt en/es/it 64,1 UND 64,2.** Der deutsche Vers traegt
  beides: „dass die Berge vor dir zerfloessen" (deren 64,1) und „wie siedendes
  Wasser durch Feuer, damit dein Name deinen Feinden kund wuerde" (deren 64,2).
- **de 64,n = en/es/it 64,n+1** fuer n >= 2.
- **Franzoesisch hat die erste Haelfte im Vorkapitel**: fr 64,1 entspricht nur
  dem **zweiten** Teil von de 64,1 (Feuer, siedendes Wasser, Feinde); der erste
  Teil steht am Ende von fr 63,19. Ab fr 64,2 = de 64,2 laeuft es gleich.

## 2. Die Leitformel: `Heerscharen` — 60 Verse, im Bestand 34-mal BELEGT

> **KORREKTUR (nach Kapitel 1).** Hier stand zuerst „im Bestand UNBELEGT",
> gestuetzt auf `fixgloss.py show Heerscharen` → nichts. **Das war falsch.**
> Der Bestand normalisiert das Lemma auf den **Singular**: `fixgloss.py show
> Heerschar` liefert **34 Belege**, restlos einheitlich, ohne jede Spaltung.
> Ich hatte die **Wortform** abgefragt statt das **Lemma** — derselbe Fehler wie
> bei `beschwoeren` im Hohelied, zwei Buecher in Folge. Siehe §7.

„Der HERR der Heerscharen" ist die Signaturformel Jesajas und steht in
**60 Versen**, verteilt ueber das ganze Buch (Kap. 19 siebenmal, 10 und 22 je
fuenfmal, 5 und 14 je viermal).

### Gesetzt: Lemma `Heerschar`, C1, *hosts · ejércitos · armées · eserciti*

Drei der vier Ausgaben decken sich mit dem Bestand (RV *ejércitos*,
LSG *armées*, RIV *eserciti*). **Nur WEB weicht ab** und schreibt durchgehend
*Armies* — die WEB-Revision hat „Hosts" flaechendeckend ersetzt, nachgeprueft an
2Sam 5,10 · 1Koen 18,15 · Ps 24,10 · Jak 5,4.

**Der Bestand gewinnt**, und der entscheidende Grund ist nicht die Zahl:

**2. Koenige 19,31 traegt `Heerschar` UND `Rest` in einem Vers** — und dieser
Vers ist die direkte Parallele zu **Jes 37,32**, das Paket 14 uebernehmen wird.
Er steht bereits annotiert im Bestand:

```
Heerscharen  →  Heerschar  C1  hosts · ejércitos · armées · eserciti
Rest         →  Rest       B1  remnant · remanente · reste · resto
```

Mit *Armies* truege derselbe deutsche Satz in Jesaja eine andere Glossenreihe
als in 2. Koenige — genau der Schaden, den §4 als groesste Gefahr des Buches
benennt. Mit *hosts* bleibt das Lemma korpusweit **94-mal einheitlich**.

### Die Kollisionsprobe fuer 13,4 geht auf

| | Heerscharen | Heer | trennt |
|---|---|---|---|
| en | **hosts** | army | lexikalisch |
| es | ejércitos | ejército | Numerus |
| fr | armées | armée | Numerus |
| it | eserciti | esercito | Numerus |

Kollisionsfrei — im Englischen sogar sauberer als bei WEB selbst
(*Armies*/*army*). **13,4 braucht keine Sonderloesung.**

**Aber Achtung fuer Kapitel 13:** `Heer` hat im Bestand auch eine Plurallesart
*armies · ejércitos · armées · eserciti* (11 Belege). Die darf dort **nicht**
genommen werden — sie fiele in allen vier Sprachen mit `Heerschar` zusammen.
In 13,4 steht „ein Heer", Singular.

**Die einzige Kollisionsstelle im ganzen Buch ist 13,4** — der einzige Vers, in
dem `Heerscharen` und `Heer` zusammenstehen: „Der HERR der **Heerscharen**
mustert ein **Heer** zum Kampf." `Heer` ist mit 161/171 Belegen an
*army · ejército · armée · esercito* gebunden. Die Ausgaben trennen dort:

| | Heerscharen | Heer |
|---|---|---|
| WEB | Armies | army |
| RV | ejércitos | **tropas** |
| LSG | armées | armée |
| RIV | eserciti | esercito |

en und es trennen lexikalisch, fr und it **nur ueber den Numerus** — das ist
kein Zusammenfall, sondern ein regulaerer Numerusunterschied. Kapitel 1 legt
die Formel fest, Kapitel 13 entscheidet die Stelle.

`Spross` ist ebenfalls unbelegt (`sproesslinge` 5×) und traegt das messianische
Bildfeld.

## 3. Buchinterne Dubletten — nur fuenf, geringe Dichte

`dubletten.py 23`: **5 Paare auf 1291 Verse** (Hohelied hatte 7 auf 117). Die
Paketreihenfolge kann deshalb der Kapitelzahl folgen — jede Vorlage steht
ohnehin vor ihrer Wiederholung.

| Paar | Aehnlichkeit | Vorlage |
|---|---|---|
| 35,10 ↔ 51,11 | **0,92** | Kap. 35 |
| 2,19 ↔ 2,21 | 0,81 | dasselbe Kapitel |
| 2,11 ↔ 2,17 | 0,68 | dasselbe Kapitel |
| 2,1 ↔ 13,1 | 0,50 | Kap. 2 |
| 48,22 ↔ 57,21 | 0,35 | Kap. 48 |

**Achtung, Lehre aus dem Hohelied:** `dubletten.py` misst **ganze Verse**. Es
findet die gemeinsamen **Teilverse** nicht, an denen dort zweimal gleichzeitig
laufende Kapitel kollidierten. Der **Kreuzvergleich aller Kapitel gegeneinander
vor dem Bauen** ist Pflicht, nicht diese Tabelle.

## 4. Die grosse aeussere Parallele: Jesaja 36–39 = 2. Koenige 18–20

**69 von 90 Versen** haben eine Entsprechung im bereits annotierten und
gebauten 2. Koenige — davon **22 nahezu woertlich** (>= 0,90), 28 nah,
19 teilweise, 21 eigenstaendig. Die Verszuordnung steht in
`JES_36_39_PARALLELEN.md`.

Diese vier Kapitel werden **uebernommen, nicht neu entschieden**. Das ist der
groesste Konsistenzgewinn des Buches — und zugleich die groesste Gefahr, wenn
es unterbleibt: dieselben deutschen Saetze truegen im Bestand zwei verschiedene
Glossenreihen.

## 5. Was der Bestand schon traegt

Jesaja hat **4578 Wortformen, davon 849 formbasiert unbelegt (19 %)**. Nach der
Erfahrung der letzten vier Buecher steht davon der grosse Teil ueber den Stamm
laengst im Bestand:

| Buch | von `hints.py` gemeldet | wirklich neu |
|---|---|---|
| Hld 1 | 20 | 3 |
| Hld 3 | 6 | 2 |
| Hld 5 | 26 | 7 |
| Hld 7 | 18 | 12 |
| Hld 8 | 10 | 3 |

**Immer beide fragen**: `lexicon.py` ueber den Stamm **und** `fixgloss.py show`
ueber das Lemma. Zweimal im Hohelied zeigte der Lexikon-Auszug ein Lemma auch
unter VERWANDT nicht, das `fixgloss.py` sofort fand (`purpurn`,
`Koenigsgewand`, `verstaerken`, `bieten`).

Fest gebunden und fuer das Buch gesetzt (Auswahl der haeufigen):
`HERR` *LORD · SEÑOR · ÉTERNEL · SIGNORE* (4669/4669) ·
`Gerechtigkeit` B2 *righteousness · justicia · justice · giustizia* (200×) ·
`Zorn` B2 *wrath · ira · colère · ira* (216×) ·
`Knecht` B2 *servant · siervo · serviteur · servo* (143×) ·
`Heer` B2 *army · ejército · armée · esercito* (161×) ·
`Goetze` B2 *idols · ídolos · idoles · idoli* (38×) ·
`Rauch` A2 *smoke · humo · fumée · fumo* (28×) ·
`Trost` B2 *comfort · consuelo · consolation · consolazione* (25×) ·
`Heil` B2 *salvation · salvación · salut · salvezza* (17×).

**`Rest` ist zweigeteilt** und das ist ein Jesaja-Thema: 20× *rest · resto ·
reste · resto* (der uebrige Teil) gegen 8× ***remnant** · remanente · reste ·
resto* (der Ueberrest des Volkes). In 1,9 ist es der Ueberrest — alle vier
Ausgaben schreiben *remnant/resto/reste/residuo*. Am Vers entscheiden.

## 6. Vorgehen

Kapitel 1 laeuft allein als **Massstab** und legt `Heerscharen` fest. Danach
Dreierwellen in Kapitelreihenfolge, mit drei Ausnahmen:

- **8 und 9 laufen zusammen** — die Kapitelgrenze verschiebt sich zwischen ihnen.
- **63 und 64 laufen zusammen** — dasselbe.
- **36–39 laufen als eigenes Paket** gegen `JES_36_39_PARALLELEN.md`.

Nach jeder Welle: Kreuzvergleich aller fertigen Kapitel, dann bauen, dann
committen. Nach dem Buch: `BINDUNGEN_AT.md` neu erzeugen.

## 7. Kapitel 1 — der Massstab

31 Verse, 667 Einzelwort- und 32 Mehrwort-Eintraege. Alle sechs Pruefungen
sauber, `glosskollision.py` 0 inhaltliche Paare.

### `Rest` in 1,9 — die Ueberrest-Lesart

**`Rest` B1 = *remnant · remanente · reste · resto***, nicht die Mehrheitslesart
*rest · resto · reste · resto*. Die acht Belege der Ueberrest-Lesart sind
5Mo 4,27 · 28,62 · **2Koen 19,4 · 19,30 · 19,31** · Esra 9,8 · Roem 9,27 ·
11,5 — durchweg der theologische Ueberrest.

Zwei Gruende fuer die **Bestandsform** statt der Ausgabenform in es/it
(RV *resto*, RIV *residuo*):

- **2Koen 19,30/31 = Jes 37,31/32.** Diese Verse kommen in Paket 14 unveraendert
  nach Jesaja. Mit der Ausgabenform spaltete sich Jesaja gegen sich selbst.
- **Roem 9,29 zitiert Jes 1,9 woertlich** und ist bereits annotiert.

### `Recht` darf in Jesaja nie *justicia · justice · giustizia* sein

Der Bestand fuehrt fuer `Recht` eine Nebenlesart *justice · justicia · justice ·
giustizia* (18 Belege). Sie ist in diesem Buch **unbrauchbar**, solange
`Gerechtigkeit` danebensteht — das ist mit 200 Belegen fest an genau diese Reihe
gebunden. In **1,21 und 1,27** stehen beide im selben Vers; die Nebenlesart
haette in **es/fr/it dreifach** kollidiert.

**Gesetzt ist die Bestandsmehrheit `Recht` B1 = *justice · derecho · droit ·
diritto*** (89 Belege). Gilt fuer das ganze Buch. Kein Skript hat diese
Kollision gemeldet — der Agent hat sie durch eigenes Nachzaehlen gefunden und
**vor** dem Schreiben entschaerft.

### Ausgabenkonventionen fuer alle 66 Kapitel

- **RV1909mod: `ustedes` durchgehend.** Ueber das ganze Buch gezaehlt:
  **74× `ustedes`, 0× `vosotros`.** Der Bestand bindet `ihr` an *vosotros*
  (2358 Belege). **Dem Bestand folgen.** Jeder Agent wird die Ausgabe in der
  2. Person Plural anders lesen als seine Glosse — das ist kein Befund und darf
  nicht „korrigiert" werden.
- **RIV1927: verschluckter Anlaut.** Vier Setzfehler **allein in Kapitel 1** —
  eine hoehere Dichte als die sechs im ganzen Hohelied: „ai giorni di **zzia**"
  (1,1, *Uzzia*), „il cuore è **anguente**" (1,5, *languente*), „calcare **i
  mie** cortili" (1,12, *i miei*), „**e vostre** mani" (1,15, *le vostre*).
  Auch ausserhalb Jesajas: 1Koen 18,15 „ad **chab**" statt *Achab*.
  **Wer eine RIV-Form nicht wiedererkennt, pruefe zuerst auf einen fehlenden
  ersten Buchstaben**, bevor er einen Uebersetzungsbefund meldet.
- **WEB: Anfuehrungszeichen als Redemarkierung im Vers**, in Kapitel 1 in neun
  Versen, teils mitten im Vers und ueber Versgrenzen unbalanciert (1,2 oeffnet,
  1,3 schliesst). Verschiebt die Wortgrenzen beim Abzaehlen.

### Lexikonfallen fuer die 65 folgenden Kapitel

| Wort | Bestandslesart | warum sie in Jesaja nicht passt |
|---|---|---|
| `Schlacke` | *écume · schiuma* (2 Belege, Ps 119,119) | dort Schaum-Metapher; Jes 1,22.25 ist metallurgisch → *scories · scoria* |
| `matt` | *weak · apagados · ternes · smorti* (1Mo 29,17) | dort Leas truebe Augen; Jes 1,5 „das Herz ist matt" → *faint · doliente · souffrant · languente* |
| `ausscheiden` | *eliminated · expulsado* (Mt 15,17 / Mk 7,19) | dort Verdauung; Jes 1,25 Metallabscheidung → *remove · quitar · enlever · togliere* |
| `loeschen` | *quench · calman* (Ps 104,11, Durst) | Jes 1,31 ist Feuer → *extinguish · apagar · éteindre · spegnere* |
| `Beule` | *tumors* (7×, Philisterplage) | Jes 1,6 ist Hautbefund → *swellings* (3Mo 14,56) |
| `Huette` | Zelt (21×) | in Jesaja regelmaessig die **Laubhuetten**-Lesart (5×) |
| `Tun` | zweigeteilt | *ways · conduite* (Verhalten, 12×) gegen *doing · agir* (Werk, 3×) — 1,16 das erste, 1,31 das zweite |

**Faustregel, die sich hier bestaetigt hat:** bei Lemmata mit ein bis drei
Belegen zaehlt die **Bedeutung**, nicht die Zahl. Die duenn belegten Woerter
sind die gefaehrlichen, nicht die haeufigen.

### Wo Bestand und Quelltext gegen die Ausgaben stehen

- **`Eiche` (1,29 · 1,30)**: **drei von vier Ausgaben weichen ab** — RV
  *olmos* (Ulme), LSG *térébinthes*, RIV *terebinti*. Nur WEB folgt dem
  Deutschen. Bestand *oak · encina · chêne · quercia* genommen.
- **`Blei` (1,25)**: WEB *tin*, RV *estaño* (Zinn) gegen LSG *plomb*, RIV
  *piombo* und den deutschen Text. Bestand genommen.
- **`Nachtwache` (1,8)**: **alle vier** Ausgaben schreiben „Huette" — sie
  uebersetzen das Hebraeische, nicht das Deutsche. Der Quelltext sagt
  `Nachtwache`, und die App glossiert das deutsche Wort.
- **`spricht`**: die Formel „spricht der HERR" (1,11 · 1,18 · 1,24) nimmt die
  Nebenlesart *says · dice · **dit** · dice* (LSG schreibt dort *dit*); in
  **1,2** („Denn der HERR spricht") dagegen *speaks · habla · parle · parla*.
  Zwei Lesarten, am Vers entschieden.

### Neues Vokabular (14 Lemmata, alle mit `belegt.py` und `fixgloss.py` geprueft)

`emporbringen` C1 · `eiternd` C1 · `Gurkenfeld` C1 · `Mastkalb` C1 ·
`Festfeier` C1 · `blutrot` B2 · `schneeweiss` B2 · `verwaessern` C1 ·
`Diebesgeselle` C1 · `ausschmelzen` C1 · `Umkehrender` C1 · `erroeten` C1 ·
`welk` B2 · `Werg` C1.

Mehrwort neu: `gleich wie` B1 · `genug haben` B2 · `aus tiefster Seele` C1 ·
`zu Anfang` B1.

`hints.py` meldete 23 unbelegte Formen, **14 waren wirklich neu** — eine
deutlich hoehere Quote als im Hohelied (dort 3 von 20 bis 12 von 18). Jesaja hat
tatsaechlich viel eigenes Vokabular.

### Fuer das ganze Buch gesetzt

`Heiliger (Israels)` B1 *Holy One · Santo · Saint · Santo* ·
`Maechtiger (Israels)` B2 *Mighty One · Poderoso · Puissant · Potente* ·
`Fuerst` B2 *princes · príncipes · princes · principi* ·
`Uebertreter` C1 / `Suender` B2 · `Waise` B2 / `Witwe` B1 ·
`wehe` B2 *Woe · Ay · Malheur · Guai* (die Weheruf-Kapitel) ·
Mehrwort `Recht verschaffen` B2 · `die Sache fuehren` B2.

**`HERR` / `Herr` ist korpusweite Konvention und nicht anzutasten:** der Bestand
hat **72 Verse** mit beiden Lemmata nebeneinander (die Adonai-JHWH-Formel, hier
1,24) und trennt immer ueber Gross-/Kleinschreibung. `glosskollision.py` fuehrt
das in einer eigenen, nicht mitgezaehlten Rubrik.

## 8. Paket 2 (Kap. 2 · 3 · 4)

### `belegt.py` hat sich in seiner ersten Welle bezahlt gemacht

Das Werkzeug wurde nach dem `Heerscharen`-Fehler gebaut. In dieser Welle hat es
**mehr als zwanzig** Form/Lemma-Abweichungen aufgedeckt, bei denen
`fixgloss.py show` geschwiegen haette:

| Kapitel | von `hints.py` als unbelegt gemeldet | wirklich neu |
|---|---|---|
| 2 | 13 | 6 |
| 3 | 22 | 15 |
| 4 | — | 4 |

Kapitel 3 allein fand dreizehn Formen, deren Lemma anders heisst (`Mäntel` →
`Mantel` 32 Belege, `Turbane` → `Turban`, `Halsketten` → `Halskette`,
`Ohrringe` → `Ohrring`, `Festgewänder` → `Festgewand`, `Hemden` → `Hemd`,
`Ringe` → `Ring`, `Umhänge` → `Umhang` …). Kapitel 2 fand **`Anbeten` mit 26
Belegen** unter dem Infinitiv-Lemma `anbeten`.

**Aber das Werkzeug zeigt nur hin, es urteilt nicht.** Bei `hochmütigen` (2,11)
fand es neun Belege unter `Hochmütiger` — dem **substantivierten** Lemma. Im
Vers steht das Wort attributiv bei `Augen`, ist also das Adjektiv `hochmütig`,
das eigenstaendig mit 13 Belegen dasteht. Der Agent hat das Lemma korrigiert.

### Die zwei buchinternen Dubletten von Kapitel 2

- **2,11 ↔ 2,17** ist **nicht** parallel gebaut: 2,11 hat *Augen + erniedrigen*,
  2,17 *Hochmut + sich beugen*, und `sich beugen` wandert zwischen den Versen
  von den Stolzen auf den Hochmut. Woertlich gleich sind nur der Mittelteil
  (`die Stolzen werden sich … muessen`) und die Schlussformel (Pos 15–23 gegen
  14–22) — dort Glosse fuer Glosse identisch.
- **2,19 ↔ 2,21**: der Schwanz ab Position 7 ist in **Wortlaut und Glossen
  identisch**, 19 Eintraege, nachgeprueft. Der Kopf hat **vier verschiedene
  Komposita**, nicht zwei: `Felsenhöhle` + `Erdkluft` (2,19) gegen `Felsspalte`
  + `Steinkluft` (2,21). Systematik der Trennung:
  **Höhle→caverna, Kluft→grieta/crepaccio, Spalte→hendidura/fenditura.**

### Entscheidungen, die weiterlaufen

- **`Mantel` gegen `Umhang` (3,22) — die teuerste Stelle des Schmuckkatalogs.**
  `Mantel` ist mit 28 von 32 Belegen an *cloak · manto · manteau · mantello*
  gebunden, **und WEB, LSG und RIV setzen genau diese Woerter an den anderen
  Slot.** Wer der Ausgabe folgt, spaltet `Mantel` gegen seine 32 Belege — und
  `Mantel` steht in **3,6 desselben Kapitels** noch einmal. Bestand behalten,
  `Umhang` weicht auf *capes · capas · capes · scialli*.
- **`Spross` C1 = *branch · renuevo · germe · germoglio*** (4,2). Das Substantiv
  ist wirklich unbelegt — `belegt.py` findet nur die Verbform `spross` von
  `sprießen` und warnt selbst vor der Verwechslung. Gewaehlt ist die Reihe, die
  in **fuenf von sechs** Belegstellen des ganzen Prophetenkorpus so dasteht
  (Jes 4,2 · 11,1 · Jer 23,5 · 33,15 · Sach 3,8 · 6,12) — die Reihe des
  **Motivs**, nicht die einer Stelle. Damit bleibt **11,1** kollisionsfrei, wo
  `Reis` und `Spross` im selben Vers stehen: `Reis` ist unbelegt und kann
  *shoot · vara · rameau · ramo* frei nehmen.
  **`Spross` steht im Buch nur zweimal** (4,2 · 11,1) — die „fuenf
  Sproesslinge" der Vorbereitung sind Verbformen von `sprießen`.
- **`einhergehen` gegen `schreiten` (3,16)** — von keinem Skript gemeldet.
  Der Bestand bindet `schreiten` an *stride · caminan · **marchent** ·
  incedono*, und **LSG schreibt fuer `einhergehen` ebenfalls „marchent"**. Wer
  der Ausgabe folgt, kollidiert. `einhergehen` weicht auf *walk along · andan ·
  s'avancent · se ne vanno*.
- **`Fremder` B1 gegen `Fremde` B2** — dieselbe Wortform, zwei Woerter. In 1,7
  sind es Personen (*strangers · extranjeros*), in 2,6 ist „Kinder der Fremde"
  der **Genitiv Singular** des fremden Landes (*foreign land · extranjero ·
  étranger · estero*); der Plural von `Fremder` hiesse „der Fremden".
  `buildbook.py` meldet die Levelspreizung — sie ist richtig.

### Neue Lexikonfallen

| Wort | Bestandslesart | warum sie hier nicht passt |
|---|---|---|
| `Umhang` | *hangings · cortinas · toiles · cortine* (12×, Stiftshuette) | 3,22 ist ein Kleidungsstueck |
| `Wohlgeruch` | *pleasing aroma · olor grato* (1 Beleg, 3Mo 2,12, Opfersprache) | 3,24 ist Parfuem, dem `Gestank` gegenuebergestellt |
| `einhergehen` | *goes along with* (Jak 2,1, abstrakt) | 3,16 ist koerperliches Gehen |
| `verfuehrerisch` | *deceiving* (1Tim 4,1, Geister) | 3,16 sind Blicke → *seductive* |
| `erhaben` | *exalted · exaltado · élevé · esaltato* (9×) | **praedikativ** richtig (2,2 · 2,11 · 2,12 · 2,17), **attributiv** in 2,14 „erhabene Huegel" → *lofty · elevadas · élevées · elevate* |
| `Erde` | — | 2,10: **alle vier** Ausgaben schreiben „Staub"; der Quelltext sagt `Erde`, und dasselbe Lemma steht in 2,19/2,21 im selben Kapitel |

### Zwei Bestandsbefunde, die spaeter teuer werden koennen

- **`Ohrring` B2 und `Ohrgehänge` B2 tragen restlos dieselbe Reihe**
  *earrings · pendientes · boucles d'oreilles · orecchini* unter **zwei
  Lemmata**. Ebenso **`Armreif` B2 und `Armring` C1** (*bracelets · brazaletes ·
  bracelets · braccialetti*) — dieselbe Sache, verschiedenes Level. In jedem
  Vers, der beide fuehrte, waere das eine Vier-Sprachen-Kollision.
- **`Hoheit` C1 (9 Belege) und `Majestät` (4) tragen beide**
  *majesty · majestad · majesté · maestà*. Solange sie in verschiedenen Versen
  stehen, nicht aufloesen; wo sie zusammentreffen, weicht `Hoheit`.
- **`Knabe` C1 (1 Beleg) neben `Junge` A1** — dieselbe Sache, Levelspreizung
  A1↔C1. Beide stehen in 3,4 / 3,5 nebeneinander, durch den Numerus getrennt.
  Bestand befolgt, nicht korrigiert.

### Ausgabenbefunde

- **RIV: zwei neue Setzfehler** — 3,8 „**rovocare**" (*provocare*), dazu ein
  Numerusfehler 3,16 „le **figliuolo** di Sion" (*figliuole*) und ein
  Personenfehler 3,14 „nelle **nostre** case" (muesste *vostre* sein, es ist
  Gottes Anklage gegen die Aeltesten). **Kapitel 2 hat keinen einzigen** — die
  Dichte schwankt stark.
- **RV1909mod: die spanische Schmuckliste 3,18–23 ist gegen das Deutsche
  verschoben.** 3,19 beginnt mit *los collares* (deutsch 3,18), 3,23 setzt
  *los tocados* an die `Schleiertücher`-Stelle. **Nach der deutschen Bedeutung
  glossieren, nicht nach dem spanischen Slot.**
- **2,16 hat im Deutschen keinen Eigennamen**: „alle **Schiffe im Meer**", wo
  alle vier Ausgaben *Tarsis* tragen.

### Vorlagen fuer spaetere Kapitel (aus `parallelen.py`, nicht aus `dubletten.py`)

- **2,20 → 31,7** — Neun-Token-Block „jenem Tag wird jeder seine silbernen und
  goldenen Götzen" (Aehnlichkeit 0,52)
- **2,12 → 13,9** — Fuenferblock „Denn der Tag des HERRN"
- **2,22 → 10,20** — „nicht mehr auf den"
- **2,1 → 13,1** — die Ueberschriftformel; 2,1 steht vollstaendig im Bericht und
  ist gegen Jes 1,1 **und** 2Koen 19,2 abgeglichen

Das ist dasselbe Muster wie im Hohelied: **`dubletten.py` misst ganze Verse und
findet diese Teilvers-Parallelen nicht.** Der Kreuzvergleich vor dem Bauen
bleibt Pflicht.

### Auflösungen, die NUR an ihrer Stelle gelten

`weil` es *ya que* (nur 3,8) · `Unglück` fr *infortune* (nur 3,9) · `einer`
fr *quelqu'un* (nur 3,6) · `in` *within · dentro de · dans · dentro* (nur 3,7) ·
`einzig` es *único* it *unico* (nur 4,1) · `aus` *out of · desde · depuis · da*
(nur an Bewegungsstellen).

## 9. Paket 3 (Kap. 5 · 6 · 7)

### Zwei Luecken in `belegt.py`, beide von Agenten gefunden und geschlossen

1. **Die Umkehrung der Heerschar-Falle** (Kap. 6): `forttreiben` steht im
   Bestand nur als `forttreibt` / `treibt fort` / `treibe fort`. Die Formsuche
   meldete „nicht belegt", `fixgloss.py show` lieferte drei Belege. Das Werkzeug
   indiziert jetzt **Form und Lemma**. Wirkung ueber das ganze Buch: die Zahl
   der scheinbar unbelegten Wortformen faellt von **849 auf 708**.
2. **Der starre Praefixvergleich** (Kap. 5): `sauer` wurde zu `saure` nicht
   gefunden (Vokalwechsel), `hacken` nicht zu `gehackt` (ge-Praefix). Jetzt mit
   Endungsabbau, Umlautaufloesung und Aehnlichkeitsmass; Lemma-Kandidaten werden
   getrennt ausgewiesen.

**Was das Werkzeug weiterhin nicht kann, und auch nicht soll:** urteilen. Bei
`reihen` (5,8) und `brausen` (5,30) meldet es die **grossgeschriebenen
Substantive** `Reihe` und `Brausen` und warnt vor der Verwechslung — im Vers
stehen die Verben. Bei `hochmütigen` (2,11) wies es auf das substantivierte
`Hochmütiger`, gebraucht ist das Adjektiv. **Es zeigt hin; entschieden wird am
Vers.**

### Die Recht/Gerechtigkeit-Probe in 5,7

Die kritischste Stelle des Buches, weil beide Woerter im selben Vers stehen:

| | Recht | Gerechtigkeit |
|---|---|---|
| en | justice | righteousness |
| es | **derecho** | justicia |
| fr | **droit** | justice |
| it | **diritto** | giustizia |

In allen vier Sprachen getrennt. Die 18-Beleg-Nebenlesart von `Recht`
(*justice · justicia · justice · giustizia*) haette hier **dreifach**
kollidiert. WEB schreibt an dieser Stelle selbst „justice … righteousness".

**5,16 hat kein `Recht`, sondern `Gericht`** B2 *judgment · juicio · jugement ·
giudizio* — die im Auftrag angekuendigte zweite Gegenueberstellung gibt es
nicht. `Recht` steht im Kapitel nur zweimal (5,7 · 5,23).

### Vom Koordinator angeglichen

- **`herbeipfeifen`** — Kapitel 5 und 7 haben dasselbe neue Lemma
  **unabhaengig voneinander erfunden** und drei von vier Glossen verschieden
  gesetzt. Angeglichen auf die Fassung aus Kapitel 7 (*whistle for · llamar con
  un silbido · siffler · fischiare*), weil fr und it dort den Ausgaben an
  **beiden** Stellen folgen. Das ist eine neue Klasse von Wellendivergenz: nicht
  ein Teilvers, sondern ein **neues Lemma an zwei Stellen derselben Welle**.
- **`Gesicht`** — Kapitel 3 nahm die 8-Beleg-Variante *cara · faccia*, der
  Bestand hat mit **94 von 110** Belegen *face · rostro · visage · volto*.
  Auf die Mehrheit angeglichen.

### Neue Lexikonfallen

| Wort | Bestandslesart | warum sie hier nicht passt |
|---|---|---|
| `Rebe` | *branch · sarmiento · sarment · tralcio* (5×, **alle Joh 15**) | 5,2 ist die Pflanze, nicht der Trieb → *vines · vides · ceps · viti* |
| `beschneiden` | *circumcised* (23×) | 5,6 ist Rebschnitt → *pruned · podada · taillée · potata* |
| `Joch` | *yoke · yugo · joug · giogo* (27×) | 5,10 ist ein **Flaechenmass** → *acres · yugadas · arpents · iugeri* |
| `sperren` | *locked · encerraron* (2×) | 5,14 ist `aufsperren`, die Gegenbewegung |
| `halten` | *keep · guardar · garder · osservare* (69×) | 7,21 ist **Vieh** halten → *criar · entretenir · nutrire* |
| `bestellen` | *appointed · designó* | 7,25 ist **Boden** bestellen → *cultivated · cultivaba* |
| `Fall` | *cases* (2Mo 18,22) | 6,13 `Fällen` ist das nominalisierte **Baumfaellen** |

### Der `Teich` in 7,3 — Kapitelkonsistenz schlaegt die Ausgabe

Der Bestand fuehrt zwei Zeilen 1:1: *estanque · **étang · stagno*** (2Sam 2,13)
gegen *estanque · **piscine · piscina*** (2Koen 18,17). **LSG und RIV schreiben
in Jes 7,3 selbst *étang* / *stagno*.** Genommen ist trotzdem die
2-Koenige-Zeile, weil **7,3 wortgleich mit Jes 36,2** ist und 36,2 in Paket 14
aus 2Koen 18,17 uebernommen wird. Mit der Ausgabenform spaltete sich Jesaja
gegen sich selbst. Dasselbe gilt fuer `Wasserleitung`, `ober`, `Straße` und
`Walkerfeld` in diesem Vers.

### `Immanuel` — die Auftragspraemisse traf nicht zu

Ich hatte einen Konflikt konstruiert: der Bestand trage den Namen bei Matthaeus
**gedeutet**, Jesaja duerfe ihn nicht deuten. **Der Bestand traegt ihn
undeutet** (*Immanuel · Emanuel · Emmanuel · Emmanuele*). Die Deutung sitzt in
Mt 1,23 auf **eigenen deutschen Tokens** („Das heisst uebersetzt: Gott mit
uns"), weil der Matthaeustext sie selbst ausspricht — sie ist Teil des Verses,
nicht der Glosse. Es gab nichts aufzuloesen.

**Und Mt 1,23 ist kein woertliches Zitat von Jes 7,14.** Gemeinsam sind sieben
Tokens (`Jungfrau wird schwanger werden und einen Sohn`); ab `gebaeren` laeuft
der Text auseinander (Mt: „zur Welt bringen … man wird ihm den Namen geben",
Jes: „gebaeren … sie wird ihn Immanuel nennen").

Ebenso **kein einziges der fuenf NT-Zitate von 6,9–10 ist woertlich** (Mt 13,14
· Mk 4,12 · Lk 8,10 · Joh 12,40 · Apg 28,26). Die Uebereinstimmung besteht auf
**Lemma**-Ebene; der einzige echte Block ist `das Herz dieses Volkes`. Bei
`umkehren` ist dennoch die **Zitatlesart** *repent · arrepentirse · se repentir ·
ravvedersi* genommen, weil genau diese Stellen genau diesen Vers zitieren.

### `Seraph` und `Dickmilch` — zwei echte Neuschoepfungen

- **`Seraph` C1 = *seraphim · serafines · séraphins · serafini*** (6,2 · 6,6).
  Der Quelltext schreibt **`Seraphim` mit ph**. Alle vier Ausgaben einstimmig
  das Lehnwort. `hints.py` schlug als „verwandt" `Serah`/`Seraja` vor — das sind
  Personennamen aus Juda-Genealogien.
- **`Dickmilch` C1 = *curds · cuajada · crème · crema*** (7,15 · 7,22 zweimal —
  alle drei Vorkommen des Buches stehen in Kapitel 7). **Nur WEB weicht mit
  *butter* ab**, und das uebersetzt das Hebraeische, nicht das deutsche Wort.

### Bestandsbefunde: das Korpus fuehrt Sachdubletten unter getrennten Lemmata

Nach `Ohrring`/`Ohrgehänge` und `Armreif`/`Armring` aus Paket 2 bestaetigt sich
das Muster:

- **`Trommel`, `Tamburin` und `Pauke`** stehen jetzt alle drei auf
  *tambourine · pandero · tambourin · tamburello*.
- **`Assyrien` (67 Belege) und `Assur` (7)** sind in **allen vier Sprachen**
  identisch (*Assyria · Asiria · Assyrie · Assiria*). In 7,17/7,20 gegen 7,18
  stehen sie in **benachbarten** Versen — sobald einer beide fuehrt, ist es eine
  Vier-Sprachen-Kollision.
- **`Getöse` und `Brausen`** teilen sich spanisch *estruendo*.

### Ausgabenbefunde

- **RIV: vier neue Fehler**, keiner in `RIV_SETZFEHLER_JESAJA.md` — 5,27
  „de' **ianchi**" (*fianchi*), 5,4 „mentr'io **'aspettavo**" (*m'aspettavo*),
  7,20 „un **rasoi**" (*rasoio*), 7,25 „**i** si lasceran" (*vi*). Die Liste
  zaehlt nur **Eigennamen** aus; ihre Grenzen stehen jetzt in der Datei.
  **Kapitel 6 hat null.**
- **Zwei Fehlalarme in meinen eigenen Auftraegen**: ich hatte 6,1 „anno" und
  7,2/7,18 „alla"/„alle" aus der **ungefilterten Rohliste** zitiert. Das sind
  gewoehnliche italienische Woerter. Beide Agenten haben es gemeldet statt
  uebernommen.
- **LSG 5,30 hat einen Zusatz ohne deutsche Entsprechung** („Avec des
  alternatives d'angoisse et d'espérance").
- **RV 5,10 rechnet die Masse um** („treinta medidas" statt Homer/Efa).
- **6,4**: drei von vier Ausgaben uebersetzen `Türschwellen` nicht (LSG/RIV
  „Tueren", RV „Tuerangeln"); nur WEB *thresholds*.
- **6,13 `Eiche`: RV schreibt *olmo* (Ulme)** — dieselbe Abweichung wie in
  1,29/1,30. Bestand genommen.

## 10. Paket 4 (Kap. 8 · 9) — die verschobene Kapitelgrenze

### Verszaehlung, von beiden Agenten unabhaengig nachgemessen

Beide haben die Kapiteldateien direkt aufgeschlagen statt `ausgaben.py` zu
glauben. Ergebnis deckt sich mit §1:

| | Kap. 8 | Kap. 9 |
|---|---|---|
| de | 23 | 20 |
| fr | 23 (Versatz 0) | 20 (Versatz 0) |
| en/es/it | 22 — **de 8,1–22 = deren 8,1–22 (Versatz 0)**, de 8,23 = **deren 9,1** | 21 — **de 9,n = deren 9,n+1** |

**Der staerkste unabhaengige Beleg kommt von RIV selbst**: die Ausgabe traegt in
Kapitel 9 durchgehend Klammernummern, und die laufen von `(8:23)` in ihrem 9,1
bis `(9:20)` in ihrem 9,21 — **exakt die deutsche Zaehlung**.

`ausgaben.py` wendet fuer Kapitel 8 weiterhin den falschen Versatz −1 an und
warnt selbst darueber. **Die Warnung hat recht, die angewandte Zahl nicht.**

### Der vierfache Kehrvers — nachgeprueft identisch

„Bei alledem wendet sich sein Zorn nicht ab, seine Hand bleibt erhoben" steht in
**5,25 · 9,11 · 9,16 · 9,20**. Alle vier sind ueber zwei Kapitel hinweg
**Eintrag fuer Eintrag, Lemma fuer Lemma, Level fuer Level identisch**
(12 Eintraege ab `Bei`, maschinell verglichen).

**Der Wortlaut im Auftrag war falsch**: es heisst „seine Hand bleibt
**erhoben**", nicht „und seine Hand bleibt ausgestreckt". `ausgestreckt` kommt
im Kapitel nicht vor.

**`parallelen.py` weist denselben Zwoelf-Token-Block in 10,4 aus** — dort noch
unannotiert. Kapitel 10 uebernimmt die Reihe aus `ch9.json`.

### Wenn der l1912mod einen Namen selbst uebersetzt

**Der Name in 8,1 und 8,3 ist nicht `Maher-Schalal-Hasch-Bas`**, sondern
**`Schnell-Raub-Eilige-Beute`** — vier deutsche Woerter. Der Text deutet selbst.

Der Agent hat Praezedenz im Bestand gefunden: Luther macht das gelegentlich, und
das Korpus folgt ihm bei **`Doppelhöhle`** C1 fuer Machpela (3 Belege) und
**`Warte`** C1 fuer Mizpa. Beide sind nach der **deutschen Bedeutung**
glossiert. Gegengeprueft: alle uebrigen rund achtzig Bindestrich-Lemmata des
Bestands (`Baal-Hamon`, `Adoni-Zedek`, `Abel-Mehola` …) sind Transliterationen
und bleiben es. **Die Regel steht jetzt in `AUFTRAG_BUCH.md`.**

Die Ausgaben helfen hier nicht: **LSG und RIV uebersetzen in 8,1 und
transliterieren in 8,3**, WEB und RV transliterieren beide Male.

### Die vier Thronnamen in 9,5

**Auch hier war mein Wortlaut falsch.** Der Text hat nicht vier
Bindestrich-Komposita, sondern **drei Adjektiv-Substantiv-Paare und ein
Kompositum**: „Wunderbarer Ratgeber, starker Gott, ewiger Vater, Friedefürst" —
sieben Tokens.

**WEB, RV und LSG lesen fuenf Namen**, weil sie „Wunderbarer" und „Ratgeber"
trennen. **Nur RIV liest vier wie das Deutsche.**

Zwei Entscheidungen gegen die Ausgaben:

- **`wunderbar` B1** *wonderful · maravilloso · merveilleux · meraviglioso* —
  attributives Adjektiv, nicht das Substantiv. RV/LSG/RIV schreiben
  *Admirable/ammirabile*; der Bestand ist mit ~17 Belegen restlos gebunden, und
  das Wort kehrt in **25,1 · 28,29 · 29,14** wieder.
- **`stark` A1** *strong · fuerte · fort · forte* — **alle vier Ausgaben sagen
  etwas anderes** (*Mighty · puissant · potente*). Mit deren Reihe waere die
  Trennung zu **`Mächtiger (Israels)`** verloren, das im Buch fest an
  *Mighty One · Poderoso · Puissant · Potente* gebunden ist (§7).

**`Friedefürst` C1** *Prince of Peace · Príncipe de paz · Prince de la paix ·
Principe della Pace* ist wirklich neu; dort entscheidet die Ausgabe, weil der
Bestand fuer das Kompositum schweigt und alle vier einstimmig sind.

### 9,6 — die zweite Recht/Gerechtigkeit-Stelle

Wie in 5,7 in **allen vier Sprachen getrennt**: `Recht` *justice · derecho ·
droit · diritto* gegen `Gerechtigkeit` *righteousness · justicia · justice ·
giustizia*. **RV schreibt hier *juicio*** — das ist die Reihe von `Gericht`.
Bestand genommen.

Dazu eine Dreier-Nachbarschaft, die der Auftrag nicht nannte: **`Herrschaft` ·
`Thron` · `Königreich`** im selben Vers. `Herrschaft` nimmt die
**Zweitzeile** *dominion · dominio · **domination** · dominio* (12 Belege, LSG
schreibt selbst *domination*) — die Mehrheitszeile *reign · reinado · règne ·
**regno*** waere italienisch mit `Königreich` zusammengefallen.

### Und wieder: kein NT-Zitat ist woertlich

**Mt 4,16 ↔ Jes 9,1** — 21 gegen 23 Tokens, drei Bloecke (4+3+6), und **jedes
finite Verb ist verschieden** (`wandelt`/`lebte`, `sieht`/`hat gesehen`,
`wohnen`/`saßen`, `strahlt auf`/`ist aufgegangen`). Matthaeus schreibt
**`Dunkeln`**, Jesaja **`Finstern`** — zwei verschiedene deutsche Woerter.

Das ist der dritte Befund dieser Art: Mt 1,23 ↔ Jes 7,14 (sieben Tokens), die
fuenf Zitate von 6,9–10 (keines woertlich), jetzt Mt 4,16. **Uebereinstimmung
besteht auf Lemma-Ebene, nicht im Wortlaut.**

### Vom Koordinator angeglichen

**`zerschmettert`** — 1,28 und 8,9 stehen beide im Plural Passiv. Der Bestand
ist selbst gespalten (*destrozados* 3 Belege Plural, *quebrantado* 4 Belege
Singular); Kapitel 8 hatte die Singularzeile pluralisiert. Auf die Plural-Zeile
aus Kapitel 1 angeglichen.

### Die fuenfte Sachdublette des Bestands

Nach `Ohrring`/`Ohrgehänge`, `Armreif`/`Armring`, `Hoheit`/`Majestät` und
`Trommel`/`Tamburin`/`Pauke` jetzt:

**`Finsternis` C1 (82×), `Dunkel` B1 (26×) und das neue `Finster` C1 tragen alle
drei *darkness · tinieblas · ténèbres · tenebre*** — mit Levelspreizung B1↔C1.
`Dunkel` steht in Mt 4,16, `Finstern` in Jes 9,1: **derselbe Satz in zwei
Buechern, zwei verschiedene deutsche Woerter.**

Kapitel 8 hat `Dunkel` an seiner eigenen Stelle (8,22, neben `Finsternis`) auf
die Zweitzeile *gloom · penumbra · obscurité · buio* ausweichen lassen.

Dazu neu: **`Fraß` C1 und `Nahrung` B1** teilen sich *food · comida ·
nourriture* und trennen nur italienisch (*pasto* / *cibo*).

### Duenn belegte Lemmata, bei denen die Bedeutung schlug

| Wort | einziger Beleg | warum er nicht traegt |
|---|---|---|
| `abhauen` B2 | 5Mo 25,12, *amputar · amputare* (eine Hand) | 9,13 ist „Kopf und Schwanz" metaphorisch → *cut off · cortar · trancher · recidere* |
| `stampfen` C1 | Ri 5,22, *piaffèrent · scalpitarono* (Pferdehufe) | 9,4 stampft ein **Stiefel**; beide Woerter sind ausschliesslich equin → fr *piétine*, it *pesta* |
| `Treiber` B2 | Hiob 39,7, *arriero · conducente* | 9,3 ist ein menschlicher Fronvogt; **alle vier Ausgaben schreiben „Unterdrücker"**. Bestand trotzdem gehalten, gemeldet |

### Ausgabenbefunde

- **RIV: sieben neue Fehler in dieser Welle**, nur einer in der Liste. Neue
  Klassen: **9,5 „arà chiamato"** (*sarà* — Anlaut an einem Nicht-Eigennamen,
  nach 7,25 der zweite Fund) und **9,5 „un fanciullo ci è nato, un fanciullo ci
  è stato dato"** — RIV wiederholt *fanciullo* fuer `Kind` **und** `Sohn`, wo
  *figliuolo* stehen muesste. Das ist eine **lexikalische Dublette**, eine
  dritte Fehlerklasse. Dazu 8,2 `eberekia`, 8,14 `Ed gli` und `n laccio`,
  8,1 „carattere leggibili".
- **RV 9,2 ist negiert**: „Multiplicaste el pueblo, **pero no** aumentaste la
  alegría" — gegen Deutsch, WEB, LSG und RIV. RV folgt der Ketiv-Lesart.
- **WEB 8,14 laesst einen halben Vers aus** („ein Stein des Anstoßes und ein
  Fels des Straucheln" fehlt ganz). Fuer diese beiden Glossen gab es nur drei
  Ausgaben; entschieden hat der Bestand ueber **Roem 9,33**, das genau diesen
  Vers zitiert.
- **WEB 9,4 loest `Stiefel` ganz auf** („the armor of the armed man").
- **LSG und RIV setzen 9,14/9,15 in Klammern**, WEB und RV nicht.

## 11. Paket 5 (Kap. 10 · 11 · 12)

Drei Kapitel gleichzeitig, 1149 Einzelwort- und 42 Mehrwort-Eintraege. Alle
sechs Pruefungen je Kapitel sauber; `validate.py 23` und `qa.py 23` melden
ueber das ganze gebaute Buch **0 Befunde**.

### `Stock` traegt im selben Kapitel zwei Zeilen — und das ist richtig so

Kapitel 10 hat das Wort dreimal neben einem zweiten Stab-Wort:

| Stelle | Paar | `Stock` | Gegenwort |
|---|---|---|---|
| **10,5** | Stock + `Rute` | *staff · bastón · bâton · bastone* | `Rute` B2 *rod · vara · verge · verga* |
| **10,15** | Stock + `Stab` | *rod · palo · verge · verga* (= Jes 9,3) | `Stab` B1 *staff · bastón · bâton · bastone* |
| **10,24** | Stock + `Stab` | *rod · palo · verge · verga* | `Stab` wie oben |

Beide Zeilen sind **Bestandszeilen**, keine Erfindung. `Rute` ist 13/13
einheitlich, `Stock` im Bestand sechsfach gespalten — also weicht `Stock` aus.
Die Jes-9,3-Zeile kollidierte in 10,5 gleich dreifach (en/fr/it), die
4-Beleg-Zeile *rod · palo · bâton · bastone* einfach; nur die staff-Zeile ist
dort kollisionsfrei. **Die Auflosung sitzt an der Kollisionsstelle, nicht am
Lemma** — genau die Regel aus `AUFTRAG_BUCH.md`.

Gegenprobe an den Ausgaben: WEB trennt in 10,5 spiegelbildlich (rod/staff),
**LSG schreibt zweimal `verge` und trennt gar nicht**, RV vertauscht in 10,15
und 10,24 (bastón/vara). In 10,15/24 deckt sich die Wahl Wort fuer Wort mit
WEB, LSG und RIV.

### Vom Koordinator angeglichen — dreimal

**1. `Völker` in 8,23 und 10,7.** Beide Kapitel hatten dort die Zeile
*nations · naciones · nations · nazioni* gesetzt, **weil ihre Ausgaben es so
schreiben** (RIV 10,7 „sterminare **nazioni**", RIV 8,23 „la Galilea de'
**Gentili**"). In den uebrigen sieben Belegen des Buches (2,2 · 2,3 · 2,4 ·
3,13 · 5,26 · 8,9 · 10,13 · 10,14 · 11,10 · 11,12 · 11,14) steht
*peoples · pueblos · peuples · popoli* — und **`Nationen` ist ein eigenes
deutsches Wort mit genau der nations-Zeile** (2,4 · 11,10, in 11,10 sogar im
selben Vers wie `Völker`). Nach der Faustregel „die Ausgabe liefert den Namen,
der Bestand die Bedeutung" gewinnt bei einem gewoehnlichen Wort mit 199 von 252
Belegen die Bindung. Beide Stellen auf *peoples* gezogen.

**Und die Genusfalle aus 5. Mose ist prompt wieder aufgetreten**: *naciones ·
nations · nazioni* sind feminin, *pueblos · peuples · popoli* maskulin. Mit dem
Wort zusammen mussten

- **10,7 pos 21 `wenige`** von *pocas · poche* auf *pocos · pochi* und
- **8,23 pos 41 `der`** von *de las · delle* auf *de los · dei*

Damals blieben 28 solcher Nachbarn stehen. **Nach jeder Glossenaenderung die
Nachbarpositionen mitpruefen.**

**2. `Seht,` in 8,18.** Der Bestand traegt die Form 48-mal als
*See · Ved · Voyez · Vedete* und **genau einmal** als
*Behold · Mirad · Voici · Ecco* — und dieser eine Beleg war Jes 8,18 aus
Paket 4. Kapitel 12 hat in 12,2 die Korpusmehrheit genommen (wie schon 7,14),
obwohl WEB *Behold*, LSG *Voici* und RIV *Ecco* schreiben und RV das Wort
auslaesst. 8,18 auf die Mehrheit gezogen.

**3. `ausrotten` in 10,7.** Kapitel 10 hatte italienisch *sterminare* nach RIV;
der Bestand fuehrt das Lemma in **allen 34 Eintraegen** auf dem Stamm
*eliminare* (dazu 6× *estirpò*), und Kapitel 11 hat in 11,13 *eliminati*
gesetzt. en/es/fr trafen die Bestandszeile ohnehin exakt; nur `it` wich ab. Auf
*eliminare* gezogen.

### Was der Kreuzabgleich sonst gefunden hat

`kreuz.py 23 10 11 12` meldet 48 gemeinsame Inhaltswortformen, 11 mit
abweichenden Lesarten. Nach Pruefung sind **acht davon legitime
Kontextvarianten** (Possessiva im Genus des Bezugsworts, `schlagen` in drei
Personen, `richten` = *judge* gegen *direct*, `Macht` = Substantiv gegen
Imperativ von `machen`) und drei die oben behandelten Faelle.

**Ein Verdacht hat sich als Ausgabentreue erwiesen:** `unter` traegt in 10,4
italienisch *fra*, in 10,16 *tra*. RIV schreibt an beiden Stellen genau das
(„curvarsi **fra** i prigionieri" / „la consunzione **tra** i suoi"), beides ist
korrektes Italienisch, und der Bestand fuehrt beide Zeilen (480× *tra*, 16×
*fra*). **Kein Befund** — anders als beim `orecchi`/`orecchie`-Fall.

### Zwei Kollisionen, die kein Skript gemeldet hat

Der Agent von Kapitel 11 hat sie selbst gefunden, beide im eigenen Vers:

- **11,7 `gemeinsam` / `zusammen`** fielen in **allen vier Sprachen** zusammen
  (*together · juntos · ensemble · insieme*). `zusammen` A2 (274 Belege) behaelt
  die Reihe, `gemeinsam` weicht auf seine **zweite Bestandslesart**
  *in common · en común · en commun · in comune* aus — die LSG dort selbst
  nahelegt („auront un même pâturage"). In 11,14 steht `gemeinsam` ohne Partner
  und behaelt die Hauptzeile.
- **11,12 `sammeln` / `zusammenbringen`** fielen es/fr/it zusammen.
  `zusammenbringen` (5 Belege) weicht auf *bring together · juntar · recueillir ·
  riunire*, `sammeln` nimmt seine Zweitzeile.

Dazu ein vierter `glosskollision.py`-Treffer, aufgeloest: in **11,11 und 11,16**
fielen das Relativpronomen `der` und `jenem` englisch auf *that* zusammen; das
Relativum nimmt jetzt in beiden Versen die Bestandszeile *which · que · qui · che*.

**Bewusst stehen geblieben** sind drei: `Neid`/`beneiden` in 11,13 (figura
etymologica — **WEB wiederholt „envy … envy" selbst**, und `Neid` ist mit 15
Belegen an *envy* gebunden), sowie zweimal die romanische Artikel/Klitikon-
Verschmelzung (11,15 fr *le*, 11,10 es/fr/it *la*).

### Neue Lemmata

**Kapitel 10:** `Erhabener` C1 *lofty ones · elevados · élevés · elevati* ·
`Fetter` B2 *fat ones · gordos · gras · grassi* · `unheilvoll` C1 ·
`Heimsuchung` C1 · `Straßendreck` C1 · `Thronender` C1 · `zwitschern` C1 ·
`fluten` B2 · `Nachtlager` C1 · `aufragen` C1 · `Brand` C1
*burning · incendio · embrasement · incendio* (**ausgewichen**: die
Mehrheitszeile *fire · fuego · feu · fuoco* fiel vierfach mit `Feuer` zusammen;
`lodern` nahm *blaze*, damit auch die Brand/lodern-Grenze haelt — LSG schreibt
selbst *embrasement*).
Mehrwort: `als ob` B1 · `aus der Ferne` B2 · `um Hilfe fliehen` B2 ·
`mit Leib und Seele` C1.

**Kapitel 11:** `Reis` C1 *shoot · vara · rameau · ramo* (unbelegt bestaetigt,
= alle vier Ausgaben) · `Gurt` C1 *sash · ceñidor · ceinturon · cinturone* ·
`Meereszunge` C1 · `sengend` C1 · `grasen` B2 (bewusst gegen `weiden`
abgesetzt) · `Patros` A1. Mehrwort neu: `ein Urteil geben` B2
*pass judgment · dictar sentencia · rendre un jugement · emettere una sentenza*.

**Kapitel 12:** `Bewohnerin` B2 *inhabitant · habitante · habitante ·
abitatrice* — Femininum Singular neben dem Plural-Maskulinum `Bewohner`;
RIV schreibt selbst *abitatrice*, WEB Singular *inhabitant*, nur LSG maskulin.
Praezedenz im Bestand: `Prophetin`, `Dienerin`, `Königin`.

**Der Tierfriede 11,6–8** (65,25 greift 11,7b und 11,9 auf): `Wolf` B1 ·
`Lamm` B1 · `Leopard` B2 · `Böckchen` B2 · `Kalb` A2 · `Mastvieh` C1
*fattened cattle · ganado cebado · bétail engraissé · bestiame ingrassato*
(die 1Sam-15,9-Zeile, **nicht** *veaux gras*, das franzoesisch mit `Kalb`
zusammengefallen waere) · `Kuh` A2 · `Bärin` A2 · `Stroh` B1 · `Rind` B1 ·
`Säugling` C1 · `entwöhnen` C1 · `Natter` C1 *cobra · áspid · aspic · aspide* ·
`Giftschlange` B2 *viper · víbora · vipère · vipera* · `Loch` B1 gegen
`Höhle` B1.

**Der Homograph des Kapitels:** `Junges` B2 *young · crías · petits · piccoli*
(11,7, Tierjunge) gegen `Junge` A1 *boy · muchacho · garçon · ragazzo* (11,6,
das Kind) — positionsgebunden geloest. **Kein Mehrwort `junger Löwe`** im
Bestand, geprueft.

### Zwei neue Lesarten fuer alte Lemmata

- **`verderben` B2** hat im ganzen Bestand ausschliesslich die **moralische**
  Lesart (*corrupt*, 5Mo 31,29 u. oe.). Jes 11,9 ist physisch („nichts Boeses tun
  und nichts verderben"), alle vier Ausgaben schreiben *destroy · dañar ·
  dommage · guasto*. Neue Lesart *destroy · destruir · détruire · distruggere*
  gesetzt — **wichtig, weil 65,25 den Vers woertlich aufgreift.**
- **`schlagen` A2** nimmt in **11,15 allein** *split · dividir · partager ·
  spartire* („den Strom in sieben Baeche schlagen"); 11,4 und 10,29 bleiben auf
  *strike*.
- **`Mächtiger` B2** traegt in Kapitel 10 **zwei** Lesarten, am Vers
  entschieden: 10,13 *mighty man · poderoso · puissant · potente* (Ps 52,3, der
  Kriegerheld) gegen 10,34 *Mighty One · Poderoso · Puissant · Potente*
  (Jes 1,24, der Gottestitel).
- **`Rat` B1** nimmt in 11,2 die counsel-Zeile (4 Belege), **nicht** die
  council-Zeile, die der formbasierte Extrakt fuer `Rates` als einzige zeigt:
  **Hiob 12,13 traegt dieselbe Trias** „Weisheit … Rat und Einsicht". Die
  Lexikonfalle in Reinform — es/fr/it sind in allen drei Zeilen identisch, nur
  en unterscheidet.

### Prompt-Hinweise: neun widerlegt

| ich schrieb | der Text sagt |
|---|---|
| `Recht` und `Gerechtigkeit` seien in 11,3–5 zu trennen | **`Recht` kommt in Kapitel 11 gar nicht vor** — nur `gerecht` (adverbial), `gerechtes` (attributiv), `Urteil`, `Gerechtigkeit` |
| `Geist` stehe sechsmal in 11,2 | **viermal**; die erste Stelle ist *Spirit* (des HERRN), die drei folgenden *spirit* |
| trennbare Verben in 11,11 · 11,13 · 11,16 | **alle drei sind kompakte Einwortformen** (`ausstrecken`, `aufhören`, `heraufzog`) — das Kapitel hat **keinen einzigen** getrennten Verbzusatz |
| `sammelt … auf` in 10,14 | `aufsammelt` und `eingesammelt`, je ein Token |
| `Macht` in 12,4 sei ein Substantiv | **Imperativ von `machen`** — die angekuendigte Kollision mit `Stärke`/`Kraft` entsteht gar nicht |
| `Rind`/`Kuh` in 11,7 sei eine Kollisionsstelle | *ox · buey · bœuf · bue* gegen *cow · vaca · vache · mucca* — in allen vier Sprachen getrennt |
| `Furcht des HERRN` sei vielleicht ein Mehrwort | **der Bestand fuehrt sie nicht als Mehrwort** — 14 Belege allein in Sprueche, alle Wort fuer Wort |
| `Säugling` und `zusammenbringen` seien unbelegt (`hints.py`) | **beide belegt**, ueber `Säuglinge` und ueber fuenf flektierte Formen. `belegt.py` hat es aufgedeckt |
| `Lascha` folge der Bestandsreihe von `Lasa` | **zwei verschiedene Orte** — s. `NAMENSSCHREIBUNG_JESAJA.md` |

Dazu **vier veraltete Belegzahlen** in meinem Auftrag: der Bestand ist seit dem
Buchbeginn gewachsen (`Heerschar` 34 → 50, `Grimm` 17 → 18, `Stab` 46 → 48,
Ueberrest-`Rest` 8 → 9). Und `hints.py` meldete in Kapitel 10 **32 unbelegte
Formen, von denen nur 10 wirklich neu waren** — `belegt.py` fand `Fetten`,
`Erhabenen`, `Sauls`, `Midians`, `Kranker`, `Säge`, `ducken`, `lodern` laengst
im Bestand.

### Der Kehrvers zum sechsten Mal

10,4 ab Position 16 ist Token fuer Token identisch mit 5,25 · 9,11 · 9,16 ·
9,20. Der Agent hat die zwoelf Eintraege plus `sich abwenden` Feld fuer Feld aus
`ch9.json` uebernommen **und maschinell gegengeprueft** (0 Abweichungen), statt
sie neu zu praegen.

### Kapitel 12: die Parallelen liegen ausserhalb des Buches

| Block | Partner | Versatz | Ergebnis |
|---|---|---|---|
| 12,2 pos 17–28 | **Ps 118,14** | +16 | **12 von 12 Tokens gleich** — Reihe komplett uebernommen |
| 12,2 pos 16–27 | **2Mo 15,2** | +16 | **11 von 12** — **nicht** uebernommen: 2Mo hat `Lobgesang` C1 *hymn*, Jesaja `Lied` A2 *song*; 2Mo endet ohne `geworden`, sein `ist` ist Praesens, Jesajas das Perfekt-Hilfsverb |
| 12,4 pos 5–18 | **1Chr 16,8 = Ps 105,1** | +5 | 14 Tokens durchgehend, inklusive beider Mehrwort-Eintraege `anrufen` und `bekannt machen` |
| 12,5 pos 11–14 | 1Chr 16,14 | +3 | 4 Tokens, uebernommen |
| 12,6 pos 7–10 | 41,14 | +11 | dort noch nicht annotiert — **12,6 ist die Vorlage** |

Das ist der Fall, vor dem die Koenigsbuecher warnen, in beiden Richtungen an
einem Vers: **Ps 118,14 ist der wortgleiche Partner, 2Mo 15,2 nur der
fast-gleiche.** Wer beide als Vorlage nimmt, glossiert `Lobgesang` an einer
Stelle, an der `Lied` steht.

### Bestandsbefunde

- **`Bewohner` B2 und `Einwohner` B2 tragen restlos dieselbe Reihe**
  *inhabitants · habitantes · habitants · abitanti* unter zwei Lemmata — die
  sechste Sachdublette nach `Ohrring`/`Ohrgehänge`, `Armreif`/`Armring`,
  `Hoheit`/`Majestät`, `Trommel`/`Tamburin`/`Pauke`,
  `Finsternis`/`Dunkel`/`Finster`, `Assyrien`/`Assur`.
- **`Lenden` C1 (6 Belege) und `Hüfte` B2 (28) fallen franzoesisch auf *reins*
  zusammen.** In 11,5 loesbar, weil `Hüfte` eine eigene Zweitzeile *hips ·
  caderas · hanches · fianchi* hat; wo `Lenden` allein steht, ist nichts zu tun.
- **`Assur` (10,5 · 10,24) und `Assyrien` (10,12) im selben Kapitel**, aber nie
  im selben Vers — **nicht aufgeloest**, nur gemeldet.
- **`überfluten`** hat im Bestand nur *floods · inunda · inonde · inonda*
  (Hiob 12,15 · Ps 124,4). In 10,22 heisst es „ueberfliessen", nicht
  „ueberschwemmen" — *overflows · desborda · déborde · trabocca* nach allen vier
  Ausgaben. Gemeldet, nicht korpusweit angefasst.
- **`Aja` ist ein Homograph, der hier nicht antwortet:** 1Mo 36,24 / 1Chr 1,40
  ist die **Person** Aja (*Aiah*), Neh 11,31 die Ortschaft. Jes 10,28 ist die
  Station Aiath, alle vier Ausgaben schreiben Aiath / Ajad / Ajjath / Aiath.
  Dritte Zeile am selben Lemma, wie beim `Sethar`-Praezedenzfall.
- **`mehr` ist im Bestand und im Buch unsettled** — 10,20 traegt
  *any longer · ya*, 11,13 *anymore · ya*, 2,4/2,22 *any longer · ya*,
  7,8/7,25 *anymore · más*, 1,13 *any more · más*. Korpusweit stehen 87 · 51 ·
  39 · 37 Belege nebeneinander. **Kein Paket-Befund**, sondern eine alte Lage;
  wenn sie einmal angefasst wird, dann buchuebergreifend.

### Ausgabenbefunde

- **RIV, drei neue Setzfehler** (in `RIV_SETZFEHLER_JESAJA.md` nachgetragen):
  **10,26 „la frustra"** (*frusta*), **10,27 „il giogo sarò scosso"** (*sarà*)
  und **11,16 „il iorno che uscì"** (*giorno*) — der dritte verschluckte Anlaut
  an einem **Gemeinwort** nach 7,25 und 9,5, also genau die Klasse, die die
  Eigennamen-Auszaehlung nicht sehen kann.
- **WEB 11,5 verliert beide Synonympaare**: „the belt of his waist, and
  faithfulness **the belt of his waist**" — `Gürtel`/`Gurt` und `Hüften`/`Lenden`
  auf **eine** Wendung eingeebnet. Fuer diese vier Glossen gab es faktisch nur
  drei Ausgaben.
- **RV 11,11 deutet drei Ortsnamen um**: `Patros` → *Partia*, `Elam` →
  *Persia*, `Schinar` → *Caldea*. **RV 10,34 laesst `den Mächtigen` ganz aus**
  („caerá con estrépito"). **RV 10,6/10,7 setzen Assur feminin**, das Deutsche
  maskulin.
- **`Zeichen` (11,10 · 11,12): alle vier Ausgaben schreiben „Banner"**
  (*banner · bandera · bannière · vessillo*). Der Bestand fuehrt fuer `Zeichen`
  **keine** Banner-Lesart (86× *sign*, 68× *signs*). Bestand genommen — dieselbe
  Lage wie `Nachtwache` in 1,8.
- **11,6: keine der vier Ausgaben uebersetzt `weiden`** — alle schreiben
  „(werden) zusammen sein". Bestand `weiden` C1 gehalten.
- **Person wechselt in 10,12**: Deutsch und RV 3. Person, WEB/LSG/RIV 1. Person.
  Glossiert ist der deutsche Text.
- **WEB 10,18** liest „as when a standard bearer faints" statt „wie ein Kranker
  dahinschwindet"; **WEB 10,19** „write their number" fuer `zählen`.
- **LSG und RIV lesen 11,3 `Wohlgefallen` als „riechen"** („Il respirera la
  crainte"), WEB/RV *delight/deleite*. Bestand genommen.
- **LSG 12,2 uebersetzt `Rettung` zweimal verschieden** („ma délivrance",
  dann verbal „m'a sauvé") und macht aus `Lied` „le sujet de mes louanges".
  **RIV 12,6 verschmilzt `Juble und jauchze`** zu „de' gridi, de' gridi di
  gioia"; **RV 12,6 setzt fuer `jauchze` „canta"**, was mit `Singt`/*Cantad* in
  12,5 zusammenfiele. Die Bestandsreihen halten beide auseinander.
- **12,2 · die Verdopplung `der HERR, der HERR`**: WEB „Yah, Yahweh" (zwei
  verschiedene Woerter), LSG und RIV doppeln, **RV loest auf** und stellt den
  Satz um. Das Eintragspaar traegt beide Male dieselbe Reihe; die RV-Aufloesung
  ist ein Ausgabenbefund.

## 12. Paket 6 (Kap. 13 · 14 · 15)

Drei Kapitel gleichzeitig, 1326 Einzelwort- und 68 Mehrwort-Eintraege. Alle
sechs Pruefungen je Kapitel sauber; `validate.py 23`, `qa.py 23` und
`hilfsverb.py 23` melden ueber das gebaute Buch **0 Befunde**.

### 13,4 — die einzige Kollisionsstelle des Buches ist entschaerft

„Der HERR der **Heerscharen** mustert ein **Heer** zum Kampf." Die in §2
vorgerechnete Probe traegt: `Heerschar` C1 *hosts · ejércitos · armées ·
eserciti* gegen `Heer` B2 *army · ejército · armée · esercito* — englisch
lexikalisch getrennt, romanisch ueber den Numerus. **Keine Sonderloesung.**
Die Falle daneben ist umgangen: `Heer` hat im Bestand auch eine Plurallesart
*armies · ejércitos · armées · eserciti*, die in allen vier Sprachen mit
`Heerschar` zusammengefallen waere; im Text steht „ein Heer", Singular.
`Heerschar` steht inzwischen bei **55 Belegen**.

### Was ein Wort in drei gleichzeitigen Kapiteln kostet — und diesmal nichts kostete

`Ausspruch` steht in **13,1 · 14,28 · 15,1**, also je einmal in jedem der drei
parallel laufenden Kapitel, und hat im ganzen Bestand **einen** Beleg
(Spr 30,1). Genau an solchen Woertern sind in 3. Mose und den Koenigsbuechern
die Wellen auseinandergelaufen. Die Reihe C1 *oracle · oráculo · oracle ·
oracolo* stand deshalb wortgleich in allen drei Auftraegen — **alle drei Agenten
haben sie unabhaengig am Vers bestaetigt** (LSG *oracle*, RIV *oracolo*
woertlich; WEB liest *burden*, RV *profecía*, beide nicht gefolgt).

**Die Gegenprobe zur Methode:** wo ein Wort nur in einem Kapitel steht, ist
nichts abzustimmen; wo es in mehreren steht, muss die Reihe **vor** dem Start im
Auftrag stehen. `vorab.py` findet diese Woerter, und `kreuz.py` prueft
hinterher, ob es gereicht hat.

### Vom Koordinator angeglichen — dreimal, alle klein

`kreuz.py 23 13 14 15` meldet 57 gemeinsame Inhaltswortformen, 19 mit
abweichenden Lesarten. **Sechzehn sind legitime Flexions- und
Kontextvarianten** (Person, Numerus, Tempus, Kontraktionen vor verschiedenen
Substantiven). Drei nicht:

| Stelle | war | ist | Grund |
|---|---|---|---|
| 13,2 `damit` fr | *pour que* | *afin que* | LSG schreibt an der Stelle einen blossen Konjunktiv („qu'ils franchissent"), gibt also **keine** Form vor; der Bestand hat 1309 Belege *afin que* und **null** *pour que* |
| 13,17 `nichts` it | *niente* | *nulla* | RIV umschreibt („non faranno alcun caso"), gibt also keine Form vor; der Bestand hat 479 Belege *nulla* und **null** *niente* |
| 14,19 `durchs` es | *por la* | *a* | **RV schreibt an beiden Stellen „a espada"** (13,15 und 14,19) — Kapitel 13 hatte es richtig, Kapitel 14 nicht |

Die Regel dahinter, zweimal in derselben Welle: **wo die Ausgabe die Form gar
nicht setzt, entscheidet der Bestand.** Die Ausgabe kann nur widersprechen, wo
sie ueberhaupt etwas sagt.

**Kein Befund war dagegen `jeder` in 13,14** (it *ognuno* statt der
Bestandszeile *ciascuno*): **RIV schreibt dort selbst zweimal „ognuno"**. Und
`durchs` italienisch bleibt in 13,15 *di* gegen 14,19 *con la*, weil RIV genau
so wechselt („cadrà di spada" / „trafitti colla spada").

### Drei Ortsnamen, deren Bestandsreihe ihrer Ausgabe widersprach

**Der wichtigste Befund der Welle**, gefunden vom Agenten fuer Kapitel 15 und
korpusweit nachgezaehlt: `Zoar` trug italienisch *Zoar*, waehrend RIV an
**allen acht** Belegstellen *Tsoar* schreibt; `Medeba` trug *Madaba* gegen
**vier von vier** *Medeba*; `Eleale` trug spanisch *Elealé* und italienisch
*Eleale* gegen **zwei von zwei** *Eleale* (RV) und *Elealeh* (RIV).

Mit `remap.py` in 1. Mose, 4. Mose, 5. Mose, Josua, 1. Chronik und Jesaja
korrigiert; alle sechs Buecher laufen danach durch `validate.py`. Einzelheiten
in `NAMENSSCHREIBUNG_JESAJA.md`.

**Die Abgrenzung, die dabei entstanden ist:** eine abweichende Sprache ist nur
dann ein Befund, wenn sich die Abweichung **an jeder Belegstelle** an der
Ausgabe widerlegen laesst. Weicht die Ausgabe selbst ab oder wechselt sie
(RIVs `fra`/`tra`, WEBs *Shushan*), ist nichts zu tun.

### `Elale` — die Gegenprobe zu `Lascha` faellt anders aus

Nach dem Irrtum des letzten Pakets war ausdruecklich verlangt, die
Namenstabelle **an allen vier Ausgaben zu pruefen statt sie zu glauben**. Hier
haelt sie: alle vier schreiben in 4Mo 32,3/32,37 und in Jes 15,4 identisch, und
**4Mo 32,3 nennt `Dibon`, `Hesbon`, `Eleale` und `Nebo` in einer Zeile** — vier
der sechzehn Ortsnamen von Jesaja 15. Derselbe Ort.

### Kollisionen, die kein Skript gemeldet hat — vier in einer Welle

- **13,10 `leuchten` / `scheinen` fielen in allen vier Sprachen zusammen**
  (*shine · brillar · briller · risplendere*). `leuchten` nimmt seine **zweite
  Bestandszeile** *give light · alumbrar · éclairer · illuminare* (4Mo 8,2, dort
  Lampen — derselbe Sachverhalt). **`glosskollision.py` hat das nicht gesehen.**
- **15,4 `zittern` / `bebt`** fielen bis auf den Numerus in allen vier zusammen.
  `zittern` ist 8/8 einheitlich, `beben` dreifach gespalten — `beben` weicht auf
  die Ps-99,1-Zeile *shakes · se estremece · chancelle · è scossa*.
- **15,6 `welken` / `verdorrt`** fielen englisch zusammen; `welken` nimmt die
  Hiob-18,16-Zeile *wilt*, womit es/fr sich zusaetzlich Wort fuer Wort mit RV
  und LSG decken.
- **14,31 `vor Angst`** ist ein Bestands-Mehrwort (4 Belege), das **weder
  `konvention.py` noch `sweep.py` gemeldet** haben — die Klasse, die fuer
  `selfcheck.py` und `qa.py` prinzipiell unsichtbar ist.

Dazu, vom Skript gemeldet und am Vers geloest: 13,4 `Getöse`/`Tosen` (it),
13,13 `erschüttern`/`beben` (en), 13,14 `zu`/`in`, 13,5+13,6 `des`/`vom` (es),
14,25 `auf`/`in` (es).

### Wo der Bestand gegen alle vier Ausgaben gehalten wurde

Das Muster von `Nachtwache` (1,8) und `Zeichen` (11,10) hat sich in dieser Welle
**fuenfmal** wiederholt. Jedes Mal gilt: die Ausgabe liefert den Namen, der
Bestand die Bedeutung.

| Stelle | alle vier Ausgaben | genommen | Belege |
|---|---|---|---|
| 13,21 `Dämonen` | *wild goats · sátiros · boucs · satiri* | `Dämon` B2 *demons · demonios · démons · demoni* | 48 |
| 13,14 `Reh` | „Gazelle" | `Reh` B2 *roe deer · corzo · chevreuil · capriolo* | 4 |
| 13,16 `geschändet` | „vergewaltigt" | `schänden` C1 *dishonored · deshonradas · déshonorées · disonorate* | 2Sam 13,22, derselbe Tatbestand |
| 15,2 `Höhen` | „high places" | `Höhe` B1 *heights · alturas · hauteurs · alture* | 13/13 — und **1Kön 22,44 fuehrt `Höhe` und `Opferhöhe` im selben Vers** und trennt genauso |
| 15,2 `Tempel` | WEB/RV transliterieren („Bayith") | `Tempel` *temple · templo · temple · tempio* | 212 |

### Die beiden schaerfsten Einzelstellen

**14,29 `Schlange` · `Natter` · `Drache` in einem Vers.** Drei der vier Ausgaben
schreiben fuer `Drache` ein Schlangenwort (WEB *fiery flying serpent*, RV
*serpiente voladora*, RIV *serpente ardente e volante*); nur LSG *dragon
volant*. **Wer den Ausgaben folgt, laesst `Drache` in allen vier Sprachen mit
`Schlange` zusammenfallen.** Der Bestand trennt alle drei: `Schlange` A2
*serpent · serpiente · serpent · serpente* · `Natter` C1 *cobra · áspid · aspic ·
aspide* (aus 11,8 uebernommen) · `Drache` B1 *dragon · dragón · dragon · drago*.
Dass die neun `Drache`-Belege saemtlich aus Offenbarung 12 stammen, ist **kein**
Hinderungsgrund — die Bedeutung (Fabeltier) ist dieselbe. **RV setzt fuer
`Natter` *víbora*, und das ist im Buch die Reihe von `Giftschlange` (11,8)** —
gefolgt waere 11,8 gegen 14,29 gespalten.

**14,11 `Maden` / `Würmer`.** RV, LSG und RIV setzen fuer beide **dasselbe
Wort**; nur WEB trennt. Der Bestand trennt in allen vier, und zwar aus
**Hiob 25,6, wo beide Woerter im selben Vers stehen**: `Made` B2 *maggot · larva
· vermisseau · vermicciuolo* gegen `Wurm` B1 *worm · gusano · ver · verme*.

### `Last`: die Spaltung im Buch ist bedeutungsgetragen — 10,27 bleibt

Der Auftrag hatte gefragt, ob 10,27 auf die Bestandsmehrheit nachzuziehen sei.
**Nein.** Die vier Ausgaben schreiben in **10,27 und 14,25 wortgleich dasselbe**
(*his burden · su carga · son fardeau · il suo carico*), waehrend 1,14 etwas
anderes meint — dort sind die Feste Gott „eine Last", und LSG schreibt *à
charge*. Beide Zeilen sind Bestandszeilen. 10,27 und 14,25 sind damit Feld fuer
Feld deckungsgleich in `Joch` C1 *yoke · yugo · joug · giogo*, `Last` B1
*burden · carga · fardeau · carico* und `Schulter` A2 *shoulder · hombro ·
épaule · spalla* — die Beinah-Dublette, die `DUBLETTEN_JESAJA.md` unterschreitet.

### Neue Lemmata

**Kapitel 13 — das Bestiarium 13,21–22** (kehrt in 34,11–15 wieder):
`Wüstentier` C1 · `Eule` B2 *owls · búhos · chats-huants · gufi* · `Strauß` B2 ·
`Dämon` B2 · `Hund` A1 · `Schakal` C1 · `Schloss` B1 *castles · castillos ·
châteaux · castelli* (**neue Lesart**, Bestand = *locks*) · `heulen` B2 *howl*
(**neue Lesart**, Bestand *wail* fuer Menschen) · `hausen` C1.
Dazu `Geweihter` C1 · `Menschenherz` B2 · `schlaff` B2 · `Feingold` C1 ·
`Zierde` C1 · `anstarren` B2. Mehrwort neu: `sich nichts machen aus` B2 ·
`sich hinziehen` B2 · `lagern lassen` B2.

**Kapitel 14 — das Unterwelt-Feld:** `Totengeist` C1 · `Made` B2 · `Wurm` B1 ·
`Grube` B2 · `Grab` B1 · `Aas` C1 · `Sprössling` C1 *shoot · retoño · rejeton ·
rampollo* (**bewusst abgesetzt** von `Spross` und `Reis` aus 4,2/11,1) ·
`Morgenröte` C1. Dazu `Philisterland` B2 · `Terror` C1 · `Todesjahr` C1 ·
`Wolkenhöhe` C1 · `Wassersumpf` C1 · `Besen` B2 · `Bösewicht` C1 · `schmettern`
C1 · `drunten` B2 · `einstig` B2. Mehrwort neu: `erzittern lassen` C1 ·
`sich niedersetzen` C1.

**Kapitel 15 — dreizehn der sechzehn Ortsnamen sind neu:** `Ar-Moab` ·
`Kir-Moab` · `Elale` · `Eglat-Schelischija` · `Luhit` · `Horonajim` · `Nimrim` ·
`Eglajim` · `Dimon` (alle A1). Dazu `Klagegeschrei` C1 *cry of anguish · grito
de angustia · cri de détresse · grido d'angoscia* · `Wehklagen` C1 *wailing ·
alarido · lamentation · urlo* · `Weidenbach` C1 · `Bewaffneter` C1 ·
`Entronnener` C1. Mehrwort neu: `in Tränen aufgelöst` C1.

**`Weidenbach` (15,7) wird uebersetzt, nicht transliteriert** — die Regel aus
`AUFTRAG_BUCH.md` („steht im deutschen Text ein deutsches Wort, wird es
uebersetzt"). Alle vier Ausgaben uebersetzen, und **der Bestand deckt beide
Haelften**: `Bach` *brook · arroyo · torrent · torrente* (61 Belege) und eine
eigene Weiden-Lesart von `Weide` *willows · sauces · saules · salici*
(Hiob 40,22 · Ps 137,2). **`Eglat-Schelischija` bleibt Name** — Lautfolge ohne
deutsche Bedeutung.

### `Rest` in 15,9: Ueberrest, und der Grund ist nicht die Theologie

Genommen ist die Ueberrest-Zeile B1 *remnant · remanente · reste · resto*
(inzwischen 15 Belege gegen 20 der Mehrheitslesart). Entschieden haben zwei
Dinge, **nicht** dass es eine Restformel waere:

1. **WEB ist die einzige der vier Sprachen, die beide Lesarten lexikalisch
   trennt** — und sie schreibt „on the remnant of the land". es/fr/it (*el resto
   · le reste · quel che resta*) sind mit beiden vertraeglich und tragen nichts
   bei.
2. **Der Parallelismus im Vers**: „einen Loewen ueber die **Entronnenen** Moabs
   und ueber den **Rest** des Landes" — beide Glieder sind Ueberlebende.

Dass es Moabs Rest ist und nicht Israels, aendert die Lesart nicht: die Bindung
gilt fuer dieselbe Bedeutung.

### Prompt-Hinweise: dreizehn widerlegt

| ich schrieb | der Text sagt |
|---|---|
| `Feldzeichen` sei gegen `Zeichen` abzugrenzen | **`Zeichen` kommt in 13,2 gar nicht vor**, und `Feldzeichen` ist mit 13 Belegen belegt (4Mo 1,52) |
| `Grab` stehe in 14,19 und 14,20 | 14,20 hat kein `Grab`, sondern das Verb `begraben` — es ist **14,18 und 14,19** |
| die Ausgaben lesen `Igel` (14,23) teils „Rohrdommel" | **keine der vier** — WEB *porcupine*, RV *erizos*, LSG *hérisson*, RIV *porcospino* |
| WEB schreibe fuer `Morgenstern` *day star* | **WEB schreibt selbst „morning star"** — nur RV, LSG, RIV weichen ab |
| `Klage` stehe in 15,3 | **kommt im Kapitel nicht vor**; 15,3 hat `jammert`, `Tränen`, `aufgelöst` |
| `Klage laut, Tor!` (14,31) sei das Substantiv | **Imperativ von `klagen`** — alle vier Ausgaben haben dort einen Imperativ; der Lexikon-Extrakt zeigt nur das Substantiv |
| `Bedrängte` (14,32) sei dasselbe Lemma wie `Bedränger` | zwei getrennte Lemmata, beide C1 |
| `Fremde` (14,1) | `Fremder` B1 — Personen im Plural, nicht das fremde Land |
| `13,11 ein Ende machen` sei ein trennbares Verb | Bestands-Mehrwort, zusammenhaengend |
| `13,20 aufschlagen` sei getrennt | kompaktes Einwort-Token |
| `Rind`/`Kuh`-Klasse: `Gras`/`Pflanzen`/`Grünes` (15,6) kollidierten | in allen vier Sprachen getrennt |
| vier Belegzahlen | veraltet: `Heerschar` → **55**, `Stab` → **50**, `Totenreich` → **29**, `Last` → **41**, `Rest` → **20:15** |
| Partikel-Hinweise | in Kap. 13 wieder **die Haelfte falsch**, und **zwei echte fehlten** (13,17 `hetze … auf`, 13,8 `starrt … an`); in Kap. 14 und 15 dagegen **alle richtig** und fuenf bzw. null zusaetzliche gefunden |

### Ausgabenbefunde

- **RIV: vier neue Setzfehler in Kapitel 13**, nachgetragen — 13,10 „non **far**
  più brillare" (*faran*), **13,11 „de' uperbi"** (*superbi*), 13,15 „**sarò**
  trafitto" (*sarà*, wie 10,27), **13,20 „la sua enda"** (*tenda*). Die beiden
  fettgedruckten sind der fuenfte und sechste verschluckte Anlaut an einem
  **Gemeinwort** nach 7,25 · 9,5 · 11,16. **Kapitel 14 und 15 haben null** —
  in Kapitel 14 wurden alle 686 Wortformen maschinell durchgesehen.
- **RIV verschiebt die Versgrenze 14,3/14,4**: der erste Halbvers von de 14,4
  steht bei RIV am Ende von 14,3. Verszahl bleibt 32 — wer RIV 14,4 als Vorlage
  nimmt, hat fuer die halbe Zeile keinen Text.
- **RV 13,21 ist um einen Slot verschoben** (*criaturas siniestras* an der
  `Eulen`-Stelle, *búhos* an der `Strauße`-Stelle). **RV 15,3 vertauscht
  `Straßen` und `Plätze`.** Beide nach der deutschen Bedeutung glossiert, wie
  schon die Schmuckliste 3,18–23.
- **LSG und RIV vertauschen 13,22 die beiden Tiere** (`Wilde Hunde` /
  `Schakale`); WEB und RV halten die deutsche Reihenfolge.
- **RIV 15,8 laesst `Eglajim` ganz aus**; **RV 15,5 uebersetzt
  `Eglat-Schelischija`** („como novilla de tres años") statt zu transliterieren.
- **RV 13,17 laesst „Denn siehe" weg**; **WEB setzt in 13,9 ein „Behold", das
  der deutsche Text nicht hat**; **WEB 14,18** liest „in his own house" statt
  `Grab`; **WEB 14,30** „The firstborn of the poor" gegen „Die Ärmsten der
  Armen"; **LSG 14,21** „remplir le monde d'ennemis" statt „mit Städten füllen".
- **14,4 `Terror`: alle vier Ausgaben lesen etwas anderes, und alle vier
  verschieden** — WEB „The golden city has ceased", RV „su furia insaciable",
  LSG „L'oppression a cessé", RIV „l'esattrice d'oro". Nach dem deutschen Wort
  glossiert.
- **RV1909mod setzt in 13,2 `ustedes`-Imperative.** Die Buchkonvention ist
  `vosotros`, und der Bestand traegt ueber **3700** `vosotros`-Imperative
  (Endungen *-ad* und *-ed*). Kein Befund, nur zur Erinnerung.

### Bestandsbefunde

- **`nahe` A2 (13,6) und `nah` A2 (13,22) tragen restlos dieselbe Reihe**
  *near · cerca · proche · vicino* unter **zwei Lemmata** — die siebte
  Sachdublette. Ebenso **`Unruhe` und `Aufruhr`** (es/fr/it *tumulto ·
  tumulte · tumulto*, 14,3 gegen 14,9) und **`hausen` / `wohnen`** (fr/it,
  13,20 gegen 13,21). Alle drei stehen in **verschiedenen** Versen — nicht
  aufgeloest.
- **`niederstrecken` (13,18) und `umstürzen` (13,19)** laufen es/it auf denselben
  Stamm (*derribar* / *abbattere*) — benachbarte Verse, nicht derselbe.
- **Duenn belegte Lemmata, bei denen die Bedeutung die Zahl schlug:** `still` B1
  (Bestand nur die Personen-Lesart *zitto*, „Sei still!" — in 14,7 ist die
  **Erde** still) · `niederwerfen` C1 (Bestand nur die Proskynese-Lesart, 14,12
  ist transitiv) · `fliegend` B1 (ein Beleg, Offb 4,7, als Relativsatz; 14,29 ist
  attributiv) · `sich niederlassen` B2 (die 1Mo-24,11-Zeile statt der Vogel-Zeile
  aus 7,19 — 13,21 sind Wuestentiere, die sich hinlegen) · `heimkehren` B1 ·
  `klagen` B2 · `sich krümmen` B2 · `lagern` B2.
- **`gedenken` als Verb war unbelegt** — der Bestand kennt nur das
  grossgeschriebene Substantiv `Gedenken` B2, und `belegt.py` warnt korrekt vor
  der Verwechslung.
- **`Assur` A1 fuehrt zwei Zeilen** (9× *Assyria · Asiria · Assyrie · Assiria*,
  2× *Asshur · Asur · Assur · Assur*). 14,25 ist das Land, also die erste —
  deckungsgleich mit 10,5 und 10,24.
- **`Elim` ist ein Homograph**: der Bestand kennt nur das Elim der
  Wuestenwanderung (2Mo 15,27), 15,8 ist Beer-Elim in Moab. Die Reihe ist in
  beiden Faellen dieselbe, also kein Konflikt — der Fall gehoert aber neben
  `Sethar` und `Aja` in die Homographenliste.

## 13. Paket 7 (Kap. 16 · 17 · 18)

Drei Kapitel gleichzeitig, 891 Einzelwort- und 42 Mehrwort-Eintraege. Alle sechs
Pruefungen je Kapitel sauber; `validate.py 23`, `qa.py 23` und `hilfsverb.py 23`
melden ueber das gebaute Buch **0 Befunde**. Damit sind **18 von 66 Kapiteln**
fertig: 350 Verse, 8110 Eintraege.

### Der groesste Fund der Welle: 52 falsche italienische Artikel vor `HERR`

Gemeldet vom Agenten fuer Kapitel 18, ueber den ganzen Bestand nachgezaehlt und
korrigiert. **Der Bestand steht 1420 : 25 fuer `il` — und alle 25 Ausreisser
waren Jesaja.** Mit den uebrigen Artikelformen zusammen 52 Eintraege, verteilt
ueber die Kapitel 1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14 und 17.

| Form | war | ist | Vorkommen |
|---|---|---|---|
| `der` | *l'* | *il* | 27 |
| `Der` | *L'* | *Il* | 12 |
| `den` | *l'* | *il* | 6 |
| `des` | *dell'* | *del* | 5 |
| `Den` | *L'* | *Il* | 1 |
| `vom` | *da parte dell'* | *da parte del* | 1 |

**Die Diagnose ist sprachspezifisch, und nur eine Sprache ist betroffen.** Die
franzoesische Elision ist **richtig**: `HERR` heisst franzoesisch `ÉTERNEL`,
vokalisch anlautend, also ist „l' ÉTERNEL" korrekt. Spanisch „el SEÑOR"
ebenfalls. **Nur italienisch ist es falsch**, weil die Glosse `SIGNORE`
konsonantisch anlautet — im Lesefluss stand dort „l' SIGNORE".

**Die Ursache ist die Nachbarfalle**, dieselbe wie bei `Völker` in 5. Mose und in
Paket 5: RIV schreibt *l'Eterno*, die Elision ist beim Uebertragen mitgewandert,
und **das Nachbarwort wurde nicht angepasst**. Der Fehler steht seit Kapitel 1
im Buch, also seit dem Massstabskapitel, und **Kapitel 17 hat ihn in dieser
Welle prompt mitgeerbt** — beim Planen waren es 50 Stellen, beim Ausfuehren 52.
Deshalb gehoert eine solche Korrektur **hinter** das Einsammeln, nicht davor.

**Woran man die Klasse erkennt:** die Glosse eines Funktionsworts richtet sich
nach dem **Anlaut der Nachbarglosse**, nicht nach dem Anlaut des Ausgabenworts.
Wo die Ausgabe elidiert und die Bestandsglosse einen anderen Anlaut hat, ist die
Elision zu loesen.

### Vom Koordinator angeglichen — zweimal

**1. `über` in 13,1** von *concerning · acerca de · sur · riguardo a* auf
***about · sobre · sur · su***. Die Formel „Der Ausspruch **über** X" steht
dreimal im Buch (13,1 · 15,1 · 17,1); **Kapitel 15 und 17 haben unabhaengig
dieselbe Zeile gewaehlt**, 13,1 war der Ausreisser — und zwar, weil **mein
Auftrag es angewiesen hatte**, `über` woertlich aus 2,1 zu uebernehmen. 2,1 ist
aber eine andere Konstruktion („Dies **sah** Jesaja … über Juda"), und die dort
verwendete Reihe steht im Bestand nicht einmal unter den sechs haeufigsten,
waehrend *about · sobre · sur · su* 98 Belege hat. **2,1 bleibt unangetastet.**

**2. `Rebe` in 18,5** von *vines · vides · ceps · viti* auf ***branches ·
sarmientos · sarments · tralci***. Siehe unten — die Vorgabe war mein Fehler.

### `Rebe`: die Vorgabe war falsch, und der Text traegt wirklich zwei Lesarten

Ich hatte beiden Kapiteln die Zeile aus **5,2** mitgegeben. Sie **faellt in 16,8
in allen vier Sprachen mit `Weinstock` zusammen** — die beiden stehen dort im
selben Vers („die **Weinstöcke** von Sibma … ihre edlen **Reben**"), und
`Weinstock` ist mit 26 Belegen gebunden und steht in 7,23 bereits auf genau
dieser Reihe. **Ich hatte eine Reihe aus einem Vers verordnet, ohne den Nachbarn
im Zielvers zu pruefen** — derselbe Fehler wie bei der `Völker`-Genusfalle, nur
eine Ebene frueher.

Der Agent ist auf die **eigene Korpusmehrheit** ausgewichen: 5 von 6
`Rebe`-Belegen tragen den *sarmiento*-Stamm, und WEB („its choice branches") wie
RV („sus mejores sarmientos") schreiben in 16,8 selbst genau das.

**Nach dem Einsammeln steht `Rebe` im Buch auf zwei Zeilen, und das ist richtig
so** — der Text unterscheidet:

| Stelle | Wortlaut | Zeile |
|---|---|---|
| 5,2 · 17,10 | „pflanzte edle Reben" · „setzt fremde Reben hinein" | *vines · vides · ceps · viti* — die **gepflanzte Pflanze** |
| 16,8 · 18,5 | „ihre edlen Reben zerschlagen" · „die Reben wegnehmen" | *branches · sarmientos · sarments · tralci* — der **abgeschnittene Trieb** |

Die Ausgaben helfen hier nicht: in 16,8 stehen WEB und RV auf der Trieb-Lesart,
**LSG und RIV auf der Pflanzen-Lesart** (*ceps* / *viti scelte*), und **LSG
verschmilzt `Weinstöcke` und `Reben` sogar zu einer Wendung**. In 18,5 dreht LSG
die beiden Woerter gegenueber dem Deutschen um. **Entschieden hat die
Bedeutung** — und in 16,8 zusaetzlich die Kollision im eigenen Vers.
`Ranke` bleibt in beiden Kapiteln *shoots · brotes · rameaux · rami* und ist
gegen die neue `Rebe`-Zeile in allen vier Sprachen frei.

### `Kir-`: die dritte Art, wie eine Namensfrage ausgehen kann

Nach `Lascha` (zwei verschiedene Orte) und `Elale` (ein Ort, eine Reihe) jetzt
der dritte Fall: **derselbe Ort, aber die Ausgaben schreiben ihn an der zweiten
Stelle anders.**

| | 15,1 `Kir-Moab` | 16,7 `Kir-Hareset` | 16,11 `Kir-Heres` | 2Kön 3,25 |
|---|---|---|---|---|
| WEB | Kir of Moab | Kir Hareseth | **Kir Heres** | Kir Hareseth |
| RV | Kir-Moab | Kir-hareset | **Kir-hareset** | Kir-hareset |
| LSG | Kir-Moab | Kir-Haréseth | **Kir-Harès** | Kir-Haréseth |
| RIV | Kir-Moab | *ir*-Hareseth | **Kir-Heres** | Kir-Hareseth |

**Der Identitaetsbeweis ist RV**: sie schreibt in 16,7 und 16,11 dasselbe Wort.
LSGs *Kir-Harès* ist die Kurzform von *Kir-Haréseth*. Genau die Gegenlage zu
`Lascha`, wo alle vier zwei verschiedene Namen setzten.

**Verfahren:** jede Stelle behaelt ihre Schreibung als Lemma **und folgt in jeder
Sprache ihrer eigenen Ausgabe**, mit der spanischen Spalte als Identitaetsanker.
`Kir-Heres` A1 ist damit neu (*Kir Heres · Kir-Hareset · Kir-Harès · Kir-Heres*),
`Kir-Hareset` behaelt die Bestandsreihe, `Kir-Moab` bleibt eigenes Lemma.

### `Sela` in 16,1 — die schaerfste Lexikonfalle des Buches

`belegt.py Sela` meldet **81 Belege**, und die Mehrheit ist keine Ortsangabe:

| Lesart | Belege | was es ist |
|---|---|---|
| *Selah · Selah · Pause · Sela* | **72** | die **Psalmen-Pause** |
| *Shelah · Sela · Schéla · Sela* | 8 | **Schela**, eine Person (1Chr 2,3) |
| *Sela · Sela · Séla · Sela* | **1** | **die Stadt** (2Kön 14,7) |

Die Ein-Beleg-Zeile ist die richtige. **Und WEB schreibt in Jes 16,1 selbst
„Selah"** — also genau die Zeichenfolge, mit der der Bestand 72-mal eine
Musikpause glossiert. Das ist die Lesefluss-Ausnahme aus `AUFTRAG_AT.md` (der
Fall „Carcass"): die Ausgabenform faellt mit einem anderen Begriff zusammen und
setzt einen falschen Sinn, also gilt die Bestandsform. Gemeldet.

### 16,6 — fuenf Hochmutswoerter in einem Vers, und die Loesung stand schon im Buch

| Wort | Lvl | en · es · fr · it | Herkunft |
|---|---|---|---|
| `Hochmut` | C1 | arrogance · soberbia · orgueil · superbia | = 2,17 · 9,8 · 10,12 · 13,11 |
| `Überheblichkeit` | C1 | **haughtiness** · arrogancia · arrogance · arroganza | **= 9,8**, die Zweitlesart |
| `Übermut` | C1 | insolence · insolencia · insolence · insolenza | = 13,11 |
| `Wut` | B2 | rage · furor · fureur · furore | = 8,21 |
| `stolz` | B1 | proud · orgulloso · fier · orgoglioso | = 4,2 · 13,19 |

**Zwei meiner Annahmen widerlegt:** die englische Kollision zwischen `Hochmut`
und `Überheblichkeit` (*arrogance*/*arrogance*) war **in 9,8 laengst geloest** —
dort steht *haughtiness*, ein Bestandsbeleg **aus diesem Buch**. Und
`Übermut`/`Überheblichkeit` kollidieren franzoesisch **nicht**. Es war nichts zu
erfinden; der Agent musste nur nachschlagen.

**16,5 geht ebenso dreifach auf:** `Recht` B1 *justice · derecho · droit ·
diritto* / `Gerechtigkeit` B2 *righteousness · justicia · justice · giustizia* /
`Rechtschaffenheit` C1 *integrity · integridad · intégrité · integrità*.

### `Rest`: das Kriterium aus Kapitel 15 traegt dreimal

16,14 und 17,3 haben unabhaengig voneinander die **Ueberrest-Lesart** B1
*remnant · remanente · reste · resto* gewaehlt, und beide mit derselben
Begruendung wie 15,9: **WEB ist die einzige der vier Sprachen, die beide
Lesarten lexikalisch trennt**, und sie schreibt an beiden Stellen *remnant*
(„the remnant will be very small and feeble" · „the remnant of Syria"). es/fr/it
(*el remanente · lo que quede · ce qui restera · del residuo*) sind mit beiden
vertraeglich und tragen nichts bei. Das Kriterium ist damit dreimal unabhaengig
bestaetigt und gehoert zur Buchpraxis.

### Kollisionen, die kein Skript gemeldet hat — sieben in einer Welle

- **17,7 + 17,8 `blicken` / `schauen`** fielen in **allen vier** Sprachen
  zusammen (`hints.py` meldete nur englisch). `schauen` weicht auf *gaze ·
  contemplar · contempler · contemplare* — RV schreibt in 17,7 selbst
  *contemplarán*, LSG in 17,8 *contemplera*. Gilt auch fuer die beiden
  Mehrwoerter `blicken auf` / `schauen auf`, die in 17,8 zusammenstehen.
- **16,8 `Weinstock` / `Rebe`** — vier Sprachen, s. o.
- **16,4 `vor` / `aus`** — vier Sprachen. `vor` → *against · contra · contre ·
  contro*, was LSG („contre le dévastateur") und RIV selbst schreiben; gilt
  **nur an dieser Stelle**.
- **17,14 `Los` / `Schicksal`** (es/fr/it): `Los` haelt mit 68 Belegen,
  `Schicksal` weicht auf *destino · destin · destino* — **RV schreibt dort
  selbst „el destino"**.
- **18,5 `wegnehmen` / `entfernen`** (es): `entfernen` → *retirar*. **Alle vier
  Ausgaben ziehen die drei deutschen Verben des Verses auf zwei zusammen** und
  geben fuer das dritte keine Form vor — also entscheidet der Bestand.
- **18,2/18,7 `Macht` / `Gewalt`**: `Gewalt` hat eine *power*-Zeile (7 Belege),
  die in beiden Versen **vierfach** mit `Macht` zusammengefallen waere. Genommen
  ist die Mehrheitszeile *violence · violencia · violence · violenza* (32).
- **17,9 `verlassen` (Partizip) / `verließen`** (en/fr/it).

Dazu vom Skript gemeldet und geloest: 16,7 `ganz`/`ganz und gar`, 16,3
`macht`/`trefft`, 16,5 `Ein`/`einer`, 16,12 `geht`/`wird`, 16,8
`sich erstrecken`/`sich ausbreiten`, 17,7 `den`/`ihn`, 17,3 `der`/`von`, 17,13
`weit`/`weg`, 18,5 `Blüte`/`Blütezeit`.

**Bewusst stehen geblieben:** `Getöse`/`tosen` in 17,12 (Stammsubstantiv zum
Verb — der Bestand bildet die Wiederholung italienisch selbst ab,
*rumore*/*rumoreggiano*, und WEB, RV und LSG wiederholen das Wort ebenfalls) und
drei romanische Artikel/Klitikon-Verschmelzungen in Kapitel 18.

### Die vier Laermwoerter von 17,12–13

| Wort | Lvl | en · es · fr · it | Herkunft |
|---|---|---|---|
| `Getöse` | C1 | roar · estruendo · fracas · rumore | **aus 13,4 uebernommen** |
| `Tosen` | C1 | roaring · rugido · mugissement · fragore | **aus 13,4 uebernommen** |
| `tosen` (Verb) | C1 | roar · rugen · mugissent · rumoreggiano | Ps 46,4 |
| `brausen` | C1 | **rush** · resuenan · retentissent · risuonano | Jes 5,30, **en ausgewichen** |

`brausen` waere englisch als dritter *roar* eingelaufen; ausgewichen ist nur en,
auf WEBs eigenes Wort an der Stelle („that rush like the rushing of mighty
waters").

### 18,2 ↔ 18,7 — vermessen, nicht abgeschrieben

`DUBLETTEN_JESAJA.md` fuehrt das Paar nicht (unter der 60-%-Schwelle). Der Agent
hat es mit einem eigenen Skript vermessen: 41 gegen 48 Tokens, **und nur zwei
Bloecke sind woertlich gleich** — `nah und fern` (Versatz −7) und der
Neun-Token-Schluss `Macht und Gewalt, deren Land von Strömen durchzogen wird`
(Versatz −5). Beide Feld fuer Feld uebernommen und maschinell auf Gleichheit
geprueft.

Alles davor formuliert um: die Praeposition wechselt (`zu` → `von`), unbestimmt
wird bestimmt (`einem` → `dem`), **praedikativ wird attributiv**
(`hochgewachsen` → `hochgewachsenen`), **18,7 verschmilzt die beiden
`Volk`-Glieder zu einem**, `gefürchtet` wandert hinter „nah und fern", und aus
`von Macht` wird der Genitiv `der Macht`.

**Und die Genusfalle war auch hier zu bedienen:** `Nation` ist romanisch
feminin, `Volk` maskulin — mitgewandert sind `einer` → *una · une · una* und
`der` (vor `Nation`) → *la · la · la*, waehrend `der` vor `Macht` maskulin
bleibt (*del · du · del*).

**Alle vier Ausgaben vertauschen in 18,2 und 18,7 `Volk` und `Nation`**: deutsch
steht *Volk – Volk – Nation*, alle vier lesen *nation – people – nation*. Genau
deshalb haelt die Trennung nur, wenn man das deutsche Wort glossiert.

### Neue Lemmata

**Kapitel 16:** `Zertreter` C1 · `Obstgarten` B2 · `Sommerfrucht` C1 ·
`flatternd` C1 · `quer` B2 · `winzig` B2 · `kümmerlich` C1 · `verächtlich` C1 ·
`Kir-Heres` A1. Mehrwort: `eine Entscheidung treffen` B2 · `ein Ende finden` B1.

**Kapitel 17:** `Ährenlesen` C1 *gleaning grain · espigueo · glanage ·
spigolatura* (gegen `Nachlese` C1 abgesetzt) · `abmagern` C1 · `heillos` C1
(gegen `unheilbar` abgesetzt) · `sorgsam` C1. Mehrwort: `blühen lassen` B2.
Neue Lesarten: `hegen` C1 *tend* (Bestand kennt nur „Groll hegen" = *harbor*) ·
`lieblich` B2 *lovely* (Bestand nur *sweet*).

**Kapitel 18:** `Flügelrauschen` C1 · `Papyrusboot` C1 · `Sonnenschein` B2 ·
`Taugewölk` C1 · `Erntehitze` C1. Neue Lesarten: `durchziehen` B1 *crossed*
(Bestand nur die Wander-Lesart fuer Menschen; hier durchziehen **Stroeme das
Land**) · `Blütezeit` C1 *flowering* · `Traube` B1 *grape* (der einzige Beleg
Hld 1,14 ist eine Bluetentraube).

**`still` in 18,4** setzt fort, was 14,7 begonnen hat: die 12 Bestandsbelege
tragen saemtlich die **Personen-Lesart** *quiet · callado · tranquille · zitto*
(„Sei still!" = schweig). In 18,4 sagt der HERR „Ich will still bleiben und
**zusehen**" — er schweigt nicht, er verhaelt sich ruhig. Genommen ist die Zeile
aus 14,7 im Maskulinum: *quiet · tranquilo · tranquille · tranquillo*, von allen
vier Ausgaben gestuetzt.

### Prompt-Hinweise: dreiundzwanzig widerlegt

Die hoechste Quote bisher. Die lehrreichsten:

| ich schrieb | der Befund |
|---|---|
| `Rebe` = *vines · vides · ceps · viti* (Vorgabe) | **kollidiert in 16,8 vierfach mit `Weinstock`** |
| `über` in 13,1 aus 2,1 uebernehmen | **falsche Konstruktion** — 15,1 und 17,1 haben unabhaengig die richtige Zeile |
| `Hochmut`/`Überheblichkeit` englisch aufloesen | **in 9,8 laengst geloest** (*haughtiness*) |
| `Übermut`/`Überheblichkeit` kollidieren franzoesisch | nein — *insolence* / *arrogance* |
| `Sonnensäulen` steht nicht im Bestand | **die Form ist 4× belegt**; nur `fixgloss.py show` schweigt |
| `Ascherapfahl` 2 Belege, Singularreihe | **5 Belege**, davon 3 Plural |
| `Refaim` sei ein Homograph wie `Aja` | **nein** — alle 3 Belege sind dasselbe Tal |
| `hochgewachsen` sei unbelegt | **Bestandslemma**, 5Mo 9,2 in **genau demselben Kontext** („ein großes und hochgewachsenes Volk") |
| WEB schreibe in 18,1 wieder *Cush* | **WEB schreibt selbst *Ethiopia*** — es gab nichts zu entscheiden |
| `Rosinenkuchen`/`Keltern`/`Tagelöhner` seien duenn belegt oder neu | alle drei belegt (6 · **15** · 2) |
| `Kelter` sei neu | **15 Belege** |
| `siehe` (17,14) sei dieselbe Lemmaform wie `Seht` | **eigenes Lemma** (32 Belege) |
| `Ranke`/`Rebe` je nur zwei Belege | `Ranke` 2, **`Rebe` 6** |
| 18,6 vier Tierwoerter, Kollisionsgefahr | in allen vier Sprachen getrennt |
| 16,4 vier „Substantivierungen" | drei sind belegt, nur `Zertreter` neu |
| `erstreckten` unbelegt (`hints.py`) | belegt, ueber `erstrecken` und `sich erstrecken` |
| Belegzahlen | wieder veraltet: `Seht` 48 → **50**, Ueberrest-`Rest` 15 → **16**, `Hochmut` 12 → 14, `stolz` 3 → 9 |

Von `hints.py` als unbelegt gemeldet: Kapitel 16 **14 Formen, 8 wirklich neu** ·
Kapitel 17 **11 Formen, 4 wirklich neu** · Kapitel 18 **9 Formen, 5 wirklich
neu**. `belegt.py` bleibt das Werkzeug, das die Differenz aufdeckt.

### Bestandsbefunde

- **`Hiwiter` (2 Belege) und `Heviter` (21) tragen restlos dieselbe Reihe**
  *Hivites · heveos · Héviens · Hivvei* unter zwei Lemmata — dieselbe Sache,
  zwei deutsche Schreibungen (5Mo 7,1 gegen 2Mo 3,8 u. oe.). Ebenso **`welken`
  und `verwelken`** (es/it) und **`von … aus` / `von aus` / `von ... aus`**, drei
  Lemma-Schreibungen derselben Wendung mit zwei Levels. Alle stehen nie im
  selben Vers → nicht aufgeloest.
- **„spricht der HERR" ist im Bestand zweigeteilt, und das ist richtig:** die
  **nachgestellte** Prophetenformel (17,3 · 17,6) traegt *says · dice · dit ·
  dice*, die **einleitende** („so spricht der HERR:", 16,14 · 18,4) *speaks ·
  habla · parle · parla* — **und die Ausgaben schreiben es genauso** (LSG 16,14
  „l'Éternel **parle**, et dit", RIV „l'Eterno **parla** e dice"). Kein Befund.
  Was **doch** einer ist: der Bestand fuehrt die nachgestellte Formel 58-mal mit
  franzoesisch *parle* neben 12-mal *dit*, obwohl englisch beide Male *says*
  steht. Buchuebergreifend zu klaeren, nicht hier.
- **`Kir-Hareset` italienisch** widerspricht seiner Ausgabe an 1 von 1
  Belegstelle (RIV 2Kön 3,25 „Kir-**Hareseth**"). Aeusserlich die
  `Zoar`/`Medeba`-Klasse, aber mit **einem** Beleg zu duenn fuer `remap.py`.
  Gemeldet, Bestand gehalten.
- **`Jaser` und `Sibma` gehoeren *nicht* dieser Klasse an**: RIV schwankt selbst
  (*Iazer* 3× / *Jaezer* 2× / *Jazer* 1×; *Sibma* / *Sibmah*). Wie `fra`/`tra`
  kein Befund.
- **`Sonnensäule` sieht aus wie die `Zoar`-Klasse und ist es nicht:** WEB und RV
  widersprechen der Bestandsreihe an jeder Belegstelle („incense altars" /
  „altares de incienso"), aber **sie uebersetzen das Hebraeische**, waehrend das
  deutsche Wort `Sonnensäule` heisst. LSG und RIV stuetzen den Bestand.
- **`übers` in 16,8** heisst „bis übers Meer" **jenseits**, nicht „ueber … hinweg"
  wie in den beiden Bestandsbelegen (2Chr 2,15 · 9,21, Seeweg). Eigene Glosse
  *beyond the · más allá del · au-delà de la · oltre il*.

### Ausgabenbefunde

- **RIV: drei neue Setzfehler**, nachgetragen — **16,7 „di *ir*-Hareseth"**
  (*Kir-Hareseth*), 16,8 „che **nebriavano**" (*inebriavano*), 17,8 „le sue
  **dite**" (*dita*). **Kapitel 18 hat null.**
- **16,7 hat eine Luecke im Verfahren aufgedeckt.** Die maschinelle Auszaehlung
  sucht **grossgeschriebene** Woerter mitten im Satz — hier hat RIV das **K**
  verschluckt, und der Stumpf `ir` ist kleingeschrieben. **Ein verschluckter
  Anlaut kann den Grossbuchstaben selbst wegnehmen**, dann faellt der Eigenname
  aus dem Suchmuster. Die Liste ist also auch bei Eigennamen eine Untergrenze;
  das steht jetzt in `RIV_SETZFEHLER_JESAJA.md`.
- **RIV verschiebt die Versgrenze 17,12/17,13** — die zweite Haelfte von de 17,12
  steht am Anfang von RIV 17,13. Nach 14,3/14,4 der zweite Fall dieser Art.
- **17,9: keine der vier Ausgaben liest `Hiwiter und Amoriter`** — alle
  uebersetzen das Hebraeische („woods and mountain top"). **16,8 `Völker`: alle
  vier schreiben „nations".** **`Obstgärten` (16,10): keine der vier uebersetzt
  es.** **`Beeren` (17,6): alle vier schreiben „Oliven".** **`Schutz` (16,4):
  alle vier schreiben „refugio/refuge/rifugio".** Fuenfmal derselbe Fall wie
  `Nachtwache` 1,8 — der deutsche Quelltext gewinnt.
- **LSG 18,1 liest etwas voellig anderes**: „le cliquetis des armes"
  (Waffengeklirr) statt `Flügelrauschen`; WEB, RV und RIV folgen dem Deutschen.
  Fuer das franzoesische Glied gab es faktisch nur drei Ausgaben.
- **RIV 18,6 fuegt ein Subjekt ein, das der deutsche Text nicht hat** („**Gli
  Assiri** saran … abbandonati"); **RV 18,3 macht aus den Imperativen
  Indikative**; **RV 16,7 und LSG 16,7 lesen `Rosinenkuchen` als „Fundamente"
  bzw. „Ruinen"**; **LSG 17,11 laesst `Krankheit` weg**; **RV 17,2 und LSG 17,2
  fuegen je einen Halbsatz hinzu**, der im Deutschen fehlt.

## 14. Paket 8 (Kap. 19 · 20 · 21)

Drei Kapitel gleichzeitig, 1089 Einzelwort- und 41 Mehrwort-Eintraege. Alle
Pruefungen je Kapitel sauber; `validate.py 23`, `qa.py 23`, `hilfsverb.py 23`
und `mehrwort.py 23` melden ueber das gebaute Buch **0 Befunde** (die zwei
`mehrwort`-Treffer sind der bekannte richtige Fall aus 8,7). Damit sind
**21 von 66 Kapiteln** fertig: 398 Verse, 9240 Eintraege.

### Die Welle hat den Artikelfehler aus Paket 7 nicht geerbt

Die 21 Stellen dieser Welle mit Artikel vor `HERR` sind **alle richtig**:
italienisch nicht elidiert (`il` · `Il` · `del` · `al` · `dal`), franzoesisch
elidiert (`l'` · `L'` · `de l'` · `à l'`). Das war die offene Frage nach Paket 7,
wo Kapitel 17 den Fehler von Kapitel 1 prompt mitgeerbt hatte. **Die Korrektur
hinter dem Einsammeln hat gehalten** — das Verfahren ist damit einmal bestaetigt.

### Vom Koordinator angeglichen — einmal, und die Ausgabe entscheidet

**`Hüfte` in 21,3** von *hips · caderas · hanches · fianchi* auf ***waist ·
cintura · reins · fianchi***. Beide Kapitel der Welle haben das Wort (20,2 · 21,3),
beide haben **unabhaengig eine andere Bestandsreihe** gewaehlt — der Bestand
fuehrt fuer `Hüfte` sieben Reihen, und keine ist falsch.

Entschieden hat nicht die Mehrheit, sondern die Ausgabe **am Vers**: **LSG
schreibt an beiden Stellen *reins*, RIV an beiden *fianchi*.** Die von Kapitel 21
gewaehlte Reihe stammt aus 11,5 und traegt fr *hanches* — was LSG in 21,3
widerspricht. WEB (*thighs*) und RV (*mi cuerpo*) stuetzen an dieser Stelle
keine der beiden Reihen, sind also frei; die Reihe mit 11 Belegen und dem
buchinternen Praezedenzfall **5,27** gewinnt.

**Die Lehre:** wo zwei Kapitel derselben Welle zwei Bestandsreihen desselben
Lemmas waehlen, entscheidet nicht die Belegzahl, sondern **welche Reihe die
Ausgaben an den beiden Versen selbst schreiben**. Kein Werkzeug meldet diesen
Fall — `konsistenz.py` sieht zwei belegte Reihen und schweigt.

Die uebrigen 27 kapiteluebergreifenden Divergenzen der Welle waren durchweg
Tempus, Numerus, Genus oder echte Bedeutungsunterschiede: `grausam` fr
*cruel*/*cruelle* (Koenig gegen Vision), `ablegen` *take off* (Sack, 20,2) gegen
*make* (Geluebde, 19,21), `ziehen` *ôte* (Schuhe) gegen *Va'* (heraufziehen).

### `Rest` = Ueberrest, viertes Mal — und diesmal traegt WEB nicht

Das Kriterium aus Kapitel 15 lautete, WEB sei die einzige Sprache, die beide
Lesarten lexikalisch trennt. In **21,17 schreibt WEB *residue***, also nicht das
Kriteriumswort. Getragen hat stattdessen **RV: „el remanente del numero de los
valientes arqueros"** — die spanische Ausgabe setzt das Ueberrest-Wort selbst.

**Ergebnis gleich, Begruendungsweg neu.** Das Kriterium ist damit nicht
widerlegt, aber es ist **nicht an WEB gebunden**: es genuegt, dass *irgendeine*
Ausgabe die beiden Lesarten am Vers trennt.

### Die zwei Dubletten wurden vermessen, nicht abgeschrieben

- **21,16 ↔ 16,14** (Versatz −3, 8 Tokens): 7 von 8 Feldern gleich. Die
  Abweichung sitzt bei `gerechnet` — 16,14 hat „In **drei Jahren**" (Plural:
  *contados · comptés · contati*), 21,16 „In **einem Jahr**" (Singular:
  *contado · compté · contato*). **Genau die Stelle, an der Abschreiben falsch
  glossiert haette.**
- **21,17 ↔ 5Mo 28,62** (Versatz +7, 7 Tokens): 5 identisch. Bei `übrig` und
  `bleiben` ist bewusst **16,14 statt 5. Mose** gefolgt — derselbe Vers-Bauplan
  im selben Buch, und 5Mo 28,62 fuehrt dort keinen `übrig bleiben`-Mehrwort-
  Eintrag, 16,14 schon.
- **19,15 ↔ 9,13**: die Viererreihe `Kopf` A1 · `Schwanz` B1 · `Palmzweig` B2 ·
  `Binse` C1 Feld fuer Feld uebernommen.

### Kollisionen, die kein Skript gemeldet hat — vier in einer Welle

`hints.py` blendet Funktionswoerter aus und prueft nur exakte Formen; diese vier
fielen durch und waren alle echt:

- **19,6 `Schilf` ↔ `Binse`** fallen es/it vollstaendig zusammen (*juncos* /
  *giunchi* fuer beide). `Binse` haelt seine Reihe aus 9,13 (derselbe
  Vers-Partner wie 19,15), `Schilf` weicht auf **RVs und RIVs eigene Woerter an
  der Stelle** aus: es *cañas*, it *canne*.
- **19,6 `Kanal` ↔ `Flussarm`** waeren fr/it identisch geworden — LSG und RIV
  schreiben *canaux* / *canali* fuer **beide**. `Kanal` haelt die Jes-8,7-Reihe,
  `Flussarm` ist neu abgesetzt.
- **19,20 `Retter` ↔ `befreien`** laufen es/fr/it auf denselben Stamm. Nur
  teilweise geloest (fr *délivre*, en *sets free*); es *libra* / it *libera*
  bleiben stammverwandt zu *libertador* / *liberatore*. Gemeldet, nicht gebogen.
- **20,2 `ablegen` ↔ `ziehen`** tragen fr beide *ôte*, it beide *togli(ti)*.
  Aufgeloest nach LSG und RIV, die selbst trennen: `ablegen` *détache* /
  *sciogliti* gegen `ziehen` *ôte* / *togli*.

Dazu drei **gemeldete** Kollisionen, die weiter reichten als der Bericht:
`austrocknen ↔ versiegen` (19,5) betrifft auch es, `Narr ↔ töricht` (19,11) auch
es, `ablegen ↔ geben` (19,21) auch fr/it.

### Und zwei gemeldete Kollisionen, die es nicht gab

- **`dieser` ↔ `jener` in 20,6** — `Küste` ist romanisch feminin, `Zeit`
  maskulin; alle vier Ausgaben trennen von selbst.
- **`gehen` ↔ `ziehen` in 20,2** kollidiert nicht, sobald man den Vers liest
  (`Geh` · „ab**ziehen**" · „**ging** umher" sind drei Formen). Die echte
  Kollision des Verses stand oben und war nicht gemeldet.

### Neue Lemmata

**Kapitel 19** (12 + 1 Mehrwort): `Baumwolle` B1 · `Leinenweber` C1 ·
`Lohnarbeiter` C1 (es *asalariados*, bewusst gegen `Tagelöhner` *jornaleros*
abgesetzt) · `Eckpfeiler` C1 (gegen `Eckstein` abgesetzt) · `Gedenksäule` C1 ·
`Sonnenstadt` C1 · `Flussarm` C1 · `Saatfeld` B2 · `Memphis` A1 · `verdunsten`
C1 · `durcheinanderbringen` C1 · `irreführen` C1. Mehrwort: `die Treue schwören`
B2.

**Kapitel 20** (2): `Sargon` A1 · `Verbannter` C1 *exiles · desterrados ·
exilés · deportati*. **`Verbanntes` in 1Chr 2,7 ist NICHT dasselbe Wort** — das
ist der Bann-Gegenstand (cherem), nicht der Deportierte. Eigenes Lemma.

**Kapitel 21** (5 + 1 Mehrwort): `dahinfegen` C1 · `ölen` B2 · `achtgeben` B2 ·
`Wucht` C1 (gegen `Wut` und `Gewalt` abgesetzt) · `Dedaniter` A1. Mehrwort:
`zunichte machen` B2 (der Bestand kennt nur `zunichte werden`).

### `Sonnenstadt` (19,18): die Ausgaben stehen 2:2, das Deutsche entscheidet

RV *Ciudad del Sol* und RIV *la città del sole* lesen die Sonne, **WEB *The city
of destruction* und LSG *ville de la destruction* das andere hebraeische
Textzeugnis**. Der l1912mod schreibt `Sonnenstadt` und setzt es selbst in
Anfuehrungszeichen — also uebersetzt, nicht transliteriert, und zwar nach dem
deutschen Wort. Dieselbe Entscheidung wie `Nachtwache` 1,8, nur mit einer
gespaltenen statt einer einhelligen Ausgabenlage.

### `Dedaniter` (21,13): jede Sprache folgt ihrer eigenen Ausgabe

WEB *Dedanites* und RIV *Dedaniti* setzen den Volksnamen, **RV *Dedán* und LSG
*Dedan* den Stammvater**. Nach dem `Kir-Heres`-Verfahren folgt jede Sprache
ihrer Ausgabe: `Dedaniter` A1 = *Dedanites · Dedán · Dedan · Dedaniti*. **Der
Artikel davor musste mitziehen** (`der` = *of · de · de · dei*), sonst stuende
im Lesefluss „de los Dedán". Der Bestandseintrag `Dedan` (5×) bleibt unangetastet.

### Prompt-Hinweise: neunzehn widerlegt

Kapitel 19 zehn, Kapitel 20 sechs, Kapitel 21 drei. Die lehrreichsten:

| ich schrieb | der Text sagt |
|---|---|
| `Heerscharen` stehe sechsmal in Kap. 19 | **siebenmal** (19,4.12.16.17.18.20.25) |
| `Wächter` stehe in 21,6 · 8 · 11 · 12 | **21,8 hat keinen** — dort stehen `Wachturm` und `Posten`; das vierte ist 21,12 |
| `An jenem Tag` sei ein Mehrwort-Kandidat | das Buch annotiert die Formel an **20 Stellen** Wort fuer Wort |
| `um … zu` und `nicht mehr` seien Kandidaten in Kap. 21 | **weder `um` noch `nicht` steht in Jesaja 21** |
| alle drei `nackt und barfuß` traegen dieselbe Zeile | 20,2/20,3 Singular, **20,4 Plural** |
| Jes 8,4 liefere `vor dem König von Assyrien` | dort ist `vor` **raeumlich**, in 20,6 heisst es „gerettet **vor**" — alle vier Ausgaben *from/del/du/dal* |
| `weisesten` gehoere zu `Weiser` | in 19,11 **attributiv** → Lemma `weise` |

**Von 40 als „unbelegt" gemeldeten Formen waren 19 wirklich neu.** `belegt.py`
und `fixgloss.py show <Lemma>` bleiben das Werkzeug, das die Differenz aufdeckt —
`aufhetzen` hat sogar einen Beleg **aus diesem Buch** (13,17), und `rasen` steht
im Bestand, obwohl `belegt.py` nur das Substantiv `Rast` zeigt.

### Bestandsbefunde

- **`von Assyrien` ist italienisch gespalten:** Jes 8,4 *di*, Jes 10,12 und
  2Kön 18,17 *d'*. **RIV schreibt an allen Stellen „d'Assiria"** — dieselbe
  Klasse wie der `l'`/`il SIGNORE`-Fund aus Paket 7 (die Funktionswortglosse
  richtet sich nach dem Anlaut der **Nachbarglosse**). 8,4 sieht falsch aus.
  Dasselbe Muster bei `von Kusch` (Jes 18,1 *de*/*di* vor *Éthiopie*/*Etiopia*).
  **Zu duenn fuer `remap.py`, buchuebergreifend zu klaeren.**
- **`Zoan` italienisch hat eine dritte, von keiner Ausgabe gedeckte Form:** der
  Bestand fuehrt fuer 4Mo 13,22 it *Soan*, was RIV nirgends schreibt (RIV hat
  *Zoan* in Ps 78,12/43, *Tsoan* in 4Mo 13,22 und Jes 19,11/13). Weil RIV selbst
  schwankt, ist es **nicht** die `Zoar`/`Medeba`-Klasse — die *Soan*-Zeile ist
  trotzdem ein Ausreisser.
- **`Kedar` italienisch: RIV widerspricht der Bestandsreihe an 3 von 4 Stellen**
  (*Kedar* in 1Chr 1,29 · Ps 120,5 · Jes 21,16/17, aber *Chedar* in Hld 1,5).
  **Nicht** die `Zoar`-Klasse, die Widerlegung an *jeder* Stelle verlangt,
  sondern der `fra`/`tra`-Fall: die Ausgabe schwankt selbst. Bestand gehalten.
- **`um zu` gegen `um ... zu`:** korpusweit 388 : 6, und **alle sechs Ausreisser
  sind Jesaja 13**. Zu bereinigen.
- **`acht geben` gegen `achtgeben`** und **`schämen` gegen `sich schämen`** —
  je zwei Lemmaschreibungen derselben Sache. Nach dem `Schinar`-Verfahren
  behandelt (Lemma aus dem Text, Reihe aus dem Bestand), nicht angefasst.
- **`Schilf` B2 und `Binse` C1 sind es/it eine Sachdublette** (beide *juncos* /
  *giunchi*) unter zwei Lemmata — die achte dieser Art. Hier **musste** sie
  aufgeloest werden, weil beide in 19,6 im selben Vers stehen.

### Ausgabenbefunde

- **RIV: sechs neue Setzfehler**, nachgetragen in `RIV_SETZFEHLER_JESAJA.md` —
  **19,22 „che ’arrenderà"** (*s’arrenderà*, zweiter Anlautfall an einem
  Klitikon nach 7,25), **20,4 „con la natiche"** (*le*), **21,3 „pieni si
  dolori"** (*di*), **21,3 „o mi contorco"** (*io*), **21,8 „di giorni"**
  (*giorno*), **21,12 „ornate un’altra volta"** (*tornate* — siebter Fall der
  Klasse „Anlaut, Gemeinwort"). 21,9 „abilonia" und 19,23 „in ssiria" standen
  bereits in der Tabelle.
- **RIV 19,1 setzt zweimal daneben**: „**l’**idoli d’Egitto" (richtig *gl’idoli*
  — dieselbe Ausgabe schreibt es in 19,3 korrekt) und „che **cavalcava**"
  (Imperfekt, wo Deutsch, WEB, RV und LSG Praesens haben).
- **Die `Nachtwache`-Klasse noch einmal viermal** — der deutsche Quelltext
  gewinnt gegen alle vier Ausgaben: **19,10 `Weber`** (alle vier lesen
  Saeulen/Stuetzen), **20,3 `Warnung`** (alle vier „Vorzeichen"), **20,4
  `wegtreiben`** (alle vier „wegfuehren"), **21,5 „breitet Decken aus"** (alle
  vier lesen Wachdienst). Dazu **21,2 `grausam`**, wo alle vier *terrible* /
  *grievous* schreiben und die Bindung *cruel · cruel · cruelle · crudele* gilt —
  gestuetzt durch **13,9 im selben Buch**.
- **19,23: alle vier lesen „der HERR", wo das Deutsche `Gott` hat**; WEB laesst
  das Objekt ganz weg. **21,16: RV schreibt „Jehová", wo das Deutsche `Herr`
  (Adonai) hat** — die drei anderen folgen dem Deutschen.
- **RV setzt in 20,6 · 21,5 · 21,12 · 21,14 `ustedes`-Imperative** gegen die
  Buchkonvention `vosotros`. Glossiert ist die Konvention, wie seit 13,2.
- **LSG 20,1 zieht zusammen** („vint assiéger Asdod") — `Aschdod` steht
  franzoesisch nur **einmal**, und fuer `kämpfte` gibt LSG keine Form vor; RIV
  baut dieselbe Stelle dreigliedrig um und liefert fuer `kam` nichts.
- **19,7 LSG liest „nudité" statt `Wiesen`**; **19,9 nur RIV stuetzt
  `Baumwolle`** (*cotone*), RV liest „tejedores de redes" (Netze); **21,1 LSG
  setzt Singular** („l’ouragan du midi") gegen `Wirbelstürme`; **21,12 LSG fuegt
  „Convertissez-vous" hinzu**, das im Deutschen fehlt; **21,3 WEB liest den
  ganzen Vers anders**; **21,4 RIV liest „la sera"** statt `Dämmerung`.
- **Versgrenzen: keine Verschiebung in allen drei Kapiteln** — `ausgaben.py`
  meldet Versatz +0 fuer alle vier Ausgaben. Anders als 14,3/14,4 und 17,12/17,13.

### Ein spanischer Konjunktiv statt einer Notloesung

**`gehen` ↔ `sehen` in 21,6** („**Geh**, stell einen Wächter auf, der berichtet,
was er **sieht**") fallen spanisch auf *ve* zusammen. Ausgewichen ist nicht das
haeufige `Geh` (118 Belege, und RV schreibt selbst „Ve, pon un centinela"),
sondern `sieht` → **es *vea***. Das ist keine Notloesung: nach unbestimmtem
Antezedens verlangt das Spanische den Konjunktiv, und **RV schreibt an der
Stelle woertlich „lo que vea"**. Mitgezogen ist `berichtet` → *informe*; fr und
it bleiben indikativisch, weil sie den Konjunktiv nicht fordern.

**Die Gegenprobe dazu, wo bewusst nichts geloest wurde:** 21,8 `stehe` und `bin`
fallen spanisch auf *estoy* zusammen — **RV schreibt in genau diesem Vers
zweimal „estoy"**, und `estar` ist fuer beide deutschen Verben die richtige
Wahl. Dasselbe Muster wie `Getöse`/`tosen` in 17,12.

## 15. Paket 9 (Kap. 22 · 23 · 24)

Drei Kapitel gleichzeitig, 1381 Einzelwort- und 51 Mehrwort-Eintraege. Alle
Pruefungen je Kapitel sauber; `validate.py 23`, `qa.py 23` und `hilfsverb.py 23`
melden ueber das gebaute Buch **0 Befunde**. Damit sind **24 von 66 Kapiteln**
fertig: 464 Verse, 10 672 Eintraege.

### Die erste Welle ohne eine einzige Angleichung

Paket 8 musste `Hüfte` angleichen, Paket 7 zweimal eingreifen. **Paket 9 gar
nicht** — und die zwei Faelle, die auf den ersten Blick danach aussahen, sind
beim Nachsehen genau richtig gewesen:

- **`in der Höhe`** traegt in 22,16 *en las alturas · sur les hauteurs · sulle
  alture* und in 24,21 *en lo alto · dans le ciel · nei luoghi eccelsi*. Zwei
  Reihen fuer dasselbe Mehrwort-Lemma in einer Welle — aber **die drei
  romanischen Ausgaben schreiben in 24,21 wortwoertlich, was dort steht** (RV
  „en lo alto", LSG „dans le ciel", RIV „nei luoghi eccelsi"). Dazu meinen die
  Stellen Verschiedenes: 22,16 ist die **Felsgruft**, 24,21 der
  **Himmelsbereich** — und der Bestand spaltet selbst so (Hiob 39,27 physisch
  gegen die sechs Himmelsbelege).
- **`es ergehen`** traegt in 23,15 die Futurzeile und in 24,2 die Praesenszeile
  desselben Bestandslemmas. LSG schreibt „il en **sera** de Tyr" gegen „il en
  **est** du sacrificateur" — die Ausgabe macht den Tempusunterschied selbst.

**Das Kriterium aus Paket 8 traegt also in beide Richtungen:** es sagt nicht nur,
wann anzugleichen ist, sondern auch, wann eine Divergenz **stehen bleiben muss**.
Massgeblich ist, was die Ausgaben **am jeweiligen Vers** schreiben — nicht die
Gleichfoermigkeit der Welle.

### Der Fund der Welle: `dei eserciti` ist ungrammatisch

Gemeldet vom Agenten fuer Kapitel 22, nachgezaehlt und korrigiert. Der Bestand
stand **70 : 5** fuer `degli` vor `Heerscharen`, und **alle fuenf Ausreisser
waren Jesaja** (9,6 · 9,12 · 9,18 · 18,7 zweimal).

Es ist nicht bloss eine Minderheit, sondern **falsches Italienisch**: vor
vokalisch anlautendem *eserciti* verlangt die Sprache `degli`, im Lesefluss
stand dort „dei eserciti". **RIV schreibt an der einzigen Stelle, an der die
Wendung in der Ausgabe ueberhaupt vorkommt (18,7), selbst *degli eserciti*.**

Das ist die **zweite Auflage der Nachbarfalle** nach dem `l'`/`il SIGNORE`-Fund
aus Paket 7: die italienische Funktionswortglosse richtet sich nach dem Anlaut
der **Nachbarglosse**. Nach der Korrektur zaehlt der Bestand 75 : 0.

### Ein Befund, der bewusst NICHT angefasst wurde

Derselbe Bericht meldete `der` vor `Heerscharen` auch englisch als gespalten.
Das Nachzaehlen ergibt ein anderes Bild als der Bericht:

| Buch | `of` | `of the` |
|---|---|---|
| Jesaja | 21 | 17 |
| Psalmen | 2 | 13 |
| 2. Samuel | — | 6 |
| 1. Chronik | — | 3 |
| uebrige | 3 | 2 |

**Beide Lesarten sind grammatisch**, ueber sieben Buecher verteilt, und Jesaja
ist in sich fast haelftig gespalten. Das ist **keine Nachbarfalle und kein
Ausreisser**, sondern eine offene Entscheidung ueber 62 Eintraege in sieben
Buechern. Sie gehoert in einen eigenen Durchgang, nicht als Nebenwirkung eines
Kapitelpakets — sonst entsteht wieder der Zustand, den Paket 7 geheilt hat.

**Die Lehre:** ein gemeldeter „Bestandsbefund" ist erst dann ein Auftrag, wenn
die Auszaehlung zeigt, dass eine Seite **falsch** ist — nicht nur seltener.

### Kollisionen: acht in einem Kapitel, keine davon gemeldet

Kapitel 24 hat mit einem **eigenen Skript, das auch Funktionswoerter prueft**,
acht echte Kollisionen gefunden, die `hints.py` prinzipiell nicht sieht. Die
lehrreichsten:

- **24,23 `beschämt` ↔ `zuschanden`** — en beide *put to shame*, es beide
  *avergonzado*. Die **neunte restlose Sachdublette** unter zwei Lemmata.
  Aufgeloest, weil alle drei romanischen Ausgaben selbst trennen (RV „se
  avergonzará … se confundirá", LSG „de honte … de confusion", RIV „di rossore …
  di vergogna").
- **24,8 `verstummt` ↔ `vorbei` ↔ `vergangen`** — hier hat der Agent den
  Ausgaben **widersprochen**, und zu Recht: alle vier schreiben dreimal dasselbe
  Wort, der Bestand trennt die drei Lemmata bereits. Waere er den Ausgaben
  gefolgt, stuende im Lesefluss dreimal dasselbe.
- **24,10 `in` ↔ `hinein`**, **24,13 `bei` ↔ `zu` ↔ `auf`**, **24,18 `vor` ↔
  `aus`**, **24,23 `auf` ↔ `in`** — vier reine Praepositionsfaelle. Genau die
  Klasse, die `hints.py` ausblendet und die `AUFTRAG_AT.md` deshalb zum
  Selbstnachzaehlen aufgibt.

Dazu in Kapitel 22 drei nicht gemeldete (`aus ↔ von` 22,19 · `anziehen ↔ legen`
22,21 · `sprechen ↔ sagen` 22,25) und in Kapitel 23 drei (`Aber ↔ sondern` ·
`man ↔ sich` · `des ↔ vom`).

**Die Gegenprobe zaehlt auch:** Kapitel 24 hat sechs vermutete Kollisionen
**widerlegt** (`Falle ↔ fällt`, `Grube ↔ Kerker`, `jubeln ↔ jauchzen`,
`taumeln ↔ schwanken`, `Freude ↔ Jubel`, und `Nachlese ↔ Ährenlesen` steht gar
nicht im Kapitel). Eine Auflösung ohne Kollisionsstelle macht den Bestand nur
inkonsistent.

### Die Trockenwoerter, zum zweiten Mal — und die Regel dahinter

Nach den sieben Austrocknungswoertern von 19,5–7 hat 24,4 fuenf weitere:
`trauern` · `verwelken` · `verdorren` · `welken` · `verkuemmern`, dazu
`schwinden` in 24,6 und `welken` noch einmal in 24,7.

Die Auflösung folgte einer Regel, die vorher nicht ausgesprochen war: **je
Sprache weicht das Wort aus, das seltener im Kapitel steht** — `welken` steht
zweimal, `verwelken` einmal, also weicht `verwelken` in en und it. Und es weicht
**auf das Wort, das die Ausgabe an der Stelle selbst schreibt** (en *fades away*
nach WEB, it *è spossata* nach RIV). Spanisch lag umgekehrt, weil **RV an beiden
`welken`-Stellen *decayó* schreibt** — dort weicht `welken`. Franzoesisch
kollidierte gar nichts.

`verdorren` bleibt bei *withers*; die Entscheidung aus 15,6 wird nicht
umgestossen.

### Neue Lemmata

**Kapitel 22** (9): `Trubel` B2 · `Ausgelassenheit` C1 (gegen `Freude`
abgesetzt) · `Zertretung` C1 · `hallen` C1 · `Waldhaus` C1 (it *foresta* nach
RIV, nicht `Wald`-*bosco*) · `Sammelbecken` B2 · `fortschleudern` C1 (bewusst
**ohne** *lejos/loin*, sonst Kollision mit `weit` im selben Vers) · `Ball` A1 ·
`Ehrenthron` C1.

**Kapitel 23** (4): `Kronenstadt` C1 · `Belagerungsturm` C1 · `horten` C1 ·
`Angesehenster` B2 (Reihe aus dem Bestand, eigenes Lemma weil substantiviert —
2Kön 10,6 ist attributiv).

**Kapitel 24** (7): `Chaos` B2 (nur RV stuetzt es) · `Entleiher` B2 (gegen
`Schuldner` abgesetzt) · `Abschlagen` C1 (Substantiv, gegen `abschlagen` = *cut
off* abgesetzt) · `bersten` C1 · `verkuemmern` C1 · `schamlos` C1 ·
`zusammentreiben` C1.

### Prompt-Hinweise: einundvierzig widerlegt

Kapitel 22 elf, Kapitel 23 neunzehn, Kapitel 24 elf — die hoechste Quote des
Buches. Die lehrreichsten:

| ich schrieb | der Text sagt |
|---|---|
| die Adonai-Jahwe-Formel stehe in Kap. 22 **fuenfmal** | **viermal** — 22,25 hat sie gar nicht |
| `durchziehen` 23,10 nehme die *crossed*-Lesart aus 18,2 | **falsch** — 18,2 ist finit mit Stroemen als Subjekt; 23,10 ist der Imperativ und deckt sich Feld fuer Feld mit **1Mo 13,17** (LSG *Parcours*, RIV *Percorri*) |
| `nicht mehr` stehe in 23,1 · 23,10 · 24,20 | **an keiner der drei Stellen** — zweimal ist es `kein … mehr`, einmal „steht **nicht wieder** auf" |
| 24,4 habe drei Trockenwoerter | **fuenf**, und `welken` steht auch in 24,7 — die Auflösung musste kapitelweit tragen |
| `Grube` stehe in 24,17 · 18 zweimal | **viermal** (24,17 · 18 · 18 · **22**) |
| 24,19 vier Bruchwoerter, Kollisionsgefahr | **keine** — drei sind in allen vier Sprachen schon getrennt |
| `aushauen`, `verjagen`, `abschiessen` seien neu | alle **belegt** — `aushauen` aus **Jes 5,2**, `verjagen` aus **Jes 17,13** |
| `Abschlagen` sei `abschlagen` = *cut off* | **andere Bedeutung** — alle vier Ausgaben lesen „schuetteln" |

**Von 46 als unbelegt gemeldeten Formen waren 17 wirklich neu.** Und die
schaerfste Falle des Pakets stand in keinem Hinweis: **`Spiel` in 23,16 ist kein
Substantiv**, sondern der Imperativ von `spielen` A1 — der Lexikon-Extrakt zeigt
dort nur `Spiel` = *game · juego · jeu · gioco*.

### Ein Mehrwort, das nur beim Lesen auffaellt

`dahinschwinden` C1 liegt in **24,6 getrennt** („schwinden die Bewohner … dahin")
und steht drei Belege stark im Bestand, darunter **Jes 17,3 im selben Buch**.
`konvention.py` prueft diese Wendung nicht, und fuer `selfcheck.py` und `qa.py`
ist ein fehlender Mehrwort-Eintrag **prinzipiell unsichtbar**. Der Agent hat ihn
und elf weitere Bestands-Mehrwoerter beim Lesen gefunden — dazu meldet
`sweep.py --kapitel` in Kapitel 23 das ebenfalls ungelistete `es geben` (150+
Belege). **`konvention.py` allein reicht nicht.**

### Bestandsbefunde

- **`beschämen`/`zuschanden` sind en/es eine Sachdublette** unter zwei Lemmata —
  erstmals in 24,23 im selben Vers, deshalb dort aufgeloest.
- **`kein mehr` (22) gegen `kein … mehr` (2)** und **`sich kümmern` gegen `sich
  kümmern um`** — zwei weitere Lemmaschreibungen derselben Sache, wie `um zu` /
  `um ... zu`. Zu bereinigen.
- **`Trank` C1 *drink* kollidiert korpusweit mit `trinken` A1 *drink*** im
  Englischen; nur in 24,9 aufgeloest.
- **Die Lexikonfalle hat dreimal gegriffen:** `Herr` in 24,2 (Bestandsmehrheit
  612:153 fuer den goettlichen *Lord*, hier der Menschenherr — LSG *maître*,
  RIV *padrone* stuetzen), `Gefangener` in 24,22 (Extrakt zeigt die NT-Lesart
  *prisoners*, gesetzt ist die AT-Bindung *captives*), und **das ganze
  Handelsfeld von Kapitel 23** ist fast rein neutestamentlich belegt (`Gewerbe`
  1 Beleg, `Markt` 4, `Verdienst` 4, `Zypern` 8 — **alle NT**).
- **`Riss` B2** fuehrt fuer den Mauerdurchbruch *cracks · grietas · brèches ·
  rotture*, waehrend alle vier Ausgaben in 22,9 „breaches/brechas/brèches/brecce"
  schreiben. es/it sehen schwach aus — zu duenn fuer `remap.py`.

### Ausgabenbefunde

- **Sieben neue RIV-Setzfehler** (22,3 · 22,8 · 23,11 · 23,13 · 23,15 · 24,19 ·
  24,20), nachgetragen. **23,13 ist eine dritte blinde Klasse:** „i palazzi di
  **tiro**" — der Eigenname ist nicht verstuemmelt, nur kleingeschrieben, und
  faellt dadurch mit dem italienischen Gemeinwort *tiro* (Wurf, Zug) zusammen.
  Er ist damit weder fuer die Eigennamensuche noch fuer die Anlautsuche
  sichtbar.
- **Der erste Setzfehler in WEB:** 24,17 „you who **inhabitant** the earth"
  (*inhabit*). Die Setzfehlerliste ist nach RIV benannt, weil dort die Haeufung
  liegt — **die anderen drei Ausgaben sind nie systematisch durchgesehen
  worden**.
- **Die `Nachtwache`-Klasse noch sechsmal** — der deutsche Quelltext gewinnt
  gegen alle vier Ausgaben: `Zypern` 23,1/12 (**alle vier transliterieren
  Kittim/Quitim**), `Fesseln` 23,10, `Wüstentiere` 23,13, `Gewerbe`/`Handel
  treiben` 23,17, `Sturm` 24,20, `schamlos` 24,16.
- **24,2 vertauschen zwei Ausgaben die Listenglieder:** WEB dreht die Paare 5
  und 6, RV die Paare 1–4; LSG und RIV folgen der deutschen Reihenfolge. Weil
  wortweise glossiert wird, hat das keine Folge — **aber es ist genau die
  Stelle, an der ein Abschreiben nach der Ausgabe um eine Position verrutscht
  waere.** Das Listenskript hat jede Position aus dem Quelltext neu abgeleitet.
- **RIV 22,14 schreibt „l'Iddio degli eserciti"**, wo dieselbe Ausgabe an fuenf
  anderen Stellen des Kapitels *l'Eterno* setzt; **RIV 22,18 schreibt `Signore`
  gross an einem menschlichen Herrn**. Beides Schwanken der Ausgabe, keine
  Glossenaenderung — dieselbe Klasse wie „degli Eserciti" in 10,33.
- **RV setzt in 22,4 · 23,1 · 23,2 · 23,6 wieder `ustedes`-Imperative** gegen die
  Buchkonvention `vosotros`, und **wechselt in 22,9–11 in die 3. Person Plural**,
  wo die vier anderen die 2. Person haben.
- **Versgrenzen: kein Versatz in allen drei Kapiteln.**

## 16. Paket 10 (Kap. 25 · 26 · 27)

Drei Kapitel gleichzeitig, 1056 Einzelwort- und 42 Mehrwort-Eintraege. Alle
Pruefungen je Kapitel sauber; `validate.py 23`, `qa.py 23` und `hilfsverb.py 23`
melden ueber das gebaute Buch **0 Befunde**. Damit sind **27 von 66 Kapiteln**
fertig: 510 Verse, 11 771 Eintraege.

### Zwei Kapitel derselben Welle haben sich ohne Absprache getroffen

25,9 und 26,1 beginnen beide mit `An jenem Tag wird man`, und beide Agenten
haben **dieselbe Zeile Feld fuer Feld** gesetzt — *On · En · En · In* / *that ·
aquel · ce · quel* / *day · día · jour · giorno*, kein Mehrwort. Die Gegenprobe
ueber den ganzen Bestand zeigt, warum das funktioniert hat: die Formel ist an
**allen 33 Buchstellen einhellig**.

**Die Lehre fuer den Wellenschnitt:** wo eine Formel im Bestand einhellig ist,
genuegt die Auflage „halte dich an die Buchpraxis" — die Kapitel treffen sich
von selbst. Absprachebedarf entsteht nur, wo der Bestand **mehrere gueltige
Reihen** fuehrt (der `Hüfte`-Fall aus Paket 8).

### Angeglichen: einmal, und der Agent hatte sich auf eine falsche Tatsache gestuetzt

**`seht` in 26,21** trug en *behold* statt *see*. Begruendet war das damit, dass
WEB an dieser Stelle „For, **behold**" schreibe, waehrend 25,9 *See* trage.

**Beide Haelften der Begruendung sind falsch.** WEB schreibt auch in **25,9**
„Behold" — die Ausgaben unterscheiden die beiden Verse also gar nicht. Und der
Bestand traegt fuer `seht` (Lemma `sehen`, Imperativ) an **107 Stellen**
*see/See · ved/Ved · voyez/Voyez · vedete/Vedete* und an **keiner einzigen**
*behold*.

Das ist der `Zahl`/*número*-Fall aus `AUFTRAG_AT.md` im Reinformat: eine Glosse
ist ein Leseassistent, und wer ein Wort hundertmal gleich gelesen hat, soll es
nicht einmal anders sehen, bloss weil eine Ausgabe an einer Zeile anders
formuliert. Gesetzt ist *see*.

### Was ein gleichzeitig laufendes Kapitel am anderen findet

Kapitel 26 hat **zwei Befunde an Kapitel 25 gemeldet**, ohne sie anzufassen —
genau das erwuenschte Verhalten:

1. **25,12 fehlte der Mehrwort-Eintrag `zu Boden werfen`** (B1, 4 Belege,
   Ps 17,11 liefert die Infinitivzeile). Der Agent fuer Kapitel 25 hatte nur das
   **reflexive** `sich zu Boden werfen` B2 gesehen („warf sich zu Boden" =
   niederwerfen) und daraus geschlossen, es gebe kein transitives Lemma. Es gibt
   eins. **Vom Koordinator ergaenzt.**
2. Zwei Divergenzen 25↔26, die **stehen bleiben muessen**, gemeldet damit sie
   nicht spaeter „geglaettet" werden: `unser` it *il nostro* (25,9) gegen
   *nostro* (26,13) — **RIV schreibt „il nostro Dio" bzw. „Dio nostro"** — und
   `werfen` es *echar* (25,12) gegen *tira* (26,5), wobei **RV in 25,12 selbst
   „las echará" schreibt**. Beide nachgeprueft und bestaetigt.

**Ein fehlender Mehrwort-Eintrag ist fuer `selfcheck.py` und `qa.py`
prinzipiell unsichtbar** — die Einzelwoerter sind vollstaendig und richtig.
Gefunden hat ihn kein Skript, sondern das Nachbarkapitel.

### Die formbasierte Suche laesst Mehrwoerter durch — drittes Paket in Folge

`konvention.py` und `sweep.py` suchen beide **Wortformen**. Beide Kapitel dieser
Welle haben deshalb **eigene lemmabasierte Skripte** gebaut und damit gefunden,
was keins von beiden meldet:

- **Kapitel 25:** `hoffen auf` (37 Belege) **zweimal in 25,9**, `machen zu`
  (36 Belege) in 25,2, `nie wieder` in 25,2.
- **Kapitel 26:** `hoffen auf` in 26,8 — dasselbe Lemma, dieselbe Welle —
  und `geboren werden` (31 Belege) in 26,18.
- **Kapitel 27:** vier Bestands-Mehrwoerter, darunter **`in den Kampf ziehen`
  mit 20 Belegen**, dazu `abbrechen`, `Erbarmen haben` (Vorlage Jes 9,16) und
  `anbeten` (Vorlage Jes 2,8).

Zusammen mit dem getrennten `dahinschwinden` aus Paket 9 sind das **elf
Mehrwort-Luecken in zwei Paketen**, die die formbasierte Suche nicht sieht.
Der lemmabasierte Sweep gehoert in den Werkzeugordner, nicht in jedes Kapitel neu.

### `abbrechen` in 27,11: die `Hüfte`-Regel wurde falsch herum angewandt

Der Agent fuer Kapitel 27 hat die Zeile aus **22,25** genommen (*break off ·
se arrancan · s'arrachent · si staccano*) und dafuer ausdruecklich die
`Hüfte`-Lehre angefuehrt: die buchinterne Vorlage wiege schwerer als die
Ausgaben. **Er hat die Entscheidung dem Koordinator anheimgestellt — richtig,
denn die Regel sagt das Gegenteil.**

Drei Gruende tragen in dieselbe Richtung:

1. **Es gibt keine Bindung zu schuetzen.** `abbrechen` hat **sieben Belege auf
   fuenf Lesarten**; die physische ruht auf zweien.
2. **Die Bedeutung ist eine andere.** Beide Belege heissen *arrancar · arracher ·
   staccare* — herausreissen. In 22,25 wird ein **Nagel aus seiner Stelle
   gerissen**; in 27,11 **knacken duerre Zweige ab**. Ein Zweig wird nicht
   „arrancado".
3. **Alle vier Ausgaben schreiben in 27,11 die Bruch-Familie** (*broken off ·
   quebradas · brise · rotti*), keine die Reiss-Familie.

Gesetzt ist die neue Lesart *break off · se quiebran · se brisent · si rompono*.
**Die `Hüfte`-Regel greift nur, wo der Bestand mehrere gueltige Reihen fuehrt** —
sie ist kein Vorrang der Naehe.

### Die Wortreihen gleicher Bedeutung, zum dritten Mal

Nach 19,5–7 (sieben Austrocknungswoerter) und 24,4 (fuenf Trockenwoerter) hat
**25,4 drei Schutzwoerter** in einem Vers: `Zuflucht`, `Schutz`, `Unterschlupf`.

Das Ergebnis ist diesmal lehrreich, weil **nur eines weichen musste**:
`Zuflucht` und `Schutz` sind im Bestand laengst getrennt und stehen in **Jes 4,6
im selben Buch schon nebeneinander**. Nur `Unterschlupf` mit seinem **einzigen**
Beleg (Hiob 24,8) kollidierte — en mit `Schutz`, es/fr/it mit `Zuflucht`.

Und das Ausweichen folgte einer besseren Quelle als der freien Wahl: die
Ausgaben schreiben in 25,4 selbst das schon vergebene Wort, also ist auf die
Woerter ausgewichen, die **dieselben Ausgaben in den Parallelversen desselben
Buches** setzen — WEB 32,2 *covert*, RV/LSG/RIV 4,6 *amparo · asile · asilo*.

### Kollisionen: `hints.py` meldete vier, sechs, null — gefunden wurden dreizehn

| Kapitel | von `hints.py` | selbst gefunden | widerlegt |
|---|---|---|---|
| 25 | 4 | 5 (alle Funktionswoerter, keine aufgeloest) | 3 |
| 26 | **1** | 4 (drei aufgeloest) | 7 |
| 27 | **0** | 4 (alle aufgeloest) | 11 |

Die lehrreichsten:

- **26,3 `fest` ↔ `beständig`** waere in **drei Sprachen stammgleich** geworden
  (*firmemente/firme*, *fermement/ferme*, *saldamente/saldo*).
- **26,5 `niedergeworfen` ↔ `gestürzt`** waere es/it **restlos identisch**
  geworden. Und die erste Auflösung des Agenten haette mit dem **gleichzeitig
  laufenden Kapitel 25** kollidiert (*humillado/umiliato* gegen `erniedrigen` in
  25,12) — er hat sie deshalb verworfen. **Ein Agent, der die Nachbarkapitel
  mitprueft, faengt die Wellenkollision selbst ab.**
- **27,5 `bei` ↔ `mit`** in allen vier Sprachen; **27,9 `zerstoßen` ↔
  `zermahlen`** es/fr stammgleich (*moler*/*broyer*) — die elfte Sachdublette.
- **26,1 `jenem` ↔ `dieses`** ist franzoesisch **echt** und bleibt stehen: `ce`
  hat attributiv keine zweite Form, und **LSG schreibt selbst „En ce jour, on
  chantera ce cantique"**. Die Gegenprobe ueber 12 Bestandsverse mit beiden
  Lemmata zeigt: Franzoesisch trennt sonst immer, aber ueber Genus, Numerus oder
  die pronominale Form — **keiner hat zwei maskuline Singulare**.
- **27,10 drei Leere-Woerter** (`einsam`, `verlassen`, `öde`) sind in allen vier
  Sprachen schon getrennt. Haette man `einsam` auf seine Zweitlesart *deserted*
  gesetzt, waere es mit `Wüste` im selben Vers kollidiert. **Widerlegen ist
  genauso viel wert wie aufloesen.**

### Zwei Lexikonfallen, die den Lesefluss verdorben haetten

- **`Wegnahme` (27,9)** hat als einzigen Beleg **Hebr 11,5**, Henochs
  Entrueckung (es *arrebatamiento*, it *rapimento*). Die Zeile haette „die
  **Entrueckung** seiner Suende" ergeben. Neu gesetzt.
- **`gestritten` (27,8)**: der Extrakt zeigt nur die Alltagslesart *argued ·
  discutido · disputé · discusso* (4 Belege). Der Bestand fuehrt daneben **13
  Belege der Rechtsstreit-Lesart** *contend* — und WEB schreibt selbst „you
  contend with them". Der Extrakt zeigt die Mehrheit, nicht die richtige Lesart.
- Dazu in **26,9 `dürr`**: der Extrakt zeigte unter VERWANDT nur *gaunt*
  (1Mo 41,19), waehrend der Bestand **drei Belege der Trocken-Lesart** fuehrt.
  **Dreimal in einem Paket war der Extrakt selbst die Fehlerquelle.**

### Neue Lemmata

**Kapitel 25** (8): `Tyrann` C1 · `Wolkenschatten` C1 · `dämpfen` C1 (gegen
`bezwingen` abgesetzt, beide in 25,5) · `Siegesgesang` C1 · `Mistloch` C1 ·
`Schwimmer` B2 · `Kunstgriff` C1 · `Festungsmauer` C1.

**Kapitel 26** (2): `Züchtigung` C1 · `hinausschieben` C1 (`Nachtwache`-Klasse —
keine Ausgabe liest „schieben").

**Kapitel 27** (3 + 1 Mehrwort): `Altarstein` C1 · `gewunden` C1 · `knospen` B2
(fr eigen, weil LSG beide Verben verschmilzt) · Mehrwort `einer nach dem andern`
B1.

### Prompt-Hinweise: einundvierzig widerlegt

Kapitel 25 elf, Kapitel 26 neunzehn, Kapitel 27 elf. Die lehrreichsten:

| ich schrieb | der Text sagt |
|---|---|
| `Schwangere` (26,17) sei neu | **belegt** als eigenes Lemma B2 — `belegt.py` schweigt, weil im Bestand nur `schwangere` klein steht; `fixgloss.py show Schwangere` findet es |
| aus 13,8 · 21,3 `Gebärende` und `sich krümmen` uebernehmen | 26,17 hat **weder das eine noch das andere Wort** — der Text schreibt `Schwangere` und `sich winden` |
| `nicht länger` (26,21) sei Mehrwort-Kandidat | **kein Bestandslemma** — steht 18-mal im Korpus und traegt nirgends einen Eintrag |
| `um zu` in 26,21 | **es gibt kein `zu`-Token** — „um … heimzu­suchen" hat das zu eingebaut |
| sieben „Wiederholungen" in Kap. 26 seien Kollisionsgefahr | **keine davon** — es ist jeweils **dasselbe** deutsche Wort; die Regel greift nur bei *verschiedenen* Woertern |
| `Bach Ägyptens` stehe evtl. als feste Grenzbezeichnung | **kein Mehrwort im ganzen Bestand** |
| `fortgehen` sei die belegte Nachbarform zu 27,8 | falsches Lemma — `fortgetrieben` → **`forttreiben`**, Beleg **Jes 6,12** |
| bei den vier Verbformen von 27,7 auf Aktiv/Passiv achten | die **beiden `geschlagen` sind beide aktiv**; Aktiv/Passiv trennt nur die beiden `getötet` |

**Von 35 als unbelegt gemeldeten Formen waren 13 wirklich neu.**

### Ausgabenbefunde

- **Drei neue RIV-Setzfehler** (25,12 · 26,9 · 26,19), nachgetragen. **26,19
  „la terrà ridarà" ist der zweite Beleg desselben Fehlers nach 24,19** („la
  terrà tremerà") — dieselbe Verwechslung von *terra* mit *terrà* zweimal im
  selben Buch.
- **Kapitel 27 hat null Setzfehler** — maschinelle Grossschreibungssuche und
  Handlesung ohne Treffer.
- **Die `Nachtwache`-Klasse fuenfzehnmal in einem Paket** (25: sechs, 26: sechs,
  27: drei). Die schaerfsten: **26,19 `Tau des Lichts`** — WEB *herbs*, RV
  *amanecer*, LSG *vivifiante*, RIV *aurora*, **keine liest „Licht"**; und
  **27,12 `dreschen`**, wo LSG und RIV *schuetteln* lesen.
- **`Sonnensäulen` in 27,9 bestaetigt den Befund aus Paket 7:** WEB „the incense
  altars" und RV „los altares de incienso" widersprechen der Bestandsreihe,
  **LSG „les statues du soleil" und RIV „le colonne solari" stuetzen sie**. Kein
  Befund, die Reihe gilt.
- **LSG 27,13 vertauscht die Attribute der beiden Gruppen** (*exilés* landet auf
  der Assur-Gruppe, die deutsch `Verlorenen` heisst); **RIV deckt sich Feld fuer
  Feld mit dem Deutschen**. Glossiert ist das deutsche Wort.
- **26,16 steht in allen vier Ausgaben in der 3. Person Plural**, wo das Deutsche
  die 1. Person Plural hat. **26,19 lesen drei Ausgaben „meine Leichen"**, nur RV
  folgt dem deutschen „ihre".
- **Versgrenzen: kein Versatz in allen drei Kapiteln.**

## 17. Paket 11 (Kap. 28 · 29 · 30)

Drei Kapitel gleichzeitig, 2112 Einzelwort- und 83 Mehrwort-Eintraege — das
groesste Paket des Buches. Alle Pruefungen je Kapitel sauber; `validate.py 23`,
`qa.py 23` und `hilfsverb.py 23` melden ueber das gebaute Buch **0 Befunde**.
Damit sind **30 von 66 Kapiteln** fertig: 596 Verse, 13 967 Eintraege.

### Zwei Kapitel widersprachen sich bei `taumeln` — und beide hatten recht

Kapitel 29 hat Kapitel 28 als fehlerhaft gemeldet: dort stehe `taumeln`
franzoesisch als *vacillent*, waehrend der Bestand an allen vier Belegen die
*chanceler*-Familie fuehre. Die Meldung war richtig recherchiert und die
Schlussfolgerung trotzdem falsch.

**LSG schreibt in 28,7 dreimal *chancellent* und einmal *vacillent*** — die
Ausgabe weicht an genau diesem Vers selbst aus, weil dort vier Taumelwoerter
zusammenstehen. In 29,9 steht `taumeln` allein, und LSG schreibt *chancellent*.

Beide Kapitel folgen also derselben Regel: **am Kollisionsvers ausweichen, sonst
die Bindung halten.** Dass das Ergebnis verschieden aussieht, ist kein Fehler,
sondern die Regel bei der Arbeit.

**Die Lehre fuer den Wellenabgleich:** eine Divergenzmeldung des Nachbarkapitels
ist ein Hinweis, kein Urteil. Zu pruefen ist nicht, ob die Reihen gleich sind,
sondern **ob jede fuer sich an ihrem Vers gedeckt ist**.

### Sechs Woerter fuer dasselbe Wanken

28,7 ist die dichteste Stelle dieser Art im Buch: `torkeln` (2×), `wanken` (2×),
`taumeln`, `straucheln`, dazu `benommen`. `hints.py` meldete **ein** Paar,
tatsaechlich kollidierten drei — franzoesisch dreifach und italienisch ueber die
Jes-5,27-Zeile von `straucheln` (*vacilla*) gegen `wanken` (*vacillare*).

Geloest nach dem eingefuehrten Verfahren, mit einem neuen Element: `straucheln`
nimmt **nicht** seine buchinterne Zeile aus 5,27, sondern die Bestandsmehrheit
(3:1 *trébucher · inciampare*) — und loest damit die italienische Kollision
gleich mit. **Wo eine buchinterne Vorlage selbst der Ausreisser ihres Lemmas
ist, ist sie keine Vorlage.**

### Die zweite Welle in Folge ohne Angleichung

Wie Paket 9 brauchte auch dieses keine einzige Korrektur durch den Koordinator.
Zwei Faelle sahen danach aus:

- **`taumeln`** (oben) — beide richtig.
- **`Boden`** traegt in 28,2 *terre · terra* und in 30,23 *sol · terreno*, zwei
  gueltige Bestandsreihen in einer Welle, also aeusserlich der `Hüfte`-Fall. Die
  Ausgaben entscheiden ihn glatt: 28,2 ist „zu Boden werfen" und **LSG schreibt
  *en terre*, RIV *a terra***; 30,23 ist der bebaute Boden und **RIV schreibt
  *il suolo***. Der Bestand spaltet die beiden Bedeutungen selbst.

### `sweeplemma.py` im ersten Einsatz

Das in diesem Paket gebaute Werkzeug lief erstmals als Pflichtpruefung. Ergebnis
ueber die drei fertigen Kapitel: **0 · 1 · 1**, und beide Treffer sind
**Fehlalarme, die sich am Vers in einem Satz erledigen**:

- **29,4 `dringen ein`** — das Skript hat den Artikel `eines` („die **eines**
  Totengeistes") als Verbpartikel gelesen.
- **30,5 `bringen Schande`** — `bringt` regiert dort eine vierteilige Objektreihe
  (`Hilfe`, `Vorteil`, `Schande`, `Spott`), nicht die Wendung. Der Agent hatte
  denselben Fall schon selbst geprueft und verworfen.

**Das ist die erwuenschte Fehlalarmrate.** Alle drei Agenten hatten daneben noch
ihre eigenen lemmabasierten Sweeps gebaut und damit zusammen **zehn** echte
Bestands-Mehrwoerter gefunden, die `konvention.py` und `sweep.py` nicht melden —
darunter `wert sein` (29,16), `jemanden in Ruhe lassen` (30,11), `weder ... noch`
(61 Belege), `nur noch` (16 Belege).

**Der lehrreichste Fund ist 30,11:** der Agent hatte `in Ruhe lassen` als *neues*
Lemma gesetzt; der Bestand fuehrt es laengst als `jemanden in Ruhe lassen`
(5Mo 9,14). Ohne den Sweep waere eine fuenfte Lemmaschreibung derselben Sache
entstanden.

**Die Grenze des Werkzeugs, vom Agenten fuer Kapitel 28 benannt:** es findet nur
mehrwortige Lemmata. Getrennte Verbzusaetze, deren Lemma **einwortig** ist
(`zuhören`, `standhalten`, `ausschlagen`, `vorüberziehen`), sieht es
prinzipiell nicht — die fand er beim Lesen. `sweep.py` bleibt dafuer zustaendig.

### `Ariel`: ein Lemma, zwei verschiedene Namen

29,1 nennt Jerusalem fuenfmal `Ariel`. `belegt.py` meldet zwei Belege — und
**einer davon ist gar nicht dasselbe Wort**: in 4Mo 26,17 schreibt das Deutsche
„Ariel", aber alle vier Ausgaben schreiben *Areli · Areli · Areéli · Areli* (der
Gad-Sohn). Esra 8,16 ist ein Mann namens Ariel, alle vier *Ariel*.

An Jes 29,1.2.7 schreiben alle vier *Ariel*, die Reihe faellt also mit Esra 8,16
zusammen und es braucht kein eigenes Lemma. **Der Bestand fuehrt aber zwei
verschiedene Namen unter einem Lemma** — `fixgloss.py show Ariel` mischt sie.
Gemeldet.

### Die Lexikonfalle, neunmal in einem Paket

Der Extrakt zeigt die Korpusmehrheit, und die war neunmal die falsche Lesart:

| Wort | der Extrakt zeigt | am Vers gebraucht wird |
|---|---|---|
| `Menge` (29) | *crowd* (81×, **78 davon NT**) | *multitude* |
| `erklären` (28,9) | *declare* (AT-Bindung) | *explain* — alle vier Ausgaben |
| `Schlachten` (30,32) | *slaughter · matadero* (das Substantiv) | Plural von `Schlacht` = *battles* |
| `Riss` (30,13) | *tear · rotura* (Stoffriss, 2 NT-Belege) | *breach · grieta* (Mauerdurchbruch) |
| `reißend` (30,28) | *ravenous* (vom Wolf, 1Mo 49,27) | *overflowing* (vom Strom) |
| `Trümmer` (30,14) | *ruins* (Gebaeuderuinen) | *fragments* (Tonscherben) |
| `fein` (29,5) | *elegante* (feine Kleidung, Mt 11,8) | *fine · minuta* (feiner Staub) |
| `haltlos` (29,21) | *unprincipled* (von Menschen) | *baseless* (von Gruenden) |
| `Rücken` (30,6) | *back · espalda* (12/13 vom Menschen) | der Eselsruecken |

**Sieben der neun ruhen auf einem oder zwei Belegen.** Eine Bestandsmehrheit ist
nur dann ein Argument, wenn die Belege aus vergleichbaren Kontexten stammen —
und bei einem Einzelbeleg gibt es gar keine Mehrheit, nur einen Zufall.

### Kollisionen: gemeldet 9, gefunden 48

| Kapitel | `hints.py` | selbst gefunden | aufgeloest | widerlegt |
|---|---|---|---|---|
| 28 | 5 | 4 | 7 | 3 |
| 29 | **1** | 9 | 5 | 13 |
| 30 | 4 | **35** | 21 | 14 |

Kapitel 30 hat damit die hoechste Zahl des Buches, und **fast alles sind
Praepositionen und Funktionswoerter** — die Klasse, die `hints.py` ausdruecklich
ausblendet. Die lehrreichsten:

- **30,6/30,20 `Not` ↔ `Bedrängnis`** sind en/es/it **restlos identisch**. `Not`
  hat die harte AT-Bindung (68/76), also weicht `Bedrängnis` auf seine zweite
  belegte Zeile *tribulation* aus — **und RV schreibt in 30,6 selbst „tierra de
  tribulación"**.
- **28,27 `Stock` ↔ `Rute`** en beide *rod*; **WEB trennt selbst** („with a
  stick" / „with a rod").
- **29,16 `wie` ↔ `als` ↔ `so`** — drei Vergleichspartikeln in einem Vers, in
  allen vier Sprachen zusammenfallend. Geloest ueber die Bestandslesart „als ob"
  (Mk 12,40) und die 202-Beleg-Reihe von `so`.
- **28,25 `in` ↔ `an`**: en/it aufgeloest, **spanisch bewusst nicht** — RV
  schreibt an dieser Stelle selbst zweimal *en*. Dasselbe Muster wie `stehe`/`bin`
  in 21,8 und `am`/`im` in 28,21.

### Neue Lemmata

**Kapitel 28** (17): `Hagelsturm` C1 · `verheerend` C1 · `Frühfeige` C1 ·
`torkeln` C1 · `benommen` B2 · `Kleinkind` A2 · `stammelnd` C1 · `Müder` A2 ·
`Pakt` B2 · `Perazim` A1 · `befremdlich` C1 · `fremdartig` C1 · `eggen` C1 ·
`Dinkel` C1 · Mehrwort `umbrechen` B2 · `morgens um morgens` A2 ·
`sich einwickeln` B1.

**Kapitel 29** (13): `Kreislauf` B2 · `aufwerfen` C1 · `wispern` C1 ·
`Nachtgesicht` C1 · `sich blenden` B2 · `angelernt` C1 · `Gebilde` C1 ·
`Former` C1 · `Fruchtgarten` B2 · `erbleichen` C1 · `Verwirrter` B2 ·
`Murrender` C1 · Mehrwort `sich belehren lassen` B2.

**Kapitel 30** (20): `Hanes` A1 · `Feuerschlange` C1 · `Höcker` C1 ·
`stillsitzen` C1 · `Schmeichelhaftes` C1 · `prophezeien` B2 · `auswölben` C1 ·
`Fahnenstange` C1 · `Lappen` B2 · `Überzug` B2 · `nahrhaft` B2 · `Wurfgabel` C1 ·
`Blutbad` C1 · `Bruch` B2 · `Sieb` B2 · `irreführend` C1 · `Niederschlag` C1 ·
`Gewitter` B2 · `Strafrute` C1 · `Scheiterhaufen` C1.

`befremdlich` und `fremdartig` mussten **spanisch** getrennt werden — RV schreibt
in 28,21 zweimal „extraña".

### Vorlagen, die hier entstanden sind

Drei Kapitel dieses Pakets liefern Zeilen fuer noch nicht annotierte Kapitel, und
alle drei Agenten haben sie ausdruecklich gemeldet:

- **29,17 `Fruchtgarten` B2 → 32,15.** Die Ausgaben stehen 2:2 (WEB *fruitful
  field*, RV *campo fértil* gegen LSG *verger*, RIV *frutteto*); nach dem
  `Sonnenstadt`-Verfahren entscheidet das deutsche Wort — ein Garten, kein Feld.
- **30,15 → 52,4**, die Formel „Denn so spricht der Herr, der HERR" (7 Tokens).
- **30,29 → 66,14**, „euer Herz wird sich freuen" (5 Tokens).

### Prompt-Hinweise: einundvierzig widerlegt

Kapitel 28 vierzehn, Kapitel 29 vierzehn, Kapitel 30 dreizehn. Die lehrreichsten:

| ich schrieb | der Text sagt |
|---|---|
| `starkes Getränk` sei evtl. ein Bestands-Mehrwort | **fuehrt keins** — alle vier Belege Wort fuer Wort |
| `mit Füßen zertreten` (28,3) sei ein Kandidat | Bestandslemma ist `mit Füßen **treten**`; hier steht `zertreten`, und ein Mehrwort haette es/it dieselbe Glosse **doppelt** gesetzt |
| `um zu` sei Kandidat in 28,20 und 29 | **28,20 hat kein freies `zu`** („um sich **auszu**strecken"); **29 hat gar kein `um … zu`** |
| 30,16 `fliehen` stehe dreimal | **zweimal** |
| „30,2 ↔ 30,3 sind eine Dublette" | 30,2 hat `Macht des Pharao`, 30,3 `Schutz des Pharao` — **verschiedene Woerter** |
| `werden ↔ ziehen` (30,29) sei eine Kollision | **keine** — verschiedene Person und Numerus |
| 29,13 aus Mt 15,8 uebernehmen | **`sich nahen` (Mt) ≠ `sich nähern` (Jes)** — anderes Lemma |
| 29,22 ← 1Sam 2,30, „5 Tokens" | **nur 4 tragen** — 1Sam setzt „der **Gott** Israels" fort, Jes „der Abraham erlöst hat"; genau die Position, an der Abschreiben falsch glossiert haette |
| `für immer` sei Mehrwort-Kandidat in 30,8 | der Bestand **schachtelt nicht**: in `für immer und ewig` steht kein `für immer` darin |
| zwoelf Formen seien unbelegt | **alle belegt** — darunter `einstürzen`, `zertrümmern`, `Schaufel`, `worfeln`, `herrichten` |

**Von 101 als unbelegt gemeldeten Formen waren 39 wirklich neu.**

### Ausgabenbefunde

- **Sieben neue RIV-Setzfehler** (28,5 · 28,16 · 28,18 · 29,12 · 30,8 · 30,22 ·
  30,30), nachgetragen. **29,12 ist besonders klar:** „**l** quale" gegen „il
  quale" in 29,11 — dieselbe Ausgabe, ein Vers weiter, richtig.
- **Der zweite Setzfehler in WEB:** 30,14 „among the **broken piece** a piece
  good enough" (*pieces*), nach 24,17.
- **Eine neue Klasse, die gar kein Setzfehler ist:** RIV 29,9 enthaelt zweimal
  das **rohe Byte 0x85** — das Windows-1252-Zeichen fuer „…", beim Import nicht
  dekodiert. Nachgezaehlt: **46 Vorkommen in 13 italienischen Buechern**. Das
  betrifft den Bibeltext, den die App anzeigt, nicht die Annotation; als eigene
  Aufgabe abgelegt.
- **Die `Nachtwache`-Klasse dreizehnmal.** Die schaerfsten: **28,16 „gerät nicht
  in Panik"** (alle vier lesen „wird nicht eilen/wanken"), **30,33
  `Scheiterhaufen`** (alle vier lesen „Tofet"), **30,9 `Weisung`** (alle vier
  „Gesetz"), **30,28 `Maul`** (alle vier „Kiefer").
- **28,18 `gelöst` folgt den Ausgaben, nicht dem Bestand** — nach dem
  `abbrechen`-Praezedenzfall aus Paket 10: der Bestand fuehrt fuer `lösen` nur
  „losbinden" (4+4 Belege, **keine Bindung**), alle vier Ausgaben lesen
  „annulliert". Dasselbe bei **28,27/28 `Wagenrad`**, wo die einzige
  Bestandsreihe den Streitwagen nennt und alle vier den Bauernwagen lesen.
- **`Dreschschlitten` nennt fr/it das falsche Geraet** (*herse* / *erpice* =
  Egge). Beide Belegverse sind ungedeckt, und **Hiob 41,22 ist ein
  Versgrenzen-Versatz** — dort steht in allen vier Ausgaben anderer Text. Zu
  duenn fuer `remap.py`; in 28,27 den Ausgaben gefolgt.
- **`Ohr` italienisch weiter gespalten** (42 *orecchi* : 8 *orecchie*), jetzt mit
  einer Gegenstelle in der Ausgabe: **RIV 30,21 schreibt „le tue orecchie"**.
  Der bekannte offene Befund.
- **Versgrenzen: kein Versatz in allen drei Kapiteln.** RIV verschiebt allerdings
  die **Satzgrenze 28,12/13**: „Doch sie wollten nicht hören" steht dort am
  Anfang von v13.
