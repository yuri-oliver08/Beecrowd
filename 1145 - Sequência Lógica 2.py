'''
Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.
'''

X,Y = list(map(int,input().split()))
cont = 1
for i in range(1,(int((Y/X))+1)):
    r = ""
    for n in range(X):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])



    


