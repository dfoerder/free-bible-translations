import sys, json
sys.path.insert(0, '/Users/dfoerd/Documents/projekte/bibel/bibles-translations/tools')
from common import load_book, write_book

TARGET = '/Users/dfoerd/Documents/projekte/bibel/bibles-translations/fra/lsg1910mod/18_lsg1910mod.json'

def update_chapter(chapter_num, verses_dict):
    book = load_book(TARGET)
    ch = str(chapter_num)
    assert ch in book['chapters'], f"chapter {ch} missing in target"
    existing_keys = set(book['chapters'][ch].keys())
    new_keys = set(verses_dict.keys())
    assert existing_keys == new_keys, f"key mismatch ch{ch}: existing={existing_keys - new_keys} new={new_keys - existing_keys}"
    book['chapters'][ch] = {str(k): v for k, v in verses_dict.items()}
    write_book(TARGET, book)
    print(f"Chapter {chapter_num} written, {len(verses_dict)} verses.")

if __name__ == '__main__':
    pass
