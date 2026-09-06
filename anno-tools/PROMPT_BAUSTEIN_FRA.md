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

## Dein wichtigstes Werkzeug: `rueckwaerts.py`

    python3 rueckwaerts.py <NR> <KAP> -o $ANNO_OUT/../work/<KAP>/rw.md

`eng/web` und `deu/l1912mod` sind **beide vollstaendig annotiert und
tragen beide eine fr-Spalte**. Zusammen decken sie genau deine vier
Zielsprachen ab. Ueber die fr-Spalte als Schluessel liegt fuer 98 Prozent
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
- **Grossschreibung.** Franzoesische Nomen sind klein. `artikel.py` und
  `kongruenz.py` finden das Nomen deshalb ueber die **deutsche** Glosse —
  das heisst: eine schlampige `de`-Spalte macht zwei Pruefungen blind.
- **`vous` ist im Franzoesischen Hoeflichkeitsform UND Plural.** Am Vers
  entscheiden, welches gemeint ist; im Spanischen wird daraus in aller
  Regel **vosotros**, nicht `usted`.

## Der Bestand waechst erst

Beim ersten Buch ist die franzoesische Anno noch leer. Das heisst:

- **`hints.py` meldet alles als unbelegt** — das ist richtig und kein
  Befund. Ab dem zweiten Buch wird es nuetzlich.
- **`lexicon.py`, `parallelen.py <NR> <KAP>`, `levelcheck.py`,
  `konvention.py`, `sweeplemma.py`** antworten leer, solange wenig
  fertig ist. Trotzdem laufen lassen: ein leerer Lauf ist eine Aussage,
  ein nicht gelaufener nicht.
- **`belegt.py` nimmt ein WORT, keine Buchnummer** — `belegt.py seigneur`.
  Mit einer Zahl meldet es die Zahl als unbelegte Wortform, und das sieht
  wie ein sauberer Lauf aus.
- **`rueckwaerts.py` tritt an ihre Stelle**, bis der eigene Bestand
  traegt.

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
    python3 konvention.py <NR> <KAP>
    python3 levelcheck.py <NR> <KAP>
    python3 sweeplemma.py <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 glosskollision.py --datei <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json
    python3 kongruenz.py <NR>
    python3 artikel.py <NR>
    python3 mehrwort.py <NR> --datei=$ANNO_OUT/<NR>/ch<KAP>.json --kapitel=<KAP>
    python3 hilfsverb.py <NR> <KAP> --datei $ANNO_OUT/<NR>/ch<KAP>.json
    python3 folgencheck.py <NR> --datei $ANNO_OUT/<NR>/ch<KAP>.json
    python3 qa.py --kapitel <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json

`qa.py --kapitel` will die drei Argumente **in dieser Reihenfolge**;
anders aufgerufen bricht es ab.

`kongruenz.py` und `artikel.py` lesen den **Bestand**, nicht deine Datei —
solange wenig fertig ist, sagt ihr sauberer Lauf ueber dein Kapitel wenig.
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
