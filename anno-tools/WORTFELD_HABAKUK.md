# Wortfeld Habakuk (Buch 35)

Ein Paket, drei Kapitel, ein Agent je Kapitel.
56 Verse, **1303 Einzelwort- und 97 Mehrwort-Eintraege**.

`selfcheck`, `konvention`, `levelcheck`, `validate`, `qa`, `hilfsverb`
alle **0**; `glosskollision` **0 inhaltliche Paare in Kapitel 1 und 3**,
in Kapitel 2 genau eine (begruendet); `paketcheck` Abschnitt A leer;
Level ueber alle drei Kapitel einheitlich; die Wiederholungs- **und** die
Reihen-Gegenrechnung **ohne einen einzigen Befund**.

## 0 · Verszaehlung

**Keine Abweichung.** Alle vier Ausgaben decken sich Vers fuer Vers,
Versatz +0 in allen drei Kapiteln — `ausgaben.py` meldet es ohne Warnung.
Das erste der letzten fuenf Buecher ohne Kapitelgrenzen-Verschiebung.

## 1 · `Last` in 1,1 — die Bindung aus Nahum traegt

Alle vier Ausgaben lesen „Oracle / Profecía / Oracle / Oracolo". Der
Bestand annotiert das prophetische *massa* aber als **`Last` B1
*burden · carga · charge · peso*** (Jeremia 23,33–38, Hesekiel 12,10),
und **Nahum 1,1 hat den Satz Wort fuer Wort ebenso**. Token fuer Token
uebernommen, samt `geschaut` nach Amos 1,1 (*beheld · contemplado ·
contemplé · contemplato*).

Der `l1912mod` schreibt in Jesaja 13,1, Sacharja 9,1 und Maleachi 1,1
`Ausspruch` — nur in Nahum und Habakuk `Last`. Zwei der drei
`Ausspruch`-Stellen (Sacharja, Maleachi) stehen noch aus.

## 2 · 2,4 ist im Neuen Testament zitiert — und weicht ab

```
    Habakuk 2,4   „…der Gerechte aber wird durch seine TREUE leben."
    Römer 1,17    „Der Gerechte wird durch seinen GLAUBEN leben."
    (ebenso Galater 3,11 und Hebräer 10,38)
```

**Der modernisierte Text unterscheidet die beiden Woerter.** `Treue` B2
*faithfulness · fidelidad · fidélité · fedeltà* — nicht `Glaube`. Der
Vier-Token-Block aus Hebr 10,38 (`Gerechte aber wird durch`) ist
uebernommen, `den Glauben` gerade nicht.

Derselbe Fall wie Joel 3,1 gegen Apostelgeschichte 2,17: **eine Vorlage
belegt nicht, dass sie hierher passt.**

## 3 · Kapitel 3 ist ein Psalm — mit einem Hapax in der Ueberschrift

```
3,1   „Ein Gebet des Propheten Habakuk, nach der Weise der Klagelieder."
3,3 · 3,9 · 3,13   `Sela`
3,19  „Fuer den Chorleiter, mit Saitenspiel."
```

`Sela` und `Saitenspiel` stehen im Psalter und wurden woertlich
uebernommen. **`Chorleiter` nicht:** der Psalter schreibt durchgehend
**`Vorsaenger`** (54× C1 *chief musician · músico principal · chef des
chantres · capo dei musici*), und `Chorleiter` steht im ganzen
`l1912mod` **genau einmal** — hier. Neu gepraegt als C1 *choir director ·
director del coro · chef de chœur · direttore del coro*, weil es ein
anderes deutsches Wort mit durchsichtiger Zusammensetzung ist und die
vier Ausgaben selbst „music director / director del coro / Capo de
Musici" lesen.

`parallelen.py` meldet fuer fast jeden Vers eine Psalmenvorlage; die
staerkste ist **3,19 ← Psalm 18,34** (Aehnlichkeit 0,55).

## 4 · Drei Erschuetterungsverben in einem Vers

