'''
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares.
Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos.
Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.
'''
pares = []
impares = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        if len(pares) == 5:
            for x in range(0,5):
                print(f'par[{x}] = {pares[x]}')
            pares.clear()
            pares.append(n)
        else:
            pares.append(n)
    else:
        if len(impares) == 5:
            for x in range(0,5):
                print(f'impar[{x}] = {impares[x]}')
            impares.clear()
            impares.append(n)
        else:
            impares.append(n)

for x in range(len(impares)):
    print(f'impar[{x}] = {impares[x]}')

for x in range(len(pares)):
    print(f'par[{x}] = {pares[x]}')