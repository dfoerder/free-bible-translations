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

    de   → *etwas · some · algo de · **di***
    la   → *den · the · la · **la***   (Genus und Kasus nach dem Nomen)

**Nachgemessen und korrigiert (Johannes 13).** `un po’ di` war falsch: der
Zeuge kennt es nicht, er liest `del denaro` (Marc 14,11 · Luc 22,5),
`dell’olio e del vino` (Luc 10,34), `delle zizzanie` (Mt 13,25). Die Regel
ist einfacher, als sie aussah, und der Bestand macht sie an 195 Stellen
schon richtig:

- **`de` vor einem Artikel** — gleich ob der Artikel ein eigenes Token ist
  (`de la salive`) oder im Wort steckt (`de l’eau`) — traegt italienisch nur
  **`di`**; der Artikel bleibt bei seinem eigenen Token (`la`, `l’acqua`).
  Zusammengelesen ergibt das `di la` bzw. `di l’acqua`, also genau `della`
  und `dell’acqua`.
- **`de` vor einem blossen Nomen** (`de pain`, `de fruit`, `de bien`) traegt
  den ganzen Teilungsartikel: **`del`/`della`** nach Genus. 60 Stellen, alle
  einstimmig, unveraendert.

29 Stellen gezogen. Wer `un po’ di` findet, hat eine Altlast vor sich.

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

**Nachgemessen mit `reflexiv.py` (neu).** Die zweite Haelfte der Regel war
an **69 Stellen** verletzt: Verbtoken mit `se` davor, kein Mehrwort
darueber, und trotzdem das schlichte Lemma — obwohl derselbe Verbstamm
anderswo im Bestand unter `se <lemma>` steht. Alle 69 gezogen, am
haeufigsten `se trouver` (21), `se retirer` (14), `se mettre` (6),
`se demander` (6).

**Und eine Warnung aus eigenem Schaden.** Ich habe die Probe zuerst
**ohne den Mehrwortfilter** gefahren und daraufhin Mt 17,14, Marc 4,37
und Marc 10,17 „korrigiert" — also genau die drei Stellen, die dieser
Abschnitt oben als richtig auffuehrt. Zurueckgenommen. Wer diese Regel
misst, **muss** die Positionen unter einem Mehrwort ausschliessen, sonst
meldet die Probe ihre eigenen Musterbeispiele als Fehler. `reflexiv.py`
tut das und trennt ausserdem die sicheren Faelle (reflexives Lemma
existiert schon) von den 95, die am Vers zu pruefen sind — dort ist `se`
oft gar nicht reflexiv, sondern Objekt (`ils se disaient` = sagten
zueinander).

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

## `ne … plus` und das elidierte `ne` ohne eigene Verneinung

Der Abschnitt oben nennt `ne pas`, `ne rien`, `ne personne` und `nul
ne`. **`ne plus` fehlte** — es steht mit **53** Belegen im Bestand, und
der Span umfasst das Verb (`ne pourras plus`, Luc 1,20; Marc 1,45). Der
Agent fuer Luc 1 hatte es als kompositionell verworfen; der neue
zweite Abschnitt von `sweeplemma.py` hat es zurueckgeholt. (Hier stand
lange „13 Belege" — das war der Stand von Lukas 1. Der Agent fuer
Roemer 6 hat nachgemessen; **Zahlen in dieser Datei altern**, und wer
sich auf eine stuetzt, misst sie besser nach.)

### `plus de` unter Verneinung: das `de` traegt das `kein`, nicht die Spanne

`n’a plus de pouvoir` (Rm 6,9) sieht aus wie ein Sonderfall, ist aber
nur der Teilungsartikel unter einer anderen Verneinung. Die 70 `pas
de`-Stellen legen das `kein` einheitlich auf das **`de`** und lassen
die Verneinungsspanne beim blossen *nicht*:

    n’eut pas → *hatte nicht*   ·   de → *keinen · any · ninguna · alcun*

