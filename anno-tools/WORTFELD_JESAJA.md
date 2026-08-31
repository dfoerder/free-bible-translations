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
