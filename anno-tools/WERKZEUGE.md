# Die Werkzeuge in `anno-tools/`

Register aller Skripte: **wozu**, **wann** und **wie aufgerufen**. Die
ausfuehrliche Begruendung steht jeweils im Docstring der Datei — dort ist
auch festgehalten, an welchem Fehler das Werkzeug entstanden ist.

**`export ANNO_OUT=<scratchpad>/out` ist Pflicht**, und alle Werkzeuge
werden **aus `anno-tools/` heraus** aufgerufen.

**Welche Ausgabe annotiert wird, sagt `ANNO_EDITION`** — Default
`deu/l1912mod`, fuer das franzoesische NT `fra/lsg1910mod`. Daraus leiten
sich Quelltextpfad, beide Dateinamensmuster und die vier Glossensprachen
ab; `common.py` fuehrt die Tabelle. Ohne die Variable arbeitet die ganze
Kette auf dem deutschen Text weiter, **ohne abzubrechen** — sie antwortet
dann nur zum falschen Buch. Einmal pruefen:

    python3 -c "import common as C; print(C.EDITION, C.LANGS)"

## Vor der Arbeit — was das Kapitel mitbringt

**`vorbereitung.py`** — Die Vorbereitungsdatei eines Pakets, maschinell.
    vorbereitung.py <buchNr> <kapitel …> [-o datei]

**`hints.py`** — Prompt-Hinweise aus dem **Quelltext** statt aus Bibelkenntnis.
    hints.py <buchNr> [<kapitel>]

**`lexicon.py`** — Gefilterter Lexikon-Extrakt für einen Versbereich.
    lexicon.py <buchNr> <kapitel> [<vonVers> <bisVers>] [-o datei]

**`rueckwaerts.py`** — Was der vorhandene Bestand ueber ein **franzoesisches**
Wort schon weiss. Die Gegenrichtung zu `lexicon.py`: `eng/web` und
`deu/l1912mod` tragen beide eine `fr`-Spalte und decken zusammen genau
de·en·es·it ab, also liegt fuer 98 Prozent der franzoesischen Tokens schon
eine Viererzeile vor. Vier Schichten, absteigend belastbar: VERS (im
selben Vers der Zeugen) · GLOSSE · TEIL · ELISION.
    rueckwaerts.py <buchNr> <kapitel> [<von> [<bis>]] [-o datei]
    rueckwaerts.py --wort <wort> …

**`belegt.py`** — belegt.py — ist dieses Wort im Bestand belegt, und unter welchem Lemma?

**`fixgloss.py`** — Alle Lesarten eines Lemmas oder einer Wortform mit Belegstellen.
Der dritte Modus, `verse`, druckt einen **ganzen Vers des Bestands** mit
Positionen, Mehrwort-Spannen, Lemma und Level — das ist die Form, in der
man eine Reihe uebernimmt. Zwei Agenten haben sich das nachgebaut, weil
sie nur die ersten beiden Modi kannten.
    fixgloss.py show <lemma> [<lemma> …]
    fixgloss.py showform <form> [<form> …]
    fixgloss.py verse <buchNr> <kapitel> <vers>

**`ausgaben.py`** — Die vier Referenzausgaben neben dem Vers des Quelltextes — ausgerichtet.
    ausgaben.py <buchNr> <kapitel> [<vonVers> [<bisVers>]]

**`parallelen.py`** — Parallelstellen eines Kapitels im **ganzen** annotierten Bestand.
    parallelen.py <buchNr> <kapitel> [minblock] [--alle]

**`wiederholungen.py`** — Welche Wortfolgen wiederholt der Quelltext eines Buches?
    wiederholungen.py <buchNr> [--min <tokens>] [--ab <vorkommen>]

**`dubletten.py`** — Buchinterne Dubletten: Verspaare mit hoher Wortueberlappung.
    dubletten.py <buchNr> [--anteil 0.6] [--min 5]

**`kapitelgrenzen.py`** — Ausrichtung ueber Kapitelgrenzen hinweg — was ausgaben.py nicht kann.
    kapitelgrenzen.py <buchNr> [<buchNr> …]

**`verszaehlung.py`** — Verszaehlung eines Buches gegen die vier Ausgaben — die Ausrichtungskarte.
    verszaehlung.py <buchNr> | alle

