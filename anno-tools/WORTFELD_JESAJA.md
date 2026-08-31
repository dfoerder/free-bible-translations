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
