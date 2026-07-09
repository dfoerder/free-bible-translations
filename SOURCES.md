# Quellen & Lizenzlage

Diese Sammlung stützt sich auf **gemeinfreie** Bibelübersetzungen. Die
modernisierten Fassungen sind maschinell erzeugte Bearbeitungen dieser
Grundtexte (siehe [README.md](README.md) → „Wie modernisiert wird").

> **Wichtiger Hinweis:** Die folgenden Einschätzungen sind nach bestem Wissen
> zusammengetragen, aber **keine Rechtsberatung**. Vor einer Veröffentlichung
> die Rechtelage jeder Übersetzung selbst prüfen — besonders die mit dem
> Vermerk „zu prüfen".

## Deutsch (`deu`)

| ID | Übersetzung | Grundtext gemeinfrei? | Begründung |
|----|-------------|-----------------------|------------|
| `l1912` / `l1912mod` | Luther 1912 (Grundtext / modernisiert) | **Ja** | Die Lutherbibel in der Revision von 1912 wird durchgängig als gemeinfrei behandelt; der Text ist weit über 100 Jahre alt. |
| `sch1951` / `sch1951mod` | Schlachter 1951 | **Zu prüfen** | Franz Eugen Schlachter (†1911) schuf die Urfassung (1905, gemeinfrei). Die **Revision 1951** wurde von späteren Bearbeitern (Genfer Bibelgesellschaft) erstellt; deren Schutzfrist (70 Jahre nach Tod des jeweiligen Bearbeiters) ist möglicherweise **noch nicht abgelaufen**. Status daher unklar. |

### Herkunft `deu/l1912`

Der Grundtext wurde aus dem Repository **Beblia/Holy-Bible-XML-Format**
(`GermanLuther1912Bible.xml`, dort als „Public Domain" ausgewiesen) importiert.
Zwei leere Platzhalter-Verse der englischen Zählung (5. Mose 29:29, Maleachi 4:1)
wurden entfernt; dadurch ist der Text **versgenau deckungsgleich** mit `l1912mod`
(66 Bücher, 31171 Verse, deutsche Maleachi-Zählung mit 3 Kapiteln).

## Weitere Sprachen (im App-Repo vorbereitet, noch nicht in dieser Sammlung)

| ID | Übersetzung | Grundtext gemeinfrei? | Begründung |
|----|-------------|-----------------------|------------|
| `eng/web` | World English Bible | **Ja** | Vom Herausgeber (Rainbow Missions) ausdrücklich in die Public Domain entlassen. Bereits modernes Englisch — keine Modernisierung nötig. |
| `fra/lsg1910` | Louis Segond 1910 | **Ja** | Louis Segond †1885; Text weit außerhalb jeder Schutzfrist. |
| `ita/riv1927` | Riveduta (Luzzi) 1927 | **Ja** | Giovanni Luzzi †1948 → in Italien seit 2019 gemeinfrei (70 Jahre p. m. a.). |
| `spa/rv1909` | Reina-Valera 1909 | **Ja** | Grundtext von Casiodoro de Reina / Cipriano de Valera (16. Jh.), Revision 1909 gemeinfrei. |

## Modernisierte Fassungen

Die `…mod`-Texte sind **Bearbeitungen** der obigen gemeinfreien Grundtexte,
erzeugt mit einem KI-Modell (Anthropic Claude). Sie ändern nichts am
gemeinfreien Charakter des Grundtextes; die Bearbeitung selbst kann unter die
gewählte Projektlizenz gestellt werden (siehe [README.md](README.md)).

## Herkunft der Rohdaten

Die deutschen JSON-Dateien stammen aus dem Schwesterprojekt
`../bible-reader` (Sprachlern-PWA), wo dieselben gemeinfreien Texte als
Datengrundlage dienen.
