# Wortfeld Klagelieder (25)

5 Kapitel · 154 Verse · 3219 Einträge · 780 Lemmata · 135 Mehrwörter · 2 Pakete.
Fertig am 04.09.2026. Planung: `PAKETE_KLAGELIEDER.txt`.

## 0. Modernisierung vor der Annotation

Erstes Buch, in dem der l1912mod vor der Annotation überarbeitet wurde:
**Kapitel 2 vollständig neu** (22 Verse), dazu 1,7 · 1,9 · 1,14 · 1,18 · 1,22
und 4,13.

Die Eichung des Archaismus-Maßes war dabei in **beide** Richtungen falsch:
`Schütte`/`Stehe`/`Hebe` sind gewöhnliche Imperative und wurden mitgezählt,
`richte…zurecht`/`zugerichtet`/`darniederliegt`/`großsprecherisch` wurden
übersehen. Kapitel 1 galt deshalb als sauber und war das schlechteste
(7 harte Archaismen). Verlässlich ist nur die maschinelle Zählung: **Wörter mit
0–2 Belegen im fertigen Bestand, pro 1000 Tokens.**

Zwei Regeln für jede weitere Modernisierung:

1. **Eine Modernisierung kann eine neue Kollision erzeugen.** 2,5 hatte nach
   der Überarbeitung `vernichtet` und `zerstört` im selben Vers auf derselben
   Bestandsreihe. Ersetzt durch `verschlungen` — was WEB/LSG/RIV dort lesen.
2. **Ein Wort, das im Bestand nur eine Lesart hat, verträgt keine Nachbarschaft
   mit seinem Synonym.** `niederwerfen` trägt 12/12 die reflexive Lesart
   (*prosterner*); 1,14 ist deshalb auf `ist so mit mir verfahren` gegangen,
   was zugleich die Parallele 1,14↔1,22 wiederherstellt.

Stehen geblieben ist bewusst `verstören` in 4,20 (Luthers *verwüsten*-Sinn) —
glossiert nach der Bedeutung (*ravaged · asolaron · dévastèrent · devastarono*),
ausdrücklich **nicht** auf der `zerstören`-Reihe aus 4,6.

## 1. Die Buchentscheidung: `schauen` gegen `sehen`

Vier Kollisionsstellen, drei verschiedene Agenten, wortgleiches Ergebnis:

    1,11 · 1,12 · 2,20 · 5,1
    sehen    A1  see  · ve/ved/ven · vois/voyez · vedi/vedete
    schauen  A2  look · mira/Mirad  · regarde/Regardez · guarda/Guardate

## 2. `paketcheck.py` Abschnitt A: leer

Über alle fünf Kapitel kein neu geprägtes Lemma verschieden entschieden.
Abschnitt C (Level): ebenfalls null. Abschnitt B: 112, ganz überwiegend
Numerus- und Genuskongruenz.

Sechs Angleichungen waren fällig:

| Stelle | vorher | nachher | Grund |
|---|---|---|---|
| `Gegner` 2,17 | *adversaries* | *opponents* | Bestandsreihe, 19 Belege |
| `achten` 5,12 | *respected* | *esteemed* | Bestandsreihe, 6 Belege |
| `liegen` 5,18 | es *está* · fr *est* | *yace* · *gît* | Buchreihe wie 1,1 |
| `aufdecken` 4,22 | *uncover* | *expose* | Schuld-Reihe wie 2,14 |
| `lauern` 3,10 | *lies in wait* | *lurks* | trennt vom Mehrwort `auflauern` |
| `daran` 5,1 | it *di ciò* | it *ci* | Buchreihe wie 1,7 · 3,19 · 3,20 |

## 3. Der zurückgenommene Zug — die wichtigste Lehre

`ausreisser.py` meldet für 3,56 `Ohr` es *oreja* gegen die Bestandsmehrheit
*oído* (41/64). Angeglichen — und `glosskollision.py` meldete **sofort ein
neues Paar**: `gehört` im selben Vers ist spanisch ebenfalls *oído*. Der Agent
hatte *oreja* als Kollisionsauflösung gesetzt, nicht aus Nachlässigkeit.
Zurückgenommen.

> **Ein `ausreisser.py`- oder `konsistenz.py`-Treffer ist erst dann ein
> Auftrag, wenn im Kollisionsvers nichts dagegen steht.** Vor jeder Angleichung
> den Vers aufschlagen und die Nachbarwörter prüfen.

## 4. Bewusste Abweichungen, die stehen bleiben

- **`Himmel` 4,19 en *sky*** gegen *heaven* in 2,1 · 3,41 · 3,50 · 3,66. Die
  Adler am Himmel; der Bestand führt *sky* 82-mal, darunter **Jeremia 8,7** für
  genau dieselben Vögel und Psalmen 104,12.
- **`Hilfe` 4,17 en *aid*** — Kollision mit `helfen` im Vers. `helfen` trägt im
  Bestand ausnahmslos die *help*-Familie und ist das stärker gebundene Wort;
  `Hilfe` führt daneben *helper* und *aid* (1. Chronika 19,12).
