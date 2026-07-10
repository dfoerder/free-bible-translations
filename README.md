# bibles-translations

Eine Sammlung **gemeinfreier Bibelübersetzungen**, für heutige Leser
**modernisiert** — verständliche, natürliche heutige Sprache statt
altertümlicher Wendungen, bei möglichst treuem Inhalt.

Die Übersetzungen liegen als schlichte JSON-Dateien vor (ein Buch pro Datei),
sodass sie sich leicht in Apps, Websites oder Skripten weiterverwenden lassen.

## Bestand

| Sprache | ID | Übersetzung | Typ | Stand |
|---------|----|-------------|-----|-------|
| Deutsch | `sch1951` | Schlachter 1951 | Grundtext | 66 Bücher |
| Deutsch | `sch1951mod` | Schlachter 1951 (modernisiert) | leicht modernisiert | 66 Bücher |
| Deutsch | `l1912` | Luther 1912 | Grundtext | 66 Bücher, 31171 Verse |
| Deutsch | `l1912mod` | Luther 1912 (modernisiert) | voll modernisiert | 66 Bücher (versgenau zu `l1912`) |
| English | `web` | World English Bible | Grundtext (bereits modern) | 66 Bücher, 31095 Verse |
| Français | `lsg1910` | Louis Segond 1910 | Grundtext | 66 Bücher, 31169 Verse |
| Français | `lsg1910mod` | Louis Segond 1910 (modernisiert) | voll modernisiert | 66 Bücher (versgenau zu `lsg1910`) |
| Italiano | `riv1927` | Riveduta (Luzzi) 1927 | Grundtext | 66 Bücher, 31039 Verse |
| Italiano | `riv1927mod` | Riveduta (Luzzi) 1927 (modernisiert) | voll modernisiert | 66 Bücher (versgenau zu `riv1927`) |
| Español | `rv1909` | Reina-Valera 1909 | Grundtext | 66 Bücher, 31084 Verse |
| Español | `rv1909mod` | Reina-Valera 1909 (modernisiert) | voll modernisiert | 66 Bücher (versgenau zu `rv1909`) |

Insgesamt **11 Übersetzungen in 5 Sprachen** (726 Buchdateien). Zur Lizenz-/
Gemeinfreiheitslage jeder Übersetzung: siehe unten.

Zur Lizenz-/Gemeinfreiheitslage jeder Übersetzung: **[SOURCES.md](SOURCES.md)**.

## Verzeichnisstruktur

```
<lang>/<id>/<nr>_<id>.json      z. B. deu/l1912mod/40_l1912mod.json
```

- `<lang>` — ISO-639-3 Sprachcode (`deu`, `eng`, `fra`, `ita`, `spa`)
- `<id>` — Übersetzungs-ID; Suffix `mod` = modernisierte Fassung
- `<nr>` — Buchnummer 1–66 (protestantischer Kanon; 1 = Genesis … 66 = Offenbarung)

Ergänzende Dateien im Wurzelverzeichnis:

- `books.json` — die 66 Bücher (Nummer, OSIS-Kürzel, Testament, Kapitelzahl, Namen)
- `manifest.json` — maschinenlesbarer Index aller Übersetzungen
- `tools/` — Python-Werkzeuge (Normalisierung, Modernisierungs-Pipeline)

## Dateiformat

Jede Buchdatei ist ein JSON-Objekt:

```json
{
"name": "1. Mose",
"chapters": {
"1": {
"1": "Im Anfang schuf Gott den Himmel und die Erde.",
"2": "..."}
}}
```

Kanonisch serialisiert mit `json.dumps(obj, ensure_ascii=False, indent=0)` —
**ein Vers pro Zeile**. Das hält git-Diffs lesbar (wichtig beim Nachbessern
modernisierter Texte), ohne die Dateien nennenswert zu vergrößern.

Vereinheitlichen/prüfen:

```bash
python3 tools/normalize.py          # gesamte Sammlung normalisieren
python3 tools/normalize.py --check  # nur validieren (Exit-Code ≠ 0 bei Fehlern)
```

`normalize.py` prüft dabei: gültiges JSON, `name` vorhanden, rein numerische
Kapitel-/Versschlüssel, keine leeren Verse, Anzahl der Bücher.

## Vergleichen & prüfen (`compare.html`)

