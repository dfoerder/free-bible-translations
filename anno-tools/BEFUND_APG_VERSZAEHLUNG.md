# Apostelgeschichte: was die Zeugen anders zaehlen

Gemessen mit `kapitelgrenzen.py 44`, bevor das erste Paket lief.
**Der franzoesische Text hat 1006 Verse in 28 Kapiteln.** Alles steht
auf Versatz +0; die folgenden vier Stellen sind trotzdem der Reihe
nach zu erwarten, damit kein Agent einem Phantom-Versatz nachjagt.

    en (web)   8,37   fehlt   — LUECKE, kein Versatz. Der Rest des
                               Kapitels steht auf gleicher Nummer.
    en (web)  15,34   fehlt   — dasselbe.
    en (web)  19,41   zuviel  — die Ausgabe hat 41 Verse gegen 40;
    it (riv)  19,41   zuviel    der franzoesische Vers 40 ist dort
                               geteilt.
    en (web)  24      laeuft ueber die Kapitelgrenze: 24,1-27 des
                      Franzoesischen entspricht 23,35 - 24,27 der
                      Ausgabe.

8,37 und 15,34 sind die bekannten Textvarianten — `lsg1910mod` fuehrt
sie, die WEB nicht. Das ist **kein** Fehler der Ausrichtung, und
`ausgaben.py` wird an diesen Kapiteln entsprechend danebengreifen.
Wer dort einen Zeugen braucht, nimmt den deutschen oder den
spanischen.

Roemer (Buch 45, 16 Kapitel, 433 Verse) steht durchgehend auf
Versatz +0; die englische Gesamtzahl weicht um drei ab, ohne dass ein
Kapitel eine Abweichung meldet.
