def convertidor(opcion,cantidad):
    if opcion == 1:
        total = cantidad * 3994
        return total
    if opcion ==2:
        total = cantidad * 178
        return total
    if opcion ==3:
        total = cantidad * 4637
        return total
    if opcion ==4:
        total = cantidad * 3678
        return total
    else:
        return "Eligio Una Opcion no valida"


def run():
    print("""
    Defina la moneda de cambio 

    1- peso colombina 
    2- peso Argentino
    3- peso Chileno 
    4- peso mexicano 
    \t
    """)
    opcion = int(input("Elija una Moneda = "))
    cantidad = int(input("Cantidad de Dinero = "))

    total = convertidor(opcion,cantidad)

    print ('Su Cantidad de dinero en su moneda es  ',total) 



if __name__ == '__main__':
    run()
