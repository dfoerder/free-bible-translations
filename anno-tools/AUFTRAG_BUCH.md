# AUFTRAG_BUCH — der Ablauf für ein Kapitel der Bücher 21–39

Gilt für alle noch offenen Bücher des Alten Testaments. Der Prompt eines
Agenten nennt nur noch die Buchnummer, das Kapitel und das, was an diesem
Kapitel besonders ist; alles Wiederkehrende steht hier.

Entstanden aus `AUFTRAG_SPRUECHE.md` nach dem Abschluss von Buch 20. Was dort
buchspezifisch war, steht jetzt in `WORTFELD_<BUCH>.md`.

## Vorbereitung — in dieser Reihenfolge

1. `SPEC.md` — Datenformat und Verbote.
2. `AUFTRAG_AT.md` — der allgemeine Ablauf für das Alte Testament.
   **Ganz lesen.** Besonders „Die drei Fallen des Alten Testaments" und
   „Die Glossen folgen den vier Referenzausgaben".
3. `WORTFELD_<BUCH>.md` — was für dieses Buch feststeht. Wächst mit jedem
   Paket; lies **alle** Abschnitte, nicht nur die ersten.
4. `VERSZAEHLUNG_21_39.md`, Abschnitt zu deinem Buch — **ob dein Kapitel
   gegen die Ausgaben ausgerichtet ist.** Bei den Prophetenbüchern ist
   Übereinstimmung die Ausnahme, nicht die Regel.
5. `DUBLETTEN_<BUCH>.md`, falls vorhanden — die buchinternen Verspaare.
   Steht dein Kapitel dort, ist der Partner entweder schon fertig (dann
   übernimmst du seine Glossenreihe, wo der Text wörtlich gleich ist) oder er
   kommt noch (dann ist deine Reihe die Vorlage). **Wo der Text nicht wörtlich
   gleich ist, nicht abschreiben.**
6. `BINDUNGEN_AT.md`, Abschnitt zu deinem Buch und die allgemeinen Bindungen.
   Die Tabelle ist **erzeugt** (`bindungen.py`) und wird nach jedem fertigen
   Buch neu gebaut — eine veraltete Tabelle führt aktiv in die Irre. Nach dem
   Abschluss von Hiob, Psalmen und Sprüchen war sie es: `Netz` stand dort mit
   *caul · redaño · membrane* („das Fettnetz des Opfertiers", damals 11 von 14
   AT-Belegen), während die AT-Mehrheit inzwischen mit 18 von 31 das
   **Fischernetz** ist. Der Agent von Prediger 9 hat es am Vers gemerkt.
   **Wenn eine Bindung nicht zum Vers passt, immer zusätzlich `fixgloss.py`
   fragen** — die Tabelle nennt nur die häufigste Lesart, `fixgloss.py` alle.
7. Den **Quelltext** deines Kapitels lesen:
   `bible-reader/bibles/deu/l1912mod/<buchNr>_l1912mod.json` →
   `chapters["<kapitel>"]`. Nicht aus der Bibelkenntnis arbeiten.

## Der Prompt ist geprüfte Ware — und trotzdem nur ein Hinweis

Seit Daniel Paket 3 läuft **jeder** Agentenprompt vor dem Abschicken durch
`promptcheck.py`. Es nimmt die in Backticks gesetzten deutschen Wörter und hält
sie gegen die Tokens der genannten Kapitel.

Der Anlass: in Daniel Paket 2 haben drei Agenten **neun** Vorgaben widerlegt,
und acht davon waren derselbe Fehler — der Koordinator hatte Kapitelwortschatz
aus der Bibelkenntnis geschrieben statt aus dem Quelltext. `Kalk`, `Gelenke`,
`Fasten`, `Siegelring`, `Verklagten` und `Wildesel` stehen in den genannten
Kapiteln nicht; `Löwe` galt als unbelegt und hat 105 Belege. Das Werkzeug lag
seit Jesaja bereit und war nur auf die Buchvorbereitung angewandt worden, nicht
auf die Prompts.