- **`kein mehr` 5,14** trägt *no longer any · ya ninguna · plus aucune · più
  alcuna*, 2,9 dagegen *ya no · ne plus de · non più*. Nur in 5,14 steht
  `nicht mehr` im selben Vers. Nicht glätten.
- **`vernichten` 2,8 *wiped out*** — im selben Vers steht `zerstören`; beide
  Lemmata sind im Bestand zu 100 % an *destroy* gebunden. LSG liest dort selbst
  *anéantis*. In 2,2 und 2,16 bleibt `vernichten` bei *destroyed*.
- **`übrig` 2,22 it *rimanente*** — Kollision mit `bleiben`.
- **`ewig` 5,19 en *eternally*** — Kollision mit `für alle Zeit`.
- **`dunkel` 4,1 it *scuro*** statt *buio*: *buio* stammt korpusweit aus
  „es wurde dunkel" (Nachtwerden), nicht aus der Farbe. Die Bindung gilt für
  dieselbe Bedeutung, nicht für dieselbe Buchstabenfolge.
- **`liegen` fr *gisent/gésir*** statt der Korpusmehrheit *reposer*: das Buch
  meint durchgehend das Daliegen von Erschlagenen (1,4 · 2,21 · 4,1 · 4,5).
- **`Land` 4,21 es *tierra*** („im Land Uz") — die Reihe
  *land · tierra · pays · paese* ist im Bestand belegt, u. a. Jeremia 48,24/33.

## 5. Reihen mit mehr als einer Lesart im Buch

    Volk      vier Reihen: people (8×) · nations (6×) · peoples (2×) · nation (4,17)
    unter     among (8×) · under (6×)
    doch      please (5×) · yet (4×) · do (3,19)
    Feind     enemy (12×) · enemies (9×)
    Himmel    heaven (4×) · sky (4,19)
    aufdecken exposed 2,14 · expose 4,22   (beide Schuld-Reihe, nur Tempus)

`Tochter Zion` bleibt durchgehend **zwei** Einträge.

## 6. Neu geprägte Lemmata

    Schwärze      C1  blackness · negrura · noirceur · nerezza
    Holzscheit    C1  log · leño · bûche · ceppo
    besudeln      C1  stained · manchados · souillés · lordati
    verstören     C1  ravaged · asolaron · dévastèrent · devastarono
    gleichsetzen  C1  liken · asemejar · assimiler · equiparare

Neues Mehrwort: `den Geist aufgeben` B2 (2,12) — im Bestand nicht geführt;
`aufgeben` allein heißt dort *give up/renunciar*, was hier falsch wäre.

## 7. Werkzeugbefunde

- **`hints.py` meldet weit mehr Unbelegtes, als neu ist.** Kapitel 2: 8
  Meldungen, 1 wirklich neu. Kapitel 4: 12 Meldungen, 4 neu. Jede Meldung
  gegen `belegt.py`/`fixgloss.py` prüfen — und dabei die Formfalle beachten
  (`belegt.py <Wort>` zählt die **Form**, nicht das Lemma).
- **`sweep.py` liefert im Buch 4 Treffer, alle vier Fehlalarme:** 1,9
  („gefallen … und hat"), 4,4 (`es` ist Objekt, kein Existenz-`es`), 4,14
  (`hin und her` ist gesetzt, `hingehen` wäre falsch), 5,15 (`ein Ende haben`
  war bereits gesetzt).
- **`konsistenz.py` Abschnitt B (15 Fälle) ist vollständig gutartig** — teils
  Numerus gegen die Bestandsmehrheit, teils richtige Idiome
  (`ohne Grund` = *without cause*, `Sache führen` = *plead the cause*).
- **`paketcheck.py` und `qa.py` brauchen die gebaute Anno-Datei bzw. die
  Kapitel in `anno-quellen/`.** Bei einem neuen Buch also zuerst die Kapitel
  nach `anno-quellen/deu/l1912mod/<nr>/` kopieren, dann `paketcheck.py`;
  `qa.py` je Kapitel mit `--kapitel <nr> <kap> <datei>`, buchweit erst nach
  `buildbook.py`.

## 8. Widerlegte Prompt-Angaben

- **`Galle` steht in keinem der fünf Kapitel** — ich hatte sie für Kapitel 4
  angekündigt. `Bitterkeit` und `Wermut` stehen nur in Kapitel 3.
- **`Jüngling`/`Knabe` in 2,21 gibt es nicht mehr** — meine Modernisierung
  hat daraus „Junge und Alte" gemacht. `PAKETE_KLAGELIEDER.txt` war an dieser
  Zeile veraltet, weil sie vor der Überarbeitung geschrieben wurde.
- **`Joch` und `Ältester` kommen in Kapitel 5 nicht vor** (dort steht `Alte`,
  ein anderes Lemma); `Hand` einmal statt zweimal. Ursache sind
  Lesartenunterschiede der Luthervorlage gegen WEB/RV/LSG/RIV, keine
  Modernisierungsfehler.
- **`starren` ist belegt** (B2, 3 Lesarten), obwohl `hints.py` `starrten` als
  unbelegte Form führt.
- **`Priester` steht in 2,6 im Singular** („König und Priester"), nicht nur
  im Plural.
