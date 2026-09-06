# Nachlese am Bestand — offene Korrekturen

Was die Buchagenten und die Einsammel-Laeufe **im fertigen Bestand**
gefunden haben, ohne es anzufassen. Bisher stand das verstreut in
Berichten und Wortfeldern; hier steht es an einem Ort.

**Nichts hiervon ist beauftragt.** Jede Zeile ist am Vers geprueft und mit
der Zahl belegt, die eine Korrektur kosten wuerde.

---

## A · Namen, mechanisch pruefbar

### 1. Die italienischen `I`-statt-`J`-Namensglossen — 672 Vorkommen in 201 Formen

Der Defekt liegt in der RIV-Ausgabe, nicht im Bestand; gefaehrlich wird er,
wo eine Glosse die RIV-Zeile uebernommen hat. Vergleichszahlen: LSG 3 ·
RV 13 · WEB 19 · de 20. Vollstaendig in `BEFUNDE_RIV_ANLAUT_J.md`;
die Messung ohne Seltenheitsdeckel in `RIV_ANLAUTFEHLER.md`.

### 2. `Michael` traegt an zehn AT-Stellen die NT-Form — belegt, abgeschlossen zaehlbar

Der Bestand fuehrt it `Michele` bzw. `di Michele`, waehrend **RIV an allen
zehn Stellen `Micael` schreibt**:

```
4. Mose 13,13 · 1. Chronika 5,13 · 5,14 · 6,25 · 7,3 · 8,16 · 12,20 · 27,18
2. Chronika 21,2 · Esra 8,8
```

Richtig stehen bereits: Daniel 10,13 · 10,21 · 12,1 (`Micael`, waehrend der
Daniel-Arbeit gesetzt) und die beiden NT-Stellen Judas 1,9 · Offb 12,7
(`Michele` — dort ist die Form korrekt).

### 3. `Hananja` in Jeremia 36,12

Einzelstelle, 28 Belege des Lemmas insgesamt. Gefunden waehrend der
Jeremia-Arbeit.

### 4. Die `Zeboim`-Reihe

Gefunden waehrend der Hosea-Arbeit, s. `WORTFELD_HOSEA.md`.

---

## B · Glossen, am Vers geprueft

### 5. Psalmen 65,13 — Artikel im falschen Genus

„die Weiden **der** Steppe": `der` steht als *of the · del · du · del*
(maskulin), waehrend derselbe Vers `Steppe` als *estepa · steppe · steppa*
fuehrt — alle drei feminin. Richtig waere *de la · de la · della*, wie es
Joel 1,19 · 1,20 · 2,22 haben. `artikel.py` meldet die Stelle von selbst.

### 6. Apostelgeschichte 2,17 — `Menschen` und `Maenner` verschmolzen

Beide tragen im selben Vers *hombres · hommes · uomini*. Joel 3,1 hat
denselben Satzbau (es ist dieselbe Prophetenstelle) und loest auf:
`Menschen` *human beings · seres humanos · êtres humains · esseri umani*.

**Diese Stelle hat beim Joel-Einsammeln beinahe Schaden angerichtet:** die
Angleichung von Joel 3,1 an Apg 2,17 war schon geschrieben, bis
`glosskollision.py` die neu gebaute Kollision meldete. Eine Vorlage kann
den Defekt tragen, den sie zu belegen scheint.

### 7. Apostelgeschichte 2,21 — franzoesisches Wort in der spanischen Spalte

`anruft` = *calls on · **invoque** · invoque · invoca*. Spanisch ist
*invoca* (so der Bestand 5× und Joel 3,5).

Eine Korpusmessung ueber alle **676 107** Eintraege auf spanische Glossen
mit franzoesischen Sonderzeichen (à â è ê ë î ï ô û ù ç œ) ergab
**0 Treffer** — der Fall ist ein Einzelstueck, kein Muster. Die Messung
lohnt die Wiederholung nicht.

### 8a. Jeremia 26,18 — italienischer Artikel im falschen Genus

`der` vor `Tempelberg` steht italienisch als **`la`**, waehrend derselbe
Vers `Tempelberg` als *monte del tempio* fuehrt — maskulin. Franzoesisch
ist `la montagne du temple` dagegen **richtig**; nur die italienische
Spalte ist falsch.

Der Vers ist die woertliche Parallele zu **Micha 3,12**, wo es richtig
steht (*il*). Gefunden vom Agenten fuer Micha 3 beim Uebernehmen der
Vorlage — er hat den Block genommen und den Fehler **nicht**
mituebernommen.

### 8. `Rechtsstreit` in Jeremia 25,31 · `kein`/`ningún` in Jeremia 14,10

