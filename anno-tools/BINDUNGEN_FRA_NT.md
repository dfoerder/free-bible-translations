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

Die Negation sitzt am `pas`; das `n’`-Token traegt nur sein Verb. Das
Paar bekommt zusaetzlich einen Mehrwort-Eintrag mit Lemma `ne pas`.

**Das Paar ist zusammenhaengend — also `pos_end`, nicht `parts`.**
`selfcheck.py` weist `parts` dort zurueck.

## Relativpronomen

`qui` und `que` als Relativum werden deutsch **`welche(r)`**, nie
`der/die/das`. Sonst kollidiert das Relativpronomen buchweit mit dem
Artikel, und `glosskollision.py` meldet in jedem Kapitel dasselbe Paar.

## Reflexiva

Ein Mehrwort **nur dort**, wo die Zielsprachen das Reflexiv nicht
spiegeln:

    se sont perdus  → sind umgekommen     Mehrwort
    se sont jetés                         Mehrwort
    s’est glissé                          Mehrwort
    se corrompent · se plaignent · se repaissant   kein Mehrwort

Wo Deutsch, Spanisch und Italienisch selbst reflexiv sind, tragen die
Einzelwoerter alles.

## Praepositionen und Artikel

- **Italienisch `par` = `da`**, und der Artikel bleibt am
  Artikeltoken: `da` + `le tenebre`, nicht `dalle` + `le tenebre`.
  Sonst steht der Artikel doppelt.
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
