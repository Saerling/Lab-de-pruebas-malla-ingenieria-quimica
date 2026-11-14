#!/usr/bin/env python3
"""Incrusta mallas/datos/*.json en index.html (bloque MALLAS_DATOS). Uso: python3 mallas/embed.py"""
import json, glob, os, re
R = os.path.dirname(os.path.abspath(__file__)); IDX = os.path.join(R, '..', 'index.html')
PLAN = {'agricola': '2541', 'civil': '2542', 'electrica': '2544', 'electronica': '2545', 'industrial': '2546', 'mecanica': '2547', 'mecatronica': '2548', 'sistemas': '2A74'}  # códigos de plan del SIA
F = json.load(open(os.path.join(R, 'fuentes.json'), encoding='utf-8'))
PDF = {p['id']: p['malla_pdf'] for p in F['programas']}
FUENTE = {'agricola': 'Acuerdo 030 de 2016', 'industrial': 'PEP 2020 (Acuerdo 024 de 2014)', 'civil': 'PEP 2018'}   # prerrequisitos confirmados
def ids(d):                                    # misma asignación de ids que la página (código, o L#/OP# en orden)
    L = O = 0; vistos = {}; por = {}
    for s in d['semestres']:
        for m in s['mat']:
            if m['cod']: mid = m['cod']
            elif m['tipo'] == 'libre': L += 1; mid = 'L%d' % L
            else: O += 1; mid = 'OP%d' % O
            if mid in vistos: vistos[mid] += 1; mid = '%s_%d' % (mid, vistos[mid])
            else: vistos[mid] = 1
            por.setdefault(m['cod'] or m['n'], mid); por.setdefault(m['n'], mid)
    return por
out = {}
for f in sorted(glob.glob(os.path.join(R, 'datos', '*.json'))):
    d = json.load(open(f, encoding='utf-8')); por = ids(d)
    res = lambda lst: ['|'.join(x if re.match(r'^(CRED|DISC)_\d+$', x) else por[x] for x in t.split('|') if re.match(r'^(CRED|DISC)_\d+$', x) or x in por) for t in lst]
    def mat(m):
        o = {k: m[k] for k in ('cod', 'n', 'c', 'cat', 'agr', 'tipo') if k in m}
        for k in ('r', 'rv'):
            if m.get(k): o[k] = [x for x in res(m[k]) if x]
        return o
    out[d['id']] = {'nombre': d['nombre'], 'creditos': d['creditos'], 'plan': PLAN[d['id']], 'pdf': PDF.get(d['id'], ''), 'fuente': FUENTE.get(d['id'], ''),
                    'semestres': [{'sem': s['sem'], 'mat': [mat(m) for m in s['mat']]} for s in d['semestres']]}
blk = '<!--MALLAS_DATOS-->\n<script id="mallas-datos">window.MALLAS_DATOS = ' + json.dumps(out, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';</script>\n<!--/MALLAS_DATOS-->'
s = open(IDX, encoding='utf-8').read()
if '<!--/MALLAS_DATOS-->' in s: s = re.sub(r'<!--MALLAS_DATOS-->.*?<!--/MALLAS_DATOS-->', lambda _: blk, s, flags=re.S)
else: s = s.replace('<!--MALLAS_DATOS-->', blk, 1)
open(IDX, 'w', encoding='utf-8').write(s); print('incrustadas', len(out), 'carreras,', len(blk), 'caracteres')
