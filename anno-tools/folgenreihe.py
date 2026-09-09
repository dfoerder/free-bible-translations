#!/usr/bin/env python3
"""Wie glossiert der Bestand eine WORTFOLGE? Vollstaendig, nie abgeschnitten.

    folgenreihe.py "So spricht der HERR" ["naechste Folge" ...]
    folgenreihe.py --buch <nr> "Folge"      nur die Buecher 1..nr-1 als Bestand

## Der Anlass

Fuer den Haggai-Prompt habe ich „So spricht der HERR" im Bestand gemessen,
mir die **zwei haeufigsten** von sechs Varianten ausgeben lassen und in den
Prompt geschrieben: „184 Vorkommen, alle mit `parle`". Der Agent hat
nachgemessen: **229 Vorkommen, vier davon mit `dit`**. Die Regel stimmte,
die Behauptung „alle" nicht.

Derselbe Fehler wie in Jona, wo ich ein Verszitat bei 95 Zeichen
abgeschnitten und aus dem Rest einen Befund abgeleitet hatte: **nie aus
einer abgeschnittenen Liste auf Vollstaendigkeit schliessen.**

Dieses Werkzeug schneidet nichts ab. Es zeigt jede Variante mit ihrer
Zahl und, wo es mehr als eine gibt, die Belegstellen der seltenen.

## Was es zaehlt

Jedes Vorkommen der Wortfolge im Quelltext eines Buches, das eine
Anno-Datei hat, mit den Glossen der **Einzeleintraege** an diesen
Positionen. Steht an einer Position kein Einzeleintrag (weil dort nur ein
Mehrwort liegt), faellt das Vorkommen als `(unvollstaendig)` heraus und
wird eigens gezaehlt — sonst waere die Gesamtzahl stillschweigend zu
klein, und genau daran ist die Haggai-Messung gescheitert.
"""
import sys, collections
import common as C


def _apo(x):
    """Beide Apostrophe auf EINE Form — den geraden.

    Diese Funktion normalisierte urspruenglich auf den TYPOGRAFISCHEN
    Apostroph, weil `lsg1910mod` ihn schreibt. `riv1927mod` schreibt den
    geraden, und damit lief die Normalisierung im Italienischen in die
    falsche Richtung: `folgenreihe.py "il Figlio dell'uomo"` meldete
    **0 Vorkommen**, von Hand sind es NEUN mit einstimmiger Reihe. Und
    weil nur die Anfrage normalisiert wurde, fand auch die typografische
    Eingabe nichts — beide Schreibungen fielen aus.

    Das trifft alle 2117 elidierten Tokens des italienischen NT in 580
    Formen, und es trifft das Werkzeug, mit dem die Agenten
    Zeichengleichheit messen: wer hier eine Null liest, praegt eine Reihe
    neu, die einstimmig dasteht. Gemeldet vom Agenten fuer Matteo 16 —
    derselbe Fehler wie in `belegt.py` (Reihe 118), an der dritten
    Stelle.

    Deshalb wird jetzt auf **beiden** Seiten normalisiert: Anfrage,
    Quelltext und Mehrwortlemma.
    """
    return (x or '').replace('\u2019', "'")


def _norm_akz(w):
    """Akzente weg und `œ`/`æ` aufgeloest — nur zum VERGLEICHEN.

    Akzente sind im Franzoesischen bedeutungstragend (`a`/`à`,
    `ou`/`où`), also wird hier nichts zusammengefasst; die Funktion
    dient allein dem Hinweis „du hast X gefragt, im Text steht Y".
    Die Ligatur gehoert dazu: `de l'oeuvre` fand 0, `de l’œuvre`
    den Beleg — dieselbe Falle, die `belegt.py` fuer den Apostroph
    laengst abfaengt. Gemeldet vom Agenten fuer Epheser 4.
    """
    w = w.replace('œ', 'oe').replace('Œ', 'OE')
    w = w.replace('æ', 'ae').replace('Æ', 'AE')
    return C.ohne_akzent(w)


