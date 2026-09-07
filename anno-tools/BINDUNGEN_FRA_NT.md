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

    Anrede an Jesus       Meister · Teacher · Maestro · Maestro   (21×)
    Gleichnisherr         Herr · master · señor · padrone         (12×)
    Besitzer einer Sache  Herr · master · dueño · padrone         (12×)
      — `maître de la vigne`, `maître de maison`
    neben `Seigneur`      Gebieter · master · dueño · padrone     (Luc 12,42 · 13,25)

Die vierte Reihe ist die Ausweichlesart und gilt nur im
Kollisionsvers; die dritte gilt ueberall, wo `maître` einen Besitz
regiert.
