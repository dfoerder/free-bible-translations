# Wo die Ausgaben anders zaehlen als `l1912mod`

`kapitelgrenzen.py` hat seit seiner Entstehung **fuer kein einziges Buch
etwas gemeldet** — es suchte den Quelltext mit einem relativen Pfad, und
jedes Werkzeug wird laut `PROMPT_BAUSTEIN.md` aus `anno-tools/` heraus
aufgerufen. Von dort aus gibt es kein `deu/l1912mod`. Das Skript meldete
brav „Buch N: kein deutscher Quelltext" und niemand las es als Fehler.

Aufgefallen an **Sacharja**, dem ersten Buch seit Daniel mit einer echten
Verschiebung. Der Pfad wird jetzt vom Ort der Datei aus gebildet.

## Was der erste vollstaendige Lauf ergibt

**23 der 66 Buecher** tragen mindestens eine Abweichung:
1, 4, 5, 9, 10, 11, 12, 13, 14, 16, 18, 19, 22, 26, 27, 28, 29, 32, 34, 38, 41, 44, 47.

Das sind die bekannten Zaehlungsunterschiede zwischen hebraeischer und
christlicher Tradition — 1. Mose 32 (der Vers 31,55 der Ausgaben ist
deutsch 32,1), 5. Mose 13 und 23, die Psalmen mit gezaehlter
Ueberschrift, Hiob 39-41, Sacharja 1/2, Maleachi 3/4.

## Was das fuer die Glossen bedeutet: nichts

Annotiert wird der **deutsche** Text. Die vier Ausgaben sind Zeugen, kein
Massstab. Eine Verschiebung fuehrt nur dazu, dass ein Agent den falschen
Vers als Zeugen liest — und genau davor warnt `ausgaben.py` seit Jona von
selbst („Versatz +0 liegt BESSER"). Die Regel „die Warnung lesen, nicht
die Zahl" hat die Luecke die ganze Zeit aufgefangen.

**Keine Korrektur an 281 Stellen.** Der Befund ist ein Werkzeugbefund.

## Die drei Faelle, die noch anstehen

```
Haggai (37)     keine Abweichung
Sacharja (38)   deutsch 2,1-17  ->  Ausgaben 1,18 - 2,13
                deutsch 1,1-17  ->  Ausgaben 1,1-17, aber die Ausgabe
                                    hat dort 21 Verse: 1,18-21 gehoeren
                                    zum deutschen Kapitel 2
Maleachi (39)   deutsch 3,1-24  ->  Ausgaben 3,1 - 4,6; die letzten
                                    sechs deutschen Verse stehen dort
                                    als eigenes Kapitel 4
```

Beide gehoeren in die Kapitelprompts. Wer Sacharja 2 annotiert, findet
seine ersten vier Verse in **Kapitel 1** der Ausgaben.