def stellen(phr, bis=None):
    # Der gerade Apostroph muss treffen wie der typografische: die
    # Vorbereitungsdateien und jede von Hand getippte Folge benutzen ihn.
    # Vorher fand `n'est pas` nichts und `n’est pas` alles — der Agent
    # fuer Matthaeus 18 hat einen Durchgang daran verloren.
    phr = _apo(phr)
    # Die Randzeichen kommen aus `common.PUNCT`, nicht aus einer eigenen
    # Liste. Die eigene fuehrte `.,;:!?„“"` und kannte weder die
    # franzoesischen noch die italienischen Anfuehrungszeichen: eine
    # Folge am VERSENDE stand im Quelltext als `vicino».` da und wurde
    # nie gefunden. `folgenreihe.py "il regno dei cieli è vicino"`
    # meldete 0, obwohl Matteo 3,2 genau so lautet — ohne das letzte
    # Wort fand es die Reihe sofort. Gemeldet vom Agenten fuer Matteo 4.
    w = [C.strip_punct(x) for x in phr.split()]
    w = [x for x in w if x]
    # Eine Folge aus einer Bindungsdatei steht ohne Apostroph da
    # (`C est pourquoi`), der Quelltext hat ein Token (`C’est`). Ohne
    # diese Zeile meldet das Werkzeug „unbelegt", wo der Bestand
    # einstimmig ist.
    if not any("'" in x for x in w):
        w = [_apo(x) for x in C.elision_zurueck(w)]
    wk = [x.lower() for x in w]
    # Endet die Folge auf einen Apostroph (`afin d’`, `de l’`), dann ist
    # das letzte Glied ein PRAEFIX: kein Token heisst `d’`, und die
    # Suche meldete 0, obwohl `afin d’aller` sehr wohl gefunden wird.
    # Gefragt ist dort das Muster „`afin d’` + beliebiger Infinitiv" —
    # genau die Konstruktion, um die sich die Elisionsregel dreht.
    # Gemeldet vom Agenten fuer 1. Thessalonicher 3.
    # Aus der ROHphrase bestimmen: `strip_punct` hat den Apostroph
    # oben schon abgeschnitten, `d’` ist dort laengst `d`.
    praefix = phr.rstrip().endswith(('’', "'"))
    voll = collections.Counter()
    orte = collections.defaultdict(list)
    unvollstaendig = []
    mehrwort = collections.defaultdict(list)
    schreibungen = collections.Counter()
    # Varianten, die sich nur in Akzenten oder in der Ligatur `œ`
    # unterscheiden, im SELBEN Durchlauf mitzaehlen. Als eigener Lauf
    # (nur bei 0 Treffern) war der Hinweis zu schwach: `a cause de`
    # liefert 2 Treffer statt 91 und schwieg deshalb — und genau der
    # Nicht-Null-Fall ist der gefaehrliche, weil er wie ein Ergebnis
    # aussieht. Gemeldet vom Agenten fuer Epheser 4.
    varianten = collections.Counter()
    wn = [_norm_akz(x) for x in wk]
    for nr in range(1, bis or 67):
        try:
            s = C.load_source(nr)
            anno = C.load_anno(nr)['chapters']
        except Exception:
            continue
        ch = s['chapters'] if 'chapters' in s else s
        for k, vv in ch.items():
            if k not in anno:
                continue
            for v, t in vv.items():
                if v not in anno[k] or wk[0] not in _apo(t).lower():
                    continue
                toks = [_apo(C.strip_punct(x)) for x in t.split()]
                E = {e['pos']: e for e in anno[k][v]
                     if 'pos_end' not in e and 'parts' not in e}
                for i in range(len(toks) - len(w) + 1):
                    stueck = toks[i:i + len(w)]
                    if ([_norm_akz(x.lower()) for x in stueck] == wn
                            and [x.lower() for x in stueck] != wk):
                        varianten[' '.join(stueck)] += 1
                    # Der Vergleich laeuft klein: `il y avait là` meldete
                    # 0, `Il y avait là` zwei einstimmige Vorkommen —
                    # dieselbe stille Null wie bei `garder/garda le
                    # silence`, nur ueber die Satzposition. Die Zeilen
                    # bleiben getrennt, wo die Glossen sich
                    # unterscheiden; die Zaehlung deckt jetzt beide
                    # Stellungen. Gemeldet vom Agenten fuer Marc 5.
                    klein = [x.lower() for x in toks[i:i + len(w)]]
                    if praefix:
                        if (klein[:-1] != wk[:-1]
                                or not klein[-1].startswith(wk[-1])):
                            continue
                    elif klein != wk:
                        continue
                    # Ein Mehrwort, das die Folge umspannt, wird
                    # IMMER erfasst — auch wenn alle Positionen
                    # zusaetzlich Einzeleintraege tragen, denn das
                    # Kopfwort behaelt seinen. Dessen Reihe ist oft die
                    # eigentliche Antwort: bei „Kehrt um" zerfaellt der
                    # Bestand als Einzelwort in sechs Varianten, als
                    # Mehrwort in genau drei — und die drei trennen sich
                    # nach Bedeutung (Richtung, Umkehrruf, Busse). Der
                    # Agent fuer Sacharja 1 musste das selbst
                    # herausfinden, weil hier frueher nur Einzelwoerter
                    # standen.
                    for m in anno[k][v]:
                        sp = m.get('parts', list(range(
                            m['pos'], m.get('pos_end', m['pos']) + 1)))
                        if len(sp) <= 1:
                            continue
                        # Frueher musste das Mehrwort GANZ in der Folge
                        # liegen. `se mit à` meldete deshalb 16 Vorkommen
                        # und KEIN Mehrwort, obwohl `se mettre à` 22x im
                        # Bestand steht — der Span umfasst dort auch den
                        # Infinitiv (`se mit à enseigner`) und ragt damit
                        # ueber die Folge hinaus. Der Agent fuer Marc 7
                        # haette danach in 7,35 ein etabliertes Mehrwort
                        # weggelassen. Jetzt zaehlt jede UEBERSCHNEIDUNG;
                        # was hinausragt, wird als solches gekennzeichnet.
                        if max(sp) < i or min(sp) >= i + len(w):
                            continue
                        weiter = min(sp) < i or max(sp) >= i + len(w)
                        mehrwort[(m['lemma'], weiter) + C.reihe(m)].append(
                            f'{C.book_name(nr)} {k},{v}')
                    if not all(i + j in E for j in range(len(w))):
                        unvollstaendig.append(f'{C.book_name(nr)} {k},{v}')
                        continue
                    key = tuple(C.reihe(E[i + j])
                                for j in range(len(w)))
                    voll[key] += 1
                    orte[key].append(f'{C.book_name(nr)} {k},{v}')
                    schreibungen[tuple(toks[i:i + len(w)])] += 1
    return (w, voll, orte, unvollstaendig, mehrwort, schreibungen,
            varianten)


