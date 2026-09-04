#!/usr/bin/env python3
"""Italienische Possessiv-Kongruenz gegen das folgende Nomen.

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
                nx = einzel.get(pos + 1)
                if not nx:
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
                    treffer.append((k, v, e['form'], e['it'],
                                    nx['form'], nx['it'], g))
    for k, v, f1, i1, f2, i2, g in sorted(
            treffer, key=lambda t: (int(t[0]), int(t[1]))):
        print('%s,%s,%-3s  %-10s it %-12s | %-14s it %-16s (%s)'
              % (buch, k, v, f1, i1, f2, i2, g))
    print()
    print('%d Verdachtsfaelle. Jeder ist am Vers zu pruefen — die Endung'
          % len(treffer))
    print('eines italienischen Nomens sagt sein Genus nicht zuverlaessig.')
    print('Wo die Nomen-Glosse die Bestandsreihe ist, liegt der Fehler')
    print('fast immer am Possessiv.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
