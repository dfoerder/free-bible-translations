#!/usr/bin/env python3
"""Sendet Modernisierungs-Aufträge an die Anthropic Batch-API (50 % günstiger).

Sprach- und übersetzungsunabhängig. Liest <lang>/<src>/, schreibt später
(via modernize_collect.py) nach <lang>/<dst>/.

Beispiele:
  ANTHROPIC_API_KEY=sk-ant-... \\
  python3 tools/modernize_submit.py --lang deu --src l1912 --dst l1912mod \\
      --name "Luther-Bibel von 1912" 1-66

  # nur Evangelien, anderes Modell, schon Vorhandenes überspringen:
  python3 tools/modernize_submit.py --lang deu --src l1912 --dst l1912mod \\
      --name "Luther-Bibel von 1912" --model claude-sonnet-5 --skip-existing 40-43

  # Reina-Valera 1909, Neues Testament (Quelle = Grundtext rv1909):
  python3 tools/modernize_submit.py --lang spa --src rv1909 --dst rv1909mod \\
      --name "Reina-Valera de 1909" 40-66
"""
import argparse
import json
import os
import sys
import time
import urllib.request

from common import ROOT, load_book

BATCH_API_URL = "https://api.anthropic.com/v1/messages/batches"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".modernize_state.json")
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

