elementos = ['piedra', 'papel', 'tijera']

opc = 1

while opc == 1:
    opc = int(input('¿Quieres jugar? 1: Sí, cualquier otro dígito: No\n'))
    if opc == 1:
        decision = input('Elige qué tirar: ')

        decision = decision.lower()
        
        if decision in elementos:
            index = elementos.index(decision)
            if index < 2:
                print(f'Perdiste! Yo escogí {elementos[index + 1]}')
            else:
                print(f'Perdiste! Yo escogí {elementos[0]}')
        else:
            print('Opción inválida')

print('Hasta luego')