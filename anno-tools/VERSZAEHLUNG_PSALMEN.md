# Die Verszählung des Psalters — gemessen, nicht angenommen

In Hiob 38–41 zählen die vier Referenzausgaben die Gottesreden alle vier
verschieden, und der Fehler war unsichtbar: die verschobene Zeile stammt aus
derselben Tierreihe und liest sich plausibel (`VERSZAEHLUNG_38_41.md`).

Im Psalter ist das kein Sonderfall, sondern der Normalfall. Die deutsche
Zählung führt die Überschrift (`Ein Psalm Davids`, `Für den Vorsänger`) als
eigenen Vers 1. WEB, RV1909 und RIV1927 zählen sie nicht mit, LSG1910 dagegen
fast durchweg schon.

**In 63 der 150 Psalmen ist der deutsche Vers 12 nicht der englische Vers 12.**

## Wie die Tabelle entstanden ist

Der Versatz kommt aus dem **letzten Vers**: wo die Überschrift vorn fehlt,
deckt sich der Schluss. Ps 19 hat deutsch 15 Verse und englisch 14, und
deutsch 15 ist englisch 14, Wort für Wort dasselbe.

Eine erste Fassung hat den Versatz aus der Folge der Verslängen geschätzt und
lag in Ps 9, 15 und 19 daneben — jedes Mal lautlos, denn die verschobene Zeile
liest sich plausibel. Die Verslängen sind seither nur noch Gegenprobe.

## Die Tabelle

Versatz = Vers der Ausgabe minus deutscher Vers.

| en | es | fr | it | Psalmen |
|---|---|---|---|---|
| +0 | +0 | +0 | +0 | **87** — 1–2, 10–11, 14–17, 23–29, 32–33, 35, 37, 43, 50, 66, 71–74, 78–79, 82, 86–87, 90–91, 93–101, 103–107, 109–139, 141, 143–150 |
| -1 | -1 | +0 | -1 | **59** — 3–9, 12–13, 18–22, 30–31, 34, 36, 38–42, 44–49, 53, 55–59, 61–65, 67–70, 75–77, 80–81, 83–85, 88–89, 92, 102, 108, 140, 142 |
| -2 | -2 | +0 | -2 | **4** — 51–52, 54, 60 |

**Das Französische folgt dem Deutschen in allen 150 Psalmen.** Englisch,
Spanisch und Italienisch lassen die Überschrift gemeinsam weg.

Eine erste Fassung dieser Tabelle führte Ps 13 als Ausnahme mit französischem
Versatz −1. Das war falsch, und der Agent der Psalmen 10–13 hat es widerlegt,
indem er LSG direkt aus der Datei gelesen hat statt der Tabelle zu glauben:
`fr 1` ist dort die Überschrift wie überall sonst, und die Besonderheit liegt
am **Ende** — LSG zieht die deutschen Verse 6 und 7 in seinen Vers 6 zusammen.
Der aus dem letzten Vers errechnete Versatz muss dabei falsch herauskommen.

`ausgaben.py` führt diesen Fall deshalb als geprüfte Ausnahme. Ein Versuch, ihn
stattdessen über die Verslängen zu erkennen, hat Ps 13 richtig bekommen und
dafür Ps 21, 58, 76 und 142 falsch — die Längen taugen dafür nicht. Was in die
Ausnahmeliste kommt, ist **am Inhalt** geprüft.

## Der italienische Psalter: 63 Psalmen ohne ihren ersten Vers

`ita/riv1927` und `ita/riv1927mod` beginnen in 63 Psalmen bei Vers 2. Der Vers ist
nicht mit dem nächsten zusammengezogen, er **fehlt in der Datei**. Der Fehler
steht schon im importierten Grundtext `riv1927`, nicht erst in der
modernisierten Fassung, und er betrifft nur diese beiden Dateien — kein anderes
Buch und keine andere Sprache hat ein Kapitel ohne Vers 1.

Welcher deutsche Vers dadurch ohne italienische Vorlage bleibt, hängt am
Versatz des Psalms:

- **Versatz 0** — es fehlt der deutsche **Vers 1**, also die Zeile mit der
  Überschrift und dem ersten Halbvers. In Ps 23 fehlt damit
  `Il Signore è il mio pastore`, der bekannteste Vers des Psalters.
  Betroffen (41): 11, 14–17, 23–29, 32, 35, 37, 50, 100–101, 103, 110, 120–134, 138–139, 141, 143–145
- **Versatz −1** — es fehlt der deutsche **Vers 2**, die erste Zeile nach der
  Überschrift. Betroffen (22): 5, 8–9, 12–13, 19–21, 31, 38–42, 44, 47–49, 53, 58, 108, 140

**Für die Annotation:** in diesen Versen hat das Italienische keine Vorlage.
Die Glosse folgt dem Bestand und den drei anderen Ausgaben. Die nächste
italienische Zeile im Text ist der **folgende** deutsche Vers — wer sie nimmt,
glossiert einen Vers aus dem nächsten. `ausgaben.py` bietet sie deshalb an
dieser Stelle nicht an, sondern schreibt `FEHLT in der Datei der Ausgabe`.

**Für die App:** italienische Leser dieser Psalmen bekommen den ersten Vers gar
nicht zu sehen. Das ist unabhängig von der Annotation zu beheben und braucht
den Text aus einer anderen Quelle.

## Ps 60: die italienische Zeile trägt die Überschrift statt des Verses

Ein dritter Schadensfall, der weder ein Versatz noch eine Lücke ist. In Ps 60
lautet die erste italienische Zeile:

> `Per il Capo de' musici. Su "il giglio della testimonianza". Inno di Davide
> da insegnare; quand'egli mosse guerra ai Siri di Mesopotamia e ai Siri di
> Soba e Joab`

Der Satz **bricht mitten in der Überschrift ab** („e Joab"), und der Versinhalt
(`O Dio, tu ci hai rigettati…`) fehlt vollständig. Weil die Zeile aber
vorhanden und sogar lang ist, richtet `ausgaben.py` sie gegen den deutschen
Vers 60,3 aus und meldet nichts — Abstand 0,13, weit unter der Warnschwelle.

**`ausgaben.py` erkennt fehlende Verse, nicht vertauschten Inhalt.** Ein
Versuch, den Fall über ein fehlendes Satzendezeichen zu finden, meldet in jeder
Ausgabe zwei- bis dreitausend Verse (Verse enden legitim auf Komma). Ein
Versuch über die Verslänge findet ihn gar nicht, weil die abgeschnittene
Überschrift länger ist als der deutsche Vers. Ein Versuch über
Überschriftenmerkmale meldet vier Verse, davon drei zu Recht.

Gefunden hat ihn der Agent der Psalmen 59–61, indem er die italienische Zeile
gelesen hat statt sie zu nehmen. Das bleibt die einzige verlässliche Prüfung.

## Die Regel

    ausgaben.py <buchNr> <kapitel> [<vonVers> [<bisVers>]]

druckt die vier Ausgaben neben dem deutschen Vers, inhaltlich ausgerichtet, mit
der Versnummer jeder Ausgabe daneben. **Eine Ausgabe nie über die deutsche
Versnummer aufschlagen.**
