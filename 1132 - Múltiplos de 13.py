'''
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

'''

X, Y = int(input()), int(input())
lista = []
nums = [X,Y]
nums.sort()

for i in range(nums[0], nums[1]+1):
    if i % 13 != 0:
        lista.append(i)
    else:
        continue

print(f'{sum(lista)}')
