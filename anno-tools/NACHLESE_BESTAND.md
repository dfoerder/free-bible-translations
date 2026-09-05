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
