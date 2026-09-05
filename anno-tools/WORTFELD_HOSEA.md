# Wortfeld Hosea (Buch 28)

Waechst mit jedem Paket. **Alle** Abschnitte lesen, nicht nur die ersten.

Die buchweiten Entscheidungen — Verszaehlung, Namen, das Hurerei-Wortfeld —
stehen vollstaendig in **`PAKETE_HOSEA.txt`**. Diese Datei sammelt, was die
Kapitel danach zusaetzlich festlegen.

## 0 · Vor dem ersten Kapitel — die vier Faelle, die jeden angehen

**1. Die vier Ausgaben zaehlen untereinander verschieden.** In Kapitel 2 und
12 folgt **allein die franzoesische** der deutschen Zaehlung; en und it sind
um zwei bzw. einen Vers versetzt, es in Kapitel 2 ebenfalls und in Kapitel 12
gar nicht. In Kapitel 14 sind alle vier versetzt. Die Tabelle steht in
`PAKETE_HOSEA.txt`; `ausgaben.py` richtet Kapitel 2 und 12 nicht zuverlaessig
aus.

**2. RIV traegt in 11,12–12,14 eine zweite Verszaehlung im Text** — fuenfzehn
Verse beginnen mit `(12:1)`, `(12:2)` und so fort. Kein Defekt, sondern ein
Fliesstext-Artefakt der italienischen Ausgabe. Wer die RIV-Zeile Wort fuer
Wort abzaehlt, hat zwei Tokens Vorsprung.

**3. `Gomer` ist ein Doppeltraeger, und die haeufigere Lesart ist die
falsche.** Fuenf Bestandsbelege fuehren das Hohlmass (*omer*), vier den Namen.
In 1,3 ist es die Frau.

**4. `Hurerei` ist mit 46 Belegen einstimmig gebunden** —
*sexual immorality · fornicación · débauche · fornicazione*. Das Wort und
seine Familie tragen das ganze Buch (20 Vorkommen).

## 1 · Paket 1 — Kapitel 1 · 2 · 3

39 Verse, 1037 Eintraege. `paketcheck` Abschnitt **A leer**.

### Die Namen des Buches stehen

    Lo-Ruhama   A1  Lo-Ruhamah · Lo-ruhama · Lo-Ruchama · Lo-ruhama   (neu)
    Lo-Ammi     A1  Lo-Ammi · Lo-ammi · Lo-Ammi · Lo-ammi             (neu)
    Diblaim     A1  of Diblaim · de Diblaim · de Diblaïm · di Diblaim (neu)
    Gomer       A1  Gomer · Gomer · Gomer · Gomer      — der **Name**, nicht das Hohlmass
    Beeri       A1  of Beeri · de Beeri · de Beéri · di Beerì         (1. Mose 26,34)
    Jesreel     A1  Jezreel · Jezreel · Jizreel · Izreel
                    Genitiv: of Jezreel · de Jezreel · de Jizreel · d'Izreel
    Jehu        A1  Jehu · Jehú · Jéhu · **Jehu**      — nicht *Iehu*, s. u.
    Usia · Jotham · Ahas · Hiskia · Jerobeam · Joas — alle belegt

