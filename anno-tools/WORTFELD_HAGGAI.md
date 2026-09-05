# Wortfeld Haggai (37)

Zwei Kapitel, 38 Verse, 935 Tokens, 28 Mehrwoerter. Ein Paket, zwei
Agenten. `paketcheck` Abschnitt A und C: **leer**.

## Die Reihen

```
HERR          A1  LORD · SEÑOR · ÉTERNEL · SIGNORE
Heerschar     C1  hosts · ejércitos · armées · eserciti     (112, einstimmig)
der + Heerschar   of the · de los · des · degli             (6:4 gemessen)
Statthalter   C1  governor · gobernador · gouverneur · governatore
Hoherpriester C1  high priest · sumo sacerdote · grand prêtre · sommo sacerdote
Herrlichkeit  C1  glory · gloria · gloire · gloria
Trümmer       B2  ruins · ruinas · ruines · rovine
erschüttern   C1  shake · sacudir · ébranler · scuotere
Gewandzipfel  C1  garment fold · borde del vestido · bord du vêtement · falda della veste
Zipfel        C1  skirt · orla · pan · lembo
später        B1  latter · posterior · postérieure · posteriore
umstürzen     B2  overthrow · derrocar · renverser · rovesciare
Getreidebrand C1  blight · tizón · nielle · carbonchio
Kornhaufen    B2  heap of grain · montón de grano · tas de grain · mucchio di grano
Saatgut       B2  seed · semilla · semence · semente
Scheune       B2  barn · granero · grenier · granaio
Siegelring    C1  signet ring · anillo de sello · anneau à cachet · anello con sigillo
getäfelt      C1  paneled · revestidas de madera · lambrissées · rivestite di legno
löchrig       B2  full of holes · rota · percée · forata
zerblasen     C2  blow away · disipo de un soplo · souffle dessus · soffio via
```

Vier davon sind neu gepraegt: `getäfelt`, `löchrig`, `zerblasen`,
`Gewandzipfel`. `zerblasen` steht auf C2, weil die *zer*-Familie im
Bestand von `zerbrechen` B1 bis `zerbersten` C2 reicht und ein Hapax
dieser Art ans obere Ende gehoert.

## Die `spricht`-Stellungsregel — und meine falsche Zahl

Fast jeder zweite Vers traegt die Botenformel. Ich hatte in beide
Prompts geschrieben: „184 Vorkommen von ‚So spricht der HERR', **alle**
mit `parle`". **Beide Agenten haben unabhaengig nachgemessen und beide
Zahlen widerlegt:**

```
vorangestellt   223 parle : 4 dit    (Jer 14,10 · 23,31 · 29,10 · Obadja 1,8)
nachgestellt    264 dit  : 46 parle
„spricht der HERR der Heerscharen", nachgestellt   6 dit : 2 parle
```

Die Regel traegt, die Behauptung „alle" nicht. Ich hatte mir mit
`most_common(2)` zwei von **sechs** Varianten ausgeben lassen und aus
den zwei auf alle geschlossen — derselbe Fehler wie in Jona, wo ich ein
Verszitat bei 95 Zeichen abgeschnitten hatte. Dagegen steht seither
`folgenreihe.py`, das nichts abschneidet.

**Der Konflikt, den kein Werkzeug gemeldet hat:** die 8-Token-Parallele
zu 2,23 ist Jesaja 22,25 — derselbe Block „An jenem Tag, spricht der
HERR der Heerscharen" — und der Bestand liest dort **nachgestellt
`parle`**. Der Agent hat die Stellungsregel ueber die Parallelenregel
gestellt, weil LSG in Haggai 2,23 selbst „dit l'Éternel des armées"
schreibt. Jesaja 22,25 steht in `NACHLESE_BESTAND.md`.

## Die drei Bloecke ueber die Kapitelgrenze

Nach der Zefanja-Erfahrung standen sie diesmal **fest im Prompt**, am
Bestand gemessen. Alle drei sind zeichengleich:

```
Statthalter von Juda und        1,1  · 2,2
am vierundzwanzigsten Tag des   1,15 · 2,20
so spricht der HERR             1,5  · 2,6
```

Beide Agenten haben zusaetzlich mit `kreuz.py` gegeneinander geprueft.
Der Agent fuer Kapitel 1 fand dabei eine Abweichung, die der Prompt
nicht abgedeckt hatte: `am` stand bei ihm als `on the · **al** · le ·
il` (aus der Vorlage Hesekiel 26,1), in Kapitel 2 als `... **el** ...`.
Gemessen ueber `am` + Ordinale + `Tag`: **83× `el` gegen 45× `al`**,
und RV1909mod liest „el primer día del mes". Er hat **seine** beiden
Stellen gezogen, nicht die fremden.

Der Agent fuer Kapitel 2 hat drei weitere Lesarten nachgezogen:
`Achtet` → *Watch* (aus 1,5/1,7), `sagte` 2,14 → *spoke*, `erging`
2,15 → *fared*. Damit stimmen die Formelbloecke „Achtet doch darauf,
wie es euch ergeht" (1,5 · 1,7) und „Achtet nun darauf, wie es euch
erging" (2,15) ueberein — ein Grenzfall, den der Prompt nicht kannte.

