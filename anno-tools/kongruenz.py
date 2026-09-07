#!/usr/bin/env python3
"""Possessiv-Kongruenz gegen das folgende Nomen — italienisch und franzoesisch.

    kongruenz.py <buchNr> [<kapitel> ...]

Ein Fehlertyp, den KEIN anderes Werkzeug sieht: `il suo Bund` statt
`la sua alleanza`. Er verletzt weder Struktur noch Bindung noch Level,
also schweigen selfcheck, qa, glosskollision, levelcheck und konvention.
`ausreisser.py` meldet ihn nur, wenn die Mehrheit zufaellig anders liegt.

Gefunden in Hesekiel Paket 8, nachdem ein Agent zehn solche Stellen im
eigenen Kapitel korrigiert hatte; der buchweite Lauf fand acht weitere,
vier davon in laengst committeten Kapiteln. Ursache ist durchweg, dass
das deutsche Genus durchschlaegt, wo das italienische abweicht:
`Hand`/`mano`, `Kopf`/`testa`, `Bund`/`alleanza`.

Franzoesisch kam in Paket 9 dazu: ein Agent fand `sa règles` in 18,6 —
`règles` ist im Sinn der Monatsblutung immer Plural, also `ses`. Der
italienische Lauf sieht das nicht, weil `mestruazione` dort Singular
ist. Geprueft wird franzoesisch nur der Numerus (sa/son gegen ses),
nicht das Genus: `sa`/`son` haengt im Franzoesischen am Genus des
Nomens, das die Glosse selbst schon traegt, und vor Vokal steht `son`
auch bei Femininum (`son épée`) — daraus wird zu leicht ein Fehlalarm.

Das Sieb ist bewusst grob — die Endung eines italienischen Nomens sagt
sein Genus nicht zuverlaessig (`ali`, `mano`, `abominazioni`, `ossa`,
`radici`, `vesti` sind alle feminin trotz gegenteiliger Endung). Die
bekannten Ausnahmen stehen unten und wachsen mit dem Gebrauch. Jeder
Treffer ist ein Verdacht, kein Urteil: am Vers ansehen.
"""
import json, sys, os, glob, re
import common as C

MASC_SG = {'il mio','il tuo','il suo','il nostro','il vostro','il loro'}
FEM_SG  = {'la mia','la tua','la sua','la nostra','la vostra','la loro'}
MASC_PL = {'i miei','i tuoi','i suoi','i nostri','i vostri','i loro'}
FEM_PL  = {'le mie','le tue','le sue','le nostre','le vostre','le loro'}