**In 2,25 setzt der deutsche Text die Deutung selbst daneben** („Lo-Ruhama,
**die Unbegnadigte**", „Lo-Ammi, **der nicht mein Volk war**"). Die Deutung
ist deutscher Text und wird uebersetzt, der Name bleibt Name — auch dort,
wo **WEB gar keinen Namen mehr setzt** („her who had not obtained mercy").

`Unbegnadigte` C1 *unpardoned one · no indultada · non graciée · non
graziata* ist neu und haengt an `begnadigen` C1 (2,3).

### `Jehu` — der erste Fall, in dem ein Agent den Korpusbefund anwendet

Der Bestand glossiert `Jehu` italienisch 58× als *Iehu*. **RIV schreibt
73× `Jehu` und kein einziges Mal `Iehu`** — das ist Fall 1 aus
`BEFUNDE_RIV_ANLAUT_J.md`, dort mit 65 Vorkommen gelistet. Der Agent fuer
Kapitel 1 hat das nachgemessen und nach dem Daniel-Praezedenzfall die
RIV-Form gesetzt, ohne dass der Prompt ihn darauf hinwies.

### `Jesreel` — gegen die Ausgabe des Verses entschieden

**RIV schreibt `Jizreel` ausschliesslich in Hosea** (5×) und sonst 31×
`Izreel`, dazu 3× `Jzreel` und 2× `Iizreel` — beides Setzfehler. Bei einer
Ausgabe, die denselben Namen auf vier Arten schreibt, traegt die
Bestandsbindung (40 von 42) mehr als die Zeile im Vers. Dieselbe
Entscheidung ist in Daniel 11 bei `Griechenland` gefallen. **Beide Agenten
haben sie unabhaengig so getroffen.**

### Das Hurerei-Wortfeld

    Hurerei          C1  sexual immorality · fornicación · débauche · fornicazione
    Hurerei treiben  C1  (Mehrwort, 24 Bestandsbelege)
    Hure             C1  prostitute · prostituta · prostituée · prostituta
    Ehebruch         C1  adultery · adulterio · adultère · adulterio
    Ehebruch treiben C1  **neu** — commits adultery · comete adulterio ·
                         commet l'adultère · commette adulterio
    Liebhaber        B2  lovers · amantes · amants · amanti   (Sg. lover · amante · amant · amante)
    nachlaufen       B1  run after · correr tras · courir après · correre dietro

**`Ehebruch treiben` fehlte im Bestand**, obwohl `Hurerei treiben` 24
Belege hat und `Ehebruch` 17. Ein Funktionsverbgefuege derselben Bauart,
in Analogie angelegt.

### Der Landwirtschafts- und Festwortschatz aus Kapitel 2

Er kehrt in Kapitel 9 wieder:

    Getreide B1 grain · trigo · blé · grano   ·   Most B2 new wine · mosto · moût · mosto
    Öl A2 · Wolle B1 · Flachs B2 flax · lino · lin · lino
    Weinstock B2 · Feigenbaum B1 · Weinberg B1
    Fest A2 · Neumond B2 · Sabbat B1 · Feiertag B1

### `Baal` — Name, auch wo zwei Ausgaben uebersetzen

    Baal Sg.  A1  Baal · Baal · Baal · Baal          2,10 · 2,18
    Baal Pl.  A1  Baals · baales · Baals · Baal      2,15 (`Baalen`) · 2,19 (`Baale`)

In **2,18** („du wirst mich `mein Mann` nennen und nicht mehr `mein
Baal`") uebersetzen **WEB** (*my master*) und **LSG** (*Mon maître*),
waehrend RV (*Baali*) und RIV (*Mio Baal*) transliterieren. Der deutsche
Text deutet nicht — also bleibt es der Name.

### Zwei Faelle, in denen der l1912mod ein Fachwort meidet

**3,4** ist der klarste: der Vers zaehlt sechs Dinge auf, und **zwei
deutsche Woerter stehen an fremden Plaetzen.**

| Position | deutsch | alle vier Ausgaben |
|---|---|---|
| 4 | `Altar` | *sacred stone · piedra sagrada · statue · statua* (Mazzebe) |
| 6 | `Heiligtum` | *idols · ídolos domésticos · théraphim · idoli domestici* (Terafim) |

Glossiert wird der deutsche Text mit seiner Bestandsbindung. `Priestergewand`
dagegen traegt die Reihe der Ausgaben selbst: C1 *ephod · efod · éphod ·
efod* (13 Lemmabelege).

**`Fürsten` in 3,4 ist Akkusativ Singular**, nicht Plural — `Fürst` ist ein
n-Deklinationswort, und alle vier Ausgaben setzen den Singular. Die
Bindungstabelle allein haette in den Plural gefuehrt (229 gegen 34).

### Was `sweeplemma.py` allein gefunden hat

In Kapitel 2 hat es **drei** Mehrwortluecken gemeldet, die `sweep.py` und
`konvention.py` beide nicht sahen: `es geht jemandem gut` (2,9) und
zweimal `zu jener Zeit` (2,20 · 2,23). Der Lauf gehoert damit fest in die
Kapitelpruefung, obwohl `AUFTRAG_BUCH.md` ihn nicht unter den sechs
Pflichtlaeufen fuehrt.

### Neue Lesarten unter vorhandenen Lemmata (8)

    zusammenschließen  Bestand: feindliche Buendnisse — hier *gather together* (2,2)
    ausziehen          keine Lesart fuer „nackt ausziehen" — *strip · despojo* (2,5)
    ziehen             „eine Mauer davor ziehen" — *put up · levanto* (2,8)
    verloben           Bestand nur *engaged* — hier *betroth · desposo* (2,21)
    Jesreel            Genitiv — *of Jezreel · d'Izreel* (1,5)
    am / über          bei `ahnden` und `sich erbarmen` (1,4 · 1,6 · 1,7)
    anderthalb         Bestand nur maskulin — hier feminin nach `Scheffel` (3,2)
    gehören            Bestand nur 1. Person — hier verneinter Imperativ (3,3)

### Die Ausgaben

**RIV: zwei Anlautfehler, beide in 1,1 und 1,6** — und beide in denselben
zwei Versen des Kapitels:

    1,1  `di zechia`  → d'Ezechia   (134× `Ezechia` im Korpus, 3× `zechia`)
    1,1  `Acaz`       → Achaz       (39× `Achaz`, 1× `Acaz` — nur hier)
    1,6  `erché`      → perché      (2853× `perché`, 17× `erché`)

`zechia` steht ausserdem in **Jesaja 39,1 und Micha 1,1** —
vorgemerkt in `VORMERKUNGEN_29_39.md`.

**In Kapitel 2 und 3 kein einziger Anlautfehler**, in keiner der vier
Ausgaben. Beide Agenten haben ihren Detektor an 1,6 verifiziert.

**RV1909mod siezt** in 1,10 · 2,1 · 2,3 — auf `vosotros` umgestellt, wie
seit dem Hohelied festgelegt.
