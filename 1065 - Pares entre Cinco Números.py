'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''

entradas = [int(input()) for x in range(5)]
count = 0
for n in entradas:
    if n % 2 == 0:
        count += 1

print(f'{count} valores pares')