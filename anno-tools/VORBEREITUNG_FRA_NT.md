# Franzoesisches NT annotieren — was vorliegt und was zu tun ist

**Auftrag:** die Buecher 40-66 des `lsg1910mod` mit Wort-fuer-Wort-Glossen
in **Englisch, Deutsch, Italienisch und Spanisch**. Die Gegenrichtung zur
bisherigen Arbeit: dort war Deutsch der annotierte Text und Franzoesisch
eine Glossenspalte.

**Stand: Judas und Matthaeus fertig — 2 von 27 NT-Buechern.**

## Was da ist

```
bibles-translations/fra/lsg1910mod/     66 Quelltextdateien
bible-reader/bibles/fra/lsg1910mod/     dieselben, App-Kopie
bible-reader/bibles/fra/lsg1910mod/anno/   existiert nicht
anno-quellen/fra/                       existiert nicht
```

Die Registry in `index.html` fuehrt `fra-lsg1910mod` mit
`hasAnno: false`, `annoDir: null`, `annoSuffix: null`. Nach dem ersten
gebauten Buch sind diese drei zu setzen — Vorbild ist der Eintrag
`deu-l1912mod`.

## Die Zeugen — und was von ihnen schon annotiert ist

Fuer die deutsche Arbeit waren es WEB, RV1909mod, LSG1910mod, RIV1927.
Fuer die franzoesische ist **LSG der Quelltext**, also treten an ihre
Stelle die vier Zielsprachen:

```
en   eng/web
de   deu/l1912mod        ← jetzt Zeuge statt Quelle
it   ita/riv1927
es   spa/rv1909mod
```

**Drei davon sind selbst vollstaendig annotiert**, alle mit allen 27
NT-Buechern:

```
eng/web         Glossen: de · es · fr · it      66 Buecher
deu/l1912mod    Glossen: en · es · fr · it      66 Buecher
spa/rv1909mod   Glossen: en                     66 Buecher
ita/riv1927     keine
```

## Die Bruecke — 98 Prozent liegen schon vor

**`eng/web` und `deu/l1912mod` haben beide eine `fr`-Spalte**, und
zusammen decken sie genau die vier Zielsprachen ab: WEBs Quelltext
liefert das Englische und seine Spalten de/es/it, l1912mods Quelltext
das Deutsche und seine Spalten en/es/it. Ueber die gemeinsame
`fr`-Spalte als Schluessel entsteht eine Rueckwaerts-Konkordanz
**franzoesisches Wort → en · de · it · es**.

Gemessen ueber das ganze NT:

```
franzoesisches NT       185 078 Tokens, 9 578 verschiedene Woerter
als fr-Glosse belegt    181 585 Tokens (98,1 %), 7 576 Woerter (79,1 %)
```

Stichprobe der haeufigsten Inhaltswoerter — jede Zeile kommt
vollstaendig aus dem vorhandenen Bestand:

```
seigneur   677×   Lord · Herrn · Señor · Signore
disciples  257×   disciples · Jünger · discípulos · discepoli
royaume    146×   kingdom · Reich · reino · regno
gloire     167×   glory · Herrlichkeit · gloria · gloria
témoignage 124×   testimony · Zeugnis · testimonio · testimonianza
```

Das ist der grosse Unterschied zur deutschen Arbeit: dort musste jedes
Wort neu entschieden werden, hier liegt fuer 98 Prozent der Tokens
bereits ein vierfach belegter Vorschlag vor. **Ein `lexicon.py` fuer
die neue Richtung ist damit im Wesentlichen eine Auswertung des
vorhandenen Bestands**, kein Neuaufbau.

Die verbleibenden 21 Prozent der Wortformen (rund 2 000) sind die
eigentliche Arbeit — plus die Entscheidung, welcher der oft mehreren
Kandidaten je Stelle der richtige ist.

## Was an der Werkzeugkette zu tun war — erledigt

`common.py` fuehrt jetzt eine Ausgabentabelle, und **`ANNO_EDITION`**
(Default `deu/l1912mod`) entscheidet, welche Zeile gilt. Daraus leiten
sich Quelltextverzeichnis, beide Dateinamensmuster, `LANGS` und die
Liste der Referenzausgaben ab. Die deutsche Kette laeuft unveraendert
weiter; das ist an `validate`, `hints`, `lexicon`, `qa`, `artikel` und
`vorgabecheck` nachgemessen.

Dreizehn Werkzeuge hatten `en/es/fr/it` ausgeschrieben und liefen mit
`C.reihe()` / `C.zeige()` nach. Drei Fehler kamen dabei ans Licht, die
in der deutschen Richtung nie aufgefallen waeren:

- **`artikel.py` und `kongruenz.py` finden das Nomen einer Attributkette
  ueber die deutsche Grossschreibung.** Sie lasen dafuer `form` — im
  franzoesischen Text sind das franzoesische Woerter, alle klein. Beide
  Pruefungen waeren **lautlos ausgefallen**: kein Treffer, keine
  Meldung, kein Hinweis darauf, dass nichts geprueft wurde. Sie lesen
  jetzt `C.de_wort()`, also die deutsche Spalte, gleich welche Ausgabe.
- **`qa.py` und `hints.py` fuehrten deutsche Funktionswortlisten.**
  Dieselbe Falle eine Ebene tiefer. Jetzt eine Liste je
  Quelltextsprache.
- **`vorgabecheck.py` normalisierte Such- und Textseite verschieden.**
  Die Suchseite liess nur deutsche Buchstaben stehen, also wurde
  `jésus` zu `j sus`, und „de notre Seigneur Jésus-Christ" galt als
  nicht im Text stehend, obwohl Judas 1,17 genau so lautet. Gefunden am
  allerersten franzoesischen Prompt.

**Bekannte Grenze:** `promptcheck.py` haelt jedes zitierte Wort gegen den
Quelltext. In einem franzoesischen Prompt sind die zitierten Woerter aber
oft **Glossen** (deutsch, englisch) — die stehen dort zu Recht nicht. Der
Lauf meldet sie trotzdem. Fuer die deutsche Richtung war das kein
Problem, weil Prompt und Text dieselbe Sprache hatten.

## Das Rueckwaerts-Lexikon — gebaut und gemessen

`rueckwaerts.py` wertet die `fr`-Spalte beider vierspaltigen Zeugen aus.
Vier Schichten, absteigend belastbar:

    VERS       das Wort steht als fr-Glosse in GENAU DIESEM Vers
    GLOSSE     es steht anderswo im NT als fr-Glosse
    TEIL       nur innerhalb einer mehrwortigen Glosse (`des` in `de les`)
    ELISION    nur die Haelften (`qu'ils` = `qu'` + `ils`)

An Judas gemessen: 612 Tokens, 98 Prozent belegt, davon rund die Haelfte
aus dem eigenen Vers. **Elf Woerter bleiben** — das ist die eigentliche
Arbeit eines Kapitels.

## Was aus der deutschen Arbeit uebertragbar ist

Alles Verfahrensmaessige: ein Agent je Kapitel, Pakete zu drei Kapiteln,
`wiederholungen.py` vor der Arbeit, `folgencheck.py` beim Einsammeln,
beide Promptpruefungen vor dem Start. **Nicht uebertragbar** sind die
inhaltlichen Bindungen: `BINDUNGEN_AT.md`, die Wortfelder und die
`spricht`-Stellungsregel gelten fuer den deutschen Text.
