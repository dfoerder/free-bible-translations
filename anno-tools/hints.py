"""Prompt-Hinweise aus dem **Quelltext** statt aus Bibelkenntnis.

    hints.py <buchNr> [<kapitel>]

Drei Abschnitte:

1. **Noch nicht belegte Wortformen** — was der Bestand nirgends kennt.
   **Achtung, formbasiert**: das Lemma kann über eine andere Form längst im
   Bestand stehen. Sieben Agenten sind darauf hereingefallen, bis der Hinweis
   im Prompt stand. Deshalb steht daneben, ob es eine stammverwandte Form gibt.

2. **Kollisionen** — zwei verschiedene Wörter, die im selben Vers stehen und
   im Bestand dieselbe Glosse tragen. Im Lesefluss wären sie nicht zu
   unterscheiden. Die Prüfung läuft über **exakte Wortformen**, nicht über
   Präfixe: die Präfixfassung schlug mit `Heil` in `Heiligung` an und erfand
   eine Kollision, die es nicht gab.

3. **Mehrdeutige Formen** — im Bestand mit mehreren Lesarten belegt, die sich
   nicht nur in Person/Numerus/Tempus unterscheiden.

Jeder Hinweis ist eine **Hypothese**, auch wenn ein Skript ihn erzeugt hat.
Der Quelltext hat immer recht.
"""
import collections
import re
import sys

import common as C

MIN_STAMM = 4  # 5 war zu lang: 'beugt' fand 'beugen' nicht (5Mo 27,19)


UMLAUT = str.maketrans({'ä': 'a', 'ö': 'o', 'ü': 'u', 'ß': 's'})


def _stammkey(wort):
    """Stammschluessel ohne Umlaut.

    Der deutsche Plural umlautet: `Wald` -> `Waelder`, `Haus` -> `Haeuser`,
    `Buch` -> `Buecher`, `Vater` -> `Vaeter`. Der Schluessel aus den ersten
    vier Zeichen trennt diese Paare, und damit meldete das Werkzeug die Form
    als unbelegt **ohne** ihr Lemma anzubieten — genau der Fehler, gegen den
    der VERWANDT-Abschnitt gebaut ist.

    Gefunden hat es der Agent der Psalmen 27-29: `Waelder` in 29,9 galt als
    unbelegt, waehrend `Wald` mit 13 Belegen im Bestand steht. Dasselbe gilt
    fuer jeden umlautenden Plural und fuer den Konjunktiv (`wuerde` gegen
    `wurde`, `haette` gegen `hatte`).
    """
    return C.ohne_akzent(wort[:MIN_STAMM].lower().translate(UMLAUT))


# Eine vorangestellte Elision (`l’affection`, `d’abord`, `qu’il`) klebt am
# Wortanfang und verdirbt damit den Stammschluessel, der aus den ERSTEN vier
# Zeichen gebildet wird: `l’af…` landet in einem anderen Eimer als `affection`.
# Gefunden hat es der Agent fuer Roemer 8: dort standen `l’affection`,
# `l’image`, `l’adoption`, `l’espérer`, `l’attendons` und `l’enfantement` als
# unbelegt und ganz ohne „verwandt"-Zeile da, obwohl `affection`, `image`,
# `adoption`, `espérer` und `attendre` mit zusammen ueber vierzig Belegen im
# Bestand stehen — die nicht-elidierte Form desselben Kapitels (`espérons`)
# bekam ihre Zeile korrekt. Im Franzoesischen trifft das jedes vierte Nomen,
# und es kostete dort beinahe ein falsches Level.
#
# Gesucht wird deshalb in BEIDEN Eimern. Abgezogen wird nichts: `d’abord` ist
# ein eigenes Lemma des Bestands und muss seinen eigenen Eimer behalten.
ELISION = re.compile(r"^[^\W\d_]{1,6}[’']")


def _ohne_elision(wort):
    """Das Wort ohne vorangestellte Elision, oder unveraendert."""
    rest = ELISION.sub('', wort)
    return rest or wort


def _gemeinsam(a, b):
    """Länge des gemeinsamen Präfixes, ohne Rücksicht auf Groß-/Kleinschreibung."""
    a = C.ohne_akzent(a.lower().translate(UMLAUT))
    b = C.ohne_akzent(b.lower().translate(UMLAUT))
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return n


