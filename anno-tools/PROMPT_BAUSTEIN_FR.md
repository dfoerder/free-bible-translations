# Der gemeinsame Prompt-Baustein — franzoesisches NT

**Platzhalter: `<NR>` = Buchnummer, `<KAP>` = Kapitelnummer, `<BUCH>` =
Buchname, `<SCRATCH>` = Scratchpad-Verzeichnis des Buches.**

Die Schwester von `PROMPT_BAUSTEIN.md`. Was dort steht, gilt hier
sinngemaess weiter; **dieser Baustein sagt, was anders ist.** Wer beide
liest, liest doppelt — fuer die franzoesische Arbeit gilt allein dieser.

---

Du annotierst **<BUCH> (Buch <NR>), Kapitel <KAP>** der franzoesischen
Louis-Segond-1910 in ihrer modernisierten Fassung `lsg1910mod` mit
Wort-fuer-Wort-Glossen in **Deutsch, Englisch, Spanisch und Italienisch**
plus CEFR-Level.

Das ist die **Gegenrichtung** zur bisherigen Arbeit: bis Maleachi war
Deutsch der annotierte Text und Franzoesisch eine Glossenspalte. Jetzt
ist Franzoesisch der Text.

## Wo alles liegt

Arbeitsverzeichnis: `/Users/dfoerd/Documents/projekte/bibel/bibles-translations`

    export ANNO_EDITION=fra/lsg1910mod
    export ANNO_OUT=<SCRATCH>/out

**Beide sind Pflicht.** Ohne `ANNO_EDITION` arbeitet die ganze Werkzeug-
kette auf dem deutschen Text weiter — sie bricht dabei nicht ab, sie
antwortet nur zum falschen Buch. Setz sie als Erstes und pruef sie:

    python3 -c "import common as C; print(C.EDITION, C.LANGS)"
    → fra/lsg1910mod ['de', 'en', 'es', 'it']

Alle Werkzeuge werden **aus `anno-tools/` heraus** aufgerufen.

Deine Abgabe: `$ANNO_OUT/<NR>/ch<KAP>.json`
Dein Arbeitsverzeichnis fuer alles andere: `$ANNO_OUT/../work/<KAP>/` —
jede Zwischendatei und jedes Hilfsskript dorthin, nicht neben die Abgabe.

## Eintragsformat

    {"pos": 3, "form": "serviteur", "lemma": "serviteur", "level": "B1",
     "de": "Knecht", "en": "servant", "es": "siervo", "it": "servo"}

Die Spalten heissen **de · en · es · it** — nicht en/es/fr/it. Eine
`fr`-Spalte gibt es nicht; Franzoesisch ist die `form`.

Mehrwoerter tragen zusaetzlich `pos_end` (zusammenhaengend) **oder**
`parts` (getrennte Positionen). Das gilt unveraendert.

