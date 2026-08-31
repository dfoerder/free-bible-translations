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

## 2. Die Leitformel: `Heerscharen` — 60 Verse, im Bestand UNBELEGT

„Der HERR der Heerscharen" ist die Signaturformel Jesajas und steht in
**60 Versen**, verteilt ueber das ganze Buch (Kap. 19 siebenmal, 10 und 22 je
fuenfmal, 5 und 14 je viermal). `fixgloss.py show Heerscharen` findet **nichts**.

**Alle vier Ausgaben sind sich einig** (geprueft an 1,9):
*Armies · ejércitos · armées · eserciti*.

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