def schreibungswarnung(w, schreibungen):
    """Wo die Treffer sich in der GROSSSCHREIBUNG unterscheiden.

    Der Vergleich laeuft absichtlich klein (`il y avait là` fand sonst
    nichts). Am Satzanfang ist das harmlos. Mitten im Satz ist es das
    nicht: `folgenreihe "même Esprit"` zeigte eine Reihe aus
    1. Korinther 1,10, wo `un même **esprit**` kleingeschrieben steht
    und „Gesinnung" heisst — und wer der Zahl folgt, setzt `Esprit` auf
    *spirit · espíritu · spirito*. Beim Leitwort des Buches ist das der
    teuerste denkbare Fehlgriff; gemeldet vom Agenten fuer
    1. Korinther 12.

    Der erste Token bleibt aussen vor — dort ist der Grossbuchstabe die
    Satzposition, nicht ein anderes Wort.
    """
    if len(w) < 2:
        return []
    abweichend = collections.Counter()
    for form, n in schreibungen.items():
        for j in range(1, len(w)):
            if j < len(form) and form[j] != w[j] and form[j].lower() == w[j].lower():
                abweichend[(w[j], form[j])] += n
    return sorted(abweichend.items(), key=lambda x: -x[1])


def als_lemma(phr):
    """Steht die Folge als LEMMA eines Mehrworts im Bestand?

    `stellen()` sucht die Zeichenkette im Quelltext. Ein Mehrwort steht
    dort aber in seiner gebeugten Form: das Lemma `garder le silence`
    erscheint als `garda le silence` (Mt 26,63), und die Suche meldete
    dafuer 0 Vorkommen. Der Agent fuer Marc 3 hat es bemerkt — wer nur
    diese Null liest, erfindet ein vorhandenes Mehrwort neu.
    """
    phr = C.strip_punct(_apo(phr))
    treffer = collections.defaultdict(list)
    for nr, k, v, e in C.iter_corpus():
        if not C.is_multi(e) or _apo(e.get('lemma', '')) != phr:
            continue
        treffer[(e.get('level', '?'),) + C.reihe(e)].append(
            f'{C.book_name(nr)} {k},{v}')
    return treffer


