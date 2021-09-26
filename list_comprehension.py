def run():
    squares = []
    for i in range(1,101):
        squares.append(i**2)

    print ("")

    list = [i**3 for i in range(1,101) if i % 3 != 0]

    print("")

    lista = [i*4 for i in range(1,99999) if i % 6 == 0 and i % 9 == 0 ]

    print('\t', lista)


if __name__ == '__main__':
    run()