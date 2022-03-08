import random

def run():
    numeroA = random.randint(1, 100)
    numero_elegido = int(input('--elige un numero entre 1 y 100--\n =-> '))
    
    vidas = 1

    while vidas < 5:
        if numero_elegido == numeroA:
            print ('HAz adivinado ')
            break
        else:
            vidas=vidas+1
            numero_elegido = int(input('Elige Otro numero =->'))


if __name__ == '__main__':
    run()