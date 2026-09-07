# Der gemeinsame Prompt-Baustein — italienisches NT

**Platzhalter: `<NR>` = Buchnummer, `<KAP>` = Kapitelnummer, `<BUCH>` =
Buchname, `<SCRATCH>` = Scratchpad-Verzeichnis des Buches.**

Die Schwester von `PROMPT_BAUSTEIN.md` (deutsch) und
`PROMPT_BAUSTEIN_FR.md` (franzoesisch). Was dort steht, gilt hier
sinngemaess weiter; **dieser Baustein sagt, was anders ist.** Wer mehrere
liest, liest doppelt — fuer die italienische Arbeit gilt allein dieser.

---

Du annotierst **<BUCH> (Buch <NR>), Kapitel <KAP>** der italienischen
Riveduta 1927 in ihrer modernisierten Fassung `riv1927mod` mit
Wort-fuer-Wort-Glossen in **Deutsch, Englisch, Spanisch und
Franzoesisch** plus CEFR-Level.

Das ist die **dritte Richtung**: bis Maleachi war Deutsch der annotierte
Text, seit dem NT-Durchgang Franzoesisch — Italienisch war beide Male
eine Glossenspalte. Jetzt ist Italienisch der Text.

## Wo alles liegt

Arbeitsverzeichnis: `/Users/dfoerd/Documents/projekte/bibel/bibles-translations`

    export ANNO_EDITION=ita/riv1927mod
    export ANNO_OUT=<SCRATCH>/out

**Beide sind Pflicht.** Ohne `ANNO_EDITION` arbeitet die ganze Werkzeug-
kette auf dem deutschen Text weiter — sie bricht dabei nicht ab, sie
antwortet nur zum falschen Buch. Setz sie als Erstes und pruef sie:

    python3 -c "import common as C; print(C.EDITION, C.LANGS)"
    → ita/riv1927mod ['de', 'en', 'es', 'fr']

Alle Werkzeuge werden **aus `anno-tools/` heraus** aufgerufen.

Deine Abgabe: `$ANNO_OUT/<NR>/ch<KAP>.json`
Dein Arbeitsverzeichnis fuer alles andere: `$ANNO_OUT/../work/<KAP>/` —
jede Zwischendatei und jedes Hilfsskript dorthin, nicht neben die Abgabe.

## Eintragsformat

    {"pos": 3, "form": "servitore", "lemma": "servitore", "level": "B1",
     "de": "Knecht", "en": "servant", "es": "siervo", "fr": "serviteur"}

Die Spalten heissen **de · en · es · fr** — nicht en/es/fr/it. Eine
`it`-Spalte gibt es nicht; Italienisch ist die `form`.

Mehrwoerter tragen zusaetzlich `pos_end` (zusammenhaengend) **oder**
`parts` (getrennte Positionen). Positionen zaehlen ueber `text.split()`.

## Dein wichtigstes Werkzeug: `rueckwaerts.py`

    python3 rueckwaerts.py <NR> <KAP> -o $ANNO_OUT/../work/<KAP>/rw.md

`eng/web`, `deu/l1912mod` und (soweit annotiert) `fra/lsg1910mod` tragen
alle drei eine **it-Spalte**. Jeder ihrer Eintraege ist damit eine
vollstaendige Zeile de · en · es · fr, und die it-Spalte ist ihr
Schluessel.

Ueber das ganze italienische NT gemessen (159 338 Tokens):

    GLOSSE     97,0 %   das Token steht im Bestand als it-Glosse
    TEIL        0,5 %   nur innerhalb einer mehrwortigen it-Glosse
    KLITIKON    0,5 %   Verb + angehaengtes Pronomen, beide Teile belegt
    ELISION     0,5 %   nur die Haelften der Elision sind belegt
    UNBELEGT    1,6 %   hier ist die Arbeit

Der Extrakt ist nach Versen geordnet und stellt die **VERS**-Schicht
voran: das Wort steht als it-Glosse in genau deinem Vers der Zeugen.

**Was die VERS-Schicht liefert, ist ein starker Vorschlag und keine
Vorgabe.** Die Zeugen sind Uebersetzungen, keine Interlinearversionen:
wo RIV anders gliedert als WEB oder Luther, steht die Zeile am falschen
Wort. Lies den Vers.

## Was aus den Zeugen NICHT uebernommen wird

