'''
NAME
        Identificación marco de lectura   

VERSION
        2.0

AUTHOR
        José ANtonio Sánchez Villicaña

DESCRIPTION
        Es un programa sencillo que identifica un marco de lectura un codón de inicio y uno de paro específicos
        a partir de una secuencia de RNA

CATEGORY
        Identificación

USAGE

        Se determinan la secuencia, codón de inicio y codón de paro en el mismo código


ARGUMENTS
        rna = almacena la secuencia en forma de cadena
        inicio = almacena lo que utilizará como codón de inicio
        paro = almacena lo que utilizará como codón de paro
        
'''


# ===========================================================================
# =                             main
# ===========================================================================


rna = 'AAGGTACGTCGCGCGTTATTAGCCTAT'
inicio = rna.find('TAC')
paro = rna.find('ATT')
print(f'Secuencia completa: {rna}\nTranscrito: {rna[inicio : paro]}')

