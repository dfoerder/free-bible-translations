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
