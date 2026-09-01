# Namen, die Jesaja anders schreibt als der uebrige Bestand

Der l1912mod ist in der Schreibung von Eigennamen nicht durchgehend einheitlich.
Gefunden am `Schinar`/`Sinear`-Fall in **11,11**, den der Agent fuer Kapitel 11
gemeldet hat: `belegt.py Schinar` sagt „nicht belegt", waehrend `Sinear`
viermal in 1. Mose steht — **derselbe Ort, zwei deutsche Schreibungen**.

**So wird verfahren:** das Lemma folgt der **Jesaja-Schreibung** (die App
glossiert das Wort, das dasteht), die **Glossenreihe** kommt aus dem Bestand
(es ist derselbe Ort). Sonst traegt dieselbe Sache zwei Reihen.

Das ist **kein Uebersetzungsbefund und keine Korrektur am Quelltext** — nur eine
Warnung, dass `belegt.py` und `lexicon.py` hier zu Recht schweigen und trotzdem
eine Vorlage existiert.

| Jesaja | Stelle | Bestand | Belege | Glossenreihe |
|---|---|---|---|---|
| `Schinar` | 11,11 | `Sinear` | 4 | *Shinar · Sinar · Schinear · Scinear* |
| `Anatot` | 10,30 | `Anathoth` | 8 | *Anathoth · Anatot · Anathoth · Anatoth* |
| `Elale` | 15,4 | `Eleale` | 2 | *Elealeh · Eleale · Élealé · Elealeh* |
| `Jeschurun` | 44,2 | `Jesurun` | 2 | *Jeshurun · Jesurún · Yeschurun · Iesurun* |
| `Nebajots` | 60,7 | `Nebajoth` | 2 | *Nebaioth · Nebaiot · Nebajoth · Nebaiot* |
| `Tubal` | 66,19 | `Thubal` | 2 | *Tubal · Tubal · Tubal · Tubal* |

## `Lascha` gehoert NICHT hierher — die Vorgabe war falsch

In der ersten Fassung stand `Lascha` (10,30) in der Tabelle oben, mit der Reihe
von `Lasa` aus 1Mo 10,19. **Der Agent fuer Kapitel 10 hat es widerlegt, und er
hat recht**: es sind **zwei verschiedene Orte**.

1Mo 10,19 ist die Kanaaniter-Grenze bei Sodom, Jes 10,30 ein Dorf neben Nob und
Anatot. Auch das Deutsche schreibt sie verschieden (`Lasa` gegen `Lascha`), und
**alle vier Ausgaben trennen sie ebenfalls**:

| | 1Mo 10,19 | Jes 10,30 |
|---|---|---|
| WEB | Lasha | **Laishah** |
| RV | Lasa | **Lais** |
| LSG | Léscha | **Laïs** |
| RIV | Lesha | **Laish** |

Gesetzt ist deshalb ein **eigenes Lemma `Lascha` A1** mit der Ausgabenreihe
*Laishah · Lais · Laïs · Laish*. `Anatot` im selben Vers ist dagegen wirklich
derselbe Ort und folgt der Bestandsreihe von `Anathoth`.

**Die Lehre:** die Tabelle oben entsteht aus der Lautaehnlichkeit zweier
deutscher Schreibungen. Lautaehnlichkeit ist ein Grund nachzusehen, kein Beweis
fuer denselben Traeger — dieselbe Warnung, die `vorab.py` fuer
grossgeschriebene Formen ausgibt. **Vor jeder Uebernahme aus dieser Tabelle die
Belegstelle und die vier Ausgaben aufschlagen.**

## `Elale` — die Gegenprobe zu `Lascha`, und sie faellt anders aus

`belegt.py Elale` schweigt; der Bestand fuehrt `Eleale` zweimal (4Mo 32,3 ·
32,37). Nach dem `Lascha`-Irrtum wurde diesmal **vor** der Uebernahme an allen
vier Ausgaben geprueft — und hier ist es wirklich derselbe Ort:

| | 4Mo 32,3 / 32,37 | Jes 15,4 |
|---|---|---|
| WEB | Elealeh | Elealeh |
| RV | Eleale | Eleale |
| LSG | Élealé | Élealé |
| RIV | Elealeh | Elealeh |

Dazu die Reihenprobe: **4Mo 32,3 nennt `Dibon`, `Hesbon`, `Eleale` und `Nebo`
in einer Zeile** — vier der sechzehn Ortsnamen von Jesaja 15. Verfahren
angewandt, Lemma `Elale`, Glossenreihe aus dem Bestand.

**Die Bestandsreihe war allerdings in zwei Sprachen falsch** und ist mit diesem
Paket korpusweit korrigiert worden (s. unten).

## Drei Bestandsreihen, die ihrer eigenen Ausgabe widersprachen

Gefunden vom Agenten fuer Kapitel 15, ueber den gesamten Bestand nachgezaehlt
und mit `remap.py` korrigiert. **Das ist nicht der Fall „eine Ausgabe wirkt
altertuemlich"** — da gilt die Ausgabe und es ist kein Befund. Hier stand die
Bestandsglosse an **keiner einzigen** Belegstelle in ihrer Ausgabe:

| Lemma | Bestand hatte | die Ausgabe schreibt | Stellen |
|---|---|---|---|
| `Zoar` | it *Zoar* | RIV **Tsoar** | 8 von 8 |
| `Medeba` | it *Madaba* | RIV **Medeba** | 4 von 4 |
| `Eleale` / `Elale` | es *Elealé*, it *Eleale* | RV **Eleale**, RIV **Elealeh** | 2 von 2 |

Korrigiert in 1. Mose, 4. Mose, 5. Mose, Josua, 1. Chronik und Jesaja;
`validate.py` laeuft fuer alle sechs Buecher ohne Befund.

**Woran man diese Klasse erkennt:** eine Sprache weicht ab, und die Abweichung
laesst sich an der Ausgabe **an jeder Belegstelle** widerlegen. Dann liegt der
Fehler im Bestand. Weicht die Ausgabe dagegen selbst ab (RIVs `fra`/`tra`, WEBs
*Shushan* fuer Susa), ist nichts zu tun.

**`Scharon` gehoert NICHT hierher**: das Hohelied hat es in 2,1 bereits als
eigenes Lemma gesetzt (A1, *Sharon · Sarón · Saron · Saron*) — dieselbe Reihe
wie `Saron`. In Jesaja 33,9 · 35,2 · 65,10 ist es also regulaer belegt und
einfach zu uebernehmen.

Ebenfalls nicht hierher, weil zufaellige Lautaehnlichkeit und keine Namen:
`Dächer`/`daher`, `Pakt`/`packt`, `Sänften`/`sanften`, `Zinnen`/`sinnen`,
`Kuschs`/`kuss`. **`Kusch` selbst ist regulaer belegt.**
