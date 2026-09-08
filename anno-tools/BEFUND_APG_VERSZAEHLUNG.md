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
    en (web)  24,7    fehlt   — KORRIGIERT, siehe unten.

8,37 und 15,34 sind die bekannten Textvarianten — `lsg1910mod` fuehrt
sie, die WEB nicht. Das ist **kein** Fehler der Ausrichtung, und
`ausgaben.py` wird an diesen Kapiteln entsprechend danebengreifen.
Wer dort einen Zeugen braucht, nimmt den deutschen oder den
spanischen.

Roemer (Buch 45, 16 Kapitel, 433 Verse) steht durchgehend auf
Versatz +0; die englische Gesamtzahl weicht um drei ab, ohne dass ein
Kapitel eine Abweichung meldet.


## Nachtrag: was `ausgaben.py` an den vier Sonderfaellen tut

Zwei Agenten haben das unabhaengig gemessen, und die beiden Faelle
verhalten sich **verschieden**:

- **Fehlender Vers (8,37 · 15,34):** der Zeuge hat den Vers nicht.
  `ausgaben.py` meldet sauber „kein Gegenstueck in dieser Ausgabe" und
  richtet die folgenden Verse wieder korrekt aus. Kein Versatz, nichts
  zu tun — gemessen vom Agenten fuer Actes 8 und bestaetigt fuer 15,34.
- **Geteilter Vers (19,40 — und NUR dort):** der Zeuge
  hat einen Vers MEHR, weil er einen franzoesischen Vers in zwei teilt.
  Der Ueberhang haengt **hinten**, aber der Versatz kommt aus dem
  letzten Vers und schiebt jede Zeile nach **vorn**. Englisch und
  Italienisch stehen dann im ganzen Kapitel eine Nummer daneben.
  Gemessen vom Agenten fuer Actes 19, der die vier Ausgaben direkt
  gegeneinandergelegt hat: **Versatz ist +0, nicht +1.**

`ausgaben.py` erkennt den zweiten Fall — es rechnet die Nachbarversaetze
mit und warnt. Die Warnung stand aber nur im Kopf der Datei, vierzig
Verse ueber der Arbeitsstelle. Seit dieser Meldung traegt die betroffene
Zeile in **jedem** Versblock ein `!`, und die Nachbarzeilen stehen mit
`?` daneben; eine davon ist die richtige. Der Versatz wird weiterhin
nicht stillschweigend ausgetauscht — das hat in Ps 9, 15 und 19 in die
andere Richtung danebengelegen.


## Korrektur: Kapitel 24 ist KEIN Kapitelgrenzen-Fall

Die erste Fassung dieses Befundes behauptete, das englische Kapitel 24
laufe von 23,35 bis 24,27. **Das war falsch, und der Fehler war meiner.**
Der Agent fuer Actes 24 hat die vier Ausgaben direkt aus
`bible-reader/bibles/<sprache>/<edition>/44_<edition>.json` gemessen:

- Alle vier Zeugen haben **Kapitel 23 mit 35 Versen**.
- WEB 24,1 ist derselbe Vers wie fr 24,1, WEB 24,27 derselbe wie fr 24,27.
- WEB hat 26 statt 27 Verse, weil ihm **genau Vers 7 fehlt** — die
  Lysias-Variante, also derselbe Fall wie 8,37 und 15,34.

Kapitel 24 gehoert damit in die **erste** Gruppe (fehlender Vers, harmlos,
`ausgaben.py` meldet die Luecke und richtet wieder aus), nicht in die
zweite. Die `!!`-Warnung im Kopf und die `?`-Nachbarzeilen sind dort
reines Rauschen, ausgeloest allein von der fehlenden Zeile.

**Der einzige echte Verschiebungsfall im ganzen Buch ist Kapitel 19.**

Der Fehler stand acht Pakete lang in diesem Befund und ist in ebenso
viele Auftraege gewandert. Er ist nur aufgefallen, weil ein Agent die
Rohdateien selbst aufgeschlagen hat, statt der Angabe zu glauben.
