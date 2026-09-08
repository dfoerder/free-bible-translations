# Der italienische Zeuge der franzoesischen Ausgabe ist die falsche Edition

**Gefunden vom Agenten fuer 1. Korinther 16, 09.09.**

`common.ZEUGE` stellt fuer `it` die **unmodernisierte** `ita/riv1927`:

    ZEUGE = {'de': 'deu/l1912mod', 'en': 'eng/web', 'es': 'spa/rv1909mod',
             'it': 'ita/riv1927', 'fr': 'fra/lsg1910'}

Der Auftrag und die Doktrin nennen dagegen `bibles/ita/riv1927mod` als
massgeblich, und die Agenten schlagen dort nach. Damit zitiert jede
`ausgaben_*.md` eine andere italienische Fassung als die, gegen die
entschieden wird.

Was das konkret kostet, zeigt 1. Korinther 16,22: die
Vorbereitungsdatei liest `Maràn-atà`, der massgebliche Zeuge
`Maranatà`. Wer die Namensform aus der Vorbereitung nimmt, setzt die
falsche. Dazu kommt bei 16,5/16,6 ein Versversatz der alten Ausgabe.

**Fuer `fr` ist die unmodernisierte Fassung Absicht** — der Kommentar
in `common.py` sagt warum: der ganze deutsche Bestand hat gegen sie
gearbeitet. Fuer `it` steht keine solche Begruendung da; es sieht nach
einem Ueberbleibsel aus.

## Warum es nicht sofort geaendert wurde

Als der Befund kam, liefen drei Agenten. `common.py` ist das zentrale
Modul der ganzen Kette — genau der Fall, den die Regel „Werkzeuge nicht
anfassen, waehrend Agenten laufen" meint, und die stammt aus einem
Schaden von derselben Nacht.

## Wie es zu aendern waere

Nicht `ZEUGE` global umstellen — das traefe auch die deutsche Ausgabe,
deren Bestand womoeglich gegen `riv1927` gearbeitet hat. Der
vorhandene `zeugen`-Schluessel je Ausgabe ist der richtige Griff:

    'fra/lsg1910mod': {…, 'zeugen': {'it': 'ita/riv1927mod'}},

Vorher pruefen, wieviele Stellen des franzoesischen Bestands eine
italienische Glosse tragen, die nur aus der alten Fassung stammen
kann — und ob die deutsche Ausgabe wirklich an `riv1927` haengt.
