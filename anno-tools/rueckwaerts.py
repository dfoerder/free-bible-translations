#!/usr/bin/env python3
"""Was der vorhandene Bestand ueber ein Wort des Quelltextes schon weiss.

    rueckwaerts.py <buchNr> <kapitel> [<vonVers> [<bisVers>]] [-o datei]
    rueckwaerts.py --wort <wort> [<wort> ...]

## Der Anlass

Fuer die deutsche Annotation musste jedes Wort neu entschieden werden —
es gab keinen Zeugen, der schon Wort fuer Wort glossiert war. Fuer die
franzoesische gibt es zwei.

`eng/web` und `deu/l1912mod` sind beide vollstaendig annotiert und tragen
**beide eine `fr`-Spalte**. Zusammen decken sie genau die vier
Zielsprachen ab:

    eng/web        Quelltext = en,  Spalten de · es · fr · it
    deu/l1912mod   Quelltext = de,  Spalten en · es · fr · it

Jeder Eintrag ist damit eine vollstaendige Zeile **de · en · es · it**,
und die `fr`-Spalte ist ihr Schluessel. Ueber das ganze NT gemessen sind
so 98 Prozent der franzoesischen Tokens bereits belegt.

## Fuenf Schichten, absteigend belastbar

    VERS       das Token steht als fr-Glosse **in genau diesem Vers**
               der Zeugen. Das ist die einzige Schicht, die nicht nur
               das Wort, sondern die Stelle trifft — hier ist die Zeile
               fast immer schon die richtige.
    BESTAND    dieselbe Form steht **schon franzoesisch annotiert** im
               eigenen Bestand, mit franzoesischem Lemma und Level. Ab
               Markus die zweitstaerkste Schicht; vorher gab es sie
               nicht, weil die franzoesische Anno leer war.
    GLOSSE     das ganze Token steht irgendwo im Bestand als fr-Glosse
    TEIL       es steht als Wort INNERHALB einer mehrwortigen fr-Glosse
               (`des` in `de les`) — die ganze Glosse steht daneben
    ELISION    nur die Haelften eines zusammengezogenen Wortes sind
               belegt (`qu'ils` = `qu'` + `ils`); dann sind es zwei
               Vorschlaege fuer EIN Token, und die Glosse muss beide
               zusammenfassen

Was in keiner Schicht steht, ist die eigentliche Arbeit. In Judas sind
das 11 von 612 Tokens.

**Die VERS-Schicht ersetzt das Nachschlagen nicht.** Sie setzt voraus,
dass die Verszaehlung der Zeugen mit der franzoesischen uebereinstimmt.
Wo `ausgaben.py` einen Versatz meldet, ist sie fuer dieses Kapitel
wertlos — dann steht ueber dem Abschnitt eine Warnung.

## Was dieses Werkzeug NICHT liefert

**Kein Lemma.** Das Lemma im Zeugen ist englisch oder deutsch; das
franzoesische muss gesetzt werden.

**Kein Level.** Das Level im Zeugen ist CEFR fuer Englisch- oder
Deutschlernende. `mangera` ist im Franzoesischen nicht dort, wo `will
eat` im Englischen steht. Das Level steht nur zur Orientierung dabei,
in Klammern und mit der Ausgabe, aus der es stammt.

**Keine Entscheidung.** Wo mehrere Zeilen stehen, ist die haeufigste
nicht automatisch die richtige — das ist die Lexikonfalle, die im
deutschen Durchgang am meisten Fehler gekostet hat. Der Vers
entscheidet.
"""
import argparse
import collections
import json
import os
import sys
import unicodedata

import common as C

