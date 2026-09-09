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

**Ein eigenes Hilfsskript erbt `ANNO_EDITION` nicht — und der Fehler ist
stumm.** Wer `import common` ohne die Variable ausfuehrt, bekommt von
`common.load_source(40)` den **deutschen** Matthaeus: gleiche Kapitel- und
Versschluessel, andere Verslaengen. Beim Agenten fuer Matteo 8 fiel es nur
an einem `IndexError` auf; waeren die deutschen Verse laenger gewesen,
haette das Skript stumm falsche `form`-Werte gebaut. Deshalb in **jedem**
eigenen Skript als erste Zeilen:

    import os
    os.environ['ANNO_EDITION'] = 'ita/riv1927mod'
    import common as C

## Eintragsformat

    {"pos": 3, "form": "servitore", "lemma": "servitore", "level": "B1",
     "de": "Knecht", "en": "servant", "es": "siervo", "fr": "serviteur"}

Die Spalten heissen **de · en · es · fr** — nicht en/es/fr/it. Eine
`it`-Spalte gibt es nicht; Italienisch ist die `form`.

Mehrwoerter tragen zusaetzlich `pos_end` (zusammenhaengend) **oder**
`parts` (getrennte Positionen). Positionen zaehlen ueber `text.split()`.

**`text.split()` ist der Massstab, nicht die Tokenzahl der
Vorbereitung.** Die Extrakte lassen alleinstehende Satzzeichen weg und
zaehlen deshalb weniger: in Giuda 1,4 stehen zwei einzelne Gedankenstriche
auf eigenen Positionen, der Extrakt nennt 583 Tokens und `text.split()`
585. Die Satzzeichen bekommen keinen Eintrag, aber ihre Position gehoert
mitgezaehlt — `selfcheck.py` rechnet genau das gegen.

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
- **Homographen bekommen ein eigenes Lemma.** `buildbook.py`
  vereinheitlicht die Level ueber das Lemma; wo zwei verschiedene
  Woerter zeichengleich sind, faellt das seltene auf das Level des
  haeufigen. Die seltenere Lesart traegt deshalb einen italienischen
  Klammerzusatz: `esseri` → `essere (sostantivo)` (B2) gegen `sono` →
  `essere` (A1). Im NT betrifft das vor allem die substantivierten
  Infinitive `potere`, `dovere`, `piacere`, `volere`, `essere`.
  Einzelheiten in `BINDUNGEN_ITA_NT.md` §15. Das ist **kein** Verstoss
  gegen „nie ein Grammatik-Tag in Klammern" — die Regel gilt fuer die
  vier Glossenspalten, nicht fuer das Lemma.
- **Die franzoesische Spalte elidiert durchgehend.** Wo das
  Franzoesische elidiert, steht die elidierte Form auch in der Glosse:
  `di` vor `Abraham` ist fr `d'`, nicht `de`; `il` vor `enfant` ist
  `l'`; `si` vor `arrêta` ist `s'`. Zehn Formen sind betroffen —
  `se me te ne le la de que ce je` —, das aspirierte `h` ist die
  Ausnahme (`la hache`). **`elision.py` prueft das — mit `--datei`,
  sonst liest es die gebaute Datei und sagt nichts ueber dein
  Kapitel.** Seine Null ist ein Ziel, kein Muss: wo die Zielsprache
  umstellt, steht die nicht elidierte Form zu Recht. `lo si salerà` ist
  franzoesisch „on le salera" — `le`, nicht `l'`. Solche Reste
  begruenden statt setzen;
  es misst das aspirierte `h` am franzoesischen Quelltext, statt es zu
  raten. Einzelheiten in Reihe 38.
- **`si` ist mehrdeutig:** Reflexivpronomen (*si lavò*), unpersoenliches
  *man* (*si dice*) und Passiversatz. Am Vers entscheiden; das Lemma ist
  in allen drei Faellen `si`, die Glossen sind es nicht.

