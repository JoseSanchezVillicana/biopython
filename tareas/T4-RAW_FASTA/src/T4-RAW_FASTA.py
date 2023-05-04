'''
NAME
        Archivo RAW a FASTA       

VERSION
        2.0

AUTHOR
        José ANtonio Sánchez Villicaña

DESCRIPTION
        Crear un archivo fasta a partir de la secuencia en un archivo de texto
        Se modifica para que tenga el formato deseado

        Ejemplo de un archivo fasta:

        > sequence_name
        ATCGACTGATCGATCGTACGAT

CATEGORY
        Convertidor de archivos

USAGE

        Se tiene que proveer la ruta absoluta del archivo de texto con la secuencia de DNA
        Se tiene que proveer la ruta absoluta de la carpeta donde se quiere guardar el archivo generado
        Se tiene que proveer el nombre (sin la extensión fasta) del archivo a generar 


ARGUMENTS
        input_file = ruta del archivo de texto con la secuencia de DNA
        my_file = variable del archivo de texto con la secuencia
        my_file_content = variable que almacena el contenido del archivo de texto (la secuencia de DNA)
        target_dir = ruta del directorio donde se quiere guardar el archivo convertido
        output_file = nombre del archivo nuevo a generar (sin extensión .fasta)
        new_file = variable del archivo nuevo al que vamos a agregar el contenido del archivo de texto con el formato deseado
        
'''
#TESTING
        #Ruta de archivo de texto a utilizar para pruebas -> #C:\Users\Pepe S\Documents\Genomicas\2doSemestre\Python\python1\tareas\T4-RAW_FASTA\data\dna.txt
        #Ruta donde queremos guardar el archivo final -> #C:\Users\Pepe S\Documents\Genomicas\2doSemestre\Python\python1\tareas\T4-RAW_FASTA\doc
        #Para la prueba se está guardando el archivo generado en la carpeta doc de esta tarea
        #En el README de esta tarea se explica por qué esta sección de testing no está en el encabezado


# ===========================================================================
# =                            imports
# ===========================================================================
import os


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
my_file_content = my_file.read()
my_file.close()

#Obtengo ruta de la carpeta donde se guardará el archivo y me muevo ahí
target_dir = input('Ingresa la ruta de la carpeta donde se guardará el archivo convertido: ')
try:
    os.chdir(target_dir)
except (FileNotFoundError):
    print('ERROR Ruta invalida')
    quit()

#Nombre del archivo de salida
output_file = input('Escribe el nombre del archivo de salida (sin la extensión .fasta): ')
output_file += '.fasta'

#Generación del nuevo archivo en formato fasta
try:
    #Abro el archivo que se va a generar, con w para que reescriba lo que tenga si es que existe
    new_file = open(output_file, 'w')
    #Introduzco el formato deseado antes de la secuencia
    new_file.write('> sequence_name\n')
    #Introduzco la secuencia obtenida a partir del archivo introducido por el usuario
    new_file.write(my_file_content)
    new_file.close()
except:
    print(f'ERROR al intentar crear el archivo {output_file}')
else:
    print('Archivo convertido exitosamente')