def _verwandt(form, stamm, wieviel=3):
    """Die stammverwandten Lemmata zu einer unbelegten Wortform.

    **Sortiert nach dem längsten gemeinsamen Präfix**, nicht alphabetisch. Die
    alphabetische Fassung war der teuerste Werkzeugfehler des Buches Hiob: sie
    schnitt nach drei Einträgen ab, und weil Großbuchstaben vor Kleinbuchstaben
    sortieren, standen dort die substantivischen Nachbarn statt des gesuchten
    Verbs. `verlierst` bekam `Verlangen`, `Verlauf`, `Verleumder` angeboten,
    während `verlieren` mit 14 Belegen im selben Eimer lag und nur wegen der
    Sortierung nicht angezeigt wurde. In Hiob 4 waren so **zehn von siebzehn**
    als unbelegt gemeldeten Formen in Wahrheit über ihr Lemma gebunden, in
    Hiob 1 drei von zwölf, in Hiob 3 drei.

    Zweites Kriterium ist die **Groß-/Kleinschreibung**: bei gleich langem
    Präfix gehört zu einer kleingeschriebenen Form das kleingeschriebene
    Lemma. Ohne das gewann `Traum` gegen `trauen` und `Vernunft` gegen
    `vernehmen` — beide über die Länge, beide falsch.

    Gewichtet wird nicht das gemeinsame Präfix allein, sondern **das Präfix
    abzüglich dessen, was am Kandidaten übrig bleibt** (`2·gemeinsam − Länge`).
    Zwei frühere Fassungen sind an den Komposita gescheitert: `Länder` bekam
    `Landesgott`, `Landesteil`, `Landesfürst` angeboten und `Land` fiel aus
    den ersten drei heraus, `Bäume` bekam `Baumeister` statt `Baum`. Beide
    gewinnen über das Präfix, weil die Umlautnormalisierung `Länder` zu
    `lander` macht und damit ein Zeichen mehr mit `Landes…` teilt als mit
    `Land`. Wer zusätzlich zählt, was am Kandidaten hängen bleibt, dreht das
    Verhältnis um: `Land` behält 0 übrig, `Landesgott` fünf.
    """
    ohne = _ohne_elision(form)
    if len(form) < MIN_STAMM and len(ohne) < MIN_STAMM:
        return []
    kand = set(stamm.get(_stammkey(form), ()))
    if ohne != form:
        kand |= set(stamm.get(_stammkey(ohne), ()))
    gross = ohne[:1].isupper()

    def naehe(x):
        return max(_gemeinsam(form, x), _gemeinsam(ohne, x))

    return sorted(kand, key=lambda x: (-(2 * naehe(x) - len(x)),
                                       0 if x[:1].isupper() == gross else 1,
                                       len(x), x))[:wieviel]