## Was Giuda festgelegt hat

**`BINDUNGEN_ITA_NT.md` ist Pflichtlektuere vor der Arbeit — und noch
einmal vor der Abgabe.** Das Pilotbuch hat dort vierzehn Reihen gesetzt,
jede mit der Stelle: wie Elisionen lemmatisiert werden (auf den
**semantischen Kopf**: `nell'amore` → `amore`, aber `nelle` → `in`), wie
die verschmolzene Praeposition glossiert wird, warum das Lemma eines
angehaengten Pronomens immer der Infinitiv ist — auch bei Imperativ und
Gerundium —, wann ein Reflexiv ein Mehrwort bekommt und warum das
essere-Hilfsverb darin seine woertliche Kopula-Glosse behaelt.

**Welches Werkzeug welchen Bestand liest — hier irren sich alle.**

- **Die Positionen zaehlen ueber `text.split()`, die `form` nicht.**
  `split()` liefert `figlio,` mit Komma; die `form` steht **ohne**
  umschliessende Satzzeichen, also durch `common.strip_punct`. Zwei
  Agenten desselben Pakets sind darueber gestolpert und haben von
  `selfcheck.py` 123 bzw. 130 Meldungen bekommen, die wie ein
  Ausrichtungsproblem aussehen und keins sind. Ein eigenes Bauskript
  braucht ausserdem `sys.path.insert(0, 'anno-tools')` **und**
  `os.environ['ANNO_EDITION']` vor `import common` (Reihe 88).
- **`fixgloss.py verse <NR> <KAP> <VERS>` zeigt den ganzen annotierten
  Vers — mit den Mehrwortspannen.** Das ist die einzige Ansicht, in der
  sichtbar wird, ob eine Wendung einen Mehrworteintrag traegt oder nicht;
  `folgenreihe.py` zeigt die Wort-fuer-Wort-Reihe und die Mehrwoerter
  getrennt, und wer die beiden Zahlen nicht selbst gegeneinanderhaelt,
  sieht die Luecke nicht. Der Agent fuer Matteo 14 hat damit gefunden,
  dass 2,16 `mandò a uccidere` **kein** Mehrwort traegt — und deshalb
  zwei erfundene Mehrwoerter wieder eingespart. **Vor jeder Entscheidung
  ueber ein Mehrwort den Vergleichsvers so ansehen, nicht nur die Reihe.**
- **`belegt.py` ueber viele Formen: `--formen <datei>`, nie `xargs`.**
  `xargs` liest den Apostroph als Anfuehrungszeichen und klebt jede
  elidierte Form (`c'è`, `dell'uomo`, `l'albero`) mit ihren Nachbarn zu
  einer einzigen Sammelzeile zusammen — der Lauf sieht sauber aus und hat
  nichts geprueft. Eine Form je Zeile in eine Datei, dann
  `python3 belegt.py --formen work/<KAP>/formen.txt`.
- **`belegt.py`, `lexicon.py`, `hints.py` und `folgenreihe.py` lesen den
  ITALIENISCHEN Bestand**, nicht den der Zeugen. `belegt.py Signore`
  meldete im Pilotbuch eine Fehlanzeige, obwohl das Wort in jeder
  anderen Ausgabe hundertfach steht — die italienische Anno war leer. Solange wenig fertig ist, ist ihre Null eine **leere Messung**,
  kein Befund; `hints.py` fuehrt aus demselben Grund fast jede Wortform
  unter den unbelegten. Sie werden mit jedem Buch nuetzlicher.
- **Nur `rueckwaerts.py` fragt die it-Spalte der Zeugen.** Es ist in
  dieser Phase deine einzige Verbindung zum vorhandenen Bestand — und
  eine Zweitmeinung, die irrt: sie kennt den Vers nicht, sondern nur das
  Wort. Wo ein Wort in keinem Zeugen eine it-Spalte hat, faellt sie ganz
  aus; dann entscheidet der Vers.
