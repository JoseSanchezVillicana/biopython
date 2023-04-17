"""
NAME
     T4-RAW_FASTA.py
     
VERSION
        1.0
AUTHOR
        José Antonio Sánchez Villicaña
        
DESCRIPTION

        Crea un archivo fasta a partir de la secuencia de DNA en formato raw
      
      input file (raw format)
ATCGACTGATCGATCGTACGAT
      
      output file (fastA format)
> sequence_name
ATCGACTGATCGATCGTACGAT

        
CATEGORY
        Genómica
USAGE
    % py T4-RAW_FASTA.py
    
TESTING

  github url input file: python1\dna.txt
  

"""

# Nombre del archivo de entrada con la secuencia en formato raw
input_file_name = input('Escribe ruta y nombre archivo con la secuencia de DNA: ')

# Nombre del archivo de salida
output_file_name = input('Escribe el nombre del archivo de salida (con extensión .fasta): ')

#Leer al archivo con la secuencia en formato raw
input_file = open(input_file_name)
dna_seq_raw = input_file.read()
input_file.close()

# Crear archivo de salida
output_file = open(output_file_name, 'w')

# Formateando secuencia a fastA y guardando en el archivo de salida
output_file.write('> sequence_name\n')
output_file.write(dna_seq_raw)
output_file.close()

print('Archivo convertido exitosamente')
