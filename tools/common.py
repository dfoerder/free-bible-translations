#!/usr/bin/env python3
"""Gemeinsame Helfer für die Werkzeuge der Übersetzungssammlung.

Kanonisches Dateiformat (ein Buch pro Datei):

    {
    "name": "1. Mose",
    "chapters": {
    "1": {
    "1": "Im Anfang schuf Gott ...",
    "2": "..."}
    ...
    }}

Serialisiert mit ``json.dumps(obj, ensure_ascii=False, indent=0)`` — dadurch
steht jeder Vers auf einer eigenen Zeile (git-Diffs bleiben lesbar), ohne
nennenswerten Größen-Aufschlag gegenüber kompaktem JSON.
"""
import json
import os

# Projektwurzel = Elternverzeichnis von tools/
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def dump_canonical(obj):
    """Serialisiere ein Buch-Objekt in das kanonische Format (String)."""
    name = obj.get("name", "")
    chapters = obj.get("chapters", {})
    ordered = {
        "name": name,
        "chapters": {
            str(c): {
                str(v): chapters[c][v]
                for v in sorted(chapters[c], key=int)
            }
            for c in sorted(chapters, key=int)
        },
    }
    return json.dumps(ordered, ensure_ascii=False, indent=0) + "\n"


def write_book(path, obj):
    """Schreibe ein Buch-Objekt kanonisch nach ``path``."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(dump_canonical(obj))


def load_book(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def iter_translation_dirs(root=ROOT):
    """Liefere (lang, version, dir_path) für jede <lang>/<version>/-Ebene."""
    for lang in sorted(os.listdir(root)):
        lang_dir = os.path.join(root, lang)
        if not os.path.isdir(lang_dir) or lang.startswith(".") or lang == "tools":
            continue
        # Sprachcodes sind 3-Buchstaben (ISO 639-3): deu, eng, fra, ...
        if len(lang) != 3:
            continue
        for version in sorted(os.listdir(lang_dir)):
            vdir = os.path.join(lang_dir, version)
            if os.path.isdir(vdir) and not version.startswith("."):
                yield lang, version, vdir


def book_files(vdir):
    """Buchdateien eines Übersetzungsordners, nach Buchnummer sortiert."""
    files = [f for f in os.listdir(vdir) if f.endswith(".json")]

    def booknr(fn):
        return int(fn.split("_", 1)[0])

    return sorted(
        (os.path.join(vdir, f) for f in files if f.split("_", 1)[0].isdigit()),
        key=lambda p: booknr(os.path.basename(p)),
    )
