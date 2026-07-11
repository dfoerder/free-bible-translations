#!/usr/bin/env python3
"""Versweise Gegenüberstellung für Modernisierungs-Piloten (stdout/Markdown)."""
import json
import re
import sys
from difflib import SequenceMatcher

from common import load_book


def tokenize(s):
    return re.findall(r"\w+|[^\w\s]", s, re.UNICODE)


def word_diff(a, b):
    wa, wb = tokenize(a), tokenize(b)
    sm = SequenceMatcher(None, wa, wb)
    left, right = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            left.extend(wa[i1:i2])
            right.extend(wb[j1:j2])
        elif tag == "replace":
            left.append(f"[-{' '.join(wa[i1:i2])}-]")
            right.append(f"[+{' '.join(wb[j1:j2])}+]")
        elif tag == "delete":
            left.append(f"[-{' '.join(wa[i1:i2])}-]")
        elif tag == "insert":
            right.append(f"[+{' '.join(wb[j1:j2])}+]")
    return " ".join(left), " ".join(right)


def compare_chapter(src_ch, variants, labels):
    keys = sorted(src_ch.keys(), key=int)
    rows = []
    for k in keys:
        src = src_ch[k]
        texts = [src] + [variants[l][k] for l in labels]
        changed = [t != src for t in texts[1:]]
        if not any(changed):
            continue
        rows.append((k, src, {l: variants[l][k] for l in labels}, changed))
    return rows


def main():
    if len(sys.argv) < 4:
        print("Usage: compare_pilot.py <src_book.json> <ch> <mod1.json> [mod2.json ...]")
        print("  Labels from filenames: mateo_pilot, grok, light, ...")
        sys.exit(1)

    src_path, chap = sys.argv[1], sys.argv[2]
    mod_paths = sys.argv[3:]

    src = load_book(src_path)
    src_ch = src["chapters"][chap]

    variants, labels = {}, []
    for p in mod_paths:
        data = load_book(p)
        ch = data["chapters"].get(chap)
        if not ch:
            print(f"  ⚠ {p}: chapter {chap} missing")
            sys.exit(1)
        label = p.split("/")[-1].replace(".json", "").replace("_rv1909mod", "").replace("40_", "mateo_")
        labels.append(label)
        variants[label] = ch

    rows = compare_chapter(src_ch, variants, labels)
    total = len(src_ch)
    print(f"# {src['name']} {chap} — {len(rows)}/{total} verses changed in at least one variant\n")

    for k, src_v, mods, changed in rows:
        print(f"## V.{k}\n")
        print(f"**RV1909:** {src_v}\n")
        for lab, ch in zip(labels, changed):
            if not ch:
                continue
            lv, rv = word_diff(src_v, mods[lab])
            print(f"**{lab}:** {mods[lab]}")
            if lv != rv:
                print(f"  diff: `{lv}` → `{rv}`")
            print()


if __name__ == "__main__":
    main()