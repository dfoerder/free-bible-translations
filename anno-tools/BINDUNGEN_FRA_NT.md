# Bindungen — franzoesisches NT

Was Judas (65) als Pilot festgelegt hat und was jedes weitere Kapitel
uebernimmt. Die Schwester von `BINDUNGEN_AT.md`; jene gilt fuer den
deutschen Quelltext und ist **nicht** uebertragbar.

Wer hiervon abweicht, begruendet es am Vers.

## Lemma bei Elision — der semantische Kopf

Das zusammengezogene Wort ist EIN Token und bekommt EINEN Eintrag. Das
Lemma ist der Kopf, nicht die Zeichenkette:

    l’autorité → autorité      l’avoir / n’ont → avoir
    n’osa → oser               s’est → s’être
    qu’il / qu’ils / qu’au → que
    lorsqu’il → lorsque        qu’Énoch → Énoch
    d’un / d’une / du / des → de
    d’autres → autre           d’Égypte → Égypte
    au / aux → à

`au`/`aux` folgen `du`/`des` — dieselbe Verschmelzung, dieselbe Regel.
Und `d’un`/`d’une` folgen ihnen ebenso: **der Kopf ist die Praeposition**,
nicht der Artikel. Der Bestand hatte das bis Markus 4 anders — `d’un`
stand 13× auf `un`, `d’une` 8× auf `de`, also dieselbe Verschmelzung
mit zwei Lemmata, getrennt nur nach dem **Genus des Artikels**. Gemessen
und gemeldet vom Agenten fuer Marc 4, danach an allen 14 Stellen auf
`de` gezogen. Zum Vergleich: `du`, `des`, `au` und `aux` stehen an 598
Stellen einstimmig auf der Praeposition.

**Die Regel greift nur, wo zwei verschiedene Woerter zusammenstossen.**
Eine **zusammengesetzte Praeposition** behaelt ihre Woerterbuchform:
`jusqu'à` bleibt `jusqu'à` und wird nicht zu `jusque`. Entschieden in
Matthaeus Paket 1, wo Kapitel 2 die Elisionsregel angewandt hatte und
die Kapitel 1 und 3 (mit Judas) die Woerterbuchform.

## `ne … pas`

Das Mehrwort mit dem Lemma `ne pas` traegt die Einheit, und **der Span
umfasst das Verb mit, wo das Verb zwischen `ne` und `pas` steht** —
`ne vivra pas`, `Ne vous inquiétez pas`, nicht nur die beiden
Randtokens.

**Wo es nicht dazwischensteht, bleibt es draussen.** Im verneinten
Infinitiv stehen `ne pas` nebeneinander und das Verb folgt: `de ne pas
le faire connaître` (Marc 3,12) traegt einen Span von zwei Tokens.
Dieselbe Unterscheidung wie bei `personne ne` unten — nicht die Regel
entscheidet, sondern die Wortstellung des Verses. Gemeldet vom Agenten
fuer Marc 5.

Die Einzelwoerter haengen davon ab, ob das `ne` elidiert ist. Gemessen
ueber den Bestand:

    ne  (eigenes Token)   → *nicht*                    66×
    n’a · n’est · n’ont   → nur das Verb (*hat*, *ist*, *haben*)

**`ne … personne` und `personne ne`** sind beide Mehrwoerter mit dem
Lemma, das die **Wortstellung des Verses** hat: `personne ne` (9,16 ·
9,30 · 11,27 · 12,19), `ne personne` (16,20 · 17,9).

Der Span laeuft vom ersten Verneinungswort zum letzten — was
dazwischenliegt, gehoert dazu. Bei `personne ne` stehen die beiden
nebeneinander und das Verb folgt erst danach, der Span ist also zwei
Tokens lang; bei `ne … personne` steht das Verb dazwischen und der Span
umfasst es. Eine fruehere Fassung sagte pauschal „der Span umfasst das
Verb"; der Agent fuer Matthaeus 20 hat alle Vorkommen nachgemessen und
gezeigt, dass das fuer `personne ne` nicht stimmt.

**Das gilt nur, solange ein `pas` da ist.** Wo die Verneinung ohne `pas`
auskommt — `ils n’entendent ni ne comprennent` (13,13), `n’amassent
rien`, `Nul ne peut` — gibt es kein `ne pas`-Mehrwort, und das elidierte
Token muss die Verneinung selbst tragen: `n’entendent` = *hören nicht*.
Gemeldet vom Agenten fuer Matthaeus 13.

Das ist kein Widerspruch, sondern die Folge daraus, dass die Positionen
ueber `text.split()` zaehlen: wo `n’` mit dem Verb ein Token bildet, hat
die Verneinung dort keinen eigenen Platz — sie steht am `pas` und im
Mehrwort. Gemessen vom Agenten fuer Matthaeus 10.

