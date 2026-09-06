# Wortfeld Maleachi (39)

Drei Kapitel, 55 Verse, 1589 Tokens, 52 Mehrwoerter. Ein Paket, drei
Agenten. `paketcheck` Abschnitt A und C **leer**.

**Das letzte Buch des Projekts.** Mit ihm sind alle 66 Buecher
annotiert.

## Die Appositionsregel — hier ist sie gefallen

Seit Zefanja stand in jedem Prompt: vorangestellt → fr `parle`,
nachgestellt → `dit`, **mit Apposition → `parle`, auch nachgestellt**.
Der Agent fuer Kapitel 2 hat als erster alle Vorkommen von „spricht der
HERR … der Gott …" mit ihrem **Vorfeld** gemessen — das hatte ich nie
getan:

```
vorangestellt   parle   72×
nachgestellt    dit      4×   Jesaja 17,6 · Jeremia 31,1 · Amos 6,8 · Amos 6,14
nachgestellt    parle    2×   Jeremia 32,36 · Zephanja 2,9
```

Beide Gegenfaelle loesen sich auf: **Jeremia 32,36 ist in Wahrheit
vorangestellt** („ainsi parle l'Éternel") — meine Messheuristik hatte
ihn falsch einsortiert, weil „Et maintenant" davorsteht. Und
**Zephanja 2,9 war mein eigener Fehler**: LSG liest dort „**Dit**
l'Éternel des armées, le Dieu d'Israël". Korrigiert.

**Es gibt keine Appositionsausnahme. Die Stellung allein entscheidet.**
Maleachi 2,16 traegt deshalb `dit`, und die Vorlage 1. Samuel 10,18
(die ich empfohlen hatte) ist selbst vorangestellt — wer ihren Block
Token fuer Token uebernimmt, holt sich genau den einen Fehler.

Im ganzen Buch: **21 nachgestellte Formeln mit `dit`, eine
vorangestellte (1,4) mit `parle`.**

## Die Streitgespraechsformel

Maleachi ist als Disput gebaut, und die Formel steht **achtmal** — nicht
sechsmal, wie mein Prompt sagte, und die dort gelisteten sieben Stellen
waren um 2,14 unvollstaendig. Sie ist ausserdem **dreiteilig**:

```
Doch ihr fragt: Worin …?     1,2 · 3,7
Ihr fragt: Womit …?          1,6 · 1,7 · 2,17 · 3,8
Ihr fragt: Warum das?        2,14
Doch ihr sagt: Was reden wir gegen dich?   3,13
```

`Doch` steht nur vor 1,2 · 1,6 · 3,7 · 3,13. Die Antwortformel `Damit,
dass ihr sagt` (1,7 · 2,17 · 3,14) **fehlte in meinem Prompt ganz** —
und war die haeufigste Folge des Buches. Ich hatte die Ausgabe von
`wiederholungen.py` mit `tail -40` gelesen; sie hat 14 Folgen, ich
nannte zehn. **Der dritte Fall desselben Fehlers in dieser Sitzung**
(nach dem abgeschnittenen Jona-Zitat und den zwei von sechs Varianten
in Haggai): aus einer gekuerzten Ausgabe auf Vollstaendigkeit
geschlossen. Die Gesamtzahl stand im Kopf der Ausgabe, den `tail`
verschluckt hat.

**Die drei Agenten haben sie trotzdem Token fuer Token gleich
gesetzt** — alle vier kapitelübergreifenden Formeln stimmen ueberein.

## Die Zaehlung

`l1912mod` hat **ein** Kapitel 3 mit 24 Versen, **alle vier Ausgaben
teilen es**: 3,1-18 bleibt Kapitel 3, **3,19-24 steht dort als Kapitel
4, Verse 1-6**. `ausgaben.py` meldet dafuer „-6 UNSICHER" und warnt im
selben Atemzug „Versatz +0 liegt BESSER" — die Regel „die Warnung
lesen, nicht die Zahl" traegt auch hier. LSG schliesst 4,6 mit
„FIN DE L'ANCIEN TESTAMENT".

## `HERR` gegen `Herr` in 1,6

Der Vers macht die Unterscheidung selbst zum Thema: „Ein Sohn ehrt
seinen Vater, ein Knecht seinen Herrn. Bin ich nun Vater - wo bleibt
meine Ehre? Bin ich Herr - wo bleibt die Furcht vor mir?"

Der Agent hat alle vier Ausgaben befragt: **drei von vieren trennen
lexikalisch** — WEB *master* gegen *Yahweh*, RV *señor* gegen *Jehová*,
LSG *maître* gegen *l'Éternel*; nur das Italienische trennt allein
ueber die Grossschreibung. Gesetzt ist deshalb `master · amo · maître ·
padrone` (Bestandszeile aus Jesaja 19,4) statt der haeufigeren Reihe,
die im Spanischen nur die Kapitaelchen unterschieden haette.

## Was die Agenten sonst am Quelltext widerlegt haben

- **Vier Substantive der Reihentabelle sind im Text Adjektive.** 1,8
  liest „ein **blindes** Tier", „ein **lahmes** oder **krankes**", 1,14
  „ein **makelloses**". Also `blind` **A2**, `krank` **A1**, `lahm` B2,
  `makellos` C1 — nicht `Blinder` B1, `Kranker` B1, `Lahmer` B2,
  `Makel` C1. **Zwei Level aendern sich dadurch.**
- **`Weihrauch`, `Brandopfer`, `Ansehen`, `Ehe`, `Makel`, `Seife`,
  `Frevler`, `Bergwerk` kommen im Buch nicht vor.** 1,11 liest
  `Rauchopfer` (eigenes Lemma, C1, 4× einstimmig), 2,9 das **Verb**
  „die Person ansieht" — im Bestand bereits ein Mehrwort `die Person
  ansehen` C1 aus Jakobus 2,9, zeichengleich uebernommen.
- **`Zehnte` ist nicht unbelegt**: Lemma `Zehnter` B2, 78 Belege.
- **`dem HERRN der Heerscharen` (2,12 · 3,14) darf nicht zeichengleich
  sein.** In 2,12 ist `dem` Dativobjekt von `bringt` (*to the · al · à
  l' · al*), in 3,14 steht es nach `vor` (*the · el · l' · il*). Beide
  Agenten haben das unabhaengig richtig gesetzt.
- **`Bote` steht dreimal im Singular** (2,7 · 3,1 zweimal), meine
  Tabelle gab den Plural. `Levi` traegt nach `mit` (2,4 · 2,8) die
  artikellose Reihe, die Genitivreihe gehoert zu 3,3.
- **Mein Verszitat zu 1,6 war nicht der Quelltext** — und die beiden
  Gedankenstriche darin sind alleinstehende Satzzeichen ohne Eintrag.
- **`scheuen` in 2,5 heisst nicht „fuerchten".** Der Vers liest „damit
  er mich fuerchtete und meinen Namen scheute" — zwei Verben im selben
  Finalsatz, also *might revere* gegen *might fear*.

## Neu gepraegt

```
Maleachi     A1  Malachi · Malaquías · Malachie · Malachia
Tempeltür    B2  temple doors · puertas del templo · portes du temple · porte del tempio
rümpfen      C1  turn up your noses · arrugáis la nariz · faites la grimace · arricciate il naso
fehlerhaft   B2  defective · defectuoso · défectueux · difettoso
unheilig     B2  unholy · profana · profane · profana
verödet      C1  laid waste · devastado · dévasté · devastato
Gefährtin    B2  companion · compañera · compagne · compagna
kleben bleiben B2  (nach dem belegten `haften bleiben`)
Wäscher      C1  launderers · lavanderos · foulons · lavandai
Schädling    B2  pests · plagas · nuisibles · parassiti
herabschütten B2  pour down · derramar · répandre · riversare
Gedenkbuch   C1  book of remembrance · libro de memorias · livre de souvenir · libro di ricordo
```

`die Nase rümpfen` ist ein Mehrwort mit `parts`, und `rümpft` traegt
dieselbe Reihe, weil es ausserhalb der Wendung keine Bedeutung hat —
die Amos-4,5-Regel.

## Eine Falle, die lautlos durch `selfcheck` lief

Der Kapitel-1-Agent hat `form` aus den Positionen abgeleitet — und weil
`parts` falsch war, war `form` **konsistent falsch mit dazu**
(`[7,9,10]` statt `[8,10,11]`, „und darueber die" statt „die Nase
ruempft"). `selfcheck.py` prueft die Form **gegen** die Positionen und
schwieg. Gefunden hat er es beim Nachlesen der fertigen JSON.

Eine maschinelle Gegenprobe dafuer gibt es nicht: die naheliegende
Regel „mindestens ein Token stammverwandt mit dem Lemma" schlaegt im
Bestand bei **20 Prozent** aller Mehrwoerter an, weil trennbare Verben
mit Ablaut sie brechen (`ansehen` → „sah an"). Gemessen und verworfen;
die Vorsichtsmassnahme steht jetzt im Prompt-Baustein.

## Ausgabenbefunde

- **1,14** laesst in zwei Ausgaben den Gottesnamen fallen, wo das
  Deutsche `HERRN` in Kapitaelchen hat: WEB „to the **Lord**", LSG „au
  **Seigneur**" — RV und RIV behalten ihn.
- **1,14** gibt `makellos` in **keiner** Ausgabe wieder (alle vier
  lesen „a male / un macho / un mâle / un maschio"); die Glosse kommt
  allein aus dem Bestand.
- **1,8/1,13**: WEB substantiviert („the blind", „the lame"), waehrend
  es/fr/it Adjektiv + Nomen setzen. `l1912mod` folgt den drei
  romanischen — genau deshalb greifen die Substantivreihen nicht.
- **RIV 1,6** „o **acerdoti**" statt *sacerdoti* — ein weiterer
  Anlautverlust.