**3,16** haeuft sie: `erbebte` (Leib) · `zitterten` (Lippen) ·
`schlotterten` (Knie). Nahum 2,11 hatte `schlottern` gegen `zittern`
schon aufgeloest — **hier reicht das nicht**, weil `erbeben` dazukommt
und im Spanischen die *estremecer*-Familie besetzt:

```
erbeben    C1  shook · se estremeció · frémit · sussultò
zittern    B1  trembled · temblaron · tremblèrent · tremarono
schlottern C1  knocked together · vacilaron · chancelèrent · vacillarono
```

Die spanische Spalte von `schlottern` weicht damit **verslokal** von der
Nahum-Reihe ab. Gemeldet, begruendet, kein Widerspruch: eine Auflösung
gilt im Kollisionsvers.

**`schlottern` ist C1, nicht B2** — `WORTFELD_NAHUM.md` schrieb B2, der
einzige Bestandsbeleg traegt C1. Berichtigt.

## 5 · Aufgeloeste Kollisionen (Auswahl)

| Vers | Paar | Auflösung |
|---|---|---|
| 1,13 | `ansehen` / `zuschauen` / `zusehen` — **drei** Verben des Sehens, in fr alle *regarder* | *look at* / *look on* / *watch*; `zuschauen` ist im Bestand unbelegt und wurde neu gepraegt |
| 1,11 | `ziehen` ↔ `fahren` | `zieht` auf *passes · pasa · passe · passa* (Hiob 30,15) |
| 1,11 | `weiter` ↔ `fort` | **von `hints.py` nicht gemeldet**; `weiter` → *further · más adelante · plus loin · oltre* |
| 1,12 | `bestimmen` ↔ `einsetzen` | *appointed* gegen *established* — beides Bestandslesarten, WEB liest genauso |
| 2,16 | `Schande` ↔ `Schmach` | das schwaecher gebundene `Schmach` (27:14) weicht auf *reproach · oprobio · outrage · oltraggio*. **Die Ausgaben verteilen es umgekehrt** — die Bestandsbindung hat Vorrang |
| 2,5 | `raffen` ↔ `sammeln` | **von keinem Werkzeug gemeldet**; `raffen` auf *carries off · se lleva · emporte · rapisce*. In 2,9 (kollisionsfrei) traegt es wieder die Normalreihe |
| 3,8 | `Fluss` ↔ `Strom` (alle vier gleich) | `Strom` auf *streams · corrientes · courants · correnti* |
| 3,11 | `Lichtglanz` ↔ `Glanz` | **nicht gemeldet**; `Lichtglanz` neu als *radiance · fulgor · rayonnement · fulgore* |
| 3,13 | `Grund` ↔ `Fundament` | `Grund` auf *bottom · fondo · fond · fondo*, nicht die foundation-Lesart |