**Für dich ändert das nichts an der Regel:** ein Hinweis lenkt die
Aufmerksamkeit, er hat nicht recht. `promptcheck.py` findet Wörter, die gar
nicht vorkommen — es findet nicht, ob eine Zahl stimmt, ob eine Stelle richtig
genannt ist oder ob ein Wort im Vers etwas anderes bedeutet als angesagt. Das
bleibt deine Arbeit, und sie ist in jedem Paket der ertragreichste Befund.

## Die Werkzeuge, die du je Kapitel laufen lässt

```
python3 ausgaben.py <nr> <kap>            # die vier Ausgaben, inhaltlich ausgerichtet
python3 lexicon.py <nr> <kap>             # wie der Bestand jede Wortform übersetzt
python3 hints.py <nr> <kap>               # unbelegte Formen, Kollisionen, Mehrdeutigkeit
python3 parallelen.py <nr> <kap>          # Parallelstellen im Bestand
```

**`ausgaben.py` ist Pflicht**, und bei den Propheten wichtiger als in den
Sprüchen: die Ausrichtungskarte zeigt, dass in fast jedem Buch einzelne Kapitel
wackeln. Wo `ausgaben.py` `FEHLT in der Datei der Ausgabe` schreibt, hat diese
Ausgabe für den Vers **keine Vorlage** — nicht die Nachbarzeile nehmen.

## Prüfung vor der Abgabe — alle sechs müssen gelaufen sein

```
python3 selfcheck.py <nr> <kap> $ANNO_OUT/<nr>/ch<kap>.json
python3 qa.py --kapitel <nr> <kap> $ANNO_OUT/<nr>/ch<kap>.json
python3 konvention.py <nr> <kap>
python3 sweep.py <nr> --kapitel <kap>
python3 glosskollision.py --datei <nr> <kap> $ANNO_OUT/<nr>/ch<kap>.json
python3 levelcheck.py <nr> <kap>
```

`selfcheck.py` muss fehlerfrei durchlaufen — das ist die harte Bedingung. Die
anderen fünf melden **Verdacht, keine Fehler**: jeden Treffer am Vers ansehen
und entscheiden.

### Was die Läufe in Buch 20 tatsächlich geleistet haben

**`glosskollision.py` ist der wichtigste.** Über das ganze Buch 20 hat
`hints.py` 30 Kollisionspaare gemeldet, davon waren **sechs Fehlalarme**; und
es hat **mindestens 25 echte Kollisionen nicht gesehen**, weil es formbasiert
im Quelltext gegen den Bestand sucht und deshalb blind ist, sobald eine Form
unbelegt ist oder die Kollision erst durch deine eigene Entscheidung entsteht.
In fünf Kapiteln meldete es null Paare, während `glosskollision.py` vier bis
sechs echte fand. **Lies die Rangfolge im Kopf des Skripts: „1 von 4" ist der
stärkste Verdacht**, und setz `--nurinhalt` nicht.

**`levelcheck.py` findet mehr als Level.** In Buch 20 hat es dreimal einen
Bestandsbeleg gefunden, den der Lexikon-Extrakt formbasiert nicht zeigte
(`Steinmauer`, `guttun`, und drei Mehrwort-Lemmata, die ein Agent für neu
hielt). Die anderen fünf Läufe waren dort mit 0 Treffern durchgelaufen.

## Die vier Fehlerklassen, die in Buch 20 am meisten gekostet haben

**1. Partikeln trennbarer Verben.** Vier der sechs `hints.py`-Fehlalarme waren
das: `ab` in „weicht … ab", `heran` in „bringt … heran", `weise … zurecht`
(zweimal als vermeintliches Adjektiv gemeldet, tatsächlich Imperative von
`weisen`). **Zähl die Partikeln deines Kapitels selbst nach**, und prüfe bei
jedem gemeldeten Paar zuerst, ob eines der beiden Wörter zu einem trennbaren
Verb gehört.

**2. Die Lexikonfalle in ihren Varianten.** Der Extrakt zeigt die
Korpusmehrheit, und die kann aus einem ganz anderen Sachfeld stammen:
`Geheimnis` hatte 22 Belege, **sämtlich NT** und alle *mystery*; `tüchtig` 11
Belege, alle „diensttaugliche Männer"; `Besonnenheit` zwei NT-Belege in der
Bedeutung „Selbstbeherrschung". Umgekehrt kann im AT die **NT**-Lesart die
richtige sein: `Fremder` hat 80 AT-Belege als *Fremdling im Land*, aber gemeint
war der Außenstehende. **Die Bindung gilt für dieselbe Bedeutung, nicht für
dieselbe Buchstabenfolge** — in beide Richtungen.

