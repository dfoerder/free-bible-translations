"""Struktur-Validator (Ebene 1 der Qualitätssicherung).

Prüft, was sich am Quelltext mechanisch nachrechnen lässt:
Vollständigkeit, Formen, Spannen, Klammern, Feldbelegung.
Inhaltliche Heuristiken stehen in qa.py.

Aufruf als Bibliothek:  validate_chapter(nr, kap, data, partial=False) -> [fehler]
"""
import re
import sys

import common as C

BRACKET_TAG = re.compile(r'^\(.*\)$')
GRAMMAR_TAG = re.compile(r'\((futuro|presente|pasado|passé|futur|imperfetto|'
                         r'subjonctif|subjuntivo|congiuntivo|plural|singular|'
                         r'passive|aktiv|dativ|genitiv|akkusativ)\)', re.I)


def _bad_value(v):
    if not isinstance(v, str):
        return 'kein String'
    if v.strip() == '':
        return 'leer'
    if v.strip() in {'-', '–', '—', '?', '…'}:
        return f'Platzhalter {v!r}'
    if BRACKET_TAG.match(v.strip()):
        return f'Klammer-Tag {v!r}'
    if GRAMMAR_TAG.search(v):
        return f'Grammatik-Tag {v!r}'
    return None


def validate_verse(text, entries, ort):
    """Fehlerliste für einen Vers. `ort` ist ein Präfix wie '3,12'."""
    errs = []
    toks = C.tokens(text)
    n = len(toks)

    seen = {}
    for e in entries:
        for f in C.FIELDS:
            if f not in e:
                errs.append(f'{ort}: Eintrag pos={e.get("pos")} ohne Feld {f}')
        if not isinstance(e.get('pos'), int):
            errs.append(f'{ort}: pos ist keine Zahl: {e.get("pos")!r}')
            continue
        for f in ['form', 'lemma'] + C.LANGS:
            if f in e:
                bad = _bad_value(e[f])
                if bad:
                    errs.append(f'{ort}: pos={e["pos"]} Feld {f}: {bad}')
        if e.get('level') not in C.LEVELS:
            errs.append(f'{ort}: pos={e["pos"]} Level {e.get("level")!r} unbekannt')

        pos = e['pos']
        if pos < 0 or pos >= n:
            errs.append(f'{ort}: pos={pos} außerhalb des Verses (0..{n-1})')
            continue

        if 'parts' in e:
            parts = e['parts']
            if not isinstance(parts, list) or len(parts) < 2:
                errs.append(f'{ort}: pos={pos} parts braucht mindestens zwei Positionen')
                continue
            if parts != sorted(parts) or len(set(parts)) != len(parts):
                errs.append(f'{ort}: pos={pos} parts nicht aufsteigend/eindeutig: {parts}')
            if parts[0] != pos:
                errs.append(f'{ort}: pos={pos} != parts[0]={parts[0]}')
            if max(parts) >= n:
                errs.append(f'{ort}: parts {parts} außerhalb des Verses (0..{n-1})')
                continue
            if parts == list(range(parts[0], parts[-1] + 1)):
                errs.append(f'{ort}: pos={pos} parts ist zusammenhängend — pos_end benutzen')
            soll = ' '.join(C.strip_punct(toks[p]) for p in parts)
            if e.get('form') != soll:
                errs.append(f'{ort}: pos={pos} form {e.get("form")!r} != Tokens {soll!r}')
        elif 'pos_end' in e:
            pe = e['pos_end']
            if not isinstance(pe, int) or pe <= pos:
                errs.append(f'{ort}: pos={pos} pos_end={pe!r} muss größer als pos sein')
                continue
            if pe >= n:
                errs.append(f'{ort}: pos={pos} pos_end={pe} außerhalb des Verses (0..{n-1})')
                continue
            soll = ' '.join(C.strip_punct(t) for t in toks[pos:pe + 1])
            if e.get('form') != soll:
                errs.append(f'{ort}: pos={pos}-{pe} form {e.get("form")!r} != Tokens {soll!r}')
        else:
            if pos in seen:
                errs.append(f'{ort}: Position {pos} doppelt annotiert')
            seen[pos] = e
            soll = C.strip_punct(toks[pos])
            if e.get('form') != soll:
                errs.append(f'{ort}: pos={pos} form {e.get("form")!r} != Token {soll!r}')

    for i, t in enumerate(toks):
        if C.is_punct_only(t):
            if i in seen:
                errs.append(f'{ort}: pos={i} ist ein alleinstehendes Satzzeichen {t!r} '
                            f'und darf keinen Eintrag haben')
        elif i not in seen:
            errs.append(f'{ort}: Position {i} ({t!r}) hat keinen Einzelwort-Eintrag')

    return errs


