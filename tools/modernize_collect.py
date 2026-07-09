#!/usr/bin/env python3
"""Holt die Ergebnisse eines Modernisierungs-Batches und schreibt die JSON-Dateien.

Sprache/Quelle/Ziel werden aus dem Batch-Status (.modernize_state.json) gelesen,
die Buchnamen aus den Quelldateien. Ausgabe im kanonischen Format (common.py).

Verwendung:
  python3 tools/modernize_collect.py                 # letzter Batch
  python3 tools/modernize_collect.py msgbatch_xxx    # bestimmter Batch
  python3 tools/modernize_collect.py --status        # nur Status
  python3 tools/modernize_collect.py --wait          # warten, dann anwenden
"""
import json
import os
import re
import sys
import time
import urllib.request

from common import ROOT, load_book, write_book

BATCH_API_URL = "https://api.anthropic.com/v1/messages/batches"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".modernize_state.json")
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"batches": []}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_batch_entry():
    """Ermittle (batch_id, entry) aus Argument oder letztem State-Eintrag."""
    state = load_state()
    for arg in sys.argv[1:]:
        if arg.startswith("msgbatch_"):
            for b in state.get("batches", []):
                if b["id"] == arg:
                    return arg, b
            return arg, {}  # unbekannt, aber Status/Download geht trotzdem
    if not state.get("batches"):
        print(f"  ⚠ Kein Batch angegeben und kein {STATE_FILE}.")
        sys.exit(1)
    entry = state["batches"][-1]
    return entry["id"], entry


def api_get(url):
    req = urllib.request.Request(
        url, headers={"x-api-key": API_KEY, "anthropic-version": "2023-06-01"}
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8")


def check_status(batch_id):
    data = json.loads(api_get(f"{BATCH_API_URL}/{batch_id}"))
    counts = data.get("request_counts", {})
    print(f"\n  Batch:  {batch_id}\n  Status: {data.get('processing_status', 'unknown')}")
    if counts:
        print(f"  Fortschritt: {counts.get('succeeded', 0)}/{sum(counts.values())} ok, "
              f"{counts.get('errored', 0)} Fehler, {counts.get('processing', 0)} laufen")
    return data


def parse_response_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    if not text.startswith("{"):
        idx = text.find("{")
        if idx >= 0:
            text = text[idx:]
    return json.loads(text)


def download_results(batch_id):
    raw = api_get(f"{BATCH_API_URL}/{batch_id}/results")
    results, errors = {}, []
    for line in raw.strip().split("\n"):
        if not line.strip():
            continue
        entry = json.loads(line)
        cid, result = entry["custom_id"], entry["result"]
        if result["type"] == "succeeded":
            text = result["message"]["content"][0]["text"]
            try:
                results[cid] = parse_response_json(text)
            except (json.JSONDecodeError, IndexError) as e:
                errors.append((cid, f"JSON-Parsefehler: {e}"))
        elif result["type"] == "errored":
            err = result.get("error", {})
            errors.append((cid, f"{err.get('type', '?')}: {err.get('message', '?')}"))
        else:
            errors.append((cid, f"Status: {result['type']}"))
    return results, errors


def parse_custom_id(cid):
    m = re.match(r"b(\d+)_c(\d+)", cid)
    return {"book": int(m.group(1)), "chapter": int(m.group(2))} if m else None


def apply_results(results, entry):
    lang, src, dst = entry.get("lang"), entry.get("src"), entry.get("dst")
    if not (lang and src and dst):
        print("  ⚠ Batch-Status ohne lang/src/dst — kann Ziel nicht bestimmen.")
        print("     (Batch mit modernize_submit.py aus dieser Sammlung neu einreichen.)")
        sys.exit(1)

    out_dir = os.path.join(ROOT, lang, dst)
    os.makedirs(out_dir, exist_ok=True)

    by_book = {}
    for cid, chapter_data in results.items():
        info = parse_custom_id(cid)
        if info:
            by_book.setdefault(info["book"], {})[str(info["chapter"])] = chapter_data

    saved_books = saved_chapters = 0
    for book_nr in sorted(by_book):
        # Buchname aus der Quelldatei übernehmen
        src_file = os.path.join(ROOT, lang, src, f"{book_nr}_{src}.json")
        book_name = load_book(src_file)["name"] if os.path.exists(src_file) else f"Buch {book_nr}"

        out_path = os.path.join(out_dir, f"{book_nr}_{dst}.json")
        book = load_book(out_path) if os.path.exists(out_path) else {"name": book_name, "chapters": {}}
        book["name"] = book_name
        for chap_nr, verses in by_book[book_nr].items():
            book["chapters"][chap_nr] = verses
            saved_chapters += 1
        write_book(out_path, book)
        print(f"  ✓ {book_name}: {len(by_book[book_nr])} Kapitel")
        saved_books += 1
    return saved_books, saved_chapters


def main():
    if not API_KEY:
        print("\n  ⚠  Kein API-Key! → export ANTHROPIC_API_KEY='sk-ant-...'\n")
        sys.exit(1)

    batch_id, entry = get_batch_entry()
    status_only = "--status" in sys.argv
    wait_mode = "--wait" in sys.argv

    status = check_status(batch_id).get("processing_status", "unknown")
    while status != "ended" and wait_mode:
        print("  ... noch nicht fertig, warte 60s")
        time.sleep(60)
        status = check_status(batch_id).get("processing_status", "unknown")

    if status != "ended":
        if status == "in_progress":
            print("\n  Batch läuft noch. Mit --wait pollen oder später erneut aufrufen.")
        sys.exit(0)
    if status_only:
        sys.exit(0)

    print("\n  Lade Ergebnisse...")
    results, errors = download_results(batch_id)
    print(f"\n  Ergebnisse: {len(results)} ok, {len(errors)} Fehler")
    for cid, msg in errors[:20]:
        print(f"  {cid}: {msg}")
    if len(errors) > 20:
        print(f"  ... und {len(errors) - 20} weitere")
    if not results:
        print("\n  Keine Ergebnisse anzuwenden.")
        sys.exit(1)

    print("\n  ─── Wende Ergebnisse an ───")
    b, c = apply_results(results, entry)
    print(f"\n  ✓ Fertig: {b} Bücher, {c} Kapitel geschrieben.")
    if errors:
        print(f"  ⚠ {len(errors)} Kapitel fehlgeschlagen — betroffene Bücher neu einreichen.")


if __name__ == "__main__":
    main()