Damit ist er in aller Regel zusammenhaengend und bekommt `pos_end`.
`parts` nur, wo etwas Nicht-Verbales dazwischensteht: `n’es … pas`
(2,6, mit `certes` dazwischen). Ueber den Bestand gemessen sind es
**52 mal `pos_end` und dreimal `parts`**.

Eine fruehere Fassung dieses Abschnitts behauptete, `selfcheck.py` weise
`parts` dort zurueck. **Das stimmt nicht** — es nimmt beides. Gemeldet
vom Agenten fuer Matthaeus 7, der den Widerspruch zum Bestand gemessen
hat.

## Relativpronomen

`qui` und `que` als Relativum werden deutsch **`welche(r)`**, nie
`der/die/das`. Sonst kollidiert das Relativpronomen buchweit mit dem
Artikel, und `glosskollision.py` meldet in jedem Kapitel dasselbe Paar.

## Reflexiva

Ein Mehrwort dort, wo die **woertlichen Einzelglossen nicht aufgehen**.
Das ist der Massstab — nicht die Frage, ob die Zielsprache ein Reflexiv
hat.

    se sont jetés    se=sich · sont=sind · jetés=geworfen
                     woertlich „sich sind geworfen"        → Mehrwort
    se sont perdus   → „sind umgekommen", gar nicht reflexiv → Mehrwort
    s’est glissé     zusammengesetzte Zeit, dt. mit „haben" → Mehrwort
    se leva          → „stand auf", dt. nicht reflexiv       → Mehrwort

    se prosterna · se retira · se trouvait · se corrompent
    se plaignent · se repaissant · se nourrissait
                     einfache Zeit, dt./es./it. selbst reflexiv
                                                            → kein Mehrwort

Die zusammengesetzten Zeiten mit `être` brauchen fast immer eins: das
franzoesische `sont` steht dort, wo das Deutsche `haben` setzt, und die
Einzelglossen addieren sich zu Unsinn.

Eine fruehere Fassung sagte „nur wo die Zielsprachen das Reflexiv nicht
spiegeln" — und widersprach damit ihrer eigenen Beispielliste, in der
`se sont jetés` (dt. *haben sich gestuerzt*, es. *se lanzaron*, it. *si
sono gettati*) sehr wohl gespiegelt wird. Gefunden vom Agenten fuer
Matthaeus 7, dem `sweeplemma.py` den fehlenden Eintrag in 7,25 meldete.

## Praepositionen und Artikel

**Vor `loro` steht der Artikel IMMER** — auch beim Verwandtschafts-
nomen, wo `mio padre` ihn weglaesst: `il loro padre`, nie `loro padre`.
`loro` ist die einzige Ausnahme von der Ausnahme. (Matthaeus 13,43
stand zuerst als `loro Padre`.)

**Die Praeposition bleibt bar, der Artikel sitzt am Folgetoken.** Das
gilt fuer den Artikel wie fuer das Possessiv:

    par les ténèbres   →  `da` + `le tenebre`      nicht `dalle` + `le`
    sur la terre       →  `su` + `la terra`        nicht `sulla` + `la`
    de son cœur        →  `di` + `il suo cuore`    nicht `del` + `suo`
    de mon Père        →  `di` + `mio Padre`

Die Regel erzeugt bewusst Folgen wie „di il suo cuore", die als Satz
niemand schriebe — aber die App zeigt **Wort unter Wort**, nicht den
Satz, und jede Position muss fuer sich stimmen. Wo der Artikel in die
Praeposition wandert, steht er entweder doppelt oder gar nicht.

Gemessen an 57 Praeposition-plus-Possessiv-Paaren des Bestands vom
Agenten fuer Matthaeus 12; die Altlast in 9,6 (`sulla` + `la`) ist
danach korrigiert.
- **Unbestimmtes Plural-`des`** = *einige · some · unos · dei|degli|delle*,
  mit Genus und Numerus nach dem **Nomen der Zielsprache**
  (`degli empi`, `delle nuvole`).

## Gerundium

`en` + Partizip Praesens: das `en` wird *indem ihr*, das Partizip eine
finite Form (`en attendant` → *indem ihr erwartet*).

## Spanisch

Durchgehend **vosotros / os / vuestro**. Die Zeugenausgabe `rv1909mod`
siezt oft (`ustedes`) — das wird nicht uebernommen.

## Die elf Reihen aus Judas

