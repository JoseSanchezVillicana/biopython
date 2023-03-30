dna = 'AAGGTACGTCGCGCGTTATTAGCCTAT'
inicio = dna.find('TAC')
paro = dna.find('ATT')
print(f'Secuencia completa: {dna}\nTranscrito: {dna[inicio : paro]}')