Genau so ist `ne plus` zu fassen: `n’a plus` → *hat nicht mehr*, `de` →
*keine*. **Jean 2,3 war die einzige Stelle, die es andersherum machte**
(`n’ont plus` → „haben keinen mehr", `de` → *an*) — auf die 70
gezogen. Nicht verwechseln mit dem **komparativen** `plus de` (`plus de
quarante`, `plus de douze`), das `de` = *als · than* traegt und mit
Verneinung nichts zu tun hat, auch wo eine im Vers steht (Actes 24,11
`il n’y a pas plus de douze jours`).

**Und eine Grenze der Regel „das elidierte Token traegt die Verneinung
selbst":** sie gilt nur, wo das `ne` die einzige Verneinung ist. In
`Car rien n’est impossible` (Luc 1,37) traegt `rien` die Verneinung
vollstaendig; `n’est` = *ist*, nicht *ist nicht*. Der Unterschied zu
Mt 17,20 (`rien ne`, dort ein Mehrwort `ne rien`) ist, dass das `ne`
dort ein FREIES Token ist und hier verschmolzen.

## `chez lui` und `chez elle`

Der Bestand ist hier asymmetrisch, und das ist keine Absicht:
`chez elle` steht als Mehrwort-Lemma (Marc 7,30), `chez lui` nicht
(Mt 10,11, Marc 8,26 stehen Wort fuer Wort). `sweeplemma` meldet
folglich nur die `elle`-Faelle. Bis zur Vereinheitlichung gilt: **wie
der Bestand es fuehrt** — gemeldet vom Agenten fuer Luc 1.

## Ein Mehrwort, dem die Elision ein Token wegnimmt

`faute de` steht im Bestand mit **drei** Tokens: `faute` + `de` +
Nomen (Mt 13,6, Marc 4,6 — „faute de racines"). In Luc 8,6 heisst es
`faute d’humidité`; das `de` ist mit dem Nomen verschmolzen, und ein
Span ueber beide Tokens zoege das Nomen in die Praepositionalglosse.

**Regel:** hier wird es nicht gesetzt — die Teile stehen einzeln
(`faute` = *Mangel*, `d’humidité` = *an Feuchtigkeit*). Was die
Elision hier verschluckt, ist das **Inhaltswort**, das die Wendung
ergaenzt; ein Span darueber zoege es in die Praepositionalglosse.

**Der zweite Satz dieser Regel — „das trifft jede Wendung, deren
letztes Funktionswort `de` oder `que` ist" — war falsch** und ist
gestrichen. Siehe den naechsten Abschnitt; er ist am Bestand
gemessen.

## Zwei Mehrwoerter duerfen sich ueberlappen — aber nur einmal zaehlen

Luc 7,30 traegt `ne pas` (Positionen 10–13) und `se faire baptiser`
(Positionen 11, 12, 14) gleichzeitig; `selfcheck` und `mehrwort`
nehmen das klaglos. Der erste Fall dieser Art im Bestand.

**Regel:** die Ueberlappung ist erlaubt, aber der Verbinhalt steht nur
in **einem** der beiden. Das kleinere, geschlossene Mehrwort faellt
auf seine schlichte Bestandsreihe zurueck — hier `ne pas` = *nicht ·
not · no · non* —, damit nicht zweimal dasselbe uebersetzt dasteht.
Gemeldet vom Agenten fuer Luc 7.

## `partout où` ist ein Mehrwort — an allen fuenf Stellen

Der Bestand fuehrte es nur in Marc 6,55 und 6,56; Mt 8,19, Mt 26,13
und Marc 14,9 standen Wort fuer Wort. Der Agent fuer Luc 7 hat die
Luecke am Parallelvers zu Luc 9,57 gefunden.

Es traegt echte Auskunft: `où` allein ist *wo · where · donde · dove*,
`partout où` ist *ueberall wo · wherever · dondequiera que · dovunque*
— drei der vier Zielsprachen haben dafuer ein eigenes Wort, das aus
den Teilen nicht entsteht. Nachgetragen, alle fuenf Stellen tragen
jetzt dieselbe Reihe; die Einzelglosse darunter bleibt gerichtet
(`où` = *wohin · adonde*, wo ein Bewegungsverb folgt).

## Die Elisionsregel gilt nur nach aussen

Die Regel aus Luc 8,6 (`faute d’humidité`) heisst: wo die Elision
einem Mehrwort ein Token nimmt, bleibt es ungesetzt. Zwei Kapitel
haben ihre Grenze gefunden.

**Sie greift** bei `ce qu’on` (Luc 10,7), `ce qu’il` (Luc 12,12): das
verschluckte Wort — `on`, `il` — gehoert **nicht** zur Wendung, ein
Span darueber zoege ein Subjekt in die Relativpronomen-Glosse. Die
Teile stehen einzeln.

**Sie greift nicht** bei `Même s’il` (Marc 14,31, Luc 12,15): das
verschluckte `il` gehoert zum Nebensatz, den `même si` ohnehin
einleitet. Der Bestand setzt das Mehrwort dort, und Luc 12,15 folgt
ihm.

Die Probe ist also nicht „ist ein Token verschmolzen", sondern
**„gehoert das verschmolzene Wort in die Spanne oder hinter sie"**.

## Nachgemessen: der Bestand setzt ueber die Elision hinweg

Der Abschnitt oben war aus zwei Kapiteln geschlossen. Beim
Einsammeln von Lukas Paket 5 ist er gegen den ganzen Bestand
gehalten worden, und die Zahlen sind eindeutig: **`ce que` steht an
39 Stellen als Mehrwort ueber der Elision** (`ce qu’il`, `ce qu’elle`,
`ce qu’ils`, `ce qu’on`) und fehlte nur an dreien, die keine groessere
Spanne deckte (Luc 10,7 · Jude 1,10 zweimal). Sie sind nachgetragen.

**Wie es funktioniert:** die Spanne nimmt das verschluckte Wort mit,
und die **Glosse des Mehrworts traegt seinen Inhalt** — `ce qu’il` =
*was er · what he*, `ce qu’on` = *was man · what they*. Der Einzel-
eintrag darunter behaelt seine eigene Glosse. Nur wo ein
**Inhaltswort** verschluckt wird, das die Wendung ergaenzt
(`faute d’humidité`), bleibt das Mehrwort aus.

Dasselbe gilt fuer `parce qu’ils` (9 Stellen, alle mit Mehrwort),
`jusqu’à ce qu’il`, `de peur qu’après` und `même s’il` — gemessen von
den Agenten fuer Luc 13 und Luc 14, die beide zuerst der falschen
Fassung gefolgt waren und sie am Bestand widerlegt haben.

## `tout ce que` ist kein Mehrwort

Sechs Stellen fuehrten `tout ce que` als Dreier-Mehrwort (Marc 6,30
zweimal, Luc 2,20 · 2,39 · 9,10 · 9,43), dreissig fuehrten `tout`
einzeln neben dem Mehrwort `ce que`. Die sechs sind aufgeloest.
`tout` = *alles · all · todo · tutto* traegt sich selbst.

Am deutlichsten war die Spaltung innerhalb **eines** Kapitels:
Luc 2,27 und 2,39 haben beide `ce qu’ordonnait`, 2,27 mit dem
Mehrwort, 2,39 ohne. Jetzt beide gleich.

## `il y a`: `da` und `dort` sind zwei Lesarten, keine Spaltung

Der Agent fuer Luc 13 hat gemeldet, die italienischen Einzelglossen
unter `il y a` liefen auseinander (`y` = *ci* gegen *vi*). Sie tun es,
aber **im Gleichschritt mit dem Deutschen**:

    55 Stellen   il = es · esso    y = da · ci      das schlichte Es gibt
     8 Stellen   il = es · ci      y = dort · vi    il y a ici plus que …

Die zweite Reihe steht ausschliesslich dort, wo der Vers auf einen
Ort zeigt (Mt 12,6 · 12,41 · 12,42 · Luc 11,31 · 11,32) oder eine
Menge verortet (Mt 9,37 · Luc 10,2). Das ist eine Unterscheidung und
kein Versehen — sie bleibt.

Ebenfalls festgehalten, weil es nirgends stand: das Lemma **`il y a`**
ist den drei verneinten Existenzsaetzen ohne `pas` vorbehalten
(*es gibt nicht*); alles Uebrige traegt `il y avoir`.

## `ce que` traegt eine Reihe

Der Bestand fuehrte 106 Vorkommen auf zwölf Reihen — 64 davon
(60 Prozent) auf `ce` = *das · that · lo · ciò* und `que` = *was ·
what · que · che*. Sechs Stellen in Matthaeus standen auf
*dasjenige · welches* und waren Altlast des ersten Buchs; sie sind
auf die Mehrheit gezogen (Mt 6,3 · 6,25 · 7,12 · 10,19 zweimal ·
21,22).

**Zwei Lesarten bleiben getrennt, und der Vers entscheidet:**
wo `que` echtes Relativum ist (*was du verborgen hast*), gilt die
Reihe oben. Wo es Konjunktion eines Tatsachensatzes ist — „ne vous
réjouissez pas **de ce que** les esprits vous sont soumis" (Luc
10,20) —, ergaebe sie „freut euch nicht ueber dasjenige, welches die
Geister euch untertan sind". Dort steht `ce que` = *darueber, dass ·
the fact that · de que · del fatto che*.

Die beiden sehen gleich aus. Luc 12,29 („ne vous inquiétez pas de ce
que vous mangerez") ist trotz derselben Wendung das Relativum — der
Agent fuer Luc 10 hat das dem fuer Luc 12 vorausgesagt, und der Vers
hat ihm recht gegeben.

## `docteur de la loi` traegt eine Reihe

Der Bestand fuehrte den Singular (Mt 22,35) auf *Gelehrter · lawyer ·
doctor · dottore* und den Plural (Luc 2,46 · 5,17 · 7,30) auf
*Lehrer · teachers · maestros · maestri*. Der franzoesische Text
unterscheidet nichts; die Spaltung war ein Zufall der Reihenfolge, in
der die Buecher entstanden, und die Agenten fuer Luc 10 und Luc 11
sind ihr folgerichtig auseinandergelaufen.

Jetzt einstimmig auf der Reihe des Plurals. *Schriftgelehrter*, was
beide deutschen Zeugen sagen, ist nicht verfuegbar — das traegt
`scribe` an 45 Stellen.

**„Eine Reihe" heisst eine Glossenzeile, nicht ein Mehrwort.**
`docteur de la loi` steht Wort fuer Wort; der Agent fuer Luc 14 hat
den Satz oben als Mehrwortvorgabe gelesen und zu Recht widersprochen.

## `maître`: die drei Reihen, nachgemessen

Der Prompt-Baustein hat bis Lukas Paket 7 gesagt, der Gleichnisherr
trage *Herr · master · señor · padrone* und weiche nur bei `Seigneur`
im selben Vers auf *dueño* aus. Der Agent fuer Luc 20 hat es
gemessen: **`maître de la vigne` steht einstimmig auf *Herr · master ·
dueño · padrone*** (Mt 20,8 · Mt 21,40 · Marc 12,9), und in keiner
der drei Stellen steht ein `Seigneur`. Das Spanische unterscheidet
den *Besitzer* vom *Herrn*, unabhaengig von jeder Kollision.

Die Lage, wie sie gemessen ist:

    Anrede an Jesus       Meister · Teacher · Maestro · Maestro   (34×)
      — direkt angesprochen: „Maître, …"
    Rede ueber Jesus      Lehrer · Teacher · Maestro · Maestro    (6×)
      — „le maître te dit" (Luc 22,11 · Marc 14,14 · Mt 26,18),
        „n’importune plus le maître" (Luc 8,49 · Marc 5,35)
    Gleichnisherr         Herr · master · señor · padrone         (12×)
    Besitzer einer Sache  Herr · master · dueño · padrone         (12×)
      — `maître de la vigne`, `maître de maison`
    neben `Seigneur`      Gebieter · master · dueño · padrone     (Luc 12,42 · 13,25)

Die vierte Reihe ist die Ausweichlesart und gilt nur im
Kollisionsvers; die dritte gilt ueberall, wo `maître` einen Besitz
regiert.

## `personne ne` traegt nur die Verneinung

27 von 32 Stellen glossieren das Mehrwort als *niemand · no one ·
nadie · nessuno* und lassen dem Verb daneben seine eigene Glosse —
`Personne n’est bon` = [niemand] + `n’est` *ist*. Fuenf zogen das Verb
hinein (*keiner wagte*, *niemand hatte*); sie sind gezogen, und in
Mt 22,46 stand darunter auch noch `personne` selbst auf *keiner ·
nobody · ninguno · alcuno* statt auf der Bestandsreihe.

Das ist derselbe Grundsatz wie bei der Ueberlappung in Luc 7,30: der
Verbinhalt steht **einmal**, und zwar dort, wo das Verb steht.

## Wenn `sweeplemma` und `paketcheck` einander widersprechen

`sweeplemma` haelt eine Reihe gegen den **Bestand**, `paketcheck`
gegen die **Nachbarkapitel des laufenden Pakets**. Wo der Bestand
selbst zwei Reihen fuehrt, koennen beide recht haben und sich
widersprechen — der Agent fuer Jean 3 ist bei `rendre témoignage`
zweimal umgestellt worden.

**Dann entscheidet das Paket.** Zeichengleichheit innerhalb des
Pakets ist teurer zu reparieren als eine Abweichung gegen eine von
zwei Bestandsreihen; die Vereinheitlichung ueber die Buchgrenze ist
Sache des Koordinators, nicht des Kapitels.

## `croire en`: italienisch `in` beim Glaubensobjekt, `a` beim Zeugnis — nachgemessen

Der Bestand hatte die Praeposition nach `croire` italienisch fast durchweg
auf `a` gesetzt (15 Stellen gegen 5). **Das war die Mehrheit und trotzdem
falsch.** Der italienische Zeuge unterscheidet, und zwar sauber:

- **Glaubensobjekt** — `croire en lui/moi/celui` von Jesus: riv1927 liest
  `crede in lui` (Jean 3,15 · 3,16 · 3,18 · 4,39 · 6,29 · 6,35 · 6,40 ·
  6,47 · 2,11), `credono in me` (Mt 18,6), `crederemo in lui` (Mt 27,42).
- **Einer Aussage glauben** — `croire en lui` vom Taeufer und seiner
  Botschaft: riv1927 nimmt den Dativ, `gli credeste` / `credere a lui`
  (Mt 21,25 · Mt 21,32 viermal · Marc 11,31 · Luc 20,5), ebenso
  `ti crediamo` in Jean 6,30 („dass wir dich sehen und dir glauben").
- **`croire en son nom`** ist eine dritte Reihe: `credere nel nome`
  (Jean 1,12 · 2,23 · Marc 16,17) — Artikelverschmelzung, nicht `a`.

Die acht Johannes-Stellen sind auf `in` gezogen; die Taeufer-Stellen
bleiben auf `a`. **Wer im Bestand nur zaehlt, zieht hier in die falsche
Richtung** — deshalb steht die Regel hier und nicht die Mehrheit.

## `être` + Partizip eines Bewegungsverbs ist das Perfekt, nicht die Kopula

`je suis venu` heisst **nicht** „ich bin (jemand) Gekommenes", sondern
„ich bin gekommen". Deutsch und Italienisch bilden das Perfekt der
Bewegungsverben selbst mit `sein`/`essere` — dort ist `bin`/`sono`
richtig. **Englisch und Spanisch nicht:** dort steht `have come` und
`he venido`, nie `am come` / `soy venido`.

Der Bestand hatte an **54 Stellen** die Kopula stehen (`suis` = *am ·
soy*, `est venue` = *is · es*, `fut venu` = *was · fue*), obendrein in
fuenf `ne suis pas`-Mehrwoertern (*am not · no soy*). Der Zeuge liest
durchweg `no he venido` / `I have not come`. Alles korrigiert; die
Betroffenen sind `venir aller arriver entrer sortir monter descendre
tomber revenir passer parvenir`.

**Zwei Fallen dabei:**
- Das Partizip muss mitziehen. `est tombé` = *has **fallen***, nicht
  *has fell* (Luc 8,14 · 8,15); spanisch ist es nach `haber`
  unveraenderlich — `ha **llegado**`, nicht `ha llegada`, auch wenn
  `l'heure` feminin ist (Marc 14,41 · Luc 22,14 · Jean 4,23 · Luc 13,4).
- **`fut passé` in Marc 16,1 bleibt.** „Lorsque le sabbat fut passé" =
  *when the Sabbath was past* — hier ist `passé` adjektivisch, und
  Englisch ist mit der Kopula richtig, waehrend Spanisch mit `hubo
  pasado` das passé antérieur nimmt. Zwei Sprachen, zwei Analysen,
  beide richtig.

## Italienische Klitikahaeufung: `mi ti ci vi` werden vor `lo la li le ne` zu `me te ce ve`

`vi l'ho detto` gibt es nicht — es heisst **`ve l'ho detto`**. Dasselbe fuer
`me lo ha dato`, `te lo comando`, `ce ne sono`. Das ist Morphologie, keine
Wortstellung: die Form des ersten Klitikons aendert sich, sobald ein zweites
folgt. Der Zeuge liest `ve l'ho predetto` (Mt 24,25) und `ve l'ho gia detto`
(Jean 9,27). **39 Stellen im Bestand korrigiert.**

**`si` bleibt ausgenommen.** Beim unpersoenlichen `on le prit` dreht das
Italienische die Reihenfolge (`lo si prese`), statt `si` zu `se` zu machen —
`se lo` waere die reflexiv-dativische Lesart und etwas anderes. Eine Glosse
Wort fuer Wort kann die Umstellung nicht abbilden; die Einzelglossen bleiben
`si` und `lo`, und das ist die Wortstellung, nicht die Form.

## `pouvoir` als Nomen: `authority`, ausser neben `autorité`

11 Stellen gegen 3. Die eine berechtigte Ausnahme ist Marc 11,28, wo
`autorité` im selben Vers steht und die Kollision aufgeloest werden muss.
Jean 1,12 und 5,27 standen ohne Kollisionsanlass auf `power` — gezogen; in
5,27 liest der Zeuge ausdruecklich `authority`.

## `avoir` als Besitzverb ist spanisch `tener`, nicht `haber`

`haber` ist im heutigen Spanisch nur noch Hilfsverb und das unpersoenliche
`hay`. „habéis los pobres" ist kein Satz — es heisst `tenéis`. Der Bestand
hatte an neun Stellen das Besitzverb mit `haber` glossiert; der Zeuge liest
ueberall `tener` (`no tiene dónde recostar la cabeza` Mt 8,20 · Luc 9,58,
`siempre tendrán pobres` Mt 26,11 · Marc 14,7, `te tenía miedo` Luc 19,21).
Bemerkenswert: an drei dieser Stellen fuehrte **derselbe Vers** schon die
richtige Form — Marc 14,7 glossiert `m'aurez` mit `me tendréis` und `avez`
mit `habéis`.

**Die Gegenprobe gilt genauso.** Unter dem Mehrwort `il y avoir` stand an
**28 Stellen** `tener` oder `haber` als Vollverb (`aura` = *tendrá*, `avait`
= *tenía*, `a` = *ha*), waehrend das Mehrwort darueber richtig `habrá`,
`había`, `hay` las. Das Existenzverb ist `hay / había / hubo / habrá`, nie
`tener`: „habrá guerras", nicht „tendrá guerras". Der Einzeleintrag traegt
immer dasselbe Verb wie sein Mehrwort.

## `mort` gegen `mourir`: Zustand gegen Ereignis — der Bestand hat recht

Zwei Agenten haben die Lemmaspaltung nach `être` fuer eine Altlast gehalten,
einmal „nach Numerus". Nachgemessen ist sie inhaltlich und richtig:

- **`mort` (Adjektiv)** = *tot · dead · muerto · morto* — ein Zustand.
  `Ta fille est morte` (Marc 5,35), `il est mort` (Marc 9,26),
  `mon fils était mort` (Luc 15,24).
- **`mourir` (Partizip)** = *gestorben · died · muerto · morto* — ein
  Ereignis. `Abraham est mort` (Jean 8,52), `vos pères sont morts`
  (Jean 6,49).

Beide Zeugen machen denselben Unterschied, im selben Vers: Marc 15,44 liest
deutsch „dass er schon **tot** war … ob Jesus schon lange **gestorben** sei",
und der Bestand bildet genau das ab. Nichts zu vereinheitlichen.

## `où je vais` spanisch: `adónde` in der indirekten Frage, `adonde` im Relativsatz

Ein Agent hat die Spaltung fuer eine Altlast gehalten und wollte 8,14
nachgezogen haben. **Sie ist richtig** — es ist die spanische
Akzentorthographie, und die unterscheidet nicht Frage von Aussage, sondern
Fragesatz von Relativsatz:

- `je sais où je vais` → indirekte Frage → **`adónde`** (Jean 8,14 zweimal)
- `vous ne pouvez venir où je vais` → Relativsatz → **`adonde`**
  (Jean 8,21 · 8,22 · 13,33 · 13,36)
- `où vas-tu?` → direkte Frage → **`adónde`** (Jean 13,36)

Der Akzent haengt am Nebensatztyp, nicht am Fragezeichen. Nicht
vereinheitlichen.

## Der verneinte Teilungsartikel: `de` heisst deutsch `kein`, nicht `irgendein`

`n'auriez pas de péché`, `ne porte pas de bons fruits`. Der Bestand war
gespalten — 19 Stellen *keine*, 12 *irgendwelche/irgendein*. **Der Zeuge
entscheidet einstimmig fuer `kein`:** „dann haettet ihr **keine** Suende"
(Jean 9,41), „der **keine** guten Fruechte bringt" (Mt 7,19 · Luc 3,9),
„in dem **keine** Falschheit ist" (Jean 1,47) — und er setzt daneben nie
ein eigenes `nicht`. 12 Stellen gezogen.

Spanisch und Italienisch bleiben unveraendert: `no … ningún` und
`non … alcun` sind dort Negationskongruenz und richtig. Englisch steht
etwa halb auf `any`, halb auf `no`; beides ist mit dem `not` des
Mehrworts lesbar, deshalb nicht angefasst.

## `ne pas` mit zusammengesetzter Zeit: die Spanne ist NICHT vereinheitlichbar

Ein Agent hat gemeldet, der Bestand sei gespalten — mal liegt das Partizip
in der `ne pas`-Spanne, mal daneben — und die 38 (nachgemessen: 96)
Gegenbelege seien eine Altlast. **Nachgemessen ist es keine.**

Die Spannenbreite haengt daran, ob die Zielsprachen an derselben Stelle
teilbar sind. `n'avez pas dansé` muss das Partizip mitnehmen, weil
Spanisch `no bailasteis` daraus **ein** Wort macht — `dansé` haette dann
keine Entsprechung. `n'ai pas` + `trouvé` darf dagegen enden, weil alle
vier Sprachen zusammengesetzt bleiben (`habe nicht` + `gefunden`).

Rund die Haelfte der breiten Spannen ist so erzwungen, die andere Haelfte
waere auch schmal moeglich — aber welche, entscheidet sich **am Vers und
an vier Sprachen**, nicht an einer Regel. Wer hier maschinell
vereinheitlicht, zerschlaegt die erzwungene Haelfte. Die Regel oben („wo
es nicht dazwischensteht, bleibt es draussen") gilt als Voreinstellung,
nicht als Gesetz.

## Das zweite Token einer Konjunktion traegt die Konjunktion mit

Bei `afin que`, `parce que`, `de peur que` und ebenso bei `ce qui` faellt die
franzoesische Fuegung auf zwei Tokens, die Zielsprachen aber oft auf eines.
Der Bestand loest das nach **einem** Muster, und zwar seit Matthaeus:

- `afin` = *damit*, `qu’il` = ***dass er*** — nicht bloss *er*. 170 Stellen
  gegen 26; alle vier Sprachen machen es gleich (*dass er · that he ·
  que él · che egli*). 26 gezogen.
- `ce` = *das*, `qui` = ***was*** — nicht *welches*. „das was" ist der
  deutsche Ausdruck, „das welches" nicht, und das Mehrwort selbst liest an
  allen 130 Stellen *was*. 55 gezogen.

Die Einzelzeilen doppeln damit die Konjunktion („damit dass er"). **Das ist
gewollt und die Regel des ganzen Bestandes** — `ne` und `pas` tragen genauso
beide *nicht*. Die lesbare Fassung steht in der Mehrwortzeile; die
Einzelzeilen sagen, welches franzoesische Wort welche Funktion traegt.

**Nachgemessen ueber alle `… que`-Mehrwoerter.** `parce que` (131) und
`afin que` (118) stehen zu hundert Prozent so; gespalten waren `pendant que`
(29:16), `pour que` (23:5), `dès que` (16:4) und `tandis que` (13:3) — 27
Stellen gezogen, die eine Ausnahme ist Luc 1,44, wo `dès` = *von* und nicht
*sobald* gelesen wird.

**Drei Gruppen bleiben ausdruecklich draussen:**
- **`ce que`** liest 220 zu 13 *was* — das ist die Relativlesart und richtig;
  die 13 sind der faktive Gebrauch („darueber, dass"), eine eigene Reihe.
- **`ainsi que` (8), `ne que` (7), `tant que` (2), `où que` (1)** stehen
  einstimmig ohne. Das sind Vergleichs- und Restriktivfuegungen, keine
  Konjunktionen mit Nebensatzsubjekt.
- Ein Agent hat aus drei `dès qu’il`-Stellen geschlossen, `dès que` folge der
  Regel nicht. **Die Stichprobe war zu klein** — ueber alle Formen gemessen
  steht es 16 zu 4 dafuer.

## `être du monde` ist praedikativ, kein Genitiv

`du monde` steht 22-mal, 17-mal als echter Genitiv („la fin du monde", „le
prince du monde") — dort ist `du` = *der* richtig. Nach `être` ist es keiner:
„Si vous étiez du monde" heisst nicht „wenn ihr der Welt waeret". Der Zeuge
liest „wenn ihr zur Welt gehoeren wuerdet"; die verschmolzene Form traegt
dann Praeposition **und** Artikel, ***von der***, wie der Bestand es fuer
`vom` (21x) und `aus dem` (12x) ohnehin tut. Jean 15,19 zweimal gezogen;
Jean 8,23 (`de ce monde`) stand schon richtig auf *von*.

## `chez lui` / `chez eux` sind Mehrwoerter wie `chez elle` / `chez elles`

Der Bestand fuehrte `chez toi` (4x), `chez elle` und `chez elles` als
Mehrwort = *nach Hause · to her house · a su casa · a casa sua*, die
maskulinen Formen aber Wort fuer Wort. Dort las das Deutsche dann
`chez` = *zu* + `lui` = *ihm*, also „er ging **zu ihm**" fuer „er ging
nach Hause" — waehrend Spanisch mit `a casa de él` und Italienisch mit
`da` die Wendung laengst richtig trugen. Die Spaltung lief allein am
Genus des Pronomens, und das ist kein Grund.

Sechs Mehrwoerter angelegt: Marc 8,3 · 8,26 · Luc 1,23 · 5,25 · 18,14 ·
24,12. **Nicht angelegt** in Luc 16,4 (`qu'ils me reçoivent chez eux` =
in ihre Haeuser aufnehmen, nicht selbst heimgehen — der Bestand
markiert das schon durch it `presso` statt `da`) und ueberall dort, wo
`chez` wirklich „bei" heisst (Jean 14,23 `notre demeure chez lui`,
Luc 11,37, Mt 26,18).

Gemeldet vom Agenten fuer Johannes 20, der die Luecke sah und der
Weisung „wie der Bestand es fuehrt" folgend nichts gesetzt hat. Das
war richtig — die Luecke gehoert dem Koordinator, nicht dem Kapitel.

## Italienisch: die Praeposition verschmilzt nie in ein Possessiv

`de ses prophètes` heisst `di` + `i suoi profeti`, nicht `di` + `dei suoi`.
Der Bestand fuehrt das an 36 Stellen richtig und hatte fuenf Ausreisser
(Luc 1,70 `dei suoi`, Luc 1,77 `dei loro`, Marc 6,22 · Luc 5,7 · Luc 18,7
`ai suoi`/`ai loro`) — zusammengelesen ergibt das `di dei suoi` und
`a ai suoi`. Alle fuenf gezogen. Das ist dieselbe Artikelregel wie beim
Teilungsartikel: **die Praeposition bleibt bar, der Artikel sitzt beim
Nomen.**

**Nicht zu verwechseln** mit dem Teilungsartikel nach einer Praeposition:
`avec des vases` = `con` + `delle vasi` ist richtig, denn `delle` ist dort
kein verschmolzener Artikel, sondern das italienische Teilungswort. Die
Regel greift nur, wenn ein **Possessiv** folgt.

## `Fils de l’homme`: die eine Formel, die den Artikel in der Praeposition traegt

Die Artikelregel („`de` vor einem Artikel traegt italienisch nur `di`, der
Artikel bleibt bei seinem Token") hat **eine gemessene Ausnahme**, und sie
ist einstimmig: `Fils de l’homme` steht **86 zu 0** auf `de` = *dell’* mit
barem `l’homme` = *uomo*. Zusammengelesen ergibt beides dasselbe richtige
`dell’uomo`; die Formel hat sich nur fuer die andere Aufteilung entschieden
und haelt sie ohne Ausnahme durch.

**Nicht angleichen.** Der Agent fuer Actes 7 hat den Widerspruch bemerkt,
gemessen und zugunsten des Bestands entschieden — das war richtig. Beim
Nachmessen fiel dabei die einzige Stelle auf, an der die Aufteilung
schiefging: Jean 1,13 `volonté de l’homme` las `di` + bares `uomo`, also
gar keinen Artikel. Gezogen.

Ausserhalb der Formel gilt die Regel unveraendert: `hors de l’homme` und
`au sujet de l’homme` stehen richtig auf `di` + `l’uomo`.

## `avoir été` ist der Perfekt-Infinitiv von `être`, nicht von `avoir`

`Après avoir été relâchés` heisst „nachdem sie freigelassen worden
**waren**", nicht „hatten". Der Agent fuer Actes 15 hat sich zuerst an die
57 Belege von `folgenreihe "Après avoir"` gehalten — **und die messen eine
andere Konstruktion.** Dort steht der aktive Perfekt-Infinitiv (`après
avoir dit`, `après avoir prié`), und da ist `hatten` richtig. Sobald `été`
folgt, ist es Passiv oder Kopula, und Deutsch braucht `war`/`waren`.

Der Bestand fuehrt es an zwei Stellen richtig (Actes 4,13 · 4,23) und hatte
zwei Ausreisser: Luc 10,36 (`avoir été le prochain` = *zu haben* statt
*zu sein*) und Luc 19,15 (`après avoir été fait roi` = *hatte* statt *war*).
Beide gezogen.

**Die allgemeine Lehre, und sie ist teuer bezahlt: die Mehrheit einer
Zeichenkette ist keine Mehrheit einer Konstruktion.** `folgenreihe` sucht
Zeichen, nicht Grammatik. Wo eine Folge zwei Konstruktionen mischt, zieht
ihre Mehrheit in die falsche Richtung.

## Plural-`des` im Skopus einer Verneinung bleibt `einige`

Der Agent fuer Actes 17 hat gefragt, ob `n’habite pas dans **des** temples`
deutsch wirklich *einigen Tempeln* tragen soll — der Zeuge liest „wohnt
nicht in Tempeln", ganz ohne Artikel. **Gemessen: der Bestand setzt die
`einige`-Reihe in 96 verneinten Versen genauso wie in den 260
unverneinten.** Die Verneinung steht am Verb, nicht am Artikel; das
franzoesische `des` ist hier der schlichte unbestimmte Plural.

**Nicht zu verwechseln mit `pas de`** — dort ersetzt `de` den Artikel und
traegt die Verneinung mit, und dort heisst es deutsch `kein` (siehe den
Abschnitt „Der verneinte Teilungsartikel"). Der Unterschied ist die
Praeposition davor: `pas de temples` = *keine Tempel*, `pas dans des
temples` = *nicht in einigen Tempeln*.

Dass Deutsch den Artikel in der laufenden Uebersetzung fallen laesst,
aendert daran nichts: die Glosse sagt, was das franzoesische Token
leistet, und das Token ist da.


## Die Elisionsregel gilt fuer verschluckte INHALTSWOERTER, nicht fuer Pronomen

Die Regel „wo die Elision das Komplement verschluckt, steht kein
Mehrwort" (der `faute d’humidité`-Fall) hat zwei Agenten in die Irre
gefuehrt — sie haben bei `du milieu d’elles` und `s’empara d’eux` kein
Mehrwort gesetzt und es ausdruecklich so begruendet.

**Nachgemessen ist die Regel zu weit gefasst.** `au milieu de` steht mit
elidiertem Pronomen (`d’eux`, `d’elles`) an **13 Stellen, und 12 tragen
das Mehrwort** — Mt 18,2 · 18,20 · Marc 9,36 · Luc 4,30 · 24,36 ·
Jean 20,19 · 20,26 · Actes 4,7 · 7,26 · 17,33 · 22,30 · 23,10 · 24,21.
Die eine Ausnahme war Actes 15,14; sie ist gezogen.

**Der Unterschied ist, was die Elision verschluckt:**

- ein **Inhaltswort** (`faute d’humidité` — das Nomen, das die Wendung
  ergaenzt): kein Mehrwort, die Wendung ist nicht vollstaendig da.
- ein **Pronomen** (`d’eux`, `d’elles`): Mehrwort. Das Pronomen ist die
  Ergaenzung selbst, nicht ein Teil der Wendung, und die Glosse des
  Mehrworts nimmt es mit („aus ihrer Mitte").
- ein **Relativpronomen** (`desquels`, Actes 20,25): kein Mehrwort — es
  gehoert syntaktisch **hinter** die Spanne, nicht hinein.

Nicht zu verwechseln mit `Vers le milieu de la fête` (Jean 7,14) und
`Vers le milieu de la nuit` (Actes 16,25): dort heisst `milieu` die
zeitliche Mitte, nicht „mitten unter". Beide stehen zu Recht Wort fuer
Wort.

## Die Elisionsregel, dritte Richtung: was von AUSSEN verschluckt wird

Zwei Agenten haben unabhaengig denselben neuen Fall gemeldet, und er
gehoert zur Regel dazu:

- **Actes 28,19 `d’en appeler`** — die Elision zieht das `de` mit hinein,
  das `forcé de` regiert. Es gehoert nicht zur Wendung, sondern kommt von
  aussen. Das Mehrwort steht trotzdem; das Token traegt die
  `en`-Einzelreihe (*darauf · of it · de ello · ne*).
- **Roemer 2,11 `point d’acception de personnes`** — hier verschluckt die
  Elision den verneinten Teilungsartikel, der **vor** der Wendung steht.
  Auch hier steht das Mehrwort; der Einzeleintrag traegt die Verneinung
  (*kein Ansehen*), das Mehrwort bleibt unverneint wie in Actes 10,34.

Damit sind es drei Faelle, und der Unterschied ist immer derselbe:
**gehoert das verschluckte Wort zur Wendung oder nicht?**

    verschluckt die Wendung selbst  →  kein Mehrwort  (`faute d’humidité`)
                                   ABER NUR, wenn danach WENIGER ALS
                                   ZWEI freie Token uebrig sind — siehe
                                   den Abschnitt unten
    verschlucktes Pronomen ist die
      Ergaenzung der Wendung        →  Mehrwort       (`du milieu d’eux`)
    verschlucktes Wort kommt von
      aussen (Rektion, Verneinung)  →  Mehrwort       (`d’en appeler`)
    verschlucktes Relativpronomen   →  kein Mehrwort, es gehoert HINTER
                                       die Spanne     (`au milieu desquels`)

## `par` vor Person und Pronomen: drei Konstruktionen, nicht eine Reihe

Der Bestand las `par` vor `Jésus-Christ`, `lui`, `celui` in zwei Reihen,
und die Grenze dazwischen war mit „personaler Mittler" begruendet. Der
Agent fuer Roemer 7 hat gemeldet, dass Roemer sie selbst 3:2 verletzt
(1,8 und 2,16 lesen die Sach-Reihe, obwohl Christus dort Mittler ist).

**Am Zeugen nachgemessen ist die Begruendung falsch und die Meldung
richtig.** riv1927 trennt nicht nach Person, sondern nach Konstruktion:

    Passiv-Agens        `baptisés par lui`   → da lui
                        von · by · por · da
    Schwurformel        `jurer par celui`    → per colui
                        bei · by · por · per
    instrumental        alles uebrige        → per mezzo di
                        durch · through · por medio de · per mezzo di

In elf gemessenen Faellen liest der Zeuge zehnmal `per mezzo di`; der
elfte (Actes 4,10) formuliert um (`per virtù sua`) und hat gar kein
Gegenstueck. **Roemer 7,11 entscheidet die Frage**: dort meint `par
lui` das GEBOT, keine Person, und riv liest trotzdem `per mezzo di`.
Elf Zeilen nachgezogen (Jean 1,7 · 1,17 · 3,17 · Actes 2,22 · 4,10 ·
10,36 · 13,38 · 13,39 · Roemer 1,8 · 2,16 · 7,11); Actes 10,36 war in
sich gespalten (es *por*, it *per mezzo di*).

Merksatz derselben Bauart wie die beiden aelteren: **eine Grenze, die
sich aus der Bedeutung begruenden laesst, ist damit noch nicht die
Grenze, die der Zeuge zieht.** Erst messen, dann begruenden.

## Spanisch: nach `haber` stimmt das Partizip NIE ueberein

Italienisch stimmt es ueberein, wenn ein Objektklitikon vorangeht (`li
hanno dati`, `le avevano adempiute`) und darf es im Relativsatz
(`la parola che ha pronunciata`) — **spanisch nie.** Nach jeder Form
von `haber` steht das Partizip unveraendert auf `-o`.

Gemeldet vom Agenten fuer Roemer 6 an einer Stelle des Nachbarkapitels
(7,6 `habiendo muertos`); der Sweep fand **dreizehn**. Zwei davon waren
kein Kongruenzfehler, sondern das falsche Hilfsverb: `étaient/furent
réunies` ist Zustand, nicht Perfekt — spanisch `estaban`/`estuvieron`,
nicht `habían` (der Zeuge liest `erano radunate`, `furono radunati`).

Und eine Falle in der Gegenrichtung: bei Mt 27,10 stand it `hanno date`
neben dem Klitikon `li`. Das Klitikon ist richtig — riv liest `li
diedero`, `sicli` ist maskulin —, das Partizip musste ihm folgen
(`dati`). **Franzoesisches und italienisches Genus laufen hier
auseinander** (`les pièces` feminin, `i sicli` maskulin); wer die
Kongruenz prueft, prueft sie innerhalb einer Sprache, nie gegen das
Franzoesische.

## `hints.py` sah nicht durch die Elision (behoben)

Der Stammschluessel kam aus den ersten vier Zeichen, und `l’af…` landet
in einem anderen Eimer als `affection`. Damit standen elidierte Nomen
ohne „verwandt"-Zeile da, obwohl ihr Lemma dutzendfach belegt war —
im Franzoesischen trifft das jedes vierte Nomen. Gefunden vom Agenten
fuer Roemer 8, dem es beinahe ein falsches Level gekostet haette
(`affection` B2 statt B1; `levelcheck` fing es). Gesucht wird jetzt in
beiden Eimern; `d’abord` behaelt seinen eigenen.

## Der erste Durchgang von `mehrwoerter.py` ueber alle 145 Kapitel

233 Treffer, geballt auf gut dreissig Signaturen. **Der weitaus groesste
Teil war kein Fehler, sondern ein Kriterium**, das der Bestand richtig
anwendet und das hier stehen soll, damit es niemand noch einmal
herleitet:

    à pied / aux pieds   dieselbe Signatur, zwei Wendungen: `à pied`
                         (zu Fuss, 3× Mehrwort) gegen `aux pieds`
                         (zu Fuessen, 14× woertlich). Kein Fall.
    de quoi              Idiom vor Infinitiv (`n’ayant pas de quoi
                         payer`) = Mehrwort; Fragewort (`de quoi
                         discutez-vous`) = woertlich.
    alors que            temporale Konjunktion (`Alors qu’il passait`)
                         = Mehrwort; `alors` + jussives `que` (`alors
                         que ceux de Judée fuient`) und die Spaltform
                         (`c’est alors que`) = woertlich.
    d’en haut            = Mehrwort (von oben); `du haut de` = woertlich.
    faire lever          Sonne und Teig gehen auf = Mehrwort; einen
                         Menschen aufrichten = woertlich.
    en bas               ortsfest (`en bas sur la terre`) = Mehrwort,
                         weil das Deutsche fuer `en` kein Wort hat;
                         gerichtet (`jette-toi en bas`) teilt sich
                         sauber in *nach · unten*. Ebenso `en haut`.
    en tout              vor einer ZAHL (`en tout douze hommes`) =
                         Mehrwort *insgesamt*; `en toute humilité` ist
                         etwas anderes.
    un autre             pronominal = Mehrwort, vor folgendem Nomen
                         nicht (`une autre loi`).
    bien des             = viele; `bien de` in `il n’est pas bien de`
                         ist woertlich.

**Sieben echte Uneinheitlichkeiten, alle angeglichen:**

    Mt 21,30    `la même chose`  stand woertlich (*gleiche Ding*),
                waehrend Mt 26,35 und Mc 14,31 dieselbe Form als
                Mehrwort *dasselbe* fuehren.
    Mt 23,30    `du temps de`    dieselbe Form und dieselbe Glosse wie
    Mc 2,26                      die vier Mehrwortstellen.
    Mc 1,26     `pousser un cri` vier Stellen woertlich gegen zwei als
    Mc 5,38                      Mehrwort. **Der Zeuge entscheidet**:
    Ac 7,57                      l1912mod liest an allen sechs ein
    Ac 8,7                       einziges Verb (*schrie laut auf*,
                                 *schrien*), riv ebenso (*gridando*,
                                 *urlava*). Das Idiom ist ueberall da.

**Offen gelassen:** `se trouver`. Mt 12,10 · Mc 3,1 · Lc 6,6 fuehren
`s’y trouvait` als Mehrwort, Mt 10,11 dieselbe Form nicht. Beide
Zeugen umschreiben an beiden Stellen (*Dort war ein Mann*, *wer dort
es wert ist*) und entscheiden also nichts; die Konstruktionen sind
zudem nicht ganz dieselbe (Existenzsatz gegen eingebetteten
Fragesatz). Hier ist die Uneinheitlichkeit der Befund.

## Die invertierte Verbform: meine Regel war falsch

In den Prompts stand ueber Jahre: „die invertierte Verbform traegt das
Subjekt in de/en/es, **nicht** im Italienischen". Der Agent fuer
Roemer 10 hat sie an allen **720** invertierten Einzeltokens des
Bestands nachgemessen und widerlegt. Nachgerechnet stimmt seine
Zaehlung auf das Token genau:

    312   nur de + en          (`serez-vous` → werdet ihr · will you)
    231   alle vier            (`Es-tu` → Bist du · Are you · Eres tú · Sei tu)
    112   keine                (Imperative: `Repentez-vous`)
     51   de + en + it         (`vend-on` → verkauft man · does one · se venden · si vendono)
      9   nur de   ·  2 nur en  ·  1 de+es+it
      0   de + en + es OHNE it

Die behauptete Kombination gibt es **kein einziges Mal**. Der einzige
Beleg, der so aussieht, ist Marc 8,4 (`pourrait-on` → es *podría uno*,
it *si potrebbe*) — und dort ist die italienische `si`-Konstruktion die
richtige Wiedergabe des unpersoenlichen `on`, nicht ein fehlendes
Subjekt.

**Was wirklich gilt:** Deutsch und Englisch tragen das Subjekt fast
immer, weil sie es muessen (Verbzweitstellung, `do`-Umschreibung).
Spanisch und Italienisch tragen es nur, wo die franzoesische Inversion
betont ist — und dann **gemeinsam**. Spanisch ohne Italienisch kommt
nicht vor.

Roemer selbst liest an allen fuenf eigenen Stellen alle vier
(`ont-ils`, `régneront-ils`, `est-il`, `fut-elle`, `condamnera-t-il`),
und die Fragekette in 10,14 folgt dem.

Das ist die zwoelfte meiner Prompt-Angaben, die ein Agent am Quelltext
widerlegt hat, und die erste, die als *Regel* formuliert war statt als
Beobachtung. **Eine Regel im Prompt ist so lange eine Behauptung, bis
sie jemand gezaehlt hat.**

## Konjunktion + elidierter EIGENNAME — die vierte Zeile der Elisionstabelle

Gemessen vom Agenten fuer Roemer 9, nachgerechnet: im ganzen Bestand
gibt es genau zwei annotierte Faelle, und beide machen es gleich.

    Jean 12,39   `parce qu’Ésaïe`     Mehrwort [parce que] *weil Jesaja*
                 Einzeleintrag        Lemma `Ésaïe`, Glosse *dass Jesaja*
    Actes 19,1   `Pendant qu’Apollos` Mehrwort [pendant que] *Während Apollos*
                 Einzeleintrag        Lemma `Apollos`, Glosse *dass Apollos*

Der verschluckte Name ist das **Subjekt des Nebensatzes**, kommt also
von aussen in die Wendung — das ist Zeile 3 der Tabelle (`d’en
appeler`), nicht Zeile 1 (`faute d’humidité`). Das Mehrwort wird
gesetzt, und der Einzeleintrag behaelt das Lemma des NAMENS, nicht das
der Konjunktion.

Ohne vorangehendes Konjunktionswort steht `qu’<Name>` allein und
bekommt kein Mehrwort — so die uebrigen vierzehn Stellen (`qu’Élie`
6×, `qu’Abraham` 3×, `qu’Archélaüs`, `qu’Énoch` …).

## Fuenfmal jetzt: ein „Werkzeugfehler", der eine abgeschnittene Ausgabe war

`folgenreihe` (dreimal `| head`), `folgenreihe` noch einmal
(„doppelte Zeilen" — ein Artefakt des Aufrufs, nicht reproduzierbar)
und zuletzt `belegt.py "L’aîné"` („meldet NICHT belegt und nennt das
Lemma nicht"). Nachgeprueft nennt `belegt.py` das Lemma `aîné` in der
dritten Zeile, mit geradem **und** typografischem Apostroph — die
Meldung „im Bestand NICHT belegt" steht nur davor.

**Die Ausgaben dieser Werkzeuge sind so gebaut, dass die Antwort UNTER
der Zusammenfassung steht.** Wer sie abschneidet, sieht die Frage und
nicht die Antwort.

Richtig an derselben Meldung war die andere Haelfte: `hints_45_9.md`
hatte fuer `L’aîné` keine „verwandt"-Zeile. Das ist kein Fehler von
`hints.py`, sondern **Alter**: die Promptdateien sind Momentaufnahmen
von `fravorb.py`, und die Elisionskorrektur kam nach ihrer Erzeugung.
Wo eine Promptdatei und ein Live-Aufruf sich widersprechen, hat der
Live-Aufruf recht.

## Die Elisionsregel, Zeile 1, praezisiert: es zaehlt, was FREI uebrig bleibt

Zeile 1 der Tabelle („verschluckt die Wendung selbst → kein Mehrwort")
war zu grob und hat gerade einen Fehler erzeugt. Der Agent fuer
Roemer 10 hat sich auf sie berufen und `au sujet d’Israël` (10,21) ohne
Mehrwort gelassen; `konvention.py` hat es gemeldet, und **das Werkzeug
hatte recht**. Gemessen ueber den ganzen Bestand:

    Mt 5,32    [pour cause de]  «pour cause»  + `d’infidélité`
    Mt 14,3    [à cause de]     «à cause»     + `d’Hérodias`
    Mc 6,17    [à cause de]     «à cause»     + `d’Hérodias`
    Lc 3,19    [au sujet de]    «au sujet»    + `d’Hérodias`
    Rm 9,27    [au sujet de]    «au sujet»    + `d’Israël`
    Rm 11,20   [pour cause de]  «pour cause»  + `d’incrédulité`

**Sechs von sechs setzen das Mehrwort und kuerzen den Span** auf die
freien Token. Roemer 10,21 war die einzige Ausnahme im ganzen Bestand
und ist nachgezogen.

Der Unterschied zu `faute d’humidité` ist nicht die Elision, sondern
die **Zahl der freien Token**: `faute de` hat zwei Token, eines davon
wird verschluckt, und ein einziges Token traegt kein Mehrwort. `à cause
de` und `au sujet de` haben drei, davon bleiben zwei frei — und zwei
Token sind eine Spanne.

    Regel:  Wendung verschluckt ihr eigenes letztes Wort
              → Mehrwort ueber die FREIEN Token, wenn es mindestens
                zwei sind; sonst gar keines.

    ACHTUNG: Diese Zaehlregel ist ueberholt. Sie gab an den sechs
    gemessenen Stellen die richtige Antwort aus dem falschen Grund.
    Was wirklich zaehlt, steht weiter unten unter „Die Elisionsregel,
    zum zweiten Mal praezisiert".

Gefunden hat die Spanne der Agent fuer Roemer 11 am Beleg Mt 5,32, und
er hat ausdruecklich darum gebeten, sie hier festzuhalten. Beide
Agenten haben dieselbe Konstruktion im selben Paket entgegengesetzt
entschieden — das ist der Beweis, dass die Regel fehlte und nicht nur
missverstanden wurde.

## `devant` spanisch: `ante` vor Gericht, `delante de` im Raum

Gemeldet vom Agenten fuer Roemer 12 als Paket-gegen-Bestand-Konflikt
(er stand auf *delante de*, das Nachbarkapitel auf *ante*). Gemessen
ist es **kein** Konflikt, sondern ein Kriterium, das die
Apostelgeschichte durchhaelt und die anderen Buecher nicht kannten:

    Mt 27 : 0     Mc 12 : 0     Jn 4 : 0      →  nur `delante de`
    Lc 43 : 9     Ac 15 : 34                  →  beide, nach Bedeutung

Actes trennt sauber: `delante de` fuer Raum und Gegenwart (`devant la
porte`, `devant moi`, `devant Dieu`), **`ante` fuer das Auftreten vor
einer Instanz** (`ante Pilato`, `ante el sanedrín`, `ante el tribunal`,
`ante reyes y gobernadores`). Lukas macht es an neun von elf Stellen
mit.

**Der Beweis, dass es dieselbe Sache ist und nicht zwei:** `devant des
gouverneurs` steht dreimal, in derselben synoptischen Aussage — Lc
21,12 liest `ante`, Mt 10,18 und Mc 13,9 lasen `delante de`. Vier
Stellen nachgezogen (Mt 10,18 · Mt 27,11 · Mc 13,9 · Lc 23,1), alle
vier das Auftreten vor einem Gericht oder Statthalter.

Roemer 14,10 (`devant le tribunal de Dieu`) bleibt deshalb auf `ante`
und 12,17 / 14,11 / 14,22 auf `delante de` — beide Agenten hatten
recht, und der gemeldete Konflikt war die Regel.

## `joie` spanisch: `gozo` war eine Drift, keine Lesart

38 `alegría` gegen 5 `gozo`, ueber vier Buecher verstreut, ohne
erkennbares Kriterium. Entschieden hat wieder die Parallele: **`avec
joie` liest siebenmal `alegría` und einmal `gozo` — und dieses eine
(Lc 8,13) ist das Gleichnis vom Saemann, dessen Parallelen Mt 13,20 und
Mc 4,16 `alegría` lesen.** Alle fuenf nachgezogen.

## Offen und gemessen: jussives `que` englisch

`Que celui qui …` steht englisch 58× auf `may/May` und 21× auf
`let/Let`. Ein Kriterium ist nicht zu sehen — die schaerfste Stelle ist
das Vaterunser, wo **Mt 6,9 `May` und Mt 6,10 `let` liest**, zwei
aufeinanderfolgende Zeilen desselben Gebets. Roemer ist in sich
einstimmig auf `Let` (3,4 · 6,12 · 11,9 · 11,10), und Kapitel 14 ist
dem gefolgt; `folgencheck` meldet die Zeichengleichheit mit Luc 3,11
deshalb zu Recht als Abweichung.

**Nicht angeglichen** — 79 Stellen, und ohne Kriterium waere es eine
Muenze. Wer es anfasst, faengt am Vaterunser an.

## `de notre Seigneur`: die Meldung war richtig gemessen und falsch gefolgert

Der Agent fuer Roemer 15 hat gemeldet, `notre` stehe an den drei
Bestandsstellen von `de notre Seigneur` auf *unserem*, obwohl es
deutsche **Genitive** seien („im Namen unseres Herrn"), und hat 15,6
abweichend auf *unseres* gesetzt.

Die drei Stellen sind richtig gezaehlt. Die Folgerung geht daneben,
weil sie das Nachbartoken nicht mitliest: **das `de` selbst steht auf
*von***, und nach *von* verlangt das Deutsche den Dativ. „Vater von
unserem Herrn" ist richtig, „Vater von unseres Herrn" ist es nicht.
Sechs Stellen, fuenf auf *unserem* — 15,6 ist zurueckgenommen.

Daraus die allgemeine Form: **eine Kasusfrage an einem Token ist nie
an diesem Token allein zu entscheiden.** Der Kasus haengt an der
Praeposition davor, und die traegt in dieser Ausgabe ihre eigene
Glosse. Wer nur die Spalte des Possessivs vergleicht, sieht den Kasus
nicht, der ihn regiert.

## `par` nach `exhorter` und `prier` ist keine vierte Konstruktion

Der Agent fuer Roemer 15 hat vorgeschlagen, die `par`-Tabelle um eine
Zeile zu erweitern, weil `Je vous exhorte … par notre Seigneur`
(15,30) nicht die Mittler-Reihe von 5,1/5,11 tragen kann. Gemessen
ueber alle Stellen mit `exhorter`/`prier`/`supplier`/`conjurer` davor:

    Rm 12,1    par les compassions de Dieu   durch · by · por · per
    Rm 15,30   par notre Seigneur            durch · by · por · per
    Ac 19,13   par Jésus (Beschwoerung)      bei · by · por · per
    Ac 15,32   par plusieurs discours        mit · with · con · con

Es braucht keine neue Zeile: 15,30 faellt auf die gewoehnliche
Sach-Reihe, und Roemer ist mit 12,1 in sich einstimmig. Was die
Konstruktion bestimmt, ist **das Verb davor, nicht das Nomen
dahinter** — dieselbe Zeichenkette `par notre Seigneur` traegt in 5,1
die Mittler-Reihe und in 15,30 die Sach-Reihe, weil dort `réconciliés`
steht und hier `exhorte`.

## Zeugenfehler: `Herodian` in l1912mod (Roemer 16,11)

Der deutsche Zeuge liest `Herodian`, die drei anderen lesen `Herodion`,
`Erodione`, `Herodión`. Die Form kommt im ganzen deutschen Zeugen
**genau einmal** vor — an dieser Stelle. Das ist ein Ausrutscher der
Modernisierung, keine deutsche Namensform; gesetzt ist `Herodion`.

Die Regel „der Zeuge ist massgeblich" bleibt fuer die Agenten
unveraendert. Der Agent fuer Roemer 16 hat richtig gehandelt: er hat
den Zeugen gesetzt und den Verdacht gemeldet, statt ihn selbst zu
ueberschreiben. **Einen nachgewiesenen Einzelfehler des Zeugen
korrigiert das Einsammeln, nicht das Kapitel.**

## `esprit`: meine Regel war zu absolut

In den Prompts stand seit Johannes: „Lemma immer `esprit`, deutsch
IMMER *Geist*; en/es/it folgen der franzoesischen Grossschreibung."
Der Agent fuer 1. Korinther 2 hat den ersten Teil widerlegt.
Nachgerechnet ueber alle **145** Eintraege:

    138  *Geist* in allen Kasus und Numeri
      7  *Sinn · Sinne · Verstand · Gemueter*
         Lc 9,46 (`vint à l’esprit`) · Lc 21,14 (`mettez dans l’esprit`)
         Lc 24,45 (`ouvrit l’esprit`) · Lc 8,35 · Mc 5,15 (`bon sens`)
         Ac 14,2 (`aigrirent les esprits`) · Ac 14,22

Alle sieben meinen den Sinn, nicht den Geist, und sind richtig gefasst.
Die Regel lautet also:

    Lemma            immer `esprit`, Level immer A2
    Grossschreibung  en/es/it folgen dem franzoesischen Quelltext
                     (54 von 145 gross; zwei Ausnahmen, Jean 4,24 und
                     Jude 1,19)
    Deutsch          folgt der BEDEUTUNG: *Geist*, wo es der Geist ist,
                     *Sinn/Verstand/Gemuet*, wo es der Sinn ist.

Die „116:2" aus den alten Prompts war die Zahl der **Ausnahmen** zur
Grossschreibungsregel, nicht die der Belege — auch das ist korrigiert.

## `Pour moi` / `Pour vous`: die Asymmetrie sass woanders

Der Agent fuer 1. Korinther 2 hat gemeldet, der topikalisierende
`Pour X` stehe fuer `vous` und `nous` als Mehrwort und fuer `moi` Wort
fuer Wort, die Grenze laufe also an der Person. Nachgemessen ueber
alle 133 `pour` + Pronomen liegt sie woanders — sie laeuft an der
**Glosse**:

    Mehrwort (5)     Mt 28,5 · Lc 9,44 · Lc 23,41 · Rm 16,19 · Jud 1,20
    woertlich, aber
    schon als Topik
    glossiert (2)    Lc 24,52 `Pour eux` · Rm 8,9 `Pour vous`
    woertlich, als
    Zweck glossiert  alle uebrigen (`für`, `um`)

**Roemer 8,9 und 16,19 sind dieselbe Wendung im selben Buch, tragen
Wort fuer Wort dieselben vier Glossen (*Was · As for · En cuanto a ·
Quanto a*), und nur eine hat das Mehrwort.** Dasselbe bei Lc 24,52
gegen Lc 9,44. Beide nachgezogen; `pour eux` ist damit ein neues
Mehrwortlemma neben `pour vous` und `pour nous`.

Die neun `Pour moi`-Stellen bleiben, wie sie sind: sie lesen deutsch
*Für*, nicht *Was*, und ob der Topikalisierer dort besser *Was mich
angeht* hiesse, ist eine andere Frage als die nach dem Mehrwort. Sie
ist gemessen und offen.

## `par` + Relativpronomen nimmt die Mittler-Reihe NIE

Die drei Konstruktionen von `par` gelten fuer `par` + Nomen oder
Personalpronomen. Vor einem **Relativum** (`par qui`, `par lequel`,
`par laquelle`) liegt die Sache anders, und zwar einstimmig:

    14 von 14 Stellen lesen spanisch `por` und italienisch `per`.
    Keine einzige liest `por medio de` / `per mezzo di`.

Deutsch und Englisch schwanken zwischen *durch · by* und *durch ·
through* — das folgt dem Vers. Spanisch und Italienisch schwanken
nicht.

**Roemer 5,11 entscheidet es in einem einzigen Vers:** dort steht `par
notre Seigneur Jésus-Christ` auf der Mittler-Reihe (*por medio de · per
mezzo di*) und wenige Token weiter `par qui`, das auf **denselben
Christus** zeigt, auf *por · per*. Der Ausloeser ist also weder der
Referent noch das Verb davor, sondern die **grammatische Form der
Ergaenzung**.

Gefunden vom Agenten fuer 1. Korinther 8, der die Regel richtig als
unanwendbar erkannt hat, statt sie zu erzwingen.

## Eine Luecke, die kein Mehrwortwerkzeug sieht: die Spiegelwendung

`de plus` steht im Bestand als Mehrwort (Luc 3,13 · 12,4). Sein
Gegenstueck `de moins` stand nirgends — und 1. Korinther 8,8 stellt
`rien de plus` und `rien de moins` symmetrisch nebeneinander.

Keines der drei Werkzeuge kann das melden: `sweep` und `sweeplemma`
brauchen Deckung ueber der Schwelle, `mehrwoerter` deckt das
Mittelfeld ab — eine Signatur mit **null** Bestandsvorkommen faellt
durch alle drei. Gefunden hat es der Agent, weil das Geschwister im
selben Vers stand.

Merksatz: **wo der Vers ein Paar bildet und der Bestand nur eine
Haelfte kennt, ist die andere Haelfte zu pruefen** — kein Lauf fragt
danach.

## Was `folgenreihe` seit dem letzten Paket kann — und was `sweeplemma` nicht kann

Diese beiden Abschnitte fehlten. Ich habe drei Agenten in ihren
Auftraegen auf sie verwiesen, bevor ich sie geschrieben hatte; der
Agent fuer 1. Korinther 10 hat es gemerkt, weil er nachgeschlagen hat
statt es zu glauben. **Ein Prompt, der auf einen Abschnitt verweist,
ist kein Beleg dafuer, dass es ihn gibt.**

**`folgenreihe` zeigt stammverwandte Mehrwortlemmata.** Wenn die
Zeichenkette weder als Folge noch als Lemmaname trifft, sucht der Lauf
nach Mehrwortlemmata, die dieselben Inhaltswoerter im Stamm haben.
Anlass war `il vaut mieux`: der Lauf schrieb „Auch nicht als Lemma
eines Mehrworts im Bestand", waehrend `valoir mieux` mit elf Belegen
dasteht. `valu mieux` findet jetzt `valoir mieux` und `aimer mieux`,
`garde le silence` findet `garder le silence`.

**`sweeplemma` ist blind fuer Mehrwoerter, deren Lemmaname nicht die
Verkettung der Einzellemmata ist.** Es baut die Signatur aus den
Lemmata, die der Agent selbst gesetzt hat: `c’est moi` wird zu
(`être`, `moi`), gesucht wird `être moi`, gefunden nichts. `c’est
ainsi que` ebenso. **Sein Verdachtsblock ist deshalb wertvoller als
sein Mehrwortblock** — er zeigt auf etwas, das er selbst nicht
benennen kann; geh jedem Verdacht mit `folgenreihe` und `belegt.py`
nach. Gemeldet vom Agenten fuer 1. Korinther 7, der `c’est moi` und
`c’est ainsi que` nur so gefunden hat.

## `folgenreihe` vergleicht klein — und warnt jetzt davor

Der kleingeschriebene Vergleich ist gewollt (`il y avait là` fand
sonst nichts, weil der Bestand `Il` schreibt). Am Satzanfang ist er
harmlos. Mitten im Satz ist er es nicht:

    folgenreihe "même Esprit"  →  zeigte eine Reihe aus 1 Ko 1,10,
    wo `un même esprit` KLEIN steht und „Gesinnung" heisst.

Beim Leitwort des Buches ist das der teuerste denkbare Fehlgriff — wer
der Zahl folgt, setzt `Esprit` auf *spirit · espíritu · spirito*.
Gemeldet vom Agenten fuer 1. Korinther 12. Der Lauf sagt jetzt
ausdruecklich, wenn Treffer sich in der Grossschreibung eines NICHT
ersten Wortes unterscheiden.

## Werkzeuge nicht anfassen, waehrend Agenten laufen

Der Agent fuer 1. Korinther 11 hat gemeldet, `reflexiv.py` sei
**waehrend seines Laufs kaputtgegangen**: derselbe Aufruf lief um
00:50 sauber durch und stuerzte ab 01:03 mit `NameError: name 're' is
not defined`. Er hat recht. Ich hatte dem Skript eine
Pfadauswertung eingebaut, den Import vergessen, den Fehler gesehen und
zwei Minuten spaeter behoben — in genau diesen zwei Minuten hat er das
Werkzeug aufgerufen. Betroffen war der `--datei`-Pfad, also genau der
Aufruf, den der Auftrag vorschreibt.

Das ist keine neue Erkenntnis, sondern eine vergessene: als
`mehrwoerter.py` gebaut wurde, ist es **absichtlich als neue Datei**
entstanden, statt `sweeplemma.py` zu erweitern, damit laufende
Pruefketten nicht angefasst werden. Dieselbe Vorsicht hat beim
naechsten Mal gefehlt.

    Regel: solange Agenten laufen, werden ihre Werkzeuge nicht
    geaendert. Neue Datei ja, Aenderung an einem Skript der
    Pflichtkette nein — die wartet bis zum Einsammeln.

Der Agent hat sich uebrigens selbst geholfen (`re` vorinjiziert) und
den Lauf nachgeholt. Gemeldet hat er es trotzdem, und das ist der
Grund, warum es hier steht.

## Die Elisionsregel, zum zweiten Mal praezisiert — und diesmal gemessen

Meine bisherige Fassung zaehlte **freie Token**: „Mehrwort ueber die
freien Token, wenn es mindestens zwei sind." Der Agent fuer
1. Korinther 13 hat sie auf `au moyen d’un miroir` angewandt, den Span
auf `au moyen` gekuerzt — und sich dann selbst widerlegt, indem er den
ganzen Bestand gezaehlt hat:

    92 Stellen  Verschmelzung IM Span
                `au milieu des` 17 · `à cause des/du` 15 · `au nom du` 14
                `le long du` 7 · `auprès des` 6 · `près d’une` 6 …

     8 Stellen  Span GEKUERZT, das elidierte Wort steht daneben
                `au sujet d’Hérodias` · `au sujet d’Israël`
                `pour cause d’infidélité` · `pour cause d’incrédulité`
                `à cause d’Hérodias` (2×)

**`à cause de` steht in BEIDEN Listen** — fuenfzehnmal mit der
Verschmelzung im Span, zweimal ohne. Dieselbe Wendung, zwei
Behandlungen. Eine Zaehlregel kann das nicht erklaeren; das Kriterium
ist, **womit** das `de` verschmilzt:

    de + ARTIKEL      (du, des, d’un, d’une, au, aux)
        → der verschmolzene Token gehoert zur Wendung, Span BIS dahin
    de + INHALTSWORT  (d’Hérodias, d’Israël, d’infidélité)
        → der Token gehoert zum Satz, nicht zur Wendung; Span davor zu Ende

Das ist dieselbe Unterscheidung, die die vierzeilige Elisionstabelle
oben schon macht — sie war nur nie auf das `de` der Wendung selbst
angewandt worden.

Warum die alte Zaehlregel trotzdem sechsmal richtig lag: bei
`au sujet d’Israël` und `pour cause d’infidélité` gibt es keinen
Artikel, also blieb genau ein freies Token uebrig, und die Zahl traf
zufaellig. Bei `au moyen d’un miroir` traf sie nicht mehr.

**Eine Regel, die aus dem falschen Grund richtig liegt, faellt beim
ersten neuen Fall um.** Das ist der Grund, warum jede Regel hier eine
Messung dabeistehen hat — und warum diese hier 100 Stellen zaehlt und
nicht sechs.

## `même` spanisch: gemessen, geteilt, nicht erzwungen

`même` = *sogar · even · … · perfino* steht spanisch **21× auf `aun`
und 21× auf `incluso`** — exakter Gleichstand auf identischen Zeilen.
Ein Kriterium ist nicht zu sehen, und **der Zeuge entscheidet nicht
mit**: rv1909mod liest an den geprüften Stellen dreimal `aun`, zweimal
`incluso` und formuliert siebenmal um.

Damit ist es derselbe Fall wie das jussive `que` (58:21 `may` gegen
`let`): **nicht angeglichen.** Zweiundvierzig Stellen auf eine Muenze
zu setzen ist kein Ertrag.

**Was aber gilt: innerhalb eines Buches muss es stimmen.** 1. Korinther
stand 4:2 auf `incluso` und ist auf `incluso` gezogen (2,10 und 15,41,
dazu 2,10 italienisch `anche` → `perfino`). 14,21 bleibt auf
`aun`/`neppure` — dort ist der Kontext verneint, und `neppure` heisst
„nicht einmal".

    Regel:  wo der Bestand ohne Kriterium geteilt ist, entscheidet das
            BUCH und nicht die Gesamtzahl. Der Leser liest ein Buch,
            nicht den Bestand.

## Die dritte Blindheit: ein eingeschobenes Wort

`folgenreihe` sucht die Zeichenkette, `sweeplemma` die Lemmasignatur —
und beide leiten die erlaubte **Lueckenweite aus der Bestandsspanne**
ab. Steht eine Wendung im Bestand zusammenhaengend, kann sie im
Kapitel auseinandergezogen nie gefunden werden.

Gefunden hat es der Agent fuer 2. Korinther 2 an `qui nous fait
**toujours** triompher`: das Mehrwort `faire triompher` steht in
Mt 12,20 zusammenhaengend, und weder Zeichenkette noch Signatur
trafen. Einziger Finder war der Parallelvers von Hand.

Der Bestand traegt den Beweis, dass die Luecke alt ist:

    `c’est pour cela que`  steht 7× als Mehrwort — und genau die
    achte Stelle, Luc 7,7, hat KEINS. Sie ist die einzige mit einem
    eingeschobenen Wort: `C’est pour cela **aussi** que`.

Nachgetragen als `parts` [0,1,2,4].

**Die Korrektur, und warum die naheliegende falsch war.** Das Fenster
in `sweeplemma` wird auf drei erweitert — aber **nur fuer Signaturen
aus lauter Inhaltswoertern**. Pauschal erweitert kostet es:

    Roemer      3 → 8 Treffer      1. Korinther   5 → 18
    davon echt: keiner             davon echt: keiner

Es sind durchweg `ce qui`, `ce que`, `selon que`, `afin de` — Paare, deren
beide Lemmata sich staendig zufaellig in drei Token Abstand treffen. Mit
der Stoppliste:

    Roemer      3 → 3               1. Korinther   5 → 6

Die eine zusaetzliche Meldung ist echt (`quelque autre chose`,
1 Ko 10,31, wo der Bestand `quelque chose` 30× fuehrt).

Dieselbe Einsicht gilt fuer die stammverwandten Mehrwortlemmata in
`folgenreihe`: dort ging `par` als Inhaltswort durch, und
`"par la puissance de Dieu"` schlug `par terre` und `deux par deux`
vor. Praepositionen stehen jetzt mit in der Stoppliste.

    Merksatz: was staendig vorkommt, trennt nichts. Ein weiteres
    Fenster gehoert nur dorthin, wo ein zufaelliges Zusammentreffen
    unwahrscheinlich ist.

## AT-Zitate: die Null gilt fuer den INHALT, nicht fuer den Rahmen

Ich habe seit Roemer 9 in jeden Prompt geschrieben, die Bilanz fuer
alttestamentliche Zitate mit Bestandsparallele stehe „bei null". Drei
Agenten haben das inzwischen halb widerlegt, zuletzt der fuer
2. Korinther 9, und sie haben recht. Die Aussage ist zu trennen:

    Der ZITATINHALT hat keine Parallele.  Bis 2. Korinther 9 ist ueber
    ein Dutzend Zitate gemessen worden; keines fand seinen Wortlaut
    anderswo im Bestand. Das Neue Testament zitiert das Alte, und das
    Alte steht in dieser Ausgabe nicht annotiert.

    Der RAHMEN steht durchgaengig.  `selon que` traegt 24 Mehrwort-
    belege, `comme il est écrit` und `dit le Seigneur` stehen ebenso
    fest. Roemer 3,10 liefert fuer 2 Kor 9,9 sogar die fuenf
    Eroeffnungstoken zeichengleich MIT Glossen.

Wer die Null hoert und die Vorbereitungsdatei gar nicht erst
aufschlaegt, verliert also genau den Teil, der zu holen ist. Der
richtige Satz lautet: **den Rahmen uebernehmen, den Inhalt praegen.**

Nebenbei dieselbe Sorgfalt bei einer zweiten Verallgemeinerung von
mir: „`sweeplemma`s Verdachtsblock ist wertvoller als sein
Mehrwortblock" gilt nicht immer. In 2. Korinther 9 war der
Verdachtsblock leer und der Mehrwortblock hat alle vierzehn Wendungen
samt Reihen bestaetigt. Beide Bloecke sind zu lesen.

## Die Bilanz der Werkzeugmeldungen — und warum sie weitergehen sollen

Der Agent fuer 2. Korinther 7 hat vermutet, `fixgloss.py verse`
schreibe seine Ausgabe auf stdout **und** stderr, und daraus die
Regel abgeleitet, man duerfe es nie mit `2>/dev/null` aufrufen. Er
hat auch die frueher als „nicht reproduzierbar" abgelegte Meldung
ueber doppelte Zeilen damit erklaeren wollen.

Nachgemessen in Dateien statt in einer Pipe: **stdout 36 Zeilen /
3880 Bytes, stderr 0 Bytes.** Der exakt gemeldete Aufruf liefert seine
dreissig Zeilen. Die Hypothese traegt nicht; die urspruengliche
Beobachtung bleibt unerklaert.

**Die Bilanz dieser Nacht, damit niemand die falsche Lehre zieht:**

    rund 22 gemeldete Werkzeugfehler waren echt und sind behoben —
      artikel (viermal), kongruenz (viermal), ausgaben, reflexiv
      (zweimal), lexicon, ausreisser, konsistenz, hints (zweimal),
      belegt (zweimal), fixgloss, folgenreihe (zweimal), sweeplemma,
      paketvorb, PROMPT_BAUSTEIN

    rund 6 haben sich nicht bestaetigt — dreimal ein `| head`,
      einmal nicht reproduzierbare Dopplung, einmal eine
      abgeschnittene `belegt`-Ausgabe, einmal diese stderr-Vermutung

Das Verhaeltnis ist der Grund, warum jede Meldung willkommen ist: auf
eine, die sich nicht bestaetigt, kommen fast vier echte. **Melden ist
richtig, auch wenn man sich irrt.**

Und die Gegenregel fuer den Koordinator: **eine Meldung ist eine
Vermutung, keine Diagnose.** Sie wird nachgemessen, bevor etwas
geaendert wird — sonst „repariert" man ein Werkzeug, das gesund ist,
und richtet dabei den Schaden an, den die echten Meldungen dieser
Nacht zweimal dokumentiert haben.

## Artikel und Genus in der Zielsprache

Ein spanisches oder italienisches Nomen hat genau EIN Genus. Steht
dasselbe Zielwort einmal mit `el` und einmal mit `la`, ist das ein
Fehler — unabhaengig davon, wie die Mehrheit steht. Zweimal stand die
Mehrheit falsch: `la consuelo` 5:1 und `la pensiero` 3:2.

Das FRANZOESISCHE Wort sagt darueber nichts. `la montagne` darf
spanisch `el monte` oder `la montaña` heissen, beides richtig — der
Befund entsteht erst, wenn man nach dem ZIELWORT aufschluesselt.

Drei Spaltungen sind richtig und bleiben:

    Nomen gemeinsamen Geschlechts   el joven / la joven, il giovane /
                                    la giovane, el guardia (die Person)
                                    gegen la guardia (die Truppe)
    spanische a-tonica-Regel        feminine Nomen mit betontem
                                    a-Anlaut nehmen im Singular `el`:
                                    el arpa, el agua, el alma
    Adjektive und Adverbien         gran, mas, piu, ultimo richten sich
                                    nach ihrem Bezugswort, nicht nach
                                    sich selbst

Nicht jedes Wort gemeinsamen Geschlechts im Spanischen ist eines im
Italienischen: `guida` ist immer feminin, auch fuer einen Mann — `la
guida dei ciechi` (Rm 2,19), waehrend spanisch `el guía` richtig ist.

## Eine Null ist erst eine Aussage, wenn das Werkzeug etwas angesehen hat

`artikel.py` meldete Buch fuer Buch „0 Verdachtsfaelle" und hatte in
2. Korinther 38 von 451 Artikeln geprueft — 8 %. Sie filterte mit
`e['form']` gegen eine Liste DEUTSCHER Artikel, und in der
franzoesischen Richtung steht in `form` das Franzoesische. Es passte
nur, was in beiden Sprachen gleich aussieht (`des`). 125 falsche
Artikel standen dahinter.

Der Docstring von `common.de_wort` beschreibt genau diesen Fehler und
nennt beide Werkzeuge, die ihn schon einmal hatten. Eine Zeile weiter
unten stand er noch. **Wo eine Null verdaechtig glatt ist, zaehle
nach, wie viele Faelle die Probe ueberhaupt erreicht haben** — die
Zahl steht in keinem Bericht, aber sie ist mit sechs Zeilen gemessen.

## AT-Zitate, dritte Fassung

Bisher stand hier: den Rahmen uebernehmen, den Inhalt praegen. Der
Agent fuer Galater 3 hat die zweite Haelfte widerlegt. Wo eine ANDERE
neutestamentliche Stelle dieselbe alttestamentliche Stelle zitiert,
steht der Zitatinhalt bereits glossiert im Bestand — und zwar Token
fuer Token:

    Hab 2,4     Gal 3,11  ← Rm 1,17    sechs Token zeichengleich
    3 Mo 18,5   Gal 3,12  ← Rm 10,5    neun Token, samt Mehrwort
    1 Mo 15,6   Gal 3,6   ← Rm 4,3     praktisch der ganze Vers
    5 Mo 21,23  Gal 3,13  — keine Parallele

Der Ort dafuer ist nicht das AT (das steht in einer anderen Ausgabe),
sondern die zweite NT-Stelle. Dasselbe Muster traegt schon 2 Ko 13,1,
wo Mt 18,16 dieselben Worte aus 5 Mo 19,15 zitiert.

**Also: erst suchen, wer sonst noch zitiert, dann praegen.** Nur wenn
niemand sonst dieselbe Stelle zitiert, ist der Inhalt wirklich neu.

## Praeposition und Artikel: die Praeposition bleibt bar

Wo im Franzoesischen Praeposition und Artikel zwei Token sind (`à la`,
`dans le`, `depuis le`), traegt die romanische Glosse den Artikel
GENAU EINMAL — auf dem Artikeltoken. Die Praeposition bleibt bar:

    à la     → `a` + `la`        NICHT `alla` + `la`
    dans le  → `in` + `il`       NICHT `nel` + `il`
    depuis le→ `da` + `il`       NICHT `dal` + `il`

Der Bestand haelt das 2403:32. Die 32 Ausnahmen waren Fehler und sind
gezogen; gemeldet vom Agenten fuer Philipper 1 an `depuis le premier
jour` (Ac 20,18), wo „dal il primo giorno" stand.

Nur wo das Franzoesische selbst verschmilzt (`du`, `au`, `aux`, `des`),
verschmilzt auch die Glosse — dort gibt es kein zweites Token.

## paketcheck ist ein bewegliches Ziel

Dreimal gemeldet (Epheser 2, Philipper 2 und 4): waehrend eines Laufs
hat ein Nachbarkapitel seine Glosse geaendert, und wer frueh abglich,
glich gegen einen Stand ab, den es Minuten spaeter nicht mehr gab —
`Épaphrodite` stand um 14:54 als *Epafrodito*, um 14:58 als
*Epafròdito*.

**`paketcheck` gehoert als LETZTER Lauf vor der Abgabe wiederholt**,
nicht nur einmal in der Mitte. Derselbe Satz, der fuer den Bestand
gilt, gilt auch fuer die Paketnachbarn.

## Pronominalverben, die der Bestand schlicht fuehrt

Dreimal gemeldet (2 Ko 11, Kolosser 3, und schon in Judas): `corrompre`
und `plaindre` stehen im Bestand unter dem schlichten Lemma, obwohl die
Belege reflexiv sind. Die Reflexiv-Regel legt `se corrompre` /
`se plaindre` nahe.

**Folg dem Bestand und melde es, praeg kein neues Lemma.** Zwei Gruende:
`corrompre` traegt einen echten transitiven Beleg (1 Ko 15,33, „schlechter
Umgang verdirbt gute Sitten"), das schlichte Lemma wird dort also
gebraucht; und eine Umstellung muesste ALLE pronominalen Verben des
Bestands zugleich erfassen — das ist ein eigener Arbeitsblock, keine
Kapitelentscheidung.

Fuer neu gepraegte Verben gilt die Reflexiv-Regel unveraendert:
`se glorifier`, `s'elever`, `se persuader` sind so entstanden.

## `Pour moi/nous/vous` am Satzanfang — die alte Regel war falsch

Hier stand, die Grenze laufe an der Glosse und die Nachzuegler seien
alle nachgezogen. Gemessen (139 `pour` + Personalpronomen im ganzen
Bestand) stimmt das nicht:

    Glosse *Was … betrifft*   4 von 4 als MEHRWORT
        (Lc 9,44 · Rm 16,19 · Rm 8,9 · Gal 4,28)
    Glosse *Fuer …*           5 als Mehrwort, 16 WOERTLICH
        (woertlich u.a. Jn 11,42 · Ac 20,6 · Ac 20,13 · Rm 7,9 ·
         1 Ko 2,1 · 3,1 · 4,3 · 5,3 · 9,15 · Gal 5,5 · 5,11)

**Das Kriterium ist die Glosse, nicht die Satzposition** — aber nur in
einer Richtung: wo die deutsche Wiedergabe *Was … betrifft* lautet,
gehen die Einzelglossen nicht auf („Fuer euch" ist etwas anderes), also
Mehrwort. Wo sie *Fuer …* lautet, tragen die Einzeltoken den Sinn, und
der Bestand steht 16:5 auf woertlich.

Die fuenf `Fuer`-Mehrwoerter (Mt 28,5 · Lc 23,41 · 2 Ko 10,13 ·
1 Th 2,17 · Jude 1,20) sind damit die Minderheit und nicht
vereinheitlicht. Gemeldet vom Agenten fuer 1. Thessalonicher 2, der
die alte Regel als „stimmt mit dem Bestand nicht ueberein" gemessen
hat — zu Recht.

## Korrektur: `ne rien` steht sehr wohl ueber der Elision

Hier stand, bei verschmolzenem `ne` gebe es kein Mehrwort. Gemessen
ist das falsch: `ne rien` steht **35× ueber einer elidierten Form**
gegen 66× ueber einer freien — darunter sechsmal genau `n'a rien`
(Lc 12,47 · 23,15 · 23,41 · Jn 14,30 · Ac 25,25 · 26,31), alle auf
*hat nichts · has nothing · no ha nada · non ha nulla*.

Die Luc-1,37-Regel, auf die sich der alte Satz stuetzte, betrifft
`rien` **vor** `ne` — nicht die Elision als solche. Gemeldet vom
Agenten fuer Hebraeer 2, gefunden von `sweeplemma`.

Dasselbe gilt fuer `ne personne`: 2 Ko 7,2 setzt es dreimal ueber
`n'avons … personne`, was schon im Kapitel-11-Bericht zu
2. Korinther stand.

## `ne … plus aucun` traegt EIN Mehrwort, nicht zwei

Wo `plus` und `aucun` in derselben Verneinung stehen, setzt der Bestand
`ne aucun` ueber die ganze Spanne und KEIN `ne plus`. Beleg: Marc 15,5
„ne fit plus aucune réponse". Gemeldet vom Agenten fuer Hebraeer 10,
der zuerst `ne plus` gesetzt hatte; `sweeplemma`s Verdachtsblock
(`avoir aucun`, 80 % gedeckt) hat ihn hingefuehrt.

## Praezisierung: Verwandtschaftsnomen, Artikel und NUMERUS

Hier stand, der Vokativ stehe italienisch artikellos. Gemessen an
`mon/mes frère(s)` ist die Trennlinie eine andere — der Numerus:

    mon frère   → `mio`      bar        13 Belege
    mes frères  → `i miei`   mit Artikel 15 Belege

Das ist die italienische Regel fuer Verwandtschaftsnomen: im SINGULAR
artikellos (`mio fratello`), im PLURAL mit Artikel (`i miei
fratelli`). Der Vokativ aendert daran nichts — die 15 Plurale stehen
gerade in Anreden (Rm 7,4 · Rm 15,14 · 1 Ko 11,33 · 1 Ko 15,58 ·
Phi 3,1).

Gemeldet vom Agenten fuer Jakobus 1, der `kongruenz.py` folgte statt
der alten Regel und damit richtig lag.

## Deutsche Homonymie: `devenir` und das Passiv-Hilfsverb

Wie `ne`/`pas` beide *nicht* tragen, tragen `deviennent` und `soient`
beide *werden* — das Deutsche hat fuer „become" und das
Passiv-Hilfsverb EIN Wort. `glosskollision` meldet das Paar als
1-von-4-Verdacht; es ist keiner.

Beide Seiten sind gemessene Bindungen: `vous soient` steht 11:0 auf
*werden* (die zehn paulinischen Grussverse plus Jude 1,2, der
wortgleiche Zwilling), `deviennent` 5:0 (Mt 4,3 · 19,5 · 1 Ko 6,16 ·
Eph 5,31 · Jn 9,39). Englisch, Spanisch und Italienisch trennen
sauber.

Gemeldet vom Agenten fuer 1. Petrus 1, der zwischenzeitlich `soient` =
*seien* gesetzt hatte — `folgencheck --gegen` meldete daraufhin die
Grussformel in ZEHN Buechern, und er hat es zurueckgenommen.
