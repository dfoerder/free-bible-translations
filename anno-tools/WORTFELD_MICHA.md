# Wortfeld Micha (Buch 33)

Zwei Pakete (Kapitel 1–4 und 5–7), ein Agent je Kapitel.
7 Kapitel, 105 Verse, **2630 Einzelwort- und 128 Mehrwort-Eintraege**.

`selfcheck`, `konvention`, `levelcheck`, `sweeplemma`, `kongruenz`,
`hilfsverb`, `validate`, `qa` alle **0**; `glosskollision` **0 inhaltliche
Paare in allen sieben Kapiteln**; `paketcheck` Abschnitt A in beiden
Paketen leer; Level ueber alle sieben Kapitel einheitlich. Die
Wiederholungs-Gegenrechnung meldet ueber das ganze Buch **genau eine**
Wortfolge — und die ist begruendet.

## 0 · Verszaehlung: die Grenze zwischen Kapitel 4 und 5

```
                Kap 4   Kap 5
    deutsch       14      14
    WEB           13      15
    RV1909mod     13      15
    LSG           14      14   ← als einzige deckungsgleich
    RIV           13      15
```

**Der deutsche Vers 4,14 ist in WEB, RV und RIV deren 5,1.** Danach laeuft
Kapitel 5 dort um einen Vers versetzt. **RIV druckt die Doppelzaehlung in
jeden Vers des Kapitels** — `(5:1)` … `(5:14)`.

`ausgaben.py` wandte fuer Kapitel 4 faelschlich Versatz −1 an **und warnte
selbst**, dass +0 besser liegt. Fuer die Kapitel 5, 6 und 7 rechnete es
richtig und ohne Warnung. **Die Warnung lesen, nicht die Zahl.**

## 1 · Der Name des Propheten steht falsch in der Bindungstabelle

`BINDUNGEN_AT.md` gab fuer `Micha` die Mehrheitsreihe
*Micah · Micaías · Mica · Mica* (32 von 60 Belegen). **Das ist der Micha
aus Richter 17 und der Michaja aus 1. Koenige 22.**

Der **Prophet** steht im Bestand genau einmal — **Jeremia 26,18** — als
*Micah · **Miqueas** · **Michée** · **Michea***, und alle vier Ausgaben
lesen ihn in Micha 1,1 genau so. Ein Homographenfall: derselbe deutsche
Name fuer zwei Personen, mit verschiedenen Schreibungen in den
Zielsprachen. **Die Tabelle traegt jetzt die Warnung.**

Gefunden vom Agenten fuer Kapitel 1, der die Tabelle nicht uebernommen,
sondern am Vers geprueft hat.

## 2 · Die n-Gramm-Bindungen — dreimal lief eine ueber eine Grenze

Das Buch hat sechs wiederholte Wortfolgen. **Drei der gemeldeten Bloecke
trugen nicht**, und jedes Mal aus demselben Grund:

```
2,8 · 3,2   „Ihr reisst den Leuten die"      — 5 Tokens gemeldet, 4 tragen
              das fuenfte `die` ist in 2,8 Relativpronomen („die arglos
              voruebergehen"), in 3,2 Artikel („die Haut").
              Von den Agenten fuer 2 UND 3 unabhaengig gefunden.
5,1 ← Jes 51,9  „der Vorzeit in den"         — laeuft ueber eine
              Konstruktionsgrenze: dort ist `der` das Genitiv-*of*,
              hier der Artikel im Dativ.
1,8 ← Jer 49,12 (Obadja-Fall, im Nachbarbuch) — ueber eine Kommagrenze.
```

**Die n-Gramm-Gegenrechnung kennt weder Satz- noch Konstruktionsgrenzen.**
Das ist ihre systematische Schwaeche; sie liefert Verdachtsfaelle, keine
Vorlagen. Die Agenten fangen sie inzwischen zuverlaessig ab.

Die Bindungen, die **tragen**:

```
3,1 · 3,9    „doch ihr Haeupter im Haus Jakob und ihr Anfuehrer im Haus
              Israel"  — 12 Tokens, laengste Wiederholung, positionsgleich
4,6 · 5,9    „An jenem Tag spricht der HERR werde ich"  — 8 Tokens,
              ueber die Paketgrenze
1,1 · 4,2    „das Wort des HERRN"             — 4 Tokens
5,4 · 5,5    „in unser Land einfaellt und unsere"  — 6 Tokens
2,13         „zieht vor ihnen her"            — zweimal im selben Vers
7,6 ← Mt 10,36  „Die eigenen Hausgenossen werden zu Feinden" — 6 Tokens,
              das NT-Zitat, Token fuer Token uebernommen
```

