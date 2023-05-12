from Bio.Seq import Seq



texto = 'Hombres necios que acusáis \
         a la mujer sin razón \
         sin ver que sois la ocasión \
         de lo mismo que culpáis: \
         si con ansia sin igual \
         solicitáis su desdén \
         ¿por qué queréis que obren bien \
         si las incitáis al mal? '

palabras = {}

texto = texto.split()

for palabra in texto:
    if palabra not in palabras.keys():
        palabras[palabra] = 1
    else:
        palabras[palabra] += 1

i = 1
for key in palabras.keys():
    print(f'{i} - {key} : {palabras[key]}')
    i += 1

# Variables
dna = "AATGATGAACGAC" 
bases = ['A','T','G','C'] 
all_counts = {} 
# Creating dinucleotides and counting
for base1 in bases: 
    for base2 in bases: 
        dinucleotide = base1 + base2 
        count = dna.count(dinucleotide) 
        if count > 0: 
            all_counts[dinucleotide] = count

print(all_counts)


my_seq = Seq('AGTACACTGGT')
my_seq
print(my_seq)