def nahe_lemmata(phr, wieviel=4):
    """Mehrwortlemmata, deren Woerter denselben Stamm haben wie die Anfrage.

    `als_lemma` sucht die Anfrage BUCHSTABENGLEICH als Lemmanamen. Das
    verfehlt jedes Mehrwort, dessen Zitierform anders flektiert als der
    Vers: `il vaut mieux` steht im Bestand unter `valoir mieux`, mit
    zehn Belegen — und der Lauf schrieb dazu „Auch nicht als Lemma
    eines Mehrworts im Bestand". Das ist keine unvollstaendige Auskunft,
    sondern eine falsche, und sie laedt zur Neupraegung ein. Gemeldet
    vom Agenten fuer 1. Korinther 7, der das Mehrwort nur deshalb nicht
    verloren hat, weil `sweeplemma` es unabhaengig fand.

    Verglichen werden die Stammschluessel der INHALTSWOERTER (vier
    Zeichen, akzentfrei). `il` und `de` tragen nichts zur Unterscheidung
    bei und wuerden die Liste fluten, also fallen sie heraus. Gemeldet
    wird nur, was mindestens ein Inhaltswort teilt UND nicht mehr als
    ein Inhaltswort mehr oder weniger hat.
    """
    # Die Liste muss die PRAEPOSITIONEN mitfuehren. Ohne sie ging `par`
    # als Inhaltswort durch, und `folgenreihe "par la puissance de Dieu"`
    # schlug `par terre` und `deux par deux` als stammverwandt vor —
    # reines Rauschen. Gemeldet vom Agenten fuer 2. Korinther 6.
    # Dieselbe Einsicht wie beim Fenster in `sweeplemma`: was staendig
    # vorkommt, trennt nichts.
    klein = {'il', 'elle', 'le', 'la', 'les', 'de', 'du', 'des', 'a', 'à',
             'en', 'y', 'ce', 'se', 's', 'l', 'd', 'un', 'une', 'que',
             'qui', 'et', 'ne', 'pas', 'on', 'nous', 'vous', 'je', 'tu',
             'par', 'pour', 'dans', 'sur', 'sous', 'avec', 'sans',
             'chez', 'entre', 'vers', 'depuis', 'aussi', 'plus', 'tout',
             'même', 'comme', 'si', 'ou', 'mais', 'au', 'aux'}

    def stamm(w):
        return C.ohne_akzent(w.lower())[:4]

    def inhalt(text):
        w = [x for x in C.strip_punct(_apo(text)).split()
             if x.lower() not in klein]
        return {stamm(x) for x in w if len(x) >= 3}

    ziel = inhalt(phr)
    if not ziel:
        return {}
    gefunden = collections.defaultdict(list)
    for nr, k, v, e in C.iter_corpus():
        if not C.is_multi(e):
            continue
        lem = e.get('lemma', '')
        s = inhalt(lem)
        if not s or not (ziel & s):
            continue
        if abs(len(s) - len(ziel)) > 1:
            continue
        gefunden[lem].append(f'{C.book_name(nr)} {k},{v}')
    return dict(sorted(gefunden.items(), key=lambda x: -len(x[1]))[:wieviel])