**`folgenreihe.py`** — Wie glossiert der Bestand eine WORTFOLGE? Vollstaendig, nie abgeschnitten.
    folgenreihe.py "So spricht der HERR" ["naechste Folge" ...]

**`bloecke.py`** — Blocktabelle fuer den Prompt — maschinell, nicht von Hand.
    bloecke.py <buchNr> <kap> <vers> <buchNr> <kap> <vers> [minlen]

**`vorab.py`** — Vorab-Bindungstabelle aus dem Bestand — maschinell, nicht von Hand.

**`vorlage.py`** — Parallelkapitel als gemessene Vorlage — Vers für Vers, mit Versatz.
    vorlage.py <nrA> <kapA> <nrB> <kapB> [minratio]

## Beim Einsammeln — eine einzelne Glosse aendern

**`setzen.py`** — Eine Glosse in einer Kapitelquelle aendern, an **einer**
Position, mit der erwarteten Oberflaechenform als Pflichtargument. Beim
Einsammeln von Matthaeus habe ich zweimal nach Wortform ersetzt und
jedesmal ein zweites, gleichlautendes Token mitgetroffen (`que` in 1,22,
`le` und `vous` in 6,2/6,5/6,16). Dieses Werkzeug kann das nicht.
    setzen.py <nr> <kap> <vers> <pos> <form> feld=wert […] [--grund …] [--trocken]

## Waehrend der Arbeit — Einzelfragen

**`mehrwort.py`** — Einzelwörter, die die Glosse ihres Mehrwort-Eintrags übernommen haben.
    mehrwort.py <buchNr …> | alle [--nur=Form,Form] [--fix]

**`unterwendung.py`** — Dasselbe Wort unter derselben Wendung, in einer Sprache anders gelesen.
    unterwendung.py <buchNr …> | alle [--min 3] [--wieoft 1]

**`sweep.py`** — Jede Mehrwort-Wendung des Bestands im Quelltext suchen — wo fehlt der Eintrag?
    sweep.py <buchNr …> | alle [--min 3] [--deckung 0.75] [--kapitel 3 4 5]

**`sweeplemma.py`** — Die Mehrwort-Luecken, die `sweep.py` prinzipiell nicht finden kann.
    sweeplemma.py <buchNr> <kapitel> <datei.json> [--deckung 0.6] [--alle]

**`mehrwoerter.py`** — Die Mehrwoerter, bei denen der Bestand selbst geteilter Meinung ist.
    mehrwoerter.py <buchNr> <kapitel> <datei.json> [--von 0.15] [--bis 0.6]
    Meldet NUR das Mittelfeld unter den Schwellen von `sweep` und `sweeplemma`
    und druckt beide Seiten mit Stellen und Wendungslemma — dort steht das
    Kriterium, das nirgends aufgeschrieben ist.

**`konvention.py`** — Feste Wendungen, die der Bestand als Mehrwort-Eintrag führt — fehlen sie?
    konvention.py <buchNr> <kapitel …>

**`remap.py`** — Korpusweite Korrektur einer Glosse, numerus-erhaltend.
    remap.py <lemma> <feld> alt=neu [alt=neu …] [--form <form>] [--trocken]

## Vor der Abgabe — Pflicht

**`selfcheck.py`** — Selbstprüfung für Agenten: Kapiteldatei gegen den Quelltext.
    selfcheck.py <buchNr> <kapitel> <datei.json> [<vonVers> <bisVers>]

**`glosskollision.py`** — Zwei deutsche Wörter im selben Vers, die dieselbe Glosse tragen.
    glosskollision.py <buchNr …> | alle [--kapitel <kap>]

**`levelcheck.py`** — Level gegen den Bestand — je Lemma, vor dem Build.
    levelcheck.py <buchNr> <kapitel …> [--fix]

**`qa.py`** — Inhaltliche Qualitätssicherung (Ebene 2).
    qa.py <buchNr …> | alle

## Beim Einsammeln — der Koordinator

**`paketcheck.py`** — Mehrere gleichzeitig gebaute Kapitel gegeneinander — vor dem Einsammeln.
    paketcheck.py <buchNr> <kapitel> <kapitel> [<kapitel> …]

**`folgencheck.py`** — Stehen die wiederkehrenden Wortfolgen eines Buches zeichengleich?
    folgencheck.py <buchNr> [--min 4] [--datei <ch.json> ...]

