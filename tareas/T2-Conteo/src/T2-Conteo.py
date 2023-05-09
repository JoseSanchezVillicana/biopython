'''
NAME
        Conteo de nucleótidos       

VERSION
        2.0

AUTHOR
        José ANtonio Sánchez Villicaña

DESCRIPTION
        Es un programa sencillo que cuenta los nucleótidos en una secuencia de DNA
        dada por el usuario mediante un archivo de texto.

CATEGORY
        Conteo

USAGE

        Se tiene que proveer la ruta absoluta del archivo de texto con la secuencia de DNA
        Se despliega los conteos 


ARGUMENTS
        input_file = ruta del archivo de texto con la secuencia de DNA
        my_file = variable del archivo de texto con la secuencia
        my_file_content = variable que almacena el contenido del archivo de texto (la secuencia de DNA)
        size = almacenará el tamaño en bytes del archivo ingresado
        isempty = booleano que nos indicará, en base a la variable size, si el archivo está vacío o no
        As = contenido de A
        Ts = contenido de T
        Gs = contenido de G
        Cs = contenido de C
        
'''
#TESTING
        #Ruta de archivo de texto a utilizar para pruebas -> 'C:\Users\Pepe S\Documents\Genomicas\2doSemestre\Python\python1\tareas\T2-Conteo\data\dna.txt'
        #En el README de esta tarea se explica por qué esta sección de testing no está en el encabezado


# ===========================================================================
# =                            imports
# ===========================================================================
import os
import re

# ===========================================================================
# =                             main
# ===========================================================================

#Accedo al archivo con la secuencia
input_file = input('Escribe la ruta del archivo con la secuencia de DNA: ')
try:
    my_file = open(input_file)
except (FileNotFoundError):
    print('ERROR Ruta invalida')
    quit()

#Leo el contenido
size = os.path.getsize(input_file)
isempty = size == 0
if not isempty: #Verifico si el archivo está vacío
        my_file_content = my_file.read()
        #Elimino saltos de línea
        my_file_content = my_file_content.replace('\n','')
        if re.search(r'[^ATCG]', my_file_content):
             print('ERROR caracter extraño identificado (no es nucleótido)')
             quit()
        my_file.close()
else: 
     print('ERROR archivo vacío')
     quit()

#Conteo
As = my_file_content.count('A')
Ts = my_file_content.count('T')
Gs = my_file_content.count('G')
Cs = my_file_content.count('C')

print(f'Total por base\nA: {As}\tT:{Ts}\tG:{Gs}\tC:{Cs}')