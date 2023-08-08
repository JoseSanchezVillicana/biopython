'''
NAME
       Piedra, papel o tijera

VERSION
        1.0

AUTHOR
        José Antonio Sánchez Villicaña
        Bernardo Chombo

DESCRIPTION
        Se trata de una simulación del juego clásico de piedra, papel o tijera en el que el usuario elegirá una de las opciones y la computadora elegirá otra al azar.
        Piedra le gana a las tijeras.
        Tijeras le ganan al papel.
        Papel le gana a la piedra.

CATEGORY
        Entretenimiento-

USAGE

    El usuario debe ingresar una de las tres opciones a través del teclado, el el formato que quiera y eso es todo!
    

ARGUMENTS
    elementos = lista con las opciones para el juego
    opc = controlador para seguir jugando
    decision = almacena la elección del uduario
    usuario = será el índice en la lista de elementos de la opción elegida por el usuario
    compu = almacena la elección de la computadora (generada al azar)

'''



# ===========================================================================
# =                            imports
# ===========================================================================
import random


# ===========================================================================
# =                             main
# ===========================================================================

elementos = ['piedra', 'papel', 'tijeras']

#Inicializo opc a 1 para que entre al menos una vez
opc = 1

while opc == 1:
    try: #Compruebo que el usuario introduzca un numero entero
        opc = int(input('¿Quieres jugar? 1: Sí, cualquier otro dígito: No\n'))
        if opc == 1:

            decision = input('Elige qué tirar [piedra, papel, tijeras]: ')
            #Me aseguro de que la palabra ingresada esté en el formato adecuado
            decision = decision.lower()

            #Busco la palabra en la lista de elementos posibles
            if decision in elementos:
                
                #Obtengo el índice de la palabra escogida por el usuario
                usuario = elementos.index(decision)

                #La computadora elige al azar
                compu = random.randint(0, 2)
                print(f'Computadora: {elementos[compu]}')

                #Comienzan evaluaciones para determinar al ganador
                if  usuario == compu:
                    print(f'UF! Yo también escogí {elementos[usuario]}, empate!')

                elif usuario > compu:
                    if compu == 0 and usuario == 2:
                        print(f'UPS! Gané!')
                    else:
                        print('OH NO! Perdí! Ganaste tu!')

                elif usuario < compu:
                    if compu == 2  and usuario == 0:
                        print(f'OH NO! Perdí! Ganaste tu!')
                    else:
                        print(f'UPS! Gané!')

            else: #ERROR en caso de que el usuario introduzca una cadena que no está en las opciones
                print('Opción inválida, debes elegir piedra, papel o tijera.')

    except: #ERROR en caso de que el usuario introduzca algo diferente a un numero entero
        print('ERROR debes ingresar un numero entero')

print('Hasta luego')