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
