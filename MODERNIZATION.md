# Modernisierungs-Konzept

Wie die modernisierten Fassungen (`…mod`) aus dem gemeinfreien Grundtext
entstehen — und nach welchen Regeln `l1912mod` konkret erzeugt wurde.

## Verfahren

- Der Grundtext wird **kapitelweise** an ein KI-Modell (Anthropic Claude) über
  die **Batch-API** gegeben, zusammen mit dem unten stehenden System-Prompt.
- Modell: `claude-sonnet-5` (Standard der Pipeline — günstiger als Opus, für
  diese Textmenge das bessere Kosten/Nutzen-Verhältnis).
- **Aktueller Stand von `l1912mod` ist gemischt:** Das **Neue Testament**
  (Bücher 40–66) wurde komplett mit dem aktuellen Konzept (Regel 4 = natürliche
  heutige Sprache, kein biblischer Ton) neu modernisiert, mit `claude-opus-4-8`
  bzw. `claude-sonnet-5`. Das **Alte Testament** (Bücher 1–39) stammt noch aus
  dem ursprünglichen Lauf mit `claude-sonnet-4-20250514` und der älteren
  Ton-Regel („würdevoll und biblisch") — eine Neu-Modernisierung ist geplant
  (siehe [README](README.md) → Roadmap).
- Das Modell gibt nur modernisierte Verse zurück (JSON), Versnummern bleiben
  erhalten → die modernisierte Fassung ist **versgenau deckungsgleich** mit dem
  Grundtext (bei `l1912` geprüft: 0 Abweichungen, 31171 Verse).
- Die maßgebliche, ausführbare Fassung dieser Regeln steht im Code:
  [`tools/modernize_submit.py`](tools/modernize_submit.py) → `SYSTEM_PROMPT_TMPL`.
  Dieses Dokument ist die lesbare Beschreibung davon.

> Hinweis zur Herkunft: `l1912mod` wurde ursprünglich im Schwesterprojekt
> `bible-reader` erzeugt (`modernize_batch_submit.py`, **identischer Regeltext**).
> Für neue Läufe wird das generalisierte Skript in `tools/` verwendet.

## Die Regeln (System-Prompt)

Dem Modell wird gesagt: *„Du modernisierst den Text der {Übersetzung} für heutige
Leser (auch Nicht-Muttersprachler)."* — mit diesen Regeln:

1. **Rechtschreibung modernisieren** — `daß→dass`, `ward→wurde`, `Laß→Lass` usw.
2. **Veraltete Wörter ersetzen**, u. a.:
   - `zeugte` → war der Vater von
   - `Weib` → Frau
   - `Gemahl` → Frau / Mann (je nach Kontext)
   - `allda` → dort · `gen` → nach
   - `Otterngezüchte` → Schlangenbrut · `genugsam` → wert
   - `Buße tun` → umkehren · `Glieder` (Generationen) → Generationen
   - `Weisen vom Morgenland` → Sterndeuter aus dem Osten
   - `erkannte sie (nicht)` → schlief (nicht) mit ihr
   - weitere veraltete Ausdrücke sinngemäß
3. **Satzbau vereinfachen** — lange Schachtelsätze in kürzere, klare Sätze teilen.
4. **Natürliche, heutige Sprache** — klar und verständlich; **kein** altertümlicher
   oder gehoben-„biblischer" Ton, sondern so, wie man heute normal schreibt.
5. **Inhaltlich treu bleiben** — keine theologischen Änderungen, keine
   Ergänzungen, nichts weglassen.
6. **Eigennamen beibehalten** wie im Original.

## Beispiele aus `l1912` → `l1912mod`

| Regel | Grundtext (Luther 1912) | modernisiert |
|-------|-------------------------|--------------|
| Rechtschreibung (1. Mose 1:5, AT — alter Stil) | …Da **ward** aus Abend und Morgen der erste Tag. | …Da **wurde** aus Abend und Morgen der erste Tag. |
| Veraltetes Wort (1. Mose 2:24, AT — alter Stil) | …an seinem **Weibe hangen**… | …seiner **Frau anhangen**… |
| Genealogie (1. Mose 5:6, AT — alter Stil) | …**zeugte** Enos | …**war der Vater von** Enos. |
| Ton + Satzbau (Johannes 3:3, NT — neuer Stil) | **Wahrlich, wahrlich**, ich sage dir: Es sei denn, **daß** jemand von neuem geboren werde… | **Ich versichere dir:** Wer nicht neu geboren wird, kann… |
| Ton (Markus 16:6, NT — neuer Stil) | Er aber **sprach** zu ihnen: **Entsetzt euch nicht!**… **Siehe da** die Stätte… | Er **sagte** zu ihnen: **Erschreckt nicht!**… **Hier ist** die Stelle… |

Die AT-Beispiele zeigen den **noch nicht neu modernisierten** Stand (Regeln 1–3
und 5–6 galten schon vorher; nur Regel 4, der Ton, war anders). Die NT-Beispiele
zeigen den **aktuellen** Stand nach der Neu-Modernisierung.

Alle Änderungen lassen sich versweise in [`compare.html`](compare.html) mit
wortgenauem Diff nachvollziehen.

## Grenzen / offene Punkte

- Die Modernisierung ist **maschinell** — sie kann vereinzelt Nuancen verändern.
  Genau dafür ist das Vergleichswerkzeug da: zum stichprobenartigen Prüfen.
- `sch1951mod` wurde **nicht** mit diesem Konzept erzeugt, sondern nur leicht
  (v. a. Rechtschreibung) — daher uneinheitlich zu `l1912mod`. Eine
  Neu-Modernisierung mit diesen Regeln steht auf der Roadmap ([README](README.md)).