# Die vierspaltigen Zeugen. `formlang` ist die Sprache ihres Quelltextes
# — die liefert die vierte Spalte, die nicht als Glosse dasteht, sondern
# als Wortform.
#
# Bis zum italienischen Durchgang standen hier `eng/web` und
# `deu/l1912mod` fest verdrahtet, weil der Schluessel fest `fr` war. Ein
# Zeuge taugt hier genau dann, wenn er (a) annotiert ist, (b) seine
# Quelltextsprache eine deiner Zielspalten ist und (c) er eine Spalte in
# der Sprache DEINES Quelltextes fuehrt. Das ergibt fuer Franzoesisch
# dieselben zwei wie bisher und fuer Italienisch drei — `fra/lsg1910mod`
# kommt dazu, und mit ihm die einzige Quelle, die alle vier Zielsprachen
# eines italienischen Wortes aus EINEM Eintrag liefert.
def _zeugenliste():
    # Nur Ausgaben, von denen wirklich etwas gebaut daliegt. Ohne die
    # Probe stuende `ita/riv1927mod` im franzoesischen Kopf als Zeuge,
    # solange kein einziges italienisches Kapitel existiert — eine
    # Quellenangabe, die auf ein leeres Verzeichnis zeigt.
    raus = []
    for ed, cfg in C.AUSGABEN.items():
        if not (cfg['anno'] and cfg['kurz'] in C.LANGS
                and C.LANG in cfg['langs']):
            continue
        d = os.path.join(C.REPO, 'bibles', *ed.split('/'), 'anno')
        if os.path.isdir(d) and any(f.endswith(cfg['anno'])
                                    for f in os.listdir(d)):
            raus.append((ed, cfg['anno'], cfg['kurz']))
    # `eng/web` und `deu/l1912mod` zuerst: sie sind vollstaendig, die
    # anderen wachsen erst. Die Reihenfolge entscheidet, welche Lesart in
    # gleich haeufigen Faellen obenan steht.
    rang = {'eng/web': 0, 'deu/l1912mod': 1}
    return sorted(raus, key=lambda z: (rang.get(z[0], 2), z[0]))


ZEUGEN = _zeugenliste()

# Die Zielspalten — immer die vier anderen Sprachen, nie die eigene.
SPALTEN = list(C.LANGS)

# Die Sprache, in der der Schluessel steht: die des Quelltextes. In den
# Zeugen ist das eine GLOSSENSPALTE, hier ist es die Wortform.
SCHLUESSEL = C.LANG
MAX_ZEILEN = 6
DECKUNG = 0.9


def norm(s):
    """Vergleichsschluessel: klein, ohne Akzente, ohne Randzeichen.

    Akzente fallen weg, weil der Bestand sie nicht durchgehend setzt —
    `a cause de christ` steht neben `à cause`. Der Apostroph bleibt: er
    traegt in `qu'ils` die ganze Information.
    """
    s = unicodedata.normalize('NFD', (s or '').lower()).replace('’', "'")
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.strip(C.PUNCT.lower() + "'").strip()


def _zeile(e, formlang):
    """Ein Zeugeneintrag als Viererzeile de·en·es·it, plus Level."""
    z = {formlang: C.strip_punct(e['form'])}
    for l in SPALTEN:
        if l != formlang:
            z[l] = e.get(l, '')
    return tuple(z[l] for l in SPALTEN), e.get('level', '')


_index = None


def index(buecher=None):
    """{fr_schluessel: Counter{(zeile, level, zeuge): n}} ueber die Zeugen.

    `buecher` schraenkt ein (Default: das ganze NT, 40-66). Das AT
    mitzunehmen kostet Zeit und bringt fuer das NT wenig — die
    Wortschaetze ueberschneiden sich, die Wendungen nicht.
    """
    global _index
    if _index is not None:
        return _index
    ganz = collections.defaultdict(collections.Counter)
    teil = collections.defaultdict(collections.Counter)
    level = collections.defaultdict(collections.Counter)
    stellen = collections.defaultdict(list)
    for edition, suffix, formlang in ZEUGEN:
        for nr in (buecher or range(40, 67)):
            p = os.path.join(C.REPO, 'bibles', *edition.split('/'),
                             'anno', f'{nr}{suffix}')
            if not os.path.exists(p):
                continue
            d = json.load(open(p, encoding='utf-8'))
            name = d.get('name', str(nr))
            for kap, vv in d['chapters'].items():
                for v, ee in vv.items():
                    for e in ee:
                        f = norm(e.get(SCHLUESSEL, ''))
                        if not f:
                            continue
                        zeile, lvl = _zeile(e, formlang)
                        # Der Schluessel ist die VIERERZEILE allein. Dieselbe
                        # Zeile aus beiden Zeugen ist ein Beleg, nicht zwei —
                        # sonst steht sie zweimal untereinander und sieht aus
                        # wie zwei Lesarten. Die Level beider Zeugen sammeln
                        # sich daneben.
                        ganz[f][zeile] += 1
                        level[(f, zeile)][(lvl, formlang)] += 1
                        if len(stellen[(f, zeile)]) < 3:
                            stellen[(f, zeile)].append(f'{name} {kap},{v}')
                        woerter = f.split()
                        if len(woerter) > 1:
                            for w in woerter:
                                teil[w][(zeile, f)] += 1
    _index = (ganz, teil, level, stellen)
    return _index


