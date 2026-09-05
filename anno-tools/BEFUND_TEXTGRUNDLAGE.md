# Woher kommt der Text, den wir glossieren?

Der Agent fuer **Micha 6** hat gemeldet, dass `l1912mod` in 6,9 und 6,16
nicht der Luther 1912 folgt, sondern der **Schlachter 1951**. Nachgeprueft
— er hat recht, und es ist kein Einzelfall.

## Der Anlass, Vers fuer Vers

**Micha 6,16**

```
l1912      „…und ihr sollt MEINES VOLKES Schmach tragen."
sch1951    „…und ihr die Schmach DER VOELKER tragen sollt."
l1912mod   „…ihr muesst die Schmach DER VOELKER tragen."      ← sch1951
```

**Micha 6,9**

```
l1912      „Es wird des HERRN Stimme ueber die Stadt rufen; aber wer
            deinen Namen fuerchtet, dem wird's gelingen. Hoeret, ihr
            Staemme, was gepredigt wird!"
sch1951    „Die Stimme des HERRN ruft der Stadt zu, und weise ist, wer
            deinen Namen fuerchtet. Hoeret die Strafe und wer sie
            festgesetzt hat!"
l1912mod   „Die Stimme des HERRN ruft der Stadt zu — wer weise ist,
            fuerchtet deinen Namen: Hoert auf die Rute und auf den, der
            sie bestimmt hat!"                                 ← sch1951
```

**Das erklaert einen Befund, der in jedem Buch auftaucht:** „alle vier
Ausgaben lesen X, der deutsche Text liest Y". In Micha 6,16 lesen WEB, RV,
LSG und RIV einstimmig „of my people / de mi pueblo / de mon peuple / del
mio popolo" — sie folgen derselben Vorlage wie Luther. Der deutsche Text
folgt Schlachter.

## Die Messung ueber das ganze Alte Testament

Fuer jeden Vers der Buecher 1–39 die Wortmengen (ab 4 Zeichen) von
`l1912mod` gegen `l1912` und gegen `sch1951` gehalten, Jaccard-Abstand,
Schwelle 0,15:

```
    23 212 Verse geprueft

     3 960  naeher an l1912
     3 514  naeher an sch1951
    15 738  unentschieden (die Modernisierung entfernt beide gleich weit)
```

**Das Verhaeltnis ist nahezu ausgeglichen.** `l1912mod` ist kein
modernisierter Luther, sondern ein **eklektischer Text**, der beide
Vorlagen benutzt. (Der Name ist irrefuehrend; im Repo liegt unter
`deu/sch1951mod` eine zweite modernisierte Ausgabe.)

Die Messung ist grob — sie misst Wortmengen, nicht Abhaengigkeit, und die
Modernisierung selbst entfernt den Text von beiden Vorlagen. Aber 3514
Verse sind kein Rauschen.

## Was daraus fuer die Arbeit folgt

**Nichts an der Regel.** Der deutsche Text ist die Grundlage, die vier
Ausgaben sind Zeugen — das gilt unveraendert, und die Agenten sind ihm
bisher an jeder Divergenz gefolgt.

**Aber die Erwartung aendert sich.** Wo alle vier Ausgaben geschlossen
anders lesen als der deutsche Text, ist das nicht notwendig ein
Uebersetzungsfehler oder eine Eigenheit der Modernisierung — es kann
schlicht die andere Vorlage sein. Zwei Beispiele aus den letzten Buechern,
die sich damit erklaeren:

- **Micha 6,16** „der Voelker" gegen viermal „meines Volkes"
- **Amos 6,2** dreht die Vergleichsrichtung gegen alle vier Ausgaben

Wer in einem Prompt schreibt „hier steht der deutsche Text allein", sollte
das im Zweifel gegen `deu/l1912` **und** `deu/sch1951` pruefen, bevor er
es als Besonderheit ausweist.
