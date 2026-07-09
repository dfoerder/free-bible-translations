# bibles-translations

Eine Sammlung **gemeinfreier Bibelübersetzungen**, für heutige Leser
**modernisiert** — verständliche Sprache statt altertümlicher Wendungen, bei
möglichst treuem Inhalt und würdevollem Ton.

Die Übersetzungen liegen als schlichte JSON-Dateien vor (ein Buch pro Datei),
sodass sie sich leicht in Apps, Websites oder Skripten weiterverwenden lassen.

## Bestand

| Sprache | ID | Übersetzung | Typ | Stand |
|---------|----|-------------|-----|-------|
| Deutsch | `sch1951` | Schlachter 1951 | Grundtext | 66 Bücher |
| Deutsch | `sch1951mod` | Schlachter 1951 (modernisiert) | leicht modernisiert | 66 Bücher |
| Deutsch | `l1912mod` | Luther 1912 (modernisiert) | voll modernisiert | 66 Bücher |

Weitere gemeinfreie Übersetzungen (Englisch, Französisch, Italienisch,
Spanisch) sind im Schwesterprojekt `../bible-reader` vorbereitet und können
übernommen werden — siehe `manifest.json` → `planned` und die
[Roadmap](#roadmap).

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

## Wie modernisiert wird

Modernisierte Fassungen (`…mod`) entstehen aus dem gemeinfreien Grundtext über
die **Anthropic Batch-API** (50 % günstiger), kapitelweise, mit einem
deutschsprachigen System-Prompt. Leitlinien: Rechtschreibung angleichen,
veraltete Wörter ersetzen, Schachtelsätze auflösen, **Ton bewahren, inhaltlich
treu bleiben, nichts hinzufügen oder weglassen, Eigennamen behalten**.

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
- [ ] Luther-1912-**Grundtext** (`deu/l1912`) mit in die Sammlung aufnehmen
      (bisher nur die modernisierte Fassung vorhanden).
- [ ] `sch1951mod` mit der vollen Pipeline neu erzeugen (aktuell nur leicht,
      d. h. uneinheitlich zu `l1912mod`).
- [ ] Weitere Sprachen übernehmen: `eng/web`, `fra/lsg1910(mod)`,
      `ita/riv1927(mod)`, `spa/rv1909(mod)`.
- [ ] Projektlizenz für die Sammlung/Bearbeitungen festlegen.

## Lizenz

Die zugrunde liegenden Bibeltexte sind gemeinfrei bzw. in Klärung
([SOURCES.md](SOURCES.md)). Für die Sammlung selbst und die modernisierten
Bearbeitungen ist noch **keine Lizenz festgelegt** — vor einer
Veröffentlichung nachtragen.
