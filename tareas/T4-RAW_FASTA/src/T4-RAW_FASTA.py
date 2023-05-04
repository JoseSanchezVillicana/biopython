"""
Tarea 4

**Problema:**

Crear un archivo fasta a partir de la secuencia de DNA que está en `dna.txt`

Ejemplo de un archivo fasta:

```
> sequence_name
ATCGACTGATCGATCGTACGAT
"""
#Autor: José Antonio Sánchez Villicaña


#Ruta a utilizar para pruebas
#C:\Users\Pepe S\Documents\Genomicas\2doSemestre\Python\python1\dna.txt

#Ruta del archivo con la secuencia
input_file = input('Escribe la ruta del archivo con la secuencia de DNA: ')

#Nombre del archivo de salida
output_file = input('Escribe el nombre del archivo de salida (con extensión .fasta): ')

#Accedo al archivo con la secuencia
my_file = open(input_file)

#Leo el contenido
my_file_content = my_file.read()
my_file.close()

#Abro el archivo que se va a generar, con w para que reescriba lo que tenga si es que existe
new_file = open(output_file, 'w')
#Introduzco el formato deseado antes de la secuencia
new_file.write('> sequence_name\n')
#Introduzco la secuencia obtenida a partir del archivo introducido por el usuario
new_file.write(my_file_content)
new_file.close()

print('Archivo convertido exitosamente')
