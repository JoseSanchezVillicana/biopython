import re

seq = 'ATCGCGpAATTCAnCGGACC'
dna = 'GGGATTT'

match = re.findall(r'[^ATGC]', seq)

if match:
    print(f'Base ambigua, el caracter extraño fue {match[0]} y {match[1]}')


scientific_name = 'Homo sapiens'

match = re.search(r'(.+) (.+)', scientific_name)

if match:
    print(f'Especie encontrada {match.group(1)} {match.group(2)}')


dna = 'CTGCATTATATCGTACGAAATTATACGCGCG'

match = re.finditer('[AT]{5,}', dna)

for m in match:
    print(f'Secuencia {m.group()} encontrada en la posición {m.start()}')

dna = 'CGCTCnTAGATGCGCrATGACTGCAyTG'

result1 = re.split(r'[^ATGC]', dna)
result2 = ''
for element in result1:
    result2 += element
print(f'Cadena original: {dna}\nComo cadena habiendo eliminado caracteres ambiguos y lista para analizar: {result2}')

match1 = re.finditer('[AT]{5,}', result2)

for m in match1:
    if m:
        print(f'Secuencia {m.group()} encontrada en la posición {m.start()}')
    else:
        print('No tiene regiones ricas en AT')

if match1:
    print('No está vacío')
    