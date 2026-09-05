"""Steht im Quelltext ueberhaupt, was der Prompt behauptet?

    promptcheck.py <buchNr> <kapitel …> --datei <prompt.md>
    promptcheck.py <buchNr> <kapitel …> --woerter <wort> <wort> …

## Der Anlass

Der haeufigste echte Befund jedes Pakets ist seit Beginn derselbe, und er
kommt immer vom Agenten, nie vom Koordinator:

    Paket 14   46 Prompt-Hinweise widerlegt
    Paket 15   12
    Paket 16   28
    Paket 17   29

Der Loewenanteil ist jedes Mal dieselbe Sorte Fehler — **im Prompt stehen
Woerter, die im Kapitel gar nicht vorkommen.** In Paket 17 war sogar die
gemeinsame „Formelstelle des Pakets" erfunden: `verkuenden` ↔ `ansagen` sollte
durch alle drei Kapitel laufen, und `ansagen` steht in **keinem** von ihnen.
Drei Agenten haben unabhaengig voneinander gemeldet, dass es den Fall nicht
gibt.

Das ist maschinell zu pruefen, bevor der Prompt abgeschickt wird. Genau das
macht dieses Skript: es nimmt die in Backticks gesetzten deutschen Woerter aus
dem Prompt und haelt sie gegen die Tokens der genannten Kapitel.

## Warum ein Stammvergleich und kein exakter

Der Prompt nennt das Lemma (`giessen`, `Goetze`, `wackeln`), der Quelltext
traegt die Flexion (`giesst`, `Goetzen`, `wackelt`). Verglichen wird deshalb
ueber einen gekuerzten Stamm, und der muss mindestens fuenf Zeichen behalten —
mit vier ging `ansagen` ueber den Stamm `an` als "stammverwandt" durch,
obwohl das Wort in keinem der drei Kapitel steht.

Das **Partizip-`ge-`** wird abgeschnitten, wenn genug uebrig bleibt: sonst
findet `troesten` sein eigenes `getroestet` nicht — in Paket 19 haette das
Skript deshalb beinahe ein Wort als fehlend gemeldet, das viermal dasteht.

Bei **trennbaren Verben steht das `ge-` in der Mitte** (`umgekehrt` zu
`umkehren`, `angefangen` zu `anfangen`). Auch das wird abgeschnitten, nach
einer Liste der gaengigen Praefixe. Der Anlass: bei der Vorbereitung von
Amos, Paket 2 meldete das Skript `umkehren` als fehlend — waehrend der
laengste Refrain des Buches („Doch ihr seid nicht zu mir umgekehrt") ihn
fuenfmal traegt.

**Ein Treffer ist ein Verdacht, kein Fehler.** Umlautwechsel (`Baum`/`Baeume`),
starke Verben (`giessen`/`goss`) und Suppletion findet der Stammvergleich
nicht — und **ein Wort als zweites Glied eines Kompositums** auch nicht
(`Bund` steht in 54,10 als `Friedensbund`), weil der Praefixvergleich nur
vorne vergleicht. Umgekehrt meldet er auch nichts, wo ein Wort zwar vorkommt, aber in
anderer Bedeutung — das bleibt die Sache des Agenten.

Was er zuverlaessig findet, ist die Klasse, um die es geht: ein Wort, das im
Kapitel **ueberhaupt nicht vorkommt**.
"""
import re
import sys
import unicodedata

import common as C

# Woerter, die in einem Prompt in Backticks stehen, ohne deutscher Kapiteltext
# zu sein: Dateinamen, Werkzeuge, Feldnamen, Sprachkuerzel.
KEIN_TEXT = re.compile(
    r'\.(py|md|json|txt)$|^[a-z_]+\.py|^(pos|form|lemma|level|parts|en|es|fr|it)$'
    r'|^(ANNO_OUT|SPEC|A1|A2|B1|B2|C1|C2)$|/|^--')

ENDUNGEN = ('ungen', 'chen', 'lein', 'ern', 'end', 'est', 'ete', 'ten', 'ung',
            'en', 'er', 'es', 'em', 'et', 'st', 'te', 'e', 'n', 's', 't', 'r')

