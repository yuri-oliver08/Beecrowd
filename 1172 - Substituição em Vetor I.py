'''
Faça um programa que leia um vetor X[10]. 
Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
'''
lista = []
for x in range(10):
    ent = int(input())
    lista.append(ent)

for i in range(len(lista)):
    if lista[i] <= 0:
        lista[i] = 1
    

for i in range(len(lista)):
    print(f'X[{i}] = {lista[i]}')