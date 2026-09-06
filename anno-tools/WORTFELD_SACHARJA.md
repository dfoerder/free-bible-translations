# Wortfeld Sacharja (38)

14 Kapitel, 211 Verse, 5176 Tokens, 145 Mehrwoerter. **Fuenf Pakete zu
drei, drei, drei, drei und zwei Kapiteln.** `paketcheck` Abschnitt A
und C in **allen fuenf Paketen leer** — kein neu gepraegtes Lemma wurde
je verschieden entschieden, keine Level-Divergenz.

## Der Paketschnitt

Die Visionskapitel 1-6 haengen untereinander am staerksten zusammen
(2,13→6,15 · 4,4→6,4 · 4,2→5,2 · 5,1→6,1 · 4,14→6,5), deshalb
**1-3 / 4-6 / 7-9 / 10-12 / 13-14**. `wiederholungen.py` fand
**63 Wortfolgen**, die meisten ueber Kapitelgrenzen; die Reihen dafuer
wurden vor jedem Paket **aus den fertigen Dateien gelesen**, nicht aus
den Berichten.

## Der staerkste Einzelbefund

**Sechzehn Vorkommen von „So spricht der HERR der Heerscharen" stehen
Token fuer Token identisch** — ueber neun Kapitel, gesetzt von neun
verschiedenen Agenten, die einander nicht gesehen haben. Die drei
Abweichungen sind alle richtig und wurden vom Kapitel-8-Agenten
begruendet: `dem` ist in 8,11 nach `mit` ein blosser Artikel und in
8,6/8,12 Dativ, `In` ist in 8,4 lokal (*Dans*) und in 8,23 temporal
(*En*), `so` steht in 2,12 satzintern klein.

## Die `spricht`-Stellungsregel — und das Ende der Appositionsregel

vorangestellt → fr `parle`, nachgestellt → `dit`. LSG bestaetigt sie in
Sacharja 1,3 **dreimal im selben Vers**: „Ainsi **parle** l'Éternel des
armées: Revenez à moi, **dit** l'Éternel des armées, et je reviendrai à
vous, **dit** l'Éternel des armées."

Die **Appositionsausnahme**, die ich seit Zefanja mitgeschleppt hatte,
ist widerlegt — der Maleachi-2-Agent hat alle Vorkommen mit ihrem
**Vorfeld** gemessen (siehe `WORTFELD_MALEACHI.md`). Zwei Folgen fuer
dieses Buch: 3,10 traegt `dit`, obwohl die Vorlage Jesaja 22,25 `parle`
liest, und die Bestandsstelle Zefanja 2,9 wurde korrigiert.

**Jesaja 22,25 ist der einzige echte Ausreisser im Korpus** — und der
Sacharja-3-Agent hat nachgewiesen, dass er sogar seiner eigenen Ausgabe
widerspricht: LSG schreibt dort „dit l'Éternel des armées".

## `der` vor `Heerscharen`

`of the · de los · des · degli` — **keine Bestandsmehrheit** (26:25),
sondern der Anschluss an Haggai. Die Spaltung verlaeuft buchweise:
Jesaja liest 25:0 `of`, alles ab Amos 26:0 `of the`. In Sacharja steht
die Reihe an **45** Stellen.

## Was die Agenten am Quelltext widerlegt haben

Ueber vierzig Angaben aus meinen Prompts. Die drei wiederkehrenden
Klassen:

**1. Numerus und Modus.** Die Reihentabelle gibt die haeufigste Form
eines Lemmas; der Vers braucht oft eine andere. In Kapitel 12 waren es
sechs auf einmal (`Sippe` Singular statt Plural, `durchbohren` Partizip
statt 3. Person, `ausspannen` umgekehrt, `Geist` klein statt gross,
`Fackel` Singular, `Flehen` statt `Gebet`). In 13 zweimal in beide
Richtungen: `Hirten` ist in 13,7 **Singular**, `Propheten` in 13,2/13,4
**Plural**.

**2. Das falsche Lemma.** `Zutritt` statt `Zugang` (9 Belege),
`Schmutz` statt `schmutzig`, `Efa` statt `Getreidemaß`, `Nacken` statt
`Rücken`, `Pest` statt `Plage`, `Kessel` statt `Kochtopf`, `Schale`
statt `Opferschale`, `Schatz` statt `Reichtum`, `Uzzia` statt
`Usijas`. Zweimal war es sogar ein Kompositum mit **eigenem Level**:
`Bock` B2 gegen `Leitbock` C1, `Pflock` B2 gegen `Zeltpflock` C1.