Alle zehn wiederkehrenden Wortfolgen des Buches sind zeichengleich.
Die zwei gemeldeten Abweichungen sind reine Satzposition: `am` steht in
2,10 am Versanfang gross, `so` in 1,5 („Nun, so spricht") und 2,6
(„Denn so spricht") klein.

## Zehn Bloecke gegen den Bestand

Sieben zeichengleich, drei begruendet abweichend:

- **1,1 gegen Hesekiel 26,1** — `am` es `el` statt `al`, siehe oben.
- **2,23 gegen Jesaja 22,25** — `spricht` fr `dit` statt `parle`
  (Stellungsregel) und `der` en `of the` statt `of` (die beiden
  Kapitel haben sich auf `of the` geeinigt, 6:4 bzw. 61:46).
- **2,6 gegen Jeremia 33,4** — der Block „Denn so spricht der HERR der"
  laeuft ueber die Konstruktionsgrenze: in Jeremia folgt „**der** Gott
  Israels" (Apposition), in Haggai „**der** Heerscharen" (Genitiv).
  Der siebte Fall dieser Art im Korpus.

## Was `hints.py` nicht sehen konnte

**2,12 traegt `Gewandzipfel` und `Zipfel` im selben Vers.** `Zipfel`
ist mit 5 Belegen fest gebunden (*skirt · orla · pan · lembo*),
`Gewandzipfel` im Bestand gar nicht belegt — und deshalb meldete
`hints.py` dort **0 Kollisionen**: die Kollisionsprobe vergleicht
Bestandsglossen, und ein unbelegtes Wort hat keine. Der Agent hat es
selbst gesehen und beide auseinandergehalten.

`hints.py` hat seither einen eigenen Abschnitt dafuer, der ohne Glossen
auskommt: **unbelegtes Wort neben einem belegten Bestandteil im selben
Vers**. Die Gegenprobe an vier abgenommenen Buechern findet acht
Stellen (`Backenzähne`/`Zähne`, `weiterverkaufen`/`verkaufen`,
`wahrsagen`/`sagen`, `Bildhauer`/`Bild`, `Lichtglanzes`/`Glanzes`,
`niederdrückt`/`nieder`, `unberegnete`/`beregnet`, dazu ein
Zufallstreffer `Weintrinker`/`weint`) — und **alle sieben echten sind
sauber getrennt**. Die Probe ist Vorsorge, kein Fund.

Dabei fiel auf, dass die Probe das **eigene Buch** aus dem Bestand
nehmen muss: ein bereits gebautes Buch weist seine eigenen neuen
Woerter als belegt aus und meldet dann nichts.

## Gegen die Ausgaben entschieden

- `Völker` → *peoples · pueblos · peuples · popoli* (Bestand 384:68),
  obwohl alle vier Ausgaben in 2,7 und 2,22 „nations" lesen — sonst
  faellt `Völker` mit `Nation` (2,14) zusammen.
- `Gemüse` (2,12) → *vegetables · verduras · légumes · verdure*,
  waehrend alle vier ein gekochtes Gericht lesen. Der deutsche Text
  sagt Gemuese.
- `Weinstock` fr `cep` (29:11, LSG schreibt „vigne"), `Siegelring` fr
  `anneau à cachet` (7×, einstimmig, LSG schreibt „un sceau").
- `Gebirge` (1,8) → nicht die dominante Reihe *highlands · serranía ·
  massif · massiccio* (103 von 105 — das ist das **benannte** Bergland,
  „das Gebirge Ephraim"), sondern die generische *mountains · monte ·
  montagne · monte*. Alle vier Ausgaben lesen den einfachen Berg.
- `heimbringen` (1,9) — die Prompt-Warnung traf: 1. Mose 42,19
  (Getreide) liest fr *rapporter*, Zephanja 3,20 (Menschen) *ramener*.
  Haggais Objekt ist der Ertrag, also `rapportez`.

## Aufgeloeste Kollisionen

- **1,2 `sagen` ↔ `sprechen`** (die einzige, die `hints.py` meldete):
  `spricht` behaelt die Botenformel, `sagt` bekommt *states · afirma ·
  dit · afferma* — **keine Erfindung**, sondern die Bestandszeile fuer
  genau diese Konstellation (Jes 65,8, Hes 29,3, Hes 36,13, Jer 3,1,
  Jer 44,26).
- **1,13 und 2,14 `sagte` ↔ `spricht`** (nur franzoesisch, von der
  Nachstellungsregel selbst erzeugt): beide Agenten sind unabhaengig
  auf dieselbe Bestandszeile *spoke · habló · parla · parlò*
  ausgewichen. Der Bestand selbst laesst dieses Paar in 4. Mose 14,28
  und 2. Koenige 22,19 stehen — steht in der Nachlese.
- **1,11 `alle`/`alles`** — kein Kollisionspaar, sondern dasselbe
  Lemma: der Bestand fuehrt die Form `alles` 21× unter `all`.

## Ausgabenbefunde

Drei RIV-Anlautfehler, alle in Kapitel 2: **2,1** `ggeo` fuer *Aggeo*,
**2,2** `ehotsadak` fuer *Jehotsadak*, **2,16** `uand'uno` fuer
*quand'uno* — der dritte vom Agenten selbst gefunden, mit
Haeufigkeitsprobe (`uand` 2× im ganzen RIV gegen `quando` 1354×).
Kapitel 1 ist frei davon.

`Jozadak` steht franzoesisch und italienisch gegen die Ausgaben — LSG
schreibt *Jotsadak* 11:2, RIV kennt *Iozadak* nicht. Die Spalten sehen
vertauscht aus; korpusweit zu entscheiden, steht in der Nachlese.

Die Ausrichtung ist in beiden Kapiteln **+0 ohne Warnung**. Haggai hat
in anderen Bibeln eine Kapitelgrenzenfalle (1,15b als 2,1); `l1912mod`
folgt ihr nicht, und das repariert die `kapitelgrenzen.py` bestaetigt.