Einzelstellen aus der Jeremia-Arbeit.

### 9. Wortpaare, die im Bestand dieselbe Reihe teilen

Kein Fehler, aber eine Kollision ueberall, wo die beiden zusammenstehen —
wer eines der Woerter in einem neuen Kapitel setzt, muss den Vers pruefen:

```
Kornspeicher ↔ Scheune      es/fr/it gleich (graneros · greniers · granai)
Trauergewand ↔ Trauersack   en gleich (sackcloth)
```

---

## C · Ausgabendefekte (nicht im Bestand, aber beim Abzaehlen gefaehrlich)

- **RIV-Anlautverluste**, zuletzt Joel 1,12 (`ecchi`), Jos 9,4 (`ecchi`),
  Joel 2,20 (`alirà`) — `RIV_ANLAUTFEHLER.md`
- **RIV-Imperativ als Infinitiv**: Joel 2,16 (`Radunare` statt `Radunate`) —
  neuer Untertyp, derselbe Test findet ihn
- **1. Chronika 27,20 traegt beide Typen im selben Vers**: `Ioel` und
  `edaia` (→ *Pedaia*)
- **LSG-Tilden**: 16 Verse, alle Buchschluesse — `BEFUND_LSG_TILDE.md`

---

## D · Befunde im deutschen Quelltext selbst

Nicht im Bestand und nicht in den Ausgaben, sondern im modernisierten
`l1912mod` — der Grundlage aller Glossen. **Hier wurde nichts geaendert;
eine Textkorrektur ist eine andere Entscheidung als eine Glossenkorrektur.**

### 10. Amos 9,3 — `Verbuergen` statt `Verbaergen`

> „**Verbuergen** sie sich vor meinen Augen auf dem Grund des Meeres,
> ich wuerde der Schlange befehlen, sie dort zu beissen."

Gemeint ist der Konjunktiv II von **`verbergen`** (`verbaergen`), nicht
`verbuergen` (= garantieren). Der Parallelsatz im selben Vers hat
`Versteckten sie sich`, und alle vier Ausgaben lesen einstimmig
„verbergen/verstecken":

    WEB  „though they be hidden from my sight"
    RV   „si se ocultan de mi vista"
    LSG  „S'ils se dérobent à mes regards"
    RIV  „quand'anche s'occultassero al mio sguardo"

Im ganzen deutschen Korpus steht die Form **einmal** — hier. Die
uebrigen Belege des Stammes sind `verbarg` (8×) und `verbargst` (1×).

Die Glosse in Amos 9,3 folgt dem Sinn (*hide*), nicht der verschriebenen
Form; das Lemma steht auf `verbergen`.


---

## E · Eine Bestandskonvention, die von LSG abweicht

### 11. „…, spricht Gott, der HERR" steht 100× auf `parle`, LSG liest dort `dit`

Kein Fehler, aber eine Entscheidung, die niemand aufgeschrieben hatte.
Gemessen ueber den ganzen Korpus, nach der Stellung im deutschen Satz:

```
                          LSG liest            Bestand glossiert
    vorangestellt         parle 78 : dit  1    parle 110  (einstimmig)
    nachgestellt          dit   80 : parle 37  parle 100  (einstimmig)
```

Vorangestellt sind sich Ausgabe und Bestand einig. **Nachgestellt nicht:**
LSG schreibt dort mehrheitlich „Dit le Seigneur, l'Éternel", der Bestand
glossiert durchgehend *parle*. Die 100 Faelle stammen fast alle aus
Hesekiel, wo die Wendung 198× steht.

