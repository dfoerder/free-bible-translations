# Jona (32): vier Ausgaben, vier Zaehlungen — und ein fehlender Vers

Vor der Arbeit gemessen, am Text nachgelesen.

```
                Kap 1   Kap 2   Kap 3   Kap 4   gesamt
    deutsch       16      11      10      11      48
    WEB           17      10      10      11      48
    RV1909mod     16      10      10      11      47   ← ein Vers FEHLT
    LSG           16      11      10      11      48   ← deckungsgleich
    RIV           17      10      10      11      48
```

## 1. WEB und RIV ziehen den Fisch-Vers ins erste Kapitel

Der deutsche Vers **2,1** („Der HERR aber schickte einen grossen Fisch,
der Jona verschlang…") steht in WEB und RIV als **1,17**. Danach laeuft
Kapitel 2 dort um **einen Vers versetzt**: deutsch 2,2 = dort 2,1, und so
fort bis deutsch 2,11 = dort 2,10.

**RIV markiert die Doppelzaehlung im Text selbst:** elf Verse beginnen mit
`(2:1)`, `(2:2)` und so fort. Kein Defekt, sondern ein Fliesstext-Artefakt
der italienischen Ausgabe — dasselbe wie in Hosea 11,12–12,14 und
Amos 3,14/3,15. Wer die RIV-Zeile Wort fuer Wort abzaehlt, hat zwei
Tokens Vorsprung.

## 2. LSG ist die einzige deckungsgleiche Ausgabe

16 / 11 / 10 / 11, Vers fuer Vers wie das l1912mod. Wo eine Ausgabe als
Zeuge fuer die Versgrenze gebraucht wird, ist LSG hier die verlaessliche.

## 3. RV1909mod zieht 2,10 und 2,11 ZUSAMMEN — der Vers fehlt nicht

RV hat 47 Verse gegen 48 deutsche, und **RV 2,10 traegt beide deutschen
Verse**:

> RV 2,10: „Yo, en cambio, te ofreceré sacrificio con voz de alabanza;
> cumpliré lo que prometí. La salvación viene de Jehová. **Entonces
> Jehová le ordenó al pez, y este vomitó a Jonás en tierra firme.**"

Der fettgesetzte Teil ist der deutsche Vers **2,11** („Da befahl der HERR
dem Fisch, und er spie Jona ans Land"). Zusammengezogen, nicht
ausgelassen — **es gibt sehr wohl eine spanische Vorlage.**

RV zaehlt ausserdem **Versatz +0** ueber das ganze Kapitel: RV 2,1 ist
der deutsche 2,1 (der Fischvers), nicht wie WEB und RIV ins erste Kapitel
gezogen.

### Wie der Fehler entstand — und was daraus folgt

Eine fruehere Fassung dieser Datei behauptete, RV fehle der Vers. Der
Grund: die Messung schnitt den RV-Vers bei 95 Zeichen ab und las den
Schluss nicht. **`ausgaben.py` hatte es gewusst** und von selbst gewarnt:

    es: angewandt −1 (Abstand 0.34), besser waere +0 (Abstand 0.10)

Widerlegt vom Agenten fuer Kapitel 2, der den Vers vollstaendig gelesen
hat.

**Nie ein Verszitat abschneiden, wenn daraus ein Befund abgeleitet wird.**
Eine Zusammenziehung sieht am Anfang genauso aus wie eine Auslassung —
der Unterschied steht am Ende.
