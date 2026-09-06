"""Hilfsverb, dessen Glosse das Vollverb des Nachbartokens verschluckt.

    hilfsverb.py <buchNr …> | alle [--abstand 12]

Gesucht wird: ein Hilfsverb (`werden`, `sollen`, `wollen`, `können`, `müssen`,
`dürfen`, `mögen`, `lassen`, `haben`, `sein`), dessen Glosse mit der Glosse
eines Vollverbs im selben Vers den Wortstamm teilt. `qa.py` sieht das nicht —
strukturell ist der Eintrag perfekt, und die Glossen sind nicht identisch,
sondern nur **stammgleich**.

## Bei `werden` ist das die Konvention, kein Fehler

Die erste Fassung dieses Werkzeugs führte „ich **würde sterben**" als
Fehlerbeispiel und hat zwei Stellen periphrastisch umgestellt (1Mo 19,19,
1Kor 14,25 → *iba a · allais · stavo per* + Infinitiv). **Diese Auffassung ist
mit Hiob revidiert worden.**

Der Grund: die Periphrase ist Futur-im-Vergangenen. Für einen Irrealis der
Gegenwart sagt sie das Falsche — *stava per mentire* heißt „er war im Begriff
zu lügen", nicht „er würde lügen". Und der Bestand war in dieser Frage von
Anfang an **gespalten**: 1Mo 42,38 (`würdet` = *llevaríais · conduiriez ·
condurreste* neben `bringen` = *llevar · conduire · condurre*) und 1Mo 44,34
(`würde` = *alcanzaría · atteindrait · colpirebbe*) tragen den Konditional des
Vollverbs und sind nie umgestellt worden — 42,38 nur deshalb nicht, weil der
Abstand elf Tokens beträgt und das Fenster damals acht war.

**Die geltende Regel** (siehe `WORTFELD_POESIE.md` des Buches Hiob): bei echtem
Irrealis trägt das Hilfsverb den Konditional des Vollverbs, bei echtem Futur
die periphrastische Lesart. 1Mo 19,19 und 1Kor 14,25 sind auf den Konditional
zurückgezogen.

Die `werden`-Treffer stehen deshalb in einem **eigenen Abschnitt**: sie sind
die erwartete Bauform und nur dann ein Befund, wenn der Vers gar kein Irrealis
ist. Die übrigen Hilfsverben bleiben Verdachtsfälle im alten Sinn.
"""
import argparse

import common as C

# Die Hilfsverben des QUELLTEXTES. Die deutsche Liste traf im
# franzoesischen Text kein einziges Lemma — der Lauf meldete '0 Treffer'
# und hatte nichts geprueft. Dieselbe Falle wie bei qa.py und hints.py.
HILFSVERBEN_JE_SPRACHE = {
    'de': {'werden', 'sollen', 'wollen', 'können', 'müssen', 'dürfen',
           'mögen', 'lassen', 'haben', 'sein'},
    'fr': {'être', 'avoir', 'aller', 'pouvoir', 'devoir', 'vouloir',
           'faire', 'laisser', 'venir'},
    'en': {'be', 'have', 'do', 'will', 'shall', 'can', 'may', 'must',
           'let', 'go'},
    'es': {'ser', 'estar', 'haber', 'tener', 'poder', 'deber', 'querer',
           'hacer', 'dejar', 'ir'},
}
HILFSVERBEN = HILFSVERBEN_JE_SPRACHE.get(C.LANG, set())
MIN_STAMM = 5
ABSTAND = 12   # war 8; 1Mo 42,38 hat elf Tokens Abstand und fiel durch


def _stamm(g):
    w = g.lower().split()
    return w[-1][:MIN_STAMM] if w else ''


def pruefe(nrs, abstand=ABSTAND, datei=None, kapitel=None):
    if not HILFSVERBEN:
        print(f'!! Fuer die Quelltextsprache {C.LANG!r} sind keine '
              'Hilfsverben hinterlegt — dieser Lauf prueft NICHTS.')
        return []
    treffer = []
    for nr in nrs:
        name = C.load_source(nr)['name']
        if datei:
            d = C.anno_wie_datei(nr, kapitel, datei)['chapters']
        else:
            d = C.load_anno(nr)['chapters']
        for kap, verses in d.items():
            for vers, entries in verses.items():
                einzel = [e for e in entries if not C.is_multi(e)]
                hilfs = [e for e in einzel if e['lemma'] in HILFSVERBEN]
                voll = [e for e in einzel if e['lemma'] not in HILFSVERBEN]
                for h in hilfs:
                    for v in voll:
                        if abs(h['pos'] - v['pos']) > abstand:
                            continue
                        gleich = [l for l in C.LANGS
                                  if len(_stamm(h[l])) >= MIN_STAMM
                                  and _stamm(h[l]) == _stamm(v[l])]
                        if len(gleich) >= 2:
                            treffer.append((f'{name} {kap},{vers}', h, v, gleich))
    konvention = [t for t in treffer if t[1]['lemma'] == 'werden']
    verdacht = [t for t in treffer if t[1]['lemma'] != 'werden']

    def zeig(liste):
        for wo, h, v, gleich in liste:
            print(f'{wo}: {h["form"]!r} (pos {h["pos"]}) und {v["form"]!r} '
                  f'(pos {v["pos"]}) stammgleich in {", ".join(gleich)}')
            for l in gleich:
                print(f'      {l}: {h[l]!r} / {v[l]!r}')

    if konvention:
        print('## werden — die Konjunktiv-Konvention, erwartete Bauform\n')
        zeig(konvention)
        print(f'\n{len(konvention)} Stellen. Befund nur, wo der Vers gar kein '
              'Irrealis ist — dann gilt die periphrastische Lesart.\n')
    if verdacht:
        print('## Andere Hilfsverben — Verdachtsfälle\n')
        zeig(verdacht)
        print(f'\n{len(verdacht)} Verdachtsfälle.')
    if not treffer:
        print('0 Treffer.')
    return treffer


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('args', nargs='+')
    p.add_argument('--abstand', type=int, default=ABSTAND,
                   help='groesster Positionsabstand zwischen Hilfs- und Vollverb')
    p.add_argument('--datei', help='eine Kapitel-Lieferdatei statt der '
                                   'gebauten Anno-Datei pruefen: '
                                   '--datei <pfad> <nr> <kap>')
    a = p.parse_args()
    if a.datei:
        if len(a.args) != 2:
            p.error('mit --datei: <buchNr> <kapitel>')
        pruefe([int(a.args[0])], a.abstand, a.datei, a.args[1])
    else:
        nrs = C.anno_books() if a.args[0] == 'alle' else [int(x) for x in a.args]
        pruefe(nrs, a.abstand)