Der Agent fuer **Amos 8** hat den Widerspruch am Vers bemerkt (LSG liest
in 8,3 · 8,9 · 8,11 dreimal „dit") und ist **bewusst beim Bestand
geblieben** — richtig, denn die Konsistenz ueber 100 Stellen wiegt
schwerer als die Treue zu einer Ausgabe an drei. Die Entscheidung gehoert
aber notiert, damit sie nicht jedes Buch neu verhandelt wird.

**Wer sie umdrehen will, muss alle 100 Stellen zugleich ziehen** — eine
halbe Aenderung waere schlechter als beide ganzen.


### 12. Micha 2,11 — `Bier` steht einmal im ganzen Korpus

> „Ich predige euch Wein und **Bier**!"

Dasselbe hebraeische Wort ist im l1912mod sonst **durchgehend anders
modernisiert**:

```
    starkes Getränk   8×   (3Mo 10,9 · 5Mo 29,5 · Ri 13,4 · 13,7 · 13,14 …)
    starkem Getränk   2×   (4Mo 6,3 · Spr 31,4)
    starken Getränk   2×   (Jes 28,7 · 29,9)
    Rauschtrank       2×   (Jes 5,11 · 5,22)
    Bier              1×   — nur Micha 2,11
```

Vierzehn Stellen gegen eine. **Nicht geaendert** — eine Vereinheitlichung
des Quelltextes ist eine andere Entscheidung als eine Glossenkorrektur,
und `Bier` ist als deutsches Wort nicht falsch, nur allein.

Die Glosse folgt dem Wort, das dasteht: `Bier` A2
*beer · cerveza · bière · birra*. **Die App glossiert Deutsch — wer
„Bier" liest, muss „Bier" lernen.** Alle vier Ausgaben lesen an der
Stelle uebrigens dasselbe (*strong drink · bebida fuerte · boissons
fortes · bevande forti*); die Abweichung besteht nicht zwischen den
Ausgaben, sondern zwischen dem deutschen Text und allen vieren.

Gefunden vom Agenten fuer Micha 2.


### 13. Jeremia 33,22 — franzoesischer Artikel im falschen Genus

`des` vor `Himmels` steht franzoesisch als **`des`** (Plural), waehrend
derselbe Vers `Himmel` als *ciel* fuehrt — maskulin **Singular**. Der
Bestand setzt vor `ciel` 106× `du` und nur 2× `des`; Jeremia 19,13
schreibt dieselbe Wendung richtig als *armée du ciel*.

Gefunden vom Agenten fuer Zefanja 1, der den Block „das Heer des
Himmels" aus Jeremia 33,22 uebernehmen wollte, den Fehler bemerkte und
in seinem eigenen Vers `du` setzte — **die Vorlage also benutzte, ohne
ihren Fehler mitzunehmen**. Derselbe Vorgang wie bei Micha 3,12 gegen
Jeremia 26,18.


### 14. Meine eigene Messung: aus zwei von sechs Varianten „alle" gemacht

Fuer den Haggai-Prompt habe ich „So spricht der HERR" im Bestand
gemessen, mir mit `most_common(2)` die **zwei haeufigsten** von
**sechs** Varianten ausgeben lassen und geschrieben: „184 Vorkommen,
**alle** mit `parle`". Der Agent fuer Kapitel 1 hat nachgemessen: es
tragen zwei Vorkommen `dit` und zwei italienisch `parla` statt `dice`.
Die Stellungsregel selbst stimmt — die Behauptung „alle" nicht.

Derselbe Fehler wie in Jona, wo ich ein RV-Verszitat bei 95 Zeichen
abgeschnitten und aus dem Rest einen Verszaehlungsbefund abgeleitet
hatte. Die Regel daraus gilt weiter und jetzt auch fuer Zaehlungen:
**nie aus einer abgeschnittenen Liste auf Vollstaendigkeit schliessen.**

Dagegen steht seit Haggai `folgenreihe.py`. Es misst die Glossen einer
Wortfolge im Bestand und schneidet **nichts** ab: jede Variante mit
ihrer Zahl, die Belegstellen der seltenen dazu, und die Vorkommen mit
einem Mehrwort an einer Position eigens gezaehlt — die fehlten in meiner
Messung stillschweigend und erklaeren, warum ich 184 zaehlte und der
Agent 229.


### 15. `Jozadak` — franzoesisch und italienisch sehen vertauscht aus

Der Bestand fuehrt den Namen als `Jehozadak · Josadac · Jehotsadak ·
Iozadak` (5 Belege, Esra/Nehemia). Gegen die Ausgaben gehalten:

- **LSG** schreibt **Jotsadak 11× gegen Jehotsadak 2×** — der Bestand
  hat die Minderheitsform.
- **RIV** schreibt Jehotsadak 7 : Jotsadak 5 und **„Iozadak" nirgends**.

Die franzoesische und die italienische Spalte sehen aus, als waeren sie
vertauscht. Gefunden vom Agenten fuer Haggai 2, der die Bestandsreihe
trotzdem gesetzt hat — richtig so: **korpusweit zu entscheiden, nicht
in einem Kapitel.** Betrifft Haggai 1,1 · 1,12 · 1,14 · 2,2 · 2,4 und
die Belege in Esra und Nehemia.

### 16. Zwei Ausreisser der `spricht`-Stellungsregel

Die Regel (vorangestellt `parle`, nachgestellt `dit`) traegt im Bestand
223:4 und 264:46. Zwei nachgestellte Stellen lesen `parle`, und beide
sind Vorlagen, die ein Agent uebernehmen wuerde:

- **Jesaja 22,25** „An jenem Tag, spricht der HERR der Heerscharen" —
  derselbe 8-Token-Block wie Haggai 2,23. Der Haggai-Agent hat die
  Stellungsregel ueber die Parallelenregel gestellt und `dit` gesetzt,
  gestuetzt darauf, dass LSG in Haggai 2,23 selbst „dit l'Éternel des
  armées" schreibt.
- **Zephanja 2,9** — dort ist es kein Ausreisser, sondern der
  Appositionsfall („der Gott Israels", siehe Eintrag zur Regel).

Jesaja 22,25 bleibt der einzige echte. Nicht angefasst.

**Nachtrag aus Sacharja 3:** Der Agent hat die Ausgabe selbst
nachgelesen — **LSG schreibt in Jesaja 22,25 „dit l'Éternel des
armées"**. Der Bestandseintrag `parle` steht dort also nicht nur gegen
die Stellungsregel, sondern gegen seinen eigenen Zeugen. Damit ist er
kein Regelausreisser mehr, sondern ein Fehler — aber ein **einzelner**:
wenn er gezogen wird, ist es ein Einzeleintrag, kein Reihenwechsel.

### 18. `der HERR der Heerscharen` — buchweise gespalten, nicht mehrheitlich

Die englische Spalte des zweiten `der` steht **26 zu 25**, also
praktisch unentschieden. Die Spaltung verlaeuft aber nicht zufaellig,
sondern **nach Buechern**:

```
Jesaja                          of      25 von 25
Amos, Nahum, Zephanja, Haggai   of the  26 von 26
```

Fuer einen Prompt taugt „Bestandsmehrheit" hier also **nicht** als
Begruendung — nur der Buchanschluss. Sacharja schliesst an Haggai an
und liest `of the`; das haben die Agenten fuer Kapitel 1 und 3
unabhaengig voneinander so gesetzt.

### 19. `Weinstock` in „unter Weinstock und Feigenbaum"

Korpusweit ist `Weinstock` auf `cep` gebunden (30:11). In **dieser
Formel** steht es 2:2 — 1. Koenige 5,5 und Micha 4,4 lesen `cep`,
2. Koenige 18,31 und Jesaja 36,16 lesen `vigne` —, waehrend **LSG an
allen diesen Stellen einschliesslich Sacharja 3,10 „vigne" liest**.
Der Sacharja-Agent ist bei der korpusweiten Bindung geblieben und hat
die Spaltung gemeldet. Sie gehoert einmal ganz entschieden, nicht
buchlokal.

### 17. `sagte` ↔ `spricht` steht im Bestand zweimal unaufgeloest

4. Mose 14,28 und 2. Koenige 22,19 tragen beide Woerter im selben Vers
mit derselben franzoesischen Glosse `dit`. Beide Haggai-Agenten haben
die Stelle in ihren Versen (1,13 und 2,14) aufgeloest — unabhaengig
voneinander mit derselben Bestandszeile `spoke · habló · parla ·
parlò`. Die zwei alten Stellen bleiben, wie sie sind; die Regel
„aufgeloest wird nur im Kollisionsvers" gilt in beide Richtungen.


### 20. `Berechja` — die italienische Glosse widerspricht RIV

Der Bestand fuehrt den Namen als *di **Berechia*** (5 Belege), **RIV
schreibt an jeder Stelle „Berekia"** — 1. Chronik 15,17, Nehemia 3,4
und Sacharja 1,1/1,7 nachgeprueft. Der Sacharja-1-Agent hat die
Bestandsreihe genommen (Konsistenz mit fuenf bestehenden Eintraegen)
und den Widerspruch gemeldet. Dieselbe Klasse wie `Jozadak` aus Haggai.

### 21. `Eifer`: die Bindung steht gegen alle vier Ausgaben

In Sacharja 1,14 („Ich eifere fuer Jerusalem und Zion mit grossem
Eifer") lesen **alle vier Ausgaben** *jealousy · celo · jalousie ·
gelosia*. Der Bestand bindet `Eifer` aber **33:0** an *zeal · celo ·
zèle · zelo* — darunter 2. Koenige 19,31, dasselbe goettliche Qin'ah.
Der Agent ist nach „bei gewoehnlichen Woertern gewinnt die Bindung"
beim Bestand geblieben.

Nebeneffekt: die Figura etymologica `eifere`/`Eifer` bricht in drei
Sprachen auf (*am jealous* neben *zeal*), weil der Bestand fuer Verb
und Substantiv zwei verschiedene Felder fuehrt. **Wenn das umgekehrt
entschieden werden soll, dann korpusweit** — Sacharja 8,2 traegt
dieselbe Stelle noch einmal.


### 22. ERLEDIGT — `Jozadak`: beide Spalten waren vertauscht

Der Bestand fuehrte den Namen als *… de **Jehotsadak** · di **Iozadak***.
An allen zwoelf Belegstellen gegen die Ausgaben geprueft:

```
LSG   schreibt Jotsadak    10 von 10   —  „Jehotsadak" nie
RIV   schreibt Jotsadak (Esra/Nehemia) oder Jehotsadak (Haggai/Sacharja)
      —  „Iozadak" nirgends
```

Die franzoesische Spalte trug also RIVs Form, die italienische eine,
die keine Ausgabe kennt. Der Haggai-Agent hatte den Verdacht gemeldet
und die Bestandsreihe stehen lassen; der Sacharja-6-Agent hat gegen den
Bestand entschieden — und damit liefen zwei Buecher derselben Sitzung
auseinander. **Korpusweit korrigiert** auf *de Jotsadak · di
Jehotsadak*: 24 Aenderungen in sieben Kapitelquellen der Buecher 13,
15, 16 und 37, danach neu gebaut, alle vier `validate` sauber.

### 23. ERLEDIGT — Offenbarung 11,4: `gli due ulivi`

Der Vers widerlegt sich selbst. „die zwei Ölbäume und **die zwei**
Leuchter" traegt an der ersten Stelle it `gli`, an der zweiten `i` —
beide vor demselben Wort `due`. Der italienische Artikel richtet sich
nach dem unmittelbar folgenden Wort, also ist `i` richtig. Gefunden vom
Agenten fuer Sacharja 4, der die Zeile fuer 4,11 uebernehmen wollte und
dabei zusaetzlich eine Kollision mit `ihn` → *gli* bekam. Korrigiert.

### 24. `Jedaja` — dieselbe Klasse, noch offen

Bestand: *Jedaiah · Jedaías · Jedaja · **Iedaia*** (10 Belege). RIV
schreibt an fuenf geprueften Stellen und in Sacharja 6,10/6,14
durchgehend **„Jedaia"**, „Iedaia" nirgends; LSG schreibt viermal von
fuenf **„Jedaeja"**. Der Sacharja-6-Agent hat nach den Ausgaben gesetzt.
Die zehn Altbelege sind noch nicht nachgezogen.

### 25. `Tobija` und `Tobia` — zwei Lemmata fuer einen Namen

`l1912mod` schreibt in Sacharja 6,10/6,14 `Tobija`, der Bestand fuehrt
15 Belege unter `Tobia`. Der Agent hat formtreu `Tobija` als eigenes
Lemma angelegt und die Glossen der `Tobia`-Reihe uebernommen — dieselbe
Zwillingslage wie `Marescha`/`Maresa` und `Zefanja`/`Zephanja`. Zu
entscheiden, ob zusammengefuehrt wird.

### 26. `Zemach` steht in beiden Stellen gegen alle vier Ausgaben

Sacharja 3,8 und 6,12 fuehren ihn als **Namen**, weil `l1912mod` ihn
nicht deutet. Alle vier Ausgaben uebersetzen ihn dagegen, und zwar
zeichengenau mit der Bestandsreihe von `Spross` C1 (*branch · renuevo ·
germe · germoglio*). In 6,12 ist es noch schaerfer: **LSG schreibt
`germe` klein** und setzt im selben Vers „**germera** dans son lieu" —
liest die Stelle also rein appellativisch. Beide Kapitel haben
zeichengleich `Zemach` gesetzt; die Frage gehoert buchweit entschieden,
nicht kapitelweise.


### 27. `Sarezer` — RIV liest an allen drei Stellen „Saretser"

Der Bestand fuehrt it *Sarezer* (2. Koenige 19,37, Jesaja 37,38).
**RIV1927 schreibt an beiden Altstellen und in Sacharja 7,2
„Saretser".** Der Sacharja-7-Agent hat im Kapitel `Saretser` gesetzt
(Textbefund vor Bindung) und die zwei Altbelege gemeldet. Dieselbe
Klasse wie `Jozadak` und `Jedaja`.

### 28. `Kislev` — die italienische Glosse passt zum falschen Vers

Der Bestand setzt fuer `Kislev` (Nehemia 1,1) it *Chisleu*. **RIV liest
in Nehemia 1,1 selbst „Kisleu"** — der Wert passt dort also nicht, wohl
aber zufaellig auf Sacharja 7,1, wo RIV „Chisleu" schreibt. Der Agent
hat die Sacharja-Form `Kislew` auf das Lemma `Kislev` gebunden und die
Reihe unveraendert uebernommen; **kein Zwillingsfall**, der Unterschied
ist rein deutsch.