# Nomen, deren Endung ihr Genus verschweigt. Ohne diese Liste ist der
# Lauf unlesbar — allein `mano` und `ali` machten 20 der ersten 59
# Verdachtsfaelle in Hesekiel aus.
AUSNAHMEN = {
    'mano':'fs', 'mani':'fp', 'ala':'fs', 'ali':'fp', 'ossa':'fp',
    # `le sue sante miriadi` (Judas 1,14) galt als Fehler, weil die
    # `-i`-Endung maskulin aussieht. `miriade` ist feminin, RIV liest
    # genau so. Gemeldet vom Agenten des franzoesischen Pilotbuchs.
    'miriade':'fs', 'miriadi':'fp',
    'braccia':'fp', 'labbra':'fp', 'dita':'fp', 'ginocchia':'fp',
    'corna':'fp', 'uova':'fp', 'mura':'fp', 'lenzuola':'fp',
    'radici':'fp', 'vesti':'fp', 'veste':'fs', 'capo':'ms', 'capi':'mp',
    'poeta':'ms', 'profeta':'ms', 'profeti':'mp', 'sacerdote':'ms',
    'sacerdoti':'mp', 'padre':'ms', 'padri':'mp', 'fratello':'ms',
    'fratelli':'mp', 'madre':'fs', 'madri':'fp', 'sorella':'fs',
    'sorelle':'fp', 'moglie':'fs', 'mogli':'fp', 'figlio':'ms',
    'figli':'mp', 'figlia':'fs', 'figlie':'fp', 'nome':'ms',
    'nomi':'mp', 'cuore':'ms', 'cuori':'mp', 'piede':'ms', 'piedi':'mp',
    'occhio':'ms', 'occhi':'mp', 'orecchio':'ms', 'orecchi':'mp',
    'orecchie':'fp', 'fine':'fs', 'parte':'fs', 'parti':'fp',
    'gente':'fs', 'notte':'fs', 'notti':'fp', 'legge':'fs', 'leggi':'fp',
    'voce':'fs', 'voci':'fp', 'carne':'fs', 'carni':'fp', 'sangue':'ms',
    'nave':'fs', 'navi':'fp',
    'immagine':'fs', 'immagini':'fp',
    # Aus Hosea: `viti` (Weinstoecke) ist feminin, die Endung sagt maskulin.
    'vite':'fs', 'viti':'fp', 'sentiero':'ms', 'sentieri':'mp',
    # Franzoesische Unveraenderliche auf -s: die Endung sagt Plural,
    # das Wort ist im Singular gleich (`puits`, `corps`, `pays`, `bois`).
    'puits':'ms', 'corps':'ms', 'pays':'ms', 'bois':'ms', 'temps':'ms',
    'mezzo':'ms', 'greggi':'fp', 'gregge':'ms', 'fonti':'fp', 'fonte':'fs',
    # Feminina auf -i im Plural: die Endung sagt hier Maskulinum, das Genus
    # ist feminin. `merci` und `torri` machten allein 12 der 12 Fehlalarme im
    # Tyrus-Kapitel aus (`le tue merci`, `le tue torri`).
    'merce':'fs', 'merci':'fp', 'torre':'fs', 'torri':'fp',
    'nave':'fs', 'navi':'fp', 'chiave':'fs', 'chiavi':'fp',
    'notte':'fs', 'notti':'fp', 'arte':'fs', 'arti':'fp',
    'corte':'fs', 'corti':'fp', 'fonte':'fs', 'fonti':'fp',
    'mente':'fs', 'menti':'fp', 'sorte':'fs', 'sorti':'fp',
    'lode':'fs', 'lodi':'fp', 'veste':'fs', 'vesti':'fp',
    'pelle':'fs', 'pelli':'fp', 'valle':'fs', 'valli':'fp',
    'prole':'fs', 'proli':'fp', 'febbre':'fs', 'febbri':'fp',
    'arma':'fs', 'armi':'fp', 'legge':'fs', 'leggi':'fp',
    'parete':'fs', 'pareti':'fp', 'palude':'fs', 'paludi':'fp', 'porta':'fs', 'porte':'fp',
    'soglia':'fs', 'soglie':'fp', 'camera':'fs', 'camere':'fp',
    'greggi':'fp', 'gregge':'ms', 'carne':'fs', 'carni':'fp',
}
# Nomen, deren Singular und Plural gleich lauten — das Possessiv ist die
# einzige Numerus-Angabe, also nie ein Fehler. Ebenso Zahlwoerter, die
# zwischen Possessiv und Nomen stehen ("meine vier Gerichte").
STUMM = {
    'citta', 'città', 'virtù', 'virtu', 'gioventù', 'gioventu',
    'schiavitù', 'schiavitu', 'tribù', 'tribu', 'crisi', 're', 'sposa',
    'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove',
    'dieci', 'undici', 'dodici', 'venti', 'trenta', 'cento', 'mille',
}
# Endungen, die auf -ione/-ioni gehen, sind praktisch immer feminin.
def genus(nomen):
    n = nomen.strip().split()[0].lower().strip("'’")
    if not n:
        return None
    if n in STUMM:
        return None
    if n in AUSNAHMEN:
        return AUSNAHMEN[n]
    if n.endswith('zioni') or n.endswith('sioni') or n.endswith('gioni'):
        return 'fp'
    if n.endswith('zione') or n.endswith('sione') or n.endswith('gione'):
        return 'fs'
    if n.endswith('i'):
        return 'mp'
    if n.endswith('a'):
        return 'fs'
    if n.endswith('o'):
        return 'ms'
    return None            # -e ist mehrdeutig, lieber schweigen


