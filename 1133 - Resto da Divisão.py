'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

'''

X, Y = int(input()), int(input())
lista = []
nums = [X,Y]
nums.sort()

for i in range(nums[0]+1, nums[1]):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
    else:
        continue


