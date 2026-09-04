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

MASC_SG = {'il mio','il tuo','il suo','il nostro','il vostro','il loro'}
FEM_SG  = {'la mia','la tua','la sua','la nostra','la vostra','la loro'}
MASC_PL = {'i miei','i tuoi','i suoi','i nostri','i vostri','i loro'}
FEM_PL  = {'le mie','le tue','le sue','le nostre','le vostre','le loro'}

# Nomen, deren Endung ihr Genus verschweigt. Ohne diese Liste ist der
# Lauf unlesbar — allein `mano` und `ali` machten 20 der ersten 59
# Verdachtsfaelle in Hesekiel aus.
AUSNAHMEN = {
    'mano':'fs', 'mani':'fp', 'ala':'fs', 'ali':'fp', 'ossa':'fp',
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


def fr_numerus(nomen):
    """Nur Numerus, nicht Genus — siehe Modulkopf."""
    n = nomen.strip().split()[0].lower().strip("'’")
    if not n or n in FR_STUMM:
        return None
    if len(n) < 4:
        return None
    if n.endswith('aux') or n.endswith('eaux'):
        return 'p'
    if n.endswith('s') or n.endswith('x'):
        return 'p'
    return 's'


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    buch = sys.argv[1]
    kaps = sys.argv[2:]
    out = os.environ.get('ANNO_OUT')
    if not out:
        raise SystemExit('ANNO_OUT ist nicht gesetzt.')
    treffer = []
    for f in sorted(glob.glob(os.path.join(out, buch, 'ch*.json'))):
        if '.part' in f:
            continue
        k = re.search(r'ch(\d+)\.json$', f).group(1)
        if kaps and k not in kaps:
            continue
        d = json.load(open(f))
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
                    form = kand.get('form') or ''
                    if form[:1].isupper():
                        nx = kand
                        break
                if nx is None:
                    continue
                g = genus(nx.get('it') or '')
                if not g:
                    continue
                soll = None
                if it in MASC_SG: soll = 'ms'
                elif it in FEM_SG: soll = 'fs'
                elif it in MASC_PL: soll = 'mp'
                elif it in FEM_PL: soll = 'fp'
                if soll and soll != g:
                    treffer.append(('it', k, v, e['form'], e['it'],
                                    nx['form'], nx['it'], g))
                fr = (e.get('fr') or '').strip().lower()
                if ((fr in FR_SG or fr in FR_PL)
                        and e.get('form', '').lower() not in DATIV):
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
    print()
    print('%d Verdachtsfaelle. Jeder ist am Vers zu pruefen — die Endung'
          % len(treffer))
    print('eines italienischen Nomens sagt sein Genus nicht zuverlaessig.')
    print('Wo die Nomen-Glosse die Bestandsreihe ist, liegt der Fehler')
    print('fast immer am Possessiv.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
