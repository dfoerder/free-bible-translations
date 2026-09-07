# Markus: zwei geteilte Verse — und was `kapitelgrenzen.py` daraus macht

Gemessen am 2026-09-07, vor Paket 1 der franzoesischen Annotation.

## Der Befund

Der franzoesische Text hat in Markus **680 Verse**, alle vier Zeugen
(de/en/es/it) haben **678**. Die Differenz sitzt an zwei Stellen, und
an beiden **teilt das Franzoesische einen Vers, den die Zeugen
zusammenlassen**:

    fr 9,50   Le sel est une bonne chose, mais s'il perd sa saveur …
    fr 9,51   Ayez du sel en vous-memes et vivez en paix …
    de 9,50   Salz ist gut. Wenn das Salz aber seine Kraft verliert, …
              Habt Salz in euch und haltet Frieden untereinander!

    fr 10,52  Jesus lui dit: Va, ta foi t'a sauve.
    fr 10,53  Aussitot il recouvra la vue et suivit Jesus sur le chemin.
    de 10,52  Jesus sagte zu ihm: Geh, dein Glaube hat dir geholfen.
              Sofort konnte er sehen und folgte Jesus auf dem Weg.

Beide Kapitel **enden** dort. Die Kapitelgrenze ist also nicht
verschoben: fr 9,1 = de 9,1, fr 10,1 = de 10,1, fr 11,1 = de 11,1.
Nur der letzte franzoesische Vers eines der beiden Kapitel hat keinen
eigenen Zeugenvers, sondern die zweite Haelfte des vorletzten.

## Was das Werkzeug daraus macht

`kapitelgrenzen.py 41` meldet fuer jeden Zeugen

    9,1-51  ->  9,1 - 10,1   << … haben dort KEINE Vorlage

und schickt damit **den Zeugenvers 10,1 neben fr 9,51**. Das ist eine
andere Perikope (der Aufbruch nach Judaea gegen das Salzwort). Ebenso
11,1 neben fr 10,53.

Das Werkzeug kennt nur einen Fall — den durchgehenden Kapitelversatz,
wie ihn die Psalmen und Joel haben. Ein **geteilter Vers am
Kapitelende** sieht in seiner Zaehlung genauso aus: ein Vers zu viel,
der Rest passt. Unterscheiden liesse sich beides nur am Text, und
`abstand()` misst erst gar nicht ueber die Kapitelgrenze hinweg.

## Folge fuer die Arbeit

Fuer **fr 9,51 und fr 10,53** traegt die VERS-Schicht von
`rueckwaerts.py` nichts (der Zeugenvers dieser Nummer existiert nicht)
und `ausgaben.py` zeigt nichts. Die Glossen dieser beiden Verse kommen
aus der **zweiten Haelfte** des Zeugenverses mit der Nummer davor.
Das steht als `--hinweis` in den Prompts von Kapitel 9 und 10.

Fuer fr 9,50 und fr 10,52 gilt umgekehrt: der Zeugenvers derselben
Nummer enthaelt **mehr** als der franzoesische — nur die erste Haelfte
gehoert dazu.

## Nachtrag: der zweite, verdeckte Versatz in 9,43-9,48

Gefunden vom Agenten fuer Marc 9, am Quelltext nachgeprueft.

Hier geht die **Zaehlung auf** — sechs Verse gegen sechs — und der
Inhalt ist trotzdem verschoben:

    fr 9,43   „Si ta main est … entrer manchot dans la vie"
    fr 9,44   „plutôt que d’avoir les deux mains … dans le feu"
    de 9,43   beides zusammen
    de 9,44   „wo ihr Wurm nicht stirbt und ihr Feuer nicht erlischt"

    fr 9,45 / 9,46   dieselbe Teilung noch einmal
    fr 9,48          der Refrain, EINMAL, am Ende
    de 9,44 · 9,46 · 9,48   der Refrain, dreimal

Weil die Zahlen stimmen, kann `kapitelgrenzen.py` das nicht sehen —
es zaehlt. `ausgaben.py` sieht es auch nicht, es misst Verslaengen.
Gesehen hat es allein die **Versatzprobe von `rueckwaerts.py`**, die den
Nachbarvers jedes Zeugen gegen den eigenen haelt: sie hat fuer 9,44 und
9,46 unabhaengig „vertauschte Perikopen — VERS-Zeilen NICHT uebernehmen"
gemeldet. Das ist die einzige Probe der Kette, die den Inhalt vergleicht
statt die Zahlen.

## Was `ausgaben.py` daraus gemacht hat

Der Versatz kommt aus dem letzten Vers: fr 9,51 gegen Zeugenvers 9,50
ergibt -1, und damit stand in `ausgaben_41_9.md` jede Zeugenzeile eine
Nummer daneben. Die Datei warnt zwar laut vor sich selbst („Versatz +0
liegt BESSER"), wendet aber den schlechteren an.

Der automatische Tausch waere gefaehrlich: in Psalm 15 bewertet der
FALSCHE Versatz 0.09 gegen 0.31 des richtigen, weil die Verslaengen dort
zufaellig besser zueinander passen — ein Tausch nach dieser Zahl haette
die italienische Spalte um eins verschoben. Marc 9 und 10 stehen deshalb
als **gemessene Ausnahme** in `AUSNAHMEN`, mit dem Grund daneben.