**3. Die „unbelegten Wortformen" sind formbasiert.** In Kapitel 9
standen **sieben von zwoelf** laengst im Bestand — `wecken` mit 22
Belegen, `ausfahren` mit 18, `reiten` mit 26. Bei `Stürmen` kam die
Homographenfalle dazu: die Form steht im Bestand, aber als Verb;
gebraucht ist der Dativ Plural von `Sturm` (52 Belege).

## Die Zaehlung

`l1912mod` hat in Kapitel 1 siebzehn Verse, **alle vier Ausgaben
einundzwanzig**: sie ziehen die deutschen Verse 2,1-4 als 1,18-21 ins
erste Kapitel. Deutsch 2,1-17 entspricht dort **1,18 - 2,13**. Der
Agent fuer Kapitel 2 musste seine ersten vier Verse im vorigen Kapitel
der Ausgaben nachschlagen. Alle uebrigen Kapitel stehen auf +0.

Gefunden hat das der reparierte `kapitelgrenzen.py` — er hatte seit
seiner Entstehung fuer **kein einziges Buch** etwas gemeldet, weil er
den Quelltext mit einem relativen Pfad suchte.

## Namen

- **`Zemach`** (3,8 · 6,12) bleibt als **Name** stehen, weil `l1912mod`
  ihn nicht deutet — aber **alle vier Ausgaben uebersetzen ihn**, und
  zwar zeichengenau mit der Bestandsreihe von `Spross` C1 (*branch ·
  renuevo · germe · germoglio*). In 6,12 ist es noch schaerfer: LSG
  schreibt `germe` **klein** und setzt im selben Vers „**germera** dans
  son lieu". Beide Kapitel haben zeichengleich `Zemach` gesetzt.
- **`Jozadak`** trug fr `Jehotsadak` und it `Iozadak` — an allen zwoelf
  Belegstellen geprueft schreibt LSG 10 von 10 „Jotsadak" und RIV
  nirgends „Iozadak". Die Spalten waren vertauscht; korpusweit
  korrigiert.
- **`Jedaja`**, **`Zephanja`**, **`Sarezer`**, **`Kislev`**,
  **`Tobija`** — vier weitere Namensbefunde, in `NACHLESE_BESTAND.md`.
- **`Usijas`** (14,5): der Prompt nannte `Uzzia`, das ist die
  RIV-Lesart. Der deutsche Text liest `Usijas`, 3× belegt.

## Werkzeuge, die an diesem Buch entstanden oder repariert wurden

- **`folgenreihe.py`** — misst die Glossen einer Wortfolge im Bestand
  und schneidet **nichts** ab. Anlass: ich hatte fuer Haggai zwei von
  sechs Varianten ausgeben lassen und daraus „alle mit `parle`"
  geschlossen. Seit Sacharja 1 zeigt es auch die **Mehrwort-Reihen** —
  bei `Kehrt um` zerfaellt der Bestand als Einzelwort in sechs
  Varianten, als Mehrwort in genau drei, nach Bedeutung getrennt.
- **`parallelen.py`** — bevorzugt bei gleicher Blocklaenge jetzt den
  Vers, der **Glossen traegt**. Vorher entschied allein die
  Aehnlichkeit, und in Kapitel 4 fuehrte das dreimal auf noch leere
  Verse desselben Buches.
- **`hints.py`** — nennt die Belegzahl jedes stammverwandten Lemmas,
  fuehrt blosse Schreibvarianten in einem eigenen Abschnitt und meldet
  unbelegte Woerter neben belegten Bestandteilen (mit den drei Faellen,
  die dabei zu unterscheiden sind).
- **`glosskollision.py`** — nannte die falsche deutsche Form, weil der
  Formenspeicher ueber die vier Sprachen hinweg ueberschrieben wurde.
- **`vorgabecheck.py`** — prueft jetzt auch **umbrochene** Zitate. Sie
  waren seit Bestehen der Probe unsichtbar, weil Prompts auf 72 Zeichen
  gebrochen sind.
- **`folgencheck.py`** — die Zeichengleichheitspruefung, die ich
  fuenfmal als Wegwerfskript geschrieben hatte.

## Kollisionen, die kein Werkzeug melden konnte

`hints.py` blendet Funktionswoerter aus. Die Agenten haben deshalb in
den Kapiteln 5, 8, 10, 11, 12, 13 und 14 **je mehrere Kollisionen
selbst gefunden**, indem sie die Praepositionen ihrer Verse
durchzaehlten — 5,9 `auf`/`empor`, 8,3 `zu`/`in`, 8,9 `aus`/`seit`,
10,1 `um`/`für`, 11,16 `Gesunde`/`heilt`, 14,18
`heraufzieht`/`heraufkommen`. Keine davon stand in einem Prompt.