FR_SG = {'mon','ma','ton','ta','son','sa','notre','votre','leur'}
# `leur` ist franzoesisch zugleich Dativpronomen ("ich gab ihnen"). Diese
# deutschen Formen schliessen den Possessiv-Fall aus.
DATIV = {'ihnen','ihm','ihr','mir','dir','uns','euch','sich','sie','ihn'}
DE_POSSESSIV = {'ihr','ihre','ihren','ihrem','ihrer','ihres',
                'Ihr','Ihre','ihr'}
# Alle deutschen Possessivformen — Anker fuer die Artikelprobe unten.
DE_POSSESSIV_ALLE = DE_POSSESSIV | {
    'mein','meine','meinen','meinem','meiner','meines',
    'dein','deine','deinen','deinem','deiner','deines',
    'sein','seine','seinen','seinem','seiner','seines',
    'unser','unsere','unseren','unserem','unserer','unseres',
    'euer','eure','euren','eurem','eurer','eures'}
# Italienische Possessive OHNE Artikel — genau die sind verdaechtig.
IT_ARTIKEL = {'il', 'lo', 'la', "l'", 'l’', 'i', 'gli', 'le'}

IT_POSSESSIV = {'mio','mia','miei','mie','tuo','tua','tuoi','tue',
                'suo','sua','suoi','sue','nostro','nostra','nostri',
                'nostre','vostro','vostra','vostri','vostre'}
# Verwandtschaftsnomen im Singular stehen ohne Artikel: `mio padre`.
# Formen von `essere` — davor steht ein praedikatives Nomen ohne Artikel.
ESSERE = {'è','sono','sei','siamo','siete','era','erano','sarà','saranno',
          'sia','siano','fu','furono','essere','sarai','sarete'}
IT_VERWANDT = {'padre','madre','figlio','figlia','fratello','sorella',
               'marito','moglie','zio','zia','nonno','nonna','cugino',
               'cugina','nipote','genero','nuora','suocero','suocera',
               # Feste Wendungen ohne Artikel. `a tuo riguardo`
               # (Matthaeus 4,6) war der erste Fehlalarm dieser Art.
               'riguardo','casa','vita','avviso','parere','favore'}
FR_PL = {'mes','tes','ses','nos','vos','leurs'}
# Franzoesische Nomen, deren Plural-s fehlt oder deren Numerus die
# Endung nicht verraet. `règles` ist der Fund, der den Lauf ausgeloest hat.
FR_STUMM = {
    'fois', 'temps', 'corps', 'bras', 'pays', 'fils', 'prix', 'choix',
    'croix', 'voix', 'nez', 'os', 'cours', 'discours', 'univers', 'nord',
    'sud', 'est', 'ouest', 'repas', 'pas', 'cas', 'gens', 'moeurs',
    'encens', 'palais', 'dos', 'poids', 'succes', 'succès', 'progres',
    'progrès', 'jamais', 'plusieurs', 'divers', 'frais', 'mois',
    'bois', 'bras', 'temps', 'velours', 'univers', 'rubis', 'tapis',
}


# Franzoesische Unveraenderliche: die Endung sagt Plural, das Wort ist im
# Singular gleich. `puits` machte den letzten Fehlalarm in Hosea aus.
FR_INVARIANT = {'puits', 'corps', 'pays', 'bois', 'temps', 'fois', 'mois',
                'bras', 'poids', 'repas', 'palais', 'prix', 'choix',
                'discours', 'cours', 'concours', 'univers', 'progrès',
                'succès', 'procès', 'dos', 'nez', 'voix', 'croix', 'noix',
                'paix', 'toux', 'faux', 'roux'}


