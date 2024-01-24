'''
Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

'''

m = 1
num = int(input())

for n in range(num):
    print(f'{m} {m**2} {m**3}')
    m += 1