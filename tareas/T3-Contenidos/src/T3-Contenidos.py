"""
Tarea 3

**Problema:**
 
 ¿Cuál es el porcetaje de `AT` y `GC` en la secuencia del archivo `dna.txt`
 

- Escribe un programa que te regrese el porcentaje de AT y GC
- El programa debe preguntar la ruta y el nombre del archivo de DNA de manera interactiva.
"""

#Autor: José Antonio Sánchez Villicaña

#Ruta utilizada
#C:\Users\Pepe S\Documents\Genomicas\2doSemestre\Python\python1\dna.txt

#Pido la ruta del archivo
path = input('Introduce la ruta del archivo con la secuencia: ')

#Abro el archivo con la ruta proporcionada
my_file = open(path)

#Leo el archivo
my_file_content = my_file.read()

#Cuento el total de nucleótidos y cada uno
total = len(my_file_content)
As = my_file_content.count('A')
Ts = my_file_content.count('T')
Gs = my_file_content.count('G')
Cs = my_file_content.count('C')

print(f'Proporciones\nAT: {((As + Ts) * 100 ) / total}%\nGC: {((Gs + Cs) * 100 ) / total}%')