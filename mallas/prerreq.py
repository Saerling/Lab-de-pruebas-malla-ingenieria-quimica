#!/usr/bin/env python3
"""Lee mallas/prerrequisitos_validacion.txt y escribe los prerrequisitos en mallas/datos/<id>.json.
r  = requisitos confirmados en Acuerdo/PEP/malla (bloquean).   rv = requisitos por validar (solo informan).
Fichas: código de 7 dígitos, CRED_n (créditos aprobados), DISC_n (créditos disciplinares), "A|B" = alternativas.
Uso: python3 mallas/prerreq.py [--dry]"""
import json, re, os, sys, unicodedata
R = os.path.dirname(os.path.abspath(__file__))
TXT = open(os.path.join(R, 'prerrequisitos_validacion.txt'), encoding='utf-8').read()
SEC = {'AGRÍCOLA': 'agricola', 'ELÉCTRICA': 'electrica', 'MECÁNICA': 'mecanica', 'INDUSTRIAL': 'industrial', 'MECATRÓNICA': 'mecatronica', 'ELECTRÓNICA': 'electronica', 'DE SISTEMAS': 'sistemas', 'CIVIL': 'civil'}
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', unicodedata.normalize('NFD', t.lower()).encode('ascii', 'ignore').decode())).strip()
dry = '--dry' in sys.argv
partes = re.split(r'\n(?=\d\. INGENIER[ÍI]A )', TXT)
informe = []
for parte in partes[1:]:
    cab = parte.split('\n', 1)[0]
    pid = next(v for k, v in SEC.items() if k in cab.upper())
    f = os.path.join(R, 'datos', pid + '.json'); d = json.load(open(f, encoding='utf-8'))
    mats = [m for s in d['semestres'] for m in s['mat']]
    total = d['creditos']
    for m in mats: m.pop('r', None); m.pop('rv', None)
    porcod = {m['cod']: m for m in mats if m['cod']}
    pornom = {}
    for m in mats:
        n = norm(m['n']); pornom.setdefault(n, m)
        if n.startswith('optativa '): pornom.setdefault(n[9:], m)
    def ficha(m): return m['cod'] or m['n']                 # sin código: se referencia por nombre (embed.py lo resuelve)
    # códigos de las opciones de cada optativa («Optativa — X: A [c1] o B [c2]») → tarjeta de esa optativa
    for ln in parte.split('\n'):
        mo = re.match(r'^- Optativa\s*(?:—|-)\s*([^:]+?):\s*([^.]*)', ln)
        if not mo: continue
        n = norm(mo.group(1)); card = pornom.get(n)
        if card and not card['cod']:
            for c in re.findall(r'\[(\d{7})\]', mo.group(2).split('exig')[0]): porcod.setdefault(c, card)
    def buscar(cod, nombre, aprox=False):
        if cod and cod in porcod: return porcod[cod]
        n = norm(nombre or '')
        if not n: return None
        if n in pornom: return pornom[n]
        if aprox:                                            # solo para ubicar la tarjeta destino (p. ej. «Construcción de Obras Civiles» → «Optativa Construcción»)
            c = [m for m in mats if not m['cod'] and m['tipo'] == 'optativa' and (lambda k: k and (n.startswith(k) or k.startswith(n)))(norm(m['n'])[9:] if norm(m['n']).startswith('optativa ') else norm(m['n']))]
            if len(c) == 1: return c[0]
        return None
    def nombre_antes(txt, pos, ini):
        seg = txt[ini:pos]
        seg = re.split(r'(?:exigen?|requiere|listan?|además)\s', seg)[-1]
        return re.sub(r'^[\s\].;,:(]*(?:(?:y|e|o)\s+)?', '', seg).strip(' .')
    def reqs_de(txt):
        """Devuelve lista de fichas (AND) a partir de 'Nombre [cod] o Nombre2 [cod2] y ...'."""
        out, grupo, omit = [], [], []
        hits = list(re.finditer(r'\[(\d{7})(?:-B)?\]', txt))
        for i, h in enumerate(hits):
            alt = i > 0 and re.match(r'^\s*o\s', txt[hits[i - 1].end():h.start()])
            if not alt and grupo: out.append(grupo); grupo = []
            m = buscar(h.group(1), nombre_antes(txt, h.start(), hits[i - 1].end() if i else 0))
            if m: grupo.append(ficha(m))
            else: omit.append(h.group(1))
        if grupo: out.append(grupo)
        fichas = []
        for g in out:
            g = list(dict.fromkeys(g)); fichas.append('|'.join(g))
        for mm in re.finditer(r'(\d+) cr[ée]ditos (?:aprobados )?del componente (?:de formaci[óo]n )?disciplinar', txt): fichas.append('DISC_' + mm.group(1))
        for mm in re.finditer(r'(\d+) cr[ée]ditos aprobados \(\d+ ?% del', txt): fichas.append('CRED_' + mm.group(1))
        for mm in re.finditer(r'(\d+) ?% de cr[ée]ditos aprobados', txt): fichas.append('CRED_' + str(round(int(mm.group(1)) * total / 100)))
        return fichas, omit
    sem = 0; vistos = set(); malla_txt = {}
    for ln in parte.split('\n'):
        mm = re.match(r'^SEMESTRE ([IVX]+)\s*$', ln.strip())
        if mm: sem = ROM[mm.group(1)]; continue
        if not ln.startswith('- ') or not sem: continue
        cuerpo = ln[2:]
        conf = 'CONFIRMADO' in cuerpo
        val = ('POR VALIDAR' in cuerpo or 'flecha en la malla' in cuerpo or 'verificar' in cuerpo.lower()) and not conf
        mt = re.match(r'^([^:\[]+?) \[(\d{7})(?:-B)?(?:[^\]]*)\]:?\s*(.*)$', cuerpo)
        mo = None if mt else (re.match(r'^Optativa\s*(?:—|-)\s*([^:]+?):\s*(.*)$', cuerpo) or re.match(r'^([^:\[]+?) \(optativa\):\s*(.*)$', cuerpo) or re.match(r'^([^:\[(]+?):\s*(.*)$', cuerpo))
        if mt:
            nom, cod, req = mt.groups(); m = buscar(cod, nom, True)
            if m: malla_txt.setdefault(sem, []).append(m['cod'] or m['n'])
        elif mo:
            nom, req = mo.groups(); m = buscar(None, nom, True)
        else: continue
        if m and not m['cod'] and m['tipo'] == 'optativa' and norm(m['n']).startswith('optativa'):   # optativa: solo si todas las opciones piden lo mismo
            if req.count('exig') > 1: continue
            ex = re.search(r'exigen? (.*)', req)
            if ex: req = ex.group(1)
            elif not re.match(r'^\d+ cr', req.strip()): continue
        if not m: informe.append(f'{pid}: sin tarjeta para «{nom}»'); continue
        if not (conf or val): continue
        # nombres sueltos dentro de [POR VALIDAR: a; b]
        fichas, omit = reqs_de(req)
        for blo in re.findall(r'POR VALIDAR: ([^\]]+)\]', req):
            for nm in re.split(r'[;,]', blo):
                x = buscar(None, nm.strip())
                if x and ficha(x) not in fichas and x is not m: fichas.append(ficha(x))
        fichas = [x for x in fichas if x != ficha(m)]
        if omit: informe.append(f'{pid}: «{m["n"]}» omite requisitos fuera de la malla {omit}')
        if not fichas: continue
        clave = 'r' if conf else 'rv'
        m[clave] = list(dict.fromkeys(m.get(clave, []) + fichas)); vistos.add(m['n'])
        if conf: m.pop('rv', None)
    # semestres del texto vs. datos
    for s in d['semestres']:
        t = set(malla_txt.get(s['sem'], [])); dd = {(m['cod'] or m['n']) for m in s['mat']}
        fuera = [x for x in t if x not in dd]
        if fuera: informe.append(f'{pid}: semestre {s["sem"]} en el texto incluye {fuera} que en los datos está en otro semestre')
    nr = sum(1 for m in mats if m.get('r')); nv = sum(1 for m in mats if m.get('rv'))
    informe.append(f'== {pid}: {nr} con requisitos confirmados, {nv} por validar')
    d['prerrequisitos'] = 'Cargados de mallas/prerrequisitos_validacion.txt (14 nov 2026). r = confirmados en Acuerdo/PEP/malla; rv = por validar en el SIA (no bloquean).'
    if not dry: json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(informe))
