# RIV1927: fehlende Anfangsbuchstaben — ein Befund, keine Reparatur

Gefunden beim Annotieren von **Jeremia 1**: der Agent meldete, RIV schreibe in
1,1 „nel paese di **eniamino**" und in 1,3 „re di **iuda**". Beides sind Woerter
ohne ihren ersten Buchstaben.

## Der Umfang

Gemessen ueber alle fuenf Ausgaben des Bestands. Gesucht wurde jede
kleingeschriebene Form, die hoechstens dreimal vorkommt und durch **einen
vorangestellten Buchstaben** zu einer mindestens zwanzigmal haeufigeren Form
des Korpus wird:

| Ausgabe | Wortformen | verdaechtige Vorkommen |
|---|---|---|
| WEB (en) | 13 332 | 32 |
| RV1909mod (es) | 26 727 | 22 |
| LSG1910 (fr) | 21 827 | 25 |
| l1912mod (de) | 25 042 | 30 |
| **RIV1927 (it)** | **31 834** | **440** |

Die rund dreissig Treffer der anderen vier Ausgaben sind Rauschen (echte
seltene Woerter, die zufaellig einem haeufigen Wort minus Anlaut gleichen).
**Der italienische Wert liegt vierzehnmal darueber** und ist damit kein
Rauschen, sondern ein Defekt der Datei.

## Die Belege

190 Stellen liegen in einer Stellung, in der ein Name zu erwarten ist (nach
`di`, `a`, `in`, `da`, `re di`, `figliuolo di` …), und **jede davon hat den
vollen Namen im selben Buch korrekt geschrieben**:

    Jer 1,1    nel paese di eniamino          → Beniamino
    Jer 1,3    re di iuda                     → Giuda
    2Sam 2,4   fu riferito a avide            → Davide
    2Re 25,28  con lui a abilonia             → Babilonia
    Neh 8,1    stabiliti da sraele            → Israele
    Ger 36,4   a dettatura di eremia          → Geremia

Betroffen sind 68 Namen (Giuda 25×, Davide 15×, Babilonia 12×, Cristo 10×,
Giacobbe und Faraone je 8× …). Der Defekt trifft aber **nicht nur Namen**:
`arte` → `parte`, `uoco` → `fuoco`, `ietra` → `pietra`, `ccidente` →
`occidente`, `utti` → `tutti`, `olui` → `colui`. Insgesamt 322 verschiedene
Formen.

## Warum hier nichts repariert wird

Die Reparatur waere mechanisch moeglich — die Regel „setze den Buchstaben
davor, der die Form zu einem im selben Buch belegten Wort macht" trifft in den
190 Namensfaellen eindeutig. Aber:

* Es sind **ueber vierhundert Aenderungen am Bibeltext selbst**, nicht an
  Annotationsdaten. Der Text ist das, was der Leser in der App sieht.
* Eine falsch geratene Ergaenzung ist im Ergebnis nicht mehr von einer
  richtigen zu unterscheiden — anders als bei einer Glosse, die jederzeit
  gegen den Quelltext nachpruefbar bleibt.
* Die verlaesslichste Korrektur kaeme aus der **Quelle** der RIV-Datei, nicht
  aus einer Heuristik ueber die Datei selbst.

Die Liste der 190 Namensfaelle liegt in `scratchpad/riv_anlaut.json`.

## Was das fuer die Annotation heisst

**Ein Name ohne Anfangsbuchstaben in RIV ist keine Schreibvariante der
Ausgabe.** Wo `NAMENSSCHREIBUNG_*.md` und `AUFTRAG_AT.md` sagen „erst die
Ausgabe aufschlagen", gilt fuer RIV zusaetzlich: sieht die Schreibung um genau
einen fehlenden Anlaut falsch aus, **dieselbe Stelle im selben Buch an einer
zweiten Belegstelle nachschlagen**.

Das ist der zweite Defekt dieser Datei nach dem Rohbyte 0x85, das als
Auslassungszeichen fehldekodiert war (46 Stellen in 13 Buechern).

## Nachtrag: derselbe Defekt am Wortende — aber nur in einer Form

Gefunden beim Annotieren von **Daniel 10**: RIV schreibt in 10,3
`entraron` statt `entrarono`. Der Agent hielt es fuer eine spanische
Form im italienischen Text.

Nachgemessen ueber alle 66 Buecher: es sind **20 Vorkommen in elf
Formen**, alle nach demselben Muster — die 3. Person Plural des Perfekts
ohne ihr Schluss-`o`:

    4×  levaron       → levarono      (32× korrekt)   4Mo 16,2 · Ri 9,34 · Mt 15,37
    3×  entraron      → entrarono     (36×)           Jos 8,19 · Dan 10,3 · Mt 25,10
    3×  alzaron       → alzarono      (13×)           1Sam 30,4 · Joh 17,13 · Apg 4,24
    2×  cavaron       → cavarono                      Ri 16,21 · 2Kön 25,7
    2×  presentaron   → presentarono  (34×)           Mt 14,35 · Apg 1,10
    je 1×: odiaron · mostraron · montaron · invocaron · prepararon · prestaron

Jede dieser Formen hat im selben Korpus die richtige Fassung, meist
dutzendfach. Ob der Setzer ein `o` verloren oder aus einer spanischen
Vorlage abgeschrieben hat, ist von aussen nicht zu entscheiden — die
Zeichenfolgen sind dieselben.

**Ein allgemeiner Defekt am Wortende ist es nicht.** Dieselbe Heuristik
wie oben, nur umgedreht (seltene Form, die durch **einen angehaengten**
Buchstaben zu einer mindestens zwanzigmal haeufigeren Form wird):

| Ausgabe | Vorkommen | Formen |
|---|---|---|
| WEB (en) | 9 | 7 |
| RV1909mod (es) | 22 | 13 |
| LSG1910 (fr) | 39 | 22 |
| l1912mod (de) | 78 | 53 |
| **RIV1927 (it)** | **97** | **72** |

Der italienische Wert liegt nur knapp ueber dem deutschen, nicht
vierzehnfach darueber wie beim Anlaut. Die Treffer sind zum
allergroessten Teil echte Woerter (`territori` gegen `territorio`,
`simil` gegen `simile`). **Der Defekt sitzt am Wortanfang; am Wortende
gibt es nur diese eine, eng umrissene Gruppe.**
