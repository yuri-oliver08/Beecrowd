'''
Faça um programa que leia 6 valores. 
Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). 
A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

nums = []
for i in range(6):
    entrada = float(input())
    if entrada > 0:
        nums.append(entrada)

cont = len(nums)

print(f'{cont} valores positivos')