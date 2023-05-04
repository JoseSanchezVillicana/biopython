"""
Tarea 2

**Problema:**

- Hacer un programa que cuente el total de A, C, G y T que hay en una secuencia de DNA.

- La secuencia debe pedirse al usuario cada vez que se ejecute el programa.
"""

#Autor: José Antonio Sánchez Villicaña

dna = input('Introduce la secuencia de DNA a analizar: ')
As = dna.count('A')
Ts = dna.count('T')
Gs = dna.count('G')
Cs = dna.count('C')
print(f'Total por base\nA: {As}\tT:{Ts}\tG:{Gs}\tC:{Cs}')