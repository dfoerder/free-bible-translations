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
import sys

import common as C

MIN_STAMM = 4  # 5 war zu lang: 'beugt' fand 'beugen' nicht (5Mo 27,19)


def _gemeinsam(a, b):
    """Länge des gemeinsamen Präfixes, ohne Rücksicht auf Groß-/Kleinschreibung."""
    a, b = a.lower(), b.lower()
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
    """
    if len(form) < MIN_STAMM:
        return []
    kand = stamm.get(form[:MIN_STAMM].lower(), set())
    gross = form[:1].isupper()
    return sorted(kand, key=lambda x: (-_gemeinsam(form, x),
                                       0 if x[:1].isupper() == gross else 1,
                                       abs(len(x) - len(form)), x))[:wieviel]

FUNKTION = {'der', 'die', 'das', 'den', 'dem', 'des', 'und', 'oder', 'ein', 'eine',
            'einen', 'einem', 'eines', 'einer', 'zu', 'in', 'an', 'auf', 'mit',
            'von', 'für', 'ist', 'sind', 'war', 'waren', 'nicht', 'er', 'sie',
            'es', 'ich', 'du', 'wir', 'ihr', 'sich', 'als', 'wie', 'so', 'auch',
            'aber', 'dann', 'da', 'wenn', 'dass', 'im', 'am', 'zum', 'zur', 'aus',
            'bei', 'nach', 'über', 'vor', 'um', 'noch', 'nur', 'schon', 'sein',
            'seine', 'seinen', 'seinem', 'seiner', 'ihre', 'ihren', 'ihrem', 'ihm',
            'ihn', 'ihnen', 'euch', 'uns', 'mich', 'dich', 'mir', 'dir', 'wer',
            'was', 'alle', 'alles', 'allen', 'aller', 'man', 'hat', 'habe',
            'haben', 'hatte', 'hatten', 'wird', 'werden', 'wurde', 'wurden',
            'soll', 'sollen', 'kann', 'können', 'will', 'wollen'}


def analyse(nr, kap=None):
    src = C.load_source(nr)
    kapitel = [str(kap)] if kap else sorted(src['chapters'], key=int)

    form_lesarten = collections.defaultdict(collections.Counter)
    lemma_formen = collections.defaultdict(set)
    for _, _, _, e in C.iter_corpus():
        if C.is_multi(e):
            continue
        form_lesarten[e['form']][(e['lemma'], e['en'], e['es'], e['fr'], e['it'])] += 1
        lemma_formen[e['lemma']].add(e['form'])

    stamm = collections.defaultdict(set)
    for lemma in lemma_formen:
        if len(lemma) >= 5:
            stamm[lemma[:MIN_STAMM].lower()].add(lemma)

    # Mehrheitsglosse je Form (für die Kollisionsprüfung)
    haupt = {}
    for f, c in form_lesarten.items():
        (lemma, en, es, fr, it), _ = c.most_common(1)[0]
        haupt[f] = (lemma, en, es, fr, it)

    unbelegt, kollisionen, mehrdeutig = {}, [], {}
    for k in kapitel:
        for v, txt in src['chapters'][k].items():
            formen = [C.strip_punct(t) for t in C.tokens(txt)]
            formen = [f for f in formen if f]

            for f in formen:
                if f not in form_lesarten and f not in unbelegt:
                    verwandt = _verwandt(f, stamm)
                    unbelegt[f] = (f'{k},{v}', verwandt)
                elif f in form_lesarten and f not in mehrdeutig and f.lower() not in FUNKTION:
                    lesarten = {(lm, en) for (lm, en, _, _, _) in form_lesarten[f]}
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
                    lemma, en, es, fr, it = haupt[f]
                    for lang, g in zip(C.LANGS, (en, es, fr, it)):
                        nach_glosse[(lang, g.lower())].add((f, lemma))
            for (lang, g), paare in nach_glosse.items():
                if len({lm for _, lm in paare}) > 1:
                    kollisionen.append((f'{k},{v}', lang, g, sorted(paare)))

    return unbelegt, kollisionen, mehrdeutig


def bericht(nr, kap=None):
    src = C.load_source(nr)
    unbelegt, kollisionen, mehrdeutig = analyse(nr, kap)
    L = [f'# Hinweise aus dem Quelltext: {src["name"]}'
         + (f' {kap}' if kap else '') , '']

    L.append(f'## Noch nicht belegte Wortformen ({len(unbelegt)})')
    L.append('')
    L.append('**Formbasiert** — das Lemma kann über eine andere Form längst im '
             'Bestand stehen. Wo eine stammverwandte Form existiert, steht sie '
             'dabei; dann erst `lexicon.py` fragen, bevor etwas Neues erfunden wird.')
    L.append('')
    for f, (wo, verwandt) in sorted(unbelegt.items()):
        z = f'- **{f}** ({wo})'
        if verwandt:
            z += '  — verwandt: ' + ', '.join(f'`{x}`' for x in verwandt)
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

    L.append(f'## Mehrdeutige Formen im Bestand ({len(mehrdeutig)})')
    L.append('')
    for f, (wo, lesarten) in sorted(mehrdeutig.items()):
        L.append(f'- **{f}** ({wo}): ' + ' · '.join(f'`{lm}` = *{en}*' for lm, en in lesarten))
    return '\n'.join(L)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    nr = int(sys.argv[1])
    kap = int(sys.argv[2]) if len(sys.argv) > 2 else None
    print(bericht(nr, kap))