Erstbelege; jedes weitere Kapitel uebernimmt sie zeichengleich, solange
die Bedeutung dieselbe ist.

    brutes        C1  Tiere · beasts · bestias · bestie
    changent      A2  verkehren · turn · convierten · volgono
    contestent    B2  widersprechen · dispute · contradicen · contestano
    enchaînés     C1  gefesselt · chained · encadenados · incatenati
    glissé        B2  eingeschlichen · crept in · infiltrado · intrufolato
    ignorent      B1  nicht kennen · do not know · ignoran · ignorano
    impudemment   C1  unverschämt · shamelessly · desvergonzadamente · sfacciatamente
    injurieuse    C1  schmähend · abusive · injurioso · ingiurioso   (Lemma `injurieux`)
    repaissant    C1  weidend · feeding · apacentando · pascendo
    sauvez-en     A2  rettet davon · save some of them · salvad de ellos · salvatene
    vices         B2  Laster · vices · vicios · vizi

Gebundene Wortfolge: **„de notre Seigneur Jésus-Christ"** (1,17 · 1,21),
zeichengleich.

## Was der Pilot am Quelltext widerlegt hat

Beides stand **so im Prompt** und war falsch — beides aus der
*un*modernisierten LSG bzw. aus dem Gedaechtnis:

- 1,4 heisst nicht `changent en dérèglement la grâce`, sondern
  **`qui changent la grâce de notre Dieu en débauche`**. Auch
  `dérèglement` ist im `lsg1910mod` zu `débauche` geworden.
- 1,12 heisst `se repaissant eux-mêmes.` — **ohne `sans crainte`**. Die
  Furchtlosigkeit steht nur bei WEB und Luther; im franzoesischen Vers
  gibt es keine Position dafuer.

`vorgabecheck.py` hat beides nicht gemeldet, weil es Zitate in
**Backticks** nicht las. Das ist seither behoben.

## Wo der Quelltext von den Zeugen abweicht

