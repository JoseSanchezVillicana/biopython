'''
NAME
        Archivo RAW a FASTA       

VERSION
        2.0

AUTHOR
        José Antonio Sánchez Villicaña

DESCRIPTION
        Crear un archivo fasta a partir de la secuencia en un archivo de texto
        Se modifica para que tenga el formato deseado

        Ejemplo de un archivo fasta:

        > sequence_name
        ATCGACTGATCGATCGTACGAT

CATEGORY
        Convertidor de archivos

USAGE

        Se tiene que proveer la ruta del archivo de texto con la secuencia de DNA
        Se tiene que proveer la ruta de la carpeta donde se quiere guardar el archivo generado
        Se tiene que proveer el nombre (sin la extensión fasta) del archivo a generar 


ARGUMENTS
        input_file = ruta del archivo de texto con la secuencia de DNA
        my_file = variable del archivo de texto con la secuencia
        my_file_content = variable que almacena el contenido del archivo de texto (la secuencia de DNA)
        target_dir = ruta del directorio donde se quiere guardar el archivo convertido
        output_file = nombre del archivo nuevo a generar (sin extensión .fasta)
        new_file = variable del archivo nuevo al que vamos a agregar el contenido del archivo de texto con el formato deseado
        
'''

# ===========================================================================
# =                            imports
# ===========================================================================
import os
import re
import argparse

# ===========================================================================
# =                            functions
# ===========================================================================

def formateo(my_file):

        my_file_content = ''
        size = os.path.getsize(args.input)
        isempty = size == 0
        
        if not isempty: #Verifico si el archivo está vacío

                for linea in my_file:
                     
                     linea = linea.replace('\n','')

                     if re.search(r'[^ATCG]', linea):
                        print('ERROR caracter extraño identificado (no es nucleótido)')
                        print(re.search(r'[^ATCG]', my_file_content))
                        quit()
                     
                     else:
                        my_file_content += '> sequence_name\n' + linea + '\n'
                
                my_file.close()
        else: 
                print('ERROR archivo vacío')
                quit()
        
        return my_file_content

# ===========================================================================
# =                             main
# ===========================================================================

#Manejo de Argumentos
parser = argparse.ArgumentParser(description= 'Script que convierte un archivo de texto con una secuencia de DNA en un archivo tipo fasta')

parser.add_argument('-i', '--input',
                    metavar='path/output/file',
                    help= 'Input file path',
                    required=True)

parser.add_argument('-o', '--output',
                    metavar='path/output/file',
                    help= 'Output file path',
                    required=True)

parser.add_argument('-n', '--name',
                    metavar='path/output/file',
                    help= 'Output file name',
                    required=True)

args = parser.parse_args()


#Accedo al archivo con la secuencia
try:
    my_file = open(args.input)
except (FileNotFoundError):
    print('ERROR Ruta invalida')
    quit()

#Llamada a fxn que formatea y verifica el archivo de entrada
my_file_content = formateo(my_file)


#Verifico que la ruta target es correcta
try:
    os.chdir(args.output)
except (OSError):
    print('ERROR Ruta invalida')
    quit()

#Generación del nuevo archivo en formato fasta
try:
    #Abro el archivo que se va a generar, con w para que reescriba lo que tenga si es que existe
    new_file = open(args.name, 'w')

    #Introduzco la secuencia obtenida a partir del archivo introducido por el usuario
    new_file.write(my_file_content)
    new_file.close()

except:
    print(f'ERROR al intentar crear el archivo {args.name}')
    quit()
else:
    print('Archivo convertido exitosamente')