import argparse
import os
import sys

def get_at_content(dna, sig_figs=2):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

def get_aa_percentage(prot, aa, sig_figs=2):
    prot = prot.upper().split('')
    aa_list = ['A', 'T', 'L', 'M', 'F', 'W', 'Y', 'V']
    length = len(prot)
    




#Parseo
my_parser = argparse.ArgumentParser(description='List the content of a folder')

my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))


#AT content fxn

content = get_at_content(sig_figs=4,dna='attgcttgcattcgct')

print(f'Contenido de AT {content}%')

#aa content fxn 
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
