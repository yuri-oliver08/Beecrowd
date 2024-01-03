'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros X e Y. 
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
'''

num = int(input())
entradas = [input() for x in range(num)]

for v in range(len(entradas)):
    valores = entradas[v].split()
    valoresIn = [int(m) for m in valores]
    valoresIn.sort()
    impares = []

    for n in range((int(valoresIn[0]))+1,int(valoresIn[1])):
        if n % 2 != 0:
            impares.append(n)

    if len(impares) > 0:
        print(sum(impares))

    else:
        print('0')

        