**`kreuz.py`** — Kreuzabgleich der gleichzeitig gelaufenen Kapitel einer Welle.
    kreuz.py <buchNr> <kapitel> <kapitel> [...]

**`crosscheck.py`** — Abschnittsgrenzen: welche Inhaltswörter weichen links und rechts ab.
    crosscheck.py <datei.json> <grenze> [<grenze> …]

**`konsistenz.py`** — Ein Lemma, zwei Lesarten — innerhalb eines Buches und gegen den Bestand.
    konsistenz.py <buchNr> [--min 3]

**`kongruenz.py`** — Possessiv-Kongruenz gegen das folgende Nomen — italienisch und franzoesisch.
    kongruenz.py <buchNr> [<kapitel> ...]

**`artikel.py`** — Romanische Artikel gegen das Genus des folgenden Nomens — datengetrieben.
    artikel.py <buchNr> [<kapitel> ...]

**`hilfsverb.py`** — Hilfsverb, dessen Glosse das Vollverb des Nachbartokens verschluckt.
    hilfsverb.py <buchNr …> | alle [--abstand 12]

**`wortzahl.py`** — Wortvorkommen eines Kapitels zaehlen — mit Stammpraefix, nicht exakt.
    wortzahl.py <buchNr> <kapitel> <wort> [<wort> ...]

**`ausreisser.py`** — Drei Sprachen sind sich einig, die vierte weicht ab.
    ausreisser.py <buchNr …> | alle [--min 4]

**`zweigleisig.py`** — Ein Lemma, zwei Lesarten im selben Buch — und eine davon ist hausgemacht.
    zweigleisig.py <buchNr …> | alle [--min 5] [--wieoft 2]

**`tabellenpruefung.py`** — Prüft eine Vorab-Bindungstabelle Zeile für Zeile gegen den fertigen Bestand.
    tabellenpruefung.py <tabelle.md>

## Bauen und pruefen

**`buildbook.py`** — Baut die Anno-Datei eines Buches aus den Kapitelquellen.
    buildbook.py <buchNr> [--trocken]

**`validate.py`** — Struktur-Validator (Ebene 1 der Qualitätssicherung).

**`quellen_sync.py`** — Schreibt die Kapitelquellen aus den gebauten Anno-Dateien zurück.
    quellen_sync.py <buchNr …> | alle [--nur-fehlende]

## Die Prompts selbst pruefen

**`promptcheck.py`** — Steht im Quelltext ueberhaupt, was der Prompt behauptet?
    promptcheck.py <buchNr> <kapitel …> --datei <prompt.md>

**`vorgabecheck.py`** — Stimmen die LEVEL und REIHEN, die eine Vorgabedatei nennt?
    vorgabecheck.py <datei.md|.txt> [<datei> ...]

## Bestandsauswertung

**`bindungen.py`** — Erzeugt die Bindungsliste für das Alte Testament aus dem Bestand.
    bindungen.py [-o BINDUNGEN_AT.md] [--min 8]


## Welche Werkzeuge aneinander haengen

In der Nacht auf den 09.09. sind zwei Werkzeuge an Aenderungen
kaputtgegangen, die einem dritten galten: `reflexiv.py` an einem
vergessenen Import, `paketvorb.py` an einem zusaetzlichen
Rueckgabewert von `folgenreihe.stellen()`. Vier Agenten haben
deshalb ohne ihre Bindungsdatei gearbeitet.

Die Regel „Werkzeuge nicht anfassen, waehrend Agenten laufen" steht in
BINDUNGEN. Hier steht, **welche** Datei wie weit reicht:

    hints.py        ← ausreisser · crosscheck · konsistenz · kreuz
                      mehrwort · paketcheck · unterwendung · vorab
                      zweigleisig                        (NEUN Werkzeuge)
    qa.py           ← mehrwort · zweigleisig
    validate.py     ← buildbook · selfcheck
    buildbook.py    ← remap
    folgenreihe.py  ← paketvorb
    wiederholungen  ← paketvorb
    annovorb.py     ← fravorb · itavorb
    common.py       ← alle

**`hints.py` und `common.py` sind die beiden Dateien, an denen nichts
beilaeufig geaendert wird.** Wer ihre Signatur anfasst, faellt neun
bzw. allen Werkzeugen in den Ruecken — und der Ausfall zeigt sich
nicht im geaenderten Werkzeug, sondern anderswo, oft erst in einer
Vorbereitungsdatei, die niemand mehr liest.

