"""Erzeugt catalog.json für die Bibel-App: je Übersetzung alle .json-Dateien (Text, anno/, train/)
mit Grösse und eine Version (Hash über alle Dateiinhalte). Ändert sich eine Datei, ändert sich die
Version, und die App bietet ein Update an.  Aufruf im Repo-Wurzelordner:  python3 tools/build_catalog.py"""
import hashlib, json, os
cfg = json.load(open('tools/catalog-config.json', encoding='utf-8'))
out = {'format': 1, 'translations': {}}
for tid, c in cfg.items():
    if tid.startswith('_'): continue
    files, h, total = [], hashlib.sha256(), 0
    for base in c['paths']:
        for root, _, names in os.walk(base):
            for n in names:
                if n.endswith('.json'): files.append(os.path.join(root, n).replace(os.sep, '/'))
    files.sort()
    for f in files:
        data = open(f, 'rb').read(); total += len(data)
        h.update(f.encode() + b'\0' + hashlib.sha256(data).digest())
    out['translations'][tid] = {'version': h.hexdigest()[:12], 'bytes': total, 'files': files}
with open('catalog.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, ensure_ascii=False, separators=(',', ':'))
for tid, t in out['translations'].items():
    print(f"{tid:16} {len(t['files']):4} Dateien  {t['bytes']/1e6:6.1f} MB  v{t['version']}")
