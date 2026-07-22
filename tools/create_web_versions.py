#!/usr/bin/env python3
"""Create web versions from modernized translations."""

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LANGUAGES = {
    'fra': ('lsg1910mod', 'lsg1910'),
    'ita': ('riv1927mod', 'riv1927'),
    'spa': ('rv1909mod', 'rv1909'),
}

def create_web_versions():
    """Create web versions from modernized translations."""

    for lang_code, (mod_version, orig_version) in LANGUAGES.items():
        lang_dir = REPO_ROOT / lang_code
        mod_dir = lang_dir / mod_version
        orig_dir = lang_dir / orig_version
        web_dir = lang_dir / 'web'

        if not mod_dir.exists():
            print(f"❌ {lang_code}: {mod_dir} does not exist")
            continue

        # Create web directory
        web_dir.mkdir(exist_ok=True)

        # Get all books from the modernized version
        mod_files = sorted(mod_dir.glob(f'*_{mod_version}.json'))
        print(f"\n📖 {lang_code.upper()} ({mod_version}):")
        print(f"   Found {len(mod_files)} books")

        for mod_file in mod_files:
            # Extract book number (e.g., "1" from "1_lsg1910mod.json")
            book_num = mod_file.stem.split('_')[0]
            web_file = web_dir / f'{book_num}_web.json'

            try:
                # Read the modernized version
                with open(mod_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Write as web version
                with open(web_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=0)

                print(f"   ✓ {book_num}: {data.get('name', '?')} → {web_file.name}")
            except Exception as e:
                print(f"   ✗ {book_num}: Error - {e}")

        print(f"   Total: {len(list(web_dir.glob('*_web.json')))} web files in {web_dir.name}/")

if __name__ == '__main__':
    create_web_versions()
