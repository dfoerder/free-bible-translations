# Italienisches NT annotieren — was vorliegt und was zu tun ist

**Auftrag:** die Buecher 40–66 des `riv1927mod` mit Wort-fuer-Wort-Glossen
in **Deutsch, Englisch, Spanisch und Franzoesisch**. Die dritte Richtung:
im deutschen Durchgang war Italienisch eine Glossenspalte, im
franzoesischen ebenso. Jetzt ist es der Text.

**Stand: Werkzeugkette umgebaut und gemessen, Pilotbuch Giuda laeuft.**

## Was da ist

```
bibles-translations/ita/riv1927mod/          66 Quelltextdateien
bible-reader/bibles/ita/riv1927mod/          dieselben, App-Kopie
bible-reader/bibles/ita/riv1927mod/anno/     existiert noch nicht
anno-quellen/ita/riv1927mod/                 existiert noch nicht
```

Die Registry in `index.html` fuehrt `ita-riv1927mod` mit `hasAnno: false`,
`annoDir: null`, `annoSuffix: null`. Nach dem ersten gebauten Buch sind
diese drei zu setzen — Vorbild ist der Eintrag `deu-l1912mod`.

## Die Zeugen

Fuer die italienische Arbeit ist **RIV der Quelltext**, an ihre Stelle
treten die vier Zielsprachen:

```
de   deu/l1912mod      Glossen en · es · fr · it     66 Buecher
en   eng/web           Glossen de · es · fr · it     66 Buecher
es   spa/rv1909mod     Glossen en                    66 Buecher
fr   fra/lsg1910mod    Glossen de · en · es · it     waechst
```

**Der franzoesische Zeuge ist die MODERNISIERTE LSG**, nicht die von
1910. Der deutsche Bestand hat gegen die alte gearbeitet — deshalb steht
`ZEUGE['fr']` weiter auf `fra/lsg1910`; die italienische Ausgabe
ueberschreibt das ueber ihren Schluessel `zeugen` in `common.py`. Wer die
alte naehme, legte eine `fr`-Glosse neben einen Text, den die App gar
nicht mehr zeigt.

## Die Bruecke — besser als im Franzoesischen

`eng/web`, `deu/l1912mod` und `fra/lsg1910mod` tragen **alle drei eine
it-Spalte**, und jeder einzelne von ihnen deckt fuer sich schon alle vier
Zielsprachen ab: der Quelltext liefert die eine, seine drei uebrigen
Spalten die anderen drei. Im Franzoesischen brauchte es dafuer noch zwei
Zeugen nebeneinander.

Gemessen ueber das ganze NT (159 338 Tokens, 11 476 Wortformen):

```
GLOSSE     154 546   97,0 %   das Token steht im Bestand als it-Glosse
TEIL           721    0,5 %   nur innerhalb einer mehrwortigen it-Glosse
KLITIKON       824    0,5 %   Verb + angehaengtes Pronomen, beide belegt
ELISION        762    0,5 %   nur die Haelften der Elision sind belegt
UNBELEGT     2 485    1,6 %   die eigentliche Arbeit
```

Am Pilotbuch: Giuda hat 583 Tokens, davon **402 im Vers der Zeugen
selbst** (69 %), 169 ueber den uebrigen Bestand, **12 unbelegt** —
`carissimi`, `dominata`, `gloriosi`, `impegnavo`, `insoddisfatti`,
`istinto`, `originaria`, `ritegno`, `trasformano`, `vivranno`.

## Was an der Werkzeugkette zu tun war — erledigt

- **`common.py`** fuehrt `ita/riv1927mod` als sechste Ausgabe
  (`langs` de/en/es/fr, Anno-Suffix `_riv1927mod_multi.json`) und kennt
  jetzt einen **Zeugen-Ueberschreiber je Ausgabe** (`zeugen`).