**3. Der Prompt-Hinweis.** In Buch 20 haben die Agenten **über fünfzig**
Prompt-Hinweise am Quelltext widerlegt: genannte Wörter, die im Text nicht
stehen, Substantive, die in Wahrheit Adjektive sind, Wendungen, die negiert
sind. Der Hinweis lenkt die Aufmerksamkeit, er hat nicht recht. **Prüf jeden
am Quelltext, und melde jede Abweichung** — das ist der häufigste echte Befund.

**4. Fehlende Mehrwort-Einträge.** Für `selfcheck.py` und `qa.py` prinzipiell
unsichtbar: die Einzelwörter sind vollständig und richtig, strukturell fehlt
nichts. `sweep.py` und `konvention.py` suchen danach; beide melden auch
Fehlalarme, die am Vers zu entscheiden sind.

## Wo aufgelöst wird, und wo nicht

Eine Kollisionsauflösung gehört **an die Kollisionsstelle, nicht ans Lemma**.
Wo zwei deutsche Wörter im selben Vers dieselbe Glosse tragen, weicht das
**schwächer gebundene** aus — und zwar bevorzugt auf eine **zweite Lesart, die
der Bestand schon führt**, nicht auf eine erfundene.

Wo sie in **verschiedenen** Versen stehen, wird **nicht** aufgelöst: eine
Auflösung ohne Kollisionsstelle macht den Bestand nur inkonsistent. Melden
genügt.

Wo nur **eine Sprache** zusammenfällt, weicht nur diese eine aus. Das war in
Buch 20 der Regelfall (8,13 · 13,20 · 21,14 · 27,19).

**Manche Kollision bleibt bewusst stehen.** Verb und Stammsubstantiv
(`Schlaf`/`schlafen`), figura etymologica („den Armen, weil er arm ist"),
synonymer Parallelismus und die echten Verschmelzungen der Zielsprachen
(spanisch *su* für „ihr"/„seine", französisch *le* für Artikel und Klitikon)
sind keine Fehler. Wenn alle vier Ausgaben das Wort selbst wiederholen, ist das
ein starkes Argument fürs Stehenlassen.

## Abgabe

Eine Datei `$ANNO_OUT/<nr>/ch<kap>.json`, Inhalt `{"<vers>": [...]}` über
**alle** Verse des Kapitels.

Dazu ein Bericht mit:

- **Wortfeld**: jeder Begriff, der über dein Kapitel hinausläuft, mit den vier
  Glossen und dem Level. Er kommt ins `WORTFELD_<BUCH>.md`.
- **Abweichungen vom Auftrag**: wo der Quelltext etwas anderes sagt als ein
  Hinweis.
- **Befunde im Bestand**: wo der Lexikon-Extrakt uneinheitlich ist oder eine
  Bindung falsch aussieht. Nicht selbst korpusweit korrigieren — melden.
- **Befunde in den Ausgaben**: fehlende Verse, Importartefakte.
- **Wenn dein Kapitel eine Dublette hat**: den Vers Wort für Wort, mit allen
  vier Glossen und Leveln. Läuft der Partner gleichzeitig, ist das die einzige
  Möglichkeit der Abstimmung — der Koordinator führt die Fassungen zusammen.

## Ein Unterschied, der kein Befund ist

Die **Kapitelquelle** und das **gebaute Buch** können sich im `level`
unterscheiden. `buildbook.py` zieht beim Bauen zwei Angleichungen durch.
**Nicht als Befund melden.**

## Was nie passiert

- ins Repository `bible-reader` schreiben (nur lesen)
- eigene Subagenten starten
- einen Namen deuten, den der Text nicht selbst deutet
- ein Kapitel als „fertig" melden, das `selfcheck.py` nicht sauber durchläuft

## „Im Bestand unbelegt" — erst `belegt.py` fragen, dann glauben

**Zweimal in zwei Buechern hat die Vorbereitung ein Wort als unbelegt gefuehrt,
das laengst im Bestand stand.** Beide Male stand es im Auftrag als Tatsache, und
beide Male hat erst der Kapitelagent es widerlegt:

| Wort | Buch | angeblich | tatsaechlich |
|---|---|---|---|
| `beschwoeren` | Hohelied | „im AT unbelegt (NT 3×)" | **13 Belege, 9 davon AT** |
| `Heerscharen` | Jesaja | „im gesamten Bestand unbelegt" | **34 Belege** unter Lemma `Heerschar` |

Die Ursache ist beide Male dieselbe: **`fixgloss.py show` erwartet ein LEMMA,
keine Wortform.** Es schweigt bei `beschwoere` (Lemma `beschwoeren`) und bei
`Heerscharen` (Lemma `Heerschar`, der Bestand normalisiert auf den Singular).
Wer die Form abfragt, die im Quelltext steht, bekommt „nichts gefunden" und
haelt das fuer eine Auskunft ueber die Sache.

**Deshalb: `belegt.py <Wortform>` fragen.** Es sucht die Form direkt im
gebauten Bestand, nennt das Lemma, unter dem sie gefuehrt wird, und warnt
ausdruecklich, wenn Lemma und Form auseinandergehen.

```
python3 belegt.py Heerscharen
python3 belegt.py Braut Schleier beschwoere      # mehrere auf einmal
python3 belegt.py -d 23                          # alle unbelegten Formen eines Buches
```

Es unterscheidet Gross- und Kleinschreibung, wo sie zwei Woerter trennt
(`Spross` das Substantiv gegen `spross` von `sprießen`).

**Bleibt es dabei, dass die Form unbelegt ist**, erst dann `lexicon.py` ueber
den Stamm und `fixgloss.py show <vermutetes Lemma>` — und erst danach etwas
Neues erfinden.

**Und umgekehrt:** steht im Auftrag „unbelegt", ist das ein **Hinweis, keine
Tatsache**. Pruefen und die Abweichung melden, wie es beide Agenten getan haben.

## Wenn der l1912mod einen Namen selbst uebersetzt

Die Regel „**niemals einen Namen deuten, den der Text nicht selbst deutet**"
hat eine Kehrseite, die leicht uebersehen wird: **manchmal deutet der Text
selbst** — dann wird die Deutung glossiert, nicht die Transliteration.

Gefunden vom Agenten fuer **Jesaja 8**. Der Auftrag nannte den Namen aus 8,1
und 8,3 `Maher-Schalal-Hasch-Bas`. Der l1912mod schreibt dort aber

> „schreib darauf in gewoehnlicher Schrift: **Schnell-Raub-Eilige-Beute**"

— vier deutsche Woerter in einem Bindestrich-Token. Luther macht das
gelegentlich, und **der Bestand folgt ihm bereits**:

| Stelle | hebraeisch | l1912mod | Bestandsglosse |
|---|---|---|---|
| 1Mo 23 u. oe. | Machpela | `Doppelhöhle` C1 | *double cave · cueva doble · grotte double · grotta doppia* |
| Ri 20,1 u. oe. | Mizpa | `Warte` C1 | *watchtower · atalaya · tour de guet · torre di guardia* |

**Woran man die beiden Faelle unterscheidet:** steht im deutschen Text ein
deutsches Wort (oder eine Kette deutscher Woerter), wird es **uebersetzt** —
auch wenn die Ausgaben transliterieren. Steht dort eine Lautfolge ohne deutsche
Bedeutung (`Baal-Hamon`, `Adoni-Zedek`, `Abel-Mehola`), bleibt sie **Name**.
Alle Bindestrich-Lemmata des Bestands ausser den beiden oben sind
Transliterationen und bleiben es.

Die Ausgaben helfen hier nicht: in Jes 8,1 **uebersetzen LSG und RIV** („Qu'on
se haate de piller, qu'on se precipite sur le butin" / „Affrettate il
saccheggio! Presto, al bottino!") und **transliterieren in 8,3**, waehrend WEB
und RV an beiden Stellen transliterieren. Entschieden wird nach dem deutschen
Text.