SYSTEM_PROMPTS = {
    "deu": """\
Du modernisierst den Text der {name} für heutige Leser (auch Nicht-Muttersprachler).

## Regeln

1. **Rechtschreibung modernisieren**: daß→dass, ward→wurde, Laß→Lass usw.
2. **Veraltete Wörter ersetzen**:
   - zeugte → war der Vater von
   - Weib → Frau
   - Gemahl → Frau / Mann (je nach Kontext)
   - allda → dort
   - gen → nach
   - Otterngezüchte → Schlangenbrut
   - genugsam → wert
   - Buße tun → umkehren
   - Glieder (Generationen) → Generationen
   - Weisen vom Morgenland → Sterndeuter aus dem Osten
   - erkannte sie (nicht) → schlief (nicht) mit ihr
   - und andere veraltete Ausdrücke sinngemäß modernisieren
3. **Satzbau vereinfachen**: Lange Schachtelsätze in kürzere, klare Sätze aufteilen.
4. **Natürliche, heutige Sprache**: klar und verständlich. Kein altertümlicher oder gehoben-„biblischer" Ton — schreib so, wie man heute normal schreibt.
5. **Inhaltlich treu bleiben**: Keine theologischen Änderungen, keine Ergänzungen, nichts weglassen.
6. **Eigennamen beibehalten** wie im Original.

## Ausgabeformat

Gib NUR ein JSON-Objekt zurück. Schlüssel = Versnummern (Strings). Werte = modernisierter Verstext (String).

Beispiel:
{{"1": "Am Anfang schuf Gott Himmel und Erde.", "2": "Und die Erde war leer und öde..."}}

Kein Markdown, keine Erklärungen — nur das JSON-Objekt.""",
    "spa": """\
Modernizas el texto de la {name} para lectores actuales (también no hispanohablantes nativos).

## Reglas

1. **Ortografía moderna**: fué→fue, vió→vio, á/é/ó/í/ú con tilde diacrítica→sin tilde (a/e/o/i/u), é→y donde corresponda.
2. **Palabras y fórmulas arcaicas**:
   - engendró → fue el padre de
   - he aquí → eliminar o sustituir por lenguaje natural (Entonces, En aquel momento…)
   - marido/mujer → esposo/esposa (según contexto)
   - transmigración → destierro / cautiverio
   - magos → sabios / astrólogos del oriente
   - parirá → dará a luz
   - no la conoció → no tuvo relaciones con ella
   - escribas → maestros de la ley
   - príncipes de los sacerdotes → principales sacerdotes
   - guiador → gobernante / líder
   - arrepentíos → arrepiéntanse
   - y otras expresiones arcaicas de forma equivalente
3. **Simplificar la sintaxis**: oraciones largas y encadenadas en frases más cortas y claras; reducir el abuso inicial de «Y».
4. **Español natural y actual**: claro y comprensible. Sin tono arcaico ni «biblico» elevado — escribe como se escribe hoy en español estándar.
5. **Fidelidad al contenido**: sin cambios teológicos, sin añadir ni omitir nada.
6. **Nombres propios**: conservar; se permite ortografía moderna (Thamar→Tamar, Bethlehem→Belén).
7. **Registro latinoamericano**: sustituir «vosotros» y sus formas verbales (sois, tenéis, haréis, arrepentíos…) por «ustedes» y sus formas correspondientes (son, tienen, harán, arrepiéntanse…) — esta traducción se usa hoy casi exclusivamente en Latinoamérica, no en España.

## Formato de salida

Devuelve SOLO un objeto JSON. Claves = números de versículo (strings). Valores = texto modernizado (string).

Ejemplo:
{{"1": "En el principio creó Dios los cielos y la tierra.", "2": "La tierra estaba desordenada y vacía..."}}

Sin Markdown, sin explicaciones — solo el objeto JSON.""",
    "ita": """\
Modernizzi il testo della {name} per i lettori di oggi (anche non madrelingua italiani).

## Regole

1. **Ortografia moderna**: elimina gli apostrofi troncati arcaici e le forme letterarie desuete (de’→dei, co’→con i/coi, pe’→per i, que’→quei, un de’→uno dei, v’era→c’era, quest’ultimo solo se non ambiguo).
2. **Parole ed espressioni arcaiche**:
   - Iddio → Dio
   - Figliuolo/Figliuoli/Figliuola → Figlio/Figli/Figlia
   - generò → fu padre di
   - eziandio → anche
   - conciossiaché → poiché / dato che
   - acciocché → affinché
   - imperocché → perché
   - quivi → lì / qui
   - dinanzi a / innanzi a / in cospetto di → davanti a
   - ond’è che → perciò
   - e altre espressioni arcaiche in modo equivalente
3. **Semplificare la sintassi**: frasi lunghe e concatenate in frasi più brevi e chiare; ridurre l'uso iniziale eccessivo di "E".
4. **Italiano naturale e attuale**: chiaro e comprensibile. Nessun tono arcaico o "biblico" elevato — scrivi come si scrive oggi in italiano standard.
5. **Fedeltà al contenuto**: nessun cambiamento teologico, senza aggiungere né omettere nulla.
6. **Nomi propri**: mantienili come nell'originale.
7. Se noti un evidente errore di trascrizione/OCR nel testo originale (una parola chiaramente sbagliata che rompe il senso della frase, es. "a somiglianza di io" invece di "a somiglianza di Dio"), correggilo silenziosamente nel testo modernizzato in base al contesto.

## Formato di output

Restituisci SOLO un oggetto JSON. Chiavi = numeri di versetto (stringhe). Valori = testo modernizzato (stringa).

Esempio:
{{"1": "Nel principio Dio creò i cieli e la terra.", "2": "La terra era informe e vuota..."}}

Nessun Markdown, nessuna spiegazione — solo l'oggetto JSON.""",
}

USER_MSG_TMPL = {
    "deu": "{book_name}, Kapitel {chap_nr} ({src_label}):\n\n{verses}\n\nModernisiere alle Verse dieses Kapitels. Gib das Ergebnis als JSON zurück.",
    "spa": "{book_name}, capítulo {chap_nr} ({src_label}):\n\n{verses}\n\nModeriza todos los versículos de este capítulo. Devuelve el resultado como JSON.",
    "ita": "{book_name}, capitolo {chap_nr} ({src_label}):\n\n{verses}\n\nModernizza tutti i versetti di questo capitolo. Restituisci il risultato come JSON.",
}


def parse_book_ranges(args):
    books = []
    for arg in args:
        if "-" in arg:
            start, end = arg.split("-", 1)
            books.extend(range(int(start), int(end) + 1))
        else:
            books.append(int(arg))
    return sorted(set(books))


def src_path(lang, src, book_nr):
    return os.path.join(ROOT, lang, src, f"{book_nr}_{src}.json")


def dst_path(lang, dst, book_nr):
    return os.path.join(ROOT, lang, dst, f"{book_nr}_{dst}.json")


