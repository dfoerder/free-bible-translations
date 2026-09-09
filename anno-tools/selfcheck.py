"""Selbstprüfung für Agenten: Kapiteldatei gegen den Quelltext.

    selfcheck.py <buchNr> <kapitel> <datei.json> [<vonVers> <bisVers>]

Ohne Versbereich wird Vollständigkeit über das ganze Kapitel verlangt.
Mit Versbereich nur über diesen Abschnitt (Teillieferung).

Rückgabewert 0 = sauber. Jeder Agent ruft das vor der Abgabe auf.
"""
import json
import sys

import common as C
import validate as V


def spannenlaenge(eintraege, ort, errs):
    """`form` eines Mehrworts muss so viele Woerter haben wie die Spanne Token.

    Eine harte Regel, keine Statistik: `form` gibt die Spanne woertlich
    wieder. Ueber den ganzen Bestand gemessen halten sie alle 2500
    Mehrwoerter ein.

    Anlass: ein Bauskript machte aus dem Tupel `(6, 10)` still ein
    `pos_end` statt `parts`. Gemeldet vom Agenten fuer Philipper 3, der
    ihn selbst fand: „keine Probe vergleicht die Laenge einer
    Mehrwortglosse mit der Laenge ihrer Spanne."

    WIE WEIT DAS TRAEGT: Wer `form` von Hand setzt und die Spanne
    danebenlegt, faellt hier auf — und `validate` faengt denselben Fall
    ohnehin ueber den Vergleich von `form` mit dem Quelltext. Wer
    `form` dagegen aus der falschen Spanne MITBAUT, bleibt in beiden
    Proben unsichtbar: dann stimmt alles mit sich selbst ueberein, nur
    nicht mit der Absicht. Diese Probe praezisiert die Meldung
    („pos_end statt parts?"), sie schliesst die Luecke nicht.
    """
    for e in eintraege:
        w = len((e.get('form') or '').split())
        if 'pos_end' in e:
            soll = e['pos_end'] - e['pos'] + 1
            wie = f"pos_end-Spanne {soll}"
        elif 'parts' in e:
            soll = len(e['parts'])
            wie = f"parts {soll}"
        else:
            continue
        if w != soll:
            errs.append(f'{ort}: Mehrwort {e.get("form")!r} deckt {wie} '
                        f'Token, `form` hat aber {w} Woerter — '
                        f'`pos_end` statt `parts` gesetzt?')


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    nr, kap, pfad = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    von = int(sys.argv[4]) if len(sys.argv) > 4 else None
    bis = int(sys.argv[5]) if len(sys.argv) > 5 else None

    with open(pfad, encoding='utf-8') as f:
        data = json.load(f)
    if 'chapters' in data:                      # ganze Buchdatei geliefert
        data = data['chapters'][str(kap)]

    errs = V.validate_chapter(nr, kap, data, partial=False, von=von, bis=bis)
    for v in sorted(data, key=lambda x: int(x)):
        spannenlaenge(data[v], f'{nr} {kap},{v}', errs)
    src = C.load_source(nr)['chapters'][str(kap)]
    soll = [v for v in src if von is None or von <= int(v) <= bis]
    tok = sum(len(C.tokens(src[v])) for v in soll)
    zeichen = sum(1 for v in soll for t in C.tokens(src[v]) if C.is_punct_only(t))
    einzel = sum(len(C.singles(data[v])) for v in data if v in src)
    mehr = sum(len(C.multis(data[v])) for v in data if v in src)

    name = C.load_source(nr)['name']
    bereich = f'{kap}' + (f',{von}–{bis}' if von is not None else '')
    print(f'{name} {bereich}: {len(data)}/{len(soll)} Verse · {einzel} Einzelwort- '
          f'· {mehr} Mehrwort-Einträge')
    print(f'Gegenrechnung: {tok} Tokens − {einzel} Einzeleinträge = {tok - einzel} '
          f'(alleinstehende Satzzeichen: {zeichen}) — '
          + ('stimmt' if tok - einzel == zeichen else 'STIMMT NICHT'))
    if errs:
        print(f'\n{len(errs)} Befunde:')
        for e in errs:
            print(' ', e)
        return 1
    print('Struktur sauber.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
