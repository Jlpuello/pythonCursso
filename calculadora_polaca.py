from os import system
from math import sqrt



def read():
    number =[]
    with open("./archivos/expresiones.txt", "r", encoding="utf-8") as f:
        for line in f:
            r=line.split()
            number.append(r)
        return(number)





def calcular(archivo):
    #l=[[2, 1 ,'+', 3, '*']]
    operadores=['+','-','*','/','^','inv','cuadrado','cubo','raiz','raiz3','clear','[',']']
    stack=[]
    for i in archivo:
        for x in i:

            if x not in operadores:
                stack.append(int(x))
            else:
                              
                if x == '+':
                    
                    aux1 = stack.pop()
                    aux2 = stack.pop()
                    stack.append(aux2 + aux1)
                elif x == '-':
                    aux1 = stack.pop()
                    aux2 = stack.pop()
                    stack.append(aux2 - aux1)
                elif x == '*':
                    aux1 = stack.pop()
                    aux2 = stack.pop()
                    stack.append(aux2 * aux1)
                elif x =='/':
                    staux1 = stack.pop()
                    aux2 = stack.pop()
                    stack.append(aux2 / aux1)
                elif x == '^':
                    aux1 = stack.pop()
                    aux2 = stack.pop()
                    stack.append(aux2 ** aux1)
                elif x =='inv':
                    aux1 = stack.pop()
                    stack.append(aux1*1/aux1)
                elif x == 'cuadrado':
                    aux1 = stack.pop()
                    stack.append(aux1 ** 2)
                elif x =='cubo':
                    aux1 = stack.pop()
                    stack.append(aux1 ** 3)
                elif x == 'raiz':
                    aux1 = stack.pop()
                    stack.append(sqrt(aux1))
                elif x =='raiz3':
                    aux1 = stack.pop()
                    stack.append(aux1**(1/3))
                elif x == 'clear':
                    system("clear")
        return 'resultado', stack.pop()

    
                

def run():
    

    lista=read()
    
    print(calcular(lista))
    


if __name__ == "__main__":
    run()