'''
NAME
       SImulación de un animal

VERSION
        1.0

AUTHOR
        José Antonio Sánchez Villicaña

DESCRIPTION
        Se trata de una simulación de animales en un zoológico o algún tipo de reserva
        en el que los animales viven en lotes numerados. La simulación incluye un sistema
        en donde los animales se reproducen, crecen y existe la posibilidad de que mueran.


CATEGORY
        Simulación

USAGE

    El usuario debe ingresar el nombre del animal, su clase (mamífero u ovíparo), su altura, peso y progenie.
    Si desea utilizar la función de simulación debe ingresarlo y si desea un tiempo definido de años para esta
    (default son 5 años).}
    Como regla los animales sólo crecen los primeros 4 años de vida, sólo se reproducen después de los
    primeros 2 años de vida y sólo empieza a tener la posibilidad de morir a partir del sexto año de vida.
    Un ejemplo de uso con parámetros:
        -c (clase de animal)(Opcional) [str]
        -n (nombre) [str]
        -ha (numero de hábitat) [int]
        -ali (alimentación) [str]
        -alt (altura) [int]
        -p (progenie)(Opcional) [int]
        -s (simulación)(Opcional) [bool]
        -l (longitud de simulación)(Opcional) [int]
    

ARGUMENTS
    atributos de la clase animal:
        nombre
        numero de hábitat
    atributos de las clases mamífero y ovíparo (heredan a Animal):
        altura
        peso
        alimentación
        progenie
    Para la simulación:
        sim: bool para determinar si se realiza la simulación
        longitud: int que representa los años a simular la vida del animal

'''

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
from random import choice, randint

# ===========================================================================
# =                             main
# ===========================================================================

class Animal():
    def __init__(self, nombre, num_habitat):
        self.alive = True
        self.nombre = nombre
        self.num_habitat = num_habitat
    
    def muerte(self):
        self.alive = False
    
    def reproducirse(self, num):
        self.progenie += choice(range(num))
    
    def haz_ruido(self):
        print(f'{self.nombre} dice: %$&!?#!')

class Mamifero(Animal):
    def __init__(self, nombre, num_habitat, alimentacion, altura, peso, progenie):
        super().__init__(nombre, num_habitat)
        self.alimentacion = alimentacion
        self.altura = altura
        self.peso = peso
        self.progenie = progenie

    def haz_ruido(self):
        print(f'{self.nombre} dice: yo nací de una placenta')
    
    def crecer(self):
        self.altura += randint(2, 5)
        self.peso += randint(2, 5) * 2

class Oviparo(Animal):
    def __init__(self, nombre, num_habitat, alimentacion, altura, peso, progenie):
        super().__init__(nombre, num_habitat)
        self.alimentacion = alimentacion
        self.altura = altura
        self.peso = peso
        self.progenie = progenie
    
    def haz_ruido(self):
        print(f'{self.nombre} dice: yo nací de una placenta')
    
    def reproducirse(self, huevos):
        self.progenie += huevos
    
    def crecer(self):
        self.altura += randint(2, 5)
        self.peso += randint(2, 5) * 0.7

parser = argparse.ArgumentParser(description= 'Script que simula la vida de un animal.')

parser.add_argument('-c', '--clase',
                    metavar='String',
                    help= 'Que clase de animal es',
                    type= str,
                    choices= ['Oviparo', 'Mamifero', 'Animal'],
                    required= False,
                    default= 'Animal')

parser.add_argument('-n', '--nombre',
                    metavar='String con un nombre',
                    type= str,
                    help= 'Nombre del animal',
                    required=True)

parser.add_argument('-ha', '--habitat',
                    metavar='Numero de habitat',
                    type= str,
                    help= 'Numero del habitat donde vive',
                    required=True)

parser.add_argument('-ali', '--alimentacion',
                    metavar='Tipo de alimentacion',
                    type= str,
                    help= 'Tipo de alimentacion',
                    required=True)

parser.add_argument('-alt', '--altura',
                    metavar='Numero',
                    type= int,
                    help= 'Altura en cm',
                    required=True)

parser.add_argument('-p', '--peso',
                    metavar='Numero',
                    type= int,
                    help= 'Peso del animal en kg',
                    required=True)

parser.add_argument('-pr', '--progenie',
                    metavar='Numero',
                    type= int,
                    help= 'Cuanta progenie tiene en este momento',
                    required= False,
                    default= 0
                    )

parser.add_argument('-s', '--sim',
                    metavar='bool',
                    type= bool,
                    help= 'Si quieres hacer una simulacion de su vida',
                    required= False,
                    default= False
                    )

parser.add_argument('-l', '--longitud',
                    metavar='Numero',
                    type= int,
                    help= 'Cuantos años quieres simular su vida',
                    required= False,
                    default= 5
                    )

args = parser.parse_args()


if args.clase == 'Animal':
    animal = Animal(args.nombre, args.habitat)
else:
    if args.clase == 'Mamifero':
        animal = Mamifero(args.nombre,
                          args.habitat,
                          args.alimentacion,
                          args.altura,
                          args.peso,
                          args.progenie
                          )
    else:
        animal = Oviparo(args.nombre,
                        args.habitat,
                        args.alimentacion,
                        args.altura,
                        args.peso,
                        args.progenie
                        )
        
animal.haz_ruido()

if args.sim:
    for i in range(1, args.longitud):
        if i < 4:
            animal.crecer()
        if i > 2:
            animal.reproducirse(args.longitud)
        if randint(1, 100) % 2 == 0 and i > 5:
            animal.muerte()
        if not animal.alive:
            print(f'Morí a los {i} años')
            break
    if animal.alive:
        print(f'Yo {animal.nombre}, he vivido {i} años, tuve una progenie de {animal.progenie} hijos, ahora mido {animal.altura}cm y peso {animal.peso}kg.')
    else:
        print(f'Yo {animal.nombre}, viví {i} años, tuve una progenie de {animal.progenie} hijos, terminé midiendo {animal.altura}cm y pesé {animal.peso}kg.')
        print(f'RIP {animal.nombre}')