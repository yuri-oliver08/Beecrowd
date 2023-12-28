'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

maior = 0
entrada = input()

valores = entrada.split()

valoresF = [eval(i) for i in valores]

for valor in valoresF:  

    atual = valor
    
    if atual > maior: 
        maior = atual
    else:   
        continue

print('{} eh o maior'.format(maior))
