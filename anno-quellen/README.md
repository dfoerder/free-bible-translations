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

Genau das ist mit **Matthäus (40) und Markus (41)** passiert — ihre Quellen
lagen nur in einem temporären Agenten-Verzeichnis und sind weg. Die beiden
Bücher sind eingefroren; Korrekturen müssen dort direkt in der gebauten
Datei erfolgen und gehen beim nächsten Build verloren, falls je einer
stattfindet.

Sie liegen in **diesem** Repo und nicht in `bible-reader`, weil `bible-reader`
sein `bibles/`-Verzeichnis vollständig ins iOS-App-Bundle spiegelt
(`sync_www.sh`). Die Quellen würden dort als toter Ballast mitausgeliefert,
obwohl die App sie nie lädt. Hier stören sie niemanden, und inhaltlich
gehören sie zu den Texten: sie beschreiben, wie aus dem Bibeltext die
Annotation wurde.

## Aufbau

`deu/l1912mod/<buchNr>/ch<kapitel>.json`, Inhalt `{"<vers>": [<eintraege>]}`.
Das ist dasselbe Format, das die Agenten liefern und das `buildbook.py` liest.

Stand: Bücher 42–66 vollständig (Lukas bis Offenbarung), rund 20 MB.
40 und 41 fehlen, siehe oben.

## Neu bauen

Die Werkzeugkette (`buildbook.py`, `levels.py`, `qa.py`, `selfcheck.py`,
`lexicon.py`, `hints.py`, `konsistenz.py`, `fixgloss.py`, `remap.py`) liegt
nicht im Repository, sondern wird je Sitzung im Scratchpad neu angelegt.
Ihr Aufbau ist in `../bible-reader/projekt-annotation-deutsch.md`
beschrieben, Abschnitt „Werkzeugkette". `buildbook.py` erwartet die
Kapitelquellen unter `out/<buchNr>/ch<N>.json` — dieses Verzeichnis dorthin
kopieren oder verlinken.