def validate_chapter(nr, kap, data, partial=False, von=None, bis=None):
    """data = {vers: [eintraege]}. partial=True erlaubt fehlende Verse."""
    src = C.load_source(nr)['chapters']
    kap = str(kap)
    if kap not in src:
        return [f'Kapitel {kap} gibt es in Buch {nr} nicht']
    verses = src[kap]
    errs = []

    soll_verse = set(verses)
    if von is not None:
        soll_verse = {v for v in soll_verse if von <= int(v) <= bis}
    ist_verse = set(data)

    fremd = sorted(ist_verse - set(verses), key=lambda v: int(v) if v.isdigit() else 0)
    if fremd:
        errs.append(f'Verse ohne Entsprechung im Quelltext: {fremd}')
    fehlend = sorted(soll_verse - ist_verse, key=int)
    if fehlend and not partial:
        errs.append(f'{len(fehlend)} Verse fehlen: {fehlend[:20]}'
                    + (' …' if len(fehlend) > 20 else ''))

    for v in sorted(ist_verse & set(verses), key=int):
        errs += validate_verse(verses[v], data[v], f'{kap},{v}')
    return errs


def validate_book(nr, quiet=False):
    """Gebaute Anno-Datei gegen den Quelltext prüfen (Ebene 1 + Vollständigkeit)."""
    src = C.load_source(nr)['chapters']
    ann = C.load_anno(nr, cache=False)['chapters']
    errs = []
    fehlend = [k for k in src if k not in ann]
    if fehlend:
        errs.append(f'Kapitel fehlen ganz: {sorted(fehlend, key=int)}')
    for kap in sorted(set(src) & set(ann), key=int):
        errs += validate_chapter(nr, kap, ann[kap])
    if not quiet:
        for e in errs:
            print(e)
    return errs


def gegenrechnung(nr):
    """Tokens im Quelltext − Einzelworteinträge = alleinstehende Satzzeichen."""
    src = C.load_source(nr)['chapters']
    ann = C.load_anno(nr, cache=False)['chapters']
    tok = sum(len(C.tokens(t)) for vs in src.values() for t in vs.values())
    zeichen = sum(1 for vs in src.values() for t in vs.values()
                  for x in C.tokens(t) if C.is_punct_only(x))
    einzel = sum(len(C.singles(e)) for vs in ann.values() for e in vs.values())
    mehr = sum(len(C.multis(e)) for vs in ann.values() for e in vs.values())
    return tok, einzel, mehr, zeichen


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Aufruf: validate.py <buchNr> [buchNr …]   |   validate.py alle')
        sys.exit(1)
    nrs = C.anno_books() if sys.argv[1] == 'alle' else [int(a) for a in sys.argv[1:]]
    schlimm = 0
    for nr in nrs:
        errs = validate_book(nr, quiet=True)
        tok, einzel, mehr, zeichen = gegenrechnung(nr)
        name = C.load_source(nr)['name']
        ok = 'ok' if not errs and tok - einzel == zeichen else 'FEHLER'
        print(f'{nr:>2} {name:<20} {tok} Tokens − {einzel} Einzel = {tok-einzel} '
              f'(Satzzeichen {zeichen}) · {mehr} Mehrwort · {len(errs)} Befunde  [{ok}]')
        for e in errs[:40]:
            print('   ', e)
        schlimm += len(errs) + (0 if tok - einzel == zeichen else 1)
    sys.exit(1 if schlimm else 0)