- **`belegt.py` nimmt ein WORT, keine Buchnummer** — `belegt.py signore`.
  Mit einer Zahl meldet es die Zahl als unbelegte Wortform, und das sieht
  wie ein sauberer Lauf aus.

**Der spanische Zeuge steht durchgehend auf `ustedes`.** Die es-Spalte
wird aus ihm nie uebernommen — hier gilt **vosotros**.

**`glosskollision.py` vergleicht nur Einzelworteintraege.** Bei einer
Mehrwortwendung ist eine geteilte Glosse keine Kollision, sondern die
Wendung selbst. Das ist Absicht, kein blinder Fleck.

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
    python3 elision.py --datei $ANNO_OUT/<NR>/ch<KAP>.json <NR> <KAP>
    python3 verschmelzung.py --datei $ANNO_OUT/<NR>/ch<KAP>.json <NR> <KAP>
    python3 qa.py --kapitel <NR> <KAP> $ANNO_OUT/<NR>/ch<KAP>.json

`qa.py --kapitel` will die drei Argumente **in dieser Reihenfolge**;
anders aufgerufen bricht es ab.

**`--kapitel <KAP>` ist bei `folgencheck` Pflicht, nicht Bequemlichkeit.**
Ohne den Filter umfasst der `--min 3`-Lauf das ganze Buch.

**Der zweite `folgencheck`-Lauf mit `--min 3` ist kein Luxus.** Der
Standardlauf sieht erst Folgen ab vier Tokens.

**`verschmelzung.py` prueft, was `glosskollision.py` nicht sehen kann.**
`nella` traegt Praeposition UND Artikel; `su` und `sulla` stehen aber auf
demselben Lemma und fallen in `glosskollision.py` deshalb in denselben
Topf, statt gegeneinander gemessen zu werden. Abschnitt A ist scharf und
soll leer sein. Abschnitt B (`--verdacht`) ist eine Verdachtsliste, in
der die Nullantwort oft richtig ist — vor dem Possessiv, vor dem
Eigennamen und vor dem Relativpronomen kann keine Zielsprache den
Artikel setzen, und diese drei Stellungen sind schon ausgenommen.

**`levelcheck.py` steht mit Absicht vor `folgencheck.py`:** eine
Levelkorrektur loest nie eine Folgenkorrektur aus, umgekehrt aber schon.
Die Level der Zeugen sind CEFR fuer Englisch-, Deutsch- und
Franzoesischlernende und verfuehren systematisch zum falschen Wert.

**Solange wenig italienischer Bestand dasteht, sind mehrere dieser
Laeufe notwendig duenn** — `levelcheck`, `konvention`, `folgencheck`,
`artikel` und `kongruenz` leiten ihre Referenz daraus ab. **Eine Null ist
dort keine Freigabe, sondern eine schmale Messung**; `konvention.py`,
`artikel.py` und `kongruenz.py` schreiben es inzwischen selbst dazu. Was
von Anfang an traegt, sind `selfcheck`, `qa`, `sweeplemma`,
`glosskollision`, `mehrwort` und der Vers selbst.

**`folgencheck.py --gegen <GEGEN>` prueft die Bindung ueber die
Buchgrenze** und ist ab dem zweiten Buch Pflicht:

    python3 folgencheck.py <NR> --gegen <GEGEN> --min 5 --kapitel <KAP> --datei $ANNO_OUT/<NR>/ch<KAP>.json

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
— die Richtung ist jung, und was dir auffaellt, kommt allen weiteren
Buechern zugute; und welche Reihen dein Kapitel praegt und welche es
uebernimmt. Reihen, die ueber dein Kapitel hinaus gelten, gehoeren in
`BINDUNGEN_ITA_NT.md` — schreib sie dort hinein, mit der Stelle.
