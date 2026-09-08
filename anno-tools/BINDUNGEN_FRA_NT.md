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
ne`. **`ne plus` fehlte** — es steht mit 13 Belegen im Bestand, und der
Span umfasst das Verb (`ne pourras plus`, Luc 1,20; Marc 1,45). Der
Agent fuer Luc 1 hatte es als kompositionell verworfen; der neue
zweite Abschnitt von `sweeplemma.py` hat es zurueckgeholt.

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