def verszeilen(nr, kap):
    """{versnr: {fr_schluessel: [(zeile, level, zeuge, form)]}} — die
    Glossen der Zeugen, Vers fuer Vers.

    Der Schluessel ist wieder die normalisierte fr-Glosse; getroffen wird
    aber nur, was im GLEICHEN Vers steht. Das ist der Unterschied
    zwischen „dieses Wort kommt im NT vor" und „dieses Wort ist hier
    gemeint".
    """
    out = collections.defaultdict(lambda: collections.defaultdict(list))
    for edition, suffix, formlang in ZEUGEN:
        p = os.path.join(C.REPO, 'bibles', *edition.split('/'),
                         'anno', f'{nr}{suffix}')
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding='utf-8'))
        for v, ee in d['chapters'].get(str(kap), {}).items():
            for e in ee:
                f = norm(e.get(SCHLUESSEL, ''))
                if not f:
                    continue
                zeile, lvl = _zeile(e, formlang)
                out[str(v)][f].append((zeile, lvl, formlang))
                for w in f.split():
                    if w != f:
                        out[str(v)][w].append((zeile, lvl, formlang))
    return out


def _kuerzen(paare):
    """Die haeufigsten Zeilen, bis 90 % gedeckt sind, hoechstens MAX_ZEILEN."""
    gesamt = sum(n for _, n in paare) or 1
    zeigen, summe = [], 0
    for p in paare:
        zeigen.append(p)
        summe += p[1]
        if len(zeigen) >= MAX_ZEILEN or summe / gesamt >= DECKUNG:
            break
    return zeigen, len(paare) - len(zeigen)


def _zeilentext(zeile, lvls, n, wo=None, anhang=''):
    reihe = ' · '.join(f'{l} *{w}*' for l, w in zip(SPALTEN, zeile) if w)
    lv = ', '.join(f'{l} fuer {z}' for (l, z), _ in lvls.most_common()) if lvls else ''
    ort = f'   ({", ".join(wo)})' if wo else ''
    return f'- {n}× · {reihe}' + (f'   [{lv}]' if lv else '') + anhang + ort


_eigen = None


def eigenindex():
    """{fr_schluessel: Counter{(lemma, level, zeile): n}} — der EIGENE Bestand.

    Bis Markus fragte dieses Werkzeug nur die Zeugen: was in deren
    `fr`-Spalte steht. Das war richtig, solange die franzoesische Anno
    leer war. Judas und Matthaeus stehen aber fertig da, und ihre
    Eintraege sind der bessere Beleg — eine an einem Vers entschiedene
    Viererzeile mit franzoesischem Lemma und franzoesischem Level, nicht
    die Rueckrechnung aus einer fremden Spalte.

    Der Anlass ist ein Befund des Agenten fuer Marc 2: `dit-il`,
    `mange-t-il`, `peut-il` und `jeuneront` standen hier unter
    „UNBELEGT — hier ist die Arbeit", obwohl `belegt.py` sie alle vier
    im Bestand findet. Die Zeugen fassen die Inversionsform anders, also
    fehlt sie in ihrer fr-Spalte — und der Agent haette vier Reihen neu
    gepraegt, die schon stehen.
    """
    global _eigen
    if _eigen is not None:
        return _eigen
    idx = collections.defaultdict(collections.Counter)
    orte = collections.defaultdict(list)
    for nr, kap, v, e in C.iter_corpus():
        if C.is_multi(e):
            continue
        k = norm(e.get('form', ''))
        if not k:
            continue
        key = (e.get('lemma', ''), e.get('level', ''), C.reihe(e))
        idx[k][key] += 1
        if len(orte[(k, key)]) < 3:
            orte[(k, key)].append(f'{C.book_name(nr)} {kap},{v}')
    _eigen = (idx, orte)
    return _eigen


def _eigentext(key, n, wo):
    lemma, lvl, zeile = key
    reihe = ' · '.join(f'{l} *{w}*' for l, w in zip(SPALTEN, zeile) if w)
    return (f'- {n}× · {reihe}   [{lemma}, {lvl}]'
            + (f'   ({", ".join(wo)})' if wo else ''))


# ------------------------------------------------------- italienische Klitika
# Italienisch haengt die unbetonten Pronomen ANS VERB: `dirgli`,
# `vedendolo`, `svegliatosi`, `opponetevi`, `gliene`. Der Rueckwaerts-
# Index kennt solche Formen nicht — die Zeugen glossieren `to tell him`
# als zwei Woerter, nie als eines. Ueber das ganze NT sind das 756
# Tokens in 547 Formen, also gut ein Fuenftel alles Unbelegten; ohne
# diese Schicht faenden die Agenten dort „UNBELEGT — hier ist die
# Arbeit", obwohl Verb und Pronomen beide hundertfach dastehen.
#
# **Kuerze zuerst.** Die erste Fassung ging von der laengsten Form aus,
# damit `glielo` vor `lo` greift — und las `salvateli` als `salva` +
# `teli`, weil `teli` (*Leinentuecher*) im Bestand steht und `salva`
# auch. Richtig ist `salvate` + `li`. Von der kuerzesten aus faellt das
# weg: `li` ergibt sofort den Stamm `salvate`, und die Doppelklitika
# bleiben trotzdem erreichbar, weil ihre kurzen Enden keinen gueltigen
# Stamm liefern (`gliene` → `ne` → `glie` steht nirgends). Gemeldet vom
# Agenten des italienischen Pilotbuchs.
KLITIKA = ['mi', 'ti', 'ci', 'vi', 'si', 'lo', 'la', 'li', 'le', 'ne',
           'gli',
           'melo', 'mela', 'meli', 'mele', 'mene',
           'telo', 'tela', 'teli', 'tele', 'tene',
           'celo', 'cela', 'celi', 'cele', 'cene',
           'velo', 'vela', 'veli', 'vele', 'vene',
           'selo', 'sela', 'seli', 'sele', 'sene',
           'glielo', 'gliela', 'glieli', 'gliele', 'gliene']

# Was beim Anhaengen am Stamm verlorengeht: der Infinitiv wirft sein
# `-e` ab (`portare` + `gli` → `portargli`), sonst bleibt der Stamm.
# Das `e` steht mit Absicht VORNE: `dirgli` findet sonst den apokopierten
# Stamm `dir`, den es im Bestand auch gibt, und zeigt ihn statt `dire`.
STAMMPROBEN = ('e', '', 'i', 'o', 'a')

# Was der Apostroph verschluckt hat. Franzoesisch bleibt das elidierte
# Stueck als eigene Glosse stehen (`qu'`), italienisch nicht: `nell` ist
# keine Wortform, `nella` ist eine.
ELISIONSPROBEN = {'it': ('a', 'o', 'e', 'i', 'he', 'la', 'lo')}


def _klitikon(k, ganz, level):
    """(zeilen, beschreibung) fuer Verb + angehaengtes Pronomen — oder ([], '')."""
    if C.LANG != 'it':
        return [], ''
    for kl in KLITIKA:
        if not k.endswith(kl) or len(k) - len(kl) < 3:
            continue
        stamm = k[:-len(kl)]
        for probe in STAMMPROBEN:
            kand = stamm + probe
            if kand in ganz:
                out = [f'  **{kand}** (Verb)']
                zeigen, _ = _kuerzen(sorted(ganz[kand].items(),
                                            key=lambda x: -x[1]))
                out += ['  ' + _zeilentext(z, level[(kand, z)], n)
                        for z, n in zeigen[:3]]
                if kl in ganz:
                    out.append(f'  **{kl}** (Pronomen)')
                    zg, _ = _kuerzen(sorted(ganz[kl].items(),
                                            key=lambda x: -x[1]))
                    out += ['  ' + _zeilentext(z, level[(kl, z)], n)
                            for z, n in zg[:2]]
                return out, f'{kand} + {kl}'
    return [], ''