Wer eine Rueckgabe erweitert, packt beim Aufrufer mit `*_` aus:

    _w, voll, orte, unvoll, mehrwort, *_ = F.stellen(phr)

Dann kostet das naechste Feld keinen Lauf. `paketvorb.py` ist die
einzige Stelle im Baum, die eine fremde Rueckgabe fest auspackte;
sie ist umgestellt.

## Die Kette lief immer nur auf dem aktuellen Buch

Beim Einsammeln von 2. Korinther Paket 4 lief sie zum ersten Mal ueber
ALLE Buecher. Ergebnis: Treffer in Matthaeus, Markus, Lukas, Johannes
und Apostelgeschichte, die keiner Aenderung dieses Pakets entstammen —
italienische Hilfsverben bei Reflexiva (`si e gettato`, nicht `si ha
gettato`) und einige Mehrwortglossen. Sie liegen in
`scratchpad/befunde/altlasten_kette.md`.

Ein Werkzeug, das nur das Buch sieht, an dem gerade gearbeitet wird,
findet nichts, was vor seiner eigenen Entstehung annotiert wurde. Nach
jedem fertigen Buch lohnt ein Lauf ueber den ganzen Bestand.

## `un seul` — ein Fehlalarm der Anlautprobe, den ich stehen lasse

`artikel.py` meldet in Galates 3,20 `uno solo` → soll `un solo`. Der
Vers ist „Dieu est un seul" und riv liest woertlich „Dio è **uno
solo**": `uno` ist dort Pronomen, `solo` Adjektiv, ein Nomen gibt es
nicht. Die Probe haelt `solo` fuer das Nomen, weil die deutsche Glosse
gross ist (*ein Einziger*) — substantiviert, aber kein Nomen.

Gemessen: `seul` steht im Bestand 94x klein und 3x gross. Die Regel
„meist klein glossiert, hier gross → Substantivierung, kein Nomen"
waere also datengetragen — aber sie verschluckt `le pauvre` = *der
Arme* und `les morts` = *die Toten*, wo der Artikel sich sehr wohl auf
das substantivierte Adjektiv bezieht und die Probe zu Recht greift.
Strukturell sind die beiden Faelle nicht zu trennen.

Zwei Agenten haben die Meldung gesehen und beide richtig eingeordnet.
Eine Falschmeldung pro Buch ist billiger als eine Regel, die echte
Treffer frisst. **Wer sie sieht: am Vers nachsehen, ob hinter dem
Adjektiv ein Nomen steht. Steht keines, ist es kein Artikel.**

## Regel fuer den Koordinator: keine Textstelle zitieren, die ich nicht gelesen habe

Im Epheser-Paket haben die Agenten fuenf meiner Prompt-Angaben
widerlegt, alle aus derselben Ursache — ich hatte aus dem Gedaechtnis
zitiert statt den Quelltext zu lesen:

    „par la grâce vous êtes sauvés, par le moyen de la foi"
        → 2,8 ist ein Spaltsatz und liest schlicht `par la foi`;
          2,5 liest `par grâce` OHNE Artikel
    `abolir`, `justifier`          → kommen im Kapitel nicht vor
    „non par les œuvres hat in Roemer 3 eine Entsprechung"
        → steht genau einmal im Bestand, Galater 2,16
    „2,14-22: dort steht viel Neues"
        → von 469 Tokens waren fuenf formunbelegt

Dasselbe in Galater: mein Zitat von 6,11 stammte aus der
UNMODERNISIERTEN LSG. Und `rueckwaerts` fuehrt die fr-Spalte der
ZEUGEN als Glosse — `rémission` sieht dort belegt aus, steht aber im
ganzen lsg1910mod nur in Eph 1,7; ueberall sonst modernisiert zu
`pardon`.

Die Agenten haben jedes Mal richtig gemessen, bevor sie folgten. Aber
es ist Arbeit, die ich ihnen aufgeladen habe. **Wo ich im Prompt einen
Wortlaut nenne, lese ich ihn vorher im Quelltext nach — oder ich nenne
ihn nicht.** Ein Hinweis „pruef, ob X vorkommt" kostet nichts; ein
falsches Zitat kostet einen Durchgang.
