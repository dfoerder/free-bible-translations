"""Gemeinsame Grundlagen der Annotations-Werkzeugkette (deu/l1912mod).

Pfade, Tokenisierung, Laden von Quelltext, Kapitelquellen und Anno-Dateien.
Alle anderen Werkzeuge importieren von hier.
"""
import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
TRANS = os.path.dirname(HERE)                              # bibles-translations
REPO = os.path.join(os.path.dirname(TRANS), 'bible-reader')
SRC_DIR = os.path.join(REPO, 'bibles', 'deu', 'l1912mod')
ANNO_DIR = os.path.join(SRC_DIR, 'anno')
QUELLEN = os.path.join(TRANS, 'anno-quellen', 'deu', 'l1912mod')

LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
LANGS = ['en', 'es', 'fr', 'it']
FIELDS = ['pos', 'form', 'lemma', 'level'] + LANGS

# Zeichen, die am Tokenrand abgestreift werden. Empirisch aus dem fertigen
# Bestand abgeleitet (1. Mose, 2. Mose, Matthäus, Römer, Offenbarung):
# , . : ; ? ! " ( ) - kommen dort vor, der Rest ist Vorsorge.
PUNCT = ',.:;?!"()[]«»„“”‚‘’\'-–—…'


def strip_punct(tok):
    """Token ohne umschließende Satzzeichen. Binnenzeichen bleiben."""
    return tok.strip(PUNCT)


def is_punct_only(tok):
    """Alleinstehendes Satzzeichen — bekommt laut Spezifikation keinen Eintrag."""
    return strip_punct(tok) == ''


def tokens(text):
    return text.split()


def book_name(nr):
    return load_source(nr)['name']


_src_cache = {}


def load_source(nr):
    """{'name':…, 'chapters': {kap: {vers: text}}} des Quelltextes."""
    nr = int(nr)
    if nr not in _src_cache:
        with open(os.path.join(SRC_DIR, f'{nr}_l1912mod.json'), encoding='utf-8') as f:
            _src_cache[nr] = json.load(f)
    return _src_cache[nr]


def anno_path(nr):
    return os.path.join(ANNO_DIR, f'{int(nr)}_l1912mod_multi.json')


def has_anno(nr):
    return os.path.exists(anno_path(nr))


_anno_cache = {}


def load_anno(nr, cache=True):
    nr = int(nr)
    if cache and nr in _anno_cache:
        return _anno_cache[nr]
    with open(anno_path(nr), encoding='utf-8') as f:
        d = json.load(f)
    if cache:
        _anno_cache[nr] = d
    return d


def anno_books():
    """Alle Buchnummern mit fertiger Anno-Datei, aufsteigend."""
    out = []
    for fn in os.listdir(ANNO_DIR):
        m = re.match(r'^(\d+)_l1912mod_multi\.json$', fn)
        if m:
            out.append(int(m.group(1)))
    return sorted(out)


def quellen_dir(nr):
    return os.path.join(QUELLEN, str(int(nr)))


def load_quelle(nr, kap):
    """Kapitelquelle {vers: [eintraege]} oder None."""
    p = os.path.join(quellen_dir(nr), f'ch{int(kap)}.json')
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def quellen_kapitel(nr):
    d = quellen_dir(nr)
    if not os.path.isdir(d):
        return []
    out = []
    for fn in os.listdir(d):
        m = re.match(r'^ch(\d+)\.json$', fn)
        if m:
            out.append(int(m.group(1)))
    return sorted(out)


def is_multi(e):
    return 'pos_end' in e or 'parts' in e


def covered(e):
    """Alle Positionen, die ein Eintrag abdeckt."""
    if 'parts' in e:
        return list(e['parts'])
    if 'pos_end' in e:
        return list(range(e['pos'], e['pos_end'] + 1))
    return [e['pos']]


def singles(entries):
    return [e for e in entries if not is_multi(e)]


def multis(entries):
    return [e for e in entries if is_multi(e)]


def write_compact(path, data):
    """Kompakt schreiben wie bibles/eng/web/anno/* — Einrückung kostet 39 %."""
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    os.replace(tmp, path)


def write_quelle(nr, kap, data):
    d = quellen_dir(nr)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, f'ch{int(kap)}.json')
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    os.replace(tmp, p)


def norm_key(s):
    """Vergleichsschlüssel: kleingeschrieben, ohne Akzente, ohne Satzzeichen."""
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9äöüß ]', '', s).strip()


def iter_corpus(books=None):
    """Iteriert (buchNr, kap, vers, eintrag) über alle Anno-Dateien."""
    for nr in (books or anno_books()):
        d = load_anno(nr)
        for kap, verses in d['chapters'].items():
            for vers, entries in verses.items():
                for e in entries:
                    yield nr, kap, vers, e