def main():
    args = list(sys.argv[1:])
    bis = None
    if '--buch' in args:
        i = args.index('--buch')
        bis = int(args[i + 1])
        del args[i:i + 2]
    # `folgenreihe.py --help` hat die Zeichenkette `--help` im Quelltext
    # gesucht und „0 Vorkommen" gemeldet — eine Hilfe, die wie ein
    # sauberer Lauf aussieht. Gemeldet vom Agenten fuer Marc 11.
    if not args or any(a in ('-h', '--help') for a in args):
        print(__doc__)
        return 2
    print(f'*{C.bestandsstand()}*')
    for phr in args:
        (w, voll, orte, unv, mehrwort, schreib,
         varianten) = stellen(phr, bis)
        ges = sum(voll.values())
        print(f'\n# „{phr}"\n')
        print(f'{ges} vollstaendig glossierte Vorkommen, '
              f'{len(voll)} verschiedene Reihen'
              + (f', {len(unv)} mit Mehrwort an einer Position'
                 if unv else ''))
        for form, n in varianten.most_common(3):
            print(f'**{ges} Treffer fuer `{" ".join(w)}`, aber {n} fuer '
                  f'`{form}`.** Der Unterschied sind nur Akzente oder die '
                  'Ligatur `œ`\n— dieselbe Wendung, andere Schreibung. '
                  'Beide Zahlen gehoeren zusammengezaehlt.')
        # Der erste Token bleibt aus `schreibungswarnung()` heraus,
        # weil dort der Grossbuchstabe die Satzposition ist und nicht
        # ein anderes Wort. Fuer die GLOSSE ist er trotzdem
        # entscheidend: sie folgt der Satzposition mit. Wer `Parce que
        # vous` gross fragt, sieht 12 kleines *weil* gegen 6 *Weil* und
        # nimmt die Mehrheit — mitten in einen Satzanfang hinein.
        # Gemeldet vom Agenten fuer Galates 4, zweiter Beleg derselben
        # Klasse nach `même Esprit`.
        erst = collections.Counter()
        for form, n in schreib.items():
            if form:
                erst[form[0] == w[0]] += n
        if erst[False] and erst[False] > erst[True]:
            print(f'**ACHTUNG: `{w[0]}` so gefragt, aber '
                  f'{erst[False]} von {erst[False] + erst[True]} Treffern '
                  f'schreiben das erste Wort anders.**\nAm Satzanfang '
                  'folgt die deutsche Glosse der Satzposition — sieh dir '
                  'die\nReihen der gleich geschriebenen Treffer getrennt an.')
        for (gefragt, gefunden), n in schreibungswarnung(w, schreib):
            print(f'**ACHTUNG: {n} dieser Vorkommen lesen `{gefunden}`, '
                  f'nicht `{gefragt}`.** Der Vergleich laeuft klein — '
                  'mitten im Satz\nist das ein ANDERES Wort, und seine '
                  'Reihe ist keine Bindung fuer deines.')
        # Die Mehrwortliste steht weiter unten, und drei Agenten haben
        # sie mit `| head` abgeschnitten und dem Werkzeug vorgeworfen,
        # es „verschweige den Mehrwortabschnitt" (`c'est toi`,
        # `près de`, `tout à coup` — alle drei standen da). Deshalb
        # jetzt eine Zeile ganz oben, die auch ein `head -5` sieht.
        if mehrwort:
            print(f'**{sum(len(v) for k, v in mehrwort.items() if not k[1])} davon sind '
                  f'im Bestand als MEHRWORT gefasst — die Liste steht '
                  f'unten, NICHT abschneiden.**')
        if len(voll) == 1:
            print('**einstimmig**')
        print()
        for r, n in voll.most_common():
            anteil = f'{100 * n / ges:.0f}%' if ges else '—'
            print(f'  {n:5}  ({anteil})')
            for j, x in enumerate(r):
                print(f'      {w[j]:<24} ' + ' · '.join(x))
            if n <= 3:
                print(f'      → {", ".join(orte[r][:5])}')
            print()
        if mehrwort:
            # Nur die Reihen zaehlen, die die Folge WIRKLICH decken.
            # `weiter` markiert Wendungen, die darueber hinausreichen —
            # die decken die gefragte Folge nicht und gehoeren nicht in
            # dieselbe Summe. Bei `sans cesse` standen so 8 Mehrwoerter
            # gegen 7 Vorkommen, und die Differenzzeile las sich „die
            # uebrigen -1 stehen Wort fuer Wort". Gemeldet vom Agenten
            # fuer 1. Thessalonicher 1.
            ges_mw = sum(len(v) for k, v in mehrwort.items() if not k[1])
            ges_ueber = sum(len(v) for k, v in mehrwort.items() if k[1])
            print(f'  Als MEHRWORT gefasst: {ges_mw} Vorkommen, '
                  f'{len(mehrwort)} Reihen')
            # Die beiden Abschnitte zeigen DIESELBEN Vorkommen aus zwei
            # Blickwinkeln — oben Wort fuer Wort, hier als Wendung. Wo
            # alle gefasst sind, stehen dieselben Stellen zweimal da;
            # der Agent fuer Roemer 10 hat das als doppelte Ausgabe
            # gemeldet und gewarnt, dass man die Zahlen leicht addiert.
            if ges_mw == ges:
                print('  — dieselben Vorkommen wie oben, nicht zusaetzliche: '
                      'jedes ist gefasst.')
            elif ges_mw:
                print(f'  — davon; die uebrigen {ges - ges_mw} stehen '
                      'Wort fuer Wort.')
            if ges_ueber:
                print(f'  Dazu {ges_ueber} Vorkommen unter einer Wendung, '
                      'die ueber die Folge HINAUSreicht —\n'
                      '  die decken deine Folge nicht.')
            print()
            for mkey, wo in sorted(
                    mehrwort.items(), key=lambda x: -len(x[1])):
                lemma, weiter, glossen = mkey[0], mkey[1], mkey[2:]
                rand = '  ← reicht ueber die Folge hinaus' if weiter else ''
                print(f'  {len(wo):5}  [{lemma}]  ' + ' · '.join(glossen)
                      + rand)
                print(f'      → {", ".join(wo[:6])}'
                      + (' …' if len(wo) > 6 else ''))
            print()
        elif unv:
            print(f'  Mehrwort an einer Position: {", ".join(unv[:8])}'
                  + (' …' if len(unv) > 8 else ''))
        if not ges and not mehrwort:
            lem = als_lemma(phr)
            if lem:
                n = sum(len(v) for v in lem.values())
                print(f'  **Als LEMMA eines Mehrworts im Bestand: '
                      f'{n} Vorkommen** — die Zeichenkette oben trifft '
                      f'nicht, weil das Mehrwort dort gebeugt steht.')
                print()
                for key, wo in sorted(lem.items(), key=lambda x: -len(x[1])):
                    print(f'  {len(wo):5}  [{phr}] {key[0]}  '
                          + ' · '.join(key[1:]))
                    print(f'      → {", ".join(wo[:6])}'
                          + (' …' if len(wo) > 6 else ''))
                print()
            else:
                nah = nahe_lemmata(phr)
                if nah:
                    print('  Diese ZEICHENKETTE steht nicht als Mehrwortlemma '
                          'im Bestand.')
                    print('  **Stammverwandte Mehrwortlemmata gibt es aber '
                          '— pruefe sie, bevor du praegst:**')
                    print()
                    for lem, wo in nah.items():
                        print(f'  {len(wo):5}  [{lem}]'
                              f'      → {", ".join(wo[:5])}'
                              + (' …' if len(wo) > 5 else ''))
                    print()
                else:
                    print('  Auch nicht als Lemma eines Mehrworts im Bestand '
                          '— auch nicht stammverwandt.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
