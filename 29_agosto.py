from random import choice, seed

class Mamifero():
    def __init__(self, alimentacion, altura, peso, progenie= 0):
        self.alimentacion = alimentacion
        self.altura = altura
        self.peso = peso
        self.progenie = progenie

    def haz_ruido(self):
        print(f'Dice: AAAAHHHHHH')

class Placentario(Mamifero):

    def __init__(self, alimentacion, altura, peso, acuatico, progenie= 0):
        super().__init__(alimentacion, altura, peso, progenie)
        self.acuatico = acuatico
    
    def crecer(self, crecimiento):
        self.altura += crecimiento
        self.peso += crecimiento * 2
    

class Marsupial(Mamifero):

    def __init__(self, alimentacion, altura, peso, progenie= 0):
        super().__init__(alimentacion, altura, peso, progenie)

    def crecer(self, crecimiento):
        self.altura += crecimiento
        self.peso += crecimiento * 0.7

cachalote = Placentario(alimentacion='carnivoro', altura=200, peso=41*10**3, acuatico= True)

tlacuache = Marsupial('omnívoro',30, 1.2)

for mamiferito in [cachalote, tlacuache]:
    mamiferito.crecer(10)

print(cachalote.peso, tlacuache.peso)