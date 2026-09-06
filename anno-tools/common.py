"""Gemeinsame Grundlagen der Annotations-Werkzeugkette.

Pfade, Tokenisierung, Laden von Quelltext, Kapitelquellen und Anno-Dateien.
Alle anderen Werkzeuge importieren von hier.

## Welche Ausgabe annotiert wird

Bis Maleachi war das fest verdrahtet: Quelltext `deu/l1912mod`, Glossen
in en/es/fr/it. Seit dem franzoesischen NT entscheidet die Umgebungs-
variable **`ANNO_EDITION`** — Default bleibt `deu/l1912mod`, damit jeder
alte Aufruf unveraendert laeuft:

    export ANNO_EDITION=fra/lsg1910mod

Daraus leiten sich Quelltextverzeichnis, beide Dateinamensmuster, die
Glossensprachen und die Liste der Referenzausgaben ab. `LANGS` sind
**immer die vier anderen** Sprachen, nie die des Quelltextes.

Die Level bedeuten CEFR aus Sicht dessen, der die **Sprache des
Quelltextes** lernt — bei `fra/lsg1910mod` also Franzoesischlernende.
"""
import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
TRANS = os.path.dirname(HERE)                              # bibles-translations
REPO = os.path.join(os.path.dirname(TRANS), 'bible-reader')

# Alle fuenf Ausgaben, die im Repo liegen. `anno` ist None, wo keine
# Annotation existiert (RIV1927) — dann taugt der Eintrag nur als Zeuge.
# Die Dateinamen sind historisch gewachsen und nicht einheitlich:
# WEB heisst `_web_deu.json`, weil die Datei einmal nur Deutsch trug.
AUSGABEN = {
    'deu/l1912mod':   {'kurz': 'de', 'text': '_l1912mod.json',
                       'anno': '_l1912mod_multi.json',
                       'langs': ['en', 'es', 'fr', 'it']},
    'eng/web':        {'kurz': 'en', 'text': '_web.json',
                       'anno': '_web_deu.json',
                       'langs': ['de', 'es', 'fr', 'it']},
    'spa/rv1909mod':  {'kurz': 'es', 'text': '_rv1909mod.json',
                       'anno': '_rv1909mod_eng.json',
                       'langs': ['en']},
    'ita/riv1927':    {'kurz': 'it', 'text': '_riv1927.json',
                       'anno': None,
                       'langs': []},
    'fra/lsg1910mod': {'kurz': 'fr', 'text': '_lsg1910mod.json',
                       'anno': '_lsg1910mod_multi.json',
                       'langs': ['de', 'en', 'es', 'it']},
}

# Welche Ausgabe jede Sprache als Zeuge vertritt. `fr` steht auf der
# unmodernisierten LSG, weil der ganze deutsche Bestand gegen sie
# gearbeitet hat; als Quelltext dient die modernisierte.
ZEUGE = {'de': 'deu/l1912mod', 'en': 'eng/web', 'es': 'spa/rv1909mod',
         'it': 'ita/riv1927', 'fr': 'fra/lsg1910'}

EDITION = os.environ.get('ANNO_EDITION', 'deu/l1912mod')
if EDITION not in AUSGABEN:
    raise SystemExit(f'ANNO_EDITION={EDITION!r} ist keine bekannte Ausgabe. '
                     f'Bekannt: {", ".join(sorted(AUSGABEN))}')
_E = AUSGABEN[EDITION]

LANG = _E['kurz']                                          # Sprache des Quelltextes
TEXT_SUFFIX = _E['text']
ANNO_SUFFIX = _E['anno']
SRC_DIR = os.path.join(REPO, 'bibles', *EDITION.split('/'))
ANNO_DIR = os.path.join(SRC_DIR, 'anno')
QUELLEN = os.path.join(TRANS, 'anno-quellen', *EDITION.split('/'))

LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
LANGS = _E['langs']
FIELDS = ['pos', 'form', 'lemma', 'level'] + LANGS


def zeugen():
    """[(kuerzel, 'spr/edition')] — die Referenzausgaben neben dem Quelltext.

    In der Reihenfolge von LANGS, ohne die eigene Ausgabe.
    """
    return [(l, ZEUGE[l]) for l in LANGS]


def text_pfad(edition, nr):
    """Pfad zum Quelltext einer beliebigen Ausgabe."""
    suffix = AUSGABEN[edition]['text'] if edition in AUSGABEN \
        else '_' + edition.split('/')[1] + '.json'
    return os.path.join(REPO, 'bibles', *edition.split('/'), f'{int(nr)}{suffix}')

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
        with open(os.path.join(SRC_DIR, f'{nr}{TEXT_SUFFIX}'), encoding='utf-8') as f:
            _src_cache[nr] = json.load(f)
    return _src_cache[nr]


def anno_path(nr):
    return os.path.join(ANNO_DIR, f'{int(nr)}{ANNO_SUFFIX}')


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
    if not os.path.isdir(ANNO_DIR):
        return []
    out = []
    for fn in os.listdir(ANNO_DIR):
        m = re.match(r'^(\d+)' + re.escape(ANNO_SUFFIX) + '$', fn)
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


def reihe(e):
    """Die Glossenreihe eines Eintrags als Tupel, in LANGS-Reihenfolge.

    Bis Maleachi stand ueberall `(e['en'], e['es'], e['fr'], e['it'])`
    ausgeschrieben. Das ist genau die Stelle, an der eine Ausgabe mit
    anderer Sprachliste mit einem KeyError abbricht — oder, schlimmer,
    stillschweigend die falsche Spalte vergleicht.
    """
    return tuple(e[l] for l in LANGS)


def zeige(vals, kurz=False):
    """Eine Glossenreihe zum Ausdrucken: `en *x* · es *y* · …`

    Mit `kurz=True` ohne die Sprachkuerzel, fuer Tabellenzeilen, in denen
    die Spaltenfolge ohnehin im Kopf steht.
    """
    vals = list(vals)
    if kurz:
        return ' · '.join(f'*{v}*' for v in vals)
    return ' · '.join(f'{l} *{v}*' for l, v in zip(LANGS, vals))


def de_wort(e):
    """Das deutsche Wort eines Eintrags — Form oder Glosse, je nach Ausgabe.

    `artikel.py` und `kongruenz.py` finden das Nomen einer Attributkette
    ueber die deutsche **Grossschreibung**: deutsche Nomen sind gross,
    Adjektive klein. Das ist eine gute Heuristik und es gibt keine
    zweite — franzoesische und englische Nomen sind klein wie ihre
    Adjektive.

    In `deu/l1912mod` steht das Deutsche in `form`, in `eng/web` und
    `fra/lsg1910mod` in der `de`-Spalte. Beide Werkzeuge lasen fest
    `form` und fielen deshalb in der franzoesischen Richtung lautlos
    aus: kein Treffer, keine Meldung, kein Hinweis darauf, dass sie
    nichts geprueft haben.
    """
    return e['form'] if LANG == 'de' else (e.get('de') or '')


def anno_wie_datei(nr, kap, pfad):
    """Eine Kapitelquelle in der Form einer Anno-Datei.

    Mehrere Pruefungen lesen die **gebaute** Anno-Datei und sind damit
    fuer ein Kapitel, das noch beim Agenten liegt, nicht benutzbar —
    beim ersten Buch einer Ausgabe fuer gar nichts. `glosskollision.py`
    und `qa.py` hatten dafuer schon eigene Schalter; das hier ist der
    gemeinsame Weg. Gemeldet vom Agenten fuer Matthaeus 3.
    """
    with open(pfad, encoding='utf-8') as f:
        d = json.load(f)
    d = d.get('chapters', {}).get(str(kap), d)
    return {'name': book_name(nr), 'chapters': {str(kap): d}}