def already_modernized(lang, dst, book_nr, chap_nr):
    path = dst_path(lang, dst, book_nr)
    if not os.path.exists(path):
        return False
    data = load_book(path)
    return str(chap_nr) in data.get("chapters", {})


def system_prompt(lang, name):
    tmpl = SYSTEM_PROMPTS.get(lang, SYSTEM_PROMPTS["deu"])
    return tmpl.format(name=name)


def build_user_message(lang, book_name, chap_nr, verses, src_label):
    verse_lines = "\n".join(
        f"{vnum}: {verses[vnum]}" for vnum in sorted(verses.keys(), key=int)
    )
    tmpl = USER_MSG_TMPL.get(lang, USER_MSG_TMPL["deu"])
    return tmpl.format(
        book_name=book_name,
        chap_nr=chap_nr,
        src_label=src_label,
        verses=verse_lines,
    )


def main():
    ap = argparse.ArgumentParser(description="Modernisierungs-Batch einreichen")
    ap.add_argument("--lang", required=True, help="ISO-639-3 Sprachcode, z. B. deu")
    ap.add_argument("--src", required=True, help="Quell-Übersetzungs-ID, z. B. l1912")
    ap.add_argument("--dst", required=True, help="Ziel-Übersetzungs-ID, z. B. l1912mod")
    ap.add_argument("--name", required=True, help="Anzeigename für den Prompt, z. B. 'Luther-Bibel von 1912'")
    ap.add_argument("--model", default=os.environ.get("MODERNIZE_MODEL", "claude-sonnet-5"))
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("books", nargs="+", help="Buchbereiche, z. B. 1-66 oder 40-43 1")
    args = ap.parse_args()

    if not API_KEY:
        print("\n  ⚠  Kein API-Key! → export ANTHROPIC_API_KEY='sk-ant-...'\n")
        sys.exit(1)

    books = parse_book_ranges(args.books)
    prompt = system_prompt(args.lang, args.name)

    requests = []
    for book_nr in books:
        path = src_path(args.lang, args.src, book_nr)
        if not os.path.exists(path):
            print(f"  ⚠ Buch {book_nr}: Datei nicht gefunden ({path})")
            sys.exit(1)

        data = load_book(path)
        book_name, chapters = data["name"], data["chapters"]
        book_requests = 0

        for chap_nr in sorted(chapters.keys(), key=int):
            if args.skip_existing and already_modernized(args.lang, args.dst, book_nr, int(chap_nr)):
                continue
            user_msg = build_user_message(args.lang, book_name, chap_nr, chapters[chap_nr], args.name)
            requests.append({
                "custom_id": f"b{book_nr}_c{chap_nr}",
                "params": {
                    "model": args.model,
                    "max_tokens": 16000,
                    "system": prompt,
                    "messages": [{"role": "user", "content": user_msg}],
                },
            })
            book_requests += 1

        print(f"  {book_nr:2d}  {book_name:20s}  {len(chapters):3d} Kap  {book_requests:4d} Anfragen")

    if not requests:
        print("\n  Nichts einzureichen (alles schon modernisiert?).")
        sys.exit(0)

    print(f"\n  Gesamt: {len(requests)} Anfragen für {len(books)} Bücher")
    print(f"  Modell: {args.model}   (Batch-API = 50 % günstiger)\n")

    payload = json.dumps({"requests": requests}).encode("utf-8")
    print(f"  Sende Batch ({len(payload) / 1024 / 1024:.1f} MB)...")

    req = urllib.request.Request(
        BATCH_API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=600) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    batch_id = result["id"]
    print(f"  ✓ Batch erstellt: {batch_id}  (Status: {result.get('processing_status', '?')})")

    state = {"batches": []}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
    state["batches"].append({
        "id": batch_id,
        "submitted_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "lang": args.lang,
        "src": args.src,
        "dst": args.dst,
        "model": args.model,
        "request_count": len(requests),
        "books": books,
    })
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    print(f"\n  Status gespeichert → {STATE_FILE}")
    print("  Weiter: python3 tools/modernize_collect.py --wait")


if __name__ == "__main__":
    main()