## 3 · Aufgeloeste Kollisionen (Auswahl)

| Vers | Paar | Auflösung |
|---|---|---|
| 2,8 | `Leute` ↔ `Volk` | `Leute` auf *folk · gente · gens · gente*. **In 3,2 steht kein `Volk` — dort gilt die Bestandsreihe.** Eine Auflösung ist verslokal, keine Buchregel |
| 2,2 | `Mann` ↔ `Mensch` | von `hints.py` nicht gemeldet, aber echt: beide Bestandsmehrheiten sind *man·hombre·homme·uomo*. `Mensch` auf *human being · ser humano · être humain · essere umano* |
| 3,8 | `Kraft` ↔ `Stärke` | ohne Eingriff kollidieren sie **englisch und franzoesisch** (*strength*/*force*). `Kraft` weicht auf *power · poder · puissance · potenza* — **WEB liest dort selbst „full of power"**. In 5,3, wo `Kraft` allein steht, gilt wieder die AT-Bindung *strength* |
| 3,7 | `beschämt` ↔ `blamieren` | **nur Spanisch** weicht: `blamiert` → *confundidos*, genau wie RV im Vers selbst |
| 5,6 | `warten` ↔ `hoffen` | auf der **hoffen**-Seite geloest (es *confía*), weil `warten` dreimal im Buch steht und `hoffen` nur hier |
| 5,6 | `niemanden` ↔ `Menschen` | nicht gemeldet, aber echt (fr *personne*). Deshalb wurde der Lukas-18,2-Block an genau diesem Token **nicht** uebernommen |
| 6,3 | `machen` ↔ `tun` | `gemacht` auf *made · vuelto · rendu · reso* |
| 6,15 | `pressen` ↔ `keltern` | `hints.py` konnte es nicht melden, weil `keltern` formseitig unbelegt ist |
| 7,18 | `erlassen` ↔ `vergeben` | `erlassen` auf *remits · condona · remet · condona* |
| 7,5 | `trauen` ↔ `sich verlassen auf` | `sich verlassen auf` auf die *apoyarse/appuyer*-Lesart |
| 7,10 | `sehen` ↔ `ansehen` | `ansehen` auf *look at · mirar · regarder · guardare* |

**`HERR` gegen `Herr` in 1,2 und 4,13 wird NICHT aufgeloest** — der
Bestand haelt die beiden in 19 Versen einstimmig allein ueber die
Grossschreibung auseinander (Amos-Befund).

## 4 · Lexikonfallen, die die Bestandsmehrheit stellt

```
höchster (4,1)   NICHT `Höchster` B2 (Gottestitel) — Superlativ zu hoch
abziehen (3,3)   NICHT der militaerische Abzug (15 von 22) — 3Mo 1,6
                 „die Haut abziehen" ist die richtige Lesart
krümmen (3,9)    NICHT physisch — „das Recht beugen", alle vier Ausgaben
einfallen (5,4)  NICHT *comes to mind* (der einzige Beleg, Mt 5,23) —
                 militaerisch
aufstellen (5,4) NICHT *set up* — die militaerische Lesart Jer 50,9
einkehren (4,8)  NICHT *turn in/loger* — hier kehrt die Herrschaft zurueck
gezückt (5,5)    ist ein EIGENES Lemma (8 Belege), nicht Form von `zücken`
Traut (7,5)      ist belegt — als kleingeschriebenes `traut` (7 Belege)
Hecke (7,4)      darf NICHT *buisson d'épines* heissen: das ist im selben
                 Vers die Reihe von `Dornstrauch`
zerlegen (3,3)   ist KEINE Falle — der einzige Beleg ist schon die
                 Schlachtlesart (eine Prompt-Behauptung, die nicht traf)
```

## 5 · Befunde ausserhalb der Glossen

**Die Textgrundlage.** `l1912mod` folgt in 6,9 und 6,16 woertlich der
**Schlachter 1951**, nicht der Luther 1912. Die Messung ueber alle 23 212
AT-Verse: 3960 stehen naeher an Luther, **3514 naeher an Schlachter**.
Der Text ist eklektisch. Das erklaert, warum in 6,16 alle vier Ausgaben
„meines Volkes" lesen und der deutsche Text „der Voelker".
Vollstaendig in `BEFUND_TEXTGRUNDLAGE.md`.

**Jeremia 26,18** — die woertliche Parallele zu Micha 3,12 — traegt einen
italienischen Artikel im falschen Genus (`la` vor dem maskulinen *monte
del tempio*; franzoesisch ist `la montagne` richtig). Der Agent hat den
Block uebernommen und den Fehler **nicht** mituebernommen.
`NACHLESE_BESTAND.md` 8a.

**Micha 2,11 schrieb `Bier`** — das Wort stand genau einmal im ganzen
deutschen Korpus, waehrend dasselbe hebraeische Wort sonst 16× als
„starke(s) Getraenk" oder „Rauschtrank" modernisiert ist. Damals nicht
geaendert, weil eine Quelltextkorrektur eine andere Entscheidung ist
als eine Glossenkorrektur.

**Inzwischen korrigiert:** der Vers liest „Ich predige euch Wein und
starkes Getraenk!". Der Vers wurde dadurch um ein Token laenger, die
Glossen sind umpositioniert; `stark` A1 und `Getraenk` A2 nach den
Vorlagen 3. Mose 10,9 und Sprueche 20,1. `NACHLESE_BESTAND.md` 12.

## 6 · Sieben RIV-Defekte in einem Buch — drei Klassen

```
Anlautverlust hinter kurzem Wort   1,1 `zechia` · 1,9 `erusalemme` ·
                                   1,13 `ion` · 4,1 `onti` · 4,6 `uelle`
ein ganzes Wort fehlt              4,11 `occhi` („E i nostri si pascan")
ein falsches echtes Wort           1,10 „in Gad" statt Gath
                                   6,10 `c'è` statt `ch'è`
```

**Nur die erste Klasse findet eine Haeufigkeitsprobe.** `Gad` ist
korpusweit 80× ein echter Name, `c'è` 118× eine echte Form — beide fallen
nur im Vergleich mit den anderen Ausgaben oder im Kontext auf.
`RIV_ANLAUTFEHLER.md`.

Dazu der schon bekannte **7,17 `erranno` → *verranno***, vom Agenten
korpusweit nachgezaehlt und bestaetigt (2 Belege, beide Defekte).

## 7 · Fuer die Nachbarbuecher

```
Micha A1 Micah·Miqueas·Michée·Michea   (NICHT die Bindungstabelle)
Moreschet A1 · Marescha A1 Mareshah·Maresa·Maréscha·Maresha
   (der Bestand schreibt die Stadt `Maresa` — Schreibungsdublette im
    l1912mod selbst, gemeldet, nicht vereinheitlicht)
Gebirge B2 highlands·serranía·massif·massiccio ≠ Berg A1 mountain·monte·montagne·monte
Haupt C1 heads·cabezas·têtes·teste  ≠  Anfuehrer B2 leaders·jefes·chefs·capi
Recht B1 justice·derecho·droit·diritto · Gerechtigkeit B2 righteousness·justicia·justice·giustizia
   üben B1 practice·practicar·pratiquer·praticare — `Recht üben` ist KEIN Mehrwort
Streit B2 dispute·disputa·dispute·disputa ≠ Rechtsstreit C1 ≠ Gericht B2 judgment·juicio·jugement·giudizio
Kraft A2 strength·fuerza·force·forza (AT-Bindung 148:96) ≠ Stärke B1 strength·fortaleza·force·forza
Volk B1 people·pueblo·peuple·popolo · Nation B1 nations·naciones·nations·nazioni
Rest B1 remnant·remanente·reste·resto · Heerschar C1 hosts·ejércitos·armées·eserciti
Zion A1 · Tochter A1 daughter·hija·fille·figlia · Assur A1 Assyria·Asiria·Assyrie·Assiria
Neu gepraegt: Herdenturm C1 · Augenlust C1 · Kriegerin B2 woman warrior·guerrera·guerrière·guerriera
   Hinkender B2 · knapp B2 scant·escasa·petite·scarsa · beiseiteschaffen B2
   Prediger B2 (Appellativ, neben der Buchtitel-Reihe)
   Feindin B2 · Treuer B2 · Bester B1 · Ehrlichster B2 · Hecke B1 hedge·seto·haie·siepe
   Wegkreuzung B2 · Ruhestatt C1 · Morgenlicht B2 · daherkommen B2 · zusammenfuehren B2
   Streit fuehren B2 · ausschauen nach B2 · weiden lassen B2 · Weh mir B2
```
