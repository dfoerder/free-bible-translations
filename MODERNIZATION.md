# Modernisierungs-Konzept

Wie die modernisierten Fassungen (`…mod`) aus dem gemeinfreien Grundtext
entstehen — und nach welchen Regeln `l1912mod` konkret erzeugt wurde.

## Verfahren

- Der Grundtext wird **kapitelweise** an ein KI-Modell (Anthropic Claude) über
  die **Batch-API** gegeben, zusammen mit dem unten stehenden System-Prompt.
- Modell: `claude-sonnet-5` (Standard der Pipeline — günstiger als Opus, für
  diese Textmenge das bessere Kosten/Nutzen-Verhältnis).
- **`l1912mod` ist vollständig mit dem aktuellen Konzept modernisiert:** alle
  66 Bücher (Regel 4 = natürliche heutige Sprache, kein biblischer Ton), mit
  `claude-opus-4-8` bzw. `claude-sonnet-5`. Neues Testament (40–66) und
  Pentateuch (1–5) wurden zuerst modernisiert und vom Nutzer per
  Vergleichstool geprüft; die restlichen Bücher 6–39 (Josua bis Maleachi)
  folgten anschließend nach demselben Konzept.
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
| Genealogie (1. Mose 5:6, Pentateuch — neuer Stil) | …**zeugte** Enos | …**war der Vater von** Enos. |
| Ton + Satzbau (Johannes 3:3, NT — neuer Stil) | **Wahrlich, wahrlich**, ich sage dir: Es sei denn, **daß** jemand von neuem geboren werde… | **Ich versichere dir:** Wer nicht neu geboren wird, kann… |
| Ton (Markus 16:6, NT — neuer Stil) | Er aber **sprach** zu ihnen: **Entsetzt euch nicht!**… **Siehe da** die Stätte… | Er **sagte** zu ihnen: **Erschreckt nicht!**… **Hier ist** die Stelle… |
| Zahlwort (4. Mose 1:46, Pentateuch — neuer Stil) | …**sechsmal hunderttausend und dreitausend fünfhundertundfünfzig**. | …**sechshundertdreitausendfünfhundertfünfzig**. (Wert unverändert, nur moderne Schreibweise) |
| Ton + Satzbau (Josua 1:9, Bücher 6–39 — neuer Stil) | **Siehe**, ich habe dir geboten, **daß** du getrost und freudig seist. **Laß** dir nicht grauen und entsetze dich nicht… | Ich habe dir befohlen, mutig und stark zu sein. **Hab keine Angst** und lass dich nicht entmutigen… |

Alle Beispiele oben zeigen den **aktuellen, einheitlichen Stand** nach der
Neu-Modernisierung — Pentateuch, NT und die restlichen Bücher 6–39 folgen
demselben Konzept (Regel 4 = natürliche heutige Sprache, kein biblischer Ton).

**Bekannte kleine Inkonsistenz:** Bei großen Zahlen (v. a. in 4. Mose) schreiben
manche Kapitel sie in moderner Zusammenschreibung („sechshundertdreitausend"),
andere behalten Luthers Schreibweise („sechsmal hunderttausend und
dreitausend") — je nachdem, welcher Batch das Kapitel bearbeitet hat. Die
**Zahlenwerte selbst sind überall korrekt**, nur der Schreibstil variiert;
eine Vereinheitlichung steht noch aus.

Alle Änderungen lassen sich versweise in [`compare.html`](compare.html) mit
wortgenauem Diff nachvollziehen.

## Grenzen / offene Punkte

- Die Modernisierung ist **maschinell** — sie kann vereinzelt Nuancen verändern.
  Genau dafür ist das Vergleichswerkzeug da: zum stichprobenartigen Prüfen.
- `sch1951mod` wurde **nicht** mit diesem Konzept erzeugt, sondern nur leicht
  (v. a. Rechtschreibung) — daher uneinheitlich zu `l1912mod`. Eine
  Neu-Modernisierung mit diesen Regeln steht auf der Roadmap ([README](README.md)).
