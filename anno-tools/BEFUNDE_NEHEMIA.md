# Bestandsbefunde aus Nehemia — gemeldet, nicht korrigiert

Was Agenten im **fertigen Bestand** gefunden haben, während sie Nehemia
annotierten. Nichts davon ist eigenmächtig korpusweit gezogen worden; jeder
Punkt braucht die Belegverse und eine Entscheidung.

## Aus Kapitel 1

- **`Susan` (Esra 4,9) trägt englisch *Shushan*, romanisch aber die modernen
  Formen *Susa · Suse · Susa*.** Das englische Feld ist die einzige archaische
  Form der Vierergruppe. Nehemia 1,1 hat `Susa` und schreibt die Lesart fort.
  Kandidat für eine Vereinheitlichung auf *Susa*.
- **`Ohr` im Plural, italienisch uneinheitlich:** 42× *orecchi*, 8× *orecchie*.
  Die Gebets-Parallelen 2Chr 6,40 und 7,15 haben *orecchie*; Nehemia 1,6 folgt
  denen. Der Bruch liegt zwischen Büchern, nicht innerhalb eines Buches.
- **`bekennen` spaltet nur im Englischen:** *profess* (5Mo 26,3) gegen
  *confess* (Jos 7,19), bei identischer romanischer Seite. Für 1,6 ist
  *confess* eindeutig; die Spaltung selbst sieht nach einer echten
  Inkonsistenz aus.
- **`Anordnung` hat genau einen Beleg** (1Chr 23,27, *decrees*), das nah
  verwandte `Ordnung` mehrere (*orders*). Beide sind nirgends im selben Vers
  geprüft. In 1,7 steht `Anordnungen` in einer Dreierreihe mit `Gebote` und
  `Rechte` — die Reihe ist dadurch empfindlich.

## Werkzeugbefund, behoben

`levelcheck.py`, `konvention.py` und `kreuz.py` hatten den Scratchpad-Pfad der
Esra-Sitzung fest eingebaut und liefen ohne ihn in einen `FileNotFoundError`.
Sie nehmen den Pfad jetzt aus **`ANNO_OUT`** und brechen mit einer klaren
Meldung ab, wenn er fehlt. Ein toter Pfad als Vorgabewert wäre beim nächsten
Buch wieder stillschweigend falsch gewesen.