Zum versweisen Gegenüberstellen von Grundtext und modernisierter Fassung gibt
es die Seite `compare.html`: Inhaltsverzeichnis (AT/NT) links, zwei Spalten
nebeneinander, **wortgenaues Hervorheben der Änderungen**, Filter „nur geänderte
Verse" und eine Änderungs-Statistik pro Kapitel. Das Übersetzungspaar ist oben
wählbar (Luther, Schlachter, Segond, Riveduta, Reina-Valera).

Sie lädt die JSON-Dateien per `fetch`, braucht also einen lokalen Server
(direktes Öffnen als Datei blockiert der Browser):

```bash
python3 -m http.server 8123      # im Projektordner
# dann im Browser öffnen:
#   http://localhost:8123/compare.html
#   http://localhost:8123/compare.html#l1912mod/43/3   (Deep-Link: Joh 3)
```

Die Seite ist datengetrieben: neue Übersetzungspaare (aus `manifest.json`)
erscheinen automatisch, sobald ein Eintrag ein `base`-Feld hat.

## Wie modernisiert wird

Modernisierte Fassungen (`…mod`) entstehen aus dem gemeinfreien Grundtext über
die **Anthropic Batch-API** (50 % günstiger), kapitelweise, mit einem
deutschsprachigen System-Prompt. Leitlinien: Rechtschreibung angleichen,
veraltete Wörter ersetzen, Schachtelsätze auflösen, **natürliche heutige Sprache
(kein biblischer Ton), inhaltlich treu bleiben, nichts hinzufügen oder weglassen,
Eigennamen behalten**.

**Das genaue Konzept — welche Regeln gelten und Vorher/Nachher-Beispiele —
steht in [MODERNIZATION.md](MODERNIZATION.md).** Die maßgebliche, ausführbare
Fassung ist der System-Prompt in [`tools/modernize_submit.py`](tools/modernize_submit.py).

```bash
export ANTHROPIC_API_KEY=sk-ant-...

# 1) Kapitel einreichen (Beispiel: Luther 1912 → l1912mod, ganze Bibel)
python3 tools/modernize_submit.py \
    --lang deu --src l1912 --dst l1912mod \
    --name "Luther-Bibel von 1912" 1-66

# 2) Ergebnisse abholen und schreiben (wartet bis fertig)
python3 tools/modernize_collect.py --wait

# danach vereinheitlichen
python3 tools/normalize.py deu/l1912mod
```

Buchbereiche sind frei wählbar (`40-43`, `1`, `1-66`), `--skip-existing`
überspringt bereits modernisierte Kapitel. Der Batch-Status liegt in
`tools/.modernize_state.json` (nicht eingecheckt).

## Roadmap

- [ ] Rechtelage klären, offene Punkte in [SOURCES.md](SOURCES.md) auflösen
      (v. a. Schlachter 1951).
- [x] Luther-1912-**Grundtext** (`deu/l1912`) aufgenommen (Quelle: Beblia,
      Public Domain; versgenau deckungsgleich mit `l1912mod`).
- [x] `l1912mod` — **Neues Testament** (Bücher 40–66) neu modernisiert mit dem
      aktuellen Ton-Konzept (natürliche heutige Sprache, kein biblischer Ton;
      siehe [MODERNIZATION.md](MODERNIZATION.md)).
- [x] `l1912mod` — **Pentateuch** (Bücher 1–5, 1. Mose bis 5. Mose) ebenso
      neu modernisiert.
- [x] `l1912mod` — **restliches Altes Testament** (Bücher 6–39, Josua bis
      Maleachi) mit demselben Konzept neu modernisiert. `l1912mod` ist damit
      komplett (alle 66 Bücher im einheitlichen neuen Stil).
- [ ] `sch1951mod` mit der vollen Pipeline neu erzeugen (aktuell nur leicht,
      d. h. uneinheitlich zu `l1912mod`).
- [x] Weitere Sprachen übernommen: `eng/web`, `fra/lsg1910(mod)`,
      `ita/riv1927(mod)`, `spa/rv1909(mod)`.
- [ ] Projektlizenz für die Sammlung/Bearbeitungen festlegen.

## Lizenz

Die zugrunde liegenden Bibeltexte sind gemeinfrei bzw. in Klärung
([SOURCES.md](SOURCES.md)). Für die Sammlung selbst und die modernisierten
Bearbeitungen ist noch **keine Lizenz festgelegt** — vor einer
Veröffentlichung nachtragen.