# Spanisch: `su`/`sus` richtet sich wie das franzoesische `sa`/`ses` nach
# dem BESITZ, nicht nach dem Besitzer. Geprueft wurde es in keiner der
# beiden Richtungen — der franzoesische Teil lief nur ueber die
# `fr`-Spalte, und die gibt es beim franzoesischen Quelltext nicht mehr.
# Gemeldet vom Agenten fuer Matthaeus 1.
ES_SG = {'mi', 'tu', 'su', 'nuestro', 'nuestra', 'vuestro', 'vuestra'}
ES_PL = {'mis', 'tus', 'sus', 'nuestros', 'nuestras', 'vuestros', 'vuestras'}
# Spanische Woerter, deren End-s kein Plural ist.
# Spanische Woerter, deren End-s kein Plural ist. Die ersten Laeufe ueber
# den deutschen Bestand haben die Liste gefuellt; `arcoíris` und
# `cumpleaños` machten allein drei der ersten sieben Treffer aus.
ES_INVARIANT = {'crisis', 'analisis', 'análisis', 'lunes', 'martes',
                'miercoles', 'miércoles', 'jueves', 'viernes', 'dios',
                'mes', 'pais', 'país', 'interes', 'interés',
                'arcoiris', 'arcoíris', 'cumpleanos', 'cumpleaños',
                'paraguas', 'ciempies', 'ciempiés', 'tos', 'mies',
                'res', 'vez', 'atlas', 'caos', 'oasis', 'exodo', 'éxodo',
                'genesis', 'génesis'}


def es_numerus(nomen):
    """Nur Numerus. Wie fr_numerus bewusst grob — jeder Treffer ist Verdacht."""
    n = nomen.strip().split()[0].lower().strip("'’")
    if not n or n in ES_INVARIANT or len(n) < 4:
        return None
    return 'p' if n.endswith('s') else 's'


def fr_numerus(nomen):
    """Nur Numerus, nicht Genus — siehe Modulkopf."""
    n = nomen.strip().split()[0].lower().strip("'’")
    if not n or n in FR_STUMM or n in FR_INVARIANT:
        return None
    if len(n) < 4:
        return None
    if n.endswith('aux') or n.endswith('eaux'):
        return 'p'
    if n.endswith('s') or n.endswith('x'):
        return 'p'
    return 's'


HABEN_FR = {'ont', 'a', 'ai', 'as', 'avez', 'avons'}
HABEN_IT = {'hanno', 'ha', 'ho', 'hai', 'avete', 'abbiamo'}
SEIN_FR = {'ont': 'sont', 'a': 'est', 'ai': 'suis', 'as': 'es',
           'avez': 'êtes', 'avons': 'sommes'}
SEIN_IT = {'hanno': 'sono', 'ha': 'è', 'ho': 'sono', 'hai': 'sei',
           'avete': 'siete', 'abbiamo': 'siamo'}


# Die Possessiv- und Artikelproben lesen die `it`-SPALTE. Bei
# `ANNO_EDITION=ita/riv1927mod` gibt es die nicht — Italienisch ist dort
# die `form`. Ohne diesen Schalter liest jede Probe `None`, findet nichts
# und meldet „0 Verdachtsfaelle": dieselbe lautlose Null, an der schon
# artikel.py und qa.py in der franzoesischen Richtung haengen geblieben
# sind. Was bleibt, sind die es- und fr-Proben; die tragen dort.
IT_SPALTE = 'it' in C.LANGS

# Woran ein reflexives Mehrwort im QUELLTEXT zu erkennen ist.
REFLEXIV_PRAEFIX = {'de': ('sich ',), 'fr': ('se ', "s'"),
                    'it': ('si ', "s'"), 'es': ('se ', "se'"),
                    'en': ('oneself ',)}

PRAEFIX = REFLEXIV_PRAEFIX.get(C.LANG, ())
HILFSLEMMA = {'de': ('haben', 'sein'), 'fr': ('avoir', 'être'),
              'it': ('avere', 'essere'), 'es': ('haber', 'ser'),
              'en': ('have', 'be')}.get(C.LANG, ())


def hilfsverb_reflexiv(d, kap):
    """Reflexives Perfekt nimmt franzoesisch être und italienisch essere.

    Zweimal in einem Buch aufgefallen: Hosea 6,10 („hat sich verunreinigt")
    trug fr *a* / it *ha*, waehrend derselbe Satz in 5,3 richtig *est* / *è*
    hatte; Hosea 7,13 („haben sich aufgelehnt") ebenso. Beide Male stand im
    Mehrwort-Eintrag die richtige Form (*s'est souillé*, *se sont révoltés*)
    und im gedeckten Einzelwort die falsche — der Fehler ist also allein am
    Hilfsverb, und er ist mechanisch zu finden.

    Gesucht wird ein Mehrwort mit Lemma `sich …`, dessen romanische Glosse
    mit être/essere gebildet ist, und davor ein Einzelwort `haben`.
    """
    raus = []
    for v, ents in d.items():
        einzel = {e['pos']: e for e in ents
                  if 'pos_end' not in e and 'parts' not in e}
        for mw in ents:
            if 'pos_end' not in mw and 'parts' not in mw:
                continue
            lem = (mw.get('lemma') or '')
            if not any(lem.startswith(p) for p in PRAEFIX):
                continue
            fr, it = (mw.get('fr') or ''), (mw.get('it') or '')
            # Bei italienischem Quelltext steht das essere-Perfekt in der
            # FORM, nicht in einer Glosse — dann ist die Frage, ob die
            # franzoesische Spalte mitzieht.
            form = mw.get('form') or ''
            if not (re.search(r"\b(s'est|se sont|me suis|nous sommes|vous êtes|s'était)\b", fr)
                    or re.search(r'\b(si è|si sono|mi sono|ci siamo|vi siete)\b', it)
                    or (C.LANG == 'it' and re.search(
                        r'\b(si è|si sono|mi sono|ti sei|ci siamo|vi siete)\b', form))):
                continue
            # Das Hilfsverb kann VOR dem Partizip stehen („hat sich
            # verunreinigt") oder dahinter — im Nebensatz ist die zweite
            # Stellung die Regel („weil sie sich aufgelehnt haben"). Die
            # erste Fassung sah nur nach vorn und uebersah deshalb
            # Hosea 8,1; gefunden vom Agenten fuer Kapitel 14.
            nachbarn = ([mw['pos'] - d for d in (1, 2, 3)]
                        + [mw['pos'] + d for d in range(1, 9)])
            for p in nachbarn:
                h = einzel.get(p)
                if not h or h.get('lemma') not in HILFSLEMMA:
                    continue
                hf, hi = (h.get('fr') or '').lower(), (h.get('it') or '').lower()
                if hf in HABEN_FR or hi in HABEN_IT:
                    raus.append((kap, v, p, h.get('form'), hf, hi,
                                 SEIN_FR.get(hf, '?'), SEIN_IT.get(hi, '?'),
                                 mw.get('lemma')))
                break
    return raus


geprueft = [0]
stumm = [0]



def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    buch = sys.argv[1]
    kaps = sys.argv[2:]
    out = os.environ.get('ANNO_OUT')
    if not out:
        raise SystemExit('ANNO_OUT ist nicht gesetzt.')
    treffer = []
    refl = []
    # `kongruenz.py 40` lief bis Markus **leer** und meldete „0
    # Verdachtsfaelle": in `$ANNO_OUT` steht nur das Buch, an dem gerade
    # gearbeitet wird, und fuer jedes andere gab es keine Kapiteldatei.
    # Der Koordinator las diese Null als geprueft. Jetzt faellt der Lauf
    # auf die Kapitelquellen zurueck und sagt in jedem Fall, woher er
    # gelesen hat und wie viele Kapitel es waren.
    quelle = out
    dateien = sorted(glob.glob(os.path.join(out, buch, 'ch*.json')))
    if not dateien:
        quelle = os.path.dirname(C.quellen_dir(int(buch)))
        dateien = sorted(glob.glob(os.path.join(quelle, buch, 'ch*.json')))
    if not dateien:
        raise SystemExit(
            f'Keine Kapiteldatei fuer Buch {buch} — weder unter '
            f'{out}/{buch}/ noch unter {quelle}/{buch}/. Es wurde NICHTS '
            f'geprueft.')
    print(f'gelesen: {quelle}/{buch}/ — {len(dateien)} Kapiteldatei(en)')
    for f in dateien:
        if '.part' in f:
            continue
        k = re.search(r'ch(\d+)\.json$', f).group(1)
        if kaps and k not in kaps:
            continue
        d = json.load(open(f))
        refl += hilfsverb_reflexiv(d, k)
        for v, ents in d.items():
            einzel = {e['pos']: e for e in ents
                      if 'pos_end' not in e and 'parts' not in e}
            for pos, e in einzel.items():
                it = (e.get('it') or '').strip().lower()
                nx = None
                for d in (1, 2, 3):
                    kand = einzel.get(pos + d)
                    if kand is None:
                        break
                    form = C.de_wort(kand)
                    if form[:1].isupper():
                        nx = kand
                        break
                if nx is None:
                    continue
                # Die Artikelproben brauchen das Genus NICHT — sie muessen
                # deshalb vor den `continue` stehen, sonst fallen sie bei
                # jedem Nomen aus, dessen Endung das Genus verschweigt.
                # Genau daran haben sie beim ersten Einbau geschwiegen.
                itw = (e.get('it') or '').strip().lower()
                dew = C.de_wort(e).lower()
                if not IT_SPALTE:
                    itw = ''
                folge = (nx.get('it') or '').strip().lower().split()
                # Nach einer Form von `essere` ist das Nomen Praedikativ
                # und steht artikellos: „sarà vostro servitore" (20,26,
                # so auch RIV1927). Gemeldet vom Agenten fuer Matthaeus 20.
                vorher = einzel.get(pos - 1)
                praedikativ = bool(vorher) and (vorher.get('it') or '').strip(
                    ).lower() in ESSERE
                # In der franzoesischen Richtung steht der Artikel auf
                # einem EIGENEN Token: `les siens` = `les` *i* +
                # `siens` *suoi*. Das Possessivtoken ist dann zu Recht
                # bar, und die Probe meldete es trotzdem — in Jean 1
                # war das ihr einziger Treffer, und er war falsch.
                # Gemeldet vom Agenten fuer Jean 1.
                art_davor = bool(vorher) and (vorher.get('it') or '').strip(
                    ).lower().split()[-1:] and (
                    vorher.get('it') or '').strip().lower().split(
                    )[-1] in IT_ARTIKEL
                if itw in IT_POSSESSIV and dew in DE_POSSESSIV_ALLE \
                        and not praedikativ and not art_davor \
                        and folge and folge[0] not in IT_VERWANDT:
                    treffer.append(('it', k, v, e['form'], e['it'],
                                    nx['form'], nx.get('it') or '',
                                    'Artikel fehlt vor dem Possessiv'))
                if (itw == 'loro' or itw.startswith('loro ')) \
                        and dew in DE_POSSESSIV and not art_davor:
                    treffer.append(('it', k, v, e['form'], e['it'],
                                    nx['form'], nx.get('it') or '',
                                    'Artikel fehlt vor loro'))
                g = genus(nx.get('it') or '') if IT_SPALTE else ''
                if IT_SPALTE:
                    geprueft[0] += 1
                if not g:
                    # `genus()` raet aus der Endung und schweigt bei
                    # `-e`. Wie oft es schweigt, stand bisher nirgends —
                    # und eine Null aus lauter Schweigen sieht aus wie
                    # eine gepruefte Null. Die Agenten fuer Marc 4 und
                    # Marc 5 haben beide danach gefragt.
                    stumm[0] += 1
                    continue
                soll = None
                if not IT_SPALTE: continue
                if it in MASC_SG: soll = 'ms'
                elif it in FEM_SG: soll = 'fs'
                elif it in MASC_PL: soll = 'mp'
                elif it in FEM_PL: soll = 'fp'
                if soll and soll != g:
                    treffer.append(('it', k, v, e['form'], e['it'],
                                    nx['form'], nx['it'], g))
                es = (e.get('es') or '').strip().lower()
                if es in ES_SG or es in ES_PL:
                    en_ = es_numerus(nx.get('es') or '')
                    if en_:
                        solles = 's' if es in ES_SG else 'p'
                        if solles != en_:
                            treffer.append(('es', k, v, e['form'], e['es'],
                                            nx['form'], nx['es'], en_))
                fr = (e.get('fr') or '').strip().lower()
                # Der Dativ-Ausschluss haengt am DEUTSCHEN Wort — das ist in
                # der einen Richtung die Form, in der anderen die de-Spalte.
                if ((fr in FR_SG or fr in FR_PL)
                        and C.de_wort(e).lower() not in DATIV):
                    fn = fr_numerus(nx.get('fr') or '')
                    if fn:
                        sollfr = 's' if fr in FR_SG else 'p'
                        if sollfr != fn:
                            treffer.append(('fr', k, v, e['form'], e['fr'],
                                            nx['form'], nx['fr'], fn))
    for sp, k, v, f1, i1, f2, i2, g in sorted(
            treffer, key=lambda t: (int(t[1]), int(t[2]), t[0])):
        print('%s,%s,%-3s  %-10s %s %-12s | %-14s %s %-16s (%s)'
              % (buch, k, v, f1, sp, i1, f2, sp, i2, g))
    if refl:
        print()
        print('## Reflexives Perfekt mit falschem Hilfsverb')
        print()
        for kap, v, p, form, hf, hi, sf, si, lem in refl:
            print(f'  {buch},{kap},{v}  pos{p} {form:8} fr {hf} -> {sf} · '
                  f'it {hi} -> {si}   (Mehrwort `{lem}`)')
        print()
        print('  Verdacht, kein Fehler: steht das Hilfsverb im Nebensatz')
        print('  hinter dem Partizip, kann es zugleich ein zweites, NICHT')
        print('  reflexives Partizip tragen („weil sie den Bund gebrochen')
        print('  und sich aufgelehnt haben"). Dann ist avoir/avere richtig.')
    print()
    if any(t[7].startswith('Artikel fehlt') for t in treffer):
        print()
        print('Zum Artikel vor dem Possessiv: der VOKATIV steht artikellos '
              '(`Amico mio`,\n„Mon ami" in Mt 20,13) — das meldet dieses '
              'Werkzeug mit, es kann ihn nicht sehen.')
    if any(len(t) > 7 and str(t[7]).startswith('Artikel fehlt')
           for t in treffer):
        print()
        print('Zum Artikel vor dem Possessiv: der VOKATIV steht artikellos')
        print('(„Mon ami" in 20,13 ist bei RIV „Amico") — das meldet dieses')
        print('Werkzeug mit, es kann ihn nicht sehen.')
    if not IT_SPALTE:
        print('Der Quelltext ist italienisch — es gibt keine `it`-Spalte.')
        print('Die Possessiv- und Artikelproben am italienischen Genus sind')
        print('deshalb NICHT gelaufen; geprueft wurden nur die spanische und')
        print('die franzoesische Numerusprobe.')
    if geprueft[0]:
        print('Italienisches Genus: %d Nomen angesehen, bei %d konnte die '
              'Endung\ndas Genus nicht entscheiden (`-e` ist mehrdeutig) — '
              'dort wurde NICHTS\ngeprueft.' % (geprueft[0], stumm[0]))
    print('%d Verdachtsfaelle. Jeder ist am Vers zu pruefen — die Endung'
          % len(treffer))
    print('eines italienischen Nomens sagt sein Genus nicht zuverlaessig.')
    print('Wo die Nomen-Glosse die Bestandsreihe ist, liegt der Fehler')
    print('fast immer am Possessiv.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
