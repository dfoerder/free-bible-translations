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

**Die Regel greift nur, wo zwei verschiedene Woerter zusammenstossen.**
Eine **zusammengesetzte Praeposition** behaelt ihre Woerterbuchform:
`jusqu'à` bleibt `jusqu'à` und wird nicht zu `jusque`. Entschieden in
Matthaeus Paket 1, wo Kapitel 2 die Elisionsregel angewandt hatte und
die Kapitel 1 und 3 (mit Judas) die Woerterbuchform.

## `ne … pas`

Das Mehrwort mit dem Lemma `ne pas` traegt die Einheit, und **der Span
umfasst das Verb mit** — `ne vivra pas`, `Ne vous inquiétez pas`, nicht
nur die beiden Randtokens.

Die Einzelwoerter haengen davon ab, ob das `ne` elidiert ist. Gemessen
ueber den Bestand:

    ne  (eigenes Token)   → *nicht*                    66×
    n’a · n’est · n’ont   → nur das Verb (*hat*, *ist*, *haben*)

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