- **Kein Lemma.** Das Lemma im Zeugen ist englisch, deutsch oder
  franzoesisch. Deins ist italienisch: Verben in den Infinitiv (`disse`
  → `dire`), Nomen in den Singular (`discepoli` → `discepolo`),
  Adjektive ins Maskulinum Singular (`amati` → `amato`), Artikel und
  Praepositionen normalisiert (`il`/`lo`/`la`/`i`/`gli`/`le`/`l'` →
  `il`, `del`/`della`/`dei`/`degli`/`delle`/`dell'` → `di`,
  `nel`/`nella`/`nei` → `in`, `al`/`alla`/`ai` → `a`).
- **Kein Level.** Das Level im Zeugen ist CEFR fuer Englisch-, Deutsch-
  oder Franzoesischlernende. Deins ist CEFR **fuer Italienischlernende**.
  Der Extrakt schreibt bei jedem Level dazu, aus welcher Ausgabe es
  stammt — das ist eine Warnung, keine Empfehlung.

## Italienische Besonderheiten

- **Elision ist EIN Token.** `l'uomo`, `dell'acqua`, `anch'essi`,
  `dov'era`, `quest'uomo`, `un'altra`, `quarant'anni` stehen im Text als
  ein Wort und bekommen **einen** Eintrag, dessen Glossen beide Teile
  abdecken: `dell'acqua` → de *des Wassers* · en *of the water* · es
  *del agua* · fr *de l'eau*. Nicht in zwei Eintraege zerlegen — die
  Positionen zaehlen ueber `text.split()`. Im NT sind das 2 117 Tokens
  in 580 Formen.
- **Das angehaengte Pronomen ist EIN Token.** `dirgli`, `vedendolo`,
  `svegliatosi`, `portargli`, `darvi`, `opponetevi`, `gliene` — Verb und
  Klitikon stehen zusammengeschrieben und bekommen **einen** Eintrag:
  `dirgli` → de *ihm zu sagen* · en *to tell him* · es *decirle* · fr
  *lui dire*. Im NT 824 Tokens in 568 Formen. Das Lemma ist der
  **Infinitiv des Verbs** (`dirgli` → `dire`), nicht die zusammen-
  gesetzte Form; `rueckwaerts.py` zeigt dir unter `KLITIKON` beide Teile
  einzeln.
- **Die verschmolzene Praeposition ist EIN Token.** `nel`, `nella`,
  `dei`, `degli`, `alla`, `sulla`, `col` tragen Praeposition **und**
  Artikel. Die Glossen tragen beides mit (`nella` → de *in der* · en *in
  the* · es *en la* · fr *dans la*); das Lemma ist die blosse
  Praeposition.
- **Apokope.** `cuor`, `amor`, `Signor`, `far`, `andar`, `voler` sind
  verkuerzte Formen. Das Lemma ist die volle (`cuore`, `amore`,
  `signore`, `fare`); die `form` bleibt, wie sie im Text steht.
- **Grossschreibung.** Italienische Nomen sind klein — wie im
  Franzoesischen und anders als im Deutschen. `artikel.py` findet das
  Nomen deshalb ueber die **deutsche** Glosse: eine schlampige
  `de`-Spalte macht diese Pruefung blind.
- **`kongruenz.py` prueft hier weniger.** Seine Possessiv- und
  Genusproben lesen die `it`-SPALTE, die es in dieser Richtung nicht
  gibt; es sagt das im Lauf selbst und prueft nur noch die spanische und
  die franzoesische Numerusprobe. **Seine Null ist hier keine Freigabe.**
- **`voi` ist im Italienischen 2. Person Plural.** Es wird spanisch
  **vosotros**, franzoesisch *vous*, deutsch *ihr*. `Ella` steht im NT
  elfmal und ist das feminine *sie*, nicht die Hoeflichkeitsform. Am
  Vers entscheiden.
- **`glosskollision.py` vergleicht klein.** Ein Paar, das sich allein in
  der Grossschreibung trennt, ist **keine** Kollision — nicht aufloesen.
- **`si` ist mehrdeutig:** Reflexivpronomen (*si lavò*), unpersoenliches
  *man* (*si dice*) und Passiversatz. Am Vers entscheiden; das Lemma ist
  in allen drei Faellen `si`, die Glossen sind es nicht.

## Dies ist das Pilotbuch

Der italienische Bestand ist **leer**. Das heisst konkret:

- `parallelen_<nr>_<kap>.md` und `lexicon.py` antworten leer — es gibt
  noch nichts, womit dein Vers gleichlauten koennte.
- `rueckwaerts.py` hat noch keine **BESTAND**-Schicht; alles kommt aus
  den Zeugen.
