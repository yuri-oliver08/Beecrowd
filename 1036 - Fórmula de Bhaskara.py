'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja:
uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente. 
Imprima sempre o final de linha após cada mensagem.
'''

from math import *

def bhaskara():
    R1 = ((B*-1) + (sqrt(delta))) / (2*A)
    R2 = ((B*-1) - (sqrt(delta))) / (2*A)
    
    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')

entrada = input()
valores = entrada.split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

delta = B**2 - (4*A*C)


if A == 0.0 or delta < 0:
    print('Impossivel calcular')
else:
    bhaskara()
