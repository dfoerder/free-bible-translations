# Kapitelquellen der Wort-für-Wort-Annotation

Hier liegen die **Quelldateien**, aus denen die Annotationen des
Schwesterprojekts `../bible-reader` gebaut werden — nicht die Annotationen
selbst. Die ausgelieferten Dateien stehen dort unter
`bibles/<sprache>/<edition>/anno/<buchNr>_<edition>_multi.json`.

## Warum sie hier liegen und nicht dort

Die Annotationen entstehen kapitelweise durch Agentenläufe; `buildbook.py`
setzt daraus je Buch **eine** Datei zusammen und gleicht dabei die
CEFR-Level buchübergreifend ab. Wer die Kapitelquellen verliert, kann ein
Buch nie wieder neu bauen: keine Level-Angleichung, keine korpusweite
Glossen-Korrektur, die einen Neubau überlebt, keine Reparatur, falls sich
ein Fehler im Build-Werkzeug findet.

Genau das ist mit **Matthäus (40), Markus (41) und 2. Mose 30–40** passiert —
ihre Quellen lagen nur in einem temporären Agenten-Verzeichnis und waren weg.

**Der Fall ist behoben.** `../anno-tools/quellen_sync.py` rechnet die Quelle
aus der gebauten Anno-Datei zurück: die enthält jeden Eintrag, und verloren
geht dabei nur, was der Build ohnehin verwirft (Satzzeichen-Einträge) oder
überschreibt (CEFR-Level). Seither sind alle Bücher wieder baubar, und ein
Neubau reproduziert jedes von ihnen byte-identisch.

Damit es nicht wieder passiert: **jedes fertige Kapitel wird hier
mitcommittet**, im selben Zug wie die gebaute Datei drüben.

Sie liegen in **diesem** Repo und nicht in `bible-reader`, weil `bible-reader`
sein `bibles/`-Verzeichnis vollständig ins iOS-App-Bundle spiegelt
(`sync_www.sh`). Die Quellen würden dort als toter Ballast mitausgeliefert,
obwohl die App sie nie lädt. Hier stören sie niemanden, und inhaltlich
gehören sie zu den Texten: sie beschreiben, wie aus dem Bibeltext die
Annotation wurde.

## Aufbau

`deu/l1912mod/<buchNr>/ch<kapitel>.json`, Inhalt `{"<vers>": [<eintraege>]}`.
Das ist dasselbe Format, das die Agenten liefern und das `buildbook.py` liest.

Stand: alle Bücher, die eine Anno-Datei haben — 1, 2, 3 (in Arbeit) und
40–66.

## Neu bauen

Die Werkzeugkette liegt in **`../anno-tools/`** — im Repository, nicht mehr
im Scratchpad. `buildbook.py` liest die Kapitelquellen direkt von hier;
kopieren muss man nichts.

    cd ../anno-tools
    python3 buildbook.py 3        # ein Buch bauen
    python3 validate.py alle      # Struktur und Gegenrechnung
    python3 qa.py alle            # inhaltliche Heuristiken

Was die Werkzeuge tun, steht in `../bible-reader/projekt-annotation-deutsch.md`,
Abschnitt „Werkzeugkette".