# Kuerzer als das raet der Stammvergleich nur noch. Gilt fuer die Endungsprobe:
# mit vier Zeichen war `ansagen` ueber den Stamm `an` (aus `ans`) als
# "stammverwandt" durchgegangen.
MIN = 5

# Der Praefixvergleich darf kuerzer sein, muss dafuer aber eng sein: beide
# Staemme mindestens KURZ Zeichen, und der laengere hoechstens ABSTAND Zeichen
# laenger. Ohne das meldete das Skript `Bote` als fehlend, obwohl 52,7 `Boten`
# schreibt — ein Fehlalarm der schaedlichen Sorte, weil er ein Wort abstreitet,
# das dasteht. Mit `an` gegen `ansag` (Abstand 3, aber Laenge 2) greift es nicht.
KURZ = 3
ABSTAND = 3


TRENNBAR = ('zusammen', 'entgegen', 'zurueck', 'hinaus', 'hinein', 'heraus',
            'herein', 'nieder', 'wieder', 'ueber', 'unter', 'durch', 'empor',
            'nach', 'fort', 'weit', 'auf', 'aus', 'ein', 'mit', 'vor', 'ab',
            'an', 'bei', 'zu', 'um', 'her', 'hin', 'los', 'weg')


def namensliste(text):
    """Namen aus den `A · B · C`-Zeilen der Prompts.

    Der Anlass: die Namenslisten stehen als Fliesstext ohne Backticks,
    und deshalb pruefte das Skript sie gar nicht. In Zefanja 2 gingen so
    zwei falsche Namen durch — der Prompt schrieb `Kereter` und
    `Aschdod`, der Text hat `Kreter` und `Asdod`. Beide sind im Bestand
    gebunden; der Agent hat es am Vers gemerkt.

    Erkannt wird eine Zeile, die ueberwiegend aus grossgeschriebenen
    Woertern besteht, die mit `·` getrennt sind.
    """
    out = []
    for zeile in text.split('\n'):
        if zeile.count('·') < 2:
            continue
        teile = [x.strip(' *`') for x in zeile.split('·')]
        gross = [x for x in teile if x[:1].isupper() and x.isalpha()]
        if len(gross) >= 3 and len(gross) >= len(teile) - 2:
            out += gross
    return out


def stamm(w):
    """Kleingeschrieben, ohne Umlaute, ohne haeufige Endung.

    Die Umschrift wird mitgezogen: die Vorbereitungsdateien schreiben
    `Goetze` und `giessen`, der Quelltext `Götze` und `gießt`. Ohne diese
    Zeile meldet das Skript jedes umgelautete Wort des Prompts als fehlend.
    """
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = w.replace('ß', 's')
    w = re.sub(r'[^a-z]', '', w)
    for a, b in (('oe', 'o'), ('ue', 'u'), ('ae', 'a'), ('ss', 's')):
        w = w.replace(a, b)
    for e in ENDUNGEN:
        if len(w) - len(e) >= MIN and w.endswith(e):
            w = w[:-len(e)]
            break
    if w.startswith('ge') and len(w) - 2 >= MIN - 1:
        w = w[2:]
    else:
        # Trennbare Verben tragen das Partizip-`ge-` in der MITTE:
        # `umgekehrt` gehoert zu `umkehren`, `angefangen` zu `anfangen`.
        # Ohne diesen Zweig meldete das Skript den Amos-4-Refrain
        # („Doch ihr seid nicht zu mir umgekehrt") als fehlend, obwohl
        # er fuenfmal dasteht.
        for pfx in TRENNBAR:
            if w.startswith(pfx + 'ge') and len(w) - 2 >= MIN:
                w = pfx + w[len(pfx) + 2:]
                break
    return w


def kapiteltokens(nr, kaps):
    """{stamm: [erste Fundstellen]} ueber alle genannten Kapitel."""
    quelle = C.load_source(nr)['chapters']
    treffer = {}
    for kap in kaps:
        for vers, text in quelle[str(int(kap))].items():
            for tok in C.tokens(text):
                s = stamm(C.strip_punct(tok))
                if s:
                    treffer.setdefault(s, []).append(f'{kap},{vers}')
    return treffer


