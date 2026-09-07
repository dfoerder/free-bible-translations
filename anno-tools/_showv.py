import json,glob,os,sys
import common as C
src=C.load_source(40)['chapters']
for arg in sys.argv[1:]:
    k,v=arg.split(',')
    print('=== Matthieu',k+','+v)
    print('   ',src[k][v])
    for p in sorted(glob.glob(os.path.join(C.ANNO_DIR,'40_*.json'))):
        d=json.load(open(p)); ch=d.get('chapters',d)
        if k in ch and v in ch[k]:
            for e in ch[k][v]:
                sp = str(e.get('pos'))+('-'+str(e['pos_end']) if 'pos_end' in e else ('/'+str(e['parts']) if 'parts' in e else ''))
                print(f"  {sp:12} {str(e.get('form')):26} {str(e.get('lemma')):18} {e.get('level')}  {e.get('de')} · {e.get('en')} · {e.get('es')} · {e.get('it')}")