**Bewusst stehen gelassen:** 2,18 `geschnitztes`/`geschnitzt` — figura
etymologica („ein geschnitztes Bild, das sein Bildhauer geschnitzt hat"),
und **alle vier Ausgaben wiederholen das Wort ebenso**. Dazu die
romanischen Artikel-gegen-Klitikon-Paare und die `um zu`-Konvention.

## 6 · Lexikonfallen

```
Beute (1,8)      prey · presa · proie · preda    — NICHT *spoil* (74:28);
                 das Raubtierbild, nicht die Kriegsbeute. Amos hat es benannt.
Kraft (1,11)     strength · fuerza · force · forza — NICHT power/poder
Garn (1,15·1,16) dragnet · malla · rets · giacchio — der einzige Bestandsbeleg
                 (2Mo 35,25) ist SPINNgarn, hier ist es das Fischernetz
üppig (1,16)     rich · abundante · succulente · succulento — der Bestand
                 kennt nur den Pflanzenwuchs
Wachtposten (2,1) NICHT `Wachposten` (8× *garrison*) — das ist die Garnison
verwirken (2,10)  NICHT `verwirren`. Alle vier Ausgaben lesen „sinned",
                 der deutsche Text „verwirkt" — dem Deutschen gefolgt
Weh (2,6 ff.)    der Text schreibt `Weh`, nicht `Wehe` — der Bestand fuehrt
                 BEIDE als eigene Lemmata (`wehe` B2, `Weh` C1)
Galt (3,8)       kein neues Lemma: `gelten` hat 94 Belege. Neu ist nur die
                 LESART (gelten + Dativ = „sich richten gegen")
Chorleiter (3,19) s. Abschnitt 3
```

## 7 · Befunde in den Ausgaben

**RIV 1,10** liest „si ridono di tutte le fortezze; **mmontano** un po'
di terra" — richtig *ammontano*. **Der Fall erweitert das Anlautmuster
gleich zweifach:** die Haeufigkeitsprobe traegt nicht (beide Formen
stehen 1×), und vor dem Wort steht **kein kurzes Vorwort, sondern ein
Semikolon**. `RIV_ANLAUTFEHLER.md`.

**RIV und LSG lesen `Habacuc`**, nicht `Abacuc`/`Habakuk` — eine fruehere
Fassung des Prompts hatte beides behauptet und einen RIV-Anlautfehler
vermutet, wo keiner ist. Nur WEB weicht ab (*Habakkuk*).

**Alle vier Ausgaben lesen 2,5 anders als der deutsche Text**: sie machen
den Wein zum Praedikat, der `l1912mod` zum Subjekt. Und in **1,5 · 1,17**
lesen alle vier „nations", der deutsche Text `Voelker`. Beides
wahrscheinlich der eklektische Schlachter-Zweig
(`BEFUND_TEXTGRUNDLAGE.md`) — dem Deutschen gefolgt.

## 8 · Fuer die Nachbarbuecher

```
Last B1 burden·carga·charge·peso              (= Nahum 1,1)
Habakuk A1 Habakkuk·Habacuc·Habacuc·Habacuc
Treue B2 faithfulness·fidelidad·fidélité·fedeltà   — NICHT Glaube
Gerechter B2 righteous one·justo·juste·giusto · Frevler C1 wicked one·malvado·méchant·empio
Kraft A2 strength·fuerza·force·forza  ·  Macht B1 power·poder·pouvoir·potere
Beute B2 prey·presa·proie·preda  ·  Netz B1 net·red·filet·rete
Garn B2 dragnet·malla·rets·giacchio
Weh C1 Woe·Ay·Malheur·Guai   ·  MW wehe jemandem B2 Woe to him·Ay de aquel·…
Wachtposten B2 watch post·puesto de guardia·poste de garde·posto di guardia
Zinne C1 pinnacle·almena·créneau·merlo · Offenbarung B2 revelation·revelación·révélation·rivelazione
Schande B2 disgrace·afrenta·honte·vergogna ≠ Schmach C1 reproach·oprobio·outrage·oltraggio
Totenreich C1 realm of the dead·reino de los muertos·séjour des morts·regno dei morti
Chorleiter C1 choir director·…  ≠  Vorsänger C1 chief musician·… (Psalter)
Lichtglanz C1 radiance·fulgor·rayonnement·fulgore ≠ Glanz B2 brightness·resplandor·éclat·splendore
Strom B2 streams·corrientes·courants·correnti ≠ Fluss A2 rivers·ríos·fleuves·fiumi
schlottern C1 · zittern B1 · erbeben C1 · erzittern C1 — vier Erschuetterungsverben
Kuschan A1 of Cushan·de Cusán·de Cuschan·di Cusan   ≠ Kusch (NICHT gleichsetzen)
Chaldäer B2 Chaldeans·caldeos·Chaldéens·Caldei
Zorn B2 wrath·ira·colère·ira ≠ Grimm C2 fury·furor·fureur·furore  (in 3,8 und 3,12 zusammen)
Sela · Saitenspiel — woertlich aus dem Psalter
```
