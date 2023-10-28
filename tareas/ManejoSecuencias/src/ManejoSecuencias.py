'''
NAME
        Manejo de Secuencias      

VERSION
        1.0

AUTHOR
        José Antonio Sánchez Villicaña

DESCRIPTION
        Script que recibe un archivo con secuencias en formato fastq y analiza su calidad,
        regresa un archivo .pkl con el diccionario de secuencias de mala calidad.
        {Seq ID} : [Seq]

CATEGORY
        Análisis de secuencias

USAGE

        Se tiene que proveer la ruta del archivo de texto con las secuencias en formato fastq
        Se puede proveer la ruta del directorio donde se quiere guardar el archivo generado
        Se puede proveer el nombre (sin extensión) del archivo binario a generar con extensión .pkl
        Se puede proveer el threshold para hacer el corte de calidad mínima


ARGUMENTS
        file_path (str) : path del archivo con las secuencias a analizar en formato fastqc
        threshold (int, optional) : threshold para hacer el corte de calidad, default: 30
        output_dir (str, optional) : path donde generar el archivo con el diccionario resultado, default: directorio actual
        output_file = args.name : nombre del archivo binario resultado sin extensión, default: 'results.pkl'
        
'''

# ===========================================================================
# =                            imports
# ===========================================================================
from Bio import SeqIO
import numpy as np
import os
import argparse
import pickle
concat_path = os.path.join

# ===========================================================================
# =                            functions
# ===========================================================================
def poor_qc(file= str, threshold: int = 30) -> dict:
    try:
        poor_seqs = {
            record.id : record.seq
            for record in SeqIO.parse(file, format='fastq')
            if np.asarray(record.letter_annotations['phred_quality']).mean() < threshold
        }
    except:
        raise OSError('Invalid input file path.')
    
    return poor_seqs

def get_args():
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
                        help= 'Output file name',
                        type= str,
                        default= 'results')
    
    parser.add_argument('-t', '--threshold',
                        metavar= 'threshold for quality',
                        type= int,
                        default= 30,
                        help= 'Threshold for quality')

    args = parser.parse_args()

    return args

def main():
    args = get_args()

    file_path = args.input
    threshold = args.threshold
    output_dir = args.output
    output_file = args.name

    poor_seqs = poor_qc(file= file_path, threshold= threshold)
    
    try:
        if len(poor_seqs) > 0:
            output_file += '.pkl'
            output_file = concat_path(output_dir, output_file)
            print(f'\n\tTotal of poor quality seqs: {len(poor_seqs)}\n\tDumping dict with Seqs ID and Seqs into {output_file}\n')
            with open(output_file, 'wb') as f:
                pickle.dump(poor_seqs, f)
    
    except (OSError):
        raise OSError('Invalid output path.')

# ===========================================================================
# =                             main
# ===========================================================================
if __name__ == "__main__":
    main() 
