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
