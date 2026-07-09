#!/usr/bin/env python3
"""Normalisiert und validiert die JSON-Dateien der Übersetzungssammlung.

Bringt jede Buchdatei in das kanonische Format (siehe common.py) und prüft
dabei die Datenintegrität.

Verwendung:
  python3 tools/normalize.py                 # gesamte Sammlung normalisieren
  python3 tools/normalize.py deu             # nur eine Sprache
  python3 tools/normalize.py deu/l1912mod    # nur eine Übersetzung
  python3 tools/normalize.py --check         # nur prüfen, nichts schreiben
"""
import sys

from common import (
    ROOT,
    book_files,
    dump_canonical,
    iter_translation_dirs,
    load_book,
)


def check_book(path):
    """Gib (verse_count, [fehler]) für eine Buchdatei zurück."""
    errors = []
    try:
        data = load_book(path)
    except (OSError, ValueError) as e:
        return 0, [f"kann nicht gelesen/geparst werden: {e}"]

    if "name" not in data or not str(data.get("name", "")).strip():
        errors.append("fehlender/leerer 'name'")
    if "chapters" not in data or not isinstance(data["chapters"], dict):
        errors.append("fehlendes 'chapters'-Objekt")
        return 0, errors

    verses = 0
    for c, vv in data["chapters"].items():
        if not str(c).isdigit():
            errors.append(f"nicht-numerischer Kapitelschlüssel: {c!r}")
        if not isinstance(vv, dict):
            errors.append(f"Kapitel {c}: kein Objekt")
            continue
        for v, txt in vv.items():
            verses += 1
            if not str(v).isdigit():
                errors.append(f"Kapitel {c}: nicht-numerischer Versschlüssel {v!r}")
            if not isinstance(txt, str):
                errors.append(f"Kapitel {c}:{v}: Wert ist kein String")
            elif not txt.strip():
                errors.append(f"Kapitel {c}:{v}: leerer Text")
    return verses, errors


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv
    scope = args[0].strip("/") if args else ""

    total_files = total_verses = total_errors = changed = 0

    for lang, version, vdir in iter_translation_dirs(ROOT):
        rel = f"{lang}/{version}"
        if scope and not (rel == scope or lang == scope):
            continue

        files = book_files(vdir)
        v_sum = 0
        errs = 0
        for path in files:
            verses, errors = check_book(path)
            v_sum += verses
            total_files += 1
            for e in errors:
                print(f"  ✗ {path.replace(ROOT + '/', '')}: {e}")
                errs += 1

            if not errors and not check_only:
                canonical = dump_canonical(load_book(path))
                with open(path, "r", encoding="utf-8") as f:
                    current = f.read()
                if current != canonical:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(canonical)
                    changed += 1

        flag = "" if len(files) == 66 else f"  ⚠ {len(files)} Bücher (erwartet 66)"
        print(f"  {rel:20s} {len(files):3d} Bücher  {v_sum:6d} Verse{flag}")
        total_verses += v_sum
        total_errors += errs

    action = "geprüft" if check_only else "normalisiert"
    print(f"\n  {total_files} Dateien {action}, {total_verses} Verse gesamt, "
          f"{changed} geändert, {total_errors} Fehler")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
