# Bestandsbefunde aus Ester — gemeldet, nicht korrigiert

Was Agenten im **fertigen Bestand** oder in den **Referenzausgaben** gefunden
haben, während sie Ester annotierten.

## Aus den Kapiteln 1 bis 3

- **`herrschen` hat im Bestand keine saubere „regieren"-Lesart.** Die
  Kombination *reinaba · régnait · regnava* ist dort durchgehend an englisch
  ***prevailed*** gekoppelt (10 Belege, alle „Hungersnot herrschte"). Für
  Ester 1,1 („der über 127 Länder herrschte") wäre das eine Lexikonfalle
  gewesen; dort steht jetzt *reigned · reinaba · régnait · regnava* — eine neue
  Kombination. **Korpusweit zu prüfen.**
- **`Getränk`:** `BINDUNGEN_AT.md` nennt *beverage · bebida · boisson ·
  bevanda* (7/10), der einzige Beleg im Bestand (Jer 42,1.15) trägt aber
  *drinks · bebidas · boissons · bevande* auf A2.
- **`reichen` hat 20 Lesarten und keine für „darreichen".** Est 1,7
  (`gereicht` = *served*) ist die erste.
- **`Erlass` gab es im Bestand nicht.** In Ester dreifach auseinandergelaufen
  und an den Ausgaben entschieden: *decree · decreto · édit · editto*, B2.
  Kapitel 3 war auf *edict* ausgewichen, um `Anordnung` (*decree*, 7 Belege)
  Platz zu machen — aber **`Anordnung` kommt in Ester gar nicht vor**. Eine
  Auflösung ohne Kollisionsstelle macht den Bestand nur inkonsistent.
- **`Ohr` italienisch weiter uneinheitlich** (42 *orecchi* / 10 *orecchie*).
  Est 2,22 folgt der Mehrwortvorlage `zu Ohren kommen` (1Mo 35,22) mit
  *alle orecchie*. Der Bruch aus `BEFUNDE_NEHEMIA.md` bleibt offen.
- **`nur` und `allein` teilen sich in nur 6 Bestandsversen eine Glosse** — also
  **keine** korpusweite Praxis. In Est 3,6 stehen beide im selben Vers und sind
  verse-lokal getrennt worden.

## Befunde in den Referenzausgaben selbst

Diese betreffen nicht den Bestand, sondern die Quellen — und sie sind der
Grund, warum die Regel „folge der Ausgabe" eine Mehrheitsentscheidung braucht,
wenn die Ausgabe selbst schwankt.

- **WEB schreibt `Susa` innerhalb desselben Buches zweierlei:** *Shushan* in
  1,2 · 1,5 · 3,15 · 4,8 · 4,16 · 9,13–18, *Susa* in 2,3 · 2,5 · 2,8 ·
  8,14–15 · 9,6–12. Die Annotation folgt der Bestandsbindung *Shushan*
  (Neh 1,1) und schreibt sie durchgehend fort.
- **LSG1910 schreibt `Hegai` zweierlei:** *Hégué* in 2,3, *Hégaï* in 2,8 ·
  2,15. Mehrheitsform *Hégaï* genommen.
- **RIV1927 hat in Kapitel 2 zwei Setzfehler:** „figliuolo di **cimei**" (2,5,
  gemeint Simei) und „il **ettimo** anno" (2,16). Der Bestand (*di Simei*) und
  die korrekte Ordinalform (*settimo*) gehen vor.
- **WEB schreibt den Kämmerer in 1,10 „Carcass"** — im Lesefluss stünde an
  einem Personennamen das englische Wort für Kadaver. Die drei anderen
  Ausgaben schreiben *Carcas*, und die gilt. Die Ausnahme ist in
  `AUFTRAG_AT.md` festgehalten.
- **`Tharsis`:** die Ausgaben schreiben uneinheitlich, der Bestand hat aus zwei
  Belegen *Tarshish · Tarsis · Tarsis · Tarsis*. Bindung geht vor.

## Werkzeugbefunde

**`vorab.py` führte bei Eigennamen aktiv in die Irre.** Die Tabelle schlägt die
Bestandslesart einer **Wortform** nach und weiß nicht, ob derselbe Träger
gemeint ist. Für `Seres` bot sie *Sheresh · Seres · Schéresch · Seres* mit
einem Beleg an — der Beleg ist **1Chr 7,16**, wo Seres der Bruder des Peres
ist. Hamans Frau schreiben alle vier Ausgaben *Zeresh · Zeres · Zéresch ·
Zeresh*. Der Agent von Kapitel 5 hat die Tabelle an den Ausgaben widerlegt;
unabhängig nachgeprüft an 5,10 · 5,14 · 6,13 in allen vier Ausgaben.

Derselbe Fall wie `Sethar` in Ester 1,10/1,14 — nur dass der dort **nicht** im
Bestand stand und die Tabelle deshalb schwieg. Seither trägt jede
großgeschriebene Zeile in `vorab.py` einen Warnhinweis **mit Belegstelle**:
`Seres | … | 1 ⚠ 1. Chronika 7,16`. Die bloße Zahl ist bei einem Eigennamen
wertlos — erst die Stelle zeigt, dass sie aus einem anderen Zusammenhang kommt.

**`lexicon.py` und `hints.py` verlieren das Lemma `laden`.** `geladen`
(Est 5,12) steht im Extrakt nur unter VERWANDT bei `Geladener`/`gelangen`,
obwohl der Bestand 36 Belege für `laden` auf B1 hat, darunter genau die
Einladungs-Lesart. Aufgedeckt hat es wieder nur `levelcheck.py` — die
Präfixverb-Lücke, viertes Vorkommen in Ester.

**Der Bestand widerspricht sich bei `kleiden`:** das Simplex steht auf B2
(22 Belege), das Reflexivum `sich kleiden` auf B1 (2 Belege). Beide Lemmata
sind fortgeschrieben worden; die Stufung ist in sich unstimmig.

## Werkzeugbefund

**`hints.py` widerspricht sich bei `Pfahl` selbst:** es listet die Form als
unbelegt und nennt im selben Eintrag `Pfahl` als verwandten Stamm. Der Singular
ist tatsächlich unbelegt, der Plural `Pfähle` steht dreimal. Harmlos, aber es
zeigt, dass der VERWANDT-Abschnitt das Lemma nicht gegen die Formliste prüft.