# Funktionswoerter des QUELLTEXTES. Sie werden aus den Meldungen
# herausgehalten — bei ihnen ist die Mehrdeutigkeit der Normalfall und
# keine Warnung wert. Welche Liste gilt, haengt an der Ausgabe.
FUNKTION_JE_SPRACHE = {
    'de': {'der', 'die', 'das', 'den', 'dem', 'des', 'und', 'oder', 'ein', 'eine',
           'einen', 'einem', 'eines', 'einer', 'zu', 'in', 'an', 'auf', 'mit',
           'von', 'für', 'ist', 'sind', 'war', 'waren', 'nicht', 'er', 'sie',
           'es', 'ich', 'du', 'wir', 'ihr', 'sich', 'als', 'wie', 'so', 'auch',
           'aber', 'dann', 'da', 'wenn', 'dass', 'im', 'am', 'zum', 'zur', 'aus',
           'bei', 'nach', 'über', 'vor', 'um', 'noch', 'nur', 'schon', 'sein',
           'seine', 'seinen', 'seinem', 'seiner', 'ihre', 'ihren', 'ihrem', 'ihm',
           'ihn', 'ihnen', 'euch', 'uns', 'mich', 'dich', 'mir', 'dir', 'wer',
           'was', 'alle', 'alles', 'allen', 'aller', 'man', 'hat', 'habe',
           'haben', 'hatte', 'hatten', 'wird', 'werden', 'wurde', 'wurden',
           'soll', 'sollen', 'kann', 'können', 'will', 'wollen'},
    'fr': {'le', 'la', 'les', "l'", 'un', 'une', 'des', 'du', 'de', "d'",
           'et', 'ou', 'mais', 'donc', 'car', 'ni', 'à', 'au', 'aux', 'en',
           'dans', 'sur', 'sous', 'pour', 'par', 'avec', 'sans', 'ce', 'cet',
           'cette', 'ces', 'qui', 'que', "qu'", 'quoi', 'dont', 'où', 'ne',
           'pas', 'plus', 'est', 'sont', 'était', 'étaient', 'sera', 'seront',
           'a', 'ont', 'avait', 'avaient', 'il', 'elle', 'ils', 'elles', 'je',
           'tu', 'nous', 'vous', 'on', 'se', "s'", 'me', 'te', 'lui', 'leur',
           'leurs', 'y', 'son', 'sa', 'ses', 'mon', 'ma', 'mes', 'ton', 'ta',
           'tes', 'notre', 'nos', 'votre', 'vos', 'comme', 'aussi', 'ainsi',
           'alors', 'quand', 'si', 'tout', 'tous', 'toute', 'toutes',
           'être', 'avoir', 'fait', 'faire', 'peut', 'doit'},
    'en': {'the', 'a', 'an', 'and', 'or', 'but', 'of', 'to', 'in', 'on', 'at',
           'by', 'for', 'with', 'from', 'is', 'are', 'was', 'were', 'be',
           'been', 'has', 'have', 'had', 'will', 'shall', 'that', 'which',
           'who', 'whom', 'not', 'he', 'she', 'it', 'they', 'i', 'you', 'we',
           'his', 'her', 'its', 'their', 'my', 'your', 'our', 'as', 'so',
           'then', 'when', 'if', 'all', 'also'},
    'es': {'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'de', 'del',
           'y', 'o', 'pero', 'a', 'al', 'en', 'con', 'sin', 'por', 'para',
           'que', 'quien', 'no', 'es', 'son', 'era', 'eran', 'ha', 'han',
           'se', 'su', 'sus', 'mi', 'mis', 'tu', 'tus', 'él', 'ella', 'ellos',
           'yo', 'tú', 'nosotros', 'vosotros', 'como', 'así', 'cuando', 'si',
           'todo', 'todos', 'toda', 'todas'},
    'it': {'il', 'lo', 'la', 'i', 'gli', 'le', "l'", 'un', 'uno', 'una',
           "un'", 'di', "d'", 'del', 'dello', 'della', 'dei', 'degli',
           'delle', 'a', 'ad', 'al', 'allo', 'alla', 'ai', 'agli', 'alle',
           'da', 'dal', 'dallo', 'dalla', 'dai', 'dagli', 'dalle', 'in',
           'nel', 'nello', 'nella', 'nei', 'negli', 'nelle', 'con', 'col',
           'su', 'sul', 'sulla', 'sui', 'sulle', 'per', 'tra', 'fra',
           'e', 'ed', 'o', 'ma', 'però', 'dunque', 'perché',
           'che', 'chi', 'cui', 'quale', 'quali', 'non', 'né',
           'è', 'sono', 'era', 'erano', 'sarà', 'saranno',
           'ha', 'hanno', 'aveva', 'avevano', 'io', 'tu', 'egli', 'ella',
           'noi', 'voi', 'essi', 'esse', 'lui', 'lei', 'loro', 'si',
           'mi', 'ti', 'ci', 'vi', 'ne', 'lo', 'gli', 'suo', 'sua',
           'suoi', 'sue', 'mio', 'mia', 'miei', 'mie', 'tuo', 'tua',
           'nostro', 'nostra', 'vostro', 'vostra', 'come', 'anche',
           'così', 'allora', 'quando', 'se', 'tutto', 'tutti',
           'tutta', 'tutte', 'essere', 'avere', 'fare', 'può',
           'deve'},
}
FUNKTION = FUNKTION_JE_SPRACHE.get(C.LANG, set())