- `folgencheck.py --gegen` hat nichts zu vergleichen.
- **`BINDUNGEN_ITA_NT.md` gibt es noch nicht — du schreibst sie.** Wie
  Elisionen und Klitika lemmatisiert werden, wie die verschmolzenen
  Praepositionen glossiert werden, wann ein Reflexiv ein Mehrwort
  bekommt und wann nicht: was du entscheidest, praegt alle 27 Buecher.
  Leg die Datei in `anno-tools/BINDUNGEN_ITA_NT.md` an und schreib jede
  Reihe hinein, die du gepraegt hast, mit der Stelle, an der sie steht.

Der Bestand der **anderen** Sprachen traegt dagegen voll: `belegt.py`,
`folgenreihe.py` und `rueckwaerts.py` fragen ihn.

- **`belegt.py` nimmt ein WORT, keine Buchnummer** — `belegt.py signore`.
  Mit einer Zahl meldet es die Zahl als unbelegte Wortform, und das sieht
  wie ein sauberer Lauf aus.
- **`folgenreihe.py "<folge>"` sucht die ZEICHENKETTE im Quelltext, nicht
  das Lemma.** Solange der italienische Bestand leer ist, antwortet es
  leer — das ist kein Befund.
- **`hints.py`** nennt zu jeder unbelegten Form die stammverwandten
  Belege mit Zahl und Level.
- **`rueckwaerts.py` ist eine Zweitmeinung, und eine, die irrt:** sie
  kennt den Vers nicht, sondern nur das Wort. Wo ein Wort in keinem
  Zeugen eine it-Spalte hat, faellt sie ganz aus — dann entscheidet der
  Vers.

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
    python3 qa.py --kapitel <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json

`qa.py --kapitel` will die drei Argumente **in dieser Reihenfolge**;
anders aufgerufen bricht es ab.

**`--kapitel <KAP>` ist bei `folgencheck` Pflicht, nicht Bequemlichkeit.**
Ohne den Filter umfasst der `--min 3`-Lauf das ganze Buch.

**Der zweite `folgencheck`-Lauf mit `--min 3` ist kein Luxus.** Der
Standardlauf sieht erst Folgen ab vier Tokens.

**`levelcheck.py` steht mit Absicht vor `folgencheck.py`:** eine
Levelkorrektur loest nie eine Folgenkorrektur aus, umgekehrt aber schon.
Die Level der Zeugen sind CEFR fuer Englisch-, Deutsch- und
Franzoesischlernende und verfuehren systematisch zum falschen Wert.

**Im Pilotbuch sind mehrere dieser Laeufe notwendig leer** —
`levelcheck`, `konvention`, `folgencheck` und `artikel` leiten ihre
Referenz aus dem italienischen Bestand ab, und der ist leer. **Eine Null
ist dort keine Freigabe, sondern eine leere Messung.** Was wirklich
traegt, sind `selfcheck`, `qa`, `sweeplemma`, `glosskollision`,
`mehrwort` und der Vers selbst.

**`paketcheck.py <NR> <PAKET>` haelt die Kapitel eines Pakets
gegeneinander** — es liest sie aus `$ANNO_OUT`, also auch, solange keins
eingesammelt ist. Lauf es, wenn die Nachbarn abgegeben haben.

**Erklaere kein Kapitel fuer fertig, das `selfcheck.py` nicht sauber
durchlaeuft.** Jeder Rest aus `glosskollision` und `sweeplemma` wird am
Vers geprueft und im Bericht begruendet — aufgeloest oder verworfen.

## Woher du den Bestand nimmst — und woher nicht

**Frag die Werkzeuge, nie die Teildateien der Vorgaenger.** In
`$ANNO_OUT/<NR>/ch*.json` stehen die Abgaben frueherer Agenten, aber
beim Einsammeln werden sie **korrigiert** — angeglichene Reihen,
vereinheitlichte Level. Wer sie als Referenz liest, setzt einen Stand,
den es nicht mehr gibt.

**Und der Bestand kann sich waehrend deines Laufs aendern.** Der
Koordinator gleicht zwischen den Paketen an. Jede Messung traegt deshalb
ihren Stand im Kopf (`Bestand: … · <commit>`). Wenn dein Lauf lange
dauert, miss die Reihen vor der Abgabe noch einmal nach.

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
**was an der Werkzeugkette in der italienischen Richtung geklemmt hat**
— dieses Buch ist der Pilot, und was dir auffaellt, kommt allen weiteren
26 Buechern zugute; und welche Reihen du in `BINDUNGEN_ITA_NT.md`
festgelegt hast.
