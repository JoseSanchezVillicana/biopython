'''
NAME
        GenBank Analyzer      

VERSION
        1.0

AUTHOR
        José Antonio Sánchez Villicaña

DESCRIPTION
        Script que recibe un archivo fromato GenBank y regresa un archivo con la info solicitada (Anotaciones y Genes)
            La info de los genes es la siguiente:
                Gen_1:  X
                DNA: [primeros 15 nt]...
                RNA: [primeros 15 nt del RNA transcrito]...
                Prot: [primeros 5 aa de la proteína codificada]...

CATEGORY
        Parseador de archivos

USAGE

        Se tiene que proveer la ruta del archivo de texto formato GenBank
        Se puede proveer la ruta del directorio donde se quiere guardar el archivo generado
        Se puede proveer el nombre (sin extensión) del archivo de texto a generar con extensión .txt
        Se puede proveer una lista de argumentos de anotaciones que se desea conservar
        Se puede proveer una lista con los genes que se desea conservar


ARGUMENTS
        file_path (str) : path del archivo con las secuencias a analizar en formato fastqc
        annots (list, optional) :  lista con los atributos de las anotaciones a conservar, default: all
        genes (list, optional) : lista con los genes a conservar, default: all
        output_dir (str, optional) : path donde generar el archivo con el diccionario resultado, default: directorio actual
        output_file = args.name : nombre del archivo binario resultado sin extensión, default: 'results.pkl'
        
'''

# ===========================================================================
# =                            imports
# ===========================================================================
from Bio import SeqIO
import os
import argparse
concat_path = os.path.join

# ===========================================================================
# =                            functions
# ===========================================================================
def get_annotations(file : str, anotations_wanted : list = ['all']):
    anot = {}
    for record in SeqIO.parse(file, format='genbank'):
        for anotation, value in record.annotations.items():
            if anotations_wanted[0] == 'all':
                anot[anotation] = value
            elif anotation in anotations_wanted:
                anot[anotation] = value
    return anot

def resumen(info_file: str, write_file: str, genes: list = ['all']):
    i = 1
    with open(write_file, 'a') as f:
        for record in SeqIO.parse(info_file, format='genbank'):
            for feat in record.features:
                if feat.type == 'source':
                    f.write(f'\n# Country: {str(record.features[0].qualifiers["country"][0])}')
                elif feat.type == 'gene' and (feat.qualifiers['gene'][0] in genes or genes[0] == 'all'):
                    f.write(f'\n# Gene_{i}:\t{feat.qualifiers["gene"][0]}')
                    seq = record.seq[
                        feat.location.nofuzzy_start 
                        :
                        feat.location.nofuzzy_end
                    ]
                    f.write(f'\n# DNA:\t{seq[0:15]}...')
                    f.write(f'\n# RNA:\t{seq[0:15].transcribe()}...')
                    f.write(f'\n# Prot:\t{seq[0:15].translate()}...')
                    i += 1

def get_args():
    def list_of_strings(arg):
        return arg.split(',')
    
    parser = argparse.ArgumentParser(description= 'Script que recibe un archivo con secuencias fasta y regresa las secuencias de mala calidad. El threshold de mala calidad lo recibe como un argumento, el default es 30.')

    parser.add_argument('-i', '--input',
                        metavar= 'path/input/file',
                        help= 'Input file path of sequences in fastq format',
                        required= True)

    parser.add_argument('-o', '--output',
                        metavar='path/output/file',
                        help= 'Output file path to dump dict with info.',
                        default= os.getcwd())

    parser.add_argument('-n', '--name',
                        metavar='path/output/file/name',
                        help= 'Output file name, without extension',
                        type= str,
                        default= 'results')
    
    parser.add_argument('-g', '--genes',
                        metavar= 'genes to search for',
                        type= list_of_strings,
                        default= ['all'],
                        help= 'Genes to search for.')
    
    parser.add_argument('-a', '--annot',
                        metavar= 'annotation to include',
                        type= list_of_strings,
                        default= ['all'],
                        help= 'Annotation to include')

    args = parser.parse_args()

    return args

def main():
    args = get_args()

    file_path = args.input
    output_dir = args.output
    output_file = args.name
    genes = args.genes
    annots = args.annot

    if not os.path.isdir(output_dir):
        raise OSError('Invalid output path.')
    else:
        output_file += '.txt'
        output_file = concat_path(output_dir, output_file)
        with open(output_file, "w") as f:
            metadata = get_annotations(
                file= file_path,
                anotations_wanted= annots
            )
            for anot, value in metadata.items():
                f.write(f'\n# {anot}:\t{value}')
        resumen(
            info_file= file_path,
            write_file= output_file,
            genes= genes
        )
            
# ===========================================================================
# =                             main
# ===========================================================================
if __name__ == "__main__":
    main() 