**1,22 `ceux qui contestent`** — alle vier Zeugen lesen dort den
Variantentext („die zweifeln" / „doubt" / „nel dubbio"). LSG liest
`contester` = widersprechen, streiten. **Der Quelltext entscheidet**,
nicht die Mehrheit der Zeugen; so stimmt es auch mit `contestait` in
1,9 zusammen.

**1,7 `que`** ist die Fortsetzung von 1,5 („Je veux vous rappeler … que"),
nicht „So auch" wie bei de/en/es. Glossiert als *dass · that · que · che*.


## `te` — Dativ und Akkusativ

Englisch hat fuer beides `you`, Franzoesisch nicht. Wo `te` **Dativ**
ist, traegt es en *to you*; wo es Akkusativ ist, *you*. Ohne diese
Unterscheidung meldet `glosskollision.py` in jedem Kapitel dasselbe Paar
`te`/`tu` als staerksten Verdacht — gemessen an Matthaeus 6, wo es
viermal auftrat.

Dasselbe fuer das tonische `toi` neben `tu`: `toi` wird *du selbst · you
yourself · tú mismo · tu stesso*.

## `règne` und `royaume` teilen sich eine Reihe

Beide tragen *Reich · kingdom · reino · regno*. Das ist eine
Kollision — und sie bleibt stehen. **Gemessen: kein Vers in ganz
Matthaeus enthaelt beide Woerter.** „Dein Reich komme" (6,10) ist der
meistgelesene Satz des Buches; eine buchlokale Ausweichuebersetzung
haette den Bestand nur inkonsistent gemacht.

**Wenn ein spaeteres Kapitel beide in einem Vers hat, wird DORT
aufgeloest** — nach der Regel „aufgeloest wird nur im Kollisionsvers".

## `ne` ohne Verneinung

Zwei Faelle, in denen `ne` nicht *nicht* heisst:

- **Das `ne` explétif** nach `de peur que`, `avant que`, `à moins que`:
  `de peur que ton pied ne heurte` (4,6). Traegt es die Verneinung,
  steht sie im Deutschen doppelt und der Sinn kippt. Gesetzt wird ein
  echtes Wort — *etwa · perhaps · acaso · talora* — plus das Mehrwort
  `de peur que` = *damit nicht*.
- **`ne … rien` / `ne … ni` / `nul ne`**: dort gibt es kein `pas`, also
  auch kein `ne pas`-Mehrwort. Fuer `ne … rien` ist `ne rien` das
  Mehrwort — Spanisch und Italienisch brauchen die doppelte Verneinung.


## Ein Wort, zwei Bedeutungen — ein Lemma

Franzoesisch haeuft die Homographen: `or` (Gold / nun), `droit`
(gerecht / rechts), `lettre` (Buchstabe / Brief), `justice`
(Gerechtigkeit / Justiz), `terre` (Erde / Land), `porte` (Tuer / traegt),
`entre` (zwischen / tritt ein).

**Der Bestand kennt keine Konvention fuer disambiguierte Lemmata** —
ueber 20 deutsche Buecher gemessen: kein einziges Lemma mit Klammer oder
Schraegstrich. Ein erfundener zweiter Name (`or¹`) waere eine Setzung,
die kein anderes Werkzeug versteht.

Deshalb:

- **Die Glossen folgen der Bedeutung**, Vers fuer Vers. Zwei Lesarten
  desselben Lemmas sind erlaubt und richtig.
- **Das Level folgt dem Lemma**, also der Korpusmehrheit. `buildbook.py`
  zieht es beim Bau ohnehin dorthin; eine Quelle, die etwas anderes
  behauptet, waere nur eine Notiz, die das Ergebnis nicht erreicht.
- Wo Wortart **und** Bedeutung auseinandergehen (`porte` Substantiv
  gegen `porter` Verb, `entre` Praeposition gegen `entrer` Verb), sind
  es zwei verschiedene Lemmata und der Fall entfaellt.

**Was die Regel kostet**, an einem gemessenen Beispiel: `pouvoir` ist im
Bestand ein Verb auf A1 (`peut`, 5,36). In 9,6 und 9,8 steht dasselbe
Wort als **Substantiv** — „le pouvoir de pardonner". Fuer
Franzoesischlernende waere das B1; es bekommt A1, weil der nominalisierte
Infinitiv keinen eigenen Lemmanamen hat. Das ist der Preis dafuer, keine
Lemmanamen zu erfinden, die kein Werkzeug versteht — und er ist es wert:
ein `pouvoir¹` wuerde `belegt.py`, `lexicon.py` und `levelcheck.py`
gleichzeitig blind machen.


## `Père` — mit oder ohne italienischen Artikel

Der Bestand schwankte: `votre Père` = *vostro Padre* (5,45 · 6,1),
`mon Père` = *il mio Padre* (7,21). **Ohne Artikel ist richtig** — das
unmodifizierte Verwandtschaftsnomen im Singular ist genau die Ausnahme
der Artikelregel.

RIV1927 hilft hier nicht weiter, weil es die Wortstellung dreht
(`del Padre vostro`, `al Padre mio`): das Possessiv steht dort hinter
dem Nomen, im Franzoesischen davor. Eine Token-fuer-Token-Spiegelung
gibt es also nicht; beide Fassungen waeren grammatisch. Entschieden
wird nach der eigenen Regel, nicht nach dem Zeugen.

## Der Teilungsartikel ueber zwei Tokens

`du vin`, `du pain` sind **ein** Token, und der Bestand glossiert es
zwanzigmal als *etwas · some · algo de · del*. Ueber zwei Tokens —
`de la salive` (Marc 8,23), `de l’eau` — gab es bis Markus 8 keine
Regel, weil kein Vers sie verlangt hatte.

Sie folgt der Artikelregel: **die Praeposition traegt das Teilungswort,
der Artikel bleibt Artikel.**

    de   → *etwas · some · algo de · un po’ di*
    la   → *den · the · la · la*   (Genus und Kasus nach dem Nomen)

Entschieden nach Marc 8,23; der Agent hat die Stelle selbst als die
schwaechste seines Kapitels benannt und um eine Entscheidung gebeten.

## Wo das reflexive Lemma sitzt

Der Bestand sah zweigeteilt aus, und der Agent fuer Marc 10 hat ihn zur
Vereinheitlichung vorgeschlagen. Gemessen ist er **nicht** gespalten,
sondern folgt einer Regel:

**Das reflexive Lemma sitzt dort, wo die reflexive Bedeutung getragen
wird.** Gibt es ein Mehrwort, traegt es sie, und das Verbtoken behaelt
das schlichte Lemma:

    Mt 17,14  se jeter à genoux [MW]  ·  jeter   (Einzeleintrag)
    Marc 10,17 se jeter à genoux [MW]  ·  jeter

Gibt es keines, traegt sie das Verbtoken selbst:

    Mt 26,39 · Marc 5,22 · 5,33 · 7,25   jeta / jeter  →  `se jeter`

So stehen im Bestand **55 Stellen**: `se prosterner`, `se rendre`,
`se souvenir`, `se repentir`, `se précipiter`, `s’approcher` und andere
tragen ihr reflexives Lemma auf dem Verbtoken, waehrend `se` daneben
seine eigene Glosse behaelt.

## `pouvoir` und `autorité`

Beide uebersetzen dasselbe griechische Wort, und der englische Zeuge
sagt zu beiden *authority*. Der Bestand haelt sie im **Deutschen**
auseinander — `autorité` = *Vollmacht* (11 Stellen), das Substantiv
`pouvoir` = *Macht* (7 Stellen) — und laesst das Englische
zusammenfallen.

Nur wo beide **im selben Vers** stehen, wird aufgeloest: Marc 11,28
(„Par quelle autorité … qui t’a donné le pouvoir") setzt `pouvoir`
englisch auf *power*. Marc 10,42 und 13,34 haben je nur eines von
beiden und bleiben auf der Bestandsreihe. Gepruefte Frage des Agenten
fuer Marc 10.
