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

## Aus den Kapiteln 4 bis 6

- **`Tür` und `Tor` tragen im ganzen Bestand dieselbe romanische Glosse**
  (*puerta · porte · porta*). Eine korpusweite Kollision, die nur auffällt, wo
  beide zusammenstehen — in Nehemia 3,6 und 6,1. In 6,1 verse-lokal aufgelöst
  (`Tore` → *portones · portails · portoni*); in 3,6 steht `Tor` als Glied des
  Namens `Das Alte Tor` und bleibt. **Kandidat für eine Bestandsentscheidung.**
- **`Gottesfurcht` ist testamentarisch gespalten:** 2Petr 1,6 und 1,7 tragen
  *godliness · piedad · piété · pietà*, 1Mo 20,11 dagegen *fear of God · temor
  de Dios · crainte de Dieu · timore di Dio*. 2:1 zugunsten der NT-Lesart — eine
  klassische Lexikonfalle. Neh 5,9 folgt 1Mo 20,11.
- **`üble Nachrede` und `verleumden` tragen beide englisch *slander***. Der
  einzige Bestandsbeleg der Wendung ist 2Kor 12,20; die beiden sind nirgends
  sonst im selben Vers geprüft. Neh 6,13 ist die erste Stelle, an der der
  Konflikt sichtbar wird — dort `verleumden` → *defame*.
- **`zugute` hat drei Belege, alle aus Paulusbriefen**, zwei mit identischer
  romanischer Seite bei verschiedener englischer (*to the benefit* / *to my
  benefit*).
- **`erlassen` ist romanisch stabil, englisch nicht:** *cancel* (5Mo 15,2)
  gegen *forgiven* (Joh 20,23) bei identischem es *perdonado*.
- **`jüdisch` ist nur neutestamentlich belegt** (12 Belege, alle mit it
  *giudaico*). Für „jüdische Brüder" (5,1 · 5,8) steht dort it *giudei* —
  „fratelli giudaici" wäre kein Italienisch.
- **`Bogen` ist nur im Singular belegt** (20×); 4,7 und 4,10 brauchen den
  Plural, neu gebildet.
- **`Aufstand` hat nur NT-Belege** (*riot* 3×, *revolt* 2×). Neh 6,6 ist der
  erste AT-Beleg und nimmt *revolt*.

## Werkzeugbefunde, behoben

`levelcheck.py`, `konvention.py` und `kreuz.py` hatten den Scratchpad-Pfad der
Esra-Sitzung fest eingebaut und liefen ohne ihn in einen `FileNotFoundError`.
Sie nehmen den Pfad jetzt aus **`ANNO_OUT`** und brechen mit einer klaren
Meldung ab, wenn er fehlt. Ein toter Pfad als Vorgabewert wäre beim nächsten
Buch wieder stillschweigend falsch gewesen.

`konvention.py` hat in Neh 6,10 eine Lücke gemeldet, die keine war: der Vers
hat zwei `um`, das erste ohne eigenes `zu` (`um dich umzubringen`). Die
Vorwärtssuche paarte das erste `um` (pos 37) mit dem `zu` des **zweiten**
Teilsatzes (pos 47), über einen Gedankenstrich hinweg. Die Suche bricht jetzt
ab, sobald ein zweites `um` oder ein alleinstehendes Satzzeichen dazwischen
steht. Gegenprobe an entkernten Kontrolldateien: alle sieben echten Lücken
werden weiterhin gefunden, 6,10 jetzt an der richtigen Stelle 45–47.

`hints.py` meldet Präfixverben systematisch als „unbelegt", obwohl das Lemma
reichlich belegt ist: bei `herunterkommen` und `hinabziehe` (Neh 6,3) führte
der VERWANDT-Abschnitt auf `herum` und `hinab` statt aufs Lemma. Aufgedeckt
hat es nur `levelcheck.py`. Der formbasierte Fallback trifft bei trennbaren
und Präfixverben oft daneben — das gehört in jeden Prompt, der `hints.py`
benutzt.
