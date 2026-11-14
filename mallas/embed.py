#!/usr/bin/env python3
"""Incrusta mallas/datos/*.json en index.html (bloque MALLAS_DATOS). Uso: python3 mallas/embed.py"""
import json, glob, os, re
R = os.path.dirname(os.path.abspath(__file__)); IDX = os.path.join(R, '..', 'index.html')
PLAN = {'agricola': '2541', 'civil': '2542', 'electrica': '2544', 'electronica': '2545', 'industrial': '2546', 'mecanica': '2547', 'mecatronica': '2548', 'sistemas': '2A74'}  # códigos de plan del SIA
F = json.load(open(os.path.join(R, 'fuentes.json'), encoding='utf-8'))
PDF = {p['id']: p['malla_pdf'] for p in F['programas']}
out = {}
for f in sorted(glob.glob(os.path.join(R, 'datos', '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    out[d['id']] = {'nombre': d['nombre'], 'creditos': d['creditos'], 'plan': PLAN[d['id']], 'pdf': PDF.get(d['id'], ''),
                    'semestres': [{'sem': s['sem'], 'mat': [{k: m[k] for k in ('cod', 'n', 'c', 'cat', 'agr', 'tipo', 'r') if k in m} for m in s['mat']]} for s in d['semestres']]}
blk = '<!--MALLAS_DATOS-->\n<script id="mallas-datos">window.MALLAS_DATOS = ' + json.dumps(out, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';</script>\n<!--/MALLAS_DATOS-->'
s = open(IDX, encoding='utf-8').read()
if '<!--/MALLAS_DATOS-->' in s: s = re.sub(r'<!--MALLAS_DATOS-->.*?<!--/MALLAS_DATOS-->', lambda _: blk, s, flags=re.S)
else: s = s.replace('<!--MALLAS_DATOS-->', blk, 1)
open(IDX, 'w', encoding='utf-8').write(s); print('incrustadas', len(out), 'carreras,', len(blk), 'caracteres')