def schicht(wort):
    """('BESTAND'|'GLOSSE'|'TEIL'|'KLITIKON'|'ELISION'|None, zeilen)."""
    ganz, teil, level, stellen = index()
    eigen, eigenorte = eigenindex()
    k = norm(wort)
    if not k:
        return None, []
    if k in eigen:
        zeigen, rest = _kuerzen(sorted(eigen[k].items(), key=lambda x: -x[1]))
        out = [_eigentext(key, n, eigenorte.get((k, key)))
               for key, n in zeigen]
        if rest:
            out.append(f'- … und {rest} weitere Lesart(en)')
        return 'BESTAND', out
    if k in ganz:
        zeigen, rest = _kuerzen(sorted(ganz[k].items(), key=lambda x: -x[1]))
        out = [_zeilentext(z, level[(k, z)], n, stellen.get((k, z)))
               for z, n in zeigen]
        if rest:
            out.append(f'- … und {rest} weitere Lesart(en)')
        return 'GLOSSE', out
    if k in teil:
        zeigen, rest = _kuerzen(sorted(teil[k].items(), key=lambda x: -x[1]))
        out = [_zeilentext(z, level[(ganzfr, z)], n,
                           anhang=f'   ← in der Glosse „{ganzfr}"')
               for (z, ganzfr), n in zeigen]
        if rest:
            out.append(f'- … und {rest} weitere')
        return 'TEIL', out
    kl, wie = _klitikon(k, ganz, level)
    if kl:
        return 'KLITIKON', [f'  *{wie}* — die beiden Teile einzeln:'] + kl
    if "'" in k:
        stuecke = [p for p in k.split("'") if p]
        gefunden = []
        for i, p in enumerate(stuecke):
            kand = p
            if kand not in ganz:
                # Italienisch ist das elidierte Stueck selbst keine
                # Wortform: `nell'` steht nirgends, `nella` hundertfach.
                for probe in ELISIONSPROBEN.get(C.LANG, ()):
                    if p + probe in ganz:
                        kand = p + probe
                        break
            if kand not in ganz:
                continue
            zeigen, _ = _kuerzen(sorted(ganz[kand].items(), key=lambda x: -x[1]))
            marke = kand if kand != p else p + ("'" if i < len(stuecke) - 1 else '')
            gefunden.append(f'  **{marke}**')
            gefunden += ['  ' + _zeilentext(z, level[(kand, z)], n)
                         for z, n in zeigen[:3]]
        if gefunden:
            return 'ELISION', gefunden
    return None, []


def versatzprobe(nr, kap, verses):
    """Wo deckt der NACHBARVERS eines Zeugen besser als der eigene?

    Die VERS-Schicht setzt voraus, dass Vers 13 der Zeugen derselbe Vers
    ist. In Matthaeus 23 stimmt das fuer die Zaehlung, aber WEB fuehrt
    die Inhalte von 23,13 und 23,14 **vertauscht** — dieselbe Nummer,
    andere Perikope. `ausgaben.py` und `kapitelgrenzen.py` koennen das
    nicht sehen, weil die Verse sich decken; `verszaehlung.py` auch
    nicht. Gefunden vom Agenten fuer Matthaeus 23, der die kreuzweise
    falschen en-Zeilen beim Lesen bemerkte.

    Geprueft wird **je Zeuge einzeln** — zusammengelegt verschwindet der
    Befund, weil der andere Zeuge richtig steht.
    """
    warnungen = []
    for edition, suffix, _formlang in ZEUGEN:
        p = os.path.join(C.REPO, 'bibles', *edition.split('/'),
                         'anno', f'{nr}{suffix}')
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding='utf-8'))
        proVers = {}
        for v, ee in d['chapters'].get(str(kap), {}).items():
            s = set()
            for e in ee:
                f = norm(e.get(SCHLUESSEL, ''))
                if f:
                    s.add(f)
                    s.update(f.split())
            proVers[str(v)] = s
        for v, txt in verses.items():
            k = [x for x in (norm(t) for t in C.tokens(txt)) if x]
            if len(k) < 8:
                continue
            eigen = sum(1 for x in k if x in proVers.get(str(v), ()))
            for dd in (-1, 1):
                nb = sum(1 for x in k
                         if x in proVers.get(str(int(v) + dd), ()))
                if nb > eigen + max(3, len(k) // 4):
                    warnungen.append(
                        f'{v}: in `{edition}` deckt Vers {int(v)+dd} '
                        f'{nb} Tokens dieses Verses, Vers {v} nur {eigen} '
                        '— dort stehen die Perikopen vertauscht. Die '
                        'VERS-Zeilen dieses Zeugen hier NICHT uebernehmen.')
    return warnungen


def extract(nr, kap, von=None, bis=None):
    verses = C.load_source(nr)['chapters'][str(kap)]
    name = C.book_name(nr)
    vz = verszeilen(nr, kap)

    L = [f'# Rueckwaerts-Lexikon: {name} {kap}'
         + (f',{von}–{bis}' if von else ''), '',
         f'*{C.bestandsstand()}*', '']
    L.append('Was ' + ', '.join(f'`{z[0]}`' for z in ZEUGEN)
             + f' in ihrer **{SCHLUESSEL}-Spalte** zu den '
             'Woertern dieses Abschnitts fuehren.')
    L.append('')
    lernende = {'de': 'Deutsch', 'en': 'Englisch', 'es': 'Spanisch',
                'fr': 'Franzoesisch', 'it': 'Italienisch'}
    fremd = '-, '.join(lernende[z[2]] for z in ZEUGEN[:-1])
    fremd = (fremd + '- oder ' if fremd else '') + lernende[ZEUGEN[-1][2]] \
        if ZEUGEN else '?'
    L.append('**Level und Lemma der Zeugen sind nicht uebertragbar.** Das Level '
             'steht in Klammern mit der Ausgabe, aus der es kommt — es ist CEFR '
             f'fuer {fremd}lernende, nicht fuer {lernende[SCHLUESSEL]}. Das '
             'Lemma steht gar nicht da; es ist im Zeugen '
             + ' oder '.join(lernende[z[2]].lower() for z in ZEUGEN) + '.')
    del fremd
    L.append('')
    if not vz:
        L.append('**Keine Verszeilen** — die Zeugen haben zu diesem Kapitel '
                 'nichts. Es gibt nur den Bestandsteil unten.')
        L.append('')
    else:
        L.append('Die **VERS-Zeilen** stehen im selben Vers der Zeugen. Das gilt '
                 'nur, solange die Verszaehlung uebereinstimmt — vorher '
                 f'`ausgaben.py {nr} {kap}` lesen.')
        L.append('')
        warnungen = versatzprobe(nr, kap, verses)
        if warnungen:
            L.append('## !! Vertauschte Verse in den Zeugen')
            L.append('')
            for w in warnungen:
                L.append(f'- {w}')
            L.append('')

    gesehen, zaehl, offen, schon = {}, collections.Counter(), {}, {}

    for v in sorted(verses, key=int):
        if von is not None and not (von <= int(v) <= bis):
            continue
        toks = [t for t in C.tokens(verses[v]) if not C.is_punct_only(t)]
        L.append(f'## {kap},{v}')
        L.append('')
        L.append(f'> {verses[v]}')
        L.append('')
        im_vers = vz.get(str(v), {})
        for i, tok in enumerate(toks):
            k = norm(tok)
            if not k:
                continue
            zaehl[k] += 1
            treffer = im_vers.get(k)
            if treffer:
                # Gleiche Viererzeile aus beiden Zeugen zusammenziehen
                gebuendelt = collections.OrderedDict()
                for zeile, lvl, zg in treffer:
                    gebuendelt.setdefault(zeile, collections.Counter())[(lvl, zg)] += 1
                zeilen = [_zeilentext(z, lv, 1).replace('- 1× · ', '- ')
                          for z, lv in gebuendelt.items()]
                # Dasselbe Wort mit derselben Zeilenliste nicht wieder
                # ausschreiben. `de` und `et` stehen in Judas je 21× und
                # tragen jedes Mal dieselben vier Zeilen — ausgeschrieben
                # ist der Extrakt dreimal so gross und niemand liest ihn.
                marke = (k, tuple(zeilen))
                if marke in schon:
                    L.append(f'**{i}** `{C.strip_punct(tok)}`   (wie {schon[marke]})')
                    continue
                schon[marke] = f'{kap},{v}'
                L.append(f'**{i}** `{C.strip_punct(tok)}`')
                L += zeilen
            else:
                L.append(f'**{i}** `{C.strip_punct(tok)}`   ← nicht in diesem '
                         'Vers der Zeugen, siehe unten')
                offen[k] = C.strip_punct(tok)
        L.append('')

    # --- Was der Vers nicht hergibt: der Bestand ueber das ganze NT
    if offen:
        L.append('# Nicht im Vers der Zeugen belegt')
        L.append('')
        L.append('Diese Woerter stehen im Vers der Zeugen nicht als '
                 f'{SCHLUESSEL}-Glosse. '
                 'Was der **ganze NT-Bestand** dazu fuehrt, steht hier — das '
                 'ist ein Vorrat an Lesarten, keine Vorgabe. Welche davon hier '
                 'gilt, entscheidet der Vers.')
        L.append('')
        gruppen = collections.defaultdict(list)
        for k, form in offen.items():
            art, zeilen = schicht(form)
            gruppen[art].append((form, zeilen))
            gesehen[k] = art
        # `KLITIKON` hat hier gefehlt, obwohl `schicht()` es liefert und
        # `gruppen` es sammelt. Die betroffenen Woerter trugen im Vers die
        # Marke „siehe unten" und standen unten dann NIRGENDS — in Judas
        # `scrivervi`, `esortarvi`, `salvateli`, ueber das NT rund 800
        # Tokens, die still verschwanden. Gemeldet vom Agenten des
        # italienischen Pilotbuchs. Wer hier eine Schicht ergaenzt, muss
        # sie an BEIDEN Stellen ergaenzen.
        for art, titel in (
                ('BESTAND', 'BESTAND — die Form steht schon annotiert da '
                            '(Lemma und Level sind gesetzt)'),
                ('GLOSSE', 'GLOSSE — das Wort steht anderswo im Bestand'),
                ('TEIL', 'TEIL — nur innerhalb einer mehrwortigen Glosse'),
                ('KLITIKON', 'KLITIKON — Verb und angehaengtes Pronomen sind '
                             'einzeln belegt'),
                ('ELISION', 'ELISION — nur die Haelften sind belegt'),
                (None, 'UNBELEGT — hier ist die Arbeit')):
            if art not in gruppen:
                continue
            L.append(f'## {titel} ({len(gruppen[art])})')
            L.append('')
            for form, zeilen in sorted(gruppen[art], key=lambda x: x[0].lower()):
                n = zaehl[norm(form)]
                L.append(f'### {form}' + (f'  ({n}× im Abschnitt)' if n > 1 else ''))
                L += zeilen if zeilen else ['- kein Beleg']
                L.append('')

    tot = sum(zaehl.values())
    imvers = tot - sum(zaehl[k] for k in offen)
    unbelegt = sum(zaehl[k] for k, a in gesehen.items() if a is None)
    L[1] = (f'{tot} Tokens · {imvers} im Vers der Zeugen belegt '
            f'({imvers / tot:.0%}) · {tot - imvers - unbelegt} ueber den '
            f'uebrigen Bestand · {unbelegt} unbelegt')
    return '\n'.join(L)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('buch', type=int, nargs='?')
    p.add_argument('kapitel', type=int, nargs='?')
    p.add_argument('von', type=int, nargs='?')
    p.add_argument('bis', type=int, nargs='?')
    p.add_argument('--wort', nargs='+')
    p.add_argument('-o', '--out')
    a = p.parse_args()
    if a.wort:
        for w in a.wort:
            art, zeilen = schicht(w)
            print(f'## {w}   [{art or "UNBELEGT"}]')
            print('\n'.join(zeilen) if zeilen else '- kein Beleg')
            print()
        sys.exit(0)
    if a.buch is None or a.kapitel is None:
        p.error('buch und kapitel fehlen (oder --wort benutzen)')
    txt = extract(a.buch, a.kapitel, a.von, a.bis)
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(txt)
        print(f'{a.out} geschrieben ({len(txt)} Zeichen)')
    else:
        sys.stdout.write(txt)
