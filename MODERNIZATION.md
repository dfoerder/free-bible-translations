# Modernisierungs-Konzept

Wie die modernisierten Fassungen (`…mod`) aus dem gemeinfreien Grundtext
entstehen — und nach welchen Regeln `l1912mod` konkret erzeugt wurde.

## Verfahren

- Der Grundtext wird **kapitelweise** an ein KI-Modell (Anthropic Claude) über
  die **Batch-API** gegeben, zusammen mit dem unten stehenden System-Prompt.
- Modell: `claude-sonnet-5` (Standard der Pipeline — günstiger als Opus, für
  diese Textmenge das bessere Kosten/Nutzen-Verhältnis). Das bestehende
  `l1912mod` wurde noch mit `claude-sonnet-4-20250514` und der alten Ton-Regel
  erzeugt und wird bei einem Neulauf ersetzt.
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
| Rechtschreibung (1. Mose 1:5) | …Da **ward** aus Abend und Morgen der erste Tag. | …Da **wurde** aus Abend und Morgen der erste Tag. |
| Wörter + Satzbau (Johannes 3:16) | **Also**… geliebt, **daß**… gab, **auf daß** alle… | **So**… geliebt, **dass**… gab, **damit** alle… |
| Veraltetes Wort (1. Mose 2:24) | …an seinem **Weibe hangen**… | …seiner **Frau anhangen**… |
| Genealogie (1. Mose 5:6) | …**zeugte** Enos | …**war der Vater von** Enos. |

Alle Änderungen lassen sich versweise in [`compare.html`](compare.html) mit
wortgenauem Diff nachvollziehen.

## Grenzen / offene Punkte

- Die Modernisierung ist **maschinell** — sie kann vereinzelt Nuancen verändern.
  Genau dafür ist das Vergleichswerkzeug da: zum stichprobenartigen Prüfen.
- `sch1951mod` wurde **nicht** mit diesem Konzept erzeugt, sondern nur leicht
  (v. a. Rechtschreibung) — daher uneinheitlich zu `l1912mod`. Eine
  Neu-Modernisierung mit diesen Regeln steht auf der Roadmap ([README](README.md)).
