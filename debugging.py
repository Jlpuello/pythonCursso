def divisor(num):
    divisor=[]

    for i in range(1, num +1):
        if num % 1 == 0:
            divisor.append(i)
    return divisor
    


def run():
    try:
        num = int(input("Ingrese un Numero: "))
        print(divisor(num))
        print("Termino El Programa!")
    except ValueError:
        print("debes ingresar un numero") 

if __name__ == '__main__':
    run()