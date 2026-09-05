# Wortfeld Nahum (Buch 34)

Ein Paket, drei Kapitel, ein Agent je Kapitel.
47 Verse, **1029 Einzelwort- und 50 Mehrwort-Eintraege**.

`selfcheck`, `konvention`, `levelcheck`, `sweeplemma`, `artikel`,
`hilfsverb`, `validate`, `qa` alle **0**; `glosskollision` **0 inhaltliche
Paare in allen drei Kapiteln**; die Wiederholungs-Gegenrechnung und die
Reihen-Gegenrechnung ueber das ganze Buch **ohne einen einzigen Befund**;
Level einheitlich.

## 0 · Verszaehlung: die Grenze zwischen Kapitel 1 und 2

```
                Kap 1   Kap 2   Kap 3
    deutsch       14      14      19
    WEB           15      13      19
    RV1909mod     15      13      19
    LSG           14      14      19   ← als einzige deckungsgleich
    RIV           15      13      19
```

**Der deutsche Vers 2,1 ist in WEB, RV und RIV der Vers 1,15.** Danach
laeuft Kapitel 2 dort um einen Vers versetzt.

**Das ist das dritte Buch in Folge, in dem LSG die einzige deckungsgleiche
Ausgabe ist** — nach Jona und Micha. Wo ein Zeuge fuer die Versgrenze
gebraucht wird, ist sie die verlaessliche.

**`ausgaben.py` rechnete zum dritten Mal falsch** (nach Jona 1 und
Micha 4): es wandte Versatz +1 an, weil der Zusatzvers **hinten** haengt,
und warnte selbst, dass +0 besser liegt. Der Code erklaert das Verhalten
ausdruecklich — er tauscht den Versatz nicht stillschweigend aus, sondern
meldet den Zweifel. **Die Warnung lesen, nicht die Zahl.** Alle drei
Agenten haben es richtig gemacht.

## 1 · Die einzige Wiederholung des Buches

    2,14 · 3,5   „komme ich ueber dich, spricht der HERR der
                  Heerscharen. Ich…"                    10 Tokens

`ch2.json` lag noch nicht vor, als Kapitel 3 an die Stelle kam. **Beide
Agenten haben unabhaengig entschieden und danach verglichen: Token fuer
Token identisch.** In 2,14 beginnt der Block bei pos 2 („Nun **aber**
komme ich"), in 3,5 bei pos 1 — positionsweise verschoben, inhaltlich
gleich.

`spricht` steht **nachgestellt** → fr *dit*. Der Agent fuer Kapitel 2 hat
dazu die Parallelstelle **2. Samuel 7,8** geprueft: dieselben sechs
Tokens, dort aber **vorangestellt**, also mit fr *parle*. **Der Block ist
nicht Token fuer Token uebernehmbar** — der vierte Fall einer Bindung,
die ueber eine Konstruktionsgrenze laeuft.

## 2 · Lesart-Entscheidungen gegen die Ausgaben

**`Last` (1,1) = *burden · carga · charge · peso***, nicht *oracle*. Alle
vier Ausgaben lesen „Oracle/Profecía/Oracle/Oracolo", aber der Bestand
annotiert das prophetische *massa* an den vergleichbaren Stellen
(Jer 23,33–38, Hes 12,10) als `Last` B1. **Habakuk 1,1 hat denselben
Satzbau und bekommt dieselbe Reihe.**

Ein Randbefund dazu: der l1912mod schreibt in **Jes 13,1, Sach 9,1 und
Mal 1,1 `Ausspruch`**, nur in **Nahum und Habakuk `Last`** — drei der
fuenf Stellen sind noch nicht annotiert.

**`Kraft` (1,3) = *strength · fuerza · force · forza***, obwohl WEB
*power* und RV *poder* lesen. `BINDUNGEN_AT.md` fuehrt `Kraft`
ausdruecklich als Lexikonfalle (AT 124/147 *strength*, NT-Mehrheit
*power*).

**`Pracht` (2,3)**: alle vier Ausgaben lesen *excellency/gloria/gloire/
gloria*, der Bestand bindet 29:3 auf *splendor · esplendor · splendeur ·
splendore*. Bestand genommen — die Ester-Faustregel: die Ausgabe liefert
den Namen, der Bestand die Bedeutung.

**`Kusch` (3,9)**: WEB schreibt „Cush", der Bestand fuehrt 14× *Ethiopia ·
Etiopía · Éthiopie · Etiopia* (nur 1× *Cush*). Bestand genommen.

**`Ziegelform` (3,14)**: alle vier Ausgaben lesen den **Brennofen**, der
deutsche Text die **Form**. Dem Deutschen gefolgt — vermutlich ein Fall
der eklektischen Vorlage (`BEFUND_TEXTGRUNDLAGE.md`).

**`Nahums` italienisch *di Nahum*, nicht *di Naum***. Der Bestandsbeleg
(Lk 3,25) ist ein **anderer Mensch** — ein Ahne Jesu. RIV selbst schreibt
in Nahum 1,1 „Nahum". Beim Namen entscheidet die Ausgabe.

## 3 · Aufgeloeste Kollisionen

| Vers | Paar | Auflösung |
|---|---|---|
| 1,4 | vier Trockenheitsverben: `austrocknen`/`versiegen`/`verwelken`/`verdorren` | in ihren Bestandsreihen fallen sie in en/es/fr **paarweise** zusammen. Ausgewichen ist die Mehrwortglosse von `austrocknen` (fr *s'assèche*, belegt); `verdorren` behaelt seine Bindung |
| 1,6 | `bestehen` ↔ `standhalten` | fr *subsister* gegen *tient bon* |
| 1,13 | `zerbrechen` ↔ `zerreissen` | es *rompo*/*rasgo*, it *spezzo*/*straccio* |
| 2,5 | `rasen` / `stuermen` / `schiessen` — **drei** Bewegungsverben in einem Vers | *race* / *rush* / *shoot*, in allen vier Sprachen getrennt |
| 2,11 | `schlottern` ↔ `zittern` | `zittern` behaelt *tremble*, `schlottern` weicht auf *knock together · se estremecen · chancellent · vacillano* |
| 2,13 | `Hoehle` ↔ `Lager` — beides der Loewenbau | `Hoehle` behaelt die Amos-Bindung *den · guarida · tanière · tana*, `Lager` weicht auf *lairs · cubiles · repaires · covi* |
| 2,13 | `Beute` ↔ `Gerissenem` | `Beute` = Amos-Bindung *prey*, `Gerissenes` = *torn prey · despojos · dépouilles · rapina* |
| 3,3 | `zahllos` ↔ `unzaehlbar` | **von `hints.py` nicht gemeldet**; `unzaehlbar` weicht auf *beyond counting · sin número · sans nombre · senza numero* |
| 3,14 | `Lehm` ↔ `Ton` | beide Bestandsreihen: `Lehm` auf Jes 41,25 (*mortar*), `Ton` auf der Mehrheit (*clay*) |
| 3,15 | `verzehren` ↔ `fressen` | die Joel-Ordnung: consum-Reihe gegen devor-Reihe |
| 3,18 | `Schlaf` ↔ `schlafen` | `schlafen` → *slumber · duermen · sommeillent · dormono* (WEB schreibt selbst „slumber") |
| 3,19 | `Untergang` ↔ `Zusammenbruch` | `Zusammenbruch` (4 Belege) weicht auf *collapse · derrumbe · effondrement · crollo* |

**In 1,6 stehen `Zorn` und `Wut` zusammen** — der Bestand trennt sie
bereits in allen vier Sprachen (*wrath · ira · colère · ira* gegen
*rage · furor · fureur · furore*), beide unveraendert. `Grimm` kommt im
ganzen Buch nicht vor.

## 4 · Die Heuschreckenbilder in 3,15–3,17

`Grashuepfer` steht **neben** `Heuschrecke` — und die Ausgaben helfen nur
halb:

```
    LSG    unterscheidet gar nicht (zweimal sauterelles)
    WEB    vertauscht zwischen 3,15 und 3,17
    RIV    vertauscht ebenfalls
    RV     als einzige konsistent (langosta ≠ saltamontes)
```

Gefolgt wurde RV; `Heuschrecke` bleibt auf der Joel-Bestandsreihe,
`Grashuepfer` ist neu: C1 *grasshoppers · saltamontes · criquets ·
cavallette* (fr eigens gepraegt).

## 5 · Neu gepraegt

```
Elkosch     A1  Elkosh · Elcós · Elkosch · Elkosh   (Ortsname, transliteriert)
No-Amon     A1  No-Amon · No-Amón · No-Amon · No-Amon
   RV deutet ihn als „Tebas" — NICHT uebernommen
langmütig   C1  slow to anger · lento para la ira · lent à la colère · lento all'ira
ineinander  B2  into one another · unos con otros · les uns dans les autres · gli uni negli altri
Grashüpfer  C1  · Schwarm B2 swarms · enjambres · essaims · sciami
Peitschenknallen C1 crack of whips · chasquido de látigo · claquement de fouet · schiocco di frusta
grenzenlos  B2 · Linderung C1 relief · alivio · soulagement · sollievo
Ziegelform  C1  brick mold · molde de ladrillos · moule à briques · forma da mattoni
niedermähen C1  (Partizip in 1,12, Infinitiv in 3,15 — der Formunterschied
                 ist kein Widerspruch, paketcheck meldet ihn trotzdem)
sich häuten B2 · fortfliegen C1 · Gerissenes C1 · Lager B1 (Loewenbau)
Vorrücken   B2  aus dem Verb-Bestand, NICHT aus `Vorrat`/`Vorrang`
schlottern  C1  knock together · se estremecen · chancellent · vacillano
wegfließen  B2  (die einzigen zwei Formen ohne Stammverwandten im Bestand)
```

## 6 · Fuer die Nachbarbuecher

```
Ninive A1 Nineveh·Nínive·Ninive·Ninive · Assur A1 Assyria·Asiria·Assyrie·Assiria
Kusch A1 Ethiopia·Etiopía·Éthiopie·Etiopia · Put A1 · Libyen A1 Libya·Libia·Libye·Libia
Last B1 burden·carga·charge·peso        ← auch Habakuk 1,1
Kraft A2 strength·fuerza·force·forza    (NICHT power/poder)
Zorn B2 wrath·ira·colère·ira  ·  Wut B2 rage·furor·fureur·furore
Höhle B1 den·guarida·tanière·tana  (Amos-Bindung, NICHT cave)
Beute B2 prey·presa·proie·preda    (Amos-Bindung, NICHT spoils)
verzehren C1 consum-Reihe  ≠  fressen B2 devor-Reihe   (Joel-Ordnung)
Heuschrecke C1 locusts·langostas·sauterelles·locuste  ≠  Grashüpfer C1
Hurerei C1 sexual immorality·fornicación·débauche·fornicazione (Hosea, 46× einstimmig)
   — im PLURAL weicht en auf `prostitutions` aus, romanisch bleibt die Familie
Festung C1 fortress·fortaleza·forteresse·fortezza
Mauer B1 wall·muro·muraille·muro  ≠  Wall C1 rampart·muralla·rempart·terrapieno
Untergang B2 ruin·ruina·ruine·rovina ≠ Zusammenbruch B2 collapse·derrumbe·effondrement·crollo
spricht: vorangestellt fr parle · nachgestellt fr dit
```