def analyse(nr, kap=None):
    src = C.load_source(nr)
    kapitel = [str(kap)] if kap else sorted(src['chapters'], key=int)

    form_lesarten = collections.defaultdict(collections.Counter)
    lemma_formen = collections.defaultdict(set)
    for _, _, _, e in C.iter_corpus():
        if C.is_multi(e):
            continue
        form_lesarten[e['form']][(e['lemma'],) + C.reihe(e)] += 1
        lemma_formen[e['lemma']].add(e['form'])

    stamm = collections.defaultdict(set)
    for lemma in lemma_formen:
        if len(lemma) >= 5:
            stamm[_stammkey(lemma)].add(lemma)

    # Mehrheitsglosse je Form (für die Kollisionsprüfung)
    haupt = {}
    for f, c in form_lesarten.items():
        key, _ = c.most_common(1)[0]
        haupt[f] = key

    # Gross-/Kleinschreibung: `form_lesarten` ist schreibungsgenau
    # indexiert, und substantivierte Adjektive wechseln staendig die
    # Schreibung. In Sacharja 11 galten `Prächtigen`, `elenden` und
    # `Gesunde` als unbelegt, obwohl `prächtigen` (15×), `Elenden` (21×)
    # und `gesunde` im Bestand stehen. Solche Formen gehoeren nicht in
    # die Unbelegt-Liste, sondern in eine eigene Zeile.
    schreibvariante = {}
    unbelegt, kollisionen, mehrdeutig = {}, [], {}
    for k in kapitel:
        for v, txt in src['chapters'][k].items():
            formen = [C.strip_punct(t) for t in C.tokens(txt)]
            formen = [f for f in formen if f]

            for f in formen:
                if f not in form_lesarten and f not in unbelegt \
                        and f not in schreibvariante:
                    andere = next((g for g in (f.lower(), f.capitalize(),
                                               f.upper())
                                   if g != f and g in form_lesarten), None)
                    if andere:
                        schreibvariante[f] = (f'{k},{v}', andere,
                                              haupt[andere][0])
                        continue
                    verwandt = _verwandt(f, stamm)
                    unbelegt[f] = (f'{k},{v}', verwandt)
                elif f in form_lesarten and f not in mehrdeutig and f.lower() not in FUNKTION:
                    # k[0] ist das Lemma, k[1] die erste Glossenspalte —
                    # welche das ist, haengt an LANGS und nicht mehr an 'en'.
                    lesarten = {(k[0], k[1]) for k in form_lesarten[f]}
                    if len({lm for lm, _ in lesarten}) > 1 or len(lesarten) > 3:
                        # Erst je Lemma eine Lesart, dann auffuellen: sonst
                        # schneidet der Deckel ein ganzes Lemma weg
                        # (`gehoert` zeigte nur `gehoeren`, nie `hoeren`).
                        gewaehlt, gesehen = [], set()
                        for lm, en in sorted(lesarten):      # je Lemma eine
                            if lm not in gesehen:
                                gesehen.add(lm)
                                gewaehlt.append((lm, en))
                        for eintrag in sorted(lesarten):     # dann auffuellen
                            if eintrag not in gewaehlt and len(gewaehlt) < 5:
                                gewaehlt.append(eintrag)
                        mehrdeutig[f] = (f'{k},{v}', sorted(gewaehlt))

            # Kollisionen im Vers
            nach_glosse = collections.defaultdict(set)
            for f in set(formen):
                if f in haupt and f.lower() not in FUNKTION:
                    lemma, glossen = haupt[f][0], haupt[f][1:]
                    for lang, g in zip(C.LANGS, glossen):
                        nach_glosse[(lang, g.lower())].add((f, lemma))
            for (lang, g), paare in nach_glosse.items():
                if len({lm for _, lm in paare}) > 1:
                    kollisionen.append((f'{k},{v}', lang, g, sorted(paare)))

    return unbelegt, kollisionen, mehrdeutig, schreibvariante