**Auch ein Mehrworteintrag traegt `form`** — die Oberflaeche, aus den
EINZELEINTRAEGEN zusammengesetzt, nie aus dem Quelltext. Ohne sie meldet
`selfcheck.py` Dutzende Scheinbefunde („Eintrag pos=0 ohne Feld form")
und der Durchgang ist verloren. Gemeldet vom Agenten fuer 2. Petrus 2.

**`form` traegt keine Satzzeichen.** Der Quelltext hat sie (`Dieu,`
`vides.`), der Bestand fuehrt sie nicht — `form` ist immer das nackte
Wort, so wie `common.strip_punct` es liefert. Wer den Rohtoken
uebernimmt, bekommt von `selfcheck.py` dreihundert Scheinbefunde der
Art `Dieu, != Dieu` und sucht den Fehler in der falschen Ecke. Bei
Mehrwoertern gilt dasselbe doppelt: die Oberflaeche des Mehrworts wird
aus den **Einzeleintraegen** zusammengesetzt, nie aus dem Quelltext,
sonst wandert der Satzpunkt in ein Mehrwort, das am Versende endet.

## Dein wichtigstes Werkzeug: `rueckwaerts.py`

    python3 rueckwaerts.py <NR> <KAP> -o $ANNO_OUT/../work/<KAP>/rw.md

`eng/web`, `deu/l1912mod` und `ita/riv1927mod` sind annotiert und
**tragen alle eine fr-Spalte**. Zusammen decken sie deine vier
Zielsprachen mehrfach ab — der Extrakt nennt bei jeder Zeile, aus
welcher Ausgabe sie stammt. Ueber die fr-Spalte als Schluessel liegt fuer 98 Prozent
der franzoesischen Tokens bereits eine vollstaendige Viererzeile vor —
und fuer etwa die Haelfte sogar aus **genau deinem Vers**.

Der Extrakt ist nach Versen geordnet. Vier Schichten:

    VERS       das Wort steht als fr-Glosse in genau diesem Vers der
               Zeugen. Fast immer schon die richtige Zeile.
    GLOSSE     es steht anderswo im NT als fr-Glosse
    TEIL       nur innerhalb einer mehrwortigen Glosse
    ELISION    nur die Haelften (`qu'ils` = `qu'` + `ils`)
    UNBELEGT   hier ist die Arbeit

**Was die VERS-Schicht liefert, ist ein starker Vorschlag und keine
Vorgabe.** Die Zeugen sind Uebersetzungen, keine Interlinearversionen:
wo LSG anders gliedert als WEB oder Luther, steht die Zeile am falschen
Wort. Lies den Vers.

## Was aus den Zeugen NICHT uebernommen wird

- **Kein Lemma.** Das Lemma im Zeugen ist englisch oder deutsch. Deins
  ist franzoesisch: Verben in den Infinitiv (`dit` → `dire`), Nomen in
  den Singular (`disciples` → `disciple`), Adjektive ins Maskulinum
  Singular (`aimés` → `aimé`), Artikel und Pronomen normalisiert
  (`le`/`la`/`les`/`l'` → `le`, `du`/`des` → `de`).
- **Kein Level.** Das Level im Zeugen ist CEFR fuer Englisch- oder
  Deutschlernende. Deins ist CEFR **fuer Franzoesischlernende**. Der
  Extrakt schreibt bei jedem Level dazu, aus welcher Ausgabe es stammt —
  das ist eine Warnung, keine Empfehlung.

## Franzoesische Besonderheiten

- **Elision ist EIN Token.** `qu'ils`, `d'un`, `l'Éternel`, `s'est`,
  `n'ont` stehen im Text als ein Wort und bekommen **einen** Eintrag,
  dessen Glossen beide Teile abdecken: `qu'ils` → de *dass sie* · en
  *that they* · es *que ellos* · it *che essi*. Nicht in zwei Eintraege
  zerlegen — die Positionen zaehlen ueber `text.split()`.
- **Die Inversion mit Bindestrich** (`est-il`, `dit-il`, `qu'est-ce`,
  `sauvez-en`) ist ebenfalls ein Token und ein Eintrag.
- **Das negative Paar `ne … pas`** steht an zwei getrennten Positionen.
  Beide bekommen ihren Einzeleintrag; wo die Negation zusammen glossiert
  gehoert, kommt ein Mehrwort mit `parts` dazu.
- **`glosskollision.py` vergleicht klein.** `Quant` = *Was* am
  Versanfang und relatives `que` = *was* gelten ihm als dasselbe Wort,
  obwohl die App beides sichtbar unterscheidet. Ein Paar, das sich
  allein in der Grossschreibung trennt, ist **keine** Kollision — nicht
  aufloesen. Gemeldet von den Agenten fuer Marc 11 und Marc 12.
- **Grossschreibung.** Franzoesische Nomen sind klein. `artikel.py` und
  `kongruenz.py` finden das Nomen deshalb ueber die **deutsche** Glosse —
  das heisst: eine schlampige `de`-Spalte macht zwei Pruefungen blind.
- **`vous` ist im Franzoesischen Hoeflichkeitsform UND Plural.** Am Vers
  entscheiden, welches gemeint ist; im Spanischen wird daraus in aller
  Regel **vosotros**, nicht `usted`.

## Der Bestand traegt jetzt

**Der eigene Bestand ist die erste Quelle, nicht die zweite.** Der Satz,
der hier bis Markus stand („beim ersten Buch ist die franzoesische Anno
noch leer, `lexicon.py` und `parallelen.py` antworten leer"), gilt nur
noch fuer das allererste Buch einer Ausgabe; der Agent fuer Marc 3 hat
ihm zu Recht widersprochen.

**Wieviel schon steht, sagt dir kein Satz in dieser Datei, sondern der
Lauf selbst:** jedes Werkzeug druckt den Bestandsstand in seine
Kopfzeile (`Bestand: <ausgabe> · <commit> <datum>`), und
`validate.py alle` zaehlt Buch fuer Buch auf. Eine Zahl, die hier
eingetragen waere, altert mit dem naechsten Paket — der Agent fuer
1. Korinther 6 hat genau die alte hier gefunden und gemeldet.

- **`parallelen_<nr>_<kap>.md`** liegt in deiner Vorbereitung und zeigt,
  wo derselbe Wortlaut schon annotiert steht. Das ist die staerkste
  Bindung, die es gibt.
- **`fixgloss.py verse <NR> <KAP> <VERS>`** zeigt einen annotierten Vers
  **ganz** — jedes Token mit Lemma, Level und Glossen, und darueber die
  Mehrwortspannen. Wenn `parallelen_<nr>_<kap>.md` dir einen Parallelvers
  nennt, ist das der Griff, mit dem du ihn liest. `folgenreihe.py`
  beantwortet nur, was du schon zu fragen weisst; der ganze Vers zeigt
  auch die Mehrwoerter, die du sonst neu erfindest (`faire asseoir`,
  `par terre` — der Agent fuer Marc 8 hat beide erst so gefunden).
- **`folgenreihe.py "<folge>"`** misst die Glossen des Bestands zu genau
  dieser Folge. **Es sucht die ZEICHENKETTE im Quelltext, nicht das
  Lemma**: `folgenreihe.py "garder le silence"` meldete 0, obwohl das
  Mehrwort im Bestand steht — dort in der Form `garda le silence`
  (Mt 26,63). Wer nur folgenreihe fragt, erfindet ein vorhandenes
  Mehrwort neu. Fuer Mehrwoerter ist **`sweeplemma.py`** der Finder: es
  hat in Marc 3 sechs Mehrwoerter gemeldet, deren Bloecke zu kurz sind,
  als dass `parallelen.py` sie zeigen koennte — fuenf standen laengst im
  Bestand.
- **`lexicon.py <NR> <KAP> -o <datei>`** ist das Werkzeug, das die
  Vorbereitung nicht mitliefert und das der Agent fuer Offenbarung 1 als
  sein nuetzlichstes bezeichnet hat: es zeigt **jede** Wortform des
  Kapitels mit Lemma, Level und den drei haeufigsten Bestandsreihen —
  und darunter einen Block „MEHRWORT-EINTRAEGE, deren Teile hier
  vorkommen". Der hat ihm `faire connaître`, `séjour des morts`,
  `Ne crains pas` und `au milieu des` samt Reihe geliefert, bevor
  `sweeplemma` sie bestaetigte. **Lauf es als Erstes.**
- **`levelcheck.py`** ist in dieser Phase das schaerfste Werkzeug: in
  Marc 3 hat es **alle vier** neu gesetzten Mehrwort-Level korrigiert.
- **`hints.py`** ist jetzt nuetzlich: es nennt zu jeder unbelegten Form
  die stammverwandten Belege mit Zahl und Level.
- **`belegt.py` nimmt ein WORT, keine Buchnummer** — `belegt.py seigneur`.
  Mit einer Zahl meldet es die Zahl als unbelegte Wortform, und das sieht
  wie ein sauberer Lauf aus. **Lies seine KOPFZEILE, nicht nur die
  Vorschlagsliste darunter.** Der Agent fuer Jakobus 5 meldete, `belegt.py
  plaignez` verschweige das Lemma `plaindre` — es steht in der Kopfzeile
  (`das LEMMA hat 4, Lemma: plaindre`); nur die alphabetische
  Aehnlichkeitsliste darunter nennt es nicht.
- **`rueckwaerts.py` ist die Zweitmeinung** — und eine, die irrt: sie
  kennt den Vers nicht, sondern nur das Wort. Der Agent fuer Matthaeus 25
  fand dort `sages` als *Weise* (die Magier aus Kapitel 2) statt
  adjektivisch *klug* und `entre` als Praeposition statt als Imperativ
  von `entrer`. Wo ein Wort in keinem Zeugen eine fr-Spalte hat, faellt
  sie ganz aus (`d’Idumée`, Marc 3,8) — dann entscheidet der Vers.

**Die Parallele ist eine Vorlage, kein Gleichheitszeichen.** Der Agent
fuer Marc 3 hat den Block aus Mt 12,26 mit `lui-même` = *himself*
gemessen und trotzdem *itself* gesetzt, weil bei ihm ein Koenigreich
Subjekt ist und nicht Satan. Das ist richtig: wo dein Vers etwas anderes
sagt als der Parallelvers, gilt **dein** Vers — und der Unterschied
gehoert in deinen Bericht.

## Was Judas festgelegt hat

**`BINDUNGEN_FRA_NT.md` ist Pflichtlektuere vor der Arbeit — und noch
einmal vor der Abgabe.** Waehrend eines Pakets kommen Bindungen dazu, die
die Nachbaragenten praegen; der Agent fuer Matthaeus 5 hat drei davon
mitten im Lauf nachgezogen, weil er noch einmal hineingesehen hat. Dort steht,
wie Elisionen lemmatisiert werden, wie `ne … pas` gesetzt wird, warum
Relativ-`qui`/`que` deutsch *welche(r)* wird und nicht *der/die/das*, wann
ein Reflexiv ein Mehrwort bekommt und wann nicht — dazu die elf Reihen,
die das Pilotbuch gepraegt hat.

## Vor der Abgabe — jeder Lauf, jedesmal, mit DEINER Buchnummer

    cd anno-tools
    python3 selfcheck.py <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 levelcheck.py <NR> <KAP>
    python3 konvention.py <NR> <KAP>
    python3 sweeplemma.py <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 glosskollision.py --datei <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 kongruenz.py <NR> <KAP>
    python3 artikel.py <NR> <KAP>
    python3 mehrwort.py <NR> --datei=$ANNO_OUT/<NR>/ch<KAP>.json --kapitel=<KAP>
    python3 hilfsverb.py <NR> <KAP> --datei $ANNO_OUT/<NR>/ch<KAP>.json
    python3 folgencheck.py <NR> --kapitel <KAP> --datei $ANNO_OUT/<NR>/ch<KAP>.json
    python3 folgencheck.py <NR> --min 3 --kapitel <KAP> --datei $ANNO_OUT/<NR>/ch<KAP>.json
    python3 folgencheck.py <NR> --gegen <GEGEN> --min 5 --kapitel <KAP> --datei $ANNO_OUT/<NR>/ch<KAP>.json
    python3 qa.py --kapitel <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json

`qa.py --kapitel` will die drei Argumente **in dieser Reihenfolge**;
anders aufgerufen bricht es ab.

**`paketcheck.py <NR> <PAKET>` haelt die drei Kapitel des
Pakets gegeneinander** — es liest sie aus `$ANNO_OUT`, also auch, solange
keins eingesammelt ist. Das ist das einzige Werkzeug, das sieht, was die
Nachbaragenten gerade praegen; `folgencheck` kennt nur den fertigen
Bestand. Lauf es, wenn die Nachbarn abgegeben haben.

**`--kapitel <KAP>` ist bei `folgencheck` Pflicht, nicht Bequemlichkeit.**
Ohne den Filter umfasst der `--min 3`-Lauf das ganze Buch — in Matthaeus
sind das ueber 300 Bloecke, von denen ein Dutzend dein Kapitel angeht.
Drei Agenten in Folge haben sich die eigenen mit einem Skript
herausgezogen, und wer stattdessen `head` nimmt, sieht nur fremde.

**`levelcheck.py` steht mit Absicht vor `folgencheck.py`:** eine
Levelkorrektur loest nie eine Folgenkorrektur aus, umgekehrt aber schon.
In Matthaeus 21 hat es 24 Abweichungen gefunden, alle echt — die Level
der Zeugen sind CEFR fuer Englisch- und Deutschlernende und verfuehren
systematisch zum falschen Wert.

**Der dritte Lauf, `--gegen <GEGEN>`, prueft die Bindung ueber die
Buchgrenze.** Bis Markus verglich `folgencheck` nur innerhalb eines
Buches — bei den Synoptikern ist das die kleinere Haelfte der Arbeit.
Die Agenten fuer Marc 1 und Marc 2 haben sich diesen Vergleich beide
selbst gebaut; einer davon mit einem Positionsversatz, der sechs
Scheinabweichungen erzeugte. Jetzt macht es das Werkzeug. Eine
Abweichung ist auch hier kein Fehler: `autour` steht in Mt 3,4 vor dem
verschmolzenen `des` und in Marc 1,6 vor einem eigenen Artikeltoken,
und `est` ist einmal Kopula und einmal Hilfsverb.

**Der zweite `folgencheck`-Lauf mit `--min 3` ist kein Luxus.** Der
Standardlauf sieht erst Folgen ab vier Tokens; in Matthaeus 15 meldete er
zwei Abweichungen, mit `--min 3` waren es zwanzig — **sechs davon echte
Anschlussfehler**, darunter eine dreiwortige Folge, die das Paket selbst
praegt (`qui souille l'homme`).

**`levelcheck.py` und `konvention.py` lesen deine Abgabe** aus
`$ANNO_OUT/<NR>/ch<KAP>.json` und halten sie gegen den Bestand — sie
brauchen kein `--datei` und ihre Null ist eine echte Aussage. (Der Agent
fuer Matthaeus 20 hielt sie fuer reine Bestandslaeufe; sie sind es nicht.)
Sie sind zusammen mit `folgencheck` die drei Werkzeuge, die in dieser
Buchphase wirklich tragen.

`kongruenz.py` und `artikel.py` leiten ihre Referenz aus dem **Bestand**
ab — solange wenig fertig ist, sagt ihr sauberer Lauf ueber dein Kapitel
wenig; `artikel.py` schreibt das inzwischen selbst dazu. **Eine Null ist
dort keine Freigabe.** Die Kapitelnummer dahinter haelt fremde Treffer
aus deinem Bericht heraus.
Die drei letzten lesen mit `--datei` deine Abgabe. `folgencheck.py` ist
das einzige, das den **Anschluss an die Nachbarkapitel** prueft; in
Matthaeus Paket 2 hat es als einziges die zwei echten Anschlussfehler
gefunden.

## Woher du den Bestand nimmst — und woher nicht

**Frag die Werkzeuge, nie die Teildateien der Vorgaenger.** In
`$ANNO_OUT/<NR>/ch*.json` stehen die Abgaben frueherer Agenten, aber
beim Einsammeln werden sie **korrigiert** — angeglichene Reihen,
vereinheitlichte Level. Wer sie als Referenz liest, setzt einen Stand,
den es nicht mehr gibt. Der Agent fuer Matthaeus 4 hat daran einen
ganzen Messdurchgang verloren: `out/ch3.json` las `annoncé` = *spoken*,
der Bestand laengst *announced*.

Der Bestand ist, was `belegt.py`, `lexicon.py`, `folgenreihe.py` und
`parallelen.py` sagen. Auch `bindungen_*.md` ist eine Momentaufnahme —
was es unter UEBERNIMMT nennt, mit `folgenreihe.py` nachmessen.

**Und der Bestand kann sich waehrend deines Laufs aendern.** Der
Koordinator gleicht zwischen den Paketen an; in Matthaeus Paket 5 hat ein
Agent an eine Reihe gebunden, die Minuten spaeter korrigiert wurde. Jede
Messung traegt deshalb ihren Stand im Kopf (`Bestand: … · <commit>`).
Wenn dein Lauf lange dauert, **miss die Reihen vor der Abgabe noch einmal
nach** — `folgencheck.py` findet den Rest.

**Erklaere kein Kapitel fuer fertig, das `selfcheck.py` nicht sauber
durchlaeuft.** Jeder Rest aus `glosskollision` und `sweeplemma` wird am
Vers geprueft und im Bericht begruendet — aufgeloest oder verworfen.

## Feste Regeln

- **Ins Repo `/Users/dfoerd/Documents/projekte/bibel/bible-reader` wird NUR
  GELESEN. Nie schreiben.**
- **Starte keine eigenen Subagenten.**
- **Nie ein Grammatik-Tag in Klammern als Glosse („(futuro)", „(plural)")
  — immer ein echtes Wort der Zielsprache.**
- **Keinen Namen deuten, den der Text nicht selbst deutet.**
- Spanisch durchgehend **vosotros**, kein `ustedes`.
- Glossen duerfen umgangssprachlich sein; nur Gassensprache vermeiden.
- **Aufgeloest wird nur im Kollisionsvers.** Zwei Woerter mit derselben
  Glosse sind nur dann ein Fehler, wenn sie im selben Vers stehen.

## Dein Bericht

Was du entschieden hast und warum; welche Prompt- oder Werkzeugangaben du
am Quelltext **widerlegt** hast (der wertvollste Teil); welche
Kollisionen du aufgeloest und welche du bewusst stehen gelassen hast;
**was an der Werkzeugkette in der franzoesischen Richtung geklemmt hat**
— dieses Buch ist der Pilot, und was dir auffaellt, kommt allen weiteren
26 Buechern zugute; und welche Reihen die naechsten Kapitel uebernehmen
sollen.
