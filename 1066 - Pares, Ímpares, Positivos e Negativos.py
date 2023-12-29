'''
Leia 5 valores Inteiros. 
A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''

entradas = [int(input()) for x in range(5)]
pares = [x for x in entradas if x % 2 == 0]
impares = [x for x in entradas if x % 2 != 0]
positivos = [x for x in entradas if x > 0]
negativos = [x for x in entradas if x < 0]

print(f'{len(pares)} valor(es) par(es)\n{len(impares)} valor(es) impar(es)\n{len(positivos)} valor(es) positivo(s)\n{len(negativos)} valor(es) negativo(s)')