def kompositum_im_vers(nr, kap=None):
    """Unbelegtes Kompositum neben einem belegten Wort, das darin steckt.

    Der Anlass: Haggai 2,12 traegt `Gewandzipfel` (im Bestand gar nicht
    belegt) und `Zipfel` (5 Belege, fest gebunden auf *skirt · orla ·
    pan · lembo*) im **selben Vers**. `hints.py` meldete dort **0
    Kollisionen** — und konnte gar nicht anders: die Kollisionsprobe
    vergleicht die Glossen des Bestands, und ein unbelegtes Wort hat
    keine. Der Agent hat es selbst gesehen und beide auseinandergehalten.

    Diese Probe braucht keine Glossen. Sie meldet, wo ein unbelegtes
    Wort ein belegtes als Bestandteil enthaelt und beide im selben Vers
    stehen — dann ist die Gefahr gross, dass die neu gepraegte Reihe
    genau die des Bestandteils wird.
    """
    src = C.load_source(nr)
    ch = src['chapters'] if 'chapters' in src else src
    # Das eigene Buch zaehlt NICHT zum Bestand. Ist es schon einmal
    # gebaut worden, weist es sonst seine eigenen neuen Woerter als
    # belegt aus und die Probe meldet nichts — genau der Fall, den
    # paketcheck.py fuer die Lemmata beschreibt.
    belegt = {C.strip_punct(e['form']).lower()
              for b, _, _, e in C.iter_corpus() if int(b) != int(nr)}
    out = []
    for k, vv in ch.items():
        if kap is not None and int(k) != int(kap):
            continue
        for v, txt in vv.items():
            formen = [C.strip_punct(x) for x in txt.split()]
            formen = [f for f in formen if f]
            klein = {f.lower(): f for f in formen}
            frei = [f for f in klein if f not in belegt and len(f) > 6]
            for f in frei:
                for g in klein:
                    if g == f or len(g) < 4 or g not in belegt:
                        continue
                    if g not in f:
                        continue
                    # Im Franzoesischen haengt an jedem invertierten Verb
                    # ein Klitikon (`Êtes-vous`, `raisonnez-vous`,
                    # `dit-il`) und an jeder Elision ein Artikel
                    # (`l’homme`). Das ist immer Fall (3) der Anleitung
                    # unten — Zufall der Zeichenkette — und nie eine
                    # Bindungsgefahr. Ohne diesen Filter rauscht die
                    # Probe in jedem franzoesischen Kapitel.
                    i = f.index(g)
                    if i and f[i - 1] in '-\u2019\'':
                        continue
                    out.append((f'{k},{v}', klein[f], klein[g]))
    return out


def bericht(nr, kap=None):
    src = C.load_source(nr)
    unbelegt, kollisionen, mehrdeutig, schreibvariante = analyse(nr, kap)
    L = [f'# Hinweise aus dem Quelltext: {src["name"]}'
         + (f' {kap}' if kap else '') , '']

    L.append(f'## Noch nicht belegte Wortformen ({len(unbelegt)})')
    L.append('')
    L.append('**Formbasiert** — das Lemma kann über eine andere Form längst im '
             'Bestand stehen. Wo eine stammverwandte Form existiert, steht sie '
             'dabei; dann erst `fixgloss.py show <lemma>` fragen, bevor etwas '
             'Neues erfunden wird.')
    L.append('')
    # Zu jedem stammverwandten Wort die LEMMA-Belegzahl. Ohne sie liest
    # sich die Liste als „das Wort gibt es nicht", und genau so ist sie
    # in jedes Paket-Prompt gewandert: in Sacharja 9 waren sieben der
    # zwoelf gemeldeten Formen laengst im Bestand, `wecken` mit 24
    # Belegen. Die Zahl daneben macht den Unterschied sofort sichtbar.
    lemmazahl = collections.Counter()
    lemmalevel = {}
    for b, _, _, e in C.iter_corpus():
        if int(b) == int(nr):
            continue
        lemmazahl[e['lemma']] += 1
        lemmalevel.setdefault(e['lemma'], e['level'])
    for f, (wo, verwandt) in sorted(unbelegt.items()):
        z = f'- **{f}** ({wo})'
        if verwandt:
            teile = []
            for x in verwandt:
                n = lemmazahl.get(x, 0)
                teile.append(f'`{x}`' + (f' ({n} Belege, {lemmalevel[x]})'
                                         if n else ''))
            z += '  — verwandt: ' + ', '.join(teile)
        L.append(z)
    L.append('')

    # Kollisionen zusammenfassen: dasselbe Paar mehrfach → einmal mit Zählung
    zus = collections.defaultdict(list)
    for wo, lang, g, paare in kollisionen:
        zus[tuple(sorted(lm for _, lm in paare))].append((wo, lang, g))
    L.append(f'## Kollisionen im selben Vers ({len(zus)} Paare)')
    L.append('')
    L.append('Zwei Wörter, die im Bestand dieselbe Glosse tragen und hier '
             'zusammenstehen. **Nur wo sie tatsächlich in einem Vers stehen** '
             'wird aufgelöst — eine Auflösung ohne Kollisionsstelle macht den '
             'Bestand nur inkonsistent. Vor jedem Zug die Belegverse lesen.')
    L.append('')
    for lemmata, stellen in sorted(zus.items(), key=lambda x: -len(x[1])):
        orte = ', '.join(f'{wo} ({lang} *{g}*)' for wo, lang, g in stellen[:4])
        mehr = f' … +{len(stellen)-4}' if len(stellen) > 4 else ''
        L.append(f'- `{"` ↔ `".join(lemmata)}` — {orte}{mehr}')
    L.append('')

    if schreibvariante:
        L.append(f'## Nur die Schreibung ist neu ({len(schreibvariante)})')
        L.append('')
        L.append('Diese Formen stehen im Bestand, nur mit anderer Gross- '
                 'oder Kleinschreibung — meist substantivierte Adjektive. '
                 'Meist ist die Reihe der belegten Form die richtige und '
                 'nichts neu zu praegen.')
        L.append('')
        L.append('**Aber pruef die Wortart.** Die Schreibung wechselt im '
                 'Deutschen auch zwischen Verb und Substantiv: `wogen` ist '
                 'in Sacharja 11,12 das Verb *wiegen*, waehrend der Bestand '
                 '`Wogen` als Substantiv `Woge` (*billows*) fuehrt. Wer '
                 'hier blind uebernimmt, setzt „Wellen" in den '
                 'Silberstueck-Vers.')
        L.append('')
        for f, (wo, andere, lemma) in sorted(schreibvariante.items()):
            L.append(f'- **{f}** ({wo}) — belegt als `{andere}`, '
                     f'Lemma `{lemma}`')
        L.append('')

    komp = kompositum_im_vers(nr, kap)
    L.append(f'## Unbelegtes Wort neben belegtem Bestandteil ({len(komp)})')
    L.append('')
    L.append('Ein Wort, das der Bestand **nicht** kennt, steht im selben Vers '
             'wie ein Wort, das darin steckt und fest gebunden ist. Die '
             'Kollisionsprobe oben sieht das nicht — sie vergleicht '
             'Bestandsglossen, und das neue Wort hat keine. '
             'Anlass: Haggai 2,12 `Gewandzipfel` neben `Zipfel`.')
    L.append('')
    L.append('**Erst pruefen, was der Fall ist — es gibt drei.** (1) Zwei '
             'verschiedene Woerter: dann praeg die Reihe des neuen so, dass '
             'sie **nicht** mit der des Bestandteils zusammenfaellt '
             '(`Gewandzipfel` gegen `Zipfel`). (2) **Die getrennte '
             'Satzklammer desselben Verbs**: „Wer euch **antastet**, der '
             '**tastet** seinen Augapfel **an**" — hier ist `tastet … an` '
             'dasselbe Verb wie `antastet`, und beide tragen dieselbe '
             'Glosse; der Bestand macht es in Hiob 1,11 und 2,5 genau so. '
             '(3) Ein Zufall der Zeichenkette (`Verherrlichung` enthaelt '
             '`HERR`). Nur der erste Fall verlangt eine Auflösung.')
    L.append('')
    for wo, lang_wort, kurz in komp:
        L.append(f'- **{lang_wort}** ({wo}) enthaelt `{kurz}` — im Bestand gebunden')
    L.append('')

    L.append(f'## Mehrdeutige Formen im Bestand ({len(mehrdeutig)})')
    L.append('')
    for f, (wo, lesarten) in sorted(mehrdeutig.items()):
        L.append(f'- **{f}** ({wo}): '
                 + ' · '.join(f'`{lm}` = *{g}*' for lm, g in lesarten))
    return '\n'.join(L)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    nr = int(sys.argv[1])
    kap = int(sys.argv[2]) if len(sys.argv) > 2 else None
    print(bericht(nr, kap))
