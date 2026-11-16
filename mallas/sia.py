#!/usr/bin/env python3
"""Aplica los prerrequisitos del catálogo del SIA (sia_prerrequisitos.json) a datos/<id>.json.
Correr después de prereq.py y antes de embed.py. Las materias que el SIA confirma pasan a 'r' (bloquean);
lo que el SIA no cubre (tarjetas sin código, requisitos por créditos) queda como estaba."""
import json, os, re, unicodedata
R = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(R, 'sia_prerrequisitos.json'), encoding='utf-8'))
# Códigos del SIA que en la malla sugerida son una tarjeta optativa sin código
ALIAS = {'mecatronica': {'2017273': 'Optativa Ingeniería de Materiales y Procesos de Manufactura', '2017274': 'Optativa Ingeniería de Materiales y Procesos de Manufactura'},
         'electronica': {'1000013': 'Optativa Probabilidad y Estadística'}}
norm = lambda x: re.sub(r'\s+', ' ', ''.join(c for c in unicodedata.normalize('NFD', x.lower()) if unicodedata.category(c) != 'Mn')).strip()
for car, P in S['planes'].items():
    f = os.path.join(R, 'datos', car + '.json')
    if not os.path.exists(f): continue
    d = json.load(open(f, encoding='utf-8'))
    mats = [m for s in d['semestres'] for m in s['mat']]
    cods = {m['cod'] for m in mats if m['cod']}
    porNombre = {}
    for m in mats:
        porNombre.setdefault(norm(m['n']), m['cod'] or m['n']); porNombre.setdefault(norm(re.sub(r'^Optativa ', '', m['n'])), m['cod'] or m['n'])
    cambios = 0
    for m in mats:
        e = P.get(m['cod']) if m['cod'] else None
        m.pop('sia_nota', None)
        if not e or 'error' in e: continue
        conds, sueltas = [], []
        for c in e['prerrequisitos']:
            alts = c.get('una_de') or c.get('todas'); toks = []
            for a in alts:
                cod, nom = a.split(' ', 1); cod = cod.split('-')[0]
                t = cod if cod in cods else ALIAS.get(car, {}).get(cod) or porNombre.get(norm(nom))
                if t and t != (m['cod'] or m['n']) and t not in toks: toks.append(t)
            if not toks: sueltas.append(' o '.join(alts)); continue
            if 'todas' in c: conds += [[t] for t in toks]
            else: conds.append(toks)
        viejos = m.get('r', []) + m.get('rv', [])
        cred = [t for t in m.get('r', []) if re.match(r'^(CRED|DISC)_', t)]
        credv = [t for t in m.get('rv', []) if re.match(r'^(CRED|DISC)_', t)]
        nuevo = cred + ['|'.join(sorted(c)) for c in conds]
        if sueltas:   # requisito que el SIA pone con materias que no están en la malla sugerida
            nuevo += [t for t in viejos if not re.match(r'^(CRED|DISC)_', t) and t not in sum(conds, []) and not any(t in c for c in conds)]
        nuevo = list(dict.fromkeys(nuevo))
        if sorted(nuevo) != sorted(m.get('r', [])) or [t for t in m.get('rv', []) if t not in credv]:
            cambios += 1
        if nuevo: m['r'] = nuevo
        else: m.pop('r', None)
        if credv: m['rv'] = credv
        else: m.pop('rv', None)
        m['sia'] = True
        if sueltas: m['sia_nota'] = 'El SIA también pide: ' + '; '.join(sueltas)
    d['prerrequisitos_sia'] = S['consultado']
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(car, 'materias cambiadas:', cambios)
