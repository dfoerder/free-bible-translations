# Wortfeld des Buches Hiob — festgelegt in Kapitel 1

Kapitel 1 ist der Maßstab für das ganze Buch. Diese Glossen sind **verbindlich,
wo dieselbe Bedeutung gemeint ist** — nicht, wo nur dieselbe Buchstabenfolge
steht. Wo dein Kapitel eine andere Bedeutung trägt, entscheidest du am Vers und
**meldest** es.

| deutsch | Lemma | Level | en · es · fr · it | Grundlage |
|---|---|---|---|---|
| `rechtschaffen` | rechtschaffen | C1 | blameless · íntegro · intègre · integro | Ausgaben; Auflösung gegen `aufrichtig` |
| `aufrichtig` | aufrichtig | B2 | upright · recto · droit · retto | Ausgaben |
| `gottesfürchtig` | gottesfürchtig | C1 | God-fearing · temeroso de Dios · craignant Dieu · timorato di Dio | Bestand (8) |
| `Gottessöhne` | Gottessohn | C1 | sons of God · hijos de Dios · fils de Dieu · figli di Dio | Ausgaben |
| `mied` | meiden | B2 | avoided · evitaba · évitait · evitava | Bestand (6) |
| `abgeneigt` | abgeneigt | C1 | averse · contrario · opposé · avverso | neu, muss von `meiden` unterscheidbar bleiben |
| `Satan` | Satan | A1 | Satan · Satanás · Satan · Satana | Bestand (37) |
| `Knecht` | Knecht | B2 | servant · siervo · serviteur · servo | AT-Bindung (174) |
| `HERR` | HERR | A1 | LORD · SEÑOR · ÉTERNEL · SIGNORE | AT-Bindung |
| `Hiob` | Hiob | A1 | Job · Job · Job · Giobbe | Jak 5,11 |
| `Uz` | Uz | A1 | Uz · Uz · Uts · Uz | Bestand + LSG |
| `Sabäer` | Sabäer | B2 | Sabeans · sabeos · Sabéens · Sabei | Ausgaben |
| `Chaldäer` | Chaldäer | B2 | Chaldeans · caldeos · Chaldéens · Caldei | Bestand (10) |
| `Böse` | Böse | B2 | evil · mal · mal · male | AT-Bindung |
| `Besitz` | Besitz | B2 | possession · posesión · possession · possesso | AT-Bindung (40/65), **nicht** die Korpusmehrheit *bienes* |
| `nur` | nur | A1 | Only · Solamente · Seulement · Soltanto | Auflösung gegen `allein` |
| `allein` | allein | A2 | alone · solo · seul · solo | Bestand |
| `entkommen` | entkommen | B2 | escape · escapar · échapper · sfuggire | Bestand |
| `berichten` | berichten | B1 | tell · contar · raconter · raccontare | Bestand |
| `treten` (vor den HERRN) | treten | B1 | present themselves · presentarse · se présenter · presentarsi | 4Mo 16,17 + Ausgaben |
| `preisen` | preisen | C1 | praised · alabado · loué · lodato | hält `segnen` frei |
| `Leib` (Mutterleib) | Leib | B2 | womb · vientre · ventre · grembo | Bestandslesart 2 |

## Die Botenformel

`Nur ich allein konnte entkommen, um es dir zu berichten.` steht in 1,15 ·
1,16 · 1,17 · 1,19 **viermal token-identisch** und ist dort viermal identisch
glossiert (nachgerechnet). Falls sie in einem weiteren Kapitel wiederkehrt:
Glossenfolge aus 1,15 übernehmen, samt `um zu`-Mehrwort auf [um, zu].

## Partikelkonventionen (aus dem Bestand)

`auf` (aufstehen) = up · arriba · debout · su · `an` (anbeten) = at · a · à · a ·
`aus` = out · fuera · dehors · fuori · `mit` (nehmen … mit) = along · consigo ·
avec eux · con sé · `ein` (einladen) = in · dentro · dedans · dentro ·
`dar` (darbringen) = forth · adelante · en avant · avanti · `vor` (vorwerfen) =
at · a · à · a.

## Zwei Auflösungen, die für das ganze Buch gelten

- **`rechtschaffen` ↔ `aufrichtig`** laufen im Bestand in es und it zusammen
  (*recto* / *retto*). In Hiob stehen sie in 1,1 · 1,8 · 2,3 nebeneinander,
  deshalb getrennt. `rechtschaffen` kollidiert außerdem mit `unschuldig` (4,7)
  und `untadelig` (12,4) — siehe `BUCHKOLLISIONEN.md`.
- **`nur` ↔ `allein`** — der Bestand gibt beiden es *solo*, it *solo*, teils fr
  *seul*. `nur` steht kapitelweit auf *Only · Solamente · Seulement · Soltanto*.

## Was der Bestand nicht hergab

Diese Fälle hat Kapitel 1 am Quelltext und an den Ausgaben entschieden, nicht
an der Bindungstabelle. Wenn sie wiederkehren, gilt dieselbe Lösung:

- **Der Quelltext schlägt die Ausgabe, wo er bewusst anders formuliert.**
  `reichste` (1,3) gegen „greatest", `Sturm` (1,19) gegen „wind", `packte`
  (1,19) gegen „struck" — jedes Mal ist das Deutsche glossiert worden.
- `hielt` in „So hielt es Hiob immer wieder" (1,5) = *did · hacía · agissait ·
  agiva*; die Bestandslesart *held/tenía* ergibt hier keinen Sinn, und einen
  Mehrwort-Eintrag `es halten` gibt es im Bestand nicht.
- `ältest` (1,13 · 1,18, ältester Bruder) = *oldest · mayor · aîné · maggiore*.
  Der eine Bestandsbeleg (1Mo 24,2) meint den dienstältesten Knecht.

## Offene Bestandsbefunde aus Kapitel 1

- **`lexicon.py` findet stammverwandte Formen bei Ablaut nicht.** `mied` →
  `meiden`, `geschützt` → `schützen` wurden als unbelegt gemeldet, obwohl das
  Lemma im Bestand steht; der VERWANDT-Abschnitt bot nur Buchstabennachbarn
  (`Geschenk`, `Geschichte`). **Drei von zwölf „unbelegten" Formen dieses
  Kapitels waren falsch etikettiert.** Immer `fixgloss.py show <lemma>` fragen,
  bevor du etwas Neues erfindest.
- `überfallen` hat zwei Lesarten, die sich nur im Englischen unterscheiden
  (*came upon* / *attacked*) — sieht nach Unschärfe aus, nicht nach zwei
  Bedeutungen.
- `Boden` in „warf sich zu Boden" ist im Bestand 11:2 uneinheitlich (fr *terre*
  gegen *sol*, it *terra* gegen *terreno*).