- **`rueckwaerts.py`** war auf `fr` fest verdrahtet: Schluesselspalte,
  Zielspalten und die zwei Zeugen standen ausgeschrieben da. Alle drei
  leiten sich jetzt aus `C.LANG`/`C.LANGS` ab, und die Zeugenliste
  entsteht aus der Ausgabentabelle — ein Zeuge taugt, wenn er annotiert
  ist, seine Quelltextsprache eine Zielspalte ist und er eine Spalte in
  der Sprache des Quelltextes fuehrt. Fuer Franzoesisch kommen dieselben
  zwei heraus wie bisher (an Markus 1–3 zeilengleich nachgemessen), fuer
  Italienisch drei.
- **Zwei neue Schichten in `rueckwaerts.py`:**
  - `KLITIKON` — `dirgli` = `dire` + `gli`. Die Zeugen glossieren *to
    tell him* als zwei Woerter, nie als eines; ohne diese Schicht
    stuenden 824 NT-Tokens unter „UNBELEGT — hier ist die Arbeit",
    obwohl Verb und Pronomen beide hundertfach dastehen.
  - Die `ELISION`-Schicht **ergaenzt den verschluckten Vokal**: `nell'`
    ist keine Wortform, `nella` ist eine. Franzoesisch bleibt das
    elidierte Stueck als eigene Glosse stehen (`qu'`), italienisch nicht.
- **`qa.py`, `hints.py`, `glosskollision.py`, `hilfsverb.py`** haben je
  eine italienische Liste bekommen. Ohne sie waere jede dieser vier
  Pruefungen **lautlos ausgefallen** — dieselbe Falle, die im
  franzoesischen Durchgang dreimal zugeschlagen hat.
- **`kongruenz.py`** las die `it`-Spalte, die es in dieser Richtung nicht
  gibt. Seine Possessiv- und Genusproben sind jetzt an `IT_SPALTE`
  gebunden und **sagen im Lauf, dass sie nicht gelaufen sind**; es
  bleiben die spanische und die franzoesische Numerusprobe. Dabei kam
  heraus, dass seine Probe auf das reflexive Perfekt am deutschen Lemma
  `sich …` und an den Lemmata `haben`/`sein` haengt — im franzoesischen
  Durchgang hat sie deshalb **nie getroffen**. Beides ist jetzt je
  Quelltextsprache hinterlegt.
- **`fravorb.py`** ist zu `annovorb.py` verallgemeinert; `fravorb.py` und
  `itavorb.py` sind zweizeilige Einstiege darauf, die je ihre Ausgabe
  festhalten. Die franzoesischen Prompts kommen zeichengleich heraus
  (an Johannes 1–3 nachgemessen). `PROMPT_BAUSTEIN_FRA.md` heisst jetzt
  `PROMPT_BAUSTEIN_FR.md`, damit der Name aus dem Sprachkuerzel folgt.
- **`vorgabecheck.py`** kennt `RIV1927mod` als eigene Ausgabe und die
  italienischen Buchnamen im Fremdbuch-Schutz.

## Was am Italienischen anders ist

Die drei Bauformen, die es im Deutschen so nicht gibt und die alle drei
**ein Token** sind:

```
Elision            l'uomo · dell'acqua · anch'essi · quarant'anni
                   2 117 Tokens in 580 Formen
angehaengtes       dirgli · vedendolo · svegliatosi · opponetevi
Pronomen           824 Tokens in 568 Formen
verschmolzene      nel · nella · dei · degli · alla · sulla · col
Praeposition       traegt Praeposition UND Artikel
```

Dazu die Apokope (`cuor`, `Signor`, `far`) — die `form` bleibt verkuerzt,
das Lemma ist die volle.

## Was aus der franzoesischen Arbeit uebertragbar ist

Alles Verfahrensmaessige: ein Agent je Kapitel, Pakete zu drei Kapiteln,
`paketvorb.py` vor der Arbeit, `folgencheck.py` beim Einsammeln, beide
Promptpruefungen vor dem Start. **Nicht uebertragbar** sind die
inhaltlichen Bindungen: `BINDUNGEN_FRA_NT.md` gilt fuer den
franzoesischen Text; die italienische Entsprechung schreibt das
Pilotbuch.