def promptwoerter(pfad):
    """Deutsche Woerter in Backticks UND in deutschen Anfuehrungszeichen.

    Die erste Fassung sah nur Backticks. In Hosea 6 hat der Prompt den Vers
    als Zitat wiedergegeben — „Kommt, wir wollen zum HERRN umkehren" — und
    zwei Woerter daraus waren falsch: der Quelltext sagt `zurueckkehren`,
    und `Morgenrot` heisst dort `Morgenroete`. Beide standen ausserhalb der
    Backticks und rutschten durch; der Agent hat sie am Vers gefunden.

    Ein Zitat aus dem Quelltext ist genau die Sorte Behauptung, die dieses
    Werkzeug pruefen soll — also werden „…"-Abschnitte mitgelesen.
    """
    with open(pfad, encoding='utf-8') as f:
        text = f.read()
    raus, gesehen = [], set()
    quellen = (re.findall(r'`([^`\n]{2,60})`', text)
               + re.findall(r'„([^„“"\n]{2,200})[“"]', text)
               + namensliste(text))
    for roh in quellen:
        roh = roh.strip()
        if KEIN_TEXT.search(roh):
            continue
        for wort in roh.split():
            wort = wort.strip('.,;:!?()[]„“"\'…—–-')
            if len(wort) < 4 or not re.fullmatch(r'[A-Za-zÄÖÜäöüß]+', wort):
                continue
            if wort.lower() in gesehen:
                continue
            gesehen.add(wort.lower())
            raus.append(wort)
    return raus


def main():
    argv = sys.argv[1:]
    if '--datei' in argv:
        i = argv.index('--datei')
        woerter = promptwoerter(argv[i + 1])
        kopf, quelle = argv[:i], argv[i + 1]
    elif '--woerter' in argv:
        i = argv.index('--woerter')
        woerter, kopf, quelle = argv[i + 1:], argv[:i], 'Argumentliste'
    else:
        print(__doc__)
        return 2
    if len(kopf) < 2:
        print(__doc__)
        return 2

    nr, kaps = int(kopf[0]), kopf[1:]
    vorhanden = kapiteltokens(nr, kaps)
    name = C.book_name(nr)

    print(f'# Promptprobe: {name} {", ".join(kaps)} gegen {quelle}')
    print(f'\n{len(woerter)} geprueft, {len(vorhanden)} verschiedene Stämme '
          f'im Quelltext.\n')

    fehlt = []
    for w in woerter:
        s = stamm(w)
        if s in vorhanden:
            continue
        # Praefixprobe: `Goetzenbild` steht als `Goetzenbilder`, `Handbreite`
        # als `Handbreit`. Nur in dieser Richtung, sonst trifft jedes kurze
        # Wort auf jedes lange.
        # Je kuerzer der Stamm, desto enger der erlaubte Abstand: `Tor` gegen
        # `Tore` ist ein Treffer, `an` gegen `ansag` bleibt keiner.
        nah = [k for k in vorhanden
               if min(len(s), len(k)) >= KURZ
               and abs(len(s) - len(k)) <= (ABSTAND if min(len(s), len(k)) >= 4 else 1)
               and (k.startswith(s) or s.startswith(k))]
        fehlt.append((w, nah))

    if not fehlt:
        print('Jedes Wort des Prompts kommt im Quelltext vor.')
    for w, nah in fehlt:
        if nah:
            bsp = ', '.join(f'{k} ({vorhanden[k][0]})' for k in sorted(nah)[:3])
            print(f'  `{w}`  — nicht als eigene Form, aber stammverwandt: {bsp}')
        else:
            print(f'  `{w}`  — **kommt im Quelltext nicht vor**')

    hart = sum(1 for _, nah in fehlt if not nah)
    print(f'\n{hart} Woerter kommen gar nicht vor, '
          f'{len(fehlt) - hart} nur stammverwandt. '
          'Jeden Treffer am Quelltext ansehen, bevor der Prompt rausgeht — '
          'ein Stammvergleich findet weder Umlautwechsel noch starke Verben